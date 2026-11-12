---
source_id: "SRC-robotics-781"
title: "Atlas using video footage"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/using-video-footage.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-781
---
# Atlas using video footage

# Using video footage with Atlas

Prepare still frames from video for scene reconstruction or a frozen-time camera move.

Use video footage as a source of still images for Atlas. You can reconstruct
a mostly static environment from selected frames, or generate a camera move
around a frozen moment captured by synchronized cameras.

Atlas takes images for these workflows. Direct video upload and
time control across a changing scene are not currently available.

## Reconstruct an environment from a walkthrough

Use this workflow when the camera moves through a room or another mostly
static space.

1. **Select a short, continuous part of the capture.** Keep the scene,
   lighting, and exposure consistent. Choose footage where the camera moves
   between positions so you see surfaces from different angles.
2. **Export selected frames as images.** Use a video editor or frame-extraction
   tool to save sharp, overlapping views. For a single room, start with
   8–16 well-distributed images. Add views where they show an unseen area or
   another side of an object; the count is a starting point, not an API limit.
3. **Reconstruct the images together.** In Viewfinder, import the selected
   images together with **Reconstruct**. Through the Developer API, send them
   in one [images2PosedRGBD](/images-to-posed-images) request. This estimates
   their relative camera positions and depth in one scene.
4. **Inspect the recovered scene.** Check that neighboring views line up and
   cover the area you want to explore. Replace blurred or inconsistent images
   and add coverage where needed before generating new views.

Choose frames by sharpness, overlap, and coverage. A fixed extraction interval
can be a starting point, but inspect the selected images: camera speed changes
how much adjacent frames overlap. Uploading every video frame can add many
near-duplicates without revealing more of the scene.

Aim for roughly 50% shared scene content between neighboring views. Include
the floor, walls, lower furniture, and areas behind obstructions. See
[Splat best practices](/splat-best-practices#cover-the-whole-area-you-need) for
capture examples and coverage guidance.

Images taken at different times work here because the scene stays mostly
static. Moving people or objects can appear in incompatible positions across
views. Avoid using those frames to reconstruct one shared scene. These recipes
use perspective images; convert 360-degree or fisheye footage to perspective
views before using the image-based workflow.

### Choose your output

For a rendered walkthrough, author a camera path in Viewfinder, generate,
and export the video. A finished splat is not required for this step.

Through the API, pass the returned posed views to
[atlasGenerate](/atlas-generate) as `contextFrames`, with the complete ordered
camera path as `targetCameras` in one request. Assemble the returned images
at the frame rate used to sample that path. Independent requests do not share
generated sequence context and can produce flicker or layout changes; see
[Generate a video or camera path](/atlas-generate#generate-a-video-or-camera-path).

For a navigable 3D asset, continue with
[Posed images to splats](/posed-images-to-splats). Inspect the reconstructed
views and their coverage first. Atlas can invent uncaptured areas, and estimated
geometry is not a guarantee of measured dimensions.

## Make a frozen-time camera move

Use synchronized cameras with overlapping views of the same event. Each camera
must show the scene at the same instant; successive frames from one camera
moving around a changing subject do not provide those simultaneous views.

1. **Choose the instant to freeze.** Align the recordings in time, then export
   one image from each camera at that instant. Matching frame numbers alone
   are insufficient if the recordings started at different times.
2. **Reconstruct those images together.** Submit the synchronized images in
   one `images2PosedRGBD` request and inspect the recovered views.
3. **Generate the virtual camera move.** Pass those posed views to
   `atlasGenerate` with your full camera path. Start and end at the physical
   camera viewpoints you want to join to the original footage.
4. **Edit the result into your video.** Play the original footage up to the
   chosen instant, insert the generated camera move, then resume the original
   footage from the ending camera at that instant.

This creates a camera move around one frozen scene. You choose the freeze
point and assemble the surrounding footage in a video editor. Atlas does
not expose continuous reframing while the captured scene changes over time.

Test a short move first and inspect the subject from the intended viewpoints.
Human faces, articulated subjects, and fine details may change in generated
views. See [Best practices](/best-practices) for current quality limitations.
