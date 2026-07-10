import json
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest import mock

from tools import xiaohongshu_ai_daily_research as tool


class XiaohongshuAiDailyResearchTests(unittest.TestCase):
    def test_normalize_candidate_extracts_note_id_from_url(self) -> None:
        candidate = tool.normalize_candidate(
            {
                "title": "具身智能机器人创业笔记",
                "url": "https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345?xsec_token=abc",
                "user": {"nickname": "Tester"},
                "tags": [{"name": "具身智能"}, {"name": "AI"}],
            }
        )

        self.assertEqual(candidate.note_id, "65f1a2b3c4d5e6f789012345")
        self.assertEqual(candidate.author, "Tester")
        self.assertIn("具身智能", candidate.tags)

    def test_extract_note_id_from_discovery_url(self) -> None:
        note_id = tool.extract_note_id(
            "https://www.xiaohongshu.com/discovery/item/65f1a2b3c4d5e6f789012345?source=webshare"
        )

        self.assertEqual(note_id, "65f1a2b3c4d5e6f789012345")

    def test_relevance_selects_embodied_ai_note(self) -> None:
        candidate = tool.NoteCandidate(
            title="具身智能机器人 VLA 世界模型创业观察",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            description="Unitree、LeRobot、Isaac GR00T 和机器人训练数据。",
        )

        score, terms, industries = tool.relevance(candidate)

        self.assertGreaterEqual(score, 2)
        self.assertIn("robotics-embodied-ai", industries)
        self.assertTrue(terms)

    def test_non_duplicate_requires_model_review_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            candidate = tool.NoteCandidate(
                title="具身智能机器人 VLA 世界模型创业观察",
                url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
                note_id="65f1a2b3c4d5e6f789012345",
            )

            decision = tool.decide_candidate(repo, candidate)

        self.assertEqual(decision.status, "needs_model_review")

    def test_selected_note_id_is_processed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            candidate = tool.NoteCandidate(
                title="AI Agent 工具链笔记",
                url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
                note_id="65f1a2b3c4d5e6f789012345",
            )

            decision = tool.decide_candidate(repo, candidate, selected_ids={"65f1a2b3c4d5e6f789012345"})

        self.assertEqual(decision.status, "selected")
        self.assertEqual(decision.reason, "selected by model relevance judgment")

    def test_duplicate_detection_ignores_failed_mentions_in_log(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            (repo / "knowledge" / "log.md").write_text(
                "- 65f1a2b3c4d5e6f789012345 failed before source card; retry later.\n",
                encoding="utf-8",
            )
            candidate = tool.NoteCandidate(
                title="机器人失败重试笔记",
                url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
                note_id="65f1a2b3c4d5e6f789012345",
            )

            hits = tool.find_duplicate_hits(repo, candidate)
            decision = tool.decide_candidate(repo, candidate, selected_ids={"65f1a2b3c4d5e6f789012345"})

        self.assertEqual(hits, [])
        self.assertEqual(decision.status, "selected")

    def test_refresh_existing_allows_selected_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            (repo / "knowledge" / "source.md").write_text(
                "https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345\n",
                encoding="utf-8",
            )
            candidate = tool.NoteCandidate(
                title="机器人重复笔记",
                url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
                note_id="65f1a2b3c4d5e6f789012345",
            )

            decision = tool.decide_candidate(
                repo,
                candidate,
                selected_ids={"65f1a2b3c4d5e6f789012345"},
                refresh_existing=True,
            )

        self.assertEqual(decision.status, "selected")
        self.assertTrue(decision.duplicate_hits)
        self.assertIn("refreshing existing", decision.reason)

    def test_load_candidates_from_nested_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "candidates.json"
            path.write_text(
                json.dumps(
                    {
                        "data": {
                            "notes": [
                                {
                                    "title": "AI Agent demo",
                                    "note_id": "65f1a2b3c4d5e6f789012345",
                                    "user": {"nickname": "Author"},
                                }
                            ]
                        }
                    }
                ),
                encoding="utf-8",
            )

            candidates = tool.load_candidates_from_json(path, limit=20)

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].note_id, "65f1a2b3c4d5e6f789012345")
        self.assertEqual(candidates[0].author, "Author")

    def test_enrich_candidate_with_note_detail(self) -> None:
        candidate = tool.NoteCandidate(
            title="旧标题",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
        )
        detail = {
            "title": "新标题",
            "author": "作者",
            "content": "正文内容 #具身智能",
            "tags": "#具身智能, #WAM",
            "likes": "32",
        }

        enriched = tool.enrich_candidate_with_detail(candidate, detail)

        self.assertEqual(enriched.title, "新标题")
        self.assertEqual(enriched.author, "作者")
        self.assertEqual(enriched.description, "正文内容 #具身智能")
        self.assertIn("具身智能", enriched.tags)
        self.assertEqual(enriched.raw["note_detail"]["likes"], "32")

    def test_fetch_note_detail_parses_field_value_output(self) -> None:
        candidate = tool.NoteCandidate(
            title="旧标题",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
        )
        args = tool.build_arg_parser().parse_args(["--candidate-url", candidate.url])
        stdout = json.dumps(
            [
                {"field": "title", "value": "新标题"},
                {"field": "content", "value": "正文内容"},
            ]
        )
        completed = tool.subprocess.CompletedProcess(args=[], returncode=0, stdout=stdout, stderr="")

        with mock.patch.object(tool, "run_command", return_value=completed):
            detail, error = tool.fetch_note_detail(candidate, args)

        self.assertEqual(error, "")
        self.assertEqual(detail["content"], "正文内容")

    def test_write_artifacts_creates_raw_packet_and_source_card(self) -> None:
        candidate = tool.NoteCandidate(
            title="具身智能机器人 VLA 世界模型创业观察",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
            description="这是关于机器人训练数据的笔记。",
            image_urls=["https://example.com/1.jpg"],
            video_url="https://example.com/1.mp4",
        )
        decision = tool.CandidateDecision(
            candidate=candidate,
            status="selected",
            reason="selected",
            relevance_score=2,
            target_industries=["robotics-embodied-ai", "ai"],
        )
        result = tool.ProcessResult(decision=decision, status="failed", reason="")

        with tempfile.TemporaryDirectory() as tmpdir:
            old_raw = tool.RAW_ARTICLES_DIR
            old_sources = tool.SOURCES_DIR
            tool.RAW_ARTICLES_DIR = Path(tmpdir) / "raw/_inbox/articles"
            tool.SOURCES_DIR = Path(tmpdir) / "knowledge/_sources"
            try:
                media = tool.MediaExtractionResult(
                    content_text=candidate.content_text() + "\n\n[Image 1 OCR]\n机器人图片文字",
                    extraction_method="base-note-text+image-ocr",
                    image_ocr=[
                        tool.ImageOcrResult(
                            index=0,
                            url="https://example.com/1.jpg",
                            text="机器人图片文字",
                            method="test-ocr",
                        )
                    ],
                    video_transcript=tool.VideoTranscriptResult(
                        url="https://example.com/1.mp4",
                        text="视频转录文字",
                        method="test-asr",
                    ),
                )
                processed = tool.write_artifacts(result, media)
                raw_path = tool.REPO_ROOT / processed.raw_artifact
                source_path = tool.REPO_ROOT / processed.source_card
                self.assertEqual(processed.status, "processed")
                self.assertTrue(raw_path.exists())
                self.assertTrue(source_path.exists())
                raw_payload = json.loads(raw_path.read_text(encoding="utf-8"))
                source_text = source_path.read_text(encoding="utf-8")
                self.assertIn("evidence_grade: C", source_text)
                self.assertEqual(raw_payload["image_ocr"][0]["text"], "机器人图片文字")
                self.assertEqual(raw_payload["video_transcript"]["text"], "视频转录文字")
                self.assertIn("| Images OCR'd | 1 |", source_text)
                self.assertIn("| Video transcript method | test-asr |", source_text)
            finally:
                tool.RAW_ARTICLES_DIR = old_raw
                tool.SOURCES_DIR = old_sources

    def test_run_image_ocr_uses_configured_command(self) -> None:
        candidate = tool.NoteCandidate(
            title="图片笔记",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
            image_urls=["https://example.com/1.jpg"],
        )
        args = tool.build_arg_parser().parse_args(["--candidate-url", candidate.url])
        completed = tool.subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=json.dumps({"ocr_text": "图片中的机器人训练数据"}),
            stderr="",
        )

        with mock.patch.dict(tool.os.environ, {"XIAOHONGSHU_IMAGE_OCR_COMMAND": "ocr --url {image_url}"}, clear=True):
            with mock.patch.object(tool, "run_command", return_value=completed):
                results = tool.run_image_ocr(candidate, args)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].text, "图片中的机器人训练数据")
        self.assertEqual(results[0].error, "")

    def test_run_video_transcript_uses_video_subtitle_command(self) -> None:
        candidate = tool.NoteCandidate(
            title="视频笔记",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
            video_url="https://example.com/video.mp4",
        )
        args = tool.build_arg_parser().parse_args(["--candidate-url", candidate.url])
        completed = tool.subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=json.dumps(
                {
                    "subtitle_text": "视频里的 VLA 讲解",
                    "source": "test-video-subtitle",
                    "frames": [{"path": "/tmp/frame.jpg", "timestamp": "00:03"}],
                }
            ),
            stderr="",
        )

        with mock.patch.dict(tool.os.environ, {"XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND": "video-sub {url}"}, clear=True):
            with mock.patch.object(tool, "run_command", return_value=completed):
                result = tool.run_video_transcript(candidate, args)

        self.assertIsNotNone(result)
        self.assertEqual(result.text, "视频里的 VLA 讲解")
        self.assertEqual(result.method, "test-video-subtitle")
        self.assertEqual(result.frames[0]["path"], "/tmp/frame.jpg")

    def test_run_video_transcript_falls_back_to_external_asr(self) -> None:
        candidate = tool.NoteCandidate(
            title="视频笔记",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
            video_url="https://example.com/video.mp4",
        )
        args = tool.build_arg_parser().parse_args(["--candidate-url", candidate.url])
        calls = []

        def fake_run_command(command, cwd=tool.REPO_ROOT, timeout=180):
            calls.append(command)
            if command[0] == "video-sub":
                return tool.subprocess.CompletedProcess(command, 1, json.dumps({"error": "no subtitle"}), "")
            return tool.subprocess.CompletedProcess(command, 0, json.dumps({"text": "ASR 转录文本"}), "")

        env = {
            "XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND": "video-sub {url}",
            "XIAOHONGSHU_ASR_COMMAND": "asr --url {url} --model {model}",
            "XIAOHONGSHU_ASR_MODEL_PRIMARY": "primary-model",
            "XIAOHONGSHU_ASR_MODEL_FALLBACK": "fallback-model",
        }
        with mock.patch.dict(tool.os.environ, env, clear=True):
            with mock.patch.object(tool, "run_command", side_effect=fake_run_command):
                result = tool.run_video_transcript(candidate, args)

        self.assertEqual(result.text, "ASR 转录文本")
        self.assertEqual(result.method, "external-asr-command:primary-model")
        self.assertEqual(len(calls), 2)

    def test_extract_media_content_combines_base_ocr_and_video(self) -> None:
        candidate = tool.NoteCandidate(
            title="混合笔记",
            url="https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
            note_id="65f1a2b3c4d5e6f789012345",
            description="正文",
            image_urls=["https://example.com/1.jpg"],
            video_url="https://example.com/video.mp4",
        )
        args = tool.build_arg_parser().parse_args(["--candidate-url", candidate.url])

        with mock.patch.object(
            tool,
            "run_image_ocr",
            return_value=[tool.ImageOcrResult(0, "https://example.com/1.jpg", "OCR 文本", "test")],
        ):
            with mock.patch.object(
                tool,
                "run_video_transcript",
                return_value=tool.VideoTranscriptResult("https://example.com/video.mp4", "ASR 文本", "test"),
            ):
                media = tool.extract_media_content(candidate, args)

        self.assertIn("正文", media.content_text)
        self.assertIn("OCR 文本", media.content_text)
        self.assertIn("ASR 文本", media.content_text)
        self.assertEqual(media.extraction_method, "base-note-text+image-ocr+test")

    def test_dry_run_json_has_empty_report(self) -> None:
        stdout = StringIO()

        with mock.patch("sys.stdout", stdout):
            exit_code = tool.main(
                [
                    "--candidate-url",
                    "https://www.xiaohongshu.com/explore/65f1a2b3c4d5e6f789012345",
                    "--selected-note-ids",
                    "65f1a2b3c4d5e6f789012345",
                    "--dry-run",
                    "--json",
                ]
            )

        payload = json.loads(stdout.getvalue())
        self.assertEqual(exit_code, 0)
        self.assertEqual(payload["report"], "")
        self.assertEqual(payload["decisions"][0]["status"], "selected")


if __name__ == "__main__":
    unittest.main()
