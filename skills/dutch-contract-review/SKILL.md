---
name: dutch-contract-review
description: Clause-by-clause review of contracts against Dutch civil law (BW Boek 6/7) with GREEN/YELLOW/RED risk flagging
---

# Dutch Contract Review

## When to Use
- User submits a contract or set of clauses for review under Dutch law
- User asks whether specific contract terms comply with Dutch law (Burgerlijk Wetboek)
- User wants a risk assessment of a commercial agreement governed by Dutch law
- User asks about general terms and conditions (algemene voorwaarden) validity
- User requests comparison of contract positions against market standard

## Process
1. **Identify contract type** - Determine which BW Book 7 specific contract type applies (koop, opdracht, aanneming, huur, arbeidsovereenkomst, etc.) or if it is an innominate contract
2. **Check governing law** - Confirm Dutch law applicability; if foreign law governs, flag and recommend local counsel
3. **Extract key clauses** - Parse the contract into reviewable sections
4. **Clause-by-clause analysis** - For each clause:
   a. Identify the legal topic (liability, indemnity, IP, termination, etc.)
   b. Check against mandatory law (dwingend recht) - provisions that cannot be contracted out of
   c. Check against default law (aanvullend/regelend recht) - assess deviations
   d. Flag consumer protection rules if B2C (Afdeling 6.5.3 BW - algemene voorwaarden)
   e. Assign risk rating: GREEN (standard/favorable), YELLOW (non-standard but negotiable), RED (legally problematic or unenforceable)
5. **Cross-clause analysis** - Check for internal inconsistencies, gaps, and missing standard clauses
6. **Generate summary** - Produce executive summary with overall risk profile
7. **Append disclaimer**

## Key Legal Framework
- **BW Boek 3** - Vermogensrecht (Property Law) - Arts. 3:33-37 (juridische handelingen), 3:40 (nullity), 3:44 (defects of will)
- **BW Boek 6** - Verbintenissenrecht (Law of Obligations):
  - Afdeling 6.1.8 (Opschortingsrechten / right of suspension)
  - Afdeling 6.1.9 (Gevolgen van niet-nakoming / consequences of non-performance)
  - Afdeling 6.1.10 (Wettelijke verplichtingen tot schadevergoeding / damages)
  - Afdeling 6.5.2 (Totstandkoming / formation of contracts)
  - Afdeling 6.5.3 (Algemene voorwaarden / general terms and conditions)
  - Afdeling 6.5.4 (Rechtsgevolgen / legal effects of contracts)
  - Art. 6:74 (Toerekenbare tekortkoming / attributable failure)
  - Art. 6:89 (Klachtplicht / duty to complain)
  - Art. 6:228 (Dwaling / mistake)
  - Art. 6:233-234 (Vernietigbaarheid algemene voorwaarden / voidability of general terms)
  - Art. 6:248 lid 2 (Beperkende werking redelijkheid en billijkheid / derogating effect of reasonableness and fairness)
- **BW Boek 7** - Bijzondere overeenkomsten (Specific Contracts):
  - Titel 1: Koop (Sale)
  - Titel 7: Opdracht (Services)
  - Titel 10: Arbeidsovereenkomst (Employment)
  - Titel 12: Aanneming van werk (Contract for work)
- **Courts**: Rechtbank (first instance), Gerechtshof (appeal), Hoge Raad (cassation)

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append the disclaimer from `assets/disclaimers/` stating this is not legal advice
- **Citation requirement**: Every legal conclusion must reference specific BW articles or case law (ECLI citations)
- **No drafting**: Do not draft contract clauses from scratch; only review and flag issues in existing text
- **Conflict check**: If the user appears to be both parties, clarify which party's perspective to review from
- **Jurisdictional limits**: If non-Dutch law governs, state inability to fully assess and recommend local counsel
- **Confidentiality warning**: Remind users not to share truly confidential documents without understanding the system's data handling

### Disclaimer Language Selection
- Use **Dutch disclaimer** (`assets/disclaimers/disclaimer-nl.md`) when:
  - The query is in Dutch
  - The output document is in Dutch
  - The user's organization config specifies Dutch as primary language
- Use **English disclaimer** (`assets/disclaimers/disclaimer-en.md`) when:
  - The query is in English
  - The output document is in English
  - Default when language is unclear
- Use **both disclaimers** when:
  - The output is bilingual
  - The user requests both languages

## MCP Tools to Use
- `search_legislation` - Look up specific BW articles referenced in contract clauses
- `get_legislation` - Retrieve full text of relevant BW provisions
- `search_case_law` - Find relevant case law on disputed clause types
- `get_case_law` - Retrieve specific court decisions by ECLI
- `search_eu_legislation` - Check EU directive implementation where relevant (e.g., consumer sales directive)

## Related Skills
- **dutch-corporate-law** - For SHA/SPA and corporate transaction agreements
- **dutch-employment-law** - For employment contracts (arbeidsovereenkomst) and related clauses
- **nda-triage-nl** - For NDA/confidentiality agreement specific triage
- **dutch-privacy-gdpr** - For data processing agreements (verwerkersovereenkomst)

## Output Format
```
## Contract Review Summary

**Contract Type**: [e.g., Service Agreement (overeenkomst van opdracht)]
**Governing Law**: [e.g., Dutch law]
**Parties**: [Party A / Party B]
**Review Perspective**: [Which party's interests]

## Overall Risk Assessment: [GREEN / YELLOW / RED]

## Clause-by-Clause Analysis

### [Clause Number/Title]
- **Risk Level**: [GREEN/YELLOW/RED]
- **Summary**: [What the clause does]
- **Legal Basis**: [Relevant BW article(s)]
- **Issues**: [Identified problems or deviations from standard]
- **Recommendation**: [Suggested action]

[Repeat for each clause]

## Missing Clauses
[Standard clauses not found in the contract]

## Key Risks
1. [Numbered list of most critical issues]

## Recommended Actions
1. [Prioritized action items]

---
[Disclaimer]
```

## Escalation Triggers
- Contract involves criminal liability or fraud allegations
- Dispute value exceeds EUR 1,000,000
- Contract involves regulated sectors (financial services, healthcare, energy) requiring sector-specific expertise
- Consumer contract with potential Afdeling 6.5.3 BW (unfair terms) implications requiring litigation assessment
- Cross-border elements requiring private international law analysis (Rome I / Rome II)
- Contract is already in dispute or litigation is pending
- Contract involves state aid or public procurement law
- User indicates they are about to sign imminently and need definitive legal advice

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
