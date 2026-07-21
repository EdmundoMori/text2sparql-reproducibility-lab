#!/usr/bin/env python3
"""SGPT Z3 P2B: exactly one torch.no_grad() forward on canary batch. No train/backward."""
from __future__ import annotations

import json
import os
import resource
import socket
import sys
import time
import traceback
from argparse import Namespace
from pathlib import Path

FORWARD_COUNT = 0


class NetworkGuard(socket.socket):
    def __init__(self, *a, **k):
        raise RuntimeError("Z3_UNEXPECTED_NETWORK_ABORT: socket forbidden during P2B")


def block_network() -> None:
    socket.socket = NetworkGuard  # type: ignore


def rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def main() -> int:
    global FORWARD_COUNT
    out = {
        "classification": "PENDING",
        "stage": "P2B",
        "forward_authorized": True,
        "backward_authorized": False,
        "checks": {},
        "errors": [],
    }
    t0 = time.time()
    for k in ("TRANSFORMERS_OFFLINE", "HF_HUB_OFFLINE", "HF_DATASETS_OFFLINE"):
        os.environ[k] = "1"

    try:
        gpt2 = Path(os.environ["SGPT_GPT2_LOCAL_PATH"]).resolve()
        assert gpt2.is_dir()
        for f in ("config.json", "pytorch_model.bin", "vocab.json", "merges.txt", "tokenizer_config.json"):
            assert (gpt2 / f).is_file(), f

        import torch
        import transformers
        from transformers import AutoConfig, AutoTokenizer

        block_network()
        out["checks"]["network_guard"] = "installed_after_torch_import"

        assert transformers.__version__ == "4.25.1"
        assert torch.__version__.startswith("1.13.1") and "+cpu" in torch.__version__
        assert not torch.cuda.is_available()
        out["checks"]["packages"] = {
            "torch": torch.__version__,
            "transformers": transformers.__version__,
            "cuda": False,
        }
        out["checks"]["rss_mb_start"] = rss_mb()

        from scripts.dataset_lcquad2 import Dataset, SPECIAL_TOKENS
        from scripts.model import GPT2LMHeadModel, run_batch_generation

        # Patch model __call__/forward counter via wrapper around run_batch path
        # We count invocations of run_batch_generation itself as the authorized unit,
        # and also wrap model.forward to ensure exactly one model forward.
        _orig_forward = GPT2LMHeadModel.forward

        def _counting_forward(self, *a, **k):
            global FORWARD_COUNT
            FORWARD_COUNT += 1
            if FORWARD_COUNT > 1:
                raise RuntimeError("Z3_UNAUTHORIZED_ACTION_ABORT: more than one forward")
            return _orig_forward(self, *a, **k)

        GPT2LMHeadModel.forward = _counting_forward  # type: ignore

        t_load0 = time.time()
        tokenizer = AutoTokenizer.from_pretrained(str(gpt2), local_files_only=True)
        config = AutoConfig.from_pretrained(str(gpt2), local_files_only=True)
        config.output_past = False
        config.knowledge_max_tokens = 50
        model, loading_info = GPT2LMHeadModel.from_pretrained(
            str(gpt2), config=config, output_loading_info=True, local_files_only=True
        )
        missing = list(loading_info.get("missing_keys") or [])
        unexpected = list(loading_info.get("unexpected_keys") or [])
        mismatched = list(loading_info.get("mismatched_keys") or [])
        if unexpected or mismatched:
            raise RuntimeError(f"incompatible keys unexpected={unexpected} mismatched={mismatched}")
        tokenizer.add_special_tokens(SPECIAL_TOKENS)
        model.resize_token_embeddings(len(tokenizer))
        model.eval()
        out["checks"]["load_seconds"] = round(time.time() - t_load0, 3)
        out["checks"]["loading_info"] = {
            "n_missing": len(missing),
            "n_unexpected": len(unexpected),
            "n_mismatched": len(mismatched),
        }
        out["checks"]["rss_mb_after_load"] = rss_mb()

        # Canary dataset — cwd must be disposable root with data/lcquad2
        dataset_args = Namespace(
            dataroot="data",
            input_max_tokens=50,
            knowledge_max_tokens=50,
            task="generation",
            knowledge=False,
        )
        ds = Dataset(dataset_args, tokenizer, name="lcquad2", split_type="train", masked=False, eval_partial=None)
        assert len(ds) == 1, len(ds)
        # uid check from raw file
        train_rec = json.loads(Path("data/lcquad2/train.json").read_text())
        assert train_rec[0]["uid"] == 8714
        # POS/DEP range
        for arr_name in ("question_pos_ids", "question_dep_lvl"):
            for v in train_rec[0][arr_name]:
                if v is None:
                    continue
                if isinstance(v, int) and v != -1 and (v < 0 or v >= 50):
                    raise RuntimeError(f"POS/DEP id out of range: {arr_name}={v}")

        batch = ds.collate_fn([ds[0]])
        assert isinstance(batch, tuple) and len(batch) == 6
        for t in batch:
            assert t.shape[0] == 1, t.shape
            # feature ids in tensors (postag/dep/dep_lvl indices 2,3,4)
        for idx, name in ((2, "postag_ids"), (3, "dep_ids"), (4, "dep_lvl")):
            mx = int(batch[idx].max().item())
            if mx >= 50:
                raise RuntimeError(f"{name} max id {mx} >= 50")

        args = Namespace(device=torch.device("cpu"))
        # Ensure no grads / no optimizer
        for p in model.parameters():
            assert p.grad is None

        t_fwd0 = time.time()
        with torch.no_grad():
            loss, lm_logits, _, _ = run_batch_generation(args, model, batch)
        t_fwd1 = time.time()

        if FORWARD_COUNT != 1:
            raise RuntimeError(f"forward_count={FORWARD_COUNT} expected 1")

        # No gradients created
        for p in model.parameters():
            if p.grad is not None:
                raise RuntimeError("gradient created during P2B")

        loss_val = float(loss.detach().cpu().item()) if hasattr(loss, "detach") else float(loss)
        if not (loss_val == loss_val) or loss_val in (float("inf"), float("-inf")):
            raise RuntimeError(f"nonfinite loss: {loss_val}")
        logits = lm_logits.detach().cpu()
        if not torch.isfinite(logits).all():
            raise RuntimeError("nonfinite logits")

        out["checks"]["forward"] = {
            "count": FORWARD_COUNT,
            "loss": loss_val,
            "logits_shape": list(logits.shape),
            "logits_dtype": str(logits.dtype),
            "batch_shapes": [list(t.shape) for t in batch],
            "forward_seconds": round(t_fwd1 - t_fwd0, 3),
            "rss_mb_after_forward": rss_mb(),
            "requires_grad_loss": bool(getattr(loss, "requires_grad", False)),
        }
        if out["checks"]["forward"]["requires_grad_loss"]:
            raise RuntimeError("loss unexpectedly requires_grad under no_grad")
        if out["checks"]["forward"]["rss_mb_after_forward"] > 5 * 1024:
            raise RuntimeError("RSS exceeds 5 GiB")

        out["checks"]["optimizer_created"] = False
        out["checks"]["backward_executed"] = False
        out["checks"]["train_main_executed"] = False
        out["classification"] = "Z3_P2B_NOGRAD_FORWARD_PASS"
        out["elapsed_seconds"] = round(time.time() - t0, 3)
    except Exception as e:
        out["classification"] = "Z3_P2B_FORWARD_FAILED"
        out["errors"].append(repr(e))
        out["traceback"] = traceback.format_exc()[-4000:]
        out["checks"]["forward_count"] = FORWARD_COUNT
        out["elapsed_seconds"] = round(time.time() - t0, 3)

    print(json.dumps(out, indent=2))
    return 0 if out["classification"] == "Z3_P2B_NOGRAD_FORWARD_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
