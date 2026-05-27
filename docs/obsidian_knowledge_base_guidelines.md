# Obsidian 知识库执行准则

## 核心原则

本项目的知识库创建、管理和维护统一使用 Obsidian。`knowledge/` 是 Obsidian vault 根目录，所有知识资产都应保持 Obsidian 兼容，同时保留普通 Markdown 的可读性。

## 目录定位

- `knowledge/`: Obsidian vault 根目录。
- `knowledge/.obsidian/`: Obsidian 本地配置。
- `knowledge/<industry>/00-index.md`: 行业入口笔记。
- `knowledge/<industry>/sources.csv`: 来源索引。
- `raw/`: 原始资料和原始数据，不直接作为知识笔记维护。

## 笔记规范

- 使用 Obsidian Flavored Markdown。
- 用 `[[wikilinks]]` 连接行业、公司、技术路线、政策、岗位、概念和来源笔记。
- 每个行业必须维护 `00-index.md`，作为 MOC/导航页。
- 跨行业主题应建立 MOC note，例如 `十五五重点产业`、`国产替代`、`AI基础设施`、`低空经济政策`。
- 重要结论要能回溯到 `sources.csv`、原始文件路径或来源笔记。
- 不在知识笔记里堆大段原文；原文留在 `raw/`，知识笔记保留摘要、判断、证据和链接。

## 可视化规范

- 产业链、公司关系、技术路线优先使用 Obsidian Canvas。
- 流程、架构、因果关系可使用 Mermaid。
- 手绘式解释、框图或概念图可使用 Excalidraw。
- 图形文件也应能从对应 Markdown 入口笔记链接回去。

## 推荐使用的本地 Codex Skills

- `obsidian-markdown`: 编写 Obsidian Markdown、wikilinks、callouts、properties。
- `obsidian-cli`: 在 Obsidian vault 中搜索、创建、读取和维护笔记。
- `obsidian-bases`: 创建和维护 Obsidian Bases。
- `obsidian-canvas-creator`: 生成 Obsidian Canvas。
- `mermaid-visualizer`: 生成 Mermaid 图。
- `excalidraw-diagram`: 生成 Excalidraw 图。
- `defuddle`: 把网页清洗成 Markdown 后再进入知识库。

## 维护流程

1. 先把原始资料放入 `raw/<industry>/documents/` 或 `raw/<industry>/data/`。
2. 在 `knowledge/<industry>/sources.csv` 记录来源。
3. 对网页来源运行 `uv run python tools/extract_sources_with_defuddle.py --industry <slug>`，并在 `knowledge/<industry>/` 维护来源抽取 MOC；详见 `docs/source_capture_sop.md`。
3. 在 `knowledge/<industry>/00-index.md` 更新研究入口和当前判断。
4. 按主题更新产业链、技术、市场政策、公司、投资、职业文件。
5. 新增重要概念时，补充 wikilinks，并在必要时新增 MOC note。
6. 做完一次较大更新后，检查断链、来源缺失和重复笔记。
