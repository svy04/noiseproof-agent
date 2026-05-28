from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import DocumentCreate, DocumentOut, DocumentProfileOut, DocumentProfileRequest
from app.services.document_profiler import profile_document

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("", response_model=DocumentOut, status_code=201)
def create_document(
    payload: DocumentCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_document(payload)


@router.get("", response_model=list[DocumentOut])
def list_documents(repository: Repository = Depends(get_repository)) -> list[dict]:
    return list(repository.list_documents())


@router.post("/profile", response_model=DocumentProfileOut)
def profile_document_text(payload: DocumentProfileRequest) -> DocumentProfileOut:
    return profile_document(payload)
