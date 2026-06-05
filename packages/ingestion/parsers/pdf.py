from typing import Any

from packages.ingestion.parsers.base import empty_content_failure
from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult

PDF_FALLBACK_WARNING = "PDF parser is currently a text-only fallback; robust PDF extraction is not claimed."
PDF_TEXT_EXTRACTION_WARNING = (
    "PDF text extraction uses PyMuPDF for digital text only; OCR, table extraction, and layout fidelity are not claimed."
)
PDF_TABLE_CANDIDATE_WARNING = (
    "PyMuPDF table candidate diagnostics found potential tables but does not extract table contents."
)
PDF_TABLE_DIAGNOSTIC_UNAVAILABLE_WARNING = (
    "PyMuPDF table candidate diagnostics were unavailable for at least one page."
)


class PdfParser:
    name = "pdf-text-fallback"
    source_types = {"pdf"}

    def parse(self, payload: ParseInput) -> ParseResult:
        if payload.content_bytes:
            extracted = _extract_pdf_text(payload.content_bytes)
            if extracted is not None:
                text, metadata, diagnostic_warnings = extracted
                warnings = [PDF_TEXT_EXTRACTION_WARNING]
                warnings.extend(diagnostic_warnings)
                failure_case_candidate: FailureCaseCandidate | None = None
                if not text:
                    warnings.append("PyMuPDF opened the PDF, but no digital text was extracted.")
                    failure_case_candidate = FailureCaseCandidate(
                        failure_type="pdf_no_extractable_text",
                        description="PDF text extraction produced an empty text result.",
                        root_cause="The PDF may be scanned, image-only, encrypted, or otherwise lacking embedded digital text.",
                        next_action="Use OCR or a more specialized PDF extraction stage before claiming PDF text coverage.",
                    )
                return ParseResult(
                    source_type="pdf",
                    parser="pdf-pymupdf",
                    text=text,
                    metadata={
                        "robust_pdf_extraction": False,
                        "text_only_fallback": False,
                        "digital_pdf_text_extraction": True,
                        "extraction_engine": "PyMuPDF",
                        **metadata,
                    },
                    warnings=warnings,
                    failure_case_candidate=failure_case_candidate,
                )

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
                "digital_pdf_text_extraction": False,
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


def _extract_pdf_text(content: bytes) -> tuple[str, dict[str, Any], list[str]] | None:
    try:
        import pymupdf
    except ImportError:
        return None

    try:
        document = pymupdf.open(stream=content, filetype="pdf")
    except Exception:
        return None

    try:
        page_text: list[str] = []
        page_text_char_counts: list[int] = []
        text_block_count = 0
        image_block_count = 0
        layout_block_diagnostics_available = True
        table_candidate_diagnostics_available = True
        table_candidate_count = 0
        table_candidate_page_counts: list[int] = []
        table_candidate_shapes: list[dict[str, int]] = []
        warnings: list[str] = []

        for page_index, page in enumerate(document):
            text = page.get_text().strip()
            page_text.append(text)
            page_text_char_counts.append(len(text))
            try:
                blocks = page.get_text("dict").get("blocks", [])
            except Exception:
                layout_block_diagnostics_available = False
                continue
            text_block_count += sum(1 for block in blocks if block.get("type") == 0)
            image_block_count += sum(1 for block in blocks if block.get("type") == 1)
            try:
                finder = page.find_tables()
                tables = list(getattr(finder, "tables", []) or [])
            except Exception:
                table_candidate_diagnostics_available = False
                table_candidate_page_counts.append(0)
                continue

            table_candidate_page_counts.append(len(tables))
            table_candidate_count += len(tables)
            for table in tables:
                row_count = _non_negative_int(getattr(table, "row_count", 0))
                col_count = _non_negative_int(getattr(table, "col_count", 0))
                table_candidate_shapes.append(
                    {
                        "page_index": page_index,
                        "row_count": row_count,
                        "col_count": col_count,
                        "cell_count": row_count * col_count,
                    }
                )

        if not layout_block_diagnostics_available:
            warnings.append("PyMuPDF layout block diagnostics were unavailable for at least one page.")
        if not table_candidate_diagnostics_available:
            warnings.append(PDF_TABLE_DIAGNOSTIC_UNAVAILABLE_WARNING)
        if table_candidate_count > 0:
            warnings.append(PDF_TABLE_CANDIDATE_WARNING)

        extracted_page_count = sum(1 for count in page_text_char_counts if count > 0)
        metadata = {
            "page_count": document.page_count,
            "page_diagnostics_available": True,
            "layout_block_diagnostics_available": layout_block_diagnostics_available,
            "extraction_scope": "digital_text_page_diagnostics",
            "page_text_char_counts": page_text_char_counts,
            "extracted_page_count": extracted_page_count,
            "empty_page_count": document.page_count - extracted_page_count,
            "text_block_count": text_block_count,
            "image_block_count": image_block_count,
            "table_candidate_diagnostics_available": table_candidate_diagnostics_available,
            "table_candidate_count": table_candidate_count,
            "table_candidate_page_counts": table_candidate_page_counts,
            "table_candidate_shapes": table_candidate_shapes,
            "table_extraction_performed": False,
        }
        return "\n".join(text for text in page_text if text), metadata, warnings
    except Exception:
        return None
    finally:
        document.close()


def _non_negative_int(value: object) -> int:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return max(value, 0)
    return 0
