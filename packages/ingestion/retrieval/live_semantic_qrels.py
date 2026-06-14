from __future__ import annotations

from math import sqrt
from typing import Any

from packages.ingestion.retrieval.qrels_eval import evaluate_qrels_backed_run
from packages.ingestion.retrieval.quality_fixture import SemanticQualityFixture


RUN_SOURCE = "caller_provided_live_semantic_cosine"
STRATEGY = "semantic-cosine"
RANKING_BOUNDARY = "exact_cosine_caller_provided_query_vector"
BOUNDARY = "caller_provided_live_semantic_qrels_baseline_not_quality_evidence"


def build_live_semantic_run_from_fixture(
    fixture: SemanticQualityFixture,
    *,
    k: int,
) -> dict[str, list[str]]:
    safe_k = max(1, k)
    candidates = [chunk for chunk in fixture.corpus if chunk.embedding is not None]
    run: dict[str, list[str]] = {}

    for query in fixture.queries:
        scored = [
            (
                _cosine_distance(query.query_embedding, chunk.embedding or []),
                index,
                chunk.chunk_id,
            )
            for index, chunk in enumerate(candidates)
        ]
        run[query.query_id] = [
            chunk_id for _distance, _index, chunk_id in sorted(scored)[:safe_k]
        ]

    return run


def evaluate_live_semantic_qrels_baseline(
    fixture: SemanticQualityFixture,
    *,
    k: int,
) -> dict[str, Any]:
    run = build_live_semantic_run_from_fixture(fixture, k=k)
    evaluation = evaluate_qrels_backed_run(qrels=fixture.qrels, run=run, k=k)
    qrels_boundary = evaluation["boundary"]
    missing_embedding_chunk_ids = [
        chunk.chunk_id for chunk in fixture.corpus if chunk.embedding is None
    ]

    claim_gate = dict(evaluation["claim_gate"])
    blocker_codes = list(claim_gate.get("blocker_codes", []))
    blocker_codes.extend(
        [
            "caller_provided_embedding_boundary",
            "no_live_embedding_generation",
            "tiny_fixture_boundary",
        ]
    )
    if missing_embedding_chunk_ids:
        blocker_codes.append("missing_chunk_embeddings")
    claim_gate["blocker_codes"] = list(dict.fromkeys(blocker_codes))
    claim_gate["summary"] = "live_semantic_qrels_baseline_quality_claim_blocked"
    claim_gate["boundary"] = BOUNDARY

    return {
        **evaluation,
        "run": run,
        "run_source": RUN_SOURCE,
        "retrieval_strategy": STRATEGY,
        "ranking_boundary": RANKING_BOUNDARY,
        "qrels_evaluation_boundary": qrels_boundary,
        "missing_embedding_chunk_ids": missing_embedding_chunk_ids,
        "claim_gate": claim_gate,
        "boundary": BOUNDARY,
    }


def build_live_semantic_qrels_baseline_report(evaluation: dict[str, Any]) -> str:
    aggregate = evaluation["aggregate"]
    lines = [
        "# Live Semantic Qrels Baseline Eval",
        "",
        "Phase marker: live semantic qrels baseline v0.",
        "",
        "This report evaluates caller-provided fixture vectors through the same exact cosine boundary used by the semantic retrieval preview/run path.",
        "",
        "This is not semantic retrieval quality evidence.",
        "",
        "## Run Source",
        "",
        f"- run_source: `{evaluation['run_source']}`",
        f"- retrieval_strategy: `{evaluation['retrieval_strategy']}`",
        f"- ranking_boundary: `{evaluation['ranking_boundary']}`",
        f"- qrels_boundary: `{evaluation['qrels_evaluation_boundary']}`",
        f"- boundary: `{evaluation['boundary']}`",
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
            "## Live Run",
            "",
            "| Query | Retrieved by caller-provided cosine | Missed relevant | Unjudged retrieved | Warnings |",
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
            "## Missing Embeddings",
            "",
            f"- missing_embedding_chunk_ids: `{_format_list(evaluation['missing_embedding_chunk_ids'])}`",
            "",
            "## Quality Claim Gate",
            "",
            "This gate blocks this caller-provided vector baseline from being cited as semantic retrieval quality evidence.",
            "",
            f"- status: `{claim_gate['status']}`",
            f"- can_claim_semantic_quality: `{_format_bool(claim_gate['can_claim_semantic_quality'])}`",
            f"- summary: `{claim_gate['summary']}`",
            f"- blocker_codes: `{_format_list(claim_gate['blocker_codes'])}`",
            "",
            "## Boundary",
            "",
            "This is a live semantic baseline over a tiny local fixture with caller-provided vectors.",
            "",
            "This is not semantic retrieval quality evidence.",
            "",
            "This is not live embedding generation.",
            "",
            "This is not representative retrieval evaluation.",
            "",
            "This is not a benchmark result.",
            "",
            "This is not hosted deployment evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


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
