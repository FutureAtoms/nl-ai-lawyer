/**
 * MCP tool definitions for Dutch case law.
 *
 * Tools:
 *   - caselaw_search_rechtspraak
 *   - caselaw_get_ruling
 *   - caselaw_get_metadata
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as rechtspraak from "../clients/rechtspraak.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const caselawSearchTool: Tool = {
  name: "caselaw_search_rechtspraak",
  description:
    "Search Dutch case law (rechtspraak) on Rechtspraak.nl. " +
    "Find court rulings (uitspraken) and opinions (conclusies) by keyword, court, subject, or date range.",
  inputSchema: {
    type: "object" as const,
    properties: {
      query: {
        type: "string",
        description:
          "Free-text search query. Examples: 'ontslagvergoeding', 'huurovereenkomst opzegging'.",
      },
      court: {
        type: "string",
        description:
          "Court name filter. Examples: 'Hoge Raad', 'Rechtbank Amsterdam', 'Gerechtshof Den Haag'.",
      },
      subject: {
        type: "string",
        description:
          "Legal subject/area filter. Examples: 'Civiel recht', 'Strafrecht', 'Bestuursrecht'.",
      },
      dateFrom: {
        type: "string",
        description: "Start of date range (YYYY-MM-DD).",
      },
      dateTo: {
        type: "string",
        description: "End of date range (YYYY-MM-DD).",
      },
      max: {
        type: "number",
        description: "Maximum number of results (default: 10, max: 1000).",
      },
      offset: {
        type: "number",
        description: "Offset for pagination (0-based).",
      },
    },
    required: ["query"],
  },
};

export const caselawGetRulingTool: Tool = {
  name: "caselaw_get_ruling",
  description:
    "Get the full text of a Dutch court ruling by its ECLI identifier. " +
    "Returns the complete judgment text including the court's reasoning (overwegingen) and decision (beslissing).",
  inputSchema: {
    type: "object" as const,
    properties: {
      ecli: {
        type: "string",
        description:
          "The ECLI identifier. Example: 'ECLI:NL:HR:2023:123'. " +
          "ECLI format: ECLI:NL:<court>:<year>:<number>.",
      },
    },
    required: ["ecli"],
  },
};

export const caselawGetMetadataTool: Tool = {
  name: "caselaw_get_metadata",
  description:
    "Get metadata for a Dutch court ruling by ECLI, without the full text. " +
    "Returns court, date, subject, procedure type, and cross-references.",
  inputSchema: {
    type: "object" as const,
    properties: {
      ecli: {
        type: "string",
        description: "The ECLI identifier of the ruling.",
      },
    },
    required: ["ecli"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleCaselawSearch(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await rechtspraak.searchCaseLaw({
    query: args.query ? String(args.query) : undefined,
    court: args.court ? String(args.court) : undefined,
    subject: args.subject ? String(args.subject) : undefined,
    dateFrom: args.dateFrom ? String(args.dateFrom) : undefined,
    dateTo: args.dateTo ? String(args.dateTo) : undefined,
    max: args.max ? Number(args.max) : 10,
    offset: args.offset ? Number(args.offset) : undefined,
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

export async function handleCaselawGetRuling(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await rechtspraak.getRuling(String(args.ecli));
  return JSON.stringify(result, null, 2);
}

export async function handleCaselawGetMetadata(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await rechtspraak.getMetadata(String(args.ecli));
  return JSON.stringify(result, null, 2);
}
