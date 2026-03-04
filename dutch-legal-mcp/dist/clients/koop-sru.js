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
import { parseXml, transformKoopSruSearch, } from "../utils/xml-transform.js";
// SRU endpoint moved from repository.overheid.nl to zoekservice.overheid.nl (2025)
const SRU_BASE_URL = "https://zoekservice.overheid.nl";
const SRU_PATH = "/sru/Search";
const WETTEN_BASE_URL = "https://wetten.overheid.nl";
const BACKEND = "koopSru";
/**
 * Build a CQL (Contextual Query Language) query for the KOOP SRU endpoint.
 */
function buildCqlQuery(params) {
    const parts = [];
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
export async function searchLegislation(params) {
    const cacheKey = MultiTierCache.key("koop-search", params.query, params.area, params.dateFrom, params.dateTo, params.max, params.startRecord);
    const cached = cache.get("search_results", cacheKey);
    if (cached)
        return cached;
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
        throw new Error(`KOOP SRU search failed (${response.status}): ${response.statusText}`);
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
export async function getArticle(bwbId, articleNumber) {
    const cacheKey = MultiTierCache.key("koop-article", bwbId, articleNumber);
    const cached = cache.get("legislation", cacheKey);
    if (cached)
        return cached;
    // Primary: Fetch from wetten.overheid.nl HTML (reliable, always has current version)
    await rateLimiter.acquire(BACKEND);
    const wettenUrl = `${WETTEN_BASE_URL}/${encodeURIComponent(bwbId)}`;
    const response = await fetch(wettenUrl, {
        headers: { Accept: "text/html" },
        redirect: "follow",
    });
    if (response.ok) {
        const html = await response.text();
        const articleText = extractArticleFromHtml(html, articleNumber);
        if (articleText) {
            const result = {
                bwbId,
                articleNumber,
                title: `Artikel ${articleNumber}`,
                text: articleText,
            };
            cache.set("legislation", cacheKey, result);
            return result;
        }
    }
    throw new Error(`Article fetch failed: Could not retrieve article ${articleNumber} from ${bwbId}. wetten.overheid.nl returned ${response.status}.`);
}
/**
 * Get version history for a law identified by BWB-ID.
 */
export async function getVersions(bwbId) {
    const cacheKey = MultiTierCache.key("koop-versions", bwbId);
    const cached = cache.get("legislation", cacheKey);
    if (cached)
        return cached;
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
        throw new Error(`KOOP version history fetch failed (${response.status}): ${response.statusText}`);
    }
    const xml = await response.text();
    const parsed = parseXml(xml);
    // Extract version entries from the SRU response (handles both SRU 1.2 and 2.0 namespace variants)
    const sruResponse = getNestedProp(parsed, "searchRetrieveResponse") ??
        getNestedProp(parsed, "srw:searchRetrieveResponse") ??
        getNestedProp(parsed, "zs:searchRetrieveResponse") ??
        parsed;
    const records = ensureArray(getNestedProp(sruResponse, "records", "record") ??
        getNestedProp(sruResponse, "srw:records", "srw:record") ??
        getNestedProp(sruResponse, "zs:records", "zs:record") ??
        []);
    const versions = records.map((rec) => {
        const record = rec;
        const data = getNestedProp(record, "recordData") ??
            getNestedProp(record, "srw:recordData") ??
            record;
        const gzd = getNestedProp(data, "gzd") ?? data;
        const enriched = getNestedProp(gzd, "enrichedData") ?? {};
        return {
            date: textOf(enriched, "geldigheidsperiode_start") ??
                textOf(enriched, "modified") ?? "",
            label: textOf(gzd, "originalData", "owmskern:title") ??
                textOf(gzd, "title") ?? bwbId,
            url: textOf(enriched, "preferred_url") ?? "",
        };
    });
    const result = { bwbId, versions };
    cache.set("legislation", cacheKey, result);
    return result;
}
// ── Internal helpers ────────────────────────────────────────────────
function getNestedProp(obj, ...keys) {
    let current = obj;
    for (const key of keys) {
        if (current == null || typeof current !== "object")
            return undefined;
        current = current[key];
    }
    return current;
}
function textOf(obj, ...keys) {
    const val = getNestedProp(obj, ...keys);
    if (val == null)
        return undefined;
    if (typeof val === "string")
        return val;
    if (typeof val === "number")
        return String(val);
    if (typeof val === "object" && val !== null) {
        const t = val["#text"];
        if (t != null)
            return String(t);
    }
    return undefined;
}
function ensureArray(val) {
    if (Array.isArray(val))
        return val;
    if (val == null)
        return [];
    return [val];
}
function findArticleContent(parsed, articleNumber) {
    // Try to find the article element in the parsed XML
    const allText = collectText(parsed);
    return {
        title: `Artikel ${articleNumber}`,
        text: allText || `Article ${articleNumber} content from parsed XML`,
    };
}
function collectText(obj) {
    if (obj == null)
        return "";
    if (typeof obj === "string")
        return obj;
    if (typeof obj === "number")
        return String(obj);
    if (Array.isArray(obj))
        return obj.map(collectText).join("\n");
    if (typeof obj === "object") {
        const parts = [];
        for (const [key, val] of Object.entries(obj)) {
            if (key.startsWith("@_"))
                continue;
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
function extractArticleFromHtml(html, articleNumber) {
    const normalizedArt = articleNumber.includes(":")
        ? articleNumber.split(":").pop()
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
            if (text.length > 20)
                return text;
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
        if (articleText.length > 30)
            return cleanWettenUiNoise(articleText.trim());
    }
    return null;
}
function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
/**
 * Remove wetten.nl UI noise from extracted text (navigation hints, buttons, etc.)
 */
function cleanWettenUiNoise(text) {
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
//# sourceMappingURL=koop-sru.js.map