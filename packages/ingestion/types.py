from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class DocumentProfileInput:
    source_type: str
    text: str
    filename: str | None = None
    source_uri: str | None = None


@dataclass(frozen=True)
class DocumentProfile:
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
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ParseInput:
    source_type: str
    content: str = ""
    filename: str | None = None
    source_uri: str | None = None


@dataclass(frozen=True)
class FailureCaseCandidate:
    failure_type: str
    description: str
    root_cause: str | None = None
    next_action: str | None = None


@dataclass(frozen=True)
class ParseResult:
    source_type: str
    parser: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    failure_case_candidate: FailureCaseCandidate | None = None


@dataclass(frozen=True)
class ChunkOptions:
    max_characters: int = 500
    overlap: int = 0


@dataclass(frozen=True)
class ChunkRecord:
    strategy: str
    chunk_index: int
    text: str
    character_count: int
    approximate_token_count: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ChunkStrategyResult:
    strategy: str
    chunks: list[ChunkRecord]
    metrics: dict[str, Any]
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RetrievalSource:
    source_id: str
    source_type: str
    content: str
    filename: str | None = None
    source_uri: str | None = None


@dataclass(frozen=True)
class RetrievalCandidate:
    source_id: str
    source_type: str
    chunk_strategy: str
    chunk_index: int
    text: str
    score: float
    matched_terms: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RetrievalExperimentResult:
    question: str
    strategy: str
    results: list[RetrievalCandidate]
    result_count: int
    missing_evidence_count: int
    hit_rate: float
    citation_coverage: float
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CollectionPlan:
    question: str
    information_need: str
    possible_claims: list[str]
    required_roles: list[str]
    source_types_to_check: list[str]
    minimum_evidence_needed: str
    known_risks: list[str]
    stop_conditions: list[str]
    warnings: list[str] = field(default_factory=list)
