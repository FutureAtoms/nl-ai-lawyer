/**
 * MCP tool definitions for Dutch government open data.
 *
 * Tools:
 *   - overheid_search_datasets
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as overheid from "../clients/overheid.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const overheidSearchDatasetsTool: Tool = {
  name: "overheid_search_datasets",
  description:
    "Search Dutch government open datasets on data.overheid.nl. " +
    "Uses the CKAN API to find datasets by keyword. Returns dataset metadata, resources, and tags.",
  inputSchema: {
    type: "object" as const,
    properties: {
      query: {
        type: "string",
        description:
          "Search keyword(s). Examples: 'criminaliteit', 'bevolking', 'woningmarkt', 'verkeer'.",
      },
      maxResults: {
        type: "number",
        description: "Maximum number of results to return (default: 10).",
      },
      offset: {
        type: "number",
        description: "Offset for pagination (0-based).",
      },
    },
    required: ["query"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleOverheidSearchDatasets(
  args: Record<string, unknown>,
): Promise<string> {
  const result = await overheid.searchDatasets(
    String(args.query),
    args.maxResults ? Number(args.maxResults) : 10,
    args.offset ? Number(args.offset) : 0,
  );

  return JSON.stringify(
    {
      totalResults: result.totalResults,
      datasets: result.datasets,
    },
    null,
    2,
  );
}
