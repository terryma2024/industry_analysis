---
source_id: "SRC-robotics-282"
title: "SPIDER official implementation"
source_type: "code_repository"
publisher: "Meta FAIR / SPIDER authors"
source_date: "2026"
url: "https://github.com/facebookresearch/spider"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T02:34:35+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/a
aliases:
  - SRC-robotics-282
---
# SPIDER official implementation

## Overview

Scalable Physics-Informed DExterous Retargeting (SPIDER) is a general framework for physics-based retargeting from human to diverse robot embodiments, including both dexterous hand and humanoid robot. It is designed to be a minimum, flexible and extendable framework for human2robot retargeting. This code base provides the following pipeline from human video to robot actions:

[![pipeline](https://github.com/facebookresearch/spider/raw/main/figs/pipeline_animation.gif)](https://github.com/facebookresearch/spider/blob/main/figs/pipeline_animation.gif)

## Gallery

### Simulation results:

| Inspire Pick Tea Pot (Gigahands Dataset) | Xhand Play Glass (Hot3D dataset) | Schunk Pick Board (Oakink dataset) | Allegro Pick Cat Toy (Reconstructed from single RGB video) |
| --- | --- | --- | --- |
| [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/inspire_pick_pot.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/inspire_pick_pot.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/xhand_glass.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/xhand_glass.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/schunk_move_board.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/schunk_move_board.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/allegro_pick_cat.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/allegro_pick_cat.gif) |

| G1 Pick | G1 Run | H1 Kick | T1 skip |
| --- | --- | --- | --- |
| [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/g1_pick.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/g1_pick.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/g1_run.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/g1_run.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/h1_kick.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/h1_kick.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/t1_skip.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/t1_skip.gif) |

### Multiple viewer support:

| Mujoco | Rerun |
| --- | --- |
| [![](https://github.com/facebookresearch/spider/raw/main/figs/viewers/mujoco_viewer.gif)](https://github.com/facebookresearch/spider/blob/main/figs/viewers/mujoco_viewer.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/viewers/rerun_viewer.gif)](https://github.com/facebookresearch/spider/blob/main/figs/viewers/rerun_viewer.gif) |

### Multiple simulators support:

| Genesis | Mujoco Warp | IsaacGym |
| --- | --- | --- |
| [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/dexmachina.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/dexmachina.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/mjwarp.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/mjwarp.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/sim/maniptrans.gif)](https://github.com/facebookresearch/spider/blob/main/figs/sim/maniptrans.gif) |

### Deployment to real-world robots:

| Pick Cup | Rotate Bulb | Unplug Charger | Pick Duck |
| --- | --- | --- | --- |
| [![](https://github.com/facebookresearch/spider/raw/main/figs/real/pick_cup_real.gif)](https://github.com/facebookresearch/spider/blob/main/figs/real/pick_cup_real.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/real/rotate_bulb_real.gif)](https://github.com/facebookresearch/spider/blob/main/figs/real/rotate_bulb_real.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/real/unplug_real.gif)](https://github.com/facebookresearch/spider/blob/main/figs/real/unplug_real.gif) | [![](https://github.com/facebookresearch/spider/raw/main/figs/real/pick_duck_real.gif)](https://github.com/facebookresearch/spider/blob/main/figs/real/pick_duck_real.gif) |

## Features

- First general **physics-based** retargeting pipeline for both dexterous hand and humanoid robot.
- Supports 9+ robots and 6+ datasets out of the box.
- Seemless integration with RL training and data augmentation for BC pipeline.
- Native support for multiple simulators (Mujoco Wrap, Genesis) and multiple downstream training pipelines (HDMI, DexMachina).
- Sim2real ready.

[![](https://github.com/facebookresearch/spider/raw/main/figs/embodiment_support.png)](https://github.com/facebookresearch/spider/blob/main/figs/embodiment_support.png)

## Quickstart

Clone example datasets:

```
sudo apt install git-lfs
git lfs install
git clone https://huggingface.co/datasets/retarget/retarget_example example_datasets
```

### (Option 1) Quickstart with uv:

Create env and install (make sure `uv` uses Python 3.12, which is what the project targets):

```
uv sync
```

If you already have the example datasets cloned, you can skip the preprocessing step where we convert the human data to robot kinematic trajectories. Pick one of the three reference tasks below — each picks the right `+override=…` Hydra config and the right `task` / `embodiment_type` for that dataset:

```
uv run examples/run_mjwp_fast.py +override=gigahand_fast    task=p36-tea          embodiment_type=bimanual data_id=0 robot_type=xhand
uv run examples/run_mjwp_fast.py +override=arcticv2_fast    task=s01-box_use_01   embodiment_type=bimanual data_id=0 robot_type=xhand
uv run examples/run_mjwp_fast.py +override=oakinkv2_fast    task=pick_spoon_bowl  embodiment_type=right    data_id=0 robot_type=xhand

# To use the original (slower) config from the paper, add the _origin
# suffix to the override (gigahand only ships _origin currently):
uv run examples/run_mjwp.py +override=gigahand_origin task=p36-tea embodiment_type=bimanual
```

> Note: `oakinkv2` is the recommended OakInk pipeline. It loads directly from the official OakInk-v2 raw data, crops each clip to a short window centered on the grasp moment (default: 1.5s pre-grasp + 2.5s post-grasp), and uses the maniptrans-derived right-hand object as the manipulation target. The legacy `oakink` pipeline (which consumes the already-baked maniptrans pickles starting after the grasp) is still available via `+override=oakink`, but for new work prefer `oakinkv2`.

> Note: `arcticv2` reads Arctic raw\_seqs and clips to a 4 s window centered on the object's motion onset (default 2 s pre / 2 s post). Only the object's bottom part is kept (rigid). Tasks are named `<subject>-<sequence>`, e.g. `s01-box_use_01`, `s01-ketchup_use_01`, `s01-laptop_use_01` — see `ARCTIC_OBJECTS` in `spider/process_datasets/arcticv2.py` for the supported objects.

For full workflow, please refer to the [Workflow](#workflow) section.

### (Option 2) Quickstart with conda:

```
conda create -n spider python=3.12
conda activate spider
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install --no-deps -e .
```

Run MJWP on a processed trial:

```
python examples/run_mjwp.py
```

## Workflow

SPIDER is designed to support multiple workflows depending on your simulator of choice and downstream tasks.

- Native Mujoco Wrap (MJWP) is the default workflow and supports dexterous hand and humanoid robot retargeting.
- We also support [Genesis](https://genesis.github.io/) simulator with [DexMachina](https://github.com/MandiZhao/dexmachina), workflow is useful for further training a policy with RL for dexterous hand.
- [HDMI](https://github.com/lecar-lab/hdmi) workflow supports humanoid robot retargeting + RL workflow with humanoid-object interaction tasks. It use [MjLab](https://github.com/mujocolab/mjlab) as its backend simulator.
- [ManipTrans](https://github.com/ManipTrans/ManipTrans) workflow supports dexterous hand retargeting with IsaacGym.

### Native Mujoco Wrap Workflow

Please refer to [Native Mujoco Wrap workflow](https://github.com/facebookresearch/spider/blob/main/docs/workflows/workflow-mjwp.md) for details.

- supports dexterous hand and humanoid robot retargeting

The pipeline is the same for every dataset: `process_datasets → decompose(_fast) → [detect_contact] → generate_xml → ik(_fast) → run_mjwp(_fast) → [read_to_robot]`. Only step 1 (the dataset processor) is dataset-specific. Below, one canonical task per dataset.

```
TASK=p36-tea
HAND_TYPE=bimanual
DATA_ID=0
ROBOT_TYPE=xhand
DATASET_NAME=gigahand

# raw data lives under ${dataset_dir}/raw/gigahand/

# 1. read raw dataset → unified NPZ schema
# Gigahand — bimanual tea-pot pour (p36-tea)
uv run examples/run_mjwp.py +override=gigahand \
    task=p36-tea embodiment_type=bimanual data_id=0 robot_type=xhand

# Arctic-v2 — bimanual box pick (s01/box_use_01)
uv run examples/run_mjwp.py +override=arcticv2 \
    task=s01-box_use_01 embodiment_type=bimanual data_id=0 robot_type=xhand

# OakInk-v2 — right-hand spoon pick (pick_spoon_bowl)
uv run examples/run_mjwp.py +override=oakinkv2 \
    task=pick_spoon_bowl embodiment_type=right data_id=0 robot_type=xhand

# 2. decompose object
# default uses CoACD (accurate but slow); decompose_fast.py is a heuristic alternative
uv run spider/preprocess/decompose.py     --task=${TASK} --dataset-name=${DATASET_NAME} --data-id=${DATA_ID} --embodiment-type=${HAND_TYPE}

# 3. (optional) detect contact
uv run spider/preprocess/detect_contact.py --task=${TASK} --dataset-name=${DATASET_NAME} --data-id=${DATA_ID} --embodiment-type=${HAND_TYPE}

# 4. generate scene XML
uv run spider/preprocess/generate_xml.py   --task=${TASK} --dataset-name=${DATASET_NAME} --data-id=${DATA_ID} --embodiment-type=${HAND_TYPE} --robot-type=${ROBOT_TYPE}

# 5. kinematic retargeting (mink-based fast IK; ik.py is the slower paper version)
uv run spider/preprocess/ik_fast.py        --task=${TASK} --dataset-name=${DATASET_NAME} --data-id=${DATA_ID} --embodiment-type=${HAND_TYPE} --robot-type=${ROBOT_TYPE}

# 6. physics retargeting
uv run examples/run_mjwp.py      +override=${DATASET_NAME}      task=${TASK} data_id=${DATA_ID} robot_type=${ROBOT_TYPE} embodiment_type=${HAND_TYPE}
# faster, sampling-based variant:
uv run examples/run_mjwp_fast.py +override=${DATASET_NAME}_fast task=${TASK} data_id=${DATA_ID} robot_type=${ROBOT_TYPE} embodiment_type=${HAND_TYPE}

# 7. (optional) export for robot deployment
uv run spider/postprocess/read_to_robot.py --task=${TASK} --dataset-name=${DATASET_NAME} --data-id=${DATA_ID} --robot-type=${ROBOT_TYPE} --embodiment-type=${HAND_TYPE}
```

> Headless rendering: `ik_fast.py` and `run_mjwp_fast.py` save MP4 previews via `mujoco.Renderer`. On a machine without a display, prefix the command with `MUJOCO_GL=egl` (or `osmesa`) — otherwise GLFW fails to init and the run aborts before saving.

### DexMachina Workflow

Please refer to [DexMachina workflow](https://github.com/facebookresearch/spider/blob/main/docs/workflows/workflow-dexmachina.md) for details.

```
# install dexmachina conda environment following their official instructions: https://mandizhao.github.io/dexmachina-docs/0_install.html
conda activate dexmachina
# note: install spider only without mujoco warp since we only use the optimization part
pip install --ignore-requires-python --no-deps -e .
# run retargeting
python examples/run_dexmachina.py
```

### HDMI Workflow

Please refer to [HDMI workflow](https://github.com/facebookresearch/spider/blob/main/docs/workflows/workflow-hdmi.md) for details.

```
# install HDMI uv environment following their official instructions:
# go to hdmi folder, install SPIDER with
uv pip install --no-deps -e ../spider
```

### ManipTrans Workflow

Please refer to [ManipTrans workflow](https://github.com/facebookresearch/spider/blob/main/docs/workflows/workflow-maniptrans.md) for details.

```
# install maniptrans conda environment following their official instructions: https://github.com/ManipTrans/ManipTrans
conda activate maniptrans
# note: install spider only without mujoco warp since we only use the optimization part
pip install --ignore-requires-python --no-deps -e .
# run retargeting
python examples/run_maniptrans.py
```

## Remote Development

```
# start rerun server
uv run rerun --serve-web --port 9876

# run SPIDER only with rerun viewer
uv run examples/run_mjwp.py viewer="rerun"
```

## License

SPIDER is released under the Creative Commons Attribution-NonCommercial 4.0 license. See `LICENSE` for details.

## Code of Conduct

We expect everyone to follow the Contributor Covenant Code of Conduct in `CODE_OF_CONDUCT.md` when participating in this project.

## Acknowledgments

- Thanks Mandi Zhao for the help with the [DexMachina workflow](https://github.com/MandiZhao/dexmachina) for SPIDER + Genesis.
- Thanks Taylor Howell for the help in the early stages of integrating [Mujoco Wrap](https://github.com/google-deepmind/mujoco_warp) for SPIDER + MJWP.
- Thanks Haoyang Weng for the help with the [HDMI workflow](https://github.com/lecar-lab/hdmi) for SPIDER + Sim2real RL.
- Inverse kinematics design is ported from [GMR](https://github.com/YanjieZe/GMR) and [LocoMujoco](https://github.com/robfiras/loco-mujoco).
- Dataset processing is ported from [Hot3D](https://github.com/facebookresearch/hot3d), [Oakinkv2](https://github.com/oakink/OakInk2), [Maniptrans](https://github.com/ManipTrans/ManipTrans), [Gigahands](https://github.com/Gigahands/Gigahands).
- Visualization inspired by other good sampling repo like [Hydrax](https://github.com/vincekurtz/hydrax) and [Judo](https://github.com/bdaiinstitute/judo).

## Citation

```
@article{pan2025spiderscalablephysicsinformeddexterous,
      title={SPIDER: Scalable Physics-Informed Dexterous Retargeting},
      ={Chaoyi Pan and Changhao Wang and Haozhi Qi and Zixi Liu and Homanga Bharadhwaj and Akash Sharma and Tingfan Wu and Guanya Shi and Jitendra Malik and Francois Hogan},
      year={2025},
      eprint={2511.09484},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2511.09484},
}
```
