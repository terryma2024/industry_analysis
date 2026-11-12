---
source_id: "SRC-robotics-786"
title: "Atlas billing"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/billing.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-786
---
# Atlas billing

# Billing

Understand credits, projects, spend limits, and payments.

Atlas Developer API usage is billed to the account that owns the API key's
project. Balances, top-ups, and monthly spend limits are under
[Settings → Developer Platform](https://atlas.worldlabs.ai/settings/credits/developer). Payment methods and
invoices are under [Settings → Billing](https://atlas.worldlabs.ai/settings/billing). Account usage is on the
[Settings → Usage](https://atlas.worldlabs.ai/settings/usage/developer) page.

## Credits and top-ups

Developer API tasks draw credits from the account balance. The current
conversion is 1,000 credits per US dollar. Credits purchased for the account
do not expire.

Account owners and billing owners can add credits manually or enable automatic
recharge. Auto-recharge charges the account's default payment method when the
balance falls below a configured threshold and restores it to the chosen
balance.

The task rate card can change. Use the current rate card shown in
the platform when estimating task costs rather than embedding model prices in
client code.

## Frameboy sessions

A Frameboy session in Atlas Studio runs for up to a minute and costs 500
credits ($0.50), charged once, after it ends. It draws on the same credits as
other Studio work. A session is free if it plays for less than 5 seconds, or if
it ends because its server stopped responding.

An account without enough credits cannot start a session: the request returns
`402 Payment Required` with `code` set to `CREDITS_UNAVAILABLE`, and no session
is started or queued. A charge can take a few minutes to appear on the Usage
page.

## Studio tools

Prompt enhancement costs 20 credits ($0.02) a request. An image edit costs 125
credits ($0.125) a request. An image upscale costs 10 credits ($0.01) an image.
A Chisel caption costs 20 credits ($0.02) a request. A Relight image edit costs
what the model provider charged for it, converted to credits.

## Projects and attribution

Create projects to separate credentials, assets, operations, and usage for
different environments or products. Every API key is bound to one project, so
usage is attributed without sending a project ID in each Developer API route.

Project isolation is useful even when one account funds all work:

- production and development can use different keys;
- teams can inspect their own usage;
- experiments can receive a tighter budget;
- a compromised key cannot access another project's resources.

## Usage

The Usage page shows the credits the account spent over a date range, per day
and grouped by task or project. Developer API usage can also be grouped by API
key. Studio and Developer usage are shown separately. Select a day to see its
breakdown. Usage reflects billed charges; a finished task can take a few
minutes to appear.

## Set monthly spend limits

Account owners and billing owners can create a monthly USD spend limit for the
entire account or for one project. Limits reset each calendar month.

When an enabled applicable limit reaches 100%, new Developer API tasks pause.
Tasks already running are allowed to finish. Raising, disabling, or deleting
the limit allows new tasks once the account also has sufficient credits.

Use an account-wide limit for the total safety ceiling, then add project limits
for workloads that need independent guardrails. A project task must satisfy
both limits when both apply.

> Spend limits are guardrails, not exact real-time accounting boundaries.
> In-flight work and delayed usage observations can produce some variance.

## Payment methods and invoices

The account uses one shared Stripe payment profile for API credit purchases,
automatic recharge, and Atlas Studio subscriptions. Account owners and
billing owners can add a payment method, choose the default, open the Stripe
customer portal, and review invoices from the billing page.

Do not put payment operations in an API integration. Billing administration
uses the authenticated platform session and account permissions, not a World
Labs API key.

## When work is paused

If a task is rejected because the account is out of credits or a spend limit is
reached, the response is `402 Payment Required` with `code` set to
`CREDITS_UNAVAILABLE` or `SPEND_LIMIT_EXCEEDED`:

1. Do not retry in a tight loop.
2. Check the API key's project limit and the account-wide limit.
3. Add credits or adjust the appropriate limit.
4. Retry the same logical submission with its original idempotency key.
