from collections.abc import Mapping
from typing import Any


SEMANTIC_RETRIEVAL_STRATEGY = "semantic-cosine"
SEMANTIC_RETRIEVAL_MODE = "semantic_persisted"


def enrich_retrieval_run_provenance(row: Mapping[str, Any]) -> dict[str, Any]:
    enriched = dict(row)
    metadata = enriched.get("metadata_json")
    if not isinstance(metadata, dict):
        metadata = {}

    retrieval_mode = metadata.get("retrieval_mode")
    enriched["retrieval_mode"] = retrieval_mode
    enriched["query_vector_source"] = metadata.get("query_vector_source")
    enriched["persistence_boundary"] = metadata.get("persistence_boundary")
    enriched["is_semantic_retrieval_run"] = (
        enriched.get("strategy") == SEMANTIC_RETRIEVAL_STRATEGY
        or retrieval_mode == SEMANTIC_RETRIEVAL_MODE
    )
    return enriched
