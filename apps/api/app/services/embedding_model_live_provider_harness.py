from __future__ import annotations

import json
import os
import sys
from collections.abc import Mapping, Sequence
from pathlib import Path


PHASE_MARKER = "embedding model live-provider owner-runtime smoke packet v0"
DISCOVERY_PHASE_MARKER = "embedding model live-provider owner-runtime input discovery v0"
VALIDATOR_PHASE_MARKER = "embedding model live-provider owner-runtime smoke validator v0"
REPORT_CONTRACT_PHASE_MARKER = (
    "embedding model live-provider owner-runtime smoke report contract v0"
)
EXPECTED_REPORT_TOP_LEVEL_FIELDS = {
    "api_calls_attempted",
    "embedding_length",
    "embedding_model",
    "embedding_status",
    "http_status",
    "openai_api_key_printed",
    "persistence_boundary",
    "provider_response_dimension_check",
    "route",
    "secret_committed_to_repo",
    "secret_exposed",
    "secret_logged",
    "usage_metadata_present",
}
SECRET_FIELD_NAMES = {
    "api_key",
    "authorization",
    "openai_api_key",
    "provider_secret",
    "secret",
    "token",
}


def _owner_runtime_smoke_packet() -> dict:
    request_payload = {
        "text": "Enterprise demand growth reached 12% in Q1.",
        "allow_provider_call": True,
        "embedding_model": "text-embedding-3-small",
        "embedding_dimension": 1536,
        "encoding_format": "float",
    }
    return {
        "phase_marker": PHASE_MARKER,
        "packet_status": "ready_for_owner_input",
        "required_input": (
            "owner-provided OPENAI_API_KEY via environment outside the repository"
        ),
        "required_runtime_env": {
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
            "OPENAI_API_KEY": "owner-provided-secret-not-in-command",
            "CI": "false",
        },
        "route": "POST /chunks/embedding-model-preview",
        "local_service_url": "http://127.0.0.1:8000",
        "request_payload": request_payload,
        "command_templates": {
            "posix": (
                "NOISEPROOF_ENABLE_OPENAI_PROVIDER=true "
                "CI=false "
                "uv run uvicorn app.main:app --host 127.0.0.1 --port 8000"
            ),
            "powershell": (
                "$env:NOISEPROOF_ENABLE_OPENAI_PROVIDER='true'; "
                "$env:CI='false'; "
                "uv run uvicorn app.main:app --host 127.0.0.1 --port 8000"
            ),
            "curl": (
                "curl -sS -X POST http://127.0.0.1:8000/chunks/embedding-model-preview "
                "-H 'Content-Type: application/json' "
                "-d '{\"text\":\"Enterprise demand growth reached 12% in Q1.\","
                "\"allow_provider_call\":true,"
                "\"embedding_model\":\"text-embedding-3-small\","
                "\"embedding_dimension\":1536,"
                "\"encoding_format\":\"float\"}'"
            ),
        },
        "success_criteria": {
            "http_status": 200,
            "embedding_status": "owner_runtime_provider_generated",
            "embedding_length": 1536,
            "provider_response_dimension_check": "passed",
            "usage_metadata_present": True,
            "secret_exposed": False,
            "persistence_boundary": "preview_only_not_persisted",
        },
        "post_run_validation_command": (
            "uv run python -m app.services.embedding_model_live_provider_harness "
            "--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>"
        ),
        "post_run_validation_commands": {
            "posix": (
                "uv run python -m app.services.embedding_model_live_provider_harness "
                "--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>"
            ),
            "powershell": (
                "uv run python -m app.services.embedding_model_live_provider_harness "
                "--validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'"
            ),
        },
        "post_run_validation_success_criteria": {
            "validation_status": "accepted",
            "accepted_owner_runtime_smoke": True,
            "missing_or_failed_checks": [],
        },
        "failure_states": [
            "missing_openai_api_key",
            "opt_in_disabled",
            "ci_runtime",
            "provider_timeout",
            "provider_error",
            "dimension_mismatch",
        ],
        "runtime_report_handling": {
            "write_report_outside_repo": True,
            "validate_metadata_only": True,
            "do_not_commit_report_if_it_contains_secret_fields": True,
        },
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_committed_to_repo": False,
        "secret_logged": False,
        "non_claims": {
            "live_embedding_generation_proof": False,
            "hosted_deployment_evidence": False,
            "semantic_retrieval_quality_evidence": False,
            "external_reviewer_feedback": False,
        },
    }


def _env_flag_enabled(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _discover_owner_runtime_input(env: Mapping[str, str]) -> dict:
    api_key_present = bool((env.get("OPENAI_API_KEY") or "").strip())
    opt_in_enabled = _env_flag_enabled(env.get("NOISEPROOF_ENABLE_OPENAI_PROVIDER"))
    ci_runtime = _env_flag_enabled(env.get("CI"))

    if not api_key_present:
        status = "missing_openai_api_key"
        next_action = (
            "configure OPENAI_API_KEY outside the repository and set "
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime smoke only"
        )
    elif ci_runtime:
        status = "blocked_by_ci"
        next_action = "rerun outside CI for owner-runtime smoke only"
    elif not opt_in_enabled:
        status = "opt_in_disabled"
        next_action = "set NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime smoke only"
    else:
        status = "ready_for_owner_runtime_smoke"
        next_action = (
            "run the manual owner-runtime smoke packet outside CI and write any "
            "runtime report outside the repository"
        )

    return {
        "phase_marker": DISCOVERY_PHASE_MARKER,
        "owner_runtime_input_status": status,
        "discoverable_input_sources": ["environment"],
        "openai_api_key_present": api_key_present,
        "openai_api_key_printed": False,
        "opt_in_enabled": opt_in_enabled,
        "ci_runtime": ci_runtime,
        "api_calls_attempted": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "next_action": next_action,
        "non_claims": {
            "live_embedding_generation_proof": False,
            "hosted_deployment_evidence": False,
            "external_reviewer_feedback": False,
        },
    }


def _owner_runtime_smoke_report_contract() -> dict[str, object]:
    accepted_report = {
        "route": "POST /chunks/embedding-model-preview",
        "http_status": 200,
        "embedding_status": "owner_runtime_provider_generated",
        "embedding_model": "text-embedding-3-small",
        "embedding_length": 1536,
        "provider_response_dimension_check": "passed",
        "usage_metadata_present": True,
        "secret_exposed": False,
        "persistence_boundary": "preview_only_not_persisted",
        "api_calls_attempted": True,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
    }
    return {
        "phase_marker": REPORT_CONTRACT_PHASE_MARKER,
        "contract_status": "ready_for_owner_runtime_report",
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "validator_command": (
            "uv run python -m app.services.embedding_model_live_provider_harness "
            "--validate-owner-runtime-smoke-report path/to/owner-runtime-smoke-report.json"
        ),
        "accepted_report": accepted_report,
        "required_top_level_fields": sorted(accepted_report),
        "forbidden_secret_fields": sorted(SECRET_FIELD_NAMES),
        "accepted_validator_output": {
            "validation_status": "accepted",
            "accepted_owner_runtime_smoke": True,
            "missing_or_failed_checks": [],
        },
        "rejected_validator_output": {
            "validation_status": "rejected",
            "accepted_owner_runtime_smoke": False,
            "missing_or_failed_checks": "non-empty",
        },
        "non_claims": {
            "live_embedding_generation_proof": False,
            "hosted_deployment_evidence": False,
            "semantic_retrieval_quality_evidence": False,
            "external_reviewer_feedback": False,
            "product_complete": False,
        },
        "boundary": [
            "contract only",
            "does not read or print OPENAI_API_KEY",
            "does not call the OpenAI provider",
            "does not persist embeddings",
            "not live embedding generation proof",
            "owner-provided runtime smoke remains pending",
        ],
    }


def _validate_owner_runtime_smoke_report(
    report: Mapping[str, object], *, report_path: Path | None = None
) -> dict:
    missing_or_failed_checks: list[str] = []
    forbidden_secret_fields = _find_forbidden_secret_fields(report)
    for field_path in forbidden_secret_fields:
        missing_or_failed_checks.append(f"forbidden secret field present: {field_path}")

    unexpected_fields = sorted(
        str(key) for key in report if str(key) not in EXPECTED_REPORT_TOP_LEVEL_FIELDS
    )
    for field_path in unexpected_fields:
        missing_or_failed_checks.append(f"unexpected field present: {field_path}")

    report_path_allowed = (
        report_path is None or not _path_is_inside_repository(report_path)
    )
    if not report_path_allowed:
        missing_or_failed_checks.append("report path must be outside repository")

    expected_values = {
        "route": "POST /chunks/embedding-model-preview",
        "http_status": 200,
        "embedding_status": "owner_runtime_provider_generated",
        "embedding_model": "text-embedding-3-small",
        "embedding_length": 1536,
        "provider_response_dimension_check": "passed",
        "usage_metadata_present": True,
        "secret_exposed": False,
        "persistence_boundary": "preview_only_not_persisted",
        "api_calls_attempted": True,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
    }
    for field, expected_value in expected_values.items():
        if report.get(field) != expected_value:
            formatted = str(expected_value).lower()
            missing_or_failed_checks.append(f"{field} must be {formatted}")

    accepted = not missing_or_failed_checks
    return {
        "phase_marker": VALIDATOR_PHASE_MARKER,
        "validation_status": "accepted" if accepted else "rejected",
        "accepted_owner_runtime_smoke": accepted,
        "missing_or_failed_checks": missing_or_failed_checks,
        "forbidden_secret_fields": forbidden_secret_fields,
        "unexpected_fields": unexpected_fields,
        "report_path_boundary": {
            "report_path_allowed": report_path_allowed,
            "required_location": "outside_repository",
        },
        "reported_embedding_status": report.get("embedding_status"),
        "reported_embedding_length": report.get("embedding_length"),
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "non_claims": {
            "validator_makes_provider_call": False,
            "hosted_deployment_evidence": False,
            "external_reviewer_feedback": False,
            "semantic_retrieval_quality_evidence": False,
        },
        "boundary": [
            "validates owner-provided runtime smoke metadata only",
            "does not read or print OPENAI_API_KEY",
            "does not call the OpenAI provider",
            "report path must remain outside the repository",
            "not hosted deployment evidence",
        ],
    }


def _find_forbidden_secret_fields(value: object, *, prefix: str = "") -> list[str]:
    if isinstance(value, Mapping):
        found: list[str] = []
        for key, child_value in value.items():
            key_text = str(key)
            field_path = f"{prefix}.{key_text}" if prefix else key_text
            if key_text.lower() in SECRET_FIELD_NAMES:
                found.append(field_path)
            found.extend(_find_forbidden_secret_fields(child_value, prefix=field_path))
        return sorted(found)
    if isinstance(value, list):
        found = []
        for index, child_value in enumerate(value):
            field_path = f"{prefix}[{index}]" if prefix else f"[{index}]"
            found.extend(_find_forbidden_secret_fields(child_value, prefix=field_path))
        return sorted(found)
    return []


def _path_is_inside_repository(path: Path) -> bool:
    repo_root = Path(__file__).resolve().parents[4]
    try:
        path.resolve().relative_to(repo_root)
    except ValueError:
        return False
    return True


def _read_json_report(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("owner runtime smoke report must be a JSON object")
    return payload


def _print_json(payload: Mapping) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: Sequence[str] | None = None, env: Mapping[str, str] | None = None) -> int:
    environment = env if env is not None else os.environ
    args = list(argv if argv is not None else sys.argv[1:])
    if args == ["--print-owner-runtime-smoke-packet"]:
        _print_json(_owner_runtime_smoke_packet())
        return 0
    if args == ["--discover-owner-runtime-input"]:
        _print_json(_discover_owner_runtime_input(environment))
        return 0
    if args == ["--print-owner-runtime-smoke-report-contract"]:
        _print_json(_owner_runtime_smoke_report_contract())
        return 0
    if len(args) == 2 and args[0] == "--validate-owner-runtime-smoke-report":
        report_path = Path(args[1])
        report = _validate_owner_runtime_smoke_report(
            _read_json_report(report_path),
            report_path=report_path,
        )
        _print_json(report)
        return 0 if report["accepted_owner_runtime_smoke"] is True else 5
    _print_json({"error": "unsupported_command", "phase_marker": PHASE_MARKER})
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
