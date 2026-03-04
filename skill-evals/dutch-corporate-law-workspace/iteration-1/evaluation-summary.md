# Dutch Corporate Law Skill Evaluation - Iteration 1

**Date**: 2026-03-04
**Skill**: dutch-corporate-law
**Skill Path**: ~/uncloud/nl-ai-lawyer/skills/dutch-corporate-law/

---

## Overall Result: PASS (9/9 criteria met)

---

## Test 1: BV Formation with Two Founders (60/40 Split)

**Prompt**: "I'm setting up a Dutch BV with two founders (60/40 split). We want a board with both founders as directors plus an advisory board. What's the minimum share capital, what governance structure do you recommend, and what should go in the aandeelhoudersovereenkomst?"

**Output**: `eval-1-with_skill/output.md`

### Grading Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| mentions_flex_bv | PASS | Explicitly discusses the Flex-BV Act (1 October 2012), removal of EUR 18,000 minimum, EUR 0.01 minimum per share, non-voting/non-profit shares, optional blokkeringsregeling |
| references_boek_2 | PASS | 15+ specific BW Boek 2 article citations including Art. 2:175, 2:178, 2:192, 2:195, 2:196, 2:216, 2:217, 2:224, 2:239, 2:239a, 2:240, 2:242, 2:244, 2:245, 2:250 |
| discusses_shareholders_agreement | PASS | Comprehensive coverage of aandeelhoudersovereenkomst: tag-along, drag-along, ROFR, lock-up, reserved matters, deadlock resolution, non-compete, good/bad leaver, IP, dividend policy, financing, exit |
| mentions_kvk | PASS | Discusses KVK registration (Handelsregisterwet 2007), 8-day deadline, EUR 75 fee, UBO registration, tekenbevoegdheid registration |
| includes_disclaimer | PASS | Full 7-point disclaimer matching the prescribed template from assets/disclaimers/disclaimer-en.md |

**Score**: 5/5

### Quality Assessment

**Strengths**:
- Follows the skill's prescribed output format (Corporate Law Analysis, Applicable Legal Framework, Analysis, Practical Requirements, Key Risks, Recommendations, Disclaimer)
- Provides practical share capital structuring advice (60 shares / 40 shares at EUR 1.00 each)
- Distinguishes between the informal advisory board (raad van advies) and the statutory supervisory board (Raad van Commissarissen) under Art. 2:250 BW
- Covers both one-tier and two-tier board options with a clear recommendation
- Discusses the uitkeringstest (Art. 2:216 BW) and director liability for distributions
- Recommends holding structure for tax optimization
- Flags the notarial deed requirement as mandatory (Art. 2:175 BW)
- Identifies Wwft/anti-money laundering obligations per skill's ethical guardrails
- Provides cost estimates and timeline

**Weaknesses**:
- Could have included more case law references (e.g., Ondernemingskamer decisions on advisory board roles)
- Does not mention the SER Fusiegedragsregels (not directly applicable here, but part of the framework)
- Tax implications are flagged but not elaborated (appropriate per skill guardrails)

---

## Test 2: Related Party Transaction with Minority Shareholder Objection

**Prompt**: "Our Dutch BV board approved a transaction with a related party (one director's other company) worth EUR 500K. The minority shareholder (30%) is objecting. What are the legal implications under Dutch corporate law?"

**Output**: `eval-2-with_skill/output.md`

### Grading Criteria

| Criterion | Result | Evidence |
|-----------|--------|----------|
| mentions_conflict_interest | PASS | Extensive treatment of tegenstrijdig belang under Art. 2:239 lid 6 BW, WBTR 2021 codification, recusal requirement, consequences of improper conflict management, CGC Chapter 2 |
| discusses_minority_protection | PASS | Covers Art. 2:15 annulment, enqueteprocedure (Art. 2:344-2:359), Ondernemingskamer powers, Art. 2:8 reasonableness/fairness, Art. 6:162 tort, kort geding option, 10% threshold analysis |
| cites_bw (art. 2:xxx) | PASS | 12+ specific Art. 2:xxx citations: Art. 2:8, 2:9, 2:14, 2:15, 2:239, 2:239 lid 6, 2:344, 2:345, 2:349a, 2:355, 2:224a, plus Art. 6:162 |
| includes_disclaimer | PASS | Full 7-point disclaimer matching the prescribed template |

**Score**: 4/4

### Quality Assessment

**Strengths**:
- Follows the skill's prescribed output format precisely
- Correctly identifies and applies Art. 2:239 lid 6 BW (the WBTR conflict of interest rule) as the primary provision
- Provides three practical scenarios (arm's length + proper process; conflict not managed; not arm's length) with escalating consequences
- Correctly identifies the 30% shareholder as exceeding the 10% threshold for the enqueteprocedure
- Discusses both the voidability of the resolution (Art. 2:15 BW) and the underlying standard (Art. 2:8 BW)
- Addresses director liability under both Art. 2:9 BW (internal) and Art. 6:162 BW (external/tort)
- Identifies escalation triggers per the skill definition: shareholder dispute, potential wanbeleid, enqueteprocedure
- Provides actionable practical steps for the minority shareholder
- Includes the arm's length assessment framework and corporate benefit (vennootschappelijk belang) analysis

**Weaknesses**:
- Could have referenced specific Ondernemingskamer case law (e.g., on wanbeleid findings in related party transactions)
- Does not discuss potential criminal law implications in depth (mentions Art. 321-323 Sr briefly)
- Could have discussed the role of the accountant in detecting related party transactions in the annual accounts

---

## Skill Compliance Assessment

### Process Adherence (per SKILL.md)

| Step | Compliance |
|------|------------|
| 1. Identify entity type | PASS - Both outputs correctly identify BV |
| 2. Determine legal question | PASS - Both clearly formulate the legal question |
| 3. Research applicable provisions | PASS - Both reference BW Boek 2 and related legislation |
| 4a. Mandatory vs optional provisions | PASS - Both distinguish mandatory (notarial deed, KVK) from optional (advisory board, blokkeringsregeling) |
| 4b. Articles of association requirements | PASS - Both discuss statuten requirements |
| 4c. Corporate governance code | PASS - Both reference the 2022 Code as best practice for private BVs |
| 4d. Case law review | PARTIAL - Limited case law citations; references are primarily statutory |
| 5. Practical guidance | PASS - Both include next steps, timelines, and costs |
| 6. Disclaimer appended | PASS - Full disclaimer in both outputs |

### Ethical Guardrails Adherence

| Guardrail | Test 1 | Test 2 |
|-----------|--------|--------|
| Mandatory disclaimer | PASS | PASS |
| Notarial requirement emphasized | PASS | N/A |
| No UBO screening for avoidance | PASS | N/A |
| Wwft awareness | PASS (mentioned) | N/A |
| Tax implications flagged | PASS | N/A |
| Cross-border complexity | N/A | N/A |

### Output Format Adherence

Both outputs follow the prescribed format from SKILL.md:
- Corporate Law Analysis header with Entity Type and Legal Question
- Applicable Legal Framework section
- Analysis section with article references
- Practical Requirements with mandatory steps, timeline, costs, and required professionals
- Key Risks section
- Recommendations section
- Disclaimer at the end

---

## Summary

The dutch-corporate-law skill performed well across both test scenarios. The WITH-SKILL responses demonstrate:

1. **Strong statutory grounding** - Extensive and accurate BW Boek 2 article references throughout both outputs.
2. **Practical utility** - Both outputs provide actionable next steps, cost estimates, timelines, and professional referrals.
3. **Proper structure** - Both outputs follow the prescribed format from the SKILL.md output template.
4. **Ethical compliance** - Disclaimers included, notarial requirements emphasized, tax implications flagged without overstepping.
5. **Flex-BV awareness** - Test 1 correctly reflects the post-2012 Flex-BV legal framework.
6. **Minority protection depth** - Test 2 provides a thorough analysis of the multiple legal avenues available to the minority shareholder.

**Area for improvement**: Both outputs could benefit from more specific case law citations (Ondernemingskamer decisions, Hoge Raad jurisprudence) to strengthen the analysis beyond purely statutory references.

**Overall Grade**: PASS (9/9 criteria, 100%)
