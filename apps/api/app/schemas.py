from datetime import date, datetime
from decimal import Decimal
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


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


class RetrievalRunResponse(RetrievalRunOut):
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


class EvidenceLedgerStoredEntryOut(EvidenceLedgerEntryOut):
    id: UUID
    question: str
    run_id: UUID | None = None
    workflow_trace_id: UUID
    agent_run_id: UUID | None = None
    workflow_run_id: UUID | None = None
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
    workflow_version: str = "phase32-workflow-lineage-read-model"
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
    workflow_version: str = "phase32-workflow-lineage-read-model"
    status: str = "created"
    trace_json: dict[str, Any] = Field(default_factory=dict)
    started_at: datetime | None = None
    ended_at: datetime | None = None
    latency_ms: int | None = None
    error_message: str | None = None


class WorkflowRunOut(WorkflowRunCreate):
    id: UUID
    created_at: datetime


class WorkflowRunDetailSummaryOut(BaseModel):
    retrieval_run_count: int
    evidence_ledger_entry_count: int
    noise_gate_record_count: int
    report_record_count: int


class WorkflowRunDetailOut(BaseModel):
    workflow_run: WorkflowRunOut
    retrieval_runs: list[RetrievalRunOut]
    evidence_ledger_entries: list[EvidenceLedgerStoredEntryOut]
    noise_gate_records: list[NoiseGateStoredRecordOut]
    report_records: list[ReportStoredRecordOut]
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
    missing_reference_count: int


class WorkflowLineageOut(BaseModel):
    workflow_run: WorkflowRunOut
    lineage_boundary: str
    evidence_ledger_entries: list[EvidenceLedgerStoredEntryOut]
    noise_gate_lineage: list[WorkflowNoiseGateLineageOut]
    report_lineage: list[WorkflowReportLineageOut]
    summary: WorkflowLineageSummaryOut
    warnings: list[str]


class FailureCaseCreate(BaseModel):
    agent_run_id: UUID | None = None
    failure_type: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    root_cause: str | None = None
    fix_status: str = "open"
    next_action: str | None = None


class FailureCaseOut(FailureCaseCreate):
    id: UUID
    created_at: datetime


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
    noise_gate_record_count: int = 0
    blocked_gate_count: int = 0
    revision_gate_count: int = 0
    report_record_count: int = 0
    generated_report_count: int = 0
    blocked_report_count: int = 0
    revision_report_count: int = 0
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
