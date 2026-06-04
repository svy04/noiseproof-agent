from app.schemas import (
    FailureCaseWorkflowReviewQueueItemOut,
    FailureCaseWorkflowReviewQueueOut,
    WorkflowRunOut,
)

REVIEWABLE_WORKFLOW_STATUSES = {"failed", "blocked", "needs_revision"}


def build_failure_case_workflow_review_queue(
    *,
    workflow_runs: list[dict],
    failure_cases: list[dict],
) -> FailureCaseWorkflowReviewQueueOut:
    failure_case_ids_by_workflow_id: dict[str, list] = {}
    for failure_case in failure_cases:
        workflow_run_id = failure_case.get("workflow_run_id")
        if workflow_run_id is None:
            continue
        failure_case_ids_by_workflow_id.setdefault(str(workflow_run_id), []).append(
            failure_case["id"]
        )

    items: list[FailureCaseWorkflowReviewQueueItemOut] = []
    for workflow_run in workflow_runs:
        status = str(workflow_run.get("status") or "")
        if status not in REVIEWABLE_WORKFLOW_STATUSES:
            continue
        workflow_run_id = str(workflow_run["id"])
        linked_failure_case_ids = failure_case_ids_by_workflow_id.get(workflow_run_id, [])
        review_status = (
            "failure_case_linked"
            if linked_failure_case_ids
            else "needs_failure_case_review"
        )
        trace_json = workflow_run.get("trace_json") or {}
        stage = str(trace_json.get("stage") or "unknown_stage")
        error_type = str(trace_json.get("error_type") or "UnknownError")
        items.append(
            FailureCaseWorkflowReviewQueueItemOut(
                workflow_run=WorkflowRunOut(**workflow_run),
                review_status=review_status,
                linked_failure_case_ids=linked_failure_case_ids,
                linked_failure_case_count=len(linked_failure_case_ids),
                draft_preview_path="/failure-cases/draft-preview",
                stage=stage,
                error_type=error_type,
                warnings=[
                    "Review queue is a read model over workflow_runs and failure_cases.",
                    "It does not create failure_cases or classify root cause automatically.",
                ],
            )
        )

    pending_review_count = sum(
        1 for item in items if item.review_status == "needs_failure_case_review"
    )
    linked_failure_case_count = sum(
        item.linked_failure_case_count for item in items
    )
    return FailureCaseWorkflowReviewQueueOut(
        queue_boundary="failed_workflow_review_queue_read_model_only",
        persistence_boundary="read_model_only_no_automatic_failure_case_creation",
        pending_review_count=pending_review_count,
        linked_failure_case_count=linked_failure_case_count,
        items=items,
        warnings=[
            "This read model does not create failure_cases.",
            "A human confirmation boundary remains required before persistence.",
            "This is not automatic failure detection or root-cause automation.",
        ],
    )
