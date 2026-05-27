---
source_id: "SRC-robotics-063"
title: "RoboBrain 2.0 Technical Report"
source_type: "paper"
publisher: "arXiv/BAAI"
source_date: "2025-07-02"
url: "https://arxiv.org/abs/2507.02029"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-05-27T01:34:04+00:00"
tags:
  - raw/source
  - source-type/paper
  - evidence/s
aliases:
  - SRC-robotics-063
---
# RoboBrain 2.0 Technical Report

## Title:RoboBrain 2.0 Technical Report

Authors:[BAAI RoboBrain Team](https://arxiv.org/search/cs?searchtype=author&query=BAAI+RoboBrain+Team): [Mingyu Cao](https://arxiv.org/search/cs?searchtype=author&query=Cao,+M), [Huajie Tan](https://arxiv.org/search/cs?searchtype=author&query=Tan,+H), [Yuheng Ji](https://arxiv.org/search/cs?searchtype=author&query=Ji,+Y), [Xiansheng Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+X), [Minglan Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+M), [Zhiyu Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+Z), [Zhou Cao](https://arxiv.org/search/cs?searchtype=author&query=Cao,+Z), [Pengwei Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+P), [Enshen Zhou](https://arxiv.org/search/cs?searchtype=author&query=Zhou,+E), [Yi Han](https://arxiv.org/search/cs?searchtype=author&query=Han,+Y), [Yingbo Tang](https://arxiv.org/search/cs?searchtype=author&query=Tang,+Y), [Xiangqi Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+X), [Wei Guo](https://arxiv.org/search/cs?searchtype=author&query=Guo,+W), [Yaoxu Lyu](https://arxiv.org/search/cs?searchtype=author&query=Lyu,+Y), [Yijie Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+Y), [Jiayu Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+J), [Mengfei Du](https://arxiv.org/search/cs?searchtype=author&query=Du,+M), [Cheng Chi](https://arxiv.org/search/cs?searchtype=author&query=Chi,+C), [Mengdi Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+M), [Xiaoshuai Hao](https://arxiv.org/search/cs?searchtype=author&query=Hao,+X), [Junkai Zhao](https://arxiv.org/search/cs?searchtype=author&query=Zhao,+J), [Xiaojie Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+X), [Shanyu Rong](https://arxiv.org/search/cs?searchtype=author&query=Rong,+S), [Huaihai Lyu](https://arxiv.org/search/cs?searchtype=author&query=Lyu,+H), [Zhengliang Cai](https://arxiv.org/search/cs?searchtype=author&query=Cai,+Z), [Yankai Fu](https://arxiv.org/search/cs?searchtype=author&query=Fu,+Y), [Ning Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+N), [Bolun Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+B), [Lingfeng Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+L), [Shuyi Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+S), [Dong Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+D), [Xi Feng](https://arxiv.org/search/cs?searchtype=author&query=Feng,+X), [Songjing Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+S), [Xiaodan Liu](https://arxiv.org/search/cs?searchtype=author&query=Liu,+X), [Yance Jiao](https://arxiv.org/search/cs?searchtype=author&query=Jiao,+Y), [Mengsi Lyu](https://arxiv.org/search/cs?searchtype=author&query=Lyu,+M), [Zhuo Chen](https://arxiv.org/search/cs?searchtype=author&query=Chen,+Z), [Chenrui He](https://arxiv.org/search/cs?searchtype=author&query=He,+C), [Yulong Ao](https://arxiv.org/search/cs?searchtype=author&query=Ao,+Y), [Xue Sun](https://arxiv.org/search/cs?searchtype=author&query=Sun,+X), [Zheqi He](https://arxiv.org/search/cs?searchtype=author&query=He,+Z), [Jingshu Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+J), [Xi Yang](https://arxiv.org/search/cs?searchtype=author&query=Yang,+X), [Donghai Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+D), [Kunchang Xie](https://arxiv.org/search/cs?searchtype=author&query=Xie,+K), [Bochao Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+B), [Shaokai Nie](https://arxiv.org/search/cs?searchtype=author&query=Nie,+S), [Chunlei Men](https://arxiv.org/search/cs?searchtype=author&query=Men,+C), [Yonghua Lin](https://arxiv.org/search/cs?searchtype=author&query=Lin,+Y), [Zhongyuan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Tiejun Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+T), [Shanghang Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+S)

[View PDF](https://arxiv.org/pdf/2507.02029) [HTML (experimental)](https://arxiv.org/html/2507.02029v5)

> Abstract:We introduce RoboBrain 2.0, our latest generation of embodied vision-language foundation models, designed to unify perception, reasoning, and planning for complex embodied tasks in physical environments. It comes in two variants: a lightweight 7B model and a full-scale 32B model, featuring a heterogeneous architecture with a vision encoder and a language model. Despite its compact size, RoboBrain 2.0 achieves strong performance across a wide spectrum of embodied reasoning tasks. On both spatial and temporal benchmarks, the 32B variant achieves leading results, surpassing prior open-source and proprietary models. In particular, it supports key real-world embodied AI capabilities, including spatial understanding (e.g., affordance prediction, spatial referring, trajectory forecasting) and temporal decision-making (e.g., closed-loop interaction, multi-agent long-horizon planning, and scene graph updating). This report details the model architecture, data construction, multi-stage training strategies, infrastructure and practical applications. We hope RoboBrain 2.0 advances embodied AI research and serves as a practical step toward building generalist embodied agents. The code, checkpoint and benchmark are available at [this https URL](https://superrobobrain.github.io/).

| Subjects: | Robotics (cs.RO) |
| --- | --- |
| Cite as: | [arXiv:2507.02029](https://arxiv.org/abs/2507.02029) \[cs.RO\] |
|  | (or [arXiv:2507.02029v5](https://arxiv.org/abs/2507.02029v5) \[cs.RO\] for this version) |
|  | [https://doi.org/10.48550/arXiv.2507.02029](https://doi.org/10.48550/arXiv.2507.02029) |

## Submission history

From: Yuheng Ji \[[view email](https://arxiv.org/show-email/79262d37/2507.02029)\]  
**[\[v1\]](https://arxiv.org/abs/2507.02029v1)** Wed, 2 Jul 2025 17:05:33 UTC (28,858 KB)  
**[\[v2\]](https://arxiv.org/abs/2507.02029v2)** Sat, 5 Jul 2025 07:29:07 UTC (28,858 KB)  
**[\[v3\]](https://arxiv.org/abs/2507.02029v3)** Tue, 15 Jul 2025 03:44:05 UTC (28,858 KB)  
**[\[v4\]](https://arxiv.org/abs/2507.02029v4)** Wed, 6 Aug 2025 03:41:42 UTC (29,057 KB)  
**\[v5\]** Sun, 14 Sep 2025 06:49:43 UTC (29,057 KB)

[Which authors of this paper are endorsers?](https://arxiv.org/auth/show-endorsers/2507.02029) | Disable MathJax ([What is MathJax?](https://info.arxiv.org/help/mathjax.html))
