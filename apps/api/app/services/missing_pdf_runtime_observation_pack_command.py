from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.missing_runtime_pack import (
    build_missing_pdf_runtime_observation_pack_report,
    build_missing_pdf_runtime_observation_pack_summary,
    load_missing_pdf_runtime_observation_pack,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the missing PDF runtime observation pack report."
    )
    parser.add_argument("--fixture", required=True, help="Fixture directory path.")
    parser.add_argument(
        "--base-observations",
        required=True,
        help="Existing PDF extraction observation JSON path.",
    )
    parser.add_argument(
        "--pack",
        required=True,
        help="Missing runtime observation pack JSON path.",
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
        base_observations = _read_observations(Path(args.base_observations))
        pack = load_missing_pdf_runtime_observation_pack(Path(args.pack))
        summary = build_missing_pdf_runtime_observation_pack_summary(
            fixture,
            base_observations,
            pack,
        )
        report = build_missing_pdf_runtime_observation_pack_report(summary)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("missing_pdf_runtime_observation_pack_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("missing_pdf_runtime_observation_pack_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("missing_pdf_runtime_observation_pack_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("missing_pdf_runtime_observation_pack_report_current")
        print("byte-for-byte regeneration")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("missing_pdf_runtime_observation_pack_v0")
    print(summary["claim_boundary"])
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


def _read_observations(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("base observations must be a JSON object")
    return payload


if __name__ == "__main__":
    raise SystemExit(main())
