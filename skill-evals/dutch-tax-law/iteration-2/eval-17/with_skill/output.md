# Tax Law Analysis

**Tax Type**: Vennootschapsbelasting (VPB) - Corporate Income Tax
**Taxpayer**: Dutch BV (resident entity), considering fiscale eenheid with 100% subsidiary
**Tax Year**: 2024/2025 (rates as stated below; verify annually)

---

## Applicable Legal Framework

- **Wet op de vennootschapsbelasting 1969 (Wet VPB)** - in particular:
  - **Art. 15 Wet VPB** - Fiscale eenheid (fiscal unity) regime
  - Art. 7-8 Wet VPB - Taxable base
  - Art. 20 Wet VPB - Loss compensation (verliesverrekening)
  - Art. 15b Wet VPB - Earnings stripping (ATAD implementation)
- **Uitvoeringsbeschikking fiscale eenheid vennootschapsbelasting 2003** (UFFE 2003)
- CJEU 22 February 2018, C-398/16 and C-399/16 (X BV and X NV) - per-element approach and spoedreparatiemaatregelen
- HR 17 december 2004, ECLI:NL:HR:2004:AQ3810 - Requirements for 95% ownership

---

## Background: What Is a Fiscale Eenheid?

A fiscale eenheid (fiscal unity) under art. 15 Wet VPB allows a parent company and one or more subsidiaries to be treated as a single taxpayer for Dutch corporate income tax (vennootschapsbelasting) purposes. The group files a single consolidated VPB return through the parent.

---

## Current Requirements (Art. 15 Wet VPB)

To form and maintain a fiscale eenheid, all of the following conditions must be met:

1. **Ownership threshold**: The parent must hold at least **95%** of the legal and economic ownership (juridisch en economisch eigendom) of the shares in the subsidiary. In your case, a 100% subsidiary clearly satisfies this requirement.

2. **Dutch tax residency**: Both the parent BV and the subsidiary must be resident in the Netherlands for VPB purposes, or alternatively have a Dutch permanent establishment (vaste inrichting). Foreign entities generally cannot be members of a Dutch fiscale eenheid for VPB purposes (with limited EU exceptions following CJEU case law).

3. **Aligned financial year**: Both entities must have the same financial year (boekjaar).

4. **Consistent profit determination**: Both entities must apply the same profit determination methods (winstbepalingsmethoden).

5. **Formal application**: A joint request must be filed with the Belastingdienst using the prescribed form. The fiscale eenheid generally takes effect from the first day of the month following the month in which the request is submitted (or from the moment of incorporation of the subsidiary if requested within 3 months).

6. **Legal form**: Both parent and subsidiary must be entities subject to VPB (BV, NV, cooperative, etc.).

---

## Advantages of Forming a Fiscale Eenheid

### 1. Consolidation of Profits and Losses (Verliesverrekening)

The most significant benefit for many groups is the ability to consolidate taxable results. Losses of one group member are automatically offset against profits of other members in the same tax year. For your group with EUR 2M consolidated profit:

- If the subsidiary is currently loss-making, those losses directly reduce the parent's taxable profit in the same year, without waiting for future carry-forward;
- Conversely, if the subsidiary is currently profitable but the parent has historic losses, consolidation enables immediate offset.

Under the standard VPB loss rules (art. 20 Wet VPB, as amended since 2022), losses above EUR 1M can only be offset at 50% per year. Inside a fiscale eenheid, current-year losses of one member are fully offset against current-year profits of another member, bypassing this limitation.

### 2. Internal Transactions Are Ignored (Interne Transacties)

Transactions between members of the fiscale eenheid - including:
- Intercompany sales of goods and services
- Asset transfers between group companies
- Intercompany financing

...are disregarded for VPB purposes while the fiscale eenheid exists. This means:
- No immediate profit or loss recognition on intercompany asset transfers;
- No VPB on intercompany margin on goods/services;
- Simplifies cash management and intercompany structuring.

### 3. Single Tax Return

The parent files one consolidated VPB return covering the entire group, significantly reducing compliance burden and costs.

### 4. Capital Gains on Internal Restructuring

Reorganizations within the fiscale eenheid (e.g., transferring a business unit or assets between group members) generally do not trigger immediate VPB. This provides significant flexibility for group restructuring.

---

## Indicative Tax Calculation (Without Fiscale Eenheid)

With EUR 2M taxable profit, the parent BV pays VPB at the following rates (2024):

| Bracket | Rate | Amount |
|---------|------|--------|
| First EUR 200,000 | 19% | EUR 38,000 |
| Remaining EUR 1,800,000 | 25.8% | EUR 464,400 |
| **Total VPB** | | **EUR 502,400** |

The subsidiary's separate result would be calculated and taxed independently.

Under a fiscale eenheid, the consolidated taxable result of both entities is taxed together as a single taxpayer. Whether this produces a better or worse outcome depends on the subsidiary's profit or loss position:
- Subsidiary with losses: overall taxable base is reduced, lowering the total VPB;
- Subsidiary with profits: profits are aggregated, which may push more income into the 25.8% bracket, compared to two separate entities each benefiting from the lower 19% band up to EUR 200,000.

*Note: The 19% bracket applies once within a fiscale eenheid (not per entity), which may be a disadvantage for groups where both entities are individually profitable but each below EUR 200,000.*

---

## Risks and Limitations

### 1. Joint and Several Liability (Hoofdelijke Aansprakelijkheid)

This is the most significant risk. All members of the fiscale eenheid are jointly and severally liable (hoofdelijk aansprakelijk) for the entire group's VPB debt. This means:
- The Belastingdienst can collect from any member of the fiscale eenheid for VPB owed by any other member;
- If the subsidiary incurs significant tax liabilities (including penalties, vergrijpboetes), the parent becomes exposed;
- This risk persists even after the fiscale eenheid is dissolved (ontvoeging) for liabilities accrued during the unity period.

### 2. Loss of Individual 19% Bracket

Within a fiscale eenheid, only one EUR 200,000 bracket at 19% applies to the consolidated group, not per entity. For groups where both entities are individually profitable but each below EUR 200,000, forming a fiscale eenheid may increase the total VPB rate.

### 3. Entry and Exit Consequences (Voegings- en Ontvoeginggevolgen)

Forming (voeging) or dissolving (ontvoeging) a fiscale eenheid triggers specific consequences:
- Intercompany transactions effected during the unity period are "unwound" at the moment of exit, potentially triggering deferred gains or losses;
- Exit from the fiscale eenheid requires careful analysis of asset basis, loss positions, and hidden reserves (stille reserves);
- The Belastingdienst has broad powers to adjust upon exit.

### 4. Spoedreparatiemaatregelen (Following CJEU Case Law)

Following the CJEU ruling in C-398/16 and C-399/16 (2018), the Netherlands introduced "emergency repair measures" (spoedreparatiemaatregelen). These apply certain anti-abuse and interest deduction limitation rules (art. 10a, 15b Wet VPB) as if the fiscale eenheid does not exist for those specific purposes. This reduces some of the structuring advantages historically available within a fiscale eenheid.

### 5. Anti-Avoidance Provisions Apply

Art. 15b Wet VPB (earnings stripping, ATAD implementation) limits net interest deductibility to 20% of fiscal EBITDA (with a EUR 1M floor). The fiscale eenheid does not eliminate this rule.

Art. 10a Wet VPB (anti-base erosion) disallows interest on loans connected to certain tainted transactions with related parties, even within a fiscale eenheid for the purposes of the spoedreparatiemaatregelen.

### 6. Cross-Border Limitations

Cross-border fiscal unity with EU subsidiaries remains limited. While the CJEU has required the Netherlands to offer some relief for "final losses" of EU subsidiaries (Marks & Spencer doctrine), a full fiscale eenheid with non-Dutch EU entities is not generally available for VPB purposes.

---

## Compliance Obligations

- File a joint VPB aangifte annually through the parent;
- Submit a joint request to the Belastingdienst to establish the fiscale eenheid;
- Maintain transfer pricing documentation for arm's length dealings with parties outside the fiscale eenheid (art. 8b Wet VPB);
- Monitor annual legislative changes to VPB rates, brackets, and anti-avoidance provisions.

---

## Anti-Avoidance Considerations

- The fiscale eenheid regime itself is a legitimate statutory tool, not a tax avoidance structure. However, forming a fiscale eenheid solely to exploit the internal transaction rules, without genuine business integration, may attract scrutiny under fraus legis or specific anti-abuse rules;
- DAC6 may be triggered in cross-border arrangements involving a fiscale eenheid with international elements;
- The spoedreparatiemaatregelen specifically limit the use of the fiscale eenheid to circumvent art. 10a Wet VPB.

---

## Recommendations

1. **Quantify the benefit**: Model the consolidated VPB under a fiscale eenheid versus two separate filings, accounting for both entities' current-year results and any historic losses;

2. **Assess joint liability exposure**: Evaluate the subsidiary's tax risk profile, potential exposures, and whether the joint and several liability risk is acceptable;

3. **Consider the 19% bracket impact**: If both entities are individually profitable and each falls within the EUR 200,000 low-rate bracket, forming a fiscale eenheid may increase rather than decrease total VPB;

4. **Review entry and exit rules**: Before proceeding, analyze the consequences of future dissolution (ontvoeging) under the current rules;

5. **Engage a belastingadviseur**: Given the complexity of the fiscale eenheid regime, particularly following the spoedreparatiemaatregelen, engage a qualified Dutch tax advisor to model scenarios and prepare the formal request;

6. **File promptly**: Once the decision is made, file the request with the Belastingdienst within the applicable window to achieve retroactive effect from the desired date.

---

## Legal Disclaimer

**IMPORTANT - READ THIS DISCLAIMER CAREFULLY**

This is an AI-generated legal analysis and does **NOT constitute legal advice** within the meaning of the Dutch Advocates Act (Advocatenwet). The information in this analysis:

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments. Tax rates and thresholds are subject to annual adjustment.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by the Netherlands AI Lawyer System - an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2024/2025 - verify current rates with the Belastingdienst*
