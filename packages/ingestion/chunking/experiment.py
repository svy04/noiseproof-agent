import csv
import re
from io import StringIO
from statistics import mean

from packages.ingestion.types import ChunkOptions, ChunkRecord, ChunkStrategyResult, ParseResult

HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def compare_chunk_strategies(
    parsed: ParseResult,
    options: ChunkOptions | None = None,
) -> list[ChunkStrategyResult]:
    if not parsed.text.strip():
        return []

    safe_options = _normalize_options(options or ChunkOptions())
    return [
        _fixed_window(parsed.text, safe_options),
        _heading_aware(parsed.text, safe_options),
        _row_aware(parsed, safe_options),
    ]


def _fixed_window(text: str, options: ChunkOptions) -> ChunkStrategyResult:
    chunks = [
        _chunk_record("fixed-window", index, chunk, {"start": start, "end": end})
        for index, (chunk, start, end) in enumerate(_window_text(text, options))
    ]
    return ChunkStrategyResult(
        strategy="fixed-window",
        chunks=chunks,
        metrics=_metrics(chunks, text, options, boundary_count=0),
        warnings=[],
    )


def _heading_aware(text: str, options: ChunkOptions) -> ChunkStrategyResult:
    sections = _markdown_sections(text)
    warnings: list[str] = []
    if not sections:
        warnings.append("No markdown headings detected; heading-aware strategy fell back to fixed windows.")
        fallback = _fixed_window(text, options)
        return ChunkStrategyResult(
            strategy="heading-aware",
            chunks=[
                ChunkRecord(
                    strategy="heading-aware",
                    chunk_index=chunk.chunk_index,
                    text=chunk.text,
                    character_count=chunk.character_count,
                    approximate_token_count=chunk.approximate_token_count,
                    metadata={**chunk.metadata, "header_path": None, "fallback": "fixed-window"},
                )
                for chunk in fallback.chunks
            ],
            metrics={**fallback.metrics, "boundary_count": 0},
            warnings=warnings,
        )

    chunk_records: list[ChunkRecord] = []
    for section in sections:
        for chunk, start, end in _window_text(section["text"], options):
            chunk_records.append(
                _chunk_record(
                    "heading-aware",
                    len(chunk_records),
                    chunk,
                    {
                        "header_path": section["header_path"],
                        "heading_level": section["heading_level"],
                        "start": start,
                        "end": end,
                    },
                )
            )

    return ChunkStrategyResult(
        strategy="heading-aware",
        chunks=chunk_records,
        metrics=_metrics(chunk_records, text, options, boundary_count=len(sections)),
        warnings=warnings,
    )


def _row_aware(parsed: ParseResult, options: ChunkOptions) -> ChunkStrategyResult:
    warnings: list[str] = []
    rows = [row for row in csv.reader(StringIO(parsed.text)) if any(cell.strip() for cell in row)]
    if parsed.source_type != "csv":
        warnings.append("Source type is not CSV; row-aware strategy used non-empty text lines as row boundaries.")
        rows = [[line] for line in parsed.text.splitlines() if line.strip()]

    if not rows:
        return ChunkStrategyResult(
            strategy="row-aware",
            chunks=[],
            metrics=_metrics([], parsed.text, options, boundary_count=0),
            warnings=["No rows or non-empty lines were available for row-aware chunking."],
        )

    headers = rows[0] if parsed.source_type == "csv" else []
    data_rows = rows[1:] if parsed.source_type == "csv" else rows
    chunks: list[ChunkRecord] = []
    for row_index, row in enumerate(data_rows, start=1):
        row_text = ",".join(row) if parsed.source_type == "csv" else row[0]
        chunk_text = f"{','.join(headers)}\n{row_text}" if headers else row_text
        for chunk, start, end in _window_text(chunk_text, options):
            chunks.append(
                _chunk_record(
                    "row-aware",
                    len(chunks),
                    chunk,
                    {
                        "headers": headers,
                        "row_start": row_index,
                        "row_end": row_index,
                        "start": start,
                        "end": end,
                    },
                )
            )

    return ChunkStrategyResult(
        strategy="row-aware",
        chunks=chunks,
        metrics=_metrics(chunks, parsed.text, options, boundary_count=len(data_rows)),
        warnings=warnings,
    )


def _markdown_sections(text: str) -> list[dict]:
    sections: list[dict] = []
    current_lines: list[str] = []
    current_path: list[str] = []
    current_level = 0
    path_by_level: dict[int, str] = {}

    def flush() -> None:
        nonlocal current_lines
        section_text = "\n".join(current_lines).strip()
        if section_text and current_path:
            sections.append(
                {
                    "text": section_text,
                    "header_path": "/".join(current_path),
                    "heading_level": current_level,
                }
            )
        current_lines = []

    for line in text.splitlines():
        match = HEADING_PATTERN.match(line)
        if match:
            flush()
            level = len(match.group(1))
            title = match.group(2).strip()
            path_by_level[level] = title
            for stale_level in [key for key in path_by_level if key > level]:
                del path_by_level[stale_level]
            current_path = [path_by_level[key] for key in sorted(path_by_level)]
            current_level = level
        current_lines.append(line)

    flush()
    return sections


def _window_text(text: str, options: ChunkOptions) -> list[tuple[str, int, int]]:
    text = text.strip()
    if not text:
        return []

    max_characters = options.max_characters
    overlap = min(max(options.overlap, 0), max_characters - 1)
    windows: list[tuple[str, int, int]] = []
    start = 0
    while start < len(text):
        hard_end = min(start + max_characters, len(text))
        end = _soft_break(text, start, hard_end)
        chunk = text[start:end].strip()
        if chunk:
            windows.append((chunk, start, end))
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return windows


def _soft_break(text: str, start: int, hard_end: int) -> int:
    if hard_end >= len(text):
        return len(text)
    break_candidates = [
        text.rfind("\n\n", start, hard_end),
        text.rfind("\n", start, hard_end),
        text.rfind(" ", start, hard_end),
    ]
    best = max(break_candidates)
    if best <= start:
        return hard_end
    return best


def _chunk_record(
    strategy: str,
    index: int,
    text: str,
    metadata: dict,
) -> ChunkRecord:
    clean_text = text.strip()
    return ChunkRecord(
        strategy=strategy,
        chunk_index=index,
        text=clean_text,
        character_count=len(clean_text),
        approximate_token_count=_approximate_tokens(len(clean_text)),
        metadata=metadata,
    )


def _metrics(
    chunks: list[ChunkRecord],
    source_text: str,
    options: ChunkOptions,
    boundary_count: int,
) -> dict:
    character_counts = [chunk.character_count for chunk in chunks]
    return {
        "chunk_count": len(chunks),
        "source_character_count": len(source_text),
        "source_line_count": len(source_text.splitlines()),
        "min_character_count": min(character_counts, default=0),
        "max_character_count": max(character_counts, default=0),
        "average_character_count": round(mean(character_counts), 2) if character_counts else 0,
        "empty_chunk_count": sum(1 for count in character_counts if count == 0),
        "oversized_chunk_count": sum(1 for count in character_counts if count > options.max_characters),
        "estimated_token_count": sum(chunk.approximate_token_count for chunk in chunks),
        "boundary_count": boundary_count,
        "max_characters": options.max_characters,
        "overlap": options.overlap,
    }


def _approximate_tokens(character_count: int) -> int:
    if character_count <= 0:
        return 0
    return max(1, (character_count + 3) // 4)


def _normalize_options(options: ChunkOptions) -> ChunkOptions:
    max_characters = max(1, min(options.max_characters, 4000))
    overlap = max(0, min(options.overlap, max_characters - 1))
    return ChunkOptions(max_characters=max_characters, overlap=overlap)
