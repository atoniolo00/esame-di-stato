import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import * as Haptics from "expo-haptics";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useEffect, useState } from "react";
import { ActivityIndicator, Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { generateQuiz, getQuiz, Question, submitAnswer } from "@/src/api";
import { ErrorState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

type Result = { correct: boolean; correct_index: number; explanation: string };

export default function QuizScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const qc = useQueryClient();
  const { category } = useLocalSearchParams<{ category: string }>();

  const quizQ = useQuery({
    queryKey: ["quiz", category],
    queryFn: () => getQuiz(category!, 10),
    enabled: !!category,
  });

  const [questions, setQuestions] = useState<Question[]>([]);
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<number | null>(null);
  const [result, setResult] = useState<Result | null>(null);
  const [score, setScore] = useState(0);
  const [finished, setFinished] = useState(false);

  useEffect(() => {
    if (quizQ.data) resetWith(quizQ.data);
  }, [quizQ.data]);

  const resetWith = (qs: Question[]) => {
    setQuestions(qs);
    setIndex(0);
    setSelected(null);
    setResult(null);
    setScore(0);
    setFinished(false);
  };

  const submitMut = useMutation({
    mutationFn: ({ qid, i }: { qid: string; i: number }) => submitAnswer(qid, i),
    onSuccess: (res, vars) => {
      setResult(res);
      setSelected(vars.i);
      if (res.correct) {
        setScore((s) => s + 1);
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {});
      } else {
        Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error).catch(() => {});
      }
      qc.invalidateQueries({ queryKey: ["progress"] });
      qc.invalidateQueries({ queryKey: ["mistakes"] });
    },
  });

  const aiMut = useMutation({
    mutationFn: () => generateQuiz(category!, 4),
    onSuccess: (qs) => resetWith(qs),
  });

  const onSelect = (i: number) => {
    if (result || submitMut.isPending) return;
    submitMut.mutate({ qid: questions[index].qid, i });
  };

  const next = () => {
    if (index + 1 >= questions.length) {
      setFinished(true);
    } else {
      setIndex((x) => x + 1);
      setSelected(null);
      setResult(null);
    }
  };

  if (quizQ.isLoading) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Quiz" />
        <Loading />
      </View>
    );
  }
  if (quizQ.isError || !questions.length) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Quiz" />
        {aiMut.isPending ? <Loading label="Genero domande con l'AI…" /> : <ErrorState onRetry={() => quizQ.refetch()} />}
      </View>
    );
  }

  if (finished) {
    const pct = Math.round((score / questions.length) * 100);
    return (
      <View style={styles.root}>
        <ScreenHeader title="Risultato" />
        <View style={styles.resultWrap}>
          <Text style={styles.resultPct}>{pct}%</Text>
          <Text style={styles.resultLabel}>
            {score} risposte corrette su {questions.length}
          </Text>
          <Pressable testID="quiz-retry" style={styles.primaryBtn} onPress={() => resetWith(quizQ.data ?? [])}>
            <Icon name="rotate-ccw" size={18} color={colors.onBrandPrimary} />
            <Text style={styles.primaryBtnText}>Rifai il quiz</Text>
          </Pressable>
          <Pressable
            testID="quiz-ai-more"
            style={styles.secondaryBtn}
            onPress={() => aiMut.mutate()}
            disabled={aiMut.isPending}
          >
            {aiMut.isPending ? (
              <ActivityIndicator color={colors.brandPrimary} />
            ) : (
              <>
                <Icon name="cpu" size={18} color={colors.onSurface} />
                <Text style={styles.secondaryBtnText}>{"Genera nuove domande con l'AI"}</Text>
              </>
            )}
          </Pressable>
          <Pressable testID="quiz-back" style={styles.textBtn} onPress={() => router.back()}>
            <Text style={styles.textBtnText}>Torna agli esercizi</Text>
          </Pressable>
        </View>
      </View>
    );
  }

  const q = questions[index];

  return (
    <View style={styles.root}>
      <ScreenHeader
        title="Quiz"
        subtitle={`Domanda ${index + 1} di ${questions.length}`}
        right={
          <Pressable testID="quiz-ai-btn" onPress={() => aiMut.mutate()} disabled={aiMut.isPending} hitSlop={10}>
            <Icon name="cpu" size={20} color={colors.brandPrimary} />
          </Pressable>
        }
      />
      <View style={styles.progressTrack}>
        <View style={[styles.progressFill, { width: `${((index) / questions.length) * 100}%` }]} />
      </View>
      <ScrollView
        contentContainerStyle={{ padding: spacing.lg, paddingBottom: insets.bottom + 120, gap: spacing.md }}
        showsVerticalScrollIndicator={false}
      >
        {q.ai_generated ? (
          <View style={styles.aiTag}>
            <Icon name="cpu" size={12} color={colors.brandPrimary} />
            <Text style={styles.aiTagText}>{"Generata dall'AI"}</Text>
          </View>
        ) : null}
        <Text style={styles.question}>{q.question}</Text>

        {q.options.map((opt, i) => {
          const isSel = selected === i;
          const showCorrect = !!result && i === result.correct_index;
          const showWrong = !!result && isSel && !result.correct;
          return (
            <Pressable
              key={i}
              testID={`quiz-option-${i}`}
              style={[
                styles.option,
                showCorrect && styles.optionCorrect,
                showWrong && styles.optionWrong,
              ]}
              onPress={() => onSelect(i)}
              disabled={!!result}
            >
              <Text
                style={[
                  styles.optionText,
                  (showCorrect || showWrong) && styles.optionTextStrong,
                ]}
              >
                {opt}
              </Text>
              {showCorrect ? <Icon name="check-circle" size={20} color={colors.success} /> : null}
              {showWrong ? <Icon name="x-circle" size={20} color={colors.error} /> : null}
            </Pressable>
          );
        })}

        {result ? (
          <View style={[styles.explainBox, result.correct ? styles.explainOk : styles.explainNo]}>
            <Text style={styles.explainTitle}>
              {result.correct ? "Corretto!" : "Impara dall'errore"}
            </Text>
            <Text style={styles.explainText}>{result.explanation}</Text>
          </View>
        ) : null}
      </ScrollView>

      {result ? (
        <View style={[styles.ctaBar, { paddingBottom: Math.max(insets.bottom, spacing.md) }]}>
          <Pressable testID="quiz-next" style={styles.cta} onPress={next}>
            <Text style={styles.ctaText}>
              {index + 1 >= questions.length ? "Vedi risultato" : "Prossima domanda"}
            </Text>
            <Icon name="arrow-right" size={18} color={colors.onBrandPrimary} />
          </Pressable>
        </View>
      ) : null}
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  progressTrack: { height: 4, backgroundColor: colors.surfaceTertiary },
  progressFill: { height: 4, backgroundColor: colors.brandPrimary },
  aiTag: {
    flexDirection: "row",
    alignItems: "center",
    gap: 4,
    alignSelf: "flex-start",
    backgroundColor: colors.brandTertiary,
    paddingHorizontal: spacing.sm,
    paddingVertical: 4,
    borderRadius: radius.pill,
  },
  aiTagText: { fontFamily: fonts.medium, fontSize: 11, color: colors.onBrandTertiary },
  question: { fontFamily: fonts.display, fontSize: 26, color: colors.onSurface, lineHeight: 32, marginBottom: spacing.sm },
  option: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.sm,
    backgroundColor: colors.surfaceSecondary,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    padding: spacing.lg,
  },
  optionCorrect: { borderColor: colors.success, backgroundColor: "#E7F0EA" },
  optionWrong: { borderColor: colors.error, backgroundColor: "#F6E7E7" },
  optionText: { flex: 1, fontFamily: fonts.regular, fontSize: 15, color: colors.onSurface, lineHeight: 21 },
  optionTextStrong: { fontFamily: fonts.medium },
  explainBox: { borderRadius: radius.lg, padding: spacing.lg, gap: spacing.xs, borderWidth: 1 },
  explainOk: { backgroundColor: "#E7F0EA", borderColor: colors.success },
  explainNo: { backgroundColor: "#F6E7E7", borderColor: colors.error },
  explainTitle: { fontFamily: fonts.bold, fontSize: 15, color: colors.onSurface },
  explainText: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 21 },
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
  resultWrap: { flex: 1, alignItems: "center", justifyContent: "center", padding: spacing.xl, gap: spacing.md },
  resultPct: { fontFamily: fonts.display, fontSize: 72, color: colors.brandPrimary },
  resultLabel: { fontFamily: fonts.regular, fontSize: 16, color: colors.muted, marginBottom: spacing.lg },
  primaryBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    alignSelf: "stretch",
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
  },
  primaryBtnText: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  secondaryBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    alignSelf: "stretch",
    backgroundColor: colors.surfaceSecondary,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
  },
  secondaryBtnText: { fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface },
  textBtn: { paddingVertical: spacing.md },
  textBtnText: { fontFamily: fonts.medium, fontSize: 14, color: colors.muted },
}));
