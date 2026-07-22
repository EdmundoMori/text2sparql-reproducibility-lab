# Graph deployment resource assessment

**RUN_ID:** `20260722T120239Z`  
Classification: **`CONDITIONAL_HIGH_RISK`** · Tag: `GRAPH_RESOURCE_FEASIBILITY_CONDITIONAL`

## Inputs (MACHINE_PROFILE + Prompt 23 observation)

| Resource | Value |
|---|---|
| WSL RAM | 7.4 GiB |
| Host RAM | ~16 GiB |
| Free disk (`/`) | ~918 GiB |
| Docker daemon | available |
| Docker Compose | absent |

## Payload metadata

| Item | Value |
|---|---|
| Available compressed bytes | **5023159516** (~4.68 GiB) |
| Available files | **81** |
| Unavailable blockers | **33** files |
| Uncompressed / triples | **UNKNOWN** (no official subset totals) |

## Feasibility

- **Disk:** feasible for compressed acquire + generous headroom.
- **RAM / Virtuoso load:** high risk on current WSL 7.4 GiB; may need host-adjusted WSL memory; still possibly tight at 16 GiB — **do not claim FEASIBLE_CURRENT_MACHINE for full load**.
- **Compose absent:** deployment scripting blocked until alternative documented.
- Scientific target **not** replaced due to resource difficulty.

Class: `CONDITIONAL_HIGH_RISK` (file-scope conditional + RAM risk). Deployment **not** executed (`GRAPH_DEPLOYMENT_NOT_EXECUTED`).
