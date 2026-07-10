# Xiaohongshu AI Daily Research Automation

This document mirrors the Bilibili favorite-folder workflow for the Xiaohongshu favorite folder `AI/具身智能调研`.

## Command

```bash
uv run python tools/xiaohongshu_ai_daily_research.py --limit 20
```

For a non-writing classification check:

```bash
uv run python tools/xiaohongshu_ai_daily_research.py --candidates-json /path/to/candidates.json --dry-run
```

For testing one Xiaohongshu note through the deterministic pipeline:

```bash
uv run python tools/xiaohongshu_ai_daily_research.py \
  --candidate-url "https://www.xiaohongshu.com/explore/..." \
  --selected-note-ids 65f1... \
  --json
```

For the daily task, run once to get candidates, let Codex judge which `needs_model_review` notes are AI / embodied-intelligence related, then rerun with selected IDs:

```bash
uv run python tools/xiaohongshu_ai_daily_research.py --limit 20 --json
uv run python tools/xiaohongshu_ai_daily_research.py --limit 20 --selected-note-ids 65f1...,65f2... --json
```

## What The Script Does

1. Loads the latest Xiaohongshu favorite notes from OpenCLI or `--candidates-json`.
2. Normalizes note title, URL, note id, author, tags, type, media URLs, text, and timestamps.
3. Searches `raw/` and `knowledge/` for existing note id/URL references.
4. Skips duplicates before writing raw/source artifacts.
5. Marks non-duplicate notes as `needs_model_review` by default. Relevance is judged by Codex, not by keyword rules.
6. Processes only notes passed through `--selected-note-ids` or the explicit testing flag `--process-all-non-duplicates`.
7. For selected notes, calls the note-detail command to fetch full text and interaction fields.
8. Combines base note text with optional image OCR and video transcript/ASR output.
9. Writes raw note JSON under `raw/_inbox/articles/`.
10. Writes traceable C-grade source cards under `knowledge/_sources/`.
11. Writes a daily run report under `knowledge/_syntheses/`.

The script prepares source packets. Codex still performs the higher-level industry synthesis after reading those packets.

## OpenCLI Configuration

By default the script discovers Xiaohongshu favorite-like commands from:

```bash
opencli list -f json
```

If discovery cannot find the right adapter, set an explicit command:

```bash
export XIAOHONGSHU_FAVORITES_OPENCLI_COMMAND='opencli xiaohongshu favorites --limit {limit} -f json'
```

The command must print JSON containing a list or a nested list of note-like objects.

## Note Detail Enrichment

The saved-list command usually returns only title, author, note id, likes, type, and URL. Before writing selected notes, the pipeline calls a detail command:

```bash
XIAOHONGSHU_NOTE_DETAIL_COMMAND='opencli xiaohongshu note {url} -f json'
```

Available placeholders:

- `{url}` / `{note_url}`: canonical Xiaohongshu note URL, including `xsec_token` when available
- `{note_id}`: canonical note id
- `{output}`: reserved for custom commands that write to a temp output path

Useful controls:

```bash
--skip-note-detail
--note-detail-timeout 240
--refresh-existing
```

Use `--refresh-existing` when a sparse source packet was already written and you want selected duplicate notes to be reprocessed and overwritten with richer detail output.

## Image OCR / Vision Hook

If a selected note has `image_urls`, the script can run one external OCR or vision command per image:

```bash
export XIAOHONGSHU_IMAGE_OCR_COMMAND='your-ocr --image-url {image_url} --output {output}'
```

Available placeholders:

- `{image_url}` / `{url}`: image URL from the note export
- `{index}`: zero-based image index
- `{note_id}`: canonical Xiaohongshu note id
- `{output}`: temp output path the command may write

The command may print plain text or JSON with one of `ocr_text`, `image_text`, `text`, `content`, or `result`.

Useful controls:

```bash
--skip-image-ocr
--max-images 9
--image-ocr-timeout 180
```

If OCR is not configured, image URLs are still preserved in the raw packet, and the source card records that OCR was skipped.

## Video Transcript / ASR Hook

For video notes, the script first tries the local video-summarizer pipeline:

```bash
XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND='uv run --group video-ytdlp python .agents/skills/video-summarizer/scripts/video_subtitle.py {url}'
```

This uses the existing multi-platform extractor, including Xiaohongshu / yt-dlp support, and may return `subtitle_text` plus optional keyframes.

If that command returns no transcript, the script falls back to an external ASR hook. It first checks `XIAOHONGSHU_ASR_COMMAND`, then reuses `VOLCENGINE_ASR_COMMAND` when present:

```bash
export XIAOHONGSHU_ASR_COMMAND='uv run --group video-ytdlp python tools/volcengine_asr.py --url {url} --model {model} --output {output}'
```

Available placeholders:

- `{url}`: selected video URL, or the note URL when no direct video URL is exported
- `{video_url}`: direct video URL if present
- `{note_url}`: canonical Xiaohongshu note URL
- `{note_id}` / `{video_id}`: canonical note id
- `{model}`: current ASR model id
- `{output}`: temp output path the command may write

Model fallback order:

```bash
XIAOHONGSHU_ASR_MODEL_PRIMARY=volc.seedasr.auc
XIAOHONGSHU_ASR_MODEL_FALLBACK=volc.bigasr.auc
```

If these are not set, the script uses `VOLCENGINE_ASR_MODEL_PRIMARY` and `VOLCENGINE_ASR_MODEL_FALLBACK`, then defaults to the same Volcengine model ids used by the Bilibili flow.

Useful controls:

```bash
--video-transcript-mode auto   # default: try only when the export indicates video
--video-transcript-mode always # force transcript/ASR attempt for selected notes
--video-transcript-mode never  # skip video extraction
--video-transcript-timeout 900
--asr-timeout 3600
```

If video extraction fails but base note text or image OCR text exists, the note still becomes a source packet and the media failure is recorded. If no text can be captured from note/OCR/ASR, the selected note is marked `failed` unless `--allow-empty-content` is used.

## Candidate JSON Shape

Any OpenCLI adapter or offline export should provide at least `title`, `url` or `note_id`, and preferably `description`/`content`.

Useful fields:

```json
{
  "notes": [
    {
      "title": "具身智能机器人创业观察",
      "url": "https://www.xiaohongshu.com/explore/65f1...",
      "note_id": "65f1...",
      "author": "作者名",
      "description": "笔记正文",
      "tags": ["具身智能", "机器人"],
      "image_urls": ["https://..."],
      "video_url": "https://...",
      "publish_time": 1783612800,
      "favorite_time": 1783612900
    }
  ]
}
```

## Evidence Policy

Xiaohongshu source cards use evidence grade `C` by default.

Use the platform for:

- discovery of practitioner experience, product demos, hiring signals, conference notes, screenshots, and weak signals;
- finding company/product/entity names that deserve primary-source verification;
- capturing application scenarios and user language around AI and embodied intelligence.

Do not use Xiaohongshu alone for:

- company financing, valuation, revenue, customer, order, or shipment claims;
- policy text, subsidy rules, standards, and market-size numbers;
- benchmark/model performance claims unless the original paper, code, product doc, or official disclosure is verified.

## Scheduled Codex Handoff

The automation should first run:

```bash
uv run python tools/xiaohongshu_ai_daily_research.py --limit 20 --json
```

Then Codex should read the generated run report and any new raw/source artifacts.

For every note that is both selected by model judgment and `status=processed`, Codex should either:

- create or update one standalone synthesis page under `knowledge/_syntheses/` when the note is unusually valuable; or
- merge the lead into existing AI / robotics research notes, entity pages, concept pages, or claim queues.

Notes that are `failed`, `skipped_duplicate`, or not selected should not receive fabricated synthesis pages; record them as retry or follow-up items instead.

## Failed Case Handling

For any `failed` selected note, identify the failing boundary:

1. candidate fetch;
2. JSON normalization;
3. duplicate detection;
4. image OCR command;
5. video subtitle extraction;
6. ASR submit/query or external ASR command;
7. missing text content;
8. source-card writing;
9. index/log update;
10. Git finalization.

If the export contains only URL/id metadata, rerun with a richer OpenCLI/JSON export, or force video extraction with `--video-transcript-mode always`. Use `--allow-empty-content` only when the URL/id itself is a deliberate tracking item.

Never fabricate note text, author names, dates, image OCR output, video transcript, media URLs, screenshots, or engagement data.

## Git Commit And Push

After capture, synthesis, index, log, and final run-report work is complete, inspect the working tree:

```bash
git status --short
```

Only stage files created or modified by the current automation run, such as:

- `raw/_inbox/articles/` Xiaohongshu note JSON files
- `knowledge/_sources/` Xiaohongshu source cards
- `knowledge/_syntheses/` daily reports or deeper research notes
- relevant `knowledge/<industry>/sources.csv` files
- `knowledge/index.md`
- `knowledge/log.md`
- task-required script or documentation changes

Do not stage unrelated user-local changes, secrets, cookies, browser state, screenshots with private data, or unrelated Obsidian app state.

If there are current-run changes, use a date-specific commit message:

```bash
git commit -m "research: daily xiaohongshu AI analysis YYYY-MM-DD"
```
