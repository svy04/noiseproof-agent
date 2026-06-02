from math import log2
from typing import Any

from packages.ingestion.retrieval.quality_fixture import SemanticQualityFixture


def evaluate_semantic_quality(
    fixture: SemanticQualityFixture,
    rankings: dict[str, list[str]],
    *,
    lexical_rankings: dict[str, list[str]] | None = None,
    k: int = 3,
) -> dict[str, Any]:
    safe_k = max(1, k)
    qrels = fixture.qrels
    chunks_by_id = {chunk.chunk_id: chunk for chunk in fixture.corpus}
    per_query: dict[str, dict[str, float]] = {}

    for query in fixture.queries:
        ranked_ids = rankings.get(query.query_id, [])[:safe_k]
        qrel = qrels.get(query.query_id, {})
        relevant_ids = {chunk_id for chunk_id, grade in qrel.items() if grade > 0}
        retrieved_relevant = [chunk_id for chunk_id in ranked_ids if chunk_id in relevant_ids]
        first_relevant_rank = _first_relevant_rank(ranked_ids, relevant_ids)

        per_query[query.query_id] = {
            "Hit@k": 1.0 if retrieved_relevant else 0.0,
            "Recall@k": _round(len(set(retrieved_relevant)) / max(len(relevant_ids), 1)),
            "MRR@k": _round(1.0 / first_relevant_rank) if first_relevant_rank else 0.0,
            "nDCG@k": _round(_ndcg(ranked_ids, qrel, safe_k)),
            "role_coverage_at_k": _round(_role_coverage(query.information_roles, ranked_ids, chunks_by_id)),
        }

    aggregate = _aggregate(per_query)
    aggregate["missing_embedding_rate"] = _round(
        sum(1 for chunk in fixture.corpus if chunk.embedding is None) / max(len(fixture.corpus), 1)
    )
    aggregate["semantic_vs_lexical_disagreement"] = (
        _round(_average_disagreement(rankings, lexical_rankings, safe_k))
        if lexical_rankings is not None
        else None
    )

    return {
        "fixture": fixture.name,
        "k": safe_k,
        "per_query": per_query,
        "aggregate": aggregate,
        "claim_boundary": "toy_fixture_metric_only_not_search_quality",
        "no_embedding_generation": fixture.no_embedding_generation,
    }


def _first_relevant_rank(ranked_ids: list[str], relevant_ids: set[str]) -> int | None:
    for index, chunk_id in enumerate(ranked_ids, start=1):
        if chunk_id in relevant_ids:
            return index
    return None


def _ndcg(ranked_ids: list[str], qrel: dict[str, int], k: int) -> float:
    ideal_grades = sorted(qrel.values(), reverse=True)[:k]
    ideal = _dcg(ideal_grades)
    if ideal == 0:
        return 0.0
    actual_grades = [qrel.get(chunk_id, 0) for chunk_id in ranked_ids[:k]]
    return _dcg(actual_grades) / ideal


def _dcg(grades: list[int]) -> float:
    return sum(((2**grade) - 1) / log2(rank + 1) for rank, grade in enumerate(grades, start=1))


def _role_coverage(
    expected_roles: list[str],
    ranked_ids: list[str],
    chunks_by_id: dict[str, Any],
) -> float:
    expected = set(expected_roles)
    if not expected:
        return 1.0
    retrieved_roles = {
        role
        for chunk_id in ranked_ids
        if chunk_id in chunks_by_id
        for role in chunks_by_id[chunk_id].information_roles
    }
    return len(expected.intersection(retrieved_roles)) / len(expected)


def _average_disagreement(
    semantic_rankings: dict[str, list[str]],
    lexical_rankings: dict[str, list[str]] | None,
    k: int,
) -> float:
    if not lexical_rankings:
        return 0.0
    scores: list[float] = []
    for query_id, semantic_ids in semantic_rankings.items():
        lexical_ids = lexical_rankings.get(query_id, [])
        semantic_set = set(semantic_ids[:k])
        lexical_set = set(lexical_ids[:k])
        union = semantic_set.union(lexical_set)
        if not union:
            scores.append(0.0)
            continue
        scores.append(1.0 - (len(semantic_set.intersection(lexical_set)) / len(union)))
    return sum(scores) / max(len(scores), 1)


def _aggregate(per_query: dict[str, dict[str, float]]) -> dict[str, float]:
    metric_names = ["Hit@k", "Recall@k", "MRR@k", "nDCG@k", "role_coverage_at_k"]
    return {
        metric: _round(
            sum(query_metrics[metric] for query_metrics in per_query.values())
            / max(len(per_query), 1)
        )
        for metric in metric_names
    }


def _round(value: float) -> float:
    return round(value, 4)
