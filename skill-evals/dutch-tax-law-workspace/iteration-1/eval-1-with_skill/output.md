# With-Skill Response: Dutch Tax Law - Test 1

**Prompt:** "We're a Dutch BV with EUR 2M profit. We're considering forming a fiscale eenheid with our 100% subsidiary. What are the advantages, risks, and current requirements?"

---

## Tax Law Analysis

**Tax Type**: Vennootschapsbelasting (VPB - Corporate Income Tax)
**Taxpayer**: Dutch BV (parent) and 100% subsidiary
**Tax Year**: Current (rates as of 2024)

## Applicable Legal Framework

- **Wet op de vennootschapsbelasting 1969 (Wet VPB)** - Corporate Income Tax Act
- **Art. 15 Wet VPB** - Fiscale eenheid (fiscal unity) provisions
- **Art. 15a-15aj Wet VPB** - Detailed fiscal unity rules
- **Art. 2 Wet VPB** - Taxpayer definitions
- **Besluit fiscale eenheid 2003** - Decree on fiscal unity
- **ATAD (Anti-Tax Avoidance Directive)** - relevant for earnings stripping rules within fiscal unity

## Analysis

### What is a Fiscale Eenheid?

A fiscale eenheid (fiscal unity) under Art. 15 Wet VPB is a tax consolidation regime whereby a parent company and one or more subsidiaries are treated as a **single taxpayer** for corporate income tax (VPB) purposes. The parent files a single consolidated tax return, and the group's profits and losses are combined.

### Requirements (Art. 15 Wet VPB)

To form a fiscale eenheid, the following conditions must be met:

1. **Ownership**: The parent must hold at least **95% of the shares** (juridisch en economisch eigendom - both legal and economic ownership) in the subsidiary
2. **Dutch tax residency**: Both parent and subsidiary must be resident in the Netherlands for VPB purposes (or have a Dutch permanent establishment -- PE)
3. **Same financial year**: Parent and subsidiary must have the same financial year (boekjaar)
4. **Same profit determination methods**: Both entities must apply the same accounting and profit determination methods for tax purposes
5. **Entity type**: Both parent and subsidiary must be entities subject to VPB (typically BVs, NVs, or cooperatives)
6. **Application**: A formal request must be filed with the Belastingdienst (Dutch Tax Authority)

Since you hold 100% of the subsidiary, the ownership requirement is clearly met.

### Advantages of Forming a Fiscale Eenheid

#### 1. Loss Consolidation (Verliesverrekening)
- Losses of the subsidiary can be offset against profits of the parent (and vice versa) **within the same tax year**
- This is particularly valuable if one entity is profitable and the other is loss-making
- Without a fiscal unity, each entity would carry its own losses forward separately

#### 2. Intercompany Transactions
- Transactions between the parent and subsidiary are **eliminated** for tax purposes (like consolidated accounting)
- No transfer pricing issues on intercompany transactions within the fiscal unity
- Intercompany asset transfers can occur without immediate tax consequences

#### 3. Single Tax Return
- One consolidated VPB return is filed by the parent on behalf of the entire fiscal unity
- Administrative simplification (fewer returns, one point of contact with the Belastingdienst)

#### 4. Tax Rate Optimization
With EUR 2M in combined profit, the tax calculation under current rates would be:

| Bracket | Rate | Tax |
|---------|------|-----|
| First EUR 200,000 | 19% | EUR 38,000 |
| Remaining EUR 1,800,000 | 25.8% | EUR 464,400 |
| **Total** | | **EUR 502,400** |

**Important**: Without a fiscal unity, if both entities are separate taxpayers, each would have its own EUR 200,000 bracket at 19%. This means the 19% bracket is used only **once** in a fiscal unity (one taxpayer), but **twice** if they file separately (two taxpayers). For a group with EUR 2M total profit, separate filing could be more advantageous if the profit is distributed between the entities, as each entity would benefit from the lower 19% rate on its first EUR 200,000.

**Example without fiscal unity** (if profit is split EUR 1M each):
- Entity 1: EUR 200,000 x 19% + EUR 800,000 x 25.8% = EUR 38,000 + EUR 206,400 = EUR 244,400
- Entity 2: EUR 200,000 x 19% + EUR 800,000 x 25.8% = EUR 38,000 + EUR 206,400 = EUR 244,400
- Total: EUR 488,800 (saving of EUR 13,600 vs. fiscal unity)

This means the fiscal unity may **not** provide a rate advantage if both entities are profitable. The primary advantage is loss consolidation and intercompany simplification.

#### 5. Participation Exemption
- Within a fiscal unity, intercompany dividends and capital gains on subsidiary shares are automatically eliminated (no need to apply the participation exemption separately)

### Risks and Limitations

#### 1. Joint and Several Liability (Hoofdelijke aansprakelijkheid)
This is the most significant risk:
- All entities within the fiscal unity are **jointly and severally liable** for the entire group's VPB debt
- If the subsidiary incurs a large tax liability, the parent is liable (and vice versa)
- This liability survives the dissolution of the fiscal unity in certain circumstances
- **Risk mitigation**: Carefully consider financial exposure; include indemnity arrangements between group entities

#### 2. Entry and Exit Consequences (Voeging and Ontvoegingseffecten)
- **Entry (voeging)**: When a subsidiary joins the fiscal unity, certain assets may be subject to step-up or step-down adjustments
- **Exit (ontoeging)**: When a subsidiary leaves the fiscal unity (e.g., upon sale), profits or losses that were deferred within the fiscal unity may crystallize
- **Art. 15ai Wet VPB**: Anti-abuse rule -- if assets are transferred within the fiscal unity and the subsidiary subsequently leaves within 6 years, the gain is added back (sanctiebepaling)
- Loss carry-forward: Pre-unity losses of the subsidiary can generally only be offset against the subsidiary's own profits within the fiscal unity (Art. 15ae Wet VPB)

#### 3. Earnings Stripping Rule (Art. 15b Wet VPB)
- The ATAD-based earnings stripping rule applies at the fiscal unity level
- Net interest expense is deductible only up to the higher of: 20% of fiscal EBITDA or EUR 1 million
- Within a fiscal unity, the EUR 1 million threshold applies only **once** (not per entity)

#### 4. Cross-Border Limitations
- A fiscal unity is generally limited to Dutch-resident entities
- Following CJEU case law (HvJ EU), cross-border fiscal unity has been partially opened but only for definitive losses of EU/EEA subsidiaries under very restricted circumstances
- If the subsidiary has foreign operations, carefully assess the implications

#### 5. Reduced Flexibility
- All entities must have the same financial year and profit determination methods
- Administrative and strategic decisions must consider the entire group's tax position

### Anti-Avoidance Considerations

- **Art. 10a Wet VPB**: Interest deduction limitations on related-party loans connected to tainted transactions apply within the fiscal unity context
- **Art. 15b Wet VPB**: Earnings stripping applies at the fiscal unity level
- **Fraus legis**: The general anti-abuse doctrine can apply if the fiscal unity is formed primarily for tax avoidance purposes without sufficient business substance

## Compliance Obligations

1. **File a request** with the Belastingdienst to form the fiscal unity (using the prescribed form)
2. **Specify the effective date** -- can be retroactive to the start of the current financial year if the request is filed timely
3. **File consolidated VPB return** annually (electronically in XBRL format)
4. **Maintain separate accounts** for each entity within the fiscal unity (commercial/legal accounting remains separate)
5. **Transfer pricing documentation** is not required for intercompany transactions within the fiscal unity (they are ignored for tax), but remains relevant for entities outside the fiscal unity

## Recommendations

1. **Perform a cost-benefit analysis**: Given EUR 2M combined profit with both entities likely profitable, the fiscal unity may not provide a rate advantage (you lose one EUR 200,000 bracket). The primary benefits are loss consolidation and intercompany simplification.
2. **Assess the joint liability risk**: Evaluate the financial health of both entities and the risk exposure from joint and several liability for the group's entire VPB debt.
3. **Consider future plans**: If you plan to sell the subsidiary, forming (and later dissolving) a fiscal unity triggers complex entry and exit consequences. Avoid forming a fiscal unity shortly before a planned divestment.
4. **Consult a belastingadviseur (tax advisor)**: The fiscal unity decision has significant long-term tax implications. A professional tax advisor can model the financial impact and advise on optimal structuring.
5. **Document the business rationale**: Ensure there is a clear business purpose for forming the fiscal unity beyond tax optimization.

---

**Disclaimer:** This information is provided for general informational purposes only and does not constitute tax advice. Dutch corporate tax law is complex and highly fact-specific. Tax rates, thresholds, and rules change frequently. The analysis above is based on currently applicable rates and provisions, which may be amended. You should consult a qualified Dutch tax advisor (belastingadviseur) or tax lawyer (fiscalist) for advice tailored to your specific situation before making any decisions regarding the formation of a fiscal unity.
