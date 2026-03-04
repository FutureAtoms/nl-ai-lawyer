# Key Case Law - Dutch Privacy / GDPR (AVG)

> This file contains landmark enforcement decisions, CJEU rulings, and Dutch court
> decisions on data protection and privacy law under the AVG (Algemene Verordening
> Gegevensbescherming, the Dutch implementation of the GDPR), the UAVG, and the
> Telecommunicatiewet.
> All ECLI numbers should be verified against [Rechtspraak.nl](https://uitspraken.rechtspraak.nl).
> AP decisions are available at [autoriteitpersoonsgegevens.nl](https://www.autoriteitpersoonsgegevens.nl).

---

## 1. Autoriteit Persoonsgegevens (AP) Enforcement Decisions

### Uber - EUR 290 Million Fine (2024)

- **Authority:** Autoriteit Persoonsgegevens
- **Date:** August 2024
- **Respondent:** Uber Technologies Inc. / Uber B.V.
- **Fine:** EUR 290,000,000
- **Key Legal Principle:** Uber transferred personal data of European drivers to
  the United States without an adequate transfer mechanism after the Schrems II
  ruling invalidated the EU-US Privacy Shield. The data transfers included sensitive
  information (identity documents, location data, photos, payment data, criminal
  records). The AP found violations of Art. 44 GDPR (general principle for transfers)
  and Chapter V GDPR.
- **Relevance:** The largest fine issued by the AP to date. Demonstrates the severity
  of enforcement for international data transfers without adequate safeguards.
  Companies must implement Standard Contractual Clauses (SCCs), Binding Corporate
  Rules (BCRs), or rely on an adequacy decision (such as the EU-US Data Privacy
  Framework, adopted July 2023) for transatlantic transfers.

### TikTok - EUR 750,000 Fine (2021)

- **Authority:** Autoriteit Persoonsgegevens
- **Date:** 2021
- **Respondent:** TikTok (ByteDance)
- **Fine:** EUR 750,000
- **Key Legal Principle:** TikTok failed to provide its privacy policy in Dutch
  for Dutch users, including minor users. This violated the transparency obligations
  under Art. 12 and Art. 13 GDPR, which require that privacy information be provided
  in a clear, plain, and accessible manner, in the language of the data subject
  where reasonably expected.
- **Relevance:** Emphasizes the importance of linguistic accessibility in privacy
  communications, especially when processing data of minors. The relatively modest
  fine reflected the limited scope and period of the violation.

### DPG Media - EUR 525,000 Fine (2022)

- **Authority:** Autoriteit Persoonsgegevens
- **Date:** 2022
- **Respondent:** DPG Media B.V. (publisher of AD, Volkskrant, Trouw, etc.)
- **Fine:** EUR 525,000
- **Key Legal Principle:** DPG Media's cookie consent mechanism did not meet the
  requirements of freely given, specific, informed, and unambiguous consent
  (Art. 4(11) and Art. 7 GDPR, in conjunction with Art. 11.7a Telecommunicatiewet).
  The "cookie wall" that denied access to content without consent was found to
  impair the freedom of consent.
- **Relevance:** Landmark decision on cookie walls in the Netherlands. Establishes
  that conditioning access to a service on acceptance of non-essential cookies
  may not constitute valid consent. Organizations must offer a genuine choice.

### Other Notable AP Fines

| Year | Respondent | Fine | Violation |
|------|-----------|------|-----------|
| 2024 | Uber | EUR 290M | International transfers |
| 2023 | Clearview AI | EUR 30.5M | Biometric data processing without basis |
| 2022 | DPG Media | EUR 525K | Cookie consent |
| 2021 | TikTok | EUR 750K | Transparency for minors |
| 2020 | OLVG Hospital | EUR 440K | Insufficient access controls on patient records |
| 2019 | Haga Hospital | EUR 460K | Insufficient access controls on patient records |
| 2019 | Dutch Tax Authority | Formal finding | Discriminatory processing (SyRI system) |

---

## 2. CJEU Landmark Decisions

### CJEU 16 July 2020, C-311/18 (Schrems II / Data Protection Commissioner v. Facebook Ireland)

- **Court:** Court of Justice of the European Union (Grand Chamber)
- **Date:** 16 July 2020
- **Parties:** Data Protection Commissioner v. Facebook Ireland Ltd, Maximillian Schrems
- **Key Legal Principle:** The EU-US Privacy Shield adequacy decision (Decision
  2016/1250) is invalid because US surveillance laws do not ensure an adequate
  level of protection for EU personal data. Standard Contractual Clauses (SCCs)
  remain valid in principle, but data exporters must conduct a *Transfer Impact
  Assessment* (TIA) to verify that the laws of the recipient country do not
  undermine the protections guaranteed by the SCCs. Supplementary measures may
  be required.
- **Relevance:** Foundational for all international data transfers from the EU/EEA.
  Since July 2023, the EU-US Data Privacy Framework (DPF) provides a new adequacy
  basis for transfers to certified US organizations, but Schrems II principles
  remain applicable for transfers to other third countries and non-DPF-certified
  US entities.

### CJEU 13 May 2014, C-131/12 (Google Spain / AEPD v. Mario Costeja Gonzalez)

- **Court:** Court of Justice of the European Union (Grand Chamber)
- **Date:** 13 May 2014
- **Parties:** Google Spain SL, Google Inc. v. Agencia Espanola de Proteccion de Datos, Mario Costeja Gonzalez
- **Key Legal Principle:** Established the *right to be forgotten* (*recht op
  vergetelheid*). An internet search engine operator is a data controller and must,
  upon request, remove links to web pages containing personal data from search
  results if the information is inadequate, irrelevant, no longer relevant, or
  excessive in relation to the purposes of the processing. This right must be
  balanced against the public interest in access to information.
- **Relevance:** The right to be forgotten is now codified in Art. 17 GDPR. In the
  Netherlands, individuals can exercise this right against search engines and, in
  certain circumstances, against the original publisher. The AP handles complaints
  regarding refusal of erasure requests.

### CJEU 1 October 2019, C-673/17 (Planet49)

- **Court:** Court of Justice of the European Union
- **Date:** 1 October 2019
- **Parties:** Bundesverband der Verbraucherzentralen v. Planet49 GmbH
- **Key Legal Principle:** Consent for the placing of cookies must be given by a
  clear affirmative act (*active consent*). Pre-ticked checkboxes do not constitute
  valid consent. The information provided must include the duration of cookies and
  whether third parties have access to the cookies.
- **Relevance:** Directly applicable to cookie consent mechanisms in the Netherlands
  under Art. 11.7a Telecommunicatiewet and the GDPR consent requirements. Pre-ticked
  cookie consent boxes are unlawful.

### CJEU 4 July 2023, C-252/21 (Meta Platforms / Bundeskartellamt)

- **Court:** Court of Justice of the European Union
- **Date:** 4 July 2023
- **Parties:** Meta Platforms Inc. v. Bundeskartellamt
- **Key Legal Principle:** Competition authorities may assess GDPR compliance as
  part of their abuse of dominance analysis. A dominant company's terms of service
  that require broad data processing without genuine consent may constitute an
  abuse of market position. The legitimate interest basis (Art. 6(1)(f) GDPR)
  requires strict necessity; personalized advertising is generally not a legitimate
  interest for a dominant platform.
- **Relevance:** Intersection of competition law and data protection. Relevant for
  large platform operators in the Netherlands, particularly in conjunction with
  the Digital Markets Act (DMA).

---

## 3. Dutch Court Decisions on Privacy

### Rb. Den Haag 5 February 2020, ECLI:NL:RBDHA:2020:865 (SyRI)

- **Court:** Rechtbank Den Haag
- **Date:** 5 February 2020
- **Parties:** NJCM and others v. Dutch State
- **Key Legal Principle:** The System Risk Indication (SyRI) legislation, which
  allowed government agencies to share and analyze personal data for fraud detection,
  was found to violate Art. 8 ECHR (right to privacy). The system lacked
  transparency, proportionality, and adequate safeguards against discrimination
  and profiling.
- **Relevance:** Landmark decision on government data analytics and profiling.
  Directly relevant to algorithmic decision-making, risk scoring, and AI systems
  used by Dutch government agencies. Sets a high standard for transparency and
  proportionality in automated data processing.

### HR 24 February 2017, ECLI:NL:HR:2017:286

- **Court:** Hoge Raad der Nederlanden
- **Date:** 24 February 2017
- **Key Legal Principle:** The right of access (now Art. 15 GDPR) includes the right
  to obtain a copy of personal data being processed. The data controller must
  provide the information in an intelligible form and within a reasonable time.
- **Relevance:** Affirms the broad scope of the data subject's right of access
  under Dutch law, consistent with the GDPR's Art. 15 requirements.

---

## 4. AP Enforcement Priorities and Statistics

### AP Priority Areas (2024-2025)

The AP has identified the following enforcement priorities:
1. **Data trading and profiling** - targeting data brokers and online tracking
2. **Digital government** - monitoring government data sharing and algorithmic decisions
3. **AI and automated decision-making** - focus on high-risk AI systems
4. **Children's data** - enforcement against platforms processing minors' data
5. **Health data** - hospital access controls and health app compliance

### Enforcement Statistics

| Year | Investigations Opened | Fines Imposed | Total Fine Amount |
|------|----------------------|---------------|-------------------|
| 2024 | ~50 | Multiple | > EUR 300M (incl. Uber) |
| 2023 | ~45 | Multiple | > EUR 35M |
| 2022 | ~40 | Multiple | > EUR 3.7M |
| 2021 | ~35 | Multiple | > EUR 2.75M |

*Note: Statistics are approximate. Consult the AP annual report (Jaarverslag) for
official figures.*

---

## 5. Data Protection by Design and Records of Processing

### Art. 25 AVG - Data Protection by Design and by Default

- **Requirement:** The controller must implement appropriate technical and
  organizational measures designed to implement data protection principles
  (such as data minimization) and integrate necessary safeguards into the
  processing, both at the time of determining the means and at the time of
  processing itself.
- **Key AP Guidance:** The AP has published guidelines emphasizing that data
  protection by design is not merely a technical requirement but a holistic
  approach that must be embedded in organizational processes, IT development
  methodologies, and vendor management.
- **Case Reference:** The OLVG Hospital fine (2020, EUR 440K) was partly based
  on failure to implement adequate technical measures (access controls) by design.

### Art. 30 AVG - Records of Processing Activities (Verwerkingsregister)

- **Requirement:** Controllers and processors with more than 250 employees, or
  those processing data that is likely to result in a risk to the rights and
  freedoms of data subjects, or processing on a non-incidental basis, or
  processing special categories of data, must maintain a record of processing
  activities.
- **Required Contents (Controller - Art. 30(1)):** Name and contact details of
  the controller, purposes of processing, categories of data subjects and
  personal data, categories of recipients, transfers to third countries,
  retention periods, and description of technical and organizational security
  measures.
- **AP Enforcement:** The AP has increasingly checked for the existence and
  quality of verwerkingsregisters during investigations.

---

## 6. Telecommunicatiewet - Cookie Requirements

### Art. 11.7a Telecommunicatiewet (Tw)

- **Requirement:** The storage of or access to information on a user's terminal
  equipment (cookies, tracking pixels, local storage) is only permitted if:
  1. The user has been clearly and fully informed about the purposes; and
  2. The user has given consent, unless the cookies are strictly necessary
     for providing the requested service (*functionele cookies*) or are
     used solely for measuring the reach of the service (*analytische cookies*,
     under certain conditions).
- **Consent Standard:** Must meet the GDPR definition: freely given, specific,
  informed, and unambiguous indication by statement or clear affirmative action.
- **Key Cases:**
  - DPG Media (2022) - cookie wall found non-compliant
  - Planet49 (CJEU, 2019) - pre-ticked boxes insufficient
- **AP Cookie Guidelines:** The AP has published a *Normuitleg cookiebeheer*
  (normative interpretation for cookie management) specifying requirements for
  consent mechanisms, including the requirement for equally prominent accept
  and refuse buttons.

---

## 7. Reference Summary Table

| Decision | Authority | Topic |
|----------|-----------|-------|
| Uber EUR 290M | AP (2024) | International transfers |
| TikTok EUR 750K | AP (2021) | Transparency / language |
| DPG Media EUR 525K | AP (2022) | Cookie consent |
| Schrems II (C-311/18) | CJEU (2020) | International transfers |
| Google Spain (C-131/12) | CJEU (2014) | Right to be forgotten |
| Planet49 (C-673/17) | CJEU (2019) | Cookie consent |
| SyRI | Rb. Den Haag (2020) | Government profiling |

---

## Notes for AI System

- Always check whether international data transfers have an adequate legal basis
  (SCCs, BCRs, adequacy decision, or derogation under Art. 49 GDPR).
- For cookie compliance, verify that consent mechanisms meet the Planet49 and
  DPG Media standards: active opt-in, no pre-ticked boxes, no cookie walls
  blocking access, and equally prominent accept/refuse options.
- The AP is increasingly active in enforcement. Check the AP website for the
  latest decisions and guidance before advising.
- The SyRI decision sets a high bar for governmental data analytics and AI systems.
  Apply the proportionality and transparency principles to any automated
  decision-making system.
- For health data processing, the UAVG (Uitvoeringswet AVG) provides additional
  Dutch-specific rules, particularly regarding the use of BSN numbers in healthcare.
- Art. 25 (data protection by design) and Art. 30 (records of processing) are
  frequently checked during AP investigations and should be proactively addressed.
