# Z3_MODEL_PREFLIGHT_CONTRACT (futuro P2)

**RUN_ID:** `20260721T134213Z` · **NOT_EXECUTED** · Prompt 14A **no** autoriza P2A ni P2B

## Comprobaciones futuras
artifacts+hashes; red bloqueada; import `scripts.model`; import entrypoint sin `main`; tokenizer/config/`GPT2LMHeadModel.from_pretrained` path local; loading info (missing/unexpected/mismatched keys); special tokens; resize; n params; dtype; RSS antes/después; tiempo carga; subset+Dataset LC-QuAD2; collate batch; límites POS/DEP; sin escrituras fuera workdir.

## Separación
| Subetapa | Alcance | Auth |
|---|---|---|
| **P2A** | load only, sin forward | formulario artefactos+preflight |
| **P2B** | un forward `torch.no_grad()` | marca explícita en el mismo o auth adicional |

Sin backward, optimizer ni checkpoint en P2.
