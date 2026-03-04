# Evaluation Summary: dutch-tax-law (Iteration 1)

## Overall Results

| Test | Assertions Passed | Total Assertions | Score |
|------|-------------------|------------------|-------|
| Test 1 (Fiscale eenheid / EUR 2M BV) | 5 | 5 | 100% |
| Test 2 (30% ruling / US citizen) | 5 | 5 | 100% |
| **Total** | **10** | **10** | **100%** |

## Quality Assessment

### Strengths

1. **Precise statutory citations**: Both responses cite the exact Wet VPB articles (Art. 15 for fiscal unity, Art. 15a-15aj for detailed rules) and related legislation. The vennootschapsbelasting.md reference is well-utilized, providing the foundation for the detailed analysis.

2. **Quantitative analysis**: Test 1 provides concrete tax calculations with current rates (19% on first EUR 200,000, 25.8% above), including a comparison showing the fiscal unity may actually lose a rate bracket. This level of quantitative detail is highly valuable for the user.

3. **Nuanced risk assessment**: Test 1 does not simply advocate for the fiscal unity but presents a balanced analysis identifying the potential disadvantage of losing one EUR 200,000 bracket and the significant joint and several liability risk. This demonstrates analytical depth.

4. **Cross-border sophistication**: Test 2 demonstrates exceptional cross-border tax knowledge, correctly identifying the interaction between the Dutch 30% ruling and US worldwide taxation (FEIE vs. FTC trade-off), FBAR/FATCA obligations, the Dutch-US tax treaty with the saving clause, and the Totalization Agreement for social security.

5. **Practical warnings**: The warning that the 30% ruling reduces available Dutch tax credits for US purposes (potentially increasing net US tax) is a critical insight that many basic tax analyses miss.

### Accuracy

- **Legal citations are correct**: Wet VPB Art. 15 for fiscal unity, Art. 15ae for loss restrictions, Art. 15ai for anti-abuse, Art. 15b for earnings stripping; Wet LB Art. 31a lid 2 sub e for the 30% ruling
- **Tax rates are current**: 19%/25.8% VPB rates, EUR 200,000 bracket threshold, 30% ruling salary thresholds cited correctly for 2024
- **Treaty reference is accurate**: Dutch-US Tax Treaty (1992, amended 2004 Protocol) with correct article references
- **Duration change is correct**: 5-year maximum (reduced from 8 years), with note about 2024 effective date
- **Minor note**: The response mentions proposals to reduce the 30% to 27% and lower levels, which reflects political discussion as of late 2024/2025. This is appropriately flagged as potentially changing.

### Completeness

- **Test 1**: Comprehensive coverage of requirements, advantages, risks (joint liability, entry/exit consequences, earnings stripping, cross-border limitations), anti-avoidance provisions, and compliance obligations. The cost-benefit analysis is particularly strong.
- **Test 2**: Thorough treatment of the 30% ruling mechanics, conditions, duration, partial non-resident status, and the full spectrum of US tax obligations (filing, FEIE/FTC, FBAR, FATCA, social security). The cross-border analysis is outstanding.

## Suggestions for Improvement

### Skill-Level Improvements

1. **Add a 30% ruling reference document**: The current references (vennootschapsbelasting.md, btw-omzetbelasting.md) do not include 30% ruling details. The vennootschapsbelasting.md briefly mentions it but notes "See immigration law skill for details." Adding a dedicated loonbelasting/30%-regeling reference would ensure consistent and accurate responses on this frequently asked topic.

2. **Add international tax reference material**: The skill's reference materials focus on domestic VPB and BTW. A reference covering Dutch tax treaty provisions, the 30% ruling, and common cross-border scenarios (US citizens, UK expats, etc.) would be valuable.

3. **Rate version control**: The skill's ethical guardrails correctly note that rates change frequently. However, the reference materials cite "current as of 2024" rates. Consider implementing a versioning system or date stamp in references so the system always flags the vintage of cited rates.

4. **Anti-avoidance depth**: The vennootschapsbelasting.md reference covers Art. 10a, 10b, and 15b well but could include more detail on the CFC rules (Art. 15c-15e) and ATAD implementation specifics.

5. **Add income tax (IB) reference**: The skill lists Wet IB 2001 in its framework but has no reference document for it. Adding a reference covering Box 1/2/3 basics, the eigenwoningregeling, and the interaction with the 30% ruling's partial non-resident status would fill a gap.

### Response-Level Improvements

1. **Include a summary table**: A concise pros/cons table for the fiscal unity decision would improve readability for Test 1.
2. **Add filing deadlines**: Test 1 could specify the deadline for filing the fiscal unity request with the Belastingdienst.
3. **State tax reference**: Test 2 mentions potential state tax obligations but could elaborate on which US states may still impose tax obligations on expats.
4. **Cost estimate**: Test 2 could note the typical cost of a cross-border tax advisor to set expectations.
