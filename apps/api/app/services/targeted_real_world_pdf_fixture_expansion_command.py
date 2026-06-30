from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.targeted_fixture_expansion import (  # noqa: E402
    build_targeted_real_world_pdf_fixture_expansion_report,
    build_targeted_real_world_pdf_fixture_expansion_summary,
    load_targeted_real_world_pdf_fixture_expansion_plan,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the targeted real-world PDF fixture expansion report."
    )
    parser.add_argument("--plan", required=True, help="Fixture expansion plan JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        plan = load_targeted_real_world_pdf_fixture_expansion_plan(Path(args.plan))
        summary = build_targeted_real_world_pdf_fixture_expansion_summary(plan)
        report = build_targeted_real_world_pdf_fixture_expansion_report(summary)
    except (OSError, ValueError) as exc:
        print("targeted_real_world_pdf_fixture_expansion_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(
                "targeted_real_world_pdf_fixture_expansion_report_failed",
                file=sys.stderr,
            )
            print(str(exc), file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 2
        if current != report:
            print(
                "targeted_real_world_pdf_fixture_expansion_report_stale",
                file=sys.stderr,
            )
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("can_claim_robust_pdf_extraction=false", file=sys.stderr)
            return 3
        print("targeted_real_world_pdf_fixture_expansion_report_current")
        print(f"candidate_count={summary['candidate_count']}")
        print("can_claim_robust_pdf_extraction=false")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("targeted_real_world_pdf_fixture_expansion_v0")
    print(f"candidate_count={summary['candidate_count']}")
    print("can_claim_robust_pdf_extraction=false")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
