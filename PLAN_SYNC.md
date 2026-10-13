# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-13 (Prompt **25B-R1**)
**Fase:** Windows-host/WSL-guest D1 replanned · host authorization pending
**SHA inicial 25B-R1:** `ed97ea76c092ec39821151d72d8f5fed2da9219b`
**RUN_ID:** `20261013T080249Z`

Gate: `WINDOWS_HOST_WSL_GUEST_D1_REPLAN_COMPLETE_READY_FOR_HOST_APPLY_AUTHORIZATION`. Freeze `f90c0d78ecdcbbad6387f3f31122f6412c7f021d2de57aafda05b27af34e261c` unchanged.

## Prompt 25B reconciliation

Initial `f271997477c8505c1d223b91d7630d09135d3cd3`; artifact
`d5813ffa39226e9cb8f7ba8a2eb8a063c21fbd97`; publication/tip
`ed97ea76c092ec39821151d72d8f5fed2da9219b`; push confirmed.

## Current state

D1P is complete. Old 12/8 is superseded; actual prior effect is recorded but not accepted as D1 PASS.
New 10/2 subprofile is documentary/not applied. D1H/D1R/D1V remain pending. DBpedia is NOT_DEPLOYED.

## Unique next action

`HUMAN_D1_WINDOWS_HOST_APPLY_AUTHORIZATION` — `HUMAN_GATE_REQUIRED`. No executable WSL shutdown prompt.

## Publication

ARTIFACT_COMMIT: *(post-commit)*
publication metadata commit: *(post-commit tip; max 2 commits)*
push: pending
