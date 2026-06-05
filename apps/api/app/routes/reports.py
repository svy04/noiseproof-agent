from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from uuid import UUID, uuid4

from app.db import Repository, get_repository
from app.schemas import ReportPreviewOut, ReportPreviewRequest, ReportStoredRecordOut
from app.services.report_markdown import render_report_record_markdown
from app.services.report_preview import preview_report
from app.services.run_trace import run_with_trace

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("", response_model=ReportStoredRecordOut, status_code=201)
def create_report_record(
    payload: ReportPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ReportStoredRecordOut:
    workflow_trace_id = uuid4()

    def operation(agent_run_id) -> ReportStoredRecordOut:
        preview = preview_report(payload)
        persisted = repository.create_report_record(
            preview,
            evidence_entry_count=len(payload.evidence_entries),
            draft_claim_count=len(payload.draft_claims),
            workflow_trace_id=workflow_trace_id,
            agent_run_id=agent_run_id,
        )
        return ReportStoredRecordOut(**persisted)

    return run_with_trace(
        repository,
        endpoint="POST /reports",
        user_question=payload.question,
        trace_json={
            "evidence_entry_count": len(payload.evidence_entries),
            "workflow_trace_id": str(workflow_trace_id),
        },
        operation=operation,
        trace_from_result=lambda result: {
            "report_status": result.status,
            "gate_decision": result.gate.decision,
            "claim_count": result.claim_count,
            "evidence_entry_count": result.evidence_entry_count,
            "draft_claim_count": result.draft_claim_count,
        },
    )


@router.get("", response_model=list[ReportStoredRecordOut])
def list_report_records(
    workflow_trace_id: UUID | None = None,
    status: str | None = None,
    repository: Repository = Depends(get_repository),
) -> list[ReportStoredRecordOut]:
    return [
        ReportStoredRecordOut(**record)
        for record in repository.list_report_records(
            workflow_trace_id=workflow_trace_id,
            status=status,
        )
    ]


@router.post("/preview", response_model=ReportPreviewOut)
def create_report_preview(
    payload: ReportPreviewRequest,
    repository: Repository = Depends(get_repository),
) -> ReportPreviewOut:
    return run_with_trace(
        repository,
        endpoint="POST /reports/preview",
        user_question=payload.question,
        trace_json={"evidence_entry_count": len(payload.evidence_entries)},
        operation=lambda _agent_run_id: preview_report(payload),
        trace_from_result=lambda result: {
            "report_status": result.status,
            "gate_decision": result.gate.decision,
            "claim_count": len(result.report.claims) if result.report is not None else 0,
        },
    )


@router.get("/{report_record_id}/markdown", response_class=PlainTextResponse)
def export_report_record_markdown(
    report_record_id: UUID,
    repository: Repository = Depends(get_repository),
) -> PlainTextResponse:
    record = repository.get_report_record(report_record_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Report record not found")
    return PlainTextResponse(
        render_report_record_markdown(record),
        media_type="text/markdown",
    )
