# Checkpoint: Archive paper + HM-6 Borel-join program (2026-10-18)

**Host repo (published in MO / X / LinkedIn posts):**  
https://github.com/ajjcoppola/hilberts-5th-oai

**Git tag:** `checkpoint/hm6-2026-10-18`  
**Component role:** self-contained “archive paper + HM-6” package living *inside* the Hilbert–Smith audit repo (not a separate public claim of classical HSC).

## What this checkpoint freezes

| Path | Role |
|------|------|
| [`papers/padic-homology-manifolds/`](../papers/padic-homology-manifolds/) | Unified arXiv-style draft PDF/TeX (relative framing + 7 contributions + HM-6 §8) |
| [`presentations/padic-homology-2026/`](../presentations/padic-homology-2026/) | Slides, checklist, sendable zip |
| [`lean/CoppolaHS/`](../lean/CoppolaHS/) | Lean 4.35.0-rc3 sources (CyclotomicTower, QuinnIndex, PadicExclusionENR, **DranishnikovHM6**) |
| [`scripts/hm6_equivariant_ew_harness.py`](../scripts/hm6_equivariant_ew_harness.py) | Gates G1–G4 + Borel-join |
| [`scripts/hm6_symbolic_lean_loop.py`](../scripts/hm6_symbolic_lean_loop.py) | `/loop` grid runner |
| [`counterexamples/hilbert-smith/`](../counterexamples/hilbert-smith/) | Campaign, ledger, HM-6 loop/harness reports |
| [`docs/SHERLOCK_HM6_DRANISHNIKOV_WILLIAMS_2026-10-18.md`](SHERLOCK_HM6_DRANISHNIKOV_WILLIAMS_2026-10-18.md) | Sherlock session |

## Honesty boundary (do not overclaim in posts)

- Theorems E/F are **relative** to OpenAI / Dabrowski 2026 geometric engines.
- HM-6 finite-stage gates **PASS**; continuous $clc_{\mathbb{Z}}$ glue remains **EDGE / open**.
- This checkpoint does **not** claim a standalone classical Hilbert–Smith proof.

## Local rebuild (optional)

```bash
# Lean (sources only are in git; .lake is gitignored)
source ~/.elan/env
cd lean/CoppolaHS && lake exe cache get && lake build

# Harness
python3 scripts/hm6_equivariant_ew_harness.py --n 5 --p 3 --stages 4
python3 scripts/hm6_symbolic_lean_loop.py
```

Full Dabrowski palomar tree for `#print axioms` stays a **local optional clone** (see [`dabrowski/PROVENANCE.md`](../dabrowski/PROVENANCE.md)); it is not vendored in this published tree.

## Outreach / collaborators

See [`OUTREACH_COLLABORATORS.md`](OUTREACH_COLLABORATORS.md) and updated [`POST_DRAFTS.md`](POST_DRAFTS.md).
