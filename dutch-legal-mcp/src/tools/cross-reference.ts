/**
 * MCP tool definitions for legal cross-referencing.
 *
 * Tools:
 *   - legal_cross_reference
 *
 * This tool combines results from multiple APIs to find related
 * case law and EU regulations for a given Dutch law article reference.
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as rechtspraak from "../clients/rechtspraak.js";
import * as eurlex from "../clients/eurlex.js";
import * as koopSru from "../clients/koop-sru.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const legalCrossReferenceTool: Tool = {
  name: "legal_cross_reference",
  description:
    "Find related case law and EU regulations for a given Dutch law article reference. " +
    "Cross-references Rechtspraak.nl case law with EUR-Lex EU legislation. " +
    "Provide an article reference like 'Artikel 6:162 BW' or a BWB-ID with article number.",
  inputSchema: {
    type: "object" as const,
    properties: {
      articleReference: {
        type: "string",
        description:
          "Article reference in natural language. Examples: 'Artikel 6:162 BW', " +
          "'Art. 7:610 Burgerlijk Wetboek', 'Artikel 1 Grondwet'.",
      },
      bwbId: {
        type: "string",
        description:
          "Optional BWB-ID for more precise lookup. Example: 'BWBR0005289'.",
      },
      articleNumber: {
        type: "string",
        description:
          "Optional article number for more precise lookup. Example: '6:162'.",
      },
      includeEuLaw: {
        type: "boolean",
        description:
          "Whether to search for related EU regulations (default: true).",
      },
      maxCaseLaw: {
        type: "number",
        description:
          "Maximum number of related case law results (default: 5).",
      },
      maxEuLaw: {
        type: "number",
        description:
          "Maximum number of related EU law results (default: 3).",
      },
    },
    required: ["articleReference"],
  },
};

// ── Tool Handler ────────────────────────────────────────────────────

interface CrossReferenceResult {
  articleReference: string;
  legislationInfo: {
    bwbId?: string;
    articleNumber?: string;
    title?: string;
    text?: string;
  } | null;
  relatedCaseLaw: Array<{
    ecli: string;
    title: string;
    summary: string;
    date: string;
    court: string;
  }>;
  relatedEuLaw: Array<{
    celexNumber: string;
    title: string;
    date: string;
    type: string;
    eurLexUrl: string;
  }>;
}

export async function handleLegalCrossReference(
  args: Record<string, unknown>,
): Promise<string> {
  const articleReference = String(args.articleReference);
  const bwbId = args.bwbId ? String(args.bwbId) : undefined;
  const articleNumber = args.articleNumber ? String(args.articleNumber) : undefined;
  const includeEuLaw = args.includeEuLaw !== false;
  const maxCaseLaw = args.maxCaseLaw ? Number(args.maxCaseLaw) : 5;
  const maxEuLaw = args.maxEuLaw ? Number(args.maxEuLaw) : 3;

  const result: CrossReferenceResult = {
    articleReference,
    legislationInfo: null,
    relatedCaseLaw: [],
    relatedEuLaw: [],
  };

  // Extract search terms from the article reference for case law search
  const searchTerms = extractSearchTerms(articleReference);

  // Run all lookups concurrently
  const promises: Promise<void>[] = [];

  // 1. Get the article text if BWB-ID and article number are provided
  if (bwbId && articleNumber) {
    promises.push(
      koopSru
        .getArticle(bwbId, articleNumber)
        .then((article) => {
          result.legislationInfo = {
            bwbId: article.bwbId,
            articleNumber: article.articleNumber,
            title: article.title,
            text: article.text.slice(0, 2000), // Limit text length
          };
        })
        .catch(() => {
          result.legislationInfo = {
            bwbId,
            articleNumber,
            title: articleReference,
          };
        }),
    );
  }

  // 2. Search related case law on Rechtspraak.nl
  promises.push(
    rechtspraak
      .searchCaseLaw({
        query: searchTerms,
        max: maxCaseLaw,
      })
      .then((caseLawResults) => {
        result.relatedCaseLaw = caseLawResults.results.map((r) => ({
          ecli: r.ecli,
          title: r.title,
          summary: r.summary,
          date: r.issued,
          court: r.court,
        }));
      })
      .catch((err) => {
        result.relatedCaseLaw = [
          {
            ecli: "",
            title: `Error searching case law: ${err instanceof Error ? err.message : "Unknown error"}`,
            summary: "",
            date: "",
            court: "",
          },
        ];
      }),
  );

  // 3. Search related EU legislation (if enabled)
  if (includeEuLaw) {
    const euSearchTerms = extractEuSearchTerms(articleReference);
    if (euSearchTerms) {
      promises.push(
        eurlex
          .searchRegulations(euSearchTerms, maxEuLaw)
          .then((euResults) => {
            result.relatedEuLaw = euResults;
          })
          .catch((err) => {
            result.relatedEuLaw = [
              {
                celexNumber: "",
                title: `Error searching EU law: ${err instanceof Error ? err.message : "Unknown error"}`,
                date: "",
                type: "",
                eurLexUrl: "",
              },
            ];
          }),
      );
    }
  }

  await Promise.all(promises);

  return JSON.stringify(result, null, 2);
}

// ── Helpers ─────────────────────────────────────────────────────────

/**
 * Extract meaningful search terms from a Dutch article reference.
 */
function extractSearchTerms(reference: string): string {
  // Common Dutch legal abbreviations to expand for search
  const expansions: Record<string, string> = {
    BW: "Burgerlijk Wetboek",
    WvSr: "Wetboek van Strafrecht",
    WvSv: "Wetboek van Strafvordering",
    Gw: "Grondwet",
    Awb: "Algemene wet bestuursrecht",
    WOR: "Wet op de ondernemingsraden",
    WVW: "Wegenverkeerswet",
  };

  let terms = reference;

  // Replace abbreviations with full names
  for (const [abbrev, full] of Object.entries(expansions)) {
    const regex = new RegExp(`\\b${abbrev}\\b`, "g");
    terms = terms.replace(regex, full);
  }

  // Remove "Artikel", "Art.", etc. as they are noise for case law search
  terms = terms.replace(/\b(Artikel|Art\.?)\b/gi, "").trim();

  return terms;
}

/**
 * Extract EU-relevant search terms from a Dutch article reference.
 * Returns null if the reference is unlikely to have EU connections.
 */
function extractEuSearchTerms(reference: string): string | null {
  // Map Dutch legal concepts to EU law search terms
  const euMappings: Array<{ pattern: RegExp; euTerm: string }> = [
    {
      pattern: /privacy|persoonsgegevens|AVG|GDPR/i,
      euTerm: "data protection",
    },
    {
      pattern: /consument|koop|garantie/i,
      euTerm: "consumer rights",
    },
    {
      pattern: /arbeid|werknem|ontslag/i,
      euTerm: "employment workers",
    },
    {
      pattern: /mededinging|kartel|monopol/i,
      euTerm: "competition",
    },
    {
      pattern: /milieu|klimaat|emissie/i,
      euTerm: "environment",
    },
    {
      pattern: /aanbesteding|procurement/i,
      euTerm: "public procurement",
    },
    {
      pattern: /financ|bank|verzeker/i,
      euTerm: "financial services",
    },
    {
      pattern: /intellectueel|auteur|octrooi|patent|merk/i,
      euTerm: "intellectual property",
    },
    {
      pattern: /transport|vervoer/i,
      euTerm: "transport",
    },
    {
      pattern: /handels|import|export|douane/i,
      euTerm: "trade",
    },
  ];

  for (const mapping of euMappings) {
    if (mapping.pattern.test(reference)) {
      return mapping.euTerm;
    }
  }

  // Generic fallback: use the reference itself (cleaned up)
  const cleaned = reference
    .replace(/\b(Artikel|Art\.?|BW|WvSr|Gw|Awb)\b/gi, "")
    .replace(/[:\d]+/g, "")
    .trim();

  return cleaned.length > 3 ? cleaned : null;
}
