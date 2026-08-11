---
source_id: "SRC-robotics-526"
title: "onshape-to-robot issue 170 Onshape API rate limit"
source_type: "user_issue"
publisher: "Rhoban/onshape-to-robot contributor"
source_date: "2025-08-18"
url: "https://github.com/Rhoban/onshape-to-robot/issues/170"
evidence_grade: "B"
capture_method: "defuddle"
captured_at: "2026-08-10T15:46:26+00:00"
tags:
  - raw/source
  - source-type/user-issue
  - evidence/b
aliases:
  - SRC-robotics-526
---
# onshape-to-robot issue 170 Onshape API rate limit

On larger projects, its difficult to download the entire assembly without hitting a rate limit. I was hoping there could be an option in the config file to pace the API requests to ensure its within the API limits of OnShape.

I got the error on a project with ~1000 parts below:

```
! ERROR (429) while using Onshape API
! {
  "message" : "Too many requests.",
  "moreInfoUrl" : "",
  "status" : 429,
  "code" : 0
}
```
