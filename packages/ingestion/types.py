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
    content_bytes: bytes | None = None
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
    content_bytes: bytes | None = None
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


@dataclass(frozen=True)
class EvidenceLedgerCandidate:
    source_id: str | None
    source_type: str | None
    chunk_strategy: str | None
    chunk_index: int | None
    text: str
    score: float = 0.0
    matched_terms: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EvidenceLedgerEntry:
    claim: str
    source_id: str | None
    source_type: str | None
    source_date: str | None
    evidence_span: str
    confidence: str
    limitation: str
    contradicting_source_ids: list[str]
    status: str
    matched_terms: list[str] = field(default_factory=list)
    role: str = "direct_support"
    metadata_json: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EvidenceLedgerSummary:
    supported_count: int
    weakly_supported_count: int
    contradicted_count: int
    unsupported_count: int
    blocked_count: int
    source_count: int


@dataclass(frozen=True)
class EvidenceLedger:
    question: str
    entries: list[EvidenceLedgerEntry]
    summary: EvidenceLedgerSummary
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class NoiseGateCheck:
    name: str
    status: str
    message: str


@dataclass(frozen=True)
class NoiseGateResult:
    question: str
    decision: str
    final_response_allowed: bool
    checks: list[NoiseGateCheck]
    blocked_claims: list[str]
    downgraded_claims: list[str]
    allowed_claims: list[str]
    required_revisions: list[str]
    fallback_message: str | None
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ReportClaim:
    claim: str
    source_ids: list[str]
    evidence_spans: list[str]
    confidence: str
    limitations: list[str]
    contradictions: list[str]


@dataclass(frozen=True)
class ClaimBoundedReport:
    summary: str
    claims: list[ReportClaim]
    limitations: list[str]
    contradictions: list[str]
    next_data_needed: list[str]


@dataclass(frozen=True)
class ReportPreview:
    question: str
    status: str
    report: ClaimBoundedReport | None
    gate: NoiseGateResult
    fallback_message: str | None
    required_revisions: list[str]
    warnings: list[str] = field(default_factory=list)
