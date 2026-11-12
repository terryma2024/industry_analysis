---
source_id: "SRC-robotics-778"
title: "How to use Atlas"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/how-to-use-atlas.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-778
---
# How to use Atlas

# How to use Atlas

Pose images, explore new views, and edit your scene with Atlas.

Atlas builds a scene through images: pose your starting views, generate new
viewpoints, then edit what is in them. Each view carries camera and depth
information that you can reuse as the project grows.

For recordings, see [Using video footage with Atlas](/using-video-footage)
to select frames from a walkthrough or synchronized cameras.

To go from images to a finished result, follow
[Build a scene from images](/build-a-scene), then [Make a video](/scene-to-video)
or [Make splats](/scene-to-splats). Coding agents can install the
[World Labs skills](/skills-and-plugins), which carry those workflows.

## 1. Pose your images

Start with [images2PosedRGBD](/images-to-posed-images). There are two ways
to build your initial scene:

- **Reconstruct an existing place.** Submit images with overlapping camera views
  together so the service can estimate their relative positions. Use sharp
  images of a mostly static scene, with similar exposure and lighting.
- **Connect images creatively.** Pose individual images in separate requests,
  then place the returned views at positions and orientations you choose in
  one shared scene. Atlas can invent the space connecting them when you
  generate new views.

> **Overlapping camera views.** Camera views may overlap _only_ if they were
> reconstructed together from the same real location or if Atlas is generating
> the view. Independently posed creative images must have non-overlapping
> camera views. Place them plausibly in the scene so their geometry fits
> together and Atlas can connect them.

Posing returns each image with a camera and a depth map. The camera describes
where the image was taken, which direction it faces, and its field of view.
Depth estimates how far the visible surfaces lie from the camera. Together,
these form a posed RGBD view: color, camera, and depth that describe the same
part of the scene.

Our example starts with one image of a blacksmith's workshop. Posing estimates
its geometry; we request `targetResolution: [1280, 720]` for the 1280 × 720
generation targets used in this example.

![Posed image of a blacksmith workshop with a forge, anvil, and window](https://docs.atlas-beta.worldlabs.ai/media/how-to-use-atlas-source.webp "Workshop image returned by images2PosedRGBD, at 1280 × 720")

![Depth of the workshop, with the foreground brighter than the back wall](https://docs.atlas-beta.worldlabs.ai/media/how-to-use-atlas-depth.webp "Estimated depth, visualized: brighter surfaces are closer. Use the depth map to create point clouds and visualize the scene.")

## 2. Generate new views

Choose where to look next. Send your posed images as `contextFrames` to
[atlasGenerate](/atlas-generate), along with new `targetCameras`.
The context tells Atlas what is already in the scene; the target cameras tell
it where to render. Your application or agent chooses those cameras and
keeps track of the scene.

Atlas returns an RGB image and camera for every target. Set `returnDepth: true`
to receive depth as well, so the new views can become context for another
request.

Starting from the workshop's original posed camera, we turn **20° to the right**
and apply a **−0.25 X translation**.

![Workshop viewed 20 degrees to the right of the original camera with a −0.25 X translation](https://docs.atlas-beta.worldlabs.ai/media/how-to-use-atlas-result.webp "Atlas-generated view: 20° right yaw and −0.25 X translation")

Inspect the result, add useful returned RGBD views to your context, and choose
the next cameras. Repeat to explore further. Atlas invents areas outside the
original images.

> **Important: reuse the scene prompt for faster generation.** For subsequent
> views of the same scene, pass the previous response's `promptUsed` as `prompt`
> and set `enhancePrompt: false`. This skips recaptioning the context images and
> reduces generation latency.

For a video or flythrough, submit the full ordered camera path in one request.
[Make a video](/scene-to-video) walks through it, and
[Generate a video or camera path](/atlas-generate#generate-a-video-or-camera-path)
covers sequence generation, preview renders, and context selection.

## 3. Edit objects

Use [atlasChisel](/inpainting) to make masked edits across
posed views. Send each RGB image in `targetFrames` with its camera and a
separate grayscale mask: **black marks the area to edit; white preserves the image**. Cover the
whole object in every affected view, and keep each image and mask aligned
with that target frame's 1280 × 720 camera.

With prompt enhancement enabled, describe the edit explicitly, such as
"replace the wooden stool beside the anvil with a metal toolbox." The prompt
enhancer uses the RGB images and your edit instruction. Inspect the completed
views before using them as scene context again.

## Keep cameras and depth aligned

The image, camera, and depth for a view are one unit. Keep the returned bundle
together, including any confidence map.

- **Pixel grid:** posing can return the source RGB beside depth on a different
  grid. Check dimensions and framing before matching their pixels. See
  [Choose the output grid](/images-to-posed-images#choose-the-output-grid).
  `atlasGenerate` supports 1280 × 720, 960 × 720, 528 × 704, and 720 × 1280
  target cameras. Its context can have another resolution. If you change a
  view's pixels, update its camera intrinsics and aligned maps to match.
- **Coordinates:** all camera poses are camera-to-world and must share one
  world frame and distance unit. Quaternions use XYZW order. RUB cameras look
  along local -Z; RDF cameras look along local +Z. Convert the camera pose when
  changing coordinate conventions.
- **Depth and scale:** calibrate the scene scale for measurements in meters.
  Linear EXR values use the scene's distance units; encoded depth PNGs need decoding.
  Scale the depth and camera positions together when resizing an entire scene.

[Cameras and posed images](/cameras-and-posed-images) covers camera math,
resizing, coordinate conversion, and EXR row order. Use it before projecting
image points into 3D or planning a camera path from depth.

## Choose context and prompts

Use context views that show the part of the scene you want to preserve. For
creative connections, place independently posed images plausibly with
non-overlapping camera views. Inspect generated views before adding them back,
since geometry or appearance errors can carry into later requests.

Describe the environment, materials, lighting, and spatial relationships.
Prompt enhancement is on by default; reuse `promptUsed` for continued
exploration as described above. For a masked edit with enhancement disabled,
describe the finished scene.
Start with the service's model and sampling defaults. See [Best
practices](/best-practices) for more input guidance.

## Choose a task

See the [task overview](/task-overview) to choose a task for the result you
want.

For runnable requests, use the [CLI guide](/cli),
[TypeScript quickstart](/web-quickstart), or [API quickstart](/quickstart).
The [API reference](/api-reference) describes the public endpoints, fields,
and limits.
