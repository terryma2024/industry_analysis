---
source_id: "SRC-robotics-779"
title: "Atlas cameras and posed images"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/cameras-and-posed-images.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-779
---
# Atlas cameras and posed images

# Cameras and posed images

Bring calibrated images into Atlas without breaking their geometry.

A posed image is an image plus the camera that captured or rendered it. Atlas
uses that pairing to understand which ray produced each pixel, relate views in
one 3D coordinate frame, and keep generated RGB and depth geometrically
aligned.

Use this guide when you already have calibrated renders, COLMAP/OpenCV output,
or cameras from a 3D engine. If you only have images, start with
[Images to posed RGBD](/images-to-posed-images) and let Atlas estimate
the cameras.

## The camera model

Atlas uses a pinhole camera with two parts:

- **Intrinsics** describe the lens and image grid: `fx`, `fy`, `cx`,
  `cy`, `width`, and `height`.
- **Extrinsics** describe the camera-to-world pose: a world-space `position`,
  an XYZW `quaternion`, and a `coordinateSystem`.

```json
{
  "imageAsset": { "assetId": "assets/your-image" },
  "camera": {
    "intrinsics": {
      "fx": 1200,
      "fy": 1200,
      "cx": 960,
      "cy": 540,
      "width": 1920,
      "height": 1080
    },
    "extrinsics": {
      "position": [0, 1.6, 4],
      "quaternion": [0, 0, 0, 1],
      "coordinateSystem": "rdf"
    }
  }
}
```

The intrinsics are in pixels, not normalized coordinates. Pixel `(0, 0)` is
the image's top-left corner, +x points right, and +y points down. `width` and
`height` name the pixel grid those intrinsics describe.

The pose is **camera-to-world**, not a view or world-to-camera transform. If
your tool exports world-to-camera matrices, invert each rigid transform before
converting its rotation to a quaternion. Quaternions use XYZW order and should
be unit length.

The horizontal field of view follows from the intrinsics:
`2 * atan(width / (2 * fx))`. A 1280-wide camera with `fx` of 762 sees 80°.

## RUB and RDF coordinates

`coordinateSystem` tells Atlas which local camera axes your pose uses.

| Value   | Camera axes                                     | Common sources                        |
| ------- | ----------------------------------------------- | ------------------------------------- |
| `"rub"` | right, up, back; the camera looks along -Z      | OpenGL, Three.js, Blender camera axes |
| `"rdf"` | right, down, forward; the camera looks along +Z | OpenCV and many calibration tools     |

![RUB camera axes point right and up and look along minus Z. RDF axes point right and down and look along plus Z.](/media/atlas-diagrams/camera-coordinate-systems.svg "Both conventions describe camera-to-world poses with XYZW quaternions.")

Use the convention your camera-to-world pose was calculated in. Do not change
only the string to convert a pose: the orientation basis must be converted too.
Within one request, every position and orientation must describe the same world
frame and use the same distance unit.

The world frame matters too. For example, Blender is Z-up while Atlas's RUB
world is Y-up, so a Blender export must convert the world-space pose even
though the camera's local axes are already RUB.

In a Y-up world, turning a RUB camera to its right is a negative rotation about
+Y. A camera with no rotation that turns 30° to the right has the quaternion
`[0, -0.2588, 0, 0.9659]`. Check the sign with one generated view before
building a long camera path.

## Euler angles

The API takes orientation only as the XYZW `quaternion`. No request or
response field holds Euler angles.

Euler angles appear only in the Atlas web app. The Chisel editor's Rotation
fields show a node's rotation in degrees, as Three.js Euler angles in the
default `XYZ` order. When the app submits a camera, it converts the camera's
world rotation to an XYZW quaternion with `coordinateSystem: "rub"`. To rebuild
that quaternion from the fields of a camera that is not aimed at a target and
has no rotated parent group:

```ts
import { Euler, MathUtils, Quaternion } from "three";

const q = new Quaternion().setFromEuler(
  new Euler(
    MathUtils.degToRad(rotationX),
    MathUtils.degToRad(rotationY),
    MathUtils.degToRad(rotationZ),
    "XYZ",
  ),
);
const quaternion = [q.x, q.y, q.z, q.w];
```

The editor also gives every camera square pixels and a centered principal
point: `fx = fy = height / (2 * tan(verticalFov / 2))`, `cx = width / 2`, and
`cy = height / 2`.

## Estimating an unposed camera

`images2PosedRGBD` takes images alone and estimates their cameras; a frame
that carries one is rejected rather than ignored. Multi-view captures with
camera translation come back on one of four grids, the closest in aspect to the
frames (1280 x 720 for 16:9 frames). Single images and captures without camera
translation use the reconstruction's native grid. Set `targetResolution` when
a later task needs a fixed size. See [Choose the output
grid](/images-to-posed-images#choose-the-output-grid) for supported sizes and
downstream requirements. This request uses the default grid:

```json
{
  "frames": [
    {
      "imageAsset": { "assetId": "assets/view-000" }
    }
  ],
  "canonicalizeToFirstFrame": false
}
```

The task always gravity-levels the reconstruction and selects confidence from
the available single-view or multi-view evidence.

## Resizing without changing the rays

An image and its camera are one geometric unit. Never resize or crop the pixels
while leaving the intrinsics unchanged.

For `images2PosedRGBD`, the returned camera and depth share a grid. Check
the returned RGB dimensions and framing before treating RGB pixel coordinates
as depth coordinates. Keep the returned intrinsics when unprojecting depth.
If RGB retains the full source framing at another size, resize it onto the
depth grid before sampling colors. A crop requires the corresponding offset
as well as a scale.

The formulas below describe a known resize and crop.

For a plain resize from `W × H` to `W' × H'`, set:

```text
sx = W' / W              sy = H' / H
fx' = sx * fx            fy' = sy * fy
cx' = sx * cx            cy' = sy * cy
width' = W'              height' = H'
```

If you then crop `x0` pixels from the left and `y0` from the top, also
shift the principal point:

```text
cx' = sx * cx - x0
cy' = sy * cy - y0
```

Apply the identical pixel transform to any mask, confidence image, or depth
buffer paired with the frame. A mask that is merely the same width and height
but came from a different crop is not aligned.

Atlas uses pinhole cameras without lens-distortion coefficients; supplying
extra camera fields is rejected with HTTP `422`. Undistort or rectify fisheye
and lens-distorted images before upload, then provide the intrinsics of the
rectified pixels. Align any paired depth, mask, and confidence maps to that
same grid. Uploading a distorted image does not automatically undistort it.

## Scale and depth

Camera positions establish the rig's scale. If positions are measured in
metres, registered linear depth is in metres; if they use another consistent
unit, depth follows that unit.

Use translated views with a meaningful baseline when scale matters. A
pure-rotation sequence (multiple orientations sharing one camera center) does
not provide a baseline from which depth scale can be recovered.

Returned linear-depth EXRs are aligned to the returned camera and its declared
grid. Treat the camera, RGB, depth, and confidence output as one bundle rather
than mixing fields from different views or runs.

Each depth value is the distance along the camera's viewing axis, not along
the ray through that pixel. In a RUB camera, the point seen at pixel `(u, v)`
with depth `z` is at `((u - cx) / fx * z, -(v - cy) / fy * z, -z)` in the
camera's axes.

## Missing values in returned depth

Returned depth EXRs can contain `NaN`. A `NaN` pixel means no reliable
geometry, not a surface at the camera.

The depth that `atlasGenerate` and `atlasChisel` reconstruct
for `returnDepth`, and `images2PosedRGBD` depth for captures with camera
translation, passes through a floater cleanup step. It rejects floating
fragments and other unreliable pixels. Each rejected pixel is written as
`NaN`, and its value in the returned confidence map is `0`. `atlasTextToImage`
depth and single-image or pure-rotation `images2PosedRGBD` results keep the
posing model's own depth, which is also non-finite where it found no geometry.

How many pixels are rejected varies by scene. Skip non-finite pixels when you
unproject points or compute depth statistics, and use the confidence map to
choose which of the remaining pixels to trust.

## Decode linear-depth EXR rows

Atlas camera intrinsics, RGB images, and confidence maps use top-left image
coordinates: row 0 is the top row. Three.js `EXRLoader` decodes EXR data in the
bottom-up row order used by its WebGL texture path. If CPU code reads the
returned `data` array to unproject points, draw a canvas preview, or compare
depth with RGB or confidence pixels, map a top-down y coordinate to
`height - 1 - y`.

With the downloaded EXR in an `ArrayBuffer` named `buffer`:

```ts
import { FloatType, RedFormat } from "three";
import { EXRLoader } from "three/examples/jsm/loaders/EXRLoader.js";

const decoded = new EXRLoader().setDataType(FloatType).setOutputFormat(RedFormat).parse(buffer);

function depthAt(x: number, yFromTop: number): number {
  const sourceY = decoded.height - 1 - yFromTop;
  return decoded.data[sourceY * decoded.width + x];
}
```

This conversion changes only how CPU code indexes the decoded array. It does
not require another API request or a rewritten EXR. `EXRLoader.load()` already
configures its Three.js texture for the decoded row order, so do not flip the
texture a second time.

A quick diagnostic is to draw the unprojected points with the camera frustum
and matching RGB image. If image features align only after reflecting depth
across the horizontal centerline, the decoded row order is wrong. In a
gravity-aligned scene with a visible floor, the floor should also stay below
the camera rather than reflect above it.

## Validation checklist

Before submitting your own posed images, verify:

1. Every pose is camera-to-world and every quaternion is XYZW.
2. `coordinateSystem` matches the pose's actual camera axes.
3. All cameras share one world frame and distance unit.
4. Every image is undistorted and paired with its own camera.
5. Intrinsics describe the uploaded image after its final resize and crop.
6. Masks and depth are pixel-aligned with the same final grid.
7. `atlasChisel` target-frame depth is planar z along the optical axis, with sky
   and other empty pixels marked as no surface
   ([Encode depth](/depth-guided-generation#encode-depth)).
8. CPU-decoded depth is remapped out of the decoder's row order before matching image pixels.
9. Frame order is preserved across images, cameras, masks, and target cameras.
10. The task's exact resolution and view-count requirements are satisfied.

If geometry is vertically mirrored while the camera frustum is correct, check
the decoded EXR row order before changing the camera. If geometry is mirrored
left-to-right or behind the camera, inspect the pose direction and coordinate
convention. If geometry is correctly oriented but shifted or scaled
incorrectly, inspect the shared world frame, camera centers, and units.
