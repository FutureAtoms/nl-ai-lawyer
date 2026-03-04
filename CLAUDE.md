# Netherlands AI Lawyer System

## Overview
Comprehensive AI lawyer system for Netherlands law as a Claude Code plugin with multi-agent team capabilities.

## Legal Domains
Corporate law (primary), contract law, employment law, privacy/GDPR, IP, real estate, tax, criminal, administrative, immigration, EU law integration.

## Architecture
- **14 domain skills** in `skills/` - each with YAML frontmatter and reference files
- **12 slash commands** in `commands/` - user-facing entry points
- **7 specialized agents** in `agents/` - for multi-agent team workflows
- **Custom MCP server** in `dutch-legal-mcp/` - TypeScript server wrapping Dutch legal APIs
- **Cerebra Legal MCP** in `cerebra-legal-mcp/` - Legal reasoning server
- **OpenTK MCP** - Dutch parliamentary data (installed via npx)
- **Python scripts** in `scripts/` - utility fallback scripts
- **Templates** in `assets/templates/` - legal document templates
- **Disclaimers** in `assets/disclaimers/` - mandatory NL + EN disclaimers

## Key APIs
- Rechtspraak.nl (case law, 500K+ rulings)
- KOOP SRU / wetten.nl (legislation)
- KVK (company registry, requires API key)
- EUR-Lex SPARQL (EU law)
- data.overheid.nl (government datasets)

## Ethical Guardrails
1. Every output MUST include disclaimer from `assets/disclaimers/`
2. Every legal statement MUST cite article/ECLI/source
3. Flag when human lawyer required (criminal liability, deadlines, vulnerable persons)
4. Warn about privileged information
5. State jurisdiction boundaries
6. Note date of last verification
