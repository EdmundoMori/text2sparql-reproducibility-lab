# RDFConfig license evidence correction

**RUN_ID:** `20261012T135645Z`

`OLD_STATUS = LICENSE_ABSENT_AT_PIN / LICENSE_NOT_CONFIRMED`.

The earlier audit treated the absence of a root LICENSE and GitHub `license=null` as dispositive and
explicitly ignored the README MIT claim. Prompt 25R3A introduces LE2 and verifies the exact pinned README:
blob `c813f08014babde306e2539b1119cf396220622c`, SHA-256
`0d234b70ebb9ac497372aa50bf56cae087fff3926a7b00a28c701c775f7481c7`, lines 110–113, statement covering
“All files in this repository” under MIT with a standard-license link.

`NEW_STATUS = CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN`.
`CORRECTION_REASON = explicit repository-wide author statement satisfies LE2`.
`EVIDENCE_DISCOVERED_DURING_25R3A = true`.

Qualifiers `NO_STANDARD_LICENSE_FILE` and `GITHUB_LICENSE_DETECTION_NULL` remain. Zenodo CC-BY-4.0 and the
nested companion MIT license remain separate and were not transferred. This corrects current lab evidence;
it does not rewrite RDFConfig's historical Phase-1 `blocked` outcome and is not legal advice.
