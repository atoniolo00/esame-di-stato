import { useQuery } from "@tanstack/react-query";
import { Image } from "expo-image";
import { LinearGradient } from "expo-linear-gradient";
import { useRouter } from "expo-router";
import { Pressable, ScrollView, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getCategories, getProgress } from "@/src/api";
import { Icon, Loading } from "@/src/components/ui";
import { usesNativeTabs } from "@/src/navigation";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

const HERO =
  "https://images.unsplash.com/photo-1714427435156-66ba34ddb75e?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjAzMzV8MHwxfHNlYXJjaHwyfHxtaW5pbWFsaXN0JTIwYXJjaGl0ZWN0dXJlJTIwdGVycmFjb3R0YXxlbnwwfHx8fDE3OTA3OTMxMDN8MA&ixlib=rb-4.1.0&q=85";

export default function HomeScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();
  const bottomChrome = usesNativeTabs ? insets.bottom : 0;

  const progressQ = useQuery({ queryKey: ["progress"], queryFn: getProgress });
  const catsQ = useQuery({ queryKey: ["categories"], queryFn: getCategories });

  const p = progressQ.data;
  const goalPct = p && p.total_topics ? p.completed_count / p.total_topics : 0;

  return (
    <View style={styles.root}>
      <ScrollView
        contentContainerStyle={{ paddingBottom: bottomChrome + spacing.xxl }}
        showsVerticalScrollIndicator={false}
      >
        {/* Hero */}
        <View style={styles.hero}>
          <Image source={{ uri: HERO }} style={styles.heroImg} contentFit="cover" transition={300} />
          <LinearGradient
            colors={["rgba(28,26,25,0.1)", "rgba(28,26,25,0.85)"]}
            style={styles.heroScrim}
          />
          <View style={[styles.heroText, { paddingTop: insets.top + spacing.xl }]}>
            <Text style={styles.heroKicker}>ESAME DI STATO · ARCHITETTO</Text>
            <Text style={styles.heroTitle}>ArchEsame</Text>
            <Text style={styles.heroSubtitle}>
              Studia, ripeti e mettiti alla prova, ogni giorno.
            </Text>
          </View>
        </View>

        <View style={styles.body}>
          {progressQ.isLoading ? (
            <Loading />
          ) : (
            <>
              {/* Streak + accuracy */}
              <View style={styles.statRow}>
                <View style={styles.statCard} testID="home-streak-card">
                  <Icon name="zap" size={20} color={colors.brandPrimary} />
                  <Text style={styles.statNum}>{p?.streak ?? 0}</Text>
                  <Text style={styles.statLabel}>giorni di fila</Text>
                </View>
                <View style={styles.statCard} testID="home-accuracy-card">
                  <Icon name="target" size={20} color={colors.success} />
                  <Text style={styles.statNum}>{p?.accuracy ?? 0}%</Text>
                  <Text style={styles.statLabel}>precisione quiz</Text>
                </View>
              </View>

              {/* Daily goal */}
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>Obiettivo di studio</Text>
                <Text style={styles.sectionBody}>
                  {p?.completed_count ?? 0} di {p?.total_topics ?? 0} argomenti completati
                </Text>
                <View style={styles.track}>
                  <View style={[styles.fill, { width: `${Math.round(goalPct * 100)}%` }]} />
                </View>
              </View>

              {/* Continue studying */}
              <View style={styles.section}>
                <Text style={styles.sectionTitle}>Continua a studiare</Text>
              </View>
              <ScrollView
                horizontal
                showsHorizontalScrollIndicator={false}
                contentContainerStyle={styles.catRow}
              >
                {(catsQ.data ?? []).slice(0, 8).map((c) => (
                  <Pressable
                    key={c.slug}
                    testID={`home-cat-${c.slug}`}
                    style={styles.catCard}
                    onPress={() => router.push(`/library?category=${c.slug}` as any)}
                  >
                    <Icon name={c.icon} size={22} color={colors.brandPrimary} />
                    <Text style={styles.catName}>{c.name}</Text>
                    <Text style={styles.catMeta}>
                      {c.topic_count} argoment{c.topic_count === 1 ? "o" : "i"}
                    </Text>
                  </Pressable>
                ))}
              </ScrollView>

              {/* Quick actions */}
              <View style={styles.section}>
                <Pressable
                  testID="home-tutor-cta"
                  style={styles.primaryCta}
                  onPress={() => router.push("/tutor" as any)}
                >
                  <Icon name="message-circle" size={20} color={colors.onBrandPrimary} />
                  <Text style={styles.primaryCtaText}>Chiedi al Tutor AI</Text>
                </Pressable>
                <Pressable
                  testID="home-progress-cta"
                  style={styles.secondaryCta}
                  onPress={() => router.push("/progress" as any)}
                >
                  <Icon name="bar-chart-2" size={20} color={colors.onSurface} />
                  <Text style={styles.secondaryCtaText}>Le mie statistiche</Text>
                  <Icon name="chevron-right" size={18} color={colors.muted} />
                </Pressable>
                <Pressable
                  testID="home-laws-cta"
                  style={styles.secondaryCta}
                  onPress={() => router.push("/laws" as any)}
                >
                  <Icon name="book" size={20} color={colors.onSurface} />
                  <Text style={styles.secondaryCtaText}>Schede normativa</Text>
                  <Icon name="chevron-right" size={18} color={colors.muted} />
                </Pressable>
              </View>
            </>
          )}
        </View>
      </ScrollView>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  hero: { height: 280, justifyContent: "flex-end" },
  heroImg: { ...StyleSheetAbsolute },
  heroScrim: { ...StyleSheetAbsolute },
  heroText: { padding: spacing.xl },
  heroKicker: { fontFamily: fonts.medium, fontSize: 11, letterSpacing: 1.5, color: "#EAC6C0" },
  heroTitle: { fontFamily: fonts.display, fontSize: 44, color: "#FFFFFF", marginTop: spacing.xs },
  heroSubtitle: { fontFamily: fonts.regular, fontSize: 15, color: "#F2EFEA", marginTop: spacing.xs },
  body: { padding: spacing.lg, gap: spacing.lg },
  statRow: { flexDirection: "row", gap: spacing.md },
  statCard: {
    flex: 1,
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.xs,
    borderWidth: 1,
    borderColor: colors.border,
  },
  statNum: { fontFamily: fonts.display, fontSize: 34, color: colors.onSurface },
  statLabel: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted },
  section: { gap: spacing.sm },
  sectionTitle: { fontFamily: fonts.display, fontSize: 22, color: colors.onSurface },
  sectionBody: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted },
  track: {
    height: 8,
    backgroundColor: colors.surfaceTertiary,
    borderRadius: radius.pill,
    overflow: "hidden",
    marginTop: spacing.xs,
  },
  fill: { height: 8, backgroundColor: colors.brandPrimary, borderRadius: radius.pill },
  catRow: { gap: spacing.md, paddingVertical: spacing.xs },
  catCard: {
    width: 140,
    backgroundColor: colors.surface,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.sm,
  },
  catName: { fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface },
  catMeta: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted },
  primaryCta: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.sm,
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
  },
  primaryCtaText: { fontFamily: fonts.bold, fontSize: 16, color: colors.onBrandPrimary },
  secondaryCta: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.sm,
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
    paddingHorizontal: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  secondaryCtaText: { flex: 1, fontFamily: fonts.medium, fontSize: 15, color: colors.onSurface },
}));

const StyleSheetAbsolute = {
  position: "absolute" as const,
  left: 0,
  right: 0,
  top: 0,
  bottom: 0,
};
