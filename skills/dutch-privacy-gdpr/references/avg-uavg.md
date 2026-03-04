# Dutch GDPR Implementation: AVG and UAVG

## AVG (Algemene Verordening Gegevensbescherming)
The AVG is the Dutch name for the GDPR (Regulation (EU) 2016/679). As an EU Regulation, it is directly applicable in the Netherlands since 25 May 2018.

## UAVG (Uitvoeringswet AVG)
The Uitvoeringswet Algemene Verordening Gegevensbescherming supplements the AVG with Dutch-specific implementation choices.

**BWB identifier**: BWBR0040940
**Entry into force**: 25 May 2018

---

## Key UAVG Provisions

### Chapter 1: General Provisions
- **Art. 1**: Definitions (aligning with AVG Art. 4)
- **Art. 2**: Establishes Autoriteit Persoonsgegevens (AP) as the supervisory authority

### Chapter 2: Legal Bases and Specific Processing Situations

#### Processing of Special Categories (Art. 9 AVG exemptions in UAVG)
- **Art. 22 UAVG**: Processing of biometric data for unique identification only with explicit consent or if necessary for authentication/security
- **Art. 23 UAVG**: Processing of genetic data only for specific purposes (health, scientific research, legal proceedings)
- **Art. 24 UAVG**: Processing of health data permitted for:
  - Treatment by healthcare professionals
  - Insurance administration
  - Occupational health (Arbodienst)
  - Scientific/statistical research with appropriate safeguards
- **Art. 25 UAVG**: Processing of data regarding political opinions by political parties for ordinary activities
- **Art. 26 UAVG**: Processing of data regarding religious/philosophical beliefs by institutions with religious/philosophical purpose
- **Art. 27 UAVG**: Processing of trade union membership data by trade unions
- **Art. 28 UAVG**: General exemption for processing special categories if:
  - Necessary for legal proceedings
  - Necessary for scientific/historical research or statistics
  - With appropriate safeguards

#### Criminal Data (Art. 10 AVG implementation)
- **Art. 31-33 UAVG**: Processing of criminal conviction data
  - Only by or under control of official authority, OR
  - If necessary for purposes specified in Art. 32-33 UAVG
  - Includes: employers may process criminal data if necessary for the function (e.g., VOG requirement)

#### National Identification Number (BSN)
- **Art. 46 UAVG**: Processing of BSN (Burgerservicenummer) only if required by law or for purposes specified by law
- General prohibition on using BSN as a general identifier in private sector

### Chapter 3: Rights of Data Subjects (Dutch specific)
- **Art. 41 UAVG**: Exemptions from right of access for certain processing (e.g., by intelligence services, for journalistic purposes)
- **Art. 42-43 UAVG**: Restrictions on data subject rights for scientific/historical research and statistics

### Chapter 4: Specific Processing Situations
- **Art. 43-44 UAVG**: Journalistic exemption (ontheffing) - many AVG provisions do not apply to journalistic, academic, artistic, or literary expression
- **Art. 45 UAVG**: Processing for archiving purposes in the public interest

### Chapter 5: Autoriteit Persoonsgegevens
- **Art. 6-17 UAVG**: Organization, powers, and procedures of the AP
- AP has power to impose administrative fines up to the AVG maximum (EUR 20 million or 4% annual worldwide turnover)

---

## Legal Bases under Art. 6 AVG (with Dutch Context)

### Art. 6(1)(a) - Consent (Toestemming)
- Must be freely given, specific, informed, and unambiguous
- Dutch context: Cookie consent (Art. 11.7a Tw), marketing consent
- Not suitable for employer-employee relationships (due to power imbalance - AP guidance)

### Art. 6(1)(b) - Contract Performance (Uitvoering overeenkomst)
- Processing necessary for performing a contract with the data subject
- Dutch context: Processing customer data for service delivery

### Art. 6(1)(c) - Legal Obligation (Wettelijke verplichting)
- Processing necessary to comply with Dutch or EU law
- Dutch examples: Tax obligations (AWR), AML (Wwft), employment law (loonadministratie), Handelsregisterwet

### Art. 6(1)(d) - Vital Interests (Vitale belangen)
- Rarely applicable; essentially life-or-death situations
- Dutch context: Emergency medical treatment

### Art. 6(1)(e) - Public Interest / Official Authority (Algemeen belang / openbaar gezag)
- Must have a basis in Dutch or EU law
- Dutch context: Government agencies, publicly funded research, education

### Art. 6(1)(f) - Legitimate Interest (Gerechtvaardigd belang)
- NOT available to public authorities in the performance of their tasks
- Requires balancing test: legitimate interest vs. data subject's rights and interests
- AP has published guidance on the legitimate interest test
- Dutch case law: strict interpretation; must document the balancing test

---

## Key Compliance Requirements

### Records of Processing (Art. 30 AVG)
- Required for organizations with 250+ employees
- Also required for smaller organizations if processing:
  - Is not occasional, OR
  - Includes special categories/criminal data, OR
  - Is likely to result in risk to rights and freedoms
- In practice: virtually all organizations need to maintain records

### Data Protection Officer (Functionaris Gegevensbescherming - FG) (Art. 37 AVG)
Mandatory appointment when:
- Processing by public authority or body
- Core activities consist of systematic monitoring on a large scale
- Core activities consist of large-scale processing of special categories or criminal data
- AP maintains a register of appointed DPOs

### Data Breach Notification (Art. 33-34 AVG)
- **To AP**: Within 72 hours of becoming aware (meldplicht datalekken)
- **To data subjects**: Without undue delay if likely high risk
- AP has published guidelines on assessing severity and notification obligations
- AP maintains a data breach register

### DPIA (Gegevensbeschermingseffectbeoordeling) (Art. 35 AVG)
- Required when processing is likely to result in high risk to rights and freedoms
- AP has published a list of processing operations requiring DPIA (Art. 35(4) list)
- See dpia-template.md for template

### International Transfers (Chapter V AVG)
- Adequate countries: EEA, adequacy decisions (currently includes: UK, Japan, South Korea, etc.)
- Standard Contractual Clauses (SCCs): new version adopted June 2021
- Binding Corporate Rules (BCRs)
- Post-Schrems II: Transfer Impact Assessment (TIA) required for transfers to countries without adequacy
- US: EU-US Data Privacy Framework (DPF) adequacy decision July 2023
