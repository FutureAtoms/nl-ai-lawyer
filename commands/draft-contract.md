---
name: draft-contract
description: Generate Dutch contract from requirements
arguments:
  - name: type
    description: Contract type (arbeidsovereenkomst, huurovereenkomst, koopovereenkomst, dienstverlening, etc.)
    required: true
  - name: requirements
    description: Key terms and requirements
    required: true
  - name: language
    description: nl or en (default nl)
    required: false
---

# Draft Dutch Contract

Generate a contract based on specified type and requirements, compliant with Dutch law.

## Skill and Tools

Use MCP tools:
- `legislation_search` -- to look up relevant BW provisions for the contract type
- `legislation_fetch` -- to retrieve mandatory statutory terms
- `caselaw_search_rechtspraak` -- to check for recent case law affecting standard clauses

## Workflow

### Step 1: Contract Type Identification

Determine the contract type and applicable law:

| Contract Type | Dutch Name | Primary BW Provisions |
|---------------|------------|----------------------|
| Employment | Arbeidsovereenkomst | BW 7:610-691 |
| Lease (residential) | Huurovereenkomst woonruimte | BW 7:201-282 |
| Lease (commercial) | Huurovereenkomst bedrijfsruimte | BW 7:290-310 / 7:230a |
| Sale | Koopovereenkomst | BW 7:1-48 |
| Services | Overeenkomst van opdracht | BW 7:400-413 |
| Contracting | Aannemingsovereenkomst | BW 7:750-769 |
| Distribution | Distributieovereenkomst | No specific BW title |
| Agency | Agentuurovereenkomst | BW 7:428-445 |
| Loan | Overeenkomst van geldlening | BW 7:129-130 (new) |
| License | Licentieovereenkomst | Various (IE laws) |
| Partnership | VOF/Maatschap | BW 7A:1655-1688 |
| Shareholders Agreement | Aandeelhoudersovereenkomst | BW 2 + contract law |

### Step 2: Requirements Analysis

Parse the `requirements` argument to identify:
- Parties (names, addresses, KVK numbers)
- Key commercial terms (price, duration, scope)
- Specific clauses requested
- Any non-standard requirements
- Language preference (default: Dutch)

### Step 3: Generate Contract

Structure the contract following Dutch legal convention:

```
[CONTRACT TITLE IN CAPITALS]

[Ondergetekenden / The undersigned:]

1. [Party 1 details]
   (hierna te noemen: "[shorthand]")

2. [Party 2 details]
   (hierna te noemen: "[shorthand]")

Gezamenlijk te noemen: "Partijen"

IN AANMERKING NEMENDE DAT / WHEREAS:
[Recitals / Overwegingen - context and background]

KOMEN OVEREEN ALS VOLGT / AGREE AS FOLLOWS:

ARTIKEL 1 -- DEFINITIES
[Definitions]

ARTIKEL 2 -- VOORWERP VAN DE OVEREENKOMST
[Subject matter / scope]

ARTIKEL 3 -- DUUR EN BEEINDIGING
[Term and termination]

ARTIKEL 4 -- VERGOEDING EN BETALING
[Remuneration and payment]

ARTIKEL 5 -- VERPLICHTINGEN VAN [PARTY 1]
[Obligations]

ARTIKEL 6 -- VERPLICHTINGEN VAN [PARTY 2]
[Obligations]

ARTIKEL 7 -- GEHEIMHOUDING
[Confidentiality]

ARTIKEL 8 -- INTELLECTUEEL EIGENDOM
[Intellectual property -- if applicable]

ARTIKEL 9 -- AANSPRAKELIJKHEID
[Liability]

ARTIKEL 10 -- OVERMACHT
[Force majeure]

ARTIKEL 11 -- PERSOONSGEGEVENS
[Personal data / privacy -- AVG compliance clause]

ARTIKEL 12 -- SLOTBEPALINGEN
[Final provisions: governing law, disputes, amendments, entire agreement]

Aldus overeengekomen en in tweevoud ondertekend te [plaats] op [datum].

[Party 1]                    [Party 2]
_______________             _______________
Naam:                       Naam:
Functie:                    Functie:
```

### Step 4: Contract-Type-Specific Provisions

Include mandatory provisions based on the contract type:

**Arbeidsovereenkomst (Employment):**
- Working hours, salary, holiday allowance (8% vakantietoeslag)
- Probationary period (proeftijd) per art. 7:652 BW
- Notice period (opzegtermijn) per art. 7:672 BW
- Non-compete clause (concurrentiebeding) per art. 7:653 BW -- requires written form and specific requirements for fixed-term contracts
- Pension arrangements
- CAO applicability
- Sick pay obligations

**Huurovereenkomst Woonruimte (Residential Lease):**
- Rent amount and indexation
- Deposit (waarborgsom) max 2 months rent
- Mandatory reference to huurcommissie
- Tenant protections (huurbescherming)
- Maintenance obligations split

**Koopovereenkomst (Sale):**
- Description of goods
- Price and payment terms
- Delivery terms (aflevering)
- Conformity (conformiteit) per art. 7:17 BW
- Warranty provisions (garantie)
- Risk transfer (risico-overgang)

**Dienstverlening (Services):**
- Scope of services
- Standard of care (zorgplicht)
- Self-employed status verification (if relevant to avoid schijnzelfstandigheid)
- Deliverables and acceptance

### Step 5: Bilingual Handling

If `language` is "en":
- Draft the contract in English
- Note that Dutch law terms will be included in parentheses for clarity
- Include a language clause specifying which version prevails in case of discrepancy

If `language` is "nl" or not specified:
- Draft entirely in Dutch
- Use standard Dutch legal terminology and conventions

### Step 6: Template Disclaimer

**CRITICAL: Include the following notice prominently at the top of the generated contract:**

```
============================================================
CONCEPT / TEMPLATE -- GEEN DEFINITIEF CONTRACT
Dit document is gegenereerd door een AI-assistent en dient
uitsluitend als uitgangspunt. Laat dit document altijd
beoordelen door een gekwalificeerde advocaat voordat u het
ondertekent.

DRAFT / TEMPLATE -- NOT A FINAL CONTRACT
This document was generated by an AI assistant and serves
only as a starting point. Always have this document reviewed
by a qualified lawyer before signing.
============================================================
```

### Step 7: Disclaimer

Always append the following disclaimer at the end of the output:

---

**Disclaimer / Juridische kennisgeving**

This contract template is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. This is a template only and should not be signed without review by a qualified Dutch advocaat. The template may not address all legal requirements for your specific situation, may contain errors, and may not reflect the most recent legal developments. No attorney-client relationship is created. Using this template without professional legal review is at your own risk.

*Dit contractsjabloon is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Dit is uitsluitend een sjabloon en mag niet worden ondertekend zonder beoordeling door een gekwalificeerde Nederlandse advocaat. Het sjabloon adresseert mogelijk niet alle juridische vereisten voor uw specifieke situatie. Het gebruik van dit sjabloon zonder professionele juridische beoordeling is op eigen risico.*
