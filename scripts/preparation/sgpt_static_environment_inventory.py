#!/usr/bin/env python3
"""AST-only import inventory for upstream/sgpt. No imports of project modules. No network."""
from __future__ import annotations

import ast
import csv
import hashlib
import json
import sys
from pathlib import Path

STDLIB = {
    "abc", "argparse", "ast", "asyncio", "base64", "builtins", "collections",
    "concurrent", "contextlib", "copy", "csv", "dataclasses", "datetime",
    "decimal", "enum", "functools", "gc", "glob", "gzip", "hashlib", "heapq",
    "io", "itertools", "json", "logging", "math", "multiprocessing", "os",
    "pathlib", "pickle", "platform", "pprint", "queue", "random", "re",
    "shutil", "signal", "socket", "sqlite3", "statistics", "string",
    "subprocess", "sys", "tempfile", "textwrap", "threading", "time",
    "traceback", "typing", "unittest", "urllib", "uuid", "warnings", "weakref",
    "xml", "zipfile",
}

LOCAL_TOP = {"scripts", "utils"}


def classify(top: str, root: Path, file: Path) -> str:
    if top in STDLIB or top.startswith("_"):
        return "stdlib"
    if top in LOCAL_TOP:
        return "local"
    # local relative package files
    if (root / top).exists() or (file.parent / f"{top}.py").exists():
        return "local"
    return "third_party"


def walk_imports(tree: ast.AST, file: Path, root: Path) -> list[dict]:
    rows: list[dict] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                top = name.split(".")[0]
                rows.append({
                    "file": str(file.relative_to(root.parent.parent) if False else file),
                    "rel_file": str(file.relative_to(root)),
                    "lineno": node.lineno,
                    "kind": "import",
                    "module": name,
                    "symbol": None,
                    "asname": alias.asname,
                    "top_level": top,
                    "category": classify(top, root, file),
                    "conditional": False,
                })
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            top = (mod.split(".")[0] if mod else ".")
            if node.level and not mod:
                category = "local"
                top = "."
            else:
                category = classify(top, root, file) if mod else "local"
            for alias in node.names:
                rows.append({
                    "file": str(file),
                    "rel_file": str(file.relative_to(root)),
                    "lineno": node.lineno,
                    "kind": "import_from",
                    "module": mod,
                    "symbol": alias.name,
                    "asname": alias.asname,
                    "top_level": top,
                    "category": category,
                    "conditional": False,
                })
    # mark imports inside If/Try as conditional (second pass)
    conditional_lines = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.If, ast.Try, ast.ExceptHandler)):
            for sub in ast.walk(node):
                if isinstance(sub, (ast.Import, ast.ImportFrom)):
                    conditional_lines.add(sub.lineno)
    for r in rows:
        if r["lineno"] in conditional_lines:
            r["conditional"] = True
    return rows


def main() -> int:
    repo = Path(__file__).resolve().parents[2]
    root = repo / "upstream" / "sgpt"
    out_dir = repo / "logs" / "environment-definition-sgpt"
    out_dir.mkdir(parents=True, exist_ok=True)

    all_rows: list[dict] = []
    files = sorted(root.rglob("*.py"))
    for f in files:
        if ".git" in f.parts:
            continue
        src = f.read_text(encoding="utf-8", errors="replace")
        try:
            tree = ast.parse(src, filename=str(f))
        except SyntaxError as e:
            all_rows.append({
                "rel_file": str(f.relative_to(root)),
                "lineno": getattr(e, "lineno", None),
                "kind": "parse_error",
                "module": None,
                "symbol": str(e),
                "asname": None,
                "top_level": None,
                "category": "error",
                "conditional": False,
            })
            continue
        all_rows.extend(walk_imports(tree, f, root))

    # normalize paths relative
    for r in all_rows:
        r.pop("file", None)

    third = sorted({r["top_level"] for r in all_rows if r.get("category") == "third_party" and r.get("top_level")})
    local = sorted({r["top_level"] for r in all_rows if r.get("category") == "local" and r.get("top_level")})
    std = sorted({r["top_level"] for r in all_rows if r.get("category") == "stdlib" and r.get("top_level")})

    payload = {
        "method_id": "sgpt",
        "upstream_root": "upstream/sgpt",
        "python_files_scanned": len(files),
        "import_rows": len(all_rows),
        "third_party_top_levels": third,
        "local_top_levels": local,
        "stdlib_top_levels": std,
        "sha256_of_csv_body": None,
        "rows": all_rows,
        "notes": [
            "AST-only; modules were not imported",
            "No network access",
            "Conditional flag marks imports nested under If/Try",
        ],
    }

    csv_path = out_dir / "import_inventory.csv"
    fields = ["rel_file", "lineno", "kind", "module", "symbol", "asname", "top_level", "category", "conditional"]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in all_rows:
            w.writerow({k: r.get(k) for k in fields})

    csv_bytes = csv_path.read_bytes()
    payload["sha256_of_csv_body"] = hashlib.sha256(csv_bytes).hexdigest()

    json_path = out_dir / "import_inventory.json"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"files={len(files)} rows={len(all_rows)}")
    print(f"third_party={third}")
    print(f"wrote {csv_path}")
    print(f"wrote {json_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
