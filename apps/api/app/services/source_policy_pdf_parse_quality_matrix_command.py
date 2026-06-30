from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_pdf_parse_quality_matrix import (  # noqa: E402
    build_source_policy_pdf_parse_quality_matrix_report,
    build_source_policy_pdf_parse_quality_matrix_summary,
    load_source_policy_pdf_parse_quality_matrix,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the source-policy PDF parse quality matrix report."
    )
    parser.add_argument("--matrix", required=True, help="Quality matrix JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        matrix = load_source_policy_pdf_parse_quality_matrix(Path(args.matrix))
        summary = build_source_policy_pdf_parse_quality_matrix_summary(matrix)
        report = build_source_policy_pdf_parse_quality_matrix_report(summary)
    except (OSError, ValueError) as exc:
        print("source_policy_pdf_parse_quality_matrix_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("source_policy_pdf_parse_quality_matrix_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 2
        if current != report:
            print("source_policy_pdf_parse_quality_matrix_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 3
        print("source_policy_pdf_parse_quality_matrix_report_current")
        print(f"quality_status={summary['quality_status']}")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("source_policy_pdf_parse_quality_matrix_v0")
    print(f"quality_status={summary['quality_status']}")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
