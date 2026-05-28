from dataclasses import dataclass, field


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
