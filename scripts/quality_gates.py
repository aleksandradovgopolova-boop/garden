#!/usr/bin/env python3
"""AI OPS quality-gate runner.

Runs the automated gates defined in
``internal/engineering/ai-ops/quality-gates.md`` and reports their status.
This is the single verification entry point referenced by ``CLAUDE.md``.

Only gates that can be checked automatically in this repository are wired in.
Human-judgement gates (product, security, accessibility) stay in the gate
document and in review; this runner never marks them as passed.

Usage:
    python scripts/quality_gates.py                # run every available gate
    python scripts/quality_gates.py --gate docs    # run one gate by name
    python scripts/quality_gates.py --list         # list available gates
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def gate_docs() -> int:
    """Documentation gate: metadata, links and single-source-of-truth checks."""
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_docs.py")]
    ).returncode


# name -> (description, callable returning a process exit code)
GATES = {
    "docs": ("Documentation gate (scripts/check_docs.py)", gate_docs),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run AI OPS quality gates.")
    parser.add_argument(
        "--gate",
        choices=sorted(GATES),
        help="run a single gate instead of all available gates",
    )
    parser.add_argument(
        "--list", action="store_true", help="list available gates and exit"
    )
    args = parser.parse_args()

    if args.list:
        for name, (desc, _) in sorted(GATES.items()):
            print(f"{name}: {desc}")
        return 0

    selected = [args.gate] if args.gate else sorted(GATES)
    failed = []
    for name in selected:
        desc, run = GATES[name]
        print(f"\n=== Gate: {name} — {desc} ===")
        if run() != 0:
            failed.append(name)

    print("\n=== AI OPS quality gates summary ===")
    for name in selected:
        print(f"  {'FAIL' if name in failed else 'PASS'}  {name}")
    if failed:
        print(f"Failed gates: {', '.join(failed)}. No agent may waive a failed gate.")
        return 1
    print("All selected gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
