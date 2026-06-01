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
    UploadEvidencePreviewOut,
    UploadFailureCaseDraftPreviewOut,
    UploadIntakeManifestPreviewOut,
    UploadedFileIntakeManifestCreate,
    UploadedFileIntakeManifestOut,
    UploadNoiseGatePreviewOut,
    UploadPreviewOut,
    UploadReportPreviewOut,
    UploadRetrievalPreviewOut,
)
from app.services.chunk_preview import preview_chunks
from app.services.document_profiler import profile_document
from app.services.parse_preview import preview_parse
from app.services.run_trace import run_with_trace
from app.services.upload_chunk_preview import preview_uploaded_chunks
from app.services.upload_evidence_preview import preview_uploaded_evidence
from app.services.upload_failure_case_draft_preview import preview_uploaded_failure_case_draft
from app.services.upload_intake_manifest_preview import preview_uploaded_intake_manifest
from app.services.upload_noise_gate_preview import preview_uploaded_noise_gate
from app.services.upload_preview import preview_upload
from app.services.upload_report_preview import preview_uploaded_report
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


@router.post("/upload-intake-manifest-preview", response_model=UploadIntakeManifestPreviewOut)
async def upload_document_intake_manifest_preview(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> UploadIntakeManifestPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-intake-manifest-preview",
        user_question=f"upload intake manifest preview: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "preview_only_not_persisted",
        },
        operation=lambda _agent_run_id: preview_uploaded_intake_manifest(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        ),
    )


@router.post(
    "/upload-intake-manifests",
    response_model=UploadedFileIntakeManifestOut,
    status_code=201,
)
async def upload_document_intake_manifest(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_uploaded_intake_manifest(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        )
        payload = UploadedFileIntakeManifestCreate(
            content_sha256=preview.content_sha256,
            filename=preview.filename,
            source_type=preview.source_type,
            content_type=preview.content_type,
            size_bytes=preview.byte_count,
            parser=preview.parser,
            profile_json=preview.profile.model_dump(),
            storage_decision=preview.storage_decision,
            replayable=preview.replayable,
            persistence_boundary="manifest_only_no_raw_file_storage",
            warnings_json=preview.warnings,
        )
        return repository.create_uploaded_file_intake_manifest(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-intake-manifests",
        user_question=f"upload intake manifest persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "manifest_only_no_raw_file_storage",
            "raw_file_storage": False,
        },
        operation=operation,
    )


@router.get(
    "/upload-intake-manifests",
    response_model=list[UploadedFileIntakeManifestOut],
)
def list_upload_document_intake_manifests(
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_uploaded_file_intake_manifests(limit=limit))


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


@router.post("/upload-evidence-preview", response_model=UploadEvidencePreviewOut)
async def upload_document_evidence_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadEvidencePreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-evidence-preview",
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
        operation=lambda _agent_run_id: preview_uploaded_evidence(
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


@router.post("/upload-noise-gate-preview", response_model=UploadNoiseGatePreviewOut)
async def upload_document_noise_gate_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadNoiseGatePreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-noise-gate-preview",
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
        operation=lambda _agent_run_id: preview_uploaded_noise_gate(
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


@router.post("/upload-report-preview", response_model=UploadReportPreviewOut)
async def upload_document_report_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadReportPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-report-preview",
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
        operation=lambda _agent_run_id: preview_uploaded_report(
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


@router.post("/upload-failure-case-draft-preview", response_model=UploadFailureCaseDraftPreviewOut)
async def upload_document_failure_case_draft_preview(
    file: UploadFile = File(...),
    question: str = Form(...),
    source_type: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    top_k: int = Form(default=5),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> UploadFailureCaseDraftPreviewOut:
    content = await file.read()

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-failure-case-draft-preview",
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
        operation=lambda _agent_run_id: preview_uploaded_failure_case_draft(
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
