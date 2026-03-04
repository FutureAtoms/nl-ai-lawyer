/**
 * Multi-tier LRU cache with TTL per content type.
 *
 * Content types and their TTLs:
 *   legislation      - 24 hours
 *   caselaw_fulltext - 7 days
 *   search_results   - 1 hour
 *   kvk_data         - 4 hours
 */

import { LRUCache } from "lru-cache";

const HOUR = 1000 * 60 * 60;

export type CacheContentType =
  | "legislation"
  | "caselaw_fulltext"
  | "search_results"
  | "kvk_data";

const TTL_MAP: Record<CacheContentType, number> = {
  legislation: 24 * HOUR,
  caselaw_fulltext: 7 * 24 * HOUR,
  search_results: 1 * HOUR,
  kvk_data: 4 * HOUR,
};

/** Wrapper to satisfy LRUCache's `V extends {}` constraint. */
interface CacheEntry {
  value: unknown;
}

/**
 * A single cache tier backed by lru-cache.
 * Max 500 entries per tier to keep memory bounded.
 */
function createTier(contentType: CacheContentType): LRUCache<string, CacheEntry> {
  return new LRUCache<string, CacheEntry>({
    max: 500,
    ttl: TTL_MAP[contentType],
  });
}

export class MultiTierCache {
  private tiers = new Map<CacheContentType, LRUCache<string, CacheEntry>>();

  private getTier(contentType: CacheContentType): LRUCache<string, CacheEntry> {
    let tier = this.tiers.get(contentType);
    if (!tier) {
      tier = createTier(contentType);
      this.tiers.set(contentType, tier);
    }
    return tier;
  }

  /**
   * Retrieve a cached value or return undefined.
   */
  get<T = unknown>(contentType: CacheContentType, key: string): T | undefined {
    const entry = this.getTier(contentType).get(key);
    return entry ? (entry.value as T) : undefined;
  }

  /**
   * Store a value in the cache under the given content type.
   */
  set(contentType: CacheContentType, key: string, value: unknown): void {
    this.getTier(contentType).set(key, { value });
  }

  /**
   * Build a cache key from an arbitrary set of parameters.
   */
  static key(...parts: (string | number | undefined | null)[]): string {
    return parts
      .map((p) => (p == null ? "_" : String(p)))
      .join("::");
  }
}

/** Singleton cache instance. */
export const cache = new MultiTierCache();
