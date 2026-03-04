#!/usr/bin/env python3
"""
kvk-lookup.py - Fallback script for querying the KVK (Kamer van Koophandel) API.

This script provides functionality to search for Dutch companies and retrieve
company profiles from the KVK API. Requires a valid API key.

Usage:
    export KVK_API_KEY="your-api-key-here"
    python kvk-lookup.py search "Acme B.V."
    python kvk-lookup.py search "technologie" --max-results 5
    python kvk-lookup.py profile 12345678

API Documentation:
    https://developers.kvk.nl/
    https://developers.kvk.nl/documentation/search-v2
    https://developers.kvk.nl/documentation/profile-v2

Note:
    A KVK API key is required. Register at https://developers.kvk.nl/ to
    obtain one. Set the KVK_API_KEY environment variable before running.
"""

import argparse
import json
import os
import sys
import time
from typing import Optional

try:
    import requests
except ImportError:
    print(
        "Missing dependency: requests. Install with: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)


# KVK API endpoints
API_BASE = "https://api.kvk.nl/api/v2"
SEARCH_ENDPOINT = f"{API_BASE}/zoeken"
PROFILE_ENDPOINT = f"{API_BASE}/basisprofielen"

# Rate limiting
MIN_REQUEST_INTERVAL = 0.5  # Be conservative with the KVK API
_last_request_time = 0.0


def _rate_limit():
    """Enforce rate limiting to avoid overloading the KVK API."""
    global _last_request_time
    now = time.time()
    elapsed = now - _last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - elapsed)
    _last_request_time = time.time()


def _get_api_key() -> str:
    """
    Retrieve the KVK API key from the environment.

    Returns:
        The API key string.

    Raises:
        SystemExit: If the API key is not set.
    """
    api_key = os.environ.get("KVK_API_KEY", "").strip()
    if not api_key:
        print(
            "Error: KVK_API_KEY environment variable is not set.\n"
            "\n"
            "To use this script, you need a KVK API key:\n"
            "  1. Register at https://developers.kvk.nl/\n"
            "  2. Create an application and obtain an API key\n"
            "  3. Set the environment variable:\n"
            "     export KVK_API_KEY=\"your-api-key-here\"\n",
            file=sys.stderr,
        )
        sys.exit(1)
    return api_key


def _make_request(url: str, params: dict) -> dict:
    """
    Make an authenticated request to the KVK API.

    Args:
        url: The API endpoint URL.
        params: Query parameters.

    Returns:
        Parsed JSON response as a dictionary.

    Raises:
        requests.RequestException: If the request fails.
        SystemExit: On authentication errors.
    """
    api_key = _get_api_key()
    _rate_limit()

    headers = {
        "apikey": api_key,
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)
    except requests.exceptions.Timeout:
        print("Error: Request to KVK API timed out.", file=sys.stderr)
        raise
    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to KVK API. Check your internet connection.",
            file=sys.stderr,
        )
        raise

    if response.status_code == 401:
        print(
            "Error: Authentication failed. Check your KVK_API_KEY.",
            file=sys.stderr,
        )
        sys.exit(1)
    elif response.status_code == 403:
        print(
            "Error: Access forbidden. Your API key may not have the required permissions.",
            file=sys.stderr,
        )
        sys.exit(1)
    elif response.status_code == 404:
        return {}
    elif response.status_code == 429:
        print(
            "Error: Rate limit exceeded. Please wait and try again.",
            file=sys.stderr,
        )
        sys.exit(1)

    response.raise_for_status()

    try:
        return response.json()
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response from KVK API.", file=sys.stderr)
        return {}


def search_company(
    query: str,
    max_results: int = 10,
    include_inactive: bool = False,
) -> list[dict]:
    """
    Search for companies in the KVK register.

    Args:
        query: Search terms (company name, KVK number, or other identifier).
        max_results: Maximum number of results to return (default 10).
        include_inactive: Whether to include inactive/deregistered companies.

    Returns:
        A list of dictionaries, each containing:
            - kvk_number: The KVK registration number.
            - name: Trade name of the company.
            - type: Legal form / type of entity.
            - address: Registered address.
            - active: Whether the company is currently active.
            - branch_number: Vestigingsnummer (establishment number).

    Raises:
        requests.RequestException: If the API request fails.
    """
    params = {
        "naam": query,
        "pagina": "1",
        "aantal": str(min(max_results, 100)),
    }

    if not include_inactive:
        params["InclusiefInactieveRegistraties"] = "false"

    data = _make_request(SEARCH_ENDPOINT, params)
    return _parse_search_results(data)


def _parse_search_results(data: dict) -> list[dict]:
    """
    Parse the KVK search API response.

    Args:
        data: Parsed JSON response.

    Returns:
        List of company result dictionaries.
    """
    results = []

    if not data or "resultaten" not in data:
        return results

    for item in data["resultaten"]:
        result = {
            "kvk_number": item.get("kvkNummer", "Unknown"),
            "name": item.get("handelsnaam", "Unknown"),
            "type": item.get("type", "Unknown"),
            "active": True,
            "branch_number": item.get("vestigingsnummer", ""),
        }

        # Extract address
        address_parts = []
        adres = item.get("adres", {})
        if isinstance(adres, dict):
            if adres.get("binnenlandsAdres"):
                ba = adres["binnenlandsAdres"]
                street = ba.get("straatnaam", "")
                number = ba.get("huisnummer", "")
                postcode = ba.get("postcode", "")
                city = ba.get("plaats", "")
                if street:
                    addr = street
                    if number:
                        addr += f" {number}"
                    address_parts.append(addr)
                if postcode or city:
                    address_parts.append(f"{postcode} {city}".strip())
        result["address"] = ", ".join(address_parts) if address_parts else "No address available"

        results.append(result)

    return results


def get_profile(kvk_number: str) -> dict:
    """
    Retrieve the full company profile by KVK number.

    Args:
        kvk_number: The 8-digit KVK registration number.

    Returns:
        A dictionary containing:
            - kvk_number: KVK registration number.
            - rsin: RSIN number (for tax purposes).
            - name: Statutory name.
            - trade_names: List of trade names.
            - legal_form: Legal form (e.g., BV, NV, Eenmanszaak).
            - addresses: List of registered addresses.
            - sbi_codes: List of SBI activity codes and descriptions.
            - founding_date: Date the company was founded.
            - total_employees: Number of employees.
            - active: Whether the company is currently active.

    Raises:
        requests.RequestException: If the API request fails.
        ValueError: If the KVK number is invalid.
    """
    # Validate KVK number format
    kvk_clean = kvk_number.strip().replace(" ", "")
    if not kvk_clean.isdigit() or len(kvk_clean) != 8:
        raise ValueError(
            f"Invalid KVK number: {kvk_number}. Must be exactly 8 digits."
        )

    url = f"{PROFILE_ENDPOINT}/{kvk_clean}"
    data = _make_request(url, {})

    if not data:
        return {
            "kvk_number": kvk_clean,
            "error": f"No profile found for KVK number {kvk_clean}.",
        }

    return _parse_profile(data, kvk_clean)


def _parse_profile(data: dict, kvk_number: str) -> dict:
    """
    Parse the KVK profile API response.

    Args:
        data: Parsed JSON response.
        kvk_number: The requested KVK number.

    Returns:
        A comprehensive company profile dictionary.
    """
    profile = {
        "kvk_number": kvk_number,
        "rsin": data.get("rsin", ""),
        "name": data.get("naam", "Unknown"),
        "trade_names": [],
        "legal_form": data.get("rechtsvorm", "Unknown"),
        "addresses": [],
        "sbi_codes": [],
        "founding_date": data.get("datumOprichting", ""),
        "total_employees": data.get("totaalWerkzamePersonen", "Unknown"),
        "active": not bool(data.get("datumUitschrijving")),
    }

    # Extract trade names
    if "handelsnamen" in data:
        for hn in data["handelsnamen"]:
            if isinstance(hn, dict):
                profile["trade_names"].append(hn.get("naam", ""))
            elif isinstance(hn, str):
                profile["trade_names"].append(hn)

    # Extract addresses
    if "adressen" in data:
        for addr in data["adressen"]:
            if isinstance(addr, dict):
                address_info = {
                    "type": addr.get("type", "Unknown"),
                    "street": addr.get("straatnaam", ""),
                    "house_number": addr.get("huisnummer", ""),
                    "postcode": addr.get("postcode", ""),
                    "city": addr.get("plaats", ""),
                    "country": addr.get("land", "Nederland"),
                }
                profile["addresses"].append(address_info)

    # Extract SBI codes (industry classification)
    if "spiActiviteiten" in data:
        for sbi in data["spiActiviteiten"]:
            if isinstance(sbi, dict):
                profile["sbi_codes"].append({
                    "code": sbi.get("sbiCode", ""),
                    "description": sbi.get("sbiOmschrijving", ""),
                    "primary": sbi.get("indHoofdactiviteit", False),
                })

    return profile


def format_search_result(result: dict) -> str:
    """
    Format a company search result for display.

    Args:
        result: A search result dictionary.

    Returns:
        Formatted string representation.
    """
    status = "Active" if result.get("active", True) else "Inactive"
    lines = [
        f"KVK Number:     {result.get('kvk_number', 'N/A')}",
        f"Name:           {result.get('name', 'N/A')}",
        f"Type:           {result.get('type', 'N/A')}",
        f"Address:        {result.get('address', 'N/A')}",
        f"Status:         {status}",
    ]
    if result.get("branch_number"):
        lines.append(f"Branch Number:  {result['branch_number']}")
    return "\n".join(lines)


def format_profile(profile: dict) -> str:
    """
    Format a full company profile for display.

    Args:
        profile: A company profile dictionary.

    Returns:
        Formatted string representation.
    """
    if "error" in profile:
        return profile["error"]

    separator = "=" * 72
    status = "Active" if profile.get("active", True) else "Inactive / Deregistered"

    lines = [
        separator,
        f"Company Profile: {profile.get('name', 'N/A')}",
        separator,
        f"KVK Number:       {profile.get('kvk_number', 'N/A')}",
        f"RSIN:             {profile.get('rsin', 'N/A') or 'N/A'}",
        f"Legal Form:       {profile.get('legal_form', 'N/A')}",
        f"Status:           {status}",
        f"Founded:          {profile.get('founding_date', 'N/A') or 'N/A'}",
        f"Total Employees:  {profile.get('total_employees', 'N/A')}",
    ]

    # Trade names
    trade_names = profile.get("trade_names", [])
    if trade_names:
        lines.append(f"\nTrade Names:")
        for tn in trade_names:
            lines.append(f"  - {tn}")

    # Addresses
    addresses = profile.get("addresses", [])
    if addresses:
        lines.append(f"\nAddresses:")
        for addr in addresses:
            street = addr.get("street", "")
            number = addr.get("house_number", "")
            postcode = addr.get("postcode", "")
            city = addr.get("city", "")
            addr_type = addr.get("type", "")
            addr_str = f"{street} {number}, {postcode} {city}".strip(", ")
            lines.append(f"  [{addr_type}] {addr_str}")

    # SBI codes
    sbi_codes = profile.get("sbi_codes", [])
    if sbi_codes:
        lines.append(f"\nSBI Activities:")
        for sbi in sbi_codes:
            primary = " (primary)" if sbi.get("primary") else ""
            lines.append(
                f"  [{sbi.get('code', 'N/A')}] {sbi.get('description', 'N/A')}{primary}"
            )

    lines.append(separator)
    return "\n".join(lines)


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Search and retrieve company information from the KVK (Kamer van Koophandel) API.",
        epilog=(
            "Examples:\n"
            '  %(prog)s search "Acme B.V."\n'
            '  %(prog)s search "technologie" --max-results 5\n'
            "  %(prog)s profile 12345678\n"
            "\n"
            "Environment:\n"
            "  KVK_API_KEY    Required. Your KVK API key from https://developers.kvk.nl/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search subcommand
    search_parser = subparsers.add_parser(
        "search", help="Search for companies by name"
    )
    search_parser.add_argument(
        "query", type=str, help="Company name or search terms"
    )
    search_parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum number of results (default: 10)",
    )
    search_parser.add_argument(
        "--include-inactive",
        action="store_true",
        default=False,
        help="Include inactive/deregistered companies in results",
    )

    # Profile subcommand
    profile_parser = subparsers.add_parser(
        "profile", help="Get a full company profile by KVK number"
    )
    profile_parser.add_argument(
        "kvk_number",
        type=str,
        help="8-digit KVK registration number",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "search":
        try:
            results = search_company(
                query=args.query,
                max_results=args.max_results,
                include_inactive=args.include_inactive,
            )
        except SystemExit:
            raise
        except Exception as e:
            print(f"Search failed: {e}", file=sys.stderr)
            sys.exit(1)

        if not results:
            print("No companies found.")
            sys.exit(0)

        print(f"Found {len(results)} result(s):\n")
        for i, result in enumerate(results, 1):
            print(f"--- Result {i} ---")
            print(format_search_result(result))
            print()

    elif args.command == "profile":
        try:
            profile = get_profile(args.kvk_number)
        except ValueError as e:
            print(f"Invalid input: {e}", file=sys.stderr)
            sys.exit(1)
        except SystemExit:
            raise
        except Exception as e:
            print(f"Failed to retrieve profile: {e}", file=sys.stderr)
            sys.exit(1)

        print(format_profile(profile))


if __name__ == "__main__":
    main()
