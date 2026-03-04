# Effective Search Strategies for Dutch Case Law (Rechtspraak.nl)

## 1. General Principles

### Use Dutch Legal Terminology
Rechtspraak.nl indexes cases in Dutch. Always search using Dutch legal terms, even if the user's question is in English.

| English Concept | Dutch Search Term(s) |
|----------------|---------------------|
| Breach of contract | Tekortkoming, wanprestatie, toerekenbare tekortkoming |
| Damages | Schadevergoeding, schade |
| Unfair dismissal | Onredelijk ontslag, ontbinding arbeidsovereenkomst |
| Force majeure | Overmacht |
| Negligence | Onrechtmatige daad, nalatigheid |
| Good faith | Redelijkheid en billijkheid |
| Non-compete clause | Concurrentiebeding |
| Confidentiality | Geheimhouding, geheimhoudingsbeding |
| Privacy / data protection | Persoonsgegevens, AVG, privacy |
| Corporate governance | Enqueterecht, wanbeleid, jaarrekeningrecht |
| Intellectual property | Auteursrecht, merkenrecht, octrooirecht |
| Unfair terms | Onredelijk bezwarend, algemene voorwaarden |

### Combine Legal Concept with Statutory Reference
The most effective searches combine a legal concept with the relevant BW article:
- `"artikel 6:74 BW" schadevergoeding` (attribution of damages)
- `"artikel 7:681 BW" billijke vergoeding` (unfair dismissal compensation)
- `"artikel 6:233" onredelijk bezwarend` (unfair general terms)

---

## 2. Search Parameters

### By Legal Area (Rechtsgebied)
The Rechtspraak.nl API supports filtering by legal area:
- **Civiel recht** - Civil law
- **Strafrecht** - Criminal law
- **Bestuursrecht** - Administrative law
- **Belastingrecht** - Tax law

Sub-areas include:
- Civiel recht > Verbintenissenrecht (obligations)
- Civiel recht > Arbeidsrecht (employment)
- Civiel recht > Ondernemingsrecht (corporate)
- Civiel recht > Huurrecht (rental)
- Civiel recht > Personen- en familierecht (family)
- Civiel recht > Intellectuele-eigendomsrecht (IP)
- Bestuursrecht > Vreemdelingenrecht (immigration)
- Bestuursrecht > Omgevingsrecht (environmental/planning)
- Bestuursrecht > Socialezekerheidsrecht (social security)

### By Court Level
Filter by court for authoritative precedent:
- Start with **Hoge Raad** for binding interpretation
- Then **Gerechtshof** for appeal-level reasoning
- Then **Rechtbank** for detailed factual analysis and first instance application

### By Date Range
- Use date filtering to find recent developments
- Also search historically for landmark decisions
- Combine: first find the leading Hoge Raad case, then search for recent application

### By Procedure Type
- **Dagvaarding** (summons) - most civil claims
- **Rekest** (petition) - corporate, family, insolvency
- **Kort geding** (summary proceedings) - interim relief
- **Hoger beroep** (appeal)
- **Cassatie** (cassation)

---

## 3. Advanced Search Techniques

### Phrase Search
Use quotes for exact phrases:
- `"redelijkheid en billijkheid"` - exact phrase
- `"6:248 lid 2"` - specific article reference

### Boolean Operators
- `AND` (default): both terms must appear
- `OR`: either term
- `NOT` or `-`: exclude term
- Example: `concurrentiebeding NOT arbeidsovereenkomst` (non-compete outside employment)

### Proximity Search
Find terms near each other:
- `"overmacht" "ontbinding"` - both concepts in same case

### Article Number Search
Search for specific statutory provisions:
- `"art. 6:265 BW"` or `"artikel 6:265"` or `"6:265 BW"`
- Include alternative notations: `"art." OR "artikel"` combined with the number

### Named Doctrines / Landmark Cases
Search by well-known case names (arresten):
- `Kelderluik` (HR 5 november 1965 - duty of care criteria)
- `Haviltex` (HR 13 maart 1981 - contract interpretation)
- `CAO-norm` (HR 17 september 1993 - interpretation of collective agreements)
- `Baris/Riezenkamp` (precontractual liability)
- `Lindenbaum/Cohen` (HR 1919 - tort law foundation)

---

## 4. Landmark Cases Every Search Should Consider

### Contract Law
| Case Name | ECLI | Principle |
|-----------|------|-----------|
| Haviltex | ECLI:NL:HR:1981:AG4158 | Contract interpretation: subjective meaning parties attached to clauses |
| CAO-norm | ECLI:NL:HR:1993:ZC1076 | Objective interpretation for collective/standard terms |
| Lundiform/Mexx | ECLI:NL:HR:2013:BZ5721 | Modern contract interpretation: spectrum between Haviltex and CAO-norm |
| PontMeyer | ECLI:NL:HR:2007:AZ4163 | Entire agreement clauses under Dutch law |

### Tort Law
| Case Name | ECLI | Principle |
|-----------|------|-----------|
| Kelderluik | ECLI:NL:HR:1965:AB7079 | Four criteria for duty of care in negligence |
| Lindenbaum/Cohen | (1919) | Foundation of modern tort law |

### General Terms and Conditions
| Case Name | ECLI | Principle |
|-----------|------|-----------|
| Geurtzen/Kampstaal | ECLI:NL:HR:1999:ZC2977 | Battle of forms |
| Bol.com | Various | Online general terms availability |

---

## 5. Search Workflow

### Step 1: Identify the Issue
- What area of law?
- What specific legal question?
- What statutory provision applies?

### Step 2: Initial Broad Search
- Search using the core Dutch legal concept
- Filter by Hoge Raad first for binding precedent
- Look for recent cases (last 5 years) for current state of law

### Step 3: Narrow Down
- Add statutory article references
- Filter by court level
- Add specific factual elements

### Step 4: Follow Citations
- Check which cases the court cites (especially Hoge Raad references)
- Follow the chain of precedent backward
- Check for subsequent decisions that may have modified the rule

### Step 5: Check Currency
- Verify the statute cited has not been amended since the decision
- Check for later Hoge Raad decisions on the same point
- Look for pending prejudiciele vragen

---

## 6. Publication and Availability Notes

- **Not all decisions are published**: Only a subset of Dutch court decisions are published on Rechtspraak.nl (estimated 5-10% of all decisions)
- **Selection criteria**: Publication is more likely for cases with legal significance, novel points, or public interest
- **Hoge Raad**: Almost all decisions are published
- **Lower courts**: Selective publication; absence of published case law does not mean no cases exist
- **Anonymization**: All published cases are anonymized; natural persons are indicated by initials or [eiser]/[gedaagde]
- **Open Data**: Rechtspraak.nl provides open data API access (data.rechtspraak.nl)
