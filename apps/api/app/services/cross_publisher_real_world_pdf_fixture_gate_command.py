from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.cross_publisher_real_world_fixture import (
    build_cross_publisher_fixture_gate_report,
    build_cross_publisher_fixture_gate_summary,
    load_cross_publisher_observation,
)
from packages.ingestion.pdf_quality.multi_real_world_pdf_parse_observation import (
    load_multi_real_world_pdf_parse_observation_matrix,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the cross-publisher real-world PDF fixture gate report."
    )
    parser.add_argument("--base-matrix", required=True, help="Base BEA matrix JSON path.")
    parser.add_argument(
        "--observation", required=True, help="Cross-publisher observation JSON path."
    )
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        base_matrix = load_multi_real_world_pdf_parse_observation_matrix(
            Path(args.base_matrix)
        )
        observation = load_cross_publisher_observation(Path(args.observation))
        summary = build_cross_publisher_fixture_gate_summary(base_matrix, observation)
        report = build_cross_publisher_fixture_gate_report(summary)
    except (OSError, ValueError) as exc:
        print("cross_publisher_real_world_pdf_fixture_gate_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(
                "cross_publisher_real_world_pdf_fixture_gate_report_failed",
                file=sys.stderr,
            )
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print(
                "cross_publisher_real_world_pdf_fixture_gate_report_stale",
                file=sys.stderr,
            )
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("cross_publisher_real_world_pdf_fixture_gate_report_current")
        print(f"cross_publisher_gate_status={summary['cross_publisher_gate_status']}")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("cross_publisher_real_world_pdf_fixture_gate_v0")
    print(f"cross_publisher_gate_status={summary['cross_publisher_gate_status']}")
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

