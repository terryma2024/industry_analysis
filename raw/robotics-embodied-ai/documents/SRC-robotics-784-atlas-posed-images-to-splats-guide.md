---
source_id: "SRC-robotics-784"
title: "Atlas posed images to splats guide"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/posed-images-to-splats.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-784
---
# Atlas posed images to splats guide

# Posed images to splats

Reconstruct refined Gaussian splats from posed RGBD images.

`posedImages2Splats` reconstructs Gaussian splats from posed RGBD images, then
refines them by rendering new views, cleaning them up, and training the splats
against them. The result is an SPZ file.

See the [`posedImages2Splats` API reference](/api-reference/posed-images2-splats) for request fields and response details.

```text
POST /api/v2/tasks:posedImages2Splats
```

The task is asynchronous.

Each successful run costs:

- Refined (the default): 5,000 credits ($5).
- Draft, with `refine: false`: 500 credits ($0.50).

Failed runs are free.

## Prepare the capture

Provide 2 to 512 ordered `posedFrames` for refined runs (the default), or
2 to 32 for drafts (`refine: false`). Each frame combines an `imageAsset`
with its camera and its `depth`: a linear-depth EXR under `depth.depthAsset`,
as [images2PosedRGBD](/images-to-posed-images) returns for each image, or
[atlasGenerate](/atlas-generate) with `returnDepth`. An asset can be a
project-owned asset ID, inline base64 smaller than 10 MiB, or a public HTTPS
URL. Every frame needs depth. Keep each returned image, camera, and depth
together. Every camera grid must be one of 1280x720, 720x1280, 960x720, or
528x704 (width x height), and all frames must declare the same grid.
RGB images are resampled to that grid. The camera
intrinsics describe this grid, which can differ from the original image. See
[Cameras and posed images](/cameras-and-posed-images).

Outputs from `images2PosedRGBD` and `atlasGenerate` at 1280x720, 960x720,
528x704, or 720x1280 can be passed directly. `images2PosedRGBD` returns one of
those grids for multi-view captures with camera translation; for a single image
or a capture without camera translation, set `targetResolution` to one of them.

```json
{
  "posedFrames": [
    {
      "imageAsset": { "assetId": "asset_view_00" },
      "depth": { "depthAsset": { "assetId": "asset_depth_00" } },
      "camera": { "...": "..." }
    },
    {
      "imageAsset": { "assetId": "asset_view_01" },
      "depth": { "depthAsset": { "assetId": "asset_depth_01" } },
      "camera": { "...": "..." }
    }
  ]
}
```

The request accepts as few as two frames. For a single room, start with 8–16
well-distributed, overlapping views and add views to cover missing areas.
Check that objects agree across views, including generated ones, before
submitting. The [Splat best practices](/splat-best-practices) guide covers
suitable scenes, common artifacts, and capture examples.

For a worked example from a single image, follow
[Build a scene from images](/build-a-scene) and [Make splats](/scene-to-splats).
For the same steps in TypeScript, see
[Generate views and reconstruct splats](/atlas-generate#reconstruct-splats-from-generated-views).
Refinement uses input depth to constrain surface geometry. Sky pixels and depth
maps that disagree substantially with the draft are excluded from depth supervision.
Inspect agreement across the inputs before reconstruction: refinement does not
guarantee that inconsistent depths or conflicting object placements will be fixed.

## Describe the scene

`prompt` is optional. Prompt enhancement is on by default: it combines your
description with the input images, or captions the images when you send no
prompt. Set `enhancePrompt` to `false` with a prepared prompt to skip
enhancement and reduce latency.

## Wait for the result

A run usually takes 15 to 25 minutes, longer than a `?wait=true` request stays
open. Submit without `?wait=true`, persist the operation ID, and poll or call
`:wait` until `done` is true, or pass a `webhookUrl` to be notified when it
finishes. See [Operations](/operations) and [Webhooks](/webhooks).

## Example completed output

When the operation reports `done: true`, check for `operation.error` before
reading a successful result from `operation.response`. `refinedSplats` maps
each published splat count to its SPZ file; the count in this example is illustrative.

```json
{
  "refinedSplats": {
    "2000000": {
      "assetId": "asset_splat_01",
      "url": "https://example.com/refined.spz"
    }
  }
}
```

Pass the asset to [splats2Mesh](/api-reference/splats2-mesh) as its
`splatAsset` to extract a mesh. Open the
[posedImages2Splats reference](/api-reference/posed-images2-splats) for the
exact fields, constraints, and response shape.
