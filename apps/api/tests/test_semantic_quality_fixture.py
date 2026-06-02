from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.quality_fixture import (
    load_semantic_quality_fixture,
    summarize_semantic_quality_fixture,
)


def test_semantic_quality_fixture_loads_queries_corpus_and_qrels():
    fixture = load_semantic_quality_fixture(
        REPO_ROOT / "examples/semantic-retrieval-quality"
    )

    assert fixture.name == "semantic-retrieval-quality-fixture-v0"
    assert fixture.embedding_dimension == 3
    assert fixture.no_embedding_generation is True
    assert len(fixture.queries) == 4
    assert len(fixture.corpus) == 6
    assert fixture.queries[0].query_id == "q-demand-growth"
    assert fixture.queries[0].relevant_chunk_ids == [
        "chunk-demand-growth",
        "chunk-revenue-growth",
    ]


def test_semantic_quality_fixture_summary_keeps_quality_boundary_visible():
    fixture = load_semantic_quality_fixture(
        REPO_ROOT / "examples/semantic-retrieval-quality"
    )
    summary = summarize_semantic_quality_fixture(fixture)

    assert summary["query_count"] == 4
    assert summary["chunk_count"] == 6
    assert summary["qrel_count"] == 8
    assert summary["missing_embedding_chunk_ids"] == ["chunk-missing-source"]
    assert summary["candidate_metrics"] == [
        "Hit@k",
        "Recall@k",
        "MRR@k",
        "nDCG@k",
        "missing_embedding_rate",
        "semantic_vs_lexical_disagreement",
        "role_coverage_at_k",
    ]
    assert "direct_support" in summary["information_roles"]
    assert "contradiction" in summary["information_roles"]
    assert "source_quality_check" in summary["information_roles"]
    assert summary["claim_boundary"] == "fixture_only_not_quality_evidence"
