/**
 * MCP tool definitions for Dutch legislation.
 *
 * Tools:
 *   - legislation_search
 *   - legislation_get_article
 *   - legislation_versions
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as koopSru from "../clients/koop-sru.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const legislationSearchTool: Tool = {
  name: "legislation_search",
  description:
    "Search Dutch legislation (wetten, besluiten, regelingen) by keyword, legal area, and/or date range. " +
    "Uses the KOOP SRU API to search BWB (Basis Wetten Bestand) documents on repository.overheid.nl.",
  inputSchema: {
    type: "object" as const,
    properties: {
      query: {
        type: "string",
        description:
          "Search query (keywords). Examples: 'huurrecht', 'Burgerlijk Wetboek', 'arbeidsovereenkomst'.",
      },
      area: {
        type: "string",
        description:
          "Legal area filter. Examples: 'staatsrecht', 'strafrecht', 'burgerlijk recht', 'bestuursrecht'.",
      },
      dateFrom: {
        type: "string",
        description: "Filter for legislation valid from this date (YYYY-MM-DD).",
      },
      dateTo: {
        type: "string",
        description: "Filter for legislation valid until this date (YYYY-MM-DD).",
      },
      max: {
        type: "number",
        description: "Maximum number of results to return (default: 10).",
      },
    },
    required: ["query"],
  },
};

export const legislationGetArticleTool: Tool = {
  name: "legislation_get_article",
  description:
    "Get a specific article from Dutch legislation by BWB-ID and article number. " +
    "For example, retrieve Article 7:610 from the Burgerlijk Wetboek.",
  inputSchema: {
    type: "object" as const,
    properties: {
      bwbId: {
        type: "string",
        description:
          "The BWB identifier of the law. Example: 'BWBR0005290' for the Burgerlijk Wetboek Boek 7.",
      },
      articleNumber: {
        type: "string",
        description:
          "The article number. Examples: '610', '7:610', '1'. Can include sub-articles like '6:162'.",
      },
    },
    required: ["bwbId", "articleNumber"],
  },
};

export const legislationVersionsTool: Tool = {
  name: "legislation_versions",
  description:
    "Get the version history of a Dutch law identified by its BWB-ID. " +
    "Shows when different versions of the law were in effect.",
  inputSchema: {
    type: "object" as const,
    properties: {
      bwbId: {
        type: "string",
        description:
          "The BWB identifier of the law. Example: 'BWBR0005290'.",
      },
    },
    required: ["bwbId"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleLegislationSearch(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await koopSru.searchLegislation({
    query: String(args.query ?? ""),
    area: args.area ? String(args.area) : undefined,
    dateFrom: args.dateFrom ? String(args.dateFrom) : undefined,
    dateTo: args.dateTo ? String(args.dateTo) : undefined,
    max: args.max ? Number(args.max) : 10,
  });

  return JSON.stringify(
    {
      totalResults: result.totalResults,
      results: result.results,
    },
    null,
    2,
  );
}

export async function handleLegislationGetArticle(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await koopSru.getArticle(
    String(args.bwbId),
    String(args.articleNumber),
  );

  return JSON.stringify(result, null, 2);
}

export async function handleLegislationVersions(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await koopSru.getVersions(String(args.bwbId));

  return JSON.stringify(result, null, 2);
}
