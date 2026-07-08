#!/usr/bin/env python3
"""Upload a local file to Volcengine TOS through the S3-compatible API.

The command prints a presigned GET URL by default, which is suitable for
Volcengine AUC ASR because the ASR service downloads audio server-side.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import hmac
import json
import mimetypes
import os
import sys
import xml.etree.ElementTree as ET
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOTENV_PATHS = (Path.home() / ".env", REPO_ROOT / ".env")
DEFAULT_REGION = "cn-beijing"
DEFAULT_ENDPOINT = "https://tos-cn-beijing.volces.com"
DEFAULT_PUBLIC_BASE_URL = "https://industry-analysis.tos-cn-beijing.volces.com"


def load_dotenv() -> None:
    for path in DOTENV_PATHS:
        if not path.exists():
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if key and key not in os.environ:
                os.environ[key] = value


def env_first(*names: str) -> str:
    for name in names:
        value = os.environ.get(name, "").strip()
        if value:
            return value
    return ""


def require_env() -> tuple[str, str, str]:
    access_key = env_first("TOS_ACCESS_KEY_ID", "VOLCENGINE_ACCESS_KEY_ID")
    secret_key = env_first("TOS_SECRET_ACCESS_KEY", "VOLCENGINE_SECRET_ACCESS_KEY")
    bucket = env_first("TOS_BUCKET", "VOLCENGINE_TOS_BUCKET") or "industry-analysis"
    missing = []
    if not access_key:
        missing.append("TOS_ACCESS_KEY_ID or VOLCENGINE_ACCESS_KEY_ID")
    if not secret_key:
        missing.append("TOS_SECRET_ACCESS_KEY or VOLCENGINE_SECRET_ACCESS_KEY")
    if not bucket:
        missing.append("TOS_BUCKET")
    if missing:
        raise SystemExit("missing required env vars: " + ", ".join(missing))
    if access_key == secret_key:
        raise SystemExit(
            "TOS_ACCESS_KEY_ID and TOS_SECRET_ACCESS_KEY are identical. "
            "Use the AccessKeyId for TOS_ACCESS_KEY_ID and the separate SecretAccessKey for TOS_SECRET_ACCESS_KEY."
        )
    return access_key, secret_key, bucket


def hmac_sha256(key: bytes, message: str) -> bytes:
    return hmac.new(key, message.encode("utf-8"), hashlib.sha256).digest()


def signing_key(secret_key: str, datestamp: str, region: str, service: str) -> bytes:
    date_key = hmac_sha256(("AWS4" + secret_key).encode("utf-8"), datestamp)
    region_key = hmac_sha256(date_key, region)
    service_key = hmac_sha256(region_key, service)
    return hmac_sha256(service_key, "aws4_request")


def normalize_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip().rstrip("/")
    if not endpoint.startswith(("http://", "https://")):
        endpoint = "https://" + endpoint
    return endpoint


def object_key(path: Path, prefix: str) -> str:
    safe_name = "".join(char if char.isalnum() or char in "._-" else "-" for char in path.name)
    now = dt.datetime.now(dt.UTC)
    prefix = prefix.strip("/")
    dated = now.strftime("%Y/%m/%d")
    key = f"{prefix}/{dated}/{now.strftime('%H%M%S')}-{safe_name}" if prefix else f"{dated}/{now.strftime('%H%M%S')}-{safe_name}"
    return key


def content_type_for(path: Path, override: str = "") -> str:
    if override:
        return override
    return mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def quote_path(path: str) -> str:
    return urllib.parse.quote(path, safe="/-_.~")


def canonical_query(params: dict[str, str]) -> str:
    pairs = []
    for key in sorted(params):
        pairs.append(f"{urllib.parse.quote(key, safe='-_.~')}={urllib.parse.quote(params[key], safe='-_.~')}")
    return "&".join(pairs)


def request_url(endpoint: str, bucket: str, key: str, addressing_style: str) -> tuple[str, str, str]:
    parsed = urllib.parse.urlparse(normalize_endpoint(endpoint))
    if addressing_style == "path":
        host = parsed.netloc
        path = f"/{bucket}/{quote_path(key)}"
    else:
        host = f"{bucket}.{parsed.netloc}"
        path = f"/{quote_path(key)}"
    return f"{parsed.scheme}://{host}{path}", host, path


def sign_headers(
    method: str,
    path: str,
    query: str,
    host: str,
    payload_hash: str,
    access_key: str,
    secret_key: str,
    region: str,
    service: str,
    content_type: str = "",
    security_token: str = "",
) -> dict[str, str]:
    now = dt.datetime.now(dt.UTC)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    datestamp = now.strftime("%Y%m%d")
    headers = {
        "content-type": content_type,
        "host": host,
        "x-amz-content-sha256": payload_hash,
        "x-amz-date": amz_date,
    }
    if not content_type:
        headers.pop("content-type")
    if security_token:
        headers["x-amz-security-token"] = security_token
    signed_headers = ";".join(sorted(headers))
    canonical_headers = "".join(f"{key}:{headers[key]}\n" for key in sorted(headers))
    canonical_request = "\n".join([method, path, query, canonical_headers, signed_headers, payload_hash])
    credential_scope = f"{datestamp}/{region}/{service}/aws4_request"
    string_to_sign = "\n".join(
        [
            "AWS4-HMAC-SHA256",
            amz_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
        ]
    )
    signature = hmac.new(
        signing_key(secret_key, datestamp, region, service),
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    headers["authorization"] = (
        f"AWS4-HMAC-SHA256 Credential={access_key}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )
    return {key.title(): value for key, value in headers.items()}


def sign_put_headers(
    method: str,
    path: str,
    host: str,
    payload_hash: str,
    content_type: str,
    access_key: str,
    secret_key: str,
    region: str,
    service: str,
    security_token: str = "",
) -> dict[str, str]:
    return sign_headers(
        method,
        path,
        "",
        host,
        payload_hash,
        access_key,
        secret_key,
        region,
        service,
        content_type,
        security_token,
    )


def presigned_get_url(
    endpoint: str,
    bucket: str,
    key: str,
    access_key: str,
    secret_key: str,
    region: str,
    service: str,
    expires: int,
    addressing_style: str,
    security_token: str = "",
) -> str:
    base_url, host, path = request_url(endpoint, bucket, key, addressing_style)
    now = dt.datetime.now(dt.UTC)
    amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    datestamp = now.strftime("%Y%m%d")
    credential_scope = f"{datestamp}/{region}/{service}/aws4_request"
    params = {
        "X-Amz-Algorithm": "AWS4-HMAC-SHA256",
        "X-Amz-Credential": f"{access_key}/{credential_scope}",
        "X-Amz-Date": amz_date,
        "X-Amz-Expires": str(expires),
        "X-Amz-SignedHeaders": "host",
    }
    if security_token:
        params["X-Amz-Security-Token"] = security_token
    query = canonical_query(params)
    canonical_headers = f"host:{host}\n"
    canonical_request = "\n".join(["GET", path, query, canonical_headers, "host", "UNSIGNED-PAYLOAD"])
    string_to_sign = "\n".join(
        [
            "AWS4-HMAC-SHA256",
            amz_date,
            credential_scope,
            hashlib.sha256(canonical_request.encode("utf-8")).hexdigest(),
        ]
    )
    signature = hmac.new(
        signing_key(secret_key, datestamp, region, service),
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return f"{base_url}?{query}&X-Amz-Signature={signature}"


def public_object_url(public_base_url: str, key: str) -> str:
    return normalize_endpoint(public_base_url) + "/" + quote_path(key)


def upload_file(
    path: Path,
    key: str,
    content_type: str,
    access_key: str,
    secret_key: str,
    bucket: str,
    region: str,
    service: str,
    endpoint: str,
    addressing_style: str,
    security_token: str = "",
) -> None:
    body = path.read_bytes()
    payload_hash = hashlib.sha256(body).hexdigest()
    url, host, request_path = request_url(endpoint, bucket, key, addressing_style)
    headers = sign_put_headers(
        "PUT",
        request_path,
        host,
        payload_hash,
        content_type,
        access_key,
        secret_key,
        region,
        service,
        security_token,
    )
    request = urllib.request.Request(url, data=body, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(request, timeout=300) as response:
            response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"TOS upload failed HTTP {exc.code}: {detail}") from exc


def parse_list_objects_xml(text: str) -> list[dict[str, object]]:
    root = ET.fromstring(text)
    objects: list[dict[str, object]] = []
    for contents in root.findall(".//{*}Contents"):
        key = contents.findtext("{*}Key") or ""
        size_text = contents.findtext("{*}Size") or "0"
        last_modified = contents.findtext("{*}LastModified") or ""
        if not key:
            continue
        try:
            size = int(size_text)
        except ValueError:
            size = 0
        objects.append({"key": key, "size": size, "last_modified": last_modified})
    return objects


def list_objects(
    prefix: str,
    access_key: str,
    secret_key: str,
    bucket: str,
    region: str,
    service: str,
    endpoint: str,
    addressing_style: str,
    max_keys: int = 100,
    security_token: str = "",
) -> list[dict[str, object]]:
    base_url, host, request_path = request_url(endpoint, bucket, "", addressing_style)
    payload_hash = hashlib.sha256(b"").hexdigest()
    query = canonical_query({"list-type": "2", "max-keys": str(max_keys), "prefix": prefix})
    headers = sign_headers(
        "GET",
        request_path,
        query,
        host,
        payload_hash,
        access_key,
        secret_key,
        region,
        service,
        security_token=security_token,
    )
    request = urllib.request.Request(f"{base_url}?{query}", headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"TOS list failed HTTP {exc.code}: {detail}") from exc
    return parse_list_objects_xml(body)


def sdk_client(access_key: str, secret_key: str, endpoint: str, region: str, security_token: str = ""):
    try:
        import tos
    except ImportError:
        return None
    return tos.TosClientV2(
        ak=access_key,
        sk=secret_key,
        endpoint=normalize_endpoint(endpoint),
        region=region,
        security_token=security_token or None,
    )


def sdk_upload_file(client, bucket: str, key: str, path: Path, content_type: str) -> None:
    client.put_object_from_file(
        bucket=bucket,
        key=key,
        file_path=str(path),
        content_type=content_type,
    )


def sdk_presigned_get_url(client, bucket: str, key: str, expires: int) -> str:
    try:
        import tos
    except ImportError as exc:
        raise RuntimeError("tos SDK disappeared after client creation") from exc
    return client.pre_signed_url(
        tos.HttpMethodType.Http_Method_Get,
        bucket,
        key,
        expires=expires,
    ).signed_url


def sdk_list_objects(client, bucket: str, prefix: str, max_keys: int) -> list[dict[str, object]]:
    output = client.list_objects_type2(bucket=bucket, prefix=prefix, max_keys=max_keys)
    objects: list[dict[str, object]] = []
    for item in getattr(output, "contents", []) or []:
        last_modified = getattr(item, "last_modified", "") or ""
        if hasattr(last_modified, "isoformat"):
            last_modified = last_modified.isoformat()
        objects.append(
            {
                "key": getattr(item, "key", "") or "",
                "size": int(getattr(item, "size", 0) or 0),
                "last_modified": str(last_modified),
            }
        )
    return [item for item in objects if item["key"]]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="local audio file")
    parser.add_argument("--filename", help="optional original filename from caller")
    parser.add_argument("--content-type", default="", help="MIME type override")
    parser.add_argument("--key", help="TOS object key; generated when omitted")
    parser.add_argument("--prefix", default=os.environ.get("TOS_UPLOAD_PREFIX", "asr-audio"))
    parser.add_argument("--expires", type=int, default=int(os.environ.get("TOS_PRESIGN_EXPIRES", "86400")))
    parser.add_argument("--public-url", action="store_true", help="print bucket-domain URL instead of a presigned URL")
    parser.add_argument("--json", action="store_true", help="print structured JSON output")
    parser.add_argument("--list-prefix", help="list objects under this TOS prefix instead of uploading")
    parser.add_argument("--list-max-keys", type=int, default=100, help="maximum keys to return for --list-prefix")
    return parser


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    args = build_parser().parse_args(argv)
    access_key, secret_key, bucket = require_env()
    region = os.environ.get("TOS_REGION", DEFAULT_REGION).strip() or DEFAULT_REGION
    endpoint = os.environ.get("TOS_ENDPOINT", DEFAULT_ENDPOINT).strip() or DEFAULT_ENDPOINT
    public_base_url = os.environ.get("TOS_PUBLIC_BASE_URL", DEFAULT_PUBLIC_BASE_URL).strip() or DEFAULT_PUBLIC_BASE_URL
    addressing_style = os.environ.get("TOS_ADDRESSING_STYLE", "virtual").strip() or "virtual"
    service = os.environ.get("TOS_SIGNING_SERVICE", "s3").strip() or "s3"
    security_token = env_first("TOS_SECURITY_TOKEN", "VOLCENGINE_SECURITY_TOKEN")
    client = sdk_client(access_key, secret_key, endpoint, region, security_token)

    if args.list_prefix:
        if client is not None:
            objects = sdk_list_objects(client, bucket, args.list_prefix, args.list_max_keys)
        else:
            objects = list_objects(
                args.list_prefix,
                access_key,
                secret_key,
                bucket,
                region,
                service,
                endpoint,
                addressing_style,
                args.list_max_keys,
                security_token,
            )
        payload = {"bucket": bucket, "prefix": args.list_prefix, "count": len(objects), "objects": objects}
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            for item in objects:
                print(item["key"])
        return 0

    if args.input is None:
        raise SystemExit("--input is required unless --list-prefix is used")
    input_path = args.input.expanduser().resolve()
    if not input_path.exists() or not input_path.is_file():
        raise SystemExit(f"input file does not exist: {input_path}")
    filename = args.filename or input_path.name
    key = args.key or object_key(Path(filename), args.prefix)
    content_type = content_type_for(input_path, args.content_type)

    if client is not None:
        sdk_upload_file(client, bucket, key, input_path, content_type)
    else:
        upload_file(
            input_path,
            key,
            content_type,
            access_key,
            secret_key,
            bucket,
            region,
            service,
            endpoint,
            addressing_style,
            security_token,
        )
    if args.public_url:
        url = public_object_url(public_base_url, key)
    else:
        if client is not None:
            url = sdk_presigned_get_url(client, bucket, key, args.expires)
        else:
            url = presigned_get_url(
                endpoint,
                bucket,
                key,
                access_key,
                secret_key,
                region,
                service,
                args.expires,
                addressing_style,
                security_token,
            )
    if args.json:
        print(json.dumps({"bucket": bucket, "key": key, "url": url}, ensure_ascii=False))
    else:
        print(url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
