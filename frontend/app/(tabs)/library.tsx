import { useQuery } from "@tanstack/react-query";
import { useLocalSearchParams, useRouter } from "expo-router";
import { useEffect, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getCategories, getProgress, getTopics } from "@/src/api";
import { Icon, Loading } from "@/src/components/ui";
import { usesNativeTabs } from "@/src/navigation";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function LibraryScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const params = useLocalSearchParams<{ category?: string }>();
  const bottomChrome = usesNativeTabs ? insets.bottom : 0;

  const catsQ = useQuery({ queryKey: ["categories"], queryFn: getCategories });
  const progressQ = useQuery({ queryKey: ["progress"], queryFn: getProgress });

  const [selected, setSelected] = useState<string | undefined>(undefined);

  useEffect(() => {
    if (params.category) setSelected(params.category);
    else if (!selected && catsQ.data?.length) setSelected(catsQ.data[0].slug);
  }, [params.category, catsQ.data]);

  const topicsQ = useQuery({
    queryKey: ["topics", selected],
    queryFn: () => getTopics(selected),
    enabled: !!selected,
  });

  const completed = new Set(progressQ.data?.completed_topics ?? []);

  return (
    <View style={styles.root}>
      {/* Sticky header + chips */}
      <View style={[styles.header, { paddingTop: insets.top + spacing.sm }]}>
        <View style={styles.headerTop}>
          <View style={{ flex: 1 }}>
            <Text style={styles.title}>Studia</Text>
            <Text style={styles.sub}>Teoria per argomento</Text>
          </View>
          <Pressable
            testID="lib-search-btn"
            onPress={() => router.push("/search" as any)}
            style={styles.headerBtn}
            hitSlop={8}
          >
            <Icon name="search" size={20} color={colors.onSurface} />
          </Pressable>
          <Pressable
            testID="lib-favorites-btn"
            onPress={() => router.push("/favorites" as any)}
            style={styles.headerBtn}
            hitSlop={8}
          >
            <Icon name="bookmark" size={20} color={colors.onSurface} />
          </Pressable>
          <Pressable
            testID="lib-laws-btn"
            onPress={() => router.push("/laws" as any)}
            style={styles.headerBtn}
            hitSlop={8}
          >
            <Icon name="book" size={20} color={colors.onSurface} />
          </Pressable>
        </View>
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.chipRow}
          style={styles.chipScroller}
        >
          {(catsQ.data ?? []).map((c) => {
            const active = c.slug === selected;
            return (
              <Pressable
                key={c.slug}
                testID={`lib-chip-${c.slug}`}
                onPress={() => setSelected(c.slug)}
                style={[styles.chip, active && styles.chipActive]}
              >
                <Text style={[styles.chipText, active && styles.chipTextActive]}>{c.name}</Text>
              </Pressable>
            );
          })}
        </ScrollView>
      </View>

      {topicsQ.isLoading ? (
        <Loading />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, paddingBottom: bottomChrome + spacing.xxl, gap: spacing.md }}
          showsVerticalScrollIndicator={false}
        >
          {(topicsQ.data ?? []).map((t) => {
            const done = completed.has(t.slug);
            return (
              <Pressable
                key={t.slug}
                testID={`topic-row-${t.slug}`}
                style={styles.topicRow}
                onPress={() => router.push(`/topic/${t.slug}` as any)}
              >
                <View style={styles.topicTextWrap}>
                  <Text style={styles.topicTitle}>{t.title}</Text>
                  <Text style={styles.topicSub} numberOfLines={2}>
                    {t.subtitle}
                  </Text>
                  <View style={styles.topicMetaRow}>
                    <Icon name="clock" size={13} color={colors.muted} />
                    <Text style={styles.topicMeta}>{t.read_minutes} min</Text>
                    {done ? (
                      <>
                        <Icon name="check-circle" size={13} color={colors.success} />
                        <Text style={[styles.topicMeta, { color: colors.success }]}>Completato</Text>
                      </>
                    ) : null}
                  </View>
                </View>
                <Icon name="chevron-right" size={20} color={colors.muted} />
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
    paddingBottom: spacing.sm,
  },
  title: { fontFamily: fonts.display, fontSize: 32, color: colors.onSurface },
  sub: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted, marginBottom: spacing.sm },
  headerTop: { flexDirection: "row", alignItems: "flex-start", gap: spacing.sm },
  headerBtn: {
    width: 40,
    height: 40,
    borderRadius: radius.md,
    backgroundColor: colors.surfaceSecondary,
    alignItems: "center",
    justifyContent: "center",
    marginTop: spacing.xs,
  },
  chipScroller: { marginHorizontal: -spacing.lg },
  chipRow: { gap: spacing.sm, paddingHorizontal: spacing.lg, height: 56, alignItems: "center" },
  chip: {
    flexShrink: 0,
    height: 36,
    paddingHorizontal: spacing.lg,
    borderRadius: radius.pill,
    borderWidth: 1,
    borderColor: colors.borderStrong,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: colors.surface,
  },
  chipActive: { backgroundColor: colors.brandPrimary, borderColor: colors.brandPrimary },
  chipText: { fontFamily: fonts.medium, fontSize: 13, color: colors.onSurfaceTertiary },
  chipTextActive: { color: colors.onBrandPrimary },
  topicRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
  },
  topicTextWrap: { flex: 1, gap: 4 },
  topicTitle: { fontFamily: fonts.display, fontSize: 21, color: colors.onSurface, lineHeight: 26 },
  topicSub: { fontFamily: fonts.regular, fontSize: 13, color: colors.onSurfaceTertiary, lineHeight: 19 },
  topicMetaRow: { flexDirection: "row", alignItems: "center", gap: spacing.xs, marginTop: spacing.xs },
  topicMeta: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted, marginRight: spacing.sm },
}));
