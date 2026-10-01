import { useQueryClient } from "@tanstack/react-query";
import * as Haptics from "expo-haptics";
import { useRouter } from "expo-router";
import { useCallback, useEffect, useRef, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getSimulation, Question, submitAnswer } from "@/src/api";
import { Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

type Phase = "setup" | "running" | "done";

const fmt = (s: number) => {
  const m = Math.floor(s / 60);
  const r = s % 60;
  return `${m}:${r.toString().padStart(2, "0")}`;
};

export default function SimulationScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const qc = useQueryClient();

  const [phase, setPhase] = useState<Phase>("setup");
  const [count, setCount] = useState(10);
  const [onlyUrban, setOnlyUrban] = useState(false);
  const [loading, setLoading] = useState(false);

  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [index, setIndex] = useState(0);
  const [timeLeft, setTimeLeft] = useState(0);
  const timerRef = useRef<any>(null);

  const finish = useCallback(() => {
    if (timerRef.current) clearInterval(timerRef.current);
    setPhase("done");
    // record answers server-side (progress, mistakes)
    questions.forEach((q, i) => {
      const sel = answers[i];
      if (sel !== undefined) submitAnswer(q.qid, sel).catch(() => {});
    });
    qc.invalidateQueries({ queryKey: ["progress"] });
    qc.invalidateQueries({ queryKey: ["mistakes"] });
  }, [questions, answers, qc]);

  useEffect(() => {
    if (phase !== "running") return;
    timerRef.current = setInterval(() => {
      setTimeLeft((t) => {
        if (t <= 1) {
          clearInterval(timerRef.current);
          finish();
          return 0;
        }
        return t - 1;
      });
    }, 1000);
    return () => clearInterval(timerRef.current);
  }, [phase, finish]);

  const start = async () => {
    setLoading(true);
    try {
      const qs = await getSimulation(count, onlyUrban ? "urbanistica" : undefined);
      setQuestions(qs);
      setAnswers({});
      setIndex(0);
      setTimeLeft(count * 60);
      setPhase("running");
    } finally {
      setLoading(false);
    }
  };

  const select = (i: number) => {
    setAnswers((a) => ({ ...a, [index]: i }));
    Haptics.selectionAsync().catch(() => {});
  };

  const next = () => {
    if (index + 1 >= questions.length) finish();
    else setIndex((x) => x + 1);
  };

  // ----- SETUP -----
  if (phase === "setup") {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Simulazione d'esame" />
        <ScrollView contentContainerStyle={styles.setup} showsVerticalScrollIndicator={false}>
          <View style={styles.heroCard}>
            <Icon name="clock" size={30} color={colors.brandPrimary} />
            <Text style={styles.heroTitle}>Mettiti alla prova</Text>
            <Text style={styles.heroSub}>
              Rispondi alle domande entro il tempo. Al termine vedrai punteggio e correzione degli errori.
            </Text>
          </View>

          <Text style={styles.label}>Numero di domande</Text>
          <View style={styles.optionRow}>
            {[10, 20, 30].map((n) => (
              <Pressable
                key={n}
                testID={`sim-count-${n}`}
                style={[styles.pill, count === n && styles.pillActive]}
                onPress={() => setCount(n)}
              >
                <Text style={[styles.pillText, count === n && styles.pillTextActive]}>{n}</Text>
              </Pressable>
            ))}
          </View>

          <Text style={styles.label}>Materia</Text>
          <View style={styles.optionRow}>
            <Pressable
              testID="sim-all"
              style={[styles.pillWide, !onlyUrban && styles.pillActive]}
              onPress={() => setOnlyUrban(false)}
            >
              <Text style={[styles.pillText, !onlyUrban && styles.pillTextActive]}>Tutte le materie</Text>
            </Pressable>
            <Pressable
              testID="sim-urban"
              style={[styles.pillWide, onlyUrban && styles.pillActive]}
              onPress={() => setOnlyUrban(true)}
            >
              <Text style={[styles.pillText, onlyUrban && styles.pillTextActive]}>Solo Urbanistica</Text>
            </Pressable>
          </View>

          <Text style={styles.timeNote}>Tempo previsto: {fmt(count * 60)} (1 minuto a domanda)</Text>

          <Pressable testID="sim-start" style={styles.startBtn} onPress={start} disabled={loading}>
            {loading ? (
              <Loading />
            ) : (
              <>
                <Icon name="play" size={20} color={colors.onBrandPrimary} />
                <Text style={styles.startText}>Inizia la simulazione</Text>
              </>
            )}
          </Pressable>
        </ScrollView>
      </View>
    );
  }

  // ----- DONE -----
  if (phase === "done") {
    const score = questions.reduce((acc, q, i) => acc + (answers[i] === q.correct ? 1 : 0), 0);
    const pct = questions.length ? Math.round((score / questions.length) * 100) : 0;
    const wrong = questions.filter((q, i) => answers[i] !== q.correct);
    return (
      <View style={styles.root}>
        <ScreenHeader title="Esito simulazione" />
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, paddingBottom: insets.bottom + spacing.xxl, gap: spacing.lg }}
          showsVerticalScrollIndicator={false}
        >
          <View style={styles.resultHero}>
            <Text style={styles.resultPct}>{pct}%</Text>
            <Text style={styles.resultLabel}>
              {score} corrette su {questions.length}
            </Text>
          </View>

          {wrong.length > 0 ? (
            <View style={{ gap: spacing.md }}>
              <Text style={styles.reviewTitle}>Correzione degli errori</Text>
              {wrong.map((q) => {
                const i = questions.indexOf(q);
                const sel = answers[i];
                return (
                  <View key={q.qid} style={styles.reviewCard} testID={`sim-review-${q.qid}`}>
                    <Text style={styles.reviewQ}>{q.question}</Text>
                    <View style={styles.answerRow}>
                      <Icon name="x-circle" size={15} color={colors.error} />
                      <Text style={styles.wrongText}>
                        {sel !== undefined ? `La tua: ${q.options[sel]}` : "Non risposta"}
                      </Text>
                    </View>
                    <View style={styles.answerRow}>
                      <Icon name="check-circle" size={15} color={colors.success} />
                      <Text style={styles.rightText}>Corretta: {q.options[q.correct]}</Text>
                    </View>
                    <Text style={styles.reviewExplain}>{q.explanation}</Text>
                  </View>
                );
              })}
            </View>
          ) : (
            <Text style={styles.perfect}>Perfetto! Nessun errore. 🎯</Text>
          )}

          <Pressable testID="sim-again" style={styles.startBtn} onPress={() => setPhase("setup")}>
            <Icon name="rotate-ccw" size={18} color={colors.onBrandPrimary} />
            <Text style={styles.startText}>Nuova simulazione</Text>
          </Pressable>
          <Pressable testID="sim-exit" style={styles.exitBtn} onPress={() => router.back()}>
            <Text style={styles.exitText}>Torna agli esercizi</Text>
          </Pressable>
        </ScrollView>
      </View>
    );
  }

  // ----- RUNNING -----
  const q = questions[index];
  const sel = answers[index];
  const lowTime = timeLeft <= 30;
  return (
    <View style={styles.root}>
      <View style={[styles.runHeader, { paddingTop: insets.top + spacing.sm }]}>
        <Text style={styles.runProgress}>
          {index + 1} / {questions.length}
        </Text>
        <View style={[styles.timer, lowTime && styles.timerLow]}>
          <Icon name="clock" size={15} color={lowTime ? colors.onError : colors.onSurfaceTertiary} />
          <Text style={[styles.timerText, lowTime && styles.timerTextLow]}>{fmt(timeLeft)}</Text>
        </View>
        <Pressable testID="sim-finish" onPress={finish} hitSlop={8}>
          <Text style={styles.finishEarly}>Termina</Text>
        </Pressable>
      </View>
      <View style={styles.progressTrack}>
        <View style={[styles.progressFill, { width: `${(index / questions.length) * 100}%` }]} />
      </View>

      <ScrollView
        contentContainerStyle={{ padding: spacing.lg, paddingBottom: insets.bottom + 110, gap: spacing.md }}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.question}>{q.question}</Text>
        {q.options.map((opt, i) => {
          const active = sel === i;
          return (
            <Pressable
              key={i}
              testID={`sim-option-${i}`}
              style={[styles.option, active && styles.optionActive]}
              onPress={() => select(i)}
            >
              <View style={[styles.radio, active && styles.radioActive]}>
                {active ? <Icon name="check" size={14} color={colors.onBrandPrimary} /> : null}
              </View>
              <Text style={[styles.optionText, active && styles.optionTextActive]}>{opt}</Text>
            </Pressable>
          );
        })}
      </ScrollView>

      <View style={[styles.ctaBar, { paddingBottom: Math.max(insets.bottom, spacing.md) }]}>
        <Pressable testID="sim-next" style={styles.cta} onPress={next}>
          <Text style={styles.ctaText}>
            {index + 1 >= questions.length ? "Concludi" : "Avanti"}
          </Text>
          <Icon name="arrow-right" size={18} color={colors.onBrandPrimary} />
        </Pressable>
      </View>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  setup: { padding: spacing.lg, gap: spacing.md, paddingBottom: spacing.xxl },
  heroCard: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.xl,
    alignItems: "center",
    gap: spacing.sm,
    borderWidth: 1,
    borderColor: colors.border,
    marginBottom: spacing.sm,
  },
  heroTitle: { fontFamily: fonts.display, fontSize: 26, color: colors.onSurface },
  heroSub: { fontFamily: fonts.regular, fontSize: 14, color: colors.muted, textAlign: "center", lineHeight: 21 },
  label: { fontFamily: fonts.medium, fontSize: 13, color: colors.onSurface, marginTop: spacing.sm },
  optionRow: { flexDirection: "row", gap: spacing.sm },
  pill: {
    flex: 1,
    paddingVertical: spacing.md,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: colors.borderStrong,
    alignItems: "center",
  },
  pillWide: {
    flex: 1,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.sm,
    borderRadius: radius.lg,
    borderWidth: 1,
    borderColor: colors.borderStrong,
    alignItems: "center",
  },
  pillActive: { backgroundColor: colors.brandPrimary, borderColor: colors.brandPrimary },
  pillText: { fontFamily: fonts.medium, fontSize: 14, color: colors.onSurfaceTertiary },
  pillTextActive: { color: colors.onBrandPrimary },
  timeNote: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted, marginTop: spacing.xs },
  startBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
    marginTop: spacing.lg,
    minHeight: 56,
  },
  startText: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  exitBtn: { paddingVertical: spacing.md, alignItems: "center" },
  exitText: { fontFamily: fonts.medium, fontSize: 14, color: colors.muted },
  // running
  runHeader: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.md,
    backgroundColor: colors.surface,
  },
  runProgress: { flex: 1, fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface },
  timer: {
    flexDirection: "row",
    alignItems: "center",
    gap: 4,
    backgroundColor: colors.surfaceTertiary,
    paddingHorizontal: spacing.md,
    paddingVertical: 6,
    borderRadius: radius.pill,
  },
  timerLow: { backgroundColor: colors.error },
  timerText: { fontFamily: fonts.bold, fontSize: 14, color: colors.onSurfaceTertiary },
  timerTextLow: { color: colors.onError },
  finishEarly: { fontFamily: fonts.medium, fontSize: 14, color: colors.brandPrimary },
  progressTrack: { height: 4, backgroundColor: colors.surfaceTertiary },
  progressFill: { height: 4, backgroundColor: colors.brandPrimary },
  question: { fontFamily: fonts.display, fontSize: 25, color: colors.onSurface, lineHeight: 31, marginBottom: spacing.sm },
  option: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    backgroundColor: colors.surfaceSecondary,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    padding: spacing.lg,
  },
  optionActive: { borderColor: colors.brandPrimary, backgroundColor: colors.brandTertiary },
  radio: {
    width: 24,
    height: 24,
    borderRadius: radius.pill,
    borderWidth: 2,
    borderColor: colors.borderStrong,
    alignItems: "center",
    justifyContent: "center",
  },
  radioActive: { backgroundColor: colors.brandPrimary, borderColor: colors.brandPrimary },
  optionText: { flex: 1, fontFamily: fonts.regular, fontSize: 15, color: colors.onSurface, lineHeight: 21 },
  optionTextActive: { fontFamily: fonts.medium, color: colors.onBrandTertiary },
  ctaBar: {
    position: "absolute",
    left: 0,
    right: 0,
    bottom: 0,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: colors.divider,
    backgroundColor: colors.surface,
  },
  cta: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
  },
  ctaText: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  // done
  resultHero: { alignItems: "center", paddingVertical: spacing.lg },
  resultPct: { fontFamily: fonts.display, fontSize: 72, color: colors.brandPrimary },
  resultLabel: { fontFamily: fonts.regular, fontSize: 16, color: colors.muted },
  reviewTitle: { fontFamily: fonts.display, fontSize: 24, color: colors.onSurface },
  reviewCard: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.sm,
    borderWidth: 1,
    borderColor: colors.border,
  },
  reviewQ: { fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface, lineHeight: 21 },
  answerRow: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  wrongText: { flex: 1, fontFamily: fonts.regular, fontSize: 13, color: colors.error },
  rightText: { flex: 1, fontFamily: fonts.regular, fontSize: 13, color: colors.success },
  reviewExplain: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 21, marginTop: spacing.xs },
  perfect: { fontFamily: fonts.medium, fontSize: 16, color: colors.success, textAlign: "center" },
}));
