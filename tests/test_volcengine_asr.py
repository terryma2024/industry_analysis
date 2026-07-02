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
