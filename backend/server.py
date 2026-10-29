from fastapi import FastAPI, APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import json
import random
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from datetime import datetime, timezone, date, timedelta

from emergentintegrations.llm.chat import LlmChat, UserMessage, TextDelta, StreamDone

import content

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

EMERGENT_LLM_KEY = os.environ.get('EMERGENT_LLM_KEY')

app = FastAPI(title="ArchEsame API")
app.get("/health")
   async def health():
       return {"status": "ok"}
api_router = APIRouter(prefix="/api")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# =============================================================================
# Helpers & Models
# =============================================================================
def today_str() -> str:
    return datetime.now(timezone.utc).date().isoformat()


class SubmitAnswer(BaseModel):
    device_id: str
    question_id: str
    selected_index: int


class CompleteTopic(BaseModel):
    device_id: str
    slug: str


class ChatIn(BaseModel):
    device_id: str
    session_id: str
    message: str


class GenerateQuizIn(BaseModel):
    category: str
    count: int = 4


CONTEXT_BLURB = (
    "Sei un tutor esperto per l'Esame di Stato da Architetto in Italia. "
    "Rispondi SEMPRE in italiano, in modo chiaro, accurato e strutturato. "
    "Basati sulla normativa italiana (L. 1150/1942, DM 1444/1968, DPR 380/2001, "
    "NTC 2018, OPCM 3274/2003, DM 3/8/2015 prevenzione incendi, D.Lgs. 192/2005, "
    "DPCM 5/12/1997 acustica, DM 236/1989 barriere, D.Lgs. 36/2023 appalti, "
    "D.Lgs. 81/2008 sicurezza) e sul riassunto Ceccarelli (prontuario tecnico). "
    "Cita i riferimenti normativi quando utile. Se un argomento è incerto o la norma "
    "è stata aggiornata, segnalalo. Usa elenchi puntati e grassetto per i concetti chiave. "
    "Sii conciso ma completo, con taglio didattico da preparazione all'esame."
)


# =============================================================================
# Seeding
# =============================================================================
async def seed_database():
    meta = await db.meta.find_one({"_id": "content"})
    current = meta.get("version") if meta else 0
    if current == content.CONTENT_VERSION:
        return

    # Categories — upsert by slug
    for c in content.CATEGORIES:
        await db.categories.update_one({"slug": c["slug"]}, {"$set": dict(c)}, upsert=True)

    # Topics — upsert by slug (refresh deepened content)
    for t in content.TOPICS:
        await db.topics.update_one({"slug": t["slug"]}, {"$set": dict(t)}, upsert=True)

    # Questions — upsert seed questions by stable qid (keeps AI-generated ones intact)
    for i, q in enumerate(content.ALL_QUESTIONS):
        d = dict(q)
        d["qid"] = f"seed-{i}"
        d.setdefault("ai_generated", False)
        # Deterministic shuffle so the correct answer isn't always the first option
        order = list(range(len(d["options"])))
        random.Random(d["qid"]).shuffle(order)
        d["options"] = [q["options"][j] for j in order]
        d["correct"] = order.index(q["correct"])
        await db.questions.update_one({"qid": d["qid"]}, {"$set": d}, upsert=True)
        # keep saved mistakes aligned with the reordered options
        async for m in db.mistakes.find({"question_id": d["qid"]}):
            old = m.get("options") or []
            sel = m.get("selected_index")
            new_sel = d["options"].index(old[sel]) if sel is not None and sel < len(old) and old[sel] in d["options"] else sel
            await db.mistakes.update_one({"_id": m["_id"]}, {"$set": {
                "question": d["question"], "options": d["options"], "correct": d["correct"],
                "explanation": d["explanation"], "selected_index": new_sel,
            }})

    # Flashcards — upsert by stable fid
    for i, f in enumerate(content.ALL_FLASHCARDS):
        d = dict(f)
        d["fid"] = f"fc-{i}"
        await db.flashcards.update_one({"fid": d["fid"]}, {"$set": d}, upsert=True)

    # Tracce — upsert by stable tid
    for i, t in enumerate(content.TRACCE):
        d = dict(t)
        d["tid"] = f"tr-{i}"
        await db.tracce.update_one({"tid": d["tid"]}, {"$set": d}, upsert=True)

    # Design questions — upsert by stable did
    for i, dqd in enumerate(content.DESIGN_QUESTIONS):
        d = dict(dqd)
        d["did"] = f"dq-{i}"
        await db.design_questions.update_one({"did": d["did"]}, {"$set": d}, upsert=True)

    # Laws — upsert by stable lid
    for i, law in enumerate(content.LAWS):
        d = dict(law)
        d["lid"] = f"law-{i}"
        await db.laws.update_one({"lid": d["lid"]}, {"$set": d}, upsert=True)

    await db.meta.update_one(
        {"_id": "content"}, {"$set": {"version": content.CONTENT_VERSION}}, upsert=True
    )
    logger.info(f"Seeded content v{content.CONTENT_VERSION}")


@app.on_event("startup")
async def on_startup():
    await seed_database()


# =============================================================================
# Content endpoints
# =============================================================================
@api_router.get("/")
async def root():
    return {"message": "ArchEsame API", "ok": True}


@api_router.get("/categories")
async def get_categories():
    cats = await db.categories.find({}, {"_id": 0}).to_list(100)
    for c in cats:
        c["topic_count"] = await db.topics.count_documents({"category": c["slug"]})
        c["question_count"] = await db.questions.count_documents({"category": c["slug"]})
        c["flashcard_count"] = await db.flashcards.count_documents({"category": c["slug"]})
    return cats


@api_router.get("/topics")
async def get_topics(category: Optional[str] = None):
    q = {"category": category} if category else {}
    topics = await db.topics.find(
        q, {"_id": 0, "content": 0}
    ).to_list(200)
    return topics


@api_router.get("/topics/search")
async def search_topics(q: str = Query("", min_length=0)):
    term = q.strip()
    if not term:
        return []
    rx = {"$regex": term, "$options": "i"}
    query = {"$or": [{"title": rx}, {"subtitle": rx}, {"content": rx}, {"key_points": rx}]}
    topics = await db.topics.find(query, {"_id": 0, "content": 0}).to_list(200)
    return topics


@api_router.get("/topics/{slug}")
async def get_topic(slug: str):
    topic = await db.topics.find_one({"slug": slug}, {"_id": 0})
    if not topic:
        raise HTTPException(status_code=404, detail="Argomento non trovato")
    return topic


@api_router.get("/flashcards")
async def get_flashcards(category: Optional[str] = None):
    q = {"category": category} if category else {}
    return await db.flashcards.find(q, {"_id": 0}).to_list(500)


@api_router.get("/tracce")
async def get_tracce():
    return await db.tracce.find({}, {"_id": 0}).to_list(100)


@api_router.get("/tracce/{tid}")
async def get_traccia(tid: str):
    t = await db.tracce.find_one({"tid": tid}, {"_id": 0})
    if not t:
        raise HTTPException(status_code=404, detail="Traccia non trovata")
    return t


@api_router.get("/design-questions")
async def get_design_questions(category: Optional[str] = None):
    q = {"category": category} if category else {}
    return await db.design_questions.find(q, {"_id": 0}).to_list(200)


@api_router.get("/laws")
async def get_laws():
    laws = await db.laws.find({}, {"_id": 0}).sort("anno", 1).to_list(500)
    return laws


# =============================================================================
# Quiz endpoints
# =============================================================================
@api_router.get("/quiz")
async def get_quiz(category: Optional[str] = None, limit: int = 10):
    pipeline = []
    if category:
        pipeline.append({"$match": {"category": category}})
    pipeline.append({"$sample": {"size": limit}})
    pipeline.append({"$project": {"_id": 0}})
    questions = await db.questions.aggregate(pipeline).to_list(limit)
    return questions


@api_router.get("/quiz/mistakes")
async def get_mistakes_quiz(device_id: str = Query(...)):
    docs = await db.mistakes.find({"device_id": device_id}, {"_id": 0}).to_list(500)
    out = []
    for m in docs:
        out.append({
            "qid": m["question_id"],
            "category": m.get("category"),
            "topic": None,
            "question": m["question"],
            "options": m["options"],
            "correct": m["correct"],
            "explanation": m["explanation"],
        })
    return out


@api_router.get("/quiz/simulation")
async def get_simulation(count: int = 20, category: Optional[str] = None):
    count = max(5, min(count, 40))
    match = {"category": category} if category else {}
    pipeline = []
    if match:
        pipeline.append({"$match": match})
    pipeline.append({"$sample": {"size": count}})
    pipeline.append({"$project": {"_id": 0}})
    return await db.questions.aggregate(pipeline).to_list(count)


@api_router.post("/quiz/submit")
async def submit_answer(payload: SubmitAnswer):
    q = await db.questions.find_one({"qid": payload.question_id}, {"_id": 0})
    if not q:
        raise HTTPException(status_code=404, detail="Domanda non trovata")
    is_correct = payload.selected_index == q["correct"]

    # record attempt
    await db.attempts.insert_one({
        "device_id": payload.device_id,
        "question_id": payload.question_id,
        "category": q["category"],
        "selected_index": payload.selected_index,
        "correct": is_correct,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    # mistakes review: keep latest wrong per question; remove if now correct
    if is_correct:
        await db.mistakes.delete_one({"device_id": payload.device_id, "question_id": payload.question_id})
    else:
        await db.mistakes.update_one(
            {"device_id": payload.device_id, "question_id": payload.question_id},
            {"$set": {
                "device_id": payload.device_id,
                "question_id": payload.question_id,
                "category": q["category"],
                "question": q["question"],
                "options": q["options"],
                "correct": q["correct"],
                "explanation": q["explanation"],
                "selected_index": payload.selected_index,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }},
            upsert=True,
        )

    await update_streak(payload.device_id)

    return {
        "correct": is_correct,
        "correct_index": q["correct"],
        "explanation": q["explanation"],
    }


@api_router.post("/quiz/generate")
async def generate_quiz(payload: GenerateQuizIn):
    if not EMERGENT_LLM_KEY:
        raise HTTPException(status_code=500, detail="Chiave AI non configurata")
    cat = await db.categories.find_one({"slug": payload.category}, {"_id": 0})
    cat_name = cat["name"] if cat else payload.category

    count = max(1, min(payload.count, 6))
    prompt = (
        f"Genera {count} domande a risposta multipla per l'Esame di Stato da Architetto "
        f"sull'argomento '{cat_name}'. Ogni domanda deve avere esattamente 4 opzioni, "
        f"una sola corretta, e una spiegazione didattica del perché la risposta è corretta "
        f"e perché le altre sono sbagliate. Rispondi SOLO con JSON valido nel formato: "
        f'{{"questions":[{{"question":"...","options":["..","..","..",".."],"correct":0,"explanation":".."}}]}}. '
        f"Nessun testo fuori dal JSON."
    )
    chat = LlmChat(
        api_key=EMERGENT_LLM_KEY,
        session_id=f"quizgen-{payload.category}",
        system_message="Sei un generatore di quiz per l'Esame di Stato da Architetto. Rispondi solo in JSON valido, in italiano.",
    ).with_model("anthropic", "claude-sonnet-4-6")

    full = ""
    async for ev in chat.stream_message(UserMessage(text=prompt)):
        if isinstance(ev, TextDelta):
            full += ev.content
        elif isinstance(ev, StreamDone):
            break

    text = full.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    try:
        data = json.loads(text)
        questions = data.get("questions", [])
    except Exception as e:
        logger.error(f"Quiz gen parse error: {e} - raw: {full[:300]}")
        raise HTTPException(status_code=502, detail="Generazione non riuscita, riprova")

    out = []
    base = int(datetime.now(timezone.utc).timestamp())
    for i, q in enumerate(questions):
        if not isinstance(q.get("options"), list) or len(q["options"]) < 2:
            continue
        qid = f"ai-{payload.category}-{base}-{i}"
        opts = list(q["options"])
        right = opts[int(q.get("correct", 0))] if 0 <= int(q.get("correct", 0)) < len(opts) else opts[0]
        random.shuffle(opts)
        doc = {
            "qid": qid,
            "category": payload.category,
            "topic": None,
            "question": q.get("question", ""),
            "options": opts,
            "correct": opts.index(right),
            "explanation": q.get("explanation", ""),
            "ai_generated": True,
        }
        await db.questions.insert_one(dict(doc))
        out.append(doc)
    if not out:
        raise HTTPException(status_code=502, detail="Nessuna domanda generata, riprova")
    return out


# =============================================================================
# Progress endpoints
# =============================================================================
async def get_or_create_progress(device_id: str) -> dict:
    p = await db.progress.find_one({"device_id": device_id})
    if not p:
        p = {
            "device_id": device_id,
            "completed_topics": [],
            "streak": 0,
            "best_streak": 0,
            "last_study_date": None,
        }
        await db.progress.insert_one(dict(p))
    return p


async def update_streak(device_id: str):
    p = await get_or_create_progress(device_id)
    t = today_str()
    last = p.get("last_study_date")
    streak = p.get("streak", 0)
    best = p.get("best_streak", 0)
    if last == t:
        return
    if last:
        yesterday = (datetime.now(timezone.utc).date() - timedelta(days=1)).isoformat()
        streak = streak + 1 if last == yesterday else 1
    else:
        streak = 1
    best = max(best, streak)
    await db.progress.update_one(
        {"device_id": device_id},
        {"$set": {"last_study_date": t, "streak": streak, "best_streak": best}},
    )


@api_router.post("/topics/complete")
async def complete_topic(payload: CompleteTopic):
    await get_or_create_progress(payload.device_id)
    await db.progress.update_one(
        {"device_id": payload.device_id},
        {"$addToSet": {"completed_topics": payload.slug}},
    )
    await update_streak(payload.device_id)
    return {"ok": True}


@api_router.get("/progress")
async def get_progress(device_id: str = Query(...)):
    p = await get_or_create_progress(device_id)
    total_topics = await db.topics.count_documents({})
    total_attempts = await db.attempts.count_documents({"device_id": device_id})
    correct_attempts = await db.attempts.count_documents({"device_id": device_id, "correct": True})
    open_mistakes = await db.mistakes.count_documents({"device_id": device_id})
    accuracy = round((correct_attempts / total_attempts) * 100) if total_attempts else 0

    # per-category accuracy (weak areas)
    cats = await db.categories.find({}, {"_id": 0, "slug": 1, "name": 1}).to_list(100)
    by_cat = []
    for c in cats:
        att = await db.attempts.count_documents({"device_id": device_id, "category": c["slug"]})
        cor = await db.attempts.count_documents({"device_id": device_id, "category": c["slug"], "correct": True})
        if att:
            by_cat.append({
                "slug": c["slug"], "name": c["name"],
                "attempts": att, "correct": cor,
                "accuracy": round((cor / att) * 100),
            })
    by_cat.sort(key=lambda x: x["accuracy"])

    return {
        "completed_topics": p.get("completed_topics", []),
        "completed_count": len(p.get("completed_topics", [])),
        "total_topics": total_topics,
        "streak": p.get("streak", 0),
        "best_streak": p.get("best_streak", 0),
        "last_study_date": p.get("last_study_date"),
        "total_attempts": total_attempts,
        "correct_attempts": correct_attempts,
        "accuracy": accuracy,
        "open_mistakes": open_mistakes,
        "by_category": by_cat,
    }


@api_router.get("/mistakes")
async def get_mistakes(device_id: str = Query(...)):
    m = await db.mistakes.find({"device_id": device_id}, {"_id": 0}).sort("updated_at", -1).to_list(200)
    return m


# =============================================================================
# AI Tutor (streaming)
# =============================================================================
@api_router.get("/tutor/history")
async def tutor_history(device_id: str = Query(...), session_id: str = Query(...)):
    msgs = await db.chat_messages.find(
        {"device_id": device_id, "session_id": session_id}, {"_id": 0}
    ).sort("created_at", 1).to_list(500)
    return msgs


@api_router.post("/tutor/chat")
async def tutor_chat(payload: ChatIn):
    if not EMERGENT_LLM_KEY:
        raise HTTPException(status_code=500, detail="Chiave AI non configurata")

    now = datetime.now(timezone.utc).isoformat()
    await db.chat_messages.insert_one({
        "device_id": payload.device_id,
        "session_id": payload.session_id,
        "role": "user",
        "content": payload.message,
        "created_at": now,
    })

    # Build short history for context
    history = await db.chat_messages.find(
        {"device_id": payload.device_id, "session_id": payload.session_id}, {"_id": 0}
    ).sort("created_at", 1).to_list(500)
    recent = history[-10:]
    convo = "\n".join([f"{m['role']}: {m['content']}" for m in recent])

    chat = LlmChat(
        api_key=EMERGENT_LLM_KEY,
        session_id=f"{payload.device_id}:{payload.session_id}",
        system_message=CONTEXT_BLURB,
    ).with_model("anthropic", "claude-sonnet-4-6")

    user_text = payload.message
    if len(recent) > 1:
        user_text = f"Contesto conversazione precedente:\n{convo}\n\nNuova domanda: {payload.message}"

    async def event_gen():
        collected = ""
        try:
            async for ev in chat.stream_message(UserMessage(text=user_text)):
                if isinstance(ev, TextDelta):
                    collected += ev.content
                    yield f"data: {json.dumps({'delta': ev.content})}\n\n"
                elif isinstance(ev, StreamDone):
                    break
        except Exception as e:
            logger.error(f"Tutor stream error: {e}")
            yield f"data: {json.dumps({'error': 'Errore nel generare la risposta'})}\n\n"
        finally:
            if collected:
                await db.chat_messages.insert_one({
                    "device_id": payload.device_id,
                    "session_id": payload.session_id,
                    "role": "assistant",
                    "content": collected,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                })
            yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(
        event_gen(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no", "Connection": "keep-alive"},
    )


app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
