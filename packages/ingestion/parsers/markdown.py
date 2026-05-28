import re

from packages.ingestion.parsers.base import empty_content_failure
from packages.ingestion.types import ParseInput, ParseResult

HEADING_PATTERN = re.compile(r"(?m)^#{1,6}\s+\S")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\([^)]+\)|https?://\S+", re.IGNORECASE)
BULLET_PATTERN = re.compile(r"(?m)^\s*(?:[-*+]|\d+\.)\s+\S")


class MarkdownParser:
    name = "markdown"
    source_types = {"markdown", "md", "memo"}

    def parse(self, payload: ParseInput) -> ParseResult:
        text = (payload.content or "").strip()
        warnings: list[str] = []
        failure_case_candidate = None

        if not text:
            warnings.append("Markdown content is empty; parser returned no text.")
            failure_case_candidate = empty_content_failure("markdown")

        return ParseResult(
            source_type=_normalize_source_type(payload.source_type),
            parser=self.name,
            text=text,
            metadata={
                "heading_count": len(HEADING_PATTERN.findall(text)),
                "link_count": len(LINK_PATTERN.findall(text)),
                "bullet_count": len(BULLET_PATTERN.findall(text)),
            },
            warnings=warnings,
            failure_case_candidate=failure_case_candidate,
        )


def _normalize_source_type(source_type: str) -> str:
    normalized = source_type.lower().strip() or "markdown"
    if normalized in {"md", "memo"}:
        return "markdown"
    return normalized
