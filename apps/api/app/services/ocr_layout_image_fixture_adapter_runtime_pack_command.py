from __future__ import annotations

import argparse
import contextlib
import io
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.ocr_layout_image_pack import (
    build_ocr_layout_image_adapter_runtime_pack,
    build_ocr_layout_image_adapter_runtime_pack_report,
    build_ocr_layout_image_adapter_runtime_pack_summary,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the OCR/layout/image adapter runtime pack report."
    )
    parser.add_argument("--fixture", required=True, help="Fixture directory path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        fixture = load_pdf_extraction_quality_fixture(Path(args.fixture))
        with contextlib.redirect_stdout(io.StringIO()):
            pack = build_ocr_layout_image_adapter_runtime_pack()
        summary = build_ocr_layout_image_adapter_runtime_pack_summary(fixture, pack)
        report = build_ocr_layout_image_adapter_runtime_pack_report(summary)
    except (OSError, ValueError) as exc:
        print("ocr_layout_image_fixture_adapter_runtime_pack_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("ocr_layout_image_fixture_adapter_runtime_pack_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("ocr_layout_image_fixture_adapter_runtime_pack_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("ocr_layout_image_fixture_adapter_runtime_pack_report_current")
        print("byte-for-byte regeneration")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("ocr_layout_image_fixture_adapter_runtime_pack_v0")
    print(summary["claim_boundary"])
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
