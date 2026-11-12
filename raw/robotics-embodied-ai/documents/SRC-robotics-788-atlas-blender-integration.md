---
source_id: "SRC-robotics-788"
title: "Atlas Blender integration"
source_type: "product_documentation"
publisher: "World Labs"
source_date: "待验证"
url: "https://docs.atlas-beta.worldlabs.ai/blender.md"
evidence_grade: "S"
capture_method: "direct-download"
captured_at: "2026-11-12T01:37:18+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/s
aliases:
  - SRC-robotics-788
---
# Atlas Blender integration

# Blender

Import Gaussian splats and calibrated RGBD images into Blender.

Import and render Gaussian splats in Blender 5.3, which has
[native Gaussian splat support](https://developer.blender.org/docs/release_notes/5.3/rendering/).

1. [Download and install Blender 5.3](https://www.blender.org/download/releases/5-3/).
2. Download your `.spz` or `.ply` splat file. If it comes in a ZIP, extract it first.
3. Drag the file into Blender's viewport and confirm the import.

Save the scene as a `.blend` file to keep working in Blender.

## Optional Atlas tools

For Atlas generation and editing inside Blender, install the
[Atlas Blender extension](https://github.com/worldlabsai/skills/blob/main/skills/atlas-blender/references/setup.md).
For calibrated RGBD images, the extension imports bundles of `PosedRGBDAsset`
records from the [World Labs JavaScript client](https://www.npmjs.com/package/@worldlabsai/client):
each record contains `imageAsset`, `camera`, and `depth`. Splat file references
use `TaskAsset`. See the [World Labs CLI](/cli) for command-line and agent workflows.

## Work with a coding agent

With the extension, the scene itself shows what Atlas knows: each posed image
is a camera with a point cloud, and you place target cameras among them before
generating. That makes Blender a good place to plan views with an agent and to
check them together.

The `atlas-blender` skill, one of the
[World Labs skills](/skills-and-plugins), tells an agent how to use the
extension: posing images, placing cameras, generating views, and creating
splats. The agent reaches an open Blender session through
[Blender MCP](https://www.blender.org/lab/mcp-server/). An agent with only a
terminal can run the same commands in Blender's background mode; the skill
covers both. The steps match the [workflow guides](/build-a-scene).
