# Deviations — sparql_llm CORE_OFFLINE run 20260719T112306Z

## What was NOT done (by design)

- No paper evaluation / benchmarks.
- No LLM / OpenRouter / OpenAI.
- No SPARQL endpoint calls.
- No RAG / agent / MCP.
- No Virtuoso / Text2SPARQL stack.
- No scientific metrics.
- Goal was CODE_VERIFIED CORE_OFFLINE install+local validate only.

## Operational deviations

1. **venv location:** Intended `workdir/runs/sparql_llm/<RUN_ID>/.venv` became **read-only** under Cursor sandbox (`Errno 30` on `site-packages`). Install completed in `/tmp/sparql_llm_5a_venv` with the same Python 3.10.12. Documented in `environment.txt`.
2. **Harness not executed:** Import of installed package failed before functional checks; `scripts/smoke/sparql_llm_core_offline.py` was created but not run.
3. **onnxruntime sample `.onnx` files** appear under the venv site-packages (package data). These are **not** Hugging Face model weight downloads for the smoke; no HF cache weights were created for this run.

## Root cause of failure

`sparql_llm` @ `3748730e` imports `Required` from `typing` (`config.py:9`). That symbol exists in the stdlib only from **Python 3.11+**. Host has **3.10.12** and no `python3.11`. `pyproject.toml` claims `requires-python = ">=3.10"`, which is inconsistent with the import.

No packaging patches or PYTHONPATH fallbacks were applied (per Prompt 5A restrictions).
