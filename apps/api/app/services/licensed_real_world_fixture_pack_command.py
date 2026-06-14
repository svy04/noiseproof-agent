from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.licensed_real_world_fixture_pack import (
    build_licensed_real_world_fixture_pack_report,
    build_licensed_real_world_fixture_pack_summary,
    load_licensed_real_world_fixture_pack,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the licensed real-world PDF fixture pack report."
    )
    parser.add_argument("--pack", required=True, help="Candidate pack JSON path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        pack = load_licensed_real_world_fixture_pack(Path(args.pack))
        summary = build_licensed_real_world_fixture_pack_summary(pack)
        report = build_licensed_real_world_fixture_pack_report(summary)
    except (OSError, ValueError) as exc:
        print("licensed_real_world_pdf_fixture_pack_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print("licensed_real_world_pdf_fixture_pack_report_failed", file=sys.stderr)
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print("licensed_real_world_pdf_fixture_pack_report_stale", file=sys.stderr)
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("licensed_real_world_pdf_fixture_pack_report_current")
        print("candidate metadata only")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("licensed_real_world_pdf_fixture_pack_v0")
    print("candidate metadata only")
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
