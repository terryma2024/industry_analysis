import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import volcengine_asr as asr


class VolcengineAsrTests(unittest.TestCase):
    def test_direct_audio_url_can_be_submitted_without_upload(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            audio_url, audio_format = asr.prepare_audio_url("https://example.com/audio.m4a")

        self.assertEqual(audio_url, "https://example.com/audio.m4a")
        self.assertEqual(audio_format, "m4a")

    def test_bilibili_url_uses_download_and_upload(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = Path(tmpdir) / "clip.m4a"
            audio_path.write_text("fake audio", encoding="utf-8")
            with mock.patch.object(asr, "download_audio", return_value=audio_path) as download:
                with mock.patch.object(asr, "upload_audio", return_value="https://cdn.example.com/clip.m4a") as upload:
                    audio_url, audio_format = asr.prepare_audio_url("https://www.bilibili.com/video/BV1BBTv6UEaf")

        self.assertEqual(audio_url, "https://cdn.example.com/clip.m4a")
        self.assertEqual(audio_format, "m4a")
        download.assert_called_once()
        upload.assert_called_once_with(audio_path)

    def test_missing_upload_command_explains_volcengine_bilibili_constraint(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = Path(tmpdir) / "clip.m4a"
            audio_path.write_text("fake audio", encoding="utf-8")
            with mock.patch.dict(os.environ, {}, clear=True):
                with self.assertRaises(SystemExit) as caught:
                    asr.upload_audio(audio_path)

        self.assertIn("VOLCENGINE_AUDIO_UPLOAD_COMMAND is required", str(caught.exception))
        self.assertIn("Bilibili signed audio URLs", str(caught.exception))

    def test_upload_command_accepts_json_url_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = Path(tmpdir) / "clip.m4a"
            audio_path.write_text("fake audio", encoding="utf-8")
            calls = []

            def fake_run(args, timeout=300):
                calls.append(args)
                return asr.subprocess.CompletedProcess(args, 0, '{"url":"https://cdn.example.com/clip.m4a"}', "")

            env = {
                "VOLCENGINE_AUDIO_UPLOAD_COMMAND": "uploader --input {input} --type {content_type}",
                "VOLCENGINE_AUDIO_UPLOAD_TIMEOUT": "123",
            }
            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(asr, "run", side_effect=fake_run):
                    public_url = asr.upload_audio(audio_path)

        self.assertEqual(public_url, "https://cdn.example.com/clip.m4a")
        self.assertEqual(calls[0][0:2], ["uploader", "--input"])
        self.assertIn(str(audio_path), calls[0])
        self.assertTrue(any(value.startswith("audio/") for value in calls[0]))

    def test_upload_command_retries_and_reports_failed_attempts(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = Path(tmpdir) / "clip.m4a"
            audio_path.write_text("fake audio", encoding="utf-8")
            calls = []

            def fake_run(args, timeout=300):
                calls.append(args)
                return asr.subprocess.CompletedProcess(args, 1, "", "TOS upload failed HTTP 403: denied")

            env = {
                "VOLCENGINE_AUDIO_UPLOAD_COMMAND": "uploader --input {input}",
                "VOLCENGINE_AUDIO_UPLOAD_RETRIES": "2",
            }
            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(asr, "run", side_effect=fake_run):
                    with mock.patch.object(asr.time, "sleep"):
                        with self.assertRaises(SystemExit) as caught:
                            asr.upload_audio(audio_path)

        self.assertEqual(len(calls), 2)
        message = str(caught.exception)
        self.assertIn("audio upload failed after 2 attempts", message)
        self.assertIn("attempt 1", message)
        self.assertIn("TOS upload failed HTTP 403", message)

    def test_upload_command_retries_when_uploaded_url_is_not_reachable(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            audio_path = Path(tmpdir) / "clip.m4a"
            audio_path.write_text("fake audio", encoding="utf-8")
            verify_results = [False, True]

            def fake_run(args, timeout=300):
                return asr.subprocess.CompletedProcess(
                    args,
                    0,
                    '{"url":"https://industry-analysis.tos-cn-beijing.volces.com/asr-audio/clip.m4a"}',
                    "",
                )

            def fake_verify(url):
                return verify_results.pop(0), "HTTP 404"

            env = {
                "VOLCENGINE_AUDIO_UPLOAD_COMMAND": "uploader --input {input}",
                "VOLCENGINE_AUDIO_UPLOAD_RETRIES": "2",
            }
            with mock.patch.dict(os.environ, env, clear=True):
                with mock.patch.object(asr, "run", side_effect=fake_run) as run:
                    with mock.patch.object(asr, "verify_public_audio_url", side_effect=fake_verify):
                        with mock.patch.object(asr.time, "sleep"):
                            public_url = asr.upload_audio(audio_path)

        self.assertEqual(public_url, "https://industry-analysis.tos-cn-beijing.volces.com/asr-audio/clip.m4a")
        self.assertEqual(run.call_count, 2)

    def test_extract_url_from_upload_output_accepts_plain_text(self) -> None:
        public_url = asr.extract_url_from_upload_output("uploaded: https://cdn.example.com/a.wav\n")

        self.assertEqual(public_url, "https://cdn.example.com/a.wav")

    def test_extract_bvid_from_bilibili_url(self) -> None:
        bvid = asr.extract_bvid(
            "https://www.bilibili.com/video/BV1BBTv6UEaf/?spm_id_from=333.1387.favlist.content.click"
        )

        self.assertEqual(bvid, "BV1BBTv6UEaf")

    def test_select_bilibili_audio_picks_highest_bandwidth(self) -> None:
        payload = {
            "data": {
                "dash": {
                    "audio": [
                        {"bandwidth": 64000, "baseUrl": "https://example.com/low.m4s"},
                        {"bandwidth": 192000, "base_url": "https://example.com/high.m4s"},
                    ]
                }
            }
        }

        self.assertEqual(asr.select_bilibili_audio(payload), "https://example.com/high.m4s")


if __name__ == "__main__":
    unittest.main()
