#!/usr/bin/env node

/**
 * Dutch Legal MCP Server
 *
 * A Model Context Protocol (MCP) server that wraps multiple Dutch legal
 * APIs, providing 15 tools for searching and retrieving:
 *
 *   - Dutch legislation (KOOP SRU / BWB)
 *   - Case law (Rechtspraak.nl)
 *   - Judge information (Open Rechtspraak)
 *   - Company data (KVK)
 *   - EU legislation (EUR-Lex SPARQL)
 *   - Government datasets (data.overheid.nl)
 *   - Cross-references between Dutch and EU law
 *
 * Transport: stdio
 */

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// ── Tool definitions & handlers ─────────────────────────────────────

import {
  handleLegislationSearch,
  handleLegislationGetArticle,
  handleLegislationVersions,
} from "./tools/legislation.js";

import {
  handleCaselawSearch,
  handleCaselawGetRuling,
  handleCaselawGetMetadata,
} from "./tools/caselaw.js";

import {
  handleJudgesSearch,
  handleJudgesGetVerdicts,
} from "./tools/judges.js";

import {
  handleKvkSearchCompany,
  handleKvkGetProfile,
  handleKvkGetNaming,
} from "./tools/corporate.js";

import {
  handleEurlexSearchRegulations,
  handleEurlexGetAct,
} from "./tools/eu-law.js";

import { handleOverheidSearchDatasets } from "./tools/government.js";

import { handleLegalCrossReference } from "./tools/cross-reference.js";

// ── Server setup ────────────────────────────────────────────────────

const server = new McpServer({
  name: "dutch-legal-mcp",
  version: "1.0.0",
  description:
    "MCP server providing access to Dutch legal APIs including " +
    "Rechtspraak.nl, KOOP SRU (BWB legislation), KVK, EUR-Lex, " +
    "Open Rechtspraak, and data.overheid.nl.",
});

// ── Helper: wrap a handler so exceptions become MCP error responses ──

function wrapHandler(
  handler: (args: Record<string, unknown>) => Promise<string>,
): (args: Record<string, unknown>) => Promise<{ content: Array<{ type: "text"; text: string }> }> {
  return async (args) => {
    try {
      const text = await handler(args);
      return { content: [{ type: "text" as const, text }] };
    } catch (error) {
      const message =
        error instanceof Error ? error.message : String(error);
      return {
        content: [
          {
            type: "text" as const,
            text: JSON.stringify({ error: message }, null, 2),
          },
        ],
      };
    }
  };
}

// ── Register all 15 tools ───────────────────────────────────────────

// 1. legislation_search
server.tool(
  "legislation_search",
  "Search Dutch legislation (wetten, besluiten, regelingen) by keyword, legal area, and/or date range. Uses the KOOP SRU API to search BWB documents.",
  {
    query: z.string().describe("Search query (keywords). Examples: 'huurrecht', 'Burgerlijk Wetboek'."),
    area: z.string().optional().describe("Legal area filter. Examples: 'staatsrecht', 'strafrecht'."),
    dateFrom: z.string().optional().describe("Legislation valid from this date (YYYY-MM-DD)."),
    dateTo: z.string().optional().describe("Legislation valid until this date (YYYY-MM-DD)."),
    max: z.number().optional().describe("Maximum number of results (default: 10)."),
  },
  wrapHandler(handleLegislationSearch),
);

// 2. legislation_get_article
server.tool(
  "legislation_get_article",
  "Get a specific article from Dutch legislation by BWB-ID and article number.",
  {
    bwbId: z.string().describe("BWB identifier. Example: 'BWBR0005290'."),
    articleNumber: z.string().describe("Article number. Examples: '610', '7:610', '6:162'."),
  },
  wrapHandler(handleLegislationGetArticle),
);

// 3. legislation_versions
server.tool(
  "legislation_versions",
  "Get version history of a Dutch law identified by BWB-ID.",
  {
    bwbId: z.string().describe("BWB identifier. Example: 'BWBR0005290'."),
  },
  wrapHandler(handleLegislationVersions),
);

// 4. caselaw_search_rechtspraak
server.tool(
  "caselaw_search_rechtspraak",
  "Search Dutch case law on Rechtspraak.nl by keyword, court, subject, or date range.",
  {
    query: z.string().describe("Free-text search query."),
    court: z.string().optional().describe("Court name filter. Example: 'Hoge Raad'."),
    subject: z.string().optional().describe("Legal subject filter. Example: 'Civiel recht'."),
    dateFrom: z.string().optional().describe("Start of date range (YYYY-MM-DD)."),
    dateTo: z.string().optional().describe("End of date range (YYYY-MM-DD)."),
    max: z.number().optional().describe("Maximum results (default: 10, max: 1000)."),
    offset: z.number().optional().describe("Pagination offset."),
  },
  wrapHandler(handleCaselawSearch),
);

// 5. caselaw_get_ruling
server.tool(
  "caselaw_get_ruling",
  "Get the full text of a Dutch court ruling by ECLI identifier.",
  {
    ecli: z.string().describe("ECLI identifier. Example: 'ECLI:NL:HR:2023:123'."),
  },
  wrapHandler(handleCaselawGetRuling),
);

// 6. caselaw_get_metadata
server.tool(
  "caselaw_get_metadata",
  "Get metadata for a Dutch court ruling by ECLI (without full text).",
  {
    ecli: z.string().describe("ECLI identifier."),
  },
  wrapHandler(handleCaselawGetMetadata),
);

// 7. judges_search
server.tool(
  "judges_search",
  "Search Dutch judges (rechters) by name using Open Rechtspraak API.",
  {
    name: z.string().describe("Name or partial name of the judge."),
  },
  wrapHandler(handleJudgesSearch),
);

// 8. judges_get_verdicts
server.tool(
  "judges_get_verdicts",
  "Get all published verdicts for a judge by their ID.",
  {
    judgeId: z.string().describe("Judge's unique identifier (from judges_search)."),
  },
  wrapHandler(handleJudgesGetVerdicts),
);

// 9. kvk_search_company
server.tool(
  "kvk_search_company",
  "Search KVK (Dutch Chamber of Commerce) by company name or KVK number. Requires KVK_API_KEY.",
  {
    nameOrNumber: z.string().describe("Company name or 8-digit KVK number."),
  },
  wrapHandler(handleKvkSearchCompany),
);

// 10. kvk_get_profile
server.tool(
  "kvk_get_profile",
  "Get detailed company profile from KVK. Requires KVK_API_KEY.",
  {
    kvkNumber: z.string().describe("8-digit KVK number."),
  },
  wrapHandler(handleKvkGetProfile),
);

// 11. kvk_get_naming
server.tool(
  "kvk_get_naming",
  "Get trade names history from KVK. Requires KVK_API_KEY.",
  {
    kvkNumber: z.string().describe("8-digit KVK number."),
  },
  wrapHandler(handleKvkGetNaming),
);

// 12. eurlex_search_regulations
server.tool(
  "eurlex_search_regulations",
  "Search EU regulations, directives, and decisions on EUR-Lex by keyword.",
  {
    query: z.string().describe("Search keywords. Examples: 'GDPR', 'consumer protection'."),
    maxResults: z.number().optional().describe("Maximum results (default: 10)."),
  },
  wrapHandler(handleEurlexSearchRegulations),
);

// 13. eurlex_get_act
server.tool(
  "eurlex_get_act",
  "Get EU act details by CELEX number including title, type, and text.",
  {
    celexNumber: z.string().describe("CELEX number. Example: '32016R0679' (GDPR)."),
  },
  wrapHandler(handleEurlexGetAct),
);

// 14. overheid_search_datasets
server.tool(
  "overheid_search_datasets",
  "Search Dutch government open datasets on data.overheid.nl.",
  {
    query: z.string().describe("Search keywords. Examples: 'criminaliteit', 'bevolking'."),
    maxResults: z.number().optional().describe("Maximum results (default: 10)."),
    offset: z.number().optional().describe("Pagination offset."),
  },
  wrapHandler(handleOverheidSearchDatasets),
);

// 15. legal_cross_reference
server.tool(
  "legal_cross_reference",
  "Find related case law and EU regulations for a Dutch law article reference. Cross-references multiple APIs.",
  {
    articleReference: z.string().describe("Article reference. Example: 'Artikel 6:162 BW'."),
    bwbId: z.string().optional().describe("Optional BWB-ID for precise lookup."),
    articleNumber: z.string().optional().describe("Optional article number."),
    includeEuLaw: z.boolean().optional().describe("Include EU law search (default: true)."),
    maxCaseLaw: z.number().optional().describe("Max case law results (default: 5)."),
    maxEuLaw: z.number().optional().describe("Max EU law results (default: 3)."),
  },
  wrapHandler(handleLegalCrossReference),
);

// ── Start the server ────────────────────────────────────────────────

async function main(): Promise<void> {
  const transport = new StdioServerTransport();

  // Graceful shutdown
  process.on("SIGINT", async () => {
    await server.close();
    process.exit(0);
  });

  process.on("SIGTERM", async () => {
    await server.close();
    process.exit(0);
  });

  await server.connect(transport);
  console.error("Dutch Legal MCP server running on stdio transport");
}

main().catch((error) => {
  console.error("Fatal error starting Dutch Legal MCP server:", error);
  process.exit(1);
});
