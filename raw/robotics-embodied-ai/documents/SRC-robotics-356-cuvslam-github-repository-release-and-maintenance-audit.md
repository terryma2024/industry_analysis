---
source_id: "SRC-robotics-356"
title: "cuVSLAM GitHub repository release and maintenance audit"
source_type: "code_repository_metadata"
publisher: "GitHub / NVIDIA"
source_date: "2026-08-05"
url: "https://api.github.com/repos/nvidia-isaac/cuVSLAM"
evidence_grade: "S"
capture_method: "github-api-manual-audit"
captured_at: "2026-08-05T06:50:08+00:00"
tags:
  - raw/source
  - source-type/code-repository-metadata
  - evidence/s
aliases:
  - SRC-robotics-356
---

# cuVSLAM GitHub repository release and maintenance audit

Read-only snapshot. Dynamic counters are contextual only.

```json
{
  "full_name": "nvidia-isaac/cuVSLAM",
  "created_at": "2024-12-19T20:40:00Z",
  "updated_at": "2026-08-05T06:10:59Z",
  "pushed_at": "2026-08-04T21:14:29Z",
  "stargazers_count": 1742,
  "forks_count": 189,
  "open_issues_count": 19,
  "default_branch": "main",
  "archived": false
}
```

The audited head was `7d2463fd8d8e5b0cf3fde94120d2570ba5f43817` dated 2026-07-28. The latest public release was `v17.0.0`, published 2026-07-23. Its release record includes packaged evaluation artifacts and author-reported KITTI KPIs for two x86/CUDA/Ubuntu configurations; this audit did not reproduce them and does not treat their FPS as portable to Jetson or a full ROS stack.

GitHub reported `NOASSERTION` for SPDX detection; the pinned repository license is the NVIDIA Community License. The downloaded API body is preserved in the adjacent `.html` file.
