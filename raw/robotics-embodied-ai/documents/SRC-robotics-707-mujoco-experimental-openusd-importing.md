---
source_id: "SRC-robotics-707"
title: "MuJoCo experimental OpenUSD importing"
source_type: "documentation"
publisher: "MuJoCo"
source_date: "待验证"
url: "https://mujoco.readthedocs.io/en/stable/OpenUSD/importing.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T02:02:52+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-707
---
# MuJoCo experimental OpenUSD importing

## Importing

> [!warning] Warning
> OpenUSD support is currently experimental and subject to frequent change.

MuJoCo can load assets from OpenUSD files (`.usd`, `.usda`, `.usdc`, `.usdz`). This allows you to incorporate assets and scenes defined in USD into your MuJoCo simulations.

## USD in MJCF

If you have built mujoco with USD enabled, you can reference USD assets from MJCF via the `<model` tag with content type `text/usd`.

```xml
<mujoco>
  <asset>
    <model file="chair.usdz" name="chair" content_type="text/usd"/>
  </asset>

  <worldbody>
    ...
  </worldbody>
</mujoco>
```

In this example the `<model file="chair.usdz"/>` line in `<asset>` tells MuJoCo to load and process the USD file.
