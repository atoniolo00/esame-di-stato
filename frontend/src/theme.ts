// Design tokens for ArchEsame — Editorial Mobile personality (light + dark).
// Keys match the "color"/"color_dark" blocks of /app/design_guidelines.json.

import { useMemo } from "react";
import { Appearance, StyleSheet, useColorScheme } from "react-native";

export type ColorScheme = "light" | "dark";

const light = {
  surface: "#F9F8F6",
  onSurface: "#1C1A19",
  surfaceSecondary: "#EFECE7",
  onSurfaceSecondary: "#1C1A19",
  surfaceTertiary: "#E5E1DB",
  onSurfaceTertiary: "#4A4543",
  surfaceInverse: "#262423",
  onSurfaceInverse: "#F2EFEA",
  muted: "#756D69",

  brand: "#C05A46",
  onBrand: "#FFFFFF",
  brandPrimary: "#C05A46",
  onBrandPrimary: "#FFFFFF",
  brandSecondary: "#D47C6A",
  onBrandSecondary: "#1C1A19",
  brandTertiary: "#EAC6C0",
  onBrandTertiary: "#5C281E",

  success: "#3A6B4C",
  onSuccess: "#FFFFFF",
  warning: "#C78D32",
  onWarning: "#FFFFFF",
  error: "#963A3A",
  onError: "#FFFFFF",
  info: "#455E6B",
  onInfo: "#FFFFFF",

  border: "#E1DCD3",
  borderStrong: "#BDB6AB",
  divider: "#E1DCD3",
};

const dark: typeof light = {
  surface: "#161514",
  onSurface: "#EAE7E1",
  surfaceSecondary: "#242220",
  onSurfaceSecondary: "#EAE7E1",
  surfaceTertiary: "#312E2C",
  onSurfaceTertiary: "#C3BDB6",
  surfaceInverse: "#F9F8F6",
  onSurfaceInverse: "#161514",
  muted: "#8F8984",

  brand: "#D0715D",
  onBrand: "#161514",
  brandPrimary: "#D0715D",
  onBrandPrimary: "#161514",
  brandSecondary: "#B4533C",
  onBrandSecondary: "#FFFFFF",
  brandTertiary: "#5C281E",
  onBrandTertiary: "#EAC6C0",

  success: "#4A825D",
  onSuccess: "#FFFFFF",
  warning: "#DBA24A",
  onWarning: "#161514",
  error: "#B84B4B",
  onError: "#FFFFFF",
  info: "#5D7A8A",
  onInfo: "#FFFFFF",

  border: "#3A3734",
  borderStrong: "#54504D",
  divider: "#3A3734",
};

export type ThemeColors = typeof light;

export const defaultScheme = "light" satisfies ColorScheme;
export const themes: { light: ThemeColors; dark?: ThemeColors } = { light, dark };

// Typography
export const fonts = {
  display: "CormorantGaramond-SemiBold",
  displayMedium: "CormorantGaramond-Medium",
  regular: "Satoshi-Regular",
  medium: "Satoshi-Medium",
  bold: "Satoshi-Bold",
};

export const spacing = { xs: 4, sm: 8, md: 12, lg: 16, xl: 24, xxl: 32, xxxl: 48 };
export const radius = { sm: 2, md: 4, lg: 8, pill: 999 };

export function setColorScheme(scheme: ColorScheme | null) {
  Appearance.setColorScheme?.(scheme ?? "unspecified");
}

setColorScheme?.(themes.dark ? null : defaultScheme);

export function useTheme(): { scheme: ColorScheme; colors: ThemeColors } {
  const system = useColorScheme();
  const scheme: ColorScheme = system && themes[system] ? system : defaultScheme;
  return { scheme, colors: themes[scheme] ?? themes.light };
}

export function makeStyles<T extends StyleSheet.NamedStyles<T> | StyleSheet.NamedStyles<any>>(
  factory: (colors: ThemeColors) => T & StyleSheet.NamedStyles<any>,
): () => T {
  return function useStyles(): T {
    const { colors } = useTheme();
    return useMemo(() => StyleSheet.create(factory(colors)), [colors]);
  };
}
