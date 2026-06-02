# Semantic Retrieval Quality Report Reviewer Request Refresh

Status: request infrastructure only.

Phase marker: semantic retrieval quality report reviewer request refresh v0.

This refresh points reviewer-facing request surfaces to the toy semantic retrieval quality report.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate.

## Latest Report To Inspect

toy semantic retrieval quality report:

```text
docs/evaluation/semantic-retrieval-quality-report.md
```

Related application refresh:

```text
docs/review/semantic-retrieval-quality-report-application-refresh.md
```

Report markers:

```text
fixture_id: semantic-retrieval-quality-fixture-v0
Hit@k: 0.75
Recall@k: 0.375
MRR@k: 0.375
nDCG@k: 0.198
semantic_vs_lexical_disagreement: 0.9167
visible failure: q-what-missing
```

## Reviewer Surfaces Refreshed

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/review/readme-proof-marker-archive.md`

## Allowed Claim

External reviewers can now reach the toy semantic retrieval quality report from the standard review entry surfaces.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not vector search quality evidence.

This is not a benchmark result.

This is not a model comparison.

This does not prove production semantic retrieval quality.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, LLM call, embedding generation, vector index behavior, Evidence Ledger generation, Critic/Noise Gate behavior, final report generation, financial advice behavior, automatic failure-case creation, or product-complete claim.

The next bounded request gate should update or verify the live public issue body so issue #1 points reviewers to the toy semantic retrieval quality report:

```text
semantic retrieval quality report reviewer issue-body refresh v0
```
