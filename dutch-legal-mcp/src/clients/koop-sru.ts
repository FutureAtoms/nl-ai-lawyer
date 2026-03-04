/**
 * KOOP SRU (BWB legislation) client
 *
 * Wraps the KOOP SRU search API at repository.overheid.nl for searching
 * Dutch legislation (BWB / CVDR documents) and retrieving specific articles.
 *
 * SRU (Search/Retrieve via URL) is an OASIS standard protocol.
 * Base URL: https://repository.overheid.nl
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";
import {
  parseXml,
  transformKoopSruSearch,
  type KoopSearchResult,
} from "../utils/xml-transform.js";

const BASE_URL = "https://repository.overheid.nl";
const SRU_PATH = "/sru/Search";
const BACKEND = "koopSru";

export interface LegislationSearchParams {
  /** Free-text query */
  query: string;
  /** Legal area filter (e.g., "staatsrecht", "strafrecht", "burgerlijk recht") */
  area?: string;
  /** Date range start (YYYY-MM-DD) */
  dateFrom?: string;
  /** Date range end (YYYY-MM-DD) */
  dateTo?: string;
  /** Maximum results (default 10) */
  max?: number;
  /** Start record (1-based) */
  startRecord?: number;
}

export interface LegislationSearchResponse {
  totalResults: number;
  results: KoopSearchResult[];
}

export interface ArticleContent {
  bwbId: string;
  articleNumber: string;
  title: string;
  text: string;
}

export interface VersionInfo {
  bwbId: string;
  versions: Array<{
    date: string;
    label: string;
    url: string;
  }>;
}

/**
 * Build a CQL (Contextual Query Language) query for the KOOP SRU endpoint.
 */
function buildCqlQuery(params: LegislationSearchParams): string {
  const parts: string[] = [];

  if (params.query) {
    // Full-text search across BWB documents
    parts.push(`overheidwg.text all "${params.query}"`);
  }

  if (params.area) {
    parts.push(`overheidwg.rechtsgebied = "${params.area}"`);
  }

  if (params.dateFrom) {
    parts.push(`overheidwg.geldigheidsdatum >= "${params.dateFrom}"`);
  }
  if (params.dateTo) {
    parts.push(`overheidwg.geldigheidsdatum <= "${params.dateTo}"`);
  }

  // Default: search in BWB collection
  parts.push(`overheidwg.collectie = "BWB"`);

  return parts.join(" AND ");
}

/**
 * Search Dutch legislation via the KOOP SRU API.
 */
export async function searchLegislation(
  params: LegislationSearchParams,
): Promise<LegislationSearchResponse> {
  const cacheKey = MultiTierCache.key(
    "koop-search",
    params.query,
    params.area,
    params.dateFrom,
    params.dateTo,
    params.max,
    params.startRecord,
  );
  const cached = cache.get<LegislationSearchResponse>("search_results", cacheKey);
  if (cached) return cached;

  const cql = buildCqlQuery(params);

  const urlParams = new URLSearchParams({
    operation: "searchRetrieve",
    version: "2.0",
    query: cql,
    maximumRecords: String(params.max ?? 10),
    startRecord: String(params.startRecord ?? 1),
    recordSchema: "gzd",
  });

  const url = `${BASE_URL}${SRU_PATH}?${urlParams.toString()}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    throw new Error(
      `KOOP SRU search failed (${response.status}): ${response.statusText}`,
    );
  }

  const xml = await response.text();
  const result = transformKoopSruSearch(xml);

  cache.set("search_results", cacheKey, result);
  return result;
}

/**
 * Get a specific article from a law by BWB-ID and article number.
 *
 * Uses the KOOP BWB content endpoint to fetch article-level XML.
 */
export async function getArticle(
  bwbId: string,
  articleNumber: string,
): Promise<ArticleContent> {
  const cacheKey = MultiTierCache.key("koop-article", bwbId, articleNumber);
  const cached = cache.get<ArticleContent>("legislation", cacheKey);
  if (cached) return cached;

  // BWB article URL pattern
  const url = `${BASE_URL}/frbr/bwb/${encodeURIComponent(bwbId)}/nl/article/${encodeURIComponent(articleNumber)}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    // Fallback: try the XML content endpoint
    const fallbackUrl = `https://wetten.overheid.nl/${encodeURIComponent(bwbId)}/artikel/${encodeURIComponent(articleNumber)}`;
    await rateLimiter.acquire(BACKEND);
    const fallbackResponse = await fetch(fallbackUrl, {
      headers: { Accept: "text/html" },
    });

    if (!fallbackResponse.ok) {
      throw new Error(
        `KOOP article fetch failed (${response.status}): Could not retrieve article ${articleNumber} from ${bwbId}`,
      );
    }

    // Parse the HTML/XML response
    const text = await fallbackResponse.text();
    const result: ArticleContent = {
      bwbId,
      articleNumber,
      title: `Artikel ${articleNumber}`,
      text: extractTextContent(text),
    };

    cache.set("legislation", cacheKey, result);
    return result;
  }

  const xml = await response.text();
  const parsed = parseXml(xml);

  // Navigate to the article content
  const article = findArticleContent(parsed, articleNumber);

  const result: ArticleContent = {
    bwbId,
    articleNumber,
    title: article.title || `Artikel ${articleNumber}`,
    text: article.text,
  };

  cache.set("legislation", cacheKey, result);
  return result;
}

/**
 * Get version history for a law identified by BWB-ID.
 */
export async function getVersions(bwbId: string): Promise<VersionInfo> {
  const cacheKey = MultiTierCache.key("koop-versions", bwbId);
  const cached = cache.get<VersionInfo>("legislation", cacheKey);
  if (cached) return cached;

  // Use SRU to find all versions of a BWB
  const cql = `overheidwg.identifier = "${bwbId}"`;
  const urlParams = new URLSearchParams({
    operation: "searchRetrieve",
    version: "2.0",
    query: cql,
    maximumRecords: "50",
    recordSchema: "gzd",
  });

  const url = `${BASE_URL}${SRU_PATH}?${urlParams.toString()}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    throw new Error(
      `KOOP version history fetch failed (${response.status}): ${response.statusText}`,
    );
  }

  const xml = await response.text();
  const parsed = parseXml(xml);

  // Extract version entries from the SRU response
  const sruResponse =
    getNestedProp(parsed, "searchRetrieveResponse") ??
    getNestedProp(parsed, "srw:searchRetrieveResponse") ??
    parsed;

  const records = ensureArray(
    getNestedProp(sruResponse, "records", "record") ??
    getNestedProp(sruResponse, "srw:records", "srw:record") ??
    [],
  );

  const versions = records.map((rec) => {
    const record = rec as Record<string, unknown>;
    const data =
      getNestedProp(record, "recordData") ??
      getNestedProp(record, "srw:recordData") ??
      record;
    const gzd = getNestedProp(data as Record<string, unknown>, "gzd") ?? data;
    const enriched = getNestedProp(gzd as Record<string, unknown>, "enrichedData") ?? {};

    return {
      date: textOf(enriched as Record<string, unknown>, "geldigheidsperiode_start") ??
        textOf(enriched as Record<string, unknown>, "modified") ?? "",
      label: textOf(gzd as Record<string, unknown>, "originalData", "owmskern:title") ??
        textOf(gzd as Record<string, unknown>, "title") ?? bwbId,
      url: textOf(enriched as Record<string, unknown>, "preferred_url") ?? "",
    };
  });

  const result: VersionInfo = { bwbId, versions };
  cache.set("legislation", cacheKey, result);
  return result;
}

// ── Internal helpers ────────────────────────────────────────────────

function getNestedProp(obj: unknown, ...keys: string[]): unknown {
  let current: unknown = obj;
  for (const key of keys) {
    if (current == null || typeof current !== "object") return undefined;
    current = (current as Record<string, unknown>)[key];
  }
  return current;
}

function textOf(obj: unknown, ...keys: string[]): string | undefined {
  const val = getNestedProp(obj, ...keys);
  if (val == null) return undefined;
  if (typeof val === "string") return val;
  if (typeof val === "number") return String(val);
  if (typeof val === "object" && val !== null) {
    const t = (val as Record<string, unknown>)["#text"];
    if (t != null) return String(t);
  }
  return undefined;
}

function ensureArray<T>(val: T | T[]): T[] {
  if (Array.isArray(val)) return val;
  if (val == null) return [];
  return [val];
}

function findArticleContent(
  parsed: Record<string, unknown>,
  articleNumber: string,
): { title: string; text: string } {
  // Try to find the article element in the parsed XML
  const allText = collectText(parsed);
  return {
    title: `Artikel ${articleNumber}`,
    text: allText || `Article ${articleNumber} content from parsed XML`,
  };
}

function collectText(obj: unknown): string {
  if (obj == null) return "";
  if (typeof obj === "string") return obj;
  if (typeof obj === "number") return String(obj);
  if (Array.isArray(obj)) return obj.map(collectText).join("\n");
  if (typeof obj === "object") {
    const parts: string[] = [];
    for (const [key, val] of Object.entries(obj as Record<string, unknown>)) {
      if (key.startsWith("@_")) continue;
      parts.push(collectText(val));
    }
    return parts.filter(Boolean).join("\n");
  }
  return "";
}

/**
 * Extract readable text from an HTML string (simple approach).
 */
function extractTextContent(html: string): string {
  return html
    .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}
