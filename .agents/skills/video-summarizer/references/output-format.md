# Output Format

When extraction succeeds, produce Markdown notes in the original language of the video.

## Required Structure

```markdown
# Video Notes: [{title}]({url})

## Source

- Platform:
- Author:
- Duration:
- Transcript source:

## Executive Summary

One concise paragraph summarizing the full video.

## Key Sections

### Section title

- Main point.
- Supporting detail or example.
    * Sub-point when useful.

### Section title

- Main point.
- Supporting detail or example.

## Highlights

- Highlight 1. [#tag] [#tag] [#tag]
- Highlight 2. [#tag] [#tag] [#tag]
- Highlight 3. [#tag] [#tag] [#tag]
- Highlight 4. [#tag] [#tag] [#tag]
- Highlight 5. [#tag] [#tag] [#tag]

## Questions

- Follow-up question 1.
- Follow-up question 2.

## Tags

[#tag1] [#tag2] [#tag3] [#tag4] [#tag5]
```

## Notes

- Preserve vivid examples, analogies, and numbers from the transcript.
- If `frames` are present, embed at most one image per major section with `![title](/absolute/path.jpg)`.
- If `source` is `ai_conclusion`, say the transcript came from Bilibili built-in AI summary.
- If `source` is `whisper_local` or `whisper_api`, say speech recognition may contain minor errors.
- If extraction fails, do not summarize the video from title or metadata alone.
