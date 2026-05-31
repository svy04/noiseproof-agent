import json
import sys
from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.append(str(REPO_ROOT))

from packages.review.external_feedback import screen_external_feedback_comments


def test_external_feedback_screen_keeps_empty_issue_pending():
    result = screen_external_feedback_comments([], repository_owner="svy04")

    assert result.status == "pending"
    assert result.candidate_count == 0
    assert result.next_gate == "external reviewer feedback v0"
    assert result.warnings == ["No public issue comments were available to screen."]


def test_external_feedback_screen_rejects_self_authored_comment():
    result = screen_external_feedback_comments(
        [
            {
                "author": {"login": "svy04"},
                "url": "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-1",
                "body": (
                    "I inspected docs/review/external-reader-proof-path.md. "
                    "The claim boundary is too broad and missing evidence is clear."
                ),
            }
        ],
        repository_owner="svy04",
    )

    assert result.status == "pending"
    assert result.candidate_count == 0
    assert result.screened_comments[0].classification == "non_qualifying"
    assert "self_authored_comment" in result.screened_comments[0].reasons


def test_external_feedback_screen_rejects_generic_external_praise():
    result = screen_external_feedback_comments(
        [
            {
                "author": {"login": "external-reviewer"},
                "url": "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-2",
                "body": "Looks good. Nice project.",
            }
        ],
        repository_owner="svy04",
    )

    assert result.status == "pending"
    assert result.candidate_count == 0
    reasons = result.screened_comments[0].reasons
    assert "missing_inspected_artifact" in reasons
    assert "missing_actionable_critique_or_boundary" in reasons


def test_external_feedback_screen_flags_external_evidence_referenced_critique_as_candidate_only():
    result = screen_external_feedback_comments(
        [
            {
                "author": {"login": "external-reviewer"},
                "url": "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-3",
                "body": (
                    "Reviewer role: RAG engineer. I inspected "
                    "docs/review/external-reader-proof-path.md and README.md. "
                    "The evidence is easiest to inspect in the proof path, but the "
                    "claim boundary still feels over-stated because the local browser "
                    "screenshot is self-authored. Missing evidence: an external reviewer "
                    "should confirm the shortest path actually scans in five minutes."
                ),
            }
        ],
        repository_owner="svy04",
    )

    assert result.status == "candidate_found_manual_review_required"
    assert result.candidate_count == 1
    candidate = result.screened_comments[0]
    assert candidate.classification == "candidate_requires_manual_acceptance"
    assert candidate.author_login == "external-reviewer"
    assert candidate.artifacts == [
        "README.md",
        "docs/review/external-reader-proof-path.md",
    ]
    assert candidate.source_url.endswith("#issuecomment-3")
    assert result.does_not_close_gate is True
    assert result.next_gate == "external reviewer feedback v0"


def test_external_feedback_cli_screens_gh_issue_view_payload(tmp_path):
    payload_path = tmp_path / "issue-comments.json"
    payload_path.write_text(
        json.dumps(
            {
                "comments": [
                    {
                        "author": {"login": "external-reviewer"},
                        "url": "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-4",
                        "body": (
                            "I inspected docs/review/external-reader-proof-path.md. "
                            "The claim boundary is still too broad and missing evidence "
                            "should be made clearer."
                        ),
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "packages.review.external_feedback_cli",
            "--input",
            str(payload_path),
            "--repository-owner",
            "svy04",
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    output = json.loads(result.stdout)
    assert output["status"] == "candidate_found_manual_review_required"
    assert output["candidate_count"] == 1
    assert output["does_not_close_gate"] is True
    assert output["next_gate"] == "external reviewer feedback v0"
    assert output["screened_comments"][0]["classification"] == (
        "candidate_requires_manual_acceptance"
    )


def test_external_feedback_cli_accepts_utf8_bom_issue_payload(tmp_path):
    payload_path = tmp_path / "issue-comments-bom.json"
    payload_path.write_text(
        json.dumps({"comments": []}),
        encoding="utf-8-sig",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "packages.review.external_feedback_cli",
            "--input",
            str(payload_path),
            "--repository-owner",
            "svy04",
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )

    output = json.loads(result.stdout)
    assert output["status"] == "pending"
    assert output["candidate_count"] == 0
