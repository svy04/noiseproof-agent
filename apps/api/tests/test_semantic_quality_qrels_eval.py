from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.qrels_eval import (
    evaluate_qrels_backed_run,
    parse_qrels_file,
    parse_trec_run_file,
)


FIXTURE_ROOT = REPO_ROOT / "examples/semantic-retrieval-quality"


def test_qrels_backed_eval_reads_trec_style_qrels_and_run_files():
    qrels = parse_qrels_file(FIXTURE_ROOT / "qrels.txt")
    run = parse_trec_run_file(FIXTURE_ROOT / "semantic-run.txt")

    result = evaluate_qrels_backed_run(qrels=qrels, run=run, k=2)

    assert result["qrel_format"] == "trec_qrels_qid_iter_docno_relevance"
    assert result["run_format"] == "trec_run_qid_Q0_docno_rank_score_runid"
    assert result["query_count"] == 4
    assert result["judged_relevant_count"] == 8
    assert result["retrieved_count_at_k"] == 6
    assert result["unjudged_retrieved_count_at_k"] == 2
    assert result["aggregate"]["Hit@k"] == 0.75
    assert result["aggregate"]["Recall@k"] == 0.375
    assert result["aggregate"]["MRR@k"] == 0.375
    assert result["aggregate"]["nDCG@k"] == 0.198
    assert result["aggregate"]["judged_coverage_at_k"] == 0.6667
    assert result["claim_gate"]["status"] == "blocked"
    assert result["claim_gate"]["can_claim_semantic_quality"] is False
    assert "toy_qrels_fixture_boundary" in result["claim_gate"]["blocker_codes"]
    assert "unjudged_retrieved_documents" in result["claim_gate"]["blocker_codes"]
    assert result["boundary"] == "qrels_backed_toy_eval_not_semantic_quality_evidence"


def test_qrels_backed_eval_exposes_per_query_unjudged_and_missing_relevance():
    qrels = parse_qrels_file(FIXTURE_ROOT / "qrels.txt")
    run = parse_trec_run_file(FIXTURE_ROOT / "semantic-run.txt")

    result = evaluate_qrels_backed_run(qrels=qrels, run=run, k=2)

    demand = result["per_query"]["q-demand-growth"]
    assert demand["unjudged_retrieved_ids"] == ["chunk-scope-boundary"]
    assert demand["missed_relevant_ids"] == ["chunk-revenue-growth"]
    assert "unjudged_retrieved_documents" in demand["warnings"]
    assert "missed_relevant_documents_at_k" in demand["warnings"]

    missing = result["per_query"]["q-what-missing"]
    assert missing["retrieved_ids"] == []
    assert missing["missed_relevant_ids"] == [
        "chunk-missing-source",
        "chunk-scope-boundary",
    ]
    assert "no_run_results_at_k" in missing["warnings"]
    assert "no_relevant_documents_retrieved_at_k" in missing["warnings"]


def test_qrels_backed_eval_command_writes_report_without_quality_claim(tmp_path):
    output_path = tmp_path / "qrels-backed-semantic-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.qrels_backed_semantic_quality_command",
            "--qrels",
            str(FIXTURE_ROOT / "qrels.txt"),
            "--run",
            str(FIXTURE_ROOT / "semantic-run.txt"),
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

    assert "qrels-backed semantic retrieval quality eval v0" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
    assert "# Qrels-backed Semantic Retrieval Quality Eval" in report
    assert "Phase marker: qrels-backed semantic retrieval quality eval v0." in report
    assert "trec_qrels_qid_iter_docno_relevance" in report
    assert "judged_coverage_at_k" in report
    assert "unjudged_retrieved_documents" in report
    assert "qrels_backed_toy_eval_not_semantic_quality_evidence" in report
    assert "This is not semantic retrieval quality evidence." in report


def test_qrels_backed_eval_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.qrels_backed_semantic_quality_command",
            "--qrels",
            str(FIXTURE_ROOT / "qrels.txt"),
            "--run",
            str(FIXTURE_ROOT / "semantic-run.txt"),
            "--output",
            str(REPO_ROOT / "docs/evaluation/qrels-backed-semantic-quality-report.md"),
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
    assert "qrels_backed_semantic_quality_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not semantic retrieval quality evidence" in result.stdout
