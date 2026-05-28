from fastapi import APIRouter

from app.schemas import HealthOut
from app.settings import get_settings

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthOut)
def health() -> HealthOut:
    settings = get_settings()
    return HealthOut(
        status="ok",
        service=settings.service_name,
        workflow_version=settings.workflow_version,
    )
