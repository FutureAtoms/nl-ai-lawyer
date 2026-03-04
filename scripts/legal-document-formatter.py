#!/usr/bin/env python3
"""
legal-document-formatter.py - Format legal documents for output.

This script provides utilities for formatting various types of Dutch legal
documents into structured, readable Markdown output. It includes formatters
for legal memoranda, contract reviews, case law summaries, and automatically
appends appropriate legal disclaimers.

Usage:
    python legal-document-formatter.py memorandum --input sections.yaml
    python legal-document-formatter.py review --input clauses.yaml
    python legal-document-formatter.py case-summary --input case.yaml
    python legal-document-formatter.py disclaimer --language nl
    python legal-document-formatter.py disclaimer --language en

Input files should be in YAML format. See examples below for structure.
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Optional

try:
    import yaml
except ImportError:
    print(
        "Missing dependency: pyyaml. Install with: pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(1)


# Legal disclaimers in multiple languages
DISCLAIMERS = {
    "nl": (
        "DISCLAIMER\n"
        "\n"
        "Dit document is opgesteld met behulp van AI-ondersteunde analyse en dient "
        "uitsluitend ter informatie. Het vormt geen juridisch advies in de zin van "
        "de Advocatenwet of enige andere beroepsregulering. Aan dit document kunnen "
        "geen rechten worden ontleend.\n"
        "\n"
        "De inhoud van dit document is gebaseerd op de informatie zoals aangeleverd "
        "en het recht zoals geldend op de datum van opstelling. Er wordt geen "
        "garantie gegeven voor de juistheid, volledigheid of actualiteit van de "
        "informatie. De opsteller aanvaardt geen aansprakelijkheid voor schade die "
        "voortvloeit uit het gebruik van of het vertrouwen op dit document.\n"
        "\n"
        "Raadpleeg altijd een gekwalificeerd advocaat of juridisch adviseur voordat "
        "u op basis van dit document handelt of beslissingen neemt."
    ),
    "en": (
        "DISCLAIMER\n"
        "\n"
        "This document was prepared with the assistance of AI-powered analysis and "
        "is provided for informational purposes only. It does not constitute legal "
        "advice and does not replace the judgment of a qualified legal professional. "
        "No rights may be derived from this document.\n"
        "\n"
        "The content of this document is based on the information provided and the "
        "law as in effect on the date of preparation. No guarantee is given "
        "regarding the accuracy, completeness, or currency of the information. "
        "The author accepts no liability for any damage arising from the use of "
        "or reliance on this document.\n"
        "\n"
        "Always consult a licensed attorney before acting on the basis of this "
        "document."
    ),
    "nl_en": (
        "DISCLAIMER\n"
        "\n"
        "Dit document is opgesteld met behulp van AI-ondersteunde analyse en dient "
        "uitsluitend ter informatie. Het vormt geen juridisch advies. Aan dit "
        "document kunnen geen rechten worden ontleend. Raadpleeg altijd een "
        "gekwalificeerd advocaat of juridisch adviseur.\n"
        "\n"
        "This document was prepared with the assistance of AI-powered analysis and "
        "is provided for informational purposes only. It does not constitute legal "
        "advice. No rights may be derived from this document. Always consult a "
        "licensed attorney."
    ),
}

# Risk level styling
RISK_LEVELS = {
    "GREEN": {"label": "GREEN", "emoji": "", "description": "No material risk"},
    "YELLOW": {"label": "YELLOW", "emoji": "", "description": "Moderate risk - review recommended"},
    "RED": {"label": "RED", "emoji": "", "description": "High risk - action required"},
}


def format_memorandum(sections: dict) -> str:
    """
    Format a legal memorandum from a dictionary of sections.

    Args:
        sections: Dictionary with the following optional keys:
            - to: Recipient name and title.
            - from_: Sender name and title.
            - date: Date of the memorandum.
            - re: Subject of the memorandum.
            - reference: Reference number.
            - confidentiality: Confidentiality level.
            - issue: The legal issue(s) presented (Rechtsvraag).
            - brief_answer: Brief answer to the issue(s).
            - facts: List of relevant facts.
            - discussion: Dictionary with subsections:
                - applicable_law: Applicable legal framework.
                - case_law: Relevant case law analysis.
                - application: Application of law to facts.
            - conclusion: Conclusions.
            - recommendations: List of recommendations.
            - sources: Dictionary with keys:
                - legislation: List of legislation references.
                - case_law: List of case law references.
                - literature: List of literature references.

    Returns:
        Formatted Markdown string of the memorandum.
    """
    lines = []

    # Header
    lines.append("# MEMORANDUM")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("| | |")
    lines.append("|---|---|")
    lines.append(f"| **Aan / To:** | {sections.get('to', '[ONTVANGER]')} |")
    lines.append(f"| **Van / From:** | {sections.get('from_', sections.get('from', '[AFZENDER]'))} |")
    lines.append(f"| **Datum / Date:** | {sections.get('date', datetime.now().strftime('%d %B %Y'))} |")
    lines.append(f"| **Betreft / Re:** | {sections.get('re', '[ONDERWERP]')} |")

    if sections.get("reference"):
        lines.append(f"| **Referentie:** | {sections['reference']} |")
    if sections.get("confidentiality"):
        lines.append(f"| **Vertrouwelijkheid:** | {sections['confidentiality']} |")

    lines.append("")
    lines.append("---")

    # I. Issue Presented
    lines.append("")
    lines.append("## I. Issue Presented (Rechtsvraag)")
    lines.append("")
    issue = sections.get("issue", "[Formuleer de juridische vraag.]")
    if isinstance(issue, list):
        for i, q in enumerate(issue, 1):
            lines.append(f"**Rechtsvraag {i}:** {q}")
            lines.append("")
    else:
        lines.append(str(issue))
    lines.append("")

    # II. Brief Answer
    lines.append("---")
    lines.append("")
    lines.append("## II. Brief Answer (Kort Antwoord)")
    lines.append("")
    brief_answer = sections.get("brief_answer", "[Kort antwoord.]")
    if isinstance(brief_answer, list):
        for answer in brief_answer:
            lines.append(str(answer))
            lines.append("")
    else:
        lines.append(str(brief_answer))
    lines.append("")

    # III. Statement of Facts
    lines.append("---")
    lines.append("")
    lines.append("## III. Statement of Facts (Feiten)")
    lines.append("")
    facts = sections.get("facts", [])
    if isinstance(facts, list):
        for i, fact in enumerate(facts, 1):
            lines.append(f"{i}. {fact}")
    else:
        lines.append(str(facts))
    lines.append("")

    # IV. Discussion
    lines.append("---")
    lines.append("")
    lines.append("## IV. Discussion (Analyse)")
    lines.append("")

    discussion = sections.get("discussion", {})
    if isinstance(discussion, dict):
        # A. Applicable Law
        if discussion.get("applicable_law"):
            lines.append("### A. Applicable Law (Toepasselijk Recht)")
            lines.append("")
            lines.append(str(discussion["applicable_law"]))
            lines.append("")

        # B. Case Law
        if discussion.get("case_law"):
            lines.append("### B. Case Law Analysis (Jurisprudentie-analyse)")
            lines.append("")
            case_law = discussion["case_law"]
            if isinstance(case_law, list):
                for case in case_law:
                    if isinstance(case, dict):
                        lines.append(f"**{case.get('name', 'Unnamed')}**")
                        if case.get("ecli"):
                            lines.append(f"- **ECLI:** {case['ecli']}")
                        if case.get("date"):
                            lines.append(f"- **Datum:** {case['date']}")
                        if case.get("consideration"):
                            lines.append(f"- **Rechtsoverweging:** {case['consideration']}")
                        if case.get("relevance"):
                            lines.append(f"- **Relevantie:** {case['relevance']}")
                        lines.append("")
                    else:
                        lines.append(f"- {case}")
            else:
                lines.append(str(case_law))
            lines.append("")

        # C. Application to Facts
        if discussion.get("application"):
            lines.append("### C. Application to Facts (Toepassing op de Feiten)")
            lines.append("")
            lines.append(str(discussion["application"]))
            lines.append("")
    else:
        lines.append(str(discussion))
        lines.append("")

    # V. Conclusion
    lines.append("---")
    lines.append("")
    lines.append("## V. Conclusion (Conclusie)")
    lines.append("")
    conclusion = sections.get("conclusion", "[Conclusie.]")
    if isinstance(conclusion, list):
        for i, c in enumerate(conclusion, 1):
            lines.append(f"**Conclusie {i}:** {c}")
            lines.append("")
    else:
        lines.append(str(conclusion))
    lines.append("")

    # VI. Recommendations
    lines.append("---")
    lines.append("")
    lines.append("## VI. Recommendations (Aanbevelingen)")
    lines.append("")
    recommendations = sections.get("recommendations", [])
    if isinstance(recommendations, list):
        for i, rec in enumerate(recommendations, 1):
            lines.append(f"{i}. {rec}")
    else:
        lines.append(str(recommendations))
    lines.append("")

    # Sources
    sources = sections.get("sources", {})
    if sources:
        lines.append("---")
        lines.append("")
        lines.append("## Appendix: Sources Cited (Bijlage: Aangehaalde Bronnen)")
        lines.append("")

        if sources.get("legislation"):
            lines.append("### Wetgeving")
            lines.append("")
            lines.append("| # | Bron | Artikelen |")
            lines.append("|---|------|-----------|")
            for i, leg in enumerate(sources["legislation"], 1):
                if isinstance(leg, dict):
                    lines.append(f"| {i} | {leg.get('name', '')} | {leg.get('articles', '')} |")
                else:
                    lines.append(f"| {i} | {leg} | |")
            lines.append("")

        if sources.get("case_law"):
            lines.append("### Jurisprudentie")
            lines.append("")
            lines.append("| # | ECLI | Instantie | Datum |")
            lines.append("|---|------|-----------|-------|")
            for i, case in enumerate(sources["case_law"], 1):
                if isinstance(case, dict):
                    lines.append(
                        f"| {i} | {case.get('ecli', '')} | "
                        f"{case.get('court', '')} | {case.get('date', '')} |"
                    )
                else:
                    lines.append(f"| {i} | {case} | | |")
            lines.append("")

        if sources.get("literature"):
            lines.append("### Literatuur")
            lines.append("")
            for i, lit in enumerate(sources["literature"], 1):
                if isinstance(lit, dict):
                    lines.append(
                        f"{i}. {lit.get('author', '')}, "
                        f"*{lit.get('title', '')}*, "
                        f"{lit.get('publication', '')} ({lit.get('year', '')})."
                    )
                else:
                    lines.append(f"{i}. {lit}")
            lines.append("")

    return "\n".join(lines)


def format_contract_review(clauses: list[dict]) -> str:
    """
    Format a contract review report with risk-level color flags.

    Args:
        clauses: List of clause dictionaries, each containing:
            - name: Name or title of the clause.
            - risk: Risk level (GREEN, YELLOW, or RED).
            - issue: Description of the issue found (if any).
            - recommendation: Recommended action.
            - article: Optional article reference.

    Returns:
        Formatted Markdown string of the contract review.
    """
    lines = []

    # Header
    lines.append("# Contract Review Report / Contractbeoordeling")
    lines.append("")
    lines.append(f"**Date:** {datetime.now().strftime('%d %B %Y')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Summary counts
    green_count = sum(1 for c in clauses if c.get("risk", "").upper() == "GREEN")
    yellow_count = sum(1 for c in clauses if c.get("risk", "").upper() == "YELLOW")
    red_count = sum(1 for c in clauses if c.get("risk", "").upper() == "RED")
    total = len(clauses)

    lines.append("## Risk Summary")
    lines.append("")
    lines.append("| Risk Level | Count | Percentage |")
    lines.append("|------------|-------|------------|")
    lines.append(f"| GREEN | {green_count} | {_percentage(green_count, total)} |")
    lines.append(f"| YELLOW | {yellow_count} | {_percentage(yellow_count, total)} |")
    lines.append(f"| RED | {red_count} | {_percentage(red_count, total)} |")
    lines.append(f"| **Total** | **{total}** | **100%** |")
    lines.append("")

    # Overall assessment
    if red_count > 0:
        overall = "RED - Critical issues found. Do not execute without resolution."
    elif yellow_count > total * 0.3:
        overall = "YELLOW - Multiple moderate issues found. Review recommended."
    else:
        overall = "GREEN - No critical issues. Minor points may need attention."

    lines.append(f"**Overall Assessment:** {overall}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Clause-by-clause analysis
    lines.append("## Clause-by-Clause Analysis")
    lines.append("")
    lines.append("| # | Clause | Risk Level | Issue | Recommendation |")
    lines.append("|---|--------|------------|-------|----------------|")

    for i, clause in enumerate(clauses, 1):
        name = clause.get("name", f"Clause {i}")
        risk = clause.get("risk", "GREEN").upper()
        issue = clause.get("issue", "No issues identified.")
        recommendation = clause.get("recommendation", "No action required.")

        # Add risk level marker
        risk_display = f"**{risk}**" if risk in ("YELLOW", "RED") else risk

        lines.append(f"| {i} | {name} | {risk_display} | {issue} | {recommendation} |")

    lines.append("")

    # Detailed findings for YELLOW and RED items
    critical_clauses = [c for c in clauses if c.get("risk", "").upper() in ("YELLOW", "RED")]
    if critical_clauses:
        lines.append("---")
        lines.append("")
        lines.append("## Detailed Findings")
        lines.append("")

        for clause in critical_clauses:
            risk = clause.get("risk", "").upper()
            name = clause.get("name", "Unknown Clause")
            lines.append(f"### [{risk}] {name}")
            lines.append("")

            if clause.get("article"):
                lines.append(f"**Article Reference:** {clause['article']}")
                lines.append("")

            lines.append(f"**Issue:** {clause.get('issue', 'N/A')}")
            lines.append("")
            lines.append(f"**Recommendation:** {clause.get('recommendation', 'N/A')}")
            lines.append("")

            if clause.get("legal_basis"):
                lines.append(f"**Legal Basis:** {clause['legal_basis']}")
                lines.append("")

    return "\n".join(lines)


def format_case_summary(case_data: dict) -> str:
    """
    Format a case law summary for a Dutch court ruling.

    Args:
        case_data: Dictionary containing:
            - ecli: ECLI identifier.
            - name: Popular name of the case (if any).
            - court: Name of the court.
            - date: Date of the ruling.
            - type: Type of case (e.g., civiel, bestuursrecht, strafrecht).
            - parties: Description of parties (anonymized).
            - procedure: Type of procedure.
            - subject: Legal subject matter.
            - facts: Summary of facts.
            - legal_questions: Key legal questions addressed.
            - considerations: Key considerations of the court.
            - ruling: The court's ruling/decision.
            - significance: Significance/impact of the ruling.
            - related_cases: List of related ECLI identifiers.
            - legislation: List of relevant legislation references.

    Returns:
        Formatted Markdown string of the case summary.
    """
    lines = []

    # Header
    lines.append("# Case Law Summary / Jurisprudentie-samenvatting")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Case identification
    lines.append("## Case Identification")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| **ECLI** | {case_data.get('ecli', 'N/A')} |")

    if case_data.get("name"):
        lines.append(f"| **Naam** | {case_data['name']} |")

    lines.append(f"| **Rechterlijke Instantie** | {case_data.get('court', 'N/A')} |")
    lines.append(f"| **Datum** | {case_data.get('date', 'N/A')} |")

    if case_data.get("type"):
        lines.append(f"| **Rechtsgebied** | {case_data['type']} |")
    if case_data.get("procedure"):
        lines.append(f"| **Procedure** | {case_data['procedure']} |")

    lines.append("")

    # URL
    ecli = case_data.get("ecli", "")
    if ecli:
        lines.append(f"**Link:** [Rechtspraak.nl](https://uitspraken.rechtspraak.nl/details?id={ecli})")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Parties
    if case_data.get("parties"):
        lines.append("## Partijen")
        lines.append("")
        lines.append(str(case_data["parties"]))
        lines.append("")

    # Subject
    if case_data.get("subject"):
        lines.append("## Onderwerp")
        lines.append("")
        lines.append(str(case_data["subject"]))
        lines.append("")

    # Facts
    if case_data.get("facts"):
        lines.append("---")
        lines.append("")
        lines.append("## Feiten")
        lines.append("")
        facts = case_data["facts"]
        if isinstance(facts, list):
            for i, fact in enumerate(facts, 1):
                lines.append(f"{i}. {fact}")
        else:
            lines.append(str(facts))
        lines.append("")

    # Legal Questions
    if case_data.get("legal_questions"):
        lines.append("---")
        lines.append("")
        lines.append("## Rechtsvragen")
        lines.append("")
        questions = case_data["legal_questions"]
        if isinstance(questions, list):
            for i, q in enumerate(questions, 1):
                lines.append(f"{i}. {q}")
        else:
            lines.append(str(questions))
        lines.append("")

    # Considerations
    if case_data.get("considerations"):
        lines.append("---")
        lines.append("")
        lines.append("## Overwegingen van de Rechter")
        lines.append("")
        considerations = case_data["considerations"]
        if isinstance(considerations, list):
            for consideration in considerations:
                lines.append(f"- {consideration}")
        else:
            lines.append(str(considerations))
        lines.append("")

    # Ruling
    if case_data.get("ruling"):
        lines.append("---")
        lines.append("")
        lines.append("## Beslissing")
        lines.append("")
        lines.append(str(case_data["ruling"]))
        lines.append("")

    # Significance
    if case_data.get("significance"):
        lines.append("---")
        lines.append("")
        lines.append("## Belang van de Uitspraak")
        lines.append("")
        lines.append(str(case_data["significance"]))
        lines.append("")

    # Related cases
    if case_data.get("related_cases"):
        lines.append("---")
        lines.append("")
        lines.append("## Gerelateerde Uitspraken")
        lines.append("")
        for ecli_ref in case_data["related_cases"]:
            lines.append(f"- [{ecli_ref}](https://uitspraken.rechtspraak.nl/details?id={ecli_ref})")
        lines.append("")

    # Relevant legislation
    if case_data.get("legislation"):
        lines.append("## Relevante Wetgeving")
        lines.append("")
        legislation = case_data["legislation"]
        if isinstance(legislation, list):
            for leg in legislation:
                lines.append(f"- {leg}")
        else:
            lines.append(str(legislation))
        lines.append("")

    return "\n".join(lines)


def add_disclaimer(text: str, language: str = "nl") -> str:
    """
    Append a legal disclaimer to a document.

    Args:
        text: The document text to which the disclaimer will be appended.
        language: Language of the disclaimer. Options:
            - "nl": Dutch disclaimer.
            - "en": English disclaimer.
            - "nl_en" or "both": Bilingual Dutch/English disclaimer.

    Returns:
        The original text with the disclaimer appended.
    """
    if language in ("both", "bilingual"):
        language = "nl_en"

    disclaimer = DISCLAIMERS.get(language, DISCLAIMERS["nl"])

    separator = "\n\n---\n\n"
    timestamp = datetime.now().strftime("%d %B %Y, %H:%M")

    return f"{text}{separator}{disclaimer}\n\n*Document generated: {timestamp}*\n"


def _percentage(count: int, total: int) -> str:
    """Calculate percentage string."""
    if total == 0:
        return "0%"
    return f"{count / total * 100:.0f}%"


def _load_input_file(filepath: str) -> dict:
    """
    Load input data from a YAML or JSON file.

    Args:
        filepath: Path to the input file.

    Returns:
        Parsed data as a dictionary or list.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is not supported or parsing fails.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    if filepath.endswith((".yaml", ".yml")):
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as e:
            print(f"Error: Failed to parse YAML: {e}", file=sys.stderr)
            sys.exit(1)
    elif filepath.endswith(".json"):
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Try YAML first, then JSON
        try:
            return yaml.safe_load(content)
        except Exception:
            try:
                return json.loads(content)
            except Exception:
                print(
                    f"Error: Could not parse {filepath} as YAML or JSON.",
                    file=sys.stderr,
                )
                sys.exit(1)


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="Format Dutch legal documents for output.",
        epilog=(
            "Examples:\n"
            "  %(prog)s memorandum --input memo_sections.yaml\n"
            "  %(prog)s review --input clauses.yaml\n"
            "  %(prog)s case-summary --input case.yaml\n"
            "  %(prog)s disclaimer --language nl\n"
            "  %(prog)s memorandum --input memo.yaml --disclaimer nl --output memo.md\n"
            "\n"
            "Input file format (YAML):\n"
            "\n"
            "  For memorandum (memo_sections.yaml):\n"
            "    to: \"Mr. A. de Vries\"\n"
            "    from_: \"AI Legal Assistant\"\n"
            "    re: \"Huurovereenkomst analyse\"\n"
            "    issue: \"Is de huurovereenkomst rechtsgeldig?\"\n"
            "    brief_answer: \"Ja, mits ...\"\n"
            "    facts:\n"
            "      - \"Partijen hebben op 1 jan 2023 een huurovereenkomst gesloten.\"\n"
            "    conclusion: \"De overeenkomst is rechtsgeldig.\"\n"
            "\n"
            "  For review (clauses.yaml):\n"
            "    - name: \"Aansprakelijkheid\"\n"
            "      risk: RED\n"
            "      issue: \"Unlimited liability clause.\"\n"
            "      recommendation: \"Cap liability at contract value.\"\n"
            "    - name: \"Looptijd\"\n"
            "      risk: GREEN\n"
            "      issue: \"Standard term.\"\n"
            "      recommendation: \"No action required.\""
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Memorandum subcommand
    memo_parser = subparsers.add_parser(
        "memorandum", help="Format a legal memorandum"
    )
    memo_parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Path to YAML/JSON file with memorandum sections",
    )
    memo_parser.add_argument(
        "--disclaimer",
        type=str,
        default=None,
        choices=["nl", "en", "both"],
        help="Append disclaimer in specified language",
    )
    memo_parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path (default: stdout)",
    )

    # Review subcommand
    review_parser = subparsers.add_parser(
        "review", help="Format a contract review"
    )
    review_parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Path to YAML/JSON file with clause analysis data",
    )
    review_parser.add_argument(
        "--disclaimer",
        type=str,
        default=None,
        choices=["nl", "en", "both"],
        help="Append disclaimer in specified language",
    )
    review_parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path (default: stdout)",
    )

    # Case summary subcommand
    case_parser = subparsers.add_parser(
        "case-summary", help="Format a case law summary"
    )
    case_parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Path to YAML/JSON file with case data",
    )
    case_parser.add_argument(
        "--disclaimer",
        type=str,
        default=None,
        choices=["nl", "en", "both"],
        help="Append disclaimer in specified language",
    )
    case_parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Output file path (default: stdout)",
    )

    # Disclaimer subcommand
    disc_parser = subparsers.add_parser(
        "disclaimer", help="Print a legal disclaimer"
    )
    disc_parser.add_argument(
        "--language", "-l",
        type=str,
        default="nl",
        choices=["nl", "en", "both"],
        help="Language of the disclaimer (default: nl)",
    )

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    output = ""

    if args.command == "memorandum":
        data = _load_input_file(args.input)
        if not isinstance(data, dict):
            print("Error: Memorandum input must be a YAML/JSON object (dictionary).", file=sys.stderr)
            sys.exit(1)
        output = format_memorandum(data)
        if args.disclaimer:
            output = add_disclaimer(output, args.disclaimer)

    elif args.command == "review":
        data = _load_input_file(args.input)
        if not isinstance(data, list):
            # Check if it's a dict with a 'clauses' key
            if isinstance(data, dict) and "clauses" in data:
                data = data["clauses"]
            else:
                print(
                    "Error: Review input must be a YAML/JSON list of clauses.",
                    file=sys.stderr,
                )
                sys.exit(1)
        output = format_contract_review(data)
        if args.disclaimer:
            output = add_disclaimer(output, args.disclaimer)

    elif args.command == "case-summary":
        data = _load_input_file(args.input)
        if not isinstance(data, dict):
            print("Error: Case summary input must be a YAML/JSON object.", file=sys.stderr)
            sys.exit(1)
        output = format_case_summary(data)
        if args.disclaimer:
            output = add_disclaimer(output, args.disclaimer)

    elif args.command == "disclaimer":
        lang = args.language
        if lang == "both":
            lang = "nl_en"
        output = DISCLAIMERS.get(lang, DISCLAIMERS["nl"])

    # Output
    if hasattr(args, "output") and args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"Output written to {args.output}")
        except IOError as e:
            print(f"Error writing output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)


if __name__ == "__main__":
    main()
