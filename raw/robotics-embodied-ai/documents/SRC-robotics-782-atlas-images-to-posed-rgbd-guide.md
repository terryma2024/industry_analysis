---
source_id: "SRC-robotics-782"
title: "Atlas images to posed RGBD guide"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/images-to-posed-images.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-782
---
# Atlas images to posed RGBD guide

# Images to posed RGBD

Estimate cameras and depth for one or more images.

`images2PosedRGBD` estimates camera parameters and linear depth for one or
more perspective images. Use it to turn unposed captures into geometry-aware
inputs for Atlas world workflows.

See the [`images2PosedRGBD` API reference](/api-reference/images2-posed-rgbd) for request fields and response details.

```text
POST /api/v2/tasks:images2PosedRGBD
```

The task is asynchronous.

## Choose your inputs

Supply one or more frames in a stable order. Each `imageAsset` can be a
project-owned asset ID, inline base64 smaller than 10 MiB, or a public HTTPS
URL. Assets are the best default for private or reusable media.

```json
{
  "frames": [
    { "imageAsset": { "assetId": "asset_room_01" } },
    { "imageAsset": { "assetId": "asset_room_02" } },
    { "imageAsset": { "assetId": "asset_room_03" } }
  ],
  "canonicalizeToFirstFrame": false
}
```

A single image uses the single-view reconstruction path. Multiple images use
the multi-view path to recover their cameras. When those cameras include
translation, a depth model uses the recovered poses to estimate the final depth.
Captures without camera translation retain the reconstruction depth.

For multiple images, the service measures focal length on several
frames and uses that estimate for guidance. This adds roughly 1-3 seconds to
the task and aims to improve camera intrinsics.

Use sharp, overlapping views with stable lighting. Keep the scene mostly
static while capturing it, and avoid mixing unrelated places in one request.

For video captures, extract selected still frames before submitting this task.
[Using video footage with Atlas](/using-video-footage) covers static-scene
walkthroughs and synchronized views of a frozen moment.

## Choose the output grid

By default, multi-view captures with camera translation are returned on one of
four grids: `[1280, 720]`, `[720, 1280]`, `[960, 720]` or `[528, 704]`. The task
picks the grid closest in aspect to the images: `[1280, 720]` for 16:9 frames,
`[960, 720]` for 4:3, `[528, 704]` for 3:4, and `[720, 1280]` for 9:16. Smaller
frames are scaled up onto that grid, and other aspects (square or 3:2, for
example) are center-cropped onto the closest one, with squares going to
`[960, 720]`. Single images and captures without
camera translation retain the reconstruction backend's native grid. Set
`targetResolution` to one of those four grids (`[width, height]`) when a
downstream stage requires one fixed raster; the result is scaled to cover that
size and center-cropped to it, so an aspect that differs from the frames'
costs field of view. Other sizes are rejected.

Depth, confidence, and camera intrinsics describe the same grid. When
`targetResolution` is omitted or `null`, `imageAsset` can reference the
original image even if its dimensions differ from the depth grid. For example,
a 4032 × 3024 image can be returned beside 960 × 720 depth. Use the returned
camera to unproject depth. Before matching RGB and depth pixels, check that
both assets use the same grid and framing. A plain resize is sufficient only
when the full image framing is unchanged. An explicit `targetResolution` puts
the returned RGB on the same grid as the depth.

Choose a target according to the next task:

- [atlasGenerate](/atlas-generate#prepare-rgbd-context) allows context
  resolution to differ from its four supported generation target sizes. All
  context cameras must share one size. With `returnDepth: true`, their aspect
  ratio must also match the target cameras'.
- [atlasChisel](/depth-guided-generation) requires 1280 × 720 target
  cameras. Request `targetResolution: [1280, 720]` when preparing
  `targetFrames` for [masked edits](/inpainting). Reference photographs in
  `contextFrames` may have other resolutions.

The task estimates the cameras. Input cameras, masks and depth are not
accepted. Gravity alignment and confidence selection are automatic.

## Refine the cameras

`refinePoses` defaults to `false`. Set it to `true` to bundle-adjust the
estimated cameras against dense matches before answering. The estimated poses
are good to about half a degree, which is enough to reconstruct from and not
enough to refine against: the residual shows up as blur wherever two views
disagree. Turn it on when the output feeds a stage that compares views against
each other.

It needs two or more frames, and it costs a matching pass and a solve on top
of the reconstruction. A solve that moves the cameras further than the service
allows is discarded and the unrefined reconstruction is returned, so a request
never fails because the refinement did not hold.

When requested, `operation.response.poseRefinementAccepted` is `true` if the
refined cameras were kept and `false` if the original reconstruction was
returned. It is `null` when refinement was not requested.

## Get the files in the submission response

`base64Outputs` defaults to `false`. A submission sent with `?wait=true` can
come back already `done: true`, and by default that response names each output
file by `assetId` and `url`. Set `base64Outputs` to `true` to receive each
output file in that response as a base64 data URL instead. The service then
skips storing the files before it answers, and you skip downloading them. A
later read of the operation names the files by `assetId` and `url` either way.
See [Operations](/operations).

## Submit large batches without waiting

A `?wait=true` submission holds one HTTP request open while the task runs, and
the API's load balancer closes a request after 60 seconds. A large batch can
outlast that and fail with HTTP `504` before any response arrives. For large
batches, submit without `?wait=true`, persist the operation ID, and poll or
call `:wait` until `done` is true.

Send an `Idempotency-Key` with each submission. If a submission fails without
a response, retry the same body with the same key: when the first attempt was
accepted, the retry returns its operation instead of starting a second task.
See [Errors and retries](/errors#retry-without-duplicate-work).

## Read the result

Persist the operation ID, then use `:wait` or poll until `done` is true. The
successful response has one frame per input image, in the same order. Each
frame includes:

- the source image or a resized or cropped replacement. Its dimensions can
  differ from the depth grid when `targetResolution` is omitted or `null`;
- a camera describing the returned depth grid;
- a linear-depth EXR in world units, stored as half-float pixels (relative
  rounding error up to about 5e-4). Three.js `EXRLoader` with `FloatType` and
  OpenCV decode it to float32; a reader that takes the raw channel gets 16-bit
  half values. Pixels with no reliable geometry are `NaN`; see
  [Missing values in returned depth](/cameras-and-posed-images#missing-values-in-returned-depth).

The returned camera provides the intrinsics for unprojecting depth. Map RGB
pixels onto the same grid and framing before matching them to depth. See
[Choose the output grid](#choose-the-output-grid).

> **Three.js EXRLoader:** Its CPU `data` array exposes EXR rows bottom-up. Map
> image-space `y` to `height - 1 - y` before unprojecting or matching depth with
> the returned image and confidence map. See the
> [reference accessor](/cameras-and-posed-images#decode-linear-depth-exr-rows).

## Example completed output

After the operation reports `done: true`, its task-specific result is in
`operation.response`:

```json
{
  "frames": [
    {
      "imageAsset": {
        "assetId": "asset_room_01",
        "url": "https://example.com/room-01.png"
      },
      "camera": {
        "extrinsics": {
          "position": [0, 0, 0],
          "quaternion": [0, 0, 0, 1],
          "coordinateSystem": "rub"
        },
        "intrinsics": {
          "width": 1280,
          "height": 720,
          "fx": 900,
          "fy": 900,
          "cx": 640,
          "cy": 360
        }
      },
      "depth": {
        "depthAsset": {
          "assetId": "asset_depth_0",
          "url": "https://example.com/depth-0.exr"
        },
        "confidenceAsset": {
          "assetId": "asset_confidence_0",
          "url": "https://example.com/confidence-0.png"
        }
      }
    }
  ]
}
```

Open the [API reference](/api-reference) for the exact camera, depth, and
operation schemas.
