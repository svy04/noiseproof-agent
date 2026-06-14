from __future__ import annotations

import json
import os
import sys
from collections.abc import Callable, Mapping, Sequence
from math import sqrt
from pathlib import Path
from typing import Any


ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.retrieval.qrels_eval import evaluate_qrels_backed_run
from packages.ingestion.retrieval.quality_fixture import (
    SemanticQualityFixture,
    load_semantic_quality_fixture,
)
from packages.ingestion.retrieval.representative_semantic_quality import (
    REQUIRED_INFORMATION_ROLES,
    REQUIRED_SOURCE_TYPES,
)


PACKET_PHASE_MARKER = "live embedding-backed domain qrels owner-runtime eval packet v0"
DISCOVERY_PHASE_MARKER = (
    "live embedding-backed domain qrels owner-runtime input discovery v0"
)
VALIDATOR_PHASE_MARKER = (
    "live embedding-backed domain qrels owner-runtime eval validator v0"
)
CONTRACT_PHASE_MARKER = (
    "live embedding-backed domain qrels owner-runtime eval report contract v0"
)
RUNNER_PHASE_MARKER = "live embedding-backed domain qrels owner-runtime runner v0"
RUN_SOURCE = "owner_runtime_openai_embedding_domain_qrels"
FIXTURE_ROOT_TEXT = "examples/representative-semantic-retrieval-quality"
BOUNDARY = "owner_runtime_live_embedding_domain_qrels_not_production_quality"
SECRET_FIELD_NAMES = {
    "api_key",
    "authorization",
    "openai_api_key",
    "provider_raw_response",
    "provider_secret",
    "secret",
    "token",
}
EXPECTED_REPORT_TOP_LEVEL_FIELDS = {
    "aggregate",
    "api_calls_attempted",
    "can_claim_production_semantic_quality",
    "chunk_count",
    "chunk_embedding_source",
    "coverage_status",
    "embedding_dimension",
    "embedding_model",
    "fixture_root",
    "openai_api_key_printed",
    "provider_call_count",
    "provider_response_dimension_check",
    "qrel_count",
    "qrels_evaluated",
    "query_count",
    "query_embedding_source",
    "run_source",
    "secret_committed_to_repo",
    "secret_exposed",
    "secret_logged",
    "unjudged_retrieved_count_at_k",
    "usage_metadata_present",
}
EXPECTED_AGGREGATE_FIELDS = {
    "Hit@k",
    "MRR@k",
    "Recall@k",
    "judged_coverage_at_k",
    "nDCG@k",
}


def evaluate_owner_runtime_domain_qrels_with_provider(
    *,
    fixture_root: Path | str,
    provider: Callable[[str], Mapping[str, Any]],
    embedding_model: str,
    embedding_dimension: int,
    k: int,
) -> dict[str, Any]:
    fixture = load_semantic_quality_fixture(fixture_root)
    query_responses = {
        query.query_id: provider(query.question)
        for query in fixture.queries
    }
    chunk_responses = {
        chunk.chunk_id: provider(chunk.text)
        for chunk in fixture.corpus
    }
    query_vectors = {
        query.query_id: _embedding_from_provider_response(
            query_responses[query.query_id],
            expected_dimension=embedding_dimension,
            item_id=query.query_id,
        )
        for query in fixture.queries
    }
    chunk_vectors = {
        chunk.chunk_id: _embedding_from_provider_response(
            chunk_responses[chunk.chunk_id],
            expected_dimension=embedding_dimension,
            item_id=chunk.chunk_id,
        )
        for chunk in fixture.corpus
    }
    run = _build_run_from_generated_embeddings(
        fixture=fixture,
        query_vectors=query_vectors,
        chunk_vectors=chunk_vectors,
        k=k,
    )
    evaluation = evaluate_qrels_backed_run(qrels=fixture.qrels, run=run, k=k)
    coverage = _fixture_coverage(fixture)
    claim_gate = _claim_gate(evaluation=evaluation)
    usage_metadata_present = all(
        bool(provider_response.get("usage"))
        for provider_response in [*query_responses.values(), *chunk_responses.values()]
    )

    return {
        **evaluation,
        "run": run,
        "run_source": RUN_SOURCE,
        "fixture_root": FIXTURE_ROOT_TEXT,
        "embedding_model": embedding_model,
        "embedding_dimension": embedding_dimension,
        "query_embedding_source": "owner_runtime_provider_generated",
        "chunk_embedding_source": "owner_runtime_provider_generated",
        "provider_call_count": len(fixture.queries) + len(fixture.corpus),
        "provider_response_dimension_check": "passed",
        "usage_metadata_present": usage_metadata_present,
        "qrels_evaluated": True,
        "fixture_coverage": coverage,
        "claim_gate": claim_gate,
        "boundary": BOUNDARY,
    }


def _owner_runtime_eval_packet() -> dict[str, object]:
    return {
        "phase_marker": PACKET_PHASE_MARKER,
        "packet_status": "ready_for_owner_input",
        "fixture_root": FIXTURE_ROOT_TEXT,
        "required_runtime_env": {
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER": "true",
            "OPENAI_API_KEY": "owner-provided-secret-not-in-command",
            "CI": "false",
        },
        "required_fixture": {
            "query_count": 6,
            "chunk_count": 12,
            "qrel_count": 24,
            "required_information_roles": REQUIRED_INFORMATION_ROLES,
            "required_source_types": REQUIRED_SOURCE_TYPES,
        },
        "manual_workflow": [
            "Generate query embeddings with the owner-runtime OpenAI provider.",
            "Generate chunk embeddings with the owner-runtime OpenAI provider.",
            "Rank chunks by cosine distance for each query.",
            "Evaluate the run against the representative domain qrels.",
            "Write a metadata-only report outside the repository.",
            "Validate the report with --validate-owner-runtime-eval-report.",
        ],
        "command_templates": {
            "discover_input": (
                "uv run python -m app.services.live_embedding_domain_qrels_harness "
                "--discover-owner-runtime-input"
            ),
            "validate_report": (
                "uv run python -m app.services.live_embedding_domain_qrels_harness "
                "--validate-owner-runtime-eval-report "
                "<runtime-report-path-outside-repo>"
            ),
        },
        "success_criteria": _accepted_owner_runtime_eval_report(),
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "non_claims": _non_claims(),
        "boundary": [
            "packet and validator only",
            "does not read or print OPENAI_API_KEY",
            "does not call the OpenAI provider",
            "does not generate embeddings by itself",
            "not live embedding generation proof",
            "not production semantic retrieval quality evidence",
        ],
    }


def _discover_owner_runtime_input(env: Mapping[str, str]) -> dict[str, object]:
    api_key_present = bool((env.get("OPENAI_API_KEY") or "").strip())
    opt_in_enabled = _env_flag_enabled(env.get("NOISEPROOF_ENABLE_OPENAI_PROVIDER"))
    ci_runtime = _env_flag_enabled(env.get("CI"))
    if not api_key_present:
        status = "missing_openai_api_key"
        next_action = (
            "configure OPENAI_API_KEY outside the repository and set "
            "NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime eval only"
        )
    elif ci_runtime:
        status = "blocked_by_ci"
        next_action = "rerun outside CI for owner-runtime eval only"
    elif not opt_in_enabled:
        status = "opt_in_disabled"
        next_action = "set NOISEPROOF_ENABLE_OPENAI_PROVIDER=true for owner-runtime eval only"
    else:
        status = "ready_for_owner_runtime_eval"
        next_action = (
            "run the owner-runtime domain qrels eval and write the metadata-only "
            "report outside the repository"
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
        "non_claims": _non_claims(),
    }


def _owner_runtime_eval_report_contract() -> dict[str, object]:
    accepted_report = _accepted_owner_runtime_eval_report()
    return {
        "phase_marker": CONTRACT_PHASE_MARKER,
        "contract_status": "ready_for_owner_runtime_eval_report",
        "required_top_level_fields": sorted(EXPECTED_REPORT_TOP_LEVEL_FIELDS),
        "required_aggregate_fields": sorted(EXPECTED_AGGREGATE_FIELDS),
        "accepted_report": accepted_report,
        "forbidden_secret_fields": sorted(SECRET_FIELD_NAMES),
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "non_claims": _non_claims(),
        "boundary": [
            "contract only",
            "does not read or print OPENAI_API_KEY",
            "does not call the OpenAI provider",
            "does not generate embeddings",
            "not live embedding generation proof",
        ],
    }


def _run_owner_runtime_eval(
    *,
    output_path: Path,
    env: Mapping[str, str],
    provider_client: object | None,
    fixture_root: Path | str = ROOT_DIR / FIXTURE_ROOT_TEXT,
    embedding_model: str = "text-embedding-3-small",
    embedding_dimension: int = 1536,
    k: int = 3,
) -> dict[str, object]:
    output_path_allowed = not _path_is_inside_repository(output_path)
    if not output_path_allowed:
        return {
            "phase_marker": RUNNER_PHASE_MARKER,
            "run_status": "output_path_rejected",
            "output_path_boundary": {
                "output_path_allowed": False,
                "required_location": "outside_repository",
            },
            "api_calls_attempted": False,
            "openai_api_key_printed": False,
            "secret_logged": False,
            "secret_committed_to_repo": False,
            "non_claims": _non_claims(),
        }

    readiness = _discover_owner_runtime_input(env)
    if readiness["owner_runtime_input_status"] != "ready_for_owner_runtime_eval":
        return {
            "phase_marker": RUNNER_PHASE_MARKER,
            "run_status": "input_not_ready",
            "owner_runtime_input_status": readiness["owner_runtime_input_status"],
            "next_action": readiness["next_action"],
            "api_calls_attempted": False,
            "openai_api_key_printed": False,
            "secret_logged": False,
            "secret_committed_to_repo": False,
            "non_claims": _non_claims(),
        }

    api_key = env.get("OPENAI_API_KEY", "")
    client = provider_client if provider_client is not None else _default_provider_client()

    def provider(text: str) -> Mapping[str, Any]:
        create_embedding = getattr(client, "create_embedding")
        return create_embedding(
            text=text,
            model=embedding_model,
            dimension=embedding_dimension,
            encoding_format="float",
            api_key=api_key,
        )

    evaluation = evaluate_owner_runtime_domain_qrels_with_provider(
        fixture_root=fixture_root,
        provider=provider,
        embedding_model=embedding_model,
        embedding_dimension=embedding_dimension,
        k=k,
    )
    report = _owner_runtime_eval_report_from_result(evaluation)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return {
        "phase_marker": RUNNER_PHASE_MARKER,
        "run_status": "report_written",
        "output_path_boundary": {
            "output_path_allowed": True,
            "required_location": "outside_repository",
        },
        "provider_call_count": report["provider_call_count"],
        "api_calls_attempted": True,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "non_claims": _non_claims(),
    }


def _owner_runtime_eval_report_from_result(
    evaluation: Mapping[str, object],
) -> dict[str, object]:
    fixture_coverage = evaluation.get("fixture_coverage")
    if not isinstance(fixture_coverage, Mapping):
        fixture_coverage = {}
    qrel_count = fixture_coverage.get("qrel_count")
    if qrel_count is None:
        qrel_count = sum(
            len(qrel)
            for qrel in load_semantic_quality_fixture(ROOT_DIR / FIXTURE_ROOT_TEXT).qrels.values()
        )
    return {
        "run_source": evaluation["run_source"],
        "fixture_root": evaluation["fixture_root"],
        "embedding_model": evaluation["embedding_model"],
        "embedding_dimension": evaluation["embedding_dimension"],
        "query_count": fixture_coverage.get("query_count", 0),
        "chunk_count": fixture_coverage.get("chunk_count", 0),
        "qrel_count": qrel_count,
        "coverage_status": fixture_coverage.get("coverage_status"),
        "query_embedding_source": evaluation["query_embedding_source"],
        "chunk_embedding_source": evaluation["chunk_embedding_source"],
        "provider_call_count": evaluation["provider_call_count"],
        "provider_response_dimension_check": evaluation["provider_response_dimension_check"],
        "usage_metadata_present": evaluation["usage_metadata_present"],
        "qrels_evaluated": evaluation["qrels_evaluated"],
        "aggregate": evaluation["aggregate"],
        "unjudged_retrieved_count_at_k": evaluation["unjudged_retrieved_count_at_k"],
        "can_claim_production_semantic_quality": False,
        "api_calls_attempted": True,
        "openai_api_key_printed": False,
        "secret_exposed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
    }


def _accepted_owner_runtime_eval_report() -> dict[str, object]:
    return {
        "run_source": RUN_SOURCE,
        "fixture_root": FIXTURE_ROOT_TEXT,
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


def _default_provider_client() -> object:
    from app.services.openai_embedding_provider import OpenAIEmbeddingProviderClient

    return OpenAIEmbeddingProviderClient()


def _validate_owner_runtime_eval_report(
    report: Mapping[str, object],
    *,
    report_path: Path | None = None,
) -> dict[str, object]:
    missing_or_failed_checks: list[str] = []
    forbidden_secret_fields = _find_forbidden_secret_fields(report)
    for field_path in forbidden_secret_fields:
        missing_or_failed_checks.append(f"forbidden secret field present: {field_path}")

    unexpected_fields = sorted(
        str(key)
        for key in report
        if str(key) not in EXPECTED_REPORT_TOP_LEVEL_FIELDS
    )
    for field_path in unexpected_fields:
        missing_or_failed_checks.append(f"unexpected field present: {field_path}")

    missing_fields = sorted(
        field for field in EXPECTED_REPORT_TOP_LEVEL_FIELDS if field not in report
    )
    for field_path in missing_fields:
        missing_or_failed_checks.append(f"missing field: {field_path}")

    report_path_allowed = (
        report_path is None or not _path_is_inside_repository(report_path)
    )
    if not report_path_allowed:
        missing_or_failed_checks.append("report path must be outside repository")

    expected_values = _accepted_owner_runtime_eval_report()
    for field, expected_value in expected_values.items():
        if field == "aggregate":
            _validate_aggregate(report.get("aggregate"), missing_or_failed_checks)
            continue
        if report.get(field) != expected_value:
            missing_or_failed_checks.append(f"{field} must be {_format_expected(expected_value)}")

    accepted = not missing_or_failed_checks
    return {
        "phase_marker": VALIDATOR_PHASE_MARKER,
        "validation_status": "accepted" if accepted else "rejected",
        "accepted_owner_runtime_eval": accepted,
        "missing_or_failed_checks": missing_or_failed_checks,
        "forbidden_secret_fields": forbidden_secret_fields,
        "unexpected_fields": unexpected_fields,
        "report_path_boundary": {
            "report_path_allowed": report_path_allowed,
            "required_location": "outside_repository",
        },
        "reported_run_source": report.get("run_source"),
        "reported_embedding_model": report.get("embedding_model"),
        "reported_query_count": report.get("query_count"),
        "reported_chunk_count": report.get("chunk_count"),
        "reported_qrel_count": report.get("qrel_count"),
        "api_calls_attempted": False,
        "openai_api_key_printed": False,
        "secret_logged": False,
        "secret_committed_to_repo": False,
        "non_claims": {
            **_non_claims(),
            "validator_makes_provider_call": False,
        },
        "boundary": [
            "validates owner-provided domain qrels eval metadata only",
            "does not read or print OPENAI_API_KEY",
            "does not call the OpenAI provider",
            "report path must remain outside the repository",
            "not production semantic retrieval quality evidence",
        ],
    }


def _build_run_from_generated_embeddings(
    *,
    fixture: SemanticQualityFixture,
    query_vectors: dict[str, list[float]],
    chunk_vectors: dict[str, list[float]],
    k: int,
) -> dict[str, list[str]]:
    safe_k = max(1, k)
    run: dict[str, list[str]] = {}
    for query in fixture.queries:
        query_vector = query_vectors[query.query_id]
        scored = [
            (
                _cosine_distance(query_vector, chunk_vectors[chunk.chunk_id]),
                index,
                chunk.chunk_id,
            )
            for index, chunk in enumerate(fixture.corpus)
        ]
        run[query.query_id] = [
            chunk_id for _distance, _index, chunk_id in sorted(scored)[:safe_k]
        ]
    return run


def _embedding_from_provider_response(
    response: Mapping[str, Any],
    *,
    expected_dimension: int,
    item_id: str,
) -> list[float]:
    embedding = response.get("embedding")
    if not isinstance(embedding, list):
        raise ValueError(f"{item_id} provider response missing embedding list")
    if len(embedding) != expected_dimension:
        raise ValueError(f"{item_id} provider response dimension mismatch")
    return [float(value) for value in embedding]


def _fixture_coverage(fixture: SemanticQualityFixture) -> dict[str, Any]:
    roles = sorted({role for chunk in fixture.corpus for role in chunk.information_roles})
    source_types = sorted({chunk.source_type for chunk in fixture.corpus})
    missing_roles = [role for role in REQUIRED_INFORMATION_ROLES if role not in roles]
    missing_source_types = [
        source_type for source_type in REQUIRED_SOURCE_TYPES if source_type not in source_types
    ]
    qrel_count = sum(len(qrel) for qrel in fixture.qrels.values())
    negative_qrel_count = sum(
        1
        for qrel in fixture.qrels.values()
        for relevance in qrel.values()
        if relevance <= 0
    )
    coverage_passed = (
        len(fixture.queries) == 6
        and len(fixture.corpus) == 12
        and qrel_count == 24
        and negative_qrel_count == 6
        and not missing_roles
        and not missing_source_types
    )
    return {
        "coverage_status": "passed" if coverage_passed else "blocked",
        "query_count": len(fixture.queries),
        "chunk_count": len(fixture.corpus),
        "qrel_count": qrel_count,
        "negative_qrel_count": negative_qrel_count,
        "missing_information_roles": missing_roles,
        "missing_source_types": missing_source_types,
    }


def _claim_gate(*, evaluation: Mapping[str, Any]) -> dict[str, Any]:
    base_gate = evaluation["claim_gate"]
    blocker_codes = list(base_gate.get("blocker_codes", []))
    blocker_codes.extend(
        [
            "owner_runtime_only",
            "not_public_benchmark",
            "not_production_benchmark",
        ]
    )
    return {
        **base_gate,
        "status": "blocked",
        "can_claim_semantic_quality": False,
        "can_claim_production_semantic_quality": False,
        "blocker_codes": list(dict.fromkeys(blocker_codes)),
        "summary": "live_embedding_domain_qrels_quality_claim_blocked",
        "boundary": BOUNDARY,
    }


def _validate_aggregate(value: object, missing_or_failed_checks: list[str]) -> None:
    if not isinstance(value, Mapping):
        missing_or_failed_checks.append("aggregate must be an object")
        return
    missing_aggregate_fields = sorted(
        field for field in EXPECTED_AGGREGATE_FIELDS if field not in value
    )
    for field in missing_aggregate_fields:
        missing_or_failed_checks.append(f"aggregate missing field: {field}")
    if value.get("judged_coverage_at_k") != 1.0:
        missing_or_failed_checks.append("aggregate.judged_coverage_at_k must be 1.0")


def _cosine_distance(query_vector: list[float], embedding: list[float]) -> float:
    if len(query_vector) != len(embedding):
        return 1.0
    query_norm = sqrt(sum(value * value for value in query_vector))
    embedding_norm = sqrt(sum(value * value for value in embedding))
    if query_norm == 0.0 or embedding_norm == 0.0:
        return 1.0
    similarity = sum(
        query_value * embedding_value
        for query_value, embedding_value in zip(query_vector, embedding)
    ) / (query_norm * embedding_norm)
    return 1.0 - similarity


def _env_flag_enabled(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _non_claims() -> dict[str, bool]:
    return {
        "live_embedding_generation_proof": False,
        "production_semantic_quality": False,
        "hosted_deployment_evidence": False,
        "external_reviewer_feedback": False,
        "product_complete": False,
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
    try:
        path.resolve().relative_to(ROOT_DIR)
    except ValueError:
        return False
    return True


def _read_json_report(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError("owner runtime domain qrels report must be a JSON object")
    return payload


def _parse_runner_args(args: Sequence[str]) -> tuple[Path | None, int]:
    output_path: Path | None = None
    k = 3
    index = 0
    while index < len(args):
        value = args[index]
        if value == "--output" and index + 1 < len(args):
            output_path = Path(args[index + 1])
            index += 2
            continue
        if value == "--k" and index + 1 < len(args):
            k = int(args[index + 1])
            index += 2
            continue
        raise ValueError(f"unsupported runner argument: {value}")
    return output_path, k


def _format_expected(value: object) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def _print_json(payload: Mapping[str, object]) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def main(
    argv: Sequence[str] | None = None,
    env: Mapping[str, str] | None = None,
    provider_client: object | None = None,
) -> int:
    environment = env if env is not None else os.environ
    args = list(argv if argv is not None else sys.argv[1:])
    if args == ["--print-owner-runtime-eval-packet"]:
        _print_json(_owner_runtime_eval_packet())
        return 0
    if args == ["--discover-owner-runtime-input"]:
        _print_json(_discover_owner_runtime_input(environment))
        return 0
    if args == ["--print-owner-runtime-eval-report-contract"]:
        _print_json(_owner_runtime_eval_report_contract())
        return 0
    if len(args) == 2 and args[0] == "--validate-owner-runtime-eval-report":
        report_path = Path(args[1])
        report = _validate_owner_runtime_eval_report(
            _read_json_report(report_path),
            report_path=report_path,
        )
        _print_json(report)
        return 0 if report["accepted_owner_runtime_eval"] is True else 5
    if args and args[0] == "--run-owner-runtime-eval":
        try:
            output_path, k = _parse_runner_args(args[1:])
        except ValueError as exc:
            _print_json({"error": str(exc), "phase_marker": RUNNER_PHASE_MARKER})
            return 2
        if output_path is None:
            _print_json(
                {
                    "error": "missing --output",
                    "phase_marker": RUNNER_PHASE_MARKER,
                    "api_calls_attempted": False,
                    "openai_api_key_printed": False,
                }
            )
            return 2
        result = _run_owner_runtime_eval(
            output_path=output_path,
            env=environment,
            provider_client=provider_client,
            k=k,
        )
        if result["run_status"] == "report_written":
            return 0
        _print_json(result)
        if result["run_status"] == "input_not_ready":
            return 4
        return 5
    _print_json({"error": "unsupported_command", "phase_marker": PACKET_PHASE_MARKER})
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
