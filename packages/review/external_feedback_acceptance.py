from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

from .external_feedback import (
    NEXT_GATE,
    ExternalFeedbackScreenResult,
    ScreenedExternalFeedbackComment,
)


@dataclass(frozen=True)
class ExternalFeedbackAcceptanceDraft:
    reviewer_identity: dict[str, str]
    public_comment_url: str
    inspected_evidence: list[str]
    accepted_critique: str
    manual_acceptance_decision: str
    accepted_as_external_reviewer_feedback: bool
    required_next_actions: list[str]


@dataclass(frozen=True)
class ExternalFeedbackAcceptanceDraftResult:
    status: str
    draft_count: int
    next_gate: str = NEXT_GATE
    does_not_close_gate: bool = True
    warnings: list[str] = field(default_factory=list)
    drafts: list[ExternalFeedbackAcceptanceDraft] = field(default_factory=list)


def build_external_feedback_acceptance_drafts(
    screen_result: ExternalFeedbackScreenResult,
) -> ExternalFeedbackAcceptanceDraftResult:
    candidates = [
        comment
        for comment in screen_result.screened_comments
        if comment.classification == "candidate_requires_manual_acceptance"
    ]
    if candidates:
        drafts = [_draft_from_candidate(comment) for comment in candidates]
        return ExternalFeedbackAcceptanceDraftResult(
            status="manual_acceptance_required",
            draft_count=len(drafts),
            warnings=[
                "Acceptance drafts require manual review and do not close the gate."
            ],
            drafts=drafts,
        )

    return ExternalFeedbackAcceptanceDraftResult(
        status="pending",
        draft_count=0,
        warnings=["No candidate comments were available for acceptance drafting."],
    )


def build_external_feedback_acceptance_drafts_from_dict(
    payload: dict[str, Any],
) -> ExternalFeedbackAcceptanceDraftResult:
    comments = [
        ScreenedExternalFeedbackComment(
            author_login=str(comment.get("author_login") or ""),
            source_url=str(comment.get("source_url") or ""),
            artifacts=list(comment.get("artifacts") or []),
            classification=str(comment.get("classification") or ""),
            reasons=list(comment.get("reasons") or []),
            comment_body=str(comment.get("comment_body") or ""),
        )
        for comment in payload.get("screened_comments", [])
    ]
    screen_result = ExternalFeedbackScreenResult(
        status=str(payload.get("status") or "pending"),
        candidate_count=int(payload.get("candidate_count") or 0),
        warnings=list(payload.get("warnings") or []),
        screened_comments=comments,
    )
    return build_external_feedback_acceptance_drafts(screen_result)


def acceptance_draft_result_to_dict(
    result: ExternalFeedbackAcceptanceDraftResult,
) -> dict[str, Any]:
    return asdict(result)


def _draft_from_candidate(
    comment: ScreenedExternalFeedbackComment,
) -> ExternalFeedbackAcceptanceDraft:
    critique = comment.comment_body.strip()
    if not critique:
        critique = (
            "Candidate comment passed the screening artifact, but the original "
            "comment body was not included in the input."
        )
    return ExternalFeedbackAcceptanceDraft(
        reviewer_identity={
            "reviewer": comment.author_login,
            "reviewer_role": "manual review required",
            "reviewer_relationship_to_repository_owner": "manual review required",
        },
        public_comment_url=comment.source_url,
        inspected_evidence=comment.artifacts,
        accepted_critique=critique,
        manual_acceptance_decision="pending",
        accepted_as_external_reviewer_feedback=False,
        required_next_actions=[
            "manual_acceptance_required",
            "compare_against_external_feedback_intake_criteria",
            "fill_external_feedback_acceptance_template",
        ],
    )
