# ADR 002: Why FastAPI and Next.js

## Status

Accepted

## Context

NoiseProof Agent needs a small full-stack service: API endpoints for ingestion and agent runs, a database-backed evidence trail, and a basic operations dashboard. The goal is not UI polish on Day 1. The goal is an inspectable service architecture that can grow into a portfolio artifact.

The default implementation stack is Python for data/RAG work and TypeScript for the web dashboard.

## Decision

Use:

```text
Backend: Python, FastAPI, Pydantic
Frontend: Next.js, TypeScript, Tailwind
Data: PostgreSQL with pgvector
```

FastAPI fits Python-native parsing, retrieval, and agent workflow code. Next.js fits a lightweight operations dashboard and portfolio-friendly web surface.

## Alternatives considered

1. Python-only Streamlit app
   - Faster for a demo, but weaker as evidence for service architecture, API design, and full-stack operations.
2. Next.js-only app with server actions
   - Simple deployment story, but less natural for PDF/CSV parsing, retrieval experiments, and Python RAG tooling.
3. Django monolith
   - Strong batteries-included framework, but heavier than needed for the first inspectable service.

## Consequences

- The backend can use mature Python parsing and retrieval libraries.
- The frontend can focus on operations visibility.
- The repo will need separate app boundaries for API and web in later phases.
- Day 1 must not define fake API/web services before they exist.

## What would change this decision

This decision would change if the project needed a single-process internal tool more than a service portfolio artifact, or if the retrieval stack moved decisively to a TypeScript-native implementation.
