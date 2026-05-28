import csv
from io import StringIO

from packages.ingestion.parsers.base import empty_content_failure
from packages.ingestion.types import FailureCaseCandidate, ParseInput, ParseResult


class CsvParser:
    name = "csv"
    source_types = {"csv"}

    def parse(self, payload: ParseInput) -> ParseResult:
        text = (payload.content or "").strip()
        warnings: list[str] = []
        failure_case_candidate: FailureCaseCandidate | None = None

        if not text:
            warnings.append("CSV content is empty; parser returned no rows.")
            failure_case_candidate = empty_content_failure("csv")
            rows: list[list[str]] = []
        else:
            rows = [row for row in csv.reader(StringIO(text)) if any(cell.strip() for cell in row)]

        if text and not rows:
            warnings.append("CSV parser found no non-empty rows.")
            failure_case_candidate = FailureCaseCandidate(
                failure_type="csv_no_rows",
                description="CSV content did not produce any non-empty rows.",
                root_cause="Input may not be comma-separated text.",
                next_action="Inspect delimiter and source encoding before chunking.",
            )

        column_count = max((len(row) for row in rows), default=0)
        inconsistent_row_count = sum(1 for row in rows if column_count and len(row) != column_count)

        if rows and "," not in text:
            warnings.append("CSV source type was selected, but comma-separated structure was not detected.")

        if inconsistent_row_count:
            warnings.append("CSV rows have inconsistent column counts; row-aware chunking may need cleanup.")
            failure_case_candidate = FailureCaseCandidate(
                failure_type="csv_inconsistent_rows",
                description="CSV rows have different column counts.",
                root_cause="The source may contain malformed rows, embedded delimiters, or missing values.",
                next_action="Preserve the malformed rows as a failure case before retrieval evaluation.",
            )

        return ParseResult(
            source_type="csv",
            parser=self.name,
            text=text,
            metadata={
                "row_count": len(rows),
                "column_count": column_count,
                "headers": rows[0] if rows else [],
                "inconsistent_row_count": inconsistent_row_count,
            },
            warnings=warnings,
            failure_case_candidate=failure_case_candidate,
        )
