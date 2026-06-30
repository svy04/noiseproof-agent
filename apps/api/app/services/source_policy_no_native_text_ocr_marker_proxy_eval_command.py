from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.pdf_quality.source_policy_no_native_text_ocr_marker_proxy_eval import (  # noqa: E402
    PHASE_MARKER,
    build_source_policy_no_native_text_ocr_marker_proxy_eval,
    build_source_policy_no_native_text_ocr_marker_proxy_eval_report,
    build_source_policy_no_native_text_ocr_marker_proxy_eval_summary,
    load_source_policy_no_native_text_ocr_marker_proxy_eval,
)


def main(argv: Sequence[str] | None = None) -> int:
    args = list(argv if argv is not None else sys.argv[1:])
    if args and args[0] == "--from-reference-pack":
        try:
            reference_pack_path, smoke_path, marker_eval_path = _parse_generation_args(
                args
            )
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
            return 2
        reference_pack = json.loads(reference_pack_path.read_text(encoding="utf-8"))
        smoke = json.loads(smoke_path.read_text(encoding="utf-8"))
        marker_eval = build_source_policy_no_native_text_ocr_marker_proxy_eval(
            reference_pack,
            smoke,
        )
        marker_eval_path.write_text(
            json.dumps(marker_eval, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print("source_policy_no_native_text_ocr_marker_proxy_eval_written")
        print(marker_eval_path)
        return 0

    try:
        marker_eval_path, output_path, check = _parse_report_args(args)
    except ValueError as exc:
        _print_json({"error": str(exc), "phase_marker": PHASE_MARKER})
        return 2

    marker_eval = load_source_policy_no_native_text_ocr_marker_proxy_eval(
        marker_eval_path
    )
    summary = build_source_policy_no_native_text_ocr_marker_proxy_eval_summary(
        marker_eval
    )
    report = build_source_policy_no_native_text_ocr_marker_proxy_eval_report(
        summary
    )
    if check:
        current = output_path.read_text(encoding="utf-8")
        if current != report:
            print("source_policy_no_native_text_ocr_marker_proxy_eval_report_stale")
            return 1
        print("source_policy_no_native_text_ocr_marker_proxy_eval_report_current")
    else:
        output_path.write_text(report, encoding="utf-8")
        print("source_policy_no_native_text_ocr_marker_proxy_eval_report_written")
    print(
        "can_claim_marker_proxy_eval="
        + _format_bool(summary["can_claim_marker_proxy_eval"])
    )
    print("can_claim_ocr_quality=" + _format_bool(summary["can_claim_ocr_quality"]))
    print(
        "can_claim_robust_pdf_extraction="
        + _format_bool(summary["can_claim_robust_pdf_extraction"])
    )
    print(output_path)
    return 0


def _parse_generation_args(args: Sequence[str]) -> tuple[Path, Path, Path]:
    if (
        len(args) != 6
        or args[0] != "--from-reference-pack"
        or args[2] != "--execution-smoke"
        or args[4] != "--output-marker-proxy-eval"
    ):
        raise ValueError(
            "expected --from-reference-pack <path> --execution-smoke <path> --output-marker-proxy-eval <path>"
        )
    return Path(args[1]), Path(args[3]), Path(args[5])


def _parse_report_args(args: Sequence[str]) -> tuple[Path, Path, bool]:
    check = False
    values = list(args)
    if "--check" in values:
        check = True
        values.remove("--check")
    if (
        len(values) != 4
        or values[0] != "--marker-proxy-eval"
        or values[2] != "--output"
    ):
        raise ValueError("expected --marker-proxy-eval <path> --output <path> [--check]")
    return Path(values[1]), Path(values[3]), check


def _print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def _format_bool(value: object) -> str:
    return "true" if value is True else "false"


if __name__ == "__main__":
    raise SystemExit(main())
