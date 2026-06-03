from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from shutil import which as default_which
from subprocess import CompletedProcess, TimeoutExpired
from typing import Callable
from uuid import UUID

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.scanning import ClamAvScannerAdapter, ScanAdapterRequest

BinaryProbe = Callable[[str], str | None]

PHASE_MARKER = "uploaded raw file ClamAV adapter runtime smoke v0"
TEMPORARY_SCAN_PATH = "C:/tmp/noiseproof/generated-key.bin"


def build_clamav_adapter_smoke_report(
    *,
    binary_name: str = "clamscan",
    binary_probe: BinaryProbe = default_which,
) -> dict[str, object]:
    scenarios = [
        _scenario_missing_binary(),
        _scenario_clean_output(),
        _scenario_infected_output(),
        _scenario_timeout(),
        _scenario_unknown_return_code(),
    ]
    smoke_passed = all(scenario["passed"] for scenario in scenarios)

    return {
        "phase_marker": PHASE_MARKER,
        "smoke_status": "passed" if smoke_passed else "failed",
        "real_clamav_runtime_verified": False,
        "clamav_binary_present": binary_probe(binary_name) is not None,
        "binary_probe_only": True,
        "scenarios": scenarios,
        "claims": {
            "adapter_boundary_exercised": True,
            "malware_scanning_evidence": False,
            "clamav_installation_verified": False,
            "signature_database_verified": False,
            "endpoint_behavior_verified": False,
            "download_endpoint_verified": False,
            "hosted_deployment_verified": False,
        },
        "boundary": [
            "not malware scanning evidence",
            "not ClamAV installation evidence",
            "not signature database evidence",
            "not endpoint behavior",
            "not download behavior",
            "not hosted deployment evidence",
            "not external reviewer feedback",
            "not product-complete",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run a deterministic ClamAV adapter smoke without executing real ClamAV."
    )
    parser.add_argument(
        "--binary-name",
        default="clamscan",
        help="Binary name to probe with shutil.which. The command does not execute it.",
    )
    parser.add_argument("--output", help="Optional JSON output path.")
    args = parser.parse_args(argv)

    report = build_clamav_adapter_smoke_report(binary_name=args.binary_name)
    payload = json.dumps(report, indent=2, sort_keys=True)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)

    return 0 if report["smoke_status"] == "passed" else 2


def _scenario_missing_binary() -> dict[str, object]:
    result = ClamAvScannerAdapter(which=lambda _: None).scan(_request())
    return _scenario_summary(
        "missing_binary",
        result,
        expected_status="failed",
        expected_verdict="scan_error",
        expected_failure_reason="missing_clamscan",
    )


def _scenario_clean_output() -> dict[str, object]:
    def runner(command, **kwargs):
        return CompletedProcess(command, 0, stdout="C:/tmp/file.bin: OK\n", stderr="")

    result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    ).scan(_request())
    return _scenario_summary(
        "clean_output",
        result,
        expected_status="completed",
        expected_verdict="clean",
    )


def _scenario_infected_output() -> dict[str, object]:
    def runner(command, **kwargs):
        return CompletedProcess(
            command,
            1,
            stdout="C:/tmp/file.bin: Eicar-Test-Signature FOUND\n",
            stderr="",
        )

    result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    ).scan(_request())
    return _scenario_summary(
        "infected_output",
        result,
        expected_status="completed",
        expected_verdict="infected",
        expected_signature="Eicar-Test-Signature",
    )


def _scenario_unknown_return_code() -> dict[str, object]:
    def runner(command, **kwargs):
        return CompletedProcess(command, 7, stdout="unexpected", stderr="weird")

    result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    ).scan(_request())
    return _scenario_summary(
        "unknown_return_code",
        result,
        expected_status="failed",
        expected_verdict="scan_error",
        expected_failure_reason="unknown_return_code",
    )


def _scenario_timeout() -> dict[str, object]:
    def runner(command, **kwargs):
        raise TimeoutExpired(cmd=command, timeout=kwargs["timeout"])

    result = ClamAvScannerAdapter(
        which=lambda _: "C:/tools/clamscan.exe",
        runner=runner,
    ).scan(_request())
    return _scenario_summary(
        "timeout",
        result,
        expected_status="failed",
        expected_verdict="scan_error",
        expected_failure_reason="timeout",
    )


def _scenario_summary(
    name: str,
    result,
    *,
    expected_status: str,
    expected_verdict: str,
    expected_failure_reason: str | None = None,
    expected_signature: str | None = None,
) -> dict[str, object]:
    failure_reason = result.metadata.get("failure_reason")
    temporary_path_leaked = (
        "temporary_scan_path" in result.metadata
        or TEMPORARY_SCAN_PATH
        in json.dumps(result.to_raw_file_scan_result_payload(), default=str)
    )
    passed = (
        result.scan_status == expected_status
        and result.scan_verdict == expected_verdict
        and failure_reason == expected_failure_reason
        and result.matched_signature == expected_signature
        and not temporary_path_leaked
    )

    return {
        "name": name,
        "passed": passed,
        "scan_status": result.scan_status,
        "scan_verdict": result.scan_verdict,
        "failure_reason": failure_reason,
        "matched_signature": result.matched_signature,
        "temporary_scan_path_leaked": temporary_path_leaked,
    }


def _request() -> ScanAdapterRequest:
    return ScanAdapterRequest(
        raw_file_id=UUID("00000000-0000-4000-8000-000000000268"),
        storage_key="raw-uploads/generated-key.bin",
        original_filename="sample.bin",
        declared_content_type="application/octet-stream",
        byte_size=64,
        content_sha256="abc123",
        temporary_scan_path=TEMPORARY_SCAN_PATH,
        scanner_timeout_seconds=3,
    )


if __name__ == "__main__":
    raise SystemExit(main())
