# Bilibili AI Daily Research Automation

This document describes the deterministic capture script used by the scheduled Codex task.

## Command

```bash
uv run python tools/bilibili_ai_daily_research.py --limit 20
```

For a non-writing classification check:

```bash
uv run python tools/bilibili_ai_daily_research.py --candidates-json /path/to/candidates.json --dry-run
```

For testing one Bilibili video through the real pipeline:

```bash
uv run python tools/bilibili_ai_daily_research.py \
  --candidate-url "https://www.bilibili.com/video/BV..." \
  --selected-video-ids BV... \
  --json
```

For the daily task, run once to get candidates, let Codex judge which `needs_model_review` videos are AI / embodied-intelligence related, then rerun with selected IDs:

```bash
uv run python tools/bilibili_ai_daily_research.py --limit 20 --json
uv run python tools/bilibili_ai_daily_research.py --limit 20 --selected-video-ids BVxxx,BVyyy --json
```

## What The Script Does

1. Loads the latest Bilibili favorite videos from OpenCLI or `--candidates-json`.
2. Normalizes video title, URL, BV/video id, author, tags, category, and timestamps.
3. Searches `raw/` and `knowledge/` for existing BV/video id/URL references.
4. Skips duplicates before subtitle extraction or ASR.
5. Marks non-duplicate videos as `needs_model_review` by default. Relevance is judged by Codex, not by keyword rules.
6. Processes only videos passed through `--selected-video-ids` or the explicit testing flag `--process-all-non-duplicates`.
7. Calls `.agents/skills/video-summarizer/scripts/video_subtitle.py` for subtitles.
8. If subtitles fail, calls `VOLCENGINE_ASR_COMMAND` when configured.
9. Writes raw transcript JSON under `raw/_inbox/transcripts/`.
10. Writes traceable source cards under `knowledge/_sources/`.
11. Checks the current TOS audio prefix when TOS credentials are configured and records the result in the daily run report.
12. Writes a daily run report under `knowledge/_syntheses/`.

The script prepares source packets. Codex still performs the higher-level industry synthesis after reading those packets.

## OpenCLI Configuration

By default the script discovers Bilibili favorite-like commands from:

```bash
opencli list -f json
```

If discovery cannot find the right adapter, set an explicit command:

```bash
export BILIBILI_FAVORITES_OPENCLI_COMMAND='opencli bilibili favorites --limit {limit} -f json'
```

The command must print JSON containing a list or a nested list of video-like objects.

## Environment

The script automatically loads simple `KEY=VALUE` lines from:

1. `~/.env`
2. project-local `.env`

Existing process environment variables win over `.env` values.

## Volcengine ASR Hook

The script does not store API credentials. Configure a local command that performs the Volcengine ASR request and prints transcript text or JSON:

```bash
export VOLCENGINE_ASR_COMMAND='uv run --group video-ytdlp python tools/volcengine_asr.py --url {url} --model {model} --output {output}'
```

Available placeholders:

- `{url}`: Bilibili video URL
- `{bvid}`: BV id when available
- `{video_id}`: canonical id
- `{model}`: current ASR model id
- `{output}`: temp output path the command may write

Expected output can be plain text or JSON with one of `subtitle_text`, `transcript`, `text`, or `result`.

Model fallback order:

```bash
VOLCENGINE_ASR_MODEL_PRIMARY=volc.seedasr.auc
VOLCENGINE_ASR_MODEL_FALLBACK=volc.bigasr.auc
```

The pipeline tries `VOLCENGINE_ASR_MODEL_PRIMARY` first. If the external ASR command exits non-zero or returns an empty transcript, it retries with `VOLCENGINE_ASR_MODEL_FALLBACK`.

The parent pipeline kills the whole external ASR process group when `--asr-timeout` is exceeded, so a stuck uploader or child process should now return a clear timeout failure instead of hanging the daily task indefinitely.

### Bilibili 412 And Audio Upload

Bilibili page/subtitle scraping can return HTTP 412. The ASR adapter handles this by asking `yt-dlp` to download the audio locally with Bilibili headers and optional cookies:

Before using cookies, `tools/volcengine_asr.py` now tries Bilibili's public metadata and `playurl` APIs to fetch the DASH audio URL by BV/cid. This avoids the webpage path that often triggers 412 and keeps the daily task independent of browser login state for public videos.

```bash
BILIBILI_YTDLP_COOKIES_FILE=/path/to/bilibili-cookies.txt
# or, only when explicitly allowed in the local environment:
BILIBILI_YTDLP_COOKIES_FROM_BROWSER=chrome
```

Volcengine AUC downloads `audio.url` from Volcengine's servers. Bilibili signed CDN URLs are not stable public audio URLs for that server-side fetch, and can fail as `Invalid audio URI`. For Bilibili videos the adapter therefore downloads audio locally, then runs an upload hook:

```bash
VOLCENGINE_AUDIO_UPLOAD_COMMAND='your-uploader --input {input} --filename {filename} --content-type {content_type}'
VOLCENGINE_ASR_FORCE_UPLOAD=1
VOLCENGINE_AUDIO_UPLOAD_RETRIES=3
```

The upload command must print either a public HTTPS URL or JSON with one of `url`, `audio_url`, `public_url`, or `uri`. The public URL should remain valid until the ASR job finishes. This hook can point to TOS, S3, R2, MinIO, or any internal uploader; the daily pipeline does not need to know which storage provider is used.

For TOS / Volcengine-hosted URLs, `tools/volcengine_asr.py` verifies the uploaded URL with a small ranged GET before submitting it to Volcengine ASR. If the upload command exits non-zero, prints no URL, or the uploaded URL is not reachable, the adapter retries up to `VOLCENGINE_AUDIO_UPLOAD_RETRIES` times and returns an explicit `audio upload failed after ... attempts` error to the daily report.

For the current Volcengine TOS bucket `industry-analysis`, use the built-in uploader:

```bash
VOLCENGINE_AUDIO_UPLOAD_COMMAND='uv run --with tos python tools/tos_upload.py --input {input} --filename {filename} --content-type {content_type}'
TOS_BUCKET=industry-analysis
TOS_REGION=cn-beijing
TOS_ENDPOINT=https://tos-cn-beijing.volces.com
TOS_PUBLIC_BASE_URL=https://industry-analysis.tos-cn-beijing.volces.com
TOS_ADDRESSING_STYLE=virtual
TOS_SIGNING_SERVICE=s3
TOS_PRESIGN_EXPIRES=86400
```

`tools/tos_upload.py` uses the Volcengine `tos` Python SDK when available, then prints a presigned `GET` URL. This means the bucket does not have to be public. If the SDK is unavailable, the script falls back to an S3-compatible signer.

For structured upload metadata, the uploader also supports JSON output:

```bash
uv run --with tos python tools/tos_upload.py \
  --input /path/to/audio.m4a \
  --filename audio.m4a \
  --content-type audio/mp4 \
  --json
```

The JSON payload includes `bucket`, `key`, and `url`. The ASR adapter still accepts plain URL output, but JSON is preferred because it makes failed or missing TOS objects easier to diagnose.

To inspect the current TOS audio directory used by the daily automation:

```bash
uv run python tools/tos_upload.py --list-prefix asr-audio/YYYY/MM/DD --json
```

`tools/bilibili_ai_daily_research.py` performs this check automatically when TOS credentials are present. The daily run report includes a `## TOS Audio Check` section with the checked prefix, object count, recent keys, or a clear error such as missing credentials or list failure. This is the first place to look when selected videos fail before transcript generation.

Reference API documentation: https://www.volcengine.com/docs/6561/1354868?lang=zh

## Volcengine Console Field Mapping

The Speech Recognition console package shown as `录音文件识别大模型-标准版` exposes service-level credentials:

| Console field | `.env` variable | Notes |
| --- | --- | --- |
| APP ID | `VOLCENGINE_APP_ID` | Numeric app id shown under service API authentication. |
| Access Token | `VOLCENGINE_ACCESS_TOKEN` | This is the speech service token, not the general cloud `AccessKeyId`. |
| Secret Key | `VOLCENGINE_SECRET_KEY` | Speech service secret key. Keep out of git. |
| 实例ID/名称 | `VOLCENGINE_ASR_INSTANCE_ID` | Optional traceability/debug field; usually not passed as auth. |
| 服务名称 | `VOLCENGINE_ASR_SERVICE_NAME` | Optional descriptive field. |

Keep legacy cloud AK/SK variables separate if a future SDK needs them:

```bash
VOLCENGINE_ACCESS_KEY_ID=
VOLCENGINE_SECRET_ACCESS_KEY=
```

For TOS uploads, use the cloud account AccessKey pair from Volcengine IAM/访问控制, not the ASR service Access Token:

```bash
TOS_ACCESS_KEY_ID=
TOS_SECRET_ACCESS_KEY=
```

`tools/tos_upload.py` also accepts the legacy aliases `VOLCENGINE_ACCESS_KEY_ID` and `VOLCENGINE_SECRET_ACCESS_KEY`, but the `TOS_*` names are clearer for this pipeline.

### How To Find TOS AK/SK

In the Volcengine console, the TOS uploader needs a cloud-account AccessKey pair:

1. Open the console avatar/account menu or search box.
2. Go to `访问控制` / `IAM`.
3. Open `访问密钥` / `AccessKey 管理`.
4. Create or reveal an AccessKey for the current account or a dedicated RAM/IAM user with TOS write/read permission on bucket `industry-analysis`.
5. Put the values into `~/.env`:

```bash
TOS_ACCESS_KEY_ID=...
TOS_SECRET_ACCESS_KEY=...
```

Do not put the ASR service `Access Token` into `TOS_ACCESS_KEY_ID`; it is only for the speech API headers.

## Scheduled Codex Handoff

The automation should first run:

```bash
uv run python tools/bilibili_ai_daily_research.py --limit 20 --json
```

Then Codex should read the generated run report, source cards, and raw transcript JSON files.

For every video that is both selected by model judgment and `status=processed`, Codex should create or update one standalone deep-research synthesis page under `knowledge/_syntheses/`. The per-video deep-research page is the primary durable output. It should cover the whole selected video, including:

- source metadata and transcript path;
- full-video thesis, not just isolated clips;
- facts, estimates, judgments, and hypotheses separated clearly;
- primary-source verification for important claims when available;
- industry implications, investment/career angles when relevant, risks, and monitoring indicators;
- follow-up verification tasks and Obsidian wikilinks.

Cross-video daily overview pages are optional navigation/synthesis artifacts. They must not replace the per-selected-video deep-research pages. Videos that are `failed`, `skipped_duplicate`, or not selected should not receive fabricated deep-research pages; record them as retry or follow-up items instead.

## Failed Case Handling And Self-Repair

For any `failed` selected video, the scheduled task should not stop at reporting the failure. Codex should autonomously investigate the root cause in the same run when feasible, then optimize the pipeline or configuration before finalizing:

1. Identify the failing boundary: candidate fetch, duplicate detection, subtitle extraction, audio download, TOS upload, uploaded URL verification, Volcengine ASR submit/query, transcript parsing, source-card writing, or Git finalization.
2. Preserve evidence in the daily run report: exact video id, failing command/stage, exit code or timeout, stderr/stdout excerpt, TOS prefix/object count when relevant, retry count, and whether any raw/source artifact was written.
3. Retry transient failures with bounded attempts. Do not retry indefinitely, and do not create source cards or deep-research pages unless the video reaches `status=processed`.
4. If the root cause is a pipeline bug, missing diagnostic, timeout problem, upload visibility problem, or recoverable script/config issue, fix the tooling in the same run, add or update tests, rerun the smallest relevant verification command, and include the fix in the same Git commit or a follow-up tooling commit.
5. If the root cause requires external state that Codex cannot change, such as expired credentials, missing paid quota, broken upstream service, unavailable Bilibili media, or user-owned TOS permission changes, report the precise manual action required and leave the failed video as a retry item.
6. Never fabricate transcript content, source metadata, publication dates, play counts, TOS object keys, or ASR output while investigating failures.

## Git Commit And Push

After all capture, synthesis, index, log, and final run-report work is complete, the scheduled Codex task should commit and push the daily changes.

The task should first inspect the working tree:

```bash
git status --short
```

Only stage files created or modified by the current automation run, such as:

- `raw/_inbox/transcripts/` transcript JSON files
- `knowledge/_sources/` Bilibili source cards
- `knowledge/_syntheses/` daily reports or deeper research notes
- relevant `knowledge/<industry>/sources.csv` files
- `knowledge/index.md`
- `knowledge/log.md`
- task-required script or documentation changes

Do not stage unrelated user-local changes. In particular, never commit:

- `.env` or any file containing secrets
- browser cookies or login state
- cached subtitles, temporary audio, or ASR scratch files
- unrelated Obsidian app state
- unrelated edits already present before the automation run

If there are no current-run changes to commit, report `无可提交变更` and do not create an empty commit.

If there are current-run changes, use a date-specific commit message:

```bash
git commit -m "research: daily bilibili AI analysis YYYY-MM-DD"
```

Then push to the current branch upstream:

```bash
git push
```

If the current branch has no upstream, set it on first push:

```bash
git push -u origin HEAD
```

If commit or push fails, include the exact failure reason and the required manual action in the final daily run report.
