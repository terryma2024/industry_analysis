---
source_id: "SRC-robotics-061"
title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
source_type: "paper"
publisher: "Physical Intelligence"
source_date: "2024"
url: "https://www.physicalintelligence.company/download/pi0.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-05-27T02:32:10+00:00"
source_markdown: "SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-061
---
# pi0: A Vision-Language-Action Flow Model for General Robot Control - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-061`
- Raw Markdown: [SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md](SRC-robotics-061-pi0-a-vision-language-action-flow-model-for-general-robot-control.md)
- Evidence grade: `S`

## Page-Level Leads

- [unpaginated] ## π 0 : A Vision-Language-Action Flow Model for General Robot Control ## Physical Intelligence Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch,
- [unpaginated] 1: Our generalist robot policy uses a pre-trained vision-language model (VLM) backbone, as well as a diverse crossembodiment dataset with a variety of dexterous manipulation tasks.

## Extracted Tables

### Table 1 (unpaginated)

where subscripts denote robot timesteps and superscripts denote flow matching timesteps, with τ ∈ [0 , 1] . Recent work in high-resolution image [14] and video [38] synthesis has shown that flow matching can achieve strong empirical performance when combined with a simple linearGaussian (or optimal transport) probability path [28], given by q ( A τ t | A t ) = N ( τ A t , (1 -τ ) I ) . In practice, the network is trained by sampling random noise ϵ ∼ N ( 0 , I ) , computing the 'noisy actions' A τ t = τ A t +(1 -τ ) ϵ , and then training the network outputs v θ ( A τ t , o t ) to match the denoising vector field u ( A τ t | A t ) = A t -ϵ . The action expert uses a full bidirectional attention mask, so that all action tokens attend to each other. During training, we sample the flow matching timestep τ from a beta distribution that emphasizes lower (noisier) timesteps. See Appendix B for more details.

### Table 2 (unpaginated)

| model part                     | inference time   |
|--------------------------------|------------------|
| image encoders                 | 14 ms            |
| observation forward pass       | 32 ms            |
| x10 action forward pass (flow) | 27 ms            |
| network latency (if off-board) | 13 ms            |
| total on-board inference       | 73 ms            |
| total off-board inference      | 86 ms            |


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
