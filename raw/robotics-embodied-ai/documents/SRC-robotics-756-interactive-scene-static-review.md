---
source_id: SRC-robotics-756
title: 可交互场景重建固定版本源码与依赖核查
source_type: source_code_inspection
date: 2026-11-10
capture_method: fixed-github-raw-static-review
evidence_grade: S
---

# 范围与关键核查

目录SRC-robotics-756-interactive-scene-static-evidence保存根LICENSE、依赖清单和固定SHA；data目录provenance JSON有文件hash。没有安装、模型推理、远程或真实交互验收。

- PhiRIE MIT；bundled PhiView MIT。官方docs/PHIVIEW.md明确完整交互构建API使用单独PhiRoom兼容后端26f834ca3468e21c584abd5808082a0b2fdf4c66，需要仓库访问；不能将公开前端等同完整无门槛流程。当前PhiRIE树替代兼容后台未验证。不能根据网页cache miss断言该仓库必然私有。
- PhiRIE run_video2sim.sh存在，但全流程含机器人评估suite，本次场景目标应只取重建／物体／导出阶段，不照抄运行全链。质量门槛、物性annotator不是实测质量／摩擦。
- DISCOVERSE核心MIT，simulator.py确实用GSRendererMuJoCo并每帧update_gaussians(mj_data)。Real2Sim另仓根未见LICENSE，其Gaussian训练／DiffusionLight等依赖单独核查；不能由运行时MIT外推全部工具。
- RialToGUI README提供cut mesh、fixed/revolute/prismatic joint和USD导出；根未见LICENSE，不作全链开源授权保证。
- SimFoundry主代码Apache，默认Gemini服务与gated模型；THIRD_PARTY_LICENSES.md实际声明多项非商业／自定义许可。固定README指向INSTALL.md，但该路径404，此失败保留在752，不能宣称已取得安装指南。
- Re3Sim README明确CC-BY-NC-4.0，Isaac和Gaussian依赖另计；不称宽松全栈开源。
- RoboSimStudio主代码Apache，pyproject标Alpha、Linux、Python>=3.12，Newton[sim]>=1.7,<1.8；是交互物理搭建／调参工具，不是直接整房照片重建器。
- 751/754/755为.sh/.py/.toml后缀，被通用抽取标fallback_html；检查实际保存的是纯文本源码，保留原状态。
