---
source_id: "SRC-robotics-714"
title: "NVIDIA monocular neural reconstruction workflow"
source_type: "documentation"
publisher: "NVIDIA"
source_date: "2026-11-10"
url: "https://docs.nvidia.com/nurec/robotics/neural_reconstruction_mono.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-11-10T02:19:51+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-714
---
# NVIDIA monocular neural reconstruction workflow

## Reconstruct Scenes from Mono Camera Data

## Overview

This reference workflow enables you to reconstruct a scene using a single camera (mono camera) sensor. This approach works with various camera types including smartphones (iPhone, Android), DSLR cameras, mirrorless cameras, action cameras, or any mono camera sensor capable of capturing still images. It’s ideal for quick prototyping and testing scenarios where specialized hardware like stereo camera rigs is not available. The reference workflow uses COLMAP for structure-from-motion and 3DGUT for neural reconstruction to create photorealistic 3D scenes that can be loaded into Isaac Sim.

## Prerequisites

### Hardware and Software Requirements

**Camera/Sensor:**

- Mono camera sensor (single camera)
- Examples: Smartphones (iPhone, Android), DSLR cameras, mirrorless cameras, action cameras, or any camera capable of capturing still images
- Recommended: Manual control over focus, exposure, and ISO for best results

**Processing System:**

- Linux system with CUDA 11.8, GCC ≤ 11, and NVIDIA GPU
- COLMAP (Structure-from-Motion software)
- 3DGUT repository
- Isaac Sim 5.0 or later

## Workflow Steps

### Step 1: Capture the Real-World Scene

Take photos of the environment you want to reconstruct using your mono camera sensor. The following photogrammetry best practices apply to any camera type, with specific examples provided for smartphones and DSLR/mirrorless cameras.

#### Lighting and Focus (All Camera Types)

- Ensure steady lighting and proper focus
- Avoid fast motion and blur
- Use faster shutter speed (1/100 second or faster recommended)
- Lock focus and exposure to maintain consistency across shots
- Use a tripod or stabilization when possible

#### Camera Settings

**For DSLR/Mirrorless Cameras:**

- **Manual mode**: Use manual mode (M) for full control
- **Shutter speed**: 1/120–1/250s outdoors, ≥1/100s indoors
- **ISO**: Keep as low as possible (ISO 100-400) while maintaining proper exposure
- **Aperture**: f/8-f/11 for good depth of field
- **White balance**: Lock white balance to avoid color shifts
- **Focus**: Use manual focus or single-point autofocus, then lock focus
- **Format**: Shoot in RAW or highest quality JPEG

**For Smartphone Built-in Camera App:**

If using the built-in camera app on your smartphone:

- **Lock focus/exposure**: On iPhone, long-press on the subject to enable AE/AF Lock. On Android, tap to focus and look for a lock icon or manual mode option
- **Adjust exposure**: If available, reduce exposure slightly (-0.3 to -0.7 EV) to keep highlights crisp
- **Stabilize**: Use a tripod or lean against a wall for stability; the sharper each frame, the better COLMAP tracks features
- **Avoid auto features**: Disable auto macro switching (iPhone Pro Settings → Camera → Auto Macro) or similar auto-focus features that may change focal length between shots

**For Smartphone Manual Camera Apps:**

For better control over smartphone cameras, use apps that allow manual shutter and ISO control:

**iOS Apps:**

- Lumina: Manual Camera
- Halide
- ProCamera
- ProCam 8
- Moment Pro Camera
- Lightroom Mobile

**Android Apps:**

- Camera FV-5
- Open Camera
- Manual Camera
- Lightroom Mobile

**Smartphone Recommended Settings:**

- **Shutter speed**: 1/120–1/250s outdoors, ≥1/100s indoors
- **ISO**: As low as possible while maintaining acceptable exposure
- **White balance**: Lock white balance to avoid color shifts between frames

**For Action Cameras (e.g., GoPro):**

- Use photo mode (not video stills)
- Disable electronic image stabilization for photogrammetry
- Lock exposure if available
- Use timer or remote trigger to avoid camera shake

#### Coverage and Overlap (All Camera Types)

- Make a slow loop around the area
- Capture multiple heights and angles
- Maintain approximately **60% overlap** between shots
- Take more photos rather than fewer—COLMAP will handle redundant images

> [!tip] Tip
> COLMAP expects standard image formats (JPEG, PNG). If your phone saves images in other formats (like HEIC on iPhone), either switch to a compatible format in your camera settings (iPhone: Settings → Camera → Formats → Most Compatible), or export/convert to JPG before processing with COLMAP.

### Step 2: Generate Sparse Reconstruction with COLMAP

COLMAP creates a sparse point cloud and estimates camera parameters from your photos using Structure-from-Motion (SfM) techniques.

#### Using COLMAP Command Line

For more control or automation, use the command-line interface:

```bash
# Feature detection & extraction
$ colmap feature_extractor \
    --database_path ./colmap/database.db \
    --image_path    ./images/ \
    --ImageReader.single_camera 1 \
    --ImageReader.camera_model   PINHOLE \
    --SiftExtraction.max_image_size 2000 \
    --SiftExtraction.estimate_affine_shape 1 \
    --SiftExtraction.domain_size_pooling 1

# Feature matching
$ colmap exhaustive_matcher \
    --database_path ./colmap/database.db \
    --SiftMatching.use_gpu 1

# Global SFM
$ colmap mapper \
    --database_path ./colmap/database.db \
    --image_path    ./images/ \
    --output_path   ./colmap/sparse

# Visualize for verification
$ colmap gui --import_path ./colmap/sparse/0 \
    --database_path ./colmap/database.db \
    --image_path    ./images/
```

**Command Parameters:**

- `database_path`: Path to COLMAP database file
- `image_path`: Directory containing your photos
- `ImageReader.single_camera`: Assumes all images from same camera
- `ImageReader.camera_model`: Camera model (PINHOLE for 3DGUT compatibility)
- `SiftExtraction.max_image_size`: Maximum image dimension for feature extraction
- `output_path`: Directory for reconstruction output

#### COLMAP Output

Once complete, you’ll have:

- **Sparse point cloud** of the scene
- **Camera pose data** for all images
- **Project folder** containing:
	- `database.db`: COLMAP database
		- `images/`: Original photos
		- `sparse/`: Reconstruction data (cameras.txt, images.txt, points3D.txt)

This is the information needed for 3DGUT reconstruction in Step 3.

> [!note] Note
> For more information, see the [COLMAP Documentation](https://colmap.github.io/).

### Step 3: Train Dense 3D Reconstruction with 3DGUT

3DGUT (3D Gaussian Ray Tracing) turns the sparse COLMAP model and images into a dense, photorealistic 3D scene using Gaussian splatting.

#### Set up 3DGUT Environment

**Requirements:**

- Linux system with CUDA 11.8
- GCC ≤ 11
- NVIDIA GPU

**Clone and Install 3DGUT:**

```bash
$ git clone --recursive https://github.com/nv-tlabs/3dgrut.git
$ cd 3dgrut
$ chmod +x install_env.sh
$ ./install_env.sh 3dgrut
$ conda activate 3dgrut
```

> [!tip] Tip
> Verify installation by running a test reconstruction on one of the sample datasets included in the repository before processing your own data.

**GCC 11 Installation (if needed):**

If your system uses GCC 12 or newer (e.g., Ubuntu 24.04), install GCC 11 inside the Conda environment:

```bash
$ conda install -c conda-forge gcc=11 gxx=11
```

#### Run 3DGUT Training and Export to USDZ

This example uses the COLMAP + 3DGUT + MCMC configuration. The MCMC (Markov Chain Monte Carlo) densification strategy adaptively samples uncertain regions to sharpen thin structures and improve overall reconstruction fidelity.

```bash
$ conda activate 3dgrut
$ python train.py --config-name apps/colmap_3dgut_mcmc.yaml \
    path=/path/to/colmap/ \
    out_dir=/path/to/out/ \
    experiment_name=3dgut_mcmc \
    export_usdz.enabled=true \
    export_usdz.apply_normalizing_transform=true
```

**Configuration Parameters:**

- `config-name` *(required)*: Configuration file (enables MCMC densification)
- `path` *(required)*: Path to COLMAP output directory
- `out_dir` *(required)*: Directory for 3DGUT training outputs
- `experiment_name` *(required)*: Custom name for the training run
- `export_usdz.enabled` *(optional)*: Set to `true` to export USDZ file for Isaac Sim
- `export_usdz.apply_normalizing_transform` *(optional)*: Set to `true` to center and scale the scene

#### Training Process

Once you run the command, 3DGUT will begin training:

- Reads your images and COLMAP data
- Optimizes a 3D Gaussian representation
- Duration varies from a few minutes (small scenes) to several hours (detailed scenes)
- Progress is logged to the console

#### Training Output

When complete, the output directory will contain:

- `ckpt_last.pt`: Final model checkpoint
- `export_last.inpg`: Intermediate representation
- `parsed.yaml`: Training configuration
- `ours_xxxxx/`: Iteration-specific outputs
- `export_last.usdz`: Final USDZ file for Isaac Sim

#### USD Export Details

The exported USDZ file:

- Uses a custom USD schema for Gaussian splatting data
- Is a packaged USD scene ready for Isaac Sim
- Contains all 3D reconstruction information

> [!note] Note
> The `apply_normalizing_transform` option applies primitive normalization (centers and scales the scene near the origin). It does **not** guarantee the floor is exactly at z = 0. You may need to adjust scene alignment in Isaac Sim.

### Step 4: Deploy in Isaac Sim

Now you can load your reconstructed scene into Isaac Sim and add robots for simulation.

#### Launch Isaac Sim

1. Launch **Isaac Sim** (version 5.0 or later, which supports NuRec/3DGUT features)
2. Start with an empty stage: **File → New**

#### Import USD Scene

**Option 1: File Menu**

1. Navigate to **File → Import**
2. Select your USDZ file (`export_last.usdz`)
3. Click Open

**Option 2: Drag and Drop**

1. Locate the USDZ file in Isaac Sim content browser
2. Drag and drop it into the viewport

The reconstructed environment will appear as a collection of colorful Gaussians, creating an almost photoreal 3D representation.

> [!tip] Tip
> Use WASD keys or right-click and drag to navigate around the scene and inspect it from different angles.

#### Add Ground Plane for Physics

Your reconstructed scene is visual geometry only—it has no inherent collision properties. Add a ground plane so robots have something to stand on:

1. Click **Create → Physics → Ground Plane**
2. A flat ground will appear (usually at Z = 0)
3. Scale the plane (e.g., X=100, Y=100) to cover your scene’s floor area
4. Adjust **Translate/Rotate/Scale** properties to align with the reconstructed floor

#### Connect Proxy Mesh for Shadows

A proxy mesh provides a surface for shadow casting, grounding objects visually in the scene:

1. Select the **NuRec prim** (the volume prim under the global xform)
2. In the **Raw USD Properties** panel, locate the **NuRec/Volume** section
3. Find the **Proxy** field and click **+** to add your proxy mesh prim
4. Select your ground plane again
5. Ensure that **Geometry → Matte Object** property is enabled

#### Insert a Robot

Isaac Sim includes many SimReady robot models:

1. Navigate to **Create → Robots** in the top menu bar
2. Choose a robot:
	- **Manipulator arms**: Franka Emika Panda, UR10, etc.
		- **Mobile robots**: LeatherBack, Carter, TurtleBot
		- **Humanoids**: Various humanoid models
3. The robot will be added to your scene
4. Use **Move/Rotate** tools to position the robot where you want it

#### Press Play and Test

1. Click the **Play** button
2. The robot should interact with your photorealistic 3D scene
3. You can now:
	- Animate the robot
		- Run reinforcement learning
		- Test navigation algorithms
		- Generate synthetic data

## Tips and Best Practices

### Camera Capture Tips (All Camera Types)

- **More is better**: Capture more photos than you think you need
- **Coverage**: Ensure all areas of interest are covered from multiple angles
- **Consistency**: Maintain consistent lighting throughout the capture session
- **Avoid reflections**: Be mindful of reflective surfaces and windows
- **Motion blur**: Keep the camera as steady as possible during capture
- **Camera settings**: Keep camera settings (focal length, focus, exposure) as consistent as possible
- **Lens choice** (DSLR/Mirrorless): Use fixed focal length lenses when possible; avoid zoom during capture

### COLMAP Optimization

- **Image resolution**: Higher resolution images provide better features but increase processing time
- **Camera model**: Use `pinhole` or `simple pinhole` for 3DGUT compatibility
- **Feature matching**: Use GPU acceleration (`--SiftMatching.use_gpu 1`) for faster processing
- **Verification**: Always visualize the COLMAP output before proceeding to 3DGUT

### 3DGUT Training

- **GPU memory**: Larger scenes require more GPU memory
- **Training time**: Start with smaller test scenes to verify the pipeline
- **Checkpoints**: Training checkpoints are saved periodically—you can resume if interrupted
- **Quality vs. speed**: MCMC configuration provides better quality with modest time overhead

### Isaac Sim Integration

- **Ground alignment**: Manually adjust the scene position if the floor doesn’t align with z=0
- **Collision setup**: Set up collision properties on the ground plane for robot interaction
- **Lighting**: Add additional lights if needed to complement the reconstructed scene
- **Robot scale**: Ensure robot models are at appropriate scale relative to the scene

## Troubleshooting

### COLMAP Issues

**Problem**: COLMAP fails to reconstruct the scene

**Solutions**:

- Ensure sufficient overlap between images (60%+)
- Check that images are in focus and not motion-blurred
- Verify consistent camera settings (focal length, focus) across all images
- Try different camera models (pinhole vs. simple pinhole)
- For DSLR/mirrorless: Ensure EXIF data is preserved (contains focal length information)
- Reduce `max_image_size` if running out of memory

**Problem**: Sparse point cloud is incomplete

**Solutions**:

- Capture additional photos from missing angles
- Increase `max_num_features` in feature extraction
- Check lighting conditions in problematic areas

### 3DGUT Issues

**Problem**: Out of GPU memory during training

**Solutions**:

- Reduce image resolution before COLMAP reconstruction
- Use a GPU with more memory
- Adjust training batch size in configuration

**Problem**: Reconstruction quality is poor

**Solutions**:

- Ensure COLMAP reconstruction is high quality
- Capture better source images with more overlap
- Increase training iterations
- Use MCMC configuration for better quality

### Isaac Sim Issues

**Problem**: Scene appears at wrong scale

**Solutions**:

- Apply the normalizing transform during export
- Manually scale the scene root in Isaac Sim
- Verify camera parameters in COLMAP

**Problem**: Robot falls through the ground

**Solutions**:

- Ensure ground plane has collision properties enabled
- Check that ground plane is positioned at correct height
- Verify physics settings in Isaac Sim

## Additional Resources

**Documentation**

**Sample Scenes**

- [Physical AI Collection on Hugging Face](https://huggingface.co/collections/nvidia/physical-ai-67c643edbb024053dcbcd6d8)

**Tutorials**

**Community**
