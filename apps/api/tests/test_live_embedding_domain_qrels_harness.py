import json
from pathlib import Path
import subprocess
import sys

from app.services.live_embedding_domain_qrels_harness import main


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "examples/representative-semantic-retrieval-quality"


def _run_harness(*args, env=None):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.live_embedding_domain_qrels_harness",
            *args,
        ],
        cwd=REPO_ROOT / "apps/api",
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def _load_stdout_json(result):
    assert result.stdout, result.stderr
    return json.loads(result.stdout)


def test_live_embedding_domain_qrels_packet_is_no_secret_no_call_owner_runtime_contract():
    result = _run_harness("--print-owner-runtime-eval-packet")

    assert result.returncode == 0, result.stderr
    payload = _load_stdout_json(result)

    assert payload["phase_marker"] == (
        "live embedding-backed domain qrels owner-runtime eval packet v0"
    )
    assert payload["packet_status"] == "ready_for_owner_input"
    assert payload["fixture_root"] == "examples/representative-semantic-retrieval-quality"
    assert payload["required_runtime_env"] == {
        "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
        "OPENAI_API_KEY": "owner-provided-secret-not-in-command",
        "CI": "false",
    }
    assert payload["success_criteria"]["run_source"] == (
        "owner_runtime_openai_embedding_domain_qrels"
    )
    assert payload["success_criteria"]["query_count"] == 6
    assert payload["success_criteria"]["chunk_count"] == 12
    assert payload["success_criteria"]["qrel_count"] == 24
    assert payload["success_criteria"]["coverage_status"] == "passed"
    assert payload["success_criteria"]["query_embedding_source"] == (
        "owner_runtime_provider_generated"
    )
    assert payload["success_criteria"]["chunk_embedding_source"] == (
        "owner_runtime_provider_generated"
    )
    assert payload["success_criteria"]["can_claim_production_semantic_quality"] is False
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["secret_logged"] is False
    assert payload["secret_committed_to_repo"] is False
    assert payload["non_claims"]["live_embedding_generation_proof"] is False
    assert payload["non_claims"]["production_semantic_quality"] is False


def test_live_embedding_domain_qrels_discovery_reports_missing_key_without_secret():
    result = _run_harness(
        "--discover-owner-runtime-input",
        env={"NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true", "CI": "false"},
    )

    assert result.returncode == 0, result.stderr
    payload = _load_stdout_json(result)

    assert payload["phase_marker"] == (
        "live embedding-backed domain qrels owner-runtime input discovery v0"
    )
    assert payload["owner_runtime_input_status"] == "missing_openai_api_key"
    assert payload["openai_api_key_present"] is False
    assert payload["openai_api_key_printed"] is False
    assert payload["opt_in_enabled"] is True
    assert payload["ci_runtime"] is False
    assert payload["api_calls_attempted"] is False
    assert payload["non_claims"]["live_embedding_generation_proof"] is False


def test_live_embedding_domain_qrels_core_eval_accepts_injected_provider_without_claiming_production_quality():
    from app.services.live_embedding_domain_qrels_harness import (
        evaluate_owner_runtime_domain_qrels_with_provider,
    )

    calls = []

    def fake_provider(text: str):
        calls.append(text)
        lowered = text.lower()
        if "buy" in lowered or "financial advice" in lowered:
            vector = [0.0, 0.0, 0.0, 0.9, 0.4]
        elif "missing" in lowered or "strong conclusion" in lowered:
            vector = [0.0, 0.0, 0.0, 1.0, 0.0]
        elif "definition" in lowered or "timeline" in lowered or "filing" in lowered:
            vector = [0.0, 0.0, 1.0, 0.0, 0.0]
        elif "quality" in lowered or "third-party" in lowered:
            vector = [0.0, 0.8, 0.4, 0.0, 0.0]
        elif "contradict" in lowered or "promotion" in lowered or "renewals" in lowered:
            vector = [0.0, 1.0, 0.0, 0.0, 0.0]
        elif "demand" in lowered or "revenue" in lowered:
            vector = [1.0, 0.0, 0.0, 0.0, 0.0]
        else:
            vector = [0.2, 0.2, 0.2, 0.2, 0.2]
        return {
            "embedding": vector,
            "model": "fake-domain-qrels-provider",
            "usage": {"total_tokens": 3},
        }

    result = evaluate_owner_runtime_domain_qrels_with_provider(
        fixture_root=FIXTURE_ROOT,
        provider=fake_provider,
        embedding_model="text-embedding-3-small",
        embedding_dimension=5,
        k=3,
    )

    assert result["run_source"] == "owner_runtime_openai_embedding_domain_qrels"
    assert result["provider_call_count"] == 18
    assert len(calls) == 18
    assert result["query_embedding_source"] == "owner_runtime_provider_generated"
    assert result["chunk_embedding_source"] == "owner_runtime_provider_generated"
    assert result["fixture_coverage"]["coverage_status"] == "passed"
    assert result["aggregate"]["judged_coverage_at_k"] == 1.0
    assert result["claim_gate"]["status"] == "blocked"
    assert result["claim_gate"]["can_claim_production_semantic_quality"] is False
    assert "not_public_benchmark" in result["claim_gate"]["blocker_codes"]


def test_live_embedding_domain_qrels_validator_accepts_metadata_only_report_outside_repo(
    tmp_path,
):
    report_path = tmp_path / "owner-runtime-domain-qrels-report.json"
    report_path.write_text(
        json.dumps(
            {
                "run_source": "owner_runtime_openai_embedding_domain_qrels",
                "fixture_root": "examples/representative-semantic-retrieval-quality",
                "embedding_model": "text-embedding-3-small",
                "embedding_dimension": 1536,
                "query_count": 6,
                "chunk_count": 12,
                "qrel_count": 24,
                "coverage_status": "passed",
                "query_embedding_source": "owner_runtime_provider_generated",
                "chunk_embedding_source": "owner_runtime_provider_generated",
                "provider_call_count": 18,
                "provider_response_dimension_check": "passed",
                "usage_metadata_present": True,
                "qrels_evaluated": True,
                "aggregate": {
                    "Hit@k": 1.0,
                    "Recall@k": 1.0,
                    "MRR@k": 1.0,
                    "nDCG@k": 0.99,
                    "judged_coverage_at_k": 1.0,
                },
                "unjudged_retrieved_count_at_k": 0,
                "can_claim_production_semantic_quality": False,
                "api_calls_attempted": True,
                "openai_api_key_printed": False,
                "secret_exposed": False,
                "secret_logged": False,
                "secret_committed_to_repo": False,
            }
        ),
        encoding="utf-8",
    )

    result = _run_harness("--validate-owner-runtime-eval-report", str(report_path))

    assert result.returncode == 0, result.stderr
    payload = _load_stdout_json(result)

    assert payload["phase_marker"] == (
        "live embedding-backed domain qrels owner-runtime eval validator v0"
    )
    assert payload["validation_status"] == "accepted"
    assert payload["accepted_owner_runtime_eval"] is True
    assert payload["missing_or_failed_checks"] == []
    assert payload["openai_api_key_printed"] is False
    assert payload["non_claims"]["validator_makes_provider_call"] is False
    assert payload["non_claims"]["production_semantic_quality"] is False


def test_live_embedding_domain_qrels_runner_blocks_missing_key_without_provider_call(
    capsys,
    tmp_path,
):
    calls = []
    report_path = tmp_path / "owner-runtime-domain-qrels-report.json"

    class FakeProviderClient:
        def create_embedding(self, **kwargs):
            calls.append(kwargs)
            return {"embedding": [0.0] * 1536, "usage": {"total_tokens": 1}}

    exit_code = main(
        ["--run-owner-runtime-eval", "--output", str(report_path)],
        env={"NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true", "CI": "false"},
        provider_client=FakeProviderClient(),
    )

    payload = json.loads(capsys.readouterr().out)
    assert exit_code == 4
    assert payload["phase_marker"] == (
        "live embedding-backed domain qrels owner-runtime runner v0"
    )
    assert payload["run_status"] == "input_not_ready"
    assert payload["owner_runtime_input_status"] == "missing_openai_api_key"
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert calls == []
    assert report_path.exists() is False


def test_live_embedding_domain_qrels_runner_rejects_output_inside_repository_before_provider_call(
    capsys,
):
    calls = []
    report_path = REPO_ROOT / ".tmp-owner-runtime-domain-qrels-report.json"

    class FakeProviderClient:
        def create_embedding(self, **kwargs):
            calls.append(kwargs)
            return {"embedding": [0.0] * 1536, "usage": {"total_tokens": 1}}

    try:
        exit_code = main(
            ["--run-owner-runtime-eval", "--output", str(report_path)],
            env={
                "OPENAI_API_KEY": "sk-test-secret",
                "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
                "CI": "false",
            },
            provider_client=FakeProviderClient(),
        )
    finally:
        report_path.unlink(missing_ok=True)

    output = capsys.readouterr().out
    payload = json.loads(output)
    assert exit_code == 5
    assert payload["phase_marker"] == (
        "live embedding-backed domain qrels owner-runtime runner v0"
    )
    assert payload["run_status"] == "output_path_rejected"
    assert payload["output_path_boundary"] == {
        "output_path_allowed": False,
        "required_location": "outside_repository",
    }
    assert payload["api_calls_attempted"] is False
    assert payload["openai_api_key_printed"] is False
    assert "sk-test-secret" not in output
    assert "sk-" not in output
    assert calls == []


def test_live_embedding_domain_qrels_runner_writes_metadata_report_with_fake_provider(
    capsys,
    tmp_path,
):
    report_path = tmp_path / "owner-runtime-domain-qrels-report.json"
    query_vectors = {
        item["question"]: item["query_embedding"]
        for item in json.loads((FIXTURE_ROOT / "queries.json").read_text())
    }
    chunk_vectors = {
        item["text"]: item["embedding"]
        for item in json.loads((FIXTURE_ROOT / "corpus.json").read_text())
    }
    calls = []

    class FakeProviderClient:
        def create_embedding(self, **kwargs):
            calls.append(kwargs)
            text = kwargs["text"]
            vector = query_vectors[text] if text in query_vectors else chunk_vectors[text]
            return {
                "embedding": vector + ([0.0] * (1536 - len(vector))),
                "model": kwargs["model"],
                "usage": {"total_tokens": 5},
            }

    exit_code = main(
        ["--run-owner-runtime-eval", "--output", str(report_path), "--k", "3"],
        env={
            "OPENAI_API_KEY": "sk-test-secret",
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
            "CI": "false",
        },
        provider_client=FakeProviderClient(),
    )

    assert exit_code == 0
    assert capsys.readouterr().out == ""
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["run_source"] == "owner_runtime_openai_embedding_domain_qrels"
    assert report["fixture_root"] == "examples/representative-semantic-retrieval-quality"
    assert report["query_count"] == 6
    assert report["chunk_count"] == 12
    assert report["qrel_count"] == 24
    assert report["provider_call_count"] == 18
    assert report["api_calls_attempted"] is True
    assert report["query_embedding_source"] == "owner_runtime_provider_generated"
    assert report["chunk_embedding_source"] == "owner_runtime_provider_generated"
    assert report["provider_response_dimension_check"] == "passed"
    assert report["usage_metadata_present"] is True
    assert report["qrels_evaluated"] is True
    assert report["can_claim_production_semantic_quality"] is False
    assert report["openai_api_key_printed"] is False
    assert report["secret_exposed"] is False
    assert report["secret_logged"] is False
    assert report["secret_committed_to_repo"] is False
    assert "run" not in report
    assert "provider_raw_response" not in report
    assert "sk-" not in json.dumps(report, sort_keys=True)
    assert len(calls) == 18
    assert all(call["api_key"] == "sk-test-secret" for call in calls)

    validate_exit_code = main(
        ["--validate-owner-runtime-eval-report", str(report_path)]
    )
    assert validate_exit_code == 0
    validation = json.loads(capsys.readouterr().out)
    assert validation["validation_status"] == "accepted"
    assert validation["accepted_owner_runtime_eval"] is True
