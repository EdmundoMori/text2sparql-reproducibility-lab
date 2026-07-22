# LOCAL_STORAGE_AND_LAYOUT_PLAN

**RUN_ID:** `20260722T105246Z` · Destino futuro (workdir, gitignored):

`workdir/datasets/qald9_plus/8eb038a61e1bc09cbd21640aa667a1714f53cda4/`

```
raw/train/qald_9_plus_train_dbpedia.json
sealed_test/qald_9_plus_test_dbpedia.json
legal/LICENSE
legal/CITATION.cff
manifests/acquisition_result.yaml
manifests/file_hashes.sha256
manifests/git_blob_verification.tsv
manifests/schema_summary.json
manifests/test_seal_manifest.yaml
```

## Reglas
- workdir ignorado por Git · raw bytes inmutables · read-only tras validación
- no copiar a upstream · no publicar payloads · no symlinks en upstream
- no almacenar contenido del test en logs versionados
