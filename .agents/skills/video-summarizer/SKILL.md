---
name: video-summarizer
description: Use when the user provides a video or audio URL and asks to summarize, extract subtitles, create video notes, 视频总结, 视频笔记, or summarize content from Bilibili, YouTube, Douyin, Xiaohongshu, TikTok, or yt-dlp supported sites.
---

# Video Summarizer

## Core Rule

Extract the transcript first, then summarize from evidence. Do not invent content when extraction fails.

This skill is a Codex-native port of `keepongo/video-summarizer` at upstream commit `481a772`.

## Supported Inputs

- Bilibili: `bilibili.com/video/`, `b23.tv/`, `BV...`
- YouTube: `youtube.com/watch`, `youtu.be/`, `youtube.com/shorts/`
- Douyin: `douyin.com`, `v.douyin.com`
- Xiaohongshu: `xiaohongshu.com`, `xhslink.com`
- TikTok and many other sites through `yt-dlp`

## Workflow

1. Choose dependencies from `references/dependencies.md`.
2. Run `scripts/video_subtitle.py` with `uv run python ...`; add `uv --group ...` dependency groups only when the platform needs them.
3. Parse the JSON output. If it contains `error`, report the failure and the next concrete fix.
4. Summarize only from `subtitle_text`. If `frames` are present, embed selected images with absolute paths.
5. Use the output format in `references/output-format.md`.

## Commands

Bilibili or direct-platform extraction:

```bash
uv run python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

YouTube:

```bash
uv run --group video-youtube python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

TikTok, generic sites, or yt-dlp fallback:

```bash
uv run --group video-ytdlp python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

OpenAI Whisper API fallback:

```bash
OPENAI_API_KEY=... uv run --group video-ytdlp --group video-whisper-api python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

Local Whisper fallback is heavy. Use it only when the user explicitly wants audio transcription and accepts model downloads:

```bash
uv run --group video-ytdlp --group video-whisper-local python .agents/skills/video-summarizer/scripts/video_subtitle.py "<VIDEO_URL>"
```

Clear cached transcript and screenshots:

```bash
uv run python .agents/skills/video-summarizer/scripts/video_subtitle.py --clear-cache
```

## Configuration

- Copy `references/config.example.json` to `.agents/skills/video-summarizer/config.json` for local settings.
- Use `references/config.whisper-api.example.json` or `references/config.whisper-local.example.json` when enabling Whisper.
- Read `references/setup.md` when initializing this skill on a new machine or checking environment readiness.
- Keep `config.json`, cookies, cache, and screenshots untracked.
- Prefer `OPENAI_API_KEY` for OpenAI Whisper API instead of writing a key into config.

## Failure Handling

- Missing dependency: rerun with the matching `uv run --group ...` command.
- No subtitles: ask whether to enable Whisper fallback.
- Frame extraction missing: continue with text-only output unless the user specifically needs images.
- Platform/cookie block: explain the platform limitation and point to `references/dependencies.md`.
