from fastapi import APIRouter, Depends, File, Form, UploadFile

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
    UploadChunkPreviewOut,
    UploadPreviewOut,
    UploadRetrievalPreviewOut,
)
from app.services.chunk_preview import preview_chunks
from app.services.document_profiler import profile_document
from app.services.parse_preview import preview_parse
from app.services.run_trace import run_with_trace
from app.services.upload_chunk_preview import preview_uploaded_chunks
from app.services.upload_preview import preview_upload
from app.services.upload_retrieval_preview import preview_uploaded_retrieval

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


@router.post("/upload-preview", response_model=UploadPreviewOut)
async def upload_document_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> UploadPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-preview",
        user_question=f"upload preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_upload(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        ),
    )


@router.post("/upload-chunk-preview", response_model=UploadChunkPreviewOut)
async def upload_document_chunk_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadChunkPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-chunk-preview",
        user_question=f"upload chunk preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_chunks(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            max_characters=max_characters,
            overlap=overlap,
        ),
    )


@router.post("/upload-retrieval-preview", response_model=UploadRetrievalPreviewOut)
async def upload_document_retrieval_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadRetrievalPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-retrieval-preview",
        user_question=question,
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "top_k": top_k,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_retrieval(
            question=question,
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            strategy=strategy,
            top_k=top_k,
            max_characters=max_characters,
            overlap=overlap,
        ),
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
