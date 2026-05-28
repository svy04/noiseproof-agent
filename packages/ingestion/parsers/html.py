from html.parser import HTMLParser

from packages.ingestion.parsers.base import empty_content_failure
from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.heading_count = 0
        self._in_heading = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_count += 1
            self._in_heading = True
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self._in_heading = False

    def handle_data(self, data: str) -> None:
        clean = data.strip()
        if clean:
            self.text_parts.append(clean)


class HtmlParser:
    name = "html"
    source_types = {"html", "url"}

    def parse(self, payload: ParseInput) -> ParseResult:
        raw = payload.content or ""
        warnings: list[str] = []
        failure_case_candidate: FailureCaseCandidate | None = None

        if not raw.strip():
            warnings.append("HTML content is empty; parser returned no text.")
            failure_case_candidate = empty_content_failure("html")

        if raw.strip() and "<" not in raw:
            warnings.append("Source type suggests HTML/URL, but no HTML tags were detected.")

        extractor = _TextExtractor()
        try:
            extractor.feed(raw)
        except Exception as exc:  # pragma: no cover - stdlib parser rarely raises here
            warnings.append(f"HTML parser warning: {exc}")
            failure_case_candidate = FailureCaseCandidate(
                failure_type="html_parse_warning",
                description="HTML parser raised while processing preview content.",
                root_cause=str(exc),
                next_action="Store this source as a parser failure example before retrieval.",
            )

        text = "\n".join(extractor.text_parts).strip()
        if raw.strip() and not text:
            warnings.append("HTML parser produced no visible text.")
            failure_case_candidate = FailureCaseCandidate(
                failure_type="html_no_visible_text",
                description="HTML content produced no visible text in preview parsing.",
                root_cause="The source may be script-heavy, empty, or malformed.",
                next_action="Add a parser adapter test before relying on this source.",
            )

        return ParseResult(
            source_type="html",
            parser=self.name,
            text=text,
            metadata={
                "heading_count": extractor.heading_count,
                "link_count": len(extractor.links),
                "links": extractor.links[:10],
            },
            warnings=warnings,
            failure_case_candidate=failure_case_candidate,
        )
