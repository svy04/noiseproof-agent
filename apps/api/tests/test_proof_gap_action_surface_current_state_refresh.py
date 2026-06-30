from pathlib import Path

from app.main import app
from fastapi.testclient import TestClient


REPO_ROOT = Path(__file__).resolve().parents[3]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_proof_gap_action_surface_advances_after_table_extraction_evidence_gate():
    client = TestClient(app)

    response = client.get("/ops/proof-gaps")

    assert response.status_code == 200
    body = response.json()
    robust_gap = next(
        gap for gap in body["gaps"] if gap["gap_id"] == "robust_pdf_extraction"
    )
    assert body["surface_boundary"] == (
        "action_surface_only_not_new_proof_or_gap_closure"
    )
    assert robust_gap["recommended_next_gate"] == (
        "source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0"
    )
    assert robust_gap["next_evidence_needed"] == (
        "source_policy_no_native_text_ocr_owner_runtime_rights_request_delivery_v0"
    )
    assert (
        "multi_real_world_pdf_parse_observation_matrix_remote_verification_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "robust_pdf_extraction_next_real_world_quality_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "cross_publisher_real_world_pdf_fixture_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_table_extraction_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_ocr_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_layout_fidelity_evidence_gate_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "robust_pdf_extraction_generalization_gap_review_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "multi_publisher_modality_stratified_pdf_eval_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "targeted_real_world_pdf_fixture_expansion_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "real_world_pdf_fixture_source_policy_download_hash_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_pdf_parse_observation_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_pdf_parse_quality_matrix_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_pdf_quality_gap_review_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_failure_route_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_readiness_review_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_dependency_check_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_dependency_resolution_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_execution_plan_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_execution_smoke_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_quality_eval_plan_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_quality_reference_pack_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_marker_proxy_eval_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_transcript_reference_plan_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_transcript_reference_pack_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_source_rights_review_request_packet_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_owner_rights_decision_record_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "source_policy_no_native_text_ocr_rights_request_delivery_record_v0"
        in robust_gap["current_evidence"]
    )
    assert (
        "docs/review/multi-real-world-pdf-parse-observation-remote-verification.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/robust-pdf-extraction-next-real-world-quality-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/robust-pdf-real-world-quality-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/cross-publisher-real-world-pdf-fixture-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-table-extraction-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-table-extraction-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-ocr-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-ocr-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/real-world-layout-fidelity-evidence-gate.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/robust-pdf-generalization-gap-review.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/robust-pdf-generalization-gap-review-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/multi-publisher-modality-stratified-pdf-eval.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/multi-publisher-modality-stratified-pdf-eval-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/targeted-real-world-pdf-fixture-expansion.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-download-hash.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-download-hash-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-pdf-parse-observation.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-pdf-parse-observation-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-pdf-parse-quality-matrix.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-pdf-parse-quality-matrix-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-pdf-quality-gap-review.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-pdf-quality-gap-review-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-failure-route.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-failure-route-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-readiness-review.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-readiness-review-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-dependency-check.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-dependency-check-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-dependency-resolution.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-dependency-resolution-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-execution-plan.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-execution-plan-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-execution-smoke.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-execution-smoke-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-quality-eval-plan.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-quality-eval-plan-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-quality-reference-pack.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-quality-reference-pack-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-marker-proxy-eval.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-marker-proxy-eval-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/review/source-policy-no-native-text-ocr-transcript-reference-plan.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "docs/evaluation/source-policy-no-native-text-ocr-transcript-reference-plan-report.md"
        in robust_gap["proof_routes"]
    )
    assert (
        "record one bounded source-policy no-native-text OCR execution smoke before OCR quality evaluation"
        in robust_gap["acceptable_evidence"]
    )
    assert (
        "plan OCR quality evaluation with required reference inputs before scoring OCR output"
        in robust_gap["acceptable_evidence"]
    )
    assert (
        "record a marker-anchor reference pack before any OCR quality proxy check"
        in robust_gap["acceptable_evidence"]
    )
    assert (
        "run a marker-presence proxy eval before any transcript-backed OCR quality plan"
        in robust_gap["acceptable_evidence"]
    )
    assert (
        "plan the transcript/reference boundary before creating any transcript reference pack"
        in robust_gap["acceptable_evidence"]
    )
    assert (
        "record rights request delivery route candidates and missing owner-runtime delivery evidence before request_sent can be claimed"
        in robust_gap["acceptable_evidence"]
    )
    assert "robust PDF extraction is implemented" in robust_gap["blocked_claims"]


def test_proof_gap_action_refresh_docs_are_linked_and_bounded():
    marker = "proof_gap_action_surface_current_state_refresh_v0"
    review_path = "docs/review/proof-gap-action-surface-current-state-refresh.md"
    spec_path = "docs/specs/2026-06-30-proof-gap-action-surface-current-state-refresh.md"

    surfaces = [
        _read("README.md"),
        _read("docs/GOAL.md"),
        _read("docs/runbook.md"),
        _read("docs/application/portfolio-index.md"),
        _read("docs/review/proof-gap-action-surface.md"),
        _read(review_path),
        _read(spec_path),
    ]

    for surface in surfaces:
        assert marker in surface
        assert "robust_pdf_extraction_next_real_world_quality_gate_v0" in surface

    for surface in [
        _read("README.md"),
        _read("docs/GOAL.md"),
        _read("docs/runbook.md"),
        _read("docs/application/portfolio-index.md"),
    ]:
        assert review_path in surface

    review = _read(review_path)
    for boundary in [
        "not new runtime evidence",
        "not robust PDF extraction evidence",
        "not semantic retrieval quality evidence",
        "not hosted deployment evidence",
        "not hosted observability evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]:
        assert boundary in review
