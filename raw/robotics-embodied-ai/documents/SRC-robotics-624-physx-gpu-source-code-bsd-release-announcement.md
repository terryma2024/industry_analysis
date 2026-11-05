---
source_id: "SRC-robotics-624"
title: "PhysX GPU source code BSD release announcement"
source_type: "documentation"
publisher: "NVIDIA"
source_date: "待验证"
url: "https://github.com/NVIDIA-Omniverse/PhysX/discussions/384"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-624
---
# PhysX GPU source code BSD release announcement

Discussion options

Since the release of PhysX SDK 4.0 in December 2018, NVIDIA PhysX has been available as open source under the BSD-3 license—with one key exception: the GPU simulation kernel source code was not included.

That changes today.

We’re excited to share that the latest update to the PhysX SDK now includes all the GPU source code, fully licensed under BSD-3!

With over 500 CUDA kernels powering features such as rigid body dynamics, fluid simulation, and deformable objects, GPU PhysX represents one of the most advanced real-time simulation use cases of CUDA and GPU programming. We hope this release will be a valuable resource for learning, experimentation, and development across the community.

In addition, we’re also open-sourcing the full GPU compute shader implementation of the Flow SDK, our real-time, sparse grid–based fluid simulation library.

We can’t wait to see what you build with it. Explore, experiment—and feel free to post issues or feedback right here on GitHub!

You must be logged in to vote

Comment options

edited

ahahah

thats noice

You must be logged in to vote

5 replies

Comment options

why they need fix PhysX in new GPUs when you can give everything to modders and they will do it all for you ( ͡° ͜ʖ ͡°)

Comment options

edited

Thank you Nvidia, despite what psych0kines said it's a helluva lot better than never getting this.

Comment options

Hopefully the smoke and fluid simulation stuff in Flex comes next and gets moved to a vendor generic compute solution.

There is a DX12 rendering backend for Flex that works on AMD/Intel GPUs, but (correct me if I'm wrong) the PhysX code currently available seems to target CUDA.

Comment options

> Hopefully the smoke and fluid simulation stuff in Flex comes next and gets moved to a vendor generic compute solution.
> 
> There is a DX12 rendering backend for Flex that works on AMD/Intel GPUs, but (correct me if I'm wrong) the PhysX code currently available seems to target CUDA.

its possible to port it to open cl it was done in the past [https://forums.legitreviews.com/viewtopic.php?t=16329](https://forums.legitreviews.com/viewtopic.php?t=16329)

Comment options

Opencl literally didn't even exist for most of 2008 (with gpu acceleration requiring almost [another](https://www.geeks3d.com/20091221/how-to-enable-opencl-support-on-nvidia-and-amd-platforms/) good year to be out of the gate).  
So either they incredibly managed to deliver the one holy grail with the one api nobody ever cared for (CTM), or I'm [pretty](https://web.archive.org/web/20080903034506/http://www.ngohq.com/graphic-cards/14494-ati-physx.html) [sure](https://web.archive.org/web/20090227151027/http://www.ngohq.com/graphic-cards/15316-ati-physx-vaporizes.html) that was a fake.

Comment options

Great! Thank you for your work!

You must be logged in to vote

0 replies

Comment options

Cool stuff!

You must be logged in to vote

0 replies

Comment options

cuda 12.8.1 still has "treat warning as error " (vs2022 x64)

You must be logged in to vote

0 replies

Comment options

Guys, port this to Vulkan so everyone can enjoy it

You must be logged in to vote

0 replies

Comment options

Hello, dear [@amoravanszky](https://github.com/amoravanszky) and big thanks for this update! And sorry for the direct tagging interrupting you!  
It's really amazing that PhysX is moving to the all-opened sources. But I can't leave one thing alone without question, sorry) A couple of months ago I was exploring old Nvidia repositories and was amazed by the old and now deprecated repositories from NVIDIAGameWorks:

- [https://github.com/NVIDIAGameWorks/Flow](https://github.com/NVIDIAGameWorks/Flow)
- [https://github.com/NVIDIAGameWorks/Flex](https://github.com/NVIDIAGameWorks/Flex)

They provides cool solutions for a lot of physics stuff like deformable bodies, softbodies, fluids, etc.  
I know that all this functionality exists in current repository and if Flow is still written with HLSL that means that it can be possibly converted to most of target platforms using stuff like HLSLcc, but FleX now is a part of the core PhysX and written only with CUDA. Maybe you could open source the shader libraries under a BSD license for these legacy repositories? Even without making it work or compile, just provide sources to comminity. I think it would be a great help to the community not only to understand it better for much more specialists and use it more flexibly for gaming or scientific purposes, but also to create something cool on mobile platforms, for example.

You must be logged in to vote

2 replies

Comment options

Flex is tricky because it is in contrast to PhysX no longer an active project, and contrary to what some people are presuming, this is not about releasing the source for discontinued projects, so it is harder to justify. Miles, the author of Flex and I are aware of numerous requests, and we would like to eventually include Flex too, but I cannot promise anything right now.

Comment options

Thanks for your super quick reply! Yeah, I understand that it has maybe even negative business value right now. Anyway thank you for clarity at this question and hope one day to see the opened shader code for the FleX.  
Have a good day, Adam!

Category

[Announcements](https://github.com/NVIDIA-Omniverse/PhysX/discussions/categories/announcements)

12 participants
