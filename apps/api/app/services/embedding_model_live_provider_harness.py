from __future__ import annotations

import json
import sys
from collections.abc import Mapping, Sequence


PHASE_MARKER = "embedding model live-provider owner-runtime smoke packet v0"


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


def _print_json(payload: Mapping) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(argv: Sequence[str] | None = None, env: Mapping[str, str] | None = None) -> int:
    _ = env
    args = list(argv if argv is not None else sys.argv[1:])
    if args == ["--print-owner-runtime-smoke-packet"]:
        _print_json(_owner_runtime_smoke_packet())
        return 0
    _print_json({"error": "unsupported_command", "phase_marker": PHASE_MARKER})
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
