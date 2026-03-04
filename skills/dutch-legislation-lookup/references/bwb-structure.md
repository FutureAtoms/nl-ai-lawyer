# BWB Identifier Structure and Legislation Database

## What is BWB?
The **Basiswettenbestand (BWB)** is the authoritative database of all Dutch national legislation, maintained by the Dutch government and accessible via wetten.overheid.nl.

---

## BWB Identifier Format

### Structure
```
BWB[TYPE][NUMBER]
```

### Types of BWB Identifiers

| Prefix | Type | Description |
|--------|------|-------------|
| BWBR | Basiswet Rijksoverheid | National legislation (Acts, AMvBs, Ministerial regulations) |
| BWBV | Basiswet Verdragen | Treaties and international agreements |
| BWBN | Basiswet BES-eilanden | Legislation for Caribbean Netherlands (Bonaire, Sint Eustatius, Saba) |

### Examples
| BWB ID | Legislation |
|--------|------------|
| BWBR0005289 | Burgerlijk Wetboek Boek 1 |
| BWBR0003045 | Burgerlijk Wetboek Boek 2 |
| BWBR0005291 | Burgerlijk Wetboek Boek 3 |
| BWBR0005289 | Burgerlijk Wetboek Boek 4 |
| BWBR0005288 | Burgerlijk Wetboek Boek 5 |
| BWBR0005289 | Burgerlijk Wetboek Boek 6 |
| BWBR0005290 | Burgerlijk Wetboek Boek 7 |
| BWBR0005293 | Burgerlijk Wetboek Boek 7A |
| BWBR0005034 | Burgerlijk Wetboek Boek 8 |
| BWBR0002656 | Burgerlijk Wetboek Boek 10 (IPR) |
| BWBR0001854 | Wetboek van Strafrecht |
| BWBR0001827 | Wetboek van Koophandel |
| BWBR0001830 | Wetboek van Burgerlijke Rechtsvordering |
| BWBR0005537 | Algemene wet bestuursrecht |
| BWBR0011823 | Uitvoeringswet AVG |

---

## URL Construction

### Current (consolidated) version:
```
https://wetten.overheid.nl/BWBR0005289/
```

### Specific article:
```
https://wetten.overheid.nl/BWBR0005289/artikel/6:74
```

### Version at specific date (geldend op):
```
https://wetten.overheid.nl/BWBR0005289/2023-01-01
```

### XML/API access:
```
https://wetten.overheid.nl/xml.php?regelingID=BWBR0005289
```

---

## Legislation Database Structure

### Hierarchical Organization
Each piece of legislation in BWB is structured as:
```
Wet (Act)
├── Hoofdstuk (Chapter)
│   ├── Afdeling (Section)
│   │   ├── Paragraaf (Paragraph)
│   │   │   └── Artikel (Article)
│   │   │       ├── Lid (Subsection/Paragraph)
│   │   │       │   └── Onderdeel (Sub-paragraph: a, b, c...)
│   │   │       └── Lid
│   │   └── Artikel
│   └── Afdeling
└── Hoofdstuk
```

### BW Specific Structure
The Burgerlijk Wetboek uses a decimal numbering system:
```
Boek [X] (Book)
└── Titel [X] (Title)
    └── Afdeling [X] (Section)
        └── Artikel [Boek]:[Number] (Article)
```
Example: Art. 6:74 BW = Book 6, Article 74

---

## CVDR - Local Legislation

### What is CVDR?
The **Centrale Voorziening Decentrale Regelgeving** contains regulations from:
- Gemeenten (municipalities)
- Provincies (provinces)
- Waterschappen (water boards)

### Access
```
https://lokaleregelgeving.overheid.nl/
```

### CVDR Identifier Format
```
CVDR[NUMBER]
```
Example: CVDR123456 for a municipal regulation

---

## API Access (Open Data)

### Wetten.overheid.nl API
- RESTful API for searching and retrieving legislation
- Returns XML or JSON
- Supports full-text search, filtering by type, date range
- SRU (Search/Retrieve via URL) protocol

### Search endpoint:
```
https://repository.overheid.nl/sru/wetten?query=...
```

### Key search parameters:
- `dcterms.title` - Title of the legislation
- `dcterms.identifier` - BWB identifier
- `dcterms.type` - Type of regulation
- `overheidwet.gpiCode` - Subject classification

---

## Historical Versions (Tijdreisversies)

- BWB maintains all historical versions of legislation
- Each version has an effective date (inwerkingtreding) and, if applicable, an end date
- Useful for determining which version of the law was in force at the time of a specific event
- Known as "tijdreizen" (time travel) through legislation
- API supports querying by date: `geldigheidsdatum=YYYY-MM-DD`

---

## Publication in Staatsblad / Staatscourant

### Before entering BWB, legislation is published in:
| Publication | Content | Identifier |
|-------------|---------|-----------|
| Staatsblad (Stb.) | Acts of Parliament, AMvBs | Stb. YYYY, NNN |
| Staatscourant (Stcrt.) | Ministerial regulations, announcements | Stcrt. YYYY, NNN |
| Tractatenblad (Trb.) | Treaties | Trb. YYYY, NNN |

### The legislative process:
1. **Wetsvoorstel** (Bill) submitted to Tweede Kamer
2. **Kamerstukken** (Parliamentary documents) published during debate
3. **Aangenomen** by Tweede Kamer, then Eerste Kamer
4. **Bekrachtigd** (Royal Assent)
5. **Gepubliceerd** in Staatsblad
6. **In werking getreden** (Entry into force) - may be immediate or deferred
7. **Opgenomen in BWB** (Incorporated into BWB database)
