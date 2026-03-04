# ECLI Identifier Format and Validation

## What is ECLI?
The **European Case Law Identifier (ECLI)** is a standardized system for identifying court decisions across EU member states. In the Netherlands, ECLI has been mandatory for published case law since 2013.

## Format
```
ECLI:NL:[COURT CODE]:[YEAR]:[IDENTIFIER]
```

### Components:
1. **ECLI** - Fixed prefix
2. **NL** - Country code (Netherlands)
3. **Court Code** - Abbreviation of the issuing court
4. **Year** - Four-digit year of the decision
5. **Identifier** - Unique alphanumeric case identifier

### Example:
```
ECLI:NL:HR:2019:1234
```
= Decision of the Hoge Raad (HR), year 2019, case number 1234

---

## Dutch Court Codes

### Supreme Court
| Code | Court | Full Name |
|------|-------|-----------|
| HR | Hoge Raad | Hoge Raad der Nederlanden |
| PHR | Parket bij de Hoge Raad | Advocate General's opinions (conclusies) |

### Courts of Appeal (Gerechtshoven)
| Code | Court | Location |
|------|-------|----------|
| GHAMS | Gerechtshof Amsterdam | Amsterdam |
| GHARL | Gerechtshof Arnhem-Leeuwarden | Arnhem / Leeuwarden |
| GHDHA | Gerechtshof Den Haag | The Hague |
| GHSHE | Gerechtshof 's-Hertogenbosch | 's-Hertogenbosch |

### District Courts (Rechtbanken)
| Code | Court | Location |
|------|-------|----------|
| RBAMS | Rechtbank Amsterdam | Amsterdam |
| RBDHA | Rechtbank Den Haag | The Hague |
| RBGEL | Rechtbank Gelderland | Arnhem / Zutphen |
| RBLIM | Rechtbank Limburg | Maastricht / Roermond |
| RBMNE | Rechtbank Midden-Nederland | Utrecht / Lelystad |
| RBNHO | Rechtbank Noord-Holland | Haarlem / Alkmaar |
| RBNNE | Rechtbank Noord-Nederland | Groningen / Leeuwarden / Assen |
| RBOBR | Rechtbank Oost-Brabant | 's-Hertogenbosch |
| RBOVE | Rechtbank Overijssel | Zwolle / Almelo |
| RBROT | Rechtbank Rotterdam | Rotterdam |
| RBZWB | Rechtbank Zeeland-West-Brabant | Breda / Middelburg |

### Specialized Administrative Courts
| Code | Court | Full Name |
|------|-------|-----------|
| RVS | Raad van State | Council of State (Afdeling Bestuursrechtspraak) |
| CRVB | Centrale Raad van Beroep | Central Appeals Tribunal (social security/civil servants) |
| CBB | College van Beroep voor het bedrijfsleven | Trade and Industry Appeals Tribunal |

### Other Courts/Tribunals
| Code | Court | Full Name |
|------|-------|-----------|
| RBROT (trade) | Rechtbank Rotterdam | Maritime / transport cases |
| GHDHA (IP) | Gerechtshof Den Haag | Patent cases in appeal |

---

## Validation Rules

1. **Format**: Must match pattern `ECLI:NL:[A-Z]{2,5}:[0-9]{4}:[A-Z0-9]+`
2. **Country code**: Must be `NL` for Dutch cases
3. **Court code**: Must be a recognized Dutch court code from the table above
4. **Year**: Must be a valid 4-digit year (typically 1900-present)
5. **Identifier**: Alphanumeric, typically numeric but can contain letters

### Common Validation Errors:
- Missing `ECLI:` prefix
- Using old LJN identifiers instead of ECLI (LJN was replaced by ECLI in 2013)
- Incorrect court code (e.g., using `RBUT` instead of `RBMNE` for Utrecht)
- Confusing Gerechtshof codes with Rechtbank codes

---

## Legacy: LJN Numbers
Before ECLI, the Netherlands used **LJN (Landelijk Jurisprudentie Nummer)**:
- Format: Two letters + four digits (e.g., `BN1234`)
- Used until June 2013
- Old LJN numbers can be converted: `ECLI:NL:XX:YYYY:LJNCODE`
- Rechtspraak.nl supports LJN lookups and redirects to ECLI

---

## URL Construction
Given an ECLI, the Rechtspraak.nl URL is:
```
https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:HR:2019:1234
```

For the XML/API endpoint:
```
https://data.rechtspraak.nl/uitspraken/content?id=ECLI:NL:HR:2019:1234
```

---

## Citing Dutch Case Law

### Standard citation format:
```
[Court abbreviation] [date] [month] [year], ECLI:[identifier]
```

### Examples:
- HR 13 september 2019, ECLI:NL:HR:2019:1234
- Gerechtshof Amsterdam 15 maart 2022, ECLI:NL:GHAMS:2022:567
- Rb. Den Haag 1 juni 2023, ECLI:NL:RBDHA:2023:8901

### With publication reference:
- HR 13 september 2019, ECLI:NL:HR:2019:1234, NJ 2020/12 (met noot [annotator])
- Additional publication sources: NJ, JOR, JAR, JIN, AB, JB
