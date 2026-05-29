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


class AgentRunCreate(BaseModel):
    user_question: str = Field(..., min_length=1)
    workflow_version: str = "phase5-retrieval-v0"
    status: str = "created"
    error_message: str | None = None
    token_cost: Decimal | None = None
    latency_ms: int | None = None
    trace_json: dict[str, Any] = Field(default_factory=dict)


class AgentRunOut(AgentRunCreate):
    id: UUID
    started_at: datetime
    ended_at: datetime | None = None


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
    unsupported_claim_count: int
    contradiction_count: int
    average_latency_ms: float | None
    notes: list[str]
