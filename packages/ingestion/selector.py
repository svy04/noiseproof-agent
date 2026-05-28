from packages.ingestion.parsers import CsvParser, HtmlParser, MarkdownParser, PdfParser
from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult

PARSERS = [
    MarkdownParser(),
    CsvParser(),
    HtmlParser(),
    PdfParser(),
]

SOURCE_TYPE_ALIASES = {
    "md": "markdown",
    "memo": "markdown",
    "url": "html",
}


def parse_document(payload: ParseInput) -> ParseResult:
    source_type = _normalize_source_type(payload.source_type)
    normalized_payload = ParseInput(
        source_type=source_type,
        content=payload.content,
        filename=payload.filename,
        source_uri=payload.source_uri,
    )

    parser = _select_parser(source_type)
    if parser is None:
        return ParseResult(
            source_type=source_type,
            parser="unknown",
            text="",
            metadata={},
            warnings=[f"No parser adapter is available for source_type '{source_type}'."],
            failure_case_candidate=FailureCaseCandidate(
                failure_type="unknown_source_type",
                description=f"No parser adapter is available for source_type '{source_type}'.",
                root_cause="The requested source type is outside the Phase 3 parser boundary.",
                next_action="Add a parser adapter or normalize the source type before chunking.",
            ),
        )

    return parser.parse(normalized_payload)


def _normalize_source_type(source_type: str) -> str:
    normalized = (source_type or "unknown").lower().strip() or "unknown"
    return SOURCE_TYPE_ALIASES.get(normalized, normalized)


def _select_parser(source_type: str):
    for parser in PARSERS:
        if source_type in parser.source_types:
            return parser
    return None
