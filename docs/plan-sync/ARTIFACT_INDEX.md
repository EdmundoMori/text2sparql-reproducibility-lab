# ARTIFACT_INDEX — Documentos específicos para el planificador

**Última actualización:** 2026-07-22 (Prompt 21B)  
**Documento general:** [`../../PLAN_SYNC.md`](../../PLAN_SYNC.md)

Cada fila es un artefacto que ChatGPT puede abrir para detalle. Tras cada prompt, Cursor añade o actualiza filas aquí.

| ID | Tema | Ruta | Cuándo leerlo |
|---|---|---|---|
| P21B-GATE | QALD T6B execution gate | `docs/protocols/common/acquisition/qald9plus/20260722T111153Z/QALD9PLUS_ACQUISITION_EXECUTION_GATE.md` | Tras T6B |
| P21B-RPT | Acquisition execution report | `audit/PHASE2_QALD9PLUS_ACQUISITION_EXECUTION_REPORT.md` | Detalle T6B |
| P21B-NEXT | Next after T6B | `audit/NEXT_AFTER_QALD9PLUS_ACQUISITION_EXECUTION_DECISION.md` | Siguiente |
| P21B-Q | Post-T6B queue | `audit/PHASE2_POST_T6B_QUEUE.csv` | Cola |
| P21A-GATE | QALD acquisition package gate | `docs/protocols/common/acquisition/qald9plus/20260722T105246Z/QALD9PLUS_ACQUISITION_PACKAGE_GATE.md` | Tras T6A |
| P21A-FORM | Human approval UNSIGNED | `docs/protocols/common/acquisition/qald9plus/20260722T105246Z/HUMAN_QALD9PLUS_ACQUISITION_APPROVAL.md` | Auth humana |
| P21A-RPT | Acquisition package report | `audit/PHASE2_QALD9PLUS_ACQUISITION_PACKAGE_REPORT.md` | Detalle T6A |
| P21A-NEXT | Next after package | `audit/NEXT_AFTER_QALD9PLUS_ACQUISITION_PACKAGE_DECISION.md` | Human gate |
| P21A-MAN | Exact file manifest | `configs/common/acquisition/qald9plus/QALD9PLUS_EN_DBPEDIA_EXACT_FILE_MANIFEST.yaml` | 4 files |
| P21A-Q | Post-T6A queue | `audit/PHASE2_POST_T6A_QUEUE.csv` | Cola |
|---|---|---|---|
| P20-GATE | Legal eligibility gate | `docs/protocols/common/legal/20260722T102434Z/LEGAL_ELIGIBILITY_GATE.md` | Tras T5 |
| P20-RPT | Legal recheck report | `audit/PHASE2_LEGAL_ELIGIBILITY_RECHECK_REPORT.md` | Detalle T5 |
| P20-NEXT | Next after legal | `audit/NEXT_AFTER_LEGAL_ELIGIBILITY_DECISION.md` | Siguiente acción |
| P20-DEC | Decisión 011 | `docs/decisions/011_phase2_legal_eligibility_and_acquisition_scope.md` | Alcance adquisición |
| P20-Q | Post-T5 queue | `audit/PHASE2_POST_T5_QUEUE.csv` | T6A/T6B/T6C |
| P20-CODE | Code license revalidation | `audit/PHASE2_CODE_LICENSE_REVALIDATION_MATRIX.csv` | Pin vs HEAD |
| P20-ACQ | Acquisition eligibility | `audit/PHASE2_CONTROLLED_ACQUISITION_ELIGIBILITY_MATRIX.csv` | Scopes |
| P20-EV | Legal evidence registry | `configs/common/LEGAL_EVIDENCE_REGISTRY.yaml` | Evidencia |
| CTX | Contexto operativo Cursor | `PROJECT_CONTEXT.md` | Siempre (reglas duras) |
| PROT | Protocolo científico | `RESEARCH_PROTOCOL.md` | Antes de proponer evaluación/adaptadores |
| MACH | Perfil host/WSL/GPU | `MACHINE_PROFILE.md` | Antes de proponer train/GPU/Docker |
| REG | Registro métodos | `METHOD_REGISTRY.yaml` | Estado inclusión / waves |
| LOCK | Pins commits clones | `REPOSITORIES.lock.yaml` | Reproducibilidad de árbol |
| DEC001 | Decisión límites máquina | `docs/decisions/001_machine_limits_warn_and_continue.md` | Política advertir→continuar |
| GATE8 | Native audit comparative gate (HIST) | `audit/NATIVE_AUDIT_COMPARATIVE_GATE.md` | superseded_by_15 |
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
| GATE-Q | Cola reproducción nativa | `audit/NATIVE_REPRODUCTION_QUEUE.csv` | 1× GO_NEXT (rdfconfig legal) |
| GATE-PF | Portafolio baselines | `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv` | diversidad metodológica |
| GATE-BR | Barreras transversales | `audit/REPRODUCIBILITY_BARRIER_MATRIX.csv` | taxonomía barreras |
| GATE-NX | Decisión siguiente acción | `audit/NEXT_EXECUTION_DECISION.md` | GO_NEXT rdfconfig legal (re-gate $0) |
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
| P9-GO | GO/NO-GO smoke futuro | `docs/protocols/sparql_llm/FUTURE_API_SMOKE_GONOGO.md` | histórico CONDITIONAL→NO_GO económico |
| P11-GATE | Gate online Prompt 11 | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/FINAL_ONLINE_SMOKE_GATE.md` | histórico; superseded por 11C ZERO_COST |
| GATE-RERUN | Re-gate interino rdfconfig | `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md` | interino; superseded por 11C formal |
| P9-RDY | Readiness protocolo | `audit/sparql_llm/API_SIB_PROTOCOL_READINESS.md` | estados por superficie |
| P9-LOG | Log Prompt 9 | `logs/sparql-llm-api-sib-protocol/commands.log` | sin llamadas |
| P10-RPT | Prep LOCAL_CHAT env/index | `audit/sparql_llm/LOCAL_CHAT_API_ENV_INDEX_PREP_REPORT.md` | Prompt 10 |
| P10-DF | Dockerfile agent Py3.11 | `environments/sparql_llm/Dockerfile.agent-py311` | extra [agent] |
| P10-SET | Settings mínimo | `environments/sparql_llm/minimal_local_chat_settings.json` | UniProt+void |
| P10-POL | Política índice mínimo | `environments/sparql_llm/MINIMAL_INDEX_POLICY.md` | LAB_MINIMAL_INDEX |
| P10-PREP | Manifest prep run | `environments/sparql_llm/preparations/20260721T084637Z/` | result/cache |
| P10-SCR | Script docs/index | `scripts/preparation/sparql_llm_minimal_index.py` | 3 modos |
| P10-PF | Script preflight | `scripts/preparation/sparql_llm_local_chat_preflight.py` | no ejecutado |
| P10-LOG | Logs prep | `logs/preparation/sparql-llm-local-chat-api/20260721T084637Z/` | docker/pip/docs |
| P10B-RPT | Download+index+preflight | `audit/sparql_llm/LOCAL_CHAT_API_EMBEDDING_INDEX_PREFLIGHT_REPORT.md` | Prompt 10B |
| P10B-AUTH | Autorización embeddings | `environments/sparql_llm/preparations/20260721T092249Z/EMBEDDING_DOWNLOAD_AUTHORIZATION.md` | Mori 2026-07-21 |
| P10B-PREP | Manifest 10B | `environments/sparql_llm/preparations/20260721T092249Z/` | result/cache inv |
| P10B-DL | Script descarga | `scripts/preparation/sparql_llm_download_embedding.py` | exact model only |
| P10B-LOG | Logs 10B | `logs/preparation/sparql-llm-embedding-index/20260721T092249Z/` | sin pesos en git |
| P11-RPT | Modelo+cota+gate final | `audit/sparql_llm/LOCAL_CHAT_API_MODEL_BUDGET_FINAL_GATE_REPORT.md` | Prompt 11 |
| P11-SNAP | Snapshot OpenRouter | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/OPENROUTER_MODEL_SNAPSHOT.json` | extracto candidatos |
| P11-MX | Matriz selección | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/MODEL_SELECTION_MATRIX.csv` | 1× SELECTED |
| P11-CLI | Defaults cliente | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/RESOLVED_CLIENT_DEFAULTS.md` | max_retries=2 |
| P11-COST | Cota económica | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/COST_BOUND.md` | TWO_CALL_BOUND |
| P11-Q | Pregunta smoke | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/SMOKE_QUESTION.md` | congelada |
| P11-REQ | Request spec | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/LOCAL_CHAT_SMOKE_REQUEST_SPEC.json` | no ejecutado |
| P11-DEC | Decisión modelo | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/MODEL_SELECTION_DECISION.md` | slug fechado |
| P11-HUM | Aprobación humana | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_LLM_SMOKE_APPROVAL.md` | sin firmar |
| P11-GATE | Gate online Prompt 11 | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/FINAL_ONLINE_SMOKE_GATE.md` | histórico; superseded 11C |
| P11-BUD | Presupuesto actualizado | `docs/protocols/sparql_llm/API_BUDGET_AND_SAFETY.md` | HUMAN_APPROVAL_PENDING |
| P11-LOG | Logs Prompt 11 | `logs/preparation/sparql-llm-model-budget-gate/20260721T100618Z/` | metadata SHA |
| P11-NOGO | NO-GO económico smoke online | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/ECONOMIC_NO_GO_DECISION.md` | Mori ZERO_USD |
| GATE-RERUN | Re-gate interino ZERO_USD | `audit/NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md` | superseded por 11C |
| DEC004 | ADR ZERO_COST + deferral online | `docs/decisions/004_zero_cost_policy_and_online_smoke_deferral.md` | Prompt 11C |
| P11C-HUM | Decisión humana coste 0 | `docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_ZERO_COST_DECISION.md` | elijo coste 0 |
| P11C-POL | Definición coste cero | `audit/ZERO_COST_POLICY.md` | prohibido/permitido |
| P11C-MX | Matriz acciones Z1–Z12 | `audit/ZERO_COST_ACTION_MATRIX.csv` | 1× GO_NEXT_ZERO_COST |
| P11C-Q | Cola ZERO_COST | `audit/ZERO_COST_NATIVE_REPRODUCTION_QUEUE.csv` | operativa |
| P11C-DEC | Decisión ejecución $0 | `audit/NEXT_ZERO_COST_EXECUTION_DECISION.md` | Z1 SGPT env |
| P11C-RPT | Informe re-gate 11C | `audit/ZERO_COST_NATIVE_AUDIT_REGATE.md` | 19 §§ |
| P11C-LOG | Logs Prompt 11C | `logs/zero-cost-native-regate/` | sin red/install |
| P12-RPT | Env definition SGPT | `audit/sgpt/ENVIRONMENT_DEFINITION_REPORT.md` | Prompt 12 |
| P12-GATE | Gate entorno SGPT | `environments/sgpt/ENVIRONMENT_GATE.md` | CONDITIONAL_DEPENDENCY_RESOLUTION |
| P12-SPEC | Spec entorno | `environments/sgpt/ENVIRONMENT_SPEC.yaml` | perfiles A/B/C |
| P12-DEP | Manifest deps | `environments/sgpt/DEPENDENCY_MANIFEST.yaml` | implícitas vs declared |
| P12-AST | Inventario imports AST | `logs/environment-definition-sgpt/import_inventory.json` | sin import runtime |
| P12-Z2 | Spec Z2 futuro | `environments/sgpt/Z2_DATA_METRIC_PREFLIGHT_SPEC.md` | no ejecutado |
| P12-LOG | Logs Prompt 12 | `logs/environment-definition-sgpt/` | coste 0 |
| P12B-RPT | Pin resolution SGPT | `audit/sgpt/PIN_RESOLUTION_REPORT.md` | Prompt 12B |
| P12B-DIR | Artefactos pin-resolution | `environments/sgpt/pin-resolution/20260721T113310Z/` | constraints+matrices |
| P12B-DF | Dockerfile Z2 candidato | `environments/sgpt/Dockerfile.z2-py38.candidate` | DO_NOT_BUILD_IN_12B |
| P12B-SCR | Resolver metadata oficial | `scripts/preparation/sgpt_official_metadata_resolver.py` | allowlist hosts |
| P12B-LOG | Logs Prompt 12B | `logs/environment-pin-resolution-sgpt/20260721T113310Z/` | network SHA |
| P13A-RPT | Z2 build+preflight | `audit/sgpt/Z2_BUILD_AND_PREFLIGHT_REPORT.md` | PASS |
| P13A-AUTH | Auth descarga Z2 | `environments/sgpt/builds/20260721T114919Z/Z2_DOWNLOAD_BUILD_AUTHORIZATION.md` | Mori |
| P13A-DF | Dockerfile Z2 build | `environments/sgpt/builds/20260721T114919Z/Dockerfile.z2-py38` | built |
| P13A-SMK | Harness offline Z2 | `scripts/smoke/sgpt_z2_offline_preflight.py` | network none |
| P13A-LOG | Logs Prompt 13A | `logs/environment-z2-build-sgpt/20260721T114919Z/` | freeze+preflight |
| P13B-RPT | Cierre Z2 + re-gate | `audit/sgpt/Z2_CLOSURE_AND_POST_Z2_REGATE_REPORT.md` | 13B |
| P13B-AUTH | Auth consumption | `environments/sgpt/builds/20260721T114919Z/AUTHORIZATION_CONSUMPTION_RECORD.md` | consumed |
| P13B-MAN | Z2 run manifest | `environments/sgpt/builds/20260721T114919Z/Z2_RUN_MANIFEST.yaml` | CLOSED |
| P13B-FRZ | Freeze resuelto | `environments/sgpt/builds/20260721T114919Z/z2-resolved-freeze.txt` | sha256 |
| P13B-EV | Matriz evidencia Z2 | `audit/sgpt/Z2_EVIDENCE_MATRIX.csv` | scope |
| P13B-LIM | Scope preflight | `audit/sgpt/Z2_PREFLIGHT_SCOPE_AND_LIMITATIONS.md` | limitations |
| P13B-CL | Cierre Z1/Z2 | `audit/sgpt/ZERO_COST_Z1_Z2_CLOSURE.md` | COMPLETE |
| P13B-MX | Matriz post-Z2 | `audit/POST_Z2_ZERO_COST_ACTION_MATRIX.csv` | PZ1-PZ12 |
| P13B-DEC | Decisión post-Z2 | `audit/NEXT_POST_Z2_ZERO_COST_DECISION.md` | PZ1 GO |
| P13B-Q | Cola post-Z2 | `audit/POST_Z2_ZERO_COST_QUEUE.csv` | operativa |
| P13B-LOG | Logs Prompt 13B | `logs/sgpt-z2-closure-regate/` | documental |
| P14A-RPT | Protocolo Z3 reduced train | `audit/sgpt/Z3_REDUCED_TRAINING_PROTOCOL_REPORT.md` | 14A |
| P14A-DIR | Artefactos protocolo Z3 | `docs/protocols/sgpt/z3/20260721T134213Z/` | gate |
| P14A-LOG | Logs Prompt 14A | `logs/protocol-definition-sgpt-z3/20260721T134213Z/` | metadata GET |
| P14B-RPT | P2A artifact+load report | `audit/sgpt/Z3_P2A_ARTIFACT_AND_MODEL_LOAD_REPORT.md` | PASS |
| P14B-AUTH | Auth 14B signed/consumed | `environments/sgpt/builds/20260721T135432Z/AUTHORIZATION_CONSUMPTION_RECORD.md` | Mori |
| P14B-SMK | Harness P2A | `scripts/smoke/sgpt_z3_p2a_model_load_preflight.py` | offline |
| P14B-LOG | Logs Prompt 14B | `logs/sgpt-z3-artifact-preflight/20260721T135432Z/` | integrity+P2A |
| P14B2-RPT | P2B no-grad forward | `audit/sgpt/Z3_P2B_NOGRAD_FORWARD_REPORT.md` | PASS |
| P14B2-SMK | Harness P2B | `scripts/smoke/sgpt_z3_p2b_nograd_forward.py` | one forward |
| P14B2-LOG | Logs Prompt 14B2 | `logs/sgpt-z3-p2b-forward/20260721T163853Z/` | offline |

| P14C-RPT | One-step reduced train report | `audit/sgpt/Z3_ONE_STEP_REDUCED_TRAINING_REPORT.md` | raw vs operativo |
| P14C-A1 | Attempt 1 build | `environments/sgpt/builds/20260721T183611Z/` | Z3_OTHER_FAILED |
| P14C-A2 | Attempt 2 build | `environments/sgpt/builds/20260722T072146Z/` | raw+evidence |
| P14C-RAW | Raw harness attempt2 | `environments/sgpt/builds/20260722T072146Z/z3_one_step_raw_harness_report.json` | optimizer_step=0 |
| P14C-SMK | One-step launcher | `scripts/smoke/sgpt_z3_one_step_train_launcher.py` | hook limitation |
| P14C-LOG | Logs 14C | `logs/sgpt-z3-one-step-train/` | att1+att2 |
| P14D-CL | Z3 closure report | `audit/sgpt/Z3_CLOSURE_REPORT.md` | 14D |
| P14D-REC | Evidence reconciliation | `audit/sgpt/Z3_ONE_STEP_EVIDENCE_RECONCILIATION.md` | hook vs flow |
| P14D-LED | Attempt ledger | `audit/sgpt/Z3_ONE_STEP_ATTEMPT_LEDGER.csv` | att1+att2 |
| P14D-EV | Evidence matrix | `audit/sgpt/Z3_ONE_STEP_EVIDENCE_MATRIX.csv` | hierarchy |
| P14D-AUTH | Authorization ledger | `audit/sgpt/Z3_AUTHORIZATION_LEDGER.md` | consumed |
| P14D-CHK | Native audit checklist | `audit/sgpt/SGPT_NATIVE_AUDIT_CLOSURE_CHECKLIST.md` | complete=true |
| P14D-GATE | Closure gate | `environments/sgpt/Z3_CLOSURE_GATE.md` | SMOKE_ONLY |
| P14D-DEC | Decision 005 | `docs/decisions/005_sgpt_z3_reduced_training_smoke_closure.md` | closure |
| P14D-MX | Matriz post-Z3 | `audit/POST_Z3_ZERO_COST_ACTION_MATRIX.csv` | Q1-Q12 |
| P14D-NEXT | Decisión post-Z3 | `audit/NEXT_POST_Z3_ZERO_COST_DECISION.md` | Q11 GO |
| P14D-Q | Cola post-Z3 | `audit/POST_Z3_ZERO_COST_QUEUE.csv` | operativa |
| P14D-LOG | Logs Prompt 14D | `logs/sgpt-z3-closure-regate/` | documental |

| P14D-HIST | Post-Z3 matrix/decision/queue | `audit/POST_Z3_ZERO_COST_*` | historical_after_15 |
| P15-SEM | Phase1 closure semantics | `audit/PHASE1_CLOSURE_SEMANTICS.md` | 15 |
| P15-CHK | Method closure checklist | `audit/PHASE1_METHOD_CLOSURE_CHECKLIST.csv` | 15 |
| P15-OUT | Final method outcomes | `audit/PHASE1_FINAL_METHOD_OUTCOMES.csv` | 15 |
| P15-MX | Final native audit matrix | `audit/PHASE1_FINAL_NATIVE_AUDIT_MATRIX.csv` | 15 |
| P15-EV | Evidence index | `audit/PHASE1_EVIDENCE_INDEX.md` | 15 |
| P15-BAR | Final barrier matrix | `audit/PHASE1_FINAL_BARRIER_MATRIX.csv` | 15 |
| P15-BSUM | Barrier summary | `audit/PHASE1_BARRIER_SUMMARY.md` | 15 |
| P15-PE | PE1-PE4 outcomes | `audit/PHASE1_EXPERIMENTAL_QUESTIONS_OUTCOME.md` | 15 |
| P15-GCHK | Global closure checklist | `audit/PHASE1_GLOBAL_CLOSURE_CHECKLIST.md` | 15 |
| P15-ELIG | Protocol eligibility matrix | `audit/COMMON_EVALUATION_PROTOCOL_ELIGIBILITY_MATRIX.csv` | 15 |
| P15-GATE | Phase1 final gate | `audit/PHASE1_FINAL_GATE.md` | 15 |
| P15-RPT | Phase1 final report | `audit/PHASE1_FINAL_NATIVE_AUDIT_REPORT.md` | 15 |
| P15-DEC | Decision 006 | `docs/decisions/006_phase1_native_audit_closure_and_phase2_transition.md` | 15 |
| P15-NEXT | Phase2 protocol decision | `audit/NEXT_PHASE2_PROTOCOL_DECISION.md` | T1 Prompt16 |
| P15-Q | Phase2 transition queue | `audit/PHASE2_TRANSITION_QUEUE.csv` | T1 selected |
| P15-LOG | Logs Prompt 15 | `logs/phase1-final-gate/` | documental |
| P15-PORT | Portfolio updated | `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv` | 15 |

| P16-TERM | Common terminology | `docs/protocols/common/20260722T083201Z/COMMON_PROTOCOL_TERMINOLOGY.md` | 16 |
| P16-TAX | Track taxonomy | `docs/protocols/common/20260722T083201Z/TRACK_TAXONOMY.md` | 16 |
| P16-DIR | Protocol pack | `docs/protocols/common/20260722T083201Z/` | 16 |
| P16-GATE | Protocol gate | `docs/protocols/common/20260722T083201Z/COMMON_PROTOCOL_GATE.md` | 16 |
| P16-PROF | Protocol profile | `configs/common/COMMON_PROTOCOL_PROFILE.yaml` | 16 |
| P16-SCH | Result schema draft | `configs/common/COMMON_RESULT_SCHEMA.json` | 16 |
| P16-TA | Track assignment | `audit/PHASE2_TRACK_ASSIGNMENT_MATRIX.csv` | candidate |
| P16-CMP | Comparison allowed | `audit/PHASE2_COMPARISON_ALLOWED_MATRIX.csv` | 16 |
| P16-DT | Dataset×track | `audit/PHASE2_DATASET_TRACK_COMPATIBILITY.csv` | 16 |
| P16-MET | Metric applicability | `audit/PHASE2_METRIC_APPLICABILITY_MATRIX.csv` | 16 |
| P16-IA | Information access | `audit/PHASE2_INFORMATION_ACCESS_MATRIX.csv` | 16 |
| P16-MG | Method gate matrix | `audit/PHASE2_METHOD_GATE_MATRIX.csv` | G0-G9 |
| P16-RISK | Protocol risk register | `audit/PHASE2_PROTOCOL_RISK_REGISTER.csv` | 16 |
| P16-RPT | Framework report | `audit/PHASE2_COMMON_EVALUATION_PROTOCOL_FRAMEWORK_REPORT.md` | 16 |
| P16-DEC | Decision 007 | `docs/decisions/007_common_evaluation_protocol_framework.md` | 16 |
| P16-Q | Protocol definition queue | `audit/PHASE2_PROTOCOL_DEFINITION_QUEUE.csv` | T2 selected |
| P16-NEXT | Next after protocol | `audit/NEXT_AFTER_COMMON_PROTOCOL_DECISION.md` | Prompt17 |
| P16-LOG | Logs Prompt 16 | `logs/common-protocol-definition/20260722T083201Z/` | documental |
| P15Q-HIST | Phase2 transition queue (HIST) | `audit/PHASE2_TRANSITION_QUEUE.csv` | preserved |

| P17-DIR | Dataset provenance pack | `docs/protocols/common/datasets/20260722T090627Z/` | 17 |
| P17-GATE | Provenance gate | `docs/protocols/common/datasets/20260722T090627Z/DATASET_PROVENANCE_GATE.md` | T2 |
| P17-REG | Source registry | `configs/common/DATASET_SOURCE_REGISTRY.yaml` | 17 |
| P17-ACQ | Acquisition template | `configs/common/DATASET_ACQUISITION_MANIFEST_TEMPLATE.yaml` | template only |
| P17-RES | Metadata resolver | `scripts/preparation/common_dataset_metadata_resolver.py` | metadata-only |
| P17-SRC | Source matrix | `audit/PHASE2_DATASET_SOURCE_MATRIX.csv` | 17 |
| P17-REP | Representation matrix | `audit/PHASE2_DATASET_REPRESENTATION_MATRIX.csv` | 17 |
| P17-HASH | Hash matrix | `audit/PHASE2_DATASET_HASH_MATRIX.csv` | 17 |
| P17-LIC | License evidence | `audit/PHASE2_DATASET_LICENSE_EVIDENCE.csv` | 17 |
| P17-LOC | Local copy lineage | `audit/PHASE2_LOCAL_DATASET_COPY_LINEAGE.csv` | read-only |
| P17-GRP | Graph provenance | `audit/PHASE2_GRAPH_PROVENANCE_MATRIX.csv` | 17 |
| P17-EP | Endpoint provenance | `audit/PHASE2_ENDPOINT_PROVENANCE_MATRIX.csv` | not queried |
| P17-RPT | Provenance report | `audit/PHASE2_DATASET_PROVENANCE_REPORT.md` | 17 |
| P17-DEC | Decision 008 | `docs/decisions/008_common_dataset_source_and_provenance.md` | 17 |
| P17-NEXT | Next after provenance | `audit/NEXT_AFTER_DATASET_PROVENANCE_DECISION.md` | Prompt18 |
| P17-Q | Post-T2 queue | `audit/PHASE2_POST_T2_QUEUE.csv` | T3 selected |
| P17-LOG | Logs Prompt 17 | `logs/dataset-provenance/20260722T090627Z/` | metadata-only |

## Qué está / no está en GitHub

| Path | En GitHub? | Notas |
|---|---|---|
| `upstream/<method_id>/` | **Sí** (árboles de trabajo) | Vendorizado 2026-07-19; pins en `REPOSITORIES.lock.yaml` |
| `upstream/*/.git_local/` | No | Metadatos git del clone original (solo local) |
| `logs/` | Sí (p. ej. clonado / smokes / audits) | Útiles para el planificador |
| `datasets/`, `results/`, `papers/`, `graph_snapshots/` | Solo placeholders | Contenido pesado futuro ignorado |
| `.env` | No | Secretos |

El planificador **puede** leer el código en `upstream/` directamente en el repo.

| P18-DIR | Metric/oracle pack | `docs/protocols/common/metrics/20260722T093257Z/` | 18 |
| P18-GATE | Metric gate | `docs/protocols/common/metrics/20260722T093257Z/METRIC_ORACLE_CONTRACT_GATE.md` | G5 doc |
| P18-REG | Metric registry | `configs/common/COMMON_METRIC_REGISTRY.yaml` | 0.1.0-documentary |
| P18-VEC | Conformance vectors | `docs/protocols/common/metrics/20260722T093257Z/METRIC_CONFORMANCE_TEST_VECTORS.yaml` | not executed |
| P18-RPT | Metric/oracle report | `audit/PHASE2_METRIC_ORACLE_CONTRACT_REPORT.md` | 18 |
| P18-DEC | Decision 009 | `docs/decisions/009_common_metric_oracle_and_statistics_contract.md` | 18 |
| P18-NEXT | Next after metric | `audit/NEXT_AFTER_METRIC_ORACLE_CONTRACT_DECISION.md` | Prompt19 |
| P18-Q | Post-T3 queue | `audit/PHASE2_POST_T3_QUEUE.csv` | T4 selected |
| P18-LOG | Logs Prompt 18 | `logs/metric-oracle-contract/20260722T093257Z/` | documental |

| P19-DIR | Adapter contracts pack | `docs/protocols/common/adapters/20260722T095602Z/` | 19 |
| P19-GATE | Adapter gate | `docs/protocols/common/adapters/20260722T095602Z/ADAPTER_CONTRACT_GATE.md` | G6D |
| P19-REG | Adapter registry | `configs/common/ADAPTER_CONTRACT_REGISTRY.yaml` | 19 |
| P19-RPT | Adapter contract report | `audit/PHASE2_ADAPTER_CONTRACT_REPORT.md` | 19 |
| P19-DEC | Decision 010 | `docs/decisions/010_common_adapter_contracts.md` | 19 |
| P19-NEXT | Next after adapters | `audit/NEXT_AFTER_ADAPTER_CONTRACT_DECISION.md` | Prompt20 |
| P19-Q | Post-T4 queue | `audit/PHASE2_POST_T4_QUEUE.csv` | T5 selected |
| P19-LOG | Logs Prompt 19 | `logs/adapter-contract-definition/20260722T095602Z/` | documental |
