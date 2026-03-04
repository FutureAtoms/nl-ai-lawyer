/**
 * MCP tool definitions for KVK (Dutch Chamber of Commerce) corporate data.
 *
 * Tools:
 *   - kvk_search_company
 *   - kvk_get_profile
 *   - kvk_get_naming
 */

import type { Tool } from "@modelcontextprotocol/sdk/types.js";
import * as kvk from "../clients/kvk.js";

// ── Tool Definitions ────────────────────────────────────────────────

export const kvkSearchCompanyTool: Tool = {
  name: "kvk_search_company",
  description:
    "Search the Dutch Chamber of Commerce (KVK) registry by company name or KVK number. " +
    "Returns basic company information including address, type, and active status. " +
    "Requires KVK_API_KEY environment variable.",
  inputSchema: {
    type: "object" as const,
    properties: {
      nameOrNumber: {
        type: "string",
        description:
          "Company name or KVK number (8 digits). Examples: 'Shell', '12345678'.",
      },
    },
    required: ["nameOrNumber"],
  },
};

export const kvkGetProfileTool: Tool = {
  name: "kvk_get_profile",
  description:
    "Get a detailed company profile from KVK including legal form, addresses, " +
    "employee count, and SBI activity codes. Requires KVK_API_KEY.",
  inputSchema: {
    type: "object" as const,
    properties: {
      kvkNumber: {
        type: "string",
        description: "The 8-digit KVK number of the company.",
      },
    },
    required: ["kvkNumber"],
  },
};

export const kvkGetNamingTool: Tool = {
  name: "kvk_get_naming",
  description:
    "Get trade names (handelsnamen) history from KVK for a company. " +
    "Returns statutory name, first trade name, and all registered trade names. " +
    "Requires KVK_API_KEY.",
  inputSchema: {
    type: "object" as const,
    properties: {
      kvkNumber: {
        type: "string",
        description: "The 8-digit KVK number of the company.",
      },
    },
    required: ["kvkNumber"],
  },
};

// ── Tool Handlers ───────────────────────────────────────────────────

export async function handleKvkSearchCompany(
  args: Record<string, unknown>,
): Promise<string> {
  try {
    const results = await kvk.searchCompany(String(args.nameOrNumber));
    return JSON.stringify({ results }, null, 2);
  } catch (error) {
    if (
      error instanceof Error &&
      error.message.includes("KVK_API_KEY")
    ) {
      return JSON.stringify(
        {
          error: "KVK_API_KEY not configured",
          message: error.message,
          hint: "Set the KVK_API_KEY environment variable with a valid API key from https://developers.kvk.nl/",
        },
        null,
        2,
      );
    }
    throw error;
  }
}

export async function handleKvkGetProfile(
  args: Record<string, unknown>,
): Promise<string> {
  try {
    const profile = await kvk.getProfile(String(args.kvkNumber));
    return JSON.stringify(profile, null, 2);
  } catch (error) {
    if (
      error instanceof Error &&
      error.message.includes("KVK_API_KEY")
    ) {
      return JSON.stringify(
        {
          error: "KVK_API_KEY not configured",
          message: error.message,
        },
        null,
        2,
      );
    }
    throw error;
  }
}

export async function handleKvkGetNaming(
  args: Record<string, unknown>,
): Promise<string> {
  try {
    const naming = await kvk.getNaming(String(args.kvkNumber));
    return JSON.stringify(naming, null, 2);
  } catch (error) {
    if (
      error instanceof Error &&
      error.message.includes("KVK_API_KEY")
    ) {
      return JSON.stringify(
        {
          error: "KVK_API_KEY not configured",
          message: error.message,
        },
        null,
        2,
      );
    }
    throw error;
  }
}
