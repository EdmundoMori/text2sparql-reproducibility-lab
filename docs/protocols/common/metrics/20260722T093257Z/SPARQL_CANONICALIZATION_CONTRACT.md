# SPARQL_CANONICALIZATION_CONTRACT

**Profile:** `SPARQL_CANONICALIZATION_V1_CONSERVATIVE`

## Permitido
Parse SPARQL 1.1; resolve PREFIX/BASE; uniform prefixes; whitespace norm; Unicode NFC; RDFTerm canon; deterministic variable α-rename; deterministic triple order within BGP; deterministic PREFIX order; safe keyword normalization.

## Prohibido
General algebraic rewrite; inference; OPTIONAL removal; UNION/MINUS reorder; FILTER simplify; property-path substitute; entailment; execute-to-prove; gold repair; LLM equivalence.

## Preservar
BGP/OPTIONAL/UNION/MINUS/GRAPH/SERVICE/subquery/FILTER/BIND/VALUES/GROUP BY/HAVING/ORDER BY/LIMIT/OFFSET/DISTINCT/REDUCED/aggregates/property-path AST.

Demuestra igualdad **dentro del perfil**, no equivalencia semántica completa.
