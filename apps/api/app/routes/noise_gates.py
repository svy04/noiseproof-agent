from fastapi import APIRouter

from app.schemas import NoiseGatePreviewOut, NoiseGatePreviewRequest
from app.services.noise_gate import preview_noise_gate

router = APIRouter(prefix="/noise-gates", tags=["noise-gates"])


@router.post("/preview", response_model=NoiseGatePreviewOut)
def create_noise_gate_preview(payload: NoiseGatePreviewRequest) -> NoiseGatePreviewOut:
    return preview_noise_gate(payload)
