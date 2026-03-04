/**
 * MCP tool definitions for judge search functionality.
 *
 * Tools:
 *   - judges_search
 *   - judges_get_verdicts
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as openRechtspraak from "../clients/open-rechtspraak.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const judgesSearchTool: Tool = {
  name: "judges_search",
  description:
    "Search Dutch judges (rechters) by name. " +
    "Uses the Open Rechtspraak API to find judges and their associated courts.",
  inputSchema: {
    type: "object" as const,
    properties: {
      name: {
        type: "string",
        description:
          "Name (or partial name) of the judge to search for.",
      },
    },
    required: ["name"],
  },
};

export const judgesGetVerdictsTool: Tool = {
  name: "judges_get_verdicts",
  description:
    "Get all published verdicts for a specific judge by their ID. " +
    "Returns a list of rulings (uitspraken) with ECLI, date, court, and summary.",
  inputSchema: {
    type: "object" as const,
    properties: {
      judgeId: {
        type: "string",
        description:
          "The judge's unique identifier (obtained from judges_search).",
      },
    },
    required: ["judgeId"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleJudgesSearch(
  args: Record<string, unknown>,
): Promise<string> {
  const results = await openRechtspraak.searchJudges(String(args.name));
  return JSON.stringify({ results }, null, 2);
}

export async function handleJudgesGetVerdicts(
  args: Record<string, unknown>,
): Promise<string> {
  const verdicts = await openRechtspraak.getJudgeVerdicts(
    String(args.judgeId),
  );
  return JSON.stringify({ verdicts }, null, 2);
}
