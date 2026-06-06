from app.schemas import FailureCaseCreate, FailureCaseDraftPreviewOut


def preview_document_failure_case_draft(
    *,
    document: dict,
) -> FailureCaseDraftPreviewOut:
    profile_json = document.get("profile_json") or {}
    failure_candidate = profile_json.get("failure_case_candidate")
    if not isinstance(failure_candidate, dict):
        raise ValueError("document has no failure_case_candidate in profile_json")

    failure_type = str(failure_candidate.get("failure_type") or "document_review_needed")
    root_cause = str(
        failure_candidate.get("root_cause")
        or failure_candidate.get("description")
        or "Document profile contains a failure candidate without a root cause."
    )
    next_action = str(
        failure_candidate.get("next_action")
        or (
            "Inspect the persisted document profile, confirm the failure candidate, "
            "then manually submit or edit the failure case."
        )
    )
    title = str(document.get("title") or document.get("filename") or document.get("id"))
    document_id = str(document.get("id"))
    document_status = str(document.get("status") or "unknown")
    source_type = str(document.get("source_type") or "unknown")

    draft = FailureCaseCreate(
        agent_run_id=None,
        workflow_run_id=None,
        failure_type=failure_type,
        description=(
            f"Document '{title}' has persisted failure candidate "
            f"'{failure_type}' with status '{document_status}'."
        ),
        root_cause=root_cause,
        fix_status="draft",
        next_action=next_action,
    )
    source_summary = {
        "document_id": document_id,
        "document_status": document_status,
        "source_type": source_type,
        "failure_type": failure_type,
        "stage": "persisted_document_failure_case_candidate",
    }
    warnings = [
        "Document failure-case draft preview is preview-only and does not create failure_cases.",
        "This is metadata-derived from document profile_json.",
        "A human confirmation boundary is required before persistence.",
        "This is not automatic failure detection or root-cause automation.",
    ]

    return FailureCaseDraftPreviewOut(
        draft=draft,
        source_summary=source_summary,
        persistence_boundary="preview_only_not_persisted",
        human_confirmation_required=True,
        warnings=warnings,
    )
