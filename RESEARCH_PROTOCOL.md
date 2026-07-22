# RESEARCH_PROTOCOL

**Proyecto:** `text2sparql-reproducibility-lab`  
**Versión del protocolo:** 0.1  
**Fecha:** 2026-07-18  
**Alcance temporal del documento:** Fase 1 (auditoría y reproducibilidad nativa) y marco para fases posteriores

---

## 1. Objetivo

Establecer un protocolo experimental reproducible para:

1. Auditar métodos publicados de Text-to-SPARQL con evidencia verificable.  
2. Reproducir, cuando sea posible, sus configuraciones nativas sin alterar el código upstream.  
3. Comparar posteriormente esos métodos bajo un protocolo común de evaluación.  
4. Fundamentar, con evidencia, el diseño de un nuevo método general Text-to-SPARQL y su evaluación en benchmarks públicos y en un caso de estudio de descubrimiento de modelos de IA.

El protocolo prioriza la **integridad experimental** sobre la velocidad: un método no se declara reproducible sin ejecución documentada; un smoke test no constituye reproducción del artículo.

---

## 2. Alcance

### 2.1 Incluido en el laboratorio

- Métodos que generan **consultas SPARQL explícitas** a partir de lenguaje natural.  
- Artículos científicos asociados y código público.  
- Datasets y métricas documentadas en las publicaciones o repositorios.  
- Clonación y estudio en `upstream/<method_id>`.  
- Registro de commits, entorno, comandos, errores y resultados.  
- Evaluación común futura mediante adaptadores externos (fuera de upstream).  
- Benchmarks previstos: QALD-9 Plus (inglés, DBpedia) y, posteriormente, LC-QuAD 2.0.

### 2.2 Excluido en esta fase (Fase 1)

- Implementación de adaptadores comunes.  
- Selección de hiperparámetros o prompts usando el conjunto de test.  
- Modificación directa de repositorios originales.  
- Declaración de reproducción sin ejecución.  
- Evaluación sobre el grafo de conocimiento del caso de estudio de modelos de IA (fase posterior).  
- Diseño e implementación del nuevo método general (fase posterior).

### 2.3 Tecnologías y estándares de referencia

- RDF, OWL, SPARQL 1.1  
- KGQA / Text-to-SPARQL  
- Evaluación de sistemas NLP y buenas prácticas de reproducibilidad experimental

---

## 3. Preguntas experimentales

### 3.1 Fase 1 — Reproducibilidad nativa

**PE1.** ¿Qué métodos candidatos cumplen los criterios de inclusión con evidencia verificable (artículo, código, datasets, métricas)?  

**PE2.** ¿Qué fracción de métodos puede instalarse y ejecutarse localmente en la configuración reportada (o la más cercana documentada)?  

**PE3.** Cuando un método es ejecutable, ¿se obtienen métricas coherentes con las reportadas en el artículo (reproducción, reproducción parcial o divergencia documentada)?  

**PE4.** ¿Cuáles son las barreras de reproducibilidad dominantes (dependencias, datos, endpoints, LLMs, hardware, documentación incompleta)?  

### 3.2 Fase posterior — Evaluación común

**PE5.** Bajo un protocolo común (QALD-9 Plus, inglés, DBpedia; métricas primarias Answer Precision/Recall/F1 y Execution Accuracy), ¿cómo se comparan los métodos adaptados externamente?  

**PE6.** ¿Qué fallos sistemáticos revelan las métricas diagnósticas (sintaxis, ejecutabilidad, linking, patrones triples, IRIs alucinadas, vacíos, latencia/coste)?  

**PE7.** ¿Qué innovaciones de Text-to-SQL no tienen equivalente claro en Text-to-SPARQL y son candidatas a transferirse?  

**PE8.** En el caso de estudio de descubrimiento de modelos de IA, ¿un nuevo método general supera a las baselines existentes según ablaciones controladas?

---

## 4. Reglas de reproducibilidad

1. **Evidencia primero:** no inventar resultados, comandos, dependencias ni configuraciones.  
2. **Ejecución requerida:** no declarar reproducción sin haber ejecutado el experimento documentado.  
3. **Estados explícitos:** cada intento se clasifica según la Sección 5.  
4. **Upstream intacto:** no modificar repositorios originales; clones solo en `upstream/<method_id>`.  
5. **Adaptaciones externas:** cualquier cambio vive fuera de upstream.  
6. **Pin de commit:** registrar el hash exacto clonado/evaluado.  
7. **Registro de entorno:** fecha, SO, hardware, versiones de runtime/paquetes relevantes, comandos exactos.  
8. **Métricas originales conservadas:** reportar siempre las del artículo; no sustituirlas por las comunes.  
9. **Separación de métricas:** métricas originales ≠ métricas del protocolo común.  
10. **Sin fuga de test:** no usar el test set para elegir prompts, hiperparámetros o ejemplos.  
11. **Un factor por comparación:** no cambiar a la vez método y LLM en comparaciones controladas.  
12. **Transparencia de fallos:** no ocultar errores; documentar sustituciones de dependencias si son inevitables.  
13. **Smoke ≠ reproducción:** una prueba mínima de arranque no equivale a reproducir el artículo.  
14. **Seguridad operativa:** no comandos destructivos; no credenciales en el repositorio.  
15. **Control de versiones del lab:** no commits automáticos salvo solicitud expresa.  
16. **Gate de fase:** no iniciar adaptación común de un método sin auditoría nativa completa.  
17. **Límites de máquina:** consultar `MACHINE_PROFILE.md` y `PROJECT_CONTEXT.md` §7. Ante pedidos inconvenientes con el hardware local: advertencia inmediata, mitigación concreta y continuación documentada (no silencio ni aborto injustificado).

---

## 5. Estados posibles de una reproducción

Cada método (y cada experimento concreto asociado) se etiqueta con **exactamente uno** de los estados siguientes, justificado con evidencia:

| Estado | Definición operativa |
|---|---|
| `not_started` | No se ha iniciado la auditoría ni la ejecución. |
| `audit_only` | Se ha documentado artículo/código/datos/métricas, sin ejecución experimental. |
| `setup_failed` | Falló la instalación, descarga de datos o preparación del entorno; no hubo ejecución válida del pipeline. |
| `smoke_only` | Solo se verificó arranque/importación/consulta trivial; **no** constituye reproducción del artículo. |
| `reported_only` | Se citan resultados del artículo u otra fuente; no hay ejecución propia. |
| `partially_reproduced` | Se ejecutó un subconjunto sustancial del protocolo original (p. ej., un split, un KG, un modelo) con métricas comparables parcialmente; divergencias documentadas. |
| `reproduced` | Se ejecutó el protocolo nativo relevante y las métricas obtenidas son coherentes con las reportadas, dentro de tolerancias documentadas. |
| `not_reproduced` | Se intentó la reproducción con evidencia suficiente y los resultados divergen de forma material, o el protocolo original no pudo completarse tras intentos documentados. |
| `not_reproducible` | Con la evidencia disponible, el método no puede reproducirse (código ausente/incompleto, datos inaccesibles, dependencias irrecuperables, etc.), sin que ello implique haber obtenido métricas divergentes. |
| `blocked` | La reproducción está temporalmente impedida por un factor externo documentado (API, cuota, endpoint, licencia, hardware). |

**Notas de uso:**

- `reported_only` nunca se promociona a `reproduced` sin ejecución.  
- `smoke_only` nunca se reporta como reproducción del artículo.  
- Ante duda entre `partially_reproduced` y `not_reproduced`, se documenta la divergencia y se elige el estado más conservador compatible con la evidencia.

---

## 6. Criterios de inclusión y exclusión de métodos

### 6.1 Inclusión (todos deben cumplirse con evidencia)

1. Traduce preguntas en lenguaje natural a **consultas SPARQL explícitas** (no solo respuestas finales sin consulta observable).  
2. Existe **artículo científico** asociado (preprint o publicación).  
3. Existe **código público** verificable.  
4. Existe **evaluación documentada** con dataset(s) y métrica(s).  
5. Es **estudiable** en este laboratorio (licencia/acceso permiten clonación y análisis; la reproducibilidad local se verifica aparte).

### 6.2 Exclusión

1. Sistemas de KGQA que no exponen o no generan SPARQL de forma utilizable para auditoría.  
2. Demostraciones sin artículo, o artículos sin código público.  
3. Repositorios vacíos, privados o claramente incompletos sin artefactos evaluables.  
4. Métodos cuya evaluación no pueda documentarse (ni en paper ni en repo).  
5. Código que requiera modificar upstream de forma inseparable para cualquier estudio (salvo que pueda encapsularse externamente; si no, se documenta como barrera).

### 6.3 Métodos candidatos iniciales

`sparql_llm`, `mkgqagent`, `cot_sparql`, `firesparql`, `rdfconfig_llm`, `sgpt`, `tebaqa`.

La inclusión definitiva de cada candidato se decide tras auditoría; la lista inicial **no** implica inclusión automática.

---

## 7. Distinción entre reproducción nativa y evaluación común

| Dimensión | Reproducción nativa | Evaluación común |
|---|---|---|
| Objetivo | Verificar lo publicado en la configuración original (o la más cercana documentada) | Comparar métodos bajo un protocolo uniforme del laboratorio |
| Código | Upstream sin modificar (`upstream/<method_id>`) | Adaptadores externos fuera de upstream |
| Datos | Datasets/splits/KGs del artículo | QALD-9 Plus (en, DBpedia) y después LC-QuAD 2.0 |
| Métricas | Las originales del artículo | Primarias y diagnósticas del laboratorio (Sección de métricas en `PROJECT_CONTEXT.md`) |
| LLM / modelos | Los reportados por los autores, si son recuperables | Controlados; no se cambian método y LLM a la vez en comparaciones |
| Prerrequisito | Auditoría nativa completa | Reproducción nativa intentada y documentada (éxito, parcialidad o imposibilidad) |
| Interpretación | Validez de la claim de reproducibilidad del trabajo | Comparabilidad entre sistemas |

**Regla de transición:** no se inicia la evaluación común de un método hasta completar su auditoría nativa. Un fallo de reproducción nativa no impide, por sí solo, una evaluación común posterior, pero debe quedar documentado como limitación.

---

## 8. Riesgos metodológicos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Confundir métricas originales y comunes | Conclusiones inválidas de superioridad | Tablas separadas; etiquetado explícito |
| Fuga de información del test set | Sobreajuste de prompts/hiperparámetros | Reservas de splits; registro de decisiones solo sobre train/dev |
| Cambiar método y LLM a la vez | Atribución causal imposible | Diseños factoriales / un factor por comparación |
| Endpoints SPARQL inestables o distintos al paper | Divergencia espuria de Execution Accuracy / F1 | Fijar endpoint, capturar versiones/dumps cuando sea posible; documentar drift |
| Dependencias o modelos irrecuperables | Falsa etiqueta de no-reproducibilidad o atajos opacos | Documentar bloqueos; no sustituir en silencio |
| Contar smoke tests como reproducción | Inflar tasas de éxito | Estados de la Sección 5; revisión de evidencia |
| Modificar upstream “por conveniencia” | Pérdida de trazabilidad | Adaptadores externos obligatorios |
| Coste/latencia de LLMs y cuotas | Experimentos incompletos o no repetibles | Presupuestos, caché de respuestas documentada, registro de tokens/coste |
| Ambigüedad en linking (entidades/relaciones) | Métricas diagnósticas no observables | Marcar “no observable” en lugar de inventar scores |
| Sesgo de selección de métodos | Generalización indebida | Criterios de inclusión/exclusión aplicados por evidencia |

---

## 9. Objetivos posteriores

Tras completar la Fase 1 (auditoría y reproducibilidad nativa documentada):

1. Construir adaptadores externos para evaluación común.  
2. Evaluar en QALD-9 Plus (inglés, DBpedia) con métricas primarias y diagnósticas.  
3. Extender a LC-QuAD 2.0 para escala y complejidad.  
4. Adaptar métodos al grafo/ontología de descubrimiento de modelos de IA (Hugging Face, Kaggle, Civitai, PyTorch Hub, TensorFlow Hub, Papers with Code).  
5. Crear un paquete de dominio (ontología, aliases, mappings, ejemplos, gold SPARQL).  
6. Analizar errores sistemáticos de los métodos existentes.  
7. Revisar innovaciones recientes de Text-to-SQL e identificar transferencias no implementadas en Text-to-SPARQL.  
8. Diseñar un nuevo método general Text-to-SPARQL.  
9. Evaluarlo en benchmarks públicos y en el caso de estudio.  
10. Validar mejoras mediante ablaciones controladas.

---

## 10. Artefactos mínimos por método (plantilla operativa)

Para cada `method_id`, el laboratorio deberá disponer eventualmente de:

- Ficha de auditoría (artículo, repo, commit, licencia, datasets, métricas originales).  
- Registro de entorno y comandos.  
- Estado de reproducción (Sección 5) con evidencia.  
- Resultados nativos (si aplica) y divergencias.  
- Decisión: ¿apto para adaptación común? (sí / no / condicionado), con justificación.

La creación de estos artefactos se realizará en fases posteriores solicitadas explícitamente; este protocolo solo define el marco.

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

## Addendum Prompt 16 — Protocolo común (framework)

**Fecha:** 2026-07-22  
**Gate:** `COMMON_PROTOCOL_FRAMEWORK_DEFINED_READY_FOR_DATASET_PROVENANCE`  
**Fase 1:** permanece cerrada; definiciones de estados de reproducción (§5) **sin cambio**.

### PE5–PE8 (registro, sin resultados de benchmark)

| PE | Estado |
|---|---|
| PE5 | `protocol_framework_defined_pending_benchmark` |
| PE6 | `diagnostic_metric_framework_defined_pending_execution` |
| PE7 | `not_started` |
| PE8 | `not_started` |

### Condición de transición

Puede avanzar T2 (dataset provenance documental). **No** implica adapters ni benchmark. `common_adapter_allowed` sigue false.

---

## Addendum Prompt 17 — Dataset provenance

**Fecha:** 2026-07-22  
**RUN_ID:** `20260722T090627Z`  
**Gate:** `DATASET_PROVENANCE_DOCUMENTED_READY_FOR_METRIC_ORACLE_CONTRACT`  
**Qualifiers:** `DATASET_PAYLOAD_NOT_ACQUIRED` · `GRAPH_SNAPSHOT_ACQUISITION_PENDING` · `G4_RUNTIME_PIN_NOT_SATISFIED`

### PE5–PE8

Estados **sin cambio experimental**. Evidencia preparatoria: `dataset_source_provenance_documented`; `payload_not_acquired`; `graph_snapshot_pending`. PE5 **no** iniciado experimentalmente.

### Condición de transición

Puede avanzar T3 (contrato métricas/oracle documental). **No** implica adquisición de payloads, SPARQL, adapters ni benchmark.


---

## Addendum Prompt 18 — Metric/oracle/statistical contract

**Fecha:** 2026-07-22  
**RUN_ID:** `20260722T093257Z`  
**Gate:** `METRIC_ORACLE_CONTRACT_DOCUMENTED_READY_FOR_ADAPTER_CONTRACTS`

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | `protocol_and_metric_contract_defined_pending_benchmark` |
| PE6 | `diagnostic_metric_contract_defined_pending_execution` |
| PE7 | `not_started` |
| PE8 | `not_started` |

Evidencia preparatoria: metric/oracle/statistical contracts documented; conformance vectors defined not executed. Sin resultados experimentales.


---

## Addendum Prompt 19 — Adapter contracts

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T095602Z`  
**Gate:** `ADAPTER_CONTRACTS_DOCUMENTED_READY_FOR_LEGAL_ELIGIBILITY_RECHECK`

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | `protocol_metric_and_adapter_contracts_defined_pending_implementation_and_benchmark` |
| PE6 | `diagnostic_metric_and_adapter_observability_contracts_defined_pending_execution` |
| PE7 | `not_started` |
| PE8 | `not_started` |

Sin implementación ni ejecución de adapters.

---

## Addendum Prompt 20 — Legal eligibility recheck

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T102434Z`  
**Gate:** `LEGAL_RECHECK_COMPLETE_PARTIAL_SCOPE_READY_FOR_ACQUISITION_AUTHORIZATION_PACKAGE`  
**Clasificación:** `LAB_POLICY_CLASSIFICATION_BASED_ON_PUBLISHED_EVIDENCE`

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | `protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark` |
| PE6 | `diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution` |
| PE7 | `not_started` |
| PE8 | `not_started` |

Evidencia preparatoria: legal_layers_revalidated · acquisition_scope_classified · attribution_requirements_documented · no_assets_acquired.

T6 dividido: T6A autorización documental · T6B ejecución (auth humana) · T6C LC-QuAD clarification.  
Sin descarga, implementación ni autorización de adquisición en Prompt 20.

---

## Addendum Prompt 21A — QALD acquisition authorization package

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T105246Z`  
**Gate:** `QALD9PLUS_ACQUISITION_PACKAGE_READY_FOR_HUMAN_AUTHORIZATION`

### PE5–PE8

| PE | Estado |
|---|---|
| PE5 | `protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark` |
| PE6 | `diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution` |
| PE7 | `not_started` |
| PE8 | `not_started` |

Evidencia preparatoria: qald_acquisition_package_documented · exact_file_scope_locked · attribution_manifest_drafted · test_seal_plan_defined · human_authorization_pending · no_assets_acquired.

Authorization **UNSIGNED**. Acquisition **NOT_ACQUIRED**. T6B no ejecutado. Prompt 21B solo reservado.

---

## Addendum Prompt 21B — QALD controlled acquisition (T6B)

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T111153Z`  
**authorization_id:** `AUTH_QALD9PLUS_T6B_20260722T105246Z_EMO_01` · CONSUMED  
**Gate:** `QALD9PLUS_CONTROLLED_ACQUISITION_PASS_VALIDATED`

Payload QALD EN/DBpedia adquirido y validado en workdir únicamente. Test SEALED. Sin grafos, SPARQL, adapters ni benchmark. Autorización consumida tras PASS.

---

## Addendum Prompt 22 — LC-QuAD T6C license clarification

**Fecha:** 2026-07-22 · **RUN_ID:** `20260722T112721Z`  
**Gate:** `LCQUAD2_SCOPE_CLARIFIED_ALL_REPRESENTATIONS_HOLD`

Authors source HOLD (LICENSE absent). HF card CC BY 3.0 = platform metadata; no alternativa elegible. Sin payload. T6C cerrado. Siguiente: decisión documental de grafo DBpedia (Prompt 23).


## Estado operativo post-Prompt 23 (2026-07-22)

- Objetivo de grafo para QALD-9 Plus EN/DBpedia: **DBpedia 2016-10 endpoint-equivalent** (primario).
- Common graph rebase: **fallback** etiquetado, no nativo.
- Endpoint público mutable: **rechazado** como primary reproducible.
- Adquisición/despliegue de grafo: **no** ejecutados; G4 runtime **no** satisfecho.
- Siguiente paso documental: cierre de file scope (Prompt 23B) antes de autorización humana de adquisición.

## Estado operativo post-Prompt 23B (2026-07-22)

- Endpoint-equivalent file scope **CLOSED** (114 files, 6925795437 bytes).
- Published MD5 coverage partial (2 LHD); local SHA-256 required post-download.
- Human acquisition authorization pending; deployment remains a separate gate.
- No graph payload acquired; G4 runtime not satisfied.

## Estado operativo post-Prompt 23C (2026-07-22)

- Manifest↔allowlist static consistency verified (114/114, no `//`).
- Human acquisition authorization still required; no payload acquired.

## Prompt 24B — DBpedia compressed acquisition

**Gate:** `DBPEDIA_2016_10_ENDPOINT_EQUIVALENT_COMPRESSED_ACQUISITION_PASS_VALIDATED`  
**Auth:** `AUTH_DBPEDIA2016_10_ACQ_20260722T134313Z_EMO_01` CONSUMED_AFTER_PASS  
**Payload:** workdir only · 114 / 6925795437 · no decompress · no Virtuoso · no SPARQL  
**Next:** `PREPARE_DBPEDIA_2016_10_DEPLOYMENT_RESOURCE_AND_AUTHORIZATION_PACKAGE`

## Prompt 25A — Deployment resource package

**Gate:** `DBPEDIA_DEPLOYMENT_RESOURCE_PACKAGE_READY_FOR_HUMAN_PROFILE_SELECTION`  
**Forms:** resource selection READY_UNSIGNED · execution NOT_READY  
**Runtime:** PINNED_METADATA_ONLY (no pull)  
**Next:** `HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION`
