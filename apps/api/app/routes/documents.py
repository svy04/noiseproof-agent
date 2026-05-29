from fastapi import APIRouter, Depends

from app.db import Repository, get_repository
from app.schemas import (
    ChunkPreviewOut,
    ChunkPreviewRequest,
    DocumentCreate,
    DocumentOut,
    DocumentProfileOut,
    DocumentProfileRequest,
    ParsePreviewOut,
    ParsePreviewRequest,
)
from app.services.chunk_preview import preview_chunks
from app.services.document_profiler import profile_document
from app.services.parse_preview import preview_parse
from app.services.run_trace import run_with_trace

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
def profile_document_text(
    payload: DocumentProfileRequest,
    repository: Repository = Depends(get_repository),
) -> DocumentProfileOut:
    def operation(_agent_run_id) -> DocumentProfileOut:
        return profile_document(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/profile",
        user_question=f"profile document: {payload.source_type}",
        trace_json={"source_type": payload.source_type},
        operation=operation,
    )


@router.post("/parse-preview", response_model=ParsePreviewOut)
def parse_document_preview(
    payload: ParsePreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ParsePreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/parse-preview",
        user_question=f"parse preview: {payload.source_type}",
        trace_json={"source_type": payload.source_type},
        operation=lambda _agent_run_id: preview_parse(payload),
    )


@router.post("/chunk-preview", response_model=ChunkPreviewOut)
def chunk_document_preview(
    payload: ChunkPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ChunkPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/chunk-preview",
        user_question=f"chunk preview: {payload.source_type}",
        trace_json={
            "source_type": payload.source_type,
            "max_characters": payload.max_characters,
            "overlap": payload.overlap,
        },
        operation=lambda _agent_run_id: preview_chunks(payload),
    )
