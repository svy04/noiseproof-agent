from __future__ import annotations

from typing import Any

from packages.ingestion.retrieval.lexical import retrieve_candidates
from packages.ingestion.retrieval.qrels_eval import evaluate_qrels_backed_run
from packages.ingestion.retrieval.quality_fixture import SemanticQualityFixture
from packages.ingestion.types import ChunkOptions, RetrievalSource


RUN_SOURCE = "live_lexical_retrieve_candidates"
BOUNDARY = "live_lexical_qrels_baseline_not_semantic_quality_evidence"


def build_live_lexical_run_from_fixture(
    fixture: SemanticQualityFixture,
    *,
    strategy: str,
    k: int,
    options: ChunkOptions | None = None,
) -> dict[str, list[str]]:
    sources = _fixture_sources(fixture)
    run: dict[str, list[str]] = {}
    for query in fixture.queries:
        result = retrieve_candidates(
            query.question,
            sources,
            strategy=strategy,
            top_k=k,
            options=options or ChunkOptions(max_characters=500, overlap=0),
        )
        run[query.query_id] = _dedupe_source_ids(
            candidate.source_id for candidate in result.results
        )
    return run


def evaluate_live_lexical_qrels_baseline(
    fixture: SemanticQualityFixture,
    *,
    strategy: str,
    k: int,
    options: ChunkOptions | None = None,
) -> dict[str, Any]:
    run = build_live_lexical_run_from_fixture(
        fixture,
        strategy=strategy,
        k=k,
        options=options,
    )
    evaluation = evaluate_qrels_backed_run(qrels=fixture.qrels, run=run, k=k)
    qrels_boundary = evaluation["boundary"]

    claim_gate = dict(evaluation["claim_gate"])
    blocker_codes = list(claim_gate.get("blocker_codes", []))
    blocker_codes.append("live_lexical_baseline_boundary")
    claim_gate["blocker_codes"] = list(dict.fromkeys(blocker_codes))
    claim_gate["summary"] = "live_lexical_qrels_baseline_quality_claim_blocked"
    claim_gate["boundary"] = BOUNDARY

    return {
        **evaluation,
        "run": run,
        "run_source": RUN_SOURCE,
        "retrieval_strategy": strategy,
        "qrels_evaluation_boundary": qrels_boundary,
        "claim_gate": claim_gate,
        "boundary": BOUNDARY,
    }


def build_live_lexical_qrels_baseline_report(evaluation: dict[str, Any]) -> str:
    aggregate = evaluation["aggregate"]
    lines = [
        "# Live Lexical Qrels Baseline Eval",
        "",
        "Phase marker: live lexical qrels baseline v0.",
        "",
        "This report evaluates the existing local lexical retriever output against the tiny qrels fixture.",
        "",
        "This is not semantic retrieval quality evidence.",
        "",
        "## Run Source",
        "",
        f"- run_source: `{evaluation['run_source']}`",
        f"- retrieval_strategy: `{evaluation['retrieval_strategy']}`",
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
            "| Query | Retrieved by live lexical retriever | Missed relevant | Unjudged retrieved | Warnings |",
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
            "This gate blocks the live lexical baseline from being cited as semantic retrieval quality evidence.",
            "",
            f"- status: `{claim_gate['status']}`",
            f"- can_claim_semantic_quality: `{_format_bool(claim_gate['can_claim_semantic_quality'])}`",
            f"- summary: `{claim_gate['summary']}`",
            f"- blocker_codes: `{_format_list(claim_gate['blocker_codes'])}`",
            "",
            "## Boundary",
            "",
            "This is a live lexical baseline over a tiny local fixture.",
            "",
            "This is not semantic retrieval quality evidence.",
            "",
            "This is not embedding generation.",
            "",
            "This is not representative retrieval evaluation.",
            "",
            "This is not a benchmark result.",
            "",
            "This is not hosted deployment evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _fixture_sources(fixture: SemanticQualityFixture) -> list[RetrievalSource]:
    return [
        RetrievalSource(
            source_id=chunk.chunk_id,
            source_type=chunk.source_type,
            content=chunk.text,
            source_uri=f"fixture://{chunk.document_id}/{chunk.chunk_id}",
        )
        for chunk in fixture.corpus
    ]


def _dedupe_source_ids(source_ids) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for source_id in source_ids:
        if source_id in seen:
            continue
        seen.add(source_id)
        unique.append(source_id)
    return unique


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
