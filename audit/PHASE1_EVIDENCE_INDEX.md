# PHASE1_EVIDENCE_INDEX — Prompt 15

**Fecha:** 2026-07-22 · Distingue Git / local pesado / externo / ausente

## Convenciones

| Marca | Significado |
|---|---|
| GIT | versionado en el lab |
| LOCAL | workdir/caches locales (gitignore) |
| EXT | recurso externo (HF, API, Zenodo) |
| ABSENT | no encontrado |
| HIST | histórico / superseded |

---

## sparql_llm

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Paper/code | STATIC_AUDIT, mapping | GIT |
| Commit | `3748730e…` | GIT lock |
| Licencia | MIT | GIT |
| Datos/métricas | audits + readiness API | GIT |
| Entorno | environments/sparql_llm + Docker py311 | GIT |
| Ejecución | CORE_OFFLINE 5A/5B reports | GIT |
| Online | ECONOMIC_NO_GO | GIT |
| Pesos | n/a (API/local models opcionales) | EXT/ABSENT |
| Estado final | smoke_only; nac=true | GIT Prompt 15 |

## mkgqagent

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Static | STATIC_AUDIT | GIT |
| Commit | `ba0f2f78…` | GIT |
| Licencia | LICENSE_NOT_CONFIRMED | ABSENT file |
| Ejecución | ninguna | — |
| Estado final | blocked; nac=true | GIT |

## rdfconfig_llm

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Static + companion | STATIC_AUDIT, COMPANION | GIT |
| Generator pin | `fe63171d…` | GIT |
| Companion MIT | pin companion | GIT |
| Zenodo | CC-BY-4.0 metadata | EXT |
| Ruby runtime | ABSENT host | ABSENT |
| Estado final | blocked; nac=true | GIT |

## sgpt

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Static + Z2/Z3 | audits, closure | GIT |
| Commit | `1f6964d1…` | GIT |
| Licencia | MIT | GIT |
| GPT-2 / checkpoints canario | workdir | LOCAL |
| Paper ckpt Table4 | — | ABSENT |
| Ejecución | Z2/Z3 logs + reports | GIT |
| Estado final | smoke_only reduced; nac=true | GIT |

## cot_sparql

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Static suite WAVE_C | audit/cot_sparql/* | GIT |
| Commit | `063edd98…` | GIT |
| Licencia | LICENSE_NOT_CONFIRMED | ABSENT |
| Embeddings/34B | — | EXT/ABSENT local |
| Estado final | blocked; nac=true | GIT |

## firesparql

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Static + results inventory | audit/firesparql/* | GIT |
| Commit | `48d6f168…` | GIT |
| Results files | inventory / posibles locales | GIT/LOCAL |
| Trainer/runner | — | ABSENT |
| HF ckpt | MIT card | EXT (≠ code license) |
| Estado final | not_reproducible; nac=true | GIT |

## tebaqa (histórico)

| Dimensión | Artefacto | Ubicación |
|---|---|---|
| Inclusión | HISTORICAL_ONLY | GIT registry |
| Fuera denominador Fase 1 activa | sí | GIT |

## Gates históricos (superseded para decisión operativa)

`NATIVE_AUDIT_COMPARATIVE_GATE.md`, `ZERO_COST_NATIVE_AUDIT_REGATE.md`, `POST_Z2_*`, `POST_Z3_*` — **HIST**; conservados; no borrar.
