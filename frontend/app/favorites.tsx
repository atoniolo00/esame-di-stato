import { useQuery } from "@tanstack/react-query";
import { useFocusEffect, useRouter } from "expo-router";
import { useCallback, useState } from "react";
import { Pressable, ScrollView, Text, View } from "react-native";

import { getTopics } from "@/src/api";
import { getFavorites } from "@/src/favorites";
import { EmptyState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, spacing, useTheme } from "@/src/theme";

export default function FavoritesScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const router = useRouter();
  const [slugs, setSlugs] = useState<string[]>([]);

  useFocusEffect(
    useCallback(() => {
      getFavorites().then(setSlugs);
    }, []),
  );

  const topicsQ = useQuery({ queryKey: ["topics", undefined], queryFn: () => getTopics() });
  const favs = (topicsQ.data ?? []).filter((t) => slugs.includes(t.slug));

  return (
    <View style={styles.root}>
      <ScreenHeader title="Preferiti" />
      {topicsQ.isLoading ? (
        <Loading />
      ) : favs.length === 0 ? (
        <EmptyState
          icon="bookmark"
          title="Nessun preferito"
          body="Salva gli argomenti chiave toccando il segnalibro nella pagina di teoria."
        />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, gap: spacing.md }}
          showsVerticalScrollIndicator={false}
        >
          {favs.map((t) => (
            <Pressable
              key={t.slug}
              testID={`fav-${t.slug}`}
              style={styles.row}
              onPress={() => router.push(`/topic/${t.slug}` as any)}
            >
              <Icon name="bookmark" size={18} color={colors.brandPrimary} />
              <View style={{ flex: 1, gap: 2 }}>
                <Text style={styles.title}>{t.title}</Text>
                <Text style={styles.sub} numberOfLines={1}>
                  {t.subtitle}
                </Text>
              </View>
              <Icon name="chevron-right" size={20} color={colors.muted} />
            </Pressable>
          ))}
        </ScrollView>
      )}
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  row: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
  },
  title: { fontFamily: fonts.display, fontSize: 20, color: colors.onSurface, lineHeight: 25 },
  sub: { fontFamily: fonts.regular, fontSize: 13, color: colors.onSurfaceTertiary },
}));
