# Selección de fuente — rdfconfig_llm (decisión futura, no ejecutada)

| # | Fuente | Licencia | Uso propuesto | Notas |
|---|---|---|---|---|
| 1 | GitHub HEAD generator `fe63171d…` | `LICENSE_NOT_CONFIRMED` | Auditado; smoke investigación interna aislada | No adapters / no redistribución |
| 2 | Zenodo v1.0.0 (DOI ya en registry) | Metadata **CC-BY-4.0** | **Preferente** para intento de fidelidad/reutilización cuando se descargue y verifique | **No descargar en 4B** |
| 3 | rdf-config **incluido** en generator (`upstream/rdfconfig_llm/rdf-config/`) | MIT típico dbcls (árbol) | Candidato **fidelidad nativa** (SETUP.md lo usa) | Puede divergir del companion pin |
| 4 | Companion lab `upstream/rdfconfig_llm_rdf-config` @ `cccc581c…` | **MIT** | Smoke **independiente** del CLI Ruby | **No** sustituye automáticamente la copia del paper |

## Decisiones futuras propuestas (no ejecutar ahora)

1. **native paper attempt:** usar artefacto/release del artículo (preferir Zenodo verificado) + su rdf-config correspondiente; checksums; workspace descartable.  
2. **independent companion smoke:** `upstream/rdfconfig_llm_rdf-config` pin MIT — listar queries CLI tras instalar Ruby/Bundler.  
3. **Nunca** ejecutar generator in-place (muta `sparql.yaml`).

## Host

Ruby/Bundler **ABSENT** → tanto (1–3 generator path) como companion CLI quedan **bloqueados** hasta install de runtime en un prompt explícito (no 4B, no micro-smoke sparql).
