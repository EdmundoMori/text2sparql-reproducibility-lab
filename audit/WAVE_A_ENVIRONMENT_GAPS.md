# WAVE_A_ENVIRONMENT_GAPS

**Fecha:** 2026-07-19 · Prompt 4B

## Gaps que impiden instalar (ahora)

| Gap | Impacto |
|---|---|
| Ninguno crítico para **sparql_llm CORE_OFFLINE** | pip/Poetry + Python 3.10 presentes |
| Ruby/Bundler **ABSENT** | Bloquea rdfconfig generator + companion CLI |
| Compose plugin **ABSENT** | Bloquea stacks documentados con `docker compose` |
| `uv` **ABSENT** | README/Dockerfile sparql asumen uv |

## Gaps que permiten instalar pero no reproducir

| Gap | Métodos |
|---|---|
| Pins LOWER_BOUND/UNPINNED → resolución no determinista | sparql agent extra; mkgq |
| MISSING_UPSTREAM deps | mkgq `requests`; rdfconfig Jaccard stack |
| Pool/ICL ≠ trazas offline paper; sin builder | mkgq |
| Mutación `sparql.yaml`; dual rdf-config trees | rdfconfig |
| Virtuoso+dumps | sparql Text2SPARQL |

## Gaps legales

| Método | Gate |
|---|---|
| mkgqagent | LICENSE_NOT_CONFIRMED — no adapters |
| rdfconfig generator HEAD | LICENSE_NOT_CONFIRMED — preferir Zenodo CC-BY tras verify |
| sparql_llm / companion | MIT — adapters aún `common_adapter_allowed: false` por protocolo |

## Gaps datos/modelos

- e5-large download (mkgq / sparql agent).  
- Dumps Virtuoso / questions YAML oficiales Text2SPARQL.  
- Zenodo archive aún no descargado.

## Gaps endpoints

- WSE IPs hardcode (mkgq).  
- Falcon / LangChain Hub / OpenAI.  
- Endpoints biodata (rdfconfig) — no probados (prohibido en 4B).

## Gaps hardware

- RAM WSL 7.4 GiB: doble agente mkgq; e5; Virtuoso bloqueado.  
- VRAM no necesaria para CORE_OFFLINE / API LLMs remotos.

---

## Decisión: primer método a instalar

**`sparql_llm` scope `CORE_OFFLINE`** — salvo nueva evidencia.

### Por qué

1. Licencia MIT confirmada.  
2. No requiere API, Ruby, Compose ni Qdrant para import/validate.  
3. Static audit + env spec completos.  
4. Señal `CODE_VERIFIED` ejecutable con menor riesgo.  
5. No escribe en upstream si solo import/validate.  
6. Desbloquea confianza en tooling del lab antes de smokes API/legally blocked.

### GO/NO-GO

| Smoke | GO si… | NO-GO si… |
|---|---|---|
| sparql CORE_OFFLINE | venv+pip/Poetry OK; sin red obligatoria | Se pide Virtuoso/Compose como “smoke” |
| sparql MCP/API | CORE_OFFLINE OK; key; 1 worker; RAM | OOM; usar 6 workers |
| mkgq API | Legal acceptance; key; **single-agent path** resuelto sin adapters ilegales | Doble e5 inevitable sin patch y RAM insuficiente |
| rdfconfig | Ruby/Bundler instalados; workdir; MISSING deps; no upstream writes | Ruby ABSENT; run in-place |
| Virtuoso Text2SPARQL | — | **Siempre NO-GO en este host** |
