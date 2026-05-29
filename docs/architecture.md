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
- Web app, file upload parsing, robust PDF extraction, persisted chunks, persisted collection plans, embeddings, Evidence Ledger, agents, and dashboard are planned but not implemented.

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
- PDF parser is a text-only fallback and does not claim robust PDF extraction
- unknown source types return a structured warning and failure-case candidate

The parser output can feed Document Profiler v0. Parse-preview does not save records to the database.

Planned defaults:

- PyMuPDF or pdfplumber for PDF
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

The goal is to compare chunk shapes before retrieval, not to assume one chunking method is always best. Chunks are not persisted yet.

Research scope note:

- `fixed-window` keeps the familiar `max_characters` / `overlap` vocabulary used by common text splitter APIs.
- `heading-aware` preserves section paths so later retrieval work can inspect whether source structure was lost.
- `row-aware` preserves CSV headers and row indices so tabular evidence can stay auditable.
- Phase 4 does not add external chunking dependencies; it only creates a local, inspectable comparison boundary.

### Indexing

Stores chunks and embeddings in PostgreSQL with pgvector for MVP.

Qdrant remains an alternative if pgvector slows delivery, but Day 1 chooses pgvector to keep the local stack small.

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

Retrieval candidates are not Evidence Ledger entries. They are possible source-linked evidence candidates for the next phase.

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

### Claim-bounded Report

Generates a final report that includes:

- claims
- source ids
- evidence spans
- confidence
- limitations
- contradictions
- next data needed

### Run Log / Failure Case

Records each agent run and failure case for later evaluation.

Failures are not hidden. They are portfolio evidence.

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
```

### EvidenceLedgerEntry

```text
id
run_id
claim
source_id
source_type
source_date
evidence_span
confidence
limitation
contradicting_source_ids
status
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

## Planned API Surface

Day 2 implemented metadata and ops skeleton endpoints. Phase 3 added parse-preview for parser adapter boundaries. Phase 4 added chunk-preview for strategy comparison. Phase 5 added retrieval-runs for lexical retrieval candidate search and run recording. Phase 5.5 added collection-plan preview for role-based information needs.

Implemented endpoints:

```text
POST /documents
GET  /documents
POST /documents/profile
POST /documents/parse-preview
POST /documents/chunk-preview
POST /collection-plans/preview
POST /retrieval-runs
GET  /retrieval-runs
POST /agent-runs
GET  /agent-runs
POST /failure-cases
GET  /failure-cases
GET  /ops/summary
```

Planned later endpoints:

```text
GET  /documents/{id}
GET  /retrieval-runs/{id}
GET  /retrieval-runs/{id}/evidence-ledger
POST /reports
```

Current endpoints do not parse uploaded files, perform robust PDF extraction, persist chunks, persist collection plans, compute embeddings, generate an Evidence Ledger, invoke an LLM, create final answers, or create final reports.

## Agent Workflow

Planned explicit workflow:

1. Ingestion Agent receives source input and creates a document profile.
2. Retrieval Agent chunks, indexes, retrieves, and records retrieval quality.
3. Analysis Agent drafts claims from retrieved evidence.
4. Critic Agent blocks unsupported claims and surfaces contradictions.
5. Report Agent produces a claim-bounded report.

Each stage must log input and output.

## Evaluation Surface

Evaluation should include:

- sample dataset description
- retrieval metrics
- answer quality checks
- unsupported claim examples
- contradiction examples
- failures and next fixes

Planned docs:

```text
docs/evaluation/eval-plan.md
docs/evaluation/retrieval-eval-report.md
docs/evaluation/failure-cases.md
```

Day 1 does not create evaluation results because no retrieval implementation exists yet.

## Operations Dashboard

The planned dashboard should show:

- recent agent runs
- failed questions
- retrieval failures
- unsupported claim count
- contradiction count
- average latency
- token cost or placeholder
- chunk strategy comparison
- failure cases

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
