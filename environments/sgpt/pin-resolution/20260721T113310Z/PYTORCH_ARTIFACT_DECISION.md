# PYTORCH_ARTIFACT_DECISION

**RUN_ID:** `20260721T113310Z`  
**Upstream declared:** `torch==1.13.1` (`CODE_VERIFIED`)

## Distinciones

| Artefacto | Fuente | Uso |
|---|---|---|
| `torch==1.13.1` (PyPI manylinux1 x86_64 cp38) | pypi.org | build tipicamente **CUDA**/grande (~887 MB) — no ideal Z2 CPU |
| `torch==1.13.1+cpu` linux cp38 | download.pytorch.org/whl/cpu | **candidato Z2 CPU** |

## Selección Z2

| Campo | Valor |
|---|---|
| Spec candidata | `torch==1.13.1+cpu` |
| Filename | `torch-1.13.1+cpu-cp38-cp38-linux_x86_64.whl` |
| SHA-256 (índice oficial) | `4a8b84834eb12b3428c24e9f264c9bd6a2cf449fffc191374e7dbb2b950fc6d7` |
| Etiqueta | `PROPOSED_Z2_CPU_BUILD_VARIANT` |
| Index | `https://download.pytorch.org/whl/cpu` |
| Descarga en 12B | **no** |

No afirmar que `+cpu` sea el artefacto exacto del paper.

## PyPI cp38 manylinux1 (referencia)

- filename: `torch-1.13.1-cp38-cp38-manylinux1_x86_64.whl`
- sha256: `727dbf00e2cf858052364c0e2a496684b9cb5aa01dc8a8bc8bbb7c54502bdcdd`
- size: 887409458

**Estado:** `WHEEL_METADATA_VERIFIED` (metadata/index only)
