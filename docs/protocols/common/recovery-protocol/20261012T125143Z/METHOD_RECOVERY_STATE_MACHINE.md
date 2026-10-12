# Method recovery state machine

Config: `configs/common/recovery-protocol/METHOD_RECOVERY_STATE_MACHINE.yaml`

After 25R2, methods enter: `RECOVERY_PROTOCOL_DEFINED`.

Transitions require explicit evidence IDs. Forbidden: "looks feasible".

Key terminals: LEGAL_BLOCKED · ARTIFACT_BLOCKED · COST_BLOCKED · RESOURCE_BLOCKED · SCIENTIFIC_INCOMPATIBILITY · TERMINAL_DOCUMENTARY_ONLY · TERMINAL_NOT_RECOVERABLE_CURRENT_PUBLIC_EVIDENCE · TERMINAL_HISTORICAL_ONLY.
