# Uploaded File Chunk Persistence Handoff Review

Status: review-only product boundary.

Phase marker: uploaded file chunk persistence handoff review v0.

Label: Uploaded file chunk persistence handoff review.

This review decides the next product gate after explicit document-scoped chunk persistence. The current system can manually persist chunks for an existing document through `POST /documents/{document_id}/chunks`, and uploaded-file chunk preview remains preview-only. The next useful product step is an explicit handoff endpoint that can take an uploaded file, parse it, create a document metadata row, and persist derived chunk text rows without storing raw uploaded bytes or full parsed text.

## Current State

Implemented:

```text
POST /documents/upload-chunk-preview
POST /documents/{document_id}/chunks
GET /documents/{document_id}/chunks
documents table
document_chunks table
chunk_text_only_no_raw_file_storage boundary
```

Still intentionally not implemented:

```text
automatic persistence from upload preview
raw uploaded byte storage
full parsed text persistence
embeddings
retrieval persistence
Evidence Ledger generation
Noise Gate generation
report generation
```

## Decision

Select an explicit handoff endpoint as the next product implementation candidate:

```text
POST /documents/upload-chunks
```

This should be a new explicit handoff endpoint, not a behavior change to the existing preview route.

The existing upload chunk preview remains preview-only.

The future endpoint uses existing documents and document_chunks tables. It should not require a new table unless implementation evidence shows that the current schema cannot represent the handoff safely.

## Intended Future Behavior

The future endpoint may:

```text
accept uploaded content
run parser/profile/chunking logic
create a document metadata row
create derived document_chunks rows for the chosen strategy
return document_id, chunk_count, chunk ids, warnings, and persistence boundary
```

The future endpoint must keep this boundary:

```text
no raw uploaded byte storage
no full parsed text persistence
no embeddings
no retrieval persistence
not automatic persistence from upload preview
human-readable parser/chunk warnings returned
failure-case draft only when handoff cannot complete
```

## Alternatives Considered

### 1. Mutate `POST /documents/upload-chunk-preview`

Rejected.

Changing preview into a write path would break the current proof boundary. Preview routes should stay safe to call without persistence side effects.

### 2. Persist retrieval next

Rejected for the next immediate gate.

Retrieval persistence over uploaded content is easier to inspect after uploaded files can produce durable document and chunk rows through an explicit handoff path.

### 3. Store raw uploaded files first

Rejected for now.

The current project thesis is inspectable evidence and claim boundaries, not file-storage infrastructure. Raw byte storage can be reviewed later if replayability requires it.

### 4. Create a new raw parsed text table first

Rejected for now.

The existing `document_chunks` table is enough for the next small product gate because the desired persisted unit is derived chunk text, not full parsed documents.

## Acceptance for the Next Gate

The next implementation gate should be:

```text
uploaded file chunk persistence handoff endpoint v0
```

It should prove only:

```text
an explicit upload-to-chunks handoff endpoint can create a document row and chunk rows
```

It must not claim:

```text
robust PDF extraction
raw file storage
full parsed text storage
retrieval persistence
embeddings
semantic retrieval
Evidence Ledger persistence
Noise Gate persistence
report persistence
product completeness
```

## Allowed Claim

NoiseProof has selected a small explicit handoff endpoint as the next product gate: uploaded file input to document metadata plus derived chunk rows, using existing documents and document_chunks tables.

## Boundary

This is review-only.

It adds no endpoint code.

It adds no schema or migration.

It creates no document rows and no chunk rows.

It is not automatic persistence from upload preview.

It is not raw uploaded byte storage.

It is not full parsed text persistence.

It adds no embeddings.

It adds no retrieval persistence.

It is not external reviewer feedback.

It is not hosted deployment evidence.

## Next Gate

```text
uploaded file chunk persistence handoff endpoint v0
```
