#!/usr/bin/env python3
"""Lab-only minimal VoID → documents → optional Qdrant index for SPARQL-LLM.

NOT an adapter, NOT a paper reproduction, NOT a SIB benchmark index.
Label: LAB_MINIMAL_INDEX

Modes:
  prepare-documents  — parse local void TTL offline; emit ≤12 docs
  build-index        — require exact offline embedding cache; write Qdrant path
  verify-index       — inspect collection metadata offline

Network: blocked (fail closed). No LLM. No homepage. No UniProt label queries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import sys
import time
from pathlib import Path
from typing import Any


DOC_TYPE = "SPARQL endpoints classes schema"
SOURCE_SCOPE = "LAB_MINIMAL_INDEX"
DEFAULT_MAX_DOCS = 12
DEFAULT_MODEL = "intfloat/multilingual-e5-large"


def _block_network() -> None:
    """Fail closed on any outbound TCP/UDP."""

    def _deny(*_a: Any, **_k: Any) -> None:
        raise RuntimeError("NETWORK_BLOCKED: outbound sockets disabled by lab preparation script")

    socket.socket.connect = _deny  # type: ignore[method-assign]
    socket.socket.connect_ex = _deny  # type: ignore[method-assign]
    try:
        import httpx

        _orig = httpx.Client.request

        def _httpx_deny(self: Any, *a: Any, **k: Any) -> Any:
            raise RuntimeError("NETWORK_BLOCKED: httpx disabled by lab preparation script")

        httpx.Client.request = _httpx_deny  # type: ignore[method-assign]
        httpx.AsyncClient.request = _httpx_deny  # type: ignore[method-assign]
    except Exception:
        pass


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _compress_iri(iri: str) -> str:
    return f"<{iri}>"


def _shex_for_class(cls: str, predicates: dict[str, list[str]]) -> str:
    subj = _compress_iri(cls)
    shape_iri = f"shape:{cls.replace(':', '_').replace('/', '_').replace('#', '_')}"
    lines = [f"{shape_iri} {{", f"  a [ {subj} ] ;"]
    for pred, objs in sorted(predicates.items()):
        p = _compress_iri(pred)
        if objs:
            joined = " ".join(_compress_iri(o) for o in sorted(objs))
            lines.append(f"  {p} [ {joined} ] ;")
        else:
            lines.append(f"  {p} IRI ;")
    # strip trailing semicolon style like upstream
    body = "\n".join(lines)
    body = body.rstrip(" ;\n") + "\n}"
    return body


def prepare_documents(
    void_file: Path,
    endpoint_url: str,
    max_documents: int,
    output_dir: Path,
) -> dict[str, Any]:
    _block_network()
    # Import after network block; do not import agent.main / indexing
    from sparql_llm.utils import get_schema_for_endpoint

    void_sha = _sha256_file(void_file)
    schema = get_schema_for_endpoint(endpoint_url, str(void_file))
    if not schema:
        raise RuntimeError("No VoID classes parsed from local void file")

    # Deterministic: sort classes by IRI
    class_iris = sorted(schema.keys())
    docs: list[dict[str, Any]] = []
    for cls in class_iris:
        if len(docs) >= max_documents:
            break
        shex = _shex_for_class(cls, schema[cls])
        payload = {
            "question": cls,
            "answer": shex,
            "endpoint_url": endpoint_url,
            "iri": cls,
            "doc_type": DOC_TYPE,
            "source_scope": SOURCE_SCOPE,
        }
        # retrieval embeds page_content ≈ question
        docs.append({"page_content": cls, "payload": payload})

    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = output_dir / "minimal-documents.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps(d, ensure_ascii=False, sort_keys=True) + "\n")

    docs_bytes = jsonl_path.read_bytes()
    manifest = {
        "label": SOURCE_SCOPE,
        "void_file": str(void_file),
        "void_sha256": void_sha,
        "endpoint_url": endpoint_url,
        "document_count": len(docs),
        "max_documents": max_documents,
        "doc_type": DOC_TYPE,
        "class_iris": [d["payload"]["iri"] for d in docs],
        "jsonl_sha256": _sha256_bytes(docs_bytes),
        "network": "blocked",
        "labels_queried": False,
        "homepage_used": False,
        "not_paper_index": True,
        "evidence": "CODE_VERIFIED_get_schema_for_endpoint_use_file;INFERENCE_lab_shex_without_remote_labels",
    }
    man_path = output_dir / "minimal-documents-manifest.json"
    man_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def _assert_exact_model_cache(cache_dir: Path, model: str) -> None:
    if model != DEFAULT_MODEL:
        raise RuntimeError(f"Refusing non-exact model: {model}")
    if not cache_dir.exists():
        raise RuntimeError(f"Embedding cache absent: {cache_dir}")
    # Heuristic presence checks — must still load offline
    markers = list(cache_dir.rglob("*"))
    if not markers:
        raise RuntimeError("Embedding cache directory empty")


def build_index(
    documents_jsonl: Path,
    qdrant_path: Path,
    collection: str,
    embedding_model: str,
    embedding_cache: Path,
) -> dict[str, Any]:
    _block_network()
    if embedding_model != DEFAULT_MODEL:
        raise RuntimeError("Only intfloat/multilingual-e5-large allowed")
    _assert_exact_model_cache(embedding_cache, embedding_model)

    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    # Common fastembed/hf cache envs
    os.environ.setdefault("FASTEMBED_CACHE_PATH", str(embedding_cache))
    os.environ.setdefault("HF_HOME", str(embedding_cache))

    docs: list[dict[str, Any]] = []
    with documents_jsonl.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                docs.append(json.loads(line))
    if not docs:
        raise RuntimeError("No documents to index")

    from fastembed import TextEmbedding
    from qdrant_client import QdrantClient
    from qdrant_client.http.models import Distance, VectorParams
    from qdrant_client import models as qdrant_models

    t0 = time.time()
    # local_files_only if supported — fail if download attempted
    try:
        model = TextEmbedding(embedding_model, cache_dir=str(embedding_cache))
    except TypeError:
        model = TextEmbedding(embedding_model)

    texts = [d["page_content"] for d in docs]
    embeddings = list(model.embed(texts))
    if not embeddings:
        raise RuntimeError("No embeddings produced")
    dim = len(embeddings[0])

    qdrant_path.mkdir(parents=True, exist_ok=True)
    client = QdrantClient(path=str(qdrant_path))
    if client.collection_exists(collection):
        client.delete_collection(collection)
    client.create_collection(
        collection_name=collection,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
    client.upsert(
        collection_name=collection,
        points=qdrant_models.Batch(
            ids=list(range(1, len(docs) + 1)),
            vectors=[list(e) for e in embeddings],
            payloads=[d["payload"] for d in docs],
        ),
    )
    info = client.get_collection(collection)
    elapsed = time.time() - t0
    result = {
        "status": "INDEX_VERIFIED_PENDING_VERIFY_MODE",
        "collection": collection,
        "points_count": info.points_count,
        "vector_size": dim,
        "distance": "Cosine",
        "embedding_model": embedding_model,
        "documents_jsonl": str(documents_jsonl),
        "qdrant_path": str(qdrant_path),
        "elapsed_seconds": elapsed,
        "label": SOURCE_SCOPE,
        "network": "blocked",
    }
    return result


def verify_index(qdrant_path: Path, collection: str, documents_jsonl: Path | None) -> dict[str, Any]:
    _block_network()
    from qdrant_client import QdrantClient

    client = QdrantClient(path=str(qdrant_path))
    if not client.collection_exists(collection):
        raise RuntimeError(f"Collection missing: {collection}")
    info = client.get_collection(collection)
    points, _ = client.scroll(collection_name=collection, limit=100, with_payload=True, with_vectors=False)
    iris = []
    doc_types = set()
    scopes = set()
    for p in points:
        payload = p.payload or {}
        iris.append(payload.get("iri"))
        doc_types.add(payload.get("doc_type"))
        scopes.add(payload.get("source_scope"))
    expected = None
    if documents_jsonl and documents_jsonl.exists():
        expected = sum(1 for line in documents_jsonl.read_text().splitlines() if line.strip())
    ok = (
        info.points_count is not None
        and info.points_count > 0
        and (expected is None or info.points_count == expected)
        and len(iris) == len(set(iris))
        and DOC_TYPE in doc_types
        and SOURCE_SCOPE in scopes
    )
    return {
        "status": "INDEX_VERIFIED" if ok else "INDEX_VERIFY_FAILED",
        "points_count": info.points_count,
        "unique_iris": len(set(iris)),
        "doc_types": sorted(x for x in doc_types if x),
        "source_scopes": sorted(x for x in scopes if x),
        "expected_from_jsonl": expected,
        "vector_size": getattr(getattr(info.config, "params", None), "vectors", None),
        "ok": ok,
    }


def main() -> int:
    p = argparse.ArgumentParser(description="LAB_MINIMAL_INDEX preparation for SPARQL-LLM")
    p.add_argument("--mode", required=True, choices=["prepare-documents", "build-index", "verify-index"])
    p.add_argument("--void-file", type=Path, default=None)
    p.add_argument("--endpoint-url", default="https://sparql.uniprot.org/sparql/")
    p.add_argument("--qdrant-path", type=Path, default=None)
    p.add_argument("--collection", default="lab_minimal_uniprot_void")
    p.add_argument("--embedding-model", default=DEFAULT_MODEL)
    p.add_argument("--embedding-cache", type=Path, default=None)
    p.add_argument("--max-documents", type=int, default=DEFAULT_MAX_DOCS)
    p.add_argument("--documents-jsonl", type=Path, default=None)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    result_path = args.output / f"{args.mode}-result.json"

    try:
        if args.mode == "prepare-documents":
            if not args.void_file:
                raise SystemExit("--void-file required")
            manifest = prepare_documents(args.void_file, args.endpoint_url, args.max_documents, args.output)
            result_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"ok": True, "document_count": manifest["document_count"]}, sort_keys=True))
            return 0
        if args.mode == "build-index":
            if not args.documents_jsonl or not args.qdrant_path or not args.embedding_cache:
                raise SystemExit("--documents-jsonl --qdrant-path --embedding-cache required")
            res = build_index(
                args.documents_jsonl,
                args.qdrant_path,
                args.collection,
                args.embedding_model,
                args.embedding_cache,
            )
            result_path.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
            print(json.dumps({"ok": True, **{k: res[k] for k in ("points_count", "vector_size")}}, sort_keys=True))
            return 0
        if args.mode == "verify-index":
            if not args.qdrant_path:
                raise SystemExit("--qdrant-path required")
            res = verify_index(args.qdrant_path, args.collection, args.documents_jsonl)
            result_path.write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
            print(json.dumps(res, sort_keys=True))
            return 0 if res.get("ok") else 2
    except Exception as e:
        err = {"ok": False, "error": str(e), "mode": args.mode}
        result_path.write_text(json.dumps(err, indent=2, sort_keys=True) + "\n")
        print(json.dumps(err, sort_keys=True), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
