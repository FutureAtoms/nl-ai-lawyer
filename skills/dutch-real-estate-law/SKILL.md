---
name: dutch-real-estate-law
description: "Real estate transactions, rental law, kadaster, leasehold, and property law under Dutch law. Use this skill whenever the user asks about buying property in the Netherlands, huurrecht, erfpacht, commercial lease, koopovereenkomst, notaris, or Dutch real estate transactions."
---

# Dutch Real Estate Law

## When to Use
- User asks about buying or selling property in the Netherlands
- User asks about residential or commercial rental law (huurrecht)
- User asks about property registration (kadaster) or title transfer
- User asks about leasehold (erfpacht), easements (erfdienstbaarheden), or other limited property rights
- User asks about construction law, building permits, or spatial planning
- User asks about landlord-tenant disputes, rent increases, or eviction
- User asks about real estate transfer tax (overdrachtsbelasting) or notarial requirements

## Process
1. **Identify the property type** - Residential (woonruimte), commercial Art. 7:290 (middenstandsbedrijfsruimte), or other commercial (overige bedrijfsruimte Art. 7:230a)
2. **Determine the legal issue** - Purchase, rental, construction, land use, financing
3. **Apply the correct legal framework** - Property law (BW Boek 5), rental law (BW Boek 7 Titel 4), or specific legislation
4. **Analyze** with attention to:
   a. Mandatory consumer protections (B2C transactions)
   b. Notarial requirements for property transfers
   c. Rental price regulations (especially for residential)
   d. Spatial planning and permit requirements
5. **Provide practical guidance**
6. **Append disclaimer**

## Key Legal Framework
- **BW Boek 3** - Vermogensrecht (Property Law - general)
- **BW Boek 5** - Zakelijke rechten (Rights in Rem):
  - Eigendom (ownership)
  - Erfpacht (leasehold)
  - Opstal (right of superficies)
  - Erfdienstbaarheden (easements)
  - Appartementsrecht (apartment rights / condominium)
- **BW Boek 7, Titel 4** - Huurrecht (Rental Law)
  - Afdeling 1-4: General rental provisions
  - Afdeling 5 (Art. 7:232-282): Woonruimte (residential rental)
  - Afdeling 6 (Art. 7:290-310): Middenstandsbedrijfsruimte (commercial retail/hospitality)
  - Art. 7:230a: Overige bedrijfsruimte (other commercial space)
- **Kadasterwet** - Cadastre Act (land registration)
- **Wet op het notarisambt** - Notarial Act
- **Omgevingswet** (since 2024, replacing Wro, Wabo, etc.) - Environmental and Planning Act
- **Huisvestingswet 2014** - Housing Act
- **Wet goed verhuurderschap** (2023) - Good Landlordship Act
- **Wet doorstroming huurmarkt** - Rental market fluidity
- **Besluit huurprijzen woonruimte** - Rent price decree
- **Woningwaarderingsstelsel (WWS)** - Housing valuation system (points system)

Consult `references/key-case-law.md` for landmark court decisions relevant to this domain.

## Ethical Guardrails
- **Mandatory disclaimer**: Always append disclaimer
- **Notarial requirement**: Emphasize that property transfer REQUIRES a notarial deed and kadaster registration
- **Tenant protection**: Dutch residential rental law is strongly protective of tenants; ensure landlords understand limitations
- **No conveyancing**: Do not perform conveyancing or prepare notarial deeds
- **Tax complexity**: Real estate transactions have significant tax implications (overdrachtsbelasting, btw, inkomstenbelasting); recommend tax advisor
- **Local regulations**: Municipal regulations (huisvestingsverordening, bestemmingsplan/omgevingsplan) vary significantly; recommend local verification

### Disclaimer Language Selection
- Use **Dutch disclaimer** (`assets/disclaimers/disclaimer-nl.md`) when:
  - The query is in Dutch
  - The output document is in Dutch
  - The user's organization config specifies Dutch as primary language
- Use **English disclaimer** (`assets/disclaimers/disclaimer-en.md`) when:
  - The query is in English
  - The output document is in English
  - Default when language is unclear
- Use **both disclaimers** when:
  - The output is bilingual
  - The user requests both languages

## MCP Tools to Use
- `search_legislation` - Look up property and rental legislation
- `get_legislation` - Retrieve specific statutory text
- `search_case_law` - Find real estate case law
- `get_case_law` - Retrieve specific decisions

## Related Skills
- **dutch-tax-law** - For transfer tax (overdrachtsbelasting) and real estate tax implications
- **dutch-administrative-law** - For environmental permits (omgevingsvergunning) and spatial planning

## Output Format
```
## Real Estate Law Analysis

**Property Type**: [Residential/Commercial/Land]
**Transaction Type**: [Purchase/Rental/Leasehold/Other]
**Legal Question**: [Formulated question]

## Applicable Legal Framework
[Relevant legislation]

## Analysis
[Detailed legal analysis]

## Practical Requirements
- Steps, timelines, costs
- Required professionals (notaris, makelaar, taxateur)

## Risks and Protections
[Key legal protections and risks]

## Recommendations
[Actionable next steps]

---
[Disclaimer]
```

## Escalation Triggers
- Property transactions involving disputes or litigation
- Eviction proceedings (ontruiming)
- Construction defects or building disputes (aanneming van werk)
- Complex commercial lease negotiations with significant financial impact
- Property development requiring environmental permits
- Cross-border property ownership or investment structures
- Foreclosure (executie) or mortgage enforcement
- VvE (Vereniging van Eigenaren) disputes in apartment complexes
- Rent tribunal (Huurcommissie) proceedings
- Social housing allocation disputes

## Disclaimer
Append the appropriate disclaimer from `assets/disclaimers/` to every output.
