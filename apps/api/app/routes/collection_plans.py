from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import CollectionPlanPreviewOut, CollectionPlanPreviewRequest
from app.services.collection_plan import preview_collection_plan
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/collection-plans", tags=["collection-plans"])


@router.post("/preview", response_model=CollectionPlanPreviewOut)
def create_collection_plan_preview(
    payload: CollectionPlanPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> CollectionPlanPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /collection-plans/preview",
        user_question=payload.question,
        trace_json={},
        operation=lambda _agent_run_id: preview_collection_plan(payload),
        trace_from_result=lambda result: {
            "required_role_count": len(result.required_roles),
            "warning_count": len(result.warnings),
            "stop_condition_count": len(result.stop_conditions),
        },
    )
