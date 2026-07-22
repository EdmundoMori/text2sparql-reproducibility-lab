# PROJECT_CONTEXT

**Proyecto:** `text2sparql-reproducibility-lab`  
**Dominio:** Text-to-SPARQL / Knowledge Graph Question Answering (KGQA)  
**Inicio documental:** 2026-07-18  
**Fase actual:** Fase 1 **cerrada** · Fase 2 **QALD adquirido** · LC-QuAD T6C **HOLD** · grafo **target 2016-10 seleccionado (scope CONDITIONAL)** · adapters **deshabilitados** · benchmark **no ejecutado**  
**Estado:** Fase 1 nativa cerrada (smokes/bloqueos documentados). Clones presentes. Fase 2: framework de evaluación común definido; adapters deshabilitados; benchmark no ejecutado.  
**Perfil de máquina (obligatorio):** [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md)  
**Auditoría documental:** `audit/PAPER_CODE_MAPPING.md`, `audit/INITIAL_AUDIT_MATRIX.csv`, `audit/INCLUSION_DECISIONS.md`, `audit/RESOURCE_ESTIMATION.md`  
**Cierre de evidencias:** `audit/EVIDENCE_CLOSURE.md`, `audit/LICENSE_MATRIX.csv`, `audit/RESULT_EVIDENCE_MATRIX.csv`, `audit/PUBLICATION_STATUS.csv`  
**Clonado:** `audit/CLONING_REPORT.md`, `REPOSITORIES.lock.yaml`, `scripts/clone_repositories.sh`, `logs/cloning/`  
**Sync planificador (ChatGPT ↔ Cursor):** [`PLAN_SYNC.md`](PLAN_SYNC.md) — documento general actualizable; índice en [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md); guía del siguiente prompt en [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md). Repo GitHub: https://github.com/EdmundoMori/text2sparql-reproducibility-lab

---

## 1. Propósito

Laboratorio local de investigación en Text-to-SPARQL orientado a:

1. Auditar, clonar, documentar y ejecutar métodos publicados que traduzcan preguntas en lenguaje natural a consultas SPARQL explícitas.
2. Compararlos bajo un protocolo experimental común.
3. Adaptarlos, en fases posteriores, a un grafo de conocimiento para descubrimiento de modelos de IA.
4. Diseñar y evaluar un nuevo método general Text-to-SPARQL, fundamentado en análisis de errores e innovaciones transferibles desde Text-to-SQL.

---

## 2. Fase 1 — Objetivo inmediato

Auditar, clonar, documentar y ejecutar métodos publicados que cumplan, con evidencia verificable:

| Criterio | Descripción |
|---|---|
| Traducción NL→SPARQL | Generan consultas SPARQL explícitas a partir de preguntas en lenguaje natural |
| Respaldo científico | Están asociados a artículos científicos |
| Código público | Disponen de repositorio público verificable |
| Evaluación documentada | Han sido evaluados con datasets y métricas documentadas |
| Estudiabilidad / reproducibilidad | Pueden estudiarse y, cuando sea posible, reproducirse localmente |

**Regla operativa:** no se asume reproducibilidad a priori. Cada método debe verificarse mediante evidencia (código, commits, dependencias, datasets, comandos y resultados).

---

## 3. Métodos candidatos

| method_id | Repositorio(s) |
|---|---|
| `sparql_llm` | [sib-swiss/sparql-llm](https://github.com/sib-swiss/sparql-llm) |
| `mkgqagent` | [WSE-research/text2sparql-agent](https://github.com/WSE-research/text2sparql-agent) |
| `cot_sparql` | [dice-group/CoT-Sparql](https://github.com/dice-group/CoT-Sparql) |
| `firesparql` | [sherry-pan/FIRESPARQL](https://github.com/sherry-pan/FIRESPARQL) |
| `rdfconfig_llm` | [scott2121/sparql_query_generator](https://github.com/scott2121/sparql_query_generator), [dbcls/rdf-config](https://github.com/dbcls/rdf-config) |
| `sgpt` | [rashad101/SGPT-SPARQL-query-generation](https://github.com/rashad101/SGPT-SPARQL-query-generation) |
| `tebaqa` | [dice-group/TeBaQA](https://github.com/dice-group/TeBaQA) |

Los clones se ubicarán exclusivamente en `upstream/<method_id>`. No se modifican repositorios originales; las adaptaciones se implementan fuera de ellos.

---

## 4. Objetivo experimental posterior

Tras reproducir (o documentar la no-reproducibilidad de) los métodos en sus configuraciones originales, se construirán **adaptadores externos** para evaluarlos bajo un protocolo común.

### 4.1 Benchmark común inicial

| Prioridad | Benchmark | Alcance inicial |
|---|---|---|
| 1 | QALD-9 Plus | Preguntas en inglés; consultas sobre DBpedia |
| 2 | LC-QuAD 2.0 | Escala y complejidad |

### 4.2 Métricas primarias comunes

- Answer Precision  
- Answer Recall  
- Answer F1  
- Execution Accuracy  

### 4.3 Métricas diagnósticas

- Syntax Validity Rate  
- Executable Query Rate  
- Normalized Exact Match  
- Entity Linking F1 *(cuando sea observable)*  
- Relation Linking F1 *(cuando sea observable)*  
- Triple-pattern F1  
- Empty-result Rate  
- Hallucinated IRI Rate  
- Latencia  
- Tokens utilizados  
- Coste estimado  
- Número de llamadas al LLM y al endpoint  

**Importante:** las métricas originales de cada artículo se conservan y se reportan por separado; no se confunden con las métricas comunes.

---

## 5. Objetivo a largo plazo

1. Adaptar los métodos a un grafo de conocimiento para descubrimiento de modelos de IA.  
2. Emplear una ontología que armonice metadatos de Hugging Face, Kaggle, Civitai, PyTorch Hub, TensorFlow Hub y Papers with Code.  
3. Crear un paquete de dominio con ontología, aliases, mappings, ejemplos y consultas gold.  
4. Analizar sistemáticamente los errores de los métodos existentes.  
5. Revisar innovaciones recientes de Text-to-SQL.  
6. Identificar una técnica aún no implementada de forma equivalente en Text-to-SPARQL.  
7. Diseñar un nuevo método general Text-to-SPARQL.  
8. Evaluarlo primero en benchmarks públicos y después en el caso de estudio.  
9. Demostrar mediante ablaciones si supera a los métodos existentes.

---

## 6. Reglas científicas no negociables

1. No inventar resultados, comandos, dependencias ni configuraciones.  
2. No declarar que un experimento ha sido reproducido si no fue ejecutado.  
3. Distinguir siempre entre: **resultado reportado**, **reproducido**, **parcialmente reproducido** y **no reproducido**.  
4. No modificar los repositorios originales directamente.  
5. Los repositorios clonados permanecen en `upstream/<method_id>`.  
6. Toda adaptación se implementa fuera del repositorio original.  
7. Registrar el commit exacto utilizado.  
8. Registrar fecha, sistema operativo, hardware, versiones y comandos.  
9. Conservar las métricas originales de cada artículo.  
10. No confundir métricas originales con métricas comunes.  
11. No usar el conjunto de test para seleccionar prompts, hiperparámetros o ejemplos.  
12. No cambiar simultáneamente el método y el LLM en una comparación controlada.  
13. No ocultar errores ni sustituir dependencias sin documentarlo.  
14. No considerar un smoke test como reproducción del artículo.  
15. No ejecutar comandos destructivos.  
16. No almacenar credenciales en el repositorio.  
17. No realizar commits automáticos salvo solicitud expresa.  
18. No avanzar a la adaptación común de un método hasta completar su auditoría nativa.

---

## 7. Limitaciones de la máquina local (operativas)

El laboratorio **sí puede continuar en esta máquina**. Las limitaciones no cancelan el proyecto: **afinan** pedidos, priorizan rutas viables y obligan a documentar degradaciones.

Detalle medido: `MACHINE_PROFILE.md`. Resumen vinculante:

| Recurso | Capacidad local | Riesgo principal |
|---|---|---|
| Plataforma | Windows + WSL2 Ubuntu 22.04 | Paths, interop, device nodes GPU |
| CPU | Ryzen 7 7840HS (8c/16t) | Adecuada para auditoría y pipelines moderados |
| RAM WSL | ≈ **7.4 GiB** (host ≈ 16 GiB) | OOM con grafos grandes, JVM pesada, varios servicios |
| GPU / VRAM | RTX 4050 ≈ **6 GiB**; CUDA driver 13.0; `nvcc` ausente | Entrenamientos grandes / LLMs locales “full” |
| Docker | Daemon OK; **Compose ausente** | Stacks `docker compose` sin plugin |
| Entornos | Poetry sí; **Conda/uv no** | Setup por método más manual |
| Disco | ≈ **901 GiB** libres | No es cuello de botella |

### 7.1 Clases de viabilidad (usar en avisos)

| Clase | Uso |
|---|---|
| `feasible_local_cpu` | Cabe en CPU/RAM actuales sin GPU ni API obligatoria |
| `feasible_local_gpu` | Cabe en RTX 4050 (≤≈6 GB VRAM), posiblemente con cuantización/batch bajo |
| `feasible_using_api` | Viable con LLM/endpoints remotos y credenciales en `.env` |
| `requires_external_gpu` | Requiere GPU/VRAM o cluster fuera de esta máquina |
| `currently_unknown` | Aún no hay evidencia de auditoría; no asumir |

### 7.2 Protocolo obligatorio del agente ante pedidos incompatibles o inconvenientes

Si un pedido del usuario **choca** o es **claramente inconveniente** con las limitaciones de esta sección / `MACHINE_PROFILE.md`, el agente debe, **en este orden y sin bloquear el trabajo**:

1. **Advertencia inmediata** (breve): qué recurso limita y por qué.  
2. **Solución o degradación propuesta** (concreta): p. ej. API en lugar de LLM local, subir RAM de WSL, cuantizar, subconjunto, Compose plugin, GPU externa, marcar `partially_reproduced` / `blocked`.  
3. **Continuar** con lo pedido usando la ruta más segura compatible, o la degradación documentada si el usuario no indica lo contrario.  
4. **Registrar** el trade-off en la ficha/auditoría/log o en `docs/decisions/` cuando afecte reproducibilidad.

**No** usar las limitaciones para rechazar el proyecto ni para omitir la fase solicitada.  
**No** silenciar el riesgo ni sustituir dependencias sin documentarlo (regla científica §6.13).

### 7.3 Disparadores típicos de advertencia

Emitir advertencia (+ solución + continuar) cuando el pedido implique, entre otros:

- Fine-tuning o inferencia local de modelos que tipicamente requieren **>6 GB VRAM**.  
- Cargar en memoria dumps RDF / endpoints embebidos / varios JVMs con **RAM WSL ≈7.4 GiB**.  
- Uso de **`docker compose`** sin instalar el plugin.  
- Asumir **Conda/uv** o **`python`** (solo existe `python3`).  
- Compilar extensiones CUDA con **`nvcc`** (ausente).  
- Ejecutar muchos servicios Docker + entrenamiento GPU + evaluación a la vez.  
- Tratar un smoke test bajo recursos como reproducción completa del artículo.

### 7.4 Mitigaciones preferidas (catálogo corto)

| Situación | Mitigación preferida |
|---|---|
| LLM local demasiado grande | API (`feasible_using_api`) o modelo cuantizado ≤VRAM |
| Entrenamiento full-scale | Documentar `requires_external_gpu`; reproducir inferencia/eval si es posible |
| OOM / RAM WSL | Subir memoria en `.wslconfig`; cerrar servicios; datasets/subsets; un proceso pesado a la vez |
| `docker compose` | Instalar plugin Compose, o comandos `docker` equivalentes documentados |
| Sin Conda/uv | venv + pip, Poetry, o contenedor por método |
| Solo `python3` | Alias documentado en el adaptador/scripts del lab, sin parchear upstream |
| Endpoint/KG enorme | Endpoint remoto o snapshot acotado en `graph_snapshots/` |

Las limitaciones **ayudan a afinar pedidos**: preferir auditoría → smoke → reproducción parcial documentada → evaluación vía API antes de lanzar entrenamientos o cargas masivas.

---

## 8. Forma de trabajo

Antes de cada tarea:

1. Leer `PROJECT_CONTEXT.md` (incluida la §7 de limitaciones).  
2. Leer `RESEARCH_PROTOCOL.md`.  
3. Consultar `MACHINE_PROFILE.md` si la tarea implica ejecución, GPU, Docker, RAM o entornos.  
4. Revisar el estado actual del proyecto (y `PLAN_SYNC.md` si se está en bucle con el planificador).  
5. Si el pedido es inconveniente con §7: **advertencia → solución → continuar** (protocolo §7.2).  
6. Explicar brevemente qué se va a realizar.  
7. Ejecutar únicamente la fase solicitada.  
8. Registrar comandos, resultados, errores y degradaciones por hardware.  
9. Actualizar la documentación; si el prompt forma parte del plan ChatGPT: actualizar `PLAN_SYNC.md`, `docs/plan-sync/ARTIFACT_INDEX.md` y, si cambia la prioridad, `NEXT_PROMPT_GUIDANCE.md`.  
10. Detenerse al finalizar la fase y presentar los resultados.  
11. Tras prompts del plan: **commit + push** a GitHub cuando el investigador lo pida (o cuando el prompt lo indique explícitamente), sin subir `upstream/`, secretos ni artefactos pesados.

### 8.1 Bucle Cursor ↔ ChatGPT (optimización del plan)

1. ChatGPT propone **un** prompt.  
2. Cursor lo ejecuta y documenta hallazgos en `PLAN_SYNC.md` + docs específicos.  
3. Commit + push a https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
4. El investigador pega en ChatGPT el meta-prompt de replanificación.  
5. ChatGPT relee el repo, valida el plan y entrega el siguiente prompt.  

Detalle: `docs/plan-sync/PLANNER_LOOP.md`.

---

## 9. Estado del laboratorio

| Elemento | Estado |
|---|---|
| Directorio del proyecto | Creado |
| `PROJECT_CONTEXT.md` | Actualizado |
| `RESEARCH_PROTOCOL.md` | Creado |
| Estructura de workspace | Creada (Prompt 1) |
| `README.md` / `MACHINE_PROFILE.md` | Creados; limitaciones operativas enlazadas |
| Reglas §7 (advertencia → solución → continuar) | Activas |
| Registros (`METHOD_REGISTRY`, `REPOSITORIES.lock`, `EXPERIMENT_REGISTRY`) | METHOD_REGISTRY + locks de clones actualizados; experimentos aún vacíos |
| `PLAN_SYNC.md` / `docs/plan-sync/` | Activo — entrada del planificador ChatGPT |
| Repo GitHub lab | https://github.com/EdmundoMori/text2sparql-reproducibility-lab |
| Auditoría paper/código (Prompt 2) | Completada |
| Cierre evidencias (licencias, T4 SGPT, venue SPARQL-LLM) | Completado — ver `EVIDENCE_CLOSURE.md` |
| Inclusión | PRIMARY: sparql_llm, mkgqagent, sgpt; CONDITIONAL: cot_sparql, firesparql, rdfconfig_llm; HISTORICAL: tebaqa |
| SPARQL-LLM publicación | preprint **Under Review** (no DOI editorial TWEB verificado) |
| Licencias no confirmadas | mkgqagent, cot_sparql, firesparql (GitHub), scott2121 HEAD |
| `Makefile` | Creado (`just` no disponible en el host) |
| Clones en `upstream/` | 7 paths (6 métodos); tebaqa no clonado; **versionados en GitHub** (árboles; `.git_local/` solo local) — ver decisión 002 |
| Ondas | A: sparql_llm, mkgqagent, rdfconfig_llm; B: sgpt; C: cot_sparql, firesparql; D: tebaqa |
| Auditorías nativas con ejecución | Pendiente (clon ≠ ejecución) |
| Adaptadores comunes | Bloqueados hasta auditoría nativa |
| Evaluación común (QALD-9 Plus / LC-QuAD 2.0) | Pendiente |
| Caso de estudio (descubrimiento de modelos de IA) | Pendiente |

### Registro de entorno

| Campo | Valor |
|---|---|
| Fecha workspace | 2026-07-18T10:46:48+02:00 |
| Plataforma | Windows host + WSL2 Ubuntu 22.04.5 LTS |
| CPU | AMD Ryzen 7 7840HS (8c/16t) |
| RAM WSL / host | ≈7.4 GiB / ≈16 GiB |
| GPU | NVIDIA GeForce RTX 4050 Laptop (≈6 GiB VRAM); CUDA driver 13.0; `nvcc` ausente |
| Docker | 29.1.3 (daemon OK); Compose plugin ausente |
| Python / Java / Node | 3.10.12 / OpenJDK 21.0.11 / v18.20.8 |
| Poetry / Conda / uv | Poetry 2.3.1 / ausente / ausente |
| Disco libre | ≈901 GiB |
| Repositorios clonados | 7 paths en `upstream/` (pins en `REPOSITORIES.lock.yaml`); no versionados |
| Métodos ejecutados | Ninguno |
| Detalle | Ver `MACHINE_PROFILE.md` |

---

## 10. Próxima acción prevista

Auditoría estática de `upstream/` y, solo bajo petición explícita, smoke tests WAVE_A (API) sin confundirlos con reproducción del artículo. No integrar en adaptadores repos `LICENSE_NOT_CONFIRMED`.

---

## Prompt 15 — Phase 1 final gate (añadido; no reescribe historia)

**Fecha cierre Fase 1:** 2026-07-22  
**Gate:** `PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION`  
**Qualifier:** `RESIDUAL_METHOD_BLOCKERS_PRESERVED`  
**phase1_status:** `closed` · **phase2_status:** `lcquad2_scope_clarified_graph_decision_pending`  
**Adapters:** `common_adapter_allowed=false` (todos)  
**Distribución (6 activos):** smoke_only×2 (sparql_llm, sgpt); blocked×3 (mkgqagent, rdfconfig_llm, cot_sparql); not_reproducible×1 (firesparql)  
**TeBaQA:** `HISTORICAL_ONLY` (fuera del denominador)  
**PE1:** substantially_answered · **PE2:** partial_evidence · **PE3:** not_started (`no_comparable_original_metric_run_available`) · **PE4:** substantially_answered_for_current_portfolio  
**Fase 2:** aún **no** ejecutada — solo elegibilidad documental; siguiente Prompt 16 (definición protocolo común), sin adapters ni benchmarks.  
**Informe:** `audit/PHASE1_FINAL_NATIVE_AUDIT_REPORT.md` · Decisión: `docs/decisions/006_phase1_native_audit_closure_and_phase2_transition.md`


---

## Estado actual post-Prompt 16

- Fase 1 cerrada; outcomes individuales intactos.
- Fase 2: protocolo común **framework-only** (`COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`).
- Tracks ortogonales; QALD-9 Plus primario; LC-QuAD 2.0 secundario; pins pending.
- `common_adapter_allowed=false`; sin benchmark.
- PE5/PE6: framework defined pending execution; PE7/PE8 not_started.
- Siguiente: Prompt 17 (T2 provenance), sin descargas.

---

## Estado actual post-Prompt 17

- Provenance RUN_ID: `20260722T090627Z`.
- Gate: `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`.
- Source pins: QALD `8eb038a61e1bc09cbd21640aa667a1714f53cda4`; LC-QuAD `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` (`CURRENT_SOURCE_SNAPSHOT_NOT_PUBLICATION_RELEASE`).
- Vistas: PRIMARY `QALD9_PLUS_EN_DBPEDIA`; SECONDARY `LCQUAD2_DBPEDIA18`; EXT `LCQUAD2_WIKIDATA`.
- Payload no adquirido; graph snapshot pending; G4 runtime pin **no** satisfecho.
- Adapters false; benchmark `NOT_CURRENTLY_ELIGIBLE`.
- PE5/PE6 sin cambio de estado experimental; evidencia preparatoria de provenance añadida.
- Siguiente: Prompt 18 (T3 métricas/oracle documental).


---

## Estado actual post-Prompt 18

- Metric contract RUN_ID: `20260722T093257Z` · version `0.1.0-documentary`.
- Gate: `METRIC_ORACLE_CONTRACT_DOCUMENTED_READY_FOR_ADAPTER_CONTRACTS`.
- Primary metrics: Answer P/R/F1 + Execution Exact; set semantics; empty≠no_output.
- RDF/SPARQL canonicalization V1; oracle/linking observability defined; stats (bootstrap 10000, Holm).
- G5 documentary satisfied; G5 runtime pending; G4 still not satisfied.
- Adapters false; benchmark not eligible; no metric implementation.
- Siguiente: Prompt 19 (T4 adapter contracts documentales).


---

## Estado actual post-Prompt 19

- Adapter contract RUN_ID: `20260722T095602Z` · version `0.1.0-documentary`.
- Gate: `ADAPTER_CONTRACTS_DOCUMENTED_READY_FOR_LEGAL_ELIGIBILITY_RECHECK`.
- G6D documented; G6I pending; common_adapter_allowed=false.
- RDFConfig dual track resolved (domain vs DBpedia negative).
- SPARQL-LLM generate-only vs feedback; SGPT q/qk; CoT native/frozen; FIRE raw/cleaned/RAG.
- Siguiente: Prompt 20 (T5 legal eligibility recheck).

---

## Estado actual post-Prompt 20

- Legal RUN_ID: `20260722T102434Z`.
- Gate: `LEGAL_RECHECK_COMPLETE_PARTIAL_SCOPE_READY_FOR_ACQUISITION_AUTHORIZATION_PACKAGE`.
- Clasificación: `LAB_POLICY_CLASSIFICATION_BASED_ON_PUBLISHED_EVIDENCE` (no asesoramiento jurídico).
- G3C: SPARQL-LLM/SGPT MIT pin verified; mKG/RDFConfig GitHub/CoT/FIRE LICENSE_ABSENT.
- G3 composite: CONDITIONAL (SPARQL-LLM/SGPT) o NOT_SATISFIED (resto activo).
- QALD-9 Plus EN/DBpedia: `LAB_POLICY_ACQUISITION_ELIGIBLE_AFTER_AUTHORIZATION` (CC BY 4.0).
- LC-QuAD authors: `LAB_POLICY_ACQUISITION_HOLD_SCOPE_UNCLEAR` (T6C).
- RDFConfig Zenodo archive separado; content equivalence NOT_VERIFIED.
- Modelos/servicios inventariados; terms NOT_INTERPRETED.
- G4 not satisfied; G5 runtime pending; G6D documented; G6I pending.
- common_adapter_allowed=false; benchmark NOT_CURRENTLY_ELIGIBLE; no download; no implementation.
- Siguiente: Prompt 21A (T6A acquisition authorization package documental).

---

## Estado actual post-Prompt 21A

- Acquisition package RUN_ID: `20260722T105246Z`.
- Gate: `QALD9PLUS_ACQUISITION_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION`.
- Exact scope: QALD9_PLUS_EN_DBPEDIA · 4 files · total 7815874 · pin `8eb038a61e1bc09cbd21640aa667a1714f53cda4` · tree `7159958810958ff185187cf603e2c4a997dc2df9`.
- Attribution draft DRAFT_NOT_APPLIED · test seal plan defined · form UNSIGNED.
- authorization_id null · acquisition NOT_ACQUIRED · no T6B · no download.
- LC-QuAD HOLD · graph pending · G4 not · G5 runtime pending · G6I pending.
- common_adapter_allowed=false · benchmark NOT_CURRENTLY_ELIGIBLE.
- Siguiente: HUMAN_QALD9PLUS_ACQUISITION_AUTHORIZATION (Prompt 21B reservado).

---

## Estado actual post-Prompt 21B

- Execution RUN_ID: `20260722T111153Z` · authorization `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` CONSUMED.
- Gate: `QALD9PLUS_CONTROLLED_ACQUISITION_PASS_VALIDATED`.
- QALD EN/DBpedia: 4 files verified · counts 408/150 · test SEALED · workdir only.
- Graph pending · G4 not satisfied · LC-QuAD HOLD · G5 runtime/G6I pending.
- common_adapter_allowed=false · benchmark NOT_CURRENTLY_ELIGIBLE.
- Siguiente: Prompt 22 (T6C LC-QuAD clarification).

---

## Estado actual post-Prompt 22

- T6C RUN_ID: `20260722T112721Z` · Gate: `LCQUAD2_SCOPE_CLARIFIED_ALL_REPRESENTATIONS_HOLD`.
- Authors LC-QuAD: LICENSE absent @ `0a5f8f85b6f863c3b80f0fa02839e25d438af3ae` · HOLD.
- HF mohnish/lc_quad: CC BY 3.0 card added by platform username · authority/lineage insufficient · no alternative.
- No LC-QuAD payload · QALD path not blocked · next Prompt 23 graph decision.

## Estado actual post-Prompt 23

- Graph RUN_ID: `20260722T120239Z` · Gate: `DBPEDIA_2016_10_NATIVE_GRAPH_TARGET_SELECTED_PACKAGE_CONDITIONAL_FILE_SCOPE`.
- Primary: `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` (2016-10) · Fallback: `COMMON_GRAPH_REBASE`.
- Available package: 81 files / 5023159516 bytes · 33 unavailable blockers · form `NOT_READY_CONDITIONAL`.
- Graph payload NOT_ACQUIRED · deployment NOT_DEPLOYED · G4 runtime not satisfied.
- QALD sealed/consumed · LC-QuAD HOLD · adapters false · benchmark NOT_CURRENTLY_ELIGIBLE.
- Siguiente: Prompt 23B (cerrar file scope).
