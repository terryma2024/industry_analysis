---
source_id: "SRC-robotics-527"
title: "onshape-to-robot issue 76 DoF in nested subassemblies"
source_type: "user_issue"
publisher: "Rhoban/onshape-to-robot contributor"
source_date: "2022-06-17"
url: "https://github.com/Rhoban/onshape-to-robot/issues/76"
evidence_grade: "B"
capture_method: "defuddle"
captured_at: "2026-08-10T15:46:26+00:00"
tags:
  - raw/source
  - source-type/user-issue
  - evidence/b
aliases:
  - SRC-robotics-527
---
# onshape-to-robot issue 76 DoF in nested subassemblies

Hi, thanks for this super tool!

I'm wondering it is possible to have some DoF defined inside an assembly which is itself included inside a global assembly multiple time.  
I guess this will lead to naming issues, but maybe could be fixed by adding a suffix?  
At the moment, onshape-to-robot detects 0 dof.

It this is not doable, I can of course simply make a big assembly.
