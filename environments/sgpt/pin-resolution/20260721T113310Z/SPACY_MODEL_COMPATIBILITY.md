# SPACY_MODEL_COMPATIBILITY

**RUN_ID:** `20260721T113310Z`  
**spaCy candidato (perfil A):** `3.4.4` (`OFFICIAL_METADATA_VERIFIED`)

## Modelos

| Modelo | Uso en código | Z2 |
|---|---|---|
| `en_core_web_sm` | `scripts/dataset_qald9.py` → `spacy.load("en_core_web_sm")` al instanciar BaseDataset | **no** instanciar BaseDataset QALD9 en Z2 |
| `en_core_web_lg` | `utils/dptree.py` load **en import time** | **DENY** import `utils.dptree` |

## Licencias

spaCy / spacy-models: MIT (metadata pública típica) — confirmar en descarga futura.

## Estado

- Modelos: `DEFERRED_DOWNLOAD` / `not_downloaded`
- Z2: spaCy package **excluido** del constraints Z2 porque el scope deniega módulos que lo requieren
