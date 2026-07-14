---
source_id: "SRC-robotics-286"
title: "NVIDIA Isaac Sim 6.0.1 license FAQ"
source_type: "license_documentation"
publisher: "NVIDIA"
source_date: "2026-06"
url: "https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-faq.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T03:30:40+00:00"
tags:
  - raw/source
  - source-type/license-documentation
  - evidence/a
aliases:
  - SRC-robotics-286
---
# NVIDIA Isaac Sim 6.0.1 license FAQ

## License FAQ

What license is Isaac Sim released under?

The Isaac Sim source code in the [GitHub repository](https://github.com/isaac-sim/IsaacSim/) is released under the [Apache 2.0 License](https://github.com/isaac-sim/IsaacSim?tab=License-1-ov-file#readme).

Building or running Isaac Sim requires additional components (such as the Omniverse Kit SDK, 3D models, and textures) that are covered under separate license terms. See [NVIDIA Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html) for details.

Is Isaac Sim free to use for commercial R&D?

Yes. Isaac Sim is free to use for internal R&D and development purposes. The only exception is if you are redistributing Isaac Sim (with Omniverse Kit) as part of an application to third parties, or delivering Isaac Sim (with Omniverse Kit) as a service to third parties. In those cases, an [NVIDIA AI Enterprise license](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/licensing.html) is required for the underlying usage of Omniverse Kit.

Do I need a license if I only sell simulation outputs (videos, reports, data)?

No. If you run the simulation internally and only sell the outputs (for example, simulation videos, analytic reports, or datasets) to clients, an NVIDIA AI Enterprise license is **not** required.

Do I need a license to sell custom code or USD assets that work with Isaac Sim?

No. If you sell only your custom Python code and `.usd` assets to a client, and the client runs them on their own Isaac Sim environment, no redistribution fees or royalties to NVIDIA are required. An NVIDIA AI Enterprise license is **not** required in this case.

Do I need a license to deliver a turn-key Isaac Sim solution to a client?

Yes. If you provide a turn-key service where you install and configure the entire Isaac Sim (with Omniverse Kit) environment on a client’s hardware, an [NVIDIA AI Enterprise license](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/licensing.html) **is** required because Isaac Sim (with Omniverse Kit) is being redistributed as part of an application or service to a third party.

Can I modify and redistribute Isaac Sim?

You may modify and redistribute the Apache 2.0 licensed source code in compliance with the [Apache 2.0 License](https://github.com/isaac-sim/IsaacSim?tab=License-1-ov-file#readme).

The additional NVIDIA-licensed components (Omniverse Kit SDK, assets, etc.) may not be modified or redistributed except as expressly permitted by their license terms. Redistribution of Isaac Sim (with Omniverse Kit) to third parties requires an [NVIDIA AI Enterprise license](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/licensing.html). See [NVIDIA Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html) for specifics.

What is the difference between the Isaac Sim open source license and the additional components license?

Isaac Sim has a dual-license structure:

- **Isaac Sim source code** — Released under the [Apache 2.0 License](https://github.com/isaac-sim/IsaacSim?tab=License-1-ov-file#readme), which permits free use, modification, and redistribution for any purpose, including commercial use.
- **Additional components** — Building and running Isaac Sim requires additional NVIDIA-owned components such as the Omniverse Kit SDK, 3D models, and textures. These are covered under the [NVIDIA Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html), which has separate terms regarding use, modification, and redistribution.

When considering redistribution or service delivery to third parties, it is the additional components (specifically Omniverse Kit) that trigger the requirement for an [NVIDIA AI Enterprise license](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/NVIDIA_Omniverse_License_Agreement.html) — not the Apache 2.0 source code.

Is there a per-user or per-seat limit for using Isaac Sim?

No. The Isaac Sim source code is released under the [Apache 2.0 License](https://github.com/isaac-sim/IsaacSim?tab=License-1-ov-file#readme), which does not impose any per-user, per-seat, or team size restrictions. Any number of developers within your organization may install, run, and collaborate on Isaac Sim.

The [NVIDIA Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html) for the additional components (Omniverse Kit SDK, assets, etc.) also does not define per-user limits for internal use. Redistribution or service delivery to third parties requires an [NVIDIA AI Enterprise license](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/NVIDIA_Omniverse_License_Agreement.html).

Where can I find NVIDIA AI Enterprise pricing?

NVIDIA AI Enterprise licensing and pricing information is available on the [NVIDIA AI Enterprise Licensing pricing page](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/pricing.html).

What license applies to NVIDIA-provided assets (3D models, textures, etc.)?

NVIDIA-provided assets are covered under the [NVIDIA Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html). Review this license for details on usage rights and restrictions.

Where can I find the full license texts?

- [Isaac Sim License (Apache 2.0)](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/licenses-isaac-sim.html)
- [Isaac Sim Additional Software and Materials License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-additional.html)
- [Isaac Sim WebRTC Streaming Client License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/license-isaac-sim-webrtc-streaming-client.html)
- [NVIDIA Omniverse License](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/NVIDIA_Omniverse_License_Agreement.html)
- [Licensing Disclaimer](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/licensing-notices-disclaimers.html)
- [Third-Party Licenses](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/licenses.html)

Does Isaac Sim include third-party open source software?

Yes. Isaac Sim includes components licensed under various open source licenses. A list of these third-party licenses is available at [License Files](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/common/licenses.html).

Can I use Isaac Sim in an air-gapped or offline environment?

Yes. You can download the Isaac Sim assets packs for offline use. See the [installation FAQ](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/installation/install_faq.html#isaac-sim-setup-faq) for instructions on setting up local assets. The same license terms apply regardless of whether Isaac Sim is used online or offline.
