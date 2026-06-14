from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.missing_runtime_pack import (
    load_missing_pdf_runtime_observation_pack,
)
from packages.ingestion.pdf_quality.multi_fixture_ocr_adapter_eval import (
    build_multi_fixture_ocr_adapter_eval_report,
    build_multi_fixture_ocr_adapter_eval_summary,
    load_owner_runtime_ocr_smoke_observation,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the multi-fixture OCR adapter eval report."
    )
    parser.add_argument("--fixture", required=True, help="Fixture directory path.")
    parser.add_argument(
        "--base-observations",
        required=True,
        help="Base PDF extraction observation JSON path.",
    )
    parser.add_argument(
        "--missing-pack",
        required=True,
        help="Missing PDF runtime observation pack JSON path.",
    )
    parser.add_argument(
        "--owner-ocr-observation",
        required=True,
        help="Sanitized owner-runtime OCR smoke observation JSON path.",
    )
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        fixture = load_pdf_extraction_quality_fixture(Path(args.fixture))
        missing_pack = load_missing_pdf_runtime_observation_pack(
            Path(args.missing_pack)
        )
        owner_ocr = load_owner_runtime_ocr_smoke_observation(
            Path(args.owner_ocr_observation)
        )
        summary = build_multi_fixture_ocr_adapter_eval_summary(
            fixture=fixture,
            base_observations_path=Path(args.base_observations),
            missing_pack=missing_pack,
            owner_ocr_observation=owner_ocr,
        )
        report = build_multi_fixture_ocr_adapter_eval_report(summary)
    except (OSError, ValueError) as exc:
        print("multi_fixture_ocr_adapter_eval_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("multi_fixture_ocr_adapter_eval_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("multi_fixture_ocr_adapter_eval_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("multi_fixture_ocr_adapter_eval_report_current")
        print("byte-for-byte regeneration")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("multi_fixture_ocr_adapter_eval_v0")
    print(summary["claim_boundary"])
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
