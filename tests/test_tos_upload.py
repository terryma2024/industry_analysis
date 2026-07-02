import datetime as real_dt
import os
import unittest
from pathlib import Path
from unittest import mock

from tools import tos_upload


class TosUploadTests(unittest.TestCase):
    def test_request_url_defaults_to_virtual_host_style(self) -> None:
        url, host, path = tos_upload.request_url(
            "https://tos-s3-cn-beijing.volces.com",
            "industry-analysis",
            "asr-audio/clip.m4a",
            "virtual",
        )

        self.assertEqual(host, "industry-analysis.tos-s3-cn-beijing.volces.com")
        self.assertEqual(path, "/asr-audio/clip.m4a")
        self.assertEqual(url, "https://industry-analysis.tos-s3-cn-beijing.volces.com/asr-audio/clip.m4a")

    def test_request_url_supports_path_style(self) -> None:
        url, host, path = tos_upload.request_url(
            "https://tos-s3-cn-beijing.volces.com",
            "industry-analysis",
            "asr-audio/clip.m4a",
            "path",
        )

        self.assertEqual(host, "tos-s3-cn-beijing.volces.com")
        self.assertEqual(path, "/industry-analysis/asr-audio/clip.m4a")
        self.assertEqual(url, "https://tos-s3-cn-beijing.volces.com/industry-analysis/asr-audio/clip.m4a")

    def test_presigned_get_url_contains_expected_s3_parameters(self) -> None:
        with mock.patch("tools.tos_upload.dt") as dt_mock:
            dt_mock.UTC = real_dt.UTC
            dt_mock.datetime.now.return_value = real_dt.datetime(2026, 7, 2, 1, 2, 3, tzinfo=real_dt.UTC)
            url = tos_upload.presigned_get_url(
                "https://tos-s3-cn-beijing.volces.com",
                "industry-analysis",
                "asr-audio/clip.m4a",
                "ak",
                "sk",
                "cn-beijing",
                "s3",
                3600,
                "virtual",
            )

        self.assertIn("X-Amz-Algorithm=AWS4-HMAC-SHA256", url)
        self.assertIn("X-Amz-Credential=ak%2F20260702%2Fcn-beijing%2Fs3%2Faws4_request", url)
        self.assertIn("X-Amz-Signature=", url)

    def test_require_env_accepts_volcengine_ak_aliases(self) -> None:
        env = {
            "VOLCENGINE_ACCESS_KEY_ID": "ak",
            "VOLCENGINE_SECRET_ACCESS_KEY": "sk",
            "TOS_BUCKET": "industry-analysis",
        }
        with mock.patch.dict(os.environ, env, clear=True):
            access_key, secret_key, bucket = tos_upload.require_env()

        self.assertEqual((access_key, secret_key, bucket), ("ak", "sk", "industry-analysis"))

    def test_require_env_rejects_identical_access_key_and_secret(self) -> None:
        env = {
            "TOS_ACCESS_KEY_ID": "same",
            "TOS_SECRET_ACCESS_KEY": "same",
            "TOS_BUCKET": "industry-analysis",
        }
        with mock.patch.dict(os.environ, env, clear=True):
            with self.assertRaises(SystemExit) as caught:
                tos_upload.require_env()

        self.assertIn("are identical", str(caught.exception))

    def test_object_key_uses_prefix_and_safe_filename(self) -> None:
        key = tos_upload.object_key(Path("音频 sample.m4a"), "asr-audio")

        self.assertTrue(key.startswith("asr-audio/"))
        self.assertTrue(key.endswith("-音频-sample.m4a"))


if __name__ == "__main__":
    unittest.main()
