# Salud estática del código — CoT-SPARQL

**Fecha:** 2026-07-20  
**Pin:** `063edd9868425e54010a0cb49ce585ed2186be4d`  
**Fuente AST:** `logs/static-audit-cot-sparql/ast_health.json`  
**Etiquetas:** `CODE_VERIFIED` | `INFERENCE` | `UNKNOWN`

---

## Parse AST

| Archivo | Líneas | Parse OK | Asserts (líneas) |
|---|---|---|---|
| `main.py` | 109 | sí | 104, 105, 106 |
| `contexta.py` | 107 | sí | — |
| `contextb.py` | 50 | sí | — |
| `validation.py` | 70 | sí | — |
| `spacy_component.py` | 264 | sí | 111 |

Todos los módulos Python del path crítico **parsean** (`CODE_VERIFIED`). No se ejecutó import runtime.

---

## Anomalías sintácticas / lógicas detectadas estáticamente

### 1. Assert de pregunta vacía roto (`main.py` L106) — BUG `CODE_VERIFIED`

```python
assert args.question != "" "Please provide a natural language (en) question"
```

Falta la coma entre expresión y mensaje. En Python, literales de cadena adyacentes se concatenan → la condición efectiva es:

`args.question != "Please provide a natural language (en) question"`

Una pregunta **vacía** (`""`) **pasa** el assert. Anomalía crítica de validación CLI.

### 2. Typo en assert KB (`main.py` L105)

`"Please provde the targeted Knowledge base"` — typo `provde` (`CODE_VERIFIED`). El assert de `kb` sí tiene coma correcta.

### 3. Imports / ruido

| Hallazgo | Ubicación | Nota |
|---|---|---|
| `warnings.filterwarnings("ignore")` | `main.py` L12 | oculta avisos runtime |
| `Accelerator` importado y **no usado** | `main.py` L3 | dead import |
| `SentenceTransformer(...)` a nivel módulo | `contextb.py` L9 | side-effect: descarga/carga HF al **importar** `contextb` |
| `import contexta as ca` en `contextb.py` | L7 | import circular potencial / no usado en body (`INFERENCE` uso) |

### 4. Path de generación

- `num_return_sequences` default **1**; si inválido, imprime “try again” **sin** reintento automático ni ranking (`main.py` L96–100) (`CODE_VERIFIED`).
- `--top_k` alimenta **sampling** del pipeline, **no** top-k de retrieval (`main.py` L86 vs `contextb` `np.argmax`) (`CODE_VERIFIED`).

### 5. Linking / validación (resumen)

Ver `CODE_ANOMALIES_AND_RISKS.md`, `GROUNDING_AND_LINKING_AUDIT.md`, `VALIDATION_AND_EXECUTION_AUDIT.md` (Falcon `None`, mismatch `propertyLabel`, validación HTTP≠parse local).

---

## Conclusión salud

El código es **sintácticamente válido** a nivel AST, pero contiene **bugs de asserts**, **side-effects de import**, **dependencias de red no acotadas** y **ausencia de harness eval**. No apto para smoke end-to-end en este host sin artefactos externos y GPU mayor.
