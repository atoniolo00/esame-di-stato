import { useQuery } from "@tanstack/react-query";
import { useRef, useState } from "react";
import { Platform, Pressable, ScrollView, Text, TextInput, View } from "react-native";
import { KeyboardAvoidingView } from "react-native-keyboard-controller";
import Markdown from "react-native-markdown-display";
import { useSafeAreaInsets } from "react-native-safe-area-context";

import { ChatMessage, getTutorHistory, streamTutor } from "@/src/api";
import { Icon } from "@/src/components/ui";
import { fonts, makeStyles, radius, spacing, useTheme } from "@/src/theme";

const SESSION = "main";
const SUGGESTIONS = [
  "Spiega le NTC 2018 in sintesi",
  "Differenza tra SCIA e permesso di costruire",
  "Cosa significa REI 120?",
  "Come funziona la gerarchia delle resistenze?",
];

export default function TutorScreen() {
  const styles = useStyles();
  const { colors } = useTheme();
  const insets = useSafeAreaInsets();
  const scrollRef = useRef<ScrollView>(null);

  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);

  useQuery({
    queryKey: ["tutor-history"],
    queryFn: async () => {
      const h = await getTutorHistory(SESSION);
      setMessages(h);
      return h;
    },
  });

  const scrollEnd = () => setTimeout(() => scrollRef.current?.scrollToEnd({ animated: true }), 60);

  const send = async (text: string) => {
    const msg = text.trim();
    if (!msg || busy) return;
    setInput("");
    setBusy(true);
    setMessages((prev) => [
      ...prev,
      { role: "user", content: msg, created_at: new Date().toISOString() },
      { role: "assistant", content: "", created_at: new Date().toISOString() },
    ]);
    scrollEnd();

    await streamTutor(SESSION, msg, {
      onDelta: (d) => {
        setMessages((prev) => {
          const next = [...prev];
          const last = next[next.length - 1];
          if (last && last.role === "assistant") next[next.length - 1] = { ...last, content: last.content + d };
          return next;
        });
        scrollEnd();
      },
      onDone: () => {
        setBusy(false);
        scrollEnd();
      },
      onError: () => {
        setMessages((prev) => {
          const next = [...prev];
          const last = next[next.length - 1];
          if (last && last.role === "assistant" && !last.content)
            next[next.length - 1] = { ...last, content: "⚠️ Errore nella risposta. Riprova." };
          return next;
        });
        setBusy(false);
      },
    });
  };

  const empty = messages.length === 0;

  return (
    <View style={styles.root}>
      <View style={[styles.header, { paddingTop: insets.top + spacing.sm }]}>
        <View style={{ flex: 1 }}>
          <Text style={styles.title}>Tutor AI</Text>
          <Text style={styles.sub}>{"Chiedi tutto sull'Esame di Stato"}</Text>
        </View>
        {!empty ? (
          <Pressable testID="tutor-clear" onPress={() => setMessages([])} hitSlop={10}>
            <Icon name="edit" size={20} color={colors.muted} />
          </Pressable>
        ) : null}
      </View>

      <KeyboardAvoidingView
        style={styles.flex}
        behavior={Platform.OS === "ios" ? "translate-with-padding" : "translate-with-padding"}
        keyboardVerticalOffset={0}
      >
        <ScrollView
          ref={scrollRef}
          style={styles.flex}
          contentContainerStyle={styles.listContent}
          showsVerticalScrollIndicator={false}
          keyboardShouldPersistTaps="handled"
        >
          {empty ? (
            <View style={styles.welcome}>
              <View style={styles.avatar}>
                <Icon name="feather" size={26} color={colors.onBrandPrimary} />
              </View>
              <Text style={styles.welcomeTitle}>Ciao! Sono il tuo tutor.</Text>
              <Text style={styles.welcomeBody}>
                Ti aiuto a capire norme, strutture, urbanistica e pratica professionale. Prova a chiedere:
              </Text>
              <View style={styles.suggestions}>
                {SUGGESTIONS.map((s) => (
                  <Pressable
                    key={s}
                    testID={`tutor-suggestion-${s.slice(0, 8)}`}
                    style={styles.suggestion}
                    onPress={() => send(s)}
                  >
                    <Text style={styles.suggestionText}>{s}</Text>
                  </Pressable>
                ))}
              </View>
            </View>
          ) : (
            messages.map((m, i) => (
              <View
                key={i}
                testID={`chat-msg-${m.role}-${i}`}
                style={[styles.bubbleWrap, m.role === "user" ? styles.userWrap : styles.aiWrap]}
              >
                {m.role === "assistant" ? (
                  <View style={styles.aiBubble}>
                    {m.content ? (
                      <Markdown style={mdStyles(colors)}>{m.content}</Markdown>
                    ) : (
                      <Text style={styles.typing}>Sto scrivendo…</Text>
                    )}
                  </View>
                ) : (
                  <View style={styles.userBubble}>
                    <Text style={styles.userText}>{m.content}</Text>
                  </View>
                )}
              </View>
            ))
          )}
        </ScrollView>

        <View style={[styles.composer, { paddingBottom: Math.max(insets.bottom, spacing.md) }]}>
          <TextInput
            testID="tutor-input"
            style={styles.input}
            placeholder="Scrivi una domanda…"
            placeholderTextColor={colors.muted}
            value={input}
            onChangeText={setInput}
            multiline
            onSubmitEditing={() => send(input)}
            onKeyPress={(e: any) => {
              if (
                Platform.OS === "web" &&
                e?.nativeEvent?.key === "Enter" &&
                !e?.nativeEvent?.shiftKey
              ) {
                e.preventDefault?.();
                send(input);
              }
            }}
          />
          <Pressable
            testID="tutor-send"
            style={[styles.sendBtn, (!input.trim() || busy) && styles.sendBtnDisabled]}
            onPress={() => send(input)}
            disabled={!input.trim() || busy}
          >
            <Icon name="arrow-up" size={20} color={colors.onBrandPrimary} />
          </Pressable>
        </View>
      </KeyboardAvoidingView>
    </View>
  );
}

const useStyles = makeStyles((colors) => ({
  root: { flex: 1, backgroundColor: colors.surface },
  flex: { flex: 1 },
  header: {
    flexDirection: "row",
    alignItems: "flex-end",
    backgroundColor: colors.surface,
    borderBottomWidth: 1,
    borderBottomColor: colors.divider,
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.md,
  },
  title: { fontFamily: fonts.display, fontSize: 32, color: colors.onSurface },
  sub: { fontFamily: fonts.regular, fontSize: 13, color: colors.muted },
  listContent: { padding: spacing.lg, gap: spacing.md },
  welcome: { alignItems: "center", gap: spacing.md, paddingTop: spacing.xxl },
  avatar: {
    width: 56,
    height: 56,
    borderRadius: radius.pill,
    backgroundColor: colors.brandPrimary,
    alignItems: "center",
    justifyContent: "center",
  },
  welcomeTitle: { fontFamily: fonts.display, fontSize: 26, color: colors.onSurface },
  welcomeBody: { fontFamily: fonts.regular, fontSize: 14, color: colors.muted, textAlign: "center", lineHeight: 21 },
  suggestions: { gap: spacing.sm, alignSelf: "stretch", marginTop: spacing.sm },
  suggestion: {
    backgroundColor: colors.surfaceSecondary,
    borderWidth: 1,
    borderColor: colors.border,
    borderRadius: radius.lg,
    padding: spacing.lg,
  },
  suggestionText: { fontFamily: fonts.medium, fontSize: 14, color: colors.onSurface },
  bubbleWrap: { maxWidth: "88%" },
  userWrap: { alignSelf: "flex-end" },
  aiWrap: { alignSelf: "flex-start" },
  userBubble: {
    backgroundColor: colors.brandPrimary,
    borderRadius: radius.lg,
    borderBottomRightRadius: radius.sm,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
  },
  userText: { fontFamily: fonts.regular, fontSize: 15, color: colors.onBrandPrimary, lineHeight: 21 },
  aiBubble: {
    backgroundColor: colors.surfaceSecondary,
    borderRadius: radius.lg,
    borderBottomLeftRadius: radius.sm,
    borderWidth: 1,
    borderColor: colors.border,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.xs,
  },
  typing: { fontFamily: fonts.regular, fontSize: 14, color: colors.muted, paddingVertical: spacing.sm },
  composer: {
    flexDirection: "row",
    alignItems: "flex-end",
    gap: spacing.sm,
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    borderTopWidth: 1,
    borderTopColor: colors.divider,
    backgroundColor: colors.surface,
  },
  input: {
    flex: 1,
    maxHeight: 120,
    backgroundColor: colors.surfaceTertiary,
    borderRadius: radius.lg,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    fontFamily: fonts.regular,
    fontSize: 15,
    color: colors.onSurface,
  },
  sendBtn: {
    width: 44,
    height: 44,
    borderRadius: radius.pill,
    backgroundColor: colors.brandPrimary,
    alignItems: "center",
    justifyContent: "center",
  },
  sendBtnDisabled: { opacity: 0.4 },
}));

const mdStyles = (colors: any) => ({
  body: { fontFamily: fonts.regular, fontSize: 15, color: colors.onSurface, lineHeight: 22 },
  strong: { fontFamily: fonts.bold, color: colors.onSurface },
  heading1: { fontFamily: fonts.display, fontSize: 22, color: colors.onSurface, marginTop: 8, marginBottom: 4 },
  heading2: { fontFamily: fonts.display, fontSize: 19, color: colors.onSurface, marginTop: 8, marginBottom: 4 },
  heading3: { fontFamily: fonts.medium, fontSize: 16, color: colors.onSurface, marginTop: 6 },
  bullet_list: { marginVertical: 4 },
  list_item: { marginVertical: 2 },
  code_inline: {
    fontFamily: Platform.select({ ios: "Menlo", default: "monospace" }),
    backgroundColor: colors.surfaceTertiary,
    color: colors.brandPrimary,
  },
});
