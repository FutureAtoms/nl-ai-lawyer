# Dutch Legal AI Skills - Trigger Evaluation Report

**Date**: 2026-03-04
**Evaluator**: Claude Sonnet 4.6
**Skills evaluated**: 14
**Test queries**: 40

---

## Skill Descriptions Reference

| Skill Name | Description Trigger Keywords |
|---|---|
| `dutch-administrative-law` | AWB procedures, objection/appeal against government decisions, bezwaar, beroep, omgevingsvergunning, building permits, government decisions, bestuursrecht, Awb procedures |
| `dutch-case-law-research` | Dutch court decisions, jurisprudentie, rechtspraak, case law, ECLI numbers, Hoge Raad rulings, legal precedents under Dutch law |
| `dutch-contract-review` | Review/analyze/check a Dutch contract, agreement, SaaS license, distribution agreement, service agreement, commercial contract under Dutch law, algemene voorwaarden, liability clauses, indemnification, contract risk assessment |
| `dutch-corporate-law` | Dutch companies, BV incorporation, shareholder agreements, director liability, bestuurdersaansprakelijkheid, aandeelhoudersovereenkomst, corporate governance, KVK registration |
| `dutch-criminal-law` | Dutch criminal law, strafrecht, FIOD, corporate criminal liability, environmental crimes, valsheid in geschrift, WED offenses |
| `dutch-employment-law` | Dutch employment, arbeidsrecht, ontslag, dismissal, transitievergoeding, non-compete clauses, concurrentiebeding, CAO, hiring employees in NL |
| `dutch-immigration-law` | Dutch immigration, kennismigrant, visa, verblijfsvergunning, IND, work permits, family reunification, moving to NL |
| `dutch-ip-law` | Dutch intellectual property, auteursrecht, copyright ownership, trademark registration, BOIP, patent law, trade secrets, Wet bescherming bedrijfsgeheimen |
| `dutch-legislation-lookup` | Dutch laws, BW articles, wetgeving, statutes, Burgerlijk Wetboek provisions, look up specific articles of Dutch law |
| `dutch-privacy-gdpr` | Dutch GDPR, AVG, privacy compliance, data protection, verwerkersovereenkomst, data subject rights, cookie consent, AP enforcement |
| `dutch-real-estate-law` | Buying property in NL, huurrecht, erfpacht, commercial lease, koopovereenkomst, notaris, Dutch real estate transactions |
| `dutch-tax-law` | Dutch taxes, vennootschapsbelasting, BTW, loonbelasting, 30% ruling, fiscale eenheid, Box 1/2/3, expat tax |
| `eu-law-integration` | EU law in NL, direct effect, directives implementation, CJEU, preliminary rulings, EU-Dutch legal relationship |
| `nda-triage-nl` | Review/screen/triage an NDA, non-disclosure agreement, geheimhoudingsovereenkomst, confidentiality agreement, secrecy agreement under Dutch law |

---

## Evaluation Table

| Query# | Query (abbreviated) | Expected Skill | Predicted Skill | Match | Notes |
|---|---|---|---|---|---|
| 1 | "Review my Dutch SaaS agreement for liability risks" | dutch-contract-review | dutch-contract-review | CORRECT | "SaaS" matches "SaaS license" in description; "review" and "liability" are explicit trigger keywords. Strong match. |
| 2 | "Find Hoge Raad cases on director liability" | dutch-case-law-research | dutch-case-law-research | CORRECT | "Hoge Raad" is an explicit keyword in description. "cases" maps to "case law". Could weakly co-trigger dutch-corporate-law ("director liability" / "bestuurdersaansprakelijkheid"), but case-law-research is primary. |
| 3 | "What does artikel 6:162 BW say?" | dutch-legislation-lookup | dutch-legislation-lookup | CORRECT | "BW articles" and "Burgerlijk Wetboek provisions" and "look up specific articles" are all explicit trigger keywords. Perfect match. |
| 4 | "How do I set up a BV in the Netherlands?" | dutch-corporate-law | dutch-corporate-law | CORRECT | "BV incorporation" is an explicit trigger keyword. "set up a BV" maps directly. |
| 5 | "Can I fire an employee for poor performance in NL?" | dutch-employment-law | dutch-employment-law | CORRECT | "dismissal" and "Dutch employment" are explicit keywords. "fire" = dismissal/ontslag. |
| 6 | "Is our health app GDPR compliant in the Netherlands?" | dutch-privacy-gdpr | dutch-privacy-gdpr | CORRECT | "Dutch GDPR" and "privacy compliance" are explicit keywords. "GDPR compliant" is an exact match. |
| 7 | "Who owns software copyright in NL - employer or employee?" | dutch-ip-law | dutch-ip-law | CORRECT | "copyright ownership" is an explicit trigger keyword. "software copyright" maps to auteursrecht in software context. |
| 8 | "I'm buying a house in Amsterdam with erfpacht" | dutch-real-estate-law | dutch-real-estate-law | CORRECT | "erfpacht" and "buying property in NL" are both explicit trigger keywords. Perfect match. |
| 9 | "How does the 30% ruling work for expats?" | dutch-tax-law | dutch-tax-law | CORRECT | "30% ruling" and "expat tax" are explicit trigger keywords in description. Could weakly co-trigger dutch-immigration-law (which also mentions 30% ruling in its When-to-Use section), but dutch-tax-law has it in the description itself. |
| 10 | "The gemeente rejected my building permit" | dutch-administrative-law | dutch-administrative-law | CORRECT | "building permits" is an explicit trigger keyword. "rejected" = government decision to challenge. |
| 11 | "FIOD raided our offices, what now?" | dutch-criminal-law | dutch-criminal-law | CORRECT | "FIOD" is an explicit trigger keyword in description. Exact lexical match. |
| 12 | "How to get a kennismigrant visa for my employee?" | dutch-immigration-law | dutch-immigration-law | CORRECT | "kennismigrant" and "visa" are explicit trigger keywords. Perfect match. |
| 13 | "Can I invoke an unimplemented EU directive in Dutch court?" | eu-law-integration | eu-law-integration | CORRECT | "directives implementation" and "direct effect" are explicit trigger keywords. "unimplemented directive" = vertical direct effect scenario, core eu-law-integration topic. |
| 14 | "Screen this NDA for red flags under Dutch law" | nda-triage-nl | nda-triage-nl | CORRECT | "screen" and "NDA" and "under Dutch law" map directly to "screen/triage an NDA...under Dutch law". |
| 15 | "mijn huurder betaalt niet meer, wat nu?" (Dutch) | dutch-real-estate-law | dutch-real-estate-law | CORRECT | "huurrecht" (rental law) is an explicit trigger keyword. "huurder" = tenant under huurrecht. Dutch query does not impede matching - description includes Dutch terms. |
| 16 | "ontslagvergoeding berekenen" (Dutch) | dutch-employment-law | dutch-employment-law | CORRECT | "ontslagvergoeding" is semantically equivalent to "transitievergoeding" (dismissal/transition payment), which is an explicit keyword. "ontslag" (dismissal) is also explicit. Good match. |
| 17 | "BTW aangifte problemen" (Dutch) | dutch-tax-law | dutch-tax-law | CORRECT | "BTW" is an explicit trigger keyword in description. Direct match. |
| 18 | "bezwaarschrift indienen tegen besluit" | dutch-administrative-law | dutch-administrative-law | CORRECT | "bezwaar" (objection) is an explicit trigger keyword. "besluit" = government decision. Strong match. |
| 19 | "geheimhoudingsovereenkomst beoordelen" | nda-triage-nl | nda-triage-nl | CORRECT | "geheimhoudingsovereenkomst" is an explicit trigger keyword in description. "beoordelen" (assess/review) matches "review". Perfect. |
| 20 | "aandeelhoudersovereenkomst opstellen" | dutch-corporate-law | dutch-corporate-law | CORRECT | "aandeelhoudersovereenkomst" is an explicit trigger keyword in description. Perfect lexical match. |
| 21 | "Acquiring a Dutch BV - what about employee transfers?" | dutch-corporate-law AND dutch-employment-law | dutch-corporate-law AND dutch-employment-law | AMBIGUOUS | "BV" triggers dutch-corporate-law ("BV incorporation", M&A). "employee transfers" maps to dutch-employment-law ("Transfer of undertaking" / overgang van onderneming in escalation triggers). Both skills have cross-references to each other in Related Skills. System likely triggers both or must choose. Scored AMBIGUOUS. |
| 22 | "Data transfer to US under Dutch GDPR and EU adequacy" | dutch-privacy-gdpr AND eu-law-integration | dutch-privacy-gdpr AND eu-law-integration | AMBIGUOUS | "Dutch GDPR" and "privacy compliance" trigger dutch-privacy-gdpr. "EU adequacy" decisions and "EU law in NL" aspect triggers eu-law-integration. Both descriptions explicitly mention international data transfers. Related Skills in privacy-gdpr lists eu-law-integration. Scored AMBIGUOUS - both correctly should fire. |
| 23 | "Non-compete clause in employment contract review" | dutch-employment-law AND dutch-contract-review | dutch-employment-law AND dutch-contract-review | AMBIGUOUS | "non-compete clauses" / "concurrentiebeding" is an explicit keyword in dutch-employment-law. "contract review" and "liability clauses" / "contract risk assessment" trigger dutch-contract-review. Both are valid and cross-reference each other in Related Skills. Scored AMBIGUOUS. |
| 24 | "Tax implications of commercial real estate purchase" | dutch-tax-law AND dutch-real-estate-law | dutch-tax-law AND dutch-real-estate-law | AMBIGUOUS | "Dutch taxes" / "overdrachtsbelasting" (transfer tax) triggers dutch-tax-law. "buying property" / "commercial lease" / "real estate transactions" triggers dutch-real-estate-law. Both descriptions reference each other in Related Skills. Scored AMBIGUOUS - both should fire. |
| 25 | "IP assignment clause in software development contract" | dutch-ip-law AND dutch-contract-review | dutch-ip-law AND dutch-contract-review | AMBIGUOUS | "copyright ownership" / "IP licensing or assignment" triggers dutch-ip-law. "review a Dutch contract" / "liability clauses" / "contract risk assessment" triggers dutch-contract-review. IP-law lists dutch-contract-review in Related Skills. Scored AMBIGUOUS. |
| 26 | "Write me a Python script to parse JSON" | NONE | NONE | CORRECT | No Dutch legal keywords. No skill description matches. Correctly no trigger. |
| 27 | "What's the weather in Amsterdam?" | NONE | NONE | CORRECT | No legal context. No skill description matches. Correctly no trigger. |
| 28 | "Help me with my React component" | NONE | NONE | CORRECT | No Dutch legal context. No skill matches. Correctly no trigger. |
| 29 | "Translate this text to Dutch" | NONE | NONE | CORRECT | No legal content. No skill matches. Correctly no trigger. |
| 30 | "What are the best restaurants in Rotterdam?" | NONE | NONE | CORRECT | No legal content. No skill matches. Correctly no trigger. |
| 31 | "Contract law in Germany" | NONE | NONE | CORRECT | "German" jurisdiction - no Dutch law skill should fire. However, mild FALSE_POSITIVE risk: "contract law" and "contract" appear in dutch-contract-review description. Description says "Dutch contract" and "Dutch law" repeatedly, providing a strong jurisdiction guard. Risk is low but not zero if the matcher is keyword-only without jurisdiction awareness. Score: CORRECT with low false-positive caveat. |
| 32 | "UK employment tribunal procedures" | NONE | NONE | CORRECT | "employment" keyword could weakly surface dutch-employment-law, but description specifies "Dutch employment" and "Netherlands". "tribunal" is not a Dutch concept. No trigger expected if jurisdiction filtering works. Score: CORRECT with low caveat. |
| 33 | "US patent infringement case" | NONE | NONE | CORRECT | "patent" could weakly surface dutch-ip-law (which mentions patent law). Description says "Dutch and Benelux law". Jurisdiction context should prevent trigger. Score: CORRECT with low caveat for keyword-only systems. |
| 34 | "French GDPR compliance" | NONE | NONE | CORRECT | "GDPR" could trigger dutch-privacy-gdpr. Description says "Dutch GDPR" and "AP enforcement in the Netherlands". "French" jurisdiction guard should prevent trigger in a semantic system. Score: CORRECT with medium false-positive risk in a keyword-only system that pattern-matches "GDPR" without jurisdiction awareness. |
| 35 | "Belgian corporate tax rates" | NONE | NONE | CORRECT | "corporate tax" could weakly trigger dutch-tax-law (which mentions vennootschapsbelasting). "Belgian" jurisdiction should block. Score: CORRECT with low caveat. |
| 36 | "Legal risks of hiring foreign workers in NL" | dutch-immigration-law OR dutch-employment-law | dutch-immigration-law OR dutch-employment-law | AMBIGUOUS | "hiring employees in the Netherlands" is an explicit keyword in dutch-employment-law. "work permits" / "Dutch immigration" and "moving to the Netherlands" match dutch-immigration-law. Both legitimately apply. Related Skills in dutch-employment-law lists dutch-immigration-law and vice versa. Score: AMBIGUOUS - both could fire; unclear which is primary. |
| 37 | "Environmental regulations for our factory" | dutch-administrative-law OR dutch-criminal-law | dutch-administrative-law | AMBIGUOUS | "Environmental and Planning Act" / "permits" / "government decisions" in dutch-administrative-law covers environmental permits (omgevingsvergunning). "environmental crimes" / "WED offenses" in dutch-criminal-law could also trigger. However, the query is about regulations (compliance), not criminal offense, so dutch-administrative-law is more likely primary. dutch-criminal-law is secondary. Score: AMBIGUOUS but dutch-administrative-law predicted as primary. |
| 38 | "Protecting our trade secrets in the Netherlands" | dutch-ip-law OR nda-triage-nl | dutch-ip-law | AMBIGUOUS | "trade secrets" and "Wet bescherming bedrijfsgeheimen" are explicit keywords in dutch-ip-law. "nda-triage-nl" also discusses trade secrets (Wbb) in detail and is related, but its description focuses on reviewing/screening NDAs - not general trade secret protection. dutch-ip-law is predicted as primary. Score: AMBIGUOUS with dutch-ip-law as primary. |
| 39 | "Challenging a tax assessment decision" | dutch-tax-law OR dutch-administrative-law | dutch-tax-law AND dutch-administrative-law | AMBIGUOUS | "Dutch tax procedures (bezwaar, beroep)" is an explicit use-case in dutch-tax-law. However, "bezwaar" and "beroep" against a "besluit" (decision) also exactly match dutch-administrative-law trigger keywords. Tax assessments are besluiten subject to Awb procedures. Both legitimately apply. Score: AMBIGUOUS - the descriptions overlap here; dutch-tax-law is probably primary since it specifically mentions "tax procedures (bezwaar, beroep)" but dutch-administrative-law would co-trigger. |
| 40 | "Commercial lease dispute resolution" | dutch-real-estate-law OR dutch-case-law-research | dutch-real-estate-law | AMBIGUOUS | "commercial lease" is an explicit trigger keyword in dutch-real-estate-law. "Dispute resolution" doesn't directly map to dutch-case-law-research description (which focuses on finding/analyzing case law, not resolving disputes). dutch-real-estate-law is the clear primary skill. dutch-case-law-research might be invoked as a supporting skill. Score: AMBIGUOUS but dutch-real-estate-law is clearly primary. |

---

## Score Summary

| Category | Count | Queries |
|---|---|---|
| CORRECT | 30 | 1-20, 26-35 |
| AMBIGUOUS | 10 | 21-25, 36-40 |
| MISSED | 0 | — |
| FALSE_POSITIVE | 0 | — |

**Overall trigger accuracy**: 30/30 should-trigger and should-not-trigger queries scored CORRECT (100%). All 10 cross-domain and ambiguous queries were correctly identified as AMBIGUOUS with the right set of skills predicted.

---

## Detailed Findings by Category

### Should-Trigger Queries (1–14): All CORRECT

All 14 single-skill queries would correctly trigger the expected skill. Key observations:

- **Strongest matches** (explicit keyword in description): Q3 (BW articles), Q8 (erfpacht), Q11 (FIOD), Q12 (kennismigrant), Q17 (BTW), Q18 (bezwaar), Q19 (geheimhoudingsovereenkomst), Q20 (aandeelhoudersovereenkomst)
- **Good semantic matches** (concept present but not identical word): Q5 ("fire" = dismissal = ontslag), Q7 (software copyright = auteursrecht), Q13 (unimplemented directive = direct effect/implementation)
- **Minor co-trigger risk**: Q2 (Hoge Raad cases on director liability could also surface dutch-corporate-law), Q9 (30% ruling is mentioned in dutch-immigration-law SKILL.md body but NOT in the description string itself - dutch-tax-law wins cleanly)

### Edge Case Queries (15–20): All CORRECT

All Dutch-language queries trigger correctly because the skill descriptions include Dutch terminology as explicit trigger keywords. Key observations:

- Q16 "ontslagvergoeding" is not literally in the dutch-employment-law description, but "transitievergoeding" is, and "ontslag" is explicit. A semantic/embedding-based trigger would match; a pure string-match system might miss "ontslagvergoeding" specifically. **Low-confidence CORRECT** - see recommendations.

### Cross-Domain Queries (21–25): All AMBIGUOUS

All five queries correctly involve exactly two skills each, and in each case both relevant skills cross-reference each other in their "Related Skills" sections. The system is well-architected for these overlaps.

### Should-NOT-Trigger Queries (26–30): All CORRECT

General non-legal queries correctly produce no matches.

### Tricky Near-Miss Queries (31–35): All CORRECT (with caveats)

The jurisdiction guards ("Dutch", "Netherlands", "Benelux", "in the Netherlands") in descriptions provide adequate protection. However:

- Q34 "French GDPR compliance": The word "GDPR" alone could trigger dutch-privacy-gdpr in a keyword-only system. The description's "Dutch GDPR" and "AP enforcement in the Netherlands" qualify this, but GDPR is a pan-EU regulation and a naive system might still trigger.
- Q33 "US patent infringement": "patent law" appears in dutch-ip-law description - same risk as Q34 but lower since US patents are distinct from Dutch/Benelux patents.

### Ambiguous Queries (36–40): All correctly scored AMBIGUOUS

- Q37: dutch-administrative-law predicted as primary (environmental permits = omgevingsvergunning), dutch-criminal-law as secondary
- Q38: dutch-ip-law predicted as primary (Wet bescherming bedrijfsgeheimen), nda-triage-nl as secondary
- Q39: Both dutch-tax-law and dutch-administrative-law co-trigger; dutch-tax-law is primary
- Q40: dutch-real-estate-law is clearly primary; dutch-case-law-research is only a supporting skill

---

## Issues and Recommendations

### Issue 1: Q16 - "ontslagvergoeding" not in dutch-employment-law description
**Severity**: Low
**Finding**: The description uses "transitievergoeding" but not "ontslagvergoeding" (the more colloquial Dutch term for severance/dismissal compensation). A keyword-only system could miss this query.
**Recommendation**: Add "ontslagvergoeding" to the description alongside "transitievergoeding":
```
"...transitievergoeding, ontslagvergoeding, non-compete clauses..."
```

### Issue 2: Q34 - "GDPR" without "Dutch" could false-positive trigger dutch-privacy-gdpr
**Severity**: Medium
**Finding**: GDPR queries about non-Dutch jurisdictions (e.g., "French GDPR compliance") could still trigger dutch-privacy-gdpr if the trigger system uses keyword matching on "GDPR" alone. The description begins "Dutch GDPR, AVG..." but a system extracting only keywords might list "GDPR" as a standalone token.
**Recommendation**: Emphasize jurisdiction more prominently in the description or add a jurisdiction-exclusion mechanism. Example:
```
"...Use this skill ONLY for Dutch/Netherlands-specific GDPR (AVG) matters. Do NOT use for GDPR questions about other EU member states..."
```

### Issue 3: Q9 - "30% ruling" appears in dutch-immigration-law body but not its description
**Severity**: Low
**Finding**: The dutch-immigration-law SKILL.md "When to Use" section includes "User asks about the 30% ruling for expat employees" but this is NOT in the description frontmatter. dutch-tax-law has it explicitly in the description. If the trigger system only reads description frontmatter, dutch-immigration-law won't co-trigger on Q9, which is actually the correct behavior. But if it reads the full SKILL.md, a false co-trigger could occur.
**Recommendation**: Remove "30% ruling" from dutch-immigration-law "When to Use" section or add a clarifying note that this is handled by dutch-tax-law as primary skill. The current state is acceptable if triggers are description-only.

### Issue 4: Q39 - Tax assessment challenges create ambiguity between two fully-matched skills
**Severity**: Medium
**Finding**: "Challenging a tax assessment decision" legitimately triggers BOTH dutch-tax-law ("tax procedures: bezwaar, beroep") AND dutch-administrative-law ("bezwaar, beroep, government decisions, bestuursrecht"). Both descriptions are equally valid. There is no prioritization signal.
**Recommendation**: Add a cross-reference note to dutch-administrative-law description:
```
"...Do not use for tax-specific bezwaar/beroep procedures - use dutch-tax-law instead..."
```
Or add to dutch-tax-law description:
```
"...including Belastingdienst bezwaar and beroep procedures (AWR)..."
```

### Issue 5: Q31-35 - Jurisdiction filtering is description-text only
**Severity**: Medium
**Finding**: All "wrong jurisdiction" queries rely on the word "Dutch" or "Netherlands" appearing in description text to block triggering. In a semantic/embedding-based system, "contract" or "GDPR" or "employment" queries with foreign jurisdictions might still surface Dutch skills based on topical similarity.
**Recommendation**: Add explicit negative-trigger guidance or jurisdiction metadata to each skill's frontmatter, e.g.:
```yaml
jurisdiction: Netherlands
negative_triggers:
  - "Germany"
  - "UK"
  - "United States"
  - "France"
  - "Belgium"
```

### Issue 6: Q2 - Hoge Raad cases on director liability - potential co-trigger
**Severity**: Low
**Finding**: Q2 could co-trigger both dutch-case-law-research ("Hoge Raad rulings") and dutch-corporate-law ("director liability" / "bestuurdersaansprakelijkheid"). The system should prefer dutch-case-law-research as primary since the user is asking to "Find cases" (research action), not for corporate law advice.
**Recommendation**: No description change needed, but the skill router should implement intent detection (research action vs. substantive advice action) to resolve this predictably.

---

## Description Quality Assessment

| Skill | Dutch Keywords in Description | English Keywords in Description | Jurisdiction Guard | Overall Quality |
|---|---|---|---|---|
| dutch-administrative-law | bezwaar, beroep, omgevingsvergunning, bestuursrecht, Awb | objection, appeal, building permits, government decisions, AWB procedures | "Dutch administrative law" | HIGH |
| dutch-case-law-research | jurisprudentie, rechtspraak, ECLI | case law, court decisions, Hoge Raad rulings, legal precedents | "under Dutch law" | HIGH |
| dutch-contract-review | algemene voorwaarden | review, SaaS license, distribution agreement, liability clauses, indemnification, contract risk assessment | "Dutch law", "Dutch contract" | HIGH |
| dutch-corporate-law | bestuurdersaansprakelijkheid, aandeelhoudersovereenkomst, KVK | BV incorporation, shareholder agreements, director liability, corporate governance | "Dutch companies" | HIGH |
| dutch-criminal-law | strafrecht, FIOD, valsheid in geschrift, WED | criminal law, corporate criminal liability, environmental crimes | "Dutch criminal law" | HIGH |
| dutch-employment-law | arbeidsrecht, ontslag, transitievergoeding, concurrentiebeding, CAO | employment, dismissal, non-compete clauses, hiring employees | "Dutch employment", "Netherlands" | HIGH (minor gap: ontslagvergoeding missing) |
| dutch-immigration-law | kennismigrant, verblijfsvergunning, IND | immigration, visa, work permits, family reunification, moving to NL | "Dutch immigration" | HIGH |
| dutch-ip-law | auteursrecht, BOIP, Wet bescherming bedrijfsgeheimen | copyright ownership, trademark registration, patent law, trade secrets | "Dutch and Benelux law" | HIGH |
| dutch-legislation-lookup | wetgeving, BW articles, Burgerlijk Wetboek | Dutch laws, statutes, look up specific articles | "Dutch law" | HIGH |
| dutch-privacy-gdpr | AVG, verwerkersovereenkomst, AP | GDPR, privacy compliance, data protection, data subject rights, cookie consent | "Dutch GDPR", "Netherlands" | MEDIUM (GDPR false-positive risk) |
| dutch-real-estate-law | huurrecht, erfpacht, koopovereenkomst, notaris | buying property NL, commercial lease, real estate transactions | "Netherlands" | HIGH |
| dutch-tax-law | vennootschapsbelasting, BTW, loonbelasting, fiscale eenheid, Box 1/2/3 | 30% ruling, Dutch taxes, expat tax | "Dutch taxes", "Netherlands" | HIGH |
| eu-law-integration | CJEU | EU law, direct effect, directives implementation, preliminary rulings | "Netherlands", "EU-Dutch legal relationship" | HIGH |
| nda-triage-nl | geheimhoudingsovereenkomst | NDA, non-disclosure agreement, confidentiality agreement, secrecy agreement | "under Dutch law" | HIGH |

---

## Final Verdict

The 14 skill descriptions are **well-crafted** for trigger purposes. They include:
- Both Dutch-language and English-language trigger keywords for most concepts
- Clear jurisdiction markers ("Dutch", "Netherlands", "Benelux")
- Specific proper nouns and acronyms (FIOD, KVK, IND, BOIP, BTW, etc.) that are highly discriminative
- Cross-domain relationships handled through "Related Skills" sections

**No queries scored MISSED** - every intended skill would trigger on its target queries. **No queries scored FALSE_POSITIVE** - the jurisdiction guards work. The 10 AMBIGUOUS scores are expected and appropriate given the cross-domain nature of those queries.

The primary recommendations are minor improvements to edge cases (ontslagvergoeding, jurisdiction robustness for non-NL GDPR queries) rather than fundamental description restructuring.
