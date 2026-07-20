---
source_id: "SRC-robotics-312"
title: "MATRiX GitHub maintenance and issue audit"
source_type: "code_repository_metadata"
publisher: "GitHub / zsibot matrix"
source_date: "2026-07-20"
url: "https://api.github.com/repos/zsibot/matrix"
evidence_grade: "S"
capture_method: "manual-api-summary"
captured_at: "2026-07-20T08:57:45+00:00"
tags:
  - raw/source
  - source-type/code-repository-metadata
  - evidence/s
aliases:
  - SRC-robotics-312
---

# MATRiX GitHub maintenance and issue audit

This is a lossless-enough analyst-readable snapshot of public GitHub API fields queried on 2026-07-20. It summarizes repository, release, commit, contributor, issue, pull-request, and tag endpoints. Exact URLs are listed at the end. User issue reports are field signals, not controlled benchmarks.

## Repository snapshot

| Field | Value |
|---|---:|
| Repository | `zsibot/matrix` |
| Created | 2025-09-01T10:25:41Z |
| Latest main commit | `918fae36216e4abb70fbbe275c687c0127fe4b02` (authored 2026-05-20) |
| GitHub `pushed_at` | 2026-07-07T09:35:04Z |
| Stars | 347 |
| Forks | 40 |
| Watchers/subscribers | 6 |
| Open issues | 0 |
| License detected by GitHub | BSD-3-Clause |
| Primary language | Shell |
| Repository size field | 1,097,772 KB |

## Commit and contributor snapshot

- 80 commits from 2025-09-24 through 2026-05-20.
- Monthly counts: 2025-09 3; 2025-10 8; 2025-11 6; 2025-12 11; 2026-01 13; 2026-02 2; 2026-04 32; 2026-05 5.
- Author-name counts: `genisom.ai` 35; `baijinde` 24; `liuxinxin` 8; `Alphabaijinde` 4; `huangkiki` 4; `Wei Pan` 3; `Kiki Huang (huangkiki)` 2.
- Contributor endpoint grouped identities differently because several commits used anonymous email identities: `GENISOM-AI` 35; `baijinde` 24; `huangkiki` 6; `liuxinxin` 5 plus 3 under another email; `Alphabaijinde` 4; `panweihit` 3.
- Seven merge commits were observed.

## Releases and download signals

Three published releases were returned: `v0.1.0` (2025-12-15), `v0.1.1` (2026-01-06), and `v0.1.2` (2026-04-28). For `v0.1.2` at capture time:

| Asset | Bytes | Downloads |
|---|---:|---:|
| `assets-0.1.2.tar.gz` | 1,030,738,643 | 867 |
| `base-0.1.2.tar.gz` | 2,116,244,298 | 789 |
| `manifest-0.1.2.json` | 6,573 | 727 |
| `shared-0.1.2.tar.part000` | 2,000,000,000 | 682 |
| `shared-0.1.2.tar.part001` | 1,451,081,662 | 555 |
| `SceneWorld-0.1.2.tar.gz` | 398,747,908 | 378 |
| `Town10World-0.1.2.tar.gz` | 1,159,597,956 | 345 |
| `YardWorld-0.1.2.tar.gz` | 687,750,590 | 309 |

Download counts are GitHub asset-download counters. They show interest/download activity, not successful installation, active users, paid customers, or production deployment.

The release manifest reports 19 optional map packages. The minimum required `assets + base` download is 3,146,982,941 bytes (about 3.15 GB decimal or 2.93 GiB). Adding the recommended shared package raises the package total to 6,598,064,603 bytes (about 6.60 GB decimal or 6.15 GiB), before optional maps.

## Tag anomaly

The tags endpoint returned `v0.2.2`, `v0.1.2`, `v0.1.1`, `v0.1.0`, and earlier `v0.0.x` tags. `v0.2.2` points to commit `4290e4e` authored 2026-04-24, but no corresponding GitHub Release was published, while `v0.1.2` was published on 2026-04-28 and main later moved to `918fae3`. Therefore `v0.2.2` is not treated as the stable latest release in this audit.

## Issues and pull requests

- GitHub search returned 26 issues and 7 pull requests in total.
- All seven pull requests were opened by `Alphabaijinde` and merged in January 2026; no external merged PR was visible in this snapshot.
- Issue topics included missing launcher assets, Git LFS/package failures, keyboard control, map loading, Docker errors, missing camera/LiDAR topics, Ubuntu 24.04 support, custom robot import, Isaac Lab compatibility, and parallel scale.
- Maintainer reply to issue 10 (2025-10-29) described 5–100 robot parallel simulation as a future plan depending on sensors and speed; this is not a shipped benchmark.
- Maintainer reply to issue 6 described Isaac Lab compatibility as a future plan.
- Issue 29 documents a user unable to receive camera/LiDAR topics; discussion moved to a WeChat group without a public resolution. Another user reported the same symptom in July 2026.
- Issue 31 documents keyboard/map-loading problems; discussion likewise moved off GitHub, and later commenters still asked for a solution.
- Several older issues were bulk-closed on 2026-07-19 without a public technical resolution in the issue thread.

## Audited repository tree observations

The main-branch checkout at `918fae3` contained no `.github/workflows`, no `Dockerfile`, no visible C/C++/Unreal project source, and no conventional automated test directory. It did contain approximately 8,824 lines across shell and Python scripts, local Debian packages, documentation, configuration files, demo media, and release-management logic. `bash -n` passed for tracked shell scripts and Python byte-compilation passed for `scripts/validate_xml_contract.py`; the full Ubuntu/ROS/GPU runtime was not executed in this audit.

## API endpoints

- `https://api.github.com/repos/zsibot/matrix`
- `https://api.github.com/repos/zsibot/matrix/releases?per_page=20`
- `https://api.github.com/repos/zsibot/matrix/commits?per_page=100`
- `https://api.github.com/repos/zsibot/matrix/contributors?per_page=100&anon=1`
- `https://api.github.com/repos/zsibot/matrix/tags?per_page=100`
- `https://api.github.com/repos/zsibot/matrix/issues?state=all&per_page=100`
- `https://api.github.com/repos/zsibot/matrix/pulls?state=all&per_page=100`

