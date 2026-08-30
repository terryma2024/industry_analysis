import json
import os
import time
import tempfile
import unittest
from io import StringIO
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

    def test_duplicate_detection_ignores_failed_mentions_in_log(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            (repo / "knowledge").mkdir()
            (repo / "raw").mkdir()
            (repo / "knowledge" / "log.md").write_text(
                "- BV1retry12345 failed before transcript/source card; retry later.\n",
                encoding="utf-8",
            )
            candidate = tool.VideoCandidate(
                title="机器人失败重试视频",
                url="https://www.bilibili.com/video/BV1retry12345",
                bvid="BV1retry12345",
            )

            hits = tool.find_duplicate_hits(repo, candidate)
            decision = tool.decide_candidate(repo, candidate, selected_ids={"BV1retry12345"})

        self.assertEqual(hits, [])
        self.assertEqual(decision.status, "selected")

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

    def test_parse_opencli_json_ignores_node_warning_before_payload(self) -> None:
        payload = tool.parse_opencli_json(
            "(node:45130) [UNDICI-EHPA] Warning: EnvHttpProxyAgent is experimental\n"
            '[{"title":"机器人视频","url":"https://www.bilibili.com/video/BV1warning"}]\n'
        )

        self.assertEqual(payload, [{"title": "机器人视频", "url": "https://www.bilibili.com/video/BV1warning"}])

    def test_opencli_discovery_only_invokes_favorite_command(self) -> None:
        """A non-favorite Bilibili command must never be used as a candidate source."""
        registry = json.dumps(
            [
                {
                    "site": "bilibili",
                    "name": "favorite",
                    "description": "我的收藏夹视频",
                },
                {
                    "site": "bilibili",
                    "name": "comments",
                    "description": "收藏视频的评论",
                },
            ]
        )
        calls: list[list[str]] = []

        def fake_run_command(args, cwd=tool.REPO_ROOT, timeout=180):
            calls.append(args)
            if args[:3] == ["opencli", "list", "-f"]:
                return tool.subprocess.CompletedProcess(args, 0, registry, "")
            if args[-1] == "--help":
                return tool.subprocess.CompletedProcess(args, 0, "--limit", "")
            return tool.subprocess.CompletedProcess(args, 0, "[]", "")

        with mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch.object(tool.shutil, "which", return_value="opencli"):
                with mock.patch.object(tool, "run_command", side_effect=fake_run_command):
                    candidates, errors = tool.fetch_candidates_with_opencli(limit=20)

        self.assertIn(["opencli", "bilibili", "favorite", "-f", "json", "--limit", "20"], calls)
        adapter_calls = [call for call in calls if call[:2] == ["opencli", "bilibili"] and call[-1] != "--help"]
        self.assertEqual(candidates, [])
        self.assertEqual(adapter_calls, [["opencli", "bilibili", "favorite", "-f", "json", "--limit", "20"]])
        self.assertIn("bilibili favorite returned no video-like items", errors)

    def test_opencli_favorite_retries_transient_navigation_failure(self) -> None:
        """A one-off Browser Bridge rejection must not erase the daily candidate pool."""
        registry = json.dumps(
            [{"site": "bilibili", "name": "favorite", "description": "我的收藏夹视频"}]
        )
        favorite_attempts = 0

        def fake_run_command(args, cwd=tool.REPO_ROOT, timeout=180):
            nonlocal favorite_attempts
            if args[:3] == ["opencli", "list", "-f"]:
                return tool.subprocess.CompletedProcess(args, 0, registry, "")
            if args[-1] == "--help":
                return tool.subprocess.CompletedProcess(args, 0, "--limit", "")
            favorite_attempts += 1
            if favorite_attempts == 1:
                return tool.subprocess.CompletedProcess(args, 1, "", "Navigation rejected")
            payload = json.dumps(
                [{"title": "机器人视频", "url": "https://www.bilibili.com/video/BV1retry123"}]
            )
            return tool.subprocess.CompletedProcess(args, 0, payload, "")

        with mock.patch.dict(os.environ, {}, clear=True):
            with mock.patch.object(tool.shutil, "which", return_value="opencli"):
                with mock.patch.object(tool, "run_command", side_effect=fake_run_command):
                    candidates, errors = tool.fetch_candidates_with_opencli(limit=20)

        self.assertEqual(favorite_attempts, 2)
        self.assertEqual([candidate.bvid for candidate in candidates], ["BV1retry123"])
        self.assertEqual(errors, [])

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

    def test_run_command_timeout_kills_child_process_group_quickly(self) -> None:
        script = (
            "import subprocess, sys, time; "
            "subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(3)']); "
            "time.sleep(3)"
        )
        start = time.monotonic()

        proc = tool.run_command([tool.sys.executable, "-c", script], timeout=1)
        elapsed = time.monotonic() - start

        self.assertEqual(proc.returncode, 124)
        self.assertLess(elapsed, 2.5)
        self.assertIn("command timed out after 1 seconds", proc.stderr)

    def test_tos_audio_status_is_included_in_run_report(self) -> None:
        candidate = tool.VideoCandidate(
            title="机器人视频",
            url="https://www.bilibili.com/video/BV1toscheck",
            bvid="BV1toscheck",
        )
        decisions = [
            tool.CandidateDecision(
                candidate=candidate,
                status="needs_model_review",
                reason="awaiting model relevance judgment",
            )
        ]
        tos_status = {
            "enabled": True,
            "prefix": "asr-audio/2026/07/08",
            "count": 0,
            "keys": [],
            "error": "",
        }

        with tempfile.TemporaryDirectory() as tmpdir:
            old_dir = tool.SYNTHESIS_DIR
            tool.SYNTHESIS_DIR = Path(tmpdir)
            try:
                report_path = tool.write_run_report(decisions, [], [], tos_status=tos_status)
                text = report_path.read_text(encoding="utf-8")
            finally:
                tool.SYNTHESIS_DIR = old_dir

        self.assertIn("## TOS Audio Check", text)
        self.assertIn("asr-audio/2026/07/08", text)
        self.assertIn("Objects found: 0", text)

    def test_append_log_uses_one_date_only_heading(self) -> None:
        candidate = tool.VideoCandidate(
            title="AI video",
            url="https://www.bilibili.com/video/BV1logcheck",
            bvid="BV1logcheck",
        )
        decision = tool.CandidateDecision(candidate=candidate, status="selected", reason="selected")
        result = tool.ProcessResult(decision=decision, status="processed", reason="captured")

        with tempfile.TemporaryDirectory() as tmpdir:
            old_log = tool.KNOWLEDGE_LOG
            tool.KNOWLEDGE_LOG = Path(tmpdir) / "log.md"
            tool.KNOWLEDGE_LOG.write_text("# Wiki Log\n", encoding="utf-8")
            try:
                with mock.patch.object(tool, "today_str", return_value="2026-07-16"):
                    tool.append_log(Path("bilibili-ai-daily-run-2026-07-16.md"), [result])
                    tool.append_log(Path("bilibili-ai-daily-run-2026-07-16.md"), [result])
                text = tool.KNOWLEDGE_LOG.read_text(encoding="utf-8")
            finally:
                tool.KNOWLEDGE_LOG = old_log

        self.assertEqual(text.count("## [2026-07-16]"), 1)
        self.assertIn("**ingest | Bilibili AI/具身智能每日视频采集**", text)

    def test_tos_audio_status_uses_tos_sdk_runner_for_list_check(self) -> None:
        env = {
            "TOS_ACCESS_KEY_ID": "ak",
            "TOS_SECRET_ACCESS_KEY": "sk",
        }
        completed = tool.subprocess.CompletedProcess(
            args=[],
            returncode=0,
            stdout=json.dumps(
                {
                    "count": 1,
                    "objects": [{"key": "asr-audio/2026/07/08/a.m4a"}],
                }
            ),
            stderr="",
        )

        with mock.patch.dict(os.environ, env, clear=True):
            with mock.patch.object(tool, "run_command", return_value=completed) as run_command:
                status = tool.check_tos_audio_status()

        args = run_command.call_args.args[0]
        self.assertEqual(args[:4], ["uv", "run", "--with", "tos"])
        self.assertIn("--list-prefix", args)
        self.assertEqual(status["count"], 1)
        self.assertEqual(status["keys"], ["asr-audio/2026/07/08/a.m4a"])

    def test_dry_run_json_has_empty_report_without_relative_path_error(self) -> None:
        candidate = tool.VideoCandidate(
            title="机器人视频",
            url="https://www.bilibili.com/video/BV1dryrun",
            bvid="BV1dryrun",
        )
        stdout = StringIO()

        with mock.patch.object(tool, "fetch_bilibili_candidate", return_value=(candidate, "")):
            with mock.patch.object(tool, "check_tos_audio_status", return_value={"enabled": False}):
                with mock.patch("sys.stdout", stdout):
                    exit_code = tool.main(
                        [
                            "--candidate-url",
                            "https://www.bilibili.com/video/BV1dryrun",
                            "--selected-video-ids",
                            "BV1dryrun",
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
