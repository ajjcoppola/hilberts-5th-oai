# CoppolaHS — Lean extension on Dabrowski arithmetic

Archive-paper formalization layer (Alan J. Coppola, 2026-10-17).

| Module | Role |
|--------|------|
| `CyclotomicTower.lean` | `p^k ∣ F(1)` from a product of `k` prime-power cyclotomics (Theorem F arithmetic) |
| `QuinnIndex.lean` | Abstract `I(X) ≡ 1 (mod 8)` + product formula hypotheses |
| `PadicExclusionENR.lean` | Conditional Theorems E/F shells |
| `ChallengeENR.lean` / `SolutionENR.lean` | Comparator-style statement + relative solution notes |
| `DranishnikovHM6.lean` | Borel-join connectivity, Dranishnikov cup-length valuation gate, HM-6 escape from ENR packaging (2026-10-18) |

**Upstream Dabrowski pin:** `dabrowski/upstream-palomar/` @ `b75523f` (`palomar-review/module-system-20261015`), Lean `v4.35.0-rc3`, mathlib `1a547d8`.

**Honest boundary:** no controlled L-theory reimplementation of Dabrowski §§7–13 for ENRs. Geometric BFMW / OpenAI / Dabrowski inputs remain named hypotheses. HM-6 continuous $clc_{\mathbb{Z}}$ glue is not formalized.

## Build (mathlib)

```bash
source ~/.elan/env
cd lean/CoppolaHS
lake exe cache get
lake build CoppolaHS
```

## Build Dabrowski HSFormal

```bash
cd dabrowski/upstream-palomar
lake exe cache get
lake build HSFormal
# then: lake env lean --run … or #print axioms via a small driver
```
