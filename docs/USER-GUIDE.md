# Netherlands AI Lawyer System - User Guide

## Table of Contents

1. [Getting Started](#getting-started)
2. [Quick Start: Your First Query](#quick-start)
3. [Slash Commands Reference](#slash-commands)
4. [Domain Skills](#domain-skills)
5. [Multi-Agent Teams](#multi-agent-teams)
6. [MCP Server & API Tools](#mcp-tools)
7. [Python Utility Scripts](#python-scripts)
8. [Templates](#templates)
9. [Organization Configuration](#org-config)
10. [Tips & Best Practices](#tips)
11. [Troubleshooting](#troubleshooting)

---

<a name="getting-started"></a>
## 1. Getting Started

### Prerequisites

- **Claude Code CLI** installed and configured
- **Node.js 18+** (for the custom MCP server)
- **Python 3.10+** (for utility scripts)
- Internet connection (for live API access to Dutch legal databases)

### Installation

```bash
# 1. Navigate to the plugin
cd ~/uncloud/nl-ai-lawyer

# 2. Build the custom MCP server
cd dutch-legal-mcp
npm install
npm run build
cd ..

# 3. Install Python dependencies
pip install -r scripts/requirements.txt

# 4. (Optional) Set KVK API key for company registry lookups
export KVK_API_KEY=your_key_here
# Get a key at https://developers.kvk.nl/ (EUR 6.40/month + EUR 0.02/query)

# 5. (Optional) Configure your organization preferences
cp assets/user-config-template.md .claude/nl-ai-lawyer.local.md
# Edit .claude/nl-ai-lawyer.local.md with your settings
```

### Verify Installation

```bash
# Check MCP server compiles
cd dutch-legal-mcp && npm run build && echo "MCP server OK" && cd ..

# Check Python scripts
python3 scripts/ecli-parser.py validate "ECLI:NL:HR:2023:123"
```

---

<a name="quick-start"></a>
## 2. Quick Start: Your First Query

Once installed, you can immediately use slash commands in Claude Code:

```
/search-rechtspraak "aansprakelijkheid bestuurder BV"
```

This searches Dutch case law for director liability cases and returns results with ECLI citations.

### Example Workflows

**Review a contract:**
```
/review-contract "paste your contract text here or provide file path"
```

**Quick NDA screening:**
```
/triage-nda "paste NDA text here"
```

**Look up a law:**
```
/search-wetgeving "Burgerlijk Wetboek Boek 2 artikel 9"
```

**Check a company:**
```
/company-check "Shell Nederland BV"
```

---

<a name="slash-commands"></a>
## 3. Slash Commands Reference

### `/review-contract` - Contract Review

Reviews a Dutch contract clause-by-clause with risk flags.

**Usage:**
```
/review-contract <contract text or file path>
```

**Optional arguments:**
- `position` - Your role: buyer, seller, licensor, licensee, employer, employee

**What you get:**
- Each clause flagged as **GREEN** (standard/favorable), **YELLOW** (needs attention), or **RED** (high risk)
- BW article references for each issue
- Missing clauses identified
- Summary with recommended changes

**Example:**
```
/review-contract --position buyer "This Software License Agreement..."
```

---

### `/triage-nda` - NDA Pre-Screening

Rapid screening of an NDA (geheimhoudingsovereenkomst).

**Usage:**
```
/triage-nda <NDA text or file path>
```

**Optional arguments:**
- `type` - "mutual" or "unilateral"

**Checks performed:**
- Definition of confidential information (too broad? too narrow?)
- Term and duration
- Penalty clause (boetebeding) - reasonable amount?
- Carve-outs (legally compelled disclosure, public domain, prior knowledge)
- Return/destruction obligations
- Governing law and dispute resolution

---

### `/search-rechtspraak` - Search Case Law

Search the Dutch case law database (500K+ rulings).

**Usage:**
```
/search-rechtspraak <search terms>
```

**Optional arguments:**
- `court` - Filter by court (e.g., "Hoge Raad", "Gerechtshof Amsterdam", "Rechtbank Den Haag")
- `date_from` - Start date (YYYY-MM-DD)
- `date_to` - End date (YYYY-MM-DD)

**Examples:**
```
/search-rechtspraak "bestuurdersaansprakelijkheid Beklamel"
/search-rechtspraak "huurprijsherziening 290-bedrijfsruimte" --court "Hoge Raad" --date_from 2020-01-01
```

**Returns:** ECLI-cited results with court, date, and summary.

---

### `/search-wetgeving` - Search Legislation

Search Dutch legislation from the official BWB/CVDR databases.

**Usage:**
```
/search-wetgeving <law name or search terms>
```

**Optional arguments:**
- `area` - Legal area filter

**Examples:**
```
/search-wetgeving "Burgerlijk Wetboek Boek 7 titel 10"
/search-wetgeving "proeftijd arbeidsovereenkomst"
/search-wetgeving "Wet bescherming bedrijfsgeheimen"
```

---

### `/company-check` - KVK Company Lookup

Look up a company in the Dutch Chamber of Commerce (KVK) registry.

**Usage:**
```
/company-check <company name or KVK number>
```

**Requires:** `KVK_API_KEY` environment variable.

**Returns:** Company name, KVK number, legal form, registered address, directors, trade names, SBI codes.

**Examples:**
```
/company-check "Booking.com BV"
/company-check 34051424
```

---

### `/gdpr-check` - AVG/GDPR Compliance Assessment

Assess a data processing activity against Dutch GDPR (AVG/UAVG) requirements.

**Usage:**
```
/gdpr-check <description of data processing>
```

**Optional arguments:**
- `scope` - "quick" (high-level) or "full" (comprehensive)

**Covers:**
- Legal basis assessment
- Special categories check (health, biometric, etc.)
- DPIA requirement analysis
- International transfer compliance (Schrems II)
- Verwerkersovereenkomst (data processing agreement) requirements
- AP (Autoriteit Persoonsgegevens) enforcement risk

**Example:**
```
/gdpr-check "We collect user email, location, and health data in our fitness app and share it with a US analytics provider"
```

---

### `/brief` - Legal Briefing

Generate a structured legal briefing on any Dutch law topic.

**Usage:**
```
/brief <legal topic>
```

**Optional arguments:**
- `depth` - "summary" (1-2 pages) or "detailed" (comprehensive)

**Example:**
```
/brief "Director liability in Dutch corporate law" --depth detailed
```

---

### `/draft-contract` - Generate Contract

Generate a Dutch contract from your requirements.

**Usage:**
```
/draft-contract --type <contract type> <requirements>
```

**Contract types:**
- `arbeidsovereenkomst` - Employment contract
- `huurovereenkomst` - Lease agreement
- `koopovereenkomst` - Purchase agreement
- `dienstverlening` - Service agreement
- `geheimhoudingsovereenkomst` - NDA
- `verwerkersovereenkomst` - Data processing agreement

**Optional arguments:**
- `language` - "nl" (Dutch, default) or "en" (English)

**Example:**
```
/draft-contract --type arbeidsovereenkomst "Senior developer, EUR 85,000/year, 40 hours/week, 1 year fixed-term, 1 month probation, Amsterdam office"
```

**Important:** Generated contracts are templates only. Always have them reviewed by a qualified Dutch lawyer before use.

---

### `/legal-memo` - Legal Memorandum

Write a structured legal memorandum.

**Usage:**
```
/legal-memo <legal question>
```

**Optional arguments:**
- `facts` - Relevant facts for the analysis

**Output structure:**
1. Issue Presented (Rechtsvraag)
2. Brief Answer (Kort Antwoord)
3. Statement of Facts (Feiten)
4. Discussion (Analyse) - with law, case law, and application
5. Conclusion (Conclusie)
6. Recommendations (Aanbevelingen)

**Example:**
```
/legal-memo "Can a Dutch BV director be held personally liable for unpaid VAT?" --facts "The BV has been insolvent for 6 months. The director did not notify the Belastingdienst of the inability to pay."
```

---

### `/arbeidsrecht` - Employment Law Query

Answer employment law questions with Dutch legal framework.

**Usage:**
```
/arbeidsrecht <question>
```

**Optional arguments:**
- `context` - "employer" or "employee" perspective

**Examples:**
```
/arbeidsrecht "What are the rules for a non-compete clause in a fixed-term contract?"
/arbeidsrecht "How is transitievergoeding calculated for 10 years of service?" --context employee
```

---

### `/respond` - Templated Legal Response

Generate formal legal response documents.

**Usage:**
```
/respond --type <response type> <details>
```

**Response types:**
- `dsar` - Data Subject Access Request response (AVG art. 15)
- `discovery-hold` - Litigation hold notice
- `bezwaar` - Administrative objection letter
- `ingebrekestelling` - Notice of default
- `sommatiebrief` - Demand letter

**Optional arguments:**
- `language` - "nl" (default) or "en"

**Example:**
```
/respond --type ingebrekestelling "Contractor BV has not delivered the software module due on January 15, 2024, as agreed in the service agreement dated October 1, 2023"
```

---

### `/kamervragen` - Parliamentary Questions

Search Dutch parliamentary questions and debates.

**Usage:**
```
/kamervragen <search terms>
```

**Optional arguments:**
- `period` - Time period filter

**Example:**
```
/kamervragen "artificial intelligence regulation"
/kamervragen "woningmarkt huurprijzen" --period "2024"
```

---

<a name="domain-skills"></a>
## 4. Domain Skills

Skills are invoked automatically by Claude when relevant to your query. You don't need to call them manually - they activate when the AI detects your question falls within their domain.

### The 14 Legal Domains

| # | Skill | What It Covers |
|---|-------|---------------|
| 1 | **dutch-contract-review** | Clause-by-clause review against BW Boek 6/7, GREEN/YELLOW/RED flags |
| 2 | **dutch-case-law-research** | Search & analyze rulings via ECLI, court hierarchy, search strategies |
| 3 | **dutch-legislation-lookup** | Retrieve & explain laws from BWB/CVDR databases |
| 4 | **dutch-corporate-law** | BV/NV formation, governance, M&A, KVK, Boek 2 BW |
| 5 | **dutch-employment-law** | Contracts, dismissal, CAO, WAB/WWZ, works councils |
| 6 | **dutch-privacy-gdpr** | AVG/UAVG, DPIA, verwerkersovereenkomst, AP enforcement |
| 7 | **dutch-ip-law** | Copyright (Auteurswet), patents (ROW), Benelux trademarks, trade secrets |
| 8 | **dutch-real-estate-law** | Purchase agreements, rental law, kadaster, erfpacht |
| 9 | **dutch-tax-law** | VPB, BTW/VAT, loonbelasting, 30% ruling, fiscale eenheid |
| 10 | **dutch-administrative-law** | AWB procedures, bezwaar/beroep, government liability |
| 11 | **dutch-criminal-law** | Wetboek van Strafrecht, WED, corporate criminal liability |
| 12 | **dutch-immigration-law** | Residence permits, kennismigrant, IND procedures |
| 13 | **eu-law-integration** | EU law supremacy in NL, directives, CJEU preliminary rulings |
| 14 | **nda-triage-nl** | Rapid NDA/geheimhoudingsovereenkomst screening |

### How Skills Work

Each skill contains:
- **SKILL.md** - The main workflow and instructions
- **references/** - Detailed legal reference documents with article numbers, procedures, and key concepts

When you ask a legal question, the relevant skill(s) activate automatically and guide the AI to:
1. Identify the applicable legal framework
2. Search relevant legislation and case law via MCP tools
3. Apply the analysis to your specific situation
4. Cite sources (BW articles, ECLI numbers, etc.)
5. Append mandatory disclaimers

### Example: How the dutch-corporate-law Skill Activates

When you ask: *"I want to set up a Dutch BV with two co-founders"*

The skill automatically:
1. References BV formation requirements from `references/bv-nv-structure.md`
2. Checks Boek 2 BW provisions from `references/boek-2-bw.md`
3. Suggests governance structure from `references/corporate-governance-code.md`
4. Notes KVK registration requirements from `references/kvk-registration.md`
5. Uses MCP tools to look up relevant case law and current legislation

---

<a name="multi-agent-teams"></a>
## 5. Multi-Agent Teams

For complex legal matters that span multiple domains, the system can deploy a team of specialized agents working in parallel.

### The 7 Agents

| Agent | Specialty |
|-------|-----------|
| **legal-researcher** | Team lead - triages, coordinates, synthesizes |
| **corporate-counsel** | BV/NV, governance, M&A, KVK |
| **contract-reviewer** | Contract review & drafting |
| **litigation-researcher** | Case law, court procedures |
| **compliance-officer** | GDPR/AVG, regulatory compliance |
| **tax-advisor** | Corporate tax, VAT, international tax |
| **employment-counsel** | Employment contracts, dismissal, CAO |

### When Teams Activate

Teams are deployed for complex queries that span multiple legal domains. For example:

**"Analyze the legal implications of acquiring a Dutch BV with 50 employees and EU customer data"**

This triggers a full team:

```
legal-researcher (lead)
  ├── corporate-counsel    → BV structure, KVK due diligence, SPA
  ├── contract-reviewer    → SPA review, representations & warranties
  ├── litigation-researcher → Litigation history, pending cases
  ├── compliance-officer   → GDPR data transfer implications
  ├── tax-advisor          → Tax structuring, fiscal unity
  └── employment-counsel   → Employee transfer, works council
```

### How It Works

1. The **legal-researcher** receives your query and analyzes which domains are involved
2. It creates a team and assigns tasks to relevant specialists
3. Each specialist works independently, using their domain skills and MCP tools
4. The legal-researcher synthesizes all findings into a unified legal memorandum
5. Disclaimers and escalation notes are appended

### Requesting a Team Analysis

Just ask a complex, multi-domain question:

```
"We're planning to acquire a Dutch tech startup. They have 30 employees,
process EU customer health data, have IP in AI algorithms, and we need to
structure this tax-efficiently. What should we consider?"
```

Or be explicit:

```
"Deploy a legal team to analyze [your complex legal matter]"
```

---

<a name="mcp-tools"></a>
## 6. MCP Server & API Tools

The system connects to Dutch legal databases through 4 MCP servers providing 15+ tools.

### Custom MCP Server: `dutch-legal-mcp`

Our custom server wraps 6 Dutch government APIs:

**Legislation Tools (KOOP SRU):**
| Tool | What It Does |
|------|-------------|
| `legislation_search` | Search Dutch laws by keyword, area, date |
| `legislation_get_article` | Get a specific article from a law by BWB-ID |
| `legislation_versions` | View version history of a law |

**Case Law Tools (Rechtspraak.nl):**
| Tool | What It Does |
|------|-------------|
| `caselaw_search_rechtspraak` | Search 500K+ rulings by subject, court, date |
| `caselaw_get_ruling` | Get full ruling text by ECLI identifier |
| `caselaw_get_metadata` | Extract metadata (court, date, legal areas) |

**Judge Tools (Open Rechtspraak):**
| Tool | What It Does |
|------|-------------|
| `judges_search` | Search judges by name |
| `judges_get_verdicts` | Get all published verdicts for a judge |

**Company Registry Tools (KVK):**
| Tool | What It Does |
|------|-------------|
| `kvk_search_company` | Search by company name or KVK number |
| `kvk_get_profile` | Get detailed company profile |
| `kvk_get_naming` | Get trade names history |

**EU Law Tools (EUR-Lex SPARQL):**
| Tool | What It Does |
|------|-------------|
| `eurlex_search_regulations` | Search EU directives and regulations |
| `eurlex_get_act` | Get act details by CELEX number |

**Government Data (data.overheid.nl):**
| Tool | What It Does |
|------|-------------|
| `overheid_search_datasets` | Search government open data catalog |

**Cross-Reference:**
| Tool | What It Does |
|------|-------------|
| `legal_cross_reference` | Given an article, find related case law + EU regulations |

### Other MCP Servers

| Server | Purpose |
|--------|---------|
| **opentk** | Dutch parliamentary data (Tweede Kamer, Eerste Kamer, kamervragen) |
| **cerebra-legal** | Legal reasoning and analysis |
| **dutch-law-downloader** | Download Dutch law texts from MinBZK |

### Rate Limits & Caching

The MCP server automatically handles rate limiting and caching:

| API | Rate Limit | Cache Duration |
|-----|-----------|---------------|
| Rechtspraak.nl | 5 req/s | 7 days (full text), 1 hour (search) |
| KOOP SRU | 5 req/s | 24 hours (legislation) |
| KVK | 3 req/s | 4 hours |
| EUR-Lex | 2 req/s | 24 hours |
| Open Rechtspraak | 10 req/s | 7 days |

---

<a name="python-scripts"></a>
## 7. Python Utility Scripts

Standalone Python scripts in `scripts/` serve as fallbacks and utilities.

### `ecli-parser.py` - ECLI Identifier Tool

Parse, validate, and format ECLI (European Case Law Identifier) numbers.

```bash
# Parse an ECLI number
python3 scripts/ecli-parser.py parse "ECLI:NL:HR:2023:1234"

# Validate an ECLI
python3 scripts/ecli-parser.py validate "ECLI:NL:HR:2023:1234"

# Format from components
python3 scripts/ecli-parser.py format NL HR 2023 1234

# List Dutch court codes
python3 scripts/ecli-parser.py courts
python3 scripts/ecli-parser.py courts --filter "Amsterdam"
```

### `fetch-rechtspraak.py` - Case Law Search

Direct Rechtspraak.nl API access.

```bash
# Search cases
python3 scripts/fetch-rechtspraak.py search "bestuurdersaansprakelijkheid"

# Get a specific ruling
python3 scripts/fetch-rechtspraak.py get "ECLI:NL:HR:2023:1234"

# List court codes
python3 scripts/fetch-rechtspraak.py courts
```

### `fetch-wetgeving.py` - Legislation Lookup

Direct KOOP SRU API access for Dutch legislation.

```bash
# Search legislation
python3 scripts/fetch-wetgeving.py search "proeftijd arbeidsovereenkomst"

# Get a specific law (by BWB-ID or common abbreviation)
python3 scripts/fetch-wetgeving.py get BW7          # Burgerlijk Wetboek Boek 7
python3 scripts/fetch-wetgeving.py get BWBR0005290   # Same, by BWB-ID

# List collections and common law abbreviations
python3 scripts/fetch-wetgeving.py collections
python3 scripts/fetch-wetgeving.py laws
```

### `kvk-lookup.py` - Company Registry

KVK API access (requires `KVK_API_KEY`).

```bash
# Search companies
python3 scripts/kvk-lookup.py search "Booking.com"

# Get company profile
python3 scripts/kvk-lookup.py profile 34051424
```

### `legal-document-formatter.py` - Document Formatting

Format legal documents from structured data.

```bash
# Format a legal memorandum from YAML
python3 scripts/legal-document-formatter.py memorandum input.yaml --output memo.md

# Format a contract review
python3 scripts/legal-document-formatter.py review clauses.json --disclaimer nl

# Format a case summary
python3 scripts/legal-document-formatter.py case-summary case.json

# Add disclaimer to any document
python3 scripts/legal-document-formatter.py disclaimer document.md --language both
```

---

<a name="templates"></a>
## 8. Templates

Pre-built templates in `assets/templates/` for common legal documents:

| Template | File | Language |
|----------|------|----------|
| Contract Review Report | `contract-review-report.md` | EN |
| Legal Memorandum | `legal-memorandum.md` | EN (with Dutch legal terms) |
| NDA | `nda-template-nl.md` | NL |
| Data Processing Agreement | `verwerkersovereenkomst.md` | NL |
| Employment Contract | `arbeidsovereenkomst.md` | NL |

### Using Templates

Templates are used automatically by the `/draft-contract` and `/legal-memo` commands. You can also reference them directly:

```
"Draft an NDA using the template in assets/templates/nda-template-nl.md,
 with these specifics: mutual NDA, 3-year term, EUR 50,000 penalty,
 between Company A and Company B"
```

### Template Placeholders

Templates use placeholders like `[PARTIJ 1]`, `[DATUM]`, `[BEDRAG]` that get filled in based on your input.

---

<a name="org-config"></a>
## 9. Organization Configuration

Customize the system for your organization by editing `.claude/nl-ai-lawyer.local.md`.

### Setup

```bash
cp assets/user-config-template.md .claude/nl-ai-lawyer.local.md
```

### What You Can Configure

**Organization Profile:**
- Company name, legal entity type, KVK number
- Industry sector and primary legal needs

**Contract Review Positions:**
- Preferred liability caps (e.g., "12 months fees")
- IP assignment preference
- Payment terms
- Governing law and dispute resolution forum
- Non-compete duration limits

**NDA Defaults:**
- Mutual vs. unilateral preference
- Standard term (e.g., 2 years)
- Penalty clause amounts
- Standard carve-outs

**Risk Appetite:**
- **Conservative** - Flag any deviation from your standard positions
- **Moderate** - Flag material deviations only
- **Aggressive** - Only flag deal-breakers

**Privacy/GDPR:**
- DPO name
- SCC preferences
- Privacy by Design approach

**Employment:**
- Applicable CAO
- Standard probation period
- 30% ruling eligibility

**Language:**
- Primary output language (NL/EN/bilingual)
- Contract language preference

### Example: Conservative Tech Company

```markdown
## Risk Appetite
- **Overall risk appetite:** Conservative

## Contract Review Positions
### Liability
- **Preferred liability cap:** Total contract value
- **Indemnification stance:** Mutual and limited

### Intellectual Property
- **IP assignment preference:** Retain all IP
- **Background IP:** Always excluded

### Governing Law & Disputes
- **Preferred governing law:** Dutch law
- **Dispute resolution:** Dutch courts
- **Preferred forum:** Rechtbank Amsterdam
```

---

<a name="tips"></a>
## 10. Tips & Best Practices

### Writing Effective Queries

**Be specific with legal context:**
```
# Good
"Review this software license agreement. We are the licensee (buyer).
 Governed by Dutch law."

# Less effective
"Review this contract"
```

**Include relevant facts:**
```
# Good
"Can we dismiss an employee for underperformance? They've been here 8 years,
 indefinite contract, verbal warnings only, no written improvement plan."

# Less effective
"How do we fire someone in the Netherlands?"
```

**Specify your role/perspective:**
```
/arbeidsrecht "What severance am I entitled to?" --context employee
/review-contract --position seller "..."
```

### Understanding the Output

**Traffic Light System:**
- **GREEN** - Standard/favorable clause, no action needed
- **YELLOW** - Needs attention, consider negotiating
- **RED** - High risk, strongly recommend changing

**ECLI Citations:**
- Format: `ECLI:NL:HR:2023:1234`
- `NL` = Netherlands, `HR` = Hoge Raad (Supreme Court)
- View any ruling at: `https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:HR:2023:1234`

**BW References:**
- `Art. 6:162 BW` = Burgerlijk Wetboek (Civil Code) Book 6, Article 162
- `Art. 7:669 lid 3 sub d BW` = Book 7, Article 669, Paragraph 3, Sub d

### Combining Commands

```
# Step 1: Research the law
/search-wetgeving "aansprakelijkheid bestuurder BV"

# Step 2: Find relevant case law
/search-rechtspraak "bestuurdersaansprakelijkheid Beklamel" --court "Hoge Raad"

# Step 3: Get a comprehensive analysis
/legal-memo "Can a director of a Dutch BV be held personally liable for the company's debts to creditors?"
```

### Bilingual Output

Most commands default to Dutch legal terminology with English explanations. For pure Dutch output:
```
/draft-contract --language nl --type arbeidsovereenkomst "..."
/respond --type ingebrekestelling --language nl "..."
```

---

<a name="troubleshooting"></a>
## 11. Troubleshooting

### MCP Server Issues

**"dutch-legal-mcp not found"**
```bash
cd ~/uncloud/nl-ai-lawyer/dutch-legal-mcp
npm install
npm run build
```

**"KVK_API_KEY not set"**
```bash
export KVK_API_KEY=your_key_here
# Or add to your shell profile (~/.zshrc or ~/.bashrc)
```

**Rate limit errors**
The system auto-throttles to stay within API limits. If you see rate limit errors, wait a few seconds and retry.

### Search Returns No Results

- Try broader search terms
- Try Dutch legal terminology (e.g., "aansprakelijkheid" instead of "liability")
- Check date range filters
- For case law: specify court level or try without court filter

### Missing Disclaimers

Every output should include a legal disclaimer. If missing, append it manually:
```
"Please add the standard legal disclaimer to this output"
```

### Python Script Errors

```bash
# Install missing dependencies
pip install -r scripts/requirements.txt

# Common: rechtspraak-extractor may need specific version
pip install rechtspraak-extractor==0.2.0
```

### Common Dutch Legal Abbreviations

| Abbreviation | Full Name | English |
|-------------|-----------|---------|
| BW | Burgerlijk Wetboek | Civil Code |
| Sr | Wetboek van Strafrecht | Criminal Code |
| Sv | Wetboek van Strafvordering | Code of Criminal Procedure |
| Rv | Wetboek van Burgerlijke Rechtsvordering | Code of Civil Procedure |
| Awb | Algemene wet bestuursrecht | General Administrative Law Act |
| AVG | Algemene Verordening Gegevensbescherming | GDPR |
| UAVG | Uitvoeringswet AVG | GDPR Implementation Act |
| Wft | Wet op het financieel toezicht | Financial Supervision Act |
| WED | Wet op de Economische Delicten | Economic Offences Act |
| VPB | Vennootschapsbelasting | Corporate Income Tax |
| BTW | Belasting over de Toegevoegde Waarde | VAT |
| HR | Hoge Raad | Supreme Court |
| Rb | Rechtbank | District Court |
| Hof | Gerechtshof | Court of Appeal |
| KVK | Kamer van Koophandel | Chamber of Commerce |
| AP | Autoriteit Persoonsgegevens | Data Protection Authority |
| UWV | Uitvoeringsinstituut Werknemersverzekeringen | Employee Insurance Agency |
| IND | Immigratie- en Naturalisatiedienst | Immigration Service |
| CAO | Collectieve Arbeidsovereenkomst | Collective Labor Agreement |

---

## Important Disclaimer

This system provides **AI-generated legal analysis** and does **NOT constitute legal advice**. The information is for informational purposes only. Always consult a qualified Dutch lawyer (advocaat) registered with the Nederlandse Orde van Advocaten for legal matters.

Do not share confidential or privileged information with this system - it is not protected by attorney-client privilege (verschoningsrecht).
