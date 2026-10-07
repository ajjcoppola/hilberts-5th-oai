# Sherlock session — Hilbert–Smith OpenAI preprint

**Date:** 2026-10-07  
**Workspace:** `/Users/ajjc/proj/Hilberts-5th-OAI`  
**Protocol:** Sherlock Mode (6 steps) + plan `hilbert-smith_reverse_audit`

## Outcome

Targeted reverse-verification of OpenAI’s Sept 23, 2026 Hilbert–Smith preprint.

- **Mechanism:** integrality vs \(p^k\)-divisibility of sheaf Witt / signature classes on \(S^d\), not Yang dim-raising.
- **Audit (Targets A–C):** 0 FAIL, ~4 WEAK (dense-doubling, witt-localization/BW, character-coproduct, equal-parts).
- **Sanity:** finite \(\mathbb{Z}/p\) breaks at `lem:averaged-test` (good).
- **Sponges:** Menger/solenoid/RW break at chart/Newman; no “proves too much” gap. Homology manifolds flagged OPEN EDGE.
- **Public:** no technical rebuttal as of 2026-10-07; no Lean for this proof.

## Deliverables

- `paper/` vendored (SHA `adc7f12…`)
- `docs/01`–`04`, `lemma_dependency_ledger.md`, `README.md`
- Canvas: `canvases/hilbert-smith-audit.canvas.tsx`

## Follow-ups (Step 5)

1. Expert check of WEAK lemmas (Pardon / Woolf / Balmer–Walter users).
2. Lean targets: `thm:dense-doubling`, `prop:equal-parts`, `thm:sphere-lattice`.
3. Homology-manifold scope note if literature finds \(\mathbb{Z}_p\) actions there.

## Cleanup (Step 6)

`/tmp/hs_paper` scratch copy may be deleted after confirming `paper/` is complete. No temporary diagnostic code was added to the proof.
