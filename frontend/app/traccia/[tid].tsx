import { useQuery } from "@tanstack/react-query";
import { useLocalSearchParams } from "expo-router";
import { ScrollView, Text, View } from "react-native";

import { getTracce } from "@/src/api";
import { ErrorState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function TracciaScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const { tid } = useLocalSearchParams<{ tid: string }>();

  const q = useQuery({ queryKey: ["tracce"], queryFn: getTracce });

  if (q.isLoading) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Traccia d'esame" />
        <Loading />
      </View>
    );
  }
  const t = (q.data ?? []).find((x) => x.tid === tid);
  if (q.isError || !t) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Traccia d'esame" />
        <ErrorState message="Traccia non trovata" onRetry={() => q.refetch()} />
      </View>
    );
  }

  return (
    <View style={styles.root}>
      <ScreenHeader title="Traccia d'esame" />
      <ScrollView contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
        <View style={styles.badges}>
          <View style={styles.badge}>
            <Text style={styles.badgeText}>{t.sezione}</Text>
          </View>
          <View style={[styles.badge, styles.badgeAlt]}>
            <Text style={[styles.badgeText, styles.badgeTextAlt]}>{t.tipo}</Text>
          </View>
        </View>
        <Text style={styles.session}>{t.sessione}</Text>
        <Text style={styles.title}>{t.titolo}</Text>

        <Text style={styles.sectionLabel}>LA TRACCIA</Text>
        <Text style={styles.body}>{t.testo}</Text>

        <View style={styles.tipBox}>
          <View style={styles.tipHead}>
            <Icon name="compass" size={16} color={colors.brandPrimary} />
            <Text style={styles.tipTitle}>Come affrontarla</Text>
          </View>
          <Text style={styles.tipText}>{t.suggerimenti}</Text>
        </View>

        <Text style={styles.note}>
          Fonte: temi estratti Esami di Stato — Università Iuav di Venezia (2024). Sintesi a scopo di studio.
        </Text>
      </ScrollView>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  content: { padding: spacing.lg, gap: spacing.sm, paddingBottom: spacing.xxl },
  badges: { flexDirection: "row", gap: spacing.sm, flexWrap: "wrap" },
  badge: {
    backgroundColor: colors.brandTertiary,
    paddingHorizontal: spacing.md,
    paddingVertical: 6,
    borderRadius: radius.pill,
  },
  badgeAlt: { backgroundColor: colors.surfaceTertiary },
  badgeText: { fontFamily: fonts.medium, fontSize: 12, color: colors.onBrandTertiary },
  badgeTextAlt: { color: colors.onSurfaceTertiary },
  session: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted, marginTop: spacing.xs },
  title: { fontFamily: fonts.display, fontSize: 30, color: colors.onSurface, lineHeight: 36, marginBottom: spacing.md },
  sectionLabel: { fontFamily: fonts.medium, fontSize: 11, letterSpacing: 1.2, color: colors.brandPrimary, marginTop: spacing.sm },
  body: { fontFamily: fonts.regular, fontSize: 16, color: colors.onSurface, lineHeight: 25 },
  tipBox: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.sm,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  tipHead: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  tipTitle: { fontFamily: fonts.bold, fontSize: 15, color: colors.onSurface },
  tipText: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurface, lineHeight: 21 },
  note: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted, marginTop: spacing.lg, lineHeight: 18, fontStyle: "italic" },
}));
