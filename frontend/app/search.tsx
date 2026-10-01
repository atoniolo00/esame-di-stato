import { useQuery } from "@tanstack/react-query";
import { useRouter } from "expo-router";
import { useEffect, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";

import { searchTopics } from "@/src/api";
import { EmptyState, Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function SearchScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const router = useRouter();
  const [term, setTerm] = useState("");
  const [debounced, setDebounced] = useState("");

  useEffect(() => {
    const id = setTimeout(() => setDebounced(term.trim()), 300);
    return () => clearTimeout(id);
  }, [term]);

  const q = useQuery({
    queryKey: ["search", debounced],
    queryFn: () => searchTopics(debounced),
    enabled: debounced.length >= 2,
  });

  const results = q.data ?? [];

  return (
    <View style={styles.root}>
      <ScreenHeader title="Cerca" />
      <View style={styles.searchBar}>
        <Icon name="search" size={18} color={colors.muted} />
        <TextInput
          testID="search-input"
          style={styles.input}
          placeholder="Cerca un argomento o un concetto…"
          placeholderTextColor={colors.muted}
          value={term}
          onChangeText={setTerm}
          autoFocus
          returnKeyType="search"
        />
        {term ? (
          <Pressable testID="search-clear" onPress={() => setTerm("")} hitSlop={8}>
            <Icon name="x" size={18} color={colors.muted} />
          </Pressable>
        ) : null}
      </View>

      {debounced.length < 2 ? (
        <EmptyState icon="search" title="Cosa vuoi ripassare?" body="Scrivi almeno due lettere per cercare tra gli argomenti." />
      ) : q.isLoading ? (
        <Loading />
      ) : results.length === 0 ? (
        <EmptyState icon="inbox" title="Nessun risultato" body={`Nessun argomento trovato per "${debounced}".`} />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, gap: spacing.md }}
          keyboardShouldPersistTaps="handled"
          showsVerticalScrollIndicator={false}
        >
          <Text style={styles.count}>{results.length} risultati</Text>
          {results.map((t) => (
            <Pressable
              key={t.slug}
              testID={`search-result-${t.slug}`}
              style={styles.row}
              onPress={() => router.push(`/topic/${t.slug}` as any)}
            >
              <View style={{ flex: 1, gap: 2 }}>
                <Text style={styles.title}>{t.title}</Text>
                <Text style={styles.sub} numberOfLines={2}>
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
  searchBar: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.sm,
    margin: spacing.lg,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    backgroundColor: colors.surfaceTertiary,
    borderRadius: radius.lg,
  },
  input: { flex: 1, fontFamily: fonts.regular, fontSize: 15, color: colors.onSurface },
  count: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted },
  row: {
    flexDirection: "row",
    alignItems: "center",
    gap: spacing.md,
    paddingVertical: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
  },
  title: { fontFamily: fonts.display, fontSize: 20, color: colors.onSurface, lineHeight: 25 },
  sub: { fontFamily: fonts.regular, fontSize: 13, color: colors.onSurfaceTertiary, lineHeight: 19 },
}));
