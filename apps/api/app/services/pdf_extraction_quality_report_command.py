from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.evaluator import evaluate_pdf_extraction_quality
from packages.ingestion.pdf_quality.fixture import load_pdf_extraction_quality_fixture
from packages.ingestion.pdf_quality.report import build_pdf_extraction_quality_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the PDF extraction quality report."
    )
    parser.add_argument("--fixture", required=True, help="Fixture directory path.")
    parser.add_argument(
        "--observations",
        required=True,
        help="PDF extraction observation JSON path.",
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
        observations = _read_observations(Path(args.observations))
        evaluation = evaluate_pdf_extraction_quality(fixture, observations)
        report = build_pdf_extraction_quality_report(fixture, evaluation)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("pdf_extraction_quality_report_regeneration_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("pdf_extraction_quality_report_regeneration_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("pdf_extraction_quality_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("pdf_extraction_quality_report_current")
        print("byte-for-byte regeneration")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("PDF extraction quality report v0")
    print(evaluation["claim_boundary"])
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


def _read_observations(path: Path) -> dict[str, dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("observations fixture must be a JSON object")
    return payload


if __name__ == "__main__":
    raise SystemExit(main())
