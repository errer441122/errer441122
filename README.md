# Riccardo Capanna

Digital Marketing background (Digital Marketing BSc · 24ORE Business School) focused on **Marketing & Revenue Operations, CRM Governance, AI Workflow Automation (n8n), and AI Search Visibility (GEO / AEO)**.

My work centers on the operational gaps between tools where B2B teams quietly lose attribution, deliverability, consent compliance, or pipeline speed. I use **n8n** for workflow automation and **Excel** (macro-free) for attribution reconciliation — fixed rules first, AI only where reading unstructured text adds value, and real audits whenever public data is available.

---

## Featured Systems & Case Studies

| Focus | Project | What it solves |
| --- | --- | --- |
| **Email deliverability & DNS** | **[Sender Domain Health](https://github.com/errer441122/sender-domain-health)** · [live page](https://errer441122.github.io/sender-domain-health/) | Checks SPF, DKIM and DMARC from public DNS and alerts on change. No AI. Executed on 23 real domains (7 of 20 Italian B2B companies only monitor DMARC). |
| **B2B pre-send gate & AI triage** | **[B2B Pre-Send Hold & Triage](https://github.com/errer441122/ecommerce-cx-analytics)** · [live page](https://errer441122.github.io/ecommerce-cx-analytics/) | Cross-checks recipients, consents, support tickets and ERP orders before a B2B send; holds the whole company by VAT/domain. AI reads only uncategorised tickets and can hold, never pass. 48 dirty cases + 48,000 random recipients, run in n8n 2.48.7. *(IT · EN summary)* |
| **Campaign-to-order attribution** | **[B2B Campaign-to-Order Reconciliation](https://github.com/errer441122/digital-campaign-performance-dashboard)** · [live page](https://errer441122.github.io/digital-campaign-performance-dashboard/) | Macro-free Excel workbook matching campaign leads, CRM contacts and ERP orders with 8 fixed rules (VAT/domain matching, credit notes, existing vs. new accounts, 180-day window) and routing edge cases to named owners. 60 dirty cases, 368 checks. *(IT · EN summary)* |
| **AI search visibility (GEO / AEO)** | **[AI Visibility Audit](https://github.com/errer441122/ai-visibility-audit-geo)** · [live page](https://errer441122.github.io/ai-visibility-audit-geo/) | Measures how often Gemini, GPT, Perplexity and Claude recommend a brand and which sources they cite. Real audit: Notion across 3 engines + 5-brand `robots.txt` benchmark. |
| **Lead routing & CRM hygiene** | **[AI Inbound Lead Router](https://github.com/errer441122/ai-inbound-lead-router)** · [live page](https://errer441122.github.io/ai-inbound-lead-router/) | Scores inbound leads with AI and routes them in HubSpot without overwriting Sales-owned records or first-touch campaign UTMs. 12 routing scenarios verified in n8n 2.48.7 + 30-case benchmark rubric. |
| **Lifecycle email & consent** | **[Klaviyo Lifecycle Lab](https://github.com/errer441122/klaviyo-lifecycle-lab)** · [live page](https://errer441122.github.io/klaviyo-lifecycle-lab/) | Welcome (double opt-in), abandoned cart and win-back flows sent for real on a Shopify dev store, plus browser-runnable pre-send QA, consent-gated lifecycle sync and repeat-timing tools. One test subscriber, no sales: proves the mechanism, not commercial results. |

> *Repository naming note:* the URLs `ecommerce-cx-analytics` and `digital-campaign-performance-dashboard` are kept unchanged so existing CV links remain valid; both repositories include their original public-dataset CV analyses under `analisi-cv/` alongside the newer B2B operational systems.

---

## Platforms & Operational Toolkit

- **Workflow Automation & AI Ops:** n8n (importable JSON workflows, error-trigger observability, webhook & form orchestration), Structured LLM Prompts & JSON Output Contracts, Human-in-the-Loop gates (AI holds or drafts, never auto-sends)
- **CRM, Attribution & Deliverability:** HubSpot (Contacts, Properties, Field Ownership, First/Last-Touch UTMs), B2B Campaign-to-ERP Reconciliation (Excel, no macros), GDPR Consent & Suppression Logic, DNS Authentication (SPF, DKIM, DMARC), Klaviyo & Shopify
- **AI Search (GEO / AEO) & Analytics:** Multi-engine AI visibility auditing (ChatGPT, Gemini, Perplexity, Claude), `robots.txt` AI-crawler governance, Source Gap & Digital PR mapping, GA4, Google Search Console
- **Operations:** Slack alerting, n8n error workflows, Trade-Show & Event Desk Operations, SOP & Playbook design

---

## Operating Principles

1. **Design for dirty data and failure, not the happy path.** Each project tests the failures of its own process: broken dates, duplicates, VAT/domain mismatches, conflicting consents across tools, Sales-owned records, unreachable websites, low AI confidence or missing exports.
2. **Fixed rules first, AI only for judgment, humans for the final call.** Deterministic checks run in Excel formulas or plain code; AI reads unstructured text only where fixed rules stop, and can never auto-approve an email send or overwrite Sales data.
3. **Say clearly what is real and what is simulated.** Real: live DNS checks on 23 real domains, live GEO audits, and Klaviyo/Shopify/DNS field notes. Simulated (and explicitly labelled): the B2B attribution (60 dirty cases / 368 checks), B2B pre-send gate (48 dirty cases / 48,000 random recipients), lead router (30 cases), and event workbooks. Every repo states its limits.

---

## Other Operational Tools & Reference Analyses

- **B2B Event Operations — [Stand Appointments & Event Follow-Up](https://github.com/errer441122/eventi-b2b-agenda-e-follow-up)** *(IT · EN summary)*: Two macro-free Excel workbooks for trade shows and open days — reschedule booth visits without losing the original booking, track pending notifications, and split post-event leads across Sales, Events, CRM Review and Excluded.
- **Retail RFM, Cohorts & CLV (5,878 customers, UCI Online Retail II):** preserved inside [digital-campaign-performance-dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard#lanalisi-del-mio-cv) · [interactive report](https://errer441122.github.io/digital-campaign-performance-dashboard/analysis.html)
- **Delivery-Delay CX Driver Analysis (95,639 reviews, Olist):** preserved inside [ecommerce-cx-analytics](https://github.com/errer441122/ecommerce-cx-analytics#lanalisi-del-mio-cv)

---

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
