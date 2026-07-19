# PROJECT_CONTEXT

**Proyecto:** `text2sparql-reproducibility-lab`  
**Dominio:** Text-to-SPARQL / Knowledge Graph Question Answering (KGQA)  
**Inicio documental:** 2026-07-18  
**Fase activa:** Fase 1 — Auditoría y reproducibilidad nativa  
**Estado:** Clonado estático de INCLUDE_PRIMARY/CONDITIONAL completado (`audit/CLONING_REPORT.md`). Sin instalaciones ni entrenamientos.  
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

1. ChatGPT propone un prompt.  
2. Cursor lo ejecuta y documenta hallazgos en `PLAN_SYNC.md` + docs específicos.  
3. Se publica en https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
4. ChatGPT relee el repo y adapta el siguiente prompt.

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
| Clones en `upstream/` | 7 paths (6 métodos); tebaqa no clonado; **no** se versionan en Git |
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
