---
source_id: "SRC-robotics-384"
title: "LightwheelOcc autonomous-driving synthetic dataset"
source_type: "dataset"
publisher: "Lightwheel AI / OpenDriveLab"
source_date: "2024"
url: "https://huggingface.co/datasets/OpenDriveLab/LightwheelOcc"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-06T02:05:23+00:00"
tags:
  - raw/source
  - source-type/dataset
  - evidence/s
aliases:
  - SRC-robotics-384
---
# LightwheelOcc autonomous-driving synthetic dataset

## LightwheelOcc like 4 107

License:

Dataset Viewer

The dataset viewer is not available for this subset.

Cannot get the split names for the config 'default' of the dataset.

```
Exception:    SplitsNotFoundError
Message:      The split names could not be parsed from the dataset config.
Traceback:    Traceback (most recent call last):
                File "/src/services/worker/src/worker/job_runners/config/split_names.py", line 159, in compute
                  compute_split_names_from_info_response(
                File "/src/services/worker/src/worker/job_runners/config/split_names.py", line 131, in compute_split_names_from_info_response
                  config_info_response = get_previous_step_or_raise(kind="config-info", dataset=dataset, config=config)
                File "/src/libs/libcommon/src/libcommon/simple_cache.py", line 567, in get_previous_step_or_raise
                  raise CachedArtifactError(
              libcommon.simple_cache.CachedArtifactError: The previous step failed.
              
              During handling of the above exception, another exception occurred:
              
              Traceback (most recent call last):
                File "/src/services/worker/.venv/lib/python3.9/site-packages/datasets/inspect.py", line 499, in get_dataset_config_info
                  for split_generator in builder._split_generators(
                File "/src/services/worker/.venv/lib/python3.9/site-packages/datasets/packaged_modules/webdataset/webdataset.py", line 88, in _split_generators
                  raise ValueError(
              ValueError: The TAR archives of the dataset should be in WebDataset format, but the files in the archive don't share the same prefix or the same types.
              
              The above exception was the direct cause of the following exception:
              
              Traceback (most recent call last):
                File "/src/services/worker/src/worker/job_runners/config/split_names.py", line 75, in compute_split_names_from_streaming_response
                  for split in get_dataset_split_names(
                File "/src/services/worker/.venv/lib/python3.9/site-packages/datasets/inspect.py", line 572, in get_dataset_split_names
                  info = get_dataset_config_info(
                File "/src/services/worker/.venv/lib/python3.9/site-packages/datasets/inspect.py", line 504, in get_dataset_config_info
                  raise SplitsNotFoundError("The split names could not be parsed from the dataset config.") from err
              datasets.inspect.SplitsNotFoundError: The split names could not be parsed from the dataset config.
```

Need help to make the dataset viewer work? Make sure to review [how to configure the dataset viewer](https://huggingface.co/docs/hub/datasets-data-files-configuration), and [open a discussion](https://huggingface.co/datasets/OpenDriveLab/LightwheelOcc/discussions/new?title=Dataset+Viewer+issue&description=The+dataset+viewer+is+not+working.%0A%0AError+details%3A%0A%0A%60%60%60%0AException%3A++++SplitsNotFoundError%0AMessage%3A++++++The+split+names+could+not+be+parsed+from+the+dataset+config.%0ATraceback%3A++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fsplit_names.py%22%2C+line+159%2C+in+compute%0A++++++++++++++++++compute_split_names_from_info_response%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fsplit_names.py%22%2C+line+131%2C+in+compute_split_names_from_info_response%0A++++++++++++++++++config_info_response+%3D+get_previous_step_or_raise%28kind%3D%22config-info%22%2C+dataset%3Ddataset%2C+config%3Dconfig%29%0A++++++++++++++++File+%22%2Fsrc%2Flibs%2Flibcommon%2Fsrc%2Flibcommon%2Fsimple_cache.py%22%2C+line+567%2C+in+get_previous_step_or_raise%0A++++++++++++++++++raise+CachedArtifactError%28%0A++++++++++++++libcommon.simple_cache.CachedArtifactError%3A+The+previous+step+failed.%0A++++++++++++++%0A++++++++++++++During+handling+of+the+above+exception%2C+another+exception+occurred%3A%0A++++++++++++++%0A++++++++++++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Finspect.py%22%2C+line+499%2C+in+get_dataset_config_info%0A++++++++++++++++++for+split_generator+in+builder._split_generators%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Fpackaged_modules%2Fwebdataset%2Fwebdataset.py%22%2C+line+88%2C+in+_split_generators%0A++++++++++++++++++raise+ValueError%28%0A++++++++++++++ValueError%3A+The+TAR+archives+of+the+dataset+should+be+in+WebDataset+format%2C+but+the+files+in+the+archive+don%27t+share+the+same+prefix+or+the+same+types.%0A++++++++++++++%0A++++++++++++++The+above+exception+was+the+direct+cause+of+the+following+exception%3A%0A++++++++++++++%0A++++++++++++++Traceback+%28most+recent+call+last%29%3A%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2Fsrc%2Fworker%2Fjob_runners%2Fconfig%2Fsplit_names.py%22%2C+line+75%2C+in+compute_split_names_from_streaming_response%0A++++++++++++++++++for+split+in+get_dataset_split_names%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Finspect.py%22%2C+line+572%2C+in+get_dataset_split_names%0A++++++++++++++++++info+%3D+get_dataset_config_info%28%0A++++++++++++++++File+%22%2Fsrc%2Fservices%2Fworker%2F.venv%2Flib%2Fpython3.9%2Fsite-packages%2Fdatasets%2Finspect.py%22%2C+line+504%2C+in+get_dataset_config_info%0A++++++++++++++++++raise+SplitsNotFoundError%28%22The+split+names+could+not+be+parsed+from+the+dataset+config.%22%29+from+err%0A++++++++++++++datasets.inspect.SplitsNotFoundError%3A+The+split+names+could+not+be+parsed+from+the+dataset+config.%0A%60%60%60%0A%0A%0Acc+%40lhoestq+%40cfahlgren1.) for direct support.

## LightwheelOcc

**A 3D Occupancy Synthetic Dataset in Autonomous Driving**

![](https://raw.githubusercontent.com/OpenDriveLab/LightwheelOcc/main/resources/occ_video.gif "Gif loading, please wait..")

> - Point of Contact: [Lightwheel AI](mailto:contact@lightwheel.ai) or [Tianyu (李天羽)](mailto:litianyu@pjlab.org.cn)

## Introduction

- LightwheelOcc, developed by Lightwheel AI, is a publicly available autonomous driving synthetic dataset. The dataset, which includes 40,000 frames and corresponding ground truth labels for a variety of tasks, is a generalized dataset that navigates a variety of regional terrains, weather patterns, vehicle types, vegetation, and roadway demarcations.
- Lightwheel AI levers generative AI and simulation to deliver 3D, physically realistic and generalizable synthetic data solutions for autonomous driving and embodied AI. By publishing LightwheelOcc, we aim to advance research in the realms of computer vision, autonomous driving and synthetic data.

## Highlights

- **Diverse data distributions, including corner cases and hard scenarios**
	- By incorporating complex traffic flows, LightwheelOcc contains diversified simulation of different traffic conditions and driving behaviors. Apart from usual scenarios, the dataset also presents corner cases like small and rare objects on the road, challenging conditions like nighttime and rainy scenes, etc., enriching real-world data diversity.
- **Accurate and dense 3D occupancy and depth label**
- **Realistic sensor configuration simulating nuScenes dataset**

## Data overview

### Basic Information

- The LightwheelOcc dataset contains 40,000 frames, totaling 240,000 images, of which 28,000 frames are used for training scenarios, 6000 frames are used for validation scenarios, and 6000 frames are used for testing scenarios.
- LightwheelOcc includes 6 camera sensor data, as well as labels for different tasks, including 3D Occupancy, Flow and Depth Map.

### Data Sample

| **3D Occupancy** | **Depth Map** |
| --- | --- |
| ![3D Occupancy](https://raw.githubusercontent.com/OpenDriveLab/LightwheelOcc/main/resources/sample_occ.jpeg) | ![Depth Map](https://raw.githubusercontent.com/OpenDriveLab/LightwheelOcc/main/resources/sample_depth.jpeg) |

()

## Related Resources

- [DriveAGI](https://github.com/OpenDriveLab/DriveAGI)
- [OccNet](https://github.com/OpenDriveLab/OccNet) | [OpenScene](https://github.com/OpenDriveLab/OpenScene)

()

Total file size:

186 GB
