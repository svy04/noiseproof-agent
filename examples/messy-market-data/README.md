# Messy Market Data Fixtures

These fixtures are intentionally small and imperfect. They exist to test Document Profiler v0 before parsing, chunking, embeddings, retrieval, or report generation exists.

## Files

- `sample-note.md`: markdown memo with dates, numbers, and a source URL.
- `sample-market.csv`: small CSV with mixed numeric fields and notes.
- `sample-report.txt`: plain text report excerpt with conflicting language.
- `sample-page.html`: HTML-like page content with links and repeated navigation text.

## Expected Difficulty

The profiler should detect:

- text length and line count
- approximate token count
- URLs
- dates
- numbers
- table-like or row-like structure
- extraction quality warnings
- a recommended next strategy

The profiler should not claim:

- successful parsing
- chunk quality
- retrieval quality
- Evidence Ledger support
- contradiction detection
- final market insight
