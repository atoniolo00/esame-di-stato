import { Tabs } from "expo-router";
import { Platform } from "react-native";

import { Icon } from "@/src/components/ui";
import { usesNativeTabs } from "@/src/navigation";
import { useTheme } from "@/src/theme";

export default function TabsLayout() {
  const { colors } = useTheme();

  if (usesNativeTabs) {
    // iOS 26+ native Liquid Glass tabs
    const { NativeTabs } = require("expo-router/unstable-native-tabs");
    return (
      <NativeTabs>
        <NativeTabs.Trigger name="index">
          <NativeTabs.Trigger.Icon sf="house.fill" />
          <NativeTabs.Trigger.Label>Home</NativeTabs.Trigger.Label>
        </NativeTabs.Trigger>
        <NativeTabs.Trigger name="library">
          <NativeTabs.Trigger.Icon sf="books.vertical.fill" />
          <NativeTabs.Trigger.Label>Studia</NativeTabs.Trigger.Label>
        </NativeTabs.Trigger>
        <NativeTabs.Trigger name="practice">
          <NativeTabs.Trigger.Icon sf="square.and.pencil" />
          <NativeTabs.Trigger.Label>Esercitati</NativeTabs.Trigger.Label>
        </NativeTabs.Trigger>
        <NativeTabs.Trigger name="tutor">
          <NativeTabs.Trigger.Icon sf="bubble.left.fill" />
          <NativeTabs.Trigger.Label>Tutor</NativeTabs.Trigger.Label>
        </NativeTabs.Trigger>
      </NativeTabs>
    );
  }

  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: colors.brandPrimary,
        tabBarInactiveTintColor: colors.muted,
        tabBarStyle: {
          backgroundColor: colors.surface,
          borderTopColor: colors.divider,
          ...(Platform.OS === "web" ? { height: 64 } : {}),
        },
        tabBarItemStyle: { alignSelf: "center" },
        tabBarLabelStyle: { fontFamily: "Satoshi-Medium", fontSize: 11 },
      }}
    >
      <Tabs.Screen
        name="index"
        options={{ title: "Home", tabBarIcon: ({ color }) => <Icon name="home" color={color} /> }}
      />
      <Tabs.Screen
        name="library"
        options={{ title: "Studia", tabBarIcon: ({ color }) => <Icon name="book-open" color={color} /> }}
      />
      <Tabs.Screen
        name="practice"
        options={{ title: "Esercitati", tabBarIcon: ({ color }) => <Icon name="edit-3" color={color} /> }}
      />
      <Tabs.Screen
        name="tutor"
        options={{ title: "Tutor", tabBarIcon: ({ color }) => <Icon name="message-circle" color={color} /> }}
      />
    </Tabs>
  );
}
