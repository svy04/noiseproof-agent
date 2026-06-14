from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.retrieval.live_semantic_qrels import (
    BOUNDARY,
    build_live_semantic_qrels_baseline_report,
    evaluate_live_semantic_qrels_baseline,
)
from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the live semantic qrels baseline report."
    )
    parser.add_argument(
        "--fixture-root",
        required=True,
        help="Semantic retrieval quality fixture directory.",
    )
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument("--k", type=int, default=10, help="Evaluation cutoff.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        fixture = load_semantic_quality_fixture(Path(args.fixture_root))
        evaluation = evaluate_live_semantic_qrels_baseline(fixture, k=args.k)
        report = build_live_semantic_qrels_baseline_report(evaluation)
    except (OSError, ValueError) as exc:
        print("live_semantic_qrels_baseline_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not semantic retrieval quality evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("live_semantic_qrels_baseline_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not semantic retrieval quality evidence", file=sys.stderr)
            return 2
        if current != report:
            print("live_semantic_qrels_baseline_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not semantic retrieval quality evidence", file=sys.stderr)
            return 3
        print("live_semantic_qrels_baseline_report_current")
        print("byte-for-byte regeneration")
        print("not semantic retrieval quality evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("live semantic qrels baseline v0")
    print(BOUNDARY)
    print("not semantic retrieval quality evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
