import csv
import tempfile
import unittest
from pathlib import Path

from tools import extract_pdf_sources as tool


class ExtractPdfSourcesTests(unittest.TestCase):
    def test_build_key_info_draft_preserves_page_traceability(self) -> None:
        row = {
            "id": "SRC-robotics-999",
            "title": "Robot Market Report",
            "source_type": "report",
            "publisher": "Test Publisher",
            "date": "2026-05-01",
            "url_or_path": "https://example.com/report.pdf",
            "evidence_grade": "A",
        }
        pages = [
            tool.PageText(page=1, text="# Executive Summary\nThe market reached RMB 10bn.\n\n| Company | Share |\n| A | 10% |"),
            tool.PageText(page=2, text="Policy support expanded.\nRisk: adoption is slower than expected."),
        ]

        draft = tool.build_key_info_draft(row, pages, source_markdown_path=Path("raw/robotics/documents/report.md"))

        self.assertIn("source_id: \"SRC-robotics-999\"", draft)
        self.assertIn("# Robot Market Report - Key Information Draft", draft)
        self.assertIn("## Page-Level Leads", draft)
        self.assertIn("[p. 1]", draft)
        self.assertIn("The market reached RMB 10bn.", draft)
        self.assertIn("## Extracted Tables", draft)
        self.assertIn("| A | 10% |", draft)
        self.assertIn("## Analyst Checklist", draft)

    def test_write_manifest_merges_rows_by_source_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            manifest_path = Path(tmpdir) / "source_capture_manifest.csv"
            manifest_path.write_text(
                "source_id,title,url,method,status,raw_path,captured_at,error\n"
                "SRC-old,Old,u,pdf-extract,ok,old.md,2026-01-01T00:00:00+00:00,\n"
                "SRC-same,Before,u,pdf-extract,failed,before.md,2026-01-01T00:00:00+00:00,error\n",
                encoding="utf-8",
            )
            new_rows = [
                {
                    "source_id": "SRC-same",
                    "title": "After",
                    "url": "u2",
                    "method": "pdf-extract-docling",
                    "status": "ok",
                    "raw_path": "after.md",
                    "captured_at": "2026-05-27T00:00:00+00:00",
                    "error": "",
                }
            ]

            merged = tool.merge_manifest(manifest_path, new_rows)

            self.assertEqual([row["source_id"] for row in merged], ["SRC-old", "SRC-same"])
            self.assertEqual(merged[1]["title"], "After")
            self.assertEqual(merged[1]["status"], "ok")

    def test_select_pdf_sources_accepts_http_and_local_paths(self) -> None:
        rows = [
            {"id": "SRC-1", "url_or_path": "https://example.com/a.pdf"},
            {"id": "SRC-2", "url_or_path": "raw/robotics/documents/local.PDF"},
            {"id": "SRC-3", "url_or_path": "https://example.com/page.html"},
        ]

        selected = tool.select_pdf_rows(rows, selected_ids=set())

        self.assertEqual([row["id"] for row in selected], ["SRC-1", "SRC-2"])


if __name__ == "__main__":
    unittest.main()
