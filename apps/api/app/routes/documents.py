from hashlib import sha256
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile

from app.db import Repository, get_repository
from app.schemas import (
    ChunkPreviewOut,
    ChunkPreviewRequest,
    DocumentChunkCreate,
    DocumentChunkOut,
    DocumentChunkRequest,
    DocumentCreate,
    DocumentOut,
    DocumentProfileOut,
    DocumentProfileRequest,
    DocumentRetrievalRunRequest,
    ParsePreviewOut,
    ParsePreviewRequest,
    RawFileScanResultCreate,
    RawFileScanResultOut,
    RetrievalRunResponse,
    SemanticRetrievalPreviewOut,
    SemanticRetrievalPreviewRequest,
    SemanticRetrievalRunRequest,
    UploadChunkPreviewOut,
    UploadChunkPersistenceOut,
    UploadEvidencePreviewOut,
    UploadFailureCaseDraftPreviewOut,
    UploadIntakeManifestPreviewOut,
    UploadedFileIntakeManifestCreate,
    UploadedFileIntakeManifestOut,
    UploadedRawFileCreate,
    UploadedRawFileOut,
    UploadNoiseGatePreviewOut,
    UploadPreviewOut,
    UploadReportPreviewOut,
    UploadRetrievalPreviewOut,
)
from app.settings import Settings, get_settings
from app.services.chunk_preview import preview_chunks
from app.services.document_chunk_retrieval import run_document_chunk_retrieval
from app.services.document_profiler import profile_document
from app.services.parse_preview import preview_parse
from app.services.run_trace import run_with_trace
from app.services.semantic_retrieval_preview import preview_semantic_retrieval
from app.services.semantic_retrieval_run import run_semantic_retrieval
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


@router.post("/{document_id}/chunks", response_model=DocumentChunkOut, status_code=201)
def create_document_chunk(
    document_id: UUID,
    payload: DocumentChunkRequest,
    repository: Repository = Depends(get_repository),
) -> dict:
    return repository.create_document_chunk(
        DocumentChunkCreate(document_id=document_id, **payload.model_dump())
    )


@router.get("/{document_id}/chunks", response_model=list[DocumentChunkOut])
def list_document_chunks(
    document_id: UUID,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_document_chunks(document_id=document_id, limit=limit))


@router.post(
    "/{document_id}/retrieval-runs",
    response_model=RetrievalRunResponse,
    status_code=201,
)
def create_document_retrieval_run(
    document_id: UUID,
    payload: DocumentRetrievalRunRequest,
    repository: Repository = Depends(get_repository),
) -> RetrievalRunResponse:
    return run_document_chunk_retrieval(document_id, payload, repository)


@router.post(
    "/{document_id}/semantic-retrieval-preview",
    response_model=SemanticRetrievalPreviewOut,
)
def semantic_retrieval_preview(
    document_id: UUID,
    payload: SemanticRetrievalPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> SemanticRetrievalPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /documents/{document_id}/semantic-retrieval-preview",
        user_question=payload.question,
        trace_json={
            "document_id": str(document_id),
            "retrieval_mode": "semantic_preview",
            "persistence_boundary": "preview_only_not_persisted",
            "query_vector_source": "caller_provided_vector",
        },
        operation=lambda _agent_run_id: preview_semantic_retrieval(
            document_id=document_id,
            payload=payload,
            repository=repository,
        ),
    )


@router.post(
    "/{document_id}/semantic-retrieval-runs",
    response_model=RetrievalRunResponse,
    status_code=201,
)
def create_semantic_retrieval_run(
    document_id: UUID,
    payload: SemanticRetrievalRunRequest,
    repository: Repository = Depends(get_repository),
) -> RetrievalRunResponse:
    return run_with_trace(
        repository,
        endpoint="POST /documents/{document_id}/semantic-retrieval-runs",
        user_question=payload.question,
        trace_json={
            "document_id": str(document_id),
            "retrieval_mode": "semantic_persisted",
            "persistence_boundary": "semantic_retrieval_run_only_no_evidence_ledger",
            "query_vector_source": "caller_provided_vector",
        },
        operation=lambda _agent_run_id: run_semantic_retrieval(
            document_id=document_id,
            payload=payload,
            repository=repository,
        ),
    )


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


@router.post(
    "/upload-raw-files",
    response_model=UploadedRawFileOut,
    status_code=201,
)
async def upload_document_raw_file(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
) -> dict:
    content = await file.read()
    byte_count = len(content)
    if byte_count > settings.max_raw_upload_bytes:
        raise HTTPException(
            status_code=413,
            detail=(
                f"raw upload size {byte_count} exceeds max_raw_upload_bytes "
                f"{settings.max_raw_upload_bytes}"
            ),
        )

    warnings = [
        "Raw upload storage is quarantine-only and stores bytes in PostgreSQL bytea.",
        "The original filename is recorded as metadata only and is not used as a storage key.",
        "No download endpoint, malware scan, robust PDF extraction, parsing guarantee, or hosted deployment evidence is claimed.",
    ]
    payload = UploadedRawFileCreate(
        content_sha256=sha256(content).hexdigest(),
        storage_key=uuid4().hex,
        filename=file.filename,
        source_type=source_type or "unknown",
        content_type=file.content_type,
        size_bytes=byte_count,
        storage_backend="postgres_bytea",
        quarantine_status="stored_quarantined",
        persistence_boundary="raw_upload_quarantine_db_bytea_no_download_endpoint",
        raw_file_storage=True,
        raw_bytes=content,
        warnings_json=warnings,
    )
    return repository.create_uploaded_raw_file(payload)


@router.get(
    "/upload-raw-files",
    response_model=list[UploadedRawFileOut],
)
def list_upload_document_raw_files(
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(repository.list_uploaded_raw_files(limit=limit))


@router.post(
    "/upload-raw-files/{raw_file_id}/scan-results",
    response_model=RawFileScanResultOut,
    status_code=201,
)
def create_upload_raw_file_scan_result(
    raw_file_id: UUID,
    payload: RawFileScanResultCreate,
    repository: Repository = Depends(get_repository),
) -> dict:
    if payload.raw_file_id != raw_file_id:
        raise HTTPException(
            status_code=400,
            detail="raw_file_id path/body mismatch",
        )
    return repository.create_raw_file_scan_result(payload)


@router.get(
    "/upload-raw-files/{raw_file_id}/scan-results",
    response_model=list[RawFileScanResultOut],
)
def list_upload_raw_file_scan_results(
    raw_file_id: UUID,
    scan_status: str | None = None,
    scan_verdict: str | None = None,
    limit: int = 20,
    repository: Repository = Depends(get_repository),
) -> list[dict]:
    return list(
        repository.list_raw_file_scan_results(
            raw_file_id=raw_file_id,
            scan_status=scan_status,
            scan_verdict=scan_verdict,
            limit=limit,
        )
    )


@router.post(
    "/upload-parsed-documents",
    response_model=DocumentOut,
    status_code=201,
)
async def upload_parsed_document(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    title: str | None = Form(default=None),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_upload(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
        )
        failure_case_candidate = (
            preview.failure_case_candidate.model_dump()
            if preview.failure_case_candidate
            else None
        )
        parse_warnings = [
            warning
            for warning in preview.warnings
            if "does not create documents" not in warning
        ]
        parse_warnings.append(
            "Upload parsed document persistence stores document metadata/profile only and "
            "does not store raw uploaded bytes or parsed text."
        )
        payload = DocumentCreate(
            source_type=preview.source_type,
            source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
            filename=file.filename,
            title=title or file.filename,
            profile_json={
                "persistence_boundary": "document_metadata_and_profile_only_no_raw_file_storage",
                "raw_file_storage": False,
                "parsed_text_storage": False,
                "parser": preview.parser,
                "metadata": preview.metadata,
                "profile": preview.profile.model_dump(),
                "parse_warnings": parse_warnings,
                "failure_case_candidate": failure_case_candidate,
                "upload": {
                    "filename": preview.filename,
                    "content_type": preview.content_type,
                    "byte_count": preview.byte_count,
                },
            },
            extraction_quality=preview.profile.extraction_quality,
            status="parsed_metadata_only",
        )
        return repository.create_document(payload)

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-parsed-documents",
        user_question=f"upload parsed document persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "persistence_boundary": "document_metadata_and_profile_only_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
        },
        operation=operation,
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


@router.post("/upload-chunks", response_model=UploadChunkPersistenceOut, status_code=201)
async def upload_document_chunks(
    file: UploadFile = File(...),
    source_type: str | None = Form(default=None),
    title: str | None = Form(default=None),
    strategy: str = Form(default="fixed-window"),
    max_characters: int = Form(default=500),
    overlap: int = Form(default=0),
    repository: Repository = Depends(get_repository),
) -> dict:
    content = await file.read()

    def operation(_agent_run_id) -> dict:
        preview = preview_uploaded_chunks(
            filename=file.filename,
            content_type=file.content_type,
            source_type=source_type,
            content=content,
            max_characters=max_characters,
            overlap=overlap,
        )
        selected_strategy = next(
            (
                chunk_strategy
                for chunk_strategy in preview.strategies
                if chunk_strategy.strategy == strategy
            ),
            None,
        )
        if selected_strategy is None and preview.strategies:
            selected_strategy = preview.strategies[0]

        selected_chunks = selected_strategy.chunks if selected_strategy else []
        chunk_strategy_name = selected_strategy.strategy if selected_strategy else strategy
        warnings = [
            warning
            for warning in preview.parse_warnings
            if "does not create documents, chunks, or retrieval runs" not in warning
        ]
        warnings.append(
            "Upload chunk handoff creates document metadata and derived chunk rows only; "
            "it does not store raw uploaded bytes or full parsed text."
        )
        if selected_strategy is None:
            warnings.append(
                "No chunk strategy produced chunks; the document metadata was persisted without chunk rows."
            )

        document = repository.create_document(
            DocumentCreate(
                source_type=preview.source_type,
                source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
                filename=file.filename,
                title=title or file.filename,
                profile_json={
                    "persistence_boundary": "document_metadata_and_chunks_only_no_raw_file_storage",
                    "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
                    "raw_file_storage": False,
                    "parsed_text_storage": False,
                    "parser": preview.parser,
                    "profile": preview.profile.model_dump(),
                    "chunk_strategy": chunk_strategy_name,
                    "chunk_count": len(selected_chunks),
                    "chunk_metrics": selected_strategy.metrics if selected_strategy else {},
                    "chunk_warnings": selected_strategy.warnings if selected_strategy else [],
                    "parse_warnings": warnings,
                    "upload": {
                        "filename": preview.filename,
                        "content_type": preview.content_type,
                        "byte_count": preview.byte_count,
                    },
                },
                extraction_quality=preview.profile.extraction_quality,
                status=(
                    "chunked_metadata_only"
                    if selected_chunks
                    else "chunk_handoff_no_chunks"
                ),
            )
        )

        persisted_chunks = []
        for chunk in selected_chunks:
            metadata = dict(chunk.metadata)
            metadata.update(
                {
                    "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
                    "raw_file_storage": False,
                    "parsed_text_storage": False,
                    "source_profile": preview.profile.model_dump(),
                }
            )
            persisted_chunks.append(
                repository.create_document_chunk(
                    DocumentChunkCreate(
                        document_id=document["id"],
                        source_type=preview.source_type,
                        source_uri=f"upload://{file.filename}" if file.filename else "upload://unnamed",
                        filename=file.filename,
                        chunk_strategy=chunk_strategy_name,
                        chunk_index=chunk.chunk_index,
                        chunk_text=chunk.text,
                        character_start=chunk.metadata.get("start"),
                        character_end=chunk.metadata.get("end"),
                        metadata_json=metadata,
                        persistence_boundary="chunk_text_only_no_raw_file_storage",
                    )
                )
            )

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "source_type": preview.source_type,
            "parser": preview.parser,
            "chunk_strategy": chunk_strategy_name,
            "chunk_count": len(persisted_chunks),
            "persistence_boundary": "chunk_text_only_no_raw_file_storage",
            "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
            "document": document,
            "chunks": persisted_chunks,
            "warnings": warnings,
        }

    return run_with_trace(
        repository,
        endpoint="POST /documents/upload-chunks",
        user_question=f"upload chunks persist: {source_type or file.filename or 'unknown'}",
        trace_json={
            "source_type": source_type,
            "filename": file.filename,
            "content_type": file.content_type,
            "byte_count": len(content),
            "strategy": strategy,
            "max_characters": max_characters,
            "overlap": overlap,
            "persistence_boundary": "chunk_text_only_no_raw_file_storage",
            "handoff_boundary": "explicit_upload_to_chunks_no_raw_file_storage",
            "raw_file_storage": False,
            "parsed_text_storage": False,
        },
        operation=operation,
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
