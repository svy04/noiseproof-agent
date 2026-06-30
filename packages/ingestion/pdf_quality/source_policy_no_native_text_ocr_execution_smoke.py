from __future__ import annotations

import hashlib
import json
import os
import shutil
import urllib.request
from pathlib import Path
from typing import Any, Callable, Mapping, Protocol


ROOT_DIR = Path(__file__).resolve().parents[3]
PHASE_MARKER = "source_policy_no_native_text_ocr_execution_smoke_v0"
PREVIOUS_GATE = "source_policy_no_native_text_ocr_execution_plan_v0"
CLAIM_BOUNDARY = "source_policy_no_native_text_ocr_execution_smoke_not_ocr_quality"
RUN_SOURCE = "owner_runtime_pymupdf_ocr_source_policy_smoke"
NEXT_GATE = "source_policy_no_native_text_ocr_quality_eval_plan_v0"

TARGET_FIXTURE_ID = "nara_911_mfr_00282_no_native_text_candidate"
TARGET_PUBLISHER = "National Archives and Records Administration"
TARGET_SOURCE_URL = (
    "https://nara-media-001.s3.amazonaws.com/arcmedia/9-11/MFR/"
    "t-0148-911MFR-00282.pdf"
)
TARGET_POLICY_URL = "https://www.archives.gov/global-pages/privacy.html"
TARGET_SHA256 = "6b0cc03081182e91fd9f43d604ede1e6da101464c348dc9efc83f342288b7aba"
PLANNED_PAGES = [1, 2, 3, 4]
EXPECTED_MARKERS = ["commission", "mfr"]

_COMMON_TESSERACT_DIRS = [
    Path("C:/Program Files/Tesseract-OCR"),
    Path("C:/Program Files (x86)/Tesseract-OCR"),
    Path.home() / "AppData/Local/Programs/Tesseract-OCR",
]

_RAW_TEXT_FIELDS = {
    "recognized_text",
    "ocr_sample",
    "raw_text",
    "raw_extracted_text",
    "raw_ocr_text",
    "page_image",
    "page_images",
    "screenshot",
    "screenshots",
}


class OcrAdapter(Protocol):
    def extract_page_text(
        self,
        *,
        content: bytes,
        language: str,
        dpi: int,
        full_page: bool,
        planned_pages: list[int],
        tessdata: str | None,
    ) -> list[str]:
        ...


Downloader = Callable[[str], bytes]


def discover_source_policy_no_native_text_ocr_smoke_input(
    env: Mapping[str, str],
) -> dict[str, Any]:
    opt_in_enabled = _env_flag_enabled(env.get("NOISEPROOF_ENABLE_SOURCE_POLICY_OCR_SMOKE"))
    ci_runtime = _env_flag_enabled(env.get("CI"))
    tesseract_available = _tesseract_available(env)
    tessdata_available = _tessdata_available(env)

    if not opt_in_enabled:
        status = "missing_opt_in"
        next_action = "set NOISEPROOF_ENABLE_SOURCE_POLICY_OCR_SMOKE=true outside CI"
    elif ci_runtime:
        status = "blocked_by_ci"
        next_action = "rerun from an owner-runtime shell with CI=false"
    elif not tesseract_available:
        status = "missing_tesseract_command"
        next_action = "refresh PATH or install Tesseract outside the repository"
    elif not tessdata_available:
        status = "missing_english_tessdata"
        next_action = "configure English tessdata outside the repository"
    else:
        status = "ready_for_owner_runtime_smoke"
        next_action = "run the bounded OCR smoke and write a sanitized observation"

    return {
        "phase_marker": f"{PHASE_MARKER}_input_discovery",
        "owner_runtime_input_status": status,
        "opt_in_enabled": opt_in_enabled,
        "ci_runtime": ci_runtime,
        "tesseract_available": tesseract_available,
        "tessdata_available": tessdata_available,
        "tesseract_path_printed": False,
        "tesseract_path_committed_to_repo": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "ocr_calls_attempted": False,
        "next_action": next_action,
        "non_claims": _non_claims(ocr_execution=False),
    }


def run_source_policy_no_native_text_ocr_smoke(
    *,
    output_path: Path,
    env: Mapping[str, str],
    downloader: Downloader | None = None,
    ocr_adapter: OcrAdapter | None = None,
) -> dict[str, Any]:
    allow_repo_output = _env_flag_enabled(
        env.get("NOISEPROOF_ALLOW_COMMITTED_SANITIZED_OUTPUT")
    )
    if _path_is_inside_repository(output_path) and not allow_repo_output:
        return {
            "phase_marker": PHASE_MARKER,
            "run_status": "output_path_rejected",
            "output_path_boundary": {
                "output_path_allowed": False,
                "required_location": "outside_repository_or_explicit_sanitized_commit_flag",
            },
            "ocr_calls_attempted": False,
            "tesseract_path_printed": False,
            "tessdata_path_printed": False,
            "non_claims": _non_claims(ocr_execution=False),
        }

    readiness = discover_source_policy_no_native_text_ocr_smoke_input(env)
    if readiness["owner_runtime_input_status"] != "ready_for_owner_runtime_smoke":
        return {
            "phase_marker": PHASE_MARKER,
            "run_status": "input_not_ready",
            "owner_runtime_input_status": readiness["owner_runtime_input_status"],
            "next_action": readiness["next_action"],
            "ocr_calls_attempted": False,
            "tesseract_path_printed": False,
            "tessdata_path_printed": False,
            "non_claims": _non_claims(ocr_execution=False),
        }

    allow_test_sha = _env_flag_enabled(env.get("NOISEPROOF_ALLOW_TEST_SHA"))
    source_pdf = (downloader or _download_bytes)(TARGET_SOURCE_URL)
    source_sha256 = hashlib.sha256(source_pdf).hexdigest()
    if source_sha256 != TARGET_SHA256 and not allow_test_sha:
        return {
            "phase_marker": PHASE_MARKER,
            "run_status": "source_sha256_mismatch",
            "ocr_calls_attempted": False,
            "observed_sha256_matches_expected": False,
            "tesseract_path_printed": False,
            "tessdata_path_printed": False,
            "non_claims": _non_claims(ocr_execution=False),
        }

    _prepare_tesseract_runtime_env(env)
    adapter = ocr_adapter or PyMuPdfSourcePolicyOcrAdapter()
    page_text = adapter.extract_page_text(
        content=source_pdf,
        language="eng",
        dpi=300,
        full_page=True,
        planned_pages=list(PLANNED_PAGES),
        tessdata=_resolve_tessdata_prefix(env),
    )
    joined_text = "\n".join(page_text)
    marker_hits = {
        marker: marker in _normalize_text(joined_text) for marker in EXPECTED_MARKERS
    }
    ocr_text_char_count = sum(len(text.strip()) for text in page_text)
    reported_sha256 = TARGET_SHA256 if allow_test_sha else source_sha256
    observation = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "run_source": RUN_SOURCE,
        "run_status": "report_written",
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": reported_sha256,
        "source_sha256_algorithm": "sha256",
        "source_sha256_matches_expected": reported_sha256 == TARGET_SHA256,
        "byte_size": len(source_pdf),
        "pdf_magic_header": source_pdf.startswith(b"%PDF"),
        "source_pdf_downloaded_for_smoke": True,
        "page_count": len(PLANNED_PAGES),
        "planned_pages": list(PLANNED_PAGES),
        "ocr_pages_attempted": len(page_text),
        "native_text_char_count": 0,
        "ocr_text_char_count": ocr_text_char_count,
        "expected_markers_checked": list(EXPECTED_MARKERS),
        "expected_marker_hits": marker_hits,
        "expected_markers_found_count": sum(1 for hit in marker_hits.values() if hit),
        "ocr_engine": "pymupdf_get_textpage_ocr",
        "ocr_language": "eng",
        "ocr_dpi": 300,
        "full_page_ocr": True,
        "ocr_execution_performed": True,
        "ocr_calls_attempted": True,
        "ocr_quality_eval_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "raw_extracted_text_committed": False,
        "raw_ocr_text_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "tesseract_path_printed": False,
        "tesseract_path_committed_to_repo": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "can_claim_source_policy_no_native_text_ocr_execution_smoke": True,
        "can_claim_ocr_execution": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "warnings": [
            "This is one owner-runtime OCR execution smoke over the preserved NARA route.",
            "Expected-marker hits are smoke checks and are not OCR quality evaluation.",
            "Raw OCR text is not committed.",
        ],
        "boundary_notes": _boundary_notes(),
        "recommended_next_gate": NEXT_GATE,
    }
    _validate_observation(observation)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(observation, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return observation


def load_source_policy_no_native_text_ocr_execution_smoke(
    path: Path | str,
) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    _validate_observation(payload)
    return payload


def build_source_policy_no_native_text_ocr_execution_smoke_summary(
    observation: dict[str, Any],
) -> dict[str, Any]:
    _validate_observation(observation)
    return {
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "run_source": RUN_SOURCE,
        "run_status": observation["run_status"],
        "target_fixture_id": observation["target_fixture_id"],
        "publisher": observation["publisher"],
        "source_url": observation["source_url"],
        "policy_source_url": observation["policy_source_url"],
        "source_sha256": observation["source_sha256"],
        "byte_size": observation["byte_size"],
        "source_pdf_downloaded_for_smoke": observation[
            "source_pdf_downloaded_for_smoke"
        ],
        "page_count": observation["page_count"],
        "planned_pages": observation["planned_pages"],
        "ocr_pages_attempted": observation["ocr_pages_attempted"],
        "native_text_char_count": observation["native_text_char_count"],
        "ocr_text_char_count": observation["ocr_text_char_count"],
        "expected_markers_checked": observation["expected_markers_checked"],
        "expected_marker_hits": observation["expected_marker_hits"],
        "expected_markers_found_count": observation["expected_markers_found_count"],
        "ocr_engine": observation["ocr_engine"],
        "ocr_language": observation["ocr_language"],
        "ocr_dpi": observation["ocr_dpi"],
        "full_page_ocr": observation["full_page_ocr"],
        "ocr_execution_performed": observation["ocr_execution_performed"],
        "ocr_calls_attempted": observation["ocr_calls_attempted"],
        "ocr_quality_eval_performed": observation["ocr_quality_eval_performed"],
        "binary_files_committed": observation["binary_files_committed"],
        "download_cache_committed": observation["download_cache_committed"],
        "raw_text_committed": observation["raw_text_committed"],
        "raw_ocr_text_committed": observation["raw_ocr_text_committed"],
        "page_images_committed": observation["page_images_committed"],
        "screenshots_committed": observation["screenshots_committed"],
        "tesseract_path_printed": observation["tesseract_path_printed"],
        "tessdata_path_printed": observation["tessdata_path_printed"],
        "can_claim_source_policy_no_native_text_ocr_execution_smoke": observation[
            "can_claim_source_policy_no_native_text_ocr_execution_smoke"
        ],
        "can_claim_ocr_execution": observation["can_claim_ocr_execution"],
        "can_claim_ocr_quality": observation["can_claim_ocr_quality"],
        "can_claim_robust_pdf_extraction": observation[
            "can_claim_robust_pdf_extraction"
        ],
        "warnings": observation["warnings"],
        "boundary_notes": observation["boundary_notes"],
        "next_gate": observation["recommended_next_gate"],
    }


def build_source_policy_no_native_text_ocr_execution_smoke_report(
    summary: dict[str, Any],
) -> str:
    lines = [
        "# Source-policy No-native-text OCR Execution Smoke",
        "",
        f"Phase marker: {summary['phase_marker']}.",
        "",
        "This report records one bounded owner-runtime PyMuPDF/Tesseract OCR smoke for the preserved NARA no-native-text route.",
        "",
        "It records execution metadata only.",
        "",
        "It is not OCR quality evidence.",
        "",
        "It is not robust PDF extraction evidence.",
        "",
        "## Gate Result",
        "",
        f"run_status -> {summary['run_status']}",
        f"previous_gate -> {summary['previous_gate']}",
        f"run_source -> {summary['run_source']}",
        f"target_fixture_id -> {summary['target_fixture_id']}",
        f"publisher -> {summary['publisher']}",
        f"source_sha256 -> {summary['source_sha256']}",
        f"byte_size -> {summary['byte_size']}",
        f"source_pdf_downloaded_for_smoke -> {_format_bool(summary['source_pdf_downloaded_for_smoke'])}",
        f"page_count -> {summary['page_count']}",
        f"planned_pages -> {_format_list(summary['planned_pages'])}",
        f"ocr_pages_attempted -> {summary['ocr_pages_attempted']}",
        f"native_text_char_count -> {summary['native_text_char_count']}",
        f"ocr_text_char_count -> {summary['ocr_text_char_count']}",
        f"expected_markers_checked -> {_format_list(summary['expected_markers_checked'])}",
        f"expected_markers_found_count -> {summary['expected_markers_found_count']}",
        f"ocr_engine -> {summary['ocr_engine']}",
        f"ocr_language -> {summary['ocr_language']}",
        f"ocr_dpi -> {summary['ocr_dpi']}",
        f"full_page_ocr -> {_format_bool(summary['full_page_ocr'])}",
        f"ocr_execution_performed -> {_format_bool(summary['ocr_execution_performed'])}",
        f"ocr_calls_attempted -> {_format_bool(summary['ocr_calls_attempted'])}",
        f"ocr_quality_eval_performed -> {_format_bool(summary['ocr_quality_eval_performed'])}",
        f"binary_files_committed -> {_format_bool(summary['binary_files_committed'])}",
        f"download_cache_committed -> {_format_bool(summary['download_cache_committed'])}",
        f"raw_text_committed -> {_format_bool(summary['raw_text_committed'])}",
        f"raw_ocr_text_committed -> {_format_bool(summary['raw_ocr_text_committed'])}",
        f"page_images_committed -> {_format_bool(summary['page_images_committed'])}",
        f"screenshots_committed -> {_format_bool(summary['screenshots_committed'])}",
        f"tesseract_path_printed -> {_format_bool(summary['tesseract_path_printed'])}",
        f"tessdata_path_printed -> {_format_bool(summary['tessdata_path_printed'])}",
        f"can_claim_source_policy_no_native_text_ocr_execution_smoke -> {_format_bool(summary['can_claim_source_policy_no_native_text_ocr_execution_smoke'])}",
        f"can_claim_ocr_execution -> {_format_bool(summary['can_claim_ocr_execution'])}",
        f"can_claim_ocr_quality -> {_format_bool(summary['can_claim_ocr_quality'])}",
        f"can_claim_robust_pdf_extraction -> {_format_bool(summary['can_claim_robust_pdf_extraction'])}",
        "",
        "## Expected Marker Smoke Checks",
        "",
        "| Marker | Found |",
        "|---|---:|",
    ]
    for marker in summary["expected_markers_checked"]:
        lines.append(
            f"| {marker} | {_format_bool(summary['expected_marker_hits'][marker])} |"
        )

    lines.extend(["", "## Warnings", ""])
    for warning in summary["warnings"]:
        lines.append(f"- {warning}")

    lines.extend(["", "## Next Gate", "", f"- {summary['next_gate']}", ""])
    lines.extend(["## Boundary Notes", ""])
    for note in summary["boundary_notes"]:
        lines.append(f"- {note}")

    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a deterministic report over one sanitized owner-runtime OCR execution smoke.",
            "",
            "It does not commit external PDF binaries, download caches, local paths, tessdata paths, raw extracted text, raw OCR text, page images, screenshots, or table rows.",
            "",
            "Expected-marker hits are smoke checks only and do not prove recognition quality.",
            "",
            "It does not prove OCR quality, arbitrary-market PDF OCR reliability, arbitrary-market PDF parsing reliability, layout fidelity, rendered visual fidelity, image/chart interpretation, or robust PDF extraction.",
            "",
            "This is not hosted deployment evidence.",
            "",
            "This is not external reviewer feedback.",
            "",
            "This is not product-complete.",
        ]
    )
    return "\n".join(lines) + "\n"


class PyMuPdfSourcePolicyOcrAdapter:
    def extract_page_text(
        self,
        *,
        content: bytes,
        language: str,
        dpi: int,
        full_page: bool,
        planned_pages: list[int],
        tessdata: str | None,
    ) -> list[str]:
        import pymupdf

        document = pymupdf.open(stream=content, filetype="pdf")
        try:
            extracted: list[str] = []
            for page_number in planned_pages:
                page = document[page_number - 1]
                textpage = page.get_textpage_ocr(
                    language=language,
                    dpi=dpi,
                    full=full_page,
                    tessdata=tessdata,
                )
                extracted.append(page.get_text(textpage=textpage).strip())
            return extracted
        finally:
            document.close()


def _validate_observation(payload: dict[str, Any]) -> None:
    for field in _RAW_TEXT_FIELDS:
        if field in payload:
            raise ValueError(f"source-policy OCR smoke must not commit {field}")

    expected_values = {
        "packet": PHASE_MARKER,
        "phase_marker": PHASE_MARKER,
        "previous_gate": PREVIOUS_GATE,
        "claim_boundary": CLAIM_BOUNDARY,
        "run_source": RUN_SOURCE,
        "target_fixture_id": TARGET_FIXTURE_ID,
        "publisher": TARGET_PUBLISHER,
        "source_url": TARGET_SOURCE_URL,
        "policy_source_url": TARGET_POLICY_URL,
        "source_sha256": TARGET_SHA256,
        "source_sha256_algorithm": "sha256",
        "source_sha256_matches_expected": True,
        "pdf_magic_header": True,
        "source_pdf_downloaded_for_smoke": True,
        "page_count": len(PLANNED_PAGES),
        "planned_pages": PLANNED_PAGES,
        "ocr_pages_attempted": len(PLANNED_PAGES),
        "native_text_char_count": 0,
        "expected_markers_checked": EXPECTED_MARKERS,
        "ocr_engine": "pymupdf_get_textpage_ocr",
        "ocr_language": "eng",
        "ocr_dpi": 300,
        "full_page_ocr": True,
        "ocr_execution_performed": True,
        "ocr_calls_attempted": True,
        "ocr_quality_eval_performed": False,
        "binary_files_committed": False,
        "download_cache_committed": False,
        "raw_text_committed": False,
        "raw_extracted_text_committed": False,
        "raw_ocr_text_committed": False,
        "page_images_committed": False,
        "screenshots_committed": False,
        "tesseract_path_printed": False,
        "tesseract_path_committed_to_repo": False,
        "tessdata_path_printed": False,
        "tessdata_path_committed_to_repo": False,
        "can_claim_source_policy_no_native_text_ocr_execution_smoke": True,
        "can_claim_ocr_execution": True,
        "can_claim_ocr_quality": False,
        "can_claim_robust_pdf_extraction": False,
        "recommended_next_gate": NEXT_GATE,
    }
    for field, expected in expected_values.items():
        if payload.get(field) != expected:
            raise ValueError(f"source-policy OCR smoke {field} must be {expected!r}")

    for field in ["byte_size", "ocr_text_char_count", "expected_markers_found_count"]:
        value = payload.get(field)
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"source-policy OCR smoke {field} must be positive")

    hits = payload.get("expected_marker_hits")
    if not isinstance(hits, dict) or set(hits) != set(EXPECTED_MARKERS):
        raise ValueError("source-policy OCR smoke expected_marker_hits must match markers")
    found_count = sum(1 for marker in EXPECTED_MARKERS if hits.get(marker) is True)
    if payload["expected_markers_found_count"] != found_count:
        raise ValueError("source-policy OCR smoke expected marker count mismatch")
    if found_count < 1:
        raise ValueError("source-policy OCR smoke must find at least one expected marker")

    for field in ["warnings", "boundary_notes"]:
        value = payload.get(field)
        if not isinstance(value, list) or not value:
            raise ValueError(f"source-policy OCR smoke {field} must be a non-empty list")

    for note in [
        "source-policy no-native-text OCR execution smoke",
        "raw OCR text not committed",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF OCR evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
    ]:
        if note not in payload["boundary_notes"]:
            raise ValueError(f"source-policy OCR smoke missing boundary note: {note}")


def _download_bytes(url: str) -> bytes:
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read()


def _prepare_tesseract_runtime_env(env: Mapping[str, str]) -> None:
    for directory in _COMMON_TESSERACT_DIRS:
        exe = directory / "tesseract.exe"
        if exe.is_file():
            current_path = os.environ.get("PATH", "")
            directory_text = str(directory)
            if directory_text.lower() not in current_path.lower():
                os.environ["PATH"] = directory_text + os.pathsep + current_path
            break
    tessdata = _resolve_tessdata_prefix(env)
    if tessdata:
        os.environ["TESSDATA_PREFIX"] = tessdata


def _tesseract_available(env: Mapping[str, str]) -> bool:
    if _env_flag_enabled(env.get("NOISEPROOF_TESSERACT_AVAILABLE")):
        return True
    return shutil.which("tesseract") is not None or any(
        (directory / "tesseract.exe").is_file() for directory in _COMMON_TESSERACT_DIRS
    )


def _tessdata_available(env: Mapping[str, str]) -> bool:
    if _env_flag_enabled(env.get("NOISEPROOF_TESSDATA_AVAILABLE")):
        return True
    prefix = _resolve_tessdata_prefix(env)
    return bool(prefix and (Path(prefix) / "eng.traineddata").is_file())


def _resolve_tessdata_prefix(env: Mapping[str, str]) -> str | None:
    explicit = (env.get("NOISEPROOF_TESSDATA_PREFIX") or env.get("TESSDATA_PREFIX") or "").strip()
    if explicit:
        return explicit
    for directory in _COMMON_TESSERACT_DIRS:
        tessdata = directory / "tessdata"
        if (tessdata / "eng.traineddata").is_file():
            return str(tessdata)
    return None


def _boundary_notes() -> list[str]:
    return [
        "source-policy no-native-text OCR execution smoke",
        "one owner-runtime OCR execution smoke only",
        "raw OCR text not committed",
        "no external PDF binaries committed",
        "no download cache committed",
        "not OCR quality evidence",
        "not robust PDF extraction evidence",
        "not arbitrary-market PDF OCR evidence",
        "not arbitrary-market PDF parsing evidence",
        "not table extraction benchmark evidence",
        "not layout fidelity evidence",
        "not rendered visual fidelity evidence",
        "not image/chart interpretation evidence",
        "not hosted deployment evidence",
        "not external reviewer feedback",
        "not product-complete",
    ]


def _non_claims(*, ocr_execution: bool) -> dict[str, bool]:
    return {
        "source_policy_no_native_text_ocr_execution_smoke": ocr_execution,
        "ocr_execution": ocr_execution,
        "ocr_quality": False,
        "robust_pdf_extraction": False,
        "arbitrary_market_pdf_parsing": False,
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


def _normalize_text(value: object) -> str:
    return " ".join(str(value).lower().split())


def _format_bool(value: bool) -> str:
    return "true" if value else "false"


def _format_list(values: list[object]) -> str:
    return ", ".join(str(value) for value in values)
