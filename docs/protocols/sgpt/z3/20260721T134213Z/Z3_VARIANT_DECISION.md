# Z3_VARIANT_DECISION

**RUN_ID:** `20260721T134213Z`  
**Etiqueta:** `PROPOSED_PROTOCOL`

| Campo | Valor |
|---|---|
| dataset | **lcquad2** |
| variant | **QUESTION_ONLY** |
| knowledge | **false** |
| masked | **false** |
| distributed | **false** |
| fp16 | **false** |
| device (primer smoke) | **CPU** |
| purpose | `RESOURCE_CANARY_NATIVE_PATH` |
| scientific_equivalence | `REDUCED_SMOKE_NOT_PAPER_REPRODUCTION` |

## Justificación (`CODE_VERIFIED`)
- LC-QuAD2 Dataset no instancia spaCy al cargar (`dataset_lcquad2.py`); usa JSON procesado presente.
- Evita QALD9 ID reuse documentado.
- Evita `utils.dptree` (spaCy lg + GPT-2 en import).
- Evita knowledge/masked como variables extra.
- Conserva código nativo de modelo y dataset del método.
