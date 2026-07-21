# NLTK_RUNTIME_RESOURCE_DECISION

**RUN_ID:** `20260721T113310Z`  
**Pin candidato:** `nltk==3.8.1`  
**Firma meteor (fuente 3.8.1):** `def single_meteor_score(
def meteor_score(`

## Z2_CORE_METRICS (sin corpus externo, fixtures)

- unigram / SP unigram
- BLEU / SP-BLEU (`sentence_bleu`)
- ROUGE local en `utils/metrics.py` (sin nltk corpus)

## Z2_FULL_NLTK_METRICS (requieren recursos)

- `word_tokenize` → **punkt** / posiblemente **punkt_tab**
- METEOR (`single_meteor_score`) → **wordnet**, **omw-1.4** (típico)

## Estado Prompt 12B

- Paquete NLTK: pin documental
- Recursos: **no descargados** (`DEFERRED_DOWNLOAD`)
- Z2 inicial: limitar harness a Z2_CORE_METRICS hasta autorización de data NLTK
