---
source_id: "SRC-robotics-648"
title: "Gazebo Physics plugin and backend feature interface"
source_type: "documentation"
publisher: "Open Robotics"
source_date: "待验证"
url: "https://gazebosim.org/api/physics/8/physicsplugin.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-648
---
# Gazebo Physics plugin and backend feature interface

The [Gazebo Physics](https://gazebosim.org/api/physics/8/namespacegz_1_1physics.html) library integrates physics engines into the Gazebo Simulation eco-system. Each physics engine is wrapped into a Gazebo Physics Plugin that can be loaded in a Gazebo simulation. The Physics Plugin interface loads physics engines with the requested features at runtime. It is also possible to integrate your own selected physics engine by writing a compatible plugin interface.

To get a more in-depth understanding of how the physics plugin works in Gazebo, we will start with some high level concepts and definitions.

## High Level Concept

Conceptually, the physics plugin can be viewed from two sides of its interface: user vs. implementation.

Each physics engine provides access to different features implemented by the Gazebo Physics engine. The interface is made possible through the [Gazebo Plugin](https://gazebosim.org/api/plugin/3/namespacegz_1_1plugin.html) library, which instantiates [Features](https://gazebosim.org/api/physics/8/classgz_1_1physics_1_1Feature.html) in [FeatureLists](https://gazebosim.org/api/physics/8/structgz_1_1physics_1_1FeatureList.html) and supplies pointers to the selected engine. This "user side interface" makes the Gazebo Physics library "callable" from other Gazebo libraries.

The implementation side interface handles specific implementations of each `Feature`. Depending on what physics engine we are using in the plugin (DART, TPE etc.), the interface might be different. This interface is more internal facing, i.e. used mostly inside the Gazebo Physics library.

The implementation of the physics plugin revolves around four key elements.

1. [Entity](https://gazebosim.org/api/physics/8/classgz_1_1physics_1_1Entity.html)
	This is the base class of all "proxy objects". The "proxy objects" are essentially interfaces into the actual objects which exist inside of the various physics engine implementations. The proxy objects contain the minimal amount of data (e.g. a unique identifier, a reference-counter for the implementation object, and a reference to the implementation interface that it needs) necessary to interface with the object inside of the implementation that it refers to.
2. [FeaturePolicy](https://gazebosim.org/api/physics/8/structgz_1_1physics_1_1FeaturePolicy.html)
	FeaturePolicy is a "policy class" used to provide metadata to features about what kind of simulation engine they are going to be used in. Many physics simulations software libraries model 3-dimensional systems, though some (like Box2d) only consider 2-dimensional systems. A FeaturePolicy is used to customize Gazebo Physics' APIs by the number of dimensions (2 or 3) and also the floating point scalar type (float or double). (All of the currently supported physics engines use FeaturePolicy3d i.e. 3 dimensions and double.)
3. [Feature](https://gazebosim.org/api/physics/8/classgz_1_1physics_1_1Feature.html)
	This class defines the concept of a `Feature`, examples like `GetWorldFromEngine`, [GetEngineInfo](https://gazebosim.org/api/physics/8/classgz_1_1physics_1_1GetEngineInfo.html) etc. There is a pre-defined list of features in Gazebo Physics. They are implemented by using external physics engines' APIs to fulfill simulation needs requested by Gazebo.
4. [FeatureList](https://gazebosim.org/api/physics/8/structgz_1_1physics_1_1FeatureList.html)
	This is the class that aggregates a list of features. FeatureLists can be constructed in hierarchies, e.g. a `FeatureList` can be passed into another `FeatureList`, and the set of all features in the new list will be the sum.

## FeatureList Organization

For example, here are the `FeatureLists` used in the implementation of the `Dartsim` physics engine. Plugin implementations for other engines may choose to organize features into `FeatureLists` differently.

| Name | Definition |
| --- | --- |
| Base | contains data structures and functions that define and use "proxy objects" |
| CustomFeatures | retrieves `World` entity from physics engine |
| EntityManagementFeatures | provides features to get, remove and construct entities |
| FreeGroupFeatures | finds free group entities and sets world pose, linear and angular velocities |
| JointFeatures | defines types of joints used and sets joint properties |
| KinematicsFeatures | computes frame relative to world |
| LinkFeatures | applies external force and torque to link |
| SDFFeatures | constructs entities from SDF file |
| ShapeFeatures | retrieves `Shape` related properties like `BoundingBox`, `ShapeSize` etc. |
| SimulationFeatures | updates `World` and everything within by defined stepsize |
| WorldFeatures | sets options like solver and collision detector |

## Available Physics Plugins

Dart ([Dynamic Animation and Robotics Toolkit](https://dartsim.github.io/)) is an open source library that provides data structures and algorithms for kinematic and dynamic applications in robotics and computer animation. It is the default physics engine used in Gazebo Simulation. The source code for Dartsim plugin can be found in [Gazebo Physics repository](https://github.com/gazebosim/gz-physics/tree/main) under `dartsim` directory.

TPE ([Trivial Physics Engine](https://github.com/gazebosim/gz-physics/tree/main/tpe)) is an open source library created by Open Robotics that enables fast, inexpensive kinematics simulation for entities at large scale. It supports higher-order fleet dynamics without real physics (eg. gravity, force, constraint etc.) and multi-machine synchronization. The source code for TPE plugin can be found in [Gazebo Physics repository](https://github.com/gazebosim/gz-physics/tree/main) under the `tpe/plugin` directory.

Bullet ([Bullet3 Physics Engine](https://github.com/bulletphysics/bullet3)) is an open source library that supports real-time collision detection and multi-physics simulation for robotics and other application domains. Since Bullet supports two different APIs - a rigid-body API and a multibody API - with different physics implementations, there are two available plugin implementations:

- The `bullet` plugin implements the rigid-body API, and the source code can be found in [Gazebo Physics repository](https://github.com/gazebosim/gz-physics/tree/main) under the `bullet` directory.
- The `bullet-featherstone` plugin implements the multibody API (based on Featherstone's algorithms), and the source code can be found in [Gazebo Physics repository](https://github.com/gazebosim/gz-physics/tree/main) under the `bullet-featherstone` directory.

### Entity Comparison

The following is a table of `Entity` names used in the Gazebo Physics plugin interface, mapped to corresponding types in each supported physics engine. Entities are arranged in top-down hierarchical order.

| Physics Plugin | Dart | TPE | Bullet | Bullet Featherstone |
| --- | --- | --- | --- | --- |
| Engine | Engine | Engine | Engine | Engine |
| World | World | World | btDiscreteDynamicsWorld | btMultiBodyDynamicsWorld |
| Frame | Frame | N/A | N/A [^1] | N/A <sup>1</sup> |
| Model | Skeleton | Model | N/A [^2] | btMultiBody |
| Joint | Joint | N/A | btTypedConstraint | btMultiBodyJoint [^3] |
| Link | BodyNode | Link | btRigidBody | btMultiBodyLink |
| Shape | Shape | Collision | btCollisionShape | btCollisionShape |
| Box/Sphere/Cylinder etc. | Box/Sphere/Cylinder etc. | Box/Sphere/Cylinder etc. | Box/Sphere/Cylinder etc. | Box/Sphere/Cylinder etc. |

### Feature Comparison

For a list of all available `Features` in the Gazebo Physics library, check the classes inherited from `Feature` in the [Gazebo Physics API](https://gazebosim.org/api/physics/8/hierarchy.html). To check if a physics plugin implements a particular `Feature`, check the `FeatureLists` supported by that plugin as specified in the plugin.cc file, for example, [dartsim/src/plugin.cc](https://github.com/gazebosim/gz-physics/blob/main/dartsim/src/plugin.cc).

Next, check out the tutorial on [Loading physics plugins](https://gazebosim.org/api/physics/8/pluginloading.html) on how to load a plugin and access a specific `Feature` interface of the plugin programmatically.

[^1]: Frames are implicitly attached to joints, links, collisions or models in the Bullet physics engine.

[^2]: The Bullet rigid-body API does not have a concept of a Model, but the plugin maintains a collection of Links and Joints in the engine associated with a Model.

[^3]: There are multiple types in the Bullet Featherstone API to interact with joints, such as btMultiBodyJointLimitConstraint, btMultiBodyJointMotor and btMultiBodyJointFeedback.
