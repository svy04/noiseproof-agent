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
