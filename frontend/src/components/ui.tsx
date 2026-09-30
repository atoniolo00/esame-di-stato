import Feather from "@react-native-vector-icons/feather";
import { useRouter } from "expo-router";
import { ActivityIndicator, Pressable, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { fonts, makeStyles, spacing, useTheme } from "@/src/theme";

export function Icon({
  name,
  size = 20,
  color,
}: {
  name: string;
  size?: number;
  color?: string;
}) {
  const { colors } = useTheme();
  // @ts-expect-error feather name typing is a large union; we pass validated names
  return <Feather name={name} size={size} color={color ?? colors.onSurface} />;
}

// Sticky, safe-area aware header for stack screens.
export function ScreenHeader({
  title,
  subtitle,
  back = true,
  right,
}: {
  title: string;
  subtitle?: string;
  back?: boolean;
  right?: React.ReactNode;
}) {
  const styles = useHeaderStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const router = useRouter();

  return (
    <View style={[styles.wrap, { paddingTop: insets.top + spacing.sm }]}>
      <View style={styles.row}>
        {back ? (
          <Pressable
            testID="header-back-button"
            onPress={() => router.back()}
            hitSlop={12}
            style={styles.backBtn}
          >
            <Icon name="chevron-left" size={24} color={colors.onSurface} />
          </Pressable>
        ) : (
          <View style={styles.backBtn} />
        )}
        <View style={styles.titles}>
          <Text style={styles.title} numberOfLines={1}>
            {title}
          </Text>
          {subtitle ? (
            <Text style={styles.subtitle} numberOfLines={1}>
              {subtitle}
            </Text>
          ) : null}
        </View>
        <View style={styles.right}>{right}</View>
      </View>
    </View>
  );
}

const useHeaderStyles = makeStyles((colors) => ({
  wrap: {
    backgroundColor: colors.surface,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.md,
  },
  row: { flexDirection: "row", alignItems: "center", gap: spacing.sm },
  backBtn: { width: 32, height: 32, alignItems: "center", justifyContent: "center" },
  titles: { flex: 1 },
  title: { fontFamily: fonts.display, fontSize: 24, color: colors.onSurface },
  subtitle: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted, marginTop: 2 },
  right: { minWidth: 32, alignItems: "flex-end" },
}));

export function Loading({ label }: { label?: string }) {
  const styles = useStateStyles();
  const { colors } = useTheme();
  return (
    <View style={styles.center} testID="loading-state">
      <ActivityIndicator color={colors.brandPrimary} size="large" />
      {label ? <Text style={styles.text}>{label}</Text> : null}
    </View>
  );
}

export function ErrorState({ message, onRetry }: { message?: string; onRetry?: () => void }) {
  const styles = useStateStyles();
  const { colors } = useTheme();
  return (
    <View style={styles.center} testID="error-state">
      <Icon name="alert-circle" size={32} color={colors.error} />
      <Text style={styles.text}>{message ?? "Si è verificato un errore."}</Text>
      {onRetry ? (
        <Pressable testID="retry-button" onPress={onRetry} style={styles.retry}>
          <Text style={styles.retryText}>Riprova</Text>
        </Pressable>
      ) : null}
    </View>
  );
}

export function EmptyState({
  icon = "inbox",
  title,
  body,
}: {
  icon?: string;
  title: string;
  body?: string;
}) {
  const styles = useStateStyles();
  const { colors } = useTheme();
  return (
    <View style={styles.center} testID="empty-state">
      <Icon name={icon} size={34} color={colors.muted} />
      <Text style={styles.emptyTitle}>{title}</Text>
      {body ? <Text style={styles.text}>{body}</Text> : null}
    </View>
  );
}

const useStateStyles = makeStyles((colors) => ({
  center: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    gap: spacing.md,
    padding: spacing.xl,
  },
  text: { fontFamily: fonts.regular, fontSize: 14, color: colors.muted, textAlign: "center" },
  emptyTitle: { fontFamily: fonts.display, fontSize: 22, color: colors.onSurface, textAlign: "center" },
  retry: {
    marginTop: spacing.sm,
    backgroundColor: colors.brandPrimary,
    paddingHorizontal: spacing.xl,
    paddingVertical: spacing.md,
    borderRadius: radiusLg,
  },
  retryText: { fontFamily: fonts.medium, color: colors.onBrandPrimary, fontSize: 14 },
}));

const radiusLg = 8;
