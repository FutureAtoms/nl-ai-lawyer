# SPARQL Queries for EUR-Lex

## Overview

EUR-Lex provides a SPARQL endpoint for querying EU legal data in a structured manner.
The endpoint is available at: `https://publications.europa.eu/webapi/rdf/sparql`

The data is modeled using the European Legislation Identifier (ELI) ontology and the
CDM (Common Data Model) of the Publications Office.

## Key Namespaces

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX eli: <http://data.europa.eu/eli/ontology#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
```

## CELEX Number Structure

CELEX numbers uniquely identify documents in EUR-Lex. Format: `[sector][year][type][number]`

| Sector | Description | Example |
|--------|-------------|---------|
| 1 | Treaties | 12016E101 (Art. 101 TFEU) |
| 3 | Legislation | 32016R0679 (GDPR Regulation) |
| 6 | Case law | 62014CJ0362 (Schrems I) |
| 5 | Preparatory acts | 52012PC0011 |
| 0 | Consolidated texts | 02016R0679-20160504 |
| 4 | Complementary legislation | International agreements |
| 8 | National implementation | National transposition measures |

**Type codes in sector 3:**
- R = Regulation (Verordening)
- L = Directive (Richtlijn)
- D = Decision (Besluit)
- F = Decision (CFSP)

## Query Templates

### 1. Search EU Legislation by Subject Matter

Find all EU regulations related to a specific topic (e.g., data protection):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?celex ?title ?date
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/REG> .
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  FILTER(CONTAINS(LCASE(?title), "data protection"))
  FILTER(?date >= "2015-01-01"^^xsd:date)
}
ORDER BY DESC(?date)
LIMIT 20
```

### 2. Retrieve a Specific Act by CELEX Number

Get details of a known act (e.g., GDPR - 32016R0679):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT ?title ?date ?oj_reference ?in_force
WHERE {
  ?act cdm:resource_legal_id_celex "32016R0679" .
  ?act cdm:resource_legal_date_document ?date .
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  OPTIONAL { ?act cdm:resource_legal_published_in_official-journal ?oj_reference }
  OPTIONAL { ?act cdm:resource_legal_in-force ?in_force }
}
```

### 3. Search Directives by Legal Basis

Find all directives adopted under a specific Treaty basis (e.g., Art. 114 TFEU - internal market):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT DISTINCT ?celex ?title ?date
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/DIR> .
  ?act cdm:resource_legal_based_on_treaty_article ?basis .
  FILTER(CONTAINS(STR(?basis), "114"))
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  FILTER(?date >= "2020-01-01"^^xsd:date)
}
ORDER BY DESC(?date)
LIMIT 25
```

### 4. Find CJEU Case Law by Subject

Search for Court of Justice judgments on a specific topic:

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT DISTINCT ?celex ?title ?date ?ecli
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/JUDG> .
  OPTIONAL { ?act cdm:case-law_ecli ?ecli }
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  FILTER(CONTAINS(LCASE(?title), "direct effect"))
}
ORDER BY DESC(?date)
LIMIT 20
```

### 5. Find National Implementation Measures for a Directive

Search for Dutch transposition of a specific directive (sector 8 - national measures):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT DISTINCT ?national_celex ?title ?date
WHERE {
  ?directive cdm:resource_legal_id_celex "32016L0680" .
  ?national_measure cdm:resource_legal_transposes_directive ?directive .
  ?national_measure cdm:resource_legal_id_celex ?national_celex .
  ?national_measure cdm:resource_legal_date_document ?date .
  FILTER(STRSTARTS(?national_celex, "7"))
  ?expr cdm:expression_belongs_to_work ?national_measure .
  ?expr cdm:expression_title ?title .
  FILTER(CONTAINS(LCASE(?national_celex), "nld"))
}
ORDER BY DESC(?date)
LIMIT 10
```

### 6. Search by Document Type and Date Range

Find all EU regulations published in a specific year:

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?celex ?title ?date
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/REG> .
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  FILTER(?date >= "2024-01-01"^^xsd:date && ?date <= "2024-12-31"^^xsd:date)
}
ORDER BY DESC(?date)
LIMIT 50
```

### 7. Find Consolidated Versions of an Act

Retrieve all consolidated versions of a regulation (e.g., GDPR):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT ?consolidated_celex ?consolidation_date
WHERE {
  ?original cdm:resource_legal_id_celex "32016R0679" .
  ?consolidated cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/REG_CONS> .
  ?consolidated cdm:resource_legal_id_celex ?consolidated_celex .
  ?consolidated cdm:resource_legal_date_document ?consolidation_date .
  FILTER(STRSTARTS(?consolidated_celex, "02016R0679"))
}
ORDER BY DESC(?consolidation_date)
```

### 8. Search for Preliminary Rulings from a Specific Member State

Find CJEU preliminary rulings originating from Dutch courts:

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT DISTINCT ?celex ?title ?date ?ecli
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:case-law_originates_in_country <http://publications.europa.eu/resource/authority/country/NLD> .
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/JUDG> .
  OPTIONAL { ?act cdm:case-law_ecli ?ecli }
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
  FILTER(?date >= "2020-01-01"^^xsd:date)
}
ORDER BY DESC(?date)
LIMIT 30
```

### 9. Search by EuroVoc Subject Matter

Find legislation classified under a specific EuroVoc concept (e.g., consumer protection):

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT DISTINCT ?celex ?title ?date
WHERE {
  ?act cdm:resource_legal_id_celex ?celex .
  ?act cdm:resource_legal_date_document ?date .
  ?act cdm:work_is_about ?subject .
  ?subject skos:prefLabel ?subjectLabel .
  FILTER(LANG(?subjectLabel) = "en")
  FILTER(CONTAINS(LCASE(?subjectLabel), "consumer protection"))
  ?act cdm:work_has_resource-type <http://publications.europa.eu/resource/authority/resource-type/DIR> .
  ?expr cdm:expression_belongs_to_work ?act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?title .
}
ORDER BY DESC(?date)
LIMIT 20
```

### 10. Find Amendments to a Specific Act

List all acts that amend a given regulation:

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>

SELECT DISTINCT ?amending_celex ?amending_title ?date
WHERE {
  ?original cdm:resource_legal_id_celex "32016R0679" .
  ?amending_act cdm:resource_legal_amends ?original .
  ?amending_act cdm:resource_legal_id_celex ?amending_celex .
  ?amending_act cdm:resource_legal_date_document ?date .
  ?expr cdm:expression_belongs_to_work ?amending_act .
  ?expr cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> .
  ?expr cdm:expression_title ?amending_title .
}
ORDER BY DESC(?date)
```

## Common CELEX Numbers for Key EU Acts

| Act | CELEX Number | Short Name |
|-----|-------------|------------|
| GDPR | 32016R0679 | General Data Protection Regulation |
| Consumer Rights Directive | 32011L0083 | CRD |
| Services Directive | 32006L0123 | Bolkestein Directive |
| E-Commerce Directive | 32000L0031 | ECD |
| Digital Services Act | 32022R2065 | DSA |
| Digital Markets Act | 32022R1925 | DMA |
| AI Act | 32024R1689 | EU AI Act |
| Sale of Goods Directive | 32019L0771 | SGD |
| Unfair Commercial Practices | 32005L0029 | UCPD |
| Product Liability Directive | 32024L2853 | PLD (revised) |
| Equal Treatment Directive | 32006L0054 | Recast ETD |
| Working Time Directive | 32003L0088 | WTD |
| Free Movement Directive | 32004L0038 | Citizens Rights Directive |
| Blue Card Directive | 32021L1883 | Revised BCD |

## Tips for Effective SPARQL Queries on EUR-Lex

1. **Always specify language** - Use the language filter to get titles in the desired language
   (ENG, NLD, FRA, DEU, etc.)

2. **Use CELEX prefixes** - When you know the sector, filter with STRSTARTS for efficiency:
   - `STRSTARTS(?celex, "3")` for legislation
   - `STRSTARTS(?celex, "6")` for case law
   - `STRSTARTS(?celex, "1")` for treaties

3. **Date filtering** - Always use `xsd:date` type casting for reliable date comparisons

4. **LIMIT results** - The endpoint may time out on large result sets; always use LIMIT

5. **Resource type URIs** - Common resource types:
   - `REG` - Regulation
   - `DIR` - Directive
   - `DEC` - Decision
   - `JUDG` - Judgment
   - `OPIN_AG` - Advocate General's Opinion
   - `REG_CONS` - Consolidated Regulation

6. **OPTIONAL for nullable fields** - Use OPTIONAL for fields that may not be present
   (e.g., ECLI numbers, OJ references)

7. **Case sensitivity** - Use `LCASE()` for case-insensitive string matching

8. **Performance** - Put the most selective triple patterns first in the WHERE clause
   to improve query performance

9. **Testing** - Test queries at the interactive endpoint before embedding in applications:
   `https://publications.europa.eu/webapi/rdf/sparql`

10. **Dutch-specific queries** - For NL national implementation measures, filter on
    country code NLD and sector 7 or 8 CELEX prefixes
