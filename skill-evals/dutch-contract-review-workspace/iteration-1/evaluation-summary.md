# Evaluation Summary: Dutch Contract Review Skill - Iteration 1

**Skill evaluated**: `dutch-contract-review`
**Date**: 2026-03-04
**Evaluator**: Automated skill evaluation
**Test prompts**: 2

---

## Aggregate Scores

| Test | Assertions | Passed | Score | Percentage |
|------|-----------|--------|-------|------------|
| Eval 1 (SaaS License) | 5 | 5 | 5.0/5.0 | 100% |
| Eval 2 (Distribution Agreement) | 4 | 4 | 4.0/4.0 | 100% |
| **Total** | **9** | **9** | **9.0/9.0** | **100%** |

---

## 1. Quality of Legal Analysis

**Rating: Strong**

Both responses demonstrate a high quality of legal analysis that goes beyond surface-level identification of issues.

**Eval 1 (SaaS License)**:
- The analysis correctly identifies the SaaS agreement as an innominate contract with elements of opdracht (Art. 7:400 BW), which reflects actual Dutch legal classification. Dutch law does not have a specific BW Book 7 title for software license agreements.
- The behandeling of the algemene voorwaarden issue is particularly thorough, correctly walking through the Art. 6:233/6:234 BW framework, the Art. 6:235 large enterprise exception, and the fallback to Art. 6:248 lid 2 BW.
- The IP analysis correctly identifies the akte requirement under Art. 2 Auteurswet for copyright assignment, which is a commonly overlooked technical requirement.
- The auto-renewal analysis appropriately references reflexwerking (analogous application of the Grey List to small B2B) and identifies the tension between 3-year lock-in and the fast-moving SaaS market.

**Eval 2 (Distribution Agreement)**:
- The distribution agreement is correctly classified as an innominate contract. Dutch law does not codify distribution agreements separately (unlike agency agreements under Art. 7:428 BW), which the response correctly identifies.
- The EU competition law analysis under the non-compete clause is the standout feature. The response correctly applies the VBER (Regulation (EU) 2022/720), identifies the Art. 5(3) safe harbor limits (1 year, limited to premises), and draws the correct conclusion about Art. 101(2) TFEU automatic voidness.
- The cross-clause analysis identifying the cumulative risk of unlimited indemnity plus excessive non-compete demonstrates the kind of integrated analysis that the skill's Process step 5 ("Cross-clause analysis") requires.

**Areas for improvement**:
- Neither response includes ECLI case law citations, which the skill's ethical guardrails require ("Every legal conclusion must reference specific BW articles or case law (ECLI citations)"). While BW article citations are extensive, adding relevant Hoge Raad or Gerechtshof case law would strengthen the analysis. For example, HR 14 June 2013 (ECLI:NL:HR:2013:BZ4163) on the scope of Art. 6:233 BW, or case law on proportionality of non-competes.
- The analysis could benefit from more explicit identification of mandatory vs. default law (dwingend recht vs. aanvullend/regelend recht) as specified in the skill's Process step 4c.

---

## 2. Accuracy of BW References

**Rating: Strong**

All BW article references were verified against the reference material in `bw-boek-6-7.md` and are accurate.

**Correctly cited and applied**:
- Art. 6:74 BW (toerekenbare tekortkoming) -- correctly used for liability/damages analysis
- Art. 6:96 BW (compensable damages including gederfde winst) -- correctly referenced in indemnity scope
- Art. 6:101 BW (eigen schuld/schadebeperkingsplicht) -- correctly applied to duty to mitigate in indemnity clause
- Art. 6:109 BW (rechterlijke matiging) -- correctly noted as judicial moderation power
- Art. 6:233 sub a and sub b BW -- correctly distinguished between content control and procedural requirement
- Art. 6:234 BW -- correctly described methods for providing reasonable opportunity
- Art. 6:235 BW -- correctly described the large enterprise exception
- Art. 6:237 sub g BW -- correctly identified as relevant Grey List provision for auto-renewal
- Art. 6:248 lid 2 BW -- correctly used as the general reasonableness safety valve throughout
- Art. 6:259 BW -- correctly cited for continuing performance contracts
- Art. 6:265 BW -- correctly referenced for dissolution rights
- Art. 7:400 BW -- correctly cited for opdracht classification
- Art. 2 Auteurswet -- correctly identified akte requirement for copyright transfer
- Art. 7 Auteurswet -- correctly noted employer copyright rule (and its inapplicability to client relationships)

**Non-BW references also accurate**:
- VBER (Regulation (EU) 2022/720) -- correct regulation number
- Art. 5(1)(a) and Art. 5(3) VBER -- correct provisions for non-compete safe harbor
- Art. 101(1), (2), and (3) TFEU -- correctly applied
- Art. 1020 et seq. Rv -- correct procedural law reference for arbitration

**No inaccurate citations were identified.**

---

## 3. Completeness of Risk Identification

**Rating: Strong**

**Eval 1**: All four risk areas mentioned in the test prompt were identified and analyzed:
- Liability cap (1x annual fees) -- rated GREEN with caveats about carve-outs (correct)
- Auto-renewal (3 years) -- rated RED (correct; exceeds market standard)
- Algemene voorwaarden (unseen) -- rated RED (correct; Art. 6:233 sub b violation)
- IP assignment (customizations) -- rated RED (correct; non-standard and unfavorable)

Additional risks identified beyond the prompt:
- Missing DPA under GDPR Art. 28
- Missing SLA, exit provisions, source code escrow
- Confidentiality warning per skill ethical guardrails

**Eval 2**: All three clause-level risks were identified:
- Unlimited indemnity -- rated RED (correct)
- 5-year EU-wide non-compete -- rated RED (correct)
- NAI arbitration -- rated YELLOW (correct; legitimate choice but cost and finality concerns)

Additional risks identified:
- EU competition law violation (VBER non-compliance) -- critically important addition
- Cumulative effect of unlimited indemnity plus excessive non-compete
- Missing liability cap, force majeure, product liability allocation

**Potential gaps**:
- Eval 1 could have more explicitly flagged the risk of the auto-renewal creating a lock-in that interacts with the IP assignment (i.e., switching costs compounded by loss of customization IP).
- Eval 2 could have discussed whether the indemnity clause might qualify as an "algemene voorwaarde" subject to Afdeling 6.5.3 BW content control if it was a standard term.

---

## 4. Proper Use of Traffic-Light System

**Rating: Strong**

Both responses consistently apply the GREEN/YELLOW/RED system at both individual clause level and overall contract level, exactly as specified in the skill's output format.

**Traffic light assignments evaluated**:

| Clause | Rating | Assessment |
|--------|--------|------------|
| Eval 1: Governing law (Dutch) | GREEN | Correct - standard and favorable |
| Eval 1: Liability cap (1x annual) | GREEN | Correct - within Playbook standard range |
| Eval 1: Auto-renewal (3 years) | RED | Correct - significantly exceeds market standard |
| Eval 1: Algemene voorwaarden (unseen) | RED | Correct - fundamental procedural defect |
| Eval 1: IP assignment | RED | Correct - materially unfavorable |
| Eval 1: Overall | RED | Correct - multiple RED clauses |
| Eval 2: Indemnity (unlimited) | RED | Correct - Playbook RED flag (blanket indemnity with no limitation) |
| Eval 2: Governing law (Dutch) | GREEN | Correct - standard |
| Eval 2: Arbitration (NAI Amsterdam) | YELLOW | Correct - legitimate but cost/appeal concerns |
| Eval 2: Non-compete (5yr, EU) | RED | Correct - exceeds both Playbook and VBER limits |
| Eval 2: Overall | RED | Correct - multiple RED clauses |

All ratings are consistent with the Dutch Contract Playbook benchmarks and the legal analysis provided.

---

## 5. Disclaimer Compliance

**Rating: Full compliance**

Both responses append the complete English-language disclaimer from `assets/disclaimers/disclaimer-en.md`. All seven numbered paragraphs are present. The date placeholder fields are populated with the current date (2026-03-04). The system attribution line is included.

The skill requirement states: "Always append the disclaimer from assets/disclaimers/ to every output." This requirement is met in both evaluations.

---

## 6. Skill Workflow Compliance

Evaluating against the 7-step Process defined in SKILL.md:

| Step | Description | Eval 1 | Eval 2 |
|------|-------------|--------|--------|
| 1 | Identify contract type | Yes (innominate SaaS/opdracht) | Yes (innominate distribution) |
| 2 | Check governing law | Yes (Dutch law confirmed) | Yes (Dutch law confirmed) |
| 3 | Extract key clauses | Yes (5 clauses identified) | Yes (4 clauses from excerpt) |
| 4 | Clause-by-clause analysis | Yes (all substeps a-e) | Yes (all substeps a-e) |
| 5 | Cross-clause analysis | Partial (gaps identified but limited cross-reference) | Yes (cumulative effect analysis) |
| 6 | Generate summary | Yes (executive summary with key risks and actions) | Yes (executive summary with key risks and actions) |
| 7 | Append disclaimer | Yes | Yes |

---

## 7. Suggestions for Skill Improvement

### 7.1 Case Law Citations
The skill's ethical guardrails require "Every legal conclusion must reference specific BW articles or case law (ECLI citations)." The reference materials (`bw-boek-6-7.md`, `nl-contract-playbook.md`, `algemene-voorwaarden.md`) provide extensive BW article references but contain zero ECLI case law citations. Adding a reference file with key case law per topic area (e.g., leading Hoge Raad decisions on liability caps, algemene voorwaarden, non-compete enforceability) would significantly improve the skill's ability to cite case law. A suggested new reference file: `references/key-case-law.md`.

### 7.2 Mandatory vs. Default Law Distinction
The skill Process step 4b/4c distinguishes between dwingend recht (mandatory law) and aanvullend/regelend recht (default law). The reference materials could more explicitly classify which BW provisions are mandatory and which are default. For example, a table in `bw-boek-6-7.md` marking each article as "dwingend" or "regelend" would help the skill produce more precise analysis.

### 7.3 B2B vs. B2C Detection
The skill's Process step 4d flags consumer protection rules "if B2C." The current reference materials describe the Black List and Grey List but do not provide a decision tree for determining whether a transaction is B2C or B2B. Adding explicit guidance on this classification (e.g., definitions of "consumer" under EU and Dutch law, mixed-purpose contracts) would improve consistency.

### 7.4 Cross-Clause Analysis Templates
Step 5 of the Process ("Cross-clause analysis") is under-specified compared to the detailed clause-by-clause instructions. Adding specific cross-clause checks to the playbook would improve this (e.g., "Does the indemnity sit outside the liability cap?", "Does the non-compete interact with IP assignment to create lock-in?", "Are termination provisions consistent with auto-renewal terms?").

### 7.5 Sector-Specific Playbook Extensions
The skill currently uses a general-purpose contract playbook. For common contract types (SaaS/IT, distribution, construction, employment), sector-specific playbook modules would improve the quality and specificity of recommendations. For example, a SaaS-specific module could address SLA standards, data processing, escrow, and uptime commitments.

### 7.6 Quantitative Risk Scoring
The GREEN/YELLOW/RED system is effective for communication but could be supplemented with a numerical risk score (e.g., 1-10 per clause, with weighted aggregate) to enable more granular comparison across contracts and over time.

### 7.7 MCP Tool Integration
The skill references MCP tools (`search_legislation`, `get_legislation`, `search_case_law`, `get_case_law`, `search_eu_legislation`) but these were not available during evaluation. When these tools are integrated, the skill should be tested with live legislation lookups to verify BW article citations against the current statutory text and to fetch supporting case law.

### 7.8 Disclaimer Localization
The skill should specify whether to use the English or Dutch disclaimer based on the language of the user's query. Currently the skill says "Append the appropriate disclaimer from assets/disclaimers/" but does not define selection criteria.

---

## Conclusion

The dutch-contract-review skill performs well across both test scenarios. It produces structured, legally grounded analysis that follows the specified workflow, applies the traffic-light system consistently, cites relevant BW articles accurately, and appends the required disclaimer. The main areas for improvement relate to case law citation capability (which requires expanding reference materials), more explicit mandatory/default law classification, and sector-specific playbook depth. The skill is ready for production use with the caveat that users should be encouraged to verify BW article citations independently, particularly as legislative amendments may post-date the reference materials.
