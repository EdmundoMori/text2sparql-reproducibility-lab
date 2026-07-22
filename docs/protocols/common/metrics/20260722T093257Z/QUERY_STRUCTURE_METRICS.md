# QUERY_STRUCTURE_METRICS

**Family:** `QUERY_STRUCTURE_DIAGNOSTIC` — **no** sustituyen Answer F1.

raw_string_exact_match · normalized_query_exact_match · query_form_match · projection_arity_match · triple_pattern_{P,R,F1} · filter_structure_match · aggregation_structure_match · modifier_structure_match · property_path_structure_match · query_grounding_constant_{P,R,F1}

Triple signature: s/p|path AST/o + graph context + structural scope + UNION/OPTIONAL/MINUS/subquery; variables α-normalized.

**No** llamar Entity Linking F1 a comparación de constantes de queries.
