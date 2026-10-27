"""Backend tests for ArchEsame API (Esame di Stato Architetto)"""
import os
import json
import time
import uuid
import pytest
import requests

BASE_URL = os.environ["EXPO_PUBLIC_BACKEND_URL"].rstrip("/")
API = f"{BASE_URL}/api"

DEVICE_ID = f"test-device-{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="module")
def s():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


# ---- Content -------------------------------------------------------------
class TestContent:
    def test_root(self, s):
        r = s.get(f"{API}/")
        assert r.status_code == 200
        assert r.json().get("ok") is True

    def test_categories(self, s):
        r = s.get(f"{API}/categories")
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)
        assert len(data) == 14, f"Expected 14 categories (12 + normativa + attualita), got {len(data)}"
        for c in data:
            assert {"slug", "name", "topic_count", "question_count", "flashcard_count"}.issubset(c.keys())
            assert "_id" not in c

    def test_topics_list(self, s):
        r = s.get(f"{API}/topics")
        assert r.status_code == 200
        topics = r.json()
        assert isinstance(topics, list) and len(topics) > 0
        # content should be excluded from list view
        assert "content" not in topics[0]

    def test_topics_by_category(self, s):
        r = s.get(f"{API}/topics", params={"category": "urbanistica"})
        assert r.status_code == 200
        assert all(t["category"] == "urbanistica" for t in r.json())

    def test_topic_detail(self, s):
        r = s.get(f"{API}/topics/urbanistica-fondamenti")
        assert r.status_code == 200
        t = r.json()
        assert t["slug"] == "urbanistica-fondamenti"
        assert "content" in t and len(t["content"]) > 100

    def test_topic_not_found(self, s):
        r = s.get(f"{API}/topics/does-not-exist")
        assert r.status_code == 404

    def test_flashcards(self, s):
        r = s.get(f"{API}/flashcards", params={"category": "urbanistica"})
        assert r.status_code == 200
        cards = r.json()
        assert len(cards) > 0
        assert all(c["category"] == "urbanistica" for c in cards)
        assert "front" in cards[0] and "back" in cards[0]

    def test_tracce(self, s):
        r = s.get(f"{API}/tracce")
        assert r.status_code == 200
        tracce = r.json()
        assert isinstance(tracce, list) and len(tracce) > 0
        first = tracce[0]
        assert "tid" in first
        # detail
        r2 = s.get(f"{API}/tracce/{first['tid']}")
        assert r2.status_code == 200
        assert r2.json()["tid"] == first["tid"]

    def test_traccia_not_found(self, s):
        r = s.get(f"{API}/tracce/nope")
        assert r.status_code == 404


# ---- Quiz ----------------------------------------------------------------
class TestQuiz:
    def test_get_quiz_random(self, s):
        r = s.get(f"{API}/quiz", params={"category": "urbanistica", "limit": 3})
        assert r.status_code == 200
        qs = r.json()
        assert 1 <= len(qs) <= 3
        for q in qs:
            assert q["category"] == "urbanistica"
            assert "options" in q and len(q["options"]) >= 2
            assert "qid" in q

    def test_submit_correct(self, s):
        r = s.get(f"{API}/quiz", params={"limit": 1})
        q = r.json()[0]
        payload = {"device_id": DEVICE_ID, "question_id": q["qid"], "selected_index": q["correct"]}
        r2 = s.post(f"{API}/quiz/submit", json=payload)
        assert r2.status_code == 200
        data = r2.json()
        assert data["correct"] is True
        assert data["correct_index"] == q["correct"]
        assert "explanation" in data

    def test_submit_wrong_creates_mistake(self, s):
        r = s.get(f"{API}/quiz", params={"limit": 1})
        q = r.json()[0]
        wrong_idx = (q["correct"] + 1) % len(q["options"])
        payload = {"device_id": DEVICE_ID, "question_id": q["qid"], "selected_index": wrong_idx}
        r2 = s.post(f"{API}/quiz/submit", json=payload)
        assert r2.status_code == 200
        assert r2.json()["correct"] is False
        # verify mistake persisted
        m = s.get(f"{API}/mistakes", params={"device_id": DEVICE_ID})
        assert m.status_code == 200
        ids = [x["question_id"] for x in m.json()]
        assert q["qid"] in ids

    def test_submit_not_found(self, s):
        r = s.post(f"{API}/quiz/submit", json={"device_id": DEVICE_ID, "question_id": "nope", "selected_index": 0})
        assert r.status_code == 404

    @pytest.mark.timeout(60)
    def test_generate_quiz_ai(self, s):
        r = s.post(f"{API}/quiz/generate", json={"category": "urbanistica", "count": 2}, timeout=90)
        assert r.status_code == 200, f"got {r.status_code}: {r.text[:200]}"
        out = r.json()
        assert isinstance(out, list) and len(out) >= 1
        assert out[0]["ai_generated"] is True
        assert len(out[0]["options"]) >= 2


# ---- Progress ------------------------------------------------------------
class TestProgress:
    def test_complete_topic(self, s):
        r = s.post(f"{API}/topics/complete", json={"device_id": DEVICE_ID, "slug": "urbanistica-fondamenti"})
        assert r.status_code == 200
        assert r.json().get("ok") is True

    def test_progress_shape(self, s):
        r = s.get(f"{API}/progress", params={"device_id": DEVICE_ID})
        assert r.status_code == 200
        p = r.json()
        for k in ["completed_topics", "streak", "best_streak", "total_attempts",
                  "accuracy", "open_mistakes", "by_category", "total_topics"]:
            assert k in p, f"missing key {k}"
        assert p["streak"] >= 1
        assert "urbanistica-fondamenti" in p["completed_topics"]
        assert p["total_attempts"] >= 2

    def test_mistakes_list(self, s):
        r = s.get(f"{API}/mistakes", params={"device_id": DEVICE_ID})
        assert r.status_code == 200
        for m in r.json():
            assert "explanation" in m and "options" in m


# ---- Tutor (SSE streaming) -----------------------------------------------
class TestTutor:
    @pytest.mark.timeout(90)
    def test_tutor_chat_stream(self, s):
        sid = f"sess-{uuid.uuid4().hex[:6]}"
        payload = {"device_id": DEVICE_ID, "session_id": sid,
                   "message": "In una riga: cos'è il DM 1444/68?"}
        r = requests.post(f"{API}/tutor/chat", json=payload, stream=True, timeout=90)
        assert r.status_code == 200
        deltas = 0
        done = False
        start = time.time()
        for line in r.iter_lines(decode_unicode=True):
            if not line:
                continue
            if line.startswith("data:"):
                data = json.loads(line[5:].strip())
                if "delta" in data:
                    deltas += 1
                if data.get("done"):
                    done = True
                    break
            if time.time() - start > 80:
                break
        assert deltas > 0, "No SSE deltas received"
        assert done, "No done event"

        # verify history persisted (needs a tiny wait for background write)
        time.sleep(1.5)
        h = s.get(f"{API}/tutor/history", params={"device_id": DEVICE_ID, "session_id": sid})
        assert h.status_code == 200
        msgs = h.json()
        roles = [m["role"] for m in msgs]
        assert "user" in roles and "assistant" in roles


# ---- Iteration 2: Urbanistica focus, Search, Design Qs, Simulation --------
class TestIteration2:
    def test_urbanistica_counts(self, s):
        r = s.get(f"{API}/categories")
        assert r.status_code == 200
        urb = next((c for c in r.json() if c["slug"] == "urbanistica"), None)
        assert urb is not None, "urbanistica category missing"
        # Expect ~8 topics and ~28 questions
        assert urb["topic_count"] >= 8, f"urbanistica topic_count={urb['topic_count']} (<8)"
        assert urb["question_count"] >= 25, f"urbanistica question_count={urb['question_count']} (<25)"

    def test_search_perequazione(self, s):
        r = s.get(f"{API}/topics/search", params={"q": "perequazione"})
        assert r.status_code == 200
        topics = r.json()
        assert isinstance(topics, list) and len(topics) >= 1
        # Should include perequazione-compensazione topic
        slugs = [t["slug"] for t in topics]
        assert "perequazione-compensazione" in slugs

    def test_search_empty_returns_empty(self, s):
        r = s.get(f"{API}/topics/search", params={"q": ""})
        assert r.status_code == 200
        assert r.json() == []

    def test_search_case_insensitive(self, s):
        r = s.get(f"{API}/topics/search", params={"q": "TOGNOLI"})
        assert r.status_code == 200
        assert len(r.json()) >= 1

    def test_design_questions_all(self, s):
        r = s.get(f"{API}/design-questions")
        assert r.status_code == 200
        dq = r.json()
        assert isinstance(dq, list) and len(dq) >= 6
        first = dq[0]
        # fields present
        for k in ("did", "category", "titolo", "prompt", "guida"):
            assert k in first, f"missing field {k} in design question"

    def test_design_questions_urbanistica(self, s):
        r = s.get(f"{API}/design-questions", params={"category": "urbanistica"})
        assert r.status_code == 200
        dq = r.json()
        assert len(dq) >= 6
        assert all(d["category"] == "urbanistica" for d in dq)

    def test_simulation_default(self, s):
        r = s.get(f"{API}/quiz/simulation", params={"count": 10})
        assert r.status_code == 200
        qs = r.json()
        assert isinstance(qs, list) and len(qs) == 10
        for q in qs:
            assert "qid" in q and "options" in q
            assert "correct" in q and isinstance(q["correct"], int)
            assert "explanation" in q

    def test_simulation_urbanistica_20(self, s):
        r = s.get(f"{API}/quiz/simulation", params={"count": 20, "category": "urbanistica"})
        assert r.status_code == 200
        qs = r.json()
        # may be <20 if fewer available, but should be close
        assert len(qs) >= 15, f"got only {len(qs)} urbanistica simulation questions"
        assert all(q["category"] == "urbanistica" for q in qs)

    def test_simulation_min_clamp(self, s):
        # count<5 should be clamped to 5
        r = s.get(f"{API}/quiz/simulation", params={"count": 1})
        assert r.status_code == 200
        assert len(r.json()) == 5

    def test_simulation_max_clamp(self, s):
        # count>40 should be clamped to 40
        r = s.get(f"{API}/quiz/simulation", params={"count": 100})
        assert r.status_code == 200
        assert len(r.json()) == 40

    @pytest.mark.parametrize("slug", [
        "piani-attuativi",
        "opere-urbanizzazione-oneri",
        "perequazione-compensazione",
        "vincoli-esproprio",
        "rigenerazione-consumo-suolo",
        "parametri-edilizi-urbanistici",
    ])
    def test_new_urbanistica_topics(self, s, slug):
        r = s.get(f"{API}/topics/{slug}")
        assert r.status_code == 200, f"topic {slug} not found"
        t = r.json()
        assert t["slug"] == slug
        assert t["category"] == "urbanistica"
        assert "content" in t and len(t["content"]) > 500, f"content too short for {slug}"
        assert "key_points" in t and len(t["key_points"]) >= 3



# ---- Iteration 3: Laws + expanded quiz pool + authentic IUAV content ----
class TestIteration3:
    def test_laws_list(self, s):
        r = s.get(f"{API}/laws")
        assert r.status_code == 200
        laws = r.json()
        assert isinstance(laws, list)
        assert len(laws) == 32, f"expected 32 laws, got {len(laws)}"
        # Required fields
        for law in laws:
            assert set(["lid", "anno", "numero", "titolo", "categoria", "apporto"]).issubset(law.keys())
            assert isinstance(law["anno"], int)
            assert isinstance(law["apporto"], str) and len(law["apporto"]) > 10
        # Sorted by anno ascending
        years = [law["anno"] for law in laws]
        assert years == sorted(years), "laws not sorted by anno asc"

    def test_laws_contains_key_norms(self, s):
        r = s.get(f"{API}/laws")
        laws = r.json()
        numeri = " | ".join(l["numero"] for l in laws)
        for needle in ["1150/1942", "1444/1968", "380/2001", "36/2023"]:
            assert needle in numeri, f"missing norm {needle} in /api/laws"

    def test_categories_total_expanded(self, s):
        r = s.get(f"{API}/categories")
        cats = r.json()
        total = sum(c["question_count"] for c in cats)
        assert total >= 100, f"expected >=100 total questions, got {total}"
        urb = next(c for c in cats if c["slug"] == "urbanistica")
        assert urb["question_count"] >= 35, f"urbanistica count low: {urb['question_count']}"

    def test_quiz_urbanistica_20(self, s):
        r = s.get(f"{API}/quiz?category=urbanistica&limit=20")
        assert r.status_code == 200
        qs = r.json()
        assert len(qs) == 20
        for q in qs:
            assert q["category"] == "urbanistica"
            assert len(q["options"]) == 4

    def test_simulation_40(self, s):
        r = s.get(f"{API}/quiz/simulation?count=40")
        assert r.status_code == 200
        qs = r.json()
        assert len(qs) == 40
        # unique ids
        assert len({q["qid"] for q in qs}) == 40

    def test_submit_still_works(self, s):
        r = s.get(f"{API}/quiz?category=urbanistica&limit=1")
        q = r.json()[0]
        payload = {"device_id": DEVICE_ID, "question_id": q["qid"], "selected_index": q["correct"]}
        sub = s.post(f"{API}/quiz/submit", data=json.dumps(payload))
        assert sub.status_code == 200
        data = sub.json()
        assert data["correct"] is True
        assert data["correct_index"] == q["correct"]
        # wrong answer -> mistake stored
        wrong_idx = (q["correct"] + 1) % 4
        payload2 = {"device_id": DEVICE_ID, "question_id": q["qid"], "selected_index": wrong_idx}
        sub2 = s.post(f"{API}/quiz/submit", data=json.dumps(payload2))
        assert sub2.status_code == 200
        assert sub2.json()["correct"] is False

    def test_tracce_count_and_iuav(self, s):
        r = s.get(f"{API}/tracce")
        assert r.status_code == 200
        ts = r.json()
        assert len(ts) == 8, f"expected 8 tracce, got {len(ts)}"
        titles = " | ".join(t["titolo"].lower() for t in ts)
        assert "scuola elementare" in titles and "5 aule" in titles
        assert ("padiglione espositivo" in titles) or ("sala conferenze" in titles)

    def test_design_questions_count_and_iuav(self, s):
        r = s.get(f"{API}/design-questions")
        assert r.status_code == 200
        dq = r.json()
        assert len(dq) == 8, f"expected 8 design questions, got {len(dq)}"
        for d in dq:
            assert set(["did", "categoria" if "categoria" in d else "category", "titolo", "prompt", "guida"]).intersection(d.keys())
            assert d["titolo"] and d["prompt"] and d["guida"]


# ---- Iteration 4: laws by topic, normativa/attualita quiz, mistakes review, related_laws ----
class TestIteration4:
    DEV = f"TEST_it4-{uuid.uuid4().hex[:8]}"

    def test_laws_grouped_with_details(self, s):
        r = s.get(f"{API}/laws")
        assert r.status_code == 200
        laws = r.json()
        assert len(laws) >= 30
        cats = {l["categoria"] for l in laws}
        assert len(cats) >= 5, f"laws should span many topics, got {cats}"
        for l in laws:
            assert "_id" not in l
            assert l["dettaglio"] and len(l["dettaglio"]) > 40, f"missing dettaglio for {l['numero']}"

    def test_new_categories_exist(self, s):
        cats = {c["slug"]: c for c in s.get(f"{API}/categories").json()}
        assert cats["normativa"]["question_count"] >= 10
        assert cats["attualita"]["question_count"] >= 10

    def test_quiz_normativa(self, s):
        qs = s.get(f"{API}/quiz", params={"category": "normativa", "limit": 10}).json()
        assert len(qs) == 10
        assert all(q["category"] == "normativa" for q in qs)
        assert all(0 <= q["correct"] < len(q["options"]) for q in qs)

    def test_quiz_attualita_has_olympics(self, s):
        qs = s.get(f"{API}/quiz", params={"category": "attualita", "limit": 50}).json()
        assert len(qs) >= 10
        assert all(q["category"] == "attualita" for q in qs)
        text = " ".join(q["question"] + " " + q["explanation"] for q in qs).lower()
        assert "olimpi" in text or "2026" in text

    def test_related_laws_resolve_to_laws(self, s):
        numeri = {l["numero"] for l in s.get(f"{API}/laws").json()}
        topics = s.get(f"{API}/topics").json()
        with_laws = [t for t in topics if t.get("related_laws")]
        assert len(with_laws) >= 15
        for t in with_laws:
            for n in t["related_laws"]:
                assert n in numeri, f"{t['slug']} -> {n} not in laws"
        d = s.get(f"{API}/topics/urbanistica-fondamenti").json()
        assert "L. 1150/1942" in d["related_laws"]

    def test_mistakes_record_and_clear(self, s):
        qs = s.get(f"{API}/quiz", params={"category": "normativa", "limit": 2}).json()
        for q in qs:
            wrong = (q["correct"] + 1) % len(q["options"])
            r = s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q["qid"], "selected_index": wrong})
            assert r.status_code == 200 and r.json()["correct"] is False
        # duplicate wrong answer must not duplicate the mistake
        q0 = qs[0]
        s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q0["qid"], "selected_index": (q0["correct"] + 1) % 4})
        m = s.get(f"{API}/mistakes", params={"device_id": self.DEV}).json()
        assert {x["question_id"] for x in m} == {q["qid"] for q in qs}
        mq = s.get(f"{API}/quiz/mistakes", params={"device_id": self.DEV}).json()
        assert len(mq) == 2
        for x in mq:
            assert {"qid", "question", "options", "correct", "explanation"}.issubset(x.keys())
            assert "_id" not in x
        p = s.get(f"{API}/progress", params={"device_id": self.DEV}).json()
        assert p["open_mistakes"] == 2
        # answer correctly -> removed
        r = s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q0["qid"], "selected_index": q0["correct"]})
        assert r.json()["correct"] is True
        mq2 = s.get(f"{API}/quiz/mistakes", params={"device_id": self.DEV}).json()
        assert [x["qid"] for x in mq2] == [qs[1]["qid"]]

    def test_mistakes_requires_device(self, s):
        assert s.get(f"{API}/quiz/mistakes").status_code == 422

    def test_mistakes_empty_for_new_device(self, s):
        r = s.get(f"{API}/quiz/mistakes", params={"device_id": f"TEST_empty-{uuid.uuid4().hex[:6]}"})
        assert r.status_code == 200 and r.json() == []

    def test_simulation_and_search_regression(self, s):
        sim = s.get(f"{API}/quiz/simulation", params={"count": 40}).json()
        assert len(sim) == 40 and len({q["qid"] for q in sim}) == 40
        res = s.get(f"{API}/topics/search", params={"q": "standard"}).json()
        assert len(res) >= 1 and all("content" not in t for t in res)
        assert len(s.get(f"{API}/flashcards").json()) >= 40
        assert len(s.get(f"{API}/tracce").json()) >= 8


# ---- Iteration 5: shuffled options, mistakes realignment ------------------
class TestIteration5:
    DEV = f"TEST_it5-{uuid.uuid4().hex[:6]}"

    def test_quiz_correct_index_balanced(self, s):
        qs = s.get(f"{API}/quiz", params={"limit": 200}).json()
        seed = [q for q in qs if q["qid"].startswith("seed-")]
        assert len(seed) >= 150
        dist = [sum(1 for q in seed if q["correct"] == i) for i in range(4)]
        assert max(dist) / len(seed) < 0.40, dist
        assert min(dist) / len(seed) > 0.12, dist

    def test_always_a_strategy_fails(self, s):
        qs = s.get(f"{API}/quiz", params={"limit": 200}).json()
        hits = sum(1 for q in qs if q["correct"] == 0)
        assert hits / len(qs) < 0.40

    def test_submit_validates_shuffled_index(self, s):
        qs = s.get(f"{API}/quiz", params={"category": "urbanistica", "limit": 20}).json()
        q = next(q for q in qs if q["correct"] != 0)
        r = s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q["qid"], "selected_index": q["correct"]}).json()
        assert r["correct"] is True and r["correct_index"] == q["correct"]
        r0 = s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q["qid"], "selected_index": 0}).json()
        assert r0["correct"] is False and r0["correct_index"] == q["correct"]

    def test_simulation_balanced_and_consistent(self, s):
        sims = []
        for _ in range(3):
            sims += s.get(f"{API}/quiz/simulation", params={"count": 40}).json()
        dist = [sum(1 for q in sims if q["correct"] == i) for i in range(4)]
        assert max(dist) / len(sims) < 0.45, dist
        q = sims[0]
        r = s.post(f"{API}/quiz/submit", json={"device_id": self.DEV, "question_id": q["qid"], "selected_index": q["correct"]}).json()
        assert r["correct"] is True

    def test_mistakes_quiz_matches_live_question_and_clears(self, s):
        dev = f"TEST_it5m-{uuid.uuid4().hex[:6]}"
        qs = s.get(f"{API}/quiz", params={"category": "edilizia", "limit": 3}).json()
        for q in qs:
            s.post(f"{API}/quiz/submit", json={"device_id": dev, "question_id": q["qid"], "selected_index": (q["correct"] + 1) % 4})
        mq = s.get(f"{API}/quiz/mistakes", params={"device_id": dev}).json()
        live = {q["qid"]: q for q in qs}
        assert len(mq) == 3
        for m in mq:
            assert m["options"] == live[m["qid"]]["options"] and m["correct"] == live[m["qid"]]["correct"]
            r = s.post(f"{API}/quiz/submit", json={"device_id": dev, "question_id": m["qid"], "selected_index": m["correct"]}).json()
            assert r["correct"] is True
        assert s.get(f"{API}/quiz/mistakes", params={"device_id": dev}).json() == []
        assert s.get(f"{API}/progress", params={"device_id": dev}).json()["open_mistakes"] == 0

    def test_existing_mistakes_aligned_with_questions(self):
        """DB integrity: pre-existing mistakes were realigned to shuffled options on reseed"""
        from pathlib import Path
        from pymongo import MongoClient
        env = dict(l.split("=", 1) for l in Path("/app/backend/.env").read_text().splitlines() if "=" in l)
        db = MongoClient(env["MONGO_URL"].strip('"'))[env["DB_NAME"].strip('"')]
        bad = []
        for m in db.mistakes.find({"question_id": {"$regex": "^seed-"}}):
            q = db.questions.find_one({"qid": m["question_id"]})
            if q["options"] != m["options"] or q["correct"] != m["correct"]:
                bad.append(m["question_id"])
        assert not bad, f"{len(bad)} misaligned mistakes: {bad[:10]}"


# ---- Iteration 6: legacy mistakes realigned, AI shuffle -------------------
class TestIteration6:
    LEGACY_DEV = "dev_1793049866387_fkmpywu6"  # pre-v6 browser device with 10 legacy mistakes

    def _live(self, s):
        qs = s.get(f"{API}/quiz", params={"limit": 500}).json()
        return {q["qid"]: q for q in qs}

    def test_legacy_mistakes_api_match_live_questions(self, s):
        live = self._live(s)
        devs = [self.LEGACY_DEV, "dev_1793050747108_yf98bs7p", "test-device-1dd0c1dc", "test1"]
        checked = 0
        for d in devs:
            for m in s.get(f"{API}/quiz/mistakes", params={"device_id": d}).json():
                q = live[m["qid"]]
                assert m["options"] == q["options"], m["qid"]
                assert m["correct"] == q["correct"], m["qid"]
                assert m["question"] == q["question"]
                checked += 1
        assert checked >= 10

    def test_legacy_mistake_submit_displayed_correct_is_correct(self, s):
        mq = s.get(f"{API}/quiz/mistakes", params={"device_id": "test-device-1dd0c1dc"}).json()
        if not mq:
            pytest.skip("legacy device has no mistakes")
        m = mq[0]
        r = s.post(f"{API}/quiz/submit", json={"device_id": "test-device-1dd0c1dc", "question_id": m["qid"], "selected_index": m["correct"]}).json()
        assert r["correct"] is True and r["correct_index"] == m["correct"]
        assert all(x["qid"] != m["qid"] for x in s.get(f"{API}/quiz/mistakes", params={"device_id": "test-device-1dd0c1dc"}).json())

    def test_mistakes_list_selected_differs_from_correct(self, s):
        for m in s.get(f"{API}/mistakes", params={"device_id": self.LEGACY_DEV}).json():
            assert m["selected_index"] != m["correct"]
            assert 0 <= m["selected_index"] < len(m["options"])

    def test_ai_generate_shuffled_and_consistent(self, s):
        r = s.post(f"{API}/quiz/generate", json={"category": "urbanistica", "count": 4}, timeout=120)
        assert r.status_code == 200, r.text
        qs = r.json()
        assert len(qs) >= 2
        live = self._live(s)
        for q in qs:
            assert q["ai_generated"] is True and len(q["options"]) == 4
            assert 0 <= q["correct"] < 4
            assert q["qid"] in live and live[q["qid"]]["correct"] == q["correct"] and live[q["qid"]]["options"] == q["options"]
            sub = s.post(f"{API}/quiz/submit", json={"device_id": "TEST_it6-ai", "question_id": q["qid"], "selected_index": q["correct"]}).json()
            assert sub["correct"] is True
        print("AI correct indices:", [q["correct"] for q in qs])
