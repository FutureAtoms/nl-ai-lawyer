# Cookie Law and e-Privacy (Telecommunicatiewet Art. 11.7a)

## Legal Framework
- **Art. 11.7a Telecommunicatiewet (Tw)**: Primary Dutch provision implementing the EU e-Privacy Directive (2002/58/EC, as amended by 2009/136/EC) regarding cookies and similar tracking technologies
- **Algemene Verordening Gegevensbescherming (AVG / GDPR)**: Applies to the processing of personal data collected through cookies
- **Autoriteit Persoonsgegevens (AP)**: Supervisory authority for both cookie compliance (Tw) and data protection (AVG)
- The cookie rules in Art. 11.7a Tw are sometimes called the "cookiewet" or "cookiebepaling" in practice

---

## Art. 11.7a Telecommunicatiewet - Core Rule

### The Consent Requirement (Art. 11.7a lid 1 Tw)
- Placing or reading cookies (or similar technologies) on a user's device is **prohibited** unless:
  1. The user has been provided with **clear and comprehensive information** (duidelijke en volledige informatie) about the cookies, including their purpose
  2. The user has given **consent** (toestemming) for the placement and reading of the cookie
- This applies to all tracking technologies: cookies, web beacons, fingerprinting, tracking pixels, local storage, etc.

### Consent Requirements
- Consent must meet the AVG standard (Art. 4 lid 11 and Art. 7 AVG):
  - **Freely given** (vrij): not a condition for access to the service (see cookie wall prohibition below)
  - **Specific** (specifiek): consent per purpose/category, not blanket consent
  - **Informed** (geinformeerd): user must understand what they are consenting to
  - **Unambiguous** (ondubbelzinnig): requires a clear affirmative act (opt-in)
- **Pre-ticked boxes do NOT constitute valid consent** (CJEU Planet49, C-673/17)
- **Scrolling or continued browsing is NOT valid consent** (AP guidance)
- Consent must be **revocable** at any time (Art. 7 lid 3 AVG) and withdrawal must be as easy as giving consent

---

## Cookie Categories and Consent Requirements

### 1. Functional / Technically Necessary Cookies (Functionele Cookies)
- **No consent required** (Art. 11.7a lid 3 sub a Tw)
- These are cookies strictly necessary for the functioning of the service explicitly requested by the user
- Examples:
  - Shopping cart cookies on e-commerce sites
  - Session cookies for login state
  - Language preference cookies
  - Cookie consent preferences storage
  - Load balancing cookies
  - Security cookies (CSRF tokens)
- Information obligation still applies: users must be told these cookies are used

### 2. Analytical Cookies (Analytische Cookies)
- **Conditional exemption** from consent requirement (Art. 11.7a lid 3 sub b Tw + AP guidance)
- First-party analytics with minimal privacy impact may be placed without consent IF:
  - The analytics service has minimal impact on the privacy of the visitor
  - Adequate measures have been taken (e.g., IP anonymization, no data sharing with third parties)
  - Data is not combined with data from other sources
  - The website has a clear privacy/cookie policy
- **Google Analytics**: The AP has stated that standard Google Analytics configuration does NOT meet the exemption requirements because data is shared with Google. A privacy-friendly configuration may qualify, but this is debated. Many organizations use alternatives (Matomo, Plausible, etc.) to avoid consent requirements
- **Self-hosted analytics** (e.g., Matomo self-hosted) generally qualify for the exemption if properly configured

### 3. Tracking / Marketing Cookies (Tracking / Marketing Cookies)
- **Consent always required** (no exemption)
- These are cookies used for:
  - Behavioral advertising (gedragsadvertenties)
  - Cross-site tracking
  - Retargeting / remarketing
  - Social media tracking (Facebook pixel, LinkedIn Insight Tag, etc.)
  - Advertising network cookies
  - Profiling for personalized content or ads
- Third-party cookies are almost always tracking cookies
- Consent must be obtained BEFORE the cookies are placed (not after)

---

## AP Cookie Guidelines and Enforcement

### AP Normuitleg (Interpretation Guidelines)
The Autoriteit Persoonsgegevens has published guidance (normuitleg cookies) covering:

#### Cookie Banner Requirements
- Must be displayed on first visit before non-exempt cookies are placed
- Must clearly explain what types of cookies are used and why
- Must offer a genuine choice (accept / reject / customize)
- The "reject" option must be **equally prominent** as the "accept" option
  - AP has indicated that design patterns making "accept" much more visible than "reject" (dark patterns) violate the informed consent requirement
- Must not use confusing language or manipulative design

#### Granularity of Consent
- Best practice: consent per cookie category (functional, analytical, marketing) at minimum
- More granular consent (per purpose or per cookie) is better but not strictly required
- "Accept all" buttons are permissible only alongside an equally prominent "Reject all" option

#### Cookie Policy / Privacy Statement
- Must describe:
  - Types of cookies used and their purposes
  - Cookie names, providers, and expiration periods
  - Whether cookies are first-party or third-party
  - How to withdraw consent
  - How to delete cookies
- Must be easily accessible (link in footer and in cookie banner)

### Cookie Wall Prohibition
- A **cookie wall** (cookiemuur) is a mechanism that blocks access to a website unless the user consents to all cookies
- The AP has taken the position that cookie walls are **generally not permitted** because consent is not freely given (Art. 7 lid 4 AVG)
- The user must have a genuine alternative: the service must remain accessible without consenting to non-essential cookies
- **Exception**: if there is a real alternative (e.g., paid subscription without tracking), a cookie wall may be permissible, but this is not fully settled in Dutch law
- The AP enforcement approach aligns with the EDPB Guidelines 05/2020 on consent

### AP Enforcement Actions
- The AP has the authority to investigate and impose fines for cookie violations
- Enforcement has been increasing:
  - Formal warnings and investigations of major Dutch websites
  - Focus on improper consent mechanisms (pre-ticked boxes, deceptive design, cookie walls)
  - International cooperation with other EU DPAs on cross-border cookie enforcement
- Fines: under the AVG, fines can reach up to EUR 20 million or 4% of annual worldwide turnover
- Under the Tw: the AP can also impose last onder dwangsom (penalty orders) for non-compliance

---

## Interaction with AVG Consent Requirements

### Dual Legal Basis
- **Placing the cookie**: governed by Art. 11.7a Tw (consent or exemption)
- **Processing the data collected by the cookie**: governed by the AVG (requires a lawful basis under Art. 6 AVG)
- Consent under Art. 11.7a Tw generally satisfies the consent requirement under Art. 6 lid 1 sub a AVG as well
- However, if the data processing has additional purposes beyond what was consented to for the cookie, a separate lawful basis is needed

### Data Subject Rights (AVG)
- Users (data subjects) have rights under the AVG regarding data collected through cookies:
  - **Right of access** (Art. 15 AVG): what data has been collected?
  - **Right to erasure** (Art. 17 AVG): delete my data
  - **Right to withdraw consent** (Art. 7 lid 3 AVG): must be as easy as giving consent
  - **Right to object** (Art. 21 AVG): especially relevant for direct marketing purposes
  - **Right to data portability** (Art. 20 AVG): if processing based on consent

### Data Processing Agreement for Third-Party Cookies
- If third-party cookies are used (e.g., Google Analytics, Facebook Pixel, advertising networks):
  - Determine the role: is the third party a verwerker (processor) or a gezamenlijke verwerkingsverantwoordelijke (joint controller)?
  - If processor: verwerkersovereenkomst required (Art. 28 AVG)
  - If joint controller: arrangement under Art. 26 AVG
  - Third-country transfers: ensure adequate safeguards if data goes outside EU/EEA (SCCs, adequacy decisions)

---

## e-Privacy Regulation (Upcoming EU Legislation)

### Status (as of 2024/2025 - verify for current status)
- The **e-Privacy Regulation** (ePR) has been in legislative development since the European Commission proposal in January 2017
- Intended to replace the e-Privacy Directive (2002/58/EC) and harmonize cookie/electronic communications rules across the EU
- As of 2024: political agreement has not yet been fully reached; timeline for adoption and entry into force is uncertain
- If adopted: will be directly applicable in all EU member states (no national transposition needed)

### Expected Key Changes
- **Directly applicable regulation**: replaces national cookie laws (Art. 11.7a Tw would be superseded)
- **Cookie consent**: likely to maintain consent requirement but may introduce:
  - Browser-based consent settings (consent managed at browser level rather than per website)
  - Standardized consent mechanisms
  - Possible expanded exemptions for certain analytics
- **Metadata protection**: broader protection for electronic communications metadata
- **B2B electronic marketing**: potential clarifications on unsolicited commercial communications
- **Enforcement**: likely enforced by national DPAs (in NL: Autoriteit Persoonsgegevens)

### Impact on Current Compliance
- Organizations should comply with current Art. 11.7a Tw and AP guidance
- When the ePR enters into force, compliance programs will need to be updated
- The ePR may provide a transition period
- Consent mechanisms built now should be designed to be adaptable to future requirements

---

## Practical Compliance Guidance

### Implementation Checklist
1. **Cookie audit**: identify all cookies and similar technologies on your website/app
2. **Categorize**: classify each cookie as functional, analytical, or tracking/marketing
3. **Cookie banner**: implement a consent management platform (CMP) with:
   - Clear information about cookie categories
   - Accept and Reject buttons of equal prominence
   - Granular consent options (per category minimum)
   - No pre-ticked boxes
   - No cookies placed before consent (except functional)
4. **Cookie policy**: draft a comprehensive cookie verklaring with:
   - Cookie names, purposes, providers, and expiration
   - Instructions for consent withdrawal and cookie deletion
   - Link to full privacy statement
5. **Technical implementation**:
   - Ensure non-exempt cookies are blocked until consent is given
   - Record consent (timestamp, version, choices made)
   - Implement consent withdrawal mechanism
   - Regularly scan for new cookies (especially from third-party scripts)
6. **Third-party management**: verwerkersovereenkomsten with all cookie-setting third parties
7. **Regular review**: audit cookie compliance at least annually and after website changes

### Common Mistakes
- Placing tracking cookies before consent is given (scripts loading on page load)
- Using "accept" button prominently while hiding "reject" in small text or settings
- Cookie wall blocking content without providing a genuine alternative
- Not updating cookie policy when new cookies are added
- Relying on implied consent (scrolling, continued browsing)
- Using Google Analytics without proper configuration or consent
- Not providing an easy mechanism to withdraw consent
- Failing to block third-party scripts that set their own cookies

---

*Last updated: 2024/2025 - The e-Privacy Regulation is still under development at EU level. AP enforcement policy and guidance may be updated. Google Analytics compliance requirements have been subject to particular scrutiny across EU member states. Cookie consent management platforms (CMPs) should be regularly updated to reflect current regulatory guidance. Verify AP normuitleg and enforcement decisions for the most current position.*
