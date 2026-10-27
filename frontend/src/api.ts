import { storage } from "@/src/utils/storage";

const BASE = `${process.env.EXPO_PUBLIC_BACKEND_URL}/api`;

// ---------------------------------------------------------------------------
// Device identity (anonymous, per-device progress)
// ---------------------------------------------------------------------------
const DEVICE_KEY = "arch_device_id";
let cachedId: string | null = null;

let pendingId: Promise<string> | null = null;

export function ensureDeviceId(): Promise<string> {
  if (cachedId) return Promise.resolve(cachedId);
  pendingId ||= (async () => {
    let id = await storage.getItem<string>(DEVICE_KEY, "");
    if (!id) {
      id = `dev_${Date.now()}_${Math.random().toString(36).slice(2, 10)}`;
      await storage.setItem(DEVICE_KEY, id);
    }
    cachedId = id;
    return id;
  })();
  return pendingId;
}

// ---------------------------------------------------------------------------
// Types
// ---------------------------------------------------------------------------
export type Category = {
  slug: string;
  name: string;
  icon: string;
  blurb: string;
  topic_count: number;
  question_count: number;
  flashcard_count: number;
};

export type TopicMeta = {
  slug: string;
  category: string;
  title: string;
  subtitle: string;
  read_minutes: number;
  key_points: string[];
};

export type Topic = TopicMeta & { content: string; related_laws?: string[] };

export type Question = {
  qid: string;
  category: string;
  topic: string | null;
  question: string;
  options: string[];
  correct: number;
  explanation: string;
  ai_generated?: boolean;
};

export type Flashcard = { fid: string; category: string; front: string; back: string };

export type Traccia = {
  tid: string;
  sezione: string;
  tipo: string;
  sessione: string;
  titolo: string;
  testo: string;
  suggerimenti: string;
};

export type Progress = {
  completed_topics: string[];
  completed_count: number;
  total_topics: number;
  streak: number;
  best_streak: number;
  last_study_date: string | null;
  total_attempts: number;
  correct_attempts: number;
  accuracy: number;
  open_mistakes: number;
  by_category: { slug: string; name: string; attempts: number; correct: number; accuracy: number }[];
};

export type Mistake = {
  question_id: string;
  category: string;
  question: string;
  options: string[];
  correct: number;
  explanation: string;
  selected_index: number;
};

export type ChatMessage = { role: "user" | "assistant"; content: string; created_at: string };

// ---------------------------------------------------------------------------
// Fetch helper
// ---------------------------------------------------------------------------
async function api<T>(path: string, opts?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...opts,
  });
  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(txt || `Errore ${res.status}`);
  }
  return res.json() as Promise<T>;
}

export const getCategories = () => api<Category[]>("/categories");
export const getTopics = (category?: string) =>
  api<TopicMeta[]>(`/topics${category ? `?category=${category}` : ""}`);
export const getTopic = (slug: string) => api<Topic>(`/topics/${slug}`);
export const getFlashcards = (category?: string) =>
  api<Flashcard[]>(`/flashcards${category ? `?category=${category}` : ""}`);
export const getTracce = () => api<Traccia[]>("/tracce");
export const getQuiz = (category: string, limit = 10) =>
  api<Question[]>(`/quiz?category=${category}&limit=${limit}`);

export const getSimulation = (count = 20, category?: string) =>
  api<Question[]>(`/quiz/simulation?count=${count}${category ? `&category=${category}` : ""}`);

export const searchTopics = (q: string) =>
  api<TopicMeta[]>(`/topics/search?q=${encodeURIComponent(q)}`);

export type DesignQuestion = { did: string; category: string; titolo: string; prompt: string; guida: string };
export const getDesignQuestions = (category?: string) =>
  api<DesignQuestion[]>(`/design-questions${category ? `?category=${category}` : ""}`);

export type Law = { lid: string; anno: number; numero: string; titolo: string; categoria: string; apporto: string; dettaglio?: string };
export const getLaws = () => api<Law[]>("/laws");

export async function getMistakesQuiz() {
  const device_id = await ensureDeviceId();
  return api<Question[]>(`/quiz/mistakes?device_id=${device_id}`);
}

export async function submitAnswer(questionId: string, selectedIndex: number) {
  const device_id = await ensureDeviceId();
  return api<{ correct: boolean; correct_index: number; explanation: string }>("/quiz/submit", {
    method: "POST",
    body: JSON.stringify({ device_id, question_id: questionId, selected_index: selectedIndex }),
  });
}

export const generateQuiz = (category: string, count = 4) =>
  api<Question[]>("/quiz/generate", {
    method: "POST",
    body: JSON.stringify({ category, count }),
  });

export async function completeTopic(slug: string) {
  const device_id = await ensureDeviceId();
  return api<{ ok: boolean }>("/topics/complete", {
    method: "POST",
    body: JSON.stringify({ device_id, slug }),
  });
}

export async function getProgress() {
  const device_id = await ensureDeviceId();
  return api<Progress>(`/progress?device_id=${device_id}`);
}

export async function getMistakes() {
  const device_id = await ensureDeviceId();
  return api<Mistake[]>(`/mistakes?device_id=${device_id}`);
}

export async function getTutorHistory(sessionId: string) {
  const device_id = await ensureDeviceId();
  return api<ChatMessage[]>(`/tutor/history?device_id=${device_id}&session_id=${sessionId}`);
}

// ---------------------------------------------------------------------------
// Tutor streaming (SSE via XHR — works on native + web)
// ---------------------------------------------------------------------------
export async function streamTutor(
  sessionId: string,
  message: string,
  handlers: { onDelta: (t: string) => void; onDone: () => void; onError: (e: string) => void },
): Promise<() => void> {
  const device_id = await ensureDeviceId();
  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${BASE}/tutor/chat`);
  xhr.setRequestHeader("Content-Type", "application/json");

  let processed = 0;
  let buffer = "";
  let finished = false;

  const flush = () => {
    const parts = buffer.split("\n\n");
    buffer = parts.pop() ?? "";
    for (const part of parts) {
      const line = part.trim();
      if (!line.startsWith("data:")) continue;
      try {
        const obj = JSON.parse(line.slice(5).trim());
        if (obj.delta) handlers.onDelta(obj.delta);
        if (obj.error) handlers.onError(obj.error);
        if (obj.done && !finished) {
          finished = true;
          handlers.onDone();
        }
      } catch {
        // ignore partials
      }
    }
  };

  xhr.onprogress = () => {
    buffer += xhr.responseText.substring(processed);
    processed = xhr.responseText.length;
    flush();
  };
  xhr.onload = () => {
    buffer += xhr.responseText.substring(processed);
    processed = xhr.responseText.length;
    flush();
    if (!finished) {
      finished = true;
      handlers.onDone();
    }
  };
  xhr.onerror = () => {
    if (!finished) {
      finished = true;
      handlers.onError("Errore di rete");
    }
  };

  xhr.send(JSON.stringify({ device_id, session_id: sessionId, message }));
  return () => xhr.abort();
}
