from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_failure_route import (  # noqa: E402
    build_source_policy_no_native_text_failure_route_report,
    build_source_policy_no_native_text_failure_route_summary,
    load_source_policy_no_native_text_failure_route,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the source-policy no-native-text failure route report."
    )
    parser.add_argument("--route", required=True, help="Failure route JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        route = load_source_policy_no_native_text_failure_route(Path(args.route))
        summary = build_source_policy_no_native_text_failure_route_summary(route)
        report = build_source_policy_no_native_text_failure_route_report(summary)
    except (OSError, ValueError) as exc:
        print("source_policy_no_native_text_failure_route_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_ocr_quality=false", file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("source_policy_no_native_text_failure_route_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("can_claim_ocr_quality=false", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 2
        if current != report:
            print("source_policy_no_native_text_failure_route_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("can_claim_ocr_quality=false", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 3
        print("source_policy_no_native_text_failure_route_report_current")
        print(f"route_status={summary['route_status']}")
        print(f"failure_type={summary['failure_type']}")
        print("can_claim_ocr_quality=false")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("source_policy_no_native_text_failure_route_v0")
    print(f"route_status={summary['route_status']}")
    print(f"failure_type={summary['failure_type']}")
    print("can_claim_ocr_quality=false")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
