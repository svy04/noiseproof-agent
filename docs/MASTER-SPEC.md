# NoiseProof Agent Master Spec

Status: active master spec.

This file is the operating constitution for NoiseProof Agent. Before any future
implementation or proof gate, read this file first, then read `docs/GOAL.md`,
then read the latest relevant short-term spec under `docs/specs/`.

Current source assimilation registry:
`docs/research/source-assimilation-registry.md`.

Current source assimilation gate: `source_assimilation_registry_v0`.

Current proof-gap prioritization gate: `proof_gap_priority_matrix_v0`.

Current proof-gap priority matrix:
`docs/research/proof-gap-priority-matrix.md`.

Current proof-gap action refresh gate:
`proof_gap_action_surface_current_state_refresh_v0`.

Previous master operating gate:
`master_spec_operating_loop_v0`.

Current robust-PDF local quality gate:
`robust_pdf_extraction_next_real_world_quality_gate_v0`.

Current cross-publisher PDF fixture gate:
`cross_publisher_real_world_pdf_fixture_gate_v0`.

Current real-world table extraction evidence gate:
`real_world_table_extraction_evidence_gate_v0`.

Current real-world OCR evidence gate:
`real_world_ocr_evidence_gate_v0`.

Current real-world layout fidelity evidence gate:
`real_world_layout_fidelity_evidence_gate_v0`.

Current robust-PDF generalization gap review gate:
`robust_pdf_extraction_generalization_gap_review_v0`.

Current multi-publisher modality-stratified PDF eval gate:
`multi_publisher_modality_stratified_pdf_eval_v0`.

Current targeted real-world PDF fixture expansion gate:
`targeted_real_world_pdf_fixture_expansion_v0`.

Current source-policy PDF download/hash gate:
`real_world_pdf_fixture_source_policy_download_hash_v0`.

Current source-policy PDF parse observation gate:
`source_policy_pdf_parse_observation_v0`.

Current source-policy PDF parse quality matrix gate:
`source_policy_pdf_parse_quality_matrix_v0`.

Current source-policy PDF quality gap review gate:
`source_policy_pdf_quality_gap_review_v0`.

Current source-policy no-native-text failure route gate:
`source_policy_no_native_text_failure_route_v0`.

Current source-policy no-native-text OCR readiness review gate:
`source_policy_no_native_text_ocr_readiness_review_v0`.

Current source-policy no-native-text OCR dependency check gate:
`source_policy_no_native_text_ocr_dependency_check_v0`.

Current source-policy no-native-text OCR dependency resolution gate:
`source_policy_no_native_text_ocr_dependency_resolution_v0`.

Current source-policy no-native-text OCR execution plan gate:
`source_policy_no_native_text_ocr_execution_plan_v0`.

Current source-policy no-native-text OCR execution smoke gate:
`source_policy_no_native_text_ocr_execution_smoke_v0`.

Current source-policy no-native-text OCR quality eval plan gate:
`source_policy_no_native_text_ocr_quality_eval_plan_v0`.

Current source-policy no-native-text OCR quality reference pack gate:
`source_policy_no_native_text_ocr_quality_reference_pack_v0`.

Current source-policy no-native-text OCR marker proxy eval gate:
`source_policy_no_native_text_ocr_marker_proxy_eval_v0`.

Current source-policy no-native-text OCR transcript reference plan gate:
`source_policy_no_native_text_ocr_transcript_reference_plan_v0`.

Current source-policy no-native-text OCR transcript reference pack gate:
`source_policy_no_native_text_ocr_transcript_reference_pack_v0`.

Current source-policy no-native-text OCR owner transcript collection plan gate:
`source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0`.

Current source-policy no-native-text OCR source rights review request packet gate:
`source_policy_no_native_text_ocr_source_rights_review_request_packet_v0`.

Current next PDF evidence gate:
`source_policy_no_native_text_ocr_owner_rights_decision_record_v0`.

NoiseProof should evolve by absorbing strong existing solutions from primary
sources, papers, standards, patents, official docs, and maintained open-source
projects. The point is not to invent a more impressive demo. The point is to
turn proven ideas into a small, inspectable system that blocks unsupported
market-intelligence claims.

## 1. Vision

NoiseProof Agent is a noise-resilient data agent for messy market intelligence.

Its long-term shape is:

```text
messy sources
  -> source profiling
  -> collection plan
  -> parser/chunk/retrieval experiments
  -> provenance-backed evidence records
  -> contradiction and limitation surfacing
  -> claim-bounded reports
  -> run logs, failure cases, reviewer proof packets
```

The core thesis remains:

```text
A good data agent does not start by answering well.
It starts by preventing unsupported answers from passing.
```

## 2. Source Assimilation Doctrine

Every non-trivial gate must begin with a source-first pass.

Order of evidence:

1. Current local repository and runtime truth.
2. Primary standards, official docs, maintained upstream code, papers, patents,
   and research artifacts.
3. Existing OSS/framework patterns that can be reused or adapted.
4. Summaries, blogs, and second-hand posts only as routing aids.
5. New bespoke design only after the above are insufficient.

For each absorbed source, record:

```text
source:
source_type: standard | paper | patent | official_doc | oss | runtime_evidence
pattern_to_borrow:
local_adaptation:
boundary:
rejection_condition:
license_or_rights_note:
```

Source cards belong in `docs/research/source-assimilation-registry.md`. A
non-trivial gate that changes architecture, evaluation, parser behavior,
retrieval behavior, report behavior, observability, or public claims should add
or update a source card before implementation.

Patent documents may inform problem framing and design patterns, but they are
not permission to copy claims, protected implementations, diagrams, or product
positioning. Patent-derived ideas must be reduced to general, independently
implemented patterns unless a legal/license review says otherwise.

## 3. Reference Spine

These references are not proof that NoiseProof implements the same maturity.
They define the patterns NoiseProof should borrow carefully.

| Source | Pattern to absorb | NoiseProof adaptation | Boundary |
|---|---|---|---|
| [W3C PROV-DM](https://www.w3.org/TR/prov-dm/) | Model provenance through entities, activities, agents, derivations, and bundles. | Evidence Ledger and run lineage should model source, retrieval, claim, report, and responsible workflow steps. | Operational provenance is not truth adjudication. |
| [SLSA Provenance](https://slsa.dev/spec/v1.0/provenance) | Keep explicit subjects, build/run details, dependencies, parameters, and byproducts. | Agent runs should record inputs, workflow version, resolved artifacts, trace ids, and generated proof packets. | Local run provenance is not supply-chain certification. |
| [OpenTelemetry](https://opentelemetry.io/docs/specs/otel/overview/) | Separate traces, metrics, logs, resources, and context propagation. | Workflow runs should make stage boundaries inspectable without implying hosted observability. | Local spans/logs are not distributed production tracing. |
| [RAGAS](https://aclanthology.org/2024.eacl-demo.16/) | Evaluate RAG as multiple surfaces instead of one answer-quality vibe check. | Retrieval, citation coverage, answer support, and failure records stay separate. | Local fixtures are not public benchmark claims. |
| [ALCE](https://aclanthology.org/2023.emnlp-main.398/) | Treat citation quality as its own evaluation surface. | Reports must keep claim, source id, evidence span, and limitation visible. | Citations do not automatically make a claim true. |
| [BEIR](https://openreview.net/forum?id=wCu6T5xFjeJ) and [trec_eval](https://github.com/usnistgov/trec_eval) | Keep retrieval quality shaped around corpus, queries, qrels, runs, and metrics. | Semantic retrieval work should remain qrels-backed before stronger claims. | Small qrels are not general retrieval quality evidence. |
| [Model Cards](https://arxiv.org/abs/1810.03993) | Report intended use, factors, metrics, caveats, and ethical boundaries. | Every externally visible capability should have a claim boundary. | NoiseProof is not model-card compliant by naming the pattern. |
| [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Document dataset motivation, composition, collection, preprocessing, and maintenance. | Fixture packs should expose source policy, collection method, omissions, and non-claims. | Fixture docs are not dataset certification. |
| [Docling](https://github.com/docling-project/docling) and [Unstructured partitioning](https://docs.unstructured.io/open-source/core-functionality/partitioning) | Treat parsing, layout, table extraction, OCR, and typed elements as separate capabilities. | PDF/document work must keep digital text, tables, OCR, layout, and image interpretation split. | One adapter smoke does not prove robust parsing. |
| [US20260105079A1](https://patents.google.com/patent/US20260105079A1/en) | Link retrieved semantic units back to original text for transparency and audit. | Future knowledge-graph or relation extraction work must preserve source-span provenance. | Pending patent material is inspiration only, not an implementation license. |
| [US10628389B2](https://patents.google.com/patent/US10628389B2/en) | Add provenance verification around systems that were not built with native provenance. | NoiseProof should prefer lightweight logs, hashes, and proof packets around existing runs before invasive rewrites. | No blockchain or cryptographic guarantee is claimed. |

## 4. Product Pillars

1. Source intake and profiling.
2. Collection planning before retrieval.
3. Parser, chunk, and retrieval experiment boundaries.
4. Evidence Ledger before answer trust.
5. Contradiction, weakness, and missing-data surfacing.
6. Noise Gate and claim blocking.
7. Claim-bounded report generation.
8. Run trace, failure case, and proof packet operations.
9. External-reader route hygiene without overstating validation.

## 5. Non-goals

NoiseProof is not:

- a trading bot
- a stock recommendation engine
- a target-price generator
- a financial advice product
- a generic chatbot
- a production SaaS claim
- a robust PDF extraction claim until real evidence exists
- a benchmark claim until representative evaluation exists

If a requested feature drifts toward those non-goals, reframe it into:

```text
What happened?
What source supports it?
Which sources conflict?
Which claim is weak?
What data is missing?
Why should this conclusion not be trusted yet?
```

## 6. Gate Loop

Every future gate follows this loop:

1. Read `docs/MASTER-SPEC.md`.
2. Read `docs/GOAL.md`.
3. Inspect current local repo state and existing proof artifacts.
4. Identify the next highest-value incomplete gate.
5. Read `docs/research/source-assimilation-registry.md` and primary/original sources relevant to that gate.
6. For proof-reduction gates, read
   `docs/research/proof-gap-priority-matrix.md` before selecting the local
   implementation target.
7. Create or update a short-term spec in `docs/specs/`.
8. Implement only that spec.
9. Run available verification.
10. Update README, runbook, GOAL, review/application docs if the gate changes public proof state.
11. Report what is implemented, what remains planned, what was verified, and what is blocked.

No gate should jump straight from idea to code.

## 7. Short-term Spec Requirements

Each short-term spec must include:

```text
title:
status:
date:
target_gate:
current_repo_state:
sources_to_absorb:
non_goals:
implementation_scope:
data_or_api_contract:
tests:
docs_to_update:
stop_conditions:
claim_boundaries:
next_gate_if_passed:
```

Short-term specs belong in `docs/specs/` and should be named:

```text
YYYY-MM-DD-<gate-slug>.md
```

## 8. Stop Conditions

Do not hide environment or evidence gaps behind vague language.

If a gate cannot continue, stop and report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

Examples:

- required runtime is absent and cannot be installed or verified in this environment
- source material is unavailable or license/rights status is unclear
- the needed external service credential is missing
- tests fail in a way that changes the meaning of the gate
- the proposed gate conflicts with this master spec or `docs/GOAL.md`
- the implementation would expand scope into retrieval, LLM calls, trading advice, or production claims without evidence

The rule is not "keep talking anyway." The rule is: solve the blocker if it is
safe and local; otherwise stop with the exact mismatch and resume after the
blocking condition is removed.

## 9. Claim Boundary Rule

For every public-facing update, write the strongest true sentence and the
strongest necessary non-claim.

Format:

```text
Implemented:
Not implemented:
Verified:
Not verified:
Can claim:
Cannot claim:
Next evidence gate:
```

If a sentence would sound impressive but cannot be inspected, remove it or move
it to a planned section.

## 10. Next Operating Gate

The current operating gate is:

```text
source_policy_no_native_text_ocr_owner_transcript_collection_plan_v0
```

This gate records an owner-runtime transcript collection plan for the preserved
source-policy NARA no-native-text route. It does not collect a reference
transcript, record source-rights approval as complete, commit transcript
hashes, evaluate OCR quality, compute CER/WER, inspect raw OCR text, prove
reference transcript availability, or support robust PDF wording.

After this operating gate is accepted, future agents should return to the next
highest-value evidence or implementation gate in `docs/GOAL.md`. The expected
next PDF evidence gate is
`source_policy_no_native_text_ocr_source_rights_review_request_packet_v0`,
unless the user deliberately redirects the product vision.
