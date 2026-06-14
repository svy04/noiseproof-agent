from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping
import hashlib


ROOT_DIR = Path(__file__).resolve().parents[3]
PHASE_MARKER = "opt_in_ocr_adapter_runtime_smoke_v0"
FIXTURE_PACKET_MARKER = "opt_in_ocr_adapter_runtime_smoke_fixture_v0"
DISCOVERY_PHASE_MARKER = "opt-in OCR adapter owner-runtime input discovery v0"
RUN_SOURCE = "owner_runtime_pymupdf_ocr_smoke"
FIXTURE_ROOT_TEXT = "examples/pdf-extraction-quality/ocr-runtime-fixtures"
PACKET_FILENAME = "ocr-runtime-provenance.json"
REQUIRED_OPT_IN_OCR_FIXTURE_IDS = ["ocr_smoke_text_image_pdf"]


def load_opt_in_ocr_fixture_provenance(path: Path | str) -> dict[str, Any]:
    root = Path(path)
    payload = json.loads((root / PACKET_FILENAME).read_text(encoding="utf-8"))
    _validate_fixture_packet(root, payload)
    return payload


def owner_runtime_smoke_packet() -> dict[str, object]:
    return {
        "phase_marker": PHASE_MARKER,
        "packet_status": "ready_for_owner_runtime_input",
        "fixture_root": FIXTURE_ROOT_TEXT,
        "fixture_ids": REQUIRED_OPT_IN_OCR_FIXTURE_IDS,
        "required_runtime_env": {
            "NOISEPROOF_ENABLE_PYMUPDF_OCR": "true",
            "NOISEPROOF_TESSDATA_PREFIX": "owner-provided-tessdata-path",
            "CI": "false",
        },
        "manual_workflow": [
            "Provide a local tessdata directory outside the repository.",
            "Set NOISEPROOF_ENABLE_PYMUPDF_OCR=true outside CI.",
            "Run the OCR smoke and write the metadata report outside the repository.",
            "Validate the metadata report before using it as owner-runtime evidence.",
        ],
        "source_basis": [
            "PyMuPDF Page.get_textpage_ocr invokes Tesseract-OCR and accepts a tessdata folder.",
            "The committed fixture is synthetic and image-only so OCR evidence remains explicit.",
        ],
        "api_calls_attempted": False,
        "ocr_calls_attempted": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "non_claims": _non_claims(ocr_evidence=False),
        "boundary": _boundary_notes(owner_runtime_succeeded=False),
    }


def discover_owner_runtime_input(env: Mapping[str, str]) -> dict[str, object]:
    tessdata_value = (env.get("NOISEPROOF_TESSDATA_PREFIX") or env.get("TESSDATA_PREFIX") or "").strip()
    tessdata_prefix_present = bool(tessdata_value)
    tessdata_prefix_exists = Path(tessdata_value).is_dir() if tessdata_prefix_present else False
    opt_in_enabled = _env_flag_enabled(env.get("NOISEPROOF_ENABLE_PYMUPDF_OCR"))
    ci_runtime = _env_flag_enabled(env.get("CI"))

    if not tessdata_prefix_present:
        status = "missing_tessdata_prefix"
        next_action = (
            "configure NOISEPROOF_TESSDATA_PREFIX outside the repository and set "
            "NOISEPROOF_ENABLE_PYMUPDF_OCR=true for owner-runtime OCR smoke only"
        )
    elif not tessdata_prefix_exists:
        status = "tessdata_prefix_not_found"
        next_action = "point NOISEPROOF_TESSDATA_PREFIX to an existing local tessdata directory"
    elif ci_runtime:
        status = "blocked_by_ci"
        next_action = "rerun outside CI for owner-runtime OCR smoke only"
    elif not opt_in_enabled:
        status = "opt_in_disabled"
        next_action = "set NOISEPROOF_ENABLE_PYMUPDF_OCR=true for owner-runtime OCR smoke only"
    else:
        status = "ready_for_owner_runtime_smoke"
        next_action = "run the OCR smoke and write the metadata-only report outside the repository"

    return {
        "phase_marker": DISCOVERY_PHASE_MARKER,
        "owner_runtime_input_status": status,
        "discoverable_input_sources": ["environment"],
        "opt_in_enabled": opt_in_enabled,
        "ci_runtime": ci_runtime,
        "tessdata_prefix_present": tessdata_prefix_present,
        "tessdata_prefix_exists": tessdata_prefix_exists,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "ocr_calls_attempted": False,
        "api_calls_attempted": False,
        "next_action": next_action,
        "non_claims": _non_claims(ocr_evidence=False),
    }


def run_owner_runtime_smoke(
    *,
    output_path: Path,
    env: Mapping[str, str],
    ocr_adapter: object | None = None,
    fixture_root: Path | str = ROOT_DIR / FIXTURE_ROOT_TEXT,
    language: str = "eng",
) -> dict[str, object]:
    if _path_is_inside_repository(output_path):
        return {
            "phase_marker": PHASE_MARKER,
            "run_status": "output_path_rejected",
            "output_path_boundary": {
                "output_path_allowed": False,
                "required_location": "outside_repository",
            },
            "ocr_calls_attempted": False,
            "tessdata_path_printed": False,
            "tessdata_path_committed_to_repo": False,
            "non_claims": _non_claims(ocr_evidence=False),
        }

    readiness = discover_owner_runtime_input(env)
    if readiness["owner_runtime_input_status"] != "ready_for_owner_runtime_smoke":
        return {
            "phase_marker": PHASE_MARKER,
            "run_status": "input_not_ready",
            "owner_runtime_input_status": readiness["owner_runtime_input_status"],
            "next_action": readiness["next_action"],
            "ocr_calls_attempted": False,
            "tessdata_path_printed": False,
            "tessdata_path_committed_to_repo": False,
            "non_claims": _non_claims(ocr_evidence=False),
        }

    root = Path(fixture_root)
    packet = load_opt_in_ocr_fixture_provenance(root)
    fixture = packet["fixtures"][0]
    content = (root / fixture["path"]).read_bytes()
    tessdata = str(env.get("NOISEPROOF_TESSDATA_PREFIX") or env.get("TESSDATA_PREFIX") or "")
    adapter = ocr_adapter if ocr_adapter is not None else PyMuPdfOcrAdapter()
    result = adapter.extract_text_from_pdf(
        content=content,
        tessdata=tessdata,
        language=language,
    )
    text = str(result.get("text", ""))
    expected_spans = [str(span) for span in fixture.get("expected_spans", [])]
    report = {
        "phase_marker": PHASE_MARKER,
        "run_source": RUN_SOURCE,
        "run_status": "report_written",
        "fixture_root": FIXTURE_ROOT_TEXT,
        "fixture_id": fixture["fixture_id"],
        "fixture_sha256": fixture["sha256"],
        "fixture_size_bytes": fixture["size_bytes"],
        "ocr_engine": str(result.get("engine") or "pymupdf_get_textpage_ocr"),
        "language": language,
        "page_count": _positive_int(result.get("page_count")),
        "ocr_page_count": _positive_int(result.get("ocr_page_count")),
        "ocr_performed": True,
        "ocr_calls_attempted": True,
        "recognized_text": text.strip(),
        "expected_spans": expected_spans,
        "expected_spans_found": _expected_spans_found(text, expected_spans),
        "tessdata_prefix_present": True,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
        "claim_boundary": "owner_runtime_ocr_smoke_only_not_robust_pdf_extraction",
        "non_claims": _non_claims(ocr_evidence=True),
        "boundary": _boundary_notes(owner_runtime_succeeded=True),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report


def validate_owner_runtime_smoke_report(
    report: Mapping[str, object],
    *,
    report_path: Path | None = None,
) -> dict[str, object]:
    missing_or_failed_checks: list[str] = []
    report_path_allowed = (
        report_path is None or not _path_is_inside_repository(report_path)
    )
    if not report_path_allowed:
        missing_or_failed_checks.append("report path must be outside repository")

    expected_values = {
        "phase_marker": PHASE_MARKER,
        "run_source": RUN_SOURCE,
        "fixture_root": FIXTURE_ROOT_TEXT,
        "fixture_id": "ocr_smoke_text_image_pdf",
        "ocr_performed": True,
        "ocr_calls_attempted": True,
        "expected_spans_found": True,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "robust_pdf_extraction_claimed": False,
        "can_claim_robust_pdf_extraction": False,
    }
    for field, expected in expected_values.items():
        if report.get(field) != expected:
            missing_or_failed_checks.append(f"{field} must be {_format_expected(expected)}")
    if not str(report.get("recognized_text") or "").strip():
        missing_or_failed_checks.append("recognized_text must be non-empty")

    accepted = not missing_or_failed_checks
    return {
        "phase_marker": "opt-in OCR adapter owner-runtime smoke validator v0",
        "validation_status": "accepted" if accepted else "rejected",
        "accepted_owner_runtime_smoke": accepted,
        "missing_or_failed_checks": missing_or_failed_checks,
        "report_path_boundary": {
            "report_path_allowed": report_path_allowed,
            "required_location": "outside_repository",
        },
        "ocr_calls_attempted": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "non_claims": {
            **_non_claims(ocr_evidence=False),
            "validator_performs_ocr": False,
        },
    }


class PyMuPdfOcrAdapter:
    def extract_text_from_pdf(
        self,
        *,
        content: bytes,
        tessdata: str,
        language: str,
    ) -> dict[str, object]:
        import pymupdf

        document = pymupdf.open(stream=content, filetype="pdf")
        try:
            page_text: list[str] = []
            for page in document:
                textpage = page.get_textpage_ocr(
                    language=language,
                    dpi=200,
                    full=True,
                    tessdata=tessdata,
                )
                page_text.append(page.get_text(textpage=textpage).strip())
            return {
                "text": "\n".join(text for text in page_text if text),
                "engine": "pymupdf_get_textpage_ocr",
                "page_count": document.page_count,
                "ocr_page_count": document.page_count,
            }
        finally:
            document.close()


def _validate_fixture_packet(root: Path, payload: dict[str, Any]) -> None:
    if payload.get("packet") != FIXTURE_PACKET_MARKER:
        raise ValueError("Unexpected opt-in OCR fixture packet.")
    if payload.get("binary_pdf_fixtures_included") is not True:
        raise ValueError("Opt-in OCR fixture packet must include a binary PDF.")
    if payload.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError("Opt-in OCR fixture packet must not claim robust PDF extraction.")
    if payload.get("ocr_claim_requires_owner_runtime") is not True:
        raise ValueError("Opt-in OCR fixture packet must require owner runtime OCR.")
    fixtures = payload.get("fixtures")
    if not isinstance(fixtures, list):
        raise ValueError("Opt-in OCR fixture entries must be a list.")
    if [item.get("fixture_id") for item in fixtures] != REQUIRED_OPT_IN_OCR_FIXTURE_IDS:
        raise ValueError("Opt-in OCR fixture packet has wrong fixture order.")
    for fixture in fixtures:
        _validate_fixture_entry(root, fixture)
    for note in [
        "not robust PDF extraction evidence",
        "not OCR evidence until owner-runtime smoke succeeds",
    ]:
        if note not in payload.get("boundary_notes", []):
            raise ValueError(f"Opt-in OCR fixture packet missing boundary note: {note}")


def _validate_fixture_entry(root: Path, item: Any) -> None:
    if not isinstance(item, dict):
        raise ValueError("Opt-in OCR fixture entries must be objects.")
    fixture_id = str(item.get("fixture_id") or "")
    relative_path = Path(str(item.get("path") or ""))
    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ValueError(f"Fixture {fixture_id} has unsafe path.")
    content = (root / relative_path).read_bytes()
    if hashlib.sha256(content).hexdigest() != item.get("sha256"):
        raise ValueError(f"Fixture {fixture_id} sha256 mismatch.")
    if len(content) != item.get("size_bytes"):
        raise ValueError(f"Fixture {fixture_id} size_bytes mismatch.")
    if item.get("expected_digital_text") is not False:
        raise ValueError(f"Fixture {fixture_id} must be image-only for OCR smoke.")
    if item.get("robust_pdf_extraction_claimed") is not False:
        raise ValueError(f"Fixture {fixture_id} must not claim robust PDF extraction.")


def _boundary_notes(*, owner_runtime_succeeded: bool) -> list[str]:
    notes = [
        "not robust PDF extraction evidence",
        "not image/chart interpretation evidence",
        "not layout fidelity evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]
    if not owner_runtime_succeeded:
        notes.insert(1, "not OCR evidence until owner-runtime smoke succeeds")
    else:
        notes.insert(1, "owner-runtime OCR smoke over one synthetic fixture only")
    return notes


def _non_claims(*, ocr_evidence: bool) -> dict[str, bool]:
    return {
        "robust_pdf_extraction": False,
        "ocr_evidence": ocr_evidence,
        "image_chart_interpretation": False,
        "layout_fidelity": False,
        "hosted_deployment": False,
        "external_reviewer_feedback": False,
        "product_complete": False,
    }


def _path_is_inside_repository(path: Path) -> bool:
    try:
        path.resolve().relative_to(ROOT_DIR)
    except ValueError:
        return False
    return True


def _env_flag_enabled(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "on"}


def _expected_spans_found(text: str, expected_spans: list[str]) -> bool:
    normalized = _normalize_text(text)
    return all(_normalize_text(span) in normalized for span in expected_spans)


def _normalize_text(value: object) -> str:
    return " ".join(str(value).lower().split())


def _positive_int(value: Any) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int) and value > 0:
        return value
    return 1


def _format_expected(value: object) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)
