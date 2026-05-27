---
source_id: "SRC-robotics-068"
title: "UMI Robot Dataset Community"
source_type: "data_format"
publisher: "UMI community"
source_date: "2026"
url: "https://umi-data.github.io/"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-05-27T01:34:04+00:00"
tags:
  - raw/source
  - source-type/data-format
  - evidence/a
aliases:
  - SRC-robotics-068
---
# UMI Robot Dataset Community

## UMI is a physical and policy interface that allows robot data to be shared between many robots.

## The best part? With just a GoPro and a 3D printed gripper, any new robot platform can get up and running with UMI policies without any robot-specific data collection!

UMI is a physical and policy interface that allows robot data to be shared between many robots.

**The best part?** With just a GoPro and a 3D printed gripper, any new robot platform can get up and running with UMI policies without any robot-specific data collection!

![UMI Dataset Statistics](https://umi-data.github.io/plots/stat.png)

UMI Dataset Statistics

## Community Principles

### 📈 No dataset is too small; small data adds up.

Even a simple, single-task dataset with 50 demonstrations is valuable. As long as you're happy to share it, we are happy to list it here. Every bit of data contributes to the community's collective knowledge.

### 🤝 Any UMI-like Dataset is welcome!

There's no strict definition of UMI data. You are encouraged to contribute datasets even if they don't follow the same hardware or data format. UMI is a constantly evolving design, and welcome enhancements like new sensor modalities (e.g., [ManiWav](https://mani-wav.github.io/)), finger designs, or cameras (e.g., [fastUMI](https://fastumi.com/)). Even if your data is not directly transferable to the current UMI setup, it can still be useful for pretraining or other creative applications. If it can benefit the robot learning community, it's worth listing!

## Datasets

| Project Name | Contact | Task | Data Links | Obs | Actions | \# Demos | \# Envs | License | Notes | Citation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 📋 Listing Your Data

If you would like your data to be listed here, please provide the following information:

- **Project:** The name of the project and link to the project website for additional context.
- **License:** The licensing terms under which the data is distributed (e.g., MIT, GPL, CC BY 4.0).
- **Citation:** Information on how to properly cite the dataset if used.
- **Contact person:** The name and email of the individual responsible for the dataset.
- **Tasks**:
	- **Metadata:** This includes the task name, the observations (e.g., Image, Proprio, Audio, Bimanual), and the actions (e.g., 6 DoF End Effector, Parallel Gripper, Bimanual).
		- **Link to Data:** A direct link to where each of the data formats can be accessed. For instance, the link for MP4 might be a Zarr link, while the link for a Zarr file might be hosted on the project's webserver. If you're unsure of which data format to use, consider using/extending the [UMI data format](#data-format).
		- **Number of demonstrations:** The number of demonstrations in the dataset.
		- **Number of environments:** The number of environments in which the data was collected.

Please send this information to [huyha@stanford.edu](mailto:huyha@stanford.edu) for review and inclusion in our listing.

**Disclaimer:** We only provide a list of references to existing data for researchers to easily search and find datasets. We do not own or host the datasets listed here. For questions about specific datasets, please reach out to the project owners directly.

## 📚 UMI Dataset Format

UMI has multiple tiers of data storage formats:

- **GoPro**: Just a folder of GoPro MP4s:)
- **SLAM** Output of ORB\_SLAM3 pipeline (volatile)
- **Zarr** A single zip file optimized for fast random reading for training.

### Zarr data format

Following [Diffusion Policy](https://diffusion-policy.cs.columbia.edu/), UMI uses [Zarr](https://zarr.dev/) as the container for training datasets. Zarr is similar to [HDF5](https://docs.hdfgroup.org/hdf5/v1_14/_intro_h_d_f5.html) but offers better flexibility for storage backends, chunking, compressors, and parallel access.

Conceptually, Zarr can be understood as a nested `dict` of "numpy arrays". For example, here is the structure of the `example_demo_session` dataset.

```python
import Zarr
from diffusion_policy.codecs.imagecodecs_numcodecs import register_codecs, JpegXl
register_codecs()

root = zarr.open('example_demo_session/dataset.zarr.zip')
print(root.tree())
>>>
/
 ├── data
 │   ├── camera0_rgb (2315, 224, 224, 3) uint8
 │   ├── robot0_demo_end_pose (2315, 6) float64
 │   ├── robot0_demo_start_pose (2315, 6) float64
 │   ├── robot0_eef_pos (2315, 3) float32
 │   ├── robot0_eef_rot_axis_angle (2315, 3) float32
 │   └── robot0_gripper_width (2315, 1) float32
 └── meta
     └── episode_ends (5,) int64
```

#### ReplayBuffer

We implemented the `ReplayBuffer` class to access Zarr data conveniently.

```python
from diffusion_policy.common.replay_buffer import ReplayBuffer

replay_buffer = ReplayBuffer.create_from_group(root)
replay_buffer.n_episodes
>>> 5

# reading an episode
ep = replay_buffer.get_episode(0)
ep.keys()
>>> dict_keys(['camera0_rgb', 'robot0_demo_end_pose', 'robot0_demo_start_pose', 'robot0_eef_pos', 'robot0_eef_rot_axis_angle', 'robot0_gripper_width'])

ep['robot0_gripper_width']
>>>
array([[0.07733118],
       [0.07733118],
       [0.07734068],
...
       [0.08239228],
       [0.08236252],
       [0.0823558 ]], dtype=float32)
```

#### Data Group

In `root['data']` "dict," we have a group of arrays containing demonstration episodes concatenated along the first dimension (time/step). In this dataset, we have 2315 steps across five episodes. In UMI, data has a frame rate of 60Hz (59.94Hz), matching the recording frame rate of GoPros. All arrays in `root['data']` must have the same size in their first (time) dimension.

```python
root['data']['robot0_eef_pos']
>>> <zarr.core.Array '/data/robot0_eef_pos' (2315, 3) float32>

root['data']['robot0_eef_pos'][0]
>>> array([ 0.1872826 , -0.35130176,  0.1859438 ], dtype=float32)

root['data']['robot0_eef_pos'][:]
>>>
array([[ 0.1872826 , -0.35130176,  0.1859438 ],
       [ 0.18733297, -0.3509169 ,  0.18603411],
       [ 0.18735182, -0.3503186 ,  0.18618457],
       ...,
       [ 0.12694108, -0.3326249 ,  0.13230264],
       [ 0.12649481, -0.3347473 ,  0.1347403 ],
       [ 0.12601827, -0.33651358,  0.13699797]], dtype=float32)
```

#### Metadata Group

How do we know the start and end of each episode? We store an integer array `root['meta']['episode_ends']` that contains each episode's `end` index into `data` arrays. For example, the first episode can be accessed with `root['data']['robot0_eef_pos'][0:468]` and the second episode can be accessed with `root['data']['robot0_eef_pos'][468:932]`.

```python
root['meta']['episode_ends'][:]
>>> array([ 468,  932, 1302, 1710, 2315])
```

#### Data Array Chunking and Compression

Note that all arrays in the dataset are of type `zarr.core.Array` instead of `numpy.ndarray`. While offering similar API to numpy arrays, Zarr arrays are optimized for fast on-disk storage with *chunked compression*. For example, camera images `root['data']['camera0_rgb']` is stored with chunk size `(1, 224, 224, 3)` and `JpegXl` compression. When reading from a Zarr array, a chunk of data is loaded from disk storage and decompressed to a numpy array.

**💡** For optimal performance, the chunk size has to be chosen carefully. A chunk size too big means that the data loader will decompress the data more than necessary (e.g., chunks=(100, 224, 244, 3) will decompress and discard 99 images when accessing \[0\]). In contrast, having the chunk size too small will incur additional overhead and reduce compression rate (e.g., chunks=(1,14,14,3) means each image is split into 256 chunks).

```python
root['data']['camera0_rgb']
>>> <zarr.core.Array '/data/camera0_rgb' (2315, 224, 224, 3) uint8>

root['data']['camera0_rgb'].chunks # chunk size
>>> (1, 224, 224, 3)

root['data']['camera0_rgb'].nchunks # number of chunks
>>> 2315

root['data']['camera0_rgb'].compressor
>>> JpegXl(decodingspeed=None, distance=None, effort=None, index=None, keeporientation=None, level=99, lossless=False, numthreads=1, photometric=None, planar=None, usecontainer=None)

root['data']['camera0_rgb'][0]
>>>
array([[[ 7,  6, 15],
        [ 7,  6, 15],
        [ 4,  4, 13],
        ...,
        [ 6,  7, 15],
        [ 4,  7, 14],
        [ 3,  6, 13]],

       ...,

       [[ 0,  0,  0],
        [ 0,  0,  0],
        [ 0,  0,  0],
        ...,
        [ 0,  0,  0],
        [ 0,  0,  0],
        [ 0,  0,  0]]], dtype=uint8)
```

We use a relatively large chunk size for low-dimensional data. Since these data are cached into a numpy array inside `UmiDataset,` no read IOPS overhead is introduced.

```python
root['data']['robot0_eef_pos'].chunks
>>> (468, 3)

root['data']['robot0_eef_pos'].compressor # uncompressed chunks
>>> None
```

#### In-memory Compression

During training, streaming datasets from a network drive is often bottlenecked by [IOPS](https://en.wikipedia.org/wiki/IOPS), especially when multiple GPUs/nodes are reading from the same network drive. While loading the entire dataset to memory works around the IOPS bottleneck, an uncompressed UMI dataset often does not fit in RAM.

We found streaming *compressed* datasets from RAM a good tradeoff between memory footprint and read performance.

```python
root.store
>>> <zarr.storage.ZipStore at 0x76b73017d400>

ram_store = zarr.MemoryStore()
# load stored chunks in bytes directly to memory, without decompression
zarr.convenience.copy_store(root.store, ram_store)
ram_root = zarr.group(ram_store)
print(ram_root.tree())
>>>
/
 ├── data
 │   ├── camera0_rgb (2315, 224, 224, 3) uint8
 │   ├── robot0_demo_end_pose (2315, 6) float64
 │   ├── robot0_demo_start_pose (2315, 6) float64
 │   ├── robot0_eef_pos (2315, 3) float32
 │   ├── robot0_eef_rot_axis_angle (2315, 3) float32
 │   └── robot0_gripper_width (2315, 1) float32
 └── meta
     └── episode_ends (5,) int64

# loading compressed data to RAM with ReplayBuffer
ram_replay_buffer = ReplayBuffer.copy_from_store(
    root.store,
    zarr.MemoryStore()
)
ep = ram_replay_buffer.get_episode(0)
```
