from datetime import UTC, datetime
from uuid import UUID

from app import schemas
from app.db import PostgresRepository
from app.settings import Settings


class FakeCursor:
    def __init__(self, *, row=None, rows=None):
        self._row = row
        self._rows = rows or []

    def fetchone(self):
        return self._row

    def fetchall(self):
        return self._rows


class FakeConnection:
    def __init__(self, *, row=None, rows=None):
        self.calls = []
        self.committed = False
        self._row = row
        self._rows = rows or []

    def __enter__(self):
        return self

    def __exit__(self, *_exc):
        return False

    def execute(self, sql, params=None):
        self.calls.append((sql, params))
        return FakeCursor(row=self._row, rows=self._rows)

    def commit(self):
        self.committed = True


def test_create_uploaded_file_intake_manifest_inserts_manifest_metadata_only():
    created_at = datetime(2026, 6, 1, tzinfo=UTC)
    manifest_id = UUID("11111111-1111-1111-1111-111111111111")
    row = {
        "id": manifest_id,
        "content_sha256": "abc123",
        "filename": "sample.md",
        "source_type": "markdown",
        "content_type": "text/markdown",
        "size_bytes": 24,
        "parser": "markdown",
        "profile_json": {"extraction_quality": "high"},
        "storage_decision": "do_not_persist_raw_upload_yet",
        "replayable": False,
        "persistence_boundary": "manifest_only_no_raw_file_storage",
        "warnings_json": [],
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.UploadedFileIntakeManifestCreate(
        content_sha256="abc123",
        filename="sample.md",
        source_type="markdown",
        content_type="text/markdown",
        size_bytes=24,
        parser="markdown",
        profile_json={"extraction_quality": "high"},
    )

    created = repository.create_uploaded_file_intake_manifest(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO uploaded_file_intake_manifests" in sql
    assert "BYTEA" not in sql
    assert params[:6] == (
        "abc123",
        "sample.md",
        "markdown",
        "text/markdown",
        24,
        "markdown",
    )
    assert getattr(params[6], "obj", params[6]) == payload.profile_json
    assert created["id"] == manifest_id
    assert created["content_sha256"] == "abc123"
    assert connection.committed is True


def test_list_uploaded_file_intake_manifests_reads_recent_manifest_metadata():
    rows = [
        {"content_sha256": "new"},
        {"content_sha256": "old"},
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_uploaded_file_intake_manifests(limit=2)

    sql, params = connection.calls[0]
    assert "SELECT * FROM uploaded_file_intake_manifests" in sql
    assert "ORDER BY created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (2,)
    assert listed == rows


def test_create_document_chunk_inserts_chunk_text_without_embeddings():
    created_at = datetime(2026, 6, 2, tzinfo=UTC)
    document_id = UUID("22222222-2222-2222-2222-222222222222")
    chunk_id = UUID("33333333-3333-3333-3333-333333333333")
    row = {
        "id": chunk_id,
        "document_id": document_id,
        "source_type": "markdown",
        "source_uri": "upload://sample.md",
        "filename": "sample.md",
        "chunk_strategy": "heading-aware",
        "chunk_index": 0,
        "chunk_text": "Revenue increased in Q1.",
        "character_start": 0,
        "character_end": 24,
        "metadata_json": {"header_path": ["Revenue"]},
        "persistence_boundary": "chunk_text_only_no_raw_file_storage",
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.DocumentChunkCreate(
        document_id=document_id,
        source_type="markdown",
        source_uri="upload://sample.md",
        filename="sample.md",
        chunk_strategy="heading-aware",
        chunk_index=0,
        chunk_text="Revenue increased in Q1.",
        character_start=0,
        character_end=24,
        metadata_json={"header_path": ["Revenue"]},
    )

    created = repository.create_document_chunk(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO document_chunks" in sql
    assert "embedding" not in sql.lower()
    assert params[:8] == (
        document_id,
        "markdown",
        "upload://sample.md",
        "sample.md",
        "heading-aware",
        0,
        "Revenue increased in Q1.",
        0,
    )
    assert params[8] == 24
    assert getattr(params[9], "obj", params[9]) == {"header_path": ["Revenue"]}
    assert params[10] == "chunk_text_only_no_raw_file_storage"
    assert created["id"] == chunk_id
    assert created["document_id"] == document_id
    assert connection.committed is True


def test_list_document_chunks_reads_recent_chunks_for_document():
    document_id = UUID("22222222-2222-2222-2222-222222222222")
    rows = [
        {"chunk_index": 0, "chunk_text": "first"},
        {"chunk_index": 1, "chunk_text": "second"},
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_document_chunks(document_id=document_id, limit=2)

    sql, params = connection.calls[0]
    assert "SELECT * FROM document_chunks" in sql
    assert "WHERE document_id = %s" in sql
    assert "ORDER BY chunk_strategy ASC, chunk_index ASC, created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (document_id, 2)
    assert listed == rows


def test_create_chunk_embedding_inserts_caller_provided_vector_without_generation():
    created_at = datetime(2026, 6, 2, tzinfo=UTC)
    chunk_id = UUID("33333333-3333-3333-3333-333333333333")
    embedding_id = UUID("44444444-4444-4444-4444-444444444444")
    row = {
        "id": embedding_id,
        "chunk_id": chunk_id,
        "embedding_model": "local-test-model",
        "embedding_dimension": 2,
        "embedding_text_hash": "sha256:abc",
        "distance_metric": "cosine",
        "embedding_status": "created",
        "embedding": "[0.1,0.2]",
        "metadata_json": {"source": "unit-test"},
        "embedding_created_at": created_at,
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.ChunkEmbeddingCreate(
        chunk_id=chunk_id,
        embedding_model="local-test-model",
        embedding_dimension=2,
        embedding_text_hash="sha256:abc",
        distance_metric="cosine",
        embedding_status="created",
        embedding=[0.1, 0.2],
        metadata_json={"source": "unit-test"},
    )

    created = repository.create_chunk_embedding(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO chunk_embeddings" in sql
    assert "SentenceTransformer" not in sql
    assert "semantic" not in sql.lower()
    assert params[:6] == (
        chunk_id,
        "local-test-model",
        2,
        "sha256:abc",
        "cosine",
        "created",
    )
    assert params[6] == "[0.1,0.2]"
    assert getattr(params[7], "obj", params[7]) == {"source": "unit-test"}
    assert created["id"] == embedding_id
    assert created["embedding"] == [0.1, 0.2]
    assert connection.committed is True


def test_list_chunk_embeddings_filters_by_chunk_model_and_status():
    chunk_id = UUID("33333333-3333-3333-3333-333333333333")
    rows = [
        {
            "embedding_model": "local-test-model",
            "embedding_status": "created",
            "embedding": "[0.1,0.2]",
        },
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_chunk_embeddings(
        chunk_id=chunk_id,
        embedding_model="local-test-model",
        embedding_status="created",
        limit=2,
    )

    sql, params = connection.calls[0]
    assert "SELECT * FROM chunk_embeddings" in sql
    assert "chunk_id = %s" in sql
    assert "embedding_model = %s" in sql
    assert "embedding_status = %s" in sql
    assert "ORDER BY embedding_created_at DESC, created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (chunk_id, "local-test-model", "created", 2)
    assert listed[0]["embedding"] == [0.1, 0.2]


def test_preview_semantic_retrieval_candidates_uses_pgvector_exact_cosine_ranking():
    document_id = UUID("22222222-2222-2222-2222-222222222222")
    chunk_id = UUID("33333333-3333-3333-3333-333333333333")
    embedding_id = UUID("44444444-4444-4444-4444-444444444444")
    rows = [
        {
            "chunk_id": chunk_id,
            "embedding_id": embedding_id,
            "document_id": document_id,
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "chunk_metadata_json": {"header_path": ["Demand"]},
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "distance_metric": "cosine",
            "embedding_metadata_json": {"embedding_source": "caller_provided_vector"},
            "distance": 0.0,
        }
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    result = repository.preview_semantic_retrieval_candidates(
        document_id=document_id,
        query_embedding=[1.0, 0.0],
        embedding_model="local-test-model",
        embedding_dimension=2,
        limit=3,
    )

    sql, params = connection.calls[0]
    assert "document_chunks" in sql
    assert "chunk_embeddings" in sql
    assert "JOIN chunk_embeddings" in sql
    assert "<=> %s::vector" in sql
    assert "distance_metric = 'cosine'" in sql
    assert "embedding_status = 'created'" in sql
    assert "INSERT INTO retrieval_runs" not in sql
    assert params == ("[1.0,0.0]", document_id, "local-test-model", 2, 3)
    assert result[0]["chunk_id"] == chunk_id
    assert result[0]["embedding_id"] == embedding_id
    assert result[0]["distance"] == 0.0


def test_create_raw_file_scan_result_inserts_caller_provided_row_without_scanner():
    created_at = datetime(2026, 6, 3, tzinfo=UTC)
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    scan_result_id = UUID("66666666-6666-6666-6666-666666666666")
    row = {
        "id": scan_result_id,
        "raw_file_id": raw_file_id,
        "scanner_name": "manual-review-placeholder",
        "scanner_version": "0.0",
        "signature_db_version": None,
        "scan_started_at": None,
        "scan_finished_at": None,
        "scan_status": "failed",
        "scan_verdict": "scan_error",
        "matched_signature": None,
        "error_message": "scanner unavailable",
        "metadata_json": {"source": "unit-test"},
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.RawFileScanResultCreate(
        raw_file_id=raw_file_id,
        scanner_name="manual-review-placeholder",
        scanner_version="0.0",
        scan_status="failed",
        scan_verdict="scan_error",
        error_message="scanner unavailable",
        metadata_json={"source": "unit-test"},
    )

    created = repository.create_raw_file_scan_result(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO raw_file_scan_results" in sql
    assert "uploaded_raw_files" not in sql
    assert "raw_bytes" not in sql
    assert "clamscan" not in sql.lower()
    assert "clamav" not in sql.lower()
    assert params[:9] == (
        raw_file_id,
        "manual-review-placeholder",
        "0.0",
        None,
        None,
        None,
        "failed",
        "scan_error",
        None,
    )
    assert params[9] == "scanner unavailable"
    assert getattr(params[10], "obj", params[10]) == {"source": "unit-test"}
    assert created["id"] == scan_result_id
    assert created["scan_verdict"] == "scan_error"
    assert created["scan_verdict"] != "clean"
    assert connection.committed is True


def test_get_uploaded_raw_file_for_scan_reads_raw_bytes_for_internal_scanner_only():
    created_at = datetime(2026, 6, 3, tzinfo=UTC)
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    row = {
        "id": raw_file_id,
        "content_sha256": "abc123",
        "storage_key": "generated-storage-key",
        "filename": "../../sample.csv",
        "source_type": "csv",
        "content_type": "text/csv",
        "size_bytes": 25,
        "storage_backend": "postgres_bytea",
        "quarantine_status": "stored_quarantined",
        "persistence_boundary": "raw_upload_quarantine_db_bytea_no_download_endpoint",
        "raw_bytes": b"ticker,revenue\nALPHA,120\n",
        "warnings_json": [],
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    fetched = repository.get_uploaded_raw_file_for_scan(raw_file_id)

    sql, params = connection.calls[0]
    assert "FROM uploaded_raw_files" in sql
    assert "WHERE id = %s" in sql
    assert "raw_bytes" in sql
    assert "download_url" not in sql
    assert params == (raw_file_id,)
    assert fetched["id"] == raw_file_id
    assert fetched["raw_bytes"] == b"ticker,revenue\nALPHA,120\n"
    assert fetched["storage_key"] == "generated-storage-key"
    assert connection.committed is False


def test_list_raw_file_scan_results_filters_without_exposing_raw_bytes():
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    rows = [
        {
            "raw_file_id": raw_file_id,
            "scanner_name": "manual-review-placeholder",
            "scan_status": "failed",
            "scan_verdict": "scan_error",
        },
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_raw_file_scan_results(
        raw_file_id=raw_file_id,
        scan_status="failed",
        scan_verdict="scan_error",
        limit=2,
    )

    sql, params = connection.calls[0]
    assert "SELECT * FROM raw_file_scan_results" in sql
    assert "raw_file_id = %s" in sql
    assert "scan_status = %s" in sql
    assert "scan_verdict = %s" in sql
    assert "raw_bytes" not in sql
    assert "ORDER BY scan_started_at DESC NULLS LAST, created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (raw_file_id, "failed", "scan_error", 2)
    assert listed == rows


def test_raw_file_download_approval_create_defaults_preserve_local_boundaries():
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    latest_scan_result_id = UUID("66666666-6666-6666-6666-666666666666")
    expires_at = datetime(2026, 6, 4, tzinfo=UTC)

    payload = schemas.RawFileDownloadApprovalCreate(
        raw_file_id=raw_file_id,
        latest_scan_result_id=latest_scan_result_id,
        approval_reason="manual local review after latest clean scan",
        approved_by_label="local-operator",
        expires_at=expires_at,
    )

    assert payload.approval_status == "approved"
    assert payload.metadata_json == {}
    assert (
        payload.approval_boundary
        == "local_v0_manual_operator_approval_not_production_auth"
    )
    assert payload.identity_boundary == "operator_label_not_authenticated_identity"
    assert payload.approved_by_label == "local-operator"


def test_create_raw_file_download_approval_inserts_manual_row_without_authorization_enforcement():
    created_at = datetime(2026, 6, 4, tzinfo=UTC)
    expires_at = datetime(2026, 6, 5, tzinfo=UTC)
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    latest_scan_result_id = UUID("66666666-6666-6666-6666-666666666666")
    approval_id = UUID("77777777-7777-7777-7777-777777777777")
    row = {
        "id": approval_id,
        "raw_file_id": raw_file_id,
        "latest_scan_result_id": latest_scan_result_id,
        "approval_status": "approved",
        "approval_reason": "manual local review after latest clean scan",
        "approved_by_label": "local-operator",
        "expires_at": expires_at,
        "revoked_at": None,
        "metadata_json": {"source": "unit-test"},
        "approval_boundary": "local_v0_manual_operator_approval_not_production_auth",
        "identity_boundary": "operator_label_not_authenticated_identity",
        "created_at": created_at,
    }
    connection = FakeConnection(row=row)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    payload = schemas.RawFileDownloadApprovalCreate(
        raw_file_id=raw_file_id,
        latest_scan_result_id=latest_scan_result_id,
        approval_reason="manual local review after latest clean scan",
        approved_by_label="local-operator",
        expires_at=expires_at,
        metadata_json={"source": "unit-test"},
    )

    created = repository.create_raw_file_download_approval(payload)

    sql, params = connection.calls[0]
    assert "INSERT INTO raw_file_download_approvals" in sql
    assert "raw_file_download_events" not in sql
    assert "raw_bytes" not in sql
    assert "download_url" not in sql
    assert "jwt" not in sql.lower()
    assert params[:7] == (
        raw_file_id,
        latest_scan_result_id,
        "approved",
        "manual local review after latest clean scan",
        "local-operator",
        expires_at,
        None,
    )
    assert getattr(params[7], "obj", params[7]) == {"source": "unit-test"}
    assert params[8] == "local_v0_manual_operator_approval_not_production_auth"
    assert params[9] == "operator_label_not_authenticated_identity"
    assert created["id"] == approval_id
    assert created["approved_by_label"] == "local-operator"
    assert connection.committed is True


def test_list_raw_file_download_approvals_filters_without_allowing_downloads():
    raw_file_id = UUID("55555555-5555-5555-5555-555555555555")
    rows = [
        {
            "raw_file_id": raw_file_id,
            "approval_status": "approved",
            "approved_by_label": "local-operator",
        },
    ]
    connection = FakeConnection(rows=rows)
    repository = PostgresRepository(Settings())
    repository._connect = lambda: connection

    listed = repository.list_raw_file_download_approvals(
        raw_file_id=raw_file_id,
        approval_status="approved",
        limit=2,
    )

    sql, params = connection.calls[0]
    assert "SELECT * FROM raw_file_download_approvals" in sql
    assert "raw_file_id = %s" in sql
    assert "approval_status = %s" in sql
    assert "raw_bytes" not in sql
    assert "download_url" not in sql
    assert "ORDER BY created_at DESC, id DESC" in sql
    assert "LIMIT %s" in sql
    assert params == (raw_file_id, "approved", 2)
    assert listed == rows
