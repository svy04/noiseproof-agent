from app.schemas import FailureCaseCreate, FailureCaseDraftPreviewOut


def evidence_quality_risk_reasons(entry: dict) -> list[str]:
    reasons: list[str] = []
    if entry.get("status") == "weakly_supported":
        reasons.append("weakly_supported")
    if entry.get("confidence") == "low":
        reasons.append("low_confidence")
    if not entry.get("source_date"):
        reasons.append("missing_source_date")
    return reasons


def preview_evidence_quality_failure_case_draft(
    entry: dict,
) -> FailureCaseDraftPreviewOut:
    reasons = evidence_quality_risk_reasons(entry)
    risk_summary = ", ".join(reasons) if reasons else "none"
    entry_id = str(entry.get("id"))
    question = str(entry.get("question") or "Unknown question")
    claim = str(entry.get("claim") or "Unknown claim")

    draft = FailureCaseCreate(
        agent_run_id=entry.get("agent_run_id"),
        workflow_run_id=entry.get("workflow_run_id"),
        failure_type="evidence_quality_risk",
        description=(
            f"Evidence Ledger entry '{entry_id}' for question '{question}' "
            "has quality risk markers before report handoff."
        ),
        root_cause=(
            f"risk_reasons={risk_summary}; status={entry.get('status')}; "
            f"confidence={entry.get('confidence')}; source_date={entry.get('source_date')}"
        ),
        fix_status="draft",
        next_action=(
            "Inspect the source, add stronger or corroborating evidence, or keep "
            "the claim boundary visible before manually creating a failure case."
        ),
    )
    source_summary = {
        "stage": "persisted_evidence_ledger_quality_risk",
        "evidence_ledger_entry_id": entry_id,
        "question": question,
        "claim": claim,
        "source_id": entry.get("source_id"),
        "source_type": entry.get("source_type"),
        "source_date": entry.get("source_date"),
        "status": entry.get("status"),
        "confidence": entry.get("confidence"),
        "risk_reasons": reasons,
    }
    warnings = [
        "Preview only; this does not create failure_cases.",
        "A human confirmation boundary is required before persistence.",
        "This is operations metadata handoff, not final truth adjudication.",
        "This is not Evidence Ledger quality evidence, retrieval quality evidence, or an LLM judgment.",
    ]
    return FailureCaseDraftPreviewOut(
        draft=draft,
        source_summary=source_summary,
        persistence_boundary="preview_only_not_persisted",
        human_confirmation_required=True,
        warnings=warnings,
    )
