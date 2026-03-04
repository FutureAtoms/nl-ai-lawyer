/**
 * EUR-Lex SPARQL client
 *
 * Queries the EUR-Lex SPARQL endpoint for EU legislation
 * (directives, regulations, decisions) relevant to Dutch law.
 *
 * SPARQL endpoint: https://publications.europa.eu/webapi/rdf/sparql
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";

const SPARQL_ENDPOINT = "https://publications.europa.eu/webapi/rdf/sparql";
const BACKEND = "eurlex";

export interface EurLexSearchResult {
  celexNumber: string;
  title: string;
  date: string;
  type: string;
  eurLexUrl: string;
}

export interface EurLexAct {
  celexNumber: string;
  title: string;
  date: string;
  type: string;
  subject: string;
  text: string;
  eurLexUrl: string;
  inForce: boolean;
}

/**
 * Execute a SPARQL query against the EUR-Lex endpoint.
 */
async function sparqlQuery(query: string): Promise<SparqlResult> {
  const params = new URLSearchParams({
    query,
    format: "application/sparql-results+json",
  });

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(SPARQL_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      Accept: "application/sparql-results+json",
    },
    body: params.toString(),
  });

  if (!response.ok) {
    const body = await response.text().catch(() => "");
    throw new Error(
      `EUR-Lex SPARQL query failed (${response.status}): ${response.statusText}. ${body}`,
    );
  }

  return response.json() as Promise<SparqlResult>;
}

interface SparqlResult {
  results: {
    bindings: Array<Record<string, { type: string; value: string }>>;
  };
}

/**
 * Extract a string value from a SPARQL binding.
 */
function bindingValue(
  binding: Record<string, { type: string; value: string }>,
  key: string,
): string {
  return binding[key]?.value ?? "";
}

/**
 * Search EU regulations and directives by keyword.
 */
export async function searchRegulations(
  query: string,
  maxResults: number = 10,
): Promise<EurLexSearchResult[]> {
  const cacheKey = MultiTierCache.key("eurlex-search", query, maxResults);
  const cached = cache.get<EurLexSearchResult[]>("search_results", cacheKey);
  if (cached) return cached;

  // Escape single quotes in the search term
  const escapedQuery = query.replace(/'/g, "\\'");

  const sparql = `
    PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT DISTINCT
      ?celexNumber
      ?title
      ?date
      ?type
      ?work
    WHERE {
      ?work cdm:work_has_resource-type ?type .
      ?work cdm:resource_legal_id_celex ?celexNumber .

      OPTIONAL { ?work cdm:work_date_document ?date . }

      ?exp cdm:expression_belongs_to_work ?work .
      ?exp cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
      ?exp cdm:expression_title ?title .

      FILTER(
        CONTAINS(LCASE(?title), LCASE('${escapedQuery}'))
      )

      FILTER(
        ?type IN (
          <http://publications.europa.eu/resource/authority/resource-type/REG>,
          <http://publications.europa.eu/resource/authority/resource-type/DIR>,
          <http://publications.europa.eu/resource/authority/resource-type/DEC>
        )
      )
    }
    ORDER BY DESC(?date)
    LIMIT ${maxResults}
  `;

  const data = await sparqlQuery(sparql);

  const results: EurLexSearchResult[] = data.results.bindings.map(
    (binding) => {
      const celex = bindingValue(binding, "celexNumber");
      const rawType = bindingValue(binding, "type");
      return {
        celexNumber: celex,
        title: bindingValue(binding, "title"),
        date: bindingValue(binding, "date"),
        type: mapResourceType(rawType),
        eurLexUrl: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:${encodeURIComponent(celex)}`,
      };
    },
  );

  cache.set("search_results", cacheKey, results);
  return results;
}

/**
 * Get detailed information about an EU act by CELEX number.
 */
export async function getAct(celexNumber: string): Promise<EurLexAct> {
  const cacheKey = MultiTierCache.key("eurlex-act", celexNumber);
  const cached = cache.get<EurLexAct>("legislation", cacheKey);
  if (cached) return cached;

  const escapedCelex = celexNumber.replace(/'/g, "\\'");

  const sparql = `
    PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT DISTINCT
      ?celexNumber
      ?title
      ?date
      ?type
      ?subject
      ?inForce
    WHERE {
      ?work cdm:resource_legal_id_celex '${escapedCelex}' .
      ?work cdm:resource_legal_id_celex ?celexNumber .
      ?work cdm:work_has_resource-type ?type .

      OPTIONAL { ?work cdm:work_date_document ?date . }
      OPTIONAL { ?work cdm:resource_legal_in-force ?inForce . }

      ?exp cdm:expression_belongs_to_work ?work .
      ?exp cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
      ?exp cdm:expression_title ?title .

      OPTIONAL {
        ?work cdm:work_is_about_concept_eurovoc ?subjectUri .
        ?subjectUri cdm:subject_heading_label ?subject .
        FILTER(LANG(?subject) = 'en')
      }
    }
    LIMIT 1
  `;

  const data = await sparqlQuery(sparql);
  const binding = data.results.bindings[0];

  if (!binding) {
    throw new Error(`EUR-Lex act not found: ${celexNumber}`);
  }

  // Attempt to get the full text via the EUR-Lex HTML endpoint
  let text = "";
  try {
    const textUrl = `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:${encodeURIComponent(celexNumber)}`;
    await rateLimiter.acquire(BACKEND);
    const textResponse = await fetch(textUrl, {
      headers: { Accept: "text/html" },
    });
    if (textResponse.ok) {
      const html = await textResponse.text();
      text = extractTextFromHtml(html);
    }
  } catch {
    // Full text retrieval is best-effort
    text = "[Full text could not be retrieved. Use the EUR-Lex URL to view the document.]";
  }

  const inForceVal = bindingValue(binding, "inForce");

  const result: EurLexAct = {
    celexNumber: bindingValue(binding, "celexNumber"),
    title: bindingValue(binding, "title"),
    date: bindingValue(binding, "date"),
    type: mapResourceType(bindingValue(binding, "type")),
    subject: bindingValue(binding, "subject"),
    text: text || "[No full text available]",
    eurLexUrl: `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:${encodeURIComponent(celexNumber)}`,
    inForce:
      inForceVal === "true" ||
      inForceVal === "1" ||
      inForceVal.toLowerCase().includes("force"),
  };

  cache.set("legislation", cacheKey, result);
  return result;
}

// ── Helpers ─────────────────────────────────────────────────────────

/**
 * Map EUR-Lex resource type URIs to human-readable labels.
 */
function mapResourceType(uri: string): string {
  if (uri.includes("REG")) return "Regulation";
  if (uri.includes("DIR")) return "Directive";
  if (uri.includes("DEC")) return "Decision";
  if (uri.includes("RECOM")) return "Recommendation";
  if (uri.includes("OPI")) return "Opinion";
  return uri.split("/").pop() ?? uri;
}

/**
 * Simple HTML-to-text extraction for EUR-Lex pages.
 */
function extractTextFromHtml(html: string): string {
  // Try to extract just the document body / main content
  const bodyMatch = html.match(
    /<div[^>]*id="TexteOnly"[^>]*>([\s\S]*?)<\/div>/i,
  );
  const content = bodyMatch ? bodyMatch[1] : html;

  return content
    .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "")
    .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, "")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, 10000); // Limit text length
}
