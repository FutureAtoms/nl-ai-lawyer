# NDA Triage Report

**NDA Type**: Mutual (Wederzijdse geheimhoudingsovereenkomst)
**Governing Law**: Dutch law
**Review Perspective**: General risk assessment (applicable to both parties equally, as mutual)
**Term**: 5-year agreement term
**Penalty**: EUR 100,000 per breach + EUR 10,000 per day continuing breach
**Dispute Resolution**: NAI arbitration

---

## Quick Summary Table

| Clause | Rating | Key Issue |
|--------|--------|-----------|
| Definition of Confidential Information | RED | "All information shared between parties" — dangerously overbroad; no carve-outs for public information, prior knowledge, or independent development |
| Scope of Obligations | YELLOW | Not specified beyond the definition issue, but the overbroad definition creates an effectively absolute obligation |
| Exceptions/Carve-outs | RED | No carve-out for legally compelled disclosure (court order, regulatory obligation); missing all four standard exceptions |
| Term & Duration | YELLOW | 5-year term is at the upper boundary of market standard; acceptable for strategic partnerships but warrants review |
| Return/Destruction | NOT SPECIFIED | No return/destruction clause mentioned — a missing standard provision |
| Penalty Clause (Boetebeding) | RED | EUR 100,000 per breach + EUR 10,000/day — at or above the RED threshold; no cap mentioned; cumulative with damages not specified |
| Non-Solicitation | NOT SPECIFIED | No non-solicitation clause mentioned |
| Residual Knowledge | RED | No residual knowledge clause — significant risk for individuals who cannot "unlearn" information |
| Governing Law & Disputes | GREEN | Dutch law; NAI arbitration is a recognized and appropriate forum for commercial disputes |
| **Overall Rating** | **RED** | **Multiple fundamental deficiencies requiring immediate attention before signing** |

---

## Overall Risk Level: RED

This NDA has three serious structural deficiencies that make it inadvisable to sign in its current form:
1. The definition of confidential information is dangerously overbroad
2. The absence of a legally compelled disclosure carve-out creates an irresolvable conflict with Dutch and EU legal obligations
3. The penalty structure is at the extreme upper end of enforceability and warrants judicial scrutiny

---

## Clause-by-Clause Triage

### Clause 1: Definition of Confidential Information — RED

**Finding**: The NDA defines confidential information as "all information shared between parties." This is a catch-all definition with no boundaries whatsoever.

**Why this is RED:**

1. **Overbroad and legally unworkable**: This definition covers every piece of information exchanged between the parties, regardless of its nature, sensitivity, or whether it was intended to be confidential. It would include:
   - Publicly available information (news, public company filings, published research)
   - Information already known to the receiving party before the NDA
   - Business card details, general pleasantries, information discussed at public events
   - Information independently developed by the receiving party

2. **No marking or designation requirement**: There is no mechanism to identify which information is actually confidential in practice. This makes the obligation effectively unlimited.

3. **Conflict with market standard**: Market standard Dutch NDAs define confidential information by:
   - Reference to specific categories (technical, commercial, financial)
   - A marking requirement (labeled "Confidential" or "Vertrouwelijk") OR
   - A catch-up provision covering information reasonably understood to be confidential in context
   - But always with the four standard exceptions (see Clause 3 below)

4. **Enforceability risk**: Under the Haviltex interpretation standard (HR 13 maart 1981, NJ 1981/635), Dutch courts will look at what parties reasonably could have understood. An overbroad definition may be moderated by a court — but this creates uncertainty rather than clarity.

**Action: Reject. Negotiate a specific, category-based definition with clear carve-outs.**

---

### Clause 2: Standard Exceptions/Carve-Outs — RED

**Finding**: The NDA contains **no carve-out for legally compelled disclosure** and apparently no other standard exceptions.

**Why this is RED:**

A well-drafted Dutch NDA must include (at minimum) the following four standard carve-outs:

1. **Public domain**: Information that is or becomes publicly available (not through the receiving party's fault)
2. **Prior knowledge**: Information already known to the receiving party at the time of disclosure
3. **Independent development**: Information independently developed by the receiving party without use of the disclosed information
4. **Third-party disclosure**: Information received from a third party who was not under a confidentiality obligation

**The missing legally compelled disclosure provision is the most serious omission:**

Without a legally compelled disclosure carve-out, the receiving party is nominally contractually prohibited from:
- Responding to a court order for document production (Art. 843a Rv — exhibitieplicht)
- Filing mandatory regulatory reports under the Wwft (anti-money laundering law)
- Responding to requests from AFM, DNB, or other supervisory authorities under the Wft
- Providing information required by the Belastingdienst under the AWR
- Complying with a parliamentary inquiry (Wet op de parlementaire enquete)

**This creates an irresolvable conflict**: Complying with the NDA would require breach of statutory duties; complying with statutory duties would require breach of the NDA. A Dutch court would likely find this clause unreasonably onerous under Art. 6:248 lid 2 BW (derogating effect of reasonableness and fairness), but this would only be determined in litigation — leaving the party uncertain in the interim.

**Action: Reject. Insist on all four standard carve-outs plus a legally compelled disclosure provision.**

---

### Clause 3: Penalty Clause (Boetebeding) — RED

**Finding**: EUR 100,000 per breach + EUR 10,000 per day continuing breach, with no cap mentioned.

**Legal framework**: Arts. 6:91–6:94 BW govern penalty clauses in Dutch law.

#### Penalty Exposure Analysis

| Scenario | Calculation | Total |
|----------|-------------|-------|
| Single breach, no continuation | EUR 100,000 × 1 | **EUR 100,000** |
| Single breach, 30-day continuation | EUR 100,000 + (EUR 10,000 × 30) | **EUR 400,000** |
| Single breach, 90-day continuation | EUR 100,000 + (EUR 10,000 × 90) | **EUR 1,000,000** |
| Maximum theoretical (1 year, 1 breach) | EUR 100,000 + (EUR 10,000 × 365) | **EUR 3,750,000** |
| Multiple breaches (e.g., 5 discrete incidents) | EUR 100,000 × 5 | **EUR 500,000** (before daily accrual) |

**Why this is RED:**

1. **Per-breach amount at the extreme threshold**: EUR 100,000 per breach sits at the very top of the SKILL.md's RED threshold (penalty exceeding EUR 100,000 per breach). Even at exactly EUR 100,000, this is a significant deterrent and at the upper boundary of what courts routinely enforce without question.

2. **Daily penalty of EUR 10,000**: EUR 10,000 per day is above the market standard for mid-market agreements (EUR 2,500–5,000/day). It is within the "strategic/critical" tier but without a cap, it creates unlimited exposure.

3. **No cap mentioned**: The absence of a cap on the daily penalty means exposure is theoretically unlimited. For the overbroad definition of confidential information in this NDA, this means an inadvertent breach (e.g., mentioning publicly available information to a third party) could trigger unlimited daily liability.

4. **Interaction with overbroad definition**: The combination of (a) "all information shared" and (b) EUR 100,000/breach + EUR 10,000/day creates extreme systemic risk. Nearly any communication about the business relationship to any third party could constitute a "breach."

5. **Judicial moderation (Art. 6:94 BW)**: Courts can reduce a penalty if "fairness clearly so requires" (klaarblijkelijk). Under HR 27 april 2007 (ECLI:NL:HR:2007:AZ6638, Intrahof/Bart Smit), moderation should be applied with restraint in B2B contracts. A court may moderate a grossly disproportionate penalty, but this is litigated — not guaranteed in advance, and the process itself is costly.

6. **No cumulation clause specified, but uncertainty**: The NDA does not clarify whether the penalty replaces damages (default under Art. 6:92 lid 2 BW) or is cumulative with actual damages. If the counterparty includes a cumulation clause (often inserted in Dutch NDAs as "onverminderd het recht op volledige schadevergoeding"), liability exposure doubles.

**Action: Negotiate. If proceeding, insist on: (a) reduction of per-breach penalty to EUR 25,000–50,000; (b) reduction of daily penalty to EUR 2,500–5,000; (c) a total cap (e.g., EUR 500,000); (d) clarity on whether penalty replaces or is cumulative with damages; (e) ingebrekestelling requirement before daily penalty accrues.**

---

### Clause 4: Term and Duration — YELLOW

**Finding**: 5-year agreement term.

**Assessment**: The 5-year term is at the upper boundary of market standard (typically 2–3 years for the information-exchange period, with confidentiality obligations surviving for 2–5 years after termination). A 5-year term is not inherently unreasonable for a strategic partnership with long-cycle information exchange (e.g., multi-year technology development, M&A exclusivity), but warrants scrutiny:

- Is the 5-year term the period during which information is exchanged, or the confidentiality obligation period post-termination?
- If the 5-year term is the confidentiality obligation period post-termination of the relationship, this approaches the upper limit and would be YELLOW/RED for non-trade-secret information.
- Trade secrets: may appropriately be protected indefinitely (aligned with Wbb, which provides protection without a time limit)
- Ordinary confidential information: a 5-year post-termination obligation is at the edge and may be subject to Art. 6:248 lid 2 BW moderation in extreme cases

**Action**: Clarify. Distinguish between (a) the term during which information is exchanged and (b) the duration of the confidentiality obligation post-termination.

---

### Clause 5: Residual Knowledge — RED

**Finding**: No residual knowledge clause.

**Why this matters**: The overbroad definition ("all information shared") combined with no residual knowledge clause means that employees who have been involved in the business relationship are permanently restricted from using knowledge they retain in their memory — even general skills and experience. This is:
- Practically unenforceable (people cannot "unlearn" experience)
- Potentially in conflict with employee freedom of movement (Art. 7:653 BW principles)
- Particularly problematic for technical staff and software developers who absorb methodologies and approaches through exposure

The absence of a residual knowledge clause in combination with an overbroad definition creates unrealistic obligations.

**Action**: Insist on a residual knowledge clause limiting the obligation to specific, documented confidential information — not general knowledge, skills, and experience retained in unaided memory.

---

### Clause 6: Dispute Resolution — GREEN

**Finding**: NAI (Nederlands Arbitrage Instituut) arbitration.

**Assessment**: NAI arbitration is a recognized and well-regarded dispute resolution forum for Dutch commercial disputes. Key features:
- Confidentiality of proceedings (important for NDAs — keeps disputes about confidential information out of public court files)
- Specialist arbitrators with commercial expertise
- Enforceable internationally under the New York Convention
- NAI arbitration clauses are routinely used in Dutch commercial contracts

**One important note**: Even with an NAI arbitration clause, Dutch courts retain jurisdiction for interim measures (kort geding, Art. 254 Rv) unless the clause explicitly and validly excludes this. For NDA disputes involving imminent disclosure of confidential information, kort geding is the fastest and most effective remedy. Confirm that the arbitration clause does not inadvertently waive the right to seek interim measures.

**Action**: Accept, subject to confirming that kort geding rights are preserved.

---

### Clause 7: Missing Clauses

The following standard NDA provisions appear to be absent:

| Missing Clause | Importance | Risk Level |
|----------------|------------|------------|
| Legally compelled disclosure carve-out | Critical | RED |
| Return/destruction obligation | Standard | YELLOW |
| Four standard carve-outs (public domain, prior knowledge, independent development, third-party disclosure) | Critical | RED |
| Residual knowledge clause | Important for technical relationships | YELLOW |
| Non-solicitation (if relevant) | Optional | N/A |
| Ingebrekestelling requirement for penalty accrual | Important for proportionality | YELLOW |
| Cap on total penalty | Important | YELLOW |
| Survival clause (which obligations survive termination) | Standard | YELLOW |

---

## Priority Actions

1. **REJECT the confidential information definition**. Replace "all information shared between parties" with a category-based definition covering specific categories (technical know-how, business plans, financial data, customer lists, etc.) plus a reasonable catch-up provision, with all four standard carve-outs.

2. **ADD the legally compelled disclosure carve-out** — without this, you cannot safely comply with your legal obligations as a Dutch business. This is non-negotiable.

3. **NEGOTIATE the penalty clause**: Request a per-breach reduction (EUR 25,000–50,000 is market standard for mid-market), a daily penalty reduction (EUR 2,500–5,000), and a total aggregate cap. Clarify whether penalty is cumulative with or replaces actual damages.

4. **ADD the residual knowledge clause** to address the practical reality that employees retain general knowledge and experience.

5. **ADD return/destruction obligations** with appropriate exceptions for legally mandated retention periods.

6. **CLARIFY the 5-year term**: Is this the agreement term (information exchange period) or the post-termination confidentiality period?

7. **CONFIRM kort geding rights** are not waived by the NAI arbitration clause.

---

## Summary

This mutual NDA has an **overall RED rating**. The combination of an overbroad confidential information definition (all information exchanged), the complete absence of legally compelled disclosure carve-outs, and a penalty clause at the extreme upper boundary of enforceability (EUR 100,000/breach + EUR 10,000/day uncapped) makes this NDA inadvisable to sign in its current form. Signing this NDA as drafted would create obligations that conflict with your statutory duties under Dutch law and expose you to theoretically unlimited financial liability for inadvertent disclosures of information that was never genuinely confidential. This NDA requires material negotiation before execution.

---

**IMPORTANT - READ THIS DISCLAIMER CAREFULLY**

This is an AI-generated legal analysis and does **NOT constitute legal advice** within the meaning of the Dutch Advocates Act (Advocatenwet). This triage report is a pre-screening assessment only — it does not constitute a full legal opinion on the enforceability of any specific clause. The information in this analysis:

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by the Netherlands AI Lawyer System — an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
