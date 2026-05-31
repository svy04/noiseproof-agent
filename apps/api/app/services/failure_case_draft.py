from app.schemas import (
    FailureCaseCreate,
    FailureCaseDraftPreviewOut,
    FailureCaseDraftPreviewRequest,
)


def preview_failure_case_draft(
    payload: FailureCaseDraftPreviewRequest,
) -> FailureCaseDraftPreviewOut:
    stage = str(payload.trace_json.get("stage") or "unknown_stage")
    error_type = str(payload.trace_json.get("error_type") or "UnknownError")
    error_message = payload.error_message or "No error message provided."
    failure_type = "workflow_stage_error"
    if payload.workflow_status not in {"failed", "blocked", "needs_revision"}:
        failure_type = "workflow_review_needed"

    draft = FailureCaseCreate(
        agent_run_id=payload.agent_run_id,
        workflow_run_id=payload.workflow_run_id,
        failure_type=failure_type,
        description=(
            f"Workflow question '{payload.question}' reached status "
            f"{payload.workflow_status} at {stage}."
        ),
        root_cause=f"{error_type}: {error_message}",
        fix_status="draft",
        next_action=(
            "Review the failed workflow stage, confirm the failure type, "
            "then manually submit or edit the failure case."
        ),
    )
    source_summary = {
        "workflow_run_id": str(payload.workflow_run_id) if payload.workflow_run_id else None,
        "workflow_status": payload.workflow_status,
        "stage": stage,
        "error_type": error_type,
    }
    warnings = [
        "Draft preview only; it does not create failure_cases.",
        "A human confirmation boundary is required before persistence.",
        "This is not automatic failure detection or root-cause automation.",
    ]
    if payload.workflow_status != "failed":
        warnings.append("Workflow status is not failed; review whether a failure case is needed.")

    return FailureCaseDraftPreviewOut(
        draft=draft,
        source_summary=source_summary,
        persistence_boundary="preview_only_not_persisted",
        human_confirmation_required=True,
        warnings=warnings,
    )
