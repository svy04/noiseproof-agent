from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.live_semantic_qrels import (
    build_live_semantic_run_from_fixture,
    evaluate_live_semantic_qrels_baseline,
)
from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture


FIXTURE_ROOT = REPO_ROOT / "examples/semantic-retrieval-quality"


def test_live_semantic_run_is_generated_from_fixture_vectors():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    run = build_live_semantic_run_from_fixture(fixture, k=2)

    assert run == {
        "q-demand-growth": ["chunk-demand-growth", "chunk-revenue-growth"],
        "q-risk-contradiction": [
            "chunk-contradictory-channel",
            "chunk-source-quality",
        ],
        "q-source-quality": ["chunk-source-quality", "chunk-contradictory-channel"],
        "q-what-missing": ["chunk-scope-boundary", "chunk-source-quality"],
    }


def test_live_semantic_qrels_baseline_blocks_quality_claims():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    result = evaluate_live_semantic_qrels_baseline(fixture, k=2)

    assert result["run_source"] == "caller_provided_live_semantic_cosine"
    assert result["retrieval_strategy"] == "semantic-cosine"
    assert result["ranking_boundary"] == "exact_cosine_caller_provided_query_vector"
    assert result["boundary"] == (
        "caller_provided_live_semantic_qrels_baseline_not_quality_evidence"
    )
    assert result["qrels_evaluation_boundary"] == (
        "qrels_backed_toy_eval_not_semantic_quality_evidence"
    )
    assert result["aggregate"]["Hit@k"] == 1.0
    assert result["aggregate"]["Recall@k"] == 0.75
    assert result["aggregate"]["MRR@k"] == 1.0
    assert result["aggregate"]["nDCG@k"] == 0.7296
    assert result["aggregate"]["judged_coverage_at_k"] == 0.75
    assert result["retrieved_count_at_k"] == 8
    assert result["unjudged_retrieved_count_at_k"] == 2
    assert result["missing_embedding_chunk_ids"] == ["chunk-missing-source"]
    assert result["claim_gate"]["status"] == "blocked"
    assert result["claim_gate"]["can_claim_semantic_quality"] is False
    assert "caller_provided_embedding_boundary" in result["claim_gate"]["blocker_codes"]
    assert "toy_qrels_fixture_boundary" in result["claim_gate"]["blocker_codes"]
    assert "missed_relevant_documents" in result["claim_gate"]["blocker_codes"]


def test_live_semantic_qrels_baseline_command_writes_reproducible_report(tmp_path):
    output_path = tmp_path / "live-semantic-qrels-baseline-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.live_semantic_qrels_baseline_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(output_path),
            "--k",
            "2",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = output_path.read_text(encoding="utf-8")

    assert "live semantic qrels baseline v0" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
    assert "# Live Semantic Qrels Baseline Eval" in report
    assert "Phase marker: live semantic qrels baseline v0." in report
    assert "run_source: `caller_provided_live_semantic_cosine`" in report
    assert "retrieval_strategy: `semantic-cosine`" in report
    assert "exact_cosine_caller_provided_query_vector" in report
    assert "chunk-source-quality, chunk-contradictory-channel" in report
    assert "caller_provided_embedding_boundary" in report
    assert "This is not semantic retrieval quality evidence." in report


def test_live_semantic_qrels_baseline_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.live_semantic_qrels_baseline_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(REPO_ROOT / "docs/evaluation/live-semantic-qrels-baseline-report.md"),
            "--k",
            "2",
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "live_semantic_qrels_baseline_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
