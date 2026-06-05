from __future__ import annotations

import json
import os
import sys
from collections.abc import Mapping, Sequence


PHASE_MARKER = "embedding model live-provider owner-runtime smoke packet v0"
DISCOVERY_PHASE_MARKER = "embedding model live-provider owner-runtime input discovery v0"


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
    _print_json({"error": "unsupported_command", "phase_marker": PHASE_MARKER})
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
