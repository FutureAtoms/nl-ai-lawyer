# Data Protection Impact Assessment (DPIA) Template
## Gegevensbeschermingseffectbeoordeling (GEB)

## Legal Basis
- **Art. 35 AVG/GDPR**: DPIA is mandatory when processing is likely to result in a **high risk** to the rights and freedoms of natural persons
- **AP List (Art. 35(4))**: The AP has published a list of processing operations that always require a DPIA

---

## When is a DPIA Required?

### Mandatory (per AP list and EDPB Guidelines)
A DPIA is required when the processing involves at least TWO of the following criteria:
1. Evaluation or scoring (profiling, prediction)
2. Automated decision-making with legal or significant effects
3. Systematic monitoring (surveillance)
4. Sensitive data or data of highly personal nature
5. Large-scale processing
6. Matching or combining datasets
7. Data concerning vulnerable data subjects (employees, children, patients, elderly)
8. Innovative use or application of new technology
9. Processing that prevents data subjects from exercising a right or using a service

### AP Specific List (Examples)
- Covert investigation of employees
- Biometric data processing for identification purposes
- Genetic data processing outside healthcare
- Location tracking of employees
- Black lists or warning systems
- Processing of communication data (metadata)
- Large-scale profiling (credit scoring, fraud detection)
- Camera surveillance of publicly accessible areas (systematic)
- Processing of health data by non-healthcare institutions

### When NOT Required
- Processing already authorized by law with DPIA performed at legislative level
- Processing on the AP's list of exemptions
- Processing identical to one for which DPIA was already performed (and circumstances have not changed)

---

## DPIA Template Structure

### 1. Introduction and Context

| Field | Description |
|-------|-------------|
| **Project name** | [Name of the processing activity/project] |
| **Date** | [Date of DPIA] |
| **Version** | [Version number] |
| **Responsible** | [Name and role of the person(s) conducting the DPIA] |
| **DPO consulted** | [Yes/No - name of DPO and date of consultation] |
| **Organization** | [Name of the data controller] |

### 2. Description of the Processing (Art. 35(7)(a))

#### 2.1 Nature of the Processing
- What personal data is collected?
- How is it collected (directly from data subject, from third parties, automated collection)?
- How is it stored (systems, databases, cloud/on-premises)?
- How is it used (purposes)?
- Who has access?
- How long is it retained?
- How is it disposed of?

#### 2.2 Scope
- Number of data subjects affected
- Volume of data processed
- Geographic scope
- Duration of processing

#### 2.3 Context
- Relationship between data controller and data subjects
- Reasonable expectations of data subjects
- Current state of technology
- Source of data

#### 2.4 Purpose (Doeleinde)
- Primary purpose of processing
- Secondary purposes (if any)
- Legal basis (Art. 6 AVG) for each purpose
- If legitimate interest: documented balancing test

### 3. Necessity and Proportionality Assessment (Art. 35(7)(b))

| Criterion | Assessment |
|-----------|------------|
| **Lawfulness** | Is there a valid legal basis? |
| **Purpose limitation** | Is the purpose specific, explicit, and legitimate? |
| **Data minimization** | Is only necessary data collected? Could the purpose be achieved with less data? |
| **Accuracy** | Are measures in place to keep data accurate and up-to-date? |
| **Storage limitation** | Is the retention period proportionate? Is there automated deletion? |
| **Integrity and confidentiality** | Are appropriate security measures in place? |
| **Accountability** | Can the controller demonstrate compliance? |
| **Necessity** | Is the processing strictly necessary for the purpose? Are there less invasive alternatives? |
| **Proportionality** | Is the processing proportionate to the purpose? |

### 4. Risk Assessment (Art. 35(7)(c))

#### 4.1 Risk Identification
For each identified risk, assess:
- **Likelihood**: Low / Medium / High
- **Severity**: Low / Medium / High
- **Overall risk**: Low / Medium / High / Critical

#### 4.2 Standard Risk Categories

| Risk Category | Description | Example |
|--------------|-------------|---------|
| Unauthorized access | Data accessed by unauthorized persons | Hacking, insider threat |
| Data loss | Data lost or destroyed | Hardware failure, ransomware |
| Unauthorized disclosure | Data shared with wrong recipients | Email to wrong recipient, data leak |
| Excessive collection | More data collected than necessary | Over-broad forms, excessive logging |
| Purpose creep | Data used for unintended purposes | Marketing use of service data |
| Inaccuracy | Decisions based on wrong data | Outdated profiles, matching errors |
| Loss of control | Data subjects cannot exercise rights | No delete mechanism, opaque profiling |
| Discrimination | Processing leads to unfair treatment | Biased algorithms, profiling |
| Financial harm | Financial loss to data subjects | Identity theft, fraud |
| Physical harm | Physical harm to data subjects | Location data stalking |
| Reputational harm | Damage to reputation of data subjects | Public exposure of private information |

### 5. Mitigation Measures (Art. 35(7)(d))

For each identified risk, document:

| Risk | Current Measures | Additional Measures | Residual Risk | Responsible | Deadline |
|------|-----------------|--------------------|-|-------------|----------|
| [Risk] | [Existing controls] | [Planned controls] | [Low/Med/High] | [Name] | [Date] |

#### Common Mitigation Measures:
- Encryption (at rest and in transit)
- Pseudonymization or anonymization
- Access controls (role-based, need-to-know)
- Logging and monitoring
- Regular security testing (penetration testing, vulnerability scanning)
- Staff training
- Data processing agreements (verwerkersovereenkomsten)
- Privacy by design and by default
- Data subject rights procedures
- Incident response procedures
- Regular audits
- Data retention and deletion procedures

### 6. Consultation

#### 6.1 DPO Advice
- DPO opinion on necessity, proportionality, and risk mitigation
- DPO recommendation

#### 6.2 Data Subject Consultation (if applicable)
- Were data subjects or their representatives consulted?
- Outcomes of consultation

#### 6.3 Prior Consultation with AP (Art. 36 AVG)
Required if residual risk remains high after mitigation:
- If residual risk is high: MUST consult AP before proceeding
- AP has 8 weeks to respond (extendable by 6 weeks)
- Document whether prior consultation was triggered

### 7. Decision

| Field | Content |
|-------|---------|
| **Overall residual risk** | [Low / Medium / High] |
| **Decision** | [Proceed / Proceed with conditions / Do not proceed / Consult AP] |
| **Conditions** | [List any conditions for proceeding] |
| **Approved by** | [Name, role, date] |

### 8. Review and Monitoring
- **Review frequency**: [Annual / upon significant change / other]
- **Next review date**: [Date]
- **Trigger events for re-assessment**: Changes in processing, new technology, security incidents, legislative changes, AP guidance

---

## Notes for Dutch Context
- Use Dutch terminology in the formal DPIA document if the organization operates in Dutch
- Reference UAVG-specific provisions where applicable (e.g., BSN processing, criminal data)
- Consider Telecommunicatiewet requirements for cookie/tracking DPIAs
- AP may request the DPIA during an investigation - ensure it is documented and accessible
- DPIA is a living document - update when processing changes
