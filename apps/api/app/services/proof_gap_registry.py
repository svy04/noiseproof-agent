from app.schemas import ProofGapOut


def build_current_proof_gap_registry() -> list[ProofGapOut]:
    return [
        ProofGapOut(
            gap_id="robust_pdf_extraction",
            status="unproven",
            current_evidence="digital_pdf_text_and_diagnostics_only",
            claim_boundary=(
                "pdf_preview_and_table_candidate_metadata_do_not_prove_robust_pdf_extraction"
            ),
            next_evidence_needed=(
                "multi_fixture_pdf_eval_with_ocr_layout_tables_and_failure_boundaries"
            ),
        ),
        ProofGapOut(
            gap_id="actual_embedding_generation",
            status="unproven",
            current_evidence="owner_runtime_gated_provider_path_without_live_call_proof",
            claim_boundary=(
                "mocked_or_readiness_paths_are_not_live_embedding_generation_evidence"
            ),
            next_evidence_needed=(
                "owner_runtime_live_provider_smoke_with_secret_redaction_and_dimension_check"
            ),
        ),
        ProofGapOut(
            gap_id="semantic_retrieval_quality",
            status="unproven",
            current_evidence="toy_fixture_and_caller_provided_vector_runs",
            claim_boundary=(
                "caller_provided_vector_runs_are_operational_counts_not_quality_evidence"
            ),
            next_evidence_needed=(
                "quality_eval_with_qrels_missed_relevant_chunks_and_claim_gate_pass_conditions"
            ),
        ),
        ProofGapOut(
            gap_id="distributed_tracing",
            status="not_claimed",
            current_evidence="local_in_memory_otel_span_export_only",
            claim_boundary=(
                "local_in_memory_spans_are_not_distributed_tracing_or_cross_service_proof"
            ),
            next_evidence_needed=(
                "multi_service_trace_propagation_with_external_collector_or_equivalent"
            ),
        ),
        ProofGapOut(
            gap_id="hosted_observability",
            status="not_implemented",
            current_evidence="local_observability_surfaces_only",
            claim_boundary=(
                "local_dashboard_and_span_export_are_not_hosted_observability"
            ),
            next_evidence_needed=(
                "explicit_hosted_target_with_logs_traces_metrics_and_access_boundary"
            ),
        ),
        ProofGapOut(
            gap_id="hosted_deployment",
            status="not_implemented",
            current_evidence="local_docker_and_github_actions_only",
            claim_boundary="local_runtime_and_remote_ci_are_not_hosted_deployment_evidence",
            next_evidence_needed=(
                "declared_hosted_environment_with_health_check_and_runbook"
            ),
        ),
        ProofGapOut(
            gap_id="external_reviewer_feedback",
            status="pending",
            current_evidence="owner_authored_issue_only",
            claim_boundary=(
                "owner_comments_issue_edits_and_workflow_screens_do_not_close_external_feedback"
            ),
            next_evidence_needed="qualifying outside reviewer comment",
        ),
    ]


def proof_gap_registry_note() -> str:
    return (
        "Proof gap registry is a current gaps only; not new proof surface. "
        "External reviewer feedback remains pending until a qualifying outside "
        "reviewer comment exists."
    )
