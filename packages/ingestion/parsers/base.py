from typing import Protocol

from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult


class Parser(Protocol):
    name: str
    source_types: set[str]

    def parse(self, payload: ParseInput) -> ParseResult:
        ...


def empty_content_failure(source_type: str) -> FailureCaseCandidate:
    return FailureCaseCandidate(
        failure_type="empty_parse_input",
        description=f"No content was provided for {source_type} parsing.",
        root_cause="The parse-preview request had empty content.",
        next_action="Provide extracted text or fixture content before parsing.",
    )
