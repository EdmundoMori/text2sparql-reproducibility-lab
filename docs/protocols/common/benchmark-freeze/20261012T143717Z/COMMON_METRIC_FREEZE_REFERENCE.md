# Common metric freeze reference

**RUN_ID:** `20261012T143717Z`
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION


Prompt18 contract `0.1.0-documentary` is locked by reference:
`configs/common/COMMON_METRIC_REGISTRY.yaml` and
`docs/protocols/common/metrics/20260722T093257Z/`.

Primary metrics are Answer Precision, Answer Recall, Answer F1 and Execution Exact Accuracy. Frozen semantics
include `SET_OF_ROWS`, valid-empty rules, canonicalization, failures scoring zero while remaining in the
denominator, paired bootstrap/Wilson procedures and Holm correction where applicable.

`metric_contract_documentary = satisfied`; `metric_runtime_conformance = pending`;
36 vectors = `DEFINED_NOT_EXECUTED`. No metric implementation or vector execution occurred.
