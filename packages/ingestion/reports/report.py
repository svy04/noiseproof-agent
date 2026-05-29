from collections import defaultdict

from packages.ingestion.noise_gate import run_noise_gate
from packages.ingestion.types import (
    ClaimBoundedReport,
    EvidenceLedgerEntry,
    ReportClaim,
    ReportPreview,
)


def create_report_preview(
    question: str,
    entries: list[EvidenceLedgerEntry],
    draft_claims: list[str] | None = None,
) -> ReportPreview:
    gate = run_noise_gate(question=question, entries=entries, draft_claims=draft_claims)
    warnings = [
        "Report Preview is deterministic and does not use an LLM.",
        "It only formats claims that passed the Noise Gate; it does not create new claims.",
    ]

    if gate.decision != "pass":
        return ReportPreview(
            question=gate.question,
            status=gate.decision,
            report=None,
            gate=gate,
            fallback_message=gate.fallback_message,
            required_revisions=gate.required_revisions,
            warnings=warnings,
        )

    report = _build_report(entries, gate.allowed_claims)
    return ReportPreview(
        question=gate.question,
        status="generated",
        report=report,
        gate=gate,
        fallback_message=None,
        required_revisions=[],
        warnings=warnings,
    )


def _build_report(entries: list[EvidenceLedgerEntry], allowed_claims: list[str]) -> ClaimBoundedReport:
    entries_by_claim: dict[str, list[EvidenceLedgerEntry]] = defaultdict(list)
    for entry in entries:
        if entry.claim in allowed_claims and entry.status == "supported":
            entries_by_claim[entry.claim].append(entry)

    claims = [
        _report_claim(claim, claim_entries)
        for claim, claim_entries in sorted(entries_by_claim.items(), key=lambda item: item[0])
    ]
    limitations = sorted(
        {
            limitation
            for claim in claims
            for limitation in claim.limitations
            if limitation
        }
    )
    contradictions = sorted(
        {
            contradiction
            for claim in claims
            for contradiction in claim.contradictions
            if contradiction
        }
    )
    return ClaimBoundedReport(
        summary=f"{len(claims)} claim(s) can be stated with current evidence boundaries.",
        claims=claims,
        limitations=limitations,
        contradictions=contradictions,
        next_data_needed=_next_data_needed(claims),
    )


def _report_claim(claim: str, entries: list[EvidenceLedgerEntry]) -> ReportClaim:
    return ReportClaim(
        claim=claim,
        source_ids=sorted({entry.source_id for entry in entries if entry.source_id}),
        evidence_spans=_unique_preserving_order(entry.evidence_span for entry in entries if entry.evidence_span),
        confidence=_lowest_confidence(entries),
        limitations=_unique_preserving_order(entry.limitation for entry in entries if entry.limitation),
        contradictions=sorted(
            {
                source_id
                for entry in entries
                for source_id in entry.contradicting_source_ids
            }
        ),
    )


def _lowest_confidence(entries: list[EvidenceLedgerEntry]) -> str:
    order = {"none": 0, "low": 1, "medium": 2, "high": 3}
    confidence = min((entry.confidence for entry in entries), key=lambda item: order.get(item, 0))
    return confidence


def _next_data_needed(claims: list[ReportClaim]) -> list[str]:
    needs: list[str] = []
    for claim in claims:
        if len(claim.source_ids) < 2:
            needs.append(f"Add an independent second source for claim: {claim.claim}")
        if not claim.contradictions:
            needs.append(f"Check for contradicting sources for claim: {claim.claim}")
    return _unique_preserving_order(needs)


def _unique_preserving_order(items) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        output.append(item)
    return output
