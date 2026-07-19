# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-19 (Prompt 4B — environment definition WAVE_A)  
**Fase lab:** 1 — auditoría / reproducibilidad nativa (WAVE_A static+env docs complete; **sin** installs ni ejecución)  
**Commit inicial 4B:** `aa141143e0a4dde5ac1de5dd645b70ecc953704a`

> Instrucción para el planificador: lee este archivo primero. Usa los documentos específicos enlazados para detalle. **No asumas reproducción experimental**: clonar ≠ ejecutar ≠ reproducir un paper. Propón el siguiente prompt adaptado a evidencias, limitaciones de máquina y gates científicos.

---

## 1. Objetivo del laboratorio (recordatorio)

Laboratorio local Text-to-SPARQL: auditar y, cuando sea posible, reproducir métodos publicados; luego evaluarlos bajo protocolo común (QALD-9 Plus EN/DBpedia → LC-QuAD 2.0); a largo plazo, adaptar a KG de descubrimiento de modelos de IA y diseñar un método nuevo con ablaciones.

Documentos rectores del lab (no sustituyen este sync):

| Documento | Ruta |
|---|---|
| Contexto operativo | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) |
| Protocolo científico | [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) |
| Perfil de máquina | [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| Registro de métodos | [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) |
| Pins de clones | [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) |

---

## 2. Bucle Cursor ↔ ChatGPT

```text
ChatGPT (plan prompts)
    → investigador ejecuta prompt en Cursor
        → Cursor actualiza PLAN_SYNC + docs específicos + push GitHub
            → ChatGPT relee repo y adapta el siguiente prompt
```

Reglas del bucle:

1. Tras cada prompt ejecutado, Cursor actualiza **este** archivo (§3–§7) y, si hace falta, docs específicos.  
2. Cursor registra rutas de docs específicos en [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md).  
3. Se hace **commit + push** al repo GitHub (sin `upstream/`, sin secretos, sin datasets/modelos pesados).  
4. ChatGPT debe proponer el **siguiente prompt concreto**, no reescribir todo el plan desde cero salvo bloqueo metodológico.  
5. Respetar `PROJECT_CONTEXT.md` §7: advertencia → solución → continuar ante límites de máquina.

---

## 3. Qué se ha completado (prompts ejecutados)

| # | Prompt / acción | Resultado clave | Docs específicos |
|---|---|---|---|
| 0 | Fundación | `PROJECT_CONTEXT.md`, `RESEARCH_PROTOCOL.md` | mismos |
| 1 | Workspace | Árbol de dirs, Makefile, registries, `.env.example` | [`README.md`](README.md), [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| 1b | Límites de máquina en contexto | Protocolo advertir→mitigar→continuar | [`docs/decisions/001_machine_limits_warn_and_continue.md`](docs/decisions/001_machine_limits_warn_and_continue.md) |
| 2 | Paper/código/evidencia | 7 candidatos auditados; inclusión decidida | [`audit/PAPER_CODE_MAPPING.md`](audit/PAPER_CODE_MAPPING.md), [`audit/INITIAL_AUDIT_MATRIX.csv`](audit/INITIAL_AUDIT_MATRIX.csv), [`audit/INCLUSION_DECISIONS.md`](audit/INCLUSION_DECISIONS.md), [`audit/RESOURCE_ESTIMATION.md`](audit/RESOURCE_ESTIMATION.md) |
| 2b | Cierre evidencias | Licencias, venue SPARQL-LLM, Table 4 SGPT | [`audit/EVIDENCE_CLOSURE.md`](audit/EVIDENCE_CLOSURE.md), [`audit/LICENSE_MATRIX.csv`](audit/LICENSE_MATRIX.csv), [`audit/RESULT_EVIDENCE_MATRIX.csv`](audit/RESULT_EVIDENCE_MATRIX.csv), [`audit/PUBLICATION_STATUS.csv`](audit/PUBLICATION_STATUS.csv) |
| 3 | Clonado estático | 7 clones; tebaqa excluido; ondas A–D | [`audit/CLONING_REPORT.md`](audit/CLONING_REPORT.md), [`scripts/clone_repositories.sh`](scripts/clone_repositories.sh) |
| Sync | Este mecanismo | `PLAN_SYNC.md` + índice para el planificador | [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md), [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md) |
| Sync-full | Vendor `upstream/` en GitHub | Árboles de código clonados versionados (~1.2 GiB); `.git` anidados → `.git_local/` local | [`docs/decisions/002_vendor_upstream_on_github.md`](docs/decisions/002_vendor_upstream_on_github.md), `upstream/<method_id>/` |
| 4A | Auditoría estática WAVE_A | Fichas + matriz + readiness; pins verificados; sin install/ejecución | [`audit/sparql_llm/STATIC_AUDIT.md`](audit/sparql_llm/STATIC_AUDIT.md), [`audit/mkgqagent/STATIC_AUDIT.md`](audit/mkgqagent/STATIC_AUDIT.md), [`audit/rdfconfig_llm/STATIC_AUDIT.md`](audit/rdfconfig_llm/STATIC_AUDIT.md), [`audit/rdfconfig_llm/COMPANION_RDF_CONFIG_AUDIT.md`](audit/rdfconfig_llm/COMPANION_RDF_CONFIG_AUDIT.md), [`audit/WAVE_A_STATIC_AUDIT_MATRIX.csv`](audit/WAVE_A_STATIC_AUDIT_MATRIX.csv), [`audit/WAVE_A_EXECUTION_READINESS.md`](audit/WAVE_A_EXECUTION_READINESS.md) |
| 4B | Definición documental entornos WAVE_A | Specs `environments/*`; matriz+gaps; Ruby/Bundler ABSENT; primer micro-smoke = sparql CORE_OFFLINE | [`environments/README.md`](environments/README.md), [`environments/EXECUTION_WORKSPACE_POLICY.md`](environments/EXECUTION_WORKSPACE_POLICY.md), [`environments/sparql_llm/`](environments/sparql_llm/), [`environments/mkgqagent/`](environments/mkgqagent/), [`environments/rdfconfig_llm/`](environments/rdfconfig_llm/), [`audit/WAVE_A_ENVIRONMENT_DEFINITION_MATRIX.csv`](audit/WAVE_A_ENVIRONMENT_DEFINITION_MATRIX.csv), [`audit/WAVE_A_ENVIRONMENT_GAPS.md`](audit/WAVE_A_ENVIRONMENT_GAPS.md) |

---

## 4. Hallazgos críticos para adaptar el plan

### 4.1 Máquina (condiciona ejecución)

- Windows + **WSL2** Ubuntu 22.04; RAM WSL ≈ **7.4 GiB**; host ≈ 16 GiB.  
- GPU: RTX 4050 ≈ **6 GiB** VRAM; `nvcc` ausente; Docker OK; **Compose plugin ausente**.  
- Sin Conda/uv; Poetry sí; solo `python3`.  
- **Ruby/Bundler ABSENT** (re-check 4B). Compose plugin ABSENT.  
- Clases útiles: `feasible_using_api`, `feasible_local_gpu` (ligero), `requires_external_gpu`.

→ WAVE_A **static + env definition** hechas. Siguiente: **Prompt 5A sparql_llm CORE_OFFLINE** (install+import smoke).

### 4.2 Inclusión de métodos

| Decisión | Métodos |
|---|---|
| INCLUDE_PRIMARY | `sparql_llm`, `mkgqagent`, `sgpt` |
| INCLUDE_CONDITIONAL | `cot_sparql`, `firesparql`, `rdfconfig_llm` |
| HISTORICAL_ONLY (no clonado) | `tebaqa` |

### 4.3 Ondas post-clon

| Wave | Métodos | Implicación para el plan |
|---|---|---|
| WAVE_A | sparql_llm, mkgqagent, rdfconfig_llm | **Static audit complete**; env definition / smokes siguientes |
| WAVE_B | sgpt | Local condicional (train/eval); no aún |
| WAVE_C | cot_sparql, firesparql | Solo auditoría estática por ahora |
| WAVE_D | tebaqa | Excluido del clon actual |

### 4.3b Hallazgos estáticos WAVE_A (Prompt 4A)

- **sparql_llm (MIT):** paquete + MCP + agent + benchmarks; Compose documentado pero **ausente en host**; sin `uv`/`uvx`; smoke offline validate/loaders viable tras install.
- **mkgqagent (LICENSE_NOT_CONFIRMED):** FastAPI + LangGraph plan→EL→feedback **CODE_VERIFIED**; experience pool **prebuilt**; script offline **NOT_FOUND**; hosts IP hardcodeados; e5-large CPU riesgo RAM.
- **rdfconfig_llm (LICENSE_NOT_CONFIRMED HEAD):** LLM elige variables → **Ruby rdf-config** construye SPARQL (**frontera clara**); `requirements.txt` incompleto vs Jaccard; muta `sparql.yaml` al correr; companion MIT **no** licencia el generator.
- Todos siguen `reproduction_status: audit_only`; `native_audit_complete: false`; `common_adapter_allowed: false`.

### 4.4 Bloqueos legales / publicación

- **LICENSE_NOT_CONFIRMED** (clon OK, **no** adaptar/integrar aún): mkgqagent, cot_sparql, firesparql, scott2121 generator.  
- SPARQL-LLM: preprint **Under Review** (arXiv); DOI TWEB **no verificado**.  
- Código público ≠ reutilizable confirmado.

### 4.5 Anomalías de clon

- `firesparql` ~598M (mucho `results/` en Git).  
- `sgpt` ~169 MiB datasets en árbol.  
- Tag mkgqagent tipográfico: `TEXT2SPAQL`.  
- Submódulos: ninguno.

### 4.6 Hallazgos Prompt 4B (entornos)

- Specs documentales listas; **nada instalado**.  
- Primer micro-smoke: **sparql_llm CORE_OFFLINE**.  
- Text2SPARQL+Virtuoso: **BLOCKED_ON_LOCAL_HOST**.  
- mkgq: `native_reproduction_ready: not_ready_or_weak`; offline smoke NOT_READY.  
- rdfconfig: Ruby ABSENT; never in-place `sparql.yaml`; Zenodo preferido para fidelidad.

### 4.7 Lo que NO se ha hecho

- Instalación de dependencias / venvs.  
- Smokes, pipelines, train, eval.  
- Adaptadores comunes.  
- Descarga Zenodo/HF/Docker images.  
- Declarar `reproduced` / `smoke_only`.  
- Auditoría estática WAVE_B/C.

---

## 5. Estado de reproducción (protocolo)

WAVE_A: `audit_only` + static_audit_complete + **environment_definition ready_documented**.  
**Ninguno** en `reproduced` / `partially_reproduced` / `smoke_only`.

---

## 6. Recomendación al planificador (siguiente prompt)

1. **Prompt 5A — sparql_llm CORE_OFFLINE** install + import/validate → `smoke_only` si OK.  
2. No Virtuoso; no mkgq/rdfconfig aún; no adapters.  
3. GO/NO-GO en [`audit/WAVE_A_ENVIRONMENT_GAPS.md`](audit/WAVE_A_ENVIRONMENT_GAPS.md).

Detalle: [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md).

---

## 7. Índice rápido de artefactos específicos

Ver lista completa y estable en:

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog de este archivo

| Fecha | Cambio |
|---|---|
| 2026-07-19 | Creación del mecanismo PLAN_SYNC + primer volcado de estado post-clon |
| 2026-07-19 | Push completo: `upstream/` vendorizado en GitHub (decisión 002); el planificador puede leer código clonado |
| 2026-07-19 | Prompt 4A: auditoría estática WAVE_A completa; readiness + matriz; siguiente=env definition |
| 2026-07-19 | Addenda estáticas sparql_llm/mkgqagent (Virtuoso no viable; pool≠trazas paper; doble e5) |
| 2026-07-19 | Prompt 4B: environments/* + matriz/gaps; Ruby ABSENT; next=5A CORE_OFFLINE |

---

## 9. Registro de publicación

### 4A (histórico)
| Campo | Valor |
|---|---|
| commit artefactos | `97e86cee` |
| HEAD con addenda | `aa141143` |
| artefactos | §3 fila 4A |

### 4B (este prompt)
| Campo | Valor |
|---|---|
| commit inicial | `aa141143e0a4dde5ac1de5dd645b70ecc953704a` |
| commit final | *(tras push)* |
| rama | `main` |
| mensaje | Document WAVE_A environment specs without installing or running methods. |
| push | pendiente |
| artefactos | §3 fila 4B |

