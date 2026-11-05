---
source_id: "SRC-robotics-625"
title: "PhysX PGS and TGS simulation solvers"
source_type: "documentation"
publisher: "NVIDIA"
source_date: "待验证"
url: "https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/Simulation.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-625
---
# PhysX PGS and TGS simulation solvers

## Simulation

## The Simulation Loop

Use the method [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") to advance the world forward in time. Here is simplified code snippet for a fixed time stepper:

```
mAccumulator = 0.0f;
mStepSize = 1.0f / 60.0f;

virtual bool advance(PxReal dt)
{
    mAccumulator  += dt;
    if(mAccumulator < mStepSize)
        return false;

    mAccumulator -= mStepSize;

    mScene->simulate(mStepSize);
    return true;
}
```

This code can be called whenever the app is done with processing events and is starting to idle. It accumulates elapsed real time until it is greater than a sixtieth of a second, and then calls [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate"), which moves all objects in the scene forward by that interval. This is probably the simplest of very many different ways to deal with time when stepping the simulation forward.

To allow the simulation to finish and return the results, simply call:

```
mScene->fetchResults(true);
```

True indicates that the simulation should block until it is finished, so that on return the results are guaranteed to be available. When [`PxScene::fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") completes, any simulation event callback functions that you defined will also be called. See the chapter. Until [`PxScene::fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") returns, the results of the current simulation step are not available. It is not allowed to add, remove or modify scene objects while the simulation is running. See the chapter [Threading](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/Threading.html#threading) for more details about reading and writing while the simulation is running.

For the human eye to perceive animated motion as smooth, use at least twenty discrete frames per second, with each frame corresponding to a physics time step. To have smooth, realistic simulation of more complex physical scenes, use at least fifty frames per second.

> [!note] Note
> If you are making a real-time interactive simulation, you may be tempted to take different sized time steps which correspond to the amount of real time that has elapsed since the last simulation frame. Be very careful if you do this, rather than taking constant-sized time steps: The simulation code is sensitive to both very small and large time steps, and also to too much variation between time steps. In these cases it will likely produce jittery simulation.

See for details on how memory is used in simulation.

## Island Management

For performance reasons the simulation of scenes with multiple actors is split up into multiple islands, which are solved independently. Each actor is assigned to exactly one island and during the solve procedure actors can only influence other actors within the same island.

Islands are created by finding disconnected subgraphs in a scene graph where actors are nodes and edges represent connections between actors. The edges of the graph may be interactions between actors, for example contacts, but also explicit constraints like attachments and joints. Most of these edges are created automatically by PhysX when contacts occur or joints are being added to the scene. In cases where users can directly write constraints into buffers, for example `PxParticleSystem::addParticleBuffer()`, the SDK does not inspect the content of these constraint buffers until the constraint solver is invoked. Therefore, it is necessary that users manually take care of creating edges (e.g., through `PxParticleSystem::addRigidAttachment()`) such that the islands can be properly formed and interacting actors end up in the same island. Also note that for performance reasons, independent small islands may be fused into a bigger island. This is particularly the case for GPU simulation, where the entire scene is merged into a single island.

Each actor in PhysX has a method for defining solver iteration counts, see e.g.,. Given those per-actor iteration counts, each solver island performs as many iterations as the actor with the highest iteration count requests. Therefore, the actual number of solver iterations each body and constraint undergoes can change over time as the assignment of actors to islands changes and actors are going to sleep. If these varying iteration counts are not desired, all actors in the scene should be configured to require the same number of iterations.

## Callback Sequence

PhysX callbacks allow any application to listen for events and react as required.

The following callbacks are executed:

> - onConstraintBreak
> - onWake
> - onSleep
> - onContact
> - onTrigger
> - onAdvance

To listen to any of these events it is necessary to subclass [`PxSimulationEventCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv425PxSimulationEventCallback "PxSimulationEventCallback") so that the various virtual functions may be implemented as desired. An instance of this subclass can then be registered per scene with either [`PxScene::setSimulationEventCallback()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene26setSimulationEventCallbackEP25PxSimulationEventCallback "PxScene::setSimulationEventCallback") or [`PxSceneDesc::simulationEventCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSceneDesc.html#_CPPv4N11PxSceneDesc23simulationEventCallbackE "PxSceneDesc::simulationEventCallback"). Following these steps alone will ensure that constraint break events are successfully reported. One more step is required to report sleep and wake events: to avoid the expense of reporting all sleep and wake events, actors identified as worthy of sleep/wake notification require the flag [`PxActorFlag::eSEND_SLEEP_NOTIFIES`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxActorFlag.html#_CPPv4N11PxActorFlag4Enum20eSEND_SLEEP_NOTIFIESE "PxActorFlag::eSEND_SLEEP_NOTIFIES") to be raised. Finally, to receive onContact and onTrigger events it is necessary to set a flag in the filter shader callback for all pairs of interacting objects for which events are required. More details on the filter shader callback can be found in [Collision Filtering](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/RigidBodyCollision.html#collisionfiltering).

Each callback allows read operations to be performed on the relevant actors involved in each event. It is important to note that for all events except [`PxSimulationEventCallback::onAdvance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback9onAdvanceEPPCK11PxRigidBodyPK11PxTransformK5PxU32 "PxSimulationEventCallback::onAdvance"), these read operations will return the state of the actors at the end of the simulation step rather than the state the actors had when the event was first detected during the course of the simulation step. This particularly affects the callbacks [`PxSimulationEventCallback::onTrigger()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback9onTriggerEP13PxTriggerPair5PxU32 "PxSimulationEventCallback::onTrigger"), [`PxSimulationEventCallback::onContact()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback9onContactERK19PxContactPairHeaderPK13PxContactPair5PxU32 "PxSimulationEventCallback::onContact") and [`PxSimulationEventCallback::onConstraintBreak()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback17onConstraintBreakEP16PxConstraintInfo5PxU32 "PxSimulationEventCallback::onConstraintBreak"). The linear velocity, angular velocity and pose used to detect [`PxSimulationEventCallback::onContact()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback9onContactERK19PxContactPairHeaderPK13PxContactPair5PxU32 "PxSimulationEventCallback::onContact") events can be retrieved by amending the simulation filter shader with the flags [`PxPairFlag::ePRE_SOLVER_VELOCITY`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxPairFlag.html#_CPPv4N10PxPairFlag4Enum20ePRE_SOLVER_VELOCITYE "PxPairFlag::ePRE_SOLVER_VELOCITY") and [`PxPairFlag::eCONTACT_EVENT_POSE`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxPairFlag.html#_CPPv4N10PxPairFlag4Enum19eCONTACT_EVENT_POSEE "PxPairFlag::eCONTACT_EVENT_POSE"). This leads to code as follows:

```
virtual void onContact(const PxContactPairHeader& pairHeader, const PxContactPair* pairs, PxU32 nbPairs)
{
        // Retrieve the current poses and velocities of the two actors involved in the contact event.

        {
                const PxTransform body0PoseAtEndOfSimulateStep = pairHeader.actors[0]->getGlobalPose();
                const PxTransform body1PoseAtEndOfSimulateStep = pairHeader.actors[1]->getGlobalPose();

                const PxVec3 body0LinVelAtEndOfSimulateStep = pairHeader.actors[0]->is<PxRigidDynamic>() ? pairHeader.actors[0]->is<PxRigidDynamic>()->getLinearVelocity() : PxVec3(PxZero);
                const PxVec3 body1LinVelAtEndOfSimulateStep = pairHeader.actors[0]->is<PxRigidDynamic>() ? pairHeader.actors[1]->is<PxRigidDynamic>()->getLinearVelocity() : PxVec3(PxZero);

                const PxVec3 body0AngVelAtEndOfSimulateStep = pairHeader.actors[0]->is<PxRigidDynamic>() ? pairHeader.actors[0]->is<PxRigidDynamic>()->getAngularVelocity() : PxVec3(PxZero);
                const PxVec3 body1AngVelAtEndOfSimulateStep = pairHeader.actors[0]->is<PxRigidDynamic>() ? pairHeader.actors[1]->is<PxRigidDynamic>()->getAngularVelocity() : PxVec3(PxZero);
        }

        // Retrieve the poses and velocities of the two actors involved in the contact event as they were
        // when the contact event was detected.

        PxContactPairExtraDataIterator iter(pairHeader.extraDataStream, pairHeader.extraDataStreamSize);
        while(iter.nextItemSet())
        {
                const PxTransform body0PoseAtContactEvent = iter.eventPose->globalPose[0];
                const PxTransform body1PoseAtContactEvent = iter.eventPose->globalPose[1];

                const PxVec3 body0LinearVelocityAtContactEvent = iter.preSolverVelocity->linearVelocity[0]
                const PxVec3 body1LinearVelocityAtContactEvent = iter.preSolverVelocity->linearVelocity[1];

                const PxVec3 body0AngularVelocityAtContactEvent = iter.preSolverVelocity->angularVelocity[0]
                const PxVec3 body1AngularVelocityAtContactEvent = iter.preSolverVelocity->angularVelocity[1];
        }
}
```

The [`PxSimulationEventCallback::onAdvance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSimulationEventCallback.html#_CPPv4N25PxSimulationEventCallback9onAdvanceEPPCK11PxRigidBodyPK11PxTransformK5PxU32 "PxSimulationEventCallback::onAdvance") callback provides early access to the new pose of moving rigid bodies. When this call occurs, rigid bodies that have the flag [`PxRigidBodyFlag::eENABLE_POSE_INTEGRATION_PREVIEW`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxRigidBodyFlag.html#_CPPv4N15PxRigidBodyFlag4Enum32eENABLE_POSE_INTEGRATION_PREVIEWE "PxRigidBodyFlag::eENABLE_POSE_INTEGRATION_PREVIEW") raised were moved by the simulation and their new poses can be accessed using the provided buffers. This callback is different from the others mentioned above in the sense that it will get called while the simulation is running. As a consequence, code in this callback should be as lightweight as possible, as it will block the simulation.

It is forbidden to perform write operations in any callback.

## Simulation memory

PhysX relies on the application for all memory allocation. The primary interface is via the [`PxAllocatorCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxAllocatorCallback.html#_CPPv419PxAllocatorCallback "PxAllocatorCallback") interface required to initialize the SDK:

```
class PxAllocatorCallback
{
public:
    virtual ~PxAllocatorCallback() {}
    virtual void* allocate(size_t size, const char* typeName, const char* filename,
        int line) = 0;
    virtual void deallocate(void* ptr) = 0;
};
```

After the self-explanatory function argument describing the size of the allocation, the next three function arguments are an identifier name, which identifies the type of allocation, and the `__FILE__` and `__LINE__` location inside the SDK code where the allocation was made. More details of these function arguments can be found in the API documentation: [`PxAllocatorCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxAllocatorCallback.html#_CPPv419PxAllocatorCallback "PxAllocatorCallback").

> [!note] Note
> An important change since 2.x: The SDK now requires that the memory that is returned to be 16-byte aligned. On many platforms `malloc()` returns memory that is 16-byte aligned, but on Windows the system function `_aligned_malloc()` provides this capability.

> [!note] Note
> On some platforms PhysX uses system library calls to determine the correct type name, and the system function that returns the type name may call the system memory allocator. If you are instrumenting system memory allocations, you may observe this behavior. To prevent PhysX requesting type names, disable allocation names using the method [`PxFoundation::setReportAllocationNames()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxFoundation.html#_CPPv4N12PxFoundation24setReportAllocationNamesEb "PxFoundation::setReportAllocationNames").

Minimizing dynamic allocation is an important aspect of performance tuning. PhysX provides several mechanisms to control and analyze memory usage. These shall be discussed in turn.

### Scene Limits

The number of allocations for tracking objects can be minimized by presizing the capacities of scene data structures, using either [`PxSceneDesc::limits`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSceneDesc.html#_CPPv4N11PxSceneDesc6limitsE "PxSceneDesc::limits") before creating the scene or the function [`PxScene::setLimits()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene9setLimitsERK13PxSceneLimits "PxScene::setLimits"). It is useful to note that these limits do not represent hard limits, meaning that PhysX will automatically perform further allocations if the number of objects exceeds the scene limits.

### 16K Data Blocks

Much of the memory PhysX uses for simulation is held in a pool of blocks, each 16K in size. The initial number of blocks allocated to the pool can be controlled by setting [`PxSceneDesc::nbContactDataBlocks`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSceneDesc.html#_CPPv4N11PxSceneDesc19nbContactDataBlocksE "PxSceneDesc::nbContactDataBlocks"), while the maximum number of blocks that can ever be in the pool is governed by [`PxSceneDesc::maxNbContactDataBlocks`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSceneDesc.html#_CPPv4N11PxSceneDesc22maxNbContactDataBlocksE "PxSceneDesc::maxNbContactDataBlocks"). If PhysX internally needs more blocks than `nbContactDataBlocks` then it will automatically allocate further blocks to the pool until the number of blocks reaches `maxNbContactDataBlocks`. If PhysX subsequently needs more blocks than the maximum number of blocks, it will simply start dropping contacts and joint constraints. When this happens, warnings are passed to the error stream in the `PX_CHECKED` configuration.

To help tune `nbContactDataBlocks` and `maxNbContactDataBlocks` it can be useful to query the number of blocks currently allocated to the pool using the function [`PxScene::getNbContactDataBlocksUsed()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4NK7PxScene26getNbContactDataBlocksUsedEv "PxScene::getNbContactDataBlocksUsed"). It can also be useful to query the maximum number of blocks that can ever be allocated to the pool with [`PxScene::getMaxNbContactDataBlocksUsed()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4NK7PxScene29getMaxNbContactDataBlocksUsedEv "PxScene::getMaxNbContactDataBlocksUsed").

Unused blocks can be reclaimed using [`PxScene::flushSimulation()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene15flushSimulationEb "PxScene::flushSimulation"). When this function is called any allocated blocks not required by the current scene state will be deleted so that they may be reused by the application. Additionally, a number of other memory resources are freed by shrinking them to the minimum size required by the scene configuration.

### Scratch Buffer

A scratch memory block may be passed as a function argument to the function [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate"). As far as possible, PhysX will internally allocate temporary buffers from the scratch memory block, thereby reducing the need to perform temporary allocations from [`PxAllocatorCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxAllocatorCallback.html#_CPPv419PxAllocatorCallback "PxAllocatorCallback"). The block may be reused by the application after the [`PxScene::fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") call, which marks the end of the simulation. One restriction on the scratch memory block is that its size must be a multiple of 16K, and it must be 16-byte aligned.

### In-Place Serialization

PhysX objects can be stored in memory owned by the application using PhysX’ binary deserialization mechanism. See [Serialization](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/Serialization.html#serialization) for details.

### GPU Memory

When simulating a GPU-accelerated scene (see [GPU Simulation](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/GPURigidBodies.html#gpurigidbodies)), PhysX will allocate GPU device memory and pinned host memory. Contrary to CPU-side host memory, these allocations are made though the appropriate CUDA and GPU driver APIs and do not use the application-provided allocator. For details on GPU memory management, refer to the Section [GPU Memory](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/GPURigidBodies.html#gpumemory).

## Completion Tasks

A completion task is a [Task](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/Threading.html#task) that executes once the chain of simulation tasks triggered during [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") has finished. If PhysX has been configured to use worker threads then [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") will start simulation tasks on the worker threads and will likely exit before the worker threads have completed the work necessary to complete the scene update. A typical completion task would first need to call [`PxScene::fetchResults(true)`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") to wrap up the simulation update step. After calling [`PxScene::fetchResults(true)`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults"), the completion task can perform any other post-physics work deemed necessary by the application:

```
scene.fetchResults(true);
game.updateA();
game.updateB();
...
game.updateZ();
```

The completion task is specified as a function argument in [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate").

## Synchronizing with Other Threads

An important consideration for substepping is that [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") and [`PxScene::fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") are considered write calls on the scene, and it is therefore illegal to read from or write to a scene while those functions are running.

> [!note] Note
> PhysX does not lock its scene graph, but it will report an error in checked build if it detects that multiple threads make concurrent calls to the same scene, unless they are all read calls.

## Substepping

For reasons of fidelity simulation or better stability it is often desired that the simulation frequency of PhysX be higher than the update rate of the application. The simplest way to do this is just to call [`PxScene::simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") and [`PxScene::fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") multiple times:

```
for(PxU32 i=0; i<substepCount; i++)
{
    ... pre-simulation work (update controllers, etc) ...
    scene->simulate(substepSize);
    scene->fetchResults(true);
    ... post simulation work (process physics events, etc) ...
}
```

Sub-stepping can also be integrated with the completion task feature of the [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") function. To illustrate this, consider the situation where the scene is simulated until the graphics component signals that it has completed updating the render state of the scene. Here, the completion task will run once the simulation tasks have finished and its first job will be to block with [`fetchResults(true)`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") to complete the simulation step. When the completion task is able to proceed, its next work item will be to query the graphics component to check if another [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") is required or if it can exit. In the case that another [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") step is required it will clearly need to pass a completion task to [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate"). A tricky point here is that a completion task cannot submit itself as the next completion task because it would cause an illegal recursion. A solution to this problem might to be to have two completion tasks where each stores a reference to the other. Each completion task can then pass its partner to [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate"):

```
scene.fetchResults(true);
if(!graphics.isComplete())
{
    scene.simulate(otherCompletionTask);
}
```

## Split sim

As an alternative to [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") / [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults"), a simulation step may be split into two phases: [`PxScene::collide()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7collideE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::collide") and [`PxScene::advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance"). This is known as split simulation. The key point here is that the [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") / [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") combination permits reads and writes only before [`simulate()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene8simulateE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::simulate") and after [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults"). The split simulation, on the other hand, relaxes this restriction and allows some reads and writes to take place at specific points during the course of a simulation step. This shall now be explained in more detail.

When using split sim, a physics simulation step would look like this:

```
scene.collide(dt)
scene.fetchCollision()
scene.advance()
scene.fetchResults()
```

As already mentioned, split sim allows some properties to be written during the simulation step. More specifically, some properties, known as write-through properties, may be modified in-between the return from [`PxScene::fetchCollision()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene14fetchCollisionEb "PxScene::fetchCollision") and the execution of the [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance") call. This allows [`collide()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7collideE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::collide") to begin before the data required by [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance") is available and to run in parallel with application-side logic that generates inputs to [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance"). This is particularly useful for animation logic generating kinematic targets, and for controllers applying forces to bodies. The write-through properties are listed below:

```
PxRigidDynamic/PxArticulationLink::addForce()/addTorque()/clearForce()/clearTorque()/setForceAndTorque()
PxRigidDynamic/PxArticulationLink::setAngularVelocity()/setLinearVelocity()
PxRigidDynamic/PxArticulation::wakeUp()
PxRigidDynamic/PxArticulation::setWakeCounter()
PxRigidDynamic::setKinematicTarget()
```

Split sim also allows API read commands to be called during [`collide()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7collideE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::collide") and in-between the return from [`fetchCollision()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene14fetchCollisionEb "PxScene::fetchCollision") and the execution of the [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance") call. These read commands are listed below:

```
PxRigidActor/PxArticulationLink::getGlobalPose()
PxRigidActor/PxArticulation/PxArticulationLink::getWorldBounds()
PxConstraint::getForce()
PxRigidActor/PxArticulationLink::getLinearVelocity()/getAngularVelocity()
```

Users can interleave the physics-dependent application logic between [`collide()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7collideE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::collide") and [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance") as follows:

```
scene.collide(dt)
read poses, velocities, world bounds and constraint forces
physics-dependent game logic (anmimation, rendering) generating a set of modifications to apply to write-through properties before the advance() phase
scene.fetchCollision()
read more poses, velocities, world bounds and constraint forces
apply user-buffered modifications to the write-through properties
scene.advance()
scene.fetchResults()
```

The function [`fetchCollision()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene14fetchCollisionEb "PxScene::fetchCollision") will wait until [`collide()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7collideE6PxRealPN5physx10PxBaseTaskEPv5PxU32b "PxScene::collide") has finished. Once [`fetchCollision()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene14fetchCollisionEb "PxScene::fetchCollision") has completed, user-buffered modifications to write-through properties can be applied to the objects in the executing scene. In the subsequent [`advance()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene7advanceEPN5physx10PxBaseTaskE "PxScene::advance") phase, the solver will take the modified write-through properties into account when computing the new sets of velocities and poses for the actors being simulated.

As a final comment, it is worth noting that illegal read and write calls are detected in all build configurations - an illegal call will immediately return with an error passed to [`PxErrorCallback`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxErrorCallback.html#_CPPv415PxErrorCallback "PxErrorCallback") and the function will not be executed.

## Split fetchResults

The [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") method is available in both a standard and split format. The split format offers some advantages over the standard [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") method because it permits the user to parallelize processing of contact reports, which can be expensive when simulating complex scenes.

A simplistic way to use split [`fetchResults()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene12fetchResultsEbP5PxU32 "PxScene::fetchResults") would look something like this:

```
gSharedIndex = 0;

gScene->simulate(1.0f / 60.0f);

//Call fetchResultsStart. Get the set of pair headers
const PxContactPairHeader* pairHeader;
PxU32 nbContactPairs;
gScene->fetchResultsStart(pairHeader, nbContactPairs, true);

//Set up continuation task to be run after callbacks have been processed in parallel
callbackFinishTask.setContinuation(*gScene->getTaskManager(), NULL);
callbackFinishTask.reset();

//process the callbacks
gScene->processCallbacks(&callbackFinishTask);

callbackFinishTask.removeReference();

callbackFinishTask.wait();

gScene->fetchResultsFinish();
```

The user is free to use their own task/threading system to process the callbacks. However, the PhysX scene provides a utility function that processes the callbacks using multiple threads, which is used in this code snippet. This method takes a continuation task that will be run when the tasks processing callbacks have completed. In this example, the completion task raises an event that can be waited upon to notify the main thread that callback processing has completed.

This feature is demonstrated in *SnippetSplitFetchResults*. In order to make use of this approach, contact notification callbacks must be thread-safe. Furthermore, for this approach to be beneficial, contact notification callbacks need to be doing a significant amount of work to benefit from multi-threading them.

## Shifting The Scene Origin

Problems arising from the limits of floating point precision become more pronounced as objects move further from the origin. This phenomenon adversely affects large world scenarios. One solution might be to teleport all objects towards the origin with the proviso that their relative positions are preserved. The problem here is that internally cached data and persistent state will become invalid. PhysX offers an API to shift the origin of an entire scene in a way that maintains the consistency of the internally cached data and persistent state.

The function [`shiftOrigin()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxScene.html#_CPPv4N7PxScene11shiftOriginERK6PxVec3 "PxScene::shiftOrigin") will shift the origin of a scene by a translation vector:

```
PxScene::shiftOrigin(const PxVec3& shift)
```

The positions of all objects in the scene and the corresponding data structures will be adjusted to reflect the new origin location (basically, the shift vector will be subtracted from all object positions). The intended use pattern for this API is to shift the origin such that object positions move closer towards zero. Please note that it is the user’s responsibility to keep track of the summed total origin shift and adjust all input/output to/from PhysX accordingly. It is worth noting that this can be an expensive operation and it is recommended to use it only in the case where distance-related precision issues arise in areas far from the origin. If extension modules of PhysX, such as the character or vehicle controller, are used then it will be necessary to propagate the scene shift to those modules as well. Please refer to the API documentation of these modules for details.

## Solver Residual

The solver residual quantifies the convergence of the iterative physics solver. A perfectly converged solution has a residual value of zero. Each constraint contributes to the accumulated residual value. This accumulation captures the maximum value among all residuals and the root mean squared (RMS) value. Once the feature is activated by setting the ENABLE\_SOLVER\_RESIDUAL\_REPORTING flag on the scene, residuals can be obtained from the following PhysX objects:

- On the physics scene (PxScene): Residual across all solver error sources, including contacts.
- On articulation roots (PxArticulationJointReducedCoordinate): Residual across all joints that are part of that articulation.
- On non-articulation joints (PxConstraint via getConstraint() on PxJoint): The joint residual

The following code demonstrates how to retrieve the residual values. Remember that the returned values are meaningless if the ENABLE\_SOLVER\_RESIDUAL\_REPORTING flag is not set during scene construction:

```
PxSceneResidual sceneResidual = scene->getSolverResidual();
PxArticulationResidual articulationResidual = articulation->getSolverResidual();
PxConstraintResidual jointResidual = joint->getConstraint()->getSolverResidual();
```

The reported residual value encompasses all residual sources associated with the queried object. Residual values are reported for the last position and velocity iteration. Higher iteration counts typically result in lower residual values because the solver can execute more correction steps while seeking the best solution. When the TGS solver is active, the residuals tend to fluctuate more, compared to the PGS solver with identical iteration counts. This discrepancy arises from the TGS solver’s nature, which internally divides a full timestep into N substeps and approximately solves them, while the PGS solver allocates all its N iterations to solving the full timestep. In many scenarios, the convergence behavior of TGS is superior to PGS at identical iteration counts, despite the residual values suggesting otherwise, because the substepping strategy optimizes the use of every iteration, whereas later PGS iterations can only apply minor corrections. An example would be a pile of small rigid bodies stored in a jar. TGS almost certainly will result in less object overlap compared to PGS, even if the solver residuals report higher errors for the TGS solver. The takeaway is that TGS and PGS residual values are not directly comparable despite being based on the same metric.

> [!warning] Warning
> The reported residual data may not provide useful data, as further internal testing revealed. Therefore, users should not rely on the residual data for tuning or optimization of simulations, and should instead use other means to judge simulation quality or solver convergence. We are planning to either rework or deprecate the feature.

## Constraint Solver

### Solver Iterations

When the motion of a rigid body is constrained either by contacts or joints, the constraint solver comes into play. The solver satisfies the constraints on the bodies by iterating over all the constraints restricting the motion of the body a certain number of times. The more iterations, the more accurate the results become. The solver iteration count defaults to 4 position iterations and 1 velocity iteration. Those counts may be set individually for each body using the following function:

```
void PxRigidDynamic::setSolverIterationCounts(PxU32 minPositionIters, PxU32 minVelocityIters);
```

The iteration counts set in this way are understood to be lower bounds. The final number of iterations is dependent on the solver island, see for more information.

In general, and in particular when the bodies are subject to contact or other constraints, one cannot expect that the reported body velocity will match the position difference between two simulation steps. This is because the solver uses a split impulse strategy for resolving geometric (position) and velocity error separately: Position iterations solve for both geometric and velocity error. They do so by including the geometric error in the velocity-level constraint equation as a bias term, which *biases* the post-solve velocities towards values that reduce the geometric error after integration. These post-solve velocities resulting from the position iterations are used for integrating the body transforms at the end of a time step. On the contrary, velocity iterations only solve for velocity error, i.e., their bias is zero except in some specific cases (see e.g., [`Px1DConstraintFlag::eKEEPBIAS`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPx1DConstraintFlag.html#_CPPv4N18Px1DConstraintFlag4Type9eKEEPBIASE "Px1DConstraintFlag::eKEEPBIAS"), [Compliant Contacts](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/RigidBodyDynamics.html#compliantcontacts)). Due to the absence of the geometric bias in the velocity iterations, they do not operate on the same constraint equations as the position iterations. The velocity iterations’ post-solve velocities are the velocities that are carried across frames and they are reported in the corresponding body velocity fields (e.g., [`PxRigidBody::getLinearVelocity()`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxRigidBody.html#_CPPv4NK11PxRigidBody17getLinearVelocityEv "PxRigidBody::getLinearVelocity")).

> [!note] Note
> The solver will become the default solver. We recommend using one velocity iteration by default.

Typically it is only necessary to significantly increase these values for objects with lots of joints and a small tolerance for joint error. If you find a need to use a setting higher than 30, you may wish to reconsider the configuration of your simulation. To tune the number of iterations, it may be helpful to use the solver residual reporting, see [`PxSceneFlag::eENABLE_SOLVER_RESIDUAL_REPORTING`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum33eENABLE_SOLVER_RESIDUAL_REPORTINGE "PxSceneFlag::eENABLE_SOLVER_RESIDUAL_REPORTING").

The solver groups contacts into friction patches; friction patches are groups of contacts which share the same materials and have similar contact normals. However, the solver permits a maximum of 32 friction patches per contact manager (pair of shapes). If more than 32 friction patches are produced, which may be due to very complex collision geometry or very large contact offsets, the solver will ignore the remaining friction patches. A warning will be issued in checked/debug builds when this happens.

### Projected Gauss-Seidel and Temporal Gauss-Seidel

PhysX supports two types of solvers: the Projected Gauss-Seidel-style (PGS) solver and the Temporal Gauss-Seidel (TGS) solver, which was introduced in PhysX 5.1. TGS is generally the recommended solver and will become the default soon, but as an alternative and for backwards compatibility the standard PGS solver is still available. Both solvers are available for CPU and GPU simulation.

The solver can be configured on a per-scene basis through the [`PxSceneDesc::solverType`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/classPxSceneDesc.html#_CPPv4N11PxSceneDesc10solverTypeE "PxSceneDesc::solverType") field. This choice is an immutable scene property that must be set before the scene is constructed.

Both solvers utilize the same equations of motion and feature implicit time discretization with approximations. However, they employ different strategies to enforce desired constraints. For a detailed justification of the approximations, see the XPBD paper (), specifically Chapter 4. Also refer to the section on solver iterations ().

Within a single call to the scene’s simulate method, each iteration of the PGS solver runs through the **same** list of constraints. After all the iterations have concluded, the (hopefully converged) velocities of all bodies are integrated over the time step duration.

In contrast, TGS subdivides the time step into multiple equally-sized substeps. The number of substeps is equal to the number of position iterations. Each position iteration involves solving all constraints for this TGS substep **once**. Subsequently, the velocities are integrated immediately over the substep before the next substep (=position iteration) begins, which will then solve slightly updated constraints because the body positions have already been modified by the previous substep(s). Therefore, the TGS substepping scheme is conceptually similar to calling the PGS solver with a smaller timestep multiple times, each time only requesting a single solver iteration.

TGS velocity iterations do not integrate velocities at every iteration anymore, they merely solve the unbiased constraint equations for the last substep. After the velocity iterations are complete, the final transformations of all objects are computed based on the velocity after the last velocity iteration (see split impulse strategy above). Unless the scene exhibits significant geometrical errors before simulation begins, it is often sufficient to run TGS without any velocity iterations because the increased time resolution should keep the effect of geometric errors small throughout all substeps.

Temporal Gauss-Seidel offers several advantages over the PGS-style solver:

- Improved convergence
- Improved handling of high-mass ratios
- Improved joint drive accuracy
- More accurate simulation of high frequency effects due to better time resolution

Each TGS iteration is generally a little slower than PGS. This is partially due to the increased complexity of the constraint solver and also partially due to TGS solving friction constraints every iteration, whereas PGS solves friction constraints only in the final 3 position iterations by default.

#### TGS Force Application

The scene flag [`PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum43eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGSE "PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS") gives the user control over how external forces and gravity are applied to simulation actors.

The current default setting (off) means external forces and gravity are applied only once at the beginning of a simulation frame in order to maintain similar free-fall behavior as with the PGS solver.

With this flag raised, external forces and gravity are instead applied proportionally at every TGS position iteration (= internal substep).

Please refer to the API documentation for technical details.

#### TGS Steady-State Velocity and Position Discrepancy

The TGS solver is the source of a discrepancy in the steady state velocity of a driven joint. This section shall outline the problem and demonstrate that it is resolved by raising [`PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum43eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGSE "PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS").

Consider a dynamic body coupled to a static rigid body with a prismatic joint. The joint has free motion along Z and gravity acts downwards along Z. A proportional derivative drive is applied to the joint.

By definition, the joint velocity at the steady state will be 0. The question now is whether the joint does indeed report a joint velocity of 0 at steady state when the TGS solver is deployed.

The easiest way to determine whether the expected joint velocity at steady state is algorithmically possible is to imagine that the expected steady state is already achieved and then compute the outcome after one more simulation step. If the updated state repeats the previous state then it may be inferred that the expected steady state is an achievable outcome with the TGS solver. If the updated state is not a repeat of the previous state then it may be inferred that it is not possible for the TGS solver to produce and report a steady state velocity of 0.

With the TGS solver deployed and [`PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum43eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGSE "PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS") lowered, PhysX proceeds algorithmically as follows:

```
//Start the simulation at the steady state joint position where
//the spring force exactly counters the gravitational force.
pZ = -M*g/kp;
vZ = 0.0f;

//Perform the simulation steps with each step
//advancing time by dt.
for(PxU32 i = 0; i < nbSimSteps; i++)
{
        //Apply gravity over the full simulation step.
        vZ -= g*dt;

        //Run the TGS solver iterations with each iteration
        //advancing time by dt/nbPosIters.
        for(j = 0; j < nbPosIters; j++)
        {
                driveForce = -kp*pZ;
                vZ += (driveForce/M) * (dt/nbPosIters);
                pZ += vZ * (dt/nbPosIters);
        }
}
```

with g denoting gravitational acceleration; dt the duration of the simulation step; nbPosIters the position iteration count; kp the drive stiffness value; M the mass of the dynamic rigid body; pZ the joint position and vZ the joint velocity.

The joint begins the simulation at the steady state; that is, vZ = 0 and pZ = -M\*g/kp. Gravity is then applied for the entire dt with the outcome that vZ = -g\*dt. The solver is now tasked with maintaining the steady state by ensuring that the joint velocity is returned to 0.0 without altering the joint position. It shall now be shown that this is not possible with nbPosIters > 1.

Consider the case nbPosIters = 2. After one solver iteration the value of vZ is -0.5\*g\*dt. The key point here is that the joint now has a non-zero velocity because gravity was applied for dt but the spring force has only so far been applied for dt/2. With a non-zero velocity it follows that the spring position will deflect from its steady state position. The joint now has a non-zero velocity and the joint position is no longer at the steady state value. At the second solver iteration there is a conundrum: it is not possible to move pZ back to its steady state position but also have vZ = 0. The expected steady state is therefore not achievable with the TGS solver.

The sequence of operations described above may be repeated with nbPosIters > 2 with the same outcome: the expected steady state velocity is not achievable. There always exists the conundrum that it is not possible to move pZ back to the steady state value during the final solver iteration but also have vZ = 0. The fundamental problem is that the joint position was updated with a non-zero velocity. This non-zero joint velocity, however, is a consequence of applying an external force for dt but then applying the spring force in shorter bursts of dt/nbPosIters.

One solution to the problem described above would be to use nbPosIters = 1. In this regime, external forces and solver forces are applied in lockstep; that is, neither is temporally ahead of the other. This works for simple systems but does not scale to complex systems with high natural frequencies that require a large number of position iterations to converge. The alternative is to raise [`PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum43eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGSE "PxSceneFlag::eENABLE_EXTERNAL_FORCES_EVERY_ITERATION_TGS") so that external forces are applied at the start of each solver iteration. For the simple case illustrated here this has the following form:

```
for(i = 0; i < nbPosIters; i++)
{
    vZ -= g*(dt/nbPosIters);
    driveForce = -kp*pZ;
    vZ += (driveForce/M) * (dt/nbPosIters);
    pZ += vZ * (dt/nbPosIters);
}
```

In the absence of contact and joint limits, this is mathematically equivalent to simulating with a simulation timestep dt/nbPosIters and a single TGS position iteration. This equivalence means that the solver is able to generate a steady state with a reported velocity of 0.

> [!note] Note
> The mathematical equivalence outlined above is not strictly true for articulations because the Coriolis force is computed and applied just once before the solver rather than recomputed and applied at each TGS solver step.

## Immediate Mode

In addition to simulation using a *PxScene*, *PhysX* offers a low-level simulation API called “immediate mode”. This provides an API to access the low-level contact generation and constraint solver. This approach currently only supports a limited feature set.

The immediate mode API is defined in *PxImmediateMode.h* and there are two Snippets demonstrating its usage: “SnippetImmediateMode” and “SnippetImmediateArticulation”. The first one does not use articulations and shows how to use the API for rigid bodies and joints that still belong to a *PxScene*. This can be used e.g. to simulate a specific actor of a scene with a higher frequency than the rest of the scene. The second snippet is a “pure” immediate mode example where all involved actors, joints and articulations exist without the need for *PxScene*, *PxActor* or *PxArticulation* objects.

The immediate mode API provides a function to perform contact generation:

```
PX_C_EXPORT PX_PHYSX_CORE_API bool PxGenerateContacts(const PxGeometry* const * geom0, const PxGeometry* const * geom1, const PxTransform* pose0, const PxTransform* pose1, PxCache* contactCache, const PxU32 nbPairs, PxContactRecorder& contactRecorder, const PxReal contactDistance, const PxReal meshContactMargin, const PxReal toleranceLength, PxCacheAllocator& allocator);
```

This function takes a set of pairs of *PxGeometry* objects located at specific poses and performs collision detection between the pairs. If the pair of geometries collide, contacts are generated, which are reported to *contactRecorder*. In addition, information may be cached in *contactCache* to accelerate future queries between these pairs of geometries. Any memory required for this cached information will be allocated using *allocator*.

In addition, the immediate mode provides APIs for the constraint solver. These include functions to create bodies used by the solver:

```
PX_C_EXPORT PX_PHYSX_CORE_API void PxConstructSolverBodies(const PxRigidBodyData* inRigidData, PxSolverBodyData* outSolverBodyData, const PxU32 nbBodies, const PxVec3& gravity, const PxReal dt);

PX_C_EXPORT PX_PHYSX_CORE_API void PxConstructStaticSolverBody(const PxTransform& globalPose, PxSolverBodyData& solverBodyData);
```

In addition to constructing the bodies, *PxConstructSolverBodies* also integrates the provided gravitational acceleration into the bodies velocities.

The following function is optional and is used to batch constraints:

```
PX_C_EXPORT PX_PHYSX_CORE_API PxU32 PxBatchConstraints( const PxSolverConstraintDesc* solverConstraintDescs, const PxU32 nbConstraints, PxSolverBody* solverBodies, const PxU32 nbBodies,
                                                                                                                PxConstraintBatchHeader* outBatchHeaders, PxSolverConstraintDesc* outOrderedConstraintDescs,
                                                                                                                Dy::ArticulationV** articulations=NULL, const PxU32 nbArticulations=0);
```

Batching constraints reorders the provided constraints and produces batchHeaders, which can be used by the solver to accelerate constraint solving by grouping together independent constraints and solving them in parallel using multiple lanes in SIMD registers. This process is entirely optional and can be bypassed if not desired. Note that this will change the order in which constraints are processed, which can change the outcome of the solver.

The following methods are provided to create contact constraints:

```
PX_C_EXPORT PX_PHYSX_CORE_API bool PxCreateContactConstraints(PxConstraintBatchHeader* batchHeaders, const PxU32 nbHeaders, PxSolverContactDesc* contactDescs,
        PxConstraintAllocator& allocator, const PxReal invDt, const PxReal bounceThreshold, const PxReal frictionOffsetThreshold, const PxReal correlationDistance);
```

This method can be provided with the contacts produced by *PxGenerateContacts* or by contacts produced by application-specific contact generation approaches.

The following methods are provided to create joint constraints:

```
PX_C_EXPORT PX_PHYSX_CORE_API bool PxCreateJointConstraints(PxConstraintBatchHeader* batchHeaders, const PxU32 nbHeaders, PxSolverConstraintPrepDesc* jointDescs, PxConstraintAllocator& allocator,
                                                                                                                        const PxReal dt, const PxReal invDt);

PX_C_EXPORT PX_PHYSX_CORE_API bool PxCreateJointConstraintsWithShaders(PxConstraintBatchHeader* batchHeaders, const PxU32 nbBatchHeaders, PxConstraint** constraints, PxSolverConstraintPrepDesc* jointDescs,
                                                                                                                                                PxConstraintAllocator& allocator, const PxReal dt, const PxReal invDt);

PX_C_EXPORT PX_PHYSX_CORE_API bool PxCreateJointConstraintsWithImmediateShaders(PxConstraintBatchHeader* batchHeaders, const PxU32 nbBatchHeaders, immConstraint* constraints, PxSolverConstraintPrepDesc* jointDescs,
                                                                                                                                                                PxConstraintAllocator& allocator, const PxReal dt, const PxReal invDt);
```

The methods provide a mechanism for the application to define joint rows or for the application to make use of *PhysX PxConstraint* objects, which create the constraint rows.

The following method solves the constraints:

```
PX_C_EXPORT PX_PHYSX_CORE_API void PxSolveConstraints(const PxConstraintBatchHeader* batchHeaders, const PxU32 nbBatchHeaders, const PxSolverConstraintDesc* solverConstraintDescs,
        const PxSolverBody* solverBodies, PxVec3* linearMotionVelocity, PxVec3* angularMotionVelocity, const PxU32 nbSolverBodies, const PxU32 nbPositionIterations, const PxU32 nbVelocityIterations,
        const float dt=0.0f, const float invDt=0.0f, const PxU32 nbSolverArticulations=0, Dy::ArticulationV** solverArticulations=NULL);
```

This method performs all required position and velocity iterations and updates the objects’ delta velocities and motion velocities, which are stored in *PxSolverBody* and *linear/angularMotionVelocity* respectively.

The following method is provided to integrate the bodies’ final poses and update the bodies’ velocities to reflect the motion produced by the constraint solver:

```
PX_C_EXPORT PX_PHYSX_CORE_API void PxIntegrateSolverBodies(PxSolverBodyData* solverBodyData, PxSolverBody* solverBody, const PxVec3* linearMotionVelocity, const PxVec3* angularMotionState, const PxU32 nbBodiesToIntegrate,
const PxReal dt);
```

The above methods are the ones needed for simulating regular rigid bodies and joints in immediate mode. See SnippetImmediateMode for an example.

Additional functions are provided to simulate reduced coordinate articulations. First, register articulation-related solver functions with *PxRegisterImmediateArticulations*:

```
PX_C_EXPORT PX_PHYSX_CORE_API void PxRegisterImmediateArticulations();
```

This is the counterpart of *PxRegisterArticulationsReducedCoordinate* for immediate mode. You only need to call it once at the start of your program. Then create a low-level reduced coordinate articulations with the following function:

```
PX_C_EXPORT PX_PHYSX_CORE_API Dy::ArticulationV*        PxCreateFeatherstoneArticulation(const PxFeatherstoneArticulationData& data);
```

Once the articulation is created, add articulation links to it with the following function:

```
PX_C_EXPORT PX_PHYSX_CORE_API Dy::ArticulationLinkHandle        PxAddArticulationLink(Dy::ArticulationV* articulation, const PxFeatherstoneArticulationLinkData& data, bool isLastLink=false);
```

The number of links per articulation is currently limited to 64, just as with PxScene-level articulations. After all links have been added, the articulation is ready to be simulated.

Note that for articulations the current API is not as “immediate” as for rigid bodies, since the returned object is still a thin “retained mode” wrapper around low-level structures. This is done to make articulations easier to use: the low-level structures currently contain data for both reduced coordinate and maximal coordinate articulations, and intimate knowledge of PhysX’s internals is needed to distinguish between the two. The thin wrapper makes things more accessible. On the other hand, the data is not directly owned by the user, and the following function must be called to eventually release it at the end of your program:

```
PX_C_EXPORT PX_PHYSX_CORE_API void      PxReleaseArticulation(Dy::ArticulationV* articulation);
```

Meanwhile there are a number of data accessor functions available:

```
PX_C_EXPORT PX_PHYSX_CORE_API Dy::ArticulationV*        PxGetLinkArticulation(const Dy::ArticulationLinkHandle link);
PX_C_EXPORT PX_PHYSX_CORE_API PxU32     PxGetLinkIndex(const Dy::ArticulationLinkHandle link);
PX_C_EXPORT PX_PHYSX_CORE_API bool      PxGetLinkData(const Dy::ArticulationLinkHandle link, PxLinkData& data);
PX_C_EXPORT PX_PHYSX_CORE_API PxU32     PxGetAllLinkData(const Dy::ArticulationV* articulation, PxLinkData* data);
PX_C_EXPORT PX_PHYSX_CORE_API bool      PxGetMutableLinkData(const Dy::ArticulationLinkHandle link, PxMutableLinkData& data);
PX_C_EXPORT PX_PHYSX_CORE_API bool      PxSetMutableLinkData(Dy::ArticulationLinkHandle link, const PxMutableLinkData& data);
PX_C_EXPORT PX_PHYSX_CORE_API bool      PxGetJointData(const Dy::ArticulationLinkHandle link, PxFeatherstoneArticulationJointData& data);
PX_C_EXPORT PX_PHYSX_CORE_API bool      PxSetJointData(Dy::ArticulationLinkHandle link, const PxFeatherstoneArticulationJointData& data);
```

Some of them are here to update the data at runtime, say for articulation drives. Some of them are needed to setup the articulation data for aforementioned immediate mode functions like *PxSolveConstraints*, which have been updated in *PhysX 4.1* to take additional articulation-related parameters (but which should otherwise be used the same way as for immediate mode rigid bodies).

The only new articulation-specific functions are otherwise:

```
PX_C_EXPORT PX_PHYSX_CORE_API void      PxComputeUnconstrainedVelocities(Dy::ArticulationV* articulation, const PxVec3& gravity, const PxReal dt);
PX_C_EXPORT PX_PHYSX_CORE_API void      PxUpdateArticulationBodies(Dy::ArticulationV* articulation, const PxReal dt);
```

Use the first one at the start of the simulation loop to compute unconstrained velocities for each immediate mode articulations. Use the second one at the end of the simulation loop to update the articulation bodies/links after *PxIntegrateSolverBodies* has finished. Please refer to SnippetImmediateArticulation for examples.

For a standalone version of the broadphase, refer to section [Standalone Broad-phase](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/docs/RigidBodyCollision.html#broadphaseimmediatemode).

## Enhanced Determinism

PhysX provides limited deterministic simulation. Specifically, the results of the simulation will be identical between runs if simulating the exact same scene (same actors inserted in the same order) using the same time-stepping scheme and same PhysX release running on the same platform. The simulation behavior is not influenced by the number of worker threads that are used.

However, the results of the simulation can change if actors are inserted in a different order. In addition, the overall behavior of the simulation can change if additional actors are added or if some actors are removed from the scene. This means that the simulation of a particular collection of actors can change depending on whether other actors are present in the scene or not, irrespective of whether these actors actually interact with the collection of actors. This behavioral property is usually tolerable but there are circumstances in which it is not acceptable.

To overcome this issue, PhysX provides a flag: [`PxSceneFlag::eENABLE_ENHANCED_DETERMINISM`](https://nvidia-omniverse.github.io/PhysX/physx/5.7.0/_api_build/structPxSceneFlag.html#_CPPv4N11PxSceneFlag4Enum28eENABLE_ENHANCED_DETERMINISME "PxSceneFlag::eENABLE_ENHANCED_DETERMINISM"), which provides additional levels of determinism. Specifically, provided the application inserts the actors in a deterministic order, with this flag raised, the simulation of an island will be identical regardless of any other islands in the scene. However, this mode sacrifices some performance to ensure this additional determinism.

## References

MACKLIN M., MÜLLER M., CHENTANEZ N. 2016: XPBD: Position-based simulation of compliant constrained dynamics. In Proceedings of the 9th International Conference on Motion in Games (New York, NY, USA, 2016), MIG ’16, Association for Computing Machinery, p. 49-54. URL: [https://doi.org/10.1145/2994258.2994272](https://doi.org/10.1145/2994258.2994272), doi:10.1145/2994258.2994272. 2, 3
