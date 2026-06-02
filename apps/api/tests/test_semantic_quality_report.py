from pathlib import Path
import subprocess
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


def test_semantic_quality_report_command_regenerates_committed_report(tmp_path):
    output_path = tmp_path / "semantic-retrieval-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.semantic_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/semantic-retrieval-quality"),
            "--rankings",
            str(REPO_ROOT / "examples/semantic-retrieval-quality/rankings.json"),
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
    committed_report = (
        REPO_ROOT / "docs/evaluation/semantic-retrieval-quality-report.md"
    ).read_text(encoding="utf-8")

    assert report == committed_report
    assert "semantic retrieval quality report v0" in result.stdout
    assert "toy_fixture_metric_only_not_search_quality" in result.stdout
    assert "not vector search quality evidence" in result.stdout


def test_semantic_quality_report_command_fails_with_boundary_for_bad_rankings(tmp_path):
    bad_rankings = tmp_path / "bad-rankings.json"
    bad_rankings.write_text('{"lexical_rankings": {}}', encoding="utf-8")
    output_path = tmp_path / "semantic-retrieval-quality-report.md"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "app.services.semantic_quality_report_command",
            "--fixture",
            str(REPO_ROOT / "examples/semantic-retrieval-quality"),
            "--rankings",
            str(bad_rankings),
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

    assert result.returncode == 2
    assert "semantic_quality_report_regeneration_failed" in result.stderr
    assert "semantic_rankings" in result.stderr
    assert "not vector search quality evidence" in result.stderr
    assert "Traceback" not in result.stderr
    assert not output_path.exists()
