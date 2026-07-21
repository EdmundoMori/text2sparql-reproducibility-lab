#!/usr/bin/env python3
"""P2A model-load preflight for SGPT Z3. NO forward. NO train. Offline only."""
from __future__ import annotations

import importlib
import json
import os
import resource
import socket
import sys
import time
import traceback
from argparse import Namespace
from pathlib import Path

class NetworkGuard(socket.socket):
    def __init__(self, *a, **k):
        raise RuntimeError("Z3_UNEXPECTED_NETWORK_ABORT: socket forbidden during P2A offline preflight")


def block_network() -> None:
    socket.socket = NetworkGuard  # type: ignore


def rss_mb():
    # Linux: ru_maxrss is KB
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main():
    out = {
        "classification": "PENDING",
        "stage": "P2A",
        "forward_authorized": False,
        "checks": {},
        "errors": [],
    }
    t0 = time.time()
    for k in ("TRANSFORMERS_OFFLINE", "HF_HUB_OFFLINE", "HF_DATASETS_OFFLINE"):
        os.environ[k] = "1"
    try:
        gpt2 = Path(os.environ["SGPT_GPT2_LOCAL_PATH"]).resolve()
        assert gpt2.is_dir(), gpt2
        for f in ("config.json", "pytorch_model.bin", "vocab.json", "merges.txt", "tokenizer_config.json"):
            assert (gpt2 / f).is_file(), f
        out["checks"]["gpt2_path"] = str(gpt2)

        # Import heavy libs BEFORE installing socket guard (ssl needs real socket type)
        import torch
        import transformers
        import tensorboardX
        import pkg_resources
        from transformers import AutoConfig, AutoTokenizer

        block_network()
        out["checks"]["network_guard"] = "installed_after_torch_import"

        pb = pkg_resources.get_distribution("protobuf").version
        assert transformers.__version__ == "4.25.1"
        assert torch.__version__.startswith("1.13.1") and "+cpu" in torch.__version__
        assert tensorboardX.__version__ == "2.5.1"
        assert pb == "3.20.1"
        assert not torch.cuda.is_available()
        out["checks"]["packages"] = {
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "tensorboardX": tensorboardX.__version__,
            "protobuf": pb,
            "cuda": False,
        }

        rss0 = rss_mb()
        out["checks"]["rss_mb_start"] = rss0

        # import scripts.model
        import scripts.model as sm

        out["checks"]["import_scripts_model"] = True
        GPT2LMHeadModel = sm.GPT2LMHeadModel

        # import train without main
        import train as train_mod

        assert hasattr(train_mod, "main")
        out["checks"]["import_train_no_main"] = True

        t_load0 = time.time()
        tokenizer = AutoTokenizer.from_pretrained(str(gpt2), local_files_only=True)
        config = AutoConfig.from_pretrained(str(gpt2), local_files_only=True)
        config.output_past = False
        config.knowledge_max_tokens = 50

        # load with loading info
        model, loading_info = GPT2LMHeadModel.from_pretrained(
            str(gpt2), config=config, output_loading_info=True, local_files_only=True
        )
        # Expected missing: custom SGPT layers not in stock GPT-2 (+ HF buffers / tied head)
        unexpected = list(loading_info.get("unexpected_keys") or [])
        mismatched = list(loading_info.get("mismatched_keys") or [])
        missing = list(loading_info.get("missing_keys") or [])
        def is_expected_missing(k: str) -> bool:
            # Custom SGPT layers + HF buffers / tied lm_head not stored in pytorch_model.bin
            if any(x in k for x in ("pose", "dep", "depl", "encoder", "decoder")):
                return True
            if k.endswith("masked_bias") or k == "lm_head.weight":
                return True
            return False

        unexplained_missing = [k for k in missing if not is_expected_missing(k)]
        # Abort only on truly incompatible load signals
        core_weight_patterns = (
            "wte.weight",
            "wpe.weight",
            "ln_f.",
            ".attn.c_attn.",
            ".attn.c_proj.",
            ".mlp.c_fc.",
            ".mlp.c_proj.",
            ".ln_1.",
            ".ln_2.",
        )
        core_bad = [k for k in unexplained_missing if any(p in k for p in core_weight_patterns)]

        out["checks"]["loading_info"] = {
            "n_missing": len(missing),
            "n_unexpected": len(unexpected),
            "n_mismatched": len(mismatched),
            "missing_sample": missing[:20],
            "unexpected": unexpected,
            "mismatched": mismatched,
            "unexplained_missing": unexplained_missing,
            "core_bad_missing": core_bad,
            "compatibility": "custom_sgpt_layers_expected_missing",
        }
        if unexpected or mismatched or core_bad:
            raise RuntimeError(
                f"incompatible loading keys unexpected={unexpected} mismatched={mismatched} core_bad={core_bad}"
            )

        from scripts.dataset_lcquad2 import Dataset, SPECIAL_TOKENS as ST

        SPECIAL_TOKENS = ST
        tokenizer.add_special_tokens(SPECIAL_TOKENS)
        model.resize_token_embeddings(len(tokenizer))
        n_params = sum(p.numel() for p in model.parameters())
        dtypes = sorted({str(p.dtype) for p in model.parameters()})
        t_load1 = time.time()
        rss1 = rss_mb()
        out["checks"]["model"] = {
            "n_params": n_params,
            "dtypes": dtypes,
            "vocab_after_special": len(tokenizer),
            "load_seconds": round(t_load1 - t_load0, 3),
            "rss_mb_after_load": rss1,
        }

        # Ensure no forward was called
        out["checks"]["forward_executed"] = False

        # Dataset + collate (cwd must contain data/lcquad2)
        dataset_args = Namespace(dataroot="data", input_max_tokens=50, knowledge_max_tokens=50, task="generation", knowledge=False)
        ds = Dataset(dataset_args, tokenizer, name="lcquad2", split_type="train", masked=False, eval_partial=None)
        assert len(ds) == 1, len(ds)
        batch = ds.collate_fn([ds[0]])
        out["checks"]["dataset"] = {
            "n_train": len(ds),
            "batch_keys": sorted(list(batch.keys()) if isinstance(batch, dict) else ["non_dict"]),
            "collate_ok": True,
        }

        # Step budget without training: recreate train() batch sizing logic
        per_gpu = 1
        n_gpu = 0  # CPU path in train.py uses device_count()==0
        train_batch_size = per_gpu * max(1, n_gpu)
        n_train = len(ds)
        # DataLoader length with batch_size
        import math

        len_dl = math.ceil(n_train / train_batch_size) if False else (n_train + train_batch_size - 1) // train_batch_size
        # PyTorch DataLoader: ceil division
        from torch.utils.data import DataLoader, SequentialSampler

        dl = DataLoader(ds, sampler=SequentialSampler(ds), batch_size=train_batch_size, collate_fn=ds.collate_fn)
        grad_accum = 1
        epochs = 1
        expected_steps = (len(dl) // grad_accum) * epochs
        out["checks"]["step_budget"] = {
            "train_n": n_train,
            "train_batch_size": train_batch_size,
            "len_dataloader": len(dl),
            "grad_accum": grad_accum,
            "epochs": epochs,
            "expected_optimizer_steps": expected_steps,
        }
        if expected_steps != 1:
            raise RuntimeError(f"step budget != 1: {expected_steps}")

        # memory gate
        if rss1 > 5 * 1024:
            raise RuntimeError(f"RSS {rss1} MiB exceeds 5 GiB")

        out["classification"] = "Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS"
        out["elapsed_seconds"] = round(time.time() - t0, 3)
    except Exception as e:
        out["classification"] = "Z3_P2A_MODEL_LOAD_FAILED"
        out["errors"].append(repr(e))
        out["traceback"] = traceback.format_exc()[-4000:]
        out["elapsed_seconds"] = round(time.time() - t0, 3)

    print(json.dumps(out, indent=2))
    return 0 if out["classification"] == "Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
