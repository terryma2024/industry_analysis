# Setup

Use this when restoring `$video-summarizer` on a fresh machine or checking whether the environment is ready.

## Bootstrap

```bash
git clone https://github.com/terryma2024/industry_analysis.git
cd industry_analysis
uv sync --locked
```

Install `uv` first if missing. Install `ffmpeg` separately when screenshots or audio processing are needed.

## Dependency Groups

Preload only the groups needed:

```bash
uv sync --locked --group video-youtube
uv sync --locked --group video-ytdlp
uv sync --locked --group video-whisper-api
uv sync --locked --group video-frames
UV_HTTP_TIMEOUT=180 uv sync --locked --group video-whisper-local
```

`video-whisper-local` is heavy and may download large wheels and model files later.

## Local Config

Default behavior works without `config.json`.

Copy one config only when needed:

```bash
cp .agents/skills/video-summarizer/references/config.example.json .agents/skills/video-summarizer/config.json
cp .agents/skills/video-summarizer/references/config.whisper-api.example.json .agents/skills/video-summarizer/config.json
cp .agents/skills/video-summarizer/references/config.whisper-local.example.json .agents/skills/video-summarizer/config.json
```

Prefer `OPENAI_API_KEY` for API mode. Never commit `config.json`, cookies, cache, or screenshots.

## Verification

```bash
uv run python .agents/skills/industry-analysis/scripts/check_workspace.py
uv run --group video-youtube --group video-ytdlp --group video-whisper-api --group video-whisper-local --group video-frames python -X pycache_prefix=/tmp -m py_compile .agents/skills/video-summarizer/scripts/video_subtitle.py
uv run --group video-youtube python -c "import youtube_transcript_api; print('youtube ok')"
uv run --group video-ytdlp python -m yt_dlp --version
uv run --group video-whisper-api python -c "import openai; from pydub import AudioSegment; print('whisper api ok')"
UV_HTTP_TIMEOUT=180 uv run --group video-whisper-local python -c "import faster_whisper; print('local whisper ok')"
uv run --group video-frames python -c "from PIL import Image; print('frames ok')"
```
