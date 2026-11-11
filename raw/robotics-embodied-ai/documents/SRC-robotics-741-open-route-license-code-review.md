---
source_id: SRC-robotics-741
title: SO101开源替代路线固定版本许可与源码检查
source_type: source_code_inspection
publisher: 各项目官方仓库／本地静态检查
date: 2026-11-10
capture_method: github-api-fixed-raw-and-local-static-inspection
evidence_grade: S
---

# 检查范围

固定提交README另见SRC-robotics-720–735。目录`SRC-robotics-741-open-route-license-and-code-evidence/`保存各仓库实际LICENSE、四仓库tree和局部实现，data目录JSON含提交与sha256。许可证全文不等于完整依赖树授权审计。

- Playground实际task.py：vision环境10Hz、增量关节动作、腕相机64x64、策略图像下采样16x16；不等价于现有ACT双640x480和绝对reference。
- Playground tree存在train之外的SO101 deploy/run.py、env.py及sysid实现／测试；未运行这些文件。
- SO101 Bench tree含任务扩展、评估／LeRobot桥、微调配方和真实运行相关文件；主README明确保留私有测试对象／背景，不可宣称完整榜单可复现。
- Luoyadan fork根未发现LICENSE；内置ManiSkill/LICENSE只说明部分授权存在，不能覆盖新增顶层代码。未找到顶层许可不等于确定禁止，也不等于获得许可。
- SplatSim根未发现LICENSE，tree有to_delete下旧许可证；不能将子目录许可自动套到所有代码。gitlink与实际Gaussian子模块许可另存。
- COLMAP自身new BSD／3条款，依赖许可另算；Open3D MIT；LeRobot、Nerfstudio、gsplat、3DGRUT、ManiSkill、Playground、SO101 Bench、Workshop根许可见保存文件。
- SRC-robotics-737–740为无Markdown后缀纯文本，经通用工具被标fallback_html；检查所得.html实际为官方纯文本。保留fallback状态，不冒称Defuddle正常清洗。

无安装、训练、下载模型／大型场景、连接真机或远程验收。
