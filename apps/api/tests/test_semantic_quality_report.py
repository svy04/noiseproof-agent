from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture
from packages.ingestion.retrieval.quality_metrics import evaluate_semantic_quality
from packages.ingestion.retrieval.quality_report import build_semantic_quality_report


def test_semantic_quality_report_keeps_toy_fixture_boundary_visible():
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
    evaluation = evaluate_semantic_quality(
        fixture,
        semantic_rankings,
        lexical_rankings=lexical_rankings,
        k=2,
    )

    report = build_semantic_quality_report(fixture, evaluation)

    assert "# Semantic Retrieval Quality Report" in report
    assert "semantic retrieval quality report v0" in report
    assert "toy_fixture_metric_only_not_search_quality" in report
    assert "Hit@k | 0.75" in report
    assert "Recall@k | 0.375" in report
    assert "MRR@k | 0.375" in report
    assert "q-what-missing" in report
    assert "not vector search quality evidence" in report
    assert "not embedding generation" in report
