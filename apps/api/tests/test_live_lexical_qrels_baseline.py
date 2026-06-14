from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.live_lexical_qrels import (
    build_live_lexical_run_from_fixture,
    evaluate_live_lexical_qrels_baseline,
)
from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture


FIXTURE_ROOT = REPO_ROOT / "examples/semantic-retrieval-quality"


def test_live_lexical_run_is_generated_from_retrieve_candidates():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    run = build_live_lexical_run_from_fixture(
        fixture,
        strategy="fixed-window",
        k=2,
    )

    assert run == {
        "q-demand-growth": ["chunk-contradictory-channel", "chunk-demand-growth"],
        "q-risk-contradiction": ["chunk-demand-growth", "chunk-contradictory-channel"],
        "q-source-quality": ["chunk-missing-source", "chunk-scope-boundary"],
        "q-what-missing": ["chunk-missing-source"],
    }


def test_live_lexical_qrels_baseline_blocks_quality_claims():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    result = evaluate_live_lexical_qrels_baseline(
        fixture,
        strategy="fixed-window",
        k=2,
    )

    assert result["run_source"] == "live_lexical_retrieve_candidates"
    assert result["retrieval_strategy"] == "fixed-window"
    assert result["boundary"] == "live_lexical_qrels_baseline_not_semantic_quality_evidence"
    assert result["qrels_evaluation_boundary"] == "qrels_backed_toy_eval_not_semantic_quality_evidence"
    assert result["aggregate"]["Hit@k"] == 1.0
    assert result["aggregate"]["Recall@k"] == 0.5
    assert result["aggregate"]["MRR@k"] == 0.75
    assert result["aggregate"]["nDCG@k"] == 0.5825
    assert result["aggregate"]["judged_coverage_at_k"] == 0.5714
    assert result["retrieved_count_at_k"] == 7
    assert result["unjudged_retrieved_count_at_k"] == 3
    assert result["claim_gate"]["status"] == "blocked"
    assert result["claim_gate"]["can_claim_semantic_quality"] is False
    assert "live_lexical_baseline_boundary" in result["claim_gate"]["blocker_codes"]
    assert "missed_relevant_documents" in result["claim_gate"]["blocker_codes"]


def test_live_lexical_qrels_baseline_command_writes_reproducible_report(tmp_path):
    output_path = tmp_path / "live-lexical-qrels-baseline-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.live_lexical_qrels_baseline_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(output_path),
            "--strategy",
            "fixed-window",
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

    assert "live lexical qrels baseline v0" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
    assert "# Live Lexical Qrels Baseline Eval" in report
    assert "Phase marker: live lexical qrels baseline v0." in report
    assert "run_source: `live_lexical_retrieve_candidates`" in report
    assert "retrieval_strategy: `fixed-window`" in report
    assert "live_lexical_qrels_baseline_not_semantic_quality_evidence" in report
    assert "chunk-contradictory-channel, chunk-demand-growth" in report
    assert "live_lexical_baseline_boundary" in report
    assert "This is not semantic retrieval quality evidence." in report


def test_live_lexical_qrels_baseline_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.live_lexical_qrels_baseline_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(REPO_ROOT / "docs/evaluation/live-lexical-qrels-baseline-report.md"),
            "--strategy",
            "fixed-window",
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
    assert "live_lexical_qrels_baseline_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
