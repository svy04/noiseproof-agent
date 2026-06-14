from __future__ import annotations

from math import log2
from pathlib import Path
from typing import Any


QREL_FORMAT = "trec_qrels_qid_iter_docno_relevance"
RUN_FORMAT = "trec_run_qid_Q0_docno_rank_score_runid"
BOUNDARY = "qrels_backed_toy_eval_not_semantic_quality_evidence"


def parse_qrels_file(path: Path | str) -> dict[str, dict[str, int]]:
    qrels: dict[str, dict[str, int]] = {}
    for line_number, raw_line in enumerate(
        Path(path).read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 4:
            raise ValueError(f"Invalid qrels line {line_number}: expected 4 fields")
        query_id, _iteration, doc_id, relevance = parts
        try:
            relevance_score = int(relevance)
        except ValueError as exc:
            raise ValueError(
                f"Invalid qrels line {line_number}: relevance must be an integer"
            ) from exc
        if relevance_score < -1:
            raise ValueError(
                f"Invalid qrels line {line_number}: relevance must be -1 or greater"
            )
        qrels.setdefault(query_id, {})[doc_id] = relevance_score
    return qrels


def parse_trec_run_file(path: Path | str) -> dict[str, list[str]]:
    rows: dict[str, list[tuple[int, float, str]]] = {}
    for line_number, raw_line in enumerate(
        Path(path).read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) != 6:
            raise ValueError(f"Invalid run line {line_number}: expected 6 fields")
        query_id, q0_marker, doc_id, rank, score, _run_id = parts
        if q0_marker != "Q0":
            raise ValueError(f"Invalid run line {line_number}: second field must be Q0")
        try:
            rank_value = int(rank)
            score_value = float(score)
        except ValueError as exc:
            raise ValueError(
                f"Invalid run line {line_number}: rank and score must be numeric"
            ) from exc
        rows.setdefault(query_id, []).append((rank_value, -score_value, doc_id))
    return {
        query_id: [doc_id for _rank, _score, doc_id in sorted(query_rows)]
        for query_id, query_rows in rows.items()
    }


def evaluate_qrels_backed_run(
    *,
    qrels: dict[str, dict[str, int]],
    run: dict[str, list[str]],
    k: int = 10,
) -> dict[str, Any]:
    safe_k = max(1, k)
    per_query: dict[str, dict[str, Any]] = {}
    retrieved_count = 0
    unjudged_count = 0
    judged_relevant_count = sum(
        1 for query_qrels in qrels.values() for relevance in query_qrels.values() if relevance > 0
    )

    for query_id in sorted(qrels):
        query_qrels = qrels[query_id]
        relevant_ids = [
            doc_id for doc_id, relevance in query_qrels.items() if relevance > 0
        ]
        retrieved_ids = run.get(query_id, [])[:safe_k]
        retrieved_count += len(retrieved_ids)

        retrieved_relevant = [
            doc_id for doc_id in retrieved_ids if query_qrels.get(doc_id, 0) > 0
        ]
        missed_relevant = [doc_id for doc_id in relevant_ids if doc_id not in retrieved_ids]
        unjudged_retrieved = [doc_id for doc_id in retrieved_ids if doc_id not in query_qrels]
        unjudged_count += len(unjudged_retrieved)
        first_relevant_rank = _first_relevant_rank(retrieved_ids, query_qrels)
        warnings = _query_warnings(
            retrieved_ids=retrieved_ids,
            retrieved_relevant=retrieved_relevant,
            missed_relevant=missed_relevant,
            unjudged_retrieved=unjudged_retrieved,
        )

        per_query[query_id] = {
            "retrieved_ids": retrieved_ids,
            "retrieved_relevant_ids": retrieved_relevant,
            "missed_relevant_ids": missed_relevant,
            "unjudged_retrieved_ids": unjudged_retrieved,
            "Hit@k": 1.0 if retrieved_relevant else 0.0,
            "Recall@k": _round(len(set(retrieved_relevant)) / max(len(relevant_ids), 1)),
            "MRR@k": _round(1.0 / first_relevant_rank) if first_relevant_rank else 0.0,
            "nDCG@k": _round(_ndcg(retrieved_ids, query_qrels, safe_k)),
            "warnings": warnings,
        }

    aggregate = _aggregate(per_query)
    aggregate["judged_coverage_at_k"] = _round(
        (retrieved_count - unjudged_count) / max(retrieved_count, 1)
    )
    claim_gate = _claim_gate(
        aggregate=aggregate,
        unjudged_count=unjudged_count,
        per_query=per_query,
    )

    return {
        "qrel_format": QREL_FORMAT,
        "run_format": RUN_FORMAT,
        "query_count": len(qrels),
        "judged_relevant_count": judged_relevant_count,
        "retrieved_count_at_k": retrieved_count,
        "unjudged_retrieved_count_at_k": unjudged_count,
        "k": safe_k,
        "per_query": per_query,
        "aggregate": aggregate,
        "claim_gate": claim_gate,
        "boundary": BOUNDARY,
    }


def build_qrels_backed_semantic_quality_report(evaluation: dict[str, Any]) -> str:
    aggregate = evaluation["aggregate"]
    lines = [
        "# Qrels-backed Semantic Retrieval Quality Eval",
        "",
        "Phase marker: qrels-backed semantic retrieval quality eval v0.",
        "",
        "This report evaluates a tiny local retrieval run against explicit qrels.",
        "",
        "This is not semantic retrieval quality evidence.",
        "",
        "## Formats",
        "",
        f"- qrels: `{evaluation['qrel_format']}`",
        f"- run: `{evaluation['run_format']}`",
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
            "This gate blocks this toy qrels-backed evaluation from being cited as semantic retrieval quality evidence.",
            "",
            f"- status: `{claim_gate['status']}`",
            f"- can_claim_semantic_quality: `{_format_bool(claim_gate['can_claim_semantic_quality'])}`",
            f"- summary: `{claim_gate['summary']}`",
            f"- blocker_codes: `{_format_list(claim_gate['blocker_codes'])}`",
            "",
            "## Boundary",
            "",
            "This is qrels-backed toy fixture evaluation only.",
            "",
            "This is not semantic retrieval quality evidence.",
            "",
            "This is not embedding generation.",
            "",
            "This is not a benchmark result.",
            "",
            "This is not a model comparison.",
            "",
            "This is not hosted deployment evidence.",
        ]
    )
    return "\n".join(lines) + "\n"


def _query_warnings(
    *,
    retrieved_ids: list[str],
    retrieved_relevant: list[str],
    missed_relevant: list[str],
    unjudged_retrieved: list[str],
) -> list[str]:
    warnings: list[str] = []
    if not retrieved_ids:
        warnings.append("no_run_results_at_k")
    if not retrieved_relevant:
        warnings.append("no_relevant_documents_retrieved_at_k")
    if missed_relevant:
        warnings.append("missed_relevant_documents_at_k")
    if unjudged_retrieved:
        warnings.append("unjudged_retrieved_documents")
    return warnings


def _claim_gate(
    *,
    aggregate: dict[str, float],
    unjudged_count: int,
    per_query: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    blocker_codes = ["toy_qrels_fixture_boundary"]
    if unjudged_count > 0:
        blocker_codes.append("unjudged_retrieved_documents")
    if aggregate.get("judged_coverage_at_k", 0.0) < 1.0:
        blocker_codes.append("incomplete_judged_coverage")
    if any(row["missed_relevant_ids"] for row in per_query.values()):
        blocker_codes.append("missed_relevant_documents")
    if any(not row["retrieved_ids"] for row in per_query.values()):
        blocker_codes.append("missing_run_results")
    return {
        "status": "blocked",
        "can_claim_semantic_quality": False,
        "blocker_codes": list(dict.fromkeys(blocker_codes)),
        "summary": "qrels_backed_semantic_quality_claim_blocked",
        "boundary": BOUNDARY,
    }


def _first_relevant_rank(
    ranked_ids: list[str],
    qrel: dict[str, int],
) -> int | None:
    for index, doc_id in enumerate(ranked_ids, start=1):
        if qrel.get(doc_id, 0) > 0:
            return index
    return None


def _ndcg(ranked_ids: list[str], qrel: dict[str, int], k: int) -> float:
    ideal_grades = sorted([grade for grade in qrel.values() if grade > 0], reverse=True)[:k]
    ideal = _dcg(ideal_grades)
    if ideal == 0:
        return 0.0
    actual_grades = [max(qrel.get(doc_id, 0), 0) for doc_id in ranked_ids[:k]]
    return _dcg(actual_grades) / ideal


def _dcg(grades: list[int]) -> float:
    return sum(
        ((2**grade) - 1) / log2(rank + 1)
        for rank, grade in enumerate(grades, start=1)
    )


def _aggregate(per_query: dict[str, dict[str, Any]]) -> dict[str, float]:
    metric_names = ["Hit@k", "Recall@k", "MRR@k", "nDCG@k"]
    return {
        metric: _round(
            sum(float(query_metrics[metric]) for query_metrics in per_query.values())
            / max(len(per_query), 1)
        )
        for metric in metric_names
    }


def _round(value: float) -> float:
    return round(value, 4)


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
