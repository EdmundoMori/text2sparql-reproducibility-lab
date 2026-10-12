# Method recovery dependency DAG

Config: `configs/common/recovery-protocol/METHOD_RECOVERY_DEPENDENCY_DAG.yaml`

- SPARQL local: 25R3 → 25R4 → G4 → local model preflight → adapter auth → execution
- SGPT: 25R3 → 25R4 → training preflight → human auth → training → G4/G5 → eval
- mKG: public LICENSE → controlled admissibility → local backend → adapter
- RDFConfig: Zenodo equivalence → legal → Ruby → local backend → schema fairness → adapter
- CoT: legal → artifacts → ZERO_COST compute → runtime → execution
- FIRE: domain-native only; does not block QALD
- TeBaQA: optional after common core
