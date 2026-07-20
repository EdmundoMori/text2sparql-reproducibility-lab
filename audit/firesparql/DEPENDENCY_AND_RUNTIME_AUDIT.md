# DEPENDENCY_AND_RUNTIME_AUDIT — firesparql

**Fecha:** 2026-07-20  
**Matriz:** `DEPENDENCY_MATRIX.csv`

---

## Definición de entorno

| Artefacto | Estado | Evidencia |
|---|---|---|
| `requirements.txt` | **NOT_FOUND** | find |
| `environment.yml` | **NOT_FOUND** | find |
| `Dockerfile` | **NOT_FOUND** | find |
| README Requirements | “Coming soon…” | `README_REPORTED` |

Deps **inferidas solo por imports** (`CODE_VERIFIED` AST/imports). Pins: **UNKNOWN**.

---

## Secretos / servicios

| Variable / servicio | Staging | Evidencia |
|---|---|---|
| `OPENAI_API_KEY` | cleaning gpt-4o | `CODE_VERIFIED` |
| `GROQ_API_KEY` | RAG context | `CODE_VERIFIED` |
| Hugging Face Hub | bases + opcional ft checkpoint + MiniLM/BGE | `EXTERNAL_ARTIFACT_REFERENCED` |
| Endpoint ORKG/QLever | ejecución | `CODE_NOT_FOUND` + results |

---

## Host lab (contexto, no medido en esta pasada)

Perfil típico lab: RTX 4050 **6 GiB**, WSL (`MACHINE_PROFILE` lab). Implicaciones:

- 8B fp16 paper-like: **blocked** sin quant (quant ≠ paper).  
- 3B: **conditional** (VRAM tight + download + LICENSE).  
- RAG/cleaning: bloqueados por APIs.

---

## Paths runtime

Hardcoded `xueli_data/...` y absolutos macOS; `merge_models/` ausente. Cualquier smoke futuro requiere **path fixes** documentados como no-nativos si se parchea.

Esta pasada: **sin** `pip install`, **sin** imports pesados, **sin** downloads.
