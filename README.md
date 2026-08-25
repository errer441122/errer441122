# Marketing, CRM & Customer Experience Analytics

Hi, I'm Riccardo. I'm building this portfolio around a simple question: how can marketing and customer data help a team make a better decision?
I enjoy working across campaigns, CRM and customer experience, and I try to make every project easy to review—not just technically correct.
I'm looking for an internship or junior role where I can keep learning by working on real business questions.

## Start here

| If you are hiring for | Open first | The business question |
| --- | --- | --- |
| Performance / Digital Marketing · CRM / Marketing Automation · E-commerce | [Digital Campaign Performance Dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard) | Which campaigns, audiences and customer segments deserve attention—and how should that change budget and CRM actions? |
| Customer Experience / Customer Insights | [E-commerce CX Analytics](https://github.com/errer441122/ecommerce-cx-analytics) | What is most closely associated with a poor Olist customer experience, and where should a CX team act first? |
| AI governance / responsible AI | [Agentic Audit Reporting](https://github.com/errer441122/agentic-audit-reporting) · [live report](https://errer441122.github.io/agentic-audit-reporting/abm_compliance_report.html) | How can an AI-assisted workflow remain traceable, reviewable and subject to human approval? |

## Why I built these projects

I wanted a portfolio that shows the work, not just a list of tools. I use
public data so another person can inspect the assumptions, rerun the code
and challenge the result. Where realistic public data does not exist, I
label the simulated parts instead of presenting them as client or production
data.

The projects are not meant to pretend I have already seen every real company
setup. They are how I practise turning an open-ended question into a useful
report, while being honest about what the data can and cannot prove.

## Featured projects

### [Digital Campaign Performance Dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard)

A marketing and CRM case study connecting campaign performance to budget,
customer lifecycle and retention decisions. The CRM work uses the real UCI
*Online Retail II* dataset; campaign, attribution and consent examples are
clearly labelled deterministic simulations because an equivalent permissive
public dataset is not available.

What to open first:

- the [dashboard preview](https://github.com/errer441122/digital-campaign-performance-dashboard#dashboard-preview);
- the [executive summary](https://github.com/errer441122/digital-campaign-performance-dashboard/blob/main/reports/executive_summary.md);
- the [five-minute recruiter route](https://github.com/errer441122/digital-campaign-performance-dashboard#recruiter-5-minute-route).

### [E-commerce CX Analytics](https://github.com/errer441122/ecommerce-cx-analytics)

A customer-experience analysis of about 95,000 real reviews from the Olist
Brazilian e-commerce dataset. The clearest finding is practical: late
delivery is strongly associated with lower satisfaction. The repository
also examines other drivers, review themes and differences across customer
groups without claiming that observational relationships are causal.

What to open first:

- the [CX driver analysis](https://github.com/errer441122/ecommerce-cx-analytics/blob/main/reports/cx_driver_analysis.md);
- the [stakeholder brief](https://github.com/errer441122/ecommerce-cx-analytics/blob/main/reports/customer_satisfaction_brief.md);
- the [data provenance](https://github.com/errer441122/ecommerce-cx-analytics/blob/main/data/REAL_DATA_PROVENANCE.md).

### [Agentic Audit Reporting](https://github.com/errer441122/agentic-audit-reporting)

A small working integrity and reporting layer for AI-assisted workflows. It
records a verifiable audit trail, preserves approval decisions and produces
an EU AI Act Articles 12/13/14 report. It is intentionally scoped: this is
not presented as a complete production agent platform.

**[Open the live compliance report](https://errer441122.github.io/agentic-audit-reporting/abm_compliance_report.html)**

## Technical evidence

This detail is here for reviewers who want to inspect methods and
implementation after the business overview.

| Project | Methods and evidence | Main tools |
| --- | --- | --- |
| Digital Campaign Performance | RFM, cohort retention, historical CLV, A/B uplift, multi-touch attribution including Markov removal effect, saturation-aware budget scenarios, GA4 event planning and UTM/consent governance | Python, SQL, Excel, Power BI/Tableau/Looker specifications, pytest, GitHub Actions |
| E-commerce CX Analytics | Disclosed NPS proxy, two-proportion tests, Cohen's *h*, confidence intervals, delivery-SLA cohorts, multivariate logistic regression and Portuguese comment themes | Python standard library, real Olist review data, unit tests, GitHub Actions |
| Agentic Audit Reporting | SHA-256 hash-chained JSONL events, replay and verification, human approval records, HTML compliance reporting | Python standard library, pytest-compatible tests, GitHub Actions, GitHub Pages |

## Data boundaries

Every project uses a real public dataset with source and license information,
or clearly labelled deterministic simulation where suitable public data is
not available. Nothing here claims access to client, advertising-platform,
CRM, user or production data.

## Contact

I'm open to internship and junior opportunities in marketing analytics, CRM
and marketing automation, customer experience, e-commerce analytics and
responsible-AI governance.
