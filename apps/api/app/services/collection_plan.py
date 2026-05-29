from dataclasses import asdict
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[4]
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from app.schemas import CollectionPlanPreviewOut, CollectionPlanPreviewRequest
from packages.ingestion.collection import create_collection_plan


def preview_collection_plan(payload: CollectionPlanPreviewRequest) -> CollectionPlanPreviewOut:
    plan = create_collection_plan(payload.question)
    return CollectionPlanPreviewOut(**asdict(plan))
