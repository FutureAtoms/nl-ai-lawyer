#!/usr/bin/env python3
"""
fetch-rechtspraak.py - Fallback script for querying the Rechtspraak.nl API.

This script provides functionality to search Dutch court rulings and retrieve
full ruling texts from the open data API at data.rechtspraak.nl.

Usage:
    python fetch-rechtspraak.py search "huurovereenkomst ontbinding"
    python fetch-rechtspraak.py search "arbeidsrecht" --court HR --max-results 5
    python fetch-rechtspraak.py get ECLI:NL:HR:2023:123

API Documentation:
    https://www.rechtspraak.nl/Uitspraken/paginas/open-data.aspx
"""

import argparse
import sys
import time
import xml.etree.ElementTree as ET
from typing import Optional

try:
    import requests
    from lxml import etree
except ImportError as e:
    print(
        f"Missing dependency: {e}. Install with: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)


# Rechtspraak.nl Open Data API endpoints
SEARCH_ENDPOINT = "https://data.rechtspraak.nl/uitspraken/zoeken"
CONTENT_ENDPOINT = "https://data.rechtspraak.nl/uitspraken/content"

# XML namespaces used in Rechtspraak responses
NAMESPACES = {
    "feed": "http://www.w3.org/2005/Atom",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dcterms": "http://purl.org/dc/terms/",
    "psi": "http://psi.rechtspraak.nl/",
    "rs": "http://www.rechtspraak.nl/schema/rechtspraak-1.0",
}

# Rate limiting: maximum 5 requests per second
MIN_REQUEST_INTERVAL = 0.2  # 200ms between requests
_last_request_time = 0.0


def _rate_limit():
    """Enforce rate limiting of 5 requests per second."""
    global _last_request_time
    now = time.time()
    elapsed = now - _last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - elapsed)
    _last_request_time = time.time()


def search_cases(
    query: str,
    court: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    max_results: int = 10,
) -> list[dict]:
    """
    Search for court rulings on Rechtspraak.nl.

    Args:
        query: Search terms (e.g., "huurovereenkomst ontbinding").
        court: Court code filter (e.g., "HR" for Hoge Raad, "RBAMS" for
               Rechtbank Amsterdam). See COURT_CODES for full mapping.
        date_from: Start date filter in YYYY-MM-DD format.
        date_to: End date filter in YYYY-MM-DD format.
        max_results: Maximum number of results to return (default 10).

    Returns:
        A list of dictionaries, each containing:
            - ecli: The ECLI identifier of the ruling.
            - title: Title or summary of the ruling.
            - date: Date of the ruling.
            - court: Name of the court.
            - link: URL to the full ruling on rechtspraak.nl.

    Raises:
        requests.RequestException: If the API request fails.
        ValueError: If the response cannot be parsed.
    """
    _rate_limit()

    params = {
        "q": query,
        "max": str(max_results),
        "return": "DOC",
        "sort": "date DESC",
    }

    if court:
        params["creator"] = court
    if date_from:
        params["date"] = date_from
        if date_to:
            params["date"] = f"{date_from} TO {date_to}"

    try:
        response = requests.get(SEARCH_ENDPOINT, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: Request to Rechtspraak.nl timed out.", file=sys.stderr)
        raise
    except requests.exceptions.HTTPError as e:
        print(
            f"Error: Rechtspraak.nl returned HTTP {e.response.status_code}.",
            file=sys.stderr,
        )
        raise
    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to Rechtspraak.nl. Check your internet connection.",
            file=sys.stderr,
        )
        raise

    results = _parse_search_response(response.text)
    return results


def _parse_search_response(xml_text: str) -> list[dict]:
    """
    Parse the Atom XML search response from Rechtspraak.nl.

    Args:
        xml_text: Raw XML response string.

    Returns:
        List of parsed result dictionaries.
    """
    results = []

    try:
        root = etree.fromstring(xml_text.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        print(f"Error: Failed to parse XML response: {e}", file=sys.stderr)
        return results

    entries = root.findall("feed:entry", NAMESPACES)

    for entry in entries:
        result = {}

        # Extract ECLI from the id element
        id_elem = entry.find("feed:id", NAMESPACES)
        result["ecli"] = id_elem.text.strip() if id_elem is not None else "Unknown"

        # Extract title
        title_elem = entry.find("feed:title", NAMESPACES)
        result["title"] = (
            title_elem.text.strip() if title_elem is not None else "No title"
        )

        # Extract date
        updated_elem = entry.find("feed:updated", NAMESPACES)
        result["date"] = (
            updated_elem.text.strip()[:10] if updated_elem is not None else "Unknown"
        )

        # Extract court from summary or content
        summary_elem = entry.find("feed:summary", NAMESPACES)
        result["court"] = (
            summary_elem.text.strip()
            if summary_elem is not None
            else "Unknown court"
        )

        # Extract link
        link_elem = entry.find("feed:link", NAMESPACES)
        result["link"] = (
            link_elem.get("href", "") if link_elem is not None else ""
        )

        results.append(result)

    return results


def get_ruling(ecli: str) -> dict:
    """
    Fetch the full text and metadata of a court ruling by its ECLI identifier.

    Args:
        ecli: The ECLI identifier (e.g., "ECLI:NL:HR:2023:123").

    Returns:
        A dictionary containing:
            - ecli: The ECLI identifier.
            - title: Title of the ruling.
            - court: Name of the issuing court.
            - date: Date of the ruling.
            - type: Type of procedure.
            - text: Full text of the ruling.
            - source_url: URL to the original document.

    Raises:
        requests.RequestException: If the API request fails.
        ValueError: If the ECLI format is invalid.
    """
    if not ecli.startswith("ECLI:"):
        raise ValueError(f"Invalid ECLI format: {ecli}. Must start with 'ECLI:'.")

    _rate_limit()

    params = {"id": ecli}

    try:
        response = requests.get(CONTENT_ENDPOINT, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: Request to Rechtspraak.nl timed out.", file=sys.stderr)
        raise
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Ruling {ecli} not found.", file=sys.stderr)
        else:
            print(
                f"Error: Rechtspraak.nl returned HTTP {e.response.status_code}.",
                file=sys.stderr,
            )
        raise
    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to Rechtspraak.nl.",
            file=sys.stderr,
        )
        raise

    return _parse_ruling_response(response.text, ecli)


def _parse_ruling_response(xml_text: str, ecli: str) -> dict:
    """
    Parse the full ruling XML response.

    Args:
        xml_text: Raw XML response string.
        ecli: The requested ECLI identifier.

    Returns:
        Dictionary with ruling metadata and full text.
    """
    ruling = {
        "ecli": ecli,
        "title": "",
        "court": "",
        "date": "",
        "type": "",
        "text": "",
        "source_url": f"https://uitspraken.rechtspraak.nl/details?id={ecli}",
    }

    try:
        root = etree.fromstring(xml_text.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        print(f"Error: Failed to parse ruling XML: {e}", file=sys.stderr)
        ruling["text"] = xml_text  # Return raw text as fallback
        return ruling

    # Try to extract metadata from RDF or Dublin Core elements
    title_elem = root.find(".//dcterms:title", NAMESPACES)
    if title_elem is not None:
        ruling["title"] = title_elem.text.strip()

    creator_elem = root.find(".//dcterms:creator", NAMESPACES)
    if creator_elem is not None:
        ruling["court"] = creator_elem.text.strip()

    date_elem = root.find(".//dcterms:date", NAMESPACES)
    if date_elem is not None:
        ruling["date"] = date_elem.text.strip()

    type_elem = root.find(".//dcterms:type", NAMESPACES)
    if type_elem is not None:
        ruling["type"] = type_elem.text.strip()

    # Extract the full text from various possible elements
    text_parts = []

    # Try Rechtspraak schema elements
    for section_tag in [
        "rs:uitspraak",
        "rs:conclusie",
        "rs:paragraaf",
        "rs:parablock",
    ]:
        for elem in root.iter("{http://www.rechtspraak.nl/schema/rechtspraak-1.0}" + section_tag.split(":")[1]):
            text = _extract_text_recursive(elem)
            if text:
                text_parts.append(text)

    # Fallback: extract all text content
    if not text_parts:
        text = _extract_text_recursive(root)
        if text:
            text_parts.append(text)

    ruling["text"] = "\n\n".join(text_parts)

    return ruling


def _extract_text_recursive(element) -> str:
    """
    Recursively extract text content from an XML element and its children.

    Args:
        element: An lxml element.

    Returns:
        Concatenated text content.
    """
    parts = []
    if element.text:
        parts.append(element.text.strip())
    for child in element:
        child_text = _extract_text_recursive(child)
        if child_text:
            parts.append(child_text)
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(parts)


def format_result(result: dict) -> str:
    """
    Format a search result for display.

    Args:
        result: A search result dictionary.

    Returns:
        Formatted string representation.
    """
    lines = [
        f"ECLI:    {result.get('ecli', 'N/A')}",
        f"Title:   {result.get('title', 'N/A')}",
        f"Date:    {result.get('date', 'N/A')}",
        f"Court:   {result.get('court', 'N/A')}",
        f"Link:    {result.get('link', 'N/A')}",
    ]
    return "\n".join(lines)


def format_ruling(ruling: dict) -> str:
    """
    Format a full ruling for display.

    Args:
        ruling: A ruling dictionary.

    Returns:
        Formatted string representation.
    """
    separator = "=" * 72
    lines = [
        separator,
        f"ECLI:    {ruling.get('ecli', 'N/A')}",
        f"Title:   {ruling.get('title', 'N/A')}",
        f"Court:   {ruling.get('court', 'N/A')}",
        f"Date:    {ruling.get('date', 'N/A')}",
        f"Type:    {ruling.get('type', 'N/A')}",
        f"Source:  {ruling.get('source_url', 'N/A')}",
        separator,
        "",
        ruling.get("text", "No text available."),
        "",
        separator,
    ]
    return "\n".join(lines)


# Dutch court code mapping
COURT_CODES = {
    "HR": "Hoge Raad der Nederlanden",
    "GHAMS": "Gerechtshof Amsterdam",
    "GHARL": "Gerechtshof Arnhem-Leeuwarden",
    "GHDHA": "Gerechtshof Den Haag",
    "GHSHE": "Gerechtshof 's-Hertogenbosch",
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
    "CRVB": "Centrale Raad van Beroep",
    "CBB": "College van Beroep voor het bedrijfsleven",
    "RVS": "Raad van State",
    "PHR": "Parket bij de Hoge Raad",
}


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Search and retrieve Dutch court rulings from Rechtspraak.nl.",
        epilog=(
            "Examples:\n"
            '  %(prog)s search "huurovereenkomst ontbinding"\n'
            '  %(prog)s search "arbeidsrecht" --court HR --max-results 5\n'
            '  %(prog)s search "AVG datalek" --date-from 2023-01-01\n'
            "  %(prog)s get ECLI:NL:HR:2023:123\n"
            "  %(prog)s courts"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search subcommand
    search_parser = subparsers.add_parser(
        "search", help="Search for court rulings"
    )
    search_parser.add_argument(
        "query", type=str, help="Search query terms"
    )
    search_parser.add_argument(
        "--court",
        type=str,
        default=None,
        help="Filter by court code (e.g., HR, RBAMS, GHAMS). Use 'courts' command to list codes.",
    )
    search_parser.add_argument(
        "--date-from",
        type=str,
        default=None,
        help="Start date filter (YYYY-MM-DD)",
    )
    search_parser.add_argument(
        "--date-to",
        type=str,
        default=None,
        help="End date filter (YYYY-MM-DD)",
    )
    search_parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum number of results (default: 10)",
    )

    # Get subcommand
    get_parser = subparsers.add_parser(
        "get", help="Fetch a full ruling by ECLI identifier"
    )
    get_parser.add_argument(
        "ecli", type=str, help="ECLI identifier (e.g., ECLI:NL:HR:2023:123)"
    )

    # Courts subcommand
    subparsers.add_parser(
        "courts", help="List available Dutch court codes"
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "courts":
        print("Dutch Court Codes:")
        print("-" * 60)
        for code, name in sorted(COURT_CODES.items()):
            print(f"  {code:<10} {name}")
        sys.exit(0)

    if args.command == "search":
        try:
            results = search_cases(
                query=args.query,
                court=args.court,
                date_from=args.date_from,
                date_to=args.date_to,
                max_results=args.max_results,
            )
        except Exception as e:
            print(f"Search failed: {e}", file=sys.stderr)
            sys.exit(1)

        if not results:
            print("No results found.")
            sys.exit(0)

        print(f"Found {len(results)} result(s):\n")
        for i, result in enumerate(results, 1):
            print(f"--- Result {i} ---")
            print(format_result(result))
            print()

    elif args.command == "get":
        try:
            ruling = get_ruling(args.ecli)
        except ValueError as e:
            print(f"Invalid input: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Failed to fetch ruling: {e}", file=sys.stderr)
            sys.exit(1)

        print(format_ruling(ruling))


if __name__ == "__main__":
    main()
