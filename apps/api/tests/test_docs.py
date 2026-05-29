from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_phase10_evaluation_and_application_artifacts_exist():
    required_files = [
        "docs/evaluation/eval-plan.md",
        "docs/evaluation/retrieval-eval-report.md",
        "docs/evaluation/failure-cases.md",
        "docs/application/braincrew-role-map.md",
        "docs/application/cover-message.md",
        "docs/application/portfolio-index.md",
    ]

    for file_path in required_files:
        assert (REPO_ROOT / file_path).is_file(), f"Missing {file_path}"


def test_braincrew_role_map_keeps_fde_first_and_bounds_claims():
    content = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(encoding="utf-8")

    assert "Forward Deployed Engineer" in content
    assert "Product Engineer" in content
    assert "FDE-first" in content
    assert "not a trading bot" in content
    assert "Unproven" in content


def test_evaluation_docs_include_examples_and_unproven_boundaries():
    eval_plan = (REPO_ROOT / "docs/evaluation/eval-plan.md").read_text(encoding="utf-8")
    retrieval_report = (REPO_ROOT / "docs/evaluation/retrieval-eval-report.md").read_text(encoding="utf-8")
    failure_cases = (REPO_ROOT / "docs/evaluation/failure-cases.md").read_text(encoding="utf-8")

    assert "sample dataset" in eval_plan
    assert "unsupported claim" in eval_plan
    assert "Not yet measured" in retrieval_report
    assert "lexical retrieval" in retrieval_report
    assert "runtime_verification" in failure_cases
    assert "No LLM" in failure_cases
