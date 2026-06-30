# Proof Gap Action Surface

Phase 858 adds proof gap action surface v0.

Phase `proof_gap_action_surface_current_state_refresh_v0` refreshes the same
surface after `proof_gap_priority_matrix_v0`.

## What Changed

NoiseProof already exposed a read-only proof gap registry through:

```text
GET /ops/summary
GET /ops/dashboard
```

This phase adds two narrower ops endpoints:

```text
GET /ops/proof-gaps
GET /ops/proof-gaps/{gap_id}
```

These endpoints return the current proof gaps plus action metadata:

```text
acceptable_evidence
blocked_claims
proof_routes
recommended_next_gate
action_boundary
```

## Current Gap Coverage

The surface covers:

```text
robust_pdf_extraction
actual_embedding_generation
semantic_retrieval_quality
distributed_tracing
hosted_observability
hosted_deployment
external_reviewer_feedback
```

## Current-state Refresh

After `proof_gap_priority_matrix_v0`, the action surface now separates:

```text
highest-trust evidence gate -> external_reviewer_feedback_v0
next local implementation gate -> proof_gap_action_surface_current_state_refresh_v0
next robust PDF local product gate -> real_world_ocr_evidence_gate_v0
```

For `robust_pdf_extraction`, the action surface no longer points at
`multi_real_world_pdf_parse_observation_matrix_remote_verification_v0` as the
next gate, because that remote workflow verification is already represented in
the current GOAL ledger and proof routes. It is now part of current evidence and
proof routing:

```text
current_evidence -> ...plus_multi_real_world_pdf_parse_observation_matrix_remote_verification_v0
proof_routes -> docs/review/multi-real-world-pdf-parse-observation-remote-verification.md
recommended_next_gate -> real_world_table_extraction_evidence_gate_v0
```

This refresh does not close the robust PDF gap.

After `source_policy_pdf_parse_quality_matrix_v0`, the action surface includes:

```text
current_evidence -> ...plus_source_policy_pdf_parse_quality_matrix_v0
proof_routes -> docs/review/source-policy-pdf-parse-quality-matrix.md
proof_routes -> docs/evaluation/source-policy-pdf-parse-quality-matrix-report.md
recommended_next_gate -> source_policy_pdf_quality_gap_review_v0
```

The quality matrix turns the source-policy parse observations into six blocker
cells and keeps `quality_claim_ready_cell_count -> 0`; it does not close the
robust-PDF gap.

After `source_policy_pdf_quality_gap_review_v0`, the action surface includes:

```text
current_evidence -> ...plus_source_policy_pdf_quality_gap_review_v0
proof_routes -> docs/review/source-policy-pdf-quality-gap-review.md
proof_routes -> docs/evaluation/source-policy-pdf-quality-gap-review-report.md
recommended_next_gate -> source_policy_no_native_text_failure_route_v0
```

The quality gap review selects the NARA no-native-text failure route as the
next smallest inspectable gate. It does not implement OCR and does not close the
robust-PDF gap.

After `source_policy_no_native_text_failure_route_v0`, the action surface
includes:

```text
current_evidence -> ...plus_source_policy_no_native_text_failure_route_v0
proof_routes -> docs/review/source-policy-no-native-text-failure-route.md
proof_routes -> docs/evaluation/source-policy-no-native-text-failure-route-report.md
recommended_next_gate -> source_policy_no_native_text_ocr_readiness_review_v0
```

The failure route preserves the NARA no-native-text case before OCR readiness
work. It does not run OCR and does not close the robust-PDF gap.

After `source_policy_no_native_text_ocr_readiness_review_v0`, the action
surface includes:

```text
current_evidence -> ...plus_source_policy_no_native_text_ocr_readiness_review_v0
proof_routes -> docs/review/source-policy-no-native-text-ocr-readiness-review.md
proof_routes -> docs/evaluation/source-policy-no-native-text-ocr-readiness-review-report.md
recommended_next_gate -> source_policy_no_native_text_ocr_dependency_check_v0
```

The readiness review identifies the Tesseract-backed OCR dependency boundary
without checking local dependency availability, running OCR, or closing the
robust-PDF gap.

After `source_policy_no_native_text_ocr_dependency_check_v0`, the action
surface includes:

```text
current_evidence -> ...plus_source_policy_no_native_text_ocr_dependency_check_v0
proof_routes -> docs/review/source-policy-no-native-text-ocr-dependency-check.md
proof_routes -> docs/evaluation/source-policy-no-native-text-ocr-dependency-check-report.md
recommended_next_gate -> source_policy_no_native_text_ocr_dependency_resolution_v0
```

The dependency check records the current missing Tesseract command state
without printing or committing local paths. It does not run OCR and does not
close the robust-PDF gap.

After `source_policy_no_native_text_ocr_dependency_resolution_v0`, the action
surface includes:

```text
current_evidence -> ...plus_source_policy_no_native_text_ocr_dependency_resolution_v0
proof_routes -> docs/review/source-policy-no-native-text-ocr-dependency-resolution.md
proof_routes -> docs/evaluation/source-policy-no-native-text-ocr-dependency-resolution-report.md
recommended_next_gate -> source_policy_no_native_text_ocr_execution_plan_v0
```

The dependency resolution records owner-runtime Tesseract command and English
language-data availability after PATH refresh. It does not run OCR, does not
evaluate OCR quality, and does not close the robust-PDF gap.

After `robust_pdf_extraction_next_real_world_quality_gate_v0`, the action
surface includes:

```text
current_evidence -> ...plus_robust_pdf_extraction_next_real_world_quality_gate_v0
proof_routes -> docs/review/robust-pdf-extraction-next-real-world-quality-gate.md
proof_routes -> docs/evaluation/robust-pdf-real-world-quality-gate-report.md
recommended_next_gate -> cross_publisher_real_world_pdf_fixture_gate_v0
```

The robust-PDF quality gate is blocked because the current real-world matrix has
one publisher family only and no table extraction, OCR, or layout fidelity
evidence.

After `cross_publisher_real_world_pdf_fixture_gate_v0`, the action surface
includes:

```text
current_evidence -> ...plus_cross_publisher_real_world_pdf_fixture_gate_v0
proof_routes -> docs/review/cross-publisher-real-world-pdf-fixture-gate.md
proof_routes -> docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md
recommended_next_gate -> real_world_table_extraction_evidence_gate_v0
```

The cross-publisher fixture gate reduces the publisher-family blocker, but the
robust-PDF gap remains open because table extraction, OCR, and layout fidelity
evidence are still missing.

After `real_world_table_extraction_evidence_gate_v0`, the action surface
includes:

```text
current_evidence -> ...plus_real_world_table_extraction_evidence_gate_v0
proof_routes -> docs/review/real-world-table-extraction-evidence-gate.md
proof_routes -> docs/evaluation/real-world-table-extraction-evidence-gate-report.md
recommended_next_gate -> real_world_ocr_evidence_gate_v0
```

The table extraction evidence gate reduces the table blocker for the listed
real-world fixtures, but the robust-PDF gap remains open because OCR and layout
fidelity evidence are still missing.

After `real_world_ocr_evidence_gate_v0`, the action surface includes:

```text
current_evidence -> ...plus_real_world_ocr_evidence_gate_v0
proof_routes -> docs/review/real-world-ocr-evidence-gate.md
proof_routes -> docs/evaluation/real-world-ocr-evidence-gate-report.md
recommended_next_gate -> real_world_layout_fidelity_evidence_gate_v0
```

The OCR evidence gate reduces the OCR blocker for one NARA fixture, but the
robust-PDF gap remains open because layout fidelity evidence is still missing.

After `real_world_layout_fidelity_evidence_gate_v0`, the action surface
includes:

```text
current_evidence -> ...plus_real_world_layout_fidelity_evidence_gate_v0
proof_routes -> docs/review/real-world-layout-fidelity-evidence-gate.md
proof_routes -> docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md
recommended_next_gate -> robust_pdf_extraction_generalization_gap_review_v0
```

The layout fidelity evidence gate reduces the layout blocker for one BEA
fixture, but the robust-PDF gap remains open because the evidence chain is still
too small to generalize to arbitrary market PDFs.

After `robust_pdf_extraction_generalization_gap_review_v0`, the action surface
includes:

```text
current_evidence -> ...plus_robust_pdf_extraction_generalization_gap_review_v0
proof_routes -> docs/review/robust-pdf-generalization-gap-review.md
proof_routes -> docs/evaluation/robust-pdf-generalization-gap-review-report.md
recommended_next_gate -> multi_publisher_modality_stratified_pdf_eval_v0
```

The generalization gap review keeps the robust-PDF gap open. It turns the
remaining missing proof into explicit capability gaps: labeled layout ground
truth, natural reading order evaluation, rendered visual fidelity, image/chart
interpretation, arbitrary-market coverage, and external reviewer validation.

After `multi_publisher_modality_stratified_pdf_eval_v0`, the action surface
includes:

```text
current_evidence -> ...plus_multi_publisher_modality_stratified_pdf_eval_v0
proof_routes -> docs/review/multi-publisher-modality-stratified-pdf-eval.md
proof_routes -> docs/evaluation/multi-publisher-modality-stratified-pdf-eval-report.md
recommended_next_gate -> targeted_real_world_pdf_fixture_expansion_v0
```

The stratified PDF eval keeps the robust-PDF gap open. It makes the current
coverage partial in a 12-cell matrix and turns the next action into a targeted
real-world fixture expansion plan rather than a broad parser claim.

After `targeted_real_world_pdf_fixture_expansion_v0`, the action surface
includes:

```text
current_evidence -> ...plus_targeted_real_world_pdf_fixture_expansion_v0
proof_routes -> docs/review/targeted-real-world-pdf-fixture-expansion.md
proof_routes -> docs/evaluation/targeted-real-world-pdf-fixture-expansion-report.md
recommended_next_gate -> real_world_pdf_fixture_source_policy_download_hash_v0
```

The targeted fixture expansion keeps the robust-PDF gap open. It maps all six
missing cells to source-policy-reviewed candidate routes, but it performs no
downloads, hashing, parsing, OCR, table extraction, visual comparison, or
external review.

After `real_world_pdf_fixture_source_policy_download_hash_v0`, the action
surface includes:

```text
current_evidence -> ...plus_real_world_pdf_fixture_source_policy_download_hash_v0
proof_routes -> docs/review/source-policy-download-hash.md
proof_routes -> docs/evaluation/source-policy-download-hash-report.md
recommended_next_gate -> source_policy_pdf_parse_observation_v0
```

The source-policy download/hash gate keeps the robust-PDF gap open. It records
three temporary owner-runtime downloaded/hashable PDFs, two BLS HTTP 403
blocked candidates, and one external route, but it performs no parsing, OCR,
table extraction, visual comparison, or external review.

After `source_policy_pdf_parse_observation_v0`, the action surface includes:

```text
current_evidence -> ...plus_source_policy_pdf_parse_observation_v0
proof_routes -> docs/review/source-policy-pdf-parse-observation.md
proof_routes -> docs/evaluation/source-policy-pdf-parse-observation-report.md
recommended_next_gate -> source_policy_pdf_parse_quality_matrix_v0
```

The source-policy parse observation gate keeps the robust-PDF gap open. It
records PyMuPDF text/block metadata for three selected candidates and preserves
one no-native-text failure candidate, but it performs no OCR, table extraction,
rendered comparison, image/chart interpretation, or external review.

## Semantic Retrieval Quality Example

For `semantic_retrieval_quality`, the action surface keeps the gap open. After
Phase 866, the gap has a local representative fixture covering all current
NoiseProof information roles and source types, plus an owner-runtime packet,
runner, and validator for a future live embedding-backed domain qrels run. The current
accepted evidence still does not include live embedding generation and does not
prove production semantic retrieval quality:

```text
status -> unproven
claim_boundary -> representative_local_fixture_and_caller_provided_vectors_do_not_prove_production_semantic_retrieval_quality
acceptable_evidence -> run a live embedding-backed domain qrels quality evaluation beyond caller-provided fixture vectors
blocked_claims -> semantic retrieval quality is proven
recommended_next_gate -> owner_runtime_live_embedding_domain_qrels_eval_v0
proof_routes -> docs/review/live-embedding-domain-qrels-owner-runtime-runner.md; docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet.md; docs/evaluation/representative-live-semantic-quality-report.md; docs/evaluation/live-semantic-qrels-baseline-report.md; docs/evaluation/live-lexical-qrels-baseline-report.md; docs/evaluation/qrels-backed-semantic-quality-report.md
```

## Boundary

This is `action_surface_only_not_new_proof_or_gap_closure`.

It is not robust PDF extraction evidence, not live embedding generation proof, not semantic retrieval quality evidence, not distributed tracing, not hosted observability, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, and not product-complete.

## Verification

Local focused tests:

```text
uv run pytest tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_routes.py::test_ops_proof_gap_action_surface_returns_404_for_unknown_gap -q
```

Observed result:

```text
2 passed
```

## Next Gate

Next recommended local product gate after this current-state refresh:

```text
source_policy_no_native_text_ocr_dependency_resolution_v0
```

If real-world fixture inputs are unavailable, stop and record the planned path,
actual state, blocking mismatch, why it blocks, and the minimum action to
resume before selecting another gate.
