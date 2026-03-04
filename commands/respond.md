---
name: respond
description: Generate templated legal response
arguments:
  - name: type
    description: Response type (dsar, discovery-hold, bezwaar, ingebrekestelling, sommatiebrief)
    required: true
  - name: details
    description: Specific details for the response
    required: true
  - name: language
    description: nl or en (default nl)
    required: false
---

# Generate Templated Legal Response

Generate a formal legal response document based on the specified type, compliant with Dutch law requirements.

## Skill and Tools

Use MCP tools:
- `legislation_search` -- to verify applicable legal provisions for each response type
- `legislation_fetch` -- to retrieve specific articles referenced in the response

## Workflow

### Step 1: Response Type Identification

Determine the response type and applicable law:

| Type | Dutch Name | Legal Basis | Purpose |
|------|-----------|-------------|---------|
| `dsar` | AVG-inzageverzoek | Art. 15 AVG | Data Subject Access Request under GDPR |
| `discovery-hold` | Litigation hold | Art. 21 Rv / good practice | Preserve documents for anticipated litigation |
| `bezwaar` | Bezwaarschrift | Art. 6:4-6:24 Awb | Administrative law objection |
| `ingebrekestelling` | Ingebrekestelling | Art. 6:82 BW | Notice of default / formal demand to perform |
| `sommatiebrief` | Sommatiebrief | Art. 6:82 BW / general | Demand letter / cease and desist |

### Step 2: Parse Details

Extract from the `details` argument:
- Names of parties (sender and recipient)
- Relevant dates, reference numbers, contract details
- Specific grievance or request
- Any deadlines or prior correspondence
- Amount claimed (if applicable)

### Step 3: Generate Response by Type

---

#### TYPE: DSAR (Data Subject Access Request / AVG-inzageverzoek)

```
[Logo / Letterhead placeholder]

[Sender name]
[Sender address]

                                        [Recipient / Data Controller]
                                        [Address]

[Place], [Date]

Betreft: Verzoek om inzage persoonsgegevens op grond van artikel 15 AVG
[Re: Data Subject Access Request pursuant to Article 15 GDPR]

Ref: [reference number if applicable]

Geachte heer/mevrouw,

Hierbij verzoek ik u, op grond van artikel 15 van de Algemene Verordening
Gegevensbescherming (AVG / Verordening (EU) 2016/679), om mij de volgende
informatie te verstrekken:

1. Een bevestiging of u persoonsgegevens van mij verwerkt;
2. Indien ja, een kopie van alle persoonsgegevens die u van mij verwerkt;
3. De verwerkingsdoeleinden;
4. De categorieeen van persoonsgegevens die worden verwerkt;
5. De ontvangers of categorieeen van ontvangers aan wie de persoonsgegevens
   zijn verstrekt;
6. De beoogde bewaartermijn of de criteria ter bepaling daarvan;
7. Het bestaan van geautomatiseerde besluitvorming, met inbegrip van
   profilering, en de onderliggende logica;
8. Indien van toepassing, informatie over de bron van de gegevens.

[Specific details from user input]

Op grond van artikel 12 lid 3 AVG dient u binnen een maand na ontvangst
van dit verzoek te reageren. Ik verzoek u de informatie te versturen naar:

[Contact details / delivery method]

Ter identificatie treft u bijgaand een kopie van [identification document].

Ik verzoek u de ontvangst van dit schrijven te bevestigen.

Met vriendelijke groet,

[Name]
[Contact details]
```

---

#### TYPE: DISCOVERY HOLD (Litigation Hold Notice)

```
[Logo / Letterhead placeholder]

VERTROUWELIJK / CONFIDENTIAL

[Date]

Aan: [Recipients -- relevant departments/persons]
Van: [Legal department / Sender]
Betreft: Litigation Hold Notice / Bewaarplicht processtukken

Ref: [matter reference]

Geachte collega / Dear colleague,

[DUTCH VERSION]
In verband met [omschrijving geschil/procedure] zijn wij verplicht alle
documenten en gegevens die relevant (kunnen) zijn voor deze kwestie te
bewaren. Dit betreft zowel fysieke als digitale documenten.

U wordt verzocht met onmiddellijke ingang:

1. NIET te verwijderen, vernietigen, wijzigen of overschrijven:
   - E-mails en bijlagen met betrekking tot [onderwerp]
   - Documenten, contracten, correspondentie met betrekking tot [onderwerp]
   - Financiele administratie betreffende [onderwerp]
   - Alle overige documenten die verband houden met [onderwerp]

2. WEL te bewaren:
   - Alle bovengenoemde documenten in hun huidige staat
   - Back-ups die deze documenten bevatten
   - Metadata van relevante bestanden

3. De automatische verwijdering van e-mails en documenten voor de
   hierboven genoemde categorieeen op te schorten.

Deze bewaarplicht geldt tot nader bericht. Het niet naleven van deze
instructie kan ernstige juridische gevolgen hebben.

[Specific details from user input]

Bij vragen kunt u contact opnemen met [contact person].

Met vriendelijke groet,

[Name]
[Title]
```

---

#### TYPE: BEZWAAR (Administrative Objection)

```
[Sender details]
[Address]

                                        [Administrative body]
                                        [Address]

Per aangetekende post / registered mail

[Place], [Date]

Betreft: BEZWAARSCHRIFT
Tegen: [description of decision]
Kenmerk besluit: [reference number]
Datum besluit: [date of decision]

Geacht college / Geachte [appropriate salutation],

Hierbij maak ik, [name sender], op grond van artikel 6:4 en verder van de
Algemene wet bestuursrecht (Awb), bezwaar tegen uw besluit van [date],
met kenmerk [reference], waarbij u [brief description of decision].

Het bezwaarschrift is tijdig ingediend, nu het besluit is gedateerd op
[date] en het bezwaarschrift binnen de wettelijke termijn van zes weken
wordt ingediend.

GRONDEN VAN HET BEZWAAR

[Substantive grounds -- derived from user's details]

1. [Ground 1: explain why the decision is incorrect or unlawful]

2. [Ground 2: if applicable]

3. [Ground 3: if applicable]

VERZOEK

Op grond van het voorgaande verzoek ik u:

Primair: [primary relief sought -- e.g., het bestreden besluit te
herroepen en alsnog het gevraagde toe te wijzen];

Subsidiair: [alternative relief if applicable].

Tevens verzoek ik u:
- Mij in de gelegenheid te stellen het bezwaar mondeling toe te lichten
  (artikel 7:2 Awb);
- [If urgent: een voorlopige voorziening te treffen / NOTE: this is a
  separate procedure at the court].

Ik behoud mij het recht voor de gronden van dit bezwaar aan te vullen.

Met vriendelijke groet,

[Name]
[Address]
[Phone / email]

Bijlagen:
- Kopie van het bestreden besluit
- [Other attachments]
```

---

#### TYPE: INGEBREKESTELLING (Notice of Default)

```
[Sender details]
[Address]

                                        [Recipient]
                                        [Address]

Per aangetekende post met ontvangstbevestiging

[Place], [Date]

Betreft: INGEBREKESTELLING
Inzake: [contract/matter description]
Ref: [reference number / contract number]

Geachte heer/mevrouw [name],

Onder verwijzing naar [de overeenkomst / het contract] van [date] tussen
[party 1] en [party 2] (hierna: "de Overeenkomst"), stel ik u hierbij
formeel in gebreke op grond van artikel 6:82 van het Burgerlijk Wetboek.

TEKORTKOMING

U bent tekortgeschoten in de nakoming van uw verplichtingen uit hoofde van
de Overeenkomst, en wel als volgt:

[Specific description of the breach / failure to perform, derived from
user's details]

SOMMATIE

Hierbij sommeer ik u om binnen een redelijke termijn van [number] dagen
na dagtekening van deze brief, derhalve uiterlijk op [calculated date],
alsnog volledig na te komen door:

[Specific performance required]

GEVOLGEN BIJ NIET-NAKOMING

Indien u niet binnen voornoemde termijn aan deze sommatie voldoet, bent u
van rechtswege in verzuim (artikel 6:82 jo. 6:81 BW). In dat geval
behoud ik mij uitdrukkelijk het recht voor om:

1. Nakoming te vorderen, vermeerderd met schadevergoeding (art. 6:74 BW);
2. De overeenkomst te ontbinden (art. 6:265 BW) en schadevergoeding te
   vorderen;
3. Alle overige rechten en rechtsmiddelen uit te oefenen die mij
   toekomen.

Tevens bent u vanaf het moment van verzuim de wettelijke (handels)rente
verschuldigd over het openstaande bedrag.

Alle kosten die voortvloeien uit uw tekortkoming, waaronder buitengerech-
telijke incassokosten conform het Besluit vergoeding voor buitengerech-
telijke incassokosten, komen voor uw rekening.

Ik vertrouw erop dat het niet zover hoeft te komen en dat u binnen de
gestelde termijn aan uw verplichtingen zult voldoen.

Met vriendelijke groet,

[Name]
[Contact details]

Per aangetekende post verzonden op: [date]
```

---

#### TYPE: SOMMATIEBRIEF (Demand Letter)

```
[Sender details]
[Address]

                                        [Recipient]
                                        [Address]

Per aangetekende post met ontvangstbevestiging

[Place], [Date]

Betreft: SOMMATIE [/ CEASE AND DESIST]
Inzake: [description]
Ref: [reference]

Geachte heer/mevrouw [name],

Namens [client/zichzelf] wend ik mij tot u inzake [subject matter].

FEITEN

[Statement of facts derived from user's details]

JURIDISCH KADER

[Applicable legal basis -- e.g., contract provisions, BW articles,
intellectual property rights, etc.]

SOMMATIE

Op grond van het voorgaande sommeer ik u hierbij om:

1. [Demand 1 -- e.g., per direct te staken en gestaakt te houden...]
2. [Demand 2 -- e.g., binnen [X] dagen een bedrag van EUR [amount] te
   voldoen...]
3. [Demand 3 -- e.g., een onthoudingsverklaring te ondertekenen...]

binnen een termijn van [number] dagen na dagtekening van deze brief,
derhalve uiterlijk op [calculated date].

GEVOLGEN BIJ NIET-VOLDOENING

Indien u niet tijdig en volledig aan deze sommatie voldoet, zal ik
zonder nadere aankondiging rechtsmaatregelen treffen, waaronder:

- [Het starten van een gerechtelijke procedure]
- [Het leggen van conservatoir beslag]
- [Het vorderen van een kort geding]
- [Overige maatregelen]

Alle hieruit voortvloeiende kosten, inclusief de volledige proceskosten
en buitengerechtelijke kosten, zullen op u worden verhaald.

Ik ga ervan uit dat u het niet zover zult laten komen.

Een kopie van deze brief wordt bewaard in mijn administratie.

Met vriendelijke groet,

[Name]
[Contact details]

Per aangetekende post verzonden op: [date]
Kopie per e-mail aan: [email if applicable]
```

### Step 4: Language Handling

If `language` is "en":
- Generate the response in English
- Include relevant Dutch legal terms in parentheses
- Note that formal Dutch legal correspondence is typically in Dutch, and an English version may have limitations
- For bezwaar: note that administrative bodies may require Dutch submissions

If `language` is "nl" or not specified:
- Generate in Dutch (as shown in templates above)

### Step 5: Template Notice

Include a notice at the top of the generated response:

```
============================================================
CONCEPT -- CONTROLEER VOOR VERZENDING
Dit document is gegenereerd door een AI-assistent. Controleer
alle gegevens en pas het aan voordat u het verzendt. Raadpleeg
een advocaat bij twijfel.

DRAFT -- REVIEW BEFORE SENDING
This document was generated by an AI assistant. Verify all
details and customize before sending. Consult a lawyer if
in doubt.
============================================================
```

### Step 6: Disclaimer

Always append the following disclaimer at the end of the output:

---

**Disclaimer / Juridische kennisgeving**

This legal response template is generated by an AI legal assistant and does not constitute legal advice within the meaning of the Advocatenwet. This is a template that must be reviewed and customized before use. Legal responses may have strict deadlines (e.g., bezwaar: 6 weeks) -- missing deadlines can result in loss of rights. You should consult a qualified Dutch advocaat before sending formal legal correspondence, especially in matters involving administrative procedures, litigation, or significant financial claims. No attorney-client relationship is created.

*Dit juridisch document is gegenereerd door een AI-juridisch assistent en vormt geen juridisch advies in de zin van de Advocatenwet. Dit is een sjabloon dat moet worden beoordeeld en aangepast voor gebruik. Juridische reacties kunnen strikte termijnen hebben (bijv. bezwaar: 6 weken). U dient een gekwalificeerde Nederlandse advocaat te raadplegen voordat u formele juridische correspondentie verstuurt.*
