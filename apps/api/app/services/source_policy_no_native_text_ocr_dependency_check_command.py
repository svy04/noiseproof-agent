from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_dependency_check import (  # noqa: E402
    build_source_policy_no_native_text_ocr_dependency_check_report,
    build_source_policy_no_native_text_ocr_dependency_check_summary,
    load_source_policy_no_native_text_ocr_dependency_check,
    probe_tesseract_dependency,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the source-policy no-native-text OCR dependency check report."
    )
    parser.add_argument("--check-packet", help="OCR dependency check JSON packet path.")
    parser.add_argument("--output", help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    parser.add_argument(
        "--probe-runtime",
        action="store_true",
        help="Print a sanitized runtime dependency probe without OCR execution.",
    )
    args = parser.parse_args(argv)

    if args.probe_runtime:
        print(json.dumps(probe_tesseract_dependency(), indent=2, sort_keys=True))
        return 0

    if not args.check_packet or not args.output:
        print("source_policy_no_native_text_ocr_dependency_check_report_failed", file=sys.stderr)
        print("expected --check-packet <path> --output <path>", file=sys.stderr)
        return 2

    try:
        packet = load_source_policy_no_native_text_ocr_dependency_check(
            Path(args.check_packet)
        )
        summary = build_source_policy_no_native_text_ocr_dependency_check_summary(
            packet
        )
        report = build_source_policy_no_native_text_ocr_dependency_check_report(
            summary
        )
    except (OSError, ValueError) as exc:
        print("source_policy_no_native_text_ocr_dependency_check_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_ocr_dependency_available=false", file=sys.stderr)
        print("can_claim_ocr_execution=false", file=sys.stderr)
        print("can_claim_ocr_quality=false", file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("source_policy_no_native_text_ocr_dependency_check_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            return 2
        if current != report:
            print("source_policy_no_native_text_ocr_dependency_check_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            return 3
        print("source_policy_no_native_text_ocr_dependency_check_report_current")
        print(f"dependency_check_status={summary['dependency_check_status']}")
        print("can_claim_ocr_dependency_available=false")
        print("can_claim_ocr_execution=false")
        print("can_claim_ocr_quality=false")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("source_policy_no_native_text_ocr_dependency_check_v0")
    print(f"dependency_check_status={summary['dependency_check_status']}")
    print("can_claim_ocr_dependency_available=false")
    print("can_claim_ocr_execution=false")
    print("can_claim_ocr_quality=false")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
