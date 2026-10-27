import { useQuery } from "@tanstack/react-query";
import { useRouter } from "expo-router";
import { useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";

import { getMistakes, getProgress } from "@/src/api";
import { Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function ProgressScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const router = useRouter();

  const progressQ = useQuery({ queryKey: ["progress"], queryFn: getProgress });
  const mistakesQ = useQuery({ queryKey: ["mistakes"], queryFn: getMistakes });
  const [open, setOpen] = useState<string | null>(null);

  if (progressQ.isLoading) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Statistiche" />
        <Loading />
      </View>
    );
  }

  const p = progressQ.data!;
  const mistakes = mistakesQ.data ?? [];

  return (
    <View style={styles.root}>
      <ScreenHeader title="Statistiche" />
      <ScrollView contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
        {/* Big metrics */}
        <View style={styles.metricRow}>
          <View style={styles.metric}>
            <Text style={styles.metricNum}>{p.streak}</Text>
            <Text style={styles.metricLabel}>giorni di fila</Text>
          </View>
          <View style={styles.metric}>
            <Text style={styles.metricNum}>{p.accuracy}%</Text>
            <Text style={styles.metricLabel}>precisione</Text>
          </View>
          <View style={styles.metric}>
            <Text style={styles.metricNum}>{p.completed_count}</Text>
            <Text style={styles.metricLabel}>argomenti</Text>
          </View>
        </View>

        {/* Study progress */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Avanzamento teoria</Text>
          <Text style={styles.sectionSub}>
            {p.completed_count} / {p.total_topics} argomenti completati · record {p.best_streak} giorni
          </Text>
          <View style={styles.track}>
            <View
              style={[
                styles.fill,
                { width: `${p.total_topics ? Math.round((p.completed_count / p.total_topics) * 100) : 0}%` },
              ]}
            />
          </View>
          <Text style={styles.sectionSub}>
            {p.total_attempts} domande risposte, {p.correct_attempts} corrette
          </Text>
        </View>

        {/* Weak areas */}
        {p.by_category.length ? (
          <View style={styles.section}>
            <Text style={styles.sectionTitle}>Aree da rinforzare</Text>
            {p.by_category.slice(0, 6).map((c) => (
              <View key={c.slug} style={styles.weakRow} testID={`weak-${c.slug}`}>
                <View style={styles.weakHead}>
                  <Text style={styles.weakName}>{c.name}</Text>
                  <Text style={styles.weakPct}>{c.accuracy}%</Text>
                </View>
                <View style={styles.weakTrack}>
                  <View
                    style={[
                      styles.weakFill,
                      {
                        width: `${c.accuracy}%`,
                        backgroundColor: c.accuracy >= 70 ? colors.success : c.accuracy >= 40 ? colors.warning : colors.error,
                      },
                    ]}
                  />
                </View>
              </View>
            ))}
          </View>
        ) : null}

        {/* Mistakes review */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Ripassa gli errori</Text>
          {mistakes.length === 0 ? (
            <Text style={styles.sectionSub}>Nessun errore da ripassare. Ottimo lavoro!</Text>
          ) : (
            <>
              <Pressable
                testID="review-mistakes-cta"
                style={styles.reviewCta}
                onPress={() => router.push("/quiz/errori" as any)}
              >
                <Icon name="refresh-cw" size={18} color={colors.onBrandPrimary} />
                <Text style={styles.reviewCtaText}>Allenati sui tuoi {mistakes.length} errori</Text>
              </Pressable>
              {mistakes.map((m) => {
              const expanded = open === m.question_id;
              return (
                <Pressable
                  key={m.question_id}
                  testID={`mistake-${m.question_id}`}
                  style={styles.mistake}
                  onPress={() => setOpen(expanded ? null : m.question_id)}
                >
                  <View style={styles.mistakeHead}>
                    <Text style={styles.mistakeQ}>{m.question}</Text>
                    <Icon name={expanded ? "chevron-up" : "chevron-down"} size={18} color={colors.muted} />
                  </View>
                  {expanded ? (
                    <View style={styles.mistakeBody}>
                      <View style={styles.answerRow}>
                        <Icon name="x-circle" size={15} color={colors.error} />
                        <Text style={styles.wrongText}>La tua risposta: {m.options[m.selected_index]}</Text>
                      </View>
                      <View style={styles.answerRow}>
                        <Icon name="check-circle" size={15} color={colors.success} />
                        <Text style={styles.rightText}>Corretta: {m.options[m.correct]}</Text>
                      </View>
                      <Text style={styles.explain}>{m.explanation}</Text>
                    </View>
                  ) : null}
                </Pressable>
              );
            })}
            </>
          )}
        </View>
      </ScrollView>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  content: { padding: spacing.lg, gap: spacing.xl, paddingBottom: spacing.xxl },
  metricRow: { flexDirection: "row", gap: spacing.md },
  metric: {
    flex: 1,
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
    alignItems: "center",
    gap: spacing.xs,
    borderWidth: 1,
    borderColor: colors.border,
  },
  metricNum: { fontFamily: fonts.display, fontSize: 32, color: colors.brandPrimary },
  metricLabel: { fontFamily: fonts.regular, fontSize: 11, color: colors.muted, textAlign: "center" },
  section: { gap: spacing.sm },
  sectionTitle: { fontFamily: fonts.display, fontSize: 24, color: colors.onSurface },
  sectionSub: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted },
  track: { height: 10, backgroundColor: colors.surfaceTertiary, borderRadius: radius.pill, overflow: "hidden", marginVertical: spacing.xs },
  fill: { height: 10, backgroundColor: colors.brandPrimary, borderRadius: radius.pill },
  weakRow: { gap: spacing.xs, marginTop: spacing.sm },
  weakHead: { flexDirection: "row", justifyContent: "space-between" },
  weakName: { fontFamily: fonts.medium, fontSize: 14, color: colors.onSurface },
  weakPct: { fontFamily: fonts.medium, fontSize: 14, color: colors.onSurfaceTertiary },
  weakTrack: { height: 8, backgroundColor: colors.surfaceTertiary, borderRadius: radius.pill, overflow: "hidden" },
  weakFill: { height: 8, borderRadius: radius.pill },
  reviewCta: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    minHeight: 52,
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    paddingHorizontal: spacing.lg,
    marginVertical: spacing.sm,
  },
  reviewCtaText: { fontFamily: fonts.bold, fontSize: 15, color: colors.onBrandPrimary },
  mistake: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
    marginTop: spacing.sm,
  },
  mistakeHead: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  mistakeQ: { flex: 1, fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface, lineHeight: 21 },
  mistakeBody: { marginTop: spacing.md, gap: spacing.sm },
  answerRow: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  wrongText: { flex: 1, fontFamily: fonts.regular, fontSize: 13, color: colors.error },
  rightText: { flex: 1, fontFamily: fonts.regular, fontSize: 13, color: colors.success },
  explain: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 21, marginTop: spacing.xs },
}));
