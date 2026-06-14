from app.schemas import ProofGapActionOut, ProofGapOut


ACTION_SURFACE_BOUNDARY = "action_surface_only_not_new_proof_or_gap_closure"


_GAP_ACTIONS = {
    "robust_pdf_extraction": {
        "acceptable_evidence": [
            "use committed_ocr_layout_image_binary_fixture_provenance_v0 as the completed fixture provenance input before OCR adapter work",
            "run opt_in_ocr_adapter_runtime_smoke_v0 only with owner-provided tessdata and explicit NOISEPROOF_ENABLE_PYMUPDF_OCR=true",
            "run a multi-fixture PDF extraction evaluation covering digital text, tables, OCR-like no-text cases, encrypted failures, and layout diagnostics",
            "publish missed spans, failed fixture classes, and boundary-preserving failure candidates",
        ],
        "blocked_claims": [
            "robust PDF extraction is implemented",
            "arbitrary market PDFs are parsed reliably",
            "OCR, table extraction, or layout fidelity is proven",
        ],
        "proof_routes": [
            "docs/review/robust-pdf-extraction-source-first-strategy-review.md",
            "docs/review/pdf-extraction-quality-observation-smoke-index.md",
            "docs/review/upload-pdf-quality-preview-coverage-summary-runtime-smoke.md",
            "docs/review/multi-fixture-pdf-extraction-quality-eval.md",
            "docs/evaluation/multi-fixture-pdf-extraction-quality-report.md",
            "docs/review/missing-pdf-runtime-observation-pack.md",
            "docs/evaluation/missing-pdf-runtime-observation-pack-report.md",
            "docs/review/ocr-layout-image-fixture-adapter-runtime-pack.md",
            "docs/evaluation/ocr-layout-image-fixture-adapter-runtime-pack-report.md",
            "docs/review/committed-ocr-layout-image-binary-fixture-provenance.md",
            "docs/evaluation/committed-ocr-layout-image-binary-fixture-provenance-report.md",
            "docs/review/opt-in-ocr-adapter-runtime-smoke.md",
            "docs/review/opt-in-ocr-adapter-owner-runtime-smoke.md",
            "docs/review/multi-fixture-ocr-adapter-eval.md",
            "docs/evaluation/multi-fixture-ocr-adapter-eval-report.md",
        ],
        "recommended_next_gate": "licensed_real_world_pdf_fixture_pack_v0",
    },
    "actual_embedding_generation": {
        "acceptable_evidence": [
            "run an owner-runtime live provider smoke only when OPENAI_API_KEY is configured by the owner",
            "record model name, embedding dimension, redaction boundary, and non-persistence of secrets",
        ],
        "blocked_claims": [
            "live embedding generation is proven",
            "provider-backed embeddings are available in CI",
            "secrets or provider calls are safe to run by default",
        ],
        "proof_routes": [
            "docs/review/embedding-provider-readiness.md",
            "docs/review/embedding-model-live-provider-harness.md",
        ],
        "recommended_next_gate": "owner_runtime_live_embedding_provider_smoke_v0",
    },
    "semantic_retrieval_quality": {
        "acceptable_evidence": [
            "run a live embedding-backed domain qrels quality evaluation beyond caller-provided fixture vectors",
            "record missed relevant chunks, unjudged retrieved documents, pass conditions, embedding provenance, and claim boundaries",
        ],
        "blocked_claims": [
            "semantic retrieval quality is proven",
            "caller-provided vectors prove answer quality",
            "toy qrels-backed evaluation proves production-grade semantic search",
        ],
        "proof_routes": [
            "docs/review/live-embedding-domain-qrels-owner-runtime-runner.md",
            "docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet.md",
            "docs/evaluation/representative-live-semantic-quality-report.md",
            "docs/review/representative-live-semantic-quality-eval.md",
            "docs/evaluation/live-semantic-qrels-baseline-report.md",
            "docs/review/live-semantic-qrels-baseline-eval.md",
            "docs/evaluation/live-lexical-qrels-baseline-report.md",
            "docs/review/live-lexical-qrels-baseline-eval.md",
            "docs/evaluation/qrels-backed-semantic-quality-report.md",
            "docs/review/qrels-backed-semantic-quality-eval.md",
            "docs/review/semantic-retrieval-quality-diagnostic-matrix.md",
            "docs/evaluation/retrieval-eval-report.md",
        ],
        "recommended_next_gate": "owner_runtime_live_embedding_domain_qrels_eval_v0",
    },
    "distributed_tracing": {
        "acceptable_evidence": [
            "propagate trace context across at least two services",
            "export spans to an external collector or equivalent trace backend",
        ],
        "blocked_claims": [
            "distributed tracing is implemented",
            "local in-memory spans prove cross-service tracing",
            "external collector integration exists",
        ],
        "proof_routes": [
            "docs/review/local-otel-span-export.md",
            "docs/review/local-otel-span-export-runtime-smoke.md",
        ],
        "recommended_next_gate": "external_collector_trace_propagation_smoke_v0",
    },
    "hosted_observability": {
        "acceptable_evidence": [
            "declare a hosted target and show logs, metrics, and traces from that hosted environment",
            "document access boundaries and what operational signal remains local-only",
        ],
        "blocked_claims": [
            "hosted observability is implemented",
            "local ops dashboard is hosted observability",
            "logs, traces, and metrics are externally available",
        ],
        "proof_routes": [
            "docs/runbook.md",
            "docs/review/local-otel-span-export-runtime-smoke.md",
        ],
        "recommended_next_gate": "hosted_observability_target_review_v0",
    },
    "hosted_deployment": {
        "acceptable_evidence": [
            "declare one hosted runtime target and record public or reviewer-accessible health evidence",
            "document deployment rollback, secrets, and environment boundaries",
        ],
        "blocked_claims": [
            "NoiseProof is hosted",
            "local Docker and GitHub Actions prove deployment",
            "production readiness is proven",
        ],
        "proof_routes": [
            "docs/runbook.md",
            "docs/review/application-ready-review.md",
        ],
        "recommended_next_gate": "hosted_runtime_target_health_smoke_v0",
    },
    "external_reviewer_feedback": {
        "acceptable_evidence": [
            "collect a qualifying outside reviewer comment that is not authored by the repository owner",
            "screen the comment for actionable feedback, timestamps, author boundary, and non-draft status",
        ],
        "blocked_claims": [
            "external reviewer feedback exists",
            "owner-authored comments close the feedback gate",
            "workflow screen success is external validation",
        ],
        "proof_routes": [
            "docs/review/external-feedback-current-state-local-otel-issue-verification.md",
            "docs/review/external-reviewer-request-brief.md",
            "https://github.com/svy04/noiseproof-agent/issues/1",
        ],
        "recommended_next_gate": "external_reviewer_feedback_v0",
    },
}


def build_current_proof_gap_registry() -> list[ProofGapOut]:
    return [
        ProofGapOut(
            gap_id="robust_pdf_extraction",
            status="unproven",
            current_evidence=(
                "digital_pdf_text_diagnostics_plus_multi_fixture_gap_matrix_plus_missing_runtime_observation_pack_plus_ocr_layout_image_adapter_runtime_pack_plus_committed_ocr_layout_image_binary_fixture_provenance_plus_opt_in_ocr_adapter_runtime_smoke_harness_plus_owner_runtime_pymupdf_ocr_smoke_with_tessdata_plus_multi_fixture_ocr_adapter_eval_v0"
            ),
            claim_boundary=(
                "pdf_preview_and_table_candidate_metadata_do_not_prove_robust_pdf_extraction"
            ),
            next_evidence_needed=(
                "licensed_real_world_pdf_fixture_pack_v0"
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
            current_evidence=(
                "representative_local_semantic_quality_eval_with_caller_provided_vectors_plus_owner_runtime_domain_qrels_packet_and_runner"
            ),
            claim_boundary=(
                "representative_local_fixture_and_caller_provided_vectors_do_not_prove_production_semantic_retrieval_quality"
            ),
            next_evidence_needed=(
                "owner_runtime_live_embedding_domain_qrels_eval_with_embedding_provenance_and_pass_conditions"
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


def build_proof_gap_actions() -> list[ProofGapActionOut]:
    actions = []
    for gap in build_current_proof_gap_registry():
        detail = _GAP_ACTIONS[gap.gap_id]
        actions.append(
            ProofGapActionOut(
                **gap.model_dump(),
                acceptable_evidence=detail["acceptable_evidence"],
                blocked_claims=detail["blocked_claims"],
                proof_routes=detail["proof_routes"],
                recommended_next_gate=detail["recommended_next_gate"],
                action_boundary=ACTION_SURFACE_BOUNDARY,
            )
        )
    return actions


def get_proof_gap_action(gap_id: str) -> ProofGapActionOut | None:
    return next(
        (gap for gap in build_proof_gap_actions() if gap.gap_id == gap_id),
        None,
    )


def proof_gap_action_surface_notes() -> list[str]:
    return [
        "This surface turns known proof gaps into next-evidence routes.",
        "It does not close gaps, add new runtime proof, or claim external validation.",
        "Gap closure still requires the acceptable evidence named for each gap.",
    ]
