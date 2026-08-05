---
source_id: "SRC-robotics-340"
title: "ORB-SLAM3 GitHub repository and maintenance audit"
source_type: "code_repository_metadata"
publisher: "GitHub / UZ-SLAMLab"
source_date: "2026-08-05"
url: "https://api.github.com/repos/UZ-SLAMLab/ORB_SLAM3"
evidence_grade: "S"
capture_method: "github-api-manual-audit"
captured_at: "2026-08-05T06:09:12+00:00"
tags:
  - raw/source
  - source-type/code-repository-metadata
  - evidence/s
aliases:
  - SRC-robotics-340
---

# ORB-SLAM3 GitHub repository and maintenance audit

This time-stamped source records a read-only audit of the official GitHub repository. Dynamic counters are evidence only for the capture date and are not performance, adoption, or support-SLA evidence.

## Repository API snapshot

Endpoint: `https://api.github.com/repos/UZ-SLAMLab/ORB_SLAM3`

```json
{
  "full_name": "UZ-SLAMLab/ORB_SLAM3",
  "created_at": "2020-07-18T07:47:46Z",
  "updated_at": "2026-08-04T11:27:45Z",
  "pushed_at": "2024-07-24T08:41:52Z",
  "stargazers_count": 8908,
  "forks_count": 3141,
  "open_issues_count": 571,
  "default_branch": "master",
  "license": "GPL-3.0",
  "archived": false,
  "disabled": false
}
```

`open_issues_count` includes pull requests. The public repository UI separately showed 541 issues and 30 pull requests, summing to 571.

## Default-branch head and recent commits

Endpoint: `https://api.github.com/repos/UZ-SLAMLab/ORB_SLAM3/commits?per_page=5`

| SHA | Committer date (UTC) | Message |
|---|---|---|
| `4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4` | 2022-02-10 | Update Dependencies.md |
| `851db0834784` | 2021-12-22 | Update README.md |
| `0df83dde1c85` | 2021-12-22 | V1.0: 22nd December 2021 |

The repository also exposes a `c++14_comp` branch, while `master` remains the default branch. The top-level tree contains `Examples`, `Examples_old`, `build.sh`, `build_ros.sh`, `Calibration_Tutorial.pdf`, `Dependencies.md`, `Thirdparty`, `Vocabulary`, `include`, and `src`.

## Latest release

Endpoint: `https://api.github.com/repos/UZ-SLAMLab/ORB_SLAM3/releases/latest`

```json
{
  "tag_name": "v1.0-release",
  "published_at": "2021-12-22T13:15:16Z",
  "commit": "0df83dde1c85"
}
```

The release notes report 16% average tracking speed-up and 19% average mapping speed-up relative to the paper timing, a new calibration format, stereo rectification and image resizing options, map load/save, Intel RealSense live examples, and bug fixes. These are maintainer-reported release claims and were not independently benchmarked in this audit.

## Interpretation boundary

- Stable default-branch and release dates indicate a mature but largely frozen upstream, not necessarily an abandoned ecosystem; community forks may remain active.
- Stars and forks show attention, not production deployments or paid adoption.
- Issue and pull-request counts show engineering/support load, not defect severity.
- The official repository documents ROS Melodic-era examples; this audit found no official ROS 2 package in the default branch. Third-party ROS 2 wrappers must be audited separately.
