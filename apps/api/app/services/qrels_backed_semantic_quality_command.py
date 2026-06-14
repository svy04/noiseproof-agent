from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.retrieval.qrels_eval import (
    build_qrels_backed_semantic_quality_report,
    evaluate_qrels_backed_run,
    parse_qrels_file,
    parse_trec_run_file,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the toy qrels-backed semantic retrieval quality report."
    )
    parser.add_argument("--qrels", required=True, help="TREC-style qrels file path.")
    parser.add_argument("--run", required=True, help="TREC-style run file path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument("--k", type=int, default=10, help="Evaluation cutoff.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        qrels = parse_qrels_file(Path(args.qrels))
        run = parse_trec_run_file(Path(args.run))
        evaluation = evaluate_qrels_backed_run(qrels=qrels, run=run, k=args.k)
        report = build_qrels_backed_semantic_quality_report(evaluation)
    except (OSError, ValueError) as exc:
        print("qrels_backed_semantic_quality_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not semantic retrieval quality evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("qrels_backed_semantic_quality_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not semantic retrieval quality evidence", file=sys.stderr)
            return 2
        if current != report:
            print("qrels_backed_semantic_quality_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not semantic retrieval quality evidence", file=sys.stderr)
            return 3
        print("qrels_backed_semantic_quality_report_current")
        print("byte-for-byte regeneration")
        print("not semantic retrieval quality evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("qrels-backed semantic retrieval quality eval v0")
    print(evaluation["boundary"])
    print("not semantic retrieval quality evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
