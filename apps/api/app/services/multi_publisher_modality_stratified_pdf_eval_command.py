from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.multi_publisher_modality_stratified_pdf_eval import (  # noqa: E402
    build_multi_publisher_modality_stratified_pdf_eval_report,
    build_multi_publisher_modality_stratified_pdf_eval_summary,
    load_multi_publisher_modality_stratified_pdf_eval,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the multi-publisher modality-stratified PDF eval report."
    )
    parser.add_argument("--evidence", required=True, help="Matrix packet JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        matrix = load_multi_publisher_modality_stratified_pdf_eval(Path(args.evidence))
        summary = build_multi_publisher_modality_stratified_pdf_eval_summary(matrix)
        report = build_multi_publisher_modality_stratified_pdf_eval_report(summary)
    except (OSError, ValueError) as exc:
        print("multi_publisher_modality_stratified_pdf_eval_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(
                "multi_publisher_modality_stratified_pdf_eval_report_failed",
                file=sys.stderr,
            )
            print(str(exc), file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 2
        if current != report:
            print(
                "multi_publisher_modality_stratified_pdf_eval_report_stale",
                file=sys.stderr,
            )
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 3
        print("multi_publisher_modality_stratified_pdf_eval_report_current")
        print(f"coverage_status={summary['coverage_status']}")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("multi_publisher_modality_stratified_pdf_eval_v0")
    print(f"coverage_status={summary['coverage_status']}")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
