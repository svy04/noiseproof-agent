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
        "embedding": [0.1, 0.2],
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
    assert connection.committed is True


def test_list_chunk_embeddings_filters_by_chunk_model_and_status():
    chunk_id = UUID("33333333-3333-3333-3333-333333333333")
    rows = [
        {"embedding_model": "local-test-model", "embedding_status": "created"},
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
    assert listed == rows
