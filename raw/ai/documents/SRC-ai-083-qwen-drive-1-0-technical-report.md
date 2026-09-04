---
source_id: "SRC-ai-083"
title: "Qwen-Drive-1.0 technical report"
source_type: "paper"
publisher: "Qwen Team and Huazhong University of Science and Technology"
source_date: "2026-09-03"
url: "https://arxiv.org/abs/2609.00111"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-04T01:16:43+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-ai-083
---
# Qwen-Drive-1.0 technical report

## Title:Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving

Authors:[Xin Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+X), [Zongchuang Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+Z), [Zhibo Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+Z), [Mingsheng Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+M), [Humen Zhong](https://arxiv.org/search/cs?searchtype=author&query=Zhong,+H), [Shuai Bai](https://arxiv.org/search/cs?searchtype=author&query=Bai,+S), [Du Chu](https://arxiv.org/search/cs?searchtype=author&query=Chu,+D), [Ruizhe Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+R), [Zhaohai Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Jun Tang](https://arxiv.org/search/cs?searchtype=author&query=Tang,+J), [Qiuyue Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Q), [Mingkun Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+M), [Jiazhao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+J), [Dayiheng Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+D), [Dingkang Liang](https://arxiv.org/search/cs?searchtype=author&query=Liang,+D), [Xiang Bai](https://arxiv.org/search/cs?searchtype=author&query=Bai,+X)

[View PDF](https://arxiv.org/pdf/2609.00111) [HTML (experimental)](https://arxiv.org/html/2609.00111v1)

> Abstract:We present Qwen-Drive-1.0, an initial step towards a vision-language foundation model for autonomous driving. Qwen-Drive-1.0 retains the architecture of the pretrained vision-language model (VLM) and integrates 3D perception, visual question answering, and motion planning within a unified framework. An external bird's-eye-view (BEV) perception head jointly performs 3D object detection, semantic occupancy prediction, and BEV map segmentation. It serves as a probe of the 3D information accessible from the shared representations and provides an explicit, inspectable interface to 3D scene structure. A Planning Expert conditions on shared VLM representations to generate future ego trajectories. A staged training recipe combines driving supervision with general-purpose vision-language data to acquire driving-specific competence while helping preserve broad visual understanding and instruction-following capabilities. Experiments demonstrate strong 3D perception and driving scene understanding while largely preserving general vision-language capability. Comprehensive evaluations across open-loop, pseudo-closed-loop, and closed-loop settings further show highly competitive motion-planning performance.

| Comments: |
| --- |
| Subjects: | Computer Vision and Pattern Recognition (cs.CV) |
| Cite as: | [arXiv:2609.00111](https://arxiv.org/abs/2609.00111) \[cs.CV\] |
|  | (or [arXiv:2609.00111v1](https://arxiv.org/abs/2609.00111v1) \[cs.CV\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2609.00111](https://doi.org/10.48550/arXiv.2609.00111) |

## Submission history

From: Zhibo Yang \[[view email](https://arxiv.org/show-email/5a87a7e1/2609.00111)\]
**\[v1\]** Mon, 31 Aug 2026 17:59:54 UTC (31,142 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2609.00111) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
