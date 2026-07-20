# NATIVE_AUDIT_COMPARATIVE_GATE — Síntesis comparativa y gate de auditoría nativa

**Fecha:** 2026-07-20  
**Prompt:** 8  
**Fase:** 1 — native audit (abierta)  
**Alcance documental:** sin instalaciones, sin ejecuciones, sin APIs, sin endpoints, sin descargas  
**Decisión vinculante:** `docs/decisions/003_native_audit_comparative_gate.md`  
**Decisión operativa:** `audit/NEXT_EXECUTION_DECISION.md`

---

## 1. Objetivo

Sintetizar la evidencia de WAVE_A–C y emitir un **gate formal** que determine:

1. qué acción única merece `GO_NEXT`;  
2. qué métodos conservan valor como baselines científicas;  
3. qué métodos quedan en espera (legal, hardware, artefactos, código);  
4. qué evidencia falta para cerrar la Fase 1;  
5. qué portafolio metodológico debe preservarse para la evaluación común futura —

sin convertir limitaciones de la laptop en juicios sobre la calidad científica de los métodos, y **sin** una puntuación única opaca.

## 2. Alcance

**Incluido:** seis métodos activos (`sparql_llm`, `mkgqagent`, `rdfconfig_llm`, `sgpt`, `cot_sparql`, `firesparql`); mención breve de `tebaqa` como histórico; dimensiones A–E del gate; colas y matrices asociadas; PE1–PE4.

**Excluido:** installs; smokes nuevos; train/infer; llamadas API; endpoints SPARQL; adapters; benchmark común; caso de estudio; cierre de Fase 1; filas de TeBaQA en las matrices principales de seis métodos.

## 3. Métodos evaluados

| method_id | inclusion | reproduction_status | wave |
|---|---|---|---|
| sparql_llm | INCLUDE_PRIMARY | **smoke_only** (5B; 5A setup_failed) | A + env + smoke |
| mkgqagent | INCLUDE_PRIMARY | audit_only | A |
| rdfconfig_llm | INCLUDE_CONDITIONAL | audit_only | A |
| sgpt | INCLUDE_PRIMARY | audit_only | B |
| cot_sparql | INCLUDE_CONDITIONAL | audit_only | C |
| firesparql | INCLUDE_CONDITIONAL | audit_only | C |
| tebaqa | HISTORICAL_ONLY | n/a (fuera de cola) | — |

Ningún método está `reproduced` o `partially_reproduced`.

## 4. Evidencia utilizada

Evidencia transversal: `INCLUSION_DECISIONS.md`, `LICENSE_MATRIX.csv`, `PAPER_CODE_MAPPING.md`, `EVIDENCE_CLOSURE.md`, `RESOURCE_ESTIMATION.md`, `METHOD_REGISTRY.yaml`, `MACHINE_PROFILE.md`, `RESEARCH_PROTOCOL.md`.

WAVE_A: matrices estáticas/entorno/readiness; audits `sparql_llm` / `mkgqagent` / `rdfconfig_llm`; smokes CORE_OFFLINE 5A/5B.  
WAVE_B: audit SGPT completo.  
WAVE_C: audits CoT-SPARQL y FIRESPARQL; `WAVE_C_STATIC_AUDIT_MATRIX.csv`.

**Etiquetas de evidencia** usadas en este gate: EXECUTION_VERIFIED, CODE_VERIFIED, DATA_VERIFIED, RESULT_FILE_VERIFIED, PAPER_REPORTED, README_REPORTED, LEGAL_VERIFIED, NOT_FOUND, UNKNOWN, INFERENCE.

**No se convierte:** `smoke_only` → reproducción; RESULT_FILE_VERIFIED → ejecución propia; LICENSE_NOT_CONFIRMED → permiso de adaptación; imposibilidad local → invalidez científica; métricas léxicas → Answer F1; HTTP 200 → corrección semántica.

## 5. Modelo del gate

Cinco dimensiones **independientes** (sin agregación aritmética):

### Dimensión A — Valor científico como baseline

Valores: `core_baseline_candidate` | `conditional_baseline_candidate` | `documentary_baseline` | `historical_reference` | `insufficient_evidence`.

### Dimensión B — Reproducibilidad nativa

Valores: `executable_now` | `executable_after_environment` | `executable_after_external_artifact` | `partial_protocol_only` | `not_ready` | `not_currently_reproducible`.

### Dimensión C — Factibilidad operativa

Valores: `local_low_cost` | `local_conditional` | `api_conditional` | `external_compute_required` | `blocked_on_current_host` | `unknown`.

### Dimensión D — Gate legal (por operación)

Operaciones: static_inspection; isolated_internal_execution; modification; adapter_integration; redistribution.  
Valores: `allowed` | `conditional` | `blocked` | `unknown`.  
**Regla:** la licencia de un checkpoint HF **no** licencia el repositorio de código.

### Dimensión E — Adaptabilidad futura

Valores: `configurable_general` | `generalizable_with_domain_package` | `retraining_required` | `domain_specific_reimplementation_required` | `unknown`.

### Regla lexicográfica de decisión (obligatoria)

1. La acción debe ser **legal** bajo el uso propuesto.  
2. Debe producir **evidencia nueva** sobre reproducibilidad nativa.  
3. El protocolo o componente debe estar **suficientemente definido** (si no, la acción puede ser definir el protocolo).  
4. Debe ser **técnicamente viable** con recursos conocidos.  
5. Debe aportar **valor metodológico distinto** a lo ya comprobado.  
6. Coste, tiempo y riesgo **proporcionales** al valor científico.  
7. **No** debe requerir sustituir silenciosamente el método publicado.

Una tabla ordinal auxiliar es legítima solo como ayuda; **no** reemplaza este orden.

## 6. Comparación por familia

| Familia | Método | Rol baseline |
|---|---|---|
| schema / RAG / validation | sparql_llm | core_baseline_candidate |
| agentic planning + feedback | mkgqagent | conditional_baseline_candidate |
| schema-guided deterministic | rdfconfig_llm | conditional_baseline_candidate |
| supervised generative (+ oracle entities) | sgpt | core_baseline_candidate |
| CoT + retrieval + external grounding | cot_sparql | documentary_baseline |
| domain-specific FT / RAG | firesparql | documentary_baseline |
| histórico template-based | tebaqa | historical_reference |

La diversidad de familias se conserva en `SCIENTIFIC_BASELINE_PORTFOLIO.csv` aunque la cola de ejecución priorice un solo prerrequisito.

## 7. Comparación de reproducibilidad

| method_id | recoverability (B) | status lab | Nota clave |
|---|---|---|---|
| sparql_llm | partial_protocol_only (CORE_OFFLINE hecho) + **executable_after_environment** (vía API) | smoke_only | Único con EXECUTION_VERIFIED parcial |
| mkgqagent | not_ready | audit_only | Offline NOT_READY; legal HOLD |
| rdfconfig_llm | executable_after_external_artifact → environment | audit_only | Zenodo/companion; Ruby ABSENT; legal generador |
| sgpt | not_ready | audit_only | Checkpoints NOT_FOUND |
| cot_sparql | not_ready | audit_only | Embeddings ausentes; 34B |
| firesparql | not_currently_reproducible | audit_only | Trainer + runner NOT_FOUND; results≠repro |

## 8. Comparación de factibilidad

Host: WSL2 ~7.4 GiB RAM; RTX 4050 6 GiB; Compose ABSENT; Ruby ABSENT; Python 3.10.12 (CODE_VERIFIED / MACHINE_PROFILE).

| method_id | local | API | compute externo |
|---|---|---|---|
| sparql_llm | local_conditional (Docker py311 CORE_OFFLINE) | api_conditional | bajo si API |
| mkgqagent | blocked_on_current_host (offline) | api_conditional | double e5 |
| rdfconfig_llm | blocked_on_current_host (Ruby) | api_conditional | bajo API+Ruby |
| sgpt | local_conditional | n/a | paper 2×12 GB |
| cot_sparql | blocked_on_current_host | n/a (GPTQ local) | 34B requerido |
| firesparql | blocked_on_current_host (8B) | api_conditional (OpenAI/Groq) | H100 train paper |

## 9. Comparación legal

| method_id | static inspection | isolated execution | modification / adapter / redistribute |
|---|---|---|---|
| sparql_llm | allowed (MIT) | allowed | allowed en principio; **adapters deferred** (`common_adapter_allowed=false`) |
| sgpt | allowed (MIT) | allowed | idem deferred |
| mkgqagent | allowed (inspección) | **blocked** (LICENSE_NOT_CONFIRMED) | blocked |
| rdfconfig_llm | allowed | **conditional/HOLD** (generador); companion MIT OK | blocked adapters hasta cierre |
| cot_sparql | allowed | blocked | blocked |
| firesparql | allowed | blocked (código); HF MIT ≠ código | blocked |

## 10. Comparación de generalidad

| method_id | generality_class |
|---|---|
| sparql_llm | configurable_general (SIB/schema) |
| mkgqagent | generalizable_with_domain_package (hosts/KG) |
| rdfconfig_llm | domain_specific_reimplementation_required (life-science schemas) |
| sgpt | retraining_required (anotaciones por KG) |
| cot_sparql | generalizable_with_domain_package (linkers/endpoints) |
| firesparql | domain_specific_reimplementation_required (ORKG/SciQA) |

## 11. Tracks experimentales

Métodos de tracks distintos **no** deben compararse en una única tabla de rendimiento.

| method_id | track |
|---|---|
| sparql_llm | end-to-end Text-to-SPARQL **con** validación de esquema |
| mkgqagent | agentic end-to-end |
| rdfconfig_llm | domain-specific / schema-guided generator |
| sgpt | supervised generative; **oracle entities** para Q_K (separar SGPT_Q vs Q_K) |
| cot_sparql | CoT + retrieval + grounding externo (**no** end-to-end puro) |
| firesparql | domain-specific fine-tuning / RAG pipeline |

Implicación: la evaluación común futura necesitará tracks etiquetados (end-to-end, oracle_grounding, agentic, domain_specific, generator_with_external_grounding), no un ranking monolítico.

## 12. Portafolio de baselines

Ver `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv`.

Se conservan las seis familias activas: dos `core_baseline_candidate` (sparql_llm, sgpt), dos `conditional` (mkgqagent, rdfconfig_llm), dos `documentary` (cot_sparql, firesparql), más TeBaQA histórico. La no-ejecutabilidad local **no** elimina a un método del portafolio científico.

## 13. Cola de reproducción nativa

Ver `audit/NATIVE_REPRODUCTION_QUEUE.csv`.

**Exactamente una fila `GO_NEXT`:** definición documental del protocolo API/SIB de SPARQL-LLM (`protocol_definition`).

Orden resumido:

1. **GO_NEXT** — protocolo API/SIB sparql_llm  
2. GO_AFTER_ENVIRONMENT — smoke API sparql_llm (después del protocolo)  
3. HOLD_LEGAL — cierre legal/fuente rdfconfig  
4. GO_AFTER_ENVIRONMENT — Ruby companion (tras legal)  
5–6. DOCUMENT_ONLY / HOLD_MISSING_MODEL — SGPT env / reduced train  
7. HOLD_LEGAL — mKGQAgent  
8–9. DOCUMENT_ONLY / HOLD_MISSING_CODE — FIRESPARQL métricas / runner  
10. HOLD_HARDWARE (+ legal) — CoT env  
11. NOT_CURRENTLY_ACTIONABLE — TeBaQA histórico  

## 14. Barreras transversales

Ver `audit/REPRODUCIBILITY_BARRIER_MATRIX.csv`.

Taxonomía aplicada: LICENSE, PAPER_CODE_MISMATCH, MISSING_CHECKPOINT, MISSING_TRAINER, MISSING_EXECUTION_RUNNER, MISSING_EVALUATOR, MISSING_DATA, SPLIT_DRIFT, ENDPOINT_DRIFT, API_MUTABILITY, HARDWARE, DEPENDENCY_DRIFT, RUNTIME_MISMATCH, METRIC_AMBIGUITY, GOLD_GROUNDING, DOMAIN_HARDCODING, NONDETERMINISM, COST, OTHER.

Barreras dominantes por método (síntesis):

- **sparql_llm:** RUNTIME_MISMATCH (Py3.10), ENDPOINT_DRIFT (Virtuoso), API_MUTABILITY (protocolo indefinido).  
- **mkgqagent:** LICENSE, DOMAIN_HARDCODING, HARDWARE (double e5).  
- **rdfconfig_llm:** LICENSE (generador), DEPENDENCY_DRIFT (Ruby), DOMAIN_HARDCODING.  
- **sgpt:** MISSING_CHECKPOINT, METRIC_AMBIGUITY, SPLIT_DRIFT, GOLD_GROUNDING.  
- **cot_sparql:** LICENSE, HARDWARE, MISSING_DATA, MISSING_EVALUATOR.  
- **firesparql:** LICENSE, MISSING_TRAINER, MISSING_EXECUTION_RUNNER, DOMAIN_HARDCODING, results≠repro.

## 15. Decisión del siguiente paso

**Acción:** protocolo API/SIB de SPARQL-LLM.  
**Tipo:** `protocol_definition`.  
**Clase cola:** `GO_NEXT`.  
**Título Prompt 9:** `Prompt 9 — Definición documental del protocolo API/SIB de SPARQL-LLM (sin llamadas de API)`.

Aplicación lexicográfica breve:

1. Legal — MIT, uso documental allowed.  
2. Evidencia nueva — acota PE2 online vs offline ya verificado.  
3. Protocolo indefinido — por eso la acción *es* definir protocolo.  
4. Viable — solo documentación.  
5. Distinto — no es un tercer CORE_OFFLINE.  
6. Coste bajo.  
7. Sin sustituir el método (no cuantizar, no cambiar LLM, no adapters).

Detalle: `NEXT_EXECUTION_DECISION.md` (§1–15).

## 16. Riesgos de sesgo de selección

- **Sesgo laptop:** priorizar solo lo que cabe en 6 GiB excluiría baselines valiosas (SGPT, CoT, FIRESPARQL, RDF-config); el portafolio mitiga este sesgo.  
- **Sesgo de código presente:** tener `results/` versionados no implica reproducibilidad (FIRESPARQL).  
- **Sesgo de smoke:** un smoke offline no responde PE3.  
- **Sesgo legal inverso:** LICENSE_NOT_CONFIRMED no borra valor científico, pero sí bloquea ejecución/adaptación.  
- **Sesgo de familia única:** elegir solo schema/RAG dejaría fuera agentic, oracle generative, CoT y domain FT — el portafolio lo impide.

## 17. Implicaciones para evaluación común

- No abrir `common_adapter_allowed`.  
- No implementar métricas comunes ni QALD-9 Plus en esta fase.  
- Diseñar (más adelante) evaluación por **tracks**, no una sola league table.  
- Answer F1 / Execution Accuracy del protocolo común no son sustituibles por BLEU léxico, HTTP 200 ni RESULT_FILE_VERIFIED.

## 18. Implicaciones para el caso de estudio

El caso de estudio (descubrimiento de modelos de IA) requiere baselines diversas: validación/schema (sparql_llm), agentic (mkgqagent), schema-guided (rdfconfig), generative supervisada (sgpt). CoT y FIRESPARQL aportan contraste documental (grounding externo; dominio académico). Nada de esto se inicia ahora; solo se preserva el portafolio.

## 19. Estado respecto de PE1–PE4

| PE | Estado | Justificación |
|---|---|---|
| **PE1** | **substantially_answered** | Inclusión PRIMARY/CONDITIONAL/HISTORICAL documentada; clones y audits estáticos de seis métodos activos. |
| **PE2** | **partial_evidence** | Solo `sparql_llm` CORE_OFFLINE `smoke_only` (Docker); no fracción amplia instalable; API aún no ejercida. |
| **PE3** | **not_started** | Ninguna reproducción de métricas del paper; smoke ≠ PE3; results versionados ≠ PE3. |
| **PE4** | **partial_evidence** | Barreras catalogadas en ondas A–C y en `REPRODUCIBILITY_BARRIER_MATRIX.csv`; taxonomía abierta a refino. |

## 20. Trabajo pendiente para cerrar Fase 1

Fase 1 **no** se declara cerrada. Falta, como mínimo:

1. Protocolo API/SIB (Prompt 9) y, si GO, un smoke API controlado etiquetado.  
2. Cierres legales donde aplique (mkgqagent, generador rdfconfig, cot, firesparql código).  
3. Política explícita ante MISSING_CHECKPOINT / MISSING_TRAINER / MISSING_RUNNER (reproducible vs not_currently_reproducible).  
4. Al menos un intento nativo adicional con métricas (PE3) **o** cierre documental motivado de no-reproducibilidad por método.  
5. Mantener `native_audit_complete=false` hasta evidencia suficiente por método; no abrir adapters.

## 21. Conclusión conservadora

El laboratorio dispone de un mapa metodológico rico y de una sola vía de ejecución parcial verificada (`sparql_llm` CORE_OFFLINE). La siguiente acción de máximo valor/riesgo mínimo es **documentar el protocolo API/SIB** — no entrenar SGPT, no instalar CoT, no recomputar FIRESPARQL, no ejecutar mKGQAgent, no instalar Ruby. El portafolio científico permanece diverso; la cola de reproducción es estricta y unitaria (`GO_NEXT` único). PE3 sigue sin iniciarse; cualquier afirmación de reproducción del paper sería, a día de hoy, incorrecta.

---

## Apéndice — Artefactos del Prompt 8

| Artefacto | Ruta |
|---|---|
| Informe de gate (este) | `audit/NATIVE_AUDIT_COMPARATIVE_GATE.md` |
| Matriz comparativa (6 filas) | `audit/NATIVE_AUDIT_GATE_MATRIX.csv` |
| Cola de reproducción | `audit/NATIVE_REPRODUCTION_QUEUE.csv` |
| Portafolio baselines | `audit/SCIENTIFIC_BASELINE_PORTFOLIO.csv` |
| Barreras | `audit/REPRODUCIBILITY_BARRIER_MATRIX.csv` |
| Decisión operativa | `audit/NEXT_EXECUTION_DECISION.md` |
| Decisión formal | `docs/decisions/003_native_audit_comparative_gate.md` |
