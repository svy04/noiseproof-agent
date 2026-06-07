from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture
from packages.ingestion.retrieval.quality_metrics import evaluate_semantic_quality


def test_semantic_quality_evaluator_scores_perfect_rankings_without_quality_claim():
    fixture = load_semantic_quality_fixture(
        REPO_ROOT / "examples/semantic-retrieval-quality"
    )
    rankings = {
        "q-demand-growth": ["chunk-demand-growth", "chunk-revenue-growth"],
        "q-risk-contradiction": ["chunk-contradictory-channel", "chunk-source-quality"],
        "q-source-quality": ["chunk-source-quality", "chunk-missing-source"],
        "q-what-missing": ["chunk-missing-source", "chunk-scope-boundary"],
    }

    result = evaluate_semantic_quality(fixture, rankings, k=3)

    assert result["claim_boundary"] == "toy_fixture_metric_only_not_search_quality"
    assert result["aggregate"]["Hit@k"] == 1.0
    assert result["aggregate"]["Recall@k"] == 1.0
    assert result["aggregate"]["MRR@k"] == 1.0
    assert result["aggregate"]["nDCG@k"] == 1.0
    assert result["aggregate"]["missing_embedding_rate"] == 0.1667
    assert result["aggregate"]["role_coverage_at_k"] == 1.0
    assert result["aggregate"]["semantic_vs_lexical_disagreement"] is None


def test_semantic_quality_evaluator_surfaces_weak_rankings_and_disagreement():
    fixture = load_semantic_quality_fixture(
        REPO_ROOT / "examples/semantic-retrieval-quality"
    )
    semantic_rankings = {
        "q-demand-growth": ["chunk-scope-boundary", "chunk-demand-growth"],
        "q-risk-contradiction": ["chunk-demand-growth", "chunk-source-quality"],
        "q-source-quality": ["chunk-demand-growth", "chunk-missing-source"],
        "q-what-missing": [],
    }
    lexical_rankings = {
        "q-demand-growth": ["chunk-demand-growth", "chunk-revenue-growth"],
        "q-risk-contradiction": ["chunk-contradictory-channel"],
        "q-source-quality": ["chunk-source-quality"],
        "q-what-missing": ["chunk-missing-source"],
    }

    result = evaluate_semantic_quality(
        fixture,
        semantic_rankings,
        lexical_rankings=lexical_rankings,
        k=2,
    )

    assert result["aggregate"]["Hit@k"] == 0.75
    assert result["aggregate"]["Recall@k"] == 0.375
    assert result["aggregate"]["MRR@k"] == 0.375
    assert result["aggregate"]["semantic_vs_lexical_disagreement"] > 0.0
    assert result["per_query"]["q-what-missing"]["Hit@k"] == 0.0


def test_semantic_quality_evaluator_exposes_per_query_diagnostics_without_quality_claim():
    fixture = load_semantic_quality_fixture(
        REPO_ROOT / "examples/semantic-retrieval-quality"
    )
    semantic_rankings = {
        "q-demand-growth": ["chunk-scope-boundary", "chunk-demand-growth"],
        "q-risk-contradiction": ["chunk-demand-growth", "chunk-source-quality"],
        "q-source-quality": ["chunk-demand-growth", "chunk-missing-source"],
        "q-what-missing": [],
    }
    lexical_rankings = {
        "q-demand-growth": ["chunk-demand-growth", "chunk-revenue-growth"],
        "q-risk-contradiction": ["chunk-contradictory-channel"],
        "q-source-quality": ["chunk-source-quality"],
        "q-what-missing": ["chunk-missing-source"],
    }

    result = evaluate_semantic_quality(
        fixture,
        semantic_rankings,
        lexical_rankings=lexical_rankings,
        k=2,
    )

    diagnostics = result["per_query_diagnostics"]
    missing = diagnostics["q-what-missing"]

    assert missing["semantic_top_k"] == []
    assert missing["lexical_top_k"] == ["chunk-missing-source"]
    assert missing["missed_relevant_chunk_ids"] == [
        "chunk-missing-source",
        "chunk-scope-boundary",
    ]
    assert missing["missing_information_roles"] == [
        "missing_data_signal",
        "scope_boundary",
        "user_intent_check",
    ]
    assert missing["relevant_missing_embedding_chunk_ids"] == [
        "chunk-missing-source"
    ]
    assert missing["lexical_rescue_chunk_ids"] == ["chunk-missing-source"]
    assert missing["warnings"] == [
        "no_semantic_candidates_at_k",
        "no_relevant_semantic_candidate_at_k",
        "missing_required_information_roles_at_k",
        "relevant_chunk_missing_embedding",
        "lexical_retrieved_relevant_not_in_semantic_top_k",
    ]
    assert result["claim_boundary"] == "toy_fixture_metric_only_not_search_quality"
