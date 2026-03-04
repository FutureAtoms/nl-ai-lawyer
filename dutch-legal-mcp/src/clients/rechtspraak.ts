/**
 * Rechtspraak.nl API client
 *
 * Wraps the official Rechtspraak open-data API for searching and
 * retrieving Dutch case law (uitspraken & conclusies).
 *
 * Base URL: https://data.rechtspraak.nl
 * Docs: https://www.rechtspraak.nl/Uitspraken/paginas/open-data.aspx
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";
import {
  parseXml,
  transformRechtspraakSearch,
  transformRechtspraakRuling,
  type RechtspraakSearchResult,
} from "../utils/xml-transform.js";

const BASE_URL = "https://data.rechtspraak.nl";
const BACKEND = "rechtspraak";

export interface CaseLawSearchFilters {
  /** Free-text query */
  query?: string;
  /** Court identifier, e.g. "Hoge Raad" */
  court?: string;
  /** Legal subject area */
  subject?: string;
  /** Date range start (YYYY-MM-DD) */
  dateFrom?: string;
  /** Date range end (YYYY-MM-DD) */
  dateTo?: string;
  /** Maximum number of results (default 10, max 1000) */
  max?: number;
  /** Offset for pagination */
  offset?: number;
}

export interface CaseLawSearchResponse {
  totalResults: number;
  results: RechtspraakSearchResult[];
}

export interface RulingContent {
  ecli: string;
  type: string;
  creator: string;
  date: string;
  subject: string;
  description: string;
  bodyText: string;
}

export interface RulingMetadata {
  ecli: string;
  type: string;
  creator: string;
  date: string;
  subject: string;
  description: string;
  procedure: string;
  references: string[];
}

/**
 * Search case law on Rechtspraak.nl.
 *
 * The search endpoint returns an Atom feed XML which we parse into JSON.
 */
export async function searchCaseLaw(
  filters: CaseLawSearchFilters,
): Promise<CaseLawSearchResponse> {
  const cacheKey = MultiTierCache.key(
    "rs-search",
    filters.query,
    filters.court,
    filters.subject,
    filters.dateFrom,
    filters.dateTo,
    filters.max,
    filters.offset,
  );
  const cached = cache.get<CaseLawSearchResponse>("search_results", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams();
  if (filters.query) params.set("q", filters.query);
  if (filters.court) params.set("creator", filters.court);
  if (filters.subject) params.set("subject", filters.subject);
  if (filters.dateFrom) params.set("date", `>=${filters.dateFrom}`);
  if (filters.dateTo) {
    const existing = params.get("date");
    if (existing) {
      // Rechtspraak supports date range via two params
      params.set("date", `${existing}&date=<=${filters.dateTo}`);
    } else {
      params.set("date", `<=${filters.dateTo}`);
    }
  }
  params.set("max", String(filters.max ?? 10));
  if (filters.offset) params.set("from", String(filters.offset));
  // Return type = Uitspraak by default
  params.set("return", "DOC");

  const url = `${BASE_URL}/uitspraken/zoeken?${params.toString()}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    throw new Error(
      `Rechtspraak search failed (${response.status}): ${response.statusText}`,
    );
  }

  const xml = await response.text();
  const result = transformRechtspraakSearch(xml);

  cache.set("search_results", cacheKey, result);
  return result;
}

/**
 * Get the full text of a ruling by ECLI identifier.
 */
export async function getRuling(ecli: string): Promise<RulingContent> {
  const cacheKey = MultiTierCache.key("rs-ruling", ecli);
  const cached = cache.get<RulingContent>("caselaw_fulltext", cacheKey);
  if (cached) return cached;

  const url = `${BASE_URL}/uitspraken/content?id=${encodeURIComponent(ecli)}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    throw new Error(
      `Rechtspraak ruling fetch failed (${response.status}): ${response.statusText}`,
    );
  }

  const xml = await response.text();
  const result = transformRechtspraakRuling(xml);

  cache.set("caselaw_fulltext", cacheKey, result);
  return result;
}

/**
 * Extract metadata from a ruling (without full body text).
 */
export async function getMetadata(ecli: string): Promise<RulingMetadata> {
  const cacheKey = MultiTierCache.key("rs-meta", ecli);
  const cached = cache.get<RulingMetadata>("search_results", cacheKey);
  if (cached) return cached;

  const url = `${BASE_URL}/uitspraken/content?id=${encodeURIComponent(ecli)}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: { Accept: "application/xml" },
  });

  if (!response.ok) {
    throw new Error(
      `Rechtspraak metadata fetch failed (${response.status}): ${response.statusText}`,
    );
  }

  const xml = await response.text();
  const parsed = parseXml(xml);

  // Navigate to the RDF description for metadata
  const root =
    getNestedValue(parsed, "open-rechtspraak") ?? parsed;
  const rdfBlock =
    getNestedValue(root, "rdf:RDF") ??
    getNestedValue(root, "RDF") ??
    {};
  const descriptions = getNestedValue(rdfBlock, "rdf:Description") ??
    getNestedValue(rdfBlock, "Description") ??
    {};
  const desc = Array.isArray(descriptions) ? descriptions[0] ?? {} : descriptions;

  const meta: RulingMetadata = {
    ecli: textOf(desc, "dcterms:identifier") ?? ecli,
    type: textOf(desc, "dcterms:type") ?? "",
    creator: textOf(desc, "dcterms:creator") ?? "",
    date: textOf(desc, "dcterms:date") ?? "",
    subject: textOf(desc, "dcterms:subject") ?? "",
    description: textOf(desc, "dcterms:description") ?? "",
    procedure: textOf(desc, "dcterms:procedure") ?? textOf(desc, "psi:procedure") ?? "",
    references: extractArrayTexts(desc, "dcterms:relation"),
  };

  cache.set("search_results", cacheKey, meta);
  return meta;
}

// ── Internal helpers ────────────────────────────────────────────────

function getNestedValue(obj: unknown, key: string): unknown {
  if (obj == null || typeof obj !== "object") return undefined;
  return (obj as Record<string, unknown>)[key];
}

function textOf(obj: unknown, key: string): string | undefined {
  if (obj == null || typeof obj !== "object") return undefined;
  const val = (obj as Record<string, unknown>)[key];
  if (val == null) return undefined;
  if (typeof val === "string") return val;
  if (typeof val === "number") return String(val);
  if (typeof val === "object" && val !== null) {
    const t = (val as Record<string, unknown>)["#text"];
    if (t != null) return String(t);
    if (Array.isArray(val) && val.length > 0) {
      const first = val[0];
      if (typeof first === "string") return first;
      if (typeof first === "object" && first !== null) {
        const ft = (first as Record<string, unknown>)["#text"];
        if (ft != null) return String(ft);
      }
    }
  }
  return undefined;
}

function extractArrayTexts(obj: unknown, key: string): string[] {
  if (obj == null || typeof obj !== "object") return [];
  const val = (obj as Record<string, unknown>)[key];
  if (val == null) return [];
  const arr = Array.isArray(val) ? val : [val];
  return arr
    .map((item) => {
      if (typeof item === "string") return item;
      if (typeof item === "object" && item !== null) {
        const t = (item as Record<string, unknown>)["#text"] ??
          (item as Record<string, unknown>)["@_resourceIdentifier"];
        return t != null ? String(t) : null;
      }
      return null;
    })
    .filter((x): x is string => x !== null);
}
