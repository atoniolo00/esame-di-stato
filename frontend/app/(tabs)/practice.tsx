import { useQuery } from "@tanstack/react-query";
import { useRouter } from "expo-router";
import { useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getCategories, getDesignQuestions, getTracce } from "@/src/api";
import { Icon, Loading } from "@/src/components/ui";
import { usesNativeTabs } from "@/src/navigation";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

type Mode = "quiz" | "flash" | "tracce" | "design";

export default function PracticeScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const bottomChrome = usesNativeTabs ? insets.bottom : 0;

  const [mode, setMode] = useState<Mode>("quiz");
  const [openDesign, setOpenDesign] = useState<string | null>(null);
  const catsQ = useQuery({ queryKey: ["categories"], queryFn: getCategories });
  const tracceQ = useQuery({ queryKey: ["tracce"], queryFn: getTracce });
  const designQ = useQuery({ queryKey: ["design-questions"], queryFn: () => getDesignQuestions() });

  const segments: { key: Mode; label: string }[] = [
    { key: "quiz", label: "Quiz" },
    { key: "flash", label: "Flashcard" },
    { key: "design", label: "Progett." },
    { key: "tracce", label: "Tracce" },
  ];

  return (
    <View style={styles.root}>
      <View style={[styles.header, { paddingTop: insets.top + spacing.sm }]}>
        <Text style={styles.title}>Esercitati</Text>
        <View style={styles.segment}>
          {segments.map((s) => {
            const active = s.key === mode;
            return (
              <Pressable
                key={s.key}
                testID={`practice-seg-${s.key}`}
                onPress={() => setMode(s.key)}
                style={[styles.segBtn, active && styles.segBtnActive]}
              >
                <Text style={[styles.segText, active && styles.segTextActive]}>{s.label}</Text>
              </Pressable>
            );
          })}
        </View>
      </View>

      {catsQ.isLoading || tracceQ.isLoading ? (
        <Loading />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, paddingBottom: bottomChrome + spacing.xxl, gap: spacing.md }}
          showsVerticalScrollIndicator={false}
        >
          {/* Simulazione d'esame banner */}
          <Pressable
            testID="practice-simulation-banner"
            style={styles.simBanner}
            onPress={() => router.push("/simulation" as any)}
          >
            <View style={styles.simIcon}>
              <Icon name="clock" size={22} color={colors.onBrandPrimary} />
            </View>
            <View style={styles.rowTextWrap}>
              <Text style={styles.simTitle}>Simulazione d&apos;esame</Text>
              <Text style={styles.simSub}>Prova a tempo con domande miste</Text>
            </View>
            <Icon name="arrow-right" size={20} color={colors.onBrandPrimary} />
          </Pressable>

          {mode === "tracce"
            ? (tracceQ.data ?? []).map((t) => (
                <Pressable
                  key={t.tid}
                  testID={`traccia-row-${t.tid}`}
                  style={styles.row}
                  onPress={() => router.push(`/traccia/${t.tid}` as any)}
                >
                  <View style={styles.rowIcon}>
                    <Icon name="file-text" size={20} color={colors.brandPrimary} />
                  </View>
                  <View style={styles.rowTextWrap}>
                    <Text style={styles.rowTitle}>{t.titolo}</Text>
                    <Text style={styles.rowSub} numberOfLines={1}>
                      {t.sezione} · {t.tipo}
                    </Text>
                  </View>
                  <Icon name="chevron-right" size={20} color={colors.muted} />
                </Pressable>
              ))
            : mode === "design"
              ? (designQ.data ?? []).map((d) => {
                  const expanded = openDesign === d.did;
                  return (
                    <Pressable
                      key={d.did}
                      testID={`design-${d.did}`}
                      style={styles.designCard}
                      onPress={() => setOpenDesign(expanded ? null : d.did)}
                    >
                      <View style={styles.designHead}>
                        <Text style={styles.designTitle}>{d.titolo}</Text>
                        <Icon name={expanded ? "chevron-up" : "chevron-down"} size={18} color={colors.muted} />
                      </View>
                      <Text style={styles.designPrompt}>{d.prompt}</Text>
                      {expanded ? (
                        <View style={styles.designGuida}>
                          <Text style={styles.designGuidaLabel}>SVOLGIMENTO GUIDATO</Text>
                          <Text style={styles.designGuidaText}>{d.guida}</Text>
                        </View>
                      ) : (
                        <Text style={styles.designHint}>Tocca per lo svolgimento guidato</Text>
                      )}
                    </Pressable>
                  );
                })
              : (catsQ.data ?? []).map((c) => {
                  const count = mode === "quiz" ? c.question_count : c.flashcard_count;
                  if (!count) return null;
                  return (
                    <Pressable
                      key={c.slug}
                      testID={`practice-cat-${c.slug}`}
                      style={styles.row}
                      onPress={() =>
                        router.push(
                          (mode === "quiz" ? `/quiz/${c.slug}` : `/flashcards/${c.slug}`) as any,
                        )
                      }
                    >
                      <View style={styles.rowIcon}>
                        <Icon name={c.icon} size={20} color={colors.brandPrimary} />
                      </View>
                      <View style={styles.rowTextWrap}>
                        <Text style={styles.rowTitle}>{c.name}</Text>
                        <Text style={styles.rowSub}>
                          {count}{" "}
                          {mode === "quiz"
                            ? count === 1
                              ? "domanda"
                              : "domande"
                            : count === 1
                              ? "carta"
                              : "carte"}
                        </Text>
                      </View>
                      <Icon name="play-circle" size={22} color={colors.brandPrimary} />
                    </Pressable>
                  );
                })}
        </ScrollView>
      )}
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  header: {
    backgroundColor: colors.surface,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.md,
    gap: spacing.md,
  },
  title: { fontFamily: fonts.display, fontSize: 32, color: colors.onSurface },
  segment: {
    flexDirection: "row",
    backgroundColor: colors.surfaceTertiary,
    borderRadius: radius.lg,
    padding: 4,
    gap: 4,
  },
  segBtn: { flex: 1, paddingVertical: spacing.sm, borderRadius: radius.md, alignItems: "center" },
  segBtnActive: { backgroundColor: colors.surface },
  segText: { fontFamily: fonts.medium, fontSize: 14, color: colors.muted },
  segTextActive: { color: colors.onSurface },
  row: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  rowIcon: {
    width: 42,
    height: 42,
    borderRadius: radius.md,
    backgroundColor: colors.brandTertiary,
    alignItems: "center",
    justifyContent: "center",
  },
  rowTextWrap: { flex: 1, gap: 2 },
  rowTitle: { fontFamily: fonts.medium, fontSize: 16, color: colors.onSurface },
  rowSub: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted },
  segText2: { fontSize: 13 },
  simBanner: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    padding: spacing.lg,
  },
  simIcon: {
    width: 42,
    height: 42,
    borderRadius: radius.md,
    backgroundColor: colors.brandSecondary,
    alignItems: "center",
    justifyContent: "center",
  },
  simTitle: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  simSub: { fontFamily: fonts.regular, fontSize: 13, color: colors.onBrandPrimary, opacity: 0.9 },
  designCard: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
    gap: spacing.sm,
  },
  designHead: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  designTitle: { flex: 1, fontFamily: fonts.bold, fontSize: 16, color: colors.onSurface },
  designPrompt: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 21 },
  designHint: { fontFamily: fonts.medium, fontSize: 12, color: colors.brandPrimary },
  designGuida: {
    backgroundColor: colors.brandTertiary,
    borderRadius: radius.md,
    padding: spacing.md,
    gap: spacing.xs,
  },
  designGuidaLabel: { fontFamily: fonts.medium, fontSize: 11, letterSpacing: 1, color: colors.onBrandTertiary },
  designGuidaText: { fontFamily: fonts.regular, fontSize: 14, color: colors.onBrandTertiary, lineHeight: 21 },
}));
