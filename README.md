# Data / Marketing / CX Analytics — Internship Portfolio

I build small, **reviewable** analytics case studies that go past KPI reporting into
modelling: a hiring manager can open one repo, read a decision-style report, and
check the code and tests behind every number.

Background in Communication Sciences and Digital Media. I use AI-assisted workflows
for research, documentation and QA, and I am explicit about data provenance — these
projects use **public** datasets or **disclosed synthetic** data, never client or
production data.

**Target internships:** Data Analyst – Customer Experience · Business Analyst ·
Marketing Analyst · Operations Analyst · AI Adoption Intern.

---

## Three projects worth your five minutes

### 1. [Regulated AI & Data Governance Cockpit](https://github.com/errer441122/regulated-ai-governance-cockpit)

AI-adoption and data-analytics case study on the **public UCI Bank Marketing** dataset,
with CI that validates every committed result.

- **Subscription-driver model** — multivariate logistic regression with Wald odds
  ratios, 95% CIs and p-values; `duration` excluded as documented target leakage;
  decision threshold selected on a validation split; held-out ROC-AUC, PR-AUC,
  calibration and cumulative-gains/lift readout.
  → [`subscription_drivers.md`](https://github.com/errer441122/regulated-ai-governance-cockpit/blob/main/digital-campaign-performance-dashboard/analysis/subscription_drivers.md)
  · [`analyze_subscription_drivers.py`](https://github.com/errer441122/regulated-ai-governance-cockpit/blob/main/digital-campaign-performance-dashboard/src/analyze_subscription_drivers.py)
- **Customer segmentation** — K-means personas with *k* chosen 4–6 by silhouette
  (the label is never used to cluster), plus a shallow decision-tree targeting
  policy with **out-of-sample lift** and a recommended action per segment.
  → [`customer_segments.md`](https://github.com/errer441122/regulated-ai-governance-cockpit/blob/main/digital-campaign-performance-dashboard/analysis/customer_segments.md)
  · [`segment_customers.py`](https://github.com/errer441122/regulated-ai-governance-cockpit/blob/main/digital-campaign-performance-dashboard/src/segment_customers.py)
- **Executive summary** written as a decision document, not a feature list.
  → [`executive_summary.md`](https://github.com/errer441122/regulated-ai-governance-cockpit/blob/main/digital-campaign-performance-dashboard/reports/executive_summary.md)

*Best fit: AI Adoption Intern · Business Analyst · Operations Analyst.*

### 2. [Industrial CX & Service Analytics Lab](https://github.com/errer441122/industrial-cx-service-analytics-lab)

Customer-experience analytics on a **disclosed synthetic** dataset (published data
card with the generative model and seed — no hidden hand-tuning).

- **Driver analysis** — two-proportion z-test (pooled), Cohen's *h* effect size,
  Wilson 95% CIs, ranked at-risk segments, plus a follow-up cohort comparison and
  comment-theme tagging.
  → [`cx_driver_analysis.md`](https://github.com/errer441122/industrial-cx-service-analytics-lab/blob/main/cx-analyst-lab/reports/cx_driver_analysis.md)
  · [`cx_driver_analysis.py`](https://github.com/errer441122/industrial-cx-service-analytics-lab/blob/main/cx-analyst-lab/src/cx_driver_analysis.py)
- **Reproducible data** — deterministic generator and a transparent data card.
  → [`generate_cx_dataset.py`](https://github.com/errer441122/industrial-cx-service-analytics-lab/blob/main/cx-analyst-lab/src/generate_cx_dataset.py)
  · [`cx_dataset_card.md`](https://github.com/errer441122/industrial-cx-service-analytics-lab/blob/main/cx-analyst-lab/data/cx_dataset_card.md)
- Behavioral tests assert the analysis *recovers the injected structure*, not brittle
  snapshots. → [`test_cx_metrics.py`](https://github.com/errer441122/industrial-cx-service-analytics-lab/blob/main/cx-analyst-lab/tests/test_cx_metrics.py)

*Best fit: Data Analyst – Customer Experience · Marketing Analyst.*

### 3. [Digital Campaign Performance Dashboard](https://github.com/errer441122/digital-campaign-performance-dashboard)

Campaign analytics with a deep dive beyond a KPI table.

- **Campaign deep dive** — variance-aware weekly trend (slope, R², coefficient of
  variation), uplift-over-time vs a baseline week, audience-segment and
  segment×channel economics with a per-segment action, and a **cross-source
  reconciliation** of the three CSVs that fails the build on a mismatch.
  → [`campaign_deep_dive.md`](https://github.com/errer441122/digital-campaign-performance-dashboard/blob/main/analysis/campaign_deep_dive.md)
  · [`campaign_deep_dive.py`](https://github.com/errer441122/digital-campaign-performance-dashboard/blob/main/src/campaign_deep_dive.py)
- **CSV formula-injection hardening** — every text cell written to the workbook is
  neutralised against spreadsheet formula/DDE injection, with tests.
  → [`build_dashboard.py`](https://github.com/errer441122/digital-campaign-performance-dashboard/blob/main/src/build_dashboard.py)
  · [`test_campaign_deep_dive.py`](https://github.com/errer441122/digital-campaign-performance-dashboard/blob/main/tests/test_campaign_deep_dive.py)

*Best fit: Marketing Analyst · Business Analyst · Operations Analyst.*

---

## What the code shows (not just the charts)

- **Leakage-aware**: target/post-outcome fields excluded; model selection on a
  validation split; results read on a held-out test split.
- **Reproducible**: fixed seeds, deterministic generators, pinned dependencies; the
  cockpit's results are re-validated in CI on every push.
- **Tested**: behavioral/range tests that check the *meaning* of the output.
- **Honest boundaries**: public vs synthetic data is stated everywhere; no causal
  claims on observational data; no client/production data.

## Recruiter routing

| If you are hiring for | Start here |
| --- | --- |
| Data Analyst – Customer Experience | CX & Service Analytics Lab → Cockpit |
| Marketing Analyst | Campaign Performance Dashboard → CX Lab |
| Business / Operations Analyst | Cockpit → Campaign Performance Dashboard |
| AI Adoption Intern | Regulated AI & Data Governance Cockpit |

## Stack

Python (pandas-free stdlib + scikit-learn / numpy) · logistic regression · K-means &
decision trees · hypothesis testing & effect sizes · Excel / Google Sheets KPI
reporting · SQL · pytest · GitHub Actions CI · AI-assisted research and documentation.

## Boundaries

All projects are portfolio case studies on **public** datasets (UCI Bank Marketing,
CC BY 4.0) or **disclosed synthetic** data with a published data card. They do not
claim access to real company, client, user, advertising, analytics or production data.
