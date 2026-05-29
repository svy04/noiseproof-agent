from fastapi import APIRouter

from app.schemas import CollectionPlanPreviewOut, CollectionPlanPreviewRequest
from app.services.collection_plan import preview_collection_plan

router = APIRouter(prefix="/collection-plans", tags=["collection-plans"])


@router.post("/preview", response_model=CollectionPlanPreviewOut)
def create_collection_plan_preview(
    payload: CollectionPlanPreviewRequest,
) -> CollectionPlanPreviewOut:
    return preview_collection_plan(payload)
