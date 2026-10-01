import { storage } from "@/src/utils/storage";

const KEY = "arch_favorites";

export async function getFavorites(): Promise<string[]> {
  const list = await storage.getItem<string[]>(KEY, []);
  return Array.isArray(list) ? list : [];
}

export async function isFavorite(slug: string): Promise<boolean> {
  const list = await getFavorites();
  return list.includes(slug);
}

export async function toggleFavorite(slug: string): Promise<boolean> {
  const list = await getFavorites();
  const exists = list.includes(slug);
  const next = exists ? list.filter((s) => s !== slug) : [...list, slug];
  await storage.setItem(KEY, next);
  return !exists; // returns new favorite state
}
