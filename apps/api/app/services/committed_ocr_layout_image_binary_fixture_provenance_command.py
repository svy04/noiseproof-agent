from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.ocr_layout_image_binary_fixture import (
    build_committed_ocr_layout_image_binary_fixture_provenance_report,
    build_committed_ocr_layout_image_binary_fixture_provenance_summary,
    load_ocr_layout_image_binary_fixture_provenance,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the committed OCR/layout/image binary fixture provenance report."
    )
    parser.add_argument("--fixture-root", required=True, help="Binary fixture root path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        fixture_root = Path(args.fixture_root)
        packet = load_ocr_layout_image_binary_fixture_provenance(fixture_root)
        summary = build_committed_ocr_layout_image_binary_fixture_provenance_summary(
            fixture_root,
            packet,
        )
        report = build_committed_ocr_layout_image_binary_fixture_provenance_report(
            summary
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("committed_ocr_layout_image_binary_fixture_provenance_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("committed_ocr_layout_image_binary_fixture_provenance_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("committed_ocr_layout_image_binary_fixture_provenance_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("committed_ocr_layout_image_binary_fixture_provenance_report_current")
        print("byte-for-byte regeneration")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print("committed_ocr_layout_image_binary_fixture_provenance_v0")
    print(summary["claim_boundary"])
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
