import json
from pathlib import Path

from app.services.embedding_model_live_provider_harness import main


REPO_ROOT = Path(__file__).resolve().parents[3]


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
    assert payload["post_run_validation_command"] == (
        "uv run python -m app.services.embedding_model_live_provider_harness "
        "--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>"
    )
    assert payload["post_run_validation_commands"] == {
        "posix": (
            "uv run python -m app.services.embedding_model_live_provider_harness "
            "--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>"
        ),
        "powershell": (
            "uv run python -m app.services.embedding_model_live_provider_harness "
            "--validate-owner-runtime-smoke-report '<runtime-report-path-outside-repo>'"
        ),
    }
    assert payload["post_run_validation_success_criteria"] == {
        "validation_status": "accepted",
        "accepted_owner_runtime_smoke": True,
        "missing_or_failed_checks": [],
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


def test_embedding_model_live_provider_harness_prints_owner_runtime_smoke_report_contract_without_secret(
    capsys,
):
    exit_code = main(["--print-owner-runtime-smoke-report-contract"], env={})

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == (
        "embedding model live-provider owner-runtime smoke report contract v0"
    )
    assert payload["contract_status"] == "ready_for_owner_runtime_report"
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_logged"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["validator_command"] == (
        "uv run python -m app.services.embedding_model_live_provider_harness "
        "--validate-owner-runtime-smoke-report path/to/owner-runtime-smoke-report.json"
    )
    assert payload["accepted_report"] == {
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
    assert payload["required_top_level_fields"] == sorted(
        payload["accepted_report"].keys()
    )
    assert "openai_api_key" in payload["forbidden_secret_fields"]
    assert "api_key" in payload["forbidden_secret_fields"]
    assert payload["accepted_validator_output"] == {
        "validation_status": "accepted",
        "accepted_owner_runtime_smoke": True,
        "missing_or_failed_checks": [],
    }
    assert payload["rejected_validator_output"] == {
        "validation_status": "rejected",
        "accepted_owner_runtime_smoke": False,
        "missing_or_failed_checks": "non-empty",
    }
    assert payload["non_claims"]["live_embedding_generation_proof"] is False
    assert payload["non_claims"]["external_reviewer_feedback"] is False
    assert "sk-" not in json.dumps(payload, sort_keys=True)


def test_embedding_model_live_provider_harness_prints_owner_runtime_smoke_report_schema_without_secret(
    capsys,
):
    exit_code = main(["--print-owner-runtime-smoke-report-schema"], env={})

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == (
        "embedding model live-provider owner-runtime smoke report schema v0"
    )
    assert payload["schema_status"] == "ready_for_owner_runtime_report"
    schema = payload["json_schema"]
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["title"] == "NoiseProof embedding owner runtime smoke report"
    assert schema["type"] == "object"
    assert schema["additionalProperties"] is False
    assert schema["required"] == sorted(
        [
            "route",
            "http_status",
            "embedding_status",
            "embedding_model",
            "embedding_length",
            "provider_response_dimension_check",
            "usage_metadata_present",
            "secret_exposed",
            "persistence_boundary",
            "api_calls_attempted",
            "openai_api_key_printed",
            "secret_logged",
            "secret_committed_to_repo",
        ]
    )
    properties = schema["properties"]
    assert properties["route"] == {"const": "POST /chunks/embedding-model-preview"}
    assert properties["http_status"] == {"const": 200}
    assert properties["embedding_status"] == {
        "const": "owner_runtime_provider_generated"
    }
    assert properties["embedding_model"] == {"const": "text-embedding-3-small"}
    assert properties["embedding_length"] == {"const": 1536}
    assert properties["provider_response_dimension_check"] == {"const": "passed"}
    assert properties["usage_metadata_present"] == {"const": True}
    assert properties["secret_exposed"] == {"const": False}
    assert properties["persistence_boundary"] == {
        "const": "preview_only_not_persisted"
    }
    assert properties["api_calls_attempted"] == {"const": True}
    assert properties["openai_api_key_printed"] == {"const": False}
    assert properties["secret_logged"] == {"const": False}
    assert properties["secret_committed_to_repo"] == {"const": False}
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_logged"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["non_claims"]["live_embedding_generation_proof"] is False
    assert "sk-" not in json.dumps(payload, sort_keys=True)


def test_embedding_model_live_provider_harness_checks_report_contract_alignment_without_secret(
    capsys,
):
    exit_code = main(
        ["--check-owner-runtime-smoke-report-contract-alignment"],
        env={},
    )

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == (
        "embedding model live-provider owner-runtime smoke report contract alignment v0"
    )
    assert payload["alignment_status"] == "aligned"
    assert payload["missing_or_failed_checks"] == []
    assert payload["checks"] == {
        "contract_fields_match_validator_expected_fields": True,
        "schema_required_fields_match_contract": True,
        "schema_properties_match_contract_constants": True,
        "schema_additional_properties_closed": True,
        "accepted_report_passes_validator": True,
        "accepted_report_contains_no_forbidden_secret_fields": True,
        "forbidden_secret_fields_match_validator": True,
    }
    assert payload["accepted_report_field_count"] == 13
    assert payload["schema_required_field_count"] == 13
    assert payload["validator_expected_field_count"] == 13
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_logged"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["non_claims"]["live_embedding_generation_proof"] is False
    assert payload["non_claims"]["validator_makes_provider_call"] is False
    assert "sk-" not in json.dumps(payload, sort_keys=True)


def test_embedding_model_live_provider_harness_rejects_unknown_command(capsys):
    exit_code = main(["--unknown"], env={})

    assert exit_code == 2
    payload = json.loads(capsys.readouterr().out)
    assert payload["error"] == "unsupported_command"


def test_embedding_model_live_provider_harness_validates_owner_runtime_smoke_metadata_report(
    capsys, tmp_path
):
    report_path = tmp_path / "embedding-provider-owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
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
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["phase_marker"] == (
        "embedding model live-provider owner-runtime smoke validator v0"
    )
    assert payload["validation_status"] == "accepted"
    assert payload["accepted_owner_runtime_smoke"] is True
    assert payload["missing_or_failed_checks"] == []
    assert payload["reported_embedding_status"] == "owner_runtime_provider_generated"
    assert payload["reported_embedding_length"] == 1536
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_logged"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["non_claims"]["validator_makes_provider_call"] is False


def test_embedding_model_live_provider_harness_rejects_secret_leak_fields_in_smoke_report(
    capsys, tmp_path
):
    report_path = tmp_path / "embedding-provider-owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
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
                "openai_api_key": "sk-test-secret",
                "provider_raw_response": {
                    "authorization": "Bearer sk-test-secret",
                },
            }
        ),
        encoding="utf-8",
    )

    exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])

    assert exit_code == 5
    output = capsys.readouterr().out
    payload = json.loads(output)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert payload["forbidden_secret_fields"] == [
        "openai_api_key",
        "provider_raw_response.authorization",
    ]
    assert "forbidden secret field present: openai_api_key" in payload[
        "missing_or_failed_checks"
    ]
    assert "forbidden secret field present: provider_raw_response.authorization" in payload[
        "missing_or_failed_checks"
    ]
    assert "sk-test-secret" not in output
    assert "sk-" not in output


def test_embedding_model_live_provider_harness_rejects_report_path_inside_repository(
    capsys,
):
    report_path = REPO_ROOT / ".tmp-embedding-provider-owner-runtime-smoke-report.json"
    report_path.write_text(
        json.dumps(
            {
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
        ),
        encoding="utf-8",
    )
    try:
        exit_code = main(["--validate-owner-runtime-smoke-report", str(report_path)])
    finally:
        report_path.unlink(missing_ok=True)

    assert exit_code == 5
    payload = json.loads(capsys.readouterr().out)
    assert payload["validation_status"] == "rejected"
    assert payload["accepted_owner_runtime_smoke"] is False
    assert payload["report_path_boundary"] == {
        "report_path_allowed": False,
        "required_location": "outside_repository",
    }
    assert "report path must be outside repository" in payload[
        "missing_or_failed_checks"
    ]
