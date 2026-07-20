#!/usr/bin/env python3
"""Lab harness: sparql_llm CORE_OFFLINE micro-smoke (not an adapter).

Local-only checks: import, version, SPARQL parse, VoID file schema load,
schema validation positive/negative. No LLM, endpoints, Qdrant, or embeddings.
"""

from __future__ import annotations

import argparse
import json
import os
import socket
import sys
from datetime import datetime, timezone
from typing import Any


def _install_network_guard() -> list[str]:
    """Fail closed on unexpected TCP connections during smoke.

    Primary isolation is Docker ``--network none``. This guard blocks
    ``socket.create_connection`` only. Do not assign to ``socket.socket.connect``
    (may be immutable / nonexistent as a type attribute on some runtimes).
    """
    attempts: list[str] = []

    def guarded_create_connection(address, *args, **kwargs):  # type: ignore[no-untyped-def]
        host = address[0] if isinstance(address, tuple) else address
        msg = f"network_attempt:{host}"
        attempts.append(msg)
        raise RuntimeError(f"CORE_OFFLINE smoke blocked unexpected network: {address}")

    socket.create_connection = guarded_create_connection  # type: ignore[assignment]
    return attempts


def main() -> int:
    parser = argparse.ArgumentParser(description="sparql_llm CORE_OFFLINE smoke harness")
    parser.add_argument("--void-file", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")

    network_attempts = _install_network_guard()
    result: dict[str, Any] = {
        "method_id": "sparql_llm",
        "scope": "CORE_OFFLINE",
        "package_version": None,
        "import_success": False,
        "version_ok": False,
        "valid_sparql_parse_success": False,
        "void_file": args.void_file,
        "void_classes_count": 0,
        "selected_class": None,
        "selected_predicate": None,
        "schema_valid_query_issue_count": None,
        "invalid_predicate_issue_count": None,
        "network_attempt_detected": False,
        "mandatory_checks_passed": False,
        "errors": [],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
    }

    try:
        import sparql_llm
        from sparql_llm import (
            SparqlExamplesLoader,
            SparqlVoidShapesLoader,
            validate_sparql,
            validate_sparql_with_void,
        )
        from sparql_llm.utils import get_prefix_converter, get_schema_for_endpoint

        _ = SparqlExamplesLoader, SparqlVoidShapesLoader
        result["import_success"] = True
        result["package_version"] = getattr(sparql_llm, "__version__", None)
        result["version_ok"] = result["package_version"] == "0.1.4"
        if not result["version_ok"]:
            result["errors"].append(f"version_mismatch:{result['package_version']}")
    except Exception as exc:  # noqa: BLE001
        result["errors"].append(f"import_failed:{exc}")
        _write(args.output, result, network_attempts)
        return 1

    try:
        parse_out = validate_sparql(
            "SELECT ?s WHERE { ?s ?p ?o } LIMIT 1",
            endpoint_url=None,
        )
        issues = parse_out.get("issues") or parse_out.get("errors") or []
        # QueryValidationOutput may use different keys; treat missing as ok if no exception
        if isinstance(parse_out, dict):
            issue_like = []
            for key in ("issues", "errors", "validation_errors", "messages"):
                val = parse_out.get(key)
                if isinstance(val, (list, set, tuple)):
                    issue_like.extend(list(val))
                elif isinstance(val, str) and val:
                    issue_like.append(val)
            # Also inspect nested common shapes
            if "fixed_query" in parse_out or "original_query" in parse_out:
                result["valid_sparql_parse_success"] = True
            else:
                result["valid_sparql_parse_success"] = len(issue_like) == 0
        else:
            result["valid_sparql_parse_success"] = True
        if not result["valid_sparql_parse_success"]:
            result["errors"].append(f"parse_issues:{issues}")
    except Exception as exc:  # noqa: BLE001
        result["errors"].append(f"parse_failed:{exc}")
        _write(args.output, result, network_attempts)
        return 1

    fake_endpoint = "urn:text2sparql-lab:fake-endpoint"
    try:
        schema = get_schema_for_endpoint(fake_endpoint, void_file=args.void_file)
        if not isinstance(schema, dict) or not schema:
            result["errors"].append("void_schema_empty_or_not_dict")
            _write(args.output, result, network_attempts)
            return 1
        result["void_classes_count"] = len(schema)
        selected_class = None
        selected_predicate = None
        for cls_iri, preds in schema.items():
            if isinstance(preds, dict) and preds:
                selected_class = cls_iri
                selected_predicate = next(iter(preds.keys()))
                break
        if not selected_class or not selected_predicate:
            result["errors"].append("no_class_with_predicate_in_void")
            _write(args.output, result, network_attempts)
            return 1
        result["selected_class"] = selected_class
        result["selected_predicate"] = selected_predicate
    except Exception as exc:  # noqa: BLE001
        result["errors"].append(f"void_load_failed:{exc}")
        _write(args.output, result, network_attempts)
        return 1

    prefix_converter = get_prefix_converter({})
    endpoints_void = {fake_endpoint: schema}

    valid_q = (
        "SELECT ?s ?o WHERE {\n"
        f"  ?s a <{selected_class}> .\n"
        f"  ?s <{selected_predicate}> ?o .\n"
        "}"
    )
    invalid_q = (
        "SELECT ?s ?o WHERE {\n"
        f"  ?s a <{selected_class}> .\n"
        "  ?s <urn:text2sparql-lab:invalid-predicate> ?o .\n"
        "}"
    )

    try:
        valid_issues = validate_sparql_with_void(
            valid_q,
            endpoint_url=fake_endpoint,
            prefix_converter=prefix_converter,
            endpoints_void_dict=endpoints_void,
        )
        invalid_issues = validate_sparql_with_void(
            invalid_q,
            endpoint_url=fake_endpoint,
            prefix_converter=prefix_converter,
            endpoints_void_dict=endpoints_void,
        )
        result["schema_valid_query_issue_count"] = len(valid_issues)
        result["invalid_predicate_issue_count"] = len(invalid_issues)
        if len(valid_issues) != 0:
            result["errors"].append(f"valid_query_unexpected_issues:{sorted(valid_issues)}")
        if len(invalid_issues) < 1:
            result["errors"].append("invalid_predicate_not_detected")
    except Exception as exc:  # noqa: BLE001
        result["errors"].append(f"schema_validate_failed:{exc}")
        _write(args.output, result, network_attempts)
        return 1

    result["network_attempt_detected"] = len(network_attempts) > 0
    if result["network_attempt_detected"]:
        result["errors"].append(f"network_attempts:{network_attempts}")

    result["mandatory_checks_passed"] = all(
        [
            result["import_success"],
            result["version_ok"],
            result["valid_sparql_parse_success"],
            result["void_classes_count"] > 0,
            result["schema_valid_query_issue_count"] == 0,
            result["invalid_predicate_issue_count"] is not None
            and result["invalid_predicate_issue_count"] >= 1,
            not result["network_attempt_detected"],
            len(result["errors"]) == 0,
        ]
    )
    _write(args.output, result, network_attempts)
    return 0 if result["mandatory_checks_passed"] else 2


def _write(path: str, result: dict[str, Any], network_attempts: list[str]) -> None:
    result["network_attempts_detail"] = network_attempts
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


if __name__ == "__main__":
    sys.exit(main())
