/**
 * Open Rechtspraak API client
 *
 * Wraps the Open Rechtspraak API for searching judges and retrieving
 * their published verdicts.
 *
 * Base URL: https://openrechtspraak.nl/api/v1/
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";

const BASE_URL = "https://openrechtspraak.nl/api/v1";
const BACKEND = "openRechtspraak";

export interface JudgeSearchResult {
  id: string;
  name: string;
  court?: string;
  title?: string;
}

export interface JudgeVerdict {
  ecli: string;
  title: string;
  date: string;
  court: string;
  summary?: string;
  type?: string;
}

/**
 * Make a request to the Open Rechtspraak API.
 */
async function openRechtspraakFetch(
  path: string,
  params?: URLSearchParams,
): Promise<unknown> {
  const url = params
    ? `${BASE_URL}${path}?${params.toString()}`
    : `${BASE_URL}${path}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: {
      Accept: "application/json",
    },
  });

  if (!response.ok) {
    const body = await response.text().catch(() => "");
    throw new Error(
      `Open Rechtspraak API request failed (${response.status}): ${response.statusText}. ${body}`,
    );
  }

  return response.json();
}

/**
 * Search for judges by name.
 */
export async function searchJudges(
  name: string,
): Promise<JudgeSearchResult[]> {
  const cacheKey = MultiTierCache.key("or-judges", name);
  const cached = cache.get<JudgeSearchResult[]>("search_results", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams({ q: name });

  const data = (await openRechtspraakFetch("/rechters", params)) as {
    results?: unknown[];
    data?: unknown[];
    items?: unknown[];
  };

  const items = data?.results ?? data?.data ?? data?.items ?? [];

  const results: JudgeSearchResult[] = (items as Record<string, unknown>[]).map(
    (item) => ({
      id: String(item.id ?? item.rechter_id ?? ""),
      name: String(item.naam ?? item.name ?? ""),
      court: optStr(item.gerecht ?? item.court),
      title: optStr(item.titel ?? item.title),
    }),
  );

  cache.set("search_results", cacheKey, results);
  return results;
}

/**
 * Get all published verdicts for a judge by judge ID.
 */
export async function getJudgeVerdicts(
  judgeId: string,
): Promise<JudgeVerdict[]> {
  const cacheKey = MultiTierCache.key("or-verdicts", judgeId);
  const cached = cache.get<JudgeVerdict[]>("search_results", cacheKey);
  if (cached) return cached;

  const data = (await openRechtspraakFetch(
    `/rechters/${encodeURIComponent(judgeId)}/uitspraken`,
  )) as {
    results?: unknown[];
    data?: unknown[];
    items?: unknown[];
  };

  const items = data?.results ?? data?.data ?? data?.items ?? [];

  const verdicts: JudgeVerdict[] = (items as Record<string, unknown>[]).map(
    (item) => ({
      ecli: String(item.ecli ?? item.id ?? ""),
      title: String(item.titel ?? item.title ?? ""),
      date: String(item.datum ?? item.date ?? ""),
      court: String(item.gerecht ?? item.court ?? ""),
      summary: optStr(item.samenvatting ?? item.summary),
      type: optStr(item.type ?? item.proceduresoort),
    }),
  );

  cache.set("search_results", cacheKey, verdicts);
  return verdicts;
}

function optStr(val: unknown): string | undefined {
  if (val == null) return undefined;
  return String(val);
}
