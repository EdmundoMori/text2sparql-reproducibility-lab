# Acquisition vs deployment resources

**RUN_ID:** `20260722T132719Z`

## A. Acquisition

| Item | Value |
|---|---|
| Compressed total | **6925795437** bytes (~6.45 GiB) |
| Free disk observed | ~918 GiB |
| Status | **`FEASIBLE_CURRENT_DISK_CONDITIONAL_HUMAN_AUTHORIZATION`** |

Tag: `ACQUISITION_RESOURCE_FEASIBLE_CURRENT_DISK`

## B. Deployment

| Item | Value |
|---|---|
| WSL RAM | 7.4 GiB |
| Host RAM | ~16 GiB |
| Compose | absent |
| Status | **`CONDITIONAL_HIGH_RISK_REQUIRES_SEPARATE_RESOURCE_AND_DEPLOYMENT_GATE`** |

Tag: `DEPLOYMENT_RESOURCE_CONDITIONAL_HIGH_RISK`

Acquisition authorization **must not** authorize decompress/load/Virtuoso/Docker.
