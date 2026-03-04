/**
 * XML-to-JSON transformation utilities for Rechtspraak.nl and KOOP SRU
 * responses using fast-xml-parser.
 */

import { XMLParser, type X2jOptions } from "fast-xml-parser";

/** Shared parser options for Dutch legal XML. */
const COMMON_OPTIONS: Partial<X2jOptions> = {
  ignoreAttributes: false,
  attributeNamePrefix: "@_",
  textNodeName: "#text",
  trimValues: true,
  parseAttributeValue: false,
  isArray: (name: string) => {
    // Force certain elements to always be arrays for consistency
    const alwaysArray = [
      "record",
      "result",
      "uitspraak",
      "conclusie",
      "subject",
      "relation",
      "identifier",
      "description",
      "creator",
      "hasVersion",
      "article",
      "dcterms:subject",
      "dcterms:relation",
      "dcterms:identifier",
      "dcterms:hasVersion",
      "psi:zpitnr",
    ];
    return alwaysArray.includes(name);
  },
};

const parser = new XMLParser(COMMON_OPTIONS);

/**
 * Parse a raw XML string into a plain JS object.
 */
export function parseXml<T = Record<string, unknown>>(xml: string): T {
  return parser.parse(xml) as T;
}

/**
 * Transform a Rechtspraak.nl search result XML document into a clean
 * JSON structure with an array of results.
 */
export function transformRechtspraakSearch(xml: string): {
  totalResults: number;
  results: RechtspraakSearchResult[];
} {
  const parsed = parseXml(xml);
  const feed = extractPath(parsed, ["feed"]) ?? parsed;

  const totalResults = Number(
    extractPath(feed, ["openSearch:totalResults"]) ??
      extractPath(feed, ["totalResults"]) ??
      0,
  );

  const entries = ensureArray(
    extractPath(feed, ["entry"]) ?? [],
  );

  const results: RechtspraakSearchResult[] = entries.map((e) => {
    const entry = e as Record<string, unknown>;
    return {
    ecli: extractText(entry, ["id"]) ?? "",
    title: extractText(entry, ["title"]) ?? "",
    summary: extractText(entry, ["summary"]) ?? "",
    issued: extractText(entry, ["updated"]) ?? extractText(entry, ["published"]) ?? "",
    court: extractText(entry, ["court"]) ?? "",
    link: typeof entry["link"] === "object" && entry["link"] !== null
      ? (entry["link"] as Record<string, string>)["@_href"] ?? ""
      : "",
  };
  });

  return { totalResults, results };
}

export interface RechtspraakSearchResult {
  ecli: string;
  title: string;
  summary: string;
  issued: string;
  court: string;
  link: string;
}

/**
 * Transform a Rechtspraak.nl full-text ruling XML into a clean structure.
 */
export function transformRechtspraakRuling(xml: string): {
  ecli: string;
  type: string;
  creator: string;
  date: string;
  subject: string;
  description: string;
  bodyText: string;
} {
  const parsed = parseXml(xml);
  const root =
    extractPath(parsed, ["open-rechtspraak"]) ??
    extractPath(parsed, ["uitspraak"]) ??
    extractPath(parsed, ["conclusie"]) ??
    parsed;

  // RDF metadata block
  const rdf =
    extractPath(root, ["rdf:RDF", "rdf:Description"]) ??
    extractPath(root, ["RDF", "Description"]) ??
    {};

  const meta = Array.isArray(rdf) ? rdf[0] ?? {} : rdf;

  // Body text - try multiple paths
  const bodySection =
    extractPath(root, ["uitspraak"]) ??
    extractPath(root, ["conclusie"]) ??
    {};

  let bodyText = "";
  if (typeof bodySection === "string") {
    bodyText = bodySection;
  } else if (typeof bodySection === "object" && bodySection !== null) {
    bodyText = extractAllText(bodySection as Record<string, unknown>);
  }

  return {
    ecli: extractText(meta as Record<string, unknown>, ["dcterms:identifier", "identifier"]) ?? "",
    type: extractText(meta as Record<string, unknown>, ["dcterms:type", "type"]) ?? "",
    creator: extractText(meta as Record<string, unknown>, ["dcterms:creator", "creator"]) ?? "",
    date: extractText(meta as Record<string, unknown>, ["dcterms:date", "date"]) ?? "",
    subject: extractText(meta as Record<string, unknown>, ["dcterms:subject", "subject"]) ?? "",
    description: extractText(meta as Record<string, unknown>, ["dcterms:description", "description"]) ?? "",
    bodyText: bodyText.trim(),
  };
}

/**
 * Transform a KOOP SRU search result XML into a clean structure.
 */
export function transformKoopSruSearch(xml: string): {
  totalResults: number;
  results: KoopSearchResult[];
} {
  const parsed = parseXml(xml);
  const searchRetrieveResponse =
    extractPath(parsed, ["searchRetrieveResponse"]) ??
    extractPath(parsed, ["srw:searchRetrieveResponse"]) ??
    extractPath(parsed, ["zs:searchRetrieveResponse"]) ??
    parsed;

  const totalResults = Number(
    extractPath(searchRetrieveResponse, ["numberOfRecords"]) ??
      extractPath(searchRetrieveResponse, ["srw:numberOfRecords"]) ??
      extractPath(searchRetrieveResponse, ["zs:numberOfRecords"]) ??
      0,
  );

  const records = ensureArray(
    extractPath(searchRetrieveResponse, ["records", "record"]) ??
      extractPath(searchRetrieveResponse, ["srw:records", "srw:record"]) ??
      extractPath(searchRetrieveResponse, ["zs:records", "zs:record"]) ??
      [],
  );

  const results: KoopSearchResult[] = records.map((rec) => {
    const record = rec as Record<string, unknown>;
    const data =
      extractPath(record, ["recordData"]) ??
      extractPath(record, ["srw:recordData"]) ??
      record;

    const gzd =
      extractPath(data as Record<string, unknown>, ["gzd"]) ??
      extractPath(data as Record<string, unknown>, ["overheidwetgeving:gzd"]) ??
      data;

    const meta = (gzd as Record<string, unknown>) ?? {};

    // SRU 1.2 nests under originalData > overheidbwb:meta > owmskern
    const owmskern =
      extractPath(meta, ["originalData", "owmskern"]) ??
      extractPath(meta, ["originalData", "overheidbwb:meta", "owmskern"]) ??
      {};

    const kern = owmskern as Record<string, unknown>;

    return {
      bwbId:
        extractText(kern, ["dcterms:identifier"]) ??
        extractText(meta, ["originalData", "owmskern:identifier"]) ??
        extractText(meta, ["identifier"]) ??
        "",
      title:
        extractText(kern, ["dcterms:title"]) ??
        extractText(meta, ["originalData", "owmskern:title"]) ??
        extractText(meta, ["title"]) ??
        "",
      type:
        extractText(kern, ["dcterms:type"]) ??
        extractText(meta, ["originalData", "owmskern:type"]) ??
        extractText(meta, ["type"]) ??
        "",
      creator:
        extractText(kern, ["dcterms:creator"]) ??
        extractText(meta, ["originalData", "owmskern:creator"]) ??
        extractText(meta, ["creator"]) ??
        "",
      modified:
        extractText(kern, ["dcterms:modified"]) ??
        extractText(meta, ["enrichedData", "modified"]) ??
        extractText(meta, ["modified"]) ??
        "",
    };
  });

  return { totalResults, results };
}

export interface KoopSearchResult {
  bwbId: string;
  title: string;
  type: string;
  creator: string;
  modified: string;
}

// ── Helpers ─────────────────────────────────────────────────────────

/**
 * Safely traverse a nested object by a sequence of keys.
 * Tries each key in `keys` at the current level and returns the first match.
 */
function extractPath(
  obj: unknown,
  keys: string[],
): unknown {
  let current: unknown = obj;
  for (const key of keys) {
    if (current == null || typeof current !== "object") return undefined;
    const rec = current as Record<string, unknown>;
    if (key in rec) {
      current = rec[key];
    } else {
      return undefined;
    }
  }
  return current;
}

/**
 * Try multiple keys on an object and return the first truthy text value.
 */
function extractText(
  obj: Record<string, unknown>,
  keys: string[],
): string | undefined {
  for (const key of keys) {
    const val = obj[key];
    if (val == null) continue;
    if (typeof val === "string") return val;
    if (typeof val === "number") return String(val);
    if (typeof val === "object") {
      const inner = (val as Record<string, unknown>)["#text"];
      if (inner != null) return String(inner);
      // Recurse into first element if array
      if (Array.isArray(val) && val.length > 0) {
        const first = val[0];
        if (typeof first === "string") return first;
        if (typeof first === "object" && first !== null) {
          const t = (first as Record<string, unknown>)["#text"];
          if (t != null) return String(t);
        }
      }
    }
  }
  return undefined;
}

/**
 * Recursively extract all #text values from an object tree and
 * concatenate them with newlines.
 */
function extractAllText(obj: Record<string, unknown>): string {
  const parts: string[] = [];

  function walk(node: unknown): void {
    if (node == null) return;
    if (typeof node === "string") {
      parts.push(node);
      return;
    }
    if (typeof node === "number") {
      parts.push(String(node));
      return;
    }
    if (Array.isArray(node)) {
      for (const item of node) walk(item);
      return;
    }
    if (typeof node === "object") {
      const rec = node as Record<string, unknown>;
      if ("#text" in rec) {
        parts.push(String(rec["#text"]));
      }
      for (const [key, val] of Object.entries(rec)) {
        if (key.startsWith("@_")) continue; // skip attributes
        if (key === "#text") continue; // already handled
        walk(val);
      }
    }
  }

  walk(obj);
  return parts.join("\n");
}

/**
 * Ensure a value is an array.
 */
function ensureArray<T>(val: T | T[]): T[] {
  if (Array.isArray(val)) return val;
  if (val == null) return [];
  return [val];
}
