## NDA Triage Report

**NDA Type**: Mutual (Wederzijds)
**Parties**: Not specified
**Governing Law**: Dutch law
**Review Perspective**: Balanced (mutual NDA, reviewing for both parties' interests)

## Overall Risk Level: YELLOW (with RED elements requiring attention)

The NDA has a standard structure and Dutch law governing clause, but contains several provisions that deviate significantly from market standard, including an overly broad definition of confidential information, a missing legally compelled disclosure carve-out, and a penalty clause at the upper end of the market range. These issues should be negotiated before signing.

## Clause-by-Clause Triage

### 1. Definition of Confidential Information
- **Rating**: RED
- **Finding**: The definition covers "all information shared between parties" without further specification, boundaries, or categories.
- **Market Standard**: A well-drafted NDA defines confidential information with reasonable specificity, typically including categories (technical, commercial, financial information) with a marking requirement (written information marked as "confidential" plus information reasonably understood to be confidential). The current definition is a catch-all that provides no meaningful boundary.
- **Risk**: An overly broad definition creates uncertainty about what is and is not covered. It may encompass publicly available information, trivial communications, and information the disclosing party does not own. Under Dutch law, a court applying the Haviltex standard might narrow the scope through interpretation, but this creates litigation risk and uncertainty. Additionally, such breadth may undermine enforceability, as it may be seen as unreasonable under Art. 6:248 lid 2 BW (derogating effect of reasonableness and fairness).
- **Action**: **Negotiate** -- Replace with a specific definition including categories of information, a marking requirement for written information, and a reasonableness standard for oral disclosures.

### 2. Term and Duration
- **Rating**: YELLOW
- **Finding**: 5-year term for the NDA agreement.
- **Market Standard**: Market standard for the agreement term is typically 1-3 years, with the confidentiality obligation surviving 2-3 years after termination (or indefinitely for trade secrets). A 5-year term is at the upper end but not unreasonable, depending on the nature of the business relationship and the information involved.
- **Risk**: A 5-year term may be longer than necessary if the business relationship or project is shorter. However, the term alone is not problematic if justified by the sensitivity and duration of information exchange.
- **Action**: **Accept with consideration** -- Verify that the 5-year term is proportionate to the anticipated business relationship. Consider whether the confidentiality obligation duration after termination is also specified (not mentioned in the NDA summary).

### 3. Standard Exceptions/Carve-Outs
- **Rating**: RED
- **Finding**: **No carve-out for legally compelled disclosure** is present. The NDA summary does not mention the other standard carve-outs (public domain, prior knowledge, independent development, third-party disclosure) either.
- **Market Standard**: Every well-drafted NDA under Dutch law should include four standard carve-outs: (1) public domain, (2) already known/independently developed, (3) received from a third party without restriction, and (4) legally compelled disclosure. The legally compelled disclosure provision is particularly critical because Dutch law imposes numerous statutory disclosure obligations (e.g., Wwft anti-money laundering reporting, AFM/DNB regulatory reporting, tax authority requests under AWR, Art. 843a Rv document production in litigation, and parliamentary inquiry obligations).
- **Risk**: Without a legally compelled disclosure carve-out, a party that discloses confidential information pursuant to a court order or regulatory requirement would technically be in breach of the NDA. This creates an impossible conflict between the NDA obligation and legal duties. A court would likely not enforce the NDA in such circumstances (applying Art. 6:248 lid 2 BW or Art. 3:40 BW), but relying on judicial correction is costly and uncertain.
- **Action**: **Reject current form** -- This is a critical gap. Insist on adding all four standard carve-outs, with the legally compelled disclosure carve-out as an absolute minimum. The legally compelled disclosure carve-out should include: (a) obligation to notify the disclosing party (if legally permitted), (b) limit disclosure to the minimum required, and (c) cooperate to obtain protective measures.

### 4. Residual Knowledge Clause
- **Rating**: YELLOW
- **Finding**: No residual knowledge clause is included.
- **Market Standard**: Residual knowledge clauses are not standard in most Dutch NDAs but are increasingly seen in technology and software transactions. Such a clause permits the receiving party to use general knowledge, skills, and experience retained in unaided memory after the NDA period.
- **Risk**: Without a residual knowledge clause, there is a theoretical risk that personnel who had access to confidential information could be accused of breach simply by applying general knowledge gained during the business relationship. In practice, this risk depends on the nature of the information and the sector.
- **Action**: **Consider adding** -- Particularly relevant if the NDA covers technology, software, or know-how where the boundary between specific confidential information and general knowledge is difficult to draw. Not a critical issue for all contexts.

### 5. Penalty Clause (Boetebeding)
- **Rating**: RED
- **Finding**: EUR 100,000 per breach plus EUR 10,000 per day of continuing breach.
- **Market Standard**: For mid-market/medium-risk transactions, market standard is EUR 10,000-25,000 per breach plus EUR 1,000-2,500 per day. For large/high-risk transactions, EUR 25,000-50,000 per breach plus EUR 2,500-5,000 per day. The specified penalty of EUR 100,000 per breach plus EUR 10,000 per day falls in the "strategic/critical" range and is at the upper boundary that triggers escalation consideration per the SKILL.md guidelines.
- **Legal Framework**: Under Art. 6:91-6:94 BW:
  - Art. 6:92 BW (default): the penalty replaces damages (no cumulation), unless the NDA deviates from this
  - Art. 6:94 BW: a court may moderate (matigen) the penalty if fairness clearly so requires ("indien de billijkheid dit klaarblijkelijk eist")
  - Per Hoge Raad (Intrahof/Bart Smit, HR 27 april 2007): moderation should be applied with restraint
- **Risk**: While Art. 6:94 BW provides a safety net, relying on judicial moderation is uncertain and expensive. The penalty amount is disproportionately high for a standard mutual NDA. Moreover, the daily penalty of EUR 10,000 without a specified cap means liability can escalate rapidly and unpredictably. It is not stated whether the penalty is in addition to or in lieu of actual damages -- if cumulative (deviating from Art. 6:92 BW), the exposure is even greater.
- **Action**: **Negotiate** -- Reduce the per-breach penalty to EUR 25,000-50,000 (depending on risk level). Reduce the daily penalty to EUR 2,500-5,000 with an explicit cap (e.g., maximum aggregate of EUR 250,000). Clarify whether the penalty is in lieu of or cumulative with actual damages. If cumulative, negotiate carefully.

### 6. Dispute Resolution
- **Rating**: GREEN
- **Finding**: Disputes via NAI arbitration (Nederlands Arbitrage Instituut).
- **Market Standard**: NAI arbitration is a recognized and standard dispute resolution mechanism for commercial contracts under Dutch law. It is specifically listed as GREEN in the SKILL.md triage criteria for NDA dispute resolution.
- **Risk**: NAI arbitration is confidential, which is appropriate for NDA disputes. However, arbitration costs can be significant, particularly for smaller disputes. Parties should ensure that the right to seek interim measures (kort geding) in state courts is preserved.
- **Action**: **Accept** -- but verify that the NDA preserves the right to seek interim measures (voorlopige voorzieningen) in Dutch state courts, which is critical for urgent NDA disputes where an imminent disclosure must be prevented. Under Dutch law, even with an arbitration clause, courts generally retain kort geding jurisdiction unless explicitly excluded.

## Missing Clauses

The following standard NDA clauses are not mentioned and should be reviewed:

1. **Return and destruction obligation** (teruggave en vernietiging) -- No mention of what happens with confidential information upon termination
2. **Scope of obligations** (how confidential information may be used; care standard) -- Not specified
3. **Permitted recipients** (employees, advisors, affiliates) -- Not specified
4. **Standard carve-outs** (public domain, prior knowledge, independent development, third-party receipt) -- Missing entirely
5. **Notice provisions** -- Not specified
6. **Assignment and transfer** -- Not specified
7. **Entire agreement clause** -- Not specified

## Priority Actions

1. **CRITICAL: Add legally compelled disclosure carve-out** -- Without this, the NDA creates an irreconcilable conflict with statutory disclosure obligations. This is the single most important change.
2. **CRITICAL: Add all four standard carve-outs** (public domain, prior knowledge, independent development, third-party disclosure) -- Their absence makes the NDA fundamentally incomplete.
3. **HIGH: Narrow the definition of confidential information** -- Replace "all information shared between parties" with a specific, bounded definition including categories and a marking mechanism.
4. **HIGH: Negotiate penalty clause downward** -- Reduce to proportionate levels (EUR 25,000-50,000 per breach, EUR 2,500-5,000 per day with a cap). Clarify relationship to actual damages.
5. **MEDIUM: Add return/destruction clause** -- Include obligation to return or destroy confidential information upon termination, with exceptions for legally required retention.
6. **MEDIUM: Verify interim measures preservation** -- Ensure the NAI arbitration clause does not exclude the right to seek kort geding for urgent matters.

## Summary

This mutual NDA has a fundamentally flawed confidential information definition (too broad), lacks essential carve-outs (particularly legally compelled disclosure), and contains a disproportionately high penalty clause. While the Dutch law governance and NAI arbitration are appropriate, the NDA should not be signed in its current form. The priority is to add the standard carve-outs, narrow the definition, and negotiate the penalty clause to proportionate levels. These are standard market requests that should not be controversial in a balanced mutual NDA negotiation.

---

**IMPORTANT - READ THIS DISCLAIMER CAREFULLY**

This is an AI-generated legal analysis and does **NOT constitute legal advice** within the meaning of the Dutch Advocates Act (Advocatenwet). The information in this analysis:

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by the Netherlands AI Lawyer System - an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2026-03-04*
