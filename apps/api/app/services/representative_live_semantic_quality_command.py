from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture
from packages.ingestion.retrieval.representative_semantic_quality import (
    BOUNDARY,
    build_representative_live_semantic_quality_report,
    evaluate_representative_live_semantic_quality,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the representative live semantic quality report."
    )
    parser.add_argument(
        "--fixture-root",
        required=True,
        help="Representative semantic retrieval quality fixture directory.",
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
        evaluation = evaluate_representative_live_semantic_quality(
            fixture,
            k=args.k,
        )
        report = build_representative_live_semantic_quality_report(evaluation)
    except (OSError, ValueError) as exc:
        print("representative_live_semantic_quality_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not production semantic retrieval quality evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("representative_live_semantic_quality_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not production semantic retrieval quality evidence", file=sys.stderr)
            return 2
        if current != report:
            print("representative_live_semantic_quality_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not production semantic retrieval quality evidence", file=sys.stderr)
            return 3
        print("representative_live_semantic_quality_report_current")
        print("byte-for-byte regeneration")
        print("not production semantic retrieval quality evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("representative live semantic quality eval v0")
    print(BOUNDARY)
    print("not production semantic retrieval quality evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
