#!/usr/bin/env python3
"""Lab-only FastAPI import preflight for SPARQL-LLM LOCAL_CHAT_API.

Runs ONLY when LAB_MINIMAL_INDEX is INDEX_VERIFIED.
Does NOT POST /chat. Does NOT call LLM. Does NOT call MCP tools.
Does NOT hit SPARQL endpoints. Network should be blocked by caller (--network none).
"""

from __future__ import annotations

import json
import os
import socket
import sys
import time
from pathlib import Path
from typing import Any


def _block_network() -> None:
    def _deny(*_a: Any, **_k: Any) -> None:
        raise RuntimeError("NETWORK_BLOCKED: outbound sockets disabled by lab preflight")

    socket.socket.connect = _deny  # type: ignore[method-assign]
    socket.socket.connect_ex = _deny  # type: ignore[method-assign]
    try:
        _orig_cc = socket.create_connection

        def _deny_cc(*_a: Any, **_k: Any) -> None:
            raise RuntimeError("NETWORK_BLOCKED: create_connection disabled by lab preflight")

        socket.create_connection = _deny_cc  # type: ignore[assignment]
    except Exception:
        pass


def main() -> int:
    out = Path(os.environ.get("PREFLIGHT_OUTPUT", "/data/output/preflight-result.json"))
    out.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    report: dict[str, Any] = {
        "ok": False,
        "post_chat": False,
        "mcp_invoked": False,
        "llm_loaded": False,
        "routes": [],
        "required_routes_present": {},
        "openapi_get": None,
        "import_seconds": None,
        "error": None,
    }
    try:
        _block_network()
        for k in (
            "OPENROUTER_API_KEY",
            "OPENAI_API_KEY",
            "LANGFUSE_SECRET_KEY",
            "LANGFUSE_PUBLIC_KEY",
            "LANGFUSE_HOST",
        ):
            os.environ.pop(k, None)

        if not os.environ.get("SETTINGS_FILEPATH"):
            raise RuntimeError("SETTINGS_FILEPATH required")

        t_imp = time.time()
        from sparql_llm.agent.main import app  # noqa: WPS433

        report["import_seconds"] = time.time() - t_imp
        routes = sorted({getattr(r, "path", str(r)) for r in app.routes})
        report["routes"] = routes
        needed = ["/chat", "/mcp", "/openapi.json"]
        report["required_routes_present"] = {p: any(p == r or r.startswith(p) for r in routes) for p in needed}

        from fastapi.testclient import TestClient

        client = TestClient(app)
        resp = client.get("/openapi.json")
        report["openapi_get"] = {"status_code": resp.status_code, "ok": resp.status_code == 200}
        report["ok"] = (
            all(report["required_routes_present"].values())
            and report["openapi_get"]["ok"]
            and report["post_chat"] is False
        )
        report["elapsed_seconds"] = time.time() - t0
    except Exception as e:
        report["error"] = str(e)
        report["elapsed_seconds"] = time.time() - t0
        out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(json.dumps(report, sort_keys=True), file=sys.stderr)
        return 1

    out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"ok": report["ok"], "routes_n": len(report["routes"])}, sort_keys=True))
    return 0 if report["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
