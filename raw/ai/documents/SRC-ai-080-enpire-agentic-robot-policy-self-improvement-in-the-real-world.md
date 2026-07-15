---
source_id: "SRC-ai-080"
title: "ENPIRE Agentic Robot Policy Self-Improvement in the Real World"
source_type: "paper"
publisher: "NVIDIA / CMU / UC Berkeley"
source_date: "2026-06-18"
url: "https://arxiv.org/abs/2606.19980"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-15T01:03:13+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-ai-080
---
# ENPIRE Agentic Robot Policy Self-Improvement in the Real World

## Title:ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

Authors:[Wenli Xiao](https://arxiv.org/search/cs?searchtype=author&query=Xiao,+W), [Jia Xie](https://arxiv.org/search/cs?searchtype=author&query=Xie,+J), [Tonghe Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+T), [Haotian Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+H), [Letian "Max" Fu](https://arxiv.org/search/cs?searchtype=author&query=Fu,+L+%22), [Haoru Xue](https://arxiv.org/search/cs?searchtype=author&query=Xue,+H), [Jalen Lu](https://arxiv.org/search/cs?searchtype=author&query=Lu,+J), [Yi Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Y), [Cunxi Dai](https://arxiv.org/search/cs?searchtype=author&query=Dai,+C), [Zi Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Jimmy Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+J), [Guanzhi Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+G), [S. Shankar Sastry](https://arxiv.org/search/cs?searchtype=author&query=Sastry,+S+S), [Ken Goldberg](https://arxiv.org/search/cs?searchtype=author&query=Goldberg,+K), [Linxi "Jim" Fan](https://arxiv.org/search/cs?searchtype=author&query=Fan,+L+%22), [Yuke Zhu](https://arxiv.org/search/cs?searchtype=author&query=Zhu,+Y), [Guanya Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+G)

[View PDF](https://arxiv.org/pdf/2606.19980) [HTML (experimental)](https://arxiv.org/html/2606.19980v1)

> Abstract:Achieving dexterous robotic manipulation in the real world heavily relies on human supervision and algorithm engineering, which becomes a central bottleneck in the pursuit of general physical intelligence. Although emerging coding agents can generate code to automate algorithm search, their successes remain largely confined in digital environments. We conjecture that the missing abstraction to automate robotics research is a repeatable feedback loop for real-world policy improvement: reset the scene, execute a policy, verify the outcome, and refine the next iteration. To bridge this gap, we introduce ENPIRE, a harness framework for coding agents that instantiates this physical feedback routine with four core modules: an Environment module (EN) for automatic reset and verification, a Policy Improvement module (PI) that launches policy refinement, a Rollout module (R) to evaluate policies with one or multiple physical robots operating in parallel, and an Evolution module (E) in which coding agents analyze logs, consult literature, improve training infrastructure and algorithm code to address failure modes. This closed-loop system transforms real-world manipulation learning into a controllable optimization procedure, minimizing human effort while allowing fair ablations across training recipe and agent variants. Powered by ENPIRE, frontier coding agents can autonomously train a policy to achieve a 99% success rate on challenging, dexterous manipulation tasks, such as organizing a pin box, fastening a zip tie, and tool use, a process that further accelerates when we dispatch an agent team on a robot fleet. Our results suggest a practical and scalable path toward deploying coding agents to autonomously advancing robotics in the physical world.

| Subjects: | Artificial Intelligence (cs.AI) |
| --- | --- |
| Cite as: | [arXiv:2606.19980](https://arxiv.org/abs/2606.19980) \[cs.AI\] |
|  | (or [arXiv:2606.19980v1](https://arxiv.org/abs/2606.19980v1) \[cs.AI\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2606.19980](https://doi.org/10.48550/arXiv.2606.19980) |

## Submission history

From: Tonghe Zhang \[[view email](https://arxiv.org/show-email/1a32fb57/2606.19980)\]
**\[v1\]** Thu, 18 Jun 2026 09:21:27 UTC (38,522 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2606.19980) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
