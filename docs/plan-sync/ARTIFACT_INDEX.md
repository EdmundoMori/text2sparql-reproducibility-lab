# ARTIFACT_INDEX — Documentos específicos para el planificador

**Última actualización:** 2026-07-20  
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
| LOOP | Ciclo Cursor↔ChatGPT | `docs/plan-sync/PLANNER_LOOP.md` | Cómo replanificar tras cada push |
| SYNC | Estado general | `PLAN_SYNC.md` | Punto de entrada |
| DEC002 | Vendor upstream en GitHub | `docs/decisions/002_vendor_upstream_on_github.md` | Por qué el código está en el repo |
| WA-S | Static audit sparql_llm | `audit/sparql_llm/STATIC_AUDIT.md` | Entrypoints/MCP/Compose/eval |
| WA-M | Static audit mkgqagent | `audit/mkgqagent/STATIC_AUDIT.md` | FastAPI/plan/feedback/legal |
| WA-R | Static audit rdfconfig_llm | `audit/rdfconfig_llm/STATIC_AUDIT.md` | Frontera Python↔Ruby |
| WA-RC | Companion rdf-config | `audit/rdfconfig_llm/COMPANION_RDF_CONFIG_AUDIT.md` | MIT companion separado |
| WA-MX | Matriz WAVE_A | `audit/WAVE_A_STATIC_AUDIT_MATRIX.csv` | Comparativa tabular |
| WA-RD | Execution readiness | `audit/WAVE_A_EXECUTION_READINESS.md` | next_safe_action por método |
| WA-LOG | Log inspección | `logs/static-audit-wave-a/commands.log` | Comandos solo lectura |
| ENV-R | Convención entornos | `environments/README.md` | native vs smoke; pins |
| ENV-W | Política workspace | `environments/EXECUTION_WORKSPACE_POLICY.md` | no writes en upstream |
| ENV-S | Env sparql_llm | `environments/sparql_llm/` | CORE_OFFLINE primero |
| ENV-M | Env mkgqagent | `environments/mkgqagent/` | legal + double e5 |
| ENV-Rcfg | Env rdfconfig | `environments/rdfconfig_llm/` | Ruby ABSENT; Zenodo |
| WA-EMX | Matriz entornos | `audit/WAVE_A_ENVIRONMENT_DEFINITION_MATRIX.csv` | scopes por método |
| WA-GAP | Gaps entornos | `audit/WAVE_A_ENVIRONMENT_GAPS.md` | GO/NO-GO + primer smoke |
| ENV-LOG | Log Prompt 4B | `logs/environment-definition-wave-a/commands.log` | host tools |
| SM5A-RPT | Smoke 5A host report | `audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md` | setup_failed Py3.10 |
| SM5B-RPT | Smoke 5B Docker report | `audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md` | smoke_only Py3.11 |
| DF311 | Dockerfile CORE | `environments/sparql_llm/Dockerfile.core-offline-py311` | digest pin |
| CT311 | Container notes | `environments/sparql_llm/container_py311.md` | runtime Docker |
| SM5A-R | Run experiment 5A | `experiments/native/sparql_llm/20260719T112306Z/` | manifest/result setup_failed |
| SM5A-L | Logs smoke 5A | `logs/smoke/sparql_llm-core-offline/20260719T112306Z/` | pip/freeze/smoke |
| SM5B-R | Run experiment 5B | `experiments/native/sparql_llm/20260720T134943Z/` | smoke_only Docker |
| SM5B-L | Logs smoke 5B | `logs/smoke/sparql_llm-core-offline-py311/20260720T134943Z/` | docker/import/smoke |
| SM-H | Harness lab | `scripts/smoke/sparql_llm_core_offline.py` | CORE_OFFLINE harness |
| WB-S | Static audit SGPT | `audit/sgpt/STATIC_AUDIT.md` | WAVE_B principal |
| WB-INV | Inventario repo SGPT | `audit/sgpt/REPOSITORY_INVENTORY.md` | árbol / archivos |
| WB-CK | Checkpoints SGPT | `audit/sgpt/CHECKPOINT_AND_RESULTS_INVENTORY.md` | ausencias |
| WB-ARCH | Arquitectura SGPT | `audit/sgpt/ARCHITECTURE_AND_DATA_FLOW.md` | modelo + Mermaid |
| WB-VAR | Variantes SGPT | `audit/sgpt/CONFIGURATION_AND_VARIANTS_MATRIX.csv` | Q / Q_K / masked |
| WB-DS | Inventario datasets | `audit/sgpt/DATASET_INVENTORY.csv` | conteos + sha256 |
| WB-PROV | Provenance splits | `audit/sgpt/DATASET_PROVENANCE_AND_SPLITS.md` | mismatch 6046; qald9 IDs |
| WB-TR | Training config | `audit/sgpt/TRAINING_CONFIGURATION_AUDIT.md` | epochs/LR/seed |
| WB-MET | Metrics audit | `audit/sgpt/METRICS_AUDIT.md` | double update; no Answer F1 |
| WB-T4 | Table 4 mapping | `audit/sgpt/PAPER_TABLE4_CODE_MAPPING.csv` | flags ↔ scores |
| WB-DEP | Dependencies | `audit/sgpt/DEPENDENCY_AND_RUNTIME_AUDIT.md` | pins / riesgos |
| WB-RD | Execution readiness | `audit/sgpt/EXECUTION_READINESS.md` | ready/blocked/not_ready |
| WB-MX | Matriz WAVE_B | `audit/WAVE_B_STATIC_AUDIT_MATRIX.csv` | fila sgpt |
| WB-LOG | Log Prompt 6 | `logs/static-audit-sgpt/commands.log` | solo lectura |
| WC-S | Static audit CoT-SPARQL | `audit/cot_sparql/STATIC_AUDIT.md` | WAVE_C Prompt 7A |
| WC-INV | Inventario CoT-SPARQL | `audit/cot_sparql/REPOSITORY_INVENTORY.md` | 22 archivos |
| WC-EXT | Artefactos externos | `audit/cot_sparql/EXTERNAL_ARTIFACT_INVENTORY.csv` | embeddings/GPTQ/APIs |
| WC-AST | Code health AST | `audit/cot_sparql/STATIC_CODE_HEALTH.md` | asserts / parse |
| WC-ARCH | Arquitectura CoT | `audit/cot_sparql/ARCHITECTURE_AND_DATA_FLOW.md` | Mermaid |
| WC-RET | Retrieval + prompt | `audit/cot_sparql/RETRIEVAL_AND_PROMPT_AUDIT.md` | one-shot MiniLM |
| WC-GR | Grounding/linking | `audit/cot_sparql/GROUNDING_AND_LINKING_AUDIT.md` | EL/RL DBpedia/Wikidata |
| WC-GRM | Grounding matrix | `audit/cot_sparql/GROUNDING_COMPONENT_MATRIX.csv` | componentes |
| WC-DS | Datasets CoT | `audit/cot_sparql/DATASET_INVENTORY.csv` | train-only |
| WC-PROV | Provenance CoT | `audit/cot_sparql/DATASET_PROVENANCE_AND_SPLITS.md` | gold en retrieval |
| WC-RT | Model/runtime | `audit/cot_sparql/MODEL_AND_RUNTIME_AUDIT.md` | GPTQ 34B |
| WC-DEP | Dependency matrix | `audit/cot_sparql/DEPENDENCY_MATRIX.csv` | conda vs pip |
| WC-VAL | Validation | `audit/cot_sparql/VALIDATION_AND_EXECUTION_AUDIT.md` | HTTP 200 |
| WC-MET | Eval/metrics | `audit/cot_sparql/EVALUATION_AND_METRICS_AUDIT.md` | PAPER_REPORTED |
| WC-MAP | Paper↔code map | `audit/cot_sparql/PAPER_CODE_EXPERIMENT_MAPPING.csv` | experimentos |
| WC-AN | Anomalías | `audit/cot_sparql/CODE_ANOMALIES_AND_RISKS.md` | assert/Falcon/RL |
| WC-RD | Readiness CoT | `audit/cot_sparql/EXECUTION_READINESS.md` | blocked/not_ready |
| WC-MX | Matriz WAVE_C | `audit/WAVE_C_STATIC_AUDIT_MATRIX.csv` | cot complete; fires pending |
| WC-LOG | Log Prompt 7A | `logs/static-audit-cot-sparql/commands.log` | solo lectura |

## Qué está / no está en GitHub

| Path | En GitHub? | Notas |
|---|---|---|
| `upstream/<method_id>/` | **Sí** (árboles de trabajo) | Vendorizado 2026-07-19; pins en `REPOSITORIES.lock.yaml` |
| `upstream/*/.git_local/` | No | Metadatos git del clone original (solo local) |
| `logs/` | Sí (p. ej. clonado / smokes / audits) | Útiles para el planificador |
| `datasets/`, `results/`, `papers/`, `graph_snapshots/` | Solo placeholders | Contenido pesado futuro ignorado |
| `.env` | No | Secretos |

El planificador **puede** leer el código en `upstream/` directamente en el repo.
