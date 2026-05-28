from packages.ingestion.parsers.base import empty_content_failure
from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult

PDF_FALLBACK_WARNING = "PDF parser is currently a text-only fallback; robust PDF extraction is not claimed."


class PdfParser:
    name = "pdf-text-fallback"
    source_types = {"pdf"}

    def parse(self, payload: ParseInput) -> ParseResult:
        text = (payload.content or "").strip()
        warnings = [PDF_FALLBACK_WARNING]
        failure_case_candidate: FailureCaseCandidate | None = None

        if not text:
            warnings.append("PDF preview content is empty; parser returned no text.")
            failure_case_candidate = empty_content_failure("pdf")
        elif _looks_binary(text):
            warnings.append("PDF preview content looks binary or corrupted; text extraction was not performed.")
            failure_case_candidate = FailureCaseCandidate(
                failure_type="pdf_binary_preview",
                description="PDF preview received binary-looking content instead of extracted text.",
                root_cause="Phase 3 does not implement real PDF extraction.",
                next_action="Add a tested PDF extraction adapter before claiming PDF parsing quality.",
            )

        return ParseResult(
            source_type="pdf",
            parser=self.name,
            text=text,
            metadata={
                "robust_pdf_extraction": False,
                "text_only_fallback": True,
            },
            warnings=warnings,
            failure_case_candidate=failure_case_candidate,
        )


def _looks_binary(text: str) -> bool:
    if "\x00" in text:
        return True
    if not text:
        return False
    control_count = sum(1 for char in text if ord(char) < 32 and char not in "\n\r\t")
    return (control_count / max(len(text), 1)) > 0.05
