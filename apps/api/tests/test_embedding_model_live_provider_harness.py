import json

from app.services.embedding_model_live_provider_harness import main


def test_embedding_model_live_provider_harness_prints_owner_runtime_smoke_packet_without_secret(
    capsys,
):
    exit_code = main(["--print-owner-runtime-smoke-packet"], env={})

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert (
        payload["phase_marker"]
        == "embedding model live-provider owner-runtime smoke packet v0"
    )
    assert payload["packet_status"] == "ready_for_owner_input"
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["secret_logged"] is False
    assert payload["required_input"] == (
        "owner-provided OPENAI_API_KEY via environment outside the repository"
    )
    assert payload["required_runtime_env"] == {
        "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
        "OPENAI_API_KEY": "owner-provided-secret-not-in-command",
        "CI": "false",
    }
    assert payload["route"] == "POST /chunks/embedding-model-preview"
    assert payload["request_payload"] == {
        "text": "Enterprise demand growth reached 12% in Q1.",
        "allow_provider_call": True,
        "embedding_model": "text-embedding-3-small",
        "embedding_dimension": 1536,
        "encoding_format": "float",
    }
    assert payload["command_templates"]["powershell"].count("OPENAI_API_KEY") == 0
    assert "<owner-provided-openai-api-key>" not in json.dumps(payload, sort_keys=True)
    assert "sk-" not in json.dumps(payload, sort_keys=True)
    assert payload["success_criteria"] == {
        "http_status": 200,
        "embedding_status": "owner_runtime_provider_generated",
        "embedding_length": 1536,
        "provider_response_dimension_check": "passed",
        "usage_metadata_present": True,
        "secret_exposed": False,
        "persistence_boundary": "preview_only_not_persisted",
    }
    assert payload["failure_states"] == [
        "missing_openai_api_key",
        "opt_in_disabled",
        "ci_runtime",
        "provider_timeout",
        "provider_error",
        "dimension_mismatch",
    ]
    assert payload["non_claims"]["live_embedding_generation_proof"] is False


def test_embedding_model_live_provider_harness_rejects_unknown_command(capsys):
    exit_code = main(["--unknown"], env={})

    assert exit_code == 2
    payload = json.loads(capsys.readouterr().out)
    assert payload["error"] == "unsupported_command"
