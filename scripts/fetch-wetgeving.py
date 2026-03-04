#!/usr/bin/env python3
"""
fetch-wetgeving.py - Fallback script for querying Dutch legislation via the KOOP SRU API.

This script provides functionality to search Dutch legislation (wetten, besluiten,
regelingen) through the KOOP (Kennis- en Exploitatiecentrum Officiële
Overheidspublicaties) repository and retrieve specific articles from laws.

Usage:
    python fetch-wetgeving.py search "huurrecht"
    python fetch-wetgeving.py search "arbeidsovereenkomst" --collection BWB
    python fetch-wetgeving.py get BWBR0005290
    python fetch-wetgeving.py get BWBR0005290 --article 7:610

API Documentation:
    https://www.overheid.nl/opendata
    https://repository.overheid.nl/
"""

import argparse
import sys
import time
from typing import Optional
from urllib.parse import quote

try:
    import requests
    from lxml import etree
except ImportError as e:
    print(
        f"Missing dependency: {e}. Install with: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)


# KOOP SRU API endpoints
SRU_BASE = "https://repository.overheid.nl/sru"
FRBR_BASE = "https://repository.overheid.nl/frbr"

# XML namespaces used in SRU and legislation responses
NAMESPACES = {
    "sru": "http://www.loc.gov/zing/srw/",
    "sru_dc": "info:srw/schema/1/dc-v1.1",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "overheidwet": "http://standaarden.overheid.nl/wetgeving/",
    "xml": "http://www.w3.org/XML/1998/namespace",
}

# Common legislation collections
COLLECTIONS = {
    "BWB": "Basis Wetten Bestand (consolidated legislation)",
    "cvdr": "Centrale Voorziening Decentrale Regelgeving (local regulations)",
    "stb": "Staatsblad (Official Gazette - Acts)",
    "stcrt": "Staatscourant (Official Gazette - Decrees)",
    "trb": "Tractatenblad (Treaty Series)",
}

# Well-known BWB identifiers for common Dutch laws
COMMON_LAWS = {
    "BW": "BWBR0005289",           # Burgerlijk Wetboek (general)
    "BW1": "BWBR0002656",          # Burgerlijk Wetboek Boek 1
    "BW2": "BWBR0003045",          # Burgerlijk Wetboek Boek 2
    "BW3": "BWBR0005291",          # Burgerlijk Wetboek Boek 3
    "BW5": "BWBR0005288",          # Burgerlijk Wetboek Boek 5
    "BW6": "BWBR0005289",          # Burgerlijk Wetboek Boek 6
    "BW7": "BWBR0005290",          # Burgerlijk Wetboek Boek 7
    "BW8": "BWBR0005034",          # Burgerlijk Wetboek Boek 8
    "Rv": "BWBR0001827",           # Wetboek van Burgerlijke Rechtsvordering
    "Sr": "BWBR0001854",           # Wetboek van Strafrecht
    "Sv": "BWBR0001903",           # Wetboek van Strafvordering
    "Awb": "BWBR0005537",          # Algemene wet bestuursrecht
    "Wft": "BWBR0020368",          # Wet op het financieel toezicht
    "UAVG": "BWBR0040940",         # Uitvoeringswet AVG
    "Wbp": "BWBR0011468",          # Wet bescherming persoonsgegevens (replaced by UAVG)
    "WOR": "BWBR0002747",          # Wet op de ondernemingsraden
    "WWZ": "BWBR0036076",          # Wet werk en zekerheid
    "WAB": "BWBR0042578",          # Wet arbeidsmarkt in balans
}

# Rate limiting
MIN_REQUEST_INTERVAL = 0.2
_last_request_time = 0.0


def _rate_limit():
    """Enforce rate limiting to avoid overloading the API."""
    global _last_request_time
    now = time.time()
    elapsed = now - _last_request_time
    if elapsed < MIN_REQUEST_INTERVAL:
        time.sleep(MIN_REQUEST_INTERVAL - elapsed)
    _last_request_time = time.time()


def search_legislation(
    query: str,
    collection: str = "BWB",
    max_results: int = 10,
) -> list[dict]:
    """
    Search for Dutch legislation in the KOOP repository.

    Args:
        query: Search terms (e.g., "huurrecht", "arbeidsovereenkomst").
        collection: The collection to search in. Default is "BWB"
                    (consolidated legislation). See COLLECTIONS for options.
        max_results: Maximum number of results to return (default 10).

    Returns:
        A list of dictionaries, each containing:
            - title: Title of the legislation.
            - identifier: BWB or other identifier.
            - date: Date of the legislation or last modification.
            - type: Type of legislation.
            - url: URL to the full text.

    Raises:
        requests.RequestException: If the API request fails.
    """
    _rate_limit()

    # Build CQL query for SRU
    cql_query = f'"{query}"'
    if collection:
        cql_query = f"({cql_query}) AND overheidwet.collectie={collection}"

    params = {
        "operation": "searchRetrieve",
        "version": "1.2",
        "query": cql_query,
        "maximumRecords": str(max_results),
        "recordSchema": "dc",
    }

    try:
        response = requests.get(SRU_BASE, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: Request to KOOP repository timed out.", file=sys.stderr)
        raise
    except requests.exceptions.HTTPError as e:
        print(
            f"Error: KOOP repository returned HTTP {e.response.status_code}.",
            file=sys.stderr,
        )
        raise
    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to KOOP repository. Check your internet connection.",
            file=sys.stderr,
        )
        raise

    return _parse_sru_response(response.text)


def _parse_sru_response(xml_text: str) -> list[dict]:
    """
    Parse the SRU XML search response.

    Args:
        xml_text: Raw XML response string.

    Returns:
        List of parsed legislation result dictionaries.
    """
    results = []

    try:
        root = etree.fromstring(xml_text.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        print(f"Error: Failed to parse SRU XML response: {e}", file=sys.stderr)
        return results

    records = root.findall(".//sru:record", NAMESPACES)

    for record in records:
        result = {}

        record_data = record.find(".//sru:recordData", NAMESPACES)
        if record_data is None:
            continue

        # Extract Dublin Core metadata
        title_elem = record_data.find(".//dc:title", NAMESPACES)
        result["title"] = (
            title_elem.text.strip() if title_elem is not None and title_elem.text else "No title"
        )

        identifier_elem = record_data.find(".//dc:identifier", NAMESPACES)
        result["identifier"] = (
            identifier_elem.text.strip()
            if identifier_elem is not None and identifier_elem.text
            else "Unknown"
        )

        date_elem = record_data.find(".//dc:date", NAMESPACES)
        result["date"] = (
            date_elem.text.strip() if date_elem is not None and date_elem.text else "Unknown"
        )

        type_elem = record_data.find(".//dc:type", NAMESPACES)
        result["type"] = (
            type_elem.text.strip() if type_elem is not None and type_elem.text else "Unknown"
        )

        # Construct URL
        if result["identifier"].startswith("BWB"):
            result["url"] = f"https://wetten.overheid.nl/{result['identifier']}"
        else:
            result["url"] = f"https://repository.overheid.nl/{result['identifier']}"

        results.append(result)

    return results


def get_article(
    bwb_id: str,
    article_number: Optional[str] = None,
) -> dict:
    """
    Retrieve the full text of a law or a specific article from the KOOP repository.

    Args:
        bwb_id: The BWB identifier (e.g., "BWBR0005290" for Burgerlijk Wetboek Boek 7).
                Can also be a common abbreviation (e.g., "BW7") which will be
                automatically resolved.
        article_number: Optional specific article number (e.g., "610", "7:610").
                       If not provided, retrieves the full law text.

    Returns:
        A dictionary containing:
            - bwb_id: The BWB identifier.
            - title: Title of the legislation.
            - article: The requested article number (if specified).
            - text: The full text or article text.
            - url: URL to the legislation on wetten.overheid.nl.

    Raises:
        requests.RequestException: If the API request fails.
    """
    # Resolve common abbreviations
    if bwb_id.upper() in COMMON_LAWS:
        bwb_id = COMMON_LAWS[bwb_id.upper()]

    _rate_limit()

    # Build the URL to fetch from wetten.overheid.nl (XML format)
    if article_number:
        url = f"https://wetten.overheid.nl/xml.php?regelingID={bwb_id}&artikel={quote(article_number)}"
    else:
        url = f"https://wetten.overheid.nl/xml.php?regelingID={bwb_id}"

    result = {
        "bwb_id": bwb_id,
        "title": "",
        "article": article_number,
        "text": "",
        "url": f"https://wetten.overheid.nl/{bwb_id}",
    }

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: Request timed out.", file=sys.stderr)
        raise
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Error: Legislation {bwb_id} not found.", file=sys.stderr)
        else:
            print(
                f"Error: Server returned HTTP {e.response.status_code}.",
                file=sys.stderr,
            )
        raise
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to wetten.overheid.nl.", file=sys.stderr)
        raise

    # Parse the XML response
    try:
        root = etree.fromstring(response.content)
    except etree.XMLSyntaxError as e:
        print(f"Error: Failed to parse XML: {e}", file=sys.stderr)
        result["text"] = response.text
        return result

    # Extract title
    title_elem = root.find(".//wetgeving/intitule")
    if title_elem is None:
        title_elem = root.find(".//intitule")
    if title_elem is not None and title_elem.text:
        result["title"] = title_elem.text.strip()

    # Extract article or full text
    if article_number:
        result["text"] = _extract_article(root, article_number)
    else:
        result["text"] = _extract_full_text(root)

    return result


def _extract_article(root, article_number: str) -> str:
    """
    Extract a specific article from parsed legislation XML.

    Args:
        root: The parsed XML root element.
        article_number: The article number to find.

    Returns:
        The text of the article, or an error message if not found.
    """
    # Look for artikel elements
    for artikel in root.iter("artikel"):
        kop = artikel.find("kop")
        if kop is not None:
            nr_elem = kop.find("nr")
            label_elem = kop.find("label")
            if nr_elem is not None and nr_elem.text:
                if nr_elem.text.strip() == article_number:
                    return _extract_text_from_element(artikel)

    # Fallback: try searching in the raw text
    return f"Article {article_number} not found in the document. Try retrieving the full text without --article."


def _extract_full_text(root) -> str:
    """
    Extract the full text of a law from parsed XML.

    Args:
        root: The parsed XML root element.

    Returns:
        The full text of the legislation.
    """
    parts = []

    for artikel in root.iter("artikel"):
        kop = artikel.find("kop")
        if kop is not None:
            label = kop.find("label")
            nr = kop.find("nr")
            titel = kop.find("titel")
            header_parts = []
            if label is not None and label.text:
                header_parts.append(label.text.strip())
            if nr is not None and nr.text:
                header_parts.append(nr.text.strip())
            if titel is not None and titel.text:
                header_parts.append(f"- {titel.text.strip()}")
            if header_parts:
                parts.append(" ".join(header_parts))

        text = _extract_text_from_element(artikel)
        if text:
            parts.append(text)
        parts.append("")  # Blank line between articles

    if not parts:
        # Fallback: extract all text
        return _extract_text_from_element(root)

    return "\n".join(parts)


def _extract_text_from_element(element) -> str:
    """
    Recursively extract text from an XML element.

    Args:
        element: An lxml element.

    Returns:
        Concatenated text content.
    """
    parts = []
    if element.text:
        parts.append(element.text.strip())
    for child in element:
        child_text = _extract_text_from_element(child)
        if child_text:
            parts.append(child_text)
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(filter(None, parts))


def format_search_result(result: dict) -> str:
    """
    Format a search result for display.

    Args:
        result: A search result dictionary.

    Returns:
        Formatted string representation.
    """
    lines = [
        f"Title:      {result.get('title', 'N/A')}",
        f"Identifier: {result.get('identifier', 'N/A')}",
        f"Date:       {result.get('date', 'N/A')}",
        f"Type:       {result.get('type', 'N/A')}",
        f"URL:        {result.get('url', 'N/A')}",
    ]
    return "\n".join(lines)


def format_article_result(result: dict) -> str:
    """
    Format a legislation retrieval result for display.

    Args:
        result: An article result dictionary.

    Returns:
        Formatted string representation.
    """
    separator = "=" * 72
    lines = [
        separator,
        f"BWB ID:     {result.get('bwb_id', 'N/A')}",
        f"Title:      {result.get('title', 'N/A')}",
    ]
    if result.get("article"):
        lines.append(f"Article:    {result['article']}")
    lines.extend([
        f"URL:        {result.get('url', 'N/A')}",
        separator,
        "",
        result.get("text", "No text available."),
        "",
        separator,
    ])
    return "\n".join(lines)


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Search and retrieve Dutch legislation from the KOOP SRU API.",
        epilog=(
            "Examples:\n"
            '  %(prog)s search "huurrecht"\n'
            '  %(prog)s search "arbeidsovereenkomst" --collection BWB\n'
            "  %(prog)s get BWBR0005290\n"
            "  %(prog)s get BW7 --article 610\n"
            "  %(prog)s get BWBR0005290 --article 7:610\n"
            "  %(prog)s collections\n"
            "  %(prog)s laws"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Search subcommand
    search_parser = subparsers.add_parser(
        "search", help="Search for legislation"
    )
    search_parser.add_argument(
        "query", type=str, help="Search query terms"
    )
    search_parser.add_argument(
        "--collection",
        type=str,
        default="BWB",
        help="Collection to search (default: BWB). Use 'collections' command to list.",
    )
    search_parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum number of results (default: 10)",
    )

    # Get subcommand
    get_parser = subparsers.add_parser(
        "get", help="Retrieve a specific law or article"
    )
    get_parser.add_argument(
        "bwb_id",
        type=str,
        help="BWB identifier (e.g., BWBR0005290) or abbreviation (e.g., BW7)",
    )
    get_parser.add_argument(
        "--article",
        type=str,
        default=None,
        help="Specific article number (e.g., 610, 7:610)",
    )

    # Collections subcommand
    subparsers.add_parser(
        "collections", help="List available legislation collections"
    )

    # Laws subcommand
    subparsers.add_parser(
        "laws", help="List common Dutch law abbreviations and their BWB IDs"
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "collections":
        print("Available Legislation Collections:")
        print("-" * 60)
        for code, description in sorted(COLLECTIONS.items()):
            print(f"  {code:<10} {description}")
        sys.exit(0)

    if args.command == "laws":
        print("Common Dutch Laws (abbreviation -> BWB ID):")
        print("-" * 60)
        for abbrev, bwb_id in sorted(COMMON_LAWS.items()):
            print(f"  {abbrev:<10} {bwb_id}")
        sys.exit(0)

    if args.command == "search":
        try:
            results = search_legislation(
                query=args.query,
                collection=args.collection,
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
            print(format_search_result(result))
            print()

    elif args.command == "get":
        try:
            result = get_article(
                bwb_id=args.bwb_id,
                article_number=args.article,
            )
        except Exception as e:
            print(f"Failed to retrieve legislation: {e}", file=sys.stderr)
            sys.exit(1)

        print(format_article_result(result))


if __name__ == "__main__":
    main()
