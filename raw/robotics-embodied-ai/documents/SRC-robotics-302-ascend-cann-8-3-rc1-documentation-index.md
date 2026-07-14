---
source_id: "SRC-robotics-302"
title: "Ascend CANN 8.3 RC1 documentation index"
source_type: "product_documentation"
publisher: "Huawei Ascend"
source_date: "2026-07-14"
url: "https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/index/index.html"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-07-14T06:34:51+00:00"
tags:
  - raw/source
  - source-type/product-documentation
  - evidence/a
aliases:
  - SRC-robotics-302
---
# Ascend CANN 8.3 RC1 documentation index

## CANN商用版

异构计算架构CANN（Compute Architecture for Neural Networks）是昇腾针对AI场景推出的异构计算架构，向上支持多种AI框架，包括MindSpore、PyTorch、TensorFlow等，向下服务AI处理器与编程，发挥承上启下的关键作用，是提升昇腾AI处理器计算效率的关键平台。同时针对多样化应用场景，提供多层次编程接口，支持用户快速构建基于昇腾平台的AI应用和业务。

- [版本说明](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/releasenote/releasenote_0000.html)
	CANN与固件驱动的配套关系、版本特性变更等信息。
- [快速入门](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/quickstart/quickstart_18_0004.html)
	通过一个样例介绍基于CANN开发AI应用的全流程。
- [昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)
	昇腾产品的具体系列名称以及其对应的全部产品。

#### 环境准备

- [软件安装](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/softwareinst/instg/instg_quick.html)
	不同操作系统及业务场景下安装、升级、卸载CANN。

#### 应用开发

- [应用开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/appdevg/acldevg/acldevg_0000.html)
	使用C&C++、Python语言API开发AI应用，实现目标识别、图像分类等功能。相关API请参见 [应用开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/appdevgapi_07_0000.html) 。
- [ISP图像调优](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/appdevg/ispdevug/ispdevug_0001.html)
	ISP（Image Signal Processing）相关的算法和功能调试方法。相关API请参见 [ISP图像调优接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ispapi/ispdevapi_0001.html) 。

#### 算子开发

- [Ascend C算子开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0001.html)
	基于Ascend C算子编程语言进行算子开发，相关API请参见 [Ascend C算子开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendcopapi/atlasascendc_api_07_0003.html) 。
- [Ascend C最佳实践](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/ascendcbestP/atlas_ascendc_best_practices_10_0001.html)
	Ascend C算子开发的性能优化思路、方法和相关案例。
- [TBE&AI CPU算子开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/tbeaicpudevg/atlasopdev_10_0001.html)
	基于TBE、AI CPU接口开发TBE和AI CPU自定义算子，相关API请参见 [TBE&AI CPU算子开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/aicpuopapi/opdevapi_07_0000.html) 。
- [毕昇编译器](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/BishengCompiler/atlas_bisheng_10_0001.html)
	使用毕昇编译器将算子代码编译成二进制可执行文件和动态库等形式的指导。
- [CCE Intrinsic开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/cceintrinsicguide/cceprogram_0001.html)
	基于CCE Intrinsic的异构编程与多流水并行编程，相关API请参见 [CCE Intrinsic开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/cceintrinsicapi/cceapi_0001.html) 。
- [AscendNPU IR](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/AscendNPUIR/ir_001.html)
	基于MLIR构建的，面向昇腾亲和算子编译时使用的中间表示

#### 图开发

- [图模式开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/graph/graphdevg/atlasag_25_0001.html)
	基于GE提供的接口，构造可直接在昇腾平台上运行的图，相关API请参见 [构图接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendgraphapi/atlasgeapi_07_0001.html) 。
- [AutoFuse自动融合](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/graph/autofuse/autofuse_1_0001.html)
	基于Ascend C的自动融合框架，支持自动融合范围识别、自动算子代码生成、Auto Tiling优化、动态shape等特性。
- [DataFlow开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/graph/dataflowdevg/dataflow_dev_001.html)
	基于DataFlow C++和PythonAPI构图（FlowGraph），相关API请参见 [DataFlow构图接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/dataflowapi/dataflow_ref_001.html) 。

#### 集合通信

- [HCCL集合通信库](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/hccl/hcclug/hcclug_000001.html)
	基于昇腾AI处理器的高性能集合通信库，提供单机多卡以及多机多卡间的数据并行、模型并行集合通信方案，相关API请参见 [HCCL集合通信库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/hcclapiref/hcclapi_07_0001.html) 。

#### 领域加速库

- [ATB加速库](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/acce/ascendtb/ascendtb_0001.html)
	介绍Ascend Transformer Boost加速库的使用方法，提升Transformer模型的训练和推理开发效率，相关API请参见 [ATB加速库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendtbapi/ascendtb_01_0098.html) 。
- [SiP加速库](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/acce/SiP/SIP_0000.html)
	介绍信号处理领域相关的高性能算子的使用方法，相关API请参见 [SiP加速库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/SiPAPI/SIP_API_0002.html) 。
- [LLM DataDist开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/acce/llmdatadistdev/llmdatadist_dev_001.html)
	使用LLM DataDist接口对大模型的推理进行分离部署，从而提高大模型推理的吞吐性能，相关API请参见 [LLM DataDist接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/llmdatadistapi/llmdatadist_ref_001.html) 。

#### API

- [应用开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/appdevgapi_07_0000.html)
	提供系统配置、运行时管理、单算子执行、模型执行、媒体数据预处理等功能的C&C++和Python API。
- [ISP图像调优接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ispapi/ispdevapi_0001.html)
	ISP提供的各种图像调优算法API。
- [Ascend C算子开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendcopapi/atlasascendc_api_07_0003.html)
	Ascend C提供的基础API、高阶API等。
- [TBE&AI CPU算子开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/aicpuopapi/opdevapi_07_0000.html)
	提供TBE&AI CPU算子开发需要使用的相关API。
- [CCE Intrinsic开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/cceintrinsicapi/cceapi_0001.html)
	基于C语言扩展的昇腾硬件API，通过CCE Intrinsic接口可控制细粒度内存分配、数据同步、double buffer。
- [构图接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendgraphapi/atlasgeapi_07_0001.html)
	通过构图接口构造直接在昇腾平台上运行的图。
- [DataFlow构图接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/dataflowapi/dataflow_ref_001.html)
	通过DataFlow C++和Python API构建、修改、编译和执行计算图，同时提供UDF接口，支持用户通过FuncProcessPoint和GraphProcessPoint编写自定义处理函数。
- [HCCL集合通信库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/hcclapiref/hcclapi_07_0001.html)
	提供C与Python两种语言接口，分别实现单算子模式与图模式下的框架适配。
- [算子库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/aolapi/operatorlist_00001.html)
	提供丰富的深度优化、硬件亲和的高性能算子。
- [ATB加速库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendtbapi/ascendtb_01_0098.html)
	使用ATB加速库需要的相关接口，包括公共类定义如Operation类、单算子类和图算子类等。
- [SiP加速库接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/SiPAPI/SIP_API_0002.html)
	使用SiP加速库需要的相关接口，包括信号处理领域相关的高性能算子等。
- [LLM DataDist接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/llmdatadistapi/llmdatadist_ref_001.html)
	LLM DataDist接口提供了集群KV数据管理能力，以支持全量图和增量图分离部署。
- [AOE接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/aoeapi/aoeref_16_0001.html)
	AOE自动调优工具提供调优API用于自动调优，提供查询知识库API用于查询之前生成的知识库文件，获取tiling。
- [基础数据结构和接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/basicdataapi/atlasopapi_07_00001.html)
	算子开发和图开发时依赖的基础数据结构和接口说明。
- [开放代码基础功能支撑接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/codeopenapi/cann_base_api_0002.html)
	CANN开放代码中依赖的接口，包括错误上报接口、日志接口，本文旨在便于您了解这部分接口在CANN开放代码中的作用。

#### 开发工具

- [开发工具快速入门](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/devtoolquickstart/pttools_qucikstart_0001.html)
	提供PyTorch训练场景开发工具、大模型推理开发工具、算子开发工具快速入门指导。
- [算子开发工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/optool/atlasopdev_16_0002.html)
	算子开发工具集（msKPP、msOpGen、msOpST、msSanitizer、msDebug和msProf等）的使用指导。
- [算子编译工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/opcompiletool/atlasop_compiler_07_0001.html)
	编译算子生成算子二进制文件。
- [ATC离线模型编译工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/atctool/atlasatc_16_0001.html)
	模型转换工具，将网络模型转换为昇腾AI处理器支持的.om格式离线模型。
- [AOE调优工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/aoe/auxiliarydevtool_aoe_0001.html)
	自动调优工具，充分利用硬件资源，提升网络的性能。
- [分析迁移工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/migrationtools/atlasfmkt_16_0001.html)
	将PyTorch训练脚本一键式迁移至昇腾NPU。
- [精度调试工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/ModelAccuracyAnalyzer/atlasaccuracy_16_1000.html)
	精度比对，辅助定位模型精度问题。
- [性能调优工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_0001.html)
	训练、推理各运行阶段的性能数据采集和分析。
- [HCCL性能测试工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/hccltool/HCCLpertest_16_0001.html)
	测试HCCL集合通信的功能正确性以及性能。
- [AMCT模型压缩工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/amct/atlasamct_16_0001.html)
	模型压缩工具包，提供量化、张量分解等多种模型压缩特性。
- [算子及模型速查工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/opmodelquery/atlasopmodelquery_16_0001.html)
	查询当前版本CANN支持的模型和算子信息。
- [msLeaks内存泄漏检测工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/msleaks/atlas_msleaks_0001.html)
	模型训练和推理过程中的内存问题定位。

#### 参考

- [故障处理](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/troubleshooting/troubleshooting_0001.html)
	问题定位与处理方法，帮助开发者快速定位并解决故障。
- [RPing功能开发](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/rpingdev/RPing_02_0001.html)
	RPing是一种基于RDMA的网络探测技术，用以实现发送检测报文、记录网络时延、统计报文收发情况。
- [日志参考](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/logreference/logreference_0001.html)
	介绍日志的内容格式，以及如何查看日志、设置日志级别等。
- [环境变量参考](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/envvar/envref_07_0001.html)
	基于CANN构建AI应用和业务过程中可使用的环境变量。
- [图融合和UB融合规则参考](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/graphubfusionref/atlasrr_30_0003.html)
	昇腾AI处理器内置的一些图融合和UB融合规则，图融合和UB融合是整网性能提升的一种关键手段。
- [通信矩阵](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/maintenref/commumatrix/commumatrix_01.html)
	产品开放的端口、该端口使用的传输层协议、认证方式、用途等信息说明。
