---
source_id: "SRC-robotics-785"
title: "Atlas splat best practices"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/splat-best-practices.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-785
---
# Atlas splat best practices

# Splat best practices

Choose scenes, prepare overlapping views, and recognize common splat artifacts.

Splat quality depends on both the scene and the views you provide. Start with a
bounded, textured environment, cover the areas you want to explore, and check
that overlapping views agree before submitting
[posedImages2Splats](/posed-images-to-splats).

See the [`posedImages2Splats` API reference](/api-reference/posed-images2-splats) for request fields and response details.

## Where splats work well

With good input, bounded indoor spaces with rich texture are a strong starting
point. Successful examples include furnished living rooms, home offices,
retail shops, wood-paneled rooms, and stylized science-fiction interiors.
Furniture, shelving, floor patterns, and wall detail give these scenes visible
structure across viewpoints.

A good overall room reconstruction does not guarantee accurate detail in every
object. Inspect the features that matter to your use case from the viewpoints
you plan to use.

## Features that need closer inspection

| Scene feature      | What can go wrong                                                                | What to inspect                                                 |
| ------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Large, open spaces | The foreground can look good while distant areas become fuzzy or lose structure. | Check the background as well as nearby objects.                 |
| Sky and clouds     | Large sky regions can contain streaks, blobs, or floating artifacts.             | Look at the sky while moving through the scene.                 |
| Trees and foliage  | Leaves and small branches can blur or merge together.                            | Inspect fine detail where vegetation is important.              |
| Large plain walls  | Uncertain depth can produce bulges or uneven surfaces.                           | View walls from an angle to check their shape.                  |
| Human faces        | Facial detail may be inaccurate.                                                 | Avoid relying on faithful facial reconstruction.                |
| Thin structures    | Chair legs, hanging wires, and similar parts can have missing segments.          | Check that important thin parts remain continuous across views. |
| Windows            | Glass and the scene beyond it can reconstruct poorly.                            | Inspect the view through the window, as well as its frame.      |

Consistent inputs help, but sky, foliage, and fine detail can remain difficult
when the views agree. These are quality limitations to evaluate for your
scene, rather than a rule that every scene containing these features will fail.

## Prepare a consistent set of views

Keep the scene mostly static, use sharp images, and keep exposure and lighting
consistent. For generated views, compare overlapping regions before splatting:
objects should retain their position, orientation, shape, and appearance.
Check again when a sequence returns to an earlier part of the room.

For example, in a cabin scene, generated views placed and shaped the same
dining table differently. The reconstruction combined those conflicting views
into overlapping, ghosted surfaces. In another living room, a coffee table
became two tables on a return view, and the duplication carried into the splat.
Resolve these disagreements in the input set before generating the splat.

![First generated cabin view with a wide table and white legs](/media/splat-cabin-input-1.webp "Input view 1: note the dining table's shape and its position relative to the kitchen.")

![Second generated cabin view with a narrower wooden table in a different orientation](/media/splat-cabin-input-2.webp "Input view 2: the same room contains a different table shape, orientation, and leg appearance.")

![Overhead splat view with overlapping table surfaces and ghosted chairs](/media/splat-cabin-ghosting.webp "Result from the full input set: inconsistent table geometry produces ghosting. The two images above are selected views from that set.")

## Cover the whole area you need

For a single room, start with 8–16 well-distributed views. Four views can miss
too much of a complex room. Add views where they reveal an unseen area or a
new side of an object; repeating an already covered viewpoint adds less value.
Larger or more occluded spaces may need more views. The count is a starting
point, not an API limit or a guarantee of quality.

Include the floor, lower furniture, walls, and areas behind obstructions that
you intend to explore. In one lobby example, the input sequence looked mostly
up at the ceiling and missed the floor. The resulting lower scene contained
blurry, invented furniture. More views of the ceiling would not fill that gap.

Neighboring views should share recognizable scene content. Aim for roughly 50%
shared image content, with at least about 10% as a practical lower bound when
planning a capture. These are approximate capture recommendations, not request
validation thresholds. Sparse overlap can make camera estimation unreliable,
and camera errors can degrade the resulting splat.

Keep the image, camera, and depth for each view together. Use the returned
frames from [images2PosedRGBD](/images-to-posed-images) when estimating cameras
and depth from photographs; their intrinsics describe the returned image grid.
See [Cameras and posed images](/cameras-and-posed-images) for coordinate and
depth conventions.

## Check the result before using it

Move through the intended viewing area, rather than judging only the first
view. Look for ghosting, duplicated objects, missing floor coverage, wall
bulges, and the difficult features above. When a problem corresponds to an
inconsistent or uncovered input region, improve those views before rerunning.
For persistent fine-detail or sky artifacts, assess whether the result meets
your use case even with a consistent, well-covered input set.

Continue with the [API task guide](/posed-images-to-splats) for submission,
waiting for completion, and using the SPZ output.
