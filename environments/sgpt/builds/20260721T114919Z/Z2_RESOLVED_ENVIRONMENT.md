# Z2_RESOLVED_ENVIRONMENT — congelación documental (Prompt 13B)

**RUN_ID:** `20260721T114919Z`  
**Freeze artifact:** `z2-resolved-freeze.txt`  
**SHA-256:** `916d4b76a980ed1b558eb3bb26122f5e6dca9e02ffaeb5ee8e553f7cd66e71a5`  
**Evidence:** `FREEZE_VERIFIED` (copia normalizada ordenada del freeze ya versionado en 13A; **sin** re-ejecutar `pip freeze`)

---

## A. DIRECT_PINS_HISTORICALLY_ANCHORED

Anclados en resolución 12B + verificación runtime 13A:

| Paquete | Versión | Nota |
|---|---|---|
| torch | `1.13.1+cpu` | variante operativa Z2 CPU; `PACKAGE_RUNTIME_VERIFIED` |
| transformers | `4.25.1` | `PACKAGE_RUNTIME_VERIFIED` + símbolos `SYMBOL_IMPORT_VERIFIED` |
| numpy | `1.23.5` | pin directo candidato |
| tqdm | `4.64.1` | pin directo candidato |
| nltk | `3.8.1` | paquete instalado; **sin** recursos/corpus NLTK |
| toolchain | pip/setuptools/wheel | estrictamente necesarios en build; no todos aparecen en freeze de usuario |

## B. TRANSITIVES_RESOLVED_AT_2026_BUILD_TIME

Del freeze resuelto (orden alfabético):

```
certifi==2026.6.17
charset-normalizer==3.4.9
click==8.1.8
filelock==3.16.1
fsspec==2025.3.0
hf-xet==1.5.2
huggingface_hub==0.36.2
idna==3.15
joblib==1.4.2
nltk==3.8.1
numpy==1.23.5
packaging==26.2
PyYAML==6.0.3
regex==2024.11.6
requests==2.32.4
tokenizers==0.13.3
torch==1.13.1+cpu
tqdm==4.64.1
transformers==4.25.1
typing_extensions==4.13.2
urllib3==2.2.3
```

## C. LIMITACIÓN

1. Este freeze **reproduce el entorno Z2 construido en 2026**, no el grafo transitivo original del paper.  
2. `torch==1.13.1+cpu` es una **variante operativa Z2**; **no** debe denominarse *native paper environment*.  
3. No hay lockfile de paper; las transitivas son resolución pip en el momento del build.  
4. No se afirma equivalencia con el entorno de Table 4.
