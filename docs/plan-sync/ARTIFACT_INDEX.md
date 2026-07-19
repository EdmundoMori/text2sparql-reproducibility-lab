# ARTIFACT_INDEX — Documentos específicos para el planificador

**Última actualización:** 2026-07-19  
**Documento general:** [`../../PLAN_SYNC.md`](../../PLAN_SYNC.md)

Cada fila es un artefacto que ChatGPT puede abrir para detalle. Tras cada prompt, Cursor añade o actualiza filas aquí.

| ID | Tema | Ruta | Cuándo leerlo |
|---|---|---|---|
| CTX | Contexto operativo Cursor | `PROJECT_CONTEXT.md` | Siempre (reglas duras) |
| PROT | Protocolo científico | `RESEARCH_PROTOCOL.md` | Antes de proponer evaluación/adaptadores |
| MACH | Perfil host/WSL/GPU | `MACHINE_PROFILE.md` | Antes de proponer train/GPU/Docker |
| REG | Registro métodos | `METHOD_REGISTRY.yaml` | Estado inclusión / waves |
| LOCK | Pins commits clones | `REPOSITORIES.lock.yaml` | Reproducibilidad de árbol |
| DEC001 | Decisión límites máquina | `docs/decisions/001_machine_limits_warn_and_continue.md` | Política advertir→continuar |
| AUD-MAP | Paper↔código | `audit/PAPER_CODE_MAPPING.md` | Origen evidencia / repos |
| AUD-MX | Matriz auditoría inicial | `audit/INITIAL_AUDIT_MATRIX.csv` | Vista tabular candidatos |
| AUD-INC | Decisiones inclusión | `audit/INCLUSION_DECISIONS.md` | PRIMARY/CONDITIONAL/HISTORICAL |
| AUD-RES | Estimación recursos | `audit/RESOURCE_ESTIMATION.md` | Factibilidad local |
| AUD-EV | Cierre evidencias | `audit/EVIDENCE_CLOSURE.md` | Licencias, venue, Table 4 |
| AUD-LIC | Matriz licencias | `audit/LICENSE_MATRIX.csv` | Gates legales |
| AUD-RESX | Matriz resultados paper | `audit/RESULT_EVIDENCE_MATRIX.csv` | Qué está cerrado vs abierto |
| AUD-PUB | Estado publicación | `audit/PUBLICATION_STATUS.csv` | Preprint / DOI |
| AUD-CLN | Informe clonado | `audit/CLONING_REPORT.md` | SHAs, ondas, anomalías |
| CLN-SCR | Script clon | `scripts/clone_repositories.sh` | Cómo se pinneó |
| CLN-CFG | Manifest clon | `configs/clone_manifest.yaml` | Lista oficial clones |
| NEXT | Guía siguiente prompt | `docs/plan-sync/NEXT_PROMPT_GUIDANCE.md` | Qué proponer ahora |
| SYNC | Estado general | `PLAN_SYNC.md` | Punto de entrada |

## Qué está / no está en GitHub

| Path | En GitHub? | Notas |
|---|---|---|
| `upstream/<method_id>/` | **Sí** (árboles de trabajo) | Vendorizado 2026-07-19; pins en `REPOSITORIES.lock.yaml` |
| `upstream/*/.git_local/` | No | Metadatos git del clone original (solo local) |
| `logs/` | Sí (p. ej. clonado) | Útiles para el planificador |
| `datasets/`, `results/`, `papers/`, `graph_snapshots/` | Solo placeholders | Contenido pesado futuro ignorado |
| `.env` | No | Secretos |

El planificador **puede** leer el código en `upstream/` directamente en el repo.
