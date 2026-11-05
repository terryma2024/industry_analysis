---
source_id: "SRC-ic-079"
title: "Cambricon MLU370-X8 product page"
source_type: "product_page"
publisher: "Cambricon"
source_date: "2022"
url: "https://www.cambricon.com/index.php?a=lists&c=index&catid=406&m=content"
evidence_grade: "A"
capture_method: "defuddle"
captured_at: "2026-09-22T02:45:08+00:00"
tags:
  - raw/source
  - source-type/product-page
  - evidence/a
aliases:
  - SRC-ic-079
---
# Cambricon MLU370-X8 product page

![寒武纪® AIDC® MLU370®-X8智能加速卡](https://www.cambricon.com/uploadfile/2022/0321/20220321123957875.jpg)

## 寒武纪® AIDC® MLU370®-X8智能加速卡 训推一体人工智能加速卡

寒武纪 <sup>®️</sup> AIDC <sup>®️</sup> MLU370 <sup>®️</sup> -X8采用双芯思元370配置，为双槽位250w全尺寸智能加速卡，提供24TFLPOS(FP32)训练算力和256TOPS (INT8)推理算力，同时提供丰富的FP16、BF16等多种训练精度。基于双芯思元370打造的MLU370-X8整合了两倍于标准思元370加速卡的内存、编解码资源，同时MLU370-X8搭载MLU-Link多芯互联技术，每张加速卡可获得200GB/s的通讯吞吐性能，是PCIe 4.0带宽的3.1倍，支持单机八卡部署，可高效执行多芯多卡训练和分布式推理任务。

## 产品规格

<table><tbody><tr><td colspan="1"><p>板卡型号</p></td><td><p>MLU370-X8</p></td></tr><tr><td colspan="1"><p>计算架构</p></td><td><p>Cambricon MLUarch03</p></td></tr><tr><td colspan="1"><p>制程工艺</p></td><td><p>7nm</p></td></tr><tr><td colspan="1"><p>计算精度支持</p></td><td><p>FP32、FP16、BF16、INT16、INT8、INT4</p></td></tr><tr><td colspan="1" rowspan="5"><p>峰值性能</p></td><td><p>256 TOPS (INT8)</p></td></tr><tr><td><p>128 TOPS (INT16)</p></td></tr><tr><td><p>96 TFLOPS (FP16)</p></td></tr><tr><td><p>96 TFLOPS (BF16)</p></td></tr><tr><td><p>24 TFLOPS (FP32)</p></td></tr><tr><td colspan="1"><p>内存类型</p></td><td><p>LPDDR5</p></td></tr><tr><td colspan="1"><p>内存容量</p></td><td><p>48GB</p></td></tr><tr><td colspan="1"><p>内存带宽</p></td><td><p>614.4 GB/s</p></td></tr><tr><td colspan="1"><p>视频编解码</p></td><td><p>最高可支持至8K；</p><p>264路HEVC全高清视频解码；</p><p>48路HEVC全高清视频编码；</p></td></tr><tr><td colspan="1"><p>图片编解码</p></td><td><p>图片编解码最高分辨率支持16384x16384；</p><p>8000 Frames/s 全高清图片解码；</p><p>6000 Frames/s 全高清图片编码；</p></td></tr><tr><td colspan="1"><p>系统接口</p></td><td><p>x16 PCIe Gen4</p></td></tr><tr><td colspan="1">MLU-Link™接口</td><td><p>4 ports, 16 Lanes, 50 Gbps</p></td></tr><tr><td colspan="1"><p>MLU-Link™带宽</p></td><td>聚合带宽200GB/s Bi-direction</td></tr><tr><td colspan="1"><p>形态</p></td><td><p>全高全长双槽位</p></td></tr><tr><td colspan="1"><p>最大热功耗</p></td><td><p>250W</p></td></tr><tr><td colspan="1"><p>散热设计</p></td><td><p>被动</p></td></tr></tbody></table>

  
  
在寒武纪基础软件平台 SDK上实测，在常见的4个人工智能模型上，MLU370-X8单卡性能与主流350W RTX GPU相当；而在多卡加速方面，MLU370-X8借助MLU-Link多芯互联技术和寒武纪基础软件平台 CNCL通讯库的优化，在8卡环境下达到更优的并行加速比。

## 性能对比

![性能对比](https://www.cambricon.com/uploadfile/2022/0321/20220321124500309.jpg)

*\** *测试环境*

*250W MLU370-X8：NF5468M5/Intel Xeon Gold 5218 CPU @ 2.30GHz/MLU370 SDK 1.2.0*

*350W GPU： Supermicro AS -4124GS-TNR/Intel Xeon Gold 6130 CPU @ 2.10GHz/Cuda11.2*
