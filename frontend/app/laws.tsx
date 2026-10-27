import { useQuery } from "@tanstack/react-query";
import { useLocalSearchParams } from "expo-router";
import { useEffect, useMemo, useState } from "react";
import { Pressable, ScrollView, Text, TextInput, View } from "react-native";

import { getCategories, getLaws, Law } from "@/src/api";
import { Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function LawsScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const params = useLocalSearchParams<{ focus?: string }>();
  const [term, setTerm] = useState("");
  const [openLid, setOpenLid] = useState<string | null>(null);

  const q = useQuery({ queryKey: ["laws"], queryFn: getLaws });
  const catsQ = useQuery({ queryKey: ["categories"], queryFn: getCategories });

  useEffect(() => {
    if (params.focus) setTerm(params.focus);
  }, [params.focus]);

  useEffect(() => {
    const hit = params.focus ? q.data?.find((l) => l.numero === params.focus) : undefined;
    if (hit) setOpenLid(hit.lid);
  }, [params.focus, q.data]);

  const catName = (slug: string) =>
    catsQ.data?.find((c) => c.slug === slug)?.name ?? slug;

  // group filtered laws by categoria
  const groups = useMemo(() => {
    const list = q.data ?? [];
    const t = term.trim().toLowerCase();
    const filtered = !t
      ? list
      : list.filter(
          (l) =>
            l.numero.toLowerCase().includes(t) ||
            l.titolo.toLowerCase().includes(t) ||
            l.categoria.toLowerCase().includes(t) ||
            l.apporto.toLowerCase().includes(t),
        );
    const map: Record<string, Law[]> = {};
    for (const l of filtered) (map[l.categoria] ||= []).push(l);
    const first = (k: string) => (k.toLowerCase().startsWith("urbanistic") ? 0 : 1);
    return Object.entries(map).sort((a, b) => first(a[0]) - first(b[0]) || a[0].localeCompare(b[0]));
  }, [q.data, term]);

  const total = groups.reduce((n, g) => n + g[1].length, 0);

  return (
    <View style={styles.root}>
      <ScreenHeader title="Normativa" subtitle="Leggi per argomento" />
      <View style={styles.searchBar}>
        <Icon name="search" size={18} color={colors.muted} />
        <TextInput
          testID="laws-search"
          style={styles.input}
          placeholder="Cerca numero, materia o contenuto…"
          placeholderTextColor={colors.muted}
          value={term}
          onChangeText={setTerm}
        />
        {term ? (
          <Pressable testID="laws-clear" onPress={() => setTerm("")} hitSlop={8}>
            <Icon name="x" size={18} color={colors.muted} />
          </Pressable>
        ) : null}
      </View>

      {q.isLoading ? (
        <Loading />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, gap: spacing.lg, paddingBottom: spacing.xxl }}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          <Text style={styles.count}>{total} {total === 1 ? "norma" : "norme"} in {groups.length} {groups.length === 1 ? "area" : "aree"}</Text>
          {groups.map(([cat, laws]) => (
            <View key={cat} style={styles.group}>
              <View style={styles.groupHead}>
                <View style={styles.dot} />
                <Text style={styles.groupTitle}>{catName(cat)}</Text>
                <Text style={styles.groupCount}>{laws.length}</Text>
              </View>
              {laws.map((l) => {
                const open = openLid === l.lid;
                return (
                  <Pressable
                    key={l.lid}
                    testID={`law-${l.lid}`}
                    style={styles.card}
                    onPress={() => setOpenLid(open ? null : l.lid)}
                  >
                    <View style={styles.cardHead}>
                      <Text style={styles.numero}>{l.numero}</Text>
                      <View style={styles.yearPill}>
                        <Text style={styles.year}>{l.anno}</Text>
                      </View>
                    </View>
                    <Text style={styles.titolo}>{l.titolo}</Text>
                    <Text style={styles.apporto}>{l.apporto}</Text>
                    {open && l.dettaglio ? (
                      <View style={styles.dettaglioBox}>
                        <Text style={styles.dettaglio}>{l.dettaglio}</Text>
                      </View>
                    ) : l.dettaglio ? (
                      <Text style={styles.more}>Tocca per approfondire</Text>
                    ) : null}
                  </Pressable>
                );
              })}
            </View>
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
    marginHorizontal: spacing.lg,
    marginTop: spacing.lg,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    backgroundColor: colors.surfaceTertiary,
    borderRadius: radius.lg,
  },
  input: { flex: 1, fontFamily: fonts.regular, fontSize: 15, color: colors.onSurface },
  count: { fontFamily: fonts.regular, fontSize: 12, color: colors.muted },
  group: { gap: spacing.sm },
  groupHead: { flexDirection: "row", alignItems: "center", gap: spacing.sm, marginBottom: spacing.xs },
  dot: { width: 8, height: 8, borderRadius: 4, backgroundColor: colors.brandPrimary },
  groupTitle: { flex: 1, fontFamily: fonts.display, fontSize: 24, color: colors.onSurface },
  groupCount: { fontFamily: fonts.medium, fontSize: 13, color: colors.muted },
  card: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    padding: spacing.lg,
    gap: spacing.xs,
    borderWidth: 1,
    borderColor: colors.border,
    borderLeftWidth: 3,
    borderLeftColor: colors.brandPrimary,
  },
  cardHead: { flexDirection: "row", alignItems: "center", justifyContent: "space-between" },
  numero: { fontFamily: fonts.bold, fontSize: 16, color: colors.brandPrimary, flex: 1 },
  yearPill: { backgroundColor: colors.surfaceTertiary, paddingHorizontal: spacing.sm, paddingVertical: 2, borderRadius: radius.pill },
  year: { fontFamily: fonts.medium, fontSize: 12, color: colors.onSurfaceTertiary },
  titolo: { fontFamily: fonts.display, fontSize: 20, color: colors.onSurface, lineHeight: 25 },
  apporto: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurfaceSecondary, lineHeight: 21 },
  more: { fontFamily: fonts.medium, fontSize: 12, color: colors.brandPrimary, marginTop: 2 },
  dettaglioBox: {
    marginTop: spacing.xs,
    backgroundColor: colors.brandTertiary,
    borderRadius: radius.md,
    padding: spacing.md,
  },
  dettaglio: { fontFamily: fonts.regular, fontSize: 14, color: colors.onBrandTertiary, lineHeight: 21 },
}));
