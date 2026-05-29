import sys
from dataclasses import asdict
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.chunking import compare_chunk_strategies
from packages.ingestion.profiler import profile_text
from packages.ingestion.selector import parse_document
from packages.ingestion.types import ChunkOptions, DocumentProfileInput, ParseInput

from app.schemas import (
    ChunkPreviewOut,
    ChunkPreviewRequest,
    ChunkStrategyOut,
    DocumentProfileOut,
)


def preview_chunks(payload: ChunkPreviewRequest) -> ChunkPreviewOut:
    parsed = parse_document(
        ParseInput(
            source_type=payload.source_type,
            content=payload.content,
            filename=payload.filename,
            source_uri=payload.source_uri,
        )
    )
    profile = profile_text(
        DocumentProfileInput(
            source_type=parsed.source_type,
            text=parsed.text,
            filename=payload.filename,
            source_uri=payload.source_uri,
        )
    )

    strategies = compare_chunk_strategies(
        parsed,
        ChunkOptions(max_characters=payload.max_characters, overlap=payload.overlap),
    )

    return ChunkPreviewOut(
        source_type=parsed.source_type,
        parser=parsed.parser,
        profile=DocumentProfileOut(**profile.__dict__),
        parse_warnings=parsed.warnings,
        failure_case_candidate=(
            asdict(parsed.failure_case_candidate)
            if parsed.failure_case_candidate is not None
            else None
        ),
        strategies=[ChunkStrategyOut(**asdict(strategy)) for strategy in strategies],
    )
