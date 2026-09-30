import { useQuery } from "@tanstack/react-query";
import * as Haptics from "expo-haptics";
import { useLocalSearchParams } from "expo-router";
import { useEffect, useRef, useState } from "react";
import { Animated, Pressable, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { getFlashcards } from "@/src/api";
import { EmptyState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function FlashcardsScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const { category } = useLocalSearchParams<{ category: string }>();

  const q = useQuery({
    queryKey: ["flashcards", category],
    queryFn: () => getFlashcards(category!),
    enabled: !!category,
  });

  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const anim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    anim.setValue(flipped ? 1 : 0);
  }, [index]);

  const flip = () => {
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light).catch(() => {});
    Animated.spring(anim, { toValue: flipped ? 0 : 1, useNativeDriver: true, friction: 8, tension: 10 }).start();
    setFlipped((f) => !f);
  };

  const go = (dir: number) => {
    const cards = q.data ?? [];
    const nextIdx = index + dir;
    if (nextIdx < 0 || nextIdx >= cards.length) return;
    setFlipped(false);
    anim.setValue(0);
    setIndex(nextIdx);
  };

  if (q.isLoading) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Flashcard" />
        <Loading />
      </View>
    );
  }

  const cards = q.data ?? [];
  if (!cards.length) {
    return (
      <View style={styles.root}>
        <ScreenHeader title="Flashcard" />
        <EmptyState icon="layers" title="Nessuna flashcard" body="Presto disponibili per questo argomento." />
      </View>
    );
  }

  const card = cards[index];
  const frontRotate = anim.interpolate({ inputRange: [0, 1], outputRange: ["0deg", "180deg"] });
  const backRotate = anim.interpolate({ inputRange: [0, 1], outputRange: ["180deg", "360deg"] });

  return (
    <View style={styles.root}>
      <ScreenHeader title="Flashcard" subtitle={`${index + 1} di ${cards.length}`} />

      <View style={styles.center}>
        <Pressable testID="flashcard" onPress={flip} style={styles.cardArea}>
          <Animated.View
            style={[styles.card, styles.cardFront, { transform: [{ perspective: 1000 }, { rotateY: frontRotate }] }]}
          >
            <Text style={styles.face}>DOMANDA</Text>
            <Text style={styles.frontText}>{card.front}</Text>
            <View style={styles.tapHint}>
              <Icon name="refresh-cw" size={14} color={colors.muted} />
              <Text style={styles.tapHintText}>Tocca per la risposta</Text>
            </View>
          </Animated.View>
          <Animated.View
            style={[
              styles.card,
              styles.cardBack,
              { transform: [{ perspective: 1000 }, { rotateY: backRotate }] },
            ]}
          >
            <Text style={[styles.face, { color: colors.onBrandPrimary }]}>RISPOSTA</Text>
            <Text style={styles.backText}>{card.back}</Text>
          </Animated.View>
        </Pressable>
      </View>

      <View style={[styles.nav, { paddingBottom: Math.max(insets.bottom, spacing.lg) }]}>
        <Pressable
          testID="flashcard-prev"
          style={[styles.navBtn, index === 0 && styles.navBtnDisabled]}
          onPress={() => go(-1)}
          disabled={index === 0}
        >
          <Icon name="chevron-left" size={22} color={colors.onSurface} />
          <Text style={styles.navText}>Precedente</Text>
        </Pressable>
        <Pressable
          testID="flashcard-next"
          style={[styles.navBtn, index === cards.length - 1 && styles.navBtnDisabled]}
          onPress={() => go(1)}
          disabled={index === cards.length - 1}
        >
          <Text style={styles.navText}>Successiva</Text>
          <Icon name="chevron-right" size={22} color={colors.onSurface} />
        </Pressable>
      </View>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  center: { flex: 1, alignItems: "center", justifyContent: "center", padding: spacing.xl },
  cardArea: { width: "100%", height: 380 },
  card: {
    position: "absolute",
    width: "100%",
    height: "100%",
    borderRadius: radius.lg,
    padding: spacing.xl,
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.lg,
    backfaceVisibility: "hidden",
  },
  cardFront: { backgroundColor: colors.surfaceSecondary, borderWidth: 1, borderColor: colors.borderStrong },
  cardBack: { backgroundColor: colors.brandPrimary },
  face: { fontFamily: fonts.medium, fontSize: 11, letterSpacing: 1.5, color: colors.brandPrimary },
  frontText: { fontFamily: fonts.display, fontSize: 30, color: colors.onSurface, textAlign: "center", lineHeight: 36 },
  backText: { fontFamily: fonts.medium, fontSize: 22, color: colors.onBrandPrimary, textAlign: "center", lineHeight: 30 },
  tapHint: { flexDirection: "row", alignItems: "center", gap: spacing.xs, position: "absolute", bottom: spacing.lg },
  tapHintText: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted },
  nav: { flexDirection: "row", gap: spacing.md, paddingHorizontal: spacing.lg, paddingTop: spacing.md },
  navBtn: {
    flex: 1,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.xs,
    backgroundColor: colors.surfaceSecondary,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    paddingVertical: spacing.lg,
  },
  navBtnDisabled: { opacity: 0.4 },
  navText: { fontFamily: fonts.medium, fontSize: 14, color: colors.onSurface },
}));
