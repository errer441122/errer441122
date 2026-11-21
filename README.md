# Riccardo Capanna

Digital Marketing background (Digital Marketing BSc · 24ORE Business School) focused on **AI Search Visibility (GEO / AEO), AI Workflow Automation, Marketing & Revenue Operations, and CRM Governance**.

My work centers on the operational gaps where marketing stacks quietly lose visibility, pipeline speed, or deliverability. I build the fixes as **n8n** workflows, with fixed rules in code, AI only where judgment is needed, and audits on real brands.

---

## Featured Systems & Case Studies

| Focus | Project | What it solves |
| --- | --- | --- |
| **AI search visibility (GEO / AEO)** | **[AI Visibility Audit](https://github.com/errer441122/ai-visibility-audit-geo)** · [live page](https://errer441122.github.io/ai-visibility-audit-geo/) | How often Gemini, GPT, Perplexity and Claude recommend a brand, and which sources they cite. Real audit: Notion on 3 engines. |
| **Lead routing & CRM hygiene** | **[AI Lead Router](https://github.com/errer441122/ai-inbound-lead-router)** · [live page](https://errer441122.github.io/ai-inbound-lead-router/) | Scores inbound leads with AI and routes them in HubSpot without overwriting Sales data or the first campaign. |
| **Email deliverability** | **[Sender Domain Health](https://github.com/errer441122/sender-domain-health)** · [live page](https://errer441122.github.io/sender-domain-health/) | Checks SPF, DKIM and DMARC from public DNS and alerts on change. 7 of 20 Italian B2B companies only monitor DMARC. |

---

## Platforms & Operational Toolkit

- **Workflow Automation & AI Ops:** n8n (importable JSON blueprints, error-trigger observability, webhook orchestration), Structured LLM Prompts & JSON Output Contracts, Human-in-the-Loop confidence gates
- **CRM, ESP & E-commerce:** HubSpot (Contacts, Properties, Field Ownership, First/Last-Touch UTMs), Klaviyo (Flows, Double Opt-In, Smart Sending, Segments), Shopify, DNS Authentication (SPF, DKIM, DMARC)
- **AI Search (GEO / AEO) & Analytics:** Multi-engine AI visibility auditing (ChatGPT, Gemini, Perplexity, Claude), `robots.txt` AI-crawler governance, Source Gap & Digital PR mapping, GA4, Google Search Console, server-log crawler analysis
- **Operations:** Slack alerting, n8n error workflows, SOP & Playbook design

---

## Operating Principles

1. **Design for failure, not just the happy path.** The workflows give each failure its own route: personal emails, duplicate contacts, records Sales already owns, unreachable websites, low AI confidence (<80%), and API errors.
2. **Code for rules, AI for judgment, people for the final word.** Fixed checks run as plain code; the AI classifies, scores and drafts an opener for a rep to review. It never emails a lead on its own.
3. **Say what is real and what is a test.** Real: the Klaviyo, Shopify and DNS field notes, the live GEO audits, and the sender-domain check run on 23 real domains. Tests: the lead router runs on example payloads until a company uses it. Each repo states its limits (sample sizes, API vs. consumer chat UI, sandbox vs. live traffic).

---

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
