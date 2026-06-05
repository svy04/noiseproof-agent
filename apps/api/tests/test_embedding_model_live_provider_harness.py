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


def test_embedding_model_live_provider_harness_discovers_missing_owner_runtime_input_without_secret(
    capsys,
):
    exit_code = main(["--discover-owner-runtime-input"], env={})

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == (
        "embedding model live-provider owner-runtime input discovery v0"
    )
    assert payload["owner_runtime_input_status"] == "missing_openai_api_key"
    assert payload["openai_api_key_present"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["opt_in_enabled"] is False
    assert payload["ci_runtime"] is False
    assert payload["api_calls_attempted"] is False
    assert payload["secret_logged"] is False
    assert payload["next_action"] == (
        "configure OPENAI_API_KEY outside the repository and set "
        "NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime smoke only"
    )


def test_embedding_model_live_provider_harness_discovers_opt_in_disabled_without_printing_key(
    capsys,
):
    exit_code = main(
        ["--discover-owner-runtime-input"],
        env={
            "OPENAI_API_KEY": "sk-test-secret",
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "false",
            "CI": "false",
        },
    )

    assert exit_code == 0
    output = capsys.readouterr().out
    payload = json.loads(output)
    assert payload["owner_runtime_input_status"] == "opt_in_disabled"
    assert payload["openai_api_key_present"] is True
    assert payload["openai_api_key_printed"] is False
    assert payload["opt_in_enabled"] is False
    assert payload["ci_runtime"] is False
    assert payload["api_calls_attempted"] is False
    assert "sk-test-secret" not in output
    assert "sk-" not in output


def test_embedding_model_live_provider_harness_discovers_ci_runtime_as_blocked_without_printing_key(
    capsys,
):
    exit_code = main(
        ["--discover-owner-runtime-input"],
        env={
            "OPENAI_API_KEY": "sk-test-secret",
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
            "CI": "true",
        },
    )

    assert exit_code == 0
    output = capsys.readouterr().out
    payload = json.loads(output)
    assert payload["owner_runtime_input_status"] == "blocked_by_ci"
    assert payload["openai_api_key_present"] is True
    assert payload["openai_api_key_printed"] is False
    assert payload["opt_in_enabled"] is True
    assert payload["ci_runtime"] is True
    assert payload["api_calls_attempted"] is False
    assert "sk-test-secret" not in output


def test_embedding_model_live_provider_harness_discovers_ready_owner_runtime_without_printing_key(
    capsys,
):
    exit_code = main(
        ["--discover-owner-runtime-input"],
        env={
            "OPENAI_API_KEY": "sk-test-secret",
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
            "CI": "false",
        },
    )

    assert exit_code == 0
    output = capsys.readouterr().out
    payload = json.loads(output)
    assert payload["owner_runtime_input_status"] == "ready_for_owner_runtime_smoke"
    assert payload["openai_api_key_present"] is True
    assert payload["openai_api_key_printed"] is False
    assert payload["opt_in_enabled"] is True
    assert payload["ci_runtime"] is False
    assert payload["api_calls_attempted"] is False
    assert payload["next_action"] == (
        "run the manual owner-runtime smoke packet outside CI and write any "
        "runtime report outside the repository"
    )
    assert "sk-test-secret" not in output
    assert "sk-" not in output


def test_embedding_model_live_provider_harness_rejects_unknown_command(capsys):
    exit_code = main(["--unknown"], env={})

    assert exit_code == 2
    payload = json.loads(capsys.readouterr().out)
    assert payload["error"] == "unsupported_command"
