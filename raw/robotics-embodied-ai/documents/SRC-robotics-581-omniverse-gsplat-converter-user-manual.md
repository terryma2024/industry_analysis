---
source_id: "SRC-robotics-581"
title: "Omniverse GSplat Converter user manual"
source_type: "technical_documentation"
publisher: "NVIDIA Omniverse"
source_date: "2026-09-22"
url: "https://docs.omniverse.nvidia.com/extensions/latest/ext_gsplat-converter/manual.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:55:41+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-581
---
# Omniverse GSplat Converter user manual

## User Manual

## Supported File Formats

The following file formats are supported by GSplat Converter:

- PLY Files (`*.ply`) — Standard 3D Gaussian Splat format; binary (little/big-endian) and ASCII. Required vertex properties: `x y z`, `scale_0/1/2`, `rot_0..3`, `opacity`, `f_dc_0/1/2`, `f_rest_0..N`.
- SPZ Files (`*.spz`) — Niantic compressed Gaussian Splat format (v2 and v3).

## Usage

There are two entry points for importing Gaussian Splat files using the GSplat Converter in Kit.

### File → Import

To import a Gaussian Splat file into Omniverse, choose **Import** in the **File** menu. For `.ply` files you can select either the default **Asset Importer** (mesh path) or the **3D Gaussian Splat (Particle Field)** importer. `.spz` files are always converted via the splat path.

### Content Browser → Convert to USD

To convert a file to USD, right-click it in the Content Browser and choose **Convert to USD**.

> [!note] Note
> There is no standalone GSplat Converter Tools window. All Kit-based conversion is handled through **omni.kit.tool.asset\_importer**.

### Converter Options

| Option | Default | Description |
| --- | --- | --- |
| `--generateSh` | `false` | Synthesize SH DC coefficients from `red/green/blue` when `f_dc` properties are absent. |
| `--generateScales` | `false` | Estimate splat scales from KNN neighborhood spacing. Requires `scipy`. |
| `--up-axis` | `Y` | USD stage up-axis: `Y` or `Z`. |
| `--rotate-x/y/z` | `0.0` | Euler rotation in degrees (XYZ order) applied before writing. Useful to correct COLMAP Y-down orientation. |
| `--name` | input stem | Override the USD prim name. |

For full option details, see the extension API reference:

- [omni.kit.converter.gsplat](https://docs.omniverse.nvidia.com/kit/docs/omni.kit.converter.gsplat/latest/Overview.html)

### CLI

Headless batch conversion is available via the pip-installable `usd-convert-gsplat` CLI or the Kit shim.

```bash
# Basic conversion (pip install)
usd-convert-gsplat -i scene.ply -o scene.usda

# SPZ input
usd-convert-gsplat -i scene.spz -o scene.usdz

# Correct COLMAP Y-down orientation
usd-convert-gsplat -i scene.ply -o scene.usda --rotate-x 180

# Synthesize SH from RGB colors
usd-convert-gsplat -i scene.ply -o scene.usda --generateSh

# Z-up output stage
usd-convert-gsplat -i scene.ply -o scene.usda --up-axis Z

# From a Kit layout (shim delegates to usd_convert_gsplat)
python -m omni.kit.converter.gsplat.cli -i scene.ply -o scene.usdc
```

### Programming Guide

Python developers can use the Kit Python Script Editor or a standalone script to convert Gaussian Splat assets to USD programmatically.

```python
from usd_convert_gsplat import read_ply, read_spz, write_gaussian_splat_usd

# Read a PLY or SPZ file
splat_data = read_ply("scene.ply")
# splat_data = read_spz("scene.spz")

# Write to USD
write_gaussian_splat_usd(
    splat_data,
    output_path="scene.usdz",
    source_file="scene.ply",          # optional, stored in the layer comment
    prim_name="MyScene",              # optional, defaults to the output file stem
    up_axis="Y",                      # "Y" or "Z"
    rotation_degrees=(0, 0, 0),       # Euler XYZ in degrees
)
```

Inside Kit, the same symbols are re-exported from `omni.kit.converter.gsplat` for convenience:

```python
from omni.kit.converter.gsplat import read_ply, write_gaussian_splat_usd
```
