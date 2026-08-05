---
source_id: "SRC-robotics-353"
title: "RTAB-Map GitHub repository release and maintenance audit"
source_type: "code_repository_metadata"
publisher: "GitHub / IntRoLab"
source_date: "2026-08-05"
url: "https://api.github.com/repos/introlab/rtabmap"
evidence_grade: "S"
capture_method: "github-api-manual-audit"
captured_at: "2026-08-05T06:50:08+00:00"
tags:
  - raw/source
  - source-type/code-repository-metadata
  - evidence/s
aliases:
  - SRC-robotics-353
---

# RTAB-Map GitHub repository release and maintenance audit

Read-only snapshot. Dynamic counters are valid only at capture time and are not performance or support-SLA evidence.

## Repository snapshot

```json
{
  "full_name": "introlab/rtabmap",
  "created_at": "2014-08-11T18:38:14Z",
  "updated_at": "2026-08-04T09:44:28Z",
  "pushed_at": "2026-08-05T06:11:55Z",
  "stargazers_count": 3930,
  "forks_count": 949,
  "open_issues_count": 581,
  "default_branch": "master",
  "archived": false
}
```

The audited head was `bcdb4b454683efc651a36f044cc85d8f2f5f4ac3` dated 2026-08-03, with message `hotfix opencv5 compressed data compatibility`. The latest public release was `0.23.8`, published 2026-07-05. Release notes include OpenCV 5 work, ROS 2 distro CI, read-only localization, LIO-SAM/OpenVINS configuration integrations and graph/database repair work; these were not independently regression-tested here.

GitHub reported `NOASSERTION` for SPDX detection, while the pinned repository LICENSE is BSD-3-Clause text. The downloaded API body is preserved in the adjacent `.html` file.
