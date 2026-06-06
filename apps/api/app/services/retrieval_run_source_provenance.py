def source_provenance_from_ledger_entries(
    ledger_entries: list[dict],
) -> dict:
    provenance = {}
    for entry in ledger_entries:
        metadata = entry.get("metadata_json") or {}
        source_retrieval_mode = metadata.get("source_retrieval_mode")
        source_query_vector_source = metadata.get("source_query_vector_source")
        source_is_semantic = metadata.get("source_is_semantic_retrieval_run")
        source_boundary = metadata.get("source_retrieval_persistence_boundary")
        if any(
            [
                source_retrieval_mode,
                source_query_vector_source,
                source_is_semantic,
                source_boundary,
            ]
        ):
            provenance.update(
                {
                    "source_retrieval_mode": source_retrieval_mode,
                    "source_query_vector_source": source_query_vector_source,
                    "source_is_semantic_retrieval_run": source_is_semantic,
                    "source_retrieval_persistence_boundary": source_boundary,
                    "handoff_performs_semantic_retrieval": False,
                }
            )

        if _has_pdf_table_adapter_metadata(metadata):
            provenance.update(
                {
                    "default_pdf_parser_table_adapter_metadata": bool(
                        metadata.get("default_pdf_parser_table_adapter_metadata")
                    ),
                    "table_adapter": metadata.get("table_adapter") or {},
                    "table_adapter_boundary": metadata.get("table_adapter_boundary"),
                    "table_adapter_extraction_performed": metadata.get(
                        "table_adapter_extraction_performed"
                    ),
                    "table_extraction_performed": metadata.get(
                        "table_extraction_performed"
                    ),
                    "source_provenance_boundary": metadata.get(
                        "source_provenance_boundary"
                    ),
                    "source_pdf_table_adapter_provenance_boundary": (
                        "noise_gate_stage_input_manifest_from_evidence_ledger_entry_metadata"
                    ),
                    "handoff_performs_pdf_table_extraction": False,
                }
            )

        if provenance:
            return provenance
    return provenance


def source_provenance_warnings(source_provenance: dict) -> list[str]:
    warnings = []
    source_retrieval_mode = source_provenance.get("source_retrieval_mode")
    source_query_vector_source = source_provenance.get("source_query_vector_source")
    source_boundary = source_provenance.get("source_retrieval_persistence_boundary")
    has_pdf_table_adapter = source_provenance.get(
        "default_pdf_parser_table_adapter_metadata"
    ) or source_provenance.get("table_adapter")
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
    if has_pdf_table_adapter:
        warnings.append(
            "Uploaded PDF table-adapter metadata was preserved into Noise Gate "
            "stage_input_manifest as provenance only."
        )
        warnings.append(
            "Noise Gate handoff does not perform PDF table extraction and is not "
            "robust PDF extraction evidence."
        )
    return warnings


def _has_pdf_table_adapter_metadata(metadata: dict) -> bool:
    return bool(
        metadata.get("default_pdf_parser_table_adapter_metadata")
        or metadata.get("table_adapter")
        or metadata.get("table_adapter_boundary")
        or metadata.get("table_adapter_extraction_performed")
    )
