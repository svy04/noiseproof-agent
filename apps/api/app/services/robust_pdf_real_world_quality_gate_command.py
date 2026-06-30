from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.multi_real_world_pdf_parse_observation import (
    load_multi_real_world_pdf_parse_observation_matrix,
)
from packages.ingestion.pdf_quality.real_world_quality_gate import (
    build_real_world_quality_gate_report,
    build_real_world_quality_gate_summary,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the robust PDF real-world quality gate report."
    )
    parser.add_argument("--matrix", required=True, help="Observation matrix JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        matrix = load_multi_real_world_pdf_parse_observation_matrix(Path(args.matrix))
        summary = build_real_world_quality_gate_summary(matrix)
        report = build_real_world_quality_gate_report(summary)
    except (OSError, ValueError) as exc:
        print("robust_pdf_real_world_quality_gate_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("robust_pdf_real_world_quality_gate_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("robust_pdf_real_world_quality_gate_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("robust_pdf_real_world_quality_gate_report_current")
        print(f"quality_gate_status={summary['quality_gate_status']}")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("robust_pdf_extraction_next_real_world_quality_gate_v0")
    print(f"quality_gate_status={summary['quality_gate_status']}")
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
