from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_rights_request_delivery_record import (  # noqa: E402
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record_report,
    build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary,
    load_source_policy_no_native_text_ocr_rights_request_delivery_record,
)


def main(argv: Sequence[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if args and args[0] == "--from-owner-rights-decision-record":
        try:
            owner_decision_path, delivery_record_path = _parse_generation_args(args)
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
            return 2
        owner_decision = json.loads(owner_decision_path.read_text(encoding="utf-8"))
        delivery_record = build_source_policy_no_native_text_ocr_rights_request_delivery_record(
            owner_decision
        )
        delivery_record_path.write_text(
            json.dumps(delivery_record, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print("source_policy_no_native_text_ocr_rights_request_delivery_record_written")
        print(delivery_record_path)
        return 0

    try:
        record_path, output_path, check = _parse_report_args(args)
    except ValueError as exc:
        _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
        return 2

    record = load_source_policy_no_native_text_ocr_rights_request_delivery_record(
        record_path
    )
    summary = build_source_policy_no_native_text_ocr_rights_request_delivery_record_summary(
        record
    )
    report = build_source_policy_no_native_text_ocr_rights_request_delivery_record_report(
        summary
    )
    if check:
        current = output_path.read_text(encoding="utf-8")
        if current != report:
            print("source_policy_no_native_text_ocr_rights_request_delivery_record_report_stale")
            return 1
        print("source_policy_no_native_text_ocr_rights_request_delivery_record_report_current")
    else:
        output_path.write_text(report, encoding="utf-8")
        print("source_policy_no_native_text_ocr_rights_request_delivery_record_report_written")
    print(
        "can_claim_rights_request_delivery_record="
        + _format_bool(summary["can_claim_rights_request_delivery_record"])
    )
    print(
        "can_claim_request_sent="
        + _format_bool(summary["can_claim_request_sent"])
    )
    print(
        "can_claim_delivery_performed="
        + _format_bool(summary["can_claim_delivery_performed"])
    )
    print(
        "can_claim_rights_clearance="
        + _format_bool(summary["can_claim_rights_clearance"])
    )
    print(
        "can_claim_source_rights_owner_approval="
        + _format_bool(summary["can_claim_source_rights_owner_approval"])
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
        or args[0] != "--from-owner-rights-decision-record"
        or args[2] != "--output-rights-request-delivery-record"
    ):
        raise ValueError(
            "expected --from-owner-rights-decision-record <path> --output-rights-request-delivery-record <path>"
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
        or values[0] != "--rights-request-delivery-record"
        or values[2] != "--output"
    ):
        raise ValueError(
            "expected --rights-request-delivery-record <path> --output <path> [--check]"
        )
    return Path(values[1]), Path(values[3]), check


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"


if __name__ == "__main__":
    raise SystemExit(main())
