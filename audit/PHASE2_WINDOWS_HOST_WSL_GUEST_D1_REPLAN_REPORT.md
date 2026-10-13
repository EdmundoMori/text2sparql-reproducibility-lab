# PHASE2 Windows-host / WSL-guest D1 replan report

**RUN_ID:** `20261013T080249Z`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_RESOURCE_MODIFICATION · NO_WSL_SHUTDOWN
**Freeze:** `COMMON_CORE_BENCHMARK_FREEZE_V1` · `1.0.0-25R4` · `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c`


## 1. Problem observed

Cursor's WSL connection terminated when the guest was shut down.

## 2. Why connection interruption is expected

Cursor execution depends on the WSL2 Ubuntu guest lifecycle.

## 3. Host/guest topology

Windows is control plane; Ubuntu/WSL2 is execution plane.

## 4. Prior D1 limitation

Single-session apply/shutdown/verify is topology-incompatible; prior 12/8 effect is not D1 PASS.

## 5. Memory reassessment

10 GiB leaves 5.19 GiB theoretical host headroom; 12 GiB leaves 3.19 GiB.

## 6. Swap reassessment

Revised proposal preserves 2 GiB; swap is not RAM.

## 7. Windows C: constraint

~7.4 GiB free makes an 8 GiB default swap expansion indefensible.

## 8. 10/2 resource profile

LOCAL_WSL_RESOURCE_CONSTRAINED_V1 is documentary, high-risk for full load, not applied.

## 9. D1P

Package prepared and published in this prompt.

## 10. D1H

Future manual Windows-host safe merge, separately authorized.

## 11. D1R

Future manual Windows PowerShell shutdown after work is closed.

## 12. D1V

Future new-session read-only Ubuntu verification.

## 13. Windows PowerShell package

Safe backup/merge/hash script exists and is not executed in 25B-R1.

## 14. Rollback

Timestamped backup and hashes preserve exact prior config.

## 15. Stop conditions

Host, WSL2, backup, merge, storage, restart, observed resources, filesystem, freeze and cost.

## 16. Future low-memory Virtuoso strategy

Separate future conservative tuning before D4; none created/executed now.

## 17. ZERO_COST

External monetary cost remains USD 0.00.

## 18. DBpedia

Compressed payload unchanged; NOT_DEPLOYED.

## 19. G4/G5/G6I

G4 NOT_SATISFIED; G5 and G6I pending; G6D documented; adapters false.

## 20. Benchmark

NOT_CURRENTLY_ELIGIBLE; QALD test remains SEALED.

## 21. Next human action

Exactly one: `HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION`.

## 22. Claim boundary

D1P only; no claim that 10/2 is applied or full load feasible.
