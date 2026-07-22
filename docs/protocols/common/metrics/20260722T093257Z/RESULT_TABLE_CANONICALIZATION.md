# RESULT_TABLE_CANONICALIZATION

**Primary semantics:** `SET_OF_ROWS`

- Duplicates ignored in primary metrics; preserved for bag-sensitive diagnostic.
- Row = tuple of canonical RDFTerms; table = unordered set of rows; order ignored in primary.
- Order-aware metric only if ranking task preregistered.
- Arity mismatch → Exact=0, Answer P/R/F1=0.
- Single-column: direct value compare.
- Multi-column: variable names independent; preserve column correlation; choose column permutation by lexicographically minimal table serialization; **do not** reorder values inside a row breaking association.
- No output ≠ valid empty result (cardinality 0).
- Arity permutation limit: if exceeded, require documented scalable algorithm — no silent factorial enumeration.
