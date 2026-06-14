from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse

from app.db import Repository, get_repository
from app.schemas import (
    OpsSummaryOut,
    ProofGapActionDetailOut,
    ProofGapActionListOut,
)
from app.services.embedding_provider_readiness import (
    summarize_embedding_provider_readiness,
)
from app.services.failure_case_review_queue import build_failure_case_workflow_review_queue
from app.services.ops_dashboard import render_ops_dashboard
from app.services.proof_gap_registry import (
    ACTION_SURFACE_BOUNDARY,
    build_current_proof_gap_registry,
    build_proof_gap_actions,
    get_proof_gap_action,
    proof_gap_action_surface_notes,
    proof_gap_registry_note,
)
from app.settings import Settings, get_settings

router = APIRouter(prefix="/ops", tags=["ops"])


@router.get("/summary", response_model=OpsSummaryOut)
def ops_summary(
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
) -> OpsSummaryOut:
    return _ops_summary_with_runtime_boundaries(repository, settings)


@router.get("/proof-gaps", response_model=ProofGapActionListOut)
def ops_proof_gaps() -> ProofGapActionListOut:
    gaps = build_proof_gap_actions()
    return ProofGapActionListOut(
        gaps=gaps,
        gap_count=len(gaps),
        surface_boundary=ACTION_SURFACE_BOUNDARY,
        notes=proof_gap_action_surface_notes(),
    )


@router.get("/proof-gaps/{gap_id}", response_model=ProofGapActionDetailOut)
def ops_proof_gap_detail(gap_id: str) -> ProofGapActionDetailOut:
    gap = get_proof_gap_action(gap_id)
    if gap is None:
        raise HTTPException(status_code=404, detail="proof gap not found")
    return ProofGapActionDetailOut(
        gap=gap,
        surface_boundary=ACTION_SURFACE_BOUNDARY,
        recommended_next_gate=gap.recommended_next_gate,
        gap_closure_allowed=False,
        notes=proof_gap_action_surface_notes(),
    )


@router.get("/dashboard", response_class=HTMLResponse)
def ops_dashboard(
    repository: Repository = Depends(get_repository),
    settings: Settings = Depends(get_settings),
) -> HTMLResponse:
    failure_cases = list(repository.list_failure_cases())
    workflow_runs = list(repository.list_workflow_runs())
    html = render_ops_dashboard(
        summary=_ops_summary_with_runtime_boundaries(repository, settings),
        agent_runs=list(repository.list_agent_runs()),
        failure_cases=failure_cases,
        workflow_runs=workflow_runs,
        retrieval_runs=list(repository.list_retrieval_runs()),
        evidence_ledger_entries=list(repository.list_evidence_ledger_entries()),
        noise_gate_records=list(repository.list_noise_gate_records()),
        report_records=list(repository.list_report_records()),
        failure_case_review_queue=build_failure_case_workflow_review_queue(
            workflow_runs=workflow_runs,
            failure_cases=failure_cases,
        ),
    )
    return HTMLResponse(content=html)


def _ops_summary_with_runtime_boundaries(
    repository: Repository,
    settings: Settings,
) -> OpsSummaryOut:
    summary = repository.ops_summary()
    notes = list(summary.notes)
    notes.append(proof_gap_registry_note())
    return summary.model_copy(
        update={
            "embedding_provider_readiness": summarize_embedding_provider_readiness(
                settings
            ),
            "proof_gap_registry": build_current_proof_gap_registry(),
            "notes": notes,
        }
    )
