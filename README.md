# Netherlands AI Lawyer System

## Overview
Comprehensive AI lawyer system for Netherlands law, built as a Claude Code plugin with multi-agent team capabilities.

## Features
- 14 domain-specific legal skills covering all major Dutch law areas
- 12 slash commands for common legal tasks
- 7 specialized agents for complex multi-agent analysis
- Custom MCP server connecting to Dutch government APIs
- Integration with Rechtspraak.nl, wetten.nl, KVK, EUR-Lex

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- Claude Code CLI

### Installation

1. Clone this repository:
```bash
git clone [repo-url] ~/uncloud/nl-ai-lawyer
cd ~/uncloud/nl-ai-lawyer
```

2. Build the custom MCP server:
```bash
cd dutch-legal-mcp
npm install
npm run build
cd ..
```

3. Install Python dependencies:
```bash
pip install -r scripts/requirements.txt
```

4. (Optional) Set up KVK API key:
```bash
export KVK_API_KEY=your_api_key_here
```
Get your key at https://developers.kvk.nl/

5. Configure organization preferences:
```bash
cp assets/user-config-template.md .claude/nl-ai-lawyer.local.md
# Edit the file with your organization's preferences
```

## Available Commands

| Command | Description |
|---------|-------------|
| `/review-contract` | Dutch contract clause-by-clause review |
| `/triage-nda` | Rapid NDA pre-screening |
| `/search-rechtspraak` | Search Dutch case law |
| `/search-wetgeving` | Search Dutch legislation |
| `/company-check` | KVK company registry lookup |
| `/gdpr-check` | AVG/GDPR compliance assessment |
| `/brief` | Legal briefing on a topic |
| `/draft-contract` | Generate Dutch contract |
| `/legal-memo` | Structured legal memorandum |
| `/arbeidsrecht` | Employment law query |
| `/respond` | Templated legal response |
| `/kamervragen` | Parliamentary questions search |

## Legal Domains

1. Corporate Law (BV/NV, Boek 2 BW)
2. Contract Law (BW Boek 6/7)
3. Employment Law (WAB, WWZ, CAO)
4. Privacy/GDPR (AVG/UAVG)
5. Intellectual Property (Auteurswet, ROW, BVIE)
6. Real Estate (Huurrecht, Kadaster)
7. Tax Law (VPB, BTW)
8. Administrative Law (AWB)
9. Criminal Law (Wetboek van Strafrecht)
10. Immigration Law (IND, Kennismigrant)
11. EU Law Integration

## Multi-Agent Teams
For complex legal matters, the system can deploy specialized agent teams.

## APIs Used
- Rechtspraak.nl - Dutch case law (500K+ rulings)
- KOOP SRU / wetten.nl - Dutch legislation
- KVK - Company registry (requires API key)
- EUR-Lex SPARQL - EU law
- data.overheid.nl - Government datasets

## Disclaimer
This system provides AI-generated legal analysis and does NOT constitute legal advice. Always consult a qualified Dutch lawyer (advocaat) for legal matters.

## License
MIT
