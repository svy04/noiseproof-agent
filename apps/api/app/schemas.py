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


class AgentRunCreate(BaseModel):
    user_question: str = Field(..., min_length=1)
    workflow_version: str = "day2-skeleton"
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
