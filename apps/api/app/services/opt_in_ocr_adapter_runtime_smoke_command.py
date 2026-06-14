from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Mapping, Sequence

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.opt_in_ocr_adapter_runtime_smoke import (
    PHASE_MARKER,
    discover_owner_runtime_input,
    owner_runtime_smoke_packet,
    run_owner_runtime_smoke,
    validate_owner_runtime_smoke_report,
)


def main(
    argv: Sequence[str] | None = None,
    env: Mapping[str, str] | None = None,
    ocr_adapter: object | None = None,
) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    environment = env if env is not None else os.environ
    if args == ["--print-owner-runtime-smoke-packet"]:
        _print_json(owner_runtime_smoke_packet())
        return 0
    if args == ["--discover-owner-runtime-input"]:
        _print_json(discover_owner_runtime_input(environment))
        return 0
    if len(args) == 2 and args[0] == "--validate-owner-runtime-smoke-report":
        report_path = Path(args[1])
        report = _read_json_report(report_path)
        validation = validate_owner_runtime_smoke_report(
            report,
            report_path=report_path,
        )
        _print_json(validation)
        return 0 if validation["accepted_owner_runtime_smoke"] is True else 5
    if args and args[0] == "--run-owner-runtime-smoke":
        try:
            output_path = _parse_output_arg(args[1:])
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
            return 2
        result = run_owner_runtime_smoke(
            output_path=output_path,
            env=environment,
            ocr_adapter=ocr_adapter,
        )
        if result.get("run_status") == "report_written":
            return 0
        _print_json(result)
        if result.get("run_status") == "input_not_ready":
            return 4
        return 5
    _print_json({"error": "unsupported_command", "phase_marker": PHASE_MARKER})
    return 2


def _parse_output_arg(args: Sequence[str]) -> Path:
    if len(args) != 2 or args[0] != "--output":
        raise ValueError("expected --output <path>")
    return Path(args[1])


def _read_json_report(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("opt-in OCR owner runtime report must be a JSON object")
    return payload


def _print_json(payload: Mapping[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    raise SystemExit(main())
