#!/usr/bin/env python3
"""
ecli-parser.py - ECLI identifier parser, validator, and formatter.

The European Case Law Identifier (ECLI) is a standardized identifier for
court decisions within the European Union. The format is:

    ECLI:[Country Code]:[Court Code]:[Year]:[Identifier]

Example: ECLI:NL:HR:2023:1234

This script provides utilities for parsing, validating, and formatting ECLI
identifiers with a focus on the Dutch (NL) court system.

Usage:
    python ecli-parser.py parse ECLI:NL:HR:2023:1234
    python ecli-parser.py validate ECLI:NL:HR:2023:1234
    python ecli-parser.py format --country NL --court HR --year 2023 --id 1234
    python ecli-parser.py courts
    python ecli-parser.py courts --filter amsterdam

Reference:
    https://www.rechtspraak.nl/Uitspraken/paginas/ECLI.aspx
    https://e-justice.europa.eu/content_european_case_law_identifier_ecli-175-en.do
"""

import argparse
import re
import sys
from typing import Optional


# Complete mapping of Dutch court codes to their names
DUTCH_COURT_CODES = {
    # Supreme Court
    "HR": "Hoge Raad der Nederlanden",
    "PHR": "Parket bij de Hoge Raad",

    # Courts of Appeal (Gerechtshoven)
    "GHAMS": "Gerechtshof Amsterdam",
    "GHARL": "Gerechtshof Arnhem-Leeuwarden",
    "GHDHA": "Gerechtshof Den Haag",
    "GHSHE": "Gerechtshof 's-Hertogenbosch",

    # District Courts (Rechtbanken)
    "RBAMS": "Rechtbank Amsterdam",
    "RBDHA": "Rechtbank Den Haag",
    "RBGEL": "Rechtbank Gelderland",
    "RBLIM": "Rechtbank Limburg",
    "RBMNE": "Rechtbank Midden-Nederland",
    "RBNHO": "Rechtbank Noord-Holland",
    "RBNNE": "Rechtbank Noord-Nederland",
    "RBOBR": "Rechtbank Oost-Brabant",
    "RBOVE": "Rechtbank Overijssel",
    "RBROT": "Rechtbank Rotterdam",
    "RBZWB": "Rechtbank Zeeland-West-Brabant",

    # Administrative Courts
    "CRVB": "Centrale Raad van Beroep",
    "CBB": "College van Beroep voor het bedrijfsleven",
    "RVS": "Raad van State (Afdeling bestuursrechtspraak)",

    # Former Courts (pre-2013 restructuring, still found in older ECLIs)
    "RBALK": "Rechtbank Alkmaar (opgeheven)",
    "RBARN": "Rechtbank Arnhem (opgeheven)",
    "RBASS": "Rechtbank Assen (opgeheven)",
    "RBBRA": "Rechtbank Breda (opgeheven)",
    "RBDOR": "Rechtbank Dordrecht (opgeheven)",
    "RBGRO": "Rechtbank Groningen (opgeheven)",
    "RBHAA": "Rechtbank Haarlem (opgeheven)",
    "RBLEE": "Rechtbank Leeuwarden (opgeheven)",
    "RBMAA": "Rechtbank Maastricht (opgeheven)",
    "RBROE": "Rechtbank Roermond (opgeheven)",
    "RBSGR": "Rechtbank 's-Gravenhage (opgeheven)",
    "RBSHE": "Rechtbank 's-Hertogenbosch (opgeheven)",
    "RBUTR": "Rechtbank Utrecht (opgeheven)",
    "RBZLY": "Rechtbank Zwolle-Lelystad (opgeheven)",
    "RBZUT": "Rechtbank Zutphen (opgeheven)",

    # Former Courts of Appeal
    "GHLEE": "Gerechtshof Leeuwarden (opgeheven)",
    "GHARN": "Gerechtshof Arnhem (opgeheven)",
    "GHSGR": "Gerechtshof 's-Gravenhage (opgeheven)",

    # Special Tribunals
    "RBNNE": "Rechtbank Noord-Nederland",
    "RBOVE": "Rechtbank Overijssel",
}

# EU country codes that use ECLI
EU_COUNTRY_CODES = {
    "AT": "Austria",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CY": "Cyprus",
    "CZ": "Czech Republic",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "ES": "Spain",
    "EU": "Court of Justice of the EU",
    "FI": "Finland",
    "FR": "France",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IT": "Italy",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "MT": "Malta",
    "NL": "Netherlands",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
}

# ECLI format regex
ECLI_PATTERN = re.compile(
    r"^ECLI:"
    r"(?P<country>[A-Z]{2}):"
    r"(?P<court>[A-Z0-9]+):"
    r"(?P<year>\d{4}):"
    r"(?P<id>[A-Za-z0-9.]+)$"
)


def parse_ecli(ecli_string: str) -> dict:
    """
    Parse an ECLI identifier into its component parts.

    Args:
        ecli_string: The ECLI string to parse (e.g., "ECLI:NL:HR:2023:1234").

    Returns:
        A dictionary containing:
            - ecli: The full ECLI string (normalized to uppercase).
            - country: Country code (e.g., "NL").
            - country_name: Full country name (e.g., "Netherlands").
            - court: Court code (e.g., "HR").
            - court_name: Full court name (e.g., "Hoge Raad der Nederlanden").
            - year: Year of the decision (as integer).
            - id: The case identifier.
            - valid: Whether the ECLI is valid.
            - url: URL to the ruling (for Dutch ECLIs on rechtspraak.nl).

    Raises:
        ValueError: If the ECLI string cannot be parsed.
    """
    ecli_clean = ecli_string.strip().upper()

    # Handle common variations
    if not ecli_clean.startswith("ECLI:"):
        # Try prepending ECLI: if it looks like it was omitted
        if re.match(r"^[A-Z]{2}:[A-Z0-9]+:\d{4}:", ecli_clean):
            ecli_clean = f"ECLI:{ecli_clean}"
        else:
            raise ValueError(
                f"Invalid ECLI format: '{ecli_string}'. "
                "ECLI must start with 'ECLI:' followed by country:court:year:id."
            )

    match = ECLI_PATTERN.match(ecli_clean)
    if not match:
        raise ValueError(
            f"Invalid ECLI format: '{ecli_string}'. "
            "Expected format: ECLI:[Country]:[Court]:[Year]:[ID]"
        )

    country = match.group("country")
    court = match.group("court")
    year = int(match.group("year"))
    case_id = match.group("id")

    result = {
        "ecli": ecli_clean,
        "country": country,
        "country_name": EU_COUNTRY_CODES.get(country, f"Unknown ({country})"),
        "court": court,
        "court_name": _resolve_court_name(country, court),
        "year": year,
        "id": case_id,
        "valid": True,
    }

    # Add URL for Dutch ECLIs
    if country == "NL":
        result["url"] = f"https://uitspraken.rechtspraak.nl/details?id={ecli_clean}"
    elif country == "EU":
        result["url"] = f"https://curia.europa.eu/juris/liste.jsf?language=en&num={ecli_clean}"
    else:
        result["url"] = f"https://e-justice.europa.eu/ecli/{ecli_clean}"

    return result


def _resolve_court_name(country: str, court_code: str) -> str:
    """
    Resolve a court code to its full name.

    Args:
        country: The country code.
        court_code: The court code.

    Returns:
        The full court name, or 'Unknown' if not found.
    """
    if country == "NL":
        return DUTCH_COURT_CODES.get(court_code, f"Unknown Dutch court ({court_code})")
    elif country == "EU":
        eu_courts = {
            "C": "Court of Justice",
            "T": "General Court",
            "F": "Civil Service Tribunal",
        }
        return eu_courts.get(court_code, f"EU court ({court_code})")
    else:
        return f"Court {court_code} ({EU_COUNTRY_CODES.get(country, country)})"


def validate_ecli(ecli_string: str) -> bool:
    """
    Validate whether a string is a properly formatted ECLI identifier.

    Performs the following checks:
    1. Correct ECLI: prefix.
    2. Valid country code (2 uppercase letters).
    3. Valid court code (uppercase letters and digits).
    4. Valid year (4-digit number, reasonable range).
    5. Valid case identifier (alphanumeric with dots).

    Args:
        ecli_string: The string to validate.

    Returns:
        True if the string is a valid ECLI identifier, False otherwise.
    """
    ecli_clean = ecli_string.strip().upper()

    if not ECLI_PATTERN.match(ecli_clean):
        return False

    match = ECLI_PATTERN.match(ecli_clean)
    country = match.group("country")
    year = int(match.group("year"))

    # Validate country code
    if country not in EU_COUNTRY_CODES:
        return False

    # Validate year range (ECLI was introduced in 2011, but older cases were retroactively assigned)
    if year < 1900 or year > 2100:
        return False

    return True


def validate_ecli_detailed(ecli_string: str) -> dict:
    """
    Perform a detailed validation of an ECLI identifier with specific error messages.

    Args:
        ecli_string: The string to validate.

    Returns:
        A dictionary containing:
            - valid: Boolean indicating overall validity.
            - ecli: The cleaned ECLI string.
            - errors: List of error messages (empty if valid).
            - warnings: List of warning messages.
    """
    result = {
        "valid": True,
        "ecli": ecli_string.strip().upper(),
        "errors": [],
        "warnings": [],
    }

    ecli = result["ecli"]

    # Check prefix
    if not ecli.startswith("ECLI:"):
        result["valid"] = False
        result["errors"].append("Missing 'ECLI:' prefix.")
        return result

    parts = ecli.split(":")
    if len(parts) != 5:
        result["valid"] = False
        result["errors"].append(
            f"Expected 5 parts separated by colons, found {len(parts)}. "
            "Format: ECLI:Country:Court:Year:ID"
        )
        return result

    _, country, court, year_str, case_id = parts

    # Validate country
    if len(country) != 2 or not country.isalpha():
        result["valid"] = False
        result["errors"].append(f"Invalid country code: '{country}'. Must be 2 uppercase letters.")
    elif country not in EU_COUNTRY_CODES:
        result["valid"] = False
        result["errors"].append(
            f"Unknown country code: '{country}'. "
            f"Valid codes: {', '.join(sorted(EU_COUNTRY_CODES.keys()))}"
        )

    # Validate court
    if not court or not re.match(r"^[A-Z0-9]+$", court):
        result["valid"] = False
        result["errors"].append(f"Invalid court code: '{court}'. Must be uppercase letters/digits.")
    elif country == "NL" and court not in DUTCH_COURT_CODES:
        result["warnings"].append(
            f"Court code '{court}' is not in the known Dutch court codes list. "
            "It may be a specialized or newer court."
        )

    # Validate year
    if not year_str.isdigit() or len(year_str) != 4:
        result["valid"] = False
        result["errors"].append(f"Invalid year: '{year_str}'. Must be 4 digits.")
    else:
        year = int(year_str)
        if year < 1900:
            result["valid"] = False
            result["errors"].append(f"Year {year} is before 1900, likely invalid.")
        elif year > 2100:
            result["valid"] = False
            result["errors"].append(f"Year {year} is after 2100, likely invalid.")

    # Validate case ID
    if not case_id or not re.match(r"^[A-Za-z0-9.]+$", case_id):
        result["valid"] = False
        result["errors"].append(
            f"Invalid case identifier: '{case_id}'. "
            "Must be alphanumeric characters and dots."
        )

    return result


def format_ecli(
    country: str,
    court: str,
    year: int,
    case_id: str,
) -> str:
    """
    Format component parts into a properly formatted ECLI string.

    Args:
        country: Country code (e.g., "NL").
        court: Court code (e.g., "HR").
        year: Year of the decision.
        case_id: The case identifier.

    Returns:
        A formatted ECLI string.

    Raises:
        ValueError: If any component is invalid.
    """
    country = country.strip().upper()
    court = court.strip().upper()
    case_id = str(case_id).strip()

    # Validate components
    if len(country) != 2 or not country.isalpha():
        raise ValueError(f"Invalid country code: '{country}'. Must be 2 uppercase letters.")

    if not court or not re.match(r"^[A-Z0-9]+$", court):
        raise ValueError(f"Invalid court code: '{court}'. Must be uppercase letters/digits.")

    if not isinstance(year, int) or year < 1900 or year > 2100:
        raise ValueError(f"Invalid year: {year}. Must be between 1900 and 2100.")

    if not case_id or not re.match(r"^[A-Za-z0-9.]+$", case_id):
        raise ValueError(f"Invalid case ID: '{case_id}'. Must be alphanumeric with dots.")

    return f"ECLI:{country}:{court}:{year}:{case_id}"


def format_parsed_ecli(parsed: dict) -> str:
    """
    Format a parsed ECLI dictionary for display.

    Args:
        parsed: Dictionary from parse_ecli().

    Returns:
        Formatted multi-line string.
    """
    lines = [
        f"ECLI:         {parsed.get('ecli', 'N/A')}",
        f"Valid:        {'Yes' if parsed.get('valid') else 'No'}",
        f"Country:      {parsed.get('country', 'N/A')} ({parsed.get('country_name', 'N/A')})",
        f"Court:        {parsed.get('court', 'N/A')} ({parsed.get('court_name', 'N/A')})",
        f"Year:         {parsed.get('year', 'N/A')}",
        f"Case ID:      {parsed.get('id', 'N/A')}",
    ]
    if parsed.get("url"):
        lines.append(f"URL:          {parsed['url']}")
    return "\n".join(lines)


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Parse, validate, and format European Case Law Identifiers (ECLI).",
        epilog=(
            "Examples:\n"
            "  %(prog)s parse ECLI:NL:HR:2023:1234\n"
            "  %(prog)s validate ECLI:NL:HR:2023:1234\n"
            "  %(prog)s format --country NL --court HR --year 2023 --id 1234\n"
            "  %(prog)s courts\n"
            '  %(prog)s courts --filter amsterdam\n'
            "  %(prog)s countries"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Parse subcommand
    parse_parser = subparsers.add_parser(
        "parse", help="Parse an ECLI identifier into its components"
    )
    parse_parser.add_argument(
        "ecli", type=str, help="The ECLI identifier to parse"
    )

    # Validate subcommand
    validate_parser = subparsers.add_parser(
        "validate", help="Validate an ECLI identifier with detailed feedback"
    )
    validate_parser.add_argument(
        "ecli", type=str, help="The ECLI identifier to validate"
    )

    # Format subcommand
    format_parser = subparsers.add_parser(
        "format", help="Format components into an ECLI identifier"
    )
    format_parser.add_argument(
        "--country", type=str, required=True, help="Country code (e.g., NL)"
    )
    format_parser.add_argument(
        "--court", type=str, required=True, help="Court code (e.g., HR)"
    )
    format_parser.add_argument(
        "--year", type=int, required=True, help="Year (e.g., 2023)"
    )
    format_parser.add_argument(
        "--id", type=str, required=True, help="Case identifier (e.g., 1234)"
    )

    # Courts subcommand
    courts_parser = subparsers.add_parser(
        "courts", help="List Dutch court codes"
    )
    courts_parser.add_argument(
        "--filter",
        type=str,
        default=None,
        help="Filter courts by name (case-insensitive)",
    )

    # Countries subcommand
    subparsers.add_parser(
        "countries", help="List EU country codes used in ECLI"
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "parse":
        try:
            parsed = parse_ecli(args.ecli)
        except ValueError as e:
            print(f"Parse error: {e}", file=sys.stderr)
            sys.exit(1)

        print(format_parsed_ecli(parsed))

    elif args.command == "validate":
        result = validate_ecli_detailed(args.ecli)
        if result["valid"]:
            print(f"VALID: {result['ecli']}")
            if result["warnings"]:
                print("\nWarnings:")
                for warning in result["warnings"]:
                    print(f"  - {warning}")
        else:
            print(f"INVALID: {result['ecli']}")
            print("\nErrors:")
            for error in result["errors"]:
                print(f"  - {error}")
            if result["warnings"]:
                print("\nWarnings:")
                for warning in result["warnings"]:
                    print(f"  - {warning}")
            sys.exit(1)

    elif args.command == "format":
        try:
            ecli = format_ecli(
                country=args.country,
                court=args.court,
                year=args.year,
                case_id=args.id,
            )
        except ValueError as e:
            print(f"Format error: {e}", file=sys.stderr)
            sys.exit(1)

        print(ecli)

    elif args.command == "courts":
        print("Dutch Court Codes:")
        print("-" * 72)
        for code, name in sorted(DUTCH_COURT_CODES.items()):
            if args.filter and args.filter.lower() not in name.lower():
                continue
            print(f"  {code:<10} {name}")

    elif args.command == "countries":
        print("EU Country Codes (ECLI):")
        print("-" * 50)
        for code, name in sorted(EU_COUNTRY_CODES.items(), key=lambda x: x[1]):
            print(f"  {code}    {name}")


if __name__ == "__main__":
    main()
