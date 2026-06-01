# Analytics & Governed-Agentic-AI Portfolio

I build practical, reviewable projects: a hiring manager can open one repo,
read a decision-style report, and check the code and tests behind every
number or every claim. The work runs on **real public datasets** — with
clearly-labelled deterministic simulation only where no permissive public
source exists, always behind a published data card. Never client or
production data.

Two tracks:

- **Marketing / CX / CRM analytics** — campaign performance, multi-touch
  attribution, CRM lifecycle and retention, Customer Experience.
- **Regulated, governed agentic AI** — a multi-agent workflow with
  provenance-tracked claims, a human approval gate, and an audit trail
  built for an external compliance review.

## Start here

| If you are hiring for | Open first | What it shows |
| --- | --- | --- |
| Performance / Digital Marketing · CRM / Marketing Automation · E-commerce | [Digital Campaign Performance Dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard) | Campaign deep dive + multi-touch attribution (data-driven Markov removal-effect), saturation-aware budget reallocation, A/B uplift (CI, p-value, Bayesian) — **plus** RFM → automation, cohort retention & CLV on the real UCI Online Retail II dataset, the CPA-vs-LTV bridge, GDPR consent as a hard gate |
| Customer Experience / Customer Insights | [CX & Service Analytics Lab](https://github.com/errer441122/industrial-cx-service-analytics-lab) | NPS with CI, multivariate logistic driver model, bivariate driver ranking, delivery-SLA cohort and comment themes on **~95k real Olist reviews**, SQL views + Power BI star schema |
| AI governance / responsible-AI / agentic workflows | [Agentic Audit Reporting](https://github.com/errer441122/agentic-audit-reporting) | Multi-agent ABM with Claim→Citation provenance, a human-in-the-loop approval gate, an append-only replayable audit log and an EU AI Act (Art. 12/13/14) compliance report |

## Featured projects

### Track A — Marketing / CX / CRM analytics

#### 1. [Digital Campaign Performance Dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard)

Full-funnel marketing & CRM analytics on **hybrid, fully-disclosed
data**: CRM lifecycle, cohort retention and CLV run on the **real UCI
*Online Retail II* dataset (CC BY 4.0)**; campaign, attribution and
consent use clearly-labelled deterministic simulation, because no
permissive public source exists for those. Includes a campaign deep
dive with real week-to-week variance, **multi-touch attribution**
(first/last/linear/position-based + a data-driven Markov removal-effect
model), **saturation-aware budget reallocation**, RFM → automation
flows, A/B uplift (CI, p-value, Bayesian summary), a GA4 event plan,
UTM taxonomy, Consent Mode/GDPR notes, SQL evidence and
Power BI/Tableau/Looker specs. Provenance + SHA256, CI-validated,
tested.

#### 2. [CX & Service Analytics Lab](https://github.com/errer441122/industrial-cx-service-analytics-lab)

Customer Experience analytics on the **real *Olist Brazilian
E-Commerce* dataset (Kaggle, CC BY-NC-SA 4.0, ~95k real reviews)**:
**Net Promoter Score** from a disclosed score→band proxy with a
variance-based 95% CI and NPS by state, a bivariate driver ranking
(two-proportion z-tests, Cohen's *h*, Wilson CIs, small-n floor), a
**multivariate logistic regression** giving each driver's odds ratio
controlling for the others, a delivery-SLA cohort, comment-theme
extraction from a disclosed Portuguese lexicon, plus SQL reporting
views and a stakeholder brief. Pure Python stdlib; CI re-verifies the
source checksum.

### Track B — Regulated, governed agentic AI

#### 3. [Agentic Audit Reporting](https://github.com/errer441122/agentic-audit-reporting)

A reference implementation of **regulated, audit-ready Account-Based
Marketing automation**. Four specialist agents (signal collector,
committee mapper, dossier writer, outreach drafter) coordinated by a
LangGraph supervisor. Public sources only, content-hashed at retrieval,
no purchased intent data. Every assertion is backed by a
**Claim → Citation** link; unprovenanced claims are rejected before
they reach the gate. A **human-in-the-loop approval gate** records
approve/reject/escalate decisions with rationale before any outbound
action. An **append-only, replayable JSONL audit log** exports to an
**EU AI Act (Art. 12/13/14) compliance report**. Scope is stated
honestly in-repo: the hash-chain primitive exists but is not yet wired
into the live write path and the log is not signed.

## Target roles

- CRM / Marketing Automation Intern
- Performance Marketing / Digital Marketing Analyst Intern
- Customer Experience / Customer Insights Intern
- E-commerce Analyst Intern
- Responsible-AI / AI-governance / agentic-workflow-adjacent roles

Adjacent: Marketing Analyst, Business Analyst, Web/Digital Analytics,
Market Intelligence.

## Stack

Python (stdlib + scikit-learn/numpy where useful) · multi-touch &
Markov attribution · RFM / cohort retention / CLV · NPS & CSAT ·
logistic regression, hypothesis testing & effect sizes · SQL ·
Excel / Power BI / Tableau / Looker specs · GA4 measurement planning ·
UTM governance · Consent Mode/GDPR notes · multi-agent orchestration
(LangGraph) · provenance / Claim→Citation tracking · human-in-the-loop
approval gates · append-only audit logging · EU AI Act Art. 12/13/14
documentation · reproducible validation · pytest · GitHub Actions CI.

## Boundaries

Every project runs on a **real public dataset** (with source, license
and SHA256 provenance) or, only where no permissive public source
exists, on **clearly-labelled deterministic simulation** behind a
published data card. The agentic project uses public sources only and
no purchased intent data. Nothing here claims access to real company,
client, user, advertising, CRM or production data, and in-repo scope
notes call out what is *not* yet implemented rather than overstating
it.

## Contact

Open to internship and junior opportunities in CRM/marketing
automation, performance & digital marketing analytics, customer
experience and customer insights — and to responsible-AI /
agentic-workflow-governance work.
