/**
 * KVK (Kamer van Koophandel) company registry API client
 *
 * Wraps the KVK API v2 for searching companies and retrieving profiles.
 * Requires KVK_API_KEY environment variable.
 *
 * Base URL: https://api.kvk.nl/api/v2/
 * Docs: https://developers.kvk.nl/
 */

import { rateLimiter } from "../utils/rate-limiter.js";
import { cache, MultiTierCache } from "../utils/cache.js";

const BASE_URL = "https://api.kvk.nl/api/v2";
const BACKEND = "kvk";

export interface KvkCompanySearchResult {
  kvkNumber: string;
  branchNumber?: string;
  name: string;
  street?: string;
  houseNumber?: string;
  postalCode?: string;
  city?: string;
  type: string;
  isActive: boolean;
}

export interface KvkCompanyProfile {
  kvkNumber: string;
  name: string;
  legalForm?: string;
  startDate?: string;
  totalEmployees?: number;
  addresses: Array<{
    type: string;
    street?: string;
    houseNumber?: string;
    postalCode?: string;
    city?: string;
    country?: string;
  }>;
  sbiActivities: Array<{
    sbiCode: string;
    description: string;
    isMainSbi: boolean;
  }>;
}

export interface KvkNamingInfo {
  kvkNumber: string;
  tradeNames: Array<{
    name: string;
    type: string;
  }>;
  statutoryName?: string;
  firstTradeName?: string;
}

/**
 * Get the KVK API key from environment or throw a clear error.
 */
function getApiKey(): string {
  const key = process.env.KVK_API_KEY;
  if (!key) {
    throw new Error(
      "KVK_API_KEY environment variable is not set. " +
        "Register at https://developers.kvk.nl/ to obtain an API key.",
    );
  }
  return key;
}

/**
 * Make an authenticated request to the KVK API.
 */
async function kvkFetch(path: string, params: URLSearchParams): Promise<unknown> {
  const apiKey = getApiKey();

  const url = `${BASE_URL}${path}?${params.toString()}`;

  await rateLimiter.acquire(BACKEND);
  const response = await fetch(url, {
    headers: {
      apikey: apiKey,
      Accept: "application/json",
    },
  });

  if (response.status === 401) {
    throw new Error("KVK API authentication failed. Check your KVK_API_KEY.");
  }
  if (response.status === 403) {
    throw new Error("KVK API access forbidden. Your API key may lack required permissions.");
  }
  if (!response.ok) {
    const body = await response.text().catch(() => "");
    throw new Error(
      `KVK API request failed (${response.status}): ${response.statusText}. ${body}`,
    );
  }

  return response.json();
}

/**
 * Search for companies by name or KVK number.
 */
export async function searchCompany(
  nameOrNumber: string,
): Promise<KvkCompanySearchResult[]> {
  const cacheKey = MultiTierCache.key("kvk-search", nameOrNumber);
  const cached = cache.get<KvkCompanySearchResult[]>("kvk_data", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams();

  // Detect if input is a KVK number (8 digits) or a name
  if (/^\d{8}$/.test(nameOrNumber.trim())) {
    params.set("kvkNumber", nameOrNumber.trim());
  } else {
    params.set("q", nameOrNumber);
  }
  params.set("resultType", "ACTIVE");

  const data = (await kvkFetch("/zoeken", params)) as {
    data?: { items?: unknown[] };
    resultaten?: unknown[];
  };

  const items = data?.data?.items ?? data?.resultaten ?? [];

  const results: KvkCompanySearchResult[] = (items as Record<string, unknown>[]).map(
    (item) => ({
      kvkNumber: String(item.kvkNummer ?? item.kvkNumber ?? ""),
      branchNumber: item.vestigingsnummer
        ? String(item.vestigingsnummer)
        : undefined,
      name: String(item.handelsnaam ?? item.naam ?? item.name ?? ""),
      street: optStr(item.straatnaam ?? item.street),
      houseNumber: optStr(item.huisnummer ?? item.houseNumber),
      postalCode: optStr(item.postcode ?? item.postalCode),
      city: optStr(item.plaats ?? item.city),
      type: String(item.type ?? item.resultaatType ?? ""),
      isActive: item.actief !== false && item.isActive !== false,
    }),
  );

  cache.set("kvk_data", cacheKey, results);
  return results;
}

/**
 * Get a detailed company profile by KVK number.
 */
export async function getProfile(
  kvkNumber: string,
): Promise<KvkCompanyProfile> {
  const cacheKey = MultiTierCache.key("kvk-profile", kvkNumber);
  const cached = cache.get<KvkCompanyProfile>("kvk_data", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams();
  params.set("kvkNumber", kvkNumber);

  const data = (await kvkFetch("/basisprofielen", params)) as Record<
    string,
    unknown
  >;

  const mainItem = (data as Record<string, unknown>) ?? {};
  const addresses = ensureArray(
    (mainItem.adressen ?? mainItem.addresses ?? []) as unknown[],
  ).map((a) => {
    const addr = a as Record<string, unknown>;
    return {
      type: String(addr.type ?? addr.adresType ?? ""),
      street: optStr(addr.straatnaam ?? addr.street),
      houseNumber: optStr(addr.huisnummer ?? addr.houseNumber),
      postalCode: optStr(addr.postcode ?? addr.postalCode),
      city: optStr(addr.plaats ?? addr.city),
      country: optStr(addr.land ?? addr.country),
    };
  });

  const sbiActivities = ensureArray(
    (mainItem.spiActiviteiten ??
      mainItem.sbiActiviteiten ??
      mainItem.sbiActivities ??
      []) as unknown[],
  ).map((s) => {
    const sbi = s as Record<string, unknown>;
    return {
      sbiCode: String(sbi.sbiCode ?? sbi.code ?? ""),
      description: String(sbi.sbiOmschrijving ?? sbi.description ?? ""),
      isMainSbi: Boolean(sbi.indHoofdactiviteit ?? sbi.isMainSbi ?? false),
    };
  });

  const profile: KvkCompanyProfile = {
    kvkNumber: String(mainItem.kvkNummer ?? mainItem.kvkNumber ?? kvkNumber),
    name: String(
      mainItem.handelsnaam ??
        mainItem.naam ??
        mainItem.name ??
        mainItem.statutaireNaam ??
        "",
    ),
    legalForm: optStr(mainItem.rechtsvorm ?? mainItem.legalForm),
    startDate: optStr(mainItem.registratiedatum ?? mainItem.startDate),
    totalEmployees:
      typeof mainItem.totaalWerkzamePersonen === "number"
        ? mainItem.totaalWerkzamePersonen
        : undefined,
    addresses,
    sbiActivities,
  };

  cache.set("kvk_data", cacheKey, profile);
  return profile;
}

/**
 * Get trade names (handelsnamen) for a company by KVK number.
 */
export async function getNaming(
  kvkNumber: string,
): Promise<KvkNamingInfo> {
  const cacheKey = MultiTierCache.key("kvk-naming", kvkNumber);
  const cached = cache.get<KvkNamingInfo>("kvk_data", cacheKey);
  if (cached) return cached;

  const params = new URLSearchParams();
  params.set("kvkNumber", kvkNumber);

  const data = (await kvkFetch("/naamgeving", params)) as Record<
    string,
    unknown
  >;

  const namesRaw = ensureArray(
    (data.handelsnamen ?? data.tradeNames ?? []) as unknown[],
  );

  const tradeNames = namesRaw.map((item) => {
    const n = item as Record<string, unknown>;
    return {
      name: String(n.naam ?? n.name ?? ""),
      type: String(n.type ?? n.volgorde ?? ""),
    };
  });

  const result: KvkNamingInfo = {
    kvkNumber,
    tradeNames,
    statutoryName: optStr(data.statutaireNaam ?? data.statutoryName),
    firstTradeName: optStr(data.eersteHandelsnaam ?? data.firstTradeName),
  };

  cache.set("kvk_data", cacheKey, result);
  return result;
}

// ── Helpers ─────────────────────────────────────────────────────────

function optStr(val: unknown): string | undefined {
  if (val == null) return undefined;
  return String(val);
}

function ensureArray<T>(val: T | T[]): T[] {
  if (Array.isArray(val)) return val;
  if (val == null) return [];
  return [val];
}
