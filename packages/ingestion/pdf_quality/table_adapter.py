from typing import Any


PDF_TABLE_ADAPTER_BOUNDARY = (
    "pymupdf_table_adapter_output_only_not_robust_pdf_extraction; "
    "adapter output only; not robust PDF extraction"
)
PDF_TABLE_ADAPTER_ENGINE = "pymupdf-find_tables-extract"
PDF_TABLE_ADAPTER_WARNING = (
    "PyMuPDF table extraction adapter output only; robust PDF extraction is not claimed."
)


def extract_pdf_tables_with_pymupdf(content: bytes) -> dict[str, Any]:
    result = _empty_result()

    if not content:
        result["failure_case_candidate"] = "pdf_table_adapter_empty_content"
        result["warnings"].append("PDF table adapter received empty content.")
        return result

    try:
        import pymupdf
    except ImportError:
        result["failure_case_candidate"] = "pdf_table_adapter_engine_unavailable"
        result["warnings"].append("PyMuPDF is unavailable; table extraction was not attempted.")
        return result

    try:
        document = pymupdf.open(stream=content, filetype="pdf")
    except Exception:
        result["failure_case_candidate"] = "pdf_table_adapter_open_failed"
        result["warnings"].append("PyMuPDF could not open the PDF for table extraction.")
        return result

    try:
        result["page_count"] = document.page_count
        if getattr(document, "needs_pass", False):
            result["failure_case_candidate"] = "pdf_encrypted_requires_password"
            result["warnings"].append(
                "PDF is encrypted and requires a password; table extraction was not attempted."
            )
            return result

        tables: list[list[list[str]]] = []
        table_shapes: list[dict[str, int]] = []
        diagnostics_available = True

        for page_index, page in enumerate(document):
            try:
                finder = page.find_tables()
                page_tables = list(getattr(finder, "tables", []) or [])
            except Exception:
                diagnostics_available = False
                result["warnings"].append(
                    f"PyMuPDF table extraction failed on page {page_index}."
                )
                continue

            for table_index, table in enumerate(page_tables):
                try:
                    rows = _normalize_rows(table.extract())
                except Exception:
                    result["warnings"].append(
                        f"PyMuPDF table.extract() failed for page {page_index} table {table_index}."
                    )
                    continue
                if not rows:
                    continue
                tables.append(rows)
                table_shapes.append(
                    {
                        "page_index": page_index,
                        "table_index": table_index,
                        "row_count": len(rows),
                        "col_count": max((len(row) for row in rows), default=0),
                        "cell_count": sum(len(row) for row in rows),
                    }
                )

        result["table_diagnostics_available"] = diagnostics_available
        result["tables"] = tables
        result["table_shapes"] = table_shapes
        result["table_count"] = len(tables)
        result["extracted_table_rows"] = [row for table in tables for row in table]
        result["table_rows_extracted"] = len(result["extracted_table_rows"])
        result["table_cell_count"] = sum(
            len(row) for row in result["extracted_table_rows"]
        )

        if not tables:
            result["failure_case_candidate"] = "pdf_no_tables_found"
            result["warnings"].append("No tables were extracted from the PDF.")
            return result

        result["table_extraction_performed"] = True
        result["warnings"].append(PDF_TABLE_ADAPTER_WARNING)
        return result
    finally:
        document.close()


def _empty_result() -> dict[str, Any]:
    return {
        "table_extraction_engine": PDF_TABLE_ADAPTER_ENGINE,
        "boundary": PDF_TABLE_ADAPTER_BOUNDARY,
        "robust_pdf_extraction": False,
        "table_extraction_performed": False,
        "table_diagnostics_available": False,
        "page_count": 0,
        "table_count": 0,
        "tables": [],
        "table_shapes": [],
        "extracted_table_rows": [],
        "table_rows_extracted": 0,
        "table_cell_count": 0,
        "warnings": [],
        "failure_case_candidate": None,
    }


def _normalize_rows(value: object) -> list[list[str]]:
    if not isinstance(value, list):
        return []
    rows: list[list[str]] = []
    for row in value:
        if not isinstance(row, list):
            continue
        normalized_row = [_normalize_cell(cell) for cell in row]
        if any(cell for cell in normalized_row):
            rows.append(normalized_row)
    return rows


def _normalize_cell(value: object) -> str:
    if value is None:
        return ""
    return " ".join(str(value).strip().split())
