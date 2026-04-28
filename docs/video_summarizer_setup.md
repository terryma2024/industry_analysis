# Video Summarizer 初始化指南

这份文档用于在新机器或新环境中快速恢复 `$video-summarizer` 能力。

## 1. 前置条件

- 已安装 `git`
- 已安装 `uv`
- 推荐安装 Python `3.13`，项目会读取 `.python-version`
- 可选安装 `ffmpeg`，用于截图和音频处理

macOS 可用：

```bash
brew install uv ffmpeg
```

如果已经安装过 `uv`，只需要确认：

```bash
uv --version
```

## 2. 拉取项目

```bash
git clone https://github.com/terryma2024/industry_analysis.git
cd industry_analysis
```

## 3. 同步基础环境

```bash
uv sync --locked
```

基础环境适合 B站等不需要额外 Python 包的平台。

## 4. 预热视频能力依赖

按需执行。全部执行会下载较多依赖，尤其本地 Whisper。

```bash
uv sync --locked --group video-youtube
uv sync --locked --group video-ytdlp
uv sync --locked --group video-whisper-api
uv sync --locked --group video-frames
```

本地 Whisper 较重，首次可能下载 `faster-whisper`、`onnxruntime` 和模型相关依赖：

```bash
UV_HTTP_TIMEOUT=180 uv sync --locked --group video-whisper-local
```

## 5. 本地配置

默认不需要创建配置文件。需要开启 Whisper 或截图时，再复制样例：

```bash
cp .agents/skills/video-summarizer/references/config.example.json \
  .agents/skills/video-summarizer/config.json
```

OpenAI Whisper API：

```bash
cp .agents/skills/video-summarizer/references/config.whisper-api.example.json \
  .agents/skills/video-summarizer/config.json
export OPENAI_API_KEY="sk-..."
```

本地 Whisper：

```bash
cp .agents/skills/video-summarizer/references/config.whisper-local.example.json \
  .agents/skills/video-summarizer/config.json
```

`config.json`、cookies、cache、screenshots 已在 `.gitignore` 中忽略，不要提交。

## 6. 验证命令

项目结构：

```bash
uv run python .agents/skills/industry-analysis/scripts/check_workspace.py
```

脚本语法：

```bash
uv run --group video-youtube --group video-ytdlp --group video-whisper-api --group video-whisper-local --group video-frames \
  python -X pycache_prefix=/tmp -m py_compile .agents/skills/video-summarizer/scripts/video_subtitle.py
```

依赖导入：

```bash
uv run --group video-youtube python -c "import youtube_transcript_api; print('youtube ok')"
uv run --group video-ytdlp python -m yt_dlp --version
uv run --group video-whisper-api python -c "import openai; from pydub import AudioSegment; print('whisper api ok')"
UV_HTTP_TIMEOUT=180 uv run --group video-whisper-local python -c "import faster_whisper; print('local whisper ok')"
uv run --group video-frames python -c "from PIL import Image; print('frames ok')"
```

## 7. 使用命令

B站或基础提取：

```bash
uv run python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

YouTube：

```bash
uv run --group video-youtube python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

yt-dlp 平台：

```bash
uv run --group video-ytdlp python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

OpenAI Whisper API：

```bash
OPENAI_API_KEY="sk-..." uv run --group video-ytdlp --group video-whisper-api \
  python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

本地 Whisper：

```bash
UV_HTTP_TIMEOUT=180 uv run --group video-ytdlp --group video-whisper-local \
  python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

## 8. 常见问题

- `onnxruntime` 下载超时：给命令加 `UV_HTTP_TIMEOUT=180`。
- `pydub` 在 Python 3.13 下缺 `audioop`：项目已在 `video-whisper-api` 组加入 `audioop-lts`。
- 没有字幕：开启 Whisper API 或本地 Whisper。
- 没有截图：安装 `ffmpeg`，并在 `config.json` 中设置 `"extract_frames": true`。
- 平台需要 cookies：把导出的 `cookies.txt` 放在 `.agents/skills/video-summarizer/`，不要提交。
