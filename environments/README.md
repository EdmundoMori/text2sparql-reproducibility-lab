# environments/ — Definición documental de entornos

**Estado:** documentado, **no** resuelto/instalado (Prompt 4B, 2026-07-19).  
**Alcance actual:** WAVE_A (`sparql_llm`, `mkgqagent`, `rdfconfig_llm`).

## native_fidelity_environment vs smoke_environment

| Tipo | Objetivo | Criterio de éxito |
|---|---|---|
| `native_fidelity_environment` | Acercarse a la configuración publicada (paper/README/release) | Métricas/protocolo/datos/modelo **comparables** al artículo |
| `smoke_environment` | Verificar install/import o **una** consulta mínima en esta laptop | Señal de vida; **nunca** implica reproducción |

## documentado vs resuelto/instalado

| Estado | Significado |
|---|---|
| **documentado** | Specs en este directorio (deps, env names, comandos futuros) |
| **resuelto/instalado** | venv/bundle/Docker creados y verificados en un prompt posterior |

Hasta un prompt de install explícito, todo permanece **documentado**.

## Reglas

1. **`upstream/` inmutable** — no editar código ni configs de método en el árbol vendorizado.  
2. **Un entorno aislado por método** — venv/Poetry env separado; no mezclar deps.  
3. **Gestor preferente en este host:** `python3 -m venv` + `pip`, o **Poetry** (presente). **No** asumir Conda/`uv`/`uvx` (ausentes).  
4. **No inferir versiones** no fijadas en upstream.  
5. **Secretos:** solo nombres de variables; valores en `.env` local (gitignored).  
6. **Comandos futuros** se registran en `future_commands.md`; no se ejecutan aquí.  
7. **Un proceso pesado / un agente a la vez** (RAM WSL ≈7.4 GiB).  
8. **No usar test set** para elegir prompts/HPs.  
9. **`smoke_only`** solo tras ejecución documentada.  
10. **Native reproduction** exige protocolo + datos + modelo + métricas comparables al paper.

## Calidad de pins (`dependency_pin_quality`)

| Valor | Significado |
|---|---|
| `EXACT_PIN` | Versión exacta (`==` / lock) |
| `LOWER_BOUND` | Solo cota inferior (`>=`) |
| `UNPINNED` | Sin versión en el manifiesto |
| `UNKNOWN` | No se pudo determinar sin resolver |
| `MISSING_UPSTREAM` | Usada en código/docs pero **ausente** del manifiesto |

## Política de workspace

Ver [`EXECUTION_WORKSPACE_POLICY.md`](EXECUTION_WORKSPACE_POLICY.md).

## Índice WAVE_A

| Método | Spec |
|---|---|
| sparql_llm | [`sparql_llm/`](sparql_llm/) |
| mkgqagent | [`mkgqagent/`](mkgqagent/) |
| rdfconfig_llm | [`rdfconfig_llm/`](rdfconfig_llm/) |
