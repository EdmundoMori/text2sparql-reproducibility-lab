# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-20 (Prompt 6 — SGPT WAVE_B static audit → **audit_only** sin ejecución)  
**Fase lab:** 1 — native audit; `sparql_llm` = **smoke_only**; `sgpt` = **audit_only** (static complete)  
**Commit inicial 6:** `b0e5fdaa0902481d1c782bc28a44e588a035facd`

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

Ciclo operativo (repetir hasta cerrar la fase):

```text
ChatGPT entrega UN prompt
  → Cursor lo ejecuta
    → Cursor actualiza docs (PLAN_SYNC + específicos) + commit + push
      → ChatGPT relee GitHub, valida el plan y entrega el siguiente prompt
```

Detalle: [`docs/plan-sync/PLANNER_LOOP.md`](docs/plan-sync/PLANNER_LOOP.md).

Reglas del bucle:

1. Tras cada prompt ejecutado, Cursor actualiza **este** archivo (§3–§7) y, si hace falta, docs específicos.  
2. Cursor registra rutas en [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md).  
3. **Commit + push** a GitHub (sin secretos; `upstream/` ya vendorizado; sin caches/modelos nuevos pesados innecesarios).  
4. ChatGPT propone el **siguiente prompt concreto** (prioridad 1), no reescribe todo el plan salvo bloqueo grave.  
5. Respetar `PROJECT_CONTEXT.md` §7: advertencia → solución → continuar.  
6. El investigador usa un **meta-prompt de replanificación** fijo tras cada push (ver `PLANNER_LOOP.md` / respuesta del agente).

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
| 5A | sparql_llm CORE_OFFLINE host Py3.10 | **setup_failed** (conservado): install OK; import FAIL `typing.Required` | [`audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_SMOKE_REPORT.md), [`experiments/native/sparql_llm/20260719T112306Z/`](experiments/native/sparql_llm/20260719T112306Z/) |
| 5B | sparql_llm CORE_OFFLINE Docker Py3.11 | **smoke_only**: digest `python@sha256:b18992999…`; VoID+validate OK; harness lab fix | [`audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md`](audit/sparql_llm/CORE_OFFLINE_PY311_SMOKE_REPORT.md), [`experiments/native/sparql_llm/20260720T134943Z/`](experiments/native/sparql_llm/20260720T134943Z/), [`environments/sparql_llm/Dockerfile.core-offline-py311`](environments/sparql_llm/Dockerfile.core-offline-py311) |
| 6 | SGPT WAVE_B static audit | **audit_only** (sin install/train); arquitectura/variants/datasets/métricas/readiness; ckpt ausente | [`audit/sgpt/STATIC_AUDIT.md`](audit/sgpt/STATIC_AUDIT.md), [`audit/WAVE_B_STATIC_AUDIT_MATRIX.csv`](audit/WAVE_B_STATIC_AUDIT_MATRIX.csv), [`audit/sgpt/`](audit/sgpt/) |

---

## 4. Hallazgos críticos para adaptar el plan

### 4.1 Máquina (condiciona ejecución)

- Windows + **WSL2** Ubuntu 22.04; RAM WSL ≈ **7.4 GiB**; host ≈ 16 GiB.  
- GPU: RTX 4050 ≈ **6 GiB** VRAM; `nvcc` ausente; Docker OK; **Compose plugin ausente**.  
- Sin Conda/uv; Poetry sí; solo `python3` 3.10.12.  
- **Ruby/Bundler ABSENT**. Compose plugin ABSENT.  
- Clases útiles: `feasible_using_api`, `feasible_local_gpu` (ligero), `requires_external_gpu`.

→ Tras 5B smoke_only y 6 static SGPT: siguiente = **WAVE_C static** (CoT-SPARQL + FIRESPARQL). No entrenar SGPT aún.

### 4.2 Inclusión de métodos

| Decisión | Métodos |
|---|---|
| INCLUDE_PRIMARY | `sparql_llm`, `mkgqagent`, `sgpt` |
| INCLUDE_CONDITIONAL | `cot_sparql`, `firesparql`, `rdfconfig_llm` |
| HISTORICAL_ONLY (no clonado) | `tebaqa` |

### 4.3 Ondas post-clon

| Wave | Métodos | Implicación para el plan |
|---|---|---|
| WAVE_A | sparql_llm, mkgqagent, rdfconfig_llm | Static + env definition; sparql CORE_OFFLINE smoke_only |
| WAVE_B | sgpt | **Static audit complete**; train/eval diferidos |
| WAVE_C | cot_sparql, firesparql | Siguiente: solo auditoría estática |
| WAVE_D | tebaqa | Excluido del clon actual |

### 4.3b Hallazgos Prompt 6 (SGPT)

- Pin `1f6964d1…` + MIT verificados; upstream intacto.  
- Checkpoints / `runs/` / pesos: **NOT_FOUND**.  
- Datasets procesados presentes: lcquad2 21497/2389/**5969** (paper ~6046 mismatch); qald9 350/58/150; vquanda 3500/500/1000.  
- **qald9:** train∩test = 150 IDs reutilizados (contenido no idéntico).  
- **SGPT_Q** ≈ sin `--knowledge`; **SGPT_Q_K** ≈ `--knowledge` (solo entidades; LC-QuAD: QIDs de `new_LabelsEnt` filtrados por gold SPARQL). `--masked` ortogonal (solo entidades en código).  
- Métricas Table 4 = léxicas; **no** Answer F1 / ejecución SPARQL; anomalía double-`update` en `eval.py`.  
- Epochs README 40 vs `params.json` 70; LR 6.25e-5; seed 42.  
- Native reproduction: **not_ready** (ckpt + VRAM 6 GiB vs paper 2×12 GB).  
- `reproduction_status: audit_only`; `native_audit_complete: false`; `common_adapter_allowed: false`.

### 4.4 Bloqueos legales / publicación

- **LICENSE_NOT_CONFIRMED** (clon OK, **no** adaptar/integrar aún): mkgqagent, cot_sparql, firesparql, scott2121 generator.  
- SPARQL-LLM: preprint **Under Review** (arXiv); DOI TWEB **no verificado**.  
- Código público ≠ reutilizable confirmado.

### 4.5 Anomalías de clon

- `firesparql` ~598M (mucho `results/` en Git).  
- `sgpt` ~218 MiB datasets en árbol.  
- Tag mkgqagent tipográfico: `TEXT2SPAQL`.  
- Submódulos: ninguno.

### 4.6 Hallazgos Prompt 4B–5B (entornos / smoke)

- Specs documentales WAVE_A listas.  
- **Instalaciones aisladas realizadas:** 5A (host venv/tmp) y 5B (Docker build + pip en imagen).  
- 5A: install OK, import FAIL en Py3.10.  
- 5B: Docker `python@sha256:b18992999…`, smoke_only; harness lab fix; `--read-only` no viable.  
- Text2SPARQL+Virtuoso: **BLOCKED_ON_LOCAL_HOST**.  
- mkgq/rdfconfig: blockers legales/Ruby sin resolver.

### 4.7 Lo que NO se ha hecho

- Smoke API/MCP/agent de sparql_llm.  
- Install / train / eval de SGPT.  
- Pipelines paper, train, eval científica (salvo smoke CORE_OFFLINE sparql).  
- Adaptadores comunes.  
- Auditoría estática WAVE_C.  
- Declarar `reproduced` / `partially_reproduced`.  
- Instalar Python 3.11 en WSL (evitar; usar contenedor).

---

## 5. Estado de reproducción (protocolo)

- `sparql_llm`: **smoke_only** (5B Docker Py3.11 CORE_OFFLINE); 5A histórico **setup_failed**; `native_audit_complete: false`; `common_adapter_allowed: false`.  
- `sgpt`: **audit_only** (WAVE_B static complete); sin ejecución; ckpt ausente; `native_audit_complete: false`; `common_adapter_allowed: false`.  
- Resto: `audit_only`.  
- **Ninguno** `reproduced` / `partially_reproduced`.

---

## 6. Recomendación al planificador (siguiente prompt)

1. **Prompt 7 — Auditoría estática WAVE_C (CoT-SPARQL + FIRESPARQL)** (prioridad).  
2. No entrenar SGPT ni descargar GPT-2/spaCy ahora.  
3. Diferir API/MCP sparql, mkgq, rdfconfig, Virtuoso, adapters.  
4. Objetivo largo plazo: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

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
| 2026-07-19 | Documentado ciclo operativo Cursor↔ChatGPT (`PLANNER_LOOP.md`); meta-prompt de replanificación |
| 2026-07-19 | Prompt 5A: sparql CORE_OFFLINE setup_failed (Py3.10/typing.Required); next=5B python3.11 |
| 2026-07-20 | Prompt 5B: Docker Py3.11 CORE_OFFLINE smoke_only; next=SGPT WAVE_B static audit |
| 2026-07-20 | Prompt 6: SGPT WAVE_B static audit complete (audit_only); next=WAVE_C |

---

## 9. Registro de publicación

### 5A (histórico)
| Campo | Valor |
|---|---|
| RUN_ID | `20260719T112306Z` |
| resultado | **setup_failed** |
| push | confirmado (`35ea955e` / `6ca23b10`) |

### 5B (histórico)
| Campo | Valor |
|---|---|
| RUN_ID | `20260720T134943Z` |
| resultado | **smoke_only** |
| base digest | `python@sha256:b18992999dbe963a45a8a4da40ac2b1975be1a776d939d098c647482bcad5cba` |
| commit final (push confirm) | `b0e5fdaa0902481d1c782bc28a44e588a035facd` |

### 6 (este prompt)
| Campo | Valor |
|---|---|
| alcance | SGPT WAVE_B static audit |
| commit inicial | `b0e5fdaa0902481d1c782bc28a44e588a035facd` |
| resultado | **audit_only** (static complete; no execution) |
| commit final | *(tras push)* |
| rama | `main` |
| push | pendiente |
| artefactos | `audit/sgpt/*`, `audit/WAVE_B_STATIC_AUDIT_MATRIX.csv` |
