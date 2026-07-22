# RDF_TERM_CANONICALIZATION

**Profile:** `RDF_TERM_CANONICALIZATION_V1` · Prompt 18

## IRIs
Unicode NFC; scheme/host lowercase; default port removal when applicable; RFC 3986 dot-segments; percent-encoding of unreserved normalized; preserve path/query/fragment case; **no** trailing-slash removal; **no** redirects; **no** owl:sameAs; **no** label resolution; **no** cross-namespace equality.

## Literales
NFC; no general case-fold; no general whitespace collapse; plain ↔ xsd:string may share textual representation; language tags lowercase; language-tagged ≠ untagged; booleans/numerics by value space; **no** implicit numeric tolerance; dates/dateTimes common zone **only** if both have explicit timezone; **no** invented timezone; preserve datatype.

## Blank nodes
No local-id equality; future result-local bijection; if unresolved → `GLOBAL_BNODE_CANONICALIZATION_UNRESOLVED` (global, not single-method penalty).

## Unbound
Canonical token `UNBOUND`.

## Ejemplos normativos (no ejecutados)
| Caso | A | B | Esperado V1 |
|---|---|---|---|
| IRI host case | `http://Example.org/a` | `http://example.org/a` | equal |
| path case | `.../A` | `.../a` | unequal |
| trailing slash | `.../a` | `.../a/` | unequal |
| plain vs xsd:string | `"x"` | `"x"^^xsd:string` | equal (textual) |
| lang | `"x"@EN` | `"x"@en` | equal |
| lang vs untagged | `"x"@en` | `"x"` | unequal |
| unbound | (missing) | (missing) | both `UNBOUND` |
