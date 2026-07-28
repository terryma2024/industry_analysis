---
source_id: "SRC-robotics-324"
title: "π_RL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models"
source_type: "paper"
publisher: "π_RL authors"
source_date: "2025-10-29"
url: "https://arxiv.org/abs/2510.25889"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-28T01:13:01+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-324
---
# π_RL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

## Title:π\_\\texttt{RL}: Online RL Fine-tuning for Flow-based Vision-Language-Action Models

Authors:[Kang Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+K), [Zhihao Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+Z), [Tonghe Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+T), [Zhen Guo](https://arxiv.org/search/cs?searchtype=author&query=Guo,+Z), [Si Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+S), [Hao Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+H), [Hongzhi Zang](https://arxiv.org/search/cs?searchtype=author&query=Zang,+H), [Xiang Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+X), [Quanlu Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+Q), [Zhaofei Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+Z), [Guoliang Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+G), [Tiejun Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+T), [Yu Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Y), [Chao Yu](https://arxiv.org/search/cs?searchtype=author&query=Yu,+C)

[View PDF](https://arxiv.org/pdf/2510.25889) [HTML (experimental)](https://arxiv.org/html/2510.25889v3)

> Abstract:Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\\eg, $\pi_0$, $\pi_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $\pi_{\texttt{RL}}$, featuring two technical approaches: (1) \\textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \\textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $\pi_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

| Subjects: | Machine Learning (cs.LG) |
| --- | --- |
| Cite as: | [arXiv:2510.25889](https://arxiv.org/abs/2510.25889) \[cs.LG\] |
|  | (or [arXiv:2510.25889v3](https://arxiv.org/abs/2510.25889v3) \[cs.LG\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2510.25889](https://doi.org/10.48550/arXiv.2510.25889) |

## Submission history

From: Tonghe Zhang \[[view email](https://arxiv.org/show-email/f9babfc1/2510.25889)\]  
**[\[v1\]](https://arxiv.org/abs/2510.25889v1)** Wed, 29 Oct 2025 18:37:39 UTC (1,805 KB)  
**[\[v2\]](https://arxiv.org/abs/2510.25889v2)** Thu, 27 Nov 2025 04:11:37 UTC (2,087 KB)  
**\[v3\]** Thu, 29 Jan 2026 16:00:57 UTC (3,095 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2510.25889) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
