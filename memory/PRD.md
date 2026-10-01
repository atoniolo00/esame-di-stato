# PRD — ArchEsame (Esame di Stato Architetto)

## Problema originale
App mobile (Expo) per studiare, ripetere e prepararsi all'Esame di Stato da Architetto in Italia.
Teoria basata sul riassunto "ceccarelli" (prontuario tecnico) e sulle tracce estratte IUAV 2024.

## Scelte utente
- Modalità: teoria + quiz a risposta multipla con punteggio + flashcard (tutte e tre).
- Tutor AI con **Claude (claude-sonnet-4-6)** per spiegazioni/approfondimenti.
- Quiz/flashcard misti: base a mano + generazione AI su richiesta; ancorati anche alle tracce IUAV.
- Tracciamento progressi: argomenti completati, precisione quiz, streak.
- Spiegazioni degli errori per imparare dagli sbagli.

## Architettura
- **Backend**: FastAPI + MongoDB (motor). Seed automatico di categorie/argomenti/quiz/flashcard/tracce.
  Progresso anonimo per `device_id`. AI via `emergentintegrations` (Claude) per tutor (SSE streaming)
  e generazione quiz.
- **Frontend**: Expo Router, React Query, react-native-keyboard-controller, expo-image,
  expo-linear-gradient, react-native-markdown-display, @react-native-vector-icons/feather.
  Tema "Editorial" (terracotta/paper) con font Cormorant Garamond + Satoshi; light + dark.
- **Tabs**: Home, Studia, Esercitati, Tutor (NativeTabs su iOS 26+, classic altrove).

## Personas
- Neolaureato/a in Architettura che prepara l'Esame di Stato (sez. A/B).

## Requisiti core (statici)
- Libreria teoria per macro-argomento con lettore e "segna come completato".
- Quiz con feedback immediato e spiegazione dell'errore + punteggio.
- Flashcard flip per ripasso veloce.
- Tutor AI conversazionale in italiano, ancorato alla normativa.
- Tracce d'esame reali (IUAV 2024) con suggerimenti.
- Statistiche: streak, precisione, aree deboli, ripasso errori.

## Implementato (2026-06-30)
- Backend completo con 15 argomenti di teoria, ~38 domande, ~34 flashcard, 6 tracce IUAV.
- Endpoint: categories, topics, quiz (get/submit/generate AI), flashcards, tracce,
  progress, mistakes, tutor chat (SSE) + history, topics/complete.
- Streak + precisione + aree deboli + mistakes review lato server.
- Frontend: Home, Studia (chip filtro + lettore markdown), Esercitati (Quiz/Flashcard/Tracce),
  Tutor AI streaming con markdown, dettaglio traccia, schermata Statistiche.
- Testato: 18/18 test backend passati; flussi frontend verificati end-to-end.
- Fix: plurali italiani, invio con Enter (web) nel tutor.

## Iterazione 2 (2026-10-01)
- Teoria approfondita e ampliata: ora 22 argomenti. Focus URBANISTICA con 8 argomenti
  (fondamenti, zone/standard, piani attuativi, opere di urbanizzazione/oneri, perequazione,
  vincoli/esproprio, rigenerazione, parametri e indici) e contenuti molto più dettagliati su tutte le materie.
- Quesiti ampliati (urbanistica ~28) + quesiti di progettazione a calcolo (MCQ).
- Nuova sezione "Progettazione": 6 quesiti aperti con svolgimento guidato (collection design_questions).
- Simulazione d'esame a tempo (/simulation): setup (10/20/30 domande, tutte le materie o solo urbanistica),
  timer countdown, esito con punteggio e correzione degli errori. Endpoint GET /api/quiz/simulation.
- Preferiti (segnalibro) sugli argomenti (storage locale) + schermata /favorites.
- Ricerca full-text sugli argomenti: endpoint GET /api/topics/search + schermata /search.
- Seeding versionato (CONTENT_VERSION) con upsert idempotente: aggiorna i contenuti senza perdere il progresso.
- Testato: 34/34 test backend passati; nuovi flussi frontend verificati end-to-end.

## Backlog prioritizzato
- P1: contenuti — più domande/flashcard per categoria; più argomenti di teoria.
- P1: ricerca full-text negli argomenti; segnalibri/preferiti.
- P2: simulazione "prova d'esame" a tempo; quiz misto multi-categoria.
- P2: esportazione appunti; modalità revisione errori come quiz dedicato.
- P2: dark mode toggle manuale (tema dark già pronto).

## Prossimi task
- Arricchire la banca dati dei quiz e flashcard.
- Aggiungere modalità "simulazione esame" cronometrata.
