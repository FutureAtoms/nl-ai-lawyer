/**
 * data.overheid.nl client
 *
 * Wraps the CKAN-based API at data.overheid.nl for searching
 * Dutch government open datasets.
 *
 * Base URL: https://data.overheid.nl/data/api/3/
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";

const BASE_URL = "https://data.overheid.nl/data/api/3";
const BACKEND = "overheid";

export interface OverheidDataset {
  id: string;
  name: string;
  title: string;
  description: string;
  organization: string;
  modified: string;
  license: string;
  url: string;
  resources: Array<{
    id: string;
    name: string;
    format: string;
    url: string;
    description: string;
  }>;
  tags: string[];
}

export interface OverheidSearchResponse {
  totalResults: number;
  datasets: OverheidDataset[];
}

/**
 * Search government datasets on data.overheid.nl via the CKAN API.
 */
export async function searchDatasets(
  query: string,
  maxResults: number = 10,
  offset: number = 0,
): Promise<OverheidSearchResponse> {
  const cacheKey = MultiTierCache.key("overheid-search", query, maxResults, offset);
  const cached = cache.get<OverheidSearchResponse>("search_results", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams({
    q: query,
    rows: String(maxResults),
    start: String(offset),
  });

  const url = `${BASE_URL}/action/package_search?${params.toString()}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/json" },
  });

  if (!response.ok) {
    const body = await response.text().catch(() => "");
    throw new Error(
      `data.overheid.nl search failed (${response.status}): ${response.statusText}. ${body}`,
    );
  }

  const data = (await response.json()) as {
    success: boolean;
    result: {
      count: number;
      results: Record<string, unknown>[];
    };
  };

  if (!data.success) {
    throw new Error("data.overheid.nl API returned success=false");
  }

  const datasets: OverheidDataset[] = data.result.results.map(
    (pkg: Record<string, unknown>) => {
      const resources = ensureArray(
        pkg.resources as unknown[],
      ).map((r) => {
        const res = r as Record<string, unknown>;
        return {
          id: String(res.id ?? ""),
          name: String(res.name ?? res.description ?? ""),
          format: String(res.format ?? ""),
          url: String(res.url ?? ""),
          description: String(res.description ?? ""),
        };
      });

      const tags = ensureArray(pkg.tags as unknown[]).map(
        (t) => {
          const tag = t as Record<string, unknown>;
          return String(tag.display_name ?? tag.name ?? "");
        },
      );

      const org = pkg.organization as Record<string, unknown> | null;

      return {
        id: String(pkg.id ?? ""),
        name: String(pkg.name ?? ""),
        title: String(pkg.title ?? ""),
        description: String(pkg.notes ?? pkg.description ?? ""),
        organization: org ? String(org.title ?? org.name ?? "") : "",
        modified: String(
          pkg.metadata_modified ?? pkg.metadata_created ?? "",
        ),
        license: String(pkg.license_title ?? pkg.license_id ?? ""),
        url: String(
          pkg.url ??
            `https://data.overheid.nl/dataset/${pkg.name ?? pkg.id}`,
        ),
        resources,
        tags,
      };
    },
  );

  const result: OverheidSearchResponse = {
    totalResults: data.result.count,
    datasets,
  };

  cache.set("search_results", cacheKey, result);
  return result;
}

// ── Helpers ─────────────────────────────────────────────────────────

function ensureArray<T>(val: T | T[] | null | undefined): T[] {
  if (Array.isArray(val)) return val;
  if (val == null) return [];
  return [val];
}
