from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_execution_plan import (  # noqa: E402
    build_source_policy_no_native_text_ocr_execution_plan_report,
    build_source_policy_no_native_text_ocr_execution_plan_summary,
    load_source_policy_no_native_text_ocr_execution_plan,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the source-policy no-native-text OCR execution plan report."
    )
    parser.add_argument("--plan", help="OCR execution plan JSON packet path.")
    parser.add_argument("--output", help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    if not args.plan or not args.output:
        print("source_policy_no_native_text_ocr_execution_plan_report_failed", file=sys.stderr)
        print("expected --plan <path> --output <path>", file=sys.stderr)
        return 2

    try:
        packet = load_source_policy_no_native_text_ocr_execution_plan(
            Path(args.plan)
        )
        summary = build_source_policy_no_native_text_ocr_execution_plan_summary(
            packet
        )
        report = build_source_policy_no_native_text_ocr_execution_plan_report(
            summary
        )
    except (OSError, ValueError) as exc:
        print("source_policy_no_native_text_ocr_execution_plan_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_ocr_execution_plan=false", file=sys.stderr)
        print("can_claim_ocr_execution=false", file=sys.stderr)
        print("can_claim_ocr_quality=false", file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("source_policy_no_native_text_ocr_execution_plan_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            return 2
        if current != report:
            print("source_policy_no_native_text_ocr_execution_plan_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            return 3
        print("source_policy_no_native_text_ocr_execution_plan_report_current")
        print(f"plan_status={summary['plan_status']}")
        print("can_claim_ocr_execution_plan=true")
        print("can_claim_ocr_execution=false")
        print("can_claim_ocr_quality=false")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("source_policy_no_native_text_ocr_execution_plan_v0")
    print(f"plan_status={summary['plan_status']}")
    print("can_claim_ocr_execution_plan=true")
    print("can_claim_ocr_execution=false")
    print("can_claim_ocr_quality=false")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
