# industry_analysis

这是一个面向学习、投资研究和职业选择的行业分析知识库，重点分析中国的重点产业，尤其关注这些产业在中国“十五五”国家规划周期中的政策定位、产业机会和个人发展机会。

## 目录约定

- `raw/`: 原始资料和原始数据。按行业分目录，每个行业下固定为 `documents/` 和 `data/`。
- `knowledge/`: Obsidian vault，由原始资料沉淀出来的结构化知识、行业地图、公司/岗位/投资分析。
- `tools/`: 研究过程中沉淀的脚本、模板和小工具。
- `.agents/skills/industry-analysis/`: 项目内 Codex skill，指导 Codex 按本项目规范做行业研究。
- `.agents/skills/video-summarizer/`: 项目内 Codex skill，用 `uv` 从视频链接提取字幕/转录并生成结构化笔记。
- `docs/`: 项目设计、方法论和长期说明文档。

## 初始行业

| 行业 | slug |
| --- | --- |
| 机器人（具身智能） | `robotics-embodied-ai` |
| 生物医药 | `biopharma` |
| AI相关 | `ai` |
| 集成电路 | `integrated-circuits` |
| 航空航天 | `aerospace` |
| 低空经济 | `low-altitude-economy` |
| 未来能源 | `future-energy` |
| 量子科技 | `quantum-technology` |
| 脑机接口 | `brain-computer-interface` |
| 6G | `6g` |

## 工作流

1. 优先收集中国语境下的原始材料：国家和地方政策、十五五相关文件、部委/协会资料、上市公司公告、招股书、财报、招聘 JD、产业数据和论文。
2. 把原始文档、研报、政策、论文、招股书、财报、招聘 JD、数据集放入 `raw/<industry>/`。
3. 在 `knowledge/<industry>/` 中沉淀结构化分析；`knowledge/` 按 Obsidian vault 维护，优先使用 Obsidian Markdown、wikilinks、MOC/index note 和可回溯来源。
4. 每次分析保留来源索引，避免“印象流”结论；来源记录模板见 `tools/templates/source-log.csv`。
5. 对 `sources.csv` 中的重要网页来源，运行 `uv run python tools/extract_sources_with_defuddle.py --industry <slug>`，把清洗后的 Markdown、原始 PDF 或 fallback HTML 落到 `raw/<industry>/documents/`。流程见 `docs/source_capture_sop.md`，并在 `knowledge/<industry>/` 维护 Obsidian-friendly 的来源抽取 MOC。
5. 可以让 Codex 使用 `$industry-analysis` skill 来新增行业、整理资料、生成行业知识、做投资/学习/求职视角分析。
6. 遇到 B站、YouTube、抖音、小红书、TikTok 等视频资料时，可以使用 `$video-summarizer` skill 先提取字幕和视频笔记，再沉淀进 `knowledge/`。

## Obsidian 执行准则

知识库的创建、管理和维护统一使用 Obsidian。`knowledge/` 是本项目的 Obsidian vault 根目录，所有行业知识文件都应保持 Obsidian 兼容：

- 使用 Obsidian Flavored Markdown。
- 用 `[[wikilinks]]` 连接概念、公司、产业链环节、政策和来源笔记。
- 为行业入口、主题地图和专题研究维护 index/MOC notes。
- 需要可视化时优先使用 Obsidian Canvas、Mermaid 或 Excalidraw。
- 重要结论仍需在 `sources.csv` 或来源笔记中保留证据链。

详细准则见 `docs/obsidian_knowledge_base_guidelines.md`。

## Python 环境

本项目的 Python 脚本统一由 `uv` 管理，不直接使用系统 Python。

常用命令：

```bash
uv run python tools/new_industry_workspace.py <slug> <行业名称>
uv run python .agents/skills/industry-analysis/scripts/check_workspace.py
```

当前项目固定使用 `.python-version` 中声明的 Python `3.13`，依赖声明在 `pyproject.toml`。

视频总结能力的换环境初始化步骤见 `docs/video_summarizer_setup.md`。

## 建议产物

每个行业最终至少形成这些文件：

- `00-index.md`: 行业入口与当前结论摘要。
- `01-industry-map.md`: 产业链、关键环节、价值流和竞争格局。
- `02-technology-and-products.md`: 技术路线、产品形态、成熟度、瓶颈。
- `03-market-and-policy.md`: 市场规模、增速、政策和监管。
- `04-companies.md`: 代表公司、商业模式、财务或融资状态。
- `05-investment-view.md`: 投资逻辑、风险、估值锚、观察指标。
- `06-career-view.md`: 岗位地图、能力要求、学习路径。
- `sources.csv`: 已使用来源索引。
