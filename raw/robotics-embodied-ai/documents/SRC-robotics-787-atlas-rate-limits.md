---
source_id: "SRC-robotics-787"
title: "Atlas rate limits"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/rate-limits.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-787
---
# Atlas rate limits

# Rate limits

Plan for provisional Atlas capacity limits.

Atlas rate limits protect shared model capacity. This page is the
placeholder rate card; final per-task quotas and commercial
throughput tiers have not been published yet.

> Do not use values from older World API documentation for an
> Atlas capacity plan.

## Rate card

| Limit                                  | Value                    |
| -------------------------------------- | ------------------------ |
| Task submissions per minute            | To be announced          |
| Task submissions per hour              | To be announced          |
| Concurrent running tasks               | To be announced          |
| Asset and operation lifecycle requests | To be announced          |
| Higher-throughput enterprise tiers     | Available by arrangement |

Limits apply to the project or account associated with the API key, depending
on the limit. Multiple keys do not create independent capacity pools.
Available throughput can also vary with model capacity and request complexity.

Task submission rates and concurrency limits are shared between the web app,
Developer API, and API playground. Submitting through another interface does not
create a separate budget: each task type uses the same per-account limits and
service-wide capacity across all three.

## Design for limits now

Even before final numbers are published:

- queue task submissions instead of starting unbounded parallel requests;
- cap concurrency per project;
- persist accepted operation IDs;
- poll existing operations instead of resubmitting work;
- add jitter to every retry schedule;
- make throughput and backoff settings configurable.

Task completion time is not a request-rate limit. A long operation should stay
in your polling queue; do not replace it because another task completed sooner.

## Concurrency limits

Each task type also caps how many of its tasks may be open at once, counted
both per account and across the whole service. A task is open from the moment
it is accepted until its operation reaches a terminal state or passes its
deadline. A submission that finds the cap reached is refused rather than
queued. The cap is soft: submissions that arrive together can exceed it.
Request-rate and burst limits still apply.

The caps can change with available model capacity and are not published. If a
request is refused, wait for the `Retry-After` delay before submitting again.
If your account has reached its concurrency limit, wait for one of your
existing operations to finish.

## Handle 429 responses

`429 Too Many Requests` means the request was not accepted under the current
limit. The `code` field in the response body says which limit refused it.

| `code`                       | Meaning                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `RATE_LIMIT_EXCEEDED`        | Too many requests in the current window.                                                                                                         |
| `CONCURRENCY_LIMIT_EXCEEDED` | Too many open tasks of this type, for your account or for the service. `Retry-After` estimates when a slot frees; do not retry faster than that. |
| `TASK_UNAVAILABLE`           | The task is temporarily closed. Retry after the `Retry-After` value, which is a minute.                                                          |

1. Honor `Retry-After` when the response provides it.
2. Pause new submissions for that project.
3. Retry with capped exponential backoff and jitter.
4. Resume gradually instead of releasing the entire queue at once.
5. Reduce concurrency if 429s continue.

Reuse the same `Idempotency-Key` when retrying an uncertain task submission.
For a definite 429, the task was not accepted, but keeping the key stable still
makes the retry safe.

## Request higher throughput

Enterprise customers can contact their World Labs account representative with
the task methods, expected requests per minute and hour, peak concurrency,
input sizes, regions, and whether traffic is bursty or sustained. Agreed limits
should be load-tested with a representative workload before launch.
