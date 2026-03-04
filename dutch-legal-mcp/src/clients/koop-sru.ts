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

// SRU endpoint moved from repository.overheid.nl to zoekservice.overheid.nl (2025)
const SRU_BASE_URL = "https://zoekservice.overheid.nl";
const SRU_PATH = "/sru/Search";
const WETTEN_BASE_URL = "https://wetten.overheid.nl";
const REPO_BASE_URL = "https://repository.officiele-overheidspublicaties.nl";
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
    // Title search using 'adj' operator for flexible matching (zoekservice.overheid.nl)
    parts.push(`overheidbwb.titel adj "${params.query}"`);
  }

  if (params.area) {
    parts.push(`overheidbwb.rechtsgebied = "${params.area}"`);
  }

  if (params.dateFrom) {
    parts.push(`overheidbwb.geldigheidsperiode_startdatum >= "${params.dateFrom}"`);
  }
  if (params.dateTo) {
    parts.push(`overheidbwb.geldigheidsperiode_einddatum <= "${params.dateTo}"`);
  }

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
    version: "1.2",
    "x-connection": "BWB",
    query: cql,
    maximumRecords: String(params.max ?? 10),
    startRecord: String(params.startRecord ?? 1),
  });

  const url = `${SRU_BASE_URL}${SRU_PATH}?${urlParams.toString()}`;

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

  // Strategy 1: Try to find the article in the XML repository via SRU metadata
  // First, search SRU for the BWB to get the current dated XML URL
  try {
    const article = await getArticleFromXmlRepo(bwbId, articleNumber);
    if (article) {
      cache.set("legislation", cacheKey, article);
      return article;
    }
  } catch {
    // Fall through to HTML fallback
  }

  // Strategy 2: Fetch from wetten.overheid.nl HTML (follows redirects)
  const wettenUrl = `${WETTEN_BASE_URL}/${encodeURIComponent(bwbId)}`;
  await rateLimiter.acquire(BACKEND);
  const response = await fetch(wettenUrl, {
    headers: { Accept: "text/html" },
    redirect: "follow",
  });

  if (response.ok) {
    const html = await response.text();
    const articleText = extractArticleFromHtml(html, articleNumber);
    if (articleText) {
      const result: ArticleContent = {
        bwbId,
        articleNumber,
        title: `Artikel ${articleNumber}`,
        text: articleText,
      };
      cache.set("legislation", cacheKey, result);
      return result;
    }
  }

  throw new Error(
    `Article fetch failed: Could not retrieve article ${articleNumber} from ${bwbId}.`,
  );
}

/**
 * Fetch a specific article from the official XML repository.
 * Tries to construct the XML URL from the BWB ID and today's date.
 */
async function getArticleFromXmlRepo(
  bwbId: string,
  articleNumber: string,
): Promise<ArticleContent | null> {
  // Construct the XML URL using today's date
  const today = new Date().toISOString().split("T")[0]; // YYYY-MM-DD
  const xmlUrl = `${REPO_BASE_URL}/bwb/${bwbId}/${today}_0/xml/${bwbId}_${today}_0.xml`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(xmlUrl, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) return null;

  const xml = await response.text();
  return extractArticleFromXml(xml, bwbId, articleNumber);
}

/**
 * Extract a specific article from BWB XML content.
 * BWB XML uses <artikel> elements with a label like 'Artikel 610'.
 */
function extractArticleFromXml(
  xml: string,
  bwbId: string,
  articleNumber: string,
): ArticleContent | null {
  // Normalize article number: "7:610" -> "610", "610" -> "610"
  const normalizedArt = articleNumber.includes(":")
    ? articleNumber.split(":").pop()!
    : articleNumber;

  // Match the article element by its label attribute
  const patterns = [
    new RegExp(
      `<artikel[^>]*label="Artikel\\s+${escapeRegex(normalizedArt)}"[^>]*>([\\s\\S]*?)</artikel>`,
      "i",
    ),
    new RegExp(
      `<artikel[^>]*label="Artikel\\s+${escapeRegex(articleNumber)}"[^>]*>([\\s\\S]*?)</artikel>`,
      "i",
    ),
  ];

  for (const pattern of patterns) {
    const match = xml.match(pattern);
    if (match) {
      // Strip XML tags to get plain text
      const text = match[0]
        .replace(/<[^>]+>/g, " ")
        .replace(/\s+/g, " ")
        .trim();
      return {
        bwbId,
        articleNumber,
        title: `Artikel ${articleNumber}`,
        text,
      };
    }
  }

  return null;
}

/**
 * Get version history for a law identified by BWB-ID.
 */
export async function getVersions(bwbId: string): Promise<VersionInfo> {
  const cacheKey = MultiTierCache.key("koop-versions", bwbId);
  const cached = cache.get<VersionInfo>("legislation", cacheKey);
  if (cached) return cached;

  // Use SRU to find all versions of a BWB
  const cql = `dcterms.identifier = "${bwbId}"`;
  const urlParams = new URLSearchParams({
    operation: "searchRetrieve",
    version: "1.2",
    "x-connection": "BWB",
    query: cql,
    maximumRecords: "50",
  });

  const url = `${SRU_BASE_URL}${SRU_PATH}?${urlParams.toString()}`;

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

  // Extract version entries from the SRU response (handles both SRU 1.2 and 2.0 namespace variants)
  const sruResponse =
    getNestedProp(parsed, "searchRetrieveResponse") ??
    getNestedProp(parsed, "srw:searchRetrieveResponse") ??
    getNestedProp(parsed, "zs:searchRetrieveResponse") ??
    parsed;

  const records = ensureArray(
    getNestedProp(sruResponse, "records", "record") ??
    getNestedProp(sruResponse, "srw:records", "srw:record") ??
    getNestedProp(sruResponse, "zs:records", "zs:record") ??
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
 * Extract a specific article from wetten.overheid.nl HTML.
 * wetten.overheid.nl uses div elements with id attributes like "Artikel610" or anchors.
 */
function extractArticleFromHtml(html: string, articleNumber: string): string | null {
  const normalizedArt = articleNumber.includes(":")
    ? articleNumber.split(":").pop()!
    : articleNumber;

  // Clean the HTML first
  const clean = html
    .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
    .replace(/<nav[^>]*>[\s\S]*?<\/nav>/gi, "")
    .replace(/<header[^>]*>[\s\S]*?<\/header>/gi, "")
    .replace(/<footer[^>]*>[\s\S]*?<\/footer>/gi, "");

  // Strategy 1: Find by id attribute (wetten.nl uses id="Artikel610")
  const idPatterns = [
    new RegExp(`id="[^"]*Artikel${escapeRegex(normalizedArt)}"[^>]*>([\\s\\S]*?)(?=<div[^>]*id="[^"]*Artikel|<\\/section|$)`, "i"),
    new RegExp(`id="[^"]*Artikel_${escapeRegex(normalizedArt)}"[^>]*>([\\s\\S]*?)(?=<div[^>]*id="[^"]*Artikel|<\\/section|$)`, "i"),
  ];

  for (const pattern of idPatterns) {
    const match = clean.match(pattern);
    if (match) {
      const text = cleanWettenUiNoise(match[0].replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim());
      if (text.length > 20) return text;
    }
  }

  // Strategy 2: Find in plain text between "Artikel X" headers
  const plainText = clean.replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
  const artStart = plainText.indexOf(`Artikel ${normalizedArt} `);
  if (artStart !== -1) {
    // Find the next "Artikel" header (but not "Artikel X" variants like "Artikel Xa")
    const nextArtPattern = new RegExp(`Artikel\\s+${escapeRegex(normalizedArt)}[a-z]\\b|Artikel\\s+(?!${escapeRegex(normalizedArt)}\\b)\\d`, "i");
    const rest = plainText.substring(artStart + 10);
    const nextMatch = rest.search(nextArtPattern);
    const articleText = nextMatch !== -1
      ? plainText.substring(artStart, artStart + 10 + nextMatch)
      : plainText.substring(artStart, artStart + 3000);

    if (articleText.length > 30) return cleanWettenUiNoise(articleText.trim());
  }

  return null;
}

function escapeRegex(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/**
 * Remove wetten.nl UI noise from extracted text (navigation hints, buttons, etc.)
 */
function cleanWettenUiNoise(text: string): string {
  return text
    .replace(/id="[^"]*"\s*/g, "")
    .replace(/Toon relaties in LiDO/gi, "")
    .replace(/Maak een permanente link/gi, "")
    .replace(/Toon wetstechnische informatie/gi, "")
    .replace(/Druk het regelingonderdeel af/gi, "")
    .replace(/Sla het regelingonderdeel op/gi, "")
    .replace(/\.\.\.\s+/g, "")
    .replace(/\s+/g, " ")
    .trim();
}
