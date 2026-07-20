# ARTIFACT_INDEX — Documentos específicos para el planificador

**Última actualización:** 2026-07-20 (Prompt 9 — protocolo API/SIB)  
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
| WC-MX | Matriz WAVE_C | `audit/WAVE_C_STATIC_AUDIT_MATRIX.csv` | cot + fires complete |
| WC-LOG | Log Prompt 7A | `logs/static-audit-cot-sparql/commands.log` | solo lectura |
| WF-S | Static audit FIRESPARQL | `audit/firesparql/STATIC_AUDIT.md` | WAVE_C Prompt 7B |
| WF-INV | Inventario FIRESPARQL | `audit/firesparql/REPOSITORY_INVENTORY.md` | ~598M / results |
| WF-CK | Checkpoints/training | `audit/firesparql/CHECKPOINT_AND_TRAINING_ARTIFACT_INVENTORY.md` | trainer absent |
| WF-EXT | Artefactos externos | `audit/firesparql/EXTERNAL_ARTIFACT_INVENTORY.csv` | HF/OpenAI/Groq |
| WF-AST | Code health | `audit/firesparql/STATIC_CODE_HEALTH.md` | AST |
| WF-ARCH | Arquitectura | `audit/firesparql/ARCHITECTURE_AND_DATA_FLOW.md` | Mermaid |
| WF-PIPE | Pipeline matrix | `audit/firesparql/PIPELINE_COMPONENT_MATRIX.csv` | etapas A–H |
| WF-FT | Fine-tuning audit | `audit/firesparql/FINE_TUNING_REPRODUCIBILITY_AUDIT.md` | LLaMa-Factory |
| WF-MOD | Model configs | `audit/firesparql/MODEL_CONFIGURATION_MATRIX.csv` | 3B/8B epochs |
| WF-GEN | Generation | `audit/firesparql/GENERATION_AUDIT.md` | cuda/mps |
| WF-1S | One-shot | `audit/firesparql/ONE_SHOT_RETRIEVAL_AUDIT.md` | MiniLM gold |
| WF-RAG | RAG | `audit/firesparql/RAG_AUDIT.md` | Groq/Chroma |
| WF-CLN | Cleaning | `audit/firesparql/CLEANING_AND_REPAIR_AUDIT.md` | gpt-4o |
| WF-EX | QLever/ORKG | `audit/firesparql/EXECUTION_AND_QLEVER_AUDIT.md` | CODE_NOT_FOUND |
| WF-DS | Datasets | `audit/firesparql/DATASET_INVENTORY.csv` | SciQA 513 |
| WF-PROV | Dataset provenance | `audit/firesparql/DATASET_PROVENANCE_AND_SPLITS.md` | splits |
| WF-RES | Results inventory | `audit/firesparql/RESULTS_INVENTORY.csv` | configs |
| WF-RP | Result provenance | `audit/firesparql/RESULT_PROVENANCE_AND_COMPLETENESS.md` | versioned≠repro |
| WF-MET | Metrics | `audit/firesparql/METRICS_AUDIT.md` | BLEU/EM/RelaxedEM |
| WF-MAP | Paper mapping | `audit/firesparql/PAPER_RESULTS_CODE_MAPPING.csv` | README table |
| WF-EXP | Experiment matrix | `audit/firesparql/EXPERIMENT_CONFIGURATION_MATRIX.csv` | variants |
| WF-DEP | Dependencies | `audit/firesparql/DEPENDENCY_AND_RUNTIME_AUDIT.md` | no requirements |
| WF-DM | Dep matrix | `audit/firesparql/DEPENDENCY_MATRIX.csv` | imports |
| WF-GENR | Generalidad | `audit/firesparql/GENERALITY_AND_KG_USAGE_AUDIT.md` | ORKG-specific |
| WF-AN | Anomalías | `audit/firesparql/CODE_ANOMALIES_AND_RISKS.md` | paths/APIs |
| WF-RD | Readiness | `audit/firesparql/EXECUTION_READINESS.md` | not_ready |
| WF-LOG | Log Prompt 7B | `logs/static-audit-firesparql/commands.log` | solo lectura |
| GATE-RPT | Gate comparativo nativo | `audit/NATIVE_AUDIT_COMPARATIVE_GATE.md` | Prompt 8 — informe 21 §§ |
| GATE-MX | Matriz gate (6 métodos) | `audit/NATIVE_AUDIT_GATE_MATRIX.csv` | dimensiones A–E |
| GATE-Q | Cola reproducción nativa | `audit/NATIVE_REPRODUCTION_QUEUE.csv` | exactamente 1× GO_NEXT |
| GATE-PF | Portafolio baselines | `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv` | diversidad metodológica |
| GATE-BR | Barreras transversales | `audit/REPRODUCIBILITY_BARRIER_MATRIX.csv` | taxonomía barreras |
| GATE-NX | Decisión siguiente acción | `audit/NEXT_EXECUTION_DECISION.md` | GO/NO-GO Prompt 9 |
| DEC003 | Decisión formal gate | `docs/decisions/003_native_audit_comparative_gate.md` | ADR Prompt 8 |
| GATE-LOG | Log Prompt 8 | `logs/native-audit-comparative-gate/commands.log` | documental; no install |
| P9-PROT | Protocolo API/SIB principal | `docs/protocols/sparql_llm/API_SIB_PROTOCOL.md` | Prompt 9 — 26 §§ |
| P9-SURF | Superficies de ejecución | `docs/protocols/sparql_llm/EXECUTION_SURFACES.csv` | 8 superficies |
| P9-MCP | Contrato MCP | `docs/protocols/sparql_llm/MCP_CONTRACT.md` | tools + transportes |
| P9-CHAT | Contrato /chat | `docs/protocols/sparql_llm/CHAT_API_CONTRACT.md` | mismatch validate_output |
| P9-MOD | Modelos/proveedores | `docs/protocols/sparql_llm/MODEL_PROVIDER_MATRIX.csv` | OpenRouter vs init |
| P9-CFG | Configuración | `docs/protocols/sparql_llm/CONFIGURATION_MATRIX.csv` | secrets redactados |
| P9-NET | Red y side effects | `docs/protocols/sparql_llm/NETWORK_AND_SIDE_EFFECT_MATRIX.csv` | import/startup/request |
| P9-OFF | Frontera offline/online | `docs/protocols/sparql_llm/OFFLINE_ONLINE_BOUNDARY.md` | CORE_OFFLINE vs online |
| P9-SIB | Protocolo benchmarks SIB | `docs/protocols/sparql_llm/SIB_BENCHMARK_PROTOCOL.md` | L0/L1/L2 |
| P9-CAND | Candidatos smoke futuro | `docs/protocols/sparql_llm/FUTURE_SMOKE_CANDIDATES.csv` | A–F; D seleccionado |
| P9-BUD | Presupuesto y seguridad | `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md` | PROPOSED |
| P9-GO | GO/NO-GO smoke futuro | `docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md` | CONDITIONAL_GO |
| P9-RDY | Readiness protocolo | `audit/sparql_llm/API_SIB_PROTOCOL_READINESS.md` | estados por superficie |
| P9-LOG | Log Prompt 9 | `logs/sparql-llm-api-sib-protocol/commands.log` | sin llamadas |

## Qué está / no está en GitHub

| Path | En GitHub? | Notas |
|---|---|---|
| `upstream/<method_id>/` | **Sí** (árboles de trabajo) | Vendorizado 2026-07-19; pins en `REPOSITORIES.lock.yaml` |
| `upstream/*/.git_local/` | No | Metadatos git del clone original (solo local) |
| `logs/` | Sí (p. ej. clonado / smokes / audits) | Útiles para el planificador |
| `datasets/`, `results/`, `papers/`, `graph_snapshots/` | Solo placeholders | Contenido pesado futuro ignorado |
| `.env` | No | Secretos |

El planificador **puede** leer el código en `upstream/` directamente en el repo.
