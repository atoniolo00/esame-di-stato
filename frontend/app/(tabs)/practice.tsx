import { useQuery } from "@tanstack/react-query";
import { useRouter } from "expo-router";
import { useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getCategories, getTracce } from "@/src/api";
import { Icon, Loading } from "@/src/components/ui";
import { usesNativeTabs } from "@/src/navigation";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

type Mode = "quiz" | "flash" | "tracce";

export default function PracticeScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const bottomChrome = usesNativeTabs ? insets.bottom : 0;

  const [mode, setMode] = useState<Mode>("quiz");
  const catsQ = useQuery({ queryKey: ["categories"], queryFn: getCategories });
  const tracceQ = useQuery({ queryKey: ["tracce"], queryFn: getTracce });

  const segments: { key: Mode; label: string }[] = [
    { key: "quiz", label: "Quiz" },
    { key: "flash", label: "Flashcard" },
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
            : (catsQ.data ?? []).map((c) => {
                const count = mode === "quiz" ? c.question_count : c.flashcard_count;
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
}));
