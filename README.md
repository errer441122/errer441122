# Riccardo Capanna

**Marketing Automation, CRM & Martech Operations** (Digital Marketing BSc, L-20 · 24ORE Business School).

I design operational bridges between the tools modern marketing and CRM teams already pay for — covering the gaps where platforms don't talk to each other and where margin, deliverability, or ad spend quietly leak.

Every project below is a **Day-1 usable tool**: load your own unmodified CSV exports from **Shopify**, **Klaviyo**, **HubSpot**, **Meta Business**, **GA4**, **Trustpilot**, or **Zendesk**, run it locally in your browser (Pyodide — zero server upload) or via CLI, and download ready-to-import operational CSVs or warehouse SQL models.

---

## Operational Martech Toolkit

| Operational Gap Covered | Tool & Live Browser Workbench | Immediate Operational Output |
| --- | --- | --- |
| **ESP → Pre-Send QA & VIP Margin Protection** | **[ESP Pre-Flight QA, VIP Margin Guard & GDPR Gate](https://github.com/errer441122/lifecycle-automation-lab)** · [Open in browser](https://errer441122.github.io/lifecycle-automation-lab/) | PASS/FAIL template QA (Klaviyo Liquid & HubSpot HubL, required GA4 UTMs, mobile truncation, Gmail clipping), **VIP Discount Exclusion CSV**, **GDPR Double Opt-In Suppression CSV**, and Klaviyo/HubSpot lifecycle sync |
| **Ads → CRM Consent & 2nd-Order Economics** | **[Ads-to-CRM Revenue, Consent & Repeat Reconciler](https://github.com/errer441122/digital-campaign-performance-dashboard)** · [Open in browser](https://errer441122.github.io/digital-campaign-performance-dashboard/) | Campaign budget actions (`SCALE` / `FIX_DOI_LEAK` / `FIX_RETENTION` / `PAUSE_WASTE`), **SHA-256 Meta Custom Audience Seeds & Exclusions**, unconfirmed paid-lead audit, BI star-schema CSV, and **BigQuery / Snowflake / Databricks SQL** |
| **Shipments / Reviews / Tickets → CRM Promo Hold** | **[CX-to-CRM Promo Guard & Proactive Recovery Engine](https://github.com/errer441122/ecommerce-cx-analytics)** · [Open in browser](https://errer441122.github.io/ecommerce-cx-analytics/) | **Klaviyo & HubSpot Global Promo Hold / Release CSVs** (`cx_promo_hold=true/false`), deduplicated LTV-weighted Customer Care queue (`P0`–`P3`), and BI-ready **Carrier SLA Scorecard** |

---

## Day-1 Native Platform Export Support

| Ecosystem | Supported Platforms & Exports |
| --- | --- |
| **E-commerce, ESP & CRM** | **Shopify** (*Orders > Export*, *Customers > Export*), **Klaviyo** (*Lists & Segments CSV*, Liquid HTML, Bulk Import API), **HubSpot** (*Contacts*, *Deals*, *Service Hub Tickets*, HubL HTML) |
| **Advertising** | **Meta Business** (*Ads Manager CSV*, *Lead Center / Instant Forms UTF-16/CSV*, SHA-256 Custom & Exclusion Audiences) |
| **Web & Product Analytics** | **GA4** (*Traffic / User Acquisition CSV* & UTM taxonomy cross-check), adapter support for **Amplitude**, **Mixpanel**, and **Adobe Analytics** |
| **Post-Purchase CX & Helpdesk** | **Trustpilot Business**, **Judge.me / Yotpo**, **Zendesk Support**, **AfterShip / Sendcloud / ShippyPro / Qapla'** |
| **Data Warehouse & BI** | **Google BigQuery**, **Snowflake**, **Databricks Delta** (portable SQL models) · BI-ready flat/star-schema exports for **Power BI**, **Tableau**, and **Looker** · B2B pipeline reconciliation modeled on **Dreamdata / HockeyStack** |

---

## Core Design Principles

1. **Actionable operational metrics, not academic exercises.** No public toy datasets (no UCI, no Olist) and no retrospective statistical models that teams never act on. Every calculation produces a concrete list, exclusion segment, budget tag, or blocking QA check.
2. **Protect margin, deliverability, and ad spend.** Stop sending promo codes to VIP full-price buyers, stop mailing unconfirmed single opt-in leaks or 365-day unengaged contacts (<0.3% Google/Yahoo complaint rule), stop scaling campaigns on vanity CPL, and stop sending DEM blasts to customers waiting on a stuck parcel or an open support ticket.
3. **Privacy-first by architecture.** All browser apps execute pure Python locally via Pyodide — customer emails and order exports never leave the user's machine, and every CSV export neutralizes spreadsheet formula injection.

---

## Transparency on Scope & Build Approach

- **Schema fixtures vs. client data:** The small CSV files inside each repository's `fixtures/` folder use synthetic `example.com` addresses solely to verify native platform parsers, edge cases (Excel semicolons, UTF-16 Meta exports, decimal commas), and automated CI test suites. None of the repositories claim fake campaign performance or client case studies.
- **Hands-on platform QA:** Real DNS authentication (DKIM/DMARC), Klaviyo flow testing, and platform edge cases discovered in a live Klaviyo + Shopify sandbox (Smart Sending suppressing abandoned-cart sends, Shopify checkout checkboxes bypassing Double Opt-In, DNS wildcard false positives) are documented in [`lifecycle-automation-lab/docs/field-notes/`](https://github.com/errer441122/lifecycle-automation-lab/tree/main/docs/field-notes).
- **AI-assisted workflow:** My domain role covers Martech architecture, platform data schemas, GDPR/deliverability governance rules, business logic, and QA validation; I leverage AI coding assistants to accelerate Python/SQL implementation and automated test coverage.

---

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
