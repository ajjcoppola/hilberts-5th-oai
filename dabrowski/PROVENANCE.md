# Provenance

**AI disclaimer:** The reverse-verification notes in this folder are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola. Dabrowski’s vendored paper and Lean tree keep their own authorship.

Vendored (sparse) from A. Dabrowski’s Hilbert–Smith repository:

- **Upstream:** https://github.com/adbrw/HS_proof
- **Upstream HEAD at vendor time:** `abb0c44d58d711235f20b666ef422a4ea87b9add` (2026-10-08 09:06:46 UTC)
- **Author / date (paper):** A. Dabrowski’s AI agents / October 8, 2026
- **Title:** *Integral tail signatures and the Hilbert–Smith conjecture* (`HSproof.pdf`, 17 pp.)
- **PDF SHA-256:** `e305fd474909694af1e032ab863d26411f5e9fd9c38e7001f5fac14fe19e5e75` (549856 bytes)
- **Lean toolchain:** `leanprover/lean4:v4.35.0-rc3`
- **mathlib:** `1a547d8a48a8fa7877d2decb69d7294723bb0187`
- **TauCeti:** `c7af81f021f76fa11afcd61c894e5fc861ab6e78`
- **HSFormal modules (upstream count):** 238 `.lean` files under `HSFormal/`

## Contents here

- `paper/HSproof.pdf` — compiled preprint
- `paper/README.md` — upstream README (Theorem 1.1 / Corollary 1.2, Lean claims)
- `paper/lakefile.toml`, `paper/lake-manifest.json`, `paper/lean-toolchain`, `paper/comparator.json`
- `paper/Challenge.lean`, `paper/Solution.lean`, `paper/HSFormal.lean` — statement / solution / library root
- `lean/` — **sparse** copy of load-bearing modules only (not the full 238-module tree, not `.lake/`, not `HilbertSmithLean4.zip`)

Sparse Lean files: `Challenge`, `Solution`, `HSFormal`, `Statement`, `HilbertSmith`, `HilbertSmithNegK`, `HilbertSmithFinal`, `HilbertSmithModel`, `EquivariantSignature`, `CharacterDetector`, `ChartData`, `Germ`, `CornerClass`, `AlgebraicReduction`, `BoundaryReduction`, `ControlledDuality`.

This copy is for reverse-verification only. It is not affiliated with A. Dabrowski. The full Lean tree remains at the upstream URL; this audit did **not** run `lake build` or `#print axioms`.

---

## Palomar full checkout (2026-10-17) — local optional, not in published tree

For `lake build` and `#print axioms`, clone Dabrowski’s tree locally (gitignored
from this published audit repo to avoid multi-GB `.lake` / nested git):

```bash
git clone https://github.com/adbrw/HS_proof.git dabrowski/upstream-palomar
cd dabrowski/upstream-palomar
git checkout palomar-review/module-system-20261015
# expect tip near b75523f0036bc857f31620ee18af970151036311
lake exe cache get && lake build HSFormal
```

Local axiom print (when rebuilt): `propext`, `Classical.choice`, `Quot.sound`
(see [`lean-extension/print_axioms.txt`](lean-extension/print_axioms.txt) /
[`lean-extension/BUILD_STATUS.md`](lean-extension/BUILD_STATUS.md)).
