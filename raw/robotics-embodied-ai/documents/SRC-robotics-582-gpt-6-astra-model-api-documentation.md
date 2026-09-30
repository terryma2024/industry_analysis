---
source_id: "SRC-robotics-582"
title: "GPT-6 Astra model API documentation"
source_type: "technical_documentation"
publisher: "OpenAI"
source_date: "2026-09-30"
url: "https://developers.openai.com/api/docs/models/gpt-6-astra"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-30T01:54:30+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-582
---
# GPT-6 Astra model API documentation

![gpt-6-astra](https://developers.openai.com/images/api/models/icons/gpt-6-astra.png)

GPT-6 Astra

Default

Our most capable model for the most demanding work.

Reasoning

Highest

Speed

Fast

Price

$10 • $50

Input• Output

Input

Text, Image

Output

Text

GPT-6 Astra is our most capable model for the most demanding work. Use it for complex reasoning, coding, computer use, research, and document creation. `reasoning.effort` supports `low`, `medium`, `high`, `xhigh`, and `max`.

Get started with GPT-6 Astra using the [model guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra).

1,050,000 context window

128,000 max output tokens

Reasoning token support

Pricing

Pricing is based on the number of tokens used, or other metrics based on the model type. For tool-specific models, like search and computer use, there’s a fee per tool call. See details in the [pricing page](https://developers.openai.com/api/docs/pricing).

Text tokens

Per 1M tokens

Input

$10.00

Cached input

$1.00

Cache writes

$12.50

Output

$50.00

Prompts with more than 272K input tokens are priced at 2x input and cache rates and 1.5x output for the full request.

Cache writes are billed at 1.25x the uncached input token rate.

Batch and Flex are priced at 50% of Standard rates. Fast mode is priced at 2x the applicable rates.

Modalities

Text

Input and output

Image

Input only

Audio

Not supported

Video

Not supported

Endpoints

Live

v1/live/sessions

Chat Completions

v1/chat/completions

Responses

v1/responses

Realtime

v1/realtime

Realtime translation

v1/realtime/translations

Realtime transcription

v1/realtime/transcription\_sessions

Assistants

v1/assistants

Batch

v1/batch

Fine-tuning

v1/fine-tuning

Embeddings

v1/embeddings

Image generation

v1/images/generations

Videos

v1/videos

Image edit

v1/images/edits

Speech generation

v1/audio/speech

Transcription

v1/audio/transcriptions

Translation

v1/audio/translations

Moderation

v1/moderations

Completions (legacy)

v1/completions

Features

Streaming

Supported

Function calling

Supported

Structured outputs

Supported

Fine-tuning

Not supported

Tools

Tools supported by this model when using the Responses API.

Web search

Supported

File search

Supported

Image generation

Supported

Code interpreter

Supported

Hosted shell

Supported

Apply patch

Supported

Skills

Supported

Computer use

Supported

MCP

Supported

Tool search

Supported

Snapshots

Snapshots let you lock in a specific version of the model so that performance and behavior remain consistent. Below is a list of all available snapshots and aliases for GPT-6 Astra.

![gpt-6-astra](https://developers.openai.com/images/api/models/icons/gpt-6-astra.png)

gpt-6-astra

gpt-6-astra

gpt-6-astra

Rate limits

Rate limits ensure fair and reliable access to the API by placing specific caps on requests, tokens, audio duration, or other usage within a given time period. Your usage tier determines how high these limits are set and automatically increases as you send more requests and spend more on the API.

<table><thead><tr><th>Tier</th><th>RPM</th><th>TPM</th><th>Batch queue limit</th></tr></thead><tbody><tr><td>Free</td><td colspan="3">Not supported</td></tr><tr><td>Tier 1</td><td>500</td><td>500,000</td><td>1,500,000</td></tr><tr><td>Tier 2</td><td>5,000</td><td>1,000,000</td><td>3,000,000</td></tr><tr><td>Tier 3</td><td>5,000</td><td>2,000,000</td><td>100,000,000</td></tr><tr><td>Tier 4</td><td>10,000</td><td>4,000,000</td><td>200,000,000</td></tr><tr><td>Tier 5</td><td>15,000</td><td>40,000,000</td><td>15,000,000,000</td></tr></tbody></table>
