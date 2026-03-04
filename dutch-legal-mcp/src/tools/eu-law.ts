/**
 * MCP tool definitions for EU law (EUR-Lex).
 *
 * Tools:
 *   - eurlex_search_regulations
 *   - eurlex_get_act
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as eurlex from "../clients/eurlex.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const eurlexSearchRegulationsTool: Tool = {
  name: "eurlex_search_regulations",
  description:
    "Search EU regulations, directives, and decisions on EUR-Lex by keyword. " +
    "Queries the EUR-Lex SPARQL endpoint. Results include CELEX number, title, date, and type.",
  inputSchema: {
    type: "object" as const,
    properties: {
      query: {
        type: "string",
        description:
          "Search keyword(s). Examples: 'GDPR', 'consumer protection', 'data protection'.",
      },
      maxResults: {
        type: "number",
        description: "Maximum number of results to return (default: 10).",
      },
    },
    required: ["query"],
  },
};

export const eurlexGetActTool: Tool = {
  name: "eurlex_get_act",
  description:
    "Get detailed information about an EU legal act by its CELEX number. " +
    "Returns title, date, type, subject, full text (when available), and enforcement status.",
  inputSchema: {
    type: "object" as const,
    properties: {
      celexNumber: {
        type: "string",
        description:
          "The CELEX number of the EU act. Example: '32016R0679' (GDPR), '32011L0083' (Consumer Rights Directive).",
      },
    },
    required: ["celexNumber"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleEurlexSearchRegulations(
  args: Record<string, unknown>,
): Promise<string> {
  const results = await eurlex.searchRegulations(
    String(args.query),
    args.maxResults ? Number(args.maxResults) : 10,
  );
  return JSON.stringify({ results }, null, 2);
}

export async function handleEurlexGetAct(
  args: Record<string, unknown>,
): Promise<string> {
  const act = await eurlex.getAct(String(args.celexNumber));
  return JSON.stringify(act, null, 2);
}
