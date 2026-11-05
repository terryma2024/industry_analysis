---
source_id: "SRC-robotics-573"
title: "Isaac Sim 6 Neural Volume Rendering"
source_type: "technical_documentation"
publisher: "NVIDIA Isaac Sim"
source_date: "2026-09-22"
url: "https://docs.isaacsim.omniverse.nvidia.com/6.0.0/assets/usd_assets_nurec.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:52:16+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-573
---
# Isaac Sim 6 Neural Volume Rendering

## Neural Volume Rendering

NuRec (Neural Reconstruction) enables scene rendering in Omniverse using neural volumes derived from real-world images. Compatible environments are published as USD stages that use OpenUSD **ParticleField** geometry (3D Gaussian splats and related radiance fields), which Omniverse RTX renders natively together with polygonal scene content. For renderer behavior, import guidance, shadows, and color handling for particle fields, see [Gaussian Splats (Particle Fields)](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/particle-fields.html#particle-fields) in the Omniverse Materials and Rendering documentation.

For NuRec-specific data preparation, reconstruction, rendering, and integration with Omniverse applications such as Isaac Sim, see the [NVIDIA Omniverse NuRec documentation](https://docs.nvidia.com/nurec/). To train splats and export **ParticleField** USD stages for Omniverse, use the open-source [3DGruT](https://github.com/nv-tlabs/3dgrut) project.

## Example

![NuRec Carter NavigationScene](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/_images/isim_5.0_full_tut_viewport_usd_nurec_assets_carter.webp)

NuRec Carter NavigationScene

The following examples show how to load a NuRec USD scene into Isaac Sim and run a simulation. Use `nurec_carter_script_editor.py` from the [Script Editor](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/development_tools/omniverse_script_editor.html#script-editor) or `nurec_carter.py` as a [Standalone Application](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/introduction/workflows.html#standalone-application). Each script iterates over the configured scenarios, opens the stage, loads the Carter navigation asset and sets the start location, optionally creates a collision ground plane at the spawn location, sets the navigation target, and steps the timeline so the wheeled robot drives toward the target.

> [!note] Note
> - Rendering particle fields with DLSS Frame Generation enabled may show visual artifacts. If that happens, disable Frame Generation in Rendering Settings. See [Gaussian Splats (Particle Fields)](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/particle-fields.html#particle-fields).

### Prerequisites

- Download the NVIDIA NuRec Dataset from [Hugging Face](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-NuRec).
- Update the `USER_PATH` variable in both scripts: `USER_PATH = "/home/user/PhysicalAI-Robotics-NuRec"`

Script Editor

```python
import asyncio
import os

import omni.kit.app
import omni.kit.commands
import omni.timeline
import omni.usd
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path_async
from pxr import PhysxSchema, UsdGeom, UsdPhysics

# User path of the HF NuRec dataset
USER_PATH = "/home/user/PhysicalAI-Robotics-NuRec"

# Paths for loading and placing the Nova Carter navigation asset and its target.
NOVA_CARTER_NAV_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
NOVA_CARTER_NAV_USD_PATH = "/World/NovaCarterNav"
NOVA_CARTER_NAV_TARGET_PATH = f"{NOVA_CARTER_NAV_USD_PATH}/targetXform"
# Scenarios for testing navigation in the environments
EXAMPLE_CONFIGS = [
    {
        "name": "Andoria",
        "stage_url": f"{USER_PATH}/hand_hold-endeavor-andoria/stage_particle.usdz",
        "nav_start_loc": (0.0, 0.5, 0.0),
        "nav_relative_target_loc": (0.0, 6.0, 0.0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Wormhole",
        "stage_url": f"{USER_PATH}/hand_hold-endeavor-wormhole/stage_particle.usdz",
        "nav_start_loc": (5, 0, 0),
        "nav_relative_target_loc": (0, -4, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Cafe",
        "stage_url": f"{USER_PATH}/nova_carter-cafe/stage_particle.usdz",
        "nav_start_loc": (0, 0, 0),
        "nav_relative_target_loc": (-3, -1.5, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Galileo",
        "stage_url": f"{USER_PATH}/nova_carter-galileo/stage_particle.usdz",
        "nav_start_loc": (-2.5, 2.5, 0),
        "nav_relative_target_loc": (4, 0, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
]

async def run_example_async(example_config):
    example_name = example_config.get("name")
    print(f"Running example: '{example_name}'")

    # Open the stage
    stage_url = example_config.get("stage_url")
    if not stage_url:
        print(f"Stage URL not provided, exiting")
        return
    if not os.path.exists(stage_url):
        print(f"Stage URL does not exist: '{stage_url}', exiting")
        return

    print(f"Opening stage: '{stage_url}'")
    await omni.usd.get_context().open_stage_async(stage_url)
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        print(f"Failed to open stage: '{stage_url}', exiting")
        return

    # Make sure the physics scene is set to synchronous for the navigation to work
    for prim in stage.Traverse():
        if prim.IsA(UsdPhysics.Scene):
            physx_scene = PhysxSchema.PhysxSceneAPI.Apply(prim)
            physx_scene.GetUpdateTypeAttr().Set("Synchronous")
            break

    # Load the carter navigation asset
    assets_root_path = await get_assets_root_path_async()
    carter_nav_path = assets_root_path + NOVA_CARTER_NAV_URL
    print(f"Loading carter nova asset: '{carter_nav_path}'")
    carter_nav_prim = add_reference_to_stage(usd_path=carter_nav_path, prim_path=NOVA_CARTER_NAV_USD_PATH)

    # Set the carter navigation start location
    nav_start_loc = example_config.get("nav_start_loc")
    if not nav_start_loc:
        print(f"Navigation start location not provided, exiting")
        return
    print(f"Setting carter navigation start location to: {nav_start_loc}")
    if not carter_nav_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_nav_prim).AddTranslateOp()
    carter_nav_prim.GetAttribute("xformOp:translate").Set(nav_start_loc)

    # Check if a collision ground plane needs to be created at the spawn location
    if example_config.get("create_collision_ground_plane"):
        plane_path = "/World/CollisionPlane"
        print(f"Creating collision ground plane {plane_path} at {nav_start_loc}")
        omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
        plane_prim = stage.GetPrimAtPath(plane_path)
        plane_prim.GetAttribute("xformOp:scale").Set((10, 10, 1))
        plane_prim.GetAttribute("xformOp:translate").Set(nav_start_loc)
        if not plane_prim.HasAPI(UsdPhysics.CollisionAPI):
            collision_api = UsdPhysics.CollisionAPI.Apply(plane_prim)
        else:
            collision_api = UsdPhysics.CollisionAPI(plane_prim)
        collision_api.CreateCollisionEnabledAttr(True)
        plane_prim.GetAttribute("visibility").Set("invisible")

    # Set the carter navigation target prim location
    nav_relative_target_loc = example_config.get("nav_relative_target_loc")
    if not nav_relative_target_loc:
        print(f"Navigation relative target location not provided, exiting")
        return
    print(f"Setting carter navigation target location to: {nav_relative_target_loc}")
    carter_navigation_target_prim = stage.GetPrimAtPath(NOVA_CARTER_NAV_TARGET_PATH)
    if not carter_navigation_target_prim.IsValid():
        print(f"Carter navigation target prim not found at path: '{NOVA_CARTER_NAV_TARGET_PATH}', exiting")
        return
    if not carter_navigation_target_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_navigation_target_prim).AddTranslateOp()
    carter_navigation_target_prim.GetAttribute("xformOp:translate").Set(nav_relative_target_loc)

    # Run the simulation for the given number of steps
    num_simulation_steps = example_config.get("num_simulation_steps")
    if not num_simulation_steps:
        print(f"Number of simulation steps not provided, exiting")
        return
    print(f"Running {num_simulation_steps} simulation steps")
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    for i in range(num_simulation_steps):
        if i % 10 == 0:
            print(f"Step {i}, time: {timeline.get_current_time():.4f}")
        await omni.kit.app.get_app().next_update_async()

    print(f"Simulation complete, pausing timeline")
    timeline.pause()

async def run_examples_async():
    for example_config in EXAMPLE_CONFIGS:
        await run_example_async(example_config)

asyncio.ensure_future(run_examples_async())
```

Standalone Application

```python
import os

from isaacsim import SimulationApp

simulation_app = SimulationApp(launch_config={"headless": False})

import omni.kit.app
import omni.kit.commands
import omni.timeline
import omni.usd
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.storage.native import get_assets_root_path
from pxr import PhysxSchema, UsdGeom, UsdPhysics

# User path of the HF NuRec dataset
USER_PATH = "/home/user/PhysicalAI-Robotics-NuRec"

# Paths for loading and placing the Nova Carter navigation asset and its target.
NOVA_CARTER_NAV_URL = "/Isaac/Samples/Replicator/OmniGraph/nova_carter_nav_only.usd"
NOVA_CARTER_NAV_USD_PATH = "/World/NovaCarterNav"
NOVA_CARTER_NAV_TARGET_PATH = f"{NOVA_CARTER_NAV_USD_PATH}/targetXform"
# Scenarios for testing navigation in the environments
EXAMPLE_CONFIGS = [
    {
        "name": "Andoria",
        "stage_url": f"{USER_PATH}/hand_hold-endeavor-andoria/stage_particle.usdz",
        "nav_start_loc": (0.0, 0.5, 0.0),
        "nav_relative_target_loc": (0.0, 6.0, 0.0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Wormhole",
        "stage_url": f"{USER_PATH}/hand_hold-endeavor-wormhole/stage_particle.usdz",
        "nav_start_loc": (5, 0, 0),
        "nav_relative_target_loc": (0, -4, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Cafe",
        "stage_url": f"{USER_PATH}/nova_carter-cafe/stage_particle.usdz",
        "nav_start_loc": (0, 0, 0),
        "nav_relative_target_loc": (-3, -1.5, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
    {
        "name": "Galileo",
        "stage_url": f"{USER_PATH}/nova_carter-galileo/stage_particle.usdz",
        "nav_start_loc": (-2.5, 2.5, 0),
        "nav_relative_target_loc": (4, 0, 0),
        "create_collision_ground_plane": False,
        "num_simulation_steps": 500,
    },
]

def run_example(example_config):
    example_name = f"{example_config.get('name')} - {example_config.get('num_simulation_steps')}"
    print(f"Running example: '{example_name}'")

    # Open the stage
    stage_url = example_config.get("stage_url")
    if not stage_url:
        print("Stage URL not provided, exiting")
        return
    if not os.path.exists(stage_url):
        print(f"Stage URL does not exist: '{stage_url}', exiting")
        return

    print(f"Opening stage: '{stage_url}'")
    omni.usd.get_context().open_stage(stage_url)
    stage = omni.usd.get_context().get_stage()
    if stage is None:
        print(f"Failed to open stage: '{stage_url}', exiting")
        return

    # Make sure the physics scene is set to synchronous for the navigation to work
    for prim in stage.Traverse():
        if prim.IsA(UsdPhysics.Scene):
            physx_scene = PhysxSchema.PhysxSceneAPI.Apply(prim)
            physx_scene.GetUpdateTypeAttr().Set("Synchronous")
            break

    # Load the carter navigation asset
    assets_root_path = get_assets_root_path()
    carter_nav_path = assets_root_path + NOVA_CARTER_NAV_URL
    print(f"Loading carter nova asset: '{carter_nav_path}'")
    carter_nav_prim = add_reference_to_stage(usd_path=carter_nav_path, prim_path=NOVA_CARTER_NAV_USD_PATH)

    # Set the carter navigation start location
    nav_start_loc = example_config.get("nav_start_loc")
    if not nav_start_loc:
        print(f"Navigation start location not provided, exiting")
        return
    print(f"Setting carter navigation start location to: {nav_start_loc}")
    if not carter_nav_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_nav_prim).AddTranslateOp()
    carter_nav_prim.GetAttribute("xformOp:translate").Set(nav_start_loc)

    # Check if a collision ground plane needs to be created at the spawn location
    if example_config.get("create_collision_ground_plane"):
        plane_path = "/World/CollisionPlane"
        print(f"Creating collision ground plane {plane_path} at {nav_start_loc}")
        omni.kit.commands.execute("CreateMeshPrimWithDefaultXform", prim_path=plane_path, prim_type="Plane")
        plane_prim = stage.GetPrimAtPath(plane_path)
        plane_prim.GetAttribute("xformOp:scale").Set((10, 10, 1))
        plane_prim.GetAttribute("xformOp:translate").Set(nav_start_loc)
        if not plane_prim.HasAPI(UsdPhysics.CollisionAPI):
            collision_api = UsdPhysics.CollisionAPI.Apply(plane_prim)
        else:
            collision_api = UsdPhysics.CollisionAPI(plane_prim)
        collision_api.CreateCollisionEnabledAttr(True)
        plane_prim.GetAttribute("visibility").Set("invisible")

    # Set the carter navigation target prim location
    nav_relative_target_loc = example_config.get("nav_relative_target_loc")
    if not nav_relative_target_loc:
        print(f"Navigation relative target location not provided, exiting")
        return
    print(f"Setting carter navigation target location to: {nav_relative_target_loc}")
    carter_navigation_target_prim = stage.GetPrimAtPath(NOVA_CARTER_NAV_TARGET_PATH)
    if not carter_navigation_target_prim.IsValid():
        print(f"Carter navigation target prim not found at path: '{NOVA_CARTER_NAV_TARGET_PATH}', exiting")
        return
    if not carter_navigation_target_prim.GetAttribute("xformOp:translate"):
        UsdGeom.Xformable(carter_navigation_target_prim).AddTranslateOp()
    carter_navigation_target_prim.GetAttribute("xformOp:translate").Set(nav_relative_target_loc)

    # Run the simulation for the given number of steps
    num_simulation_steps = example_config.get("num_simulation_steps")
    if not num_simulation_steps:
        print(f"Number of simulation steps not provided, exiting")
        return
    print(f"Running {num_simulation_steps} simulation steps")
    timeline = omni.timeline.get_timeline_interface()
    timeline.play()
    for i in range(num_simulation_steps):
        if i % 10 == 0:
            print(f"Step {i}, time: {timeline.get_current_time():.4f}")
        simulation_app.update()

    print(f"Simulation complete, pausing timeline")
    timeline.pause()

def run_examples():
    for example_config in EXAMPLE_CONFIGS:
        run_example(example_config)

run_examples()

simulation_app.close()
```

## Known Limitations

- Opening a `.usdz` file as the root stage and then adding another USD asset to it (via **Add Reference**, **Add Payload**, or drag-and-drop into the Stage) fails to load the added asset. The new prim appears empty with its name shown in red. As a workaround, open a `.usd` or `.usda` file (or create a new stage) as the root stage and reference the `.usdz` assets from there. This limitation will be addressed in a future release.
