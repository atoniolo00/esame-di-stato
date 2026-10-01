import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import * as Haptics from "expo-haptics";
import { useLocalSearchParams } from "expo-router";
import { useEffect, useState } from "react";
import { Platform, Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import Markdown from "react-native-markdown-display";

import { completeTopic, getProgress, getTopic } from "@/src/api";
import { isFavorite, toggleFavorite } from "@/src/favorites";
import { ErrorState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function TopicScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const qc = useQueryClient();
  const { slug } = useLocalSearchParams<{ slug: string }>();

  const topicQ = useQuery({ queryKey: ["topic", slug], queryFn: () => getTopic(slug!), enabled: !!slug });
  const progressQ = useQuery({ queryKey: ["progress"], queryFn: getProgress });

  const completed = !!progressQ.data?.completed_topics?.includes(slug!);

  const [fav, setFav] = useState(false);
  useEffect(() => {
    if (slug) isFavorite(slug).then(setFav);
  }, [slug]);
  const onToggleFav = async () => {
    const state = await toggleFavorite(slug!);
    setFav(state);
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light).catch(() => {});
  };

  const completeMut = useMutation({
    mutationFn: () => completeTopic(slug!),
    onSuccess: () => {
      Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success).catch(() => {});
      qc.invalidateQueries({ queryKey: ["progress"] });
    },
  });

  if (topicQ.isLoading) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Argomento" />
        <Loading />
      </View>
    );
  }
  if (topicQ.isError || !topicQ.data) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Argomento" />
        <ErrorState onRetry={() => topicQ.refetch()} />
      </View>
    );
  }

  const t = topicQ.data;

  return (
    <View style={styles.root}>
      <ScreenHeader
        title="Argomento"
        right={
          <Pressable testID="topic-favorite-button" onPress={onToggleFav} hitSlop={10}>
            <Icon name="bookmark" size={22} color={fav ? colors.brandPrimary : colors.muted} />
          </Pressable>
        }
      />
      <ScrollView
        contentContainerStyle={{ padding: spacing.lg, paddingBottom: 120 }}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.title}>{t.title}</Text>
        <Text style={styles.subtitle}>{t.subtitle}</Text>

        <View style={styles.keyBox}>
          <Text style={styles.keyTitle}>PUNTI CHIAVE</Text>
          {t.key_points.map((k, i) => (
            <View key={i} style={styles.keyRow}>
              <Icon name="check" size={15} color={colors.brandPrimary} />
              <Text style={styles.keyText}>{k}</Text>
            </View>
          ))}
        </View>

        <Markdown style={mdStyles(colors)}>{t.content}</Markdown>
      </ScrollView>

      <View style={[styles.ctaBar, { paddingBottom: Math.max(insets.bottom, spacing.md) }]}>
        <Pressable
          testID="topic-complete-button"
          style={[styles.cta, completed && styles.ctaDone]}
          onPress={() => !completed && completeMut.mutate()}
          disabled={completed || completeMut.isPending}
        >
          <Icon
            name={completed ? "check-circle" : "circle"}
            size={20}
            color={completed ? colors.onSuccess : colors.onBrandPrimary}
          />
          <Text style={[styles.ctaText, completed && styles.ctaTextDone]}>
            {completed ? "Completato" : "Segna come completato"}
          </Text>
        </Pressable>
      </View>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  title: { fontFamily: fonts.display, fontSize: 32, color: colors.onSurface, lineHeight: 38 },
  subtitle: { fontFamily: fonts.regular, fontSize: 15, color: colors.muted, marginTop: spacing.xs, marginBottom: spacing.lg },
  keyBox: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.sm,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  keyTitle: { fontFamily: fonts.medium, fontSize: 11, letterSpacing: 1.2, color: colors.brandPrimary },
  keyRow: { flexDirection: "row", gap: spacing.sm, alignItems: "flex-start" },
  keyText: { flex: 1, fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 20 },
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
  ctaDone: { backgroundColor: colors.success },
  ctaText: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  ctaTextDone: { color: colors.onSuccess },
}));

const mdStyles = (colors: any) => ({
  body: { fontFamily: fonts.regular, fontSize: 16, color: colors.onSurface, lineHeight: 24 },
  strong: { fontFamily: fonts.bold, color: colors.onSurface },
  heading2: { fontFamily: fonts.display, fontSize: 24, color: colors.onSurface, marginTop: spacing.lg, marginBottom: spacing.xs },
  heading3: { fontFamily: fonts.medium, fontSize: 17, color: colors.onSurface, marginTop: spacing.md, marginBottom: spacing.xs },
  bullet_list: { marginVertical: spacing.xs },
  list_item: { marginVertical: 3 },
  blockquote: {
    backgroundColor: colors.brandTertiary,
    borderLeftWidth: 3,
    borderLeftColor: colors.brandPrimary,
    paddingHorizontal: spacing.md,
    paddingVertical: spacing.sm,
    borderRadius: radius.sm,
  },
  code_inline: {
    fontFamily: Platform.select({ ios: "Menlo", default: "monospace" }),
    backgroundColor: colors.surfaceTertiary,
    color: colors.brandPrimary,
  },
});
