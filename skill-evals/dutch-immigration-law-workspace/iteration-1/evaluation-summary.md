# Evaluation Summary: dutch-immigration-law (Iteration 1)

## Overall Assessment

**Skill Quality**: Strong
**Assertion Pass Rate**: 9/9 (100%)
**Recommendation**: Ready for use with minor improvements suggested

## Test Results

| Test | Prompt Summary | Assertions Passed | Overall |
|------|---------------|-------------------|---------|
| Eval 1 | Brazilian kennismigrant hire - full process + salary | 5/5 | PASS |
| Eval 2 | Japanese partner family reunification - income + timeline | 4/4 | PASS |

## Quality Assessment

### Accuracy

The skill produces responses with high factual accuracy. Key observations:

- **Salary thresholds**: Correctly cited with 2025 indexed amounts and the distinction between age 30+ and under-30 categories. The exclusion of holiday allowance (8%) and variable components is accurately noted.
- **MVV procedure**: Correctly identifies that Brazil requires MVV while Japan is MVV-exempt, and adjusts the procedural guidance accordingly. The TEV combined procedure (Art. 2a Vw 2000) is properly explained.
- **Legal references**: Statutory articles are accurate (Art. 3.30a Vb, Art. 2c Vw, Art. 3.22 Vb, Art. 17 Vw). The reference material provides a solid foundation.
- **Recognized sponsor**: The erkend referent requirement is consistently emphasized as required by the SKILL.md ethical guardrails.
- **Income requirement**: The family reunification income threshold (100% netto minimumloon, approximately EUR 1,934.40/month) is correctly stated with the three qualifying criteria (independent, sufficient, durable).

### Completeness

Both responses are comprehensive and follow the SKILL.md output format:

- **Eval 1**: Covers the full process from sponsor recognition through arrival, including timeline estimates, document requirements, fees, and rights/obligations. Also addresses the 30% ruling as a related consideration.
- **Eval 2**: Covers income requirements, MVV-exempt status, both application routes (VVB from NL and TEV from Japan), civic integration (distinguishing between abroad exam exemption and in-country obligation), and the path to permanent residence and citizenship. Correctly handles the nuance about Japanese dual nationality restrictions.

### Adherence to Skill Guidelines

- **Output format**: Both responses follow the prescribed format (Immigration Law Analysis header, sections for Requirements, Application Procedure, Rights and Obligations, Duration and Renewal, Path to Permanent Residence).
- **Process steps**: The skill's 7-step process is followed (identify nationality, identify purpose, determine scheme, analyze requirements, outline procedure, flag conditions, append disclaimer).
- **Ethical guardrails**: Disclaimer is appended. No application filing is suggested. Deadlines are emphasized. Recognized sponsor requirement is highlighted.
- **Escalation triggers**: None were triggered (appropriate, as neither scenario involves asylum, deportation, or criminal background issues).

## Strengths

1. **Nationality-aware procedural guidance**: The skill correctly adapts the procedure based on nationality (MVV-required vs. MVV-exempt), which is the most critical branching point in Dutch immigration practice.

2. **Specific, actionable information**: Provides concrete numbers (salary thresholds, fees, timelines) rather than vague generalities. Users can use this to plan and budget.

3. **Comprehensive coverage**: Goes beyond the immediate question to cover related topics (30% ruling, path to permanent residence, civic integration) that users would naturally want to know about.

4. **Proper legal sourcing**: References are specific (Art. 3.30a Vb, Art. 2c Vw 2000, etc.) and verifiable, not vague citations.

5. **Practical process structure**: The step-by-step process with timeline tables makes the information immediately actionable.

## Suggestions for Improvement

### 1. Update Salary Thresholds Annually (HIGH)
The reference material contains 2024 and 2025 salary thresholds. The skill should include a mechanism or note to verify current thresholds, as they change annually on 1 January. For a 2026 evaluation date, the 2025 figures are the latest available in the reference material -- a note about potential 2026 updates would be prudent.

### 2. Add Cost Breakdown Table (MEDIUM)
While individual fees are mentioned throughout, a consolidated cost breakdown table (application fees, sponsor registration, biometrics, legalization of documents, etc.) would help users budget more effectively.

### 3. Expand Family Reunification for Kennismigrant Families (MEDIUM)
Eval 1 mentions that family members can apply for dependent permits but does not detail the process. Since many kennismigrant hires bring families, a brief sub-section on dependent permits (partner, children) with the simultaneous application option would be valuable.

### 4. Add Processing Time Variability Note (LOW)
The skill gives standard processing times (2 weeks for recognized sponsors, 90 days standard). It would be helpful to note that IND backlogs can significantly extend these, particularly in certain periods, and to recommend checking the IND website for current processing times.

### 5. Include Civic Integration for Kennismigrant Partners (LOW)
Eval 1 does not mention that the kennismigrant's partner (if they follow on a dependent permit) will be subject to civic integration requirements. This is a common question that users may not think to ask.

### 6. Reference Material Gap: 2026 Threshold Updates (LOW)
The kennismigrant.md reference contains 2024 and 2025 thresholds. A mechanism for updating these annually (or a note that they are subject to annual indexing) would improve the reference material's longevity.

## Conclusion

The dutch-immigration-law skill performs well across both test scenarios, producing accurate, comprehensive, and well-structured responses. The skill correctly handles the critical nationality-based branching (MVV-required vs. MVV-exempt) and provides actionable procedural guidance with specific numbers and timelines. The reference material (verblijfsvergunningen.md and kennismigrant.md) provides a solid factual foundation. The suggested improvements are refinements rather than corrections -- the skill is ready for production use in its current form.
