# ADR 001: Why RAG/Agent Instead of Chat-Only Analysis

## Status

Accepted

## Context

NoiseProof Agent works with messy market documents where source quality, contradictions, and missing evidence matter. A chat-only LLM can answer quickly, but it does not naturally preserve source profiles, retrieval metrics, evidence spans, blocked claims, or failure records.

The project needs an inspectable workflow that can show why a report should or should not be trusted.

## Decision

Use a RAG/agent workflow with explicit stages:

```text
ingestion -> profiling -> chunking -> retrieval -> evidence ledger -> critic gate -> report -> run log
```

The workflow should remain explicit before adopting a complex agent framework.

## Alternatives considered

1. Chat-only LLM with pasted context
   - Simpler to start, but weak at preserving retrieval quality, source metadata, and failure cases.
2. Manual research notebook
   - Highly inspectable, but does not prove service design, workflow automation, or operational logging.
3. End-to-end autonomous multi-agent system
   - Sounds impressive, but increases scope before evidence and logging are stable.

## Consequences

- The system can log each stage.
- Evidence can be reviewed before final report generation.
- Unsupported claims can be blocked.
- Implementation is larger than a simple chat demo.
- The project must avoid pretending planned agent stages are already implemented.

## What would change this decision

This decision would change if a simpler non-RAG workflow could reliably ingest mixed documents, retrieve source-linked evidence, surface contradictions, block unsupported claims, and record failure cases with less implementation complexity.
