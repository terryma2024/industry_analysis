import datetime as real_dt
import json
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

    def test_parse_list_objects_xml_returns_key_metadata(self) -> None:
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
          <Contents>
            <Key>asr-audio/2026/07/08/010203-a.m4a</Key>
            <LastModified>2026-07-08T01:02:03.000Z</LastModified>
            <Size>123</Size>
          </Contents>
        </ListBucketResult>
        """

        objects = tos_upload.parse_list_objects_xml(xml)

        self.assertEqual(objects[0]["key"], "asr-audio/2026/07/08/010203-a.m4a")
        self.assertEqual(objects[0]["size"], 123)

    def test_main_list_prefix_prints_json_without_input_file(self) -> None:
        env = {
            "TOS_ACCESS_KEY_ID": "ak",
            "TOS_SECRET_ACCESS_KEY": "sk",
            "TOS_BUCKET": "industry-analysis",
        }
        with mock.patch.dict(os.environ, env, clear=True):
            with mock.patch.object(
                tos_upload,
                "list_objects",
                return_value=[{"key": "asr-audio/2026/07/08/a.m4a", "size": 123, "last_modified": ""}],
            ):
                with mock.patch("builtins.print") as printed:
                    code = tos_upload.main(["--list-prefix", "asr-audio/2026/07/08", "--json"])

        self.assertEqual(code, 0)
        payload = json.loads(printed.call_args.args[0])
        self.assertEqual(payload["count"], 1)
        self.assertEqual(payload["prefix"], "asr-audio/2026/07/08")


if __name__ == "__main__":
    unittest.main()
