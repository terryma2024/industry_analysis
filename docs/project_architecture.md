# 行业分析项目架构设计

## 目标

本项目面向中国“十五五”国家规划周期中的重点产业，把行业研究拆成四层资产：

1. 原始资料：未经改写的文档、数据、网页摘录、论文、政策、财报、招聘信息。
2. 结构化知识：中国语境下的产业链、技术路线、市场格局、政策、公司、岗位、投资逻辑，并以 Obsidian vault 方式维护。
3. 可复用工具：模板、数据清洗脚本、来源检查脚本、行业目录初始化脚本。
4. Codex skill：让后续分析都遵守同一套目录、证据和输出规范。

## 目录模型

```text
raw/<industry>/
  documents/    # PDF、网页导出、研报、政策、论文、财报、招股书
  data/         # CSV、XLSX、JSON、数据库导出、统计表

knowledge/<industry>/
  00-index.md
  01-industry-map.md
  02-technology-and-products.md
  03-market-and-policy.md
  04-companies.md
  05-investment-view.md
  06-career-view.md
  sources.csv

knowledge/.obsidian/
  app.json
  appearance.json
  core-plugins.json
  workspace.json

tools/
  templates/
  new_industry_workspace.py

.agents/skills/industry-analysis/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

## Python 执行环境

项目脚本统一用 `uv` 管理，入口格式为：

```bash
uv run python tools/new_industry_workspace.py <slug> <行业名称>
uv run python .agents/skills/industry-analysis/scripts/check_workspace.py
```

Python 版本由 `.python-version` 固定，依赖由 `pyproject.toml` 声明。不要在项目脚本中依赖系统 Python 的隐式环境。

## 分析框架

每个行业都从三个最终用途倒推：

- 学习：这个行业的基本概念、技术栈、关键问题、推荐学习路径。
- 投资：市场空间、竞争格局、商业模式、产业周期、关键公司、风险和观察指标。
- 找工作：岗位地图、核心能力、公司类型、作品集项目、招聘信号。

同时，每个行业都必须回答一个“中国十五五定位”问题：

- 国家为什么重视这个产业？
- 它对应哪些国家战略目标、产业升级方向或安全约束？
- 中国在全球产业链中的位置、短板和机会是什么？
- 中央政策与地方政策分别如何影响产业落地？
- 哪些公司、岗位和投资机会最直接受益？

## Obsidian 知识库准则

`knowledge/` 是本项目的 Obsidian vault。所有知识库创建、管理和维护都默认使用 Obsidian 及 Obsidian 兼容 Markdown：

- 用 `00-index.md` 作为每个行业的入口笔记。
- 用 `[[wikilinks]]` 连接行业、公司、技术路线、政策、岗位和关键概念。
- 对跨行业主题使用 MOC note，例如“十五五未来产业”“国产替代”“AI+制造”。
- 对产业链、技术路线和公司关系，优先使用 Obsidian Canvas、Mermaid 或 Excalidraw。
- 事实来源保留在 `sources.csv` 或来源笔记中，结论笔记通过链接回溯证据。
- 修改知识库时，优先使用本地已安装的 Obsidian skills：`obsidian-markdown`、`obsidian-cli`、`obsidian-bases`、`obsidian-canvas-creator`、`mermaid-visualizer`、`excalidraw-diagram`。

更详细规范见 `docs/obsidian_knowledge_base_guidelines.md`。

## 证据分级

- S 级：国家和地方政策、监管文件、十五五相关文件、上市公司公告、财报、招股书、标准、原始统计数据、论文原文。
- A 级：头部咨询/券商/产业研究报告、公司白皮书、协会报告。
- B 级：媒体深度报道、访谈、会议纪要、招聘数据整理。
- C 级：社媒观点、二手摘录、无法追溯来源的图表。

重要判断应优先由 S/A 级来源支撑。B/C 级来源可以用于线索发现，但不应单独支撑投资结论。

## 迭代节奏

1. 收集资料：先建立 `sources.csv`，再放入原始文件。
2. 快速扫图：形成 `00-index.md`，写明行业边界和当前问题清单。
3. 深挖模块：按产业链、技术、市场、公司、投资、职业逐步补齐。
4. 复盘更新：每次新增关键资料后更新结论、风险和下一步问题。

## 命名规则

- 行业目录使用稳定英文 slug。
- 原始文件建议格式：`YYYY-MM-DD_source_topic.ext`。
- 数据文件建议带口径：`YYYY_metric_region_frequency_source.ext`。
- 知识文件保持编号前缀，方便阅读顺序和检索。
