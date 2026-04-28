# Dependencies

Use `uv run` for all Python execution. Video dependencies are managed as `uv` dependency groups in `pyproject.toml`.

## Minimal

Bilibili usually works with Python standard library only:

```bash
uv run python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"
```

## Platform Packages


| Need                              | Command                                                                                                                                            |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| YouTube transcript API            | `uv run --group video-youtube python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"`                                            |
| yt-dlp fallback and generic sites | `uv run --group video-ytdlp python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"`                                              |
| OpenAI Whisper API                | `OPENAI_API_KEY=... uv run --group video-ytdlp --group video-whisper-api python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"` |
| Local Whisper                     | `uv run --group video-ytdlp --group video-whisper-local python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"`                  |
| Screenshot image optimization     | `uv run --group video-frames python .agents/skills/video-summarizer/scripts/video_subtitle.py "<URL>"`                                             |


## Dependency Groups

- `video-youtube`: `youtube-transcript-api`
- `video-ytdlp`: `yt-dlp`
- `video-whisper-api`: `openai`, `pydub`, `audioop-lts` on Python 3.13+
- `video-whisper-local`: `faster-whisper`
- `video-frames`: `pillow`

## System Tools

- `ffmpeg` is required for keyframe screenshots and audio handling.
- If `ffmpeg` is missing, the script should still return text when subtitles are available.

## Local Files

Do not commit these files:

- `.agents/skills/video-summarizer/config.json`
- `.agents/skills/video-summarizer/cache/`
- `.agents/skills/video-summarizer/screenshots/`
- `.agents/skills/video-summarizer/*cookies*.txt`

TikTok and some other sites may require exported browser cookies. Save cookie files in the skill directory only when needed.
