from datetime import date, datetime
from decimal import Decimal
from typing import Any, Literal
from uuid import UUID

from pydantic import BaseModel, Field, model_validator


class DocumentCreate(BaseModel):
    source_type: str = Field(..., min_length=1)
    source_uri: str | None = None
    filename: str | None = None
    title: str | None = None
    source_date: date | None = None
    profile_json: dict[str, Any] = Field(default_factory=dict)
    extraction_quality: str = "unknown"
    status: str = "registered"


class DocumentOut(DocumentCreate):
    id: UUID
    created_at: datetime


class DocumentProfileRequest(BaseModel):
    source_type: str = Field(..., min_length=1)
    text: str = ""
    filename: str | None = None
    source_uri: str | None = None


class DocumentProfileOut(BaseModel):
    source_type: str
    character_count: int
    line_count: int
    approximate_token_count: int
    has_tables: bool
    has_urls: bool
    has_dates: bool
    has_numbers: bool
    extraction_quality: str
    recommended_strategy: str
    warnings: list[str]


class ParsePreviewRequest(BaseModel):
    source_type: str = Field(..., min_length=1)
    content: str = ""
    filename: str | None = None
    source_uri: str | None = None


class FailureCaseCandidateOut(BaseModel):
    failure_type: str
    description: str
    root_cause: str | None = None
    next_action: str | None = None


class ParsePreviewOut(BaseModel):
    source_type: str
    parser: str
    text: str
    metadata: dict[str, Any]
    warnings: list[str]
    failure_case_candidate: FailureCaseCandidateOut | None = None
    profile: DocumentProfileOut


class UploadPreviewOut(ParsePreviewOut):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str


class UploadIntakeManifestPreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    content_sha256: str
    source_type: str
    parser: str
    profile: DocumentProfileOut
    parse_warnings: list[str]
    manifest: dict[str, Any]
    storage_decision: str
    replayable: bool
    persistence_boundary: str
    warnings: list[str]


class UploadedFileIntakeManifestCreate(BaseModel):
    content_sha256: str = Field(..., min_length=1)
    filename: str | None = None
    source_type: str = Field(..., min_length=1)
    content_type: str | None = None
    size_bytes: int = Field(default=0, ge=0)
    parser: str | None = None
    profile_json: dict[str, Any] = Field(default_factory=dict)
    storage_decision: str = "do_not_persist_raw_upload_yet"
    replayable: bool = False
    persistence_boundary: str = "manifest_only_no_raw_file_storage"
    warnings_json: list[str] = Field(default_factory=list)


class UploadedFileIntakeManifestOut(UploadedFileIntakeManifestCreate):
    id: UUID
    created_at: datetime


class UploadedRawFileMetadata(BaseModel):
    content_sha256: str = Field(..., min_length=1)
    storage_key: str = Field(..., min_length=1)
    filename: str | None = None
    source_type: str = Field(..., min_length=1)
    content_type: str | None = None
    size_bytes: int = Field(default=0, ge=0)
    storage_backend: str = "postgres_bytea"
    quarantine_status: str = "stored_quarantined"
    persistence_boundary: str = "raw_upload_quarantine_db_bytea_guarded_download_endpoint"
    raw_file_storage: bool = True
    warnings_json: list[str] = Field(default_factory=list)


class UploadedRawFileCreate(UploadedRawFileMetadata):
    raw_bytes: bytes


class UploadedRawFileOut(UploadedRawFileMetadata):
    id: UUID
    created_at: datetime


class RawFileScanResultCreate(BaseModel):
    raw_file_id: UUID
    scanner_name: str = Field(..., min_length=1)
    scanner_version: str | None = None
    signature_db_version: str | None = None
    scan_started_at: datetime | None = None
    scan_finished_at: datetime | None = None
    scan_status: str = "pending"
    scan_verdict: str = "pending"
    matched_signature: str | None = None
    error_message: str | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class RawFileScanResultOut(RawFileScanResultCreate):
    id: UUID
    created_at: datetime


class RawFileDownloadEventCreate(BaseModel):
    raw_file_id: UUID
    latest_scan_result_id: UUID | None = None
    download_result: str = Field(..., min_length=1)
    blocked_reason: str | None = None
    http_status_code: int = Field(..., ge=100, le=599)
    authorization_boundary: str = "local_v0_no_auth_not_production"
    rate_limit_boundary: str = "local_v0_in_memory_fixed_window_not_production"
    filename_boundary: str = "local_v0_content_disposition_filename_safety_not_production"
    client_host_boundary: str = "local_request_client_host_not_identity"
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class RawFileDownloadEventOut(RawFileDownloadEventCreate):
    id: UUID
    created_at: datetime


class RawFileDownloadApprovalBase(BaseModel):
    raw_file_id: UUID
    latest_scan_result_id: UUID
    approval_status: Literal["approved", "revoked", "expired"] = "approved"
    approval_reason: str = Field(..., min_length=1)
    approved_by_label: str = Field(..., min_length=1)
    expires_at: datetime
    revoked_at: datetime | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)
    approval_boundary: str = "local_v0_manual_operator_approval_not_production_auth"
    identity_boundary: str = "operator_label_not_authenticated_identity"


class RawFileDownloadApprovalCreate(RawFileDownloadApprovalBase):
    @model_validator(mode="after")
    def approved_status_requires_future_expiry(self) -> "RawFileDownloadApprovalCreate":
        if self.approval_status != "approved":
            return self
        now = datetime.now(self.expires_at.tzinfo)
        if self.expires_at <= now:
            raise ValueError("expires_at must be in the future for approved download approvals")
        return self


class RawFileDownloadApprovalOut(RawFileDownloadApprovalBase):
    id: UUID
    created_at: datetime


class RawFileDownloadReadinessCheckOut(BaseModel):
    name: str
    status: Literal["passed", "failed", "skipped"]
    detail: str
    boundary: str | None = None


class RawFileDownloadReadinessOut(BaseModel):
    raw_file_id: UUID
    decision: Literal["allowed", "blocked"]
    blocked_reason: str | None = None
    http_status_code_if_download_attempted: int = Field(..., ge=100, le=599)
    latest_scan_result_id: UUID | None = None
    active_approval_id: UUID | None = None
    approval_boundary: str | None = None
    identity_boundary: str | None = None
    raw_bytes_returned: bool = False
    rate_limit_consumed: bool = False
    readiness_boundary: str = "download_readiness_preflight_no_raw_bytes_not_authorization"
    authorization_boundary: str = "local_v0_no_auth_not_production"
    rate_limit_boundary: str = "local_v0_in_memory_fixed_window_not_production"
    checks: list[RawFileDownloadReadinessCheckOut]


class DocumentChunkCreate(BaseModel):
    document_id: UUID
    source_type: str = Field(..., min_length=1)
    source_uri: str | None = None
    filename: str | None = None
    chunk_strategy: str = Field(..., min_length=1)
    chunk_index: int = Field(..., ge=0)
    chunk_text: str = Field(..., min_length=1)
    character_start: int | None = Field(default=None, ge=0)
    character_end: int | None = Field(default=None, ge=0)
    metadata_json: dict[str, Any] = Field(default_factory=dict)
    persistence_boundary: str = "chunk_text_only_no_raw_file_storage"


class DocumentChunkOut(DocumentChunkCreate):
    id: UUID
    created_at: datetime


class ChunkEmbeddingCreate(BaseModel):
    chunk_id: UUID
    embedding_model: str = Field(..., min_length=1)
    embedding_dimension: int = Field(..., ge=1)
    embedding_text_hash: str = Field(..., min_length=1)
    distance_metric: str = "cosine"
    embedding_status: str = "planned"
    embedding: list[float] | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class ChunkEmbeddingOut(ChunkEmbeddingCreate):
    id: UUID
    embedding_created_at: datetime
    created_at: datetime


class SemanticRetrievalPreviewRequest(BaseModel):
    question: str = Field(..., min_length=1)
    query_embedding: list[float] = Field(..., min_length=1)
    embedding_model: str = Field(..., min_length=1)
    embedding_dimension: int = Field(..., ge=1)
    limit: int = Field(default=5, ge=1, le=20)


class SemanticRetrievalRunRequest(SemanticRetrievalPreviewRequest):
    pass


class SemanticRetrievalCandidateOut(BaseModel):
    chunk_id: UUID
    embedding_id: UUID
    document_id: UUID
    chunk_index: int
    chunk_strategy: str
    text: str
    distance: float
    distance_metric: str
    embedding_model: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class SemanticRetrievalPreviewOut(BaseModel):
    question: str
    retrieval_mode: str
    persistence_boundary: str
    ranking_boundary: str
    candidates: list[SemanticRetrievalCandidateOut]
    missing_embedding_chunk_ids: list[str]
    warnings: list[str]
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class TextEmbeddingPreviewRequest(BaseModel):
    text: str = Field(..., min_length=1)
    embedding_model: str = "local-hash-embedding-preview-v0"
    embedding_dimension: int = Field(default=8, ge=1, le=4096)
    distance_metric: str = "cosine"


class TextEmbeddingPreviewOut(BaseModel):
    embedding_model: str
    embedding_dimension: int
    embedding_text_hash: str
    distance_metric: str
    embedding_status: str
    embedding: list[float]
    metadata_json: dict[str, Any] = Field(default_factory=dict)
    warnings: list[str]


class EmbeddingModelPreviewRequest(BaseModel):
    text: str = Field(..., min_length=1)
    provider: str = "openai"
    embedding_model: str | None = None
    embedding_dimension: int | None = Field(default=None, ge=1, le=4096)
    encoding_format: str = "float"
    allow_provider_call: bool = False


class EmbeddingModelPreviewOut(BaseModel):
    provider: str
    embedding_model: str
    embedding_dimension: int
    encoding_format: str
    configured: bool
    embedding_status: str
    embedding: list[float] | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)
    warnings: list[str]


class ChunkEmbeddingRequest(BaseModel):
    embedding_model: str = Field(..., min_length=1)
    embedding_dimension: int = Field(..., ge=1)
    embedding_text_hash: str = Field(..., min_length=1)
    distance_metric: str = "cosine"
    embedding_status: str = "planned"
    embedding: list[float] | None = None
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class DocumentChunkRequest(BaseModel):
    source_type: str = Field(..., min_length=1)
    source_uri: str | None = None
    filename: str | None = None
    chunk_strategy: str = Field(..., min_length=1)
    chunk_index: int = Field(..., ge=0)
    chunk_text: str = Field(..., min_length=1)
    character_start: int | None = Field(default=None, ge=0)
    character_end: int | None = Field(default=None, ge=0)
    metadata_json: dict[str, Any] = Field(default_factory=dict)
    persistence_boundary: str = "chunk_text_only_no_raw_file_storage"


class ChunkPreviewRequest(BaseModel):
    source_type: str = Field(..., min_length=1)
    content: str = ""
    filename: str | None = None
    source_uri: str | None = None
    max_characters: int = Field(default=500, ge=1, le=4000)
    overlap: int = Field(default=0, ge=0)


class ChunkOut(BaseModel):
    strategy: str
    chunk_index: int
    text: str
    character_count: int
    approximate_token_count: int
    metadata: dict[str, Any]


class ChunkStrategyOut(BaseModel):
    strategy: str
    chunks: list[ChunkOut]
    metrics: dict[str, Any]
    warnings: list[str]


class ChunkPreviewOut(BaseModel):
    source_type: str
    parser: str
    profile: DocumentProfileOut
    parse_warnings: list[str]
    failure_case_candidate: FailureCaseCandidateOut | None = None
    strategies: list[ChunkStrategyOut]


class UploadChunkPreviewOut(ChunkPreviewOut):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class UploadChunkPersistenceOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    source_type: str
    parser: str
    chunk_strategy: str
    chunk_count: int
    persistence_boundary: str
    handoff_boundary: str
    raw_file_storage: bool
    parsed_text_storage: bool
    document: DocumentOut
    chunks: list[DocumentChunkOut]
    warnings: list[str]


class RetrievalSourceIn(BaseModel):
    source_id: str = Field(..., min_length=1)
    source_type: str = Field(..., min_length=1)
    content: str = ""
    filename: str | None = None
    source_uri: str | None = None


class RetrievalRunRequest(BaseModel):
    question: str = Field(..., min_length=1)
    strategy: str = "fixed-window"
    sources: list[RetrievalSourceIn] = Field(..., min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)
    max_characters: int = Field(default=500, ge=1, le=4000)
    overlap: int = Field(default=0, ge=0)


class DocumentRetrievalRunRequest(BaseModel):
    question: str = Field(..., min_length=1)
    strategy: str = "fixed-window"
    top_k: int = Field(default=5, ge=1, le=20)


class RetrievalRunCreate(BaseModel):
    question: str = Field(..., min_length=1)
    strategy: str = "fixed-window"
    workflow_run_id: UUID | None = None
    status: str = "completed"
    latency_ms: int | None = None
    result_count: int = 0
    hit_rate: float = 0.0
    citation_coverage: float = 0.0
    missing_evidence_count: int = 0
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class RetrievalCandidateOut(BaseModel):
    source_id: str
    source_type: str
    chunk_strategy: str
    chunk_index: int
    text: str
    score: float
    matched_terms: list[str]
    metadata: dict[str, Any]


class RetrievalRunOut(RetrievalRunCreate):
    id: UUID
    created_at: datetime
    is_semantic_retrieval_run: bool = False
    retrieval_mode: str | None = None
    query_vector_source: str | None = None
    persistence_boundary: str | None = None


class RetrievalRunResponse(RetrievalRunOut):
    results: list[RetrievalCandidateOut]
    warnings: list[str]


class UploadRetrievalPreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    source_type: str
    question: str
    strategy: str
    status: str
    result_count: int
    hit_rate: float
    citation_coverage: float
    missing_evidence_count: int
    trading_advice_boundary: str | None = None
    results: list[RetrievalCandidateOut]
    warnings: list[str]


class CollectionPlanPreviewRequest(BaseModel):
    question: str = Field(..., min_length=1)


class CollectionPlanPreviewOut(BaseModel):
    question: str
    information_need: str
    possible_claims: list[str]
    required_roles: list[str]
    source_types_to_check: list[str]
    minimum_evidence_needed: str
    known_risks: list[str]
    stop_conditions: list[str]
    warnings: list[str]


class EvidenceLedgerCandidateIn(BaseModel):
    source_id: str | None = None
    source_type: str | None = None
    chunk_strategy: str | None = None
    chunk_index: int | None = None
    text: str = ""
    score: float = 0.0
    matched_terms: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class EvidenceLedgerPreviewRequest(BaseModel):
    question: str = Field(..., min_length=1)
    retrieval_results: list[EvidenceLedgerCandidateIn] = Field(default_factory=list)


class EvidenceLedgerEntryOut(BaseModel):
    claim: str
    source_id: str | None
    source_type: str | None
    source_date: str | None
    evidence_span: str
    confidence: str
    limitation: str
    contradicting_source_ids: list[str]
    status: str
    matched_terms: list[str]
    role: str
    metadata_json: dict[str, Any] = Field(default_factory=dict)


class EvidenceLedgerSummaryOut(BaseModel):
    supported_count: int
    weakly_supported_count: int
    contradicted_count: int
    unsupported_count: int
    blocked_count: int
    source_count: int


class EvidenceLedgerPreviewOut(BaseModel):
    question: str
    entries: list[EvidenceLedgerEntryOut]
    summary: EvidenceLedgerSummaryOut
    warnings: list[str]


class UploadEvidencePreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    source_type: str
    question: str
    status: str
    retrieval: UploadRetrievalPreviewOut
    evidence: EvidenceLedgerPreviewOut
    warnings: list[str]


class EvidenceLedgerStoredEntryOut(EvidenceLedgerEntryOut):
    id: UUID
    question: str
    run_id: UUID | None = None
    workflow_trace_id: UUID
    agent_run_id: UUID | None = None
    workflow_run_id: UUID | None = None
    retrieval_run_id: UUID | None = None
    created_at: datetime


class EvidenceLedgerPersistedOut(BaseModel):
    question: str
    entries: list[EvidenceLedgerStoredEntryOut]
    summary: EvidenceLedgerSummaryOut
    warnings: list[str]
    stored_entry_count: int


class NoiseGatePreviewRequest(BaseModel):
    question: str = Field(..., min_length=1)
    evidence_entries: list[EvidenceLedgerEntryOut] = Field(default_factory=list)
    draft_claims: list[str] = Field(default_factory=list)


class NoiseGateCheckOut(BaseModel):
    name: str
    status: str
    message: str


class NoiseGatePreviewOut(BaseModel):
    question: str
    decision: str
    final_response_allowed: bool
    checks: list[NoiseGateCheckOut]
    blocked_claims: list[str]
    downgraded_claims: list[str]
    allowed_claims: list[str]
    required_revisions: list[str]
    fallback_message: str | None
    warnings: list[str]


class UploadNoiseGatePreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    source_type: str
    question: str
    status: str
    retrieval: UploadRetrievalPreviewOut
    evidence: EvidenceLedgerPreviewOut
    gate: NoiseGatePreviewOut
    warnings: list[str]


class NoiseGateStoredRecordOut(NoiseGatePreviewOut):
    id: UUID
    workflow_trace_id: UUID
    agent_run_id: UUID | None = None
    workflow_run_id: UUID | None = None
    stage_input_manifest: dict[str, Any] = Field(default_factory=dict)
    evidence_entry_count: int
    draft_claim_count: int
    created_at: datetime


class ReportPreviewRequest(BaseModel):
    question: str = Field(..., min_length=1)
    evidence_entries: list[EvidenceLedgerEntryOut] = Field(default_factory=list)
    draft_claims: list[str] = Field(default_factory=list)


class ReportClaimOut(BaseModel):
    claim: str
    source_ids: list[str]
    evidence_spans: list[str]
    confidence: str
    limitations: list[str]
    contradictions: list[str]


class ClaimBoundedReportOut(BaseModel):
    summary: str
    claims: list[ReportClaimOut]
    limitations: list[str]
    contradictions: list[str]
    next_data_needed: list[str]


class ReportPreviewOut(BaseModel):
    question: str
    status: str
    report: ClaimBoundedReportOut | None
    gate: NoiseGatePreviewOut
    fallback_message: str | None
    required_revisions: list[str]
    warnings: list[str]


class UploadReportPreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    source_type: str
    question: str
    status: str
    retrieval: UploadRetrievalPreviewOut
    evidence: EvidenceLedgerPreviewOut
    report: ReportPreviewOut
    warnings: list[str]


class ReportStoredRecordOut(ReportPreviewOut):
    id: UUID
    workflow_trace_id: UUID
    agent_run_id: UUID | None = None
    workflow_run_id: UUID | None = None
    stage_input_manifest: dict[str, Any] = Field(default_factory=dict)
    gate_decision: str
    claim_count: int
    evidence_entry_count: int
    draft_claim_count: int
    created_at: datetime


class WorkflowStageLinkCreate(BaseModel):
    workflow_run_id: UUID
    workflow_trace_id: UUID
    link_type: str
    from_table: str
    from_id: UUID
    to_table: str
    to_id: UUID
    source_manifest_field: str
    persistence_boundary: str = (
        "workflow_created_records_only_not_standalone_payload_lineage"
    )


class WorkflowStageLinkOut(WorkflowStageLinkCreate):
    id: UUID
    created_at: datetime


class WorkflowRunExecutePreviewRequest(RetrievalRunRequest):
    draft_claims: list[str] = Field(default_factory=list)


class WorkflowRunExecutePreviewOut(BaseModel):
    workflow_run: "WorkflowRunOut"
    workflow_trace_id: UUID
    execution_boundary: str
    retrieval: RetrievalRunResponse
    evidence: EvidenceLedgerPersistedOut
    gate: NoiseGateStoredRecordOut
    report: ReportStoredRecordOut
    warnings: list[str]


class AgentRunCreate(BaseModel):
    user_question: str = Field(..., min_length=1)
    workflow_version: str = "phase40-lineage-warning-code-dashboard"
    status: str = "created"
    error_message: str | None = None
    token_cost: Decimal | None = None
    latency_ms: int | None = None
    trace_json: dict[str, Any] = Field(default_factory=dict)


class AgentRunOut(AgentRunCreate):
    id: UUID
    started_at: datetime
    ended_at: datetime | None = None


class WorkflowRunCreate(BaseModel):
    question: str = Field(..., min_length=1)
    workflow_version: str = "phase40-lineage-warning-code-dashboard"
    status: str = "created"
    trace_json: dict[str, Any] = Field(default_factory=dict)
    started_at: datetime | None = None
    ended_at: datetime | None = None
    latency_ms: int | None = None
    error_message: str | None = None


class WorkflowRunOut(WorkflowRunCreate):
    id: UUID
    created_at: datetime


class WorkflowStageEventCreate(BaseModel):
    workflow_run_id: UUID
    workflow_trace_id: UUID
    stage_name: str = Field(..., min_length=1)
    stage_order: int
    stage_status: str = "completed"
    started_at: datetime
    ended_at: datetime | None = None
    latency_ms: int | None = None
    input_summary_json: dict[str, Any] = Field(default_factory=dict)
    output_summary_json: dict[str, Any] = Field(default_factory=dict)
    event_boundary: str = "local_workflow_stage_event_log_not_distributed_tracing"


class WorkflowStageEventOut(WorkflowStageEventCreate):
    id: UUID
    created_at: datetime


class WorkflowRunDetailSummaryOut(BaseModel):
    retrieval_run_count: int
    evidence_ledger_entry_count: int
    noise_gate_record_count: int
    report_record_count: int
    failure_case_count: int
    workflow_stage_event_count: int = 0


class WorkflowRunDetailOut(BaseModel):
    workflow_run: WorkflowRunOut
    retrieval_runs: list[RetrievalRunOut]
    evidence_ledger_entries: list[EvidenceLedgerStoredEntryOut]
    noise_gate_records: list[NoiseGateStoredRecordOut]
    report_records: list[ReportStoredRecordOut]
    failure_cases: list[dict[str, Any]]
    stage_events: list[WorkflowStageEventOut] = Field(default_factory=list)
    summary: WorkflowRunDetailSummaryOut


class WorkflowNoiseGateLineageOut(BaseModel):
    record: NoiseGateStoredRecordOut
    input_evidence_entry_ids: list[str]
    input_evidence_entries: list[EvidenceLedgerStoredEntryOut]
    missing_evidence_entry_ids: list[str]


class WorkflowReportLineageOut(BaseModel):
    record: ReportStoredRecordOut
    input_evidence_entry_ids: list[str]
    input_evidence_entries: list[EvidenceLedgerStoredEntryOut]
    input_noise_gate_record_id: str | None
    input_noise_gate_record: NoiseGateStoredRecordOut | None
    missing_evidence_entry_ids: list[str]
    missing_noise_gate_record_id: str | None


class WorkflowLineageSummaryOut(BaseModel):
    evidence_ledger_entry_count: int
    noise_gate_record_count: int
    report_record_count: int
    gate_input_evidence_reference_count: int
    report_input_evidence_reference_count: int
    report_input_gate_reference_count: int
    direct_stage_link_count: int
    missing_reference_count: int


class WorkflowLineageOut(BaseModel):
    workflow_run: WorkflowRunOut
    lineage_boundary: str
    evidence_ledger_entries: list[EvidenceLedgerStoredEntryOut]
    noise_gate_lineage: list[WorkflowNoiseGateLineageOut]
    report_lineage: list[WorkflowReportLineageOut]
    direct_stage_links: list[WorkflowStageLinkOut]
    summary: WorkflowLineageSummaryOut
    warnings: list[str]
    warning_codes: list[str]


class FailureCaseCreate(BaseModel):
    agent_run_id: UUID | None = None
    workflow_run_id: UUID | None = None
    failure_type: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    root_cause: str | None = None
    fix_status: str = "open"
    next_action: str | None = None


class FailureCaseOut(FailureCaseCreate):
    id: UUID
    created_at: datetime


class FailureCaseWorkflowPersistenceOut(BaseModel):
    failure_case: FailureCaseOut
    source_summary: dict[str, Any]
    persistence_boundary: str
    warnings: list[str]


class FailureCaseDraftPreviewRequest(BaseModel):
    workflow_run_id: UUID | None = None
    agent_run_id: UUID | None = None
    question: str = Field(..., min_length=1)
    workflow_status: str = Field(..., min_length=1)
    error_message: str | None = None
    trace_json: dict[str, Any] = Field(default_factory=dict)


class FailureCaseDraftPreviewOut(BaseModel):
    draft: FailureCaseCreate
    source_summary: dict[str, Any]
    persistence_boundary: str
    human_confirmation_required: bool
    warnings: list[str]


class FailureCaseWorkflowReviewQueueItemOut(BaseModel):
    workflow_run: WorkflowRunOut
    review_status: str
    linked_failure_case_ids: list[UUID]
    linked_failure_case_count: int
    draft_preview_path: str
    stage: str
    error_type: str
    warnings: list[str]


class FailureCaseWorkflowReviewQueueOut(BaseModel):
    queue_boundary: str
    persistence_boundary: str
    pending_review_count: int
    linked_failure_case_count: int
    items: list[FailureCaseWorkflowReviewQueueItemOut]
    warnings: list[str]


class UploadFailureCaseDraftPreviewOut(BaseModel):
    filename: str | None = None
    content_type: str | None = None
    byte_count: int
    persistence_boundary: str
    source_type: str
    question: str
    status: str
    report: UploadReportPreviewOut
    draft_preview: FailureCaseDraftPreviewOut
    warnings: list[str]


class HealthOut(BaseModel):
    status: str
    service: str
    workflow_version: str


class OpsSummaryOut(BaseModel):
    status: str
    workflow_version: str
    document_count: int
    agent_run_count: int
    failure_case_count: int
    retrieval_run_count: int = 0
    semantic_retrieval_run_count: int = 0
    chunk_embedding_count: int = 0
    caller_provided_embedding_count: int = 0
    noise_gate_record_count: int = 0
    blocked_gate_count: int = 0
    revision_gate_count: int = 0
    report_record_count: int = 0
    generated_report_count: int = 0
    blocked_report_count: int = 0
    revision_report_count: int = 0
    chunk_handoff_no_chunks_count: int = 0
    pdf_no_text_failure_candidate_count: int = 0
    pdf_encrypted_failure_candidate_count: int = 0
    uploaded_raw_file_count: int = 0
    raw_file_scan_result_count: int = 0
    raw_file_clean_scan_count: int = 0
    raw_file_scan_error_count: int = 0
    raw_file_download_approval_count: int = 0
    active_download_approval_count: int = 0
    raw_file_download_event_count: int = 0
    blocked_download_event_count: int = 0
    allowed_download_event_count: int = 0
    unsupported_claim_count: int
    contradiction_count: int
    average_latency_ms: float | None
    notes: list[str]


class TraceLookupSummaryOut(BaseModel):
    agent_run_count: int
    evidence_ledger_entry_count: int
    noise_gate_record_count: int
    report_record_count: int


class TraceLookupOut(BaseModel):
    workflow_trace_id: UUID
    agent_runs: list[AgentRunOut]
    evidence_ledger_entries: list[EvidenceLedgerStoredEntryOut]
    noise_gate_records: list[NoiseGateStoredRecordOut]
    report_records: list[ReportStoredRecordOut]
    summary: TraceLookupSummaryOut


class WorkflowProofChecklistItemOut(BaseModel):
    check_id: str
    proof_surface: str | None
    status: str
    inspection_goal: str
    boundary: str


class WorkflowProofBundleOut(BaseModel):
    workflow_run: WorkflowRunOut
    workflow_trace_id: UUID | None
    bundle_boundary: str
    detail: WorkflowRunDetailOut
    lineage: WorkflowLineageOut
    trace: TraceLookupOut | None
    proof_surfaces: list[str]
    reviewer_checklist: list[WorkflowProofChecklistItemOut]
    warnings: list[str]
