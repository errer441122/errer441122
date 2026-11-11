# Riccardo Capanna

Hi, I'm Riccardo. I build and run marketing and CRM projects. This page
separates what I have set up and run on real accounts from what is practice on
public data.

## Run on real accounts

**[Lifecycle Automation Lab](https://github.com/errer441122/lifecycle-automation-lab)**

Three Klaviyo flows on a Shopify development store: welcome with double opt-in,
abandoned cart and win-back. I authenticated the sending domain (NS delegation,
DKIM, DMARC) and wrote the script that turns order history into the segment the
win-back triggers on.

It proves the mechanism, not a result: one subscriber, three delivered emails,
no sales. The useful part is
[what broke when the flows were actually sent](https://github.com/errer441122/lifecycle-automation-lab/blob/main/reports/results.md):

- Smart Sending silently skipped the first abandoned-cart email, because a
  welcome email had gone out five hours earlier.
- A sign-up through Shopify's newsletter field landed in Klaviyo as subscribed
  with no confirmation, even though the list was set to double opt-in.
- A "Verified" DNS check in the ESP turned out to be another owner's wildcard
  record.

## Practice on public data

**[CRM retention analysis](https://github.com/errer441122/digital-campaign-performance-dashboard)** · [live dashboard](https://errer441122.github.io/digital-campaign-performance-dashboard/)

RFM segments, cohort retention and customer value on the UCI *Online Retail II*
dataset (5,878 customers). Champions are 26% of customers and 71% of revenue.
It is an exercise on a public dataset, not client work. Its lifecycle
thresholds are the ones the Klaviyo win-back uses.

## Archived

Earlier exercises, kept for reference:

- [E-commerce CX analytics](https://github.com/errer441122/ecommerce-cx-analytics):
  what drives low review scores in the public Olist dataset.
- [Agentic audit reporting](https://github.com/errer441122/agentic-audit-reporting):
  a tamper-evident log for AI-assisted workflows.

## How I built these

I used AI coding assistants as a pair programmer: they drafted most of the code
and documentation. My part was choosing the questions and the data, setting up
and running the accounts, checking results against the source and deciding what
to report, including what did not work.

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
