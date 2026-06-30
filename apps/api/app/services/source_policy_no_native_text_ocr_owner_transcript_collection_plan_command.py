from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_owner_transcript_collection_plan import (  # noqa: E402
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_report,
    build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary,
    load_source_policy_no_native_text_ocr_owner_transcript_collection_plan,
)


def main(argv: Sequence[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if args and args[0] == "--from-transcript-reference-pack":
        try:
            pack_path, plan_path = _parse_generation_args(args)
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
            return 2
        pack = json.loads(pack_path.read_text(encoding="utf-8"))
        plan = build_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
            pack
        )
        plan_path.write_text(
            json.dumps(plan, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print("source_policy_no_native_text_ocr_owner_transcript_collection_plan_written")
        print(plan_path)
        return 0

    try:
        plan_path, output_path, check = _parse_report_args(args)
    except ValueError as exc:
        _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
        return 2

    plan = load_source_policy_no_native_text_ocr_owner_transcript_collection_plan(
        plan_path
    )
    summary = (
        build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_summary(
            plan
        )
    )
    report = (
        build_source_policy_no_native_text_ocr_owner_transcript_collection_plan_report(
            summary
        )
    )
    if check:
        current = output_path.read_text(encoding="utf-8")
        if current != report:
            print("source_policy_no_native_text_ocr_owner_transcript_collection_plan_report_stale")
            return 1
        print("source_policy_no_native_text_ocr_owner_transcript_collection_plan_report_current")
    else:
        output_path.write_text(report, encoding="utf-8")
        print("source_policy_no_native_text_ocr_owner_transcript_collection_plan_report_written")
    print(
        "can_claim_owner_transcript_collection_plan="
        + _format_bool(summary["can_claim_owner_transcript_collection_plan"])
    )
    print(
        "can_claim_transcript_collection="
        + _format_bool(summary["can_claim_transcript_collection"])
    )
    print(
        "can_claim_reference_transcript_available="
        + _format_bool(summary["can_claim_reference_transcript_available"])
    )
    print("can_claim_ocr_quality=" + _format_bool(summary["can_claim_ocr_quality"]))
    print(
        "can_claim_robust_pdf_extraction="
        + _format_bool(summary["can_claim_robust_pdf_extraction"])
    )
    print(output_path)
    return 0


def _parse_generation_args(args: Sequence[str]) -> tuple[Path, Path]:
    if (
        len(args) != 4
        or args[0] != "--from-transcript-reference-pack"
        or args[2] != "--output-owner-transcript-collection-plan"
    ):
        raise ValueError(
            "expected --from-transcript-reference-pack <path> --output-owner-transcript-collection-plan <path>"
        )
    return Path(args[1]), Path(args[3])


def _parse_report_args(args: Sequence[str]) -> tuple[Path, Path, bool]:
    check = False
    values = list(args)
    if "--check" in values:
        check = True
        values.remove("--check")
    if (
        len(values) != 4
        or values[0] != "--owner-transcript-collection-plan"
        or values[2] != "--output"
    ):
        raise ValueError(
            "expected --owner-transcript-collection-plan <path> --output <path> [--check]"
        )
    return Path(values[1]), Path(values[3]), check


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"


if __name__ == "__main__":
    raise SystemExit(main())
