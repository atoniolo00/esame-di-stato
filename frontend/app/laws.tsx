import { useQuery } from "@tanstack/react-query";
import { useMemo, useState } from "react";
import { ScrollView, Text, TextInput, View } from "react-native";

import { getLaws, Law } from "@/src/api";
import { Icon, Loading, ScreenHeader } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

export default function LawsScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const [term, setTerm] = useState("");

  const q = useQuery({ queryKey: ["laws"], queryFn: getLaws });

  const filtered = useMemo(() => {
    const list = q.data ?? [];
    const t = term.trim().toLowerCase();
    if (!t) return list;
    return list.filter(
      (l) =>
        l.numero.toLowerCase().includes(t) ||
        l.titolo.toLowerCase().includes(t) ||
        l.categoria.toLowerCase().includes(t) ||
        l.apporto.toLowerCase().includes(t),
    );
  }, [q.data, term]);

  return (
    <View style={styles.root}>
      <ScreenHeader title="Normativa" subtitle="Leggi chiave in sintesi" />
      <View style={styles.searchBar}>
        <Icon name="search" size={18} color={colors.muted} />
        <TextInput
          testID="laws-search"
          style={styles.input}
          placeholder="Cerca per numero, titolo o contenuto…"
          placeholderTextColor={colors.muted}
          value={term}
          onChangeText={setTerm}
        />
      </View>

      {q.isLoading ? (
        <Loading />
      ) : (
        <ScrollView
          contentContainerStyle={{ padding: spacing.lg, gap: spacing.md, paddingBottom: spacing.xxl }}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          <Text style={styles.count}>{filtered.length} norme</Text>
          {filtered.map((l: Law) => (
            <View key={l.lid} style={styles.card} testID={`law-${l.lid}`}>
              <View style={styles.cardHead}>
                <Text style={styles.numero}>{l.numero}</Text>
                <View style={styles.yearPill}>
                  <Text style={styles.year}>{l.anno}</Text>
                </View>
              </View>
              <Text style={styles.titolo}>{l.titolo}</Text>
              <Text style={styles.apporto}>{l.apporto}</Text>
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
  yearPill: {
    backgroundColor: colors.surfaceTertiary,
    paddingHorizontal: spacing.sm,
    paddingVertical: 2,
    borderRadius: radius.pill,
  },
  year: { fontFamily: fonts.medium, fontSize: 12, color: colors.onSurfaceTertiary },
  titolo: { fontFamily: fonts.display, fontSize: 20, color: colors.onSurface, lineHeight: 25 },
  apporto: { fontFamily: fonts.regular, fontSize: 14, color: colors.onSurfaceSecondary, lineHeight: 21 },
}));
