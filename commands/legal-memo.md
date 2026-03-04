---
name: legal-memo
description: "Write a structured Dutch legal memorandum with citations and analysis"
arguments:
  - name: question
    description: Legal question to analyze
    required: true
  - name: facts
    description: Relevant facts
    required: false
---

# Legal Memorandum

Produce a formal legal memorandum analyzing a Dutch law question, following the standard IRAC/CREAC methodology adapted for Dutch legal practice.

## Skill and Tools

Use all available MCP tools:
- `legislation_search` -- to find relevant statutes and regulations
- `legislation_fetch` -- to retrieve full text of specific provisions
- `caselaw_search_rechtspraak` -- to find relevant case law
- `caselaw_fetch_uitspraak` -- to retrieve full text of key decisions

## Workflow

### Step 1: Question Analysis

- Parse the `question` to identify the core legal issue(s)
- Identify the area of Dutch law involved
- If `facts` are provided, extract legally relevant facts
- If facts are sparse, note assumptions made and flag that the analysis depends on these assumptions
- Identify sub-questions if the main question has multiple legal dimensions

### Step 2: Research

Conduct thorough research using all available MCP tools:

1. **Statutory Research:**
   - Identify primary legislation (wet)
   - Identify secondary legislation (AMvB, ministeriele regeling)
   - Check EU law sources if applicable
   - Retrieve the current text of relevant provisions

2. **Case Law Research:**
   - Search for Hoge Raad decisions (highest authority in civil/criminal matters)
   - Search for Raad van State decisions (administrative law)
   - Search for relevant lower court decisions
   - Identify the leading cases (standaardarresten) on the issue
   - Note any conflicting decisions or developing trends

3. **Doctrinal Context:**
   - Reference established legal principles and doctrines
   - Note the prevailing academic view if relevant
   - Identify any ongoing debate on the issue

### Step 3: Draft Memorandum

Produce the memorandum in the following format:

```
# LEGAL MEMORANDUM

**Date:** [date]
**Re:** [subject line derived from the question]
**Prepared by:** AI Legal Assistant

---

## I. ISSUE (Rechtsvraag)

[Precise statement of the legal question(s) to be analyzed. If there are sub-questions, number them.]

1. [Primary question]
2. [Sub-question, if any]
3. [Sub-question, if any]

---

## II. BRIEF ANSWER (Kort antwoord)

[Direct, concise answer to each question posed. This should be 1-3 paragraphs that give the reader the bottom line before reading the full analysis.]

---

## III. FACTS (Feiten)

[Statement of the relevant facts as provided or assumed. Clearly distinguish between:
- **Given facts:** facts provided by the user
- **Assumed facts:** facts assumed for the purpose of analysis (marked with [ASSUMED])
]

---

## IV. DISCUSSION (Bespreking)

### A. Legal Framework (Juridisch kader)

[Overview of the applicable legal framework:]
- [Relevant articles of the BW, with full citation]
- [Other applicable legislation]
- [EU law, if applicable]
- [Relevant legal principles]

### B. Analysis of Issue 1 (Analyse vraagstuk 1)

#### 1. Statutory Provisions
[Analysis of the relevant statutory provisions and their application to the facts]

#### 2. Case Law
[Analysis of relevant case law and its application. For each key case:]
- **[Case name / ECLI reference]** ([Court], [date])
  - Facts: [brief relevant facts]
  - Holding: [what the court decided]
  - Application: [how this applies to the present question]

#### 3. Application to Present Facts
[Apply the law to the specific facts to reach a conclusion on this issue]

### C. Analysis of Issue 2 (if applicable)
[Same structure as above]

### D. Counter-Arguments and Risks
[Present potential counter-arguments and legal risks:]
- [Counter-argument 1 and why it may or may not prevail]
- [Counter-argument 2]
- [Risk assessment of each possible outcome]

---

## V. CONCLUSION (Conclusie)

[Clear, definitive conclusion addressing each issue posed:]

1. **Regarding [Issue 1]:** [conclusion with confidence level]
2. **Regarding [Issue 2]:** [conclusion with confidence level]

---

## VI. RECOMMENDATIONS (Aanbevelingen)

[Practical recommendations based on the analysis:]

1. [Recommendation 1 -- specific actionable step]
2. [Recommendation 2]
3. [Recommendation 3]

**Additional steps to consider:**
- [Further research or investigation needed]
- [Protective measures to take]
- [Timeline considerations]

---

## VII. SOURCES (Bronnen)

### Legislation
- [Full citation with article references and links]

### Case Law
- [ECLI number -- Court, date, brief description]

### Other Sources
- [Parliamentary history, policy documents, etc.]
```

### Step 4: Quality Standards

Ensure the memorandum meets these standards:
- **Objectivity:** Present the law as it is, not as the user might want it to be
- **Completeness:** Address all aspects of the question
- **Accuracy:** All citations must be verified against available sources
- **Balance:** Present arguments on both sides where applicable
- **Clarity:** Use clear language; explain Dutch legal terms for non-specialist readers
- **Precision:** Use correct legal terminology in Dutch with translations where helpful
- **Confidence levels:** Where the answer is uncertain, indicate the level of confidence and explain why

### Step 5: Disclaimer

Always append the following disclaimer at the end:

---

**Disclaimer / Juridische kennisgeving**

This legal memorandum is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. This memorandum is for informational and analytical purposes only. No attorney-client relationship is created. The analysis may not be complete and may contain errors. Laws, regulations, and case law are subject to change. You should consult a qualified Dutch advocaat before making legal decisions based on this memorandum. The opinions expressed are AI-generated and do not represent the views of any law firm or legal professional.

*Dit juridisch memorandum is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Dit memorandum is uitsluitend bedoeld ter informatie en analyse. U dient een gekwalificeerde Nederlandse advocaat te raadplegen voordat u juridische beslissingen neemt op basis van dit memorandum.*
