# Lean build status (2026-10-17)

## Dabrowski HSFormal (palomar)

| Field | Value |
|-------|--------|
| Pin | `b75523f0036bc857f31620ee18af970151036311` |
| Branch | `palomar-review/module-system-20261015` |
| Path | `dabrowski/upstream-palomar/` |
| Toolchain | `leanprover/lean4:v4.35.0-rc3` |
| `lake build HSFormal` | **SUCCESS** |
| `#print axioms HSFormal.hilbertSmith` | `propext`, `Classical.choice`, `Quot.sound` |

See `print_axioms.txt`, `lake_build_HSFormal.log`.

## CoppolaHS extension

| Field | Value |
|-------|--------|
| Path | `lean/CoppolaHS/` |
| `lake build CoppolaHS` | **SUCCESS** (ChallengeENR uses intentional `sorry`) |
| Modules | CyclotomicTower, QuinnIndex, PadicExclusionENR, ChallengeENR, SolutionENR |

See `coppolahs_build.log`.
