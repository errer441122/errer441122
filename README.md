# Riccardo Capanna

Digital Marketing background (Digital Marketing BSc · 24ORE Business School) focused on **AI Search Visibility (GEO / AEO), AI Workflow Automation, Marketing & Revenue Operations, and CRM Governance**.

My work centers on the operational gaps where modern marketing stacks quietly lose visibility, pipeline speed, margin, or deliverability — designed as visual workflows (**n8n**), structured AI prompts with human-in-the-loop guardrails, platform governance matrices, and verifiable real-brand audits.

---

## Featured Systems & Case Studies

| Focus Area | Project & Live Showcase | What It Solves |
| --- | --- | --- |
| **AI Search Visibility (GEO / AEO)** | **[AI Visibility Audit — Methodology & Real-Brand Showcase](https://github.com/errer441122/ai-visibility-audit-geo)** · [Live showcase](https://errer441122.github.io/ai-visibility-audit-geo/) | Variance-aware multi-engine GEO auditing (**Gemini, OpenAI GPT, Perplexity, Claude**), Source Gap mapping, GA4/Search Console & 19-bot server-log crawler tracking. Includes a **live Notion audit readout** and a **live-verified 5-brand AI crawler `robots.txt` benchmark** *(application source code kept private)* |
| **Inbound Lead Routing & CRM Hygiene** | **[AI Inbound Lead Enrichment, ICP Scoring & HubSpot Routing](https://github.com/errer441122/ai-inbound-lead-router)** · [Interactive walkthrough](https://errer441122.github.io/ai-inbound-lead-router/) | Importable **n8n** workflow turning raw inbound form fills into clean, deduplicated, UTM-attributed **HubSpot** records & instant Tier 1 Slack alerts. It leaves contacts Sales already owns alone, filters free emails before any AI call, and adds a **Field Ownership Matrix**, an **AI confidence ≥80% human-review gate**, and 30 test cases (real domains, invented messages) |
| **Post-Purchase CX → CRM Automation** | **[CX-to-CRM AI Promo Guard & Proactive Recovery](https://github.com/errer441122/cx-crm-promo-guard)** · [Interactive walkthrough](https://errer441122.github.io/cx-crm-promo-guard/) | Importable **n8n** blueprint pausing **Klaviyo** promos & review requests for customers with a stuck parcel, a 1–2★ review, or a Zendesk ticket. Each problem writes an end date the Klaviyo segment reads, so the pause lifts by itself. Fixed pause rules, AI-drafted **Zendesk internal notes** for a human, VIP `P0` Slack escalation |
| **Email Deliverability & Sender Authentication** | **[Sender Domain Health: SPF, DKIM & DMARC Check and Monitor](https://github.com/errer441122/sender-domain-health)** · [Live checker](https://errer441122.github.io/sender-domain-health/) | **n8n** workflow that reads SPF, DKIM, DMARC and MX from public DNS, grades them with fixed rules, and alerts only when a domain gets worse or its records change. Run for real on 23 domains: of 20 Italian B2B companies, 7 leave DMARC in monitoring mode and 5 are at or past the SPF lookup limit. The live page checks any domain with the workflow's own nodes. It grew out of a hands-on **Klaviyo, Shopify & Cloudflare DNS** setup, where a dashboard showed "Verified" for a record that did not exist |

---

## Platforms & Operational Toolkit

- **Workflow Automation & AI Ops:** n8n (importable JSON blueprints, error-trigger observability, webhook orchestration), Structured LLM Prompts & JSON Output Contracts, Human-in-the-Loop confidence gates
- **CRM, ESP & E-commerce:** HubSpot (Contacts, Properties, Field Ownership, First/Last-Touch UTMs), Klaviyo (Flows, Double Opt-In, Smart Sending, Global Exclusion Segments), Shopify, DNS Authentication (SPF, DKIM, DMARC)
- **AI Search (GEO / AEO) & Analytics:** Multi-engine AI visibility auditing (ChatGPT, Gemini, Perplexity, Claude), `robots.txt` AI-crawler governance, Source Gap & Digital PR mapping, GA4, Google Search Console, server-log crawler analysis
- **Post-Purchase & Operations:** webhook designs for Zendesk, Trustpilot and AfterShip / Sendcloud (not yet run live), Slack alerting, SOP & Playbook design

---

## Operating Principles

1. **Design for failure, not just the happy path.** The workflows give each failure its own route: personal emails, duplicate contacts, records Sales already owns, unreachable websites, low AI confidence (<80%), and API errors.
2. **Code for rules, AI for judgment, people for the final word.** Fixed checks run as plain code; the AI classifies, scores and drafts internal notes. It never emails angry customers or unverified leads on its own.
3. **Say what is real and what is a test.** Real: the Klaviyo, Shopify and DNS field notes, the live GEO audits, and the sender-domain check run on 23 real domains. Tests: the lead router and the CX guard run on example payloads until a company uses them. Each repo states its limits (sample sizes, API vs. consumer chat UI, sandbox vs. live traffic).

---

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
