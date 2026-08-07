---
source_id: "SRC-robotics-427"
title: "Unreal Engine Chaos Physics documentation"
source_type: "technical_documentation"
publisher: "Epic Games"
source_date: "2026-08-06"
url: "https://dev.epicgames.com/documentation/unreal-engine/physics-in-unreal-engine?lang=en-US"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-06T07:11:41+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-427
---
# Unreal Engine Chaos Physics documentation

## Physics in Unreal Engine

![Chaos Physics](https://dev.epicgames.com/community/api/documentation/image/477b3aeb-33db-4f06-bd9a-6c941ef17039?resizing_type=fit&width=1400&height=581)

Chaos Physics

**Chaos Physics** is a light-weight physics simulation solution available in Unreal Engine, built from the ground up to meet the needs of next-generation games. The system includes the following major features:

- Destruction
- Networked Physics
- Chaos Visual Debugger
- Rigid Body Dynamics
- Rigid Body Animation Nodes and Physical Animation
- Cloth Physics and Machine Learning Cloth Simulation
- Ragdoll Physics
- Vehicles
- Physics Fields
- Fluid Simulation
- Hair Physics
- Flesh Simulation

Here is an overview of each of these features:

### Destruction

![Chaos Destruction](https://dev.epicgames.com/community/api/documentation/image/00d86f9d-f470-4ede-9699-6ef039904e2b?resizing_type=fit&width=1400&height=765)

Chaos Destruction

The **Chaos Destruction** system is a collection of tools within Unreal Engine that can be used to achieve cinematic-quality levels of destruction in real time. In addition to great-looking visuals, the system is optimized for performance, and provides more control for artists and designers over content creation.

The Chaos Destruction system utilizes **Geometry Collections**, a type of asset built from one or more Static Meshes, including those nested in Blueprints. These Geometry Collections can be fractured to achieve real-time destruction.

The system provides unprecedented control over the fracturing process by using an intuitive non-linear workflow. The user can create multiple levels of fracturing, as well as selective fracturing on parts of the Geometry Collection, for greater artistic control. Users can also define the **Damage Thresholds** per cluster that will trigger a fracture.

**Connection Graphs** can be used to further manipulate how a structure collapses as it takes damage to simulate real-world structure integrity. Chaos Destruction comes with World Support, which allows certain parts of the Geometry Collection to be set to **Kinematic**, reducing the need to use **Anchor Fields**.

Chaos Destruction also comes with a **Cache System** capable of tracking events and transforms. This system captures per-frame transforms and events, and reduces the destruction data for efficient storage and replay capabilities. This system allows for smooth replay of complex destruction at runtime with minimal impact on performance. It's important to note that cached simulations can still be interactive, as certain parts of the simulation can become “live” upon interaction.

Chaos Destruction has deep integration with the **Niagara particle system** in Unreal Engine. Niagara can read Chaos Destruction **Break Events** and **Collision Events** to spawn particles or modify an existing particle system at runtime.

In addition, Chaos Destruction integrates with **Physics Fields**, a system that users can use to affect Chaos Physics simulations at runtime in a specified region of space. Physics Fields can affect physics simulation in a variety of ways, such as exerting force on rigid bodies, breaking Geometry Collection Clusters, and anchoring or disabling fractured rigid bodies.

You can learn more about Chaos Destruction by reading the documentation:

- [![Chaos Destruction](https://dev.epicgames.com/community/api/documentation/image/ffc18f9e-be1f-46c4-840d-95ca6aa77042?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/chaos-destruction-in-unreal-engine)

### Networked Physics

![Networked Physics](https://dev.epicgames.com/community/api/documentation/image/6ba137fa-e582-4c8d-a80c-d0207283e3f9?resizing_type=fit&width=1400&height=595)

Networked Physics

Networking, or replication in games, refers to the ability to communicate gameplay information between multiple machines over an internet connection. Unreal Engine features a robust networking framework that helps developers streamline the creation of multiplayer games.

**Networked physics** is part of the networking framework and enables physics-driven simulations to work in a multiplayer environment. In Unreal Engine, physics replication refers to Actors with replicated movement that simulate physics. These simulations run inside the local client (player’s machine) during gameplay.

Unreal Engine comes with three replication modes:

The **Default** replication mode is Unreal Engine’s legacy physics replication mode. This mode is active on Actors that **replicate their movement** and their **root component** is set to **simulate physics**.

The **Predictive Interpolation** replication mode is designed for server-authoritative Actors. It works by altering each object’s velocity on the client to match the object’s velocity on the server at that time, similarly to the Default mode. However, this mode is designed to better handle interactions and local physics alterations on the client, as long as they are done predictively (expected to be applied the same on the server and the client).

The **Resimulation** replication mode is designed for server-authoritative Pawns and Actors. This mode is designed to make physics Pawns possible in multiplayer through client prediction of physics and to handle interactions with better accuracy. When the client receives state information from the server, it compares them with the cached physics state in its history for the corresponding physics frame. If the state information differs enough, it triggers a physics resimulation.

You can learn more about networked physics by reading the documentation:

- [![Networked Physics](https://dev.epicgames.com/community/api/documentation/image/e5993607-f840-4c27-b445-7c2a6685741b?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/networked-physics)

### Chaos Visual Debugger

![Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/8fe5af91-ee8d-471f-9828-50bf2de89f2f?resizing_type=fit&width=1400&height=787)

Chaos Visual Debugger

The **Chaos Visual Debugger (CVD)** is a visual debugging tool for Chaos Physics simulations. It provides a graphical view of the Chaos Physics scene and comes with various tools to visualize data and analyze simulation results.

CVD is included in Unreal Engine as an editor tool and runtime system that records the state of physics simulations during gameplay. It can then replay those simulations inside the tool and inspect data for any given frame or sub-step of the simulation.

You can learn more about the Chaos Visual Debugger by reading the documentation:

- [![Chaos Visual Debugger](https://dev.epicgames.com/community/api/documentation/image/d6ef2fc0-66f1-490a-9427-813595988fb5?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/chaos-visual-debugger-in-unreal-engine)

### Rigid Body Dynamics

![Physics Constraints](https://dev.epicgames.com/community/api/documentation/image/f1f0aaf1-d45c-4abd-a225-c7019d173ae2?resizing_type=fit&width=1400&height=894)

Physics Constraints

Chaos Physics provides many features for **rigid-body dynamics**. This includes collision responses, physics constraints, and damping and friction. In addition, it provides asynchronous physics simulation and networked physics.

You can learn more about rigid body dynamics by reading the documentation:

- [![Collision](https://dev.epicgames.com/community/api/documentation/image/029cc3c8-e69f-4d09-b7d1-167b63d809b0?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/collision-in-unreal-engine)
- [![Traces with Raycasts](https://dev.epicgames.com/community/api/documentation/image/db70d3c0-1ddd-4fef-9300-51acf89c47bf?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/traces-with-raycasts-in-unreal-engine)
- [![Physics Constraints](https://dev.epicgames.com/community/api/documentation/image/81a1c49b-6015-4f53-a065-752969cab06f?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physics-constraints-in-unreal-engine)
- [![Physics Components](https://dev.epicgames.com/community/api/documentation/image/1060329f-8b63-48d7-aa56-684880db28c9?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physics-components-in-unreal-engine)

### Rigid Body Animation Nodes and Physical Animation

![Physics RBAN](https://dev.epicgames.com/community/api/documentation/image/8d858ab6-23c0-474d-9d42-4148b7443222?resizing_type=fit)

Physics RBAN

Chaos Physics provides **Rigid Body simulation** and **physical animations** for characters at runtime. The system uses the **Physical Asset Editor** to set up rigid bodies attached to the character’s Skeletal Mesh that can be simulated along the character’s animations. This results in more realistic movement of the simulated bodies, compared to a static animation.

You can learn more about Rigid Body Animation Nodes and physical animation by reading the documentation:

- [![Physics Asset Editor](https://dev.epicgames.com/community/api/documentation/image/3f0a500c-0ddf-41e6-8e21-010bfef144ad?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physics-asset-editor-in-unreal-engine)

### Cloth Physics and Machine Learning Cloth Simulation

<iframe src="https://dev.epicgames.com/community/api/cms/videos/V_KKnICi/embed.html"></iframe>

**Chaos Cloth** provides accurate and performant cloth simulation for games and real-time experiences. The system comes with extensive user controls, along with **physical reactions** such as wind, to achieve a specific artistic vision. In addition, Chaos Cloth also comes with a powerful **Animation Drive system**, which deforms a cloth Mesh to match its parent’s animated Skeletal Mesh.

Chaos Cloth parameters are exposed to Blueprints for unprecedented control over the cloth simulation at runtime. Users can **modify simulation parameters based on gameplay conditions** for specific use cases. For example, a character’s clothing can react differently when under water.

Chaos Cloth comes with a **suite of powerful debugging tools**, such as visualization tools and debug console commands that provide easier debugging and improved iteration times. Users can visualize active cloth simulations, kinematic and dynamic particles, and even simulation time.

Chaos Cloth also provides **machine learning cloth simulation**. This system results in higher fidelity simulation compared to a traditional physics-based model by using a trained dataset that can be used in real-time to produce results that were previously only achievable with offline simulation.

The **Chaos Cloth Panel node editor** is a new workflow introduced in Unreal Engine 5.3. This workflow focuses on improving iteration times and providing a more flexible, non-destructive way of authoring Chaos Cloth in-engine. This system uses a **cloth asset** that holds all the information needed to generate and simulate the asset at runtime. When building your clothing asset, you can import Static Meshes from external panel-based Digital Content Creation (DCC) packages, and transfer skin weights and masks. Once you create the asset, you can use it with any Skeletal or Static Mesh via the Chaos Cloth component.

You can learn more about cloth physics by reading the documentation:

- [![Cloth Simulation](https://dev.epicgames.com/community/api/documentation/image/b75f7210-bb27-4bc6-a1eb-af9f7c11c990?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/cloth-simulation-in-unreal-engine)

### Ragdoll Physics

![Ragdoll Physics](https://dev.epicgames.com/community/api/documentation/image/d5ae45a1-cff5-4b21-9e27-84dca7605ce3?resizing_type=fit&width=1400&height=788)

Ragdoll Physics

Chaos Physics comes with **ragdoll physics**, which refers to a system where rigid bodies connected to a Skeletal Mesh are animated (simulated) in real-time. These types of systems are commonly used to animate a humanoid character falling. In the example below, you can see the MetaHuman sample project, which comes with a ragdoll physics setup for the player character.

If you want to learn more, read the [MetaHuman Sample documentation](https://dev.epicgames.com/documentation/metahuman/metahumans-sample-for-unreal-engine-5?application_version=5.0-5.5) and download the [MetaHuman sample](https://www.fab.com/listings/0281d63e-71f7-4e07-a344-5fa721ac4d35) to see a well-documented ragdoll setup.

### Chaos Vehicles

![Chaos Vehicles](https://dev.epicgames.com/community/api/documentation/image/acf0d649-56c0-431f-9046-0179815229ad?resizing_type=fit&width=1400&height=765)

Chaos Vehicles

**Chaos Vehicles** is Unreal Engine’s lightweight system for performing vehicle physics simulations.

This system provides more flexibility to the user by **simulating any number of wheels** per vehicle. You can also configure any number of forward and reverse gears as well for added customization.

Chaos Vehicles can be configured for complex vehicle simulations. You can add **any number of aerofoil surfaces** that provide downforce or uplift at specific locations in the chassis. These can simulate vehicle spoilers, or even aircraft wings or rudders. Each of these control surfaces can be manipulated via roll, pitch, and yaw.

It is also possible to **turn off wheel friction and engine simulation** entirely while the simulation is running. In addition, users can configure any number of **thrust forces** that can be applied at specific locations to push and steer the vehicle.

The system supports the **Asynchronous Physics** mode in Unreal Engine 5, which improves the determinism of the simulation and allows for predictable results every time the simulation runs.

A Skeletal Mesh and one or more Wheel Blueprints are used to represent the vehicle inside the engine. A Physics Asset is used to generate the appropriate collision geometry inside the Physics Editor, and an Animation Blueprint is used to automatically generate the steering and rotation animations of the wheels.

Finally, a **Wheeled Vehicle Pawn** Blueprint is created that contains the Skeletal Mesh, Animation Blueprint, and vehicle controls.

You can learn more about Chaos Vehicles by reading the documentation:

- [![Vehicles](https://dev.epicgames.com/community/api/documentation/image/fb04f7bb-9239-4f53-9a46-e71fc20772f7?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/vehicles-in-unreal-engine)

### Physics Fields

<iframe src="https://dev.epicgames.com/community/api/cms/videos/V_88H8yf/embed.html"></iframe>

The **Physics Field System** provides a tool to directly affect **Chaos Physics** simulations at runtime on a specified region of space. These fields can be configured to influence the physics simulation in a variety of ways, such as exerting force on rigid bodies, breaking Geometry Collection Clusters, and anchoring or disabling fractured rigid bodies.

In addition, the Physics Field System can communicate with other engine systems, such as Niagara and Materials. These systems can sample Physics Fields by using built-in functions that can evaluate a Field at a specific location.

Fields are set up by creating a **Field System Component** Blueprint and specifying which systems are allowed to query your field. You can configure a field as a **World Field** to allow **Materials** and **Niagara systems** to sample the Field. You can also configure it as a **Chaos Field** to allow Geometry Collections and other physics objects to interact with it.

You can learn more about Physics Fields by reading the documentation:

- [![Physics Fields](https://dev.epicgames.com/community/api/documentation/image/f5a42288-d3d9-483e-ac65-ed887c7b91f2?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physics-fields-in-unreal-engine)

### Fluid Simulation

![Fluid Simulation](https://dev.epicgames.com/community/api/documentation/image/78c78a6d-5dc9-4710-8b72-e321780f2c56?resizing_type=fit&width=1400&height=894)

Fluid Simulation

Unreal Engine 5 includes a set of tools for simulating **2D and 3D fluid effects in real time**. These systems use physically-based simulation methods to produce realistic effects for things such as fire, smoke, clouds, rivers, splashes, and waves breaking on a beach.

The toolset is designed to be artist-friendly and an open platform for experimentation by utilizing simulation stages, reusable modules, and robust Data Interfaces.

Artists can achieve their desired results in real time by modifying only a few parameters, while advanced users and R&D engineers can dive in and break apart the simulators to try new algorithms

You can learn more about fluid simulation by reading the documentation:

- [![Fluid Simulation](https://dev.epicgames.com/community/api/documentation/image/9a8a32e9-2db6-4f19-9a89-19615ba63ec5?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/fluid-simulation-in-unreal-engine)

### Hair Physics

![Hair Physics](https://dev.epicgames.com/community/api/documentation/image/fede0db7-fcc9-4f01-b181-a7ba1233ec0b?resizing_type=fit&width=1400&height=765)

Hair Physics

The Unreal Engine's **Hair rendering and simulation system** uses a strand-based workflow to render each individual strand of hair with physically accurate motion. It enables artists to simulate and render hundreds of thousands (or more) photoreal hairs in real-time for grooms created in DCC packages.

You can learn more about hair physics by reading the documentation:

- [![Hair Physics](https://dev.epicgames.com/community/api/documentation/image/c946965a-fec1-4249-81af-56e53fc67e5f?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/hair-physics-in-unreal-engine)

### Chaos Flesh

<iframe src="https://dev.epicgames.com/community/api/cms/videos/V_8nCoWw/embed.html"></iframe>

The **Chaos Flesh** system provides high-quality, real-time simulation of deformable (soft) bodies in Unreal Engine. Unlike rigid body simulation, the shape of soft bodies can change during simulation based on their properties.

The system supports the simulation of Static and Skeletal Meshes with various parameters - giving artists unprecedented control over the end result. We designed the system to primarily focus on the simulation of a character's muscle deformation during skeletal animation.

The Chaos Flesh system achieves high performance by simulating low-resolution geometry at runtime, along with cached results from an offline simulation of high-resolution cinematic-quality geometry.

You can learn more about Chaos Flesh by reading the documentation:

- [![Chaos Flesh](https://dev.epicgames.com/community/api/documentation/image/2209df1b-b768-4df7-8e29-bd27344d7adf?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/chaos-flesh)

### Dataflow Graph System

![Workflow differences](https://dev.epicgames.com/community/api/documentation/image/1beb071a-42f6-4112-9fd6-391321ae2c57?resizing_type=fit&width=1400&height=751)

Workflow differences

The **Dataflow Graph** system is a **node-based procedural asset generation environment** inside the Unreal Engine editor.

Dataflow was created to **improve iteration times** when creating certain asset types in the engine. The same Dataflow graph can be **used by multiple assets** and the graph itself can produce different results depending on the inputs given by the source asset.

Dataflow is a **general-purpose system** that can be adapted to various physics asset types, such as **Chaos Cloth**, **Chaos Flesh**, and **Geometry Collection fracturing**. The system is **designed to be extensible** by developers using C++. Developers can further adapt the system to accommodate their specific needs.

You can learn more about Dataflow by reading the documentation:

- [![Dataflow Graph](https://dev.epicgames.com/community/api/documentation/image/c064586f-cc49-4add-bae6-ab3a475050ba?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/dataflow-graph)
- [![Physical Materials](https://dev.epicgames.com/community/api/documentation/image/629c7d2f-8c3f-48fa-a1b3-a339e2907f79?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physical-materials-in-unreal-engine)
- [![Physics Sub-Stepping](https://dev.epicgames.com/community/api/documentation/image/73bd12be-67b8-4a27-9f6c-39e4cdb8e7b6?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/physics-sub-stepping-in-unreal-engine)
- [![Walkable Slope](https://dev.epicgames.com/community/api/documentation/image/93eddfb0-abec-4649-a665-3b4c53549599?resizing_type=fit&width=640&height=640)](https://dev.epicgames.com/documentation/unreal-engine/walkable-slope-in-unreal-engine)
