from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.robust_pdf_generalization_gap_review import (  # noqa: E402
    build_robust_pdf_generalization_gap_review_report,
    build_robust_pdf_generalization_gap_review_summary,
    load_robust_pdf_generalization_gap_review,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the robust PDF generalization gap review report."
    )
    parser.add_argument("--evidence", required=True, help="Review packet JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        review = load_robust_pdf_generalization_gap_review(Path(args.evidence))
        summary = build_robust_pdf_generalization_gap_review_summary(review)
        report = build_robust_pdf_generalization_gap_review_report(summary)
    except (OSError, ValueError) as exc:
        print("robust_pdf_generalization_gap_review_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(
                "robust_pdf_generalization_gap_review_report_failed",
                file=sys.stderr,
            )
            print(str(exc), file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 2
        if current != report:
            print(
                "robust_pdf_generalization_gap_review_report_stale",
                file=sys.stderr,
            )
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 3
        print("robust_pdf_generalization_gap_review_report_current")
        print(f"generalization_gap_status={summary['generalization_gap_status']}")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("robust_pdf_extraction_generalization_gap_review_v0")
    print(f"generalization_gap_status={summary['generalization_gap_status']}")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
