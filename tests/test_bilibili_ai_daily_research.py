import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import bilibili_ai_daily_research as tool


class BilibiliAiDailyResearchTests(unittest.TestCase):
    def test_normalize_candidate_extracts_bvid_from_url(self) -> None:
        candidate = tool.normalize_candidate(
            {
                "title": "A robot world model demo",
                "url": "https://www.bilibili.com/video/BV1abc123xyz/",
                "owner": {"name": "Tester"},
                "tags": [{"name": "robotics"}, {"name": "AI"}],
            }
        )

        self.assertEqual(candidate.bvid, "BV1abc123xyz")
        self.assertEqual(candidate.author, "Tester")
        self.assertIn("robotics", candidate.tags)

    def test_extract_bvid_from_url(self) -> None:
        bvid = tool.extract_bvid(
            "https://www.bilibili.com/video/BV1BBTv6UEaf/?spm_id_from=333.1387.favlist.content.click"
        )

        self.assertEqual(bvid, "BV1BBTv6UEaf")

    def test_relevance_selects_embodied_ai_video(self) -> None:
        candidate = tool.VideoCandidate(
            title="具身智能机器人 VLA 世界模型最新进展",
            url="https://www.bilibili.com/video/BV1robotai",
            description="Unitree, LeRobot, Isaac GR00T and robot training data.",
        )

        score, terms, industries = tool.relevance(candidate)

        self.assertGreaterEqual(score, 2)
        self.assertIn("robotics-embodied-ai", industries)
        self.assertTrue(terms)

    def test_relevance_marks_unrelated_video_low_score(self) -> None:
        candidate = tool.VideoCandidate(
            title="周末旅行美食记录",
            url="https://www.bilibili.com/video/BV1travel",
            description="城市散步与咖啡馆。",
        )

        score, terms, industries = tool.relevance(candidate)

        self.assertEqual(score, 0)
        self.assertEqual(terms, [])
        self.assertEqual(industries, ["ai"])

    def test_relevance_selects_codex_tooling_video(self) -> None:
        candidate = tool.VideoCandidate(
            title="安了这5个skill，让Codex自动控制matlab",
            url="https://www.bilibili.com/video/BV1BBTv6UEaf",
        )

        score, terms, industries = tool.relevance(candidate)

        self.assertGreaterEqual(score, 2)
        self.assertIn("ai", industries)
        self.assertTrue(any("codex" in term.lower() for term in terms))

    def test_non_duplicate_requires_model_review_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            candidate = tool.VideoCandidate(
                title="具身智能机器人 VLA 世界模型最新进展",
                url="https://www.bilibili.com/video/BV1robotai",
                bvid="BV1robotai",
            )

            decision = tool.decide_candidate(repo, candidate)

        self.assertEqual(decision.status, "needs_model_review")

    def test_selected_video_id_is_processed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            candidate = tool.VideoCandidate(
                title="安了这5个skill，让Codex自动控制matlab",
                url="https://www.bilibili.com/video/BV1BBTv6UEaf",
                bvid="BV1BBTv6UEaf",
            )

            decision = tool.decide_candidate(repo, candidate, selected_ids={"BV1BBTv6UEaf"})

        self.assertEqual(decision.status, "selected")
        self.assertEqual(decision.reason, "selected by model relevance judgment")

    def test_duplicate_detection_finds_existing_bvid(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            (repo / "knowledge" / "note.md").write_text(
                "Already processed https://www.bilibili.com/video/BV1dup12345",
                encoding="utf-8",
            )
            candidate = tool.VideoCandidate(
                title="机器人视频",
                url="https://www.bilibili.com/video/BV1dup12345",
                bvid="BV1dup12345",
            )

            hits = tool.find_duplicate_hits(repo, candidate)

        self.assertTrue(hits)

    def test_load_candidates_from_nested_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "candidates.json"
            path.write_text(
                json.dumps(
                    {
                        "data": {
                            "medias": [
                                {
                                    "title": "AI Agent demo",
                                    "bvid": "BV1agent123",
                                    "upper": {"name": "UP"},
                                }
                            ]
                        }
                    }
                ),
                encoding="utf-8",
            )

            candidates = tool.load_candidates_from_json(path, limit=20)

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].bvid, "BV1agent123")
        self.assertEqual(candidates[0].author, "UP")

    def test_external_asr_falls_back_to_big_model(self) -> None:
        candidate = tool.VideoCandidate(
            title="机器人视频",
            url="https://www.bilibili.com/video/BV1asr123",
            bvid="BV1asr123",
        )
        calls = []

        def fake_run_command(args, cwd=tool.REPO_ROOT, timeout=180):
            calls.append(args)
            if "volc.seedasr.auc" in args:
                return tool.subprocess.CompletedProcess(args, 1, "", "seed failed")
            return tool.subprocess.CompletedProcess(args, 0, "fallback transcript", "")

        env = {
            **os.environ,
            "VOLCENGINE_ASR_COMMAND": "asr --url {url} --model {model} --output {output}",
            "VOLCENGINE_ASR_MODEL_PRIMARY": "volc.seedasr.auc",
            "VOLCENGINE_ASR_MODEL_FALLBACK": "volc.bigasr.auc",
        }
        with mock.patch.dict(os.environ, env, clear=True):
            with mock.patch.object(tool, "run_command", side_effect=fake_run_command):
                text, method, error = tool.run_external_asr(candidate, timeout=10)

        self.assertEqual(text, "fallback transcript")
        self.assertEqual(method, "volcengine-external-command:volc.bigasr.auc")
        self.assertEqual(error, "")
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
