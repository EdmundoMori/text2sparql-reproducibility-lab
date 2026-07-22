#!/usr/bin/env python3
"""Launcher for SGPT Z3 one-step training smoke (Prompt 14C). Disposable only."""
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

COUNTERS = {
    "optimizer_step": 0,
    "scheduler_step_total": 0,
    "scheduler_step_after_optimizer": 0,
    "backward": 0,
    "train_batches": 0,
}


class NetworkGuard(socket.socket):
    def __init__(self, *a, **k):
        raise RuntimeError("Z3_UNEXPECTED_NETWORK_ABORT")


def block_network():
    socket.socket = NetworkGuard  # type: ignore


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def prevalidate_step_budget():
    """Mirror train() batch sizing with canary assumptions; abort if != 1."""
    import math
    import torch
    from torch.utils.data import DataLoader, SequentialSampler
    from transformers import AutoTokenizer
    from scripts.dataset_lcquad2 import Dataset, SPECIAL_TOKENS

    params = json.loads(Path("config/lab-z3/params.json").read_text())
    tok = AutoTokenizer.from_pretrained(params["model_name_or_path"], local_files_only=True)
    tok.add_special_tokens(SPECIAL_TOKENS)
    ds_args = Namespace(
        dataroot="data",
        input_max_tokens=params["dataset_args"]["input_max_tokens"],
        knowledge_max_tokens=params["dataset_args"]["knowledge_max_tokens"],
        task="generation",
        knowledge=False,
    )
    ds = Dataset(ds_args, tok, name="lcquad2", split_type="train", masked=False, eval_partial=None)
    assert len(ds) == 1
    n_gpu = 0  # CPU path
    train_batch_size = params["per_gpu_train_batch_size"] * max(1, n_gpu)
    dl = DataLoader(ds, sampler=SequentialSampler(ds), batch_size=train_batch_size, collate_fn=ds.collate_fn)
    grad = params["gradient_accumulation_steps"]
    epochs = 1
    expected = (len(dl) // grad) * epochs
    info = {
        "train_n": len(ds),
        "train_batch_size": train_batch_size,
        "len_dataloader": len(dl),
        "grad_accum": grad,
        "epochs": epochs,
        "expected_optimizer_steps": expected,
    }
    if expected != 1:
        raise RuntimeError(f"Z3_STEP_COUNT_MISMATCH: {info}")
    if len(dl) != 1:
        raise RuntimeError(f"Z3_UNAUTHORIZED_ACTION_ABORT: more than one train batch: {len(dl)}")
    return info


def install_hooks():
    import torch
    from torch.optim import Optimizer
    from torch.optim.lr_scheduler import _LRScheduler

    _orig_opt_step = Optimizer.step
    _orig_sched_step = _LRScheduler.step
    _orig_backward = torch.Tensor.backward

    def counted_opt_step(self, *a, **k):
        COUNTERS["optimizer_step"] += 1
        if COUNTERS["optimizer_step"] > 1:
            raise RuntimeError("Z3_UNAUTHORIZED_ACTION_ABORT: more than one optimizer.step")
        return _orig_opt_step(self, *a, **k)

    def counted_sched_step(self, *a, **k):
        COUNTERS["scheduler_step_total"] += 1
        if COUNTERS["optimizer_step"] >= 1:
            COUNTERS["scheduler_step_after_optimizer"] += 1
            if COUNTERS["scheduler_step_after_optimizer"] > 1:
                raise RuntimeError("Z3_UNAUTHORIZED_ACTION_ABORT: more than one post-optimizer scheduler.step")
        # Allow LambdaLR __init__ pre-optimizer step(s)
        return _orig_sched_step(self, *a, **k)

    def counted_backward(self, *a, **k):
        COUNTERS["backward"] += 1
        if COUNTERS["backward"] > 1:
            raise RuntimeError("Z3_UNAUTHORIZED_ACTION_ABORT: more than one backward")
        return _orig_backward(self, *a, **k)

    Optimizer.step = counted_opt_step  # type: ignore
    _LRScheduler.step = counted_sched_step  # type: ignore
    torch.Tensor.backward = counted_backward  # type: ignore


def main():
    out = {
        "classification": "PENDING",
        "attempt": 2,
        "checks": {},
        "counters": COUNTERS,
        "errors": [],
    }
    t0 = time.time()
    for k in ("TRANSFORMERS_OFFLINE", "HF_HUB_OFFLINE", "HF_DATASETS_OFFLINE"):
        os.environ[k] = "1"
    report_path = Path("z3_one_step_report.json")

    try:
        import torch
        import transformers

        assert transformers.__version__ == "4.25.1"
        assert torch.__version__.startswith("1.13.1") and "+cpu" in torch.__version__
        assert not torch.cuda.is_available()
        block_network()

        out["checks"]["rss_mb_start"] = rss_mb()
        out["checks"]["pre_step_budget"] = prevalidate_step_budget()
        install_hooks()

        # Invoke native entrypoint with authorized CLI
        sys.argv = [
            "train.py",
            "--params_file",
            "config/lab-z3/params.json",
            "--dataset",
            "lcquad2",
            "--epochs",
            "1",
            "--eval_dataset",
            "test",
            "--exp_name",
            os.environ.get("SGPT_Z3_EXP_NAME", "sgpt-z3-canary"),
            "--device",
            "cpu",
            "--scheduler",
            "linear",
        ]
        import train as train_mod

        train_mod.main()

        # Validate counters / artifacts
        if COUNTERS["optimizer_step"] != 1:
            raise RuntimeError(f"optimizer_step={COUNTERS['optimizer_step']} expected 1")
        if COUNTERS["backward"] != 1:
            raise RuntimeError(f"backward={COUNTERS['backward']} expected 1")
        if COUNTERS["scheduler_step_after_optimizer"] != 1:
            raise RuntimeError(
                f"scheduler_step_after_optimizer={COUNTERS['scheduler_step_after_optimizer']} expected 1"
            )

        exp = os.environ.get("SGPT_Z3_EXP_NAME", "sgpt-z3-canary")
        out_dir = Path("runs") / exp / "lcquad2"
        ckpt = out_dir / "checkpoint-1"
        arts = {
            "output_dir": str(out_dir),
            "output_dir_exists": out_dir.is_dir(),
            "checkpoint_1": ckpt.is_dir(),
            "eval_results": (out_dir / "eval_results.txt").is_file(),
            "params_json": (out_dir / "params.json").is_file(),
            "training_args_bin": (out_dir / "training_args.bin").is_file(),
            "tokenizer_files": (out_dir / "tokenizer_config.json").is_file() or (out_dir / "vocab.json").is_file(),
            "model_weights": (out_dir / "pytorch_model.bin").is_file(),
            "files": sorted([p.name for p in out_dir.iterdir()]) if out_dir.is_dir() else [],
        }
        out["checks"]["artifacts"] = arts
        missing = [k for k, v in arts.items() if k not in ("output_dir", "files") and v is False]
        if missing:
            raise RuntimeError(f"missing artifacts: {missing}")

        # Output size budget
        def du(path: Path) -> int:
            total = 0
            for p in path.rglob("*"):
                if p.is_file():
                    total += p.stat().st_size
            return total

        out_bytes = du(Path("runs")) if Path("runs").exists() else 0
        out["checks"]["output_bytes"] = out_bytes
        if out_bytes > 6 * (1024**3):
            raise RuntimeError("Z3_DISK_BUDGET_ABORT")

        out["checks"]["rss_mb_end"] = rss_mb()
        if out["checks"]["rss_mb_end"] > 6 * 1024:
            raise RuntimeError("Z3_OOM_ABORT: RSS>6GiB")

        out["classification"] = "Z3_ONE_STEP_REDUCED_TRAINING_PASS"
        out["elapsed_seconds"] = round(time.time() - t0, 3)
    except Exception as e:
        out["classification"] = "Z3_OTHER_FAILED"
        # Refine known codes
        msg = repr(e)
        if "STEP_COUNT" in msg:
            out["classification"] = "Z3_STEP_COUNT_MISMATCH"
        elif "NETWORK" in msg:
            out["classification"] = "Z3_UNEXPECTED_NETWORK_ABORT"
        elif "OOM" in msg or "Disk" in msg.upper() or "DISK" in msg:
            out["classification"] = "Z3_OOM_ABORT" if "OOM" in msg else "Z3_DISK_BUDGET_ABORT"
        elif "UNAUTHORIZED" in msg:
            out["classification"] = "Z3_UNAUTHORIZED_ACTION_ABORT"
        out["errors"].append(msg)
        out["traceback"] = traceback.format_exc()[-4000:]
        out["elapsed_seconds"] = round(time.time() - t0, 3)

    report_path.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    return 0 if out["classification"] == "Z3_ONE_STEP_REDUCED_TRAINING_PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
