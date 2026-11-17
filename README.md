# Riccardo Capanna

Hi, I'm Riccardo. I study Digital Marketing (bachelor's degree, class L-20, and
24ORE Business School) and I am looking for my first role: an internship or a
junior position in CRM, marketing automation or digital marketing.

I have no work experience yet. What I have is practice. I like understanding
how customer data and automated flows help a team decide who to talk to, when,
and with which message. These three projects are how I practise that.

## Start here

| If you are hiring for | Open this project | The business question |
| --- | --- | --- |
| CRM / Marketing Automation | [Lifecycle Automation Lab](https://github.com/errer441122/lifecycle-automation-lab) | Which customer gets which email, and when? Is every template safe to send, and can every subscriber's consent be proven? |
| Performance / Digital Marketing | [CRM retention practice](https://github.com/errer441122/digital-campaign-performance-dashboard) · [live page](https://errer441122.github.io/digital-campaign-performance-dashboard/) | Which customers bring the revenue, who is about to leave, and what should each group receive? |
| Customer Experience / Insights | [E-commerce CX Analytics](https://github.com/errer441122/ecommerce-cx-analytics) | Why do customers leave bad reviews, and where should the team act first? |

## The projects in short

### [Lifecycle Automation Lab](https://github.com/errer441122/lifecycle-automation-lab)

Three email flows in Klaviyo on a Shopify test store (welcome with double
opt-in, abandoned cart, win-back), plus three tools that run on the files any
Shopify + Klaviyo team already has:

- **Pre-send check** for email templates: a greeting that reads "Ciao ,", dead
  links, broken UTMs, a missing unsubscribe link, a subject cut off on a phone.
  Its first run found a problem in all seven of my live emails.
- **Lifecycle sync** from a Shopify orders export to Klaviyo, only for people
  whose consent has a recorded source and date. Everyone else goes to a
  suppression list, with the reason.
- **Second-order timing**: how many customers buy again by day 30, 60, 90, 180
  and 365, which sets the delay of the post-purchase email.

The store has no real customers, so there are no sales results. What I learned
came from running the flows:

- Smart Sending silently skipped the first abandoned-cart email, because a
  welcome email had gone out a few hours earlier.
- A sign-up through Shopify's newsletter checkbox entered the list without
  confirmation, even though the list was set to double opt-in.

### [CRM retention practice](https://github.com/errer441122/digital-campaign-performance-dashboard)

RFM segmentation, lifecycle stages and repeat purchases on a public dataset of
5,878 customers of a UK online shop. The main finding: 26% of customers bring
71% of revenue, and 588 customers are in the window where a win-back still
makes sense. Of the customers with a full year of data, half of those who came
back did so within 71 days. The dataset has no advertising data, so this is
about customers, not campaigns.

The same report runs on any store's Shopify orders export: the page, plus a
customer list with the segment, lifecycle stage and action for each person.
On the 36,969 real orders of the dataset it reproduces every published number
exactly.

### [E-commerce CX Analytics](https://github.com/errer441122/ecommerce-cx-analytics)

About 95,000 customer reviews from a public Brazilian marketplace dataset. The
main finding: when an order arrives on time, 83% of customers are satisfied;
when it arrives late, 27% are.

Two tools turn that into a daily routine on a store's own exports: the list of
late orders not delivered yet (to contact first and to keep out of promotions),
with the late rate by carrier, and a triage of 1-2 star reviews by urgency and
by the team that should handle them. On the real Olist comments the triage
queues 9,191 reviews and finds 2,080 orders that never arrived.

## What I work with

- **Klaviyo**: flows, segments, double opt-in lists, sending-domain setup.
- **Shopify**: store setup, products, test orders, the Klaviyo integration.
- **Marketing and CRM metrics**: RFM segmentation, cohort retention, conversion
  and satisfaction rates, consent management (double opt-in, GDPR).
- **Excel** for tables and summaries.

## What these projects are, honestly

- The Klaviyo account, the Shopify store and the sending domain are real, but
  the store is a test store. There are no real customers and no sales.
- The two analysis projects use public datasets that many people practise on.
  Their tools run on a store's own exports, but have not been used on a real
  client's data yet.
- None of this is client work.
- I am not a developer. The code in these repositories was written mostly by
  AI coding assistants. My part was choosing the questions and the data,
  setting up and running the accounts, checking the results and deciding what
  to report, including what did not work.

## Contact

[LinkedIn](https://www.linkedin.com/in/riccardo-capanna-039a43415/)
