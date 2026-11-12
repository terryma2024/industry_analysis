---
source_id: "SRC-robotics-789"
title: "Atlas general best practices"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/best-practices.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-789
---
# Atlas general best practices

# Best practices

Choose strong inputs and design reliable world workflows.

Atlas models do especially well on worlds: spaces, environments,
architecture, landscapes, and the relationships between surfaces. They are not
yet as strong on humans or dynamic objects. Design inputs and product promises
around those limits, and test with inputs representative of your use case before
launch.

## Choose world-first inputs

- Use sharp images with a clear environment and enough visible surfaces to
  establish depth.
- Prefer wide or medium views over extreme close-ups.
- Keep exposure, white balance, and scene state consistent across views.
- Capture overlapping viewpoints with translation, not only rotation, when
  geometry or metric scale matters.
- Remove frames with blur, heavy occlusion, or unrelated locations.

Crowds, close-up people, articulated motion, vehicles in motion, water in
motion, and objects that change pose between views can reduce consistency.
People can still appear in an input, but they should not be the main
quality target.

For Gaussian splat reconstruction, see [Splat best practices](/splat-best-practices)
for scene selection, overlapping views, and examples of common artifacts.

## Build small, observable pipelines

Treat each task as one durable job:

1. Validate media and request shape locally.
2. Upload reusable or private inputs as project assets.
3. Submit once with an idempotency key.
4. Persist the operation ID.
5. Wait or poll until terminal.
6. Store output asset IDs and the input operation trace.

Do not hide several uncontrolled retries inside one product action. Expose a
job state to your application so users can leave and return while work runs.

## Preserve coordinate conventions

Camera-bearing schemas state their coordinate convention. Atlas outputs use
OpenGL/Three.js right-up-back (`rub`) unless the live schema says otherwise.
Convert once at your system boundary and test with a known camera rather than
sprinkling axis flips through rendering code.

## Protect media and secrets

- Keep API keys server-side and scope one key to one deployed service.
- Use project assets for private media.

## Pin integrations to the live contract

The public [API reference](/api-reference) is generated from
the same Atlas schemas as the service. Use it when generating clients.
Examples for the older World API v1 are not compatible with this API.

Keep schema generation and a small end-to-end request in CI. Treat
new optional fields as additive, and fail clearly if a task disappears from an
account rather than silently falling back to another model.
