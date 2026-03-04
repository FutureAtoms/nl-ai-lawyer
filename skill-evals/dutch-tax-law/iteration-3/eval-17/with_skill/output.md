# Tax Law Analysis

**Tax Type**: Vennootschapsbelasting (VPB) - Corporate Income Tax
**Taxpayer**: Dutch BV (resident taxpayer - binnenlandse belastingplichtige) with 100% subsidiary
**Tax Year**: 2024 (rates and rules as of 2024; verify for current year)

---

## Applicable Legal Framework

- **Wet op de vennootschapsbelasting 1969 (Wet VPB)** - Principal statute
  - **Art. 15 Wet VPB**: Fiscale eenheid (fiscal unity) regime
  - **Art. 15b Wet VPB**: Earnings stripping rules (ATAD)
  - **Art. 20 Wet VPB**: Loss carry-forward and carry-back rules
  - **Art. 13 Wet VPB**: Participation exemption (deelnemingsvrijstelling)
  - **Art. 10a Wet VPB**: Anti-base erosion (interest deduction limitation)
- **CJEU 22 February 2018, C-398/16 and C-399/16** (X BV and X NV): EU freedom of establishment constraints on the fiscal unity regime
- **HR 17 december 2004, ECLI:NL:HR:2004:AQ3810**: Requirements for a valid fiscale eenheid
- **HR 22 februari 2008, ECLI:NL:HR:2008:BB6186**: Consequences of involuntary dissolution of a fiscal unity

---

## What Is a Fiscale Eenheid?

Under Art. 15 Wet VPB, a parent company and one or more Dutch-resident subsidiaries can elect to be treated as a **single taxpayer** for Dutch corporate income tax purposes. The parent company files a single consolidated VPB return covering all members of the unity. The Belastingdienst must approve the formation by means of an administrative request.

---

## Requirements for Forming a Fiscale Eenheid (Art. 15 Wet VPB)

To qualify, all of the following conditions must be satisfied:

1. **Minimum ownership threshold**: The parent must hold at least **95%** of the legal and economic ownership (juridisch en economisch eigendom) of the shares in the subsidiary. Since your BV holds 100% of the subsidiary, this condition is met.
2. **Dutch tax residence**: Both the parent BV and the subsidiary must be **Dutch-resident** for VPB purposes (established in the Netherlands, or having a Dutch permanent establishment). Non-resident entities cannot be included.
3. **Same financial year**: Both entities must have the same fiscal year end.
4. **Same profit determination methods**: Both must apply the same accounting and profit determination principles (goed koopmansgebruik).
5. **Formal request**: A joint application must be filed with the Belastingdienst. The unity takes effect from the date specified in the request (which can be the start of the financial year if filed in time).

---

## Tax Rates (2024)

The standard VPB rates applicable to the consolidated fiscal unity are:

| Taxable profit | Rate |
|---------------|------|
| Up to EUR 200,000 | **19%** |
| Above EUR 200,000 | **25.8%** |

Given your EUR 2M profit, the combined taxable base of the fiscal unity would be taxed at **19%** on the first EUR 200,000 and **25.8%** on the remaining EUR 1,800,000.

*Note: Tax rates are subject to annual adjustment. These are 2024 rates; always verify current year rates with the Belastingdienst or a tax advisor.*

---

## Advantages of a Fiscale Eenheid

### 1. Consolidation of Profits and Losses (Verliesverrekening)
The most significant advantage is that profits and losses of group companies are automatically offset against each other. If the parent BV has profit of EUR 2M and the subsidiary has a loss, these are netted within the fiscal unity, reducing the overall VPB liability.

Under the standard loss compensation rules (Art. 20 Wet VPB):
- Losses can be fully offset against the first EUR 1 million of taxable profit.
- Above EUR 1 million, only 50% of the excess can be offset.
- Within a fiscal unity, pre-existing losses of each entity remain subject to these limitations, but post-unity losses are freely pooled.

### 2. Tax-Neutral Intercompany Transactions (Interne Transacties)
Within a fiscale eenheid, **intercompany transactions between members are ignored for VPB purposes** (they are treated as internal transactions within a single taxpayer). This means:
- Asset transfers between parent and subsidiary do not trigger immediate VPB recognition of gains or losses.
- Intercompany loans do not give rise to interest income/deduction at the group level.
- Services rendered between group members do not generate taxable profit or deductible expenses within the unity.
- This eliminates the administrative burden of managing arm's length transfer pricing between the parent and subsidiary.

### 3. Single VPB Return
The parent files one consolidated VPB return on behalf of all members of the fiscal unity. This simplifies compliance, reduces administrative costs, and eliminates the need for separate VPB filings for each subsidiary.

### 4. Intercompany Asset Transfers Without Immediate Tax Consequences
Asset transfers between fiscal unity members can be done without triggering immediate VPB on gains, enabling group reorganizations and restructurings without a tax charge at the time of transfer (though exit charges apply if the asset leaves the unity later).

---

## Risks and Limitations

### 1. Joint and Several Liability (Hoofdelijke Aansprakelijkheid)
This is the most significant risk of a fiscal unity. Under the rules governing the regime, **all members of the fiscal unity are jointly and severally liable for the VPB debt of the entire group**. This means:
- If the fiscal unity collectively has a VPB debt that the parent cannot pay, the Belastingdienst can recover the full amount from the subsidiary.
- Conversely, if the subsidiary causes the group to incur a large VPB liability (e.g., through an unexpected taxable event), the parent is fully liable.
- This joint liability continues for the period during which the unity existed; it does not simply end when the unity is dissolved.
- **Practical implication**: If the subsidiary has financial difficulties or incurs large unexpected profits or losses, the parent is fully exposed.

### 2. Entry and Exit Consequences (Voegings- en Ontvoeging-effecten)
Joining and leaving a fiscal unity can have complex tax consequences:
- **Entry (voeging)**: Latent gains or losses in assets of the joining entity may be subject to special rules.
- **Exit (ontvoeging)**: When a subsidiary leaves the fiscal unity (e.g., through sale of shares), latent gains that were "frozen" during the unity period may crystallize and become taxable. Intercompany transactions that were tax-neutral during the unity may be revisited.
- **Sale of subsidiary**: Selling shares in a subsidiary that is part of a fiscal unity requires careful planning. The exit from the fiscal unity can trigger unforeseen tax charges.

### 3. Anti-Abuse Restrictions (Spoedreparatiemaatregelen)
Following the CJEU ruling in Cases C-398/16 and C-399/16 (X BV and X NV, 22 February 2018), the Dutch legislature introduced emergency repair measures (spoedreparatiemaatregelen) effective 1 January 2018. These measures require a "per-element benadering": certain anti-avoidance provisions (Art. 10a, 10b, Art. 13 lid 9-17, and Art. 15b Wet VPB) must be applied as if no fiscal unity existed. The effect is that:
- Interest deduction limitations under Art. 10a Wet VPB must be tested at the level of each individual entity, not at the consolidated level.
- The benefit of the fiscal unity for interest deduction purposes is partially neutralized.

### 4. Earnings Stripping (Art. 15b Wet VPB - ATAD)
The earnings stripping rule limits net interest deductions to the higher of (a) 20% of fiscal EBITDA, or (b) EUR 1 million. This rule applies **at the level of the fiscal unity as a whole**, which can be either an advantage (pooling of EBITDA) or a disadvantage (if one entity's interest expense is high relative to group EBITDA).

### 5. Loss Utilization Restrictions After Exit
When a subsidiary exits the fiscal unity, pre-existing losses and subsequent losses of that entity may not be freely available to the parent or other group members.

### 6. Cross-Border Fiscal Unity Is Limited
The fiscal unity under Art. 15 Wet VPB is only available to Dutch-resident entities (or entities with Dutch permanent establishments). Following the CJEU case law, some EU cross-border arrangements may be required, but the scope remains limited. Foreign subsidiaries cannot be included.

---

## Tax Calculation (Indicative)

With EUR 2M taxable profit in the fiscal unity:

| Tranche | Amount | Rate | Tax |
|---------|--------|------|-----|
| First EUR 200,000 | EUR 200,000 | 19% | EUR 38,000 |
| Remaining EUR 1,800,000 | EUR 1,800,000 | 25.8% | EUR 464,400 |
| **Total VPB** | **EUR 2,000,000** | | **EUR 502,400** |

If the subsidiary had losses, these would reduce the taxable base (subject to the EUR 1M full offset / 50% above EUR 1M limitation under Art. 20 Wet VPB for pre-unity losses).

---

## Compliance Obligations

1. **Joint application**: File the application for fiscale eenheid with the Belastingdienst before the unity is to take effect (typically by the first day of the financial year).
2. **Single VPB return**: The parent BV files the consolidated VPB return annually.
3. **Documentation**: Maintain records of the intercompany transactions that were disregarded; these become relevant if the unity is dissolved.
4. **Transfer pricing**: Even within a fiscal unity, keep records of intercompany arrangements for post-dissolution purposes.
5. **Monitor subsidiary's financial position**: Given the joint liability, maintain oversight of the subsidiary's financial health.

---

## Anti-Avoidance Considerations

- **Art. 10a Wet VPB**: Interest on related-party debt connected to tainted transactions (e.g., capital contributions, profit distributions within the group) must be analyzed at the entity level (post-spoedreparatie).
- **Fraus legis**: If the fiscal unity is formed primarily for tax purposes without business substance, the Belastingdienst or courts may invoke fraus legis (HR 26 mei 1926 and subsequent case law). In practice, the fiscal unity is a statutory regime that the legislature has sanctioned, so fraus legis risk is low for a straightforward parent-subsidiary arrangement with genuine commercial operations.
- **Exit planning**: Any planned disposal of the subsidiary should be analyzed in advance to understand the exit consequences.

---

## Recommendations

1. **Verify all conditions** with a Dutch tax advisor (belastingadviseur) before filing the application. In particular, confirm that the subsidiary is Dutch-resident and that both entities share the same financial year.
2. **Assess the joint liability risk**: Conduct a financial risk assessment of the subsidiary to understand the maximum VPB exposure you are accepting.
3. **Model the loss consolidation benefit**: If the subsidiary has existing or anticipated losses, model the VPB savings to confirm the commercial case for forming the unity.
4. **Understand exit consequences**: Have a tax advisor analyze the exit charges that would arise if you ever sell the subsidiary or dissolve the unity.
5. **File the application timely**: The unity takes effect from the date specified in the application. To achieve effect from the beginning of the financial year, the application must be filed in time.
6. **Review intercompany arrangements**: Identify existing intercompany transactions between parent and subsidiary that will become tax-neutral once the unity is in place, and those that may need to be revisited under the spoedreparatie rules.
7. **Specialist advice for complex situations**: If the subsidiary has international operations, third-party financing, or significant asset transfers planned, specialist tax advice is essential before proceeding.

---

## Legal Disclaimer

**IMPORTANT - READ THIS DISCLAIMER CAREFULLY**

This is an AI-generated legal analysis and does **NOT constitute legal advice** within the meaning of the Dutch Advocates Act (Advocatenwet). The information in this analysis:

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) or tax advisor (belastingadviseur).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a tax advisor.** Dutch tax law is highly fact-specific. For tax planning, compliance, and dispute matters, you must consult a qualified belastingadviseur (tax advisor) and/or advocaat registered in the Netherlands.

4. **Tax rates and thresholds change annually.** The rates and figures cited in this analysis reflect 2024 rules. Always verify current year rates with the Belastingdienst or your tax advisor.

5. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal or tax advisor.**

*Generated by the Netherlands AI Lawyer System - an AI tool for legal analysis.*
*Date of analysis: 2026-03-04*
*Legislation verification date: 2024/2025*
