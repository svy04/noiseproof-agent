from dataclasses import asdict
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.profiler import profile_text
from packages.ingestion.selector import parse_document
from packages.ingestion.types import DocumentProfileInput, ParseInput

from app.schemas import DocumentProfileOut, ParsePreviewOut, ParsePreviewRequest


def preview_parse(payload: ParsePreviewRequest) -> ParsePreviewOut:
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

    return ParsePreviewOut(
        source_type=parsed.source_type,
        parser=parsed.parser,
        text=parsed.text,
        metadata=parsed.metadata,
        warnings=parsed.warnings,
        failure_case_candidate=(
            asdict(parsed.failure_case_candidate)
            if parsed.failure_case_candidate is not None
            else None
        ),
        profile=DocumentProfileOut(**profile.__dict__),
    )
