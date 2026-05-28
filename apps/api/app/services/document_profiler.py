import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from packages.ingestion.profiler import profile_text
from packages.ingestion.types import DocumentProfileInput

from app.schemas import DocumentProfileRequest, DocumentProfileOut


def profile_document(payload: DocumentProfileRequest) -> DocumentProfileOut:
    profile = profile_text(
        DocumentProfileInput(
            source_type=payload.source_type,
            text=payload.text,
            filename=payload.filename,
            source_uri=payload.source_uri,
        )
    )
    return DocumentProfileOut(**profile.__dict__)
