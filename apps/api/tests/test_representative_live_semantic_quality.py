from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.ingestion.retrieval.quality_fixture import load_semantic_quality_fixture
from packages.ingestion.retrieval.representative_semantic_quality import (
    REQUIRED_INFORMATION_ROLES,
    REQUIRED_SOURCE_TYPES,
    evaluate_representative_live_semantic_quality,
)


FIXTURE_ROOT = REPO_ROOT / "examples/representative-semantic-retrieval-quality"


def test_representative_fixture_covers_noiseproof_information_roles_and_sources():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    result = evaluate_representative_live_semantic_quality(fixture, k=3)
    coverage = result["fixture_coverage"]

    assert fixture.name == "representative-semantic-retrieval-quality-fixture-v0"
    assert coverage["query_count"] == 6
    assert coverage["chunk_count"] == 12
    assert coverage["qrel_count"] == 24
    assert coverage["required_information_roles"] == REQUIRED_INFORMATION_ROLES
    assert coverage["required_source_types"] == REQUIRED_SOURCE_TYPES
    assert coverage["missing_information_roles"] == []
    assert coverage["missing_source_types"] == []
    assert coverage["role_coverage_ratio"] == 1.0
    assert coverage["source_type_coverage_ratio"] == 1.0
    assert coverage["negative_qrel_count"] == 6
    assert coverage["missing_embedding_chunk_ids"] == []
    assert coverage["coverage_status"] == "passed"


def test_representative_live_semantic_quality_eval_keeps_claim_gate_blocked():
    fixture = load_semantic_quality_fixture(FIXTURE_ROOT)

    result = evaluate_representative_live_semantic_quality(fixture, k=3)

    assert result["run_source"] == "representative_caller_provided_live_semantic_cosine"
    assert result["retrieval_strategy"] == "semantic-cosine"
    assert result["ranking_boundary"] == "exact_cosine_caller_provided_query_vector"
    assert result["boundary"] == (
        "representative_local_fixture_not_production_semantic_quality_evidence"
    )
    assert result["aggregate"]["Hit@k"] == 1.0
    assert result["aggregate"]["Recall@k"] == 1.0
    assert result["aggregate"]["MRR@k"] == 1.0
    assert result["aggregate"]["judged_coverage_at_k"] == 1.0
    assert result["retrieved_count_at_k"] == 18
    assert result["unjudged_retrieved_count_at_k"] == 0
    assert result["claim_gate"]["status"] == "blocked"
    assert result["claim_gate"]["can_claim_semantic_quality"] is False
    assert result["claim_gate"]["summary"] == (
        "representative_live_semantic_quality_claim_blocked"
    )
    assert "caller_provided_embedding_boundary" in result["claim_gate"]["blocker_codes"]
    assert "no_live_embedding_generation" in result["claim_gate"]["blocker_codes"]
    assert "local_fixture_boundary" in result["claim_gate"]["blocker_codes"]
    assert "not_production_benchmark" in result["claim_gate"]["blocker_codes"]


def test_representative_live_semantic_quality_command_writes_report(tmp_path):
    output_path = tmp_path / "representative-live-semantic-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.representative_live_semantic_quality_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(output_path),
            "--k",
            "3",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = output_path.read_text(encoding="utf-8")

    assert "representative live semantic quality eval v0" in result.stdout
    assert "not production semantic retrieval quality evidence" in result.stdout
    assert "# Representative Live Semantic Quality Eval" in report
    assert "Phase marker: representative live semantic quality eval v0." in report
    assert "run_source: `representative_caller_provided_live_semantic_cosine`" in report
    assert "coverage_status: `passed`" in report
    assert "role_coverage_ratio: `1`" in report
    assert "source_type_coverage_ratio: `1`" in report
    assert "representative_live_semantic_quality_claim_blocked" in report
    assert "This is not production semantic retrieval quality evidence." in report


def test_representative_live_semantic_quality_command_check_mode_accepts_committed_report():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.representative_live_semantic_quality_command",
            "--fixture-root",
            str(FIXTURE_ROOT),
            "--output",
            str(
                REPO_ROOT
                / "docs/evaluation/representative-live-semantic-quality-report.md"
            ),
            "--k",
            "3",
            "--check",
        ],
        cwd=REPO_ROOT / "apps/api",
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "representative_live_semantic_quality_report_current" in result.stdout
    assert "byte-for-byte regeneration" in result.stdout
    assert "not production semantic retrieval quality evidence" in result.stdout
