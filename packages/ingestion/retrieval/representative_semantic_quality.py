from __future__ import annotations

from typing import Any

from packages.ingestion.retrieval.live_semantic_qrels import (
    RANKING_BOUNDARY,
    STRATEGY,
    build_live_semantic_run_from_fixture,
)
from packages.ingestion.retrieval.qrels_eval import evaluate_qrels_backed_run
from packages.ingestion.retrieval.quality_fixture import SemanticQualityFixture


REQUIRED_INFORMATION_ROLES = [
    "direct_support",
    "contradiction",
    "quantitative_anchor",
    "timeline_anchor",
    "definition_anchor",
    "source_quality_check",
    "missing_data_signal",
    "scope_boundary",
    "user_intent_check",
]
REQUIRED_SOURCE_TYPES = ["csv", "html", "markdown", "memo", "pdf"]
RUN_SOURCE = "representative_caller_provided_live_semantic_cosine"
BOUNDARY = "representative_local_fixture_not_production_semantic_quality_evidence"


def evaluate_representative_live_semantic_quality(
    fixture: SemanticQualityFixture,
    *,
    k: int,
) -> dict[str, Any]:
    run = build_live_semantic_run_from_fixture(fixture, k=k)
    evaluation = evaluate_qrels_backed_run(qrels=fixture.qrels, run=run, k=k)
    qrels_boundary = evaluation["boundary"]
    coverage = _fixture_coverage(fixture)

    claim_gate = dict(evaluation["claim_gate"])
    blocker_codes = list(claim_gate.get("blocker_codes", []))
    blocker_codes.extend(
        [
            "caller_provided_embedding_boundary",
            "no_live_embedding_generation",
            "local_fixture_boundary",
            "not_production_benchmark",
        ]
    )
    if coverage["coverage_status"] != "passed":
        blocker_codes.append("representative_fixture_coverage_incomplete")
    claim_gate["blocker_codes"] = list(dict.fromkeys(blocker_codes))
    claim_gate["summary"] = "representative_live_semantic_quality_claim_blocked"
    claim_gate["boundary"] = BOUNDARY

    return {
        **evaluation,
        "run": run,
        "run_source": RUN_SOURCE,
        "retrieval_strategy": STRATEGY,
        "ranking_boundary": RANKING_BOUNDARY,
        "qrels_evaluation_boundary": qrels_boundary,
        "fixture_coverage": coverage,
        "claim_gate": claim_gate,
        "boundary": BOUNDARY,
    }


def build_representative_live_semantic_quality_report(
    evaluation: dict[str, Any],
) -> str:
    aggregate = evaluation["aggregate"]
    coverage = evaluation["fixture_coverage"]
    lines = [
        "# Representative Live Semantic Quality Eval",
        "",
        "Phase marker: representative live semantic quality eval v0.",
        "",
        "This report evaluates a local representative fixture for NoiseProof information roles and source types using caller-provided vectors.",
        "",
        "This is not production semantic retrieval quality evidence.",
        "",
        "## Run Source",
        "",
        f"- run_source: `{evaluation['run_source']}`",
        f"- retrieval_strategy: `{evaluation['retrieval_strategy']}`",
        f"- ranking_boundary: `{evaluation['ranking_boundary']}`",
        f"- qrels_boundary: `{evaluation['qrels_evaluation_boundary']}`",
        f"- boundary: `{evaluation['boundary']}`",
        "",
        "## Fixture Coverage",
        "",
        f"- coverage_status: `{coverage['coverage_status']}`",
        f"- role_coverage_ratio: `{_format_metric(coverage['role_coverage_ratio'])}`",
        f"- source_type_coverage_ratio: `{_format_metric(coverage['source_type_coverage_ratio'])}`",
        f"- query_count: `{coverage['query_count']}`",
        f"- chunk_count: `{coverage['chunk_count']}`",
        f"- qrel_count: `{coverage['qrel_count']}`",
        f"- negative_qrel_count: `{coverage['negative_qrel_count']}`",
        f"- required_information_roles: `{_format_list(coverage['required_information_roles'])}`",
        f"- required_source_types: `{_format_list(coverage['required_source_types'])}`",
        f"- missing_information_roles: `{_format_list(coverage['missing_information_roles'])}`",
        f"- missing_source_types: `{_format_list(coverage['missing_source_types'])}`",
        f"- missing_embedding_chunk_ids: `{_format_list(coverage['missing_embedding_chunk_ids'])}`",
        "",
        "## Aggregate Metrics",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for metric in [
        "Hit@k",
        "Recall@k",
        "MRR@k",
        "nDCG@k",
        "judged_coverage_at_k",
    ]:
        lines.append(f"| {metric} | {_format_metric(aggregate.get(metric))} |")
    lines.extend(
        [
            f"| retrieved_count_at_k | {evaluation['retrieved_count_at_k']} |",
            f"| unjudged_retrieved_count_at_k | {evaluation['unjudged_retrieved_count_at_k']} |",
            f"| judged_relevant_count | {evaluation['judged_relevant_count']} |",
            "",
            "## Per-query Diagnostics",
            "",
            "| Query | Retrieved | Missed relevant | Unjudged retrieved | Warnings |",
            "|---|---|---|---|---|",
        ]
    )
    for query_id, row in evaluation["per_query"].items():
        lines.append(
            "| "
            + " | ".join(
                [
                    query_id,
                    _format_list(row["retrieved_ids"]),
                    _format_list(row["missed_relevant_ids"]),
                    _format_list(row["unjudged_retrieved_ids"]),
                    _format_list(row["warnings"]),
                ]
            )
            + " |"
        )

    claim_gate = evaluation["claim_gate"]
    lines.extend(
        [
            "",
            "## Quality Claim Gate",
            "",
            "This gate blocks this local representative fixture from being cited as production semantic retrieval quality evidence.",
            "",
            f"- status: `{claim_gate['status']}`",
            f"- can_claim_semantic_quality: `{_format_bool(claim_gate['can_claim_semantic_quality'])}`",
            f"- summary: `{claim_gate['summary']}`",
            f"- blocker_codes: `{_format_list(claim_gate['blocker_codes'])}`",
            "",
            "## Boundary",
            "",
            "This is a local representative fixture for NoiseProof information roles and source types.",
            "",
            "This is not production semantic retrieval quality evidence.",
            "",
            "This is not live embedding generation.",
            "",
            "This is not a public benchmark result.",
            "",
            "This is not hosted deployment evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _fixture_coverage(fixture: SemanticQualityFixture) -> dict[str, Any]:
    roles = sorted({role for chunk in fixture.corpus for role in chunk.information_roles})
    source_types = sorted({chunk.source_type for chunk in fixture.corpus})
    missing_roles = [role for role in REQUIRED_INFORMATION_ROLES if role not in roles]
    missing_source_types = [
        source_type for source_type in REQUIRED_SOURCE_TYPES if source_type not in source_types
    ]
    missing_embedding_chunk_ids = [
        chunk.chunk_id for chunk in fixture.corpus if chunk.embedding is None
    ]
    qrel_count = sum(len(qrel) for qrel in fixture.qrels.values())
    negative_qrel_count = sum(
        1
        for qrel in fixture.qrels.values()
        for relevance in qrel.values()
        if relevance <= 0
    )
    coverage_passed = (
        len(fixture.queries) >= 6
        and len(fixture.corpus) >= 12
        and qrel_count >= 24
        and negative_qrel_count >= 6
        and not missing_roles
        and not missing_source_types
        and not missing_embedding_chunk_ids
    )
    return {
        "query_count": len(fixture.queries),
        "chunk_count": len(fixture.corpus),
        "qrel_count": qrel_count,
        "negative_qrel_count": negative_qrel_count,
        "required_information_roles": REQUIRED_INFORMATION_ROLES,
        "required_source_types": REQUIRED_SOURCE_TYPES,
        "present_information_roles": roles,
        "present_source_types": source_types,
        "missing_information_roles": missing_roles,
        "missing_source_types": missing_source_types,
        "missing_embedding_chunk_ids": missing_embedding_chunk_ids,
        "role_coverage_ratio": _ratio(
            len(REQUIRED_INFORMATION_ROLES) - len(missing_roles),
            len(REQUIRED_INFORMATION_ROLES),
        ),
        "source_type_coverage_ratio": _ratio(
            len(REQUIRED_SOURCE_TYPES) - len(missing_source_types),
            len(REQUIRED_SOURCE_TYPES),
        ),
        "coverage_status": "passed" if coverage_passed else "blocked",
    }


def _ratio(numerator: int, denominator: int) -> float:
    return round(numerator / max(denominator, 1), 4)


def _format_metric(value: Any) -> str:
    if value is None:
        return "n/a"
    if isinstance(value, float):
        text = f"{value:.4f}".rstrip("0").rstrip(".")
        return text or "0"
    return str(value)


def _format_list(value: Any) -> str:
    if not value:
        return "none"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def _format_bool(value: Any) -> str:
    return "true" if value else "false"
