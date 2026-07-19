# RESOURCE_ESTIMATION

**Fecha:** 2026-07-18  
**Host de referencia:** `MACHINE_PROFILE.md` (WSL2, RAM ≈7.4 GiB, RTX 4050 ≈6 GiB VRAM, Docker sin Compose, sin Conda/uv)  
**Naturaleza:** estimaciones **antes de clonar/ejecutar**. Incertidumbre = `UNKNOWN` o rango amplio.  
**Clases de viabilidad:** ver `MACHINE_PROFILE.md` §4 / `PROJECT_CONTEXT.md` §7.

---

## Escala cualitativa usada

| Nivel | CPU | RAM | GPU | Storage |
|---|---|---|---|---|
| low | ≤2 cores efectivos | ≤2 GiB | no | ≤2 GiB |
| medium | 2–8 cores | 2–8 GiB | ≤6 GiB VRAM inferencia ligera | 2–20 GiB |
| high | ≥8 cores sostenidos | ≥8 GiB (supera WSL actual) | >6 GiB o train multi-GPU | ≥20 GiB |
| unknown | evidencia insuficiente | | | |

---

## Por método

### sparql_llm

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | medium | API + indexing/retrieval |
| RAM | medium → high si vectordb+embeddings entidades | README advierte indexing masivo |
| GPU | optional (indexing embeddings); inferencia LLM vía API | `feasible_using_api` |
| Storage | medium (repo ~23k KB GitHub size; índices UNKNOWN) | |
| API | **requerida** (LLM) + endpoints SPARQL | |
| Viabilidad host | `feasible_using_api` | **ADVERTENCIA [Compose]:** README usa `docker compose` (plugin ausente). **SOLUCIÓN:** instalar plugin o desplegar servicios con `docker`/`podman`. **CONTINÚO:** auditoría documental OK. |

### mkgqagent

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | low–medium | FastAPI + embeddings |
| RAM | medium (`multilingual-e5-large` + FAISS) | vigilar 7.4 GiB |
| GPU | no (API OpenAI; faiss-cpu en requirements) | |
| Storage | low–medium | |
| API | **requerida** (`OPENAI_API_KEY`) | |
| Viabilidad host | `feasible_using_api` | Adecuado para siguiente fase de clon/smoke. |

### cot_sparql

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | high (si LLM local) | |
| RAM | high | modelos GPTQ grandes |
| GPU | **requires_external_gpu** para CodeLlama-34B “tal cual”; cuantizado/más pequeño: UNKNOWN | paper usa CodeLlama-34B-Instruct-GPTQ |
| Storage | medium (embeddings parquet/pkl externos) | |
| API | no obligatoria | alternativa API cambiaría condición experimental |
| Viabilidad host | `requires_external_gpu` o `currently_unknown` tras prueba de modelo ≤6 GB | **ADVERTENCIA [VRAM]:** 34B GPTQ suele exceder 6 GiB. **SOLUCIÓN:** documentar modelo menor o API; no llamar reproducción del paper si cambia el LLM. **CONTINÚO:** INCLUDE_CONDITIONAL. |

### firesparql

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | medium (inferencia) / high (train) | |
| RAM | high en train | |
| GPU | train paper: **1× H100** → `requires_external_gpu` para FT; inferencia 8B LoRA: borderline 6 GiB (`feasible_local_gpu` condicional con cuantización UNKNOWN) | |
| Storage | high (repo size GitHub ~31k; datasets/results) | |
| API | no para núcleo FT | |
| Viabilidad host | inferencia: UNKNOWN hasta medición; train: `requires_external_gpu` | **ADVERTENCIA [GPU/RAM]:** no reproducir train H100 en local. **SOLUCIÓN:** evaluar checkpoint HF en inferencia o API. **CONTINÚO:** INCLUDE_CONDITIONAL SciQA. |

### rdfconfig_llm

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | low | |
| RAM | low | |
| GPU | no | |
| Storage | low–medium (+ clone rdf-config grande ~67k size) | |
| API | **requerida** | + Ruby/bundler para rdf-config |
| Viabilidad host | `feasible_using_api` | Ruby no auditado en MACHINE_PROFILE → presencia Ruby: **UNKNOWN** hasta `ruby -v`. |

### sgpt

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | medium | |
| RAM | medium | |
| GPU | `feasible_local_gpu` (paper: 2 GPUs × 12 GB; GPT-2 117M cabe en 6 GB) | train QALD-9 ~35 min (paper) |
| Storage | medium | |
| API | no | |
| Viabilidad host | `feasible_local_gpu` / `feasible_local_cpu` posible con batch bajo | **ADVERTENCIA [Conda]:** README prioriza conda (ausente). **SOLUCIÓN:** venv+pip según README. **CONTINÚO:** INCLUDE_PRIMARY. |

### tebaqa

| Recurso | Estimación | Notas |
|---|---|---|
| CPU | high (5 servicios JVM + ES + CoreNLP) | |
| RAM | **high** — probable OOM en WSL 7.4 GiB | |
| GPU | no | |
| Storage | **very high** (índices ES DBpedia 2016-10; repo size ~737k KB) | |
| API | no | |
| Viabilidad host | inconveniente / posible `blocked` por RAM | **ADVERTENCIA [RAM/storage]:** stack completo no conviene en WSL actual. **SOLUCIÓN:** subir RAM WSL, usar demo remota, o limitar a análisis de código/HISTORICAL_ONLY. **CONTINÚO:** no priorizar ejecución. |

---

## Priorización sugerida (solo afinado; no es ejecución)

1. `mkgqagent`, `rdfconfig_llm`, `sparql_llm` — API, alineados a Text-to-SPARQL moderno.  
2. `sgpt` — local GPU ligera.  
3. `cot_sparql`, `firesparql` — condicionales por VRAM/KG.  
4. `tebaqa` — histórico / infra pesada.

---

## Qué no se estima aún

- Tiempos wall-clock reales en este host.  
- Coste USD exacto de APIs (salvo cifras **reportadas** en papers).  
- Tamaño on-disk tras clone (solo `size` de GitHub API).  
- Compatibilidad real Docker+GPU WSL para cada imagen.
