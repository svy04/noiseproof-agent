from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.owner_approved_real_world_pdf_download_hash import (
    build_owner_approved_real_world_pdf_download_hash_report,
    build_owner_approved_real_world_pdf_download_hash_summary,
    load_owner_approved_real_world_pdf_download_hash_manifest,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Regenerate the owner-approved real-world PDF download/hash report."
    )
    parser.add_argument("--manifest", required=True, help="Download/hash manifest path.")
    parser.add_argument("--output", required=True, help="Markdown report output path.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compare generated report with output path without writing.",
    )
    args = parser.parse_args(argv)

    try:
        manifest = load_owner_approved_real_world_pdf_download_hash_manifest(
            Path(args.manifest)
        )
        summary = build_owner_approved_real_world_pdf_download_hash_summary(manifest)
        report = build_owner_approved_real_world_pdf_download_hash_report(summary)
    except (OSError, ValueError) as exc:
        print("owner_approved_real_world_pdf_download_hash_report_failed", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        print("not robust PDF extraction evidence", file=sys.stderr)
        return 2

    output = Path(args.output)
    if args.check:
        try:
            current = output.read_text(encoding="utf-8")
        except OSError as exc:
            print(
                "owner_approved_real_world_pdf_download_hash_report_failed",
                file=sys.stderr,
            )
            print(str(exc), file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 2
        if current != report:
            print(
                "owner_approved_real_world_pdf_download_hash_report_stale",
                file=sys.stderr,
            )
            print("byte-for-byte regeneration mismatch", file=sys.stderr)
            print("not robust PDF extraction evidence", file=sys.stderr)
            return 3
        print("owner_approved_real_world_pdf_download_hash_report_current")
        print("download/hash metadata only")
        print("not robust PDF extraction evidence")
        print(str(output))
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")

    print("owner_approved_real_world_pdf_download_and_hash_v0")
    print("download/hash metadata only")
    print("not robust PDF extraction evidence")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
