# Metric and failure-accounting alignment

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


Common primary metrics remain Answer Precision, Answer Recall, Answer F1 and Execution Exact Accuracy under
the Prompt 18 canonicalization, empty-answer, timeout, error-category, denominator and aggregation contracts.
Syntax/execution errors, timeout, abstention, no output and invalid output stay in the common denominator.
Native metrics are supplementary. BLEU, ROUGE and query exact match never substitute for Answer F1.
Runtime status remains G5 implementation/conformance pending.
