def source_provenance_from_ledger_entries(
    ledger_entries: list[dict],
) -> dict:
    for entry in ledger_entries:
        metadata = entry.get("metadata_json") or {}
        source_retrieval_mode = metadata.get("source_retrieval_mode")
        source_query_vector_source = metadata.get("source_query_vector_source")
        source_is_semantic = metadata.get("source_is_semantic_retrieval_run")
        source_boundary = metadata.get("source_retrieval_persistence_boundary")
        if not any(
            [
                source_retrieval_mode,
                source_query_vector_source,
                source_is_semantic,
                source_boundary,
            ]
        ):
            continue
        return {
            "source_retrieval_mode": source_retrieval_mode,
            "source_query_vector_source": source_query_vector_source,
            "source_is_semantic_retrieval_run": source_is_semantic,
            "source_retrieval_persistence_boundary": source_boundary,
            "handoff_performs_semantic_retrieval": False,
        }
    return {}


def source_provenance_warnings(source_provenance: dict) -> list[str]:
    warnings = []
    source_retrieval_mode = source_provenance.get("source_retrieval_mode")
    source_query_vector_source = source_provenance.get("source_query_vector_source")
    source_boundary = source_provenance.get("source_retrieval_persistence_boundary")
    if source_retrieval_mode:
        warnings.append(f"Source retrieval run mode: {source_retrieval_mode}.")
    if source_query_vector_source:
        warnings.append(f"Source query vector source: {source_query_vector_source}.")
    if source_boundary:
        warnings.append(f"Source retrieval persistence boundary: {source_boundary}.")
    if source_provenance:
        warnings.append(
            "Source retrieval provenance was preserved from linked Evidence Ledger rows."
        )
    return warnings
