# Architecture: NoiseProof Agent

## Implementation Status

Current status:

- Architecture is documented.
- PostgreSQL with pgvector is configured in Docker Compose.
- PostgreSQL schema init SQL exists for documents, agent runs, and failure cases.
- FastAPI skeleton exists for health, metadata persistence, and ops summary placeholder.
- Messy market data fixtures exist.
- Document Profiler v0 exists for fixture-like text and direct text payloads.
- Parser adapter stubs exist for direct parse-preview payloads.
- Chunk strategy experiment v0 exists for direct chunk-preview payloads.
- Retrieval v0 exists for lexical candidate search over generated chunks.
- Collection Plan Preview v0 exists for question-only role planning before Evidence Ledger work.
- Evidence Ledger Preview v0 exists for deterministic claim-level entries over retrieval candidates.
- Noise Gate Preview v0 exists for deterministic pre-report checks over ledger entries and draft claims.
- Claim-bounded Report Preview v0 exists for deterministic report-shaped output after the Noise Gate passes.
- Operations Dashboard v0 exists as a plain FastAPI HTML view over current metadata records.
- Evaluation/Application Package v0 exists for evaluation planning, failure records, and Braincrew role mapping.
- Auto Trace Recording v0 exists for preview endpoint metadata in `agent_runs.trace_json`.
- Persisted Evidence Ledger Records v0 exists for stored claim-level entries and operations counts.
- Persisted Noise Gate Records v0 exists for stored pass / needs_revision / blocked gate decisions.
- Persisted Report Preview Records v0 exists for stored generated / needs_revision / blocked report-shaped outputs.
- Record Linkage v0 exists with shared `workflow_trace_id` values across persisted evidence, gate, report records, and matching `agent_runs.trace_json`.
- Trace-id Lookup v0 exists for direct inspection by `workflow_trace_id`.
- Persisted Record Filtering v0 exists for read-only filtering of persisted evidence, gate, and report records.
- Dashboard Trace/Filter Links v0 exists for browser-readable trace lookup and record filter navigation.
- Agent-run Linkage Review v0 exists as a review artifact that preceded direct child-record linkage.
- Agent-run Lifecycle v0 exists: traced operations create a parent `agent_runs` row before execution, then update the same row after completion or failure.
- Persisted Child Record Agent-run Linkage v0 exists for Evidence Ledger, Noise Gate, and Report records.
- Dashboard Parent/Child Provenance Links v0 exists for parent run links on persisted Noise Gate and Report rows.
- Evidence Ledger Dashboard Table v0 exists for browser-readable persisted evidence rows.
- Evidence-to-gate/report Local Cross-links Review v0 exists as a review artifact; direct cross-stage links are deferred until a single workflow parent exists.
- Single Workflow Parent Review v0 exists as a review artifact; future workflow-level provenance should use a separate `workflow_runs` table instead of reusing `agent_runs`.
- WorkflowRun Schema v0 exists as a database table and migration.
- WorkflowRun Metadata Persistence v0 exists for create/list only; workflow orchestration behavior is not implemented.
- WorkflowRun Dashboard Table v0 exposes workflow-run metadata in the plain operations dashboard.
- WorkflowRun Child-link Review v0 exists as a review artifact; child `workflow_run_id` columns were deferred there, then implemented after the Phase 28 execution boundary.
- Deterministic Workflow Execution Preview v0 exists: `POST /workflow-runs/execute-preview` creates a workflow parent and runs deterministic retrieval -> evidence -> gate -> report preview steps.
- WorkflowRun Child-record Links v0 exists with nullable `workflow_run_id` on retrieval, Evidence Ledger, Noise Gate, and Report records created by the deterministic workflow preview.
- WorkflowRun Child Inspection Surface v0 exists: `GET /workflow-runs/{id}` returns the parent workflow row, linked child records, and child summary counts.
- Direct Evidence-to-gate/report Cross-link Review v0 exists as a review artifact; direct evidence -> gate -> report foreign-key links remain deferred until downstream stages consume persisted upstream row ids.
- Workflow Stage Input Manifest v0 exists with `stage_input_manifest` on deterministic workflow-created Noise Gate and Report records.
- Direct Cross-stage Link Schema Review v0 exists as a review artifact; direct FK/join-table storage remains deferred in favor of a derived lineage read model.
- Workflow Lineage Read Model v0 exists: `GET /workflow-runs/{id}/lineage` derives stage lineage from existing workflow child records and `stage_input_manifest`, without new storage or direct FK/join-table lineage.
- Workflow Lineage Dashboard Links v0 exists: `GET /ops/dashboard` workflow rows link to both workflow detail and the derived lineage read model, without dashboard polish.
- Workflow Lineage Missing-reference Review v0 exists: missing manifest reference behavior is reviewed as a bounded follow-up, with a targeted missing-reference test selected before any schema or runtime mutation expansion.
- Workflow Lineage Missing-reference Test v0 exists: a targeted fixture proves the derived lineage read model surfaces unresolved manifest ids without adding schema, join tables, or mutation endpoints.
- Workflow Lineage Boundary Hardening Review v0 exists: non-list manifest values, duplicate references, and cross-workflow references are reviewed before the next manifest-shape hardening gate.
- Workflow Lineage Manifest-shape Hardening v0 exists: non-list evidence id values are ignored with a warning, duplicate references preserve order/count, and cross-workflow references remain local missing references.
- Workflow Lineage Warning Taxonomy Review v0 exists: lineage warning categories are reviewed before adding structured warning fields; current warning strings remain human-readable.
- Structured Warning Taxonomy v0 exists: `GET /workflow-runs/{id}/lineage` returns `warning_codes` while preserving human-readable `warnings`.
- Workflow Lineage Warning Code Documentation Review v0 exists: warning-code documentation is reviewed before dashboard or persistence expansion.
- Workflow Lineage Warning Code Runbook Example v0 exists: the runbook shows the lineage response shape with both `warnings` and `warning_codes`.
- Workflow Lineage Warning Code Dashboard Review v0 exists: warning-code dashboard surfacing is reviewed before any `GET /ops/dashboard` rendering change.
- Workflow Lineage Warning Code Dashboard Surfacing v0 exists: `GET /ops/dashboard` shows a compact warning-code legend without adding storage or analytics.
- Workflow Lineage Warning Code Dashboard Smoke Example v0 exists: the runbook shows the expected dashboard legend text.
- Workflow Version Naming Review v0 exists: runtime `workflow_version` naming was reviewed before changing `phase36-structured-warning-taxonomy`.
- Workflow Version Naming Update v0 exists: runtime `workflow_version` is now `phase40-lineage-warning-code-dashboard`.
- Current implemented current-state surfaces include uploaded file intake manifest persistence, uploaded file parsed document metadata persistence, uploaded file chunk persistence, uploaded file retrieval persistence, uploaded raw file quarantine storage, metadata-only raw-file scan records, explicit scan execution with scanner-unavailable defaults, ClamAV opt-in clean-file endpoint proof, caller-provided chunk embeddings, caller-provided semantic retrieval persistence, retrieval-run-linked Evidence Ledger, retrieval-run-linked Noise Gate, retrieval-run-linked Report, workflow lineage read models, dashboard lineage links, and failure-case records.
- still unproven: robust PDF extraction, embedding generation, production semantic retrieval quality, hosted deployment evidence, hosted observability, external reviewer feedback, endpoint malicious-detection runtime proof, autonomous/LLM-backed agents, and a polished web app.

This document describes the intended system so implementation can proceed without drifting into a trading bot or a generic RAG demo.

## System Overview

NoiseProof Agent is an evidence-first RAG/agent workflow for messy market intelligence.

Core flow:

```text
Source Upload / URL Input
  -> Document Profiler
  -> Parser Selector
  -> Chunk Strategy Experiment
  -> Collection Plan Preview
  -> Indexing
  -> Retrieval
  -> Evidence Ledger
  -> Analysis Draft
  -> Critic / Noise Gate
  -> Claim-bounded Report
  -> Run Log / Failure Case
```

Short form:

```text
Source -> Document Profiler -> Parser -> Chunker -> Collection Plan -> Retrieval -> Evidence Ledger -> Critic -> Report -> Run Log
```

## Component Responsibilities

### Source Upload / URL Input

Accepts planned input types:

- PDF
- CSV
- URL/HTML
- markdown memo

It should store metadata before parsing so failed parsing attempts can still be recorded.

### Document Profiler

Document Profiler v0 generates a lightweight profile for provided text:

- source type
- character count
- line count
- approximate token count
- table-like structure
- URL presence
- date presence
- number presence
- extraction quality
- recommended strategy
- warnings

It does not parse uploaded files yet.

### Parser Selector

Chooses the parser by input type and extraction quality.

Phase 3 implements a small parse-preview boundary, not full production parsing:

- markdown parser returns text plus heading, link, and bullet metadata
- CSV parser returns text plus row, column, header, and inconsistent-row metadata
- HTML/URL parser strips tags into visible text and records link metadata
- PDF upload-preview can extract digital text with PyMuPDF from uploaded PDF bytes; PDF upload chunk and retrieval handoffs reuse PyMuPDF digital text extraction for `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, and `POST /documents/upload-retrieval-preview`; JSON parse-preview still supports text-only fallback for already-extracted text. OCR, table extraction, layout fidelity, and robust PDF extraction are not claimed
- unknown source types return a structured warning and failure-case candidate

The parser output can feed Document Profiler v0. Parse-preview does not save records to the database.

Planned defaults:

- PyMuPDF for uploaded digital PDF text extraction v0
- pandas for CSV
- BeautifulSoup or trafilatura for URL/HTML
- plain markdown parser for memo

### Chunk Strategy Experiment

Runs multiple chunking strategies against the same document.

Implemented Phase 4 strategies:

- fixed-window chunking with configurable max characters and overlap
- heading-aware chunking with `header_path` metadata
- row-aware chunking with CSV header and row metadata

Phase 4 records comparison metrics only:

- chunk count
- source character and line counts
- min, max, and average chunk character counts
- empty and oversized chunk counts
- estimated token count
- structural boundary count

The goal is to compare chunk shapes before retrieval, not to assume one chunking method is always best.

Current persistence boundary:

- `POST /documents/{document_id}/chunks` can manually persist derived chunk text for an explicit document id.
- `POST /documents/upload-chunks` can explicitly hand off uploaded content into a document row plus `document_chunks` rows.
- `POST /documents/upload-chunk-preview` remains preview-only and does not create documents or chunks.

Chunk persistence stores derived chunk text only. It stores no raw uploaded bytes and no full parsed text. PDF-derived upload chunks preserve minimal parser provenance (`parser`, `digital_pdf_text_extraction`, and `robust_pdf_extraction`) so persisted document retrieval runs can summarize candidate provenance without claiming robust PDF extraction. Retrieval persistence is a separate explicit handoff surface, and embeddings are a separate caller-provided chunk embedding surface.

Research scope note:

- `fixed-window` keeps the familiar `max_characters` / `overlap` vocabulary used by common text splitter APIs.
- `heading-aware` preserves section paths so later retrieval work can inspect whether source structure was lost.
- `row-aware` preserves CSV headers and row indices so tabular evidence can stay auditable.
- Phase 4 does not add external chunking dependencies; it only creates a local, inspectable comparison boundary.

### Indexing

Current implementation stores chunks in PostgreSQL and supports caller-provided chunk embeddings in `chunk_embeddings` with pgvector-compatible storage.

Qdrant remains an alternative if pgvector slows delivery, but Day 1 chooses pgvector to keep the local stack small.

Current boundary:

- chunk text can be persisted through explicit document-scoped or upload handoff endpoints
- caller-provided chunk embeddings can be persisted and listed
- embedding generation is still unproven and not implemented
- vector quality claims remain blocked by the semantic retrieval quality report boundary

### Retrieval

Retrieval v0 runs a question against generated chunks and records:

- strategy
- latency
- result count
- hit rate
- citation coverage
- missing evidence count

Implemented Phase 5 boundary:

- lexical term matching only
- no embeddings
- no vector index
- source id attached to every returned candidate
- retrieval run metadata persisted to `retrieval_runs`
- no-results runs recorded with `status: no_results`

Later implemented retrieval surfaces add explicit upload-file retrieval persistence and caller-provided semantic retrieval persistence. The semantic path ranks stored chunk embeddings against a caller-provided query vector; it does not generate embeddings and does not prove production semantic retrieval quality.

Retrieval candidates are not final evidence by themselves. Evidence Ledger stages can promote, weaken, contradict, or block them before any report-shaped output.

### Collection Plan Preview

Collection Plan Preview v0 converts a user question into required information roles before evidence work starts.

Implemented Phase 5.5 boundary:

- deterministic local rules only
- question-only input
- no LLM calls
- no external search
- no retrieval expansion
- no DB persistence
- no truth judgment

The preview returns the question, information need, possible claim candidates, required roles, source types to check, minimum evidence needed, risks, stop conditions, and warnings. Buy/sell drift is represented as `user_intent_check` plus a stop condition, not as financial advice.

### Evidence Ledger

Turns retrieved evidence into claim-level records before final answer generation.

The ledger is the main trust surface of the product.

Implemented Phase 6 boundary:

- deterministic preview only
- direct retrieval-candidate input
- no LLM calls
- no external search
- no final report generation

The preview returns claim-level entries with source id, source type, source date, evidence span, confidence, limitation, contradicting source ids, status, matched terms, and role. It can block no-evidence and buy/sell-drift questions, and it can surface contradiction language before report generation.

Implemented Phase 12 boundary:

- `POST /evidence-ledgers` persists generated preview entries
- `GET /evidence-ledgers` lists stored entries
- operations summary and dashboard counts use persisted unsupported, blocked, and contradicted entries
- `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger` creates retrieval-run-linked Evidence Ledger entries from an existing retrieval run
- direct evidence -> gate -> report foreign-key lineage remains deferred; workflow lineage uses workflow parents and stage input manifests instead

### Analysis Draft

Produces a draft interpretation from the Evidence Ledger.

The draft is not final. It must pass the Critic / Noise Gate.

### Critic / Noise Gate

Blocks or downgrades:

- unsupported claims
- overconfident language
- missing limitations
- contradictions
- buy/sell recommendation drift
- prediction without evidence

Implemented Phase 7 boundary:

- deterministic preview only
- direct Evidence Ledger entry input
- optional draft-claim checks
- no LLM calls
- no final report generation

The preview returns pass / needs_revision / blocked decisions, check results, blocked claims, downgraded claims, allowed claims, required revisions, a fallback message, and warnings. It blocks unsupported ledger entries and trading-advice drift, and it requires revision for contradictions, missing source recency, missing limitations, and high-confidence single-source claims.

Implemented Phase 13 boundary:

- `POST /noise-gates` persists a gate decision record
- `GET /noise-gates` lists stored gate records
- operations summary and dashboard count blocked and needs-revision gate decisions
- persisted Noise Gate records can link to parent `agent_runs` and workflow parents where created through traced/workflow paths
- `POST /retrieval-runs/{retrieval_run_id}/noise-gate` creates a retrieval-run-linked Noise Gate after linked Evidence Ledger entries exist
- retrieval-run-linked Noise Gate records expose consumed upstream ids in metadata rather than claiming broad free-form judgment

### Claim-bounded Report

Generates a claim-bounded report-shaped preview that includes:

- claims
- source ids
- evidence spans
- confidence
- limitations
- contradictions
- next data needed

Implemented Phase 8 boundary:

- deterministic preview only
- runs Noise Gate before report formatting
- no LLM calls
- no DB persistence in `/reports/preview`
- no dashboard

The preview generates report-shaped output only when the gate passes. Blocked or revision-needed gate outputs return the fallback message and required revisions instead of a report.

Implemented Phase 14 boundary:

- `POST /reports` persists deterministic report preview records
- `GET /reports` lists stored report preview records
- operations summary and dashboard count generated, blocked, and needs-revision report records
- persisted Report records can link to parent `agent_runs` and workflow parents where created through traced/workflow paths
- `POST /retrieval-runs/{retrieval_run_id}/report` creates a retrieval-run-linked Report after the linked Noise Gate exists
- retrieval-run-linked Report records preserve the input Noise Gate id in `stage_input_manifest`; they are not free-form final answers

### Run Log / Failure Case

Records each agent run and failure case for later evaluation.

Failures are not hidden. They are portfolio evidence.

The current tracing boundary creates `agent_runs` records for traced operations and records workflow parent/child provenance for deterministic preview workflows. `trace_json`, `workflow_trace_id`, `workflow_run_id`, and stage input manifests are metadata tracing for inspectability, not distributed tracing or hosted observability.

The failure-case workflow review queue is a read model over failed, blocked, and needs-revision `workflow_runs` plus existing `failure_cases.workflow_run_id` links. `GET /failure-cases/workflow-review-queue` surfaces parents that still need human review, but it does not create failure_cases, does not automate root-cause classification, and does not prove complete workflow failure causality.

The failure-case workflow review queue dashboard surfacing adds a compact read-model section to `GET /ops/dashboard`. It shows queue counts and review statuses, but it does not create failure_cases or change workflow/failure-case persistence.

## Planned Data Model

### Document

```text
id
source_type
source_uri
filename
title
created_at
source_date
profile_json
extraction_quality
status
```

### Chunk

```text
id
document_id
chunk_strategy
chunk_index
text
metadata_json
embedding
created_at
```

### RetrievalRun

```text
id
question
strategy
created_at
latency_ms
result_count
hit_rate
citation_coverage
missing_evidence_count
status
metadata_json
workflow_run_id
```

### EvidenceLedgerEntry

```text
id
run_id
agent_run_id
workflow_trace_id
workflow_run_id
question
claim
source_id
source_type
source_date
evidence_span
confidence
limitation
contradicting_source_ids
status
matched_terms
role
created_at
```

Status values:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

### AgentRun

```text
id
user_question
workflow_version
started_at
ended_at
status
error_message
token_cost
latency_ms
trace_json
```

### WorkflowRun

```text
id
question
workflow_version
status
trace_json
created_at
started_at
ended_at
latency_ms
error_message
```

### FailureCase

```text
id
agent_run_id
failure_type
description
root_cause
fix_status
next_action
created_at
```

### NoiseGateRecord

```text
id
workflow_trace_id
agent_run_id
workflow_run_id
stage_input_manifest
question
decision
final_response_allowed
checks
blocked_claims
downgraded_claims
allowed_claims
required_revisions
fallback_message
warnings
evidence_entry_count
draft_claim_count
created_at
```

### ReportRecord

```text
id
workflow_trace_id
agent_run_id
workflow_run_id
stage_input_manifest
question
status
report
gate
gate_decision
fallback_message
required_revisions
warnings
claim_count
evidence_entry_count
draft_claim_count
created_at
```

## Planned API Surface

Day 2 implemented metadata and ops skeleton endpoints. Phase 3 added parse-preview for parser adapter boundaries. Phase 4 added chunk-preview for strategy comparison. Phase 5 added retrieval-runs for lexical retrieval candidate search and run recording. Phase 5.5 added collection-plan preview for role-based information needs. Phase 6 added evidence-ledger preview for claim-level evidence records over retrieval candidates. Phase 7 added noise-gate preview for pre-report claim checks. Phase 8 added report preview for claim-bounded output after the gate passes. Phase 9 added a plain operations dashboard over existing metadata. Phase 11 added auto-created `agent_runs.trace_json` records for preview endpoints. Phase 12 added persisted Evidence Ledger records. Phase 13 added persisted Noise Gate records. Phase 14 added persisted Report Preview records. Phase 15 added shared `workflow_trace_id` correlation across persisted evidence/gate/report records and agent-run traces. Phase 16 added direct trace-id lookup. Phase 17 added read-only filters on persisted Evidence Ledger, Noise Gate, and Report record lists. Phase 18 added trace lookup and filter links to the plain operations dashboard. Phase 18.5 reviewed direct `agent_run_id` foreign-key linkage and kept it unimplemented until the run lifecycle is changed. Phase 19 added parent agent-run lifecycle updates before child-record foreign keys. Phase 20 added `agent_run_id` fields to persisted evidence, gate, and report records. Phase 21 added parent run links for persisted gate and report rows in the plain operations dashboard. Phase 22 added persisted Evidence Ledger rows to the dashboard. Phase 22.5 reviewed direct evidence -> gate -> report links and deferred them until a single workflow parent exists. Phase 23 reviewed workflow parent ownership and deferred a separate `workflow_runs` table to the next implementation gate. Phase 24 added the `workflow_runs` schema and migration without implementing workflow execution. Phase 25 added `workflow_runs` create/list metadata persistence without implementing orchestration. Phase 26 added workflow-run rows to the plain operations dashboard with metadata-only boundary copy. Phase 27 reviewed child `workflow_run_id` links and deferred them until workflow execution owns the sequence. Phase 28 added deterministic workflow execution preview. Phase 29 added nullable child `workflow_run_id` links for retrieval, evidence, gate, and report rows created by that deterministic preview. Phase 30 added workflow-run detail lookup for inspecting those linked child records from one workflow parent. Phase 30.5 reviewed direct evidence -> gate -> report links again and deferred foreign-key links until downstream stages consume persisted upstream row ids. Phase 31 added `stage_input_manifest` to deterministic workflow-created Noise Gate and Report records so persisted upstream ids are visible without claiming direct foreign-key lineage. Phase 31.5 reviewed direct cross-stage schema links and deferred new FK/join-table storage in favor of a derived workflow lineage read model. Phase 32 added `GET /workflow-runs/{id}/lineage` as that derived read model over existing workflow child records and `stage_input_manifest` values. Phase 33 linked workflow dashboard rows to both the detail and lineage read-model endpoints. Phase 33.5 reviewed missing-reference behavior and deferred proof to a targeted test fixture rather than schema or mutation changes. Phase 34 added that targeted missing-reference test fixture. Phase 34.5 reviewed manifest-shape hardening risks before any schema expansion. Phase 35 hardened manifest-shape parsing without adding schema. Phase 35.5 reviewed lineage warning categories before adding structured warning fields. Phase 36 added `warning_codes` to the lineage response while preserving human-readable warnings. Phase 36.5 reviewed warning-code documentation boundaries before adding dashboard or persistence behavior. Phase 37 added a runbook lineage response shape with both `warnings` and `warning_codes`.

Implemented endpoints:

```text
POST /documents
GET  /documents
POST /documents/profile
POST /documents/parse-preview
POST /documents/chunk-preview
POST /documents/upload-intake-manifest-preview
POST /documents/upload-intake-manifests
GET  /documents/upload-intake-manifests
POST /documents/upload-parsed-documents
POST /documents/{document_id}/chunks
GET  /documents/{document_id}/chunks
POST /documents/upload-chunks
POST /documents/upload-retrieval-preview
POST /chunks/{chunk_id}/embeddings
GET  /chunks/{chunk_id}/embeddings
POST /documents/{document_id}/semantic-retrieval-preview
POST /documents/{document_id}/semantic-retrieval-runs
POST /documents/upload-raw-files
GET  /documents/upload-raw-files
POST /documents/upload-raw-files/{raw_file_id}/scan-results
GET  /documents/upload-raw-files/{raw_file_id}/scan-results
POST /documents/upload-raw-files/{raw_file_id}/scan
POST /collection-plans/preview
POST /retrieval-runs
GET  /retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
POST /retrieval-runs/{retrieval_run_id}/report
POST /evidence-ledgers/preview
POST /evidence-ledgers
GET  /evidence-ledgers
POST /noise-gates/preview
POST /noise-gates
GET  /noise-gates
POST /reports/preview
POST /reports
GET  /reports
GET  /traces/{workflow_trace_id}
POST /agent-runs
GET  /agent-runs
POST /workflow-runs
GET  /workflow-runs
POST /workflow-runs/execute-preview
GET  /workflow-runs/{id}
GET  /workflow-runs/{id}/lineage
POST /failure-cases
GET  /failure-cases
GET  /failure-cases/workflow-review-queue
GET  /ops/summary
GET  /ops/dashboard
```

Planned later endpoints:

```text
GET  /documents/{id}
GET  /retrieval-runs/{id}
```

Current endpoints include uploaded file preview/parsing handoffs, parsed document metadata persistence, chunk persistence, retrieval persistence, raw upload quarantine storage, caller-provided embeddings, caller-provided semantic retrieval persistence, and retrieval-run-linked Evidence Ledger / Noise Gate / Report handoffs.

Current endpoints still do not perform robust PDF extraction, generate embeddings, persist collection plans, create direct evidence -> gate -> report foreign-key lineage, invoke an LLM, search external sources, create autonomous free-form agents, create free-form final answers, prove endpoint malicious-detection runtime behavior, prove hosted deployment, or provide distributed tracing. The current workflow parent proves common workflow membership, not direct stage-level causality between persisted Evidence Ledger rows, Noise Gate records, and Report records.

## Agent Workflow

Planned explicit workflow:

1. Ingestion Agent receives source input and creates a document profile.
2. Retrieval Agent chunks, indexes, retrieves, and records retrieval quality.
3. Analysis Agent drafts claims from retrieved evidence.
4. Critic Agent blocks unsupported claims and surfaces contradictions.
5. Report Agent produces a claim-bounded report.

Each stage must log input and output. Current runtime evidence includes traced operations, workflow parent rows, child record links, stage input manifests, and a derived lineage read model. This is still deterministic preview/workflow metadata, not autonomous multi-agent orchestration, hosted observability, or distributed tracing.

## Evaluation Surface

Evaluation should include:

- sample dataset description
- retrieval metrics
- answer quality checks
- unsupported claim examples
- contradiction examples
- failures and next fixes

Implemented Phase 10 docs:

```text
docs/evaluation/eval-plan.md
docs/evaluation/retrieval-eval-report.md
docs/evaluation/failure-cases.md
docs/application/braincrew-role-map.md
docs/application/cover-message.md
docs/application/portfolio-index.md
docs/review/application-ready-review.md
```

These documents do not claim production retrieval quality. They describe current evidence, remaining gaps, and application framing.

## Operations Dashboard

Phase 9 implements a plain FastAPI HTML dashboard at `GET /ops/dashboard`.

It currently shows:

- recent agent runs
- failed questions
- retrieval failures
- unsupported claim count
- contradiction count
- blocked and needs-revision gate counts
- average latency
- failure cases

Current limitations:

- unsupported claim and contradiction counts come from persisted Evidence Ledger entries
- blocked and needs-revision gate counts come from persisted Noise Gate records
- generated, blocked, and needs-revision report counts come from persisted Report records
- the failure-case workflow review queue dashboard surfacing is a read-model display over existing workflow and failure-case rows
- token cost rollups and chunk strategy comparison require later persistence work
- dashboard does not add Next.js or a polished product UI
- dashboard does not create new retrieval, evidence, gate, or report behavior

This matters more than visual polish.

## Deployment Plan

MVP deployment order:

1. Local Docker Compose
2. GitHub Actions CI
3. Local demo with sample messy data
4. Optional hosted deployment only after local workflow works

Planned hosting options after MVP:

- Render
- Fly.io
- AWS Lightsail
- EC2

No hosted deployment is claimed on Day 1.
