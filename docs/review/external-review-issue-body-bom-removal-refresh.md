# External Review Issue Body BOM Removal Refresh

Status: owner-authored issue body readability repair.

Phase marker: external review issue body BOM removal refresh v0.

Public issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

This artifact records a live issue body repair that removed a leading UTF-8 BOM character from the reviewer-facing issue body while preserving the latest persisted Report markdown export routing.

## Repair Evidence

```text
before_first_codepoint: 65279
after_first_codepoint: 35
after_starts_with_request: true
utf8_no_bom_body_file
updatedAt: 2026-06-05T15:48:38Z
comment_count: 1
```

The issue body still includes the latest proof routing:

```text
persisted Report markdown export proof
docs/review/persisted-report-markdown-export.md
GET /reports/{report_record_id}/markdown
docs/review/persisted-report-markdown-export-remote-verification.md
docs/review/external-reviewer-persisted-report-markdown-export-request-refresh.md
docs/review/external-review-issue-body-persisted-report-markdown-export-refresh.md
```

## Command Shape

The body file was written with UTF-8 without BOM before calling `gh issue edit`:

```powershell
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($tmp, $clean, $utf8NoBom)
gh issue edit 1 --repo svy04/noiseproof-agent --body-file $tmp
```

## Boundary

This is an owner-authored issue body readability repair.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not free-form report generation.

This is not a new report-generation path.

This is not an LLM call.

This is not retrieval.

This is not Evidence Ledger creation.

This is not Noise Gate behavior.

This is not Report record creation.

This is not financial advice.

This is not product-complete.
