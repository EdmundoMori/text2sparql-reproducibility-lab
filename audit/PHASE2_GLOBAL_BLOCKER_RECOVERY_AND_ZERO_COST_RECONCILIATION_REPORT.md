# PHASE2 — Global blocker recovery and ZERO_COST reconciliation (Prompt 25R1)

**RUN_ID:** `20261012T122043Z` · **Gate:** `GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION_COMPLETE_READY_FOR_METHOD_RECOVERY_PROTOCOL` · **Cost:** 0.00

## 1. Executive summary

Replanning wave maps all method blockers under `ZERO_EXTERNAL_MONETARY_COST` without executing methods, training, SPARQL, or deployment. QALD primary and DBpedia 2016-10 target preserved. Deployment profile selection **deferred, not cancelled** (`READY_UNSIGNED`).

## 2. Reason for replanning

Before DBpedia load, convert permanent-looking Phase-1 blocks into formal recovery classes and ZERO_COST eligibility.

## 3–4. Scope / out of scope

In: documentary recovery map, taxonomy, ZC gates, matrices, master-state reconciliation.  
Out: execution, training, inference, docker pull, decompress, Virtuoso, gold, adapters impl, benchmark, author contact.

## 5. Phase 1 preserved

sparql_llm smoke_only · sgpt smoke_only · mkgqagent blocked · rdfconfig blocked · cot blocked · firesparql not_reproducible · tebaqa historical_only.

## 6. Phase 2 state reconciliation

- QALD payload: ACQUIRED_VALIDATED (master fields corrected from DATASET_PAYLOAD_NOT_ACQUIRED)
- Graph compressed: ACQUIRED_VALIDATED_COMPRESSED_WORKDIR_ONLY
- Deployment: NOT_DEPLOYED · G4 runtime NOT_SATISFIED · gold PENDING
- Profile selection: DEFERRED_BY_SCIENTIFIC_REPLAN_READY_UNSIGNED

## 7–10. Taxonomy / recoverability / ZERO_COST / ZC1–ZC8

See recovery docs under `docs/protocols/common/recovery/20261012T122043Z/` and `configs/common/recovery/`.

## 11–17. Methods

See per-method assessments. Highlights:

| Method | ZERO_COST overall | Native faithful | Controlled variant |
|---|---|---|---|
| sparql_llm | faithful NOT_FEASIBLE; local-backend CANDIDATE | API path not ZERO_COST | YES |
| sgpt | CONDITIONAL_RECOVERY | train/ckpt conditional | RESOURCE_EQUIVALENT possible |
| mkgqagent | DOCUMENTARY_ONLY | BLOCKED_LEGAL | after LICENSE |
| rdfconfig_llm | CONDITIONAL | legal+cost | after Zenodo equivalence |
| cot_sparql | DOCUMENTARY_ONLY | multi-blocked | not invented |
| firesparql | DOCUMENTARY_ONLY | not_reproducible | not for QALD (R7) |
| tebaqa | HISTORICAL_ONLY | KEEP | optional later |

## 18–22. Cross comparison / variants / recovery / fairness / QALD

Matrices in `audit/recovery/`. No cross-track global ranking. QALD primary unchanged.

## 23–25. LC-QuAD HOLD · TEXT2SPARQL25 future validation candidate only

## 26–28. Executable / recoverable / documentary

Currently executable for full common benchmark: **none** (G4/G5/G6I pending).  
Potentially recoverable ZERO_COST: sparql_llm local-backend, sgpt training, rdfconfig after legal, mkg after LICENSE.  
Documentary/R7/historical: cot (now), firesparql common-core, tebaqa.

## 29–33. Risks / G4 / G5 / G6I / benchmark

G4 NOT_SATISFIED · G5 pending · G6D documented · G6I pending · adapters false · benchmark NOT_CURRENTLY_ELIGIBLE.

## 34–35. Roadmap / next

`audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv` · next **`DEFINE_ZERO_COST_METHOD_RECOVERY_PROTOCOL`** (Prompt 25R2).

## 36–38. Long-term / claims / conclusion

Doctoral sequence intact. No Phase-1 claim upgrades. Compressed acquisition ≠ authorization to decompress/load. Blocked ≠ permanently excluded without taxonomy.
