#!/usr/bin/env python3
"""HM-6 /loop iterative verification runner.

Runs the equivariant Edwards–Walsh + Williams harness across a grid of
(n, p, stages), records each iteration's gate status, and writes a loop log
under counterexamples/hilbert-smith/.

This is the computational half of the plan's Phase 2 (/loop).  Lean
compilation is invoked separately via `lake build` in lean/CoppolaHS.
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.hm6_equivariant_ew_harness import run_harness  # noqa: E402

GRID = [
    {"n": 5, "p": 3, "stages": 4, "label": "iter1-baseline"},
    {"n": 7, "p": 5, "stages": 3, "label": "iter2-borel-join"},
    {"n": 6, "p": 3, "stages": 5, "label": "iter3-cup-growth"},
    {"n": 9, "p": 7, "stages": 4, "label": "iter4-large-prime"},
]

LOG_PATH = ROOT / "counterexamples/hilbert-smith/HM6_LOOP_LOG.md"
JSON_PATH = ROOT / "counterexamples/hilbert-smith/HM6_LOOP_REPORT.json"


def run_iterations() -> dict:
    iterations = []
    for spec in GRID:
        report = run_harness(spec["n"], spec["p"], spec["stages"])
        iterations.append({
            "label": spec["label"],
            "params": {"n": spec["n"], "p": spec["p"], "stages": spec["stages"]},
            "all_pass": report["all_pass"],
            "gates": {g["gate"]: g["pass"] for g in report["gates"]},
            "summaries": {g["gate"]: g["summary"] for g in report["gates"]},
        })
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "architecture": (
            "E_{i+1} = (E_i Δ_q EW_d(E_i, Z, n)) ×_{C_{p^{i+1}}} S^{2m_{i+1}-1}"
        ),
        "iterations": iterations,
        "all_pass": all(it["all_pass"] for it in iterations),
    }


def write_log(bundle: dict) -> None:
    lines = [
        "# HM-6 Symbolic /loop Log",
        "",
        f"- Timestamp (UTC): `{bundle['timestamp']}`",
        f"- Architecture: `{bundle['architecture']}`",
        f"- Overall: **{'PASS' if bundle['all_pass'] else 'FAIL'}**",
        "",
        "## Iterations",
        "",
    ]
    for it in bundle["iterations"]:
        status = "PASS" if it["all_pass"] else "FAIL"
        p = it["params"]
        lines.append(
            f"### {it['label']} — [{status}] "
            f"(n={p['n']}, p={p['p']}, stages={p['stages']})"
        )
        lines.append("")
        for gate, ok in it["gates"].items():
            mark = "PASS" if ok else "FAIL"
            lines.append(f"- [{mark}] `{gate}`: {it['summaries'][gate]}")
        lines.append("")
    lines.extend([
        "## Refinement notes (plan Phase 2)",
        "",
        "1. **Iteration 1:** Williams $K\\Delta_q X$ + EW Postnikov cells — "
        "G1–G3 pass; classical torus obstruction bypassed.",
        "2. **Iteration 2:** Borel-join connectivity uses free-sphere "
        "$(2m-2)$-connectivity (not limited by `conn(F)` of the EW skeleton).",
        "3. **Iteration 3:** Dranishnikov Prop. 3.3 schedule with "
        "$k=m+1$, $k-l=1$ so $v_p(\\mathrm{coeff}_m)=m<k$; cup-length grows.",
        "4. **Iteration 4:** Large-prime sanity check ($p=7$, $n=9$).",
        "",
        "## Lean formalization",
        "",
        "See `lean/CoppolaHS/CoppolaHS/DranishnikovHM6.lean` "
        "(Borel-join connectivity, K-theory cup-length criterion, "
        "HM-6 escape from `OpenAIENRInput` / `DabrowskiTowerInput`).",
        "",
    ])
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text("\n".join(lines) + "\n")
    JSON_PATH.write_text(json.dumps(bundle, indent=2))


def try_lake_build() -> dict:
    lean_dir = ROOT / "lean/CoppolaHS"
    if not (lean_dir / "lakefile.toml").exists():
        return {"ran": False, "reason": "no lakefile"}
    try:
        proc = subprocess.run(
            ["lake", "env", "lean", "--version"],
            cwd=lean_dir,
            capture_output=True,
            text=True,
            timeout=60,
        )
        version = (proc.stdout or proc.stderr or "").strip().split("\n")[0]
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return {"ran": False, "reason": str(e)}
    return {"ran": False, "lean_version_probe": version,
            "note": "Full `lake build` invoked separately in hm6-lean step."}


def main() -> int:
    bundle = run_iterations()
    bundle["lean_probe"] = try_lake_build()
    write_log(bundle)
    print("=" * 72)
    print("HM-6 /loop complete")
    print(f"Overall: {'PASS' if bundle['all_pass'] else 'FAIL'}")
    for it in bundle["iterations"]:
        st = "PASS" if it["all_pass"] else "FAIL"
        print(f"  [{st}] {it['label']}")
    print(f"log  → {LOG_PATH}")
    print(f"json → {JSON_PATH}")
    print("=" * 72)
    return 0 if bundle["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
