from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture
from packages.ingestion.retrieval.quality_metrics import evaluate_semantic_quality
from packages.ingestion.retrieval.quality_report import build_semantic_quality_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the toy semantic retrieval quality report."
    )
    parser.add_argument("--fixture", required=True, help="Fixture directory path.")
    parser.add_argument("--rankings", required=True, help="Toy rankings JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument("--k", type=int, default=2, help="Evaluation cutoff.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        fixture = load_semantic_quality_fixture(Path(args.fixture))
        ranking_fixture = _read_rankings(Path(args.rankings))
        evaluation = evaluate_semantic_quality(
            fixture,
            ranking_fixture["semantic_rankings"],
            lexical_rankings=ranking_fixture.get("lexical_rankings"),
            k=args.k,
        )
        report = build_semantic_quality_report(fixture, evaluation)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print("semantic_quality_report_regeneration_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not vector search quality evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("semantic_quality_report_regeneration_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not vector search quality evidence", file=sys.stderr)
            return 2
        if current != report:
            print("semantic_quality_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not vector search quality evidence", file=sys.stderr)
            return 3
        print("semantic_quality_report_current")
        print("byte-for-byte regeneration")
        print("not vector search quality evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("semantic retrieval quality report v0")
    print(evaluation["claim_boundary"])
    print("not vector search quality evidence")
    print(str(output))
    return 0


def _read_rankings(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    semantic_rankings = payload.get("semantic_rankings")
    if not isinstance(semantic_rankings, dict):
        raise ValueError("rankings fixture must include semantic_rankings object")
    return payload


if __name__ == "__main__":
    raise SystemExit(main())
