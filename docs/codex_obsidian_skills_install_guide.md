# Codex Obsidian Skills 安装指南

本指南用于在新机器或新 Codex 环境中重新安装 Obsidian 相关 skills。

## 安装目标

默认安装到：

```bash
${CODEX_HOME:-$HOME/.codex}/skills
```

安装后需要重启 Codex，新的 skills 才会进入发现列表。

## 本次安装清单

| Skill | 来源 |
| --- | --- |
| `defuddle` | `kepano/obsidian-skills:skills/defuddle` |
| `obsidian-cli` | `kepano/obsidian-skills:skills/obsidian-cli` |
| `obsidian-bases` | `kepano/obsidian-skills:skills/obsidian-bases` |
| `obsidian-markdown` | `kepano/obsidian-skills:skills/obsidian-markdown` |
| `json-canvas` | `kepano/obsidian-skills:skills/json-canvas` |
| `obsidian-canvas-creator` | `axtonliu/axton-obsidian-visual-skills:obsidian-canvas-creator` |
| `mermaid-visualizer` | `axtonliu/axton-obsidian-visual-skills:mermaid-visualizer` |
| `excalidraw-diagram` | `axtonliu/axton-obsidian-visual-skills:excalidraw-diagram` |
| `tutor-setup` | `RoundTable02/tutor-skills:skills/tutor-setup` |
| `tutor` | `RoundTable02/tutor-skills:skills/tutor` |
| `scholar-skill` | `EESJGong/scholar-skill:zh-CN` |

不安装：

- `openclaw/openclaw:skills/obsidian`：旧版 Obsidian skill，已按当前决策跳过。

## 前置条件

确认 Codex 自带 `skill-installer` 存在：

```bash
ls "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py"
```

设置安装脚本变量：

```bash
export CODEX_SKILL_INSTALLER="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py"
```

## 安装命令

安装 Kepano Obsidian skills：

```bash
python3 "$CODEX_SKILL_INSTALLER" \
  --repo kepano/obsidian-skills \
  --path \
  skills/defuddle \
  skills/obsidian-cli \
  skills/obsidian-bases \
  skills/obsidian-markdown \
  skills/json-canvas
```

安装视觉类 skills：

```bash
python3 "$CODEX_SKILL_INSTALLER" \
  --repo axtonliu/axton-obsidian-visual-skills \
  --path \
  obsidian-canvas-creator \
  mermaid-visualizer \
  excalidraw-diagram
```

安装学习/论文类 skills：

```bash
python3 "$CODEX_SKILL_INSTALLER" \
  --repo RoundTable02/tutor-skills \
  --path skills/tutor-setup skills/tutor

python3 "$CODEX_SKILL_INSTALLER" \
  --repo EESJGong/scholar-skill \
  --path zh-CN \
  --name scholar-skill
```

## ScholarSkill Frontmatter 修正

`EESJGong/scholar-skill` 的 `zh-CN/SKILL.md` 默认没有 Codex YAML frontmatter。安装后补上：

```bash
perl -0pi -e 'BEGIN{$p="---\nname: scholar-skill\ndescription: Use when working with academic papers, Obsidian-based paper reading workflows, literature notes, memory extraction, research knowledge internalization, or Chinese requests for 论文阅读, 学术阅读, 文献笔记, and 知识内化.\n---\n\n"} s/\A(?!---\n)/$p/' \
  "${CODEX_HOME:-$HOME/.codex}/skills/scholar-skill/SKILL.md"
```

## 验证

确认目录和顶层 `SKILL.md` 存在：

```bash
for d in \
  defuddle \
  obsidian-cli \
  obsidian-bases \
  obsidian-markdown \
  json-canvas \
  obsidian-canvas-creator \
  mermaid-visualizer \
  excalidraw-diagram \
  tutor-setup \
  tutor \
  scholar-skill
do
  test -f "${CODEX_HOME:-$HOME/.codex}/skills/$d/SKILL.md" && echo "OK $d" || echo "MISSING $d"
done
```

确认 OpenClaw 旧版未安装：

```bash
test ! -e "${CODEX_HOME:-$HOME/.codex}/skills/obsidian" && echo "OK skipped openclaw obsidian"
```

确认 frontmatter：

```bash
for d in \
  defuddle \
  obsidian-cli \
  obsidian-bases \
  obsidian-markdown \
  json-canvas \
  obsidian-canvas-creator \
  mermaid-visualizer \
  excalidraw-diagram \
  tutor-setup \
  tutor \
  scholar-skill
do
  printf "%s: " "$d"
  sed -n '1p' "${CODEX_HOME:-$HOME/.codex}/skills/$d/SKILL.md"
done
```

每一行都应输出 `---`。

## 使用提示

- `obsidian-cli` 需要 Obsidian 正在运行，并且本机可用对应 CLI。
- `obsidian-canvas-creator` 是 `json-canvas` 的更高层替代；新建 Canvas 时优先使用它。
- `json-canvas` 保留用于底层 `.canvas` 文件格式编辑。
- `defuddle` 适合把网页清洗成 Markdown，再进入 Obsidian 或知识库。
- `tutor-setup` / `tutor` 适合把资料转成 Obsidian 学习 vault 并做测验复习。
- `scholar-skill` 适合论文阅读、文献笔记和研究知识内化。
