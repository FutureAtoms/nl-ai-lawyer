---
name: kamervragen
description: "Search Dutch parliamentary questions, debates, and legislative history"
arguments:
  - name: query
    description: Search terms for parliamentary documents
    required: true
  - name: period
    description: Time period filter
    required: false
---

# Search Dutch Parliamentary Questions and Debates (Kamervragen)

Search the Dutch parliamentary records for kamervragen (parliamentary questions), moties (motions), wetsvoorstellen (legislative proposals), and other parliamentary documents.

## Skill and Tools

Use MCP tools:
- `opentk` MCP server tools -- to search Tweede Kamer (House of Representatives) and Eerste Kamer (Senate) records
- `legislation_search` -- to find related legislation
- `caselaw_search_rechtspraak` -- to find case law related to parliamentary topics

## Workflow

### Step 1: Query Preparation

- If the query is in English, translate to Dutch for better search results in parliamentary databases
- Identify the type of parliamentary document sought:
  - **Kamervragen** -- written questions by Members of Parliament to ministers
  - **Kamerstukken** -- official parliamentary documents
  - **Moties** -- motions proposed and voted on
  - **Amendementen** -- amendments to legislative proposals
  - **Wetsvoorstellen** -- legislative proposals (initiatiefwetsvoorstel or regeringsvoorstel)
  - **Handelingen** -- verbatim records of plenary debates
  - **Commissieverslagen** -- committee reports
  - **Begrotingen** -- budget documents
  - **Memories van Toelichting** -- explanatory memoranda

### Step 2: Execute Search

Use the `opentk` MCP server to search parliamentary records:

- Apply the `query` search terms
- If `period` is specified, filter by date range:
  - Accept formats like "2023-2024", "last year", "current kabinet", etc.
  - Map to appropriate date ranges
- Search both Tweede Kamer and Eerste Kamer records

### Step 3: Present Results

```
## Parliamentary Search: "[query]"

**Period:** [filter applied or "all available"]
**Results Found:** [count]
**Document Types Found:** [types]

---

### Kamervragen (Parliamentary Questions)

#### 1. [Question Title / Subject]

| Field | Details |
|-------|---------|
| **Document Number** | [Kamerstuk number, e.g., 2023Z12345] |
| **Date Submitted** | [date] |
| **Submitted By** | [MP name(s)] ([Party]) |
| **Addressed To** | [Minister / State Secretary] |
| **Ministry** | [ministry] |
| **Status** | [answered / pending / withdrawn] |
| **Date Answered** | [date if answered] |

**Questions:**
[Summary of the questions asked]

**Government Response (if answered):**
[Summary of the minister's response]

**Link:** [link to full document]

---

### Moties (Motions)

#### 1. [Motion Title / Subject]

| Field | Details |
|-------|---------|
| **Document Number** | [number] |
| **Date** | [date] |
| **Proposed By** | [MP name(s)] ([Party]) |
| **Subject** | [legislative proposal or topic] |
| **Vote Result** | [aangenomen (adopted) / verworpen (rejected) / aangehouden (held)] |
| **Vote Tally** | [voor/tegen if available] |

**Content:**
[Summary of what the motion requests]

---

### Wetsvoorstellen (Legislative Proposals)

#### 1. [Proposal Title]

| Field | Details |
|-------|---------|
| **Kamerstuk Number** | [e.g., 35XXX] |
| **Type** | [regeringsvoorstel / initiatiefwetsvoorstel] |
| **Submitted By** | [government / MP name(s)] |
| **Date Submitted** | [date] |
| **Status** | [in behandeling / aangenomen TK / aangenomen EK / ingetrokken / verworpen] |
| **Lead Ministry** | [ministry] |

**Summary:**
[Brief description of the legislative proposal]

**Key Provisions:**
- [Key provision 1]
- [Key provision 2]

**Parliamentary History:**
- [Key debate dates and outcomes]

---

### Handelingen (Debate Records)

#### 1. [Debate Title / Subject]

| Field | Details |
|-------|---------|
| **Date** | [date] |
| **Chamber** | [Tweede Kamer / Eerste Kamer] |
| **Type** | [plenair debat / commissiedebat / wetgevingsoverleg / etc.] |
| **Minister(s)** | [attending minister(s)] |

**Key Points from Debate:**
- [Key point 1]
- [Key point 2]
- [Key point 3]

**Link:** [link to full Handelingen]
```

### Step 4: Analysis and Context

Provide context for the results:

```
### Analysis

**Political Context:**
[Brief overview of the political context surrounding these parliamentary activities]

**Current Government Position:**
[The government's stated position on this topic based on the parliamentary record]

**Party Positions:**
| Party | Position |
|-------|----------|
| [Party 1] | [brief stance] |
| [Party 2] | [brief stance] |

**Legislative Impact:**
[Whether these parliamentary activities have led to or are expected to lead to legislative changes]

**Related Legislation:**
[Current laws that are relevant to the parliamentary discussion]

**Timeline of Key Events:**
1. [Date] -- [event]
2. [Date] -- [event]
3. [Date] -- [event]
```

### Step 5: Cross-Reference

If relevant:
- Use `legislation_search` to find current legislation related to the parliamentary topic
- Use `caselaw_search_rechtspraak` to find court decisions that may have prompted parliamentary questions
- Note any pending legislative changes (wetswijzigingen) discussed in parliament

### Step 6: Disclaimer

Always append the following disclaimer at the end:

---

**Disclaimer / Juridische kennisgeving**

This parliamentary research is generated by an AI legal assistant and does not constitute legal or political advice. Parliamentary records are public documents. The summaries provided are AI-generated and may not capture all nuances of parliamentary proceedings. For official and complete parliamentary records, consult tweedekamer.nl and eerstekamer.nl. Political analysis is descriptive only and does not represent endorsement of any position. No attorney-client relationship is created by this research.

*Dit parlementair onderzoek is gegenereerd door een AI-juridisch assistent en vormt geen juridisch of politiek advies. Parlementaire stukken zijn openbare documenten. De samenvattingen zijn door AI gegenereerd en geven mogelijk niet alle nuances weer. Raadpleeg voor offici\u00eble en volledige parlementaire stukken tweedekamer.nl en eerstekamer.nl.*
