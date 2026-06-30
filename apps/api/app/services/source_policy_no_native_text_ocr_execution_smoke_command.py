from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Mapping, Sequence


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_execution_smoke import (  # noqa: E402
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_execution_smoke_report,
    build_source_policy_no_native_text_ocr_execution_smoke_summary,
    discover_source_policy_no_native_text_ocr_smoke_input,
    load_source_policy_no_native_text_ocr_execution_smoke,
    run_source_policy_no_native_text_ocr_smoke,
)


def main(
    argv: Sequence[str] | None = None,
    env: Mapping[str, str] | None = None,
) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    environment = env if env is not None else os.environ
    if args == ["--discover-owner-runtime-input"]:
        _print_json(discover_source_policy_no_native_text_ocr_smoke_input(environment))
        return 0
    if args and args[0] == "--run-owner-runtime-smoke":
        try:
            output_path = _parse_output_arg(args[1:])
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
            return 2
        result = run_source_policy_no_native_text_ocr_smoke(
            output_path=output_path,
            env=environment,
        )
        if result.get("run_status") == "report_written":
            _print_json(
                {
                    "phase_marker": PHASE_MARKER,
                    "run_status": "report_written",
                    "ocr_execution_performed": True,
                    "can_claim_ocr_quality": False,
                    "can_claim_robust_pdf_extraction": False,
                }
            )
            return 0
        _print_json(result)
        if result.get("run_status") == "input_not_ready":
            return 4
        return 5
    try:
        observation_path, output_path, check = _parse_report_args(args)
    except ValueError as exc:
        _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
        return 2

    observation = load_source_policy_no_native_text_ocr_execution_smoke(
        observation_path
    )
    summary = build_source_policy_no_native_text_ocr_execution_smoke_summary(
        observation
    )
    report = build_source_policy_no_native_text_ocr_execution_smoke_report(summary)
    if check:
        current = output_path.read_text(encoding="utf-8")
        if current != report:
            print("source_policy_no_native_text_ocr_execution_smoke_report_stale")
            return 1
        print("source_policy_no_native_text_ocr_execution_smoke_report_current")
    else:
        output_path.write_text(report, encoding="utf-8")
        print("source_policy_no_native_text_ocr_execution_smoke_report_written")
    print(
        "ocr_execution_performed="
        + _format_bool(summary["ocr_execution_performed"])
    )
    print("can_claim_ocr_execution=" + _format_bool(summary["can_claim_ocr_execution"]))
    print("can_claim_ocr_quality=" + _format_bool(summary["can_claim_ocr_quality"]))
    print(
        "can_claim_robust_pdf_extraction="
        + _format_bool(summary["can_claim_robust_pdf_extraction"])
    )
    print(output_path)
    return 0


def _parse_report_args(args: Sequence[str]) -> tuple[Path, Path, bool]:
    check = False
    values = list(args)
    if "--check" in values:
        check = True
        values.remove("--check")
    if len(values) != 4 or values[0] != "--observation" or values[2] != "--output":
        raise ValueError("expected --observation <path> --output <path> [--check]")
    return Path(values[1]), Path(values[3]), check


def _parse_output_arg(args: Sequence[str]) -> Path:
    if len(args) != 2 or args[0] != "--output":
        raise ValueError("expected --output <path>")
    return Path(args[1])


def _print_json(payload: Mapping[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"


if __name__ == "__main__":
    raise SystemExit(main())
