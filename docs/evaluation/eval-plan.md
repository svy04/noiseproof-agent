# Evaluation Plan

Status: Phase 10 initial evaluation plan.

This document defines how NoiseProof Agent should be evaluated before it is described as more than a small, inspectable portfolio system.

## Evaluation Principle

NoiseProof Agent should not be judged by whether it gives impressive answers.

It should be judged by whether unsupported answers fail to pass.

## Sample Dataset

The current sample dataset is intentionally small and fixture-like:

- `examples/messy-market-data/sample-note.md`
- `examples/messy-market-data/sample-market.csv`
- `examples/messy-market-data/sample-report.txt`
- `examples/messy-market-data/sample-page.html`

The sample dataset covers markdown, CSV-like rows, report text, and HTML-like source material. It does not prove production ingestion quality.

## Metrics

Current measurable checks:

- parser returns text, metadata, warnings, or a failure-case candidate
- profiler detects source type, character count, line count, URLs, dates, numbers, tables, extraction quality, and recommended strategy
- chunk preview compares fixed-window, heading-aware, and row-aware strategies
- lexical retrieval returns source ids
- no-result retrieval runs are persisted with `status: no_results`
- Evidence Ledger Preview can mark supported, weakly_supported, contradicted, unsupported, and blocked entries
- Noise Gate Preview can block unsupported claim and buy/sell drift
- Report Preview returns no report when the gate blocks or requires revision
- Operations Dashboard v0 surfaces agent runs, failure cases, and retrieval runs

Planned later metrics:

- retrieval hit rate across a larger labeled fixture set
- citation coverage over expected source ids
- missing evidence count by question type
- contradiction surfacing rate
- unsupported claim block rate
- report revision rate after Noise Gate

## Evaluation Questions

Use these question classes:

- general market question
- underspecified question
- numeric evidence question
- source quality question
- contradiction question
- unsupported claim question
- buy/sell drift question

## Unsupported Claim Checks

An unsupported claim should not reach final report output.

Examples:

- no retrieval candidates
- empty evidence span
- missing source id
- explicit buy/sell intent
- overconfident draft language without evidence

Expected behavior:

- Evidence Ledger entry becomes `unsupported` or `blocked`
- Noise Gate decision becomes `blocked` or `needs_revision`
- Report Preview returns `report: null`

## Commands

From `apps/api`:

```bash
uv run python -m compileall app ../../packages/ingestion
uv run pytest -q
```

From repo root, if Docker is available:

```bash
docker compose config --quiet
docker compose ps
```

## Not Yet Proven

- robust PDF extraction
- semantic retrieval quality
- embeddings
- production-scale ingestion
- persisted chunks
- retrieval-run-linked Evidence Ledger records
- agent-run-linked Noise Gate records
- persisted reports
- external user validation
- financial prediction quality
