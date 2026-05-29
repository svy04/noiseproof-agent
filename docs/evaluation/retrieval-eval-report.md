# Retrieval Evaluation Report

Status: Phase 10 initial report.

This is not a benchmark claim. It records what the current lexical retrieval v0 can and cannot show.

## Current Retrieval Surface

Implemented:

- lexical retrieval over chunk-preview output
- `POST /retrieval-runs`
- `GET /retrieval-runs`
- source ids attached to retrieval candidates
- persisted retrieval run metadata
- no-results runs recorded with `status: no_results`

Not implemented:

- embeddings
- vector search
- semantic reranking
- persisted chunks
- larger labeled evaluation set

## Not Yet Measured

Not yet measured:

- corpus-level hit rate
- recall against a labeled gold set
- precision by question type
- semantic retrieval quality
- cross-document contradiction recall
- chunk strategy performance on real PDFs

## Verified Behaviors

The current automated tests verify that lexical retrieval can:

- return ranked chunk candidates with source ids
- record retrieval run metadata
- record `no_results` when no candidate matches the question
- preserve citation-related metadata for later Evidence Ledger work

## Example Interpretation

If a question asks:

```text
Which segment had enterprise demand growth?
```

and a markdown source contains:

```text
Enterprise demand grew 12% in 2026.
```

lexical retrieval can return that chunk with a source id and matched terms.

This does not prove truth. It only gives later phases a source-linked candidate to inspect.

## Boundary

Current retrieval is useful as a portfolio proof of service shape and evidence plumbing.

It should not be described as production RAG quality.
