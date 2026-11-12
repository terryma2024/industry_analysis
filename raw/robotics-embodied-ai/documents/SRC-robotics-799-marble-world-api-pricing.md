---
source_id: "SRC-robotics-799"
title: "Marble World API pricing"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.worldlabs.ai/api/pricing"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-799
---
# Marble World API pricing

## Credits

World API billing is separate from Marble web app billing.

- Credits purchased for the Marble app at [marble.worldlabs.ai](https://marble.worldlabs.ai/) CANNOT be used with the API
- API usage requires credits purchased through the World Labs Platform at [platform.worldlabs.ai](https://platform.worldlabs.ai/)

If you plan to use the API, make sure you purchase credits on the World Labs Platform, not in the Marble app.

The World Labs API uses a credit-based pricing model.

You may purchase credits at a fixed rate of $1.00 USD per 1,250 credits through the [World Labs Platform](https://platform.worldlabs.ai/billing). The minimum purchase is 6,250 credits or $5.00 USD.

API credits do not expire.

You can check your current API credit balance with [`GET /marble/v1/credits`](https://docs.worldlabs.ai/api/reference/credits/get).

### Auto-refill

You may enable auto-refill to avoid service interruptions by automatically purchasing credits when your balance is low.

On the [billing page](https://platform.worldlabs.ai/billing), you may enable and configure auto-refill once you have a payment method on file.

You may configure the threshold at which auto-refill is triggered, as well as the target balance to refill to.

Note that when auto-refill is triggered, your balance will not settle at the target balance. This is because the refill is applied before the cost of the API request is deducted from your balance.

For example, assume your threshold is 10,000 credits and your target balance is 20,000 credits, and you have a balance of 10,000 credits.

1. You make an API request that costs 1,500 credits. We would observe that your balance would drop to 8,500 credits, which is below your threshold.
2. The auto-refill would then be triggered and you would be charged to bring your balance to 20,000 credits.
3. Finally, your balance would drop to 18,500 credits to charge for the API request.

## Usage events

Credits are consumed as you use the API.

API requests may map to one or more usage events, and each usage event may have its own cost in credits associated with it. The total cost of an API request is the sum of the costs of all the usage events it maps to. The cost of each usage event is determined largely by the compute resources required to complete the underlying operation.

You may view your usage event history in the [usage page](https://platform.worldlabs.ai/usage).

Note that not all API requests consume credits, such as API key creation, media asset upload and management, and Operation polling.

If your credit balance is too low when a request arrives, the API returns `402 Payment Required` with a response body that links to the [billing page](https://platform.worldlabs.ai/billing), where you can add credits or enable auto-refill.

### Overage

The credit check above compares your balance against a low-balance threshold. It is not a per-request cost estimate, so it does not guarantee that your remaining balance covers the request it admits. A request that starts while your balance is low can cost more credits than you have left and take your balance below zero.

Credits used beyond your prepaid balance are not refused and not written off. They become an overage. Unlike prepaid credits, which you pay for up front and draw down as you go, an overage is settled after the fact: at the end of each monthly billing period, usage your prepaid credits did not cover is converted to USD at your account’s credit rate — $1.00 USD per 1,250 credits on standard pay-as-you-go accounts, the same rate at which credits are sold — and charged to your payment method on file.

Two things about overage charges surprise people:

- **The charge arrives after the usage.** Usage in one month is invoiced at the start of the next, so a charge can land weeks after your last API request.
- **Auto-refill does not gate it.** Auto-refill only controls whether we top up your balance automatically. Turning it off does not cap your usage and does not prevent an end-of-period overage charge.

To check what an overage charge covers, compare the billing period shown on the invoice against your usage events for that period on the [usage page](https://platform.worldlabs.ai/usage).

### World generation pricing

Generating a world using the [World Generation API](https://docs.worldlabs.ai/api/reference/worlds/generate) is the most common API request. However, the number of usage events and the cost of generating a world depends on the input type.

The World Generation API requires a panorama image (pano) to convert into a 3D world, so it first generates a pano from your input if a pano is not provided. Image prompts use `is_pano: "auto"` by default; when the API detects a valid equirectangular pano, it skips pano generation. As a result, a World Generation API request often includes two usage events:

1. Pano generation (if needed)
2. World generation (from pano)

For **Marble 1.0 / `marble-1.0`** and **Marble 1.1 / `marble-1.1`**, the **world generation** usage event is billed at **1,500 credits**. Draft world generation (`marble-1.0-draft`) is billed at **150 credits**.

For **Marble 1.1 Plus / `marble-1.1-plus`**, a request always includes **1 world generation** event billed at **1,500 credits**. For larger worlds, our system may automatically determine to include up to 1,500 additional credits for variable world generation.

Depending on your input type, you may also incur a **pano generation** usage event. If you generate from an existing pano and the API treats it as a pano, there is no pano generation step, so there is no additional pano generation cost.

#### Usage event costs

| Usage event | Credits |
| --- | --- |
| Pano generation (image, pano) | 0 |
| Pano generation (text) | 80 |
| Pano generation (image, non-pano) | 80 |
| Pano generation (multi-image) | 100 |
| Pano generation (video) | 100 |
| Draft world generation | 150 |
| World generation | 1,500 |
| HQ mesh export | 3,500 |

#### Draft model totals (marble-1.0-draft)

| Input type | Pano generation | World generation | Total |
| --- | --- | --- | --- |
| Image (pano) | 0 | 150 | 150 |
| Text | 80 | 150 | 230 |
| Image (non-pano) | 80 | 150 | 230 |
| Multi-image | 100 | 150 | 250 |
| Video | 100 | 150 | 250 |

#### Standard model totals (marble-1.0, marble-1.1)

| Input type | Pano generation | World generation | Total |
| --- | --- | --- | --- |
| Image (pano) | 0 | 1,500 | 1,500 |
| Text | 80 | 1,500 | 1,580 |
| Image (non-pano) | 80 | 1,500 | 1,580 |
| Multi-image | 100 | 1,500 | 1,600 |
| Video | 100 | 1,500 | 1,600 |

#### Marble 1.1 Plus totals (marble-1.1-plus)

| Input type | Pano generation | Base world generation | Variable world generation | Total |
| --- | --- | --- | --- | --- |
| Image (pano) | 0 | 1,500 | 0-1,500 | 1,500-3,000 |
| Text | 80 | 1,500 | 0-1,500 | 1,580-3,080 |
| Image (non-pano) | 80 | 1,500 | 0-1,500 | 1,580-3,080 |
| Multi-image | 100 | 1,500 | 0-1,500 | 1,600-3,100 |
| Video | 100 | 1,500 | 0-1,500 | 1,600-3,100 |

#### Observed Marble 1.1 Plus costs

The variable world generation charge depends on the size of the world, so actual costs vary by request. The table below shows observed succeeded `marble-1.1-plus` World Generation API costs through June 25, 2026.

1,250 credits = $1.00.

| Input type | Mean | Median | P75 | P90 | P95 | P99 | Max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Image (pano) | $1.707 | $1.200 | $2.400 | $2.400 | $2.400 | $2.400 | $2.400 |
| Text | $1.600 | $1.264 | $2.224 | $2.464 | $2.464 | $2.464 | $2.464 |
| Image (non-pano) | $1.755 | $1.264 | $2.464 | $2.464 | $2.464 | $2.464 | $2.464 |
| Multi-image | $1.770 | $1.280 | $2.480 | $2.480 | $2.480 | $2.480 | $2.480 |
| Video | $1.735 | $1.280 | $2.480 | $2.480 | $2.480 | $2.480 | $2.480 |

Overall `marble-1.1-plus` costs across these input types:

- Mean: $1.714
- Median: $1.280
- P75/P90: $2.464
- P95/P99/max: $2.480

### Mesh export pricing

Exporting a high-quality mesh with the [Export API](https://docs.worldlabs.ai/api/reference/worlds/export) (`{"asset_type": "mesh", "format": "glb"}`) is billed as a single **HQ mesh export** usage event of **3,500 credits** ($2.80).

A single export run produces both mesh variants (`textured` and `vertex_colored`), so you are charged once per world, not once per variant. You are only charged when a new export run starts:

- If the world already has an exported mesh, the API returns the cached result at no cost.
- If a mesh export is already running for the world, the API returns the existing operation at no cost.

PLY splat exports (`{"asset_type": "splats", "format": "ply"}`) are free.

| Usage event | Credits |
| --- | --- |
| HQ mesh export | 3,500 |
