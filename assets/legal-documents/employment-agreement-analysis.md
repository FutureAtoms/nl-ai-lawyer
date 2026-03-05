# Employment Agreement Analysis: Can You Run FutureAtoms Alongside Axelera?

**Prepared for:** Abhilash Chadhar
**Date:** 5 March 2026
**Document type:** Comprehensive Employment Agreement Analysis
**Jurisdiction:** Netherlands (Kingdom of the Netherlands)
**Contract reviewed:** Axelera AI B.V. Employment Agreement (DocuSign ID: F3BAD03D-59AE-4277-8ABB-BA2DA2B5D56E, signed August 2022)
**Employment type:** Indefinite contract (*arbeidsovereenkomst voor onbepaalde tijd*) since 1 December 2022
**Position:** Senior Verification Engineer

---

## Context

Abhilash Chadhar asks whether his Axelera AI employment agreement (signed August 2022, indefinite contract since 1 December 2022) permits him to operate FutureAtoms (eenmanszaak, KvK: 99153289) and develop ChipOS in parallel, and what happens if Axelera objects.

This analysis examines every relevant clause of the employment agreement against current Dutch statutory law.

---

## SHORT ANSWER

**Yes, it is legally possible** — but it requires Axelera's prior written consent under Clause 13. The good news: your contract already says that consent **"shall not be unreasonably withheld on objective grounds"**, and Dutch law (Art. 7:653a BW, effective since 1 August 2022) makes it very difficult for Axelera to refuse without a concrete, objective justification. If they refuse without proper grounds, you can challenge the refusal in court.

---

## CLAUSE-BY-CLAUSE ANALYSIS

### 1. Clause 13 — "No ancillary activities" (THE KEY CLAUSE)

**What it says (page 6-7):**

> "Without the Employer's prior written consent, **which consent shall not be unreasonably withheld on objective grounds**, the Employee may not accept any remunerated work at or for third parties and must refrain from doing business for his own account, **if that, in the Employer's opinion, may harm the Employer's interests**"

**Your position is STRONG here. Here's why:**

| Factor | Analysis |
|--------|----------|
| **Built-in safeguard** | The clause itself says consent cannot be "unreasonably withheld on objective grounds" — this is already employee-friendly language |
| **Harm requirement** | The restriction only applies if the side activity "may harm the Employer's interests" — FutureAtoms has zero revenue, zero clients, and most projects (healthcare, music, wellness) have nothing to do with Axelera |
| **Art. 7:653a BW override** | Since 1 August 2022, Dutch law provides that ANY clause prohibiting side activities is **void** unless the employer demonstrates an "objective justification" at the time of invoking it. This statutory protection OVERRIDES any contractual language that is less favorable to the employee. |
| **Charity carve-out** | The clause already allows "limited and non-conflicting charity work or activities" — showing the parties contemplated that some outside activities are acceptable |

**Conditions attached to consent (important — you must comply with these):**
- Do NOT use Axelera's technologies or IP for FutureAtoms work
- Maintain all confidentiality obligations (Clause 11)
- No financial interest in competitive businesses without approval (2% stock exception)

**Legal framework — Art. 7:653a BW:**

Article 7:653a of the Dutch Civil Code (*Burgerlijk Wetboek*), effective since 1 August 2022, implements EU Directive 2019/1152 (Transparent and Predictable Working Conditions). It provides:

> *"Een beding waarbij de werkgever verbiedt of beperkt dat de werknemer voor anderen arbeid verricht buiten de tijdstippen waarop de arbeid moet worden verricht bij die werkgever, is nietig, tenzij dit beding kan worden gerechtvaardigd op grond van een objectieve reden."*

Translation: A clause whereby the employer prohibits or restricts the employee from performing work for others outside the times when work must be performed for the employer is **void**, unless the clause can be justified on objective grounds.

Recognized objective grounds include:
- Health and safety (e.g., Working Time Act compliance)
- Protection of business confidentiality
- Avoidance of genuine conflicts of interest
- Compliance with integrity rules

The objective justification need not be stated in the clause itself but must be demonstrable at the time the employer invokes the restriction.

**Bottom line on Clause 13:** You need written approval, but Axelera has a high legal bar to clear if they want to refuse. Request it formally in writing.

---

### 2. Clause 10 — Non-compete and non-solicitation (THE RISK CLAUSE)

**What it says (page 5):**

> During employment AND for **1 year after termination**, the Employee shall not "engage in or carry out or be concerned or interested in **the Business worldwide**"

**"The Business"** is defined in Recital A as:

> "research and development, enhancement, maintenance and exploitation of intellectual properties, **software and hardware products for artificial intelligence**"

**This is your biggest contractual risk.** Here's the analysis:

| Issue | Assessment |
|-------|-----------|
| **Scope** | Extremely broad — covers ALL AI software and hardware worldwide |
| **ChipOS overlap?** | ChipOS is a semiconductor design orchestration platform. It uses AI. Under the literal wording of "software products for artificial intelligence," Axelera *could* argue ChipOS falls within scope. |
| **Geographic scope** | "Worldwide" — Dutch courts regularly narrow overly broad geographic restrictions |
| **Duration** | 1 year post-termination — this is within the normal range Dutch courts accept |
| **During employment** | Applies NOW while you are employed |

**However, Dutch law provides significant protection:**

- **Art. 7:653 BW** (non-compete clause): A court (*kantonrechter*) can **wholly or partially nullify** a non-compete clause if the employee is "unjustly disadvantaged in proportion to the interest to be protected" (*onbillijk benadeeld in verhouding tot het te beschermen belang*). The relevant text of Art. 7:653 lid 2 BW provides:

  > *"De rechter kan zulk een beding geheel of gedeeltelijk vernietigen op grond dat, in verhouding tot het te beschermen belang van de werkgever, de werknemer door dat beding onbillijk wordt benadeeld."*

- The **worldwide scope** covering ALL AI software is almost certainly disproportionate — a court would likely narrow this to Axelera's specific field (AI hardware accelerators)

- **Art. 7:653a BW** (the newer 2022 law on side activities) provides an additional layer of protection that operates separately from the non-compete analysis

- ChipOS is **vendor-neutral semiconductor design tooling**, NOT an AI hardware accelerator. The overlap with "the Business" is arguable, not clear-cut.

**Key distinction**: Clause 10 says "except with the prior written approval of the Employer." If Axelera gives written approval for FutureAtoms under Clause 13, this also addresses the non-compete concern during employment.

---

### 3. Clause 15 — Intellectual Property (THE IP CLAUSE)

**What it says (page 7):**

> "Any intellectual property rights... arising from or **in connection with the activities of the Employee in the context this Agreement**... are owned by the Employer"

**Critical limiting language:** "in the context this Agreement" — this scopes IP ownership to work done **in the context of your employment**. Activities you do independently, outside working hours, with your own equipment, on your own initiative, are arguably NOT "in the context of this Agreement."

| Factor | Your position |
|--------|--------------|
| **"in the context this Agreement"** | ChipOS was developed independently, outside hours, own equipment — NOT in the context of the employment agreement |
| **Art. 7 Auteurswet** | Employer copyright requires a "functional connection" (*functioneel verband*) between employment duties and the creative work. Your job is Senior Verification Engineer, not AI platform developer. The seminal case HR 19 januari 1951, NJ 1952/37 (*Van der Laan/Schoonderbeek*) established that the work must be created "in dienst van" (in the service of) the employer with a functional connection to employment duties. |
| **Clause 15.2.3** | "Employee shall refrain from registering any Intellectual Property Right in his own name" — BUT this refers to "the Intellectual Property Rights" as defined (those arising from employment activities), NOT independently created IP |
| **Advance transfer (15.2.1)** | The *bij voorbaat* transfer only covers IP "arising from or in connection with" employment activities |
| **EU Directive 2009/24/EC Art. 2(3)** | Employer copyright in software requires creation "in the execution of duties" or "following employer instructions." Independent work satisfies neither condition. |

**Bottom line on IP:** Clause 15 is broad in language but legally limited to work done in the employment context. ChipOS, developed independently on your own time and resources, has a strong argument for falling outside this scope. However, this is the clause Axelera would most aggressively try to use, so **documentation of independence is critical** (separate equipment, outside hours, no Axelera resources).

---

### 4. Clause 14 — Business Opportunities

**What it says:**

> "The Employee shall, during the term of this Agreement, offer any business opportunity reasonably relating to the Business first to the Employer in writing."

This is a **right of first refusal**. If a FutureAtoms opportunity relates to AI hardware/software (Axelera's Business definition), you must offer it to Axelera first. If Axelera rejects it in writing, you're free to pursue it.

**Practical impact:** Most FutureAtoms projects (healthcare, music, wellness) clearly don't relate to Axelera's Business. ChipOS's vendor-neutral semiconductor tooling is arguable. Wingman (Voyager SDK) clearly does relate — which is why the Wingman delivery arrangement was negotiated.

---

### 5. Clause 16 — Penalty Clause

**What it says:**

> EUR **50,000 per breach** + EUR **500/day** for continuing breaches

This applies to violations of Clauses 10, 11, 12, 13, 14, and 15. This is a real financial risk. However:

- Under **Art. 6:94 BW**, a court can **moderate** (*matigen*) penalty clauses if the penalty is disproportionate. The relevant provision states:

  > *"Op verlangen van de schuldenaar kan de rechter, indien de billijkheid dit klaarblijkelijk eist, de bedongen boete matigen."*

  Translation: At the debtor's request, the court may moderate the stipulated penalty if fairness manifestly so requires.

- The penalty must be proportionate to actual harm suffered
- If you're operating a zero-revenue side business that doesn't compete, a EUR 50,000 penalty would likely be moderated significantly
- The Hoge Raad has held (HR 27 april 2007, ECLI:NL:HR:2007:AZ6638, *Intrahof/Bart Smit*) that courts should exercise restraint in moderation but can do so where the result is manifestly disproportionate

---

## WHAT HAPPENS IF AXELERA SAYS NO?

### Scenario A: Axelera refuses consent without objective grounds

**Your legal position is strong:**

1. **Art. 7:653a BW** makes the refusal legally defective — a restriction on side activities without objective justification is **void by operation of law** (*nietig*)
2. **Clause 13 itself** says consent "shall not be unreasonably withheld on objective grounds" — an unreasonable refusal violates the contract
3. You could bring a **kort geding** (summary proceedings) before the *kantonrechter* to compel consent or obtain a declaratory judgment that you may continue
4. **Art. 7:611 BW** (*goed werkgeverschap*) requires Axelera to act as a reasonable employer. This provision states:

   > *"De werkgever en de werknemer zijn verplicht zich als een goed werkgever en een goed werknemer te gedragen."*

   Translation: The employer and employee are obliged to behave as a good employer and good employee.

5. **Equal treatment argument**: If approximately 34% of Axelera employees maintain concurrent roles or side businesses (based on publicly available data), refusing one employee while tolerating others may constitute unequal treatment in breach of good employer practice

### Scenario B: Axelera claims FutureAtoms competes and invokes Clause 10

**This is the harder fight, but still defensible:**

1. Challenge the **disproportionate scope** of the non-compete (worldwide, all AI software) under Art. 7:653 lid 2 BW
2. Argue ChipOS is **vendor-neutral semiconductor design tooling**, not an AI hardware accelerator
3. Point out that **8 of 9 FutureAtoms projects** have zero overlap with Axelera's business
4. Request the court to **nullify or narrow** the non-compete to Axelera's actual competitive interest (AI hardware accelerator products)
5. The **Stoof/Mammoet test** (HR 11 July 2008, ECLI:NL:HR:2008:BD1847) applies to any unilateral changes to employment terms: the employer must show (i) changed circumstances, (ii) a reasonable proposal, and (iii) that the employee cannot reasonably refuse

### Scenario C: Axelera threatens termination

**You have substantial protection:**

1. Dutch dismissal law (Art. 7:669 BW) requires a **reasonable ground** (*redelijke grond*) for termination — operating a lawful side business is not automatically a ground for dismissal. The law enumerates eight exhaustive grounds (the a-h grounds):
   - (a) economic/organizational reasons (bedrijfseconomisch)
   - (b) long-term incapacity (langdurige arbeidsongeschiktheid)
   - (c) frequent absenteeism (frequent ziekteverzuim)
   - (d) dysfunction (disfunctioneren)
   - (e) culpable behavior (verwijtbaar handelen of nalaten)
   - (f) conscientious objection (gewetensbezwaren)
   - (g) disrupted employment relationship (verstoorde arbeidsverhouding)
   - (h) other circumstances (overige omstandigheden)

   Operating a lawful side business does not fit neatly into any of these categories. Axelera would need to argue either (e) culpable behavior or (g) disrupted relationship, both of which require substantial evidence.

2. Axelera would need UWV or court permission to dismiss
3. If dismissed, you're entitled to a **transition payment** (*transitievergoeding*) — Art. 7:673 BW. The formula: 1/3 monthly salary per year of service.
4. If the dismissal is found to be "seriously culpable" (*ernstig verwijtbaar*) on Axelera's part, you could receive an **additional fair compensation** (*billijke vergoeding*) — Art. 7:681 BW
5. **Important**: As a kennismigrant, termination has immigration consequences — see the immigration risk assessment (`immigration-risk-assessment.md`)

---

## PART 2: THE PROPOSED ADDENDUM (Clauses 1.1–1.19)

**This addendum is a completely different document from your original contract.** Where your original Clause 15 only captures IP created "in the context of this Agreement" (i.e., employment activities), the proposed addendum attempts to reach far beyond your employment and claim rights over ChipOS itself — a product you developed independently.

### OVERALL ASSESSMENT: The addendum is dramatically overbroad and contains several provisions that are legally vulnerable under Dutch law.

A detailed clause-by-clause analysis is provided in the separate addendum analysis document (`axelera-addendum-analysis.md`). Below is a summary of the key issues.

---

### Addendum Clause-by-Clause: Problems and Legal Vulnerabilities

#### 1.2 — ChipOS Definition: OVERBROAD

> "including any successor, derivative, fork, update, extension, architectural variation or **related technology** developed within the Company"

**Problem:** "Related technology" is undefined and could capture virtually any software you ever develop. This is a **catch-all** that goes far beyond what is reasonable.

**Legal vulnerability:** Under **Art. 6:248 lid 2 BW** (*derogerende werking van redelijkheid en billijkheid*), a provision that is unconscionably broad may be unenforceable. A court would likely read "related technology" narrowly or strike it. Art. 6:248 lid 2 BW provides:

> *"Een tussen partijen als gevolg van de overeenkomst geldende regel is niet van toepassing, voor zover dit in de gegeven omstandigheden naar maatstaven van redelijkheid en billijkheid onaanvaardbaar zou zijn."*

Translation: A rule applicable between parties as a result of the agreement does not apply insofar as this would be unacceptable by standards of reasonableness and fairness in the given circumstances.

---

#### 1.3a — Non-Exclusive License to ALL of ChipOS: GOES BEYOND WINGMAN

> "perpetual, irrevocable, worldwide, fully paid-up, royalty-free, transferable and sublicensable non-exclusive licence to use, reproduce, modify, adapt, integrate, commercialise, distribute and otherwise exploit **the ChipOS** in all fields of use"

**Problem:** This grants Axelera a full non-exclusive license to your **entire ChipOS platform** — all 11 App Packs, vendor-neutral tooling, everything — not just the Wingman deliverable. This is far beyond what was discussed.

**Legal vulnerability:**
- You and Axelera discussed **Wingman** delivery, not a ChipOS platform license
- Granting away a perpetual, irrevocable license to an independently developed platform without adequate compensation may fail the **Stoof/Mammoet test** (HR 11 July 2008, ECLI:NL:HR:2008:BD1847) — an employer cannot unilaterally impose unreasonable employment term changes
- The consideration offered (continued employment + existing salary) may be legally insufficient for a perpetual irrevocable license to an entire platform

---

#### 1.3b — Exclusive License in "Defined Fields": CAPTURES ALL COMPUTING

> "any and all fields of developing software and code for AI applications on CPUs, GPUs, AIPUs, accelerators, and **any other compute processors**"

**Problem:** "Any other compute processors" means **all hardware that exists**. CPUs, GPUs, NPUs, FPGAs, quantum processors — everything. This exclusive license covers developing AI software for ANY computing device worldwide. This is not a Wingman-scoped clause; it's a blanket claim on all AI software development.

**Legal vulnerability:**
- This is **disproportionate** under Art. 6:248 lid 2 BW — Axelera makes AI accelerator chips, not all computing hardware
- A court would very likely narrow this to Axelera's actual products (Metis NPU / AI accelerator hardware)

---

#### 1.5–1.6 — Delivery: DEMANDS CHIPOS SOURCE CODE, NOT JUST WINGMAN

> "full source code repository for **ChipOS** and Voyager Wingman"

**Problem:** This demands delivery of the **entire ChipOS source code** — your independently developed platform — not just Wingman. The agreed deliverable was Wingman v1.0.0.

**You should NOT deliver ChipOS source code.** The agreed deliverable is Wingman. ChipOS is your independent IP.

---

#### 1.8 — Future Developments: CAPTURES ALL WORK, EVEN OUTSIDE HOURS

> "All intellectual property rights in any developments... created **during the employment, whether during or outside working hours and whether at the workplace or elsewhere**, shall vest exclusively in the Company"

**This is the single most dangerous clause.** It attempts to capture ALL future work you do — including evenings, weekends, from home, on your own equipment — if it "relates to or builds upon" ChipOS.

**Legal vulnerabilities:**

| Issue | Law | Analysis |
|-------|-----|----------|
| **Captures work outside employment** | **Art. 7 Auteurswet** | Employer copyright ONLY applies to works created "in the service of" (*in dienst van*) the employer. Work done outside hours, on own equipment, on own initiative is NOT "in dienst van." This clause attempts to override a mandatory statutory provision. |
| **Violates side activities freedom** | **Art. 7:653a BW** | Since 1 August 2022, restricting what an employee does outside working hours requires objective justification. Capturing all outside-hours IP without justification violates this. |
| **Violates EU Directive** | **2009/24/EC Art. 2(3)** | Employer copyright in software requires creation "in the execution of duties" OR "following employer instructions." Independent work satisfies neither condition. |
| **Disproportionate** | **Art. 6:248 lid 2 BW** | Claiming ownership of all work an employee does anywhere, anytime, is unconscionable (*onaanvaardbaar*) |

**A court would very likely refuse to enforce this clause as written.** It contradicts mandatory Dutch copyright law.

---

#### 1.13 — Business Activities Ban: BLANKET PROHIBITION

> "the Employee shall not, without the Company's prior written consent, operate, promote, develop or otherwise participate in **any business or commercial activity related to artificial intelligence, software development or technologies** overlapping with the Company's business"

**Problem:** This bans you from participating in ANY AI or software development business — which is essentially your entire professional skill set. This is far broader than the original Clause 13 (which only restricted activities that "may harm" Axelera's interests).

**Legal vulnerability:**
- **Art. 7:653a BW** makes this void without objective justification per restriction
- A blanket ban on "software development" for a software engineer is disproportionate
- The original contract (Clause 13) already had the nuanced "not unreasonably withheld" standard — this addendum tries to replace it with a blanket ban

---

#### 1.14 — Suspension of FutureAtoms: ATTEMPTS FORCED SHUTDOWN

> "Any existing business activities of the Employee shall be **suspended** unless expressly approved in writing"

**Problem:** This demands you shut down FutureAtoms entirely. The "alternative" offered is switching to contractor status, which (as analyzed in the immigration risk assessment) would **destroy your HSM permit and citizenship timeline**.

**Legal vulnerability:**
- Cannot be imposed unilaterally — requires your consent
- The "contractor alternative" creates an immigration catastrophe, making this effectively coercive
- Conflicts with Art. 7:653a BW

---

#### 1.17 — Irrevocable License, No Termination Rights: EXTREMELY AGGRESSIVE

> "the Employee **waives any right** to terminate, rescind, dissolve or otherwise set aside the licence(s)"

**Problem:** This attempts to make you permanently waive all legal rights to ever challenge or modify the license, even if circumstances change dramatically. Under Dutch law, certain termination rights are mandatory and cannot be waived in advance.

**Legal vulnerability:**
- Advance waiver of rescission rights (*ontbinding*) based on material breach may conflict with mandatory law
- **Art. 6:265 BW** (right to dissolve on breach) is not fully waivable in employment contracts where the employee is the weaker party
- A court may find this waiver unconscionable under Art. 6:248 lid 2 BW

---

### Summary: Original Contract vs. Proposed Addendum

| Aspect | Original Contract (2022) | Proposed Addendum |
|--------|-------------------------|-------------------|
| **Side activities** | Allowed with consent "not unreasonably withheld" | Blanket ban on AI/software activities (1.13) |
| **IP scope** | Only IP "in the context of this Agreement" | ALL ChipOS IP + all future work anywhere, anytime (1.8) |
| **Deliverable** | No specific deliverable defined | Full ChipOS + Wingman source code delivery (1.5-1.6) |
| **License** | None (standard employment IP for employment work) | Perpetual irrevocable non-exclusive to ALL of ChipOS (1.3a) + exclusive in ALL computing (1.3b) |
| **FutureAtoms** | Permitted with approval | Must be suspended (1.14) |
| **Post-employment** | 1-year non-compete (Clause 10) | License survives forever, irrevocable, no termination (1.16-1.17) |
| **Compensation for IP** | N/A (only employment IP) | Your existing salary (1.19) — no additional compensation for ChipOS license |

### KEY CONCLUSION ON THE ADDENDUM

**You should NOT sign this addendum as drafted.** It goes far beyond the agreed Wingman delivery and attempts to capture your entire independent ChipOS platform, all future work, and shut down FutureAtoms. The counter-proposal you already prepared (in `employment-addendum-counter-proposal.md`) is the right approach: give Axelera strong rights to **Wingman** while protecting ChipOS and FutureAtoms.

If Axelera insists on this version, engage a Dutch employment lawyer immediately. Multiple clauses are legally vulnerable and a court would likely narrow them significantly.

---

## PRACTICAL RECOMMENDATIONS

### On the Original Contract (your current legal position)

1. **Your original contract PERMITS a side business with consent** — Clause 13 cannot be unreasonably refused. Combined with Art. 7:653a BW, your position is strong.

2. **Request written approval NOW** — Send a formal letter under Clause 13 disclosing FutureAtoms and requesting consent. A draft already exists in `side-business-permission-request.md`.

3. **Maintain strict separation** — Different equipment, outside working hours, no Axelera resources, no Axelera confidential information. Document this separation rigorously.

4. **Do NOT resign or switch to contractor** — Your employment provides immigration security (kennismigrant permit) and significant financial benefits. See `immigration-risk-assessment.md` for the full analysis.

### On the Proposed Addendum

5. **DO NOT sign the addendum as drafted** — It goes far beyond the agreed Wingman delivery and would effectively hand over ChipOS and shut down FutureAtoms.

6. **Respond with the counter-proposal** — The counter-proposal (`employment-addendum-counter-proposal.md`) gives Axelera strong exclusive Wingman rights while protecting ChipOS. This is the fair compromise. The response letter (`response-to-axelera-legal.md`) provides the cover letter for submitting the counter-proposal.

7. **Key negotiation points:**
   - Scope the license to **Wingman v1.0.0**, not all of ChipOS
   - "Defined Fields" should be **Axelera AI accelerator hardware**, not all computing
   - Clause 1.8 (all future IP) must be **deleted or narrowed** to Wingman-related work during employment duties only
   - Clause 1.13 (blanket business ban) must be replaced with the original Clause 13 standard ("not unreasonably withheld")
   - Clause 1.14 (suspend FutureAtoms) must be **deleted** — it conflicts with Art. 7:653a BW
   - Delivery (1.5-1.6) should cover **Wingman source code only**, not ChipOS

8. **Engage a Dutch employment lawyer (*arbeidsrechtadvocaat*)** — The addendum is aggressive enough that professional legal review is essential before signing anything. Given the immigration implications, also consult an immigration lawyer (*vreemdelingenadvocaat*).

9. **Do NOT deliver ChipOS source code** — Only the Wingman v1.0.0 deliverable should be provided. See `wingman-delivery-manifest.md` for the agreed delivery scope.

---

## RELATED DOCUMENTS

| Document | Description |
|----------|-------------|
| `axelera-addendum-analysis.md` | Detailed clause-by-clause analysis of the proposed addendum |
| `employment-addendum-counter-proposal.md` | Complete counter-proposal with fair Wingman licensing terms |
| `response-to-axelera-legal.md` | Cover letter for submitting the counter-proposal |
| `side-business-permission-request.md` | Formal request for written approval under Clause 13 |
| `immigration-risk-assessment.md` | Full immigration risk analysis (employee vs. contractor) |
| `chipos-wingman-independence-report.md` | Technical evidence of ChipOS/Wingman separation |
| `wingman-delivery-manifest.md` | Specification of the Wingman v1.0.0 delivery scope |
| `cover-message-to-bram.md` | Cover message for internal communication |
| `axelera-dual-roles-precedent.md` | Analysis of dual role precedents at Axelera |

---

## LEGAL PROVISIONS REFERENCED

| Provision | Subject | Key Text |
|-----------|---------|----------|
| **Art. 7:653a BW** | Side activities clause void without objective justification (since 1 Aug 2022) | *Nevenwerkzaamhedenbeding nietig tenzij objectieve rechtvaardiging* |
| **Art. 7:653 BW** | Non-compete clause; court can nullify if disproportionate | *Rechter kan beding geheel of gedeeltelijk vernietigen bij onbillijke benadeling* |
| **Art. 7 Auteurswet** | Employer copyright: requires functional connection to employment duties | *Werkgeversauteursrecht bij functioneel verband met dienstbetrekking* |
| **Art. 7:611 BW** | Good employer practice (*goed werkgeverschap*) | *Werkgever en werknemer verplicht zich als goed werkgever/werknemer te gedragen* |
| **Art. 7:669 BW** | Reasonable grounds required for dismissal (exhaustive a-h grounds) | *Redelijke grond vereist voor opzegging arbeidsovereenkomst* |
| **Art. 7:673 BW** | Transition payment on termination | *Transitievergoeding: 1/3 maandsalaris per dienstjaar* |
| **Art. 6:94 BW** | Court moderation of penalty clauses | *Rechter kan boete matigen indien billijkheid dit klaarblijkelijk eist* |
| **Art. 6:248 lid 2 BW** | Limitation based on reasonableness and fairness | *Derogerende werking van redelijkheid en billijkheid* |
| **Art. 6:265 BW** | Right to dissolve contract on material breach | *Ontbindingsrecht bij tekortkoming in de nakoming* |
| **EU Directive 2019/1152** | Transparent and predictable working conditions (underlies Art. 7:653a BW) | Implemented in Dutch law 1 August 2022 |
| **EU Directive 2009/24/EC Art. 2(3)** | Employer copyright in software: requires "execution of duties" or "employer instructions" | Software Directive |

## KEY CASE LAW REFERENCED

| Case | Subject |
|------|---------|
| **HR 11 July 2008, ECLI:NL:HR:2008:BD1847** (*Stoof/Mammoet*) | Employer cannot unilaterally impose unreasonable employment term changes; three-part test: (i) changed circumstances, (ii) reasonable proposal, (iii) employee cannot reasonably refuse |
| **HR 19 januari 1951, NJ 1952/37** (*Van der Laan/Schoonderbeek*) | Employer copyright under Art. 7 Auteurswet requires functional connection (*functioneel verband*) between employment duties and the creative work |
| **HR 27 april 2007, ECLI:NL:HR:2007:AZ6638** (*Intrahof/Bart Smit*) | Court moderation of penalty clauses under Art. 6:94 BW; courts should exercise restraint but can moderate manifestly disproportionate penalties |
| **CJEU C-406/10** (*SAS Institute v. WPL*) | Ideas and principles underlying a computer program are not protectable by copyright under EU Directive 2009/24/EC Art. 1(2); applied in Dutch law via *richtlijnconforme interpretatie* |
| **HR 25 februari 2000, NJ 2000/471** | Application of Art. 6:248 lid 2 BW: contractual provision not binding if application is unacceptable by standards of reasonableness and fairness |

---

**DISCLAIMER:** This is an AI-generated analysis and does NOT constitute legal advice within the meaning of the Dutch Advocates Act (Advocatenwet). This document is for informational purposes only and must be reviewed and finalized by a licensed attorney admitted to the Dutch bar (*advocaat*). Employment situations involving immigration status (kennismigrant) require particular care — consult both an employment lawyer (*arbeidsrechtadvocaat*) and an immigration lawyer (*vreemdelingenadvocaat*) before taking any action.

1. **Is for informational purposes only** and must not be considered a substitute for professional legal advice from a qualified Dutch lawyer (advocaat) registered with the Netherlands Bar Association (Nederlandse Orde van Advocaten).

2. **Is generated by artificial intelligence** and may contain inaccuracies, omissions, or outdated information, despite efforts to consult current and accurate sources.

3. **Does not replace a lawyer.** For legal decisions, proceedings, contracts, or disputes, you must always consult a qualified lawyer authorized to practice law in the Netherlands.

4. **Does not guarantee confidentiality.** Information shared with this AI system is not protected by attorney-client privilege (verschoningsrecht). Do not share confidential or privileged information.

5. **May not reflect current law.** Dutch legislation and case law change continuously. This analysis is based on the state of the law as of the indicated date and may not account for recent amendments.

6. **Cannot be used as evidence** in judicial or administrative proceedings.

7. **Does not guarantee the accuracy** of references to statutory articles, ECLI numbers, or other legal sources. Independently verify all source citations.

**By using this analysis, you acknowledge that you have read and understood this disclaimer and that you do not consider the AI system to be your legal advisor.**

---

*Generated by the Netherlands AI Lawyer System*
*Date of analysis: 2026-03-05*
*Legislation verification date: 2026-03-05*
*Contract reviewed: Axelera AI B.V. Employment Agreement (DocuSign ID: F3BAD03D-59AE-4277-8ABB-BA2DA2B5D56E, signed August 2022)*
