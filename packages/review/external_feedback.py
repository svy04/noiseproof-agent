from __future__ import annotations

from dataclasses import dataclass, field
from dataclasses import asdict
import re
from typing import Any


NEXT_GATE = "external reviewer feedback v0"

ARTIFACT_PATTERN = re.compile(r"\b(?:README\.md|docs/[A-Za-z0-9_./-]+\.md)\b")
ACTIONABLE_PATTERN = re.compile(
    r"\b("
    r"claim boundary|boundary|missing evidence|missing|over-stated|overstated|"
    r"too self-authored|self-authored|trust|critique|stronger|weaker|should|"
    r"would make|does not yet prove|not yet prove|evidence"
    r")\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ScreenedExternalFeedbackComment:
    author_login: str
    source_url: str
    artifacts: list[str]
    classification: str
    reasons: list[str]


@dataclass(frozen=True)
class ExternalFeedbackScreenResult:
    status: str
    candidate_count: int
    next_gate: str = NEXT_GATE
    does_not_close_gate: bool = True
    warnings: list[str] = field(default_factory=list)
    screened_comments: list[ScreenedExternalFeedbackComment] = field(default_factory=list)


def screen_external_feedback_comments(
    comments: list[dict[str, Any]], *, repository_owner: str
) -> ExternalFeedbackScreenResult:
    """Screen public issue comments for possible external-feedback candidates.

    This function intentionally does not accept feedback into the proof path.
    It only separates obvious non-qualifying comments from comments that still
    require manual review against the intake criteria.
    """

    if not comments:
        return ExternalFeedbackScreenResult(
            status="pending",
            candidate_count=0,
            warnings=["No public issue comments were available to screen."],
        )

    screened = [
        _screen_comment(comment, repository_owner=repository_owner) for comment in comments
    ]
    candidate_count = sum(
        1
        for comment in screened
        if comment.classification == "candidate_requires_manual_acceptance"
    )
    status = (
        "candidate_found_manual_review_required" if candidate_count else "pending"
    )
    return ExternalFeedbackScreenResult(
        status=status,
        candidate_count=candidate_count,
        screened_comments=screened,
    )


def screen_issue_view_payload(
    payload: dict[str, Any] | list[dict[str, Any]], *, repository_owner: str
) -> ExternalFeedbackScreenResult:
    if isinstance(payload, list):
        comments = payload
    else:
        comments = payload.get("comments") or []
    return screen_external_feedback_comments(comments, repository_owner=repository_owner)


def screen_result_to_dict(result: ExternalFeedbackScreenResult) -> dict[str, Any]:
    return asdict(result)


def _screen_comment(
    comment: dict[str, Any], *, repository_owner: str
) -> ScreenedExternalFeedbackComment:
    body = str(comment.get("body") or "")
    author_login = _extract_author_login(comment)
    artifacts = sorted(set(ARTIFACT_PATTERN.findall(body)))
    reasons: list[str] = []

    if author_login.lower() == repository_owner.lower():
        reasons.append("self_authored_comment")

    if not artifacts:
        reasons.append("missing_inspected_artifact")

    if not ACTIONABLE_PATTERN.search(body):
        reasons.append("missing_actionable_critique_or_boundary")

    classification = (
        "candidate_requires_manual_acceptance" if not reasons else "non_qualifying"
    )
    return ScreenedExternalFeedbackComment(
        author_login=author_login,
        source_url=str(comment.get("url") or ""),
        artifacts=artifacts,
        classification=classification,
        reasons=reasons,
    )


def _extract_author_login(comment: dict[str, Any]) -> str:
    author = comment.get("author") or comment.get("user") or {}
    if isinstance(author, dict):
        return str(author.get("login") or "")
    return ""
