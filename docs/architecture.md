# Architecture: NoiseProof Agent

## Implementation Status

Day 2 status:

- Architecture is documented.
- PostgreSQL with pgvector is configured in Docker Compose.
- PostgreSQL schema init SQL exists for documents, agent runs, and failure cases.
- FastAPI skeleton exists for health, metadata persistence, and ops summary placeholder.
- Web app, ingestion, retrieval, Evidence Ledger, agents, and dashboard are planned but not implemented.

This document describes the intended system so implementation can proceed without drifting into a trading bot or a generic RAG demo.

## System Overview

NoiseProof Agent is an evidence-first RAG/agent workflow for messy market intelligence.

Core flow:

```text
Source Upload / URL Input
  -> Document Profiler
  -> Parser Selector
  -> Chunk Strategy Experiment
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
Source -> Document Profiler -> Parser -> Chunker -> Index -> Retrieval -> Evidence Ledger -> Critic -> Report -> Run Log
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

Generates a profile for each document:

- source type
- source URI or filename
- title if available
- source date if available
- extraction quality
- text length
- likely parser
- limitations

### Parser Selector

Chooses the parser by input type and extraction quality.

Planned defaults:

- PyMuPDF or pdfplumber for PDF
- pandas for CSV
- BeautifulSoup or trafilatura for URL/HTML
- plain markdown parser for memo

### Chunk Strategy Experiment

Runs multiple chunking strategies against the same document.

Planned strategies:

- fixed-size chunking
- heading-based chunking
- semantic or simple heuristic chunking

The goal is to compare retrieval quality, not to assume one chunking method is always best.

### Indexing

Stores chunks and embeddings in PostgreSQL with pgvector for MVP.

Qdrant remains an alternative if pgvector slows delivery, but Day 1 chooses pgvector to keep the local stack small.

### Retrieval

Runs a question against indexed chunks and records:

- strategy
- latency
- result count
- hit rate
- citation coverage
- missing evidence count

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

Day 2 implemented only metadata and ops skeleton endpoints.

Implemented endpoints:

```text
POST /documents
GET  /documents
POST /agent-runs
GET  /agent-runs
POST /failure-cases
GET  /failure-cases
GET  /ops/summary
```

Planned later endpoints:

```text
GET  /documents/{id}
POST /retrieval-runs
GET  /retrieval-runs/{id}
GET  /retrieval-runs/{id}/evidence-ledger
POST /reports
```

Day 2 endpoints do not parse files, run retrieval, generate an Evidence Ledger, invoke an LLM, or create final reports.

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
