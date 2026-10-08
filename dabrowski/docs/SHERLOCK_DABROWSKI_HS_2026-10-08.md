# Sherlock session — Dabrowski Hilbert–Smith preprint

**Date:** 2026-10-08  
**Workspace:** `/Users/ajjc/proj/Hilberts-5th-OAI`  
**Protocol:** Sherlock Mode (6 steps) + plan `dabrowski_hs_sherlock`

## Step 1 — candidate failure sources (wide net)

1. Newman / chart reduction (same family as OpenAI `prop:chart-reduction`).
2. Integral tail construction: \(L_4\) / Witt / Karoubi / Ranicki Poincaré pairs.
3. \(p\)-divisibility / transfer / averaging on finite covers of \(T\).
4. Negative-\(K\) / `NegKHighAll` / decoration-map bijectivity.
5. Lean vs PDF gap: `sorry`, extra axioms, statement mismatch.
6. Homotopy / duality signs (cylinder / dual-block foot-guns).
7. Overclaim on sponges/solenoids if hypotheses are weaker than manifolds.

## Step 2 — distill (most likely)

- **A.** Signature-tail lattice / integer signatures independent of \(p\)-power.
- **B.** Transfer/averaging multiplies by \(p\) without leaving the integral setting.
- **C.** Lean certificate actually proves the published theorem.

## Step 3 — investigate

- Vendored `HSproof.pdf` (SHA-256 `e305fd47…`) and sparse Lean from https://github.com/adbrw/HS_proof at `abb0c44`.
- Line-by-line on load-bearing PDF lemmas (not all 238 Lean modules).
- Same sponge matrix as OpenAI; comparison table in `05_vs_openai.md`.

## Step 4 — analysis

- **Mechanism:** integer signature tail: realization gives \(\sigma_{\mathrm{tail}}=1\); divisibility gives eventually \(p\mid\sigma\); hence \(1\in p\mathbb{Z}\). Same obstruction class as OpenAI, packaged as Ranicki \(L_4\) + \(\mathbb{CP}^2\) rather than Witt sheaves on \(S^d\).
- **Audit (A–C):** 0 FAIL on PDF load-bearing lemmas. WEAK: Prop. 3.2 / NegK, Lemma 4.2 MV nilpotence, graph corner §§10–11, Prop. 12.4 signs, Lean axiom print.
- **Sanity:** finite \(\mathbb{Z}/p\) breaks at unbounded tail / degree-one Haar.
- **Sponges:** Menger/solenoid/RW break at chart / PL dual cells; no overclaim. Homology manifolds OPEN EDGE.
- **Public:** no technical rebuttal as of 2026-10-08 morning. Garbled third-party README paste listed `HSproof.pdf` as an axiom; vendored README does not.

## Step 5 — follow-ups

1. Independent `#print axioms HSFormal.hilbertSmith` after `lake build`.
2. Expert check of Lemma 4.2 against [CP95] ultimate \(L\) Mayer–Vietoris.
3. Expert check of Prop. 12.4 iterated boundary evaluation.
4. MO rewrite as Euclidean-structure question citing both proofs (not work-checking).

## Step 6 — cleanup

`/tmp/hs_dabrowski` clone may be deleted after confirming `dabrowski/` is complete. No temporary diagnostic code was added to the proof. Full `HSFormal/` (238 modules) and `HilbertSmithLean4.zip` were **not** copied into the repo on purpose (sparse vendor).

## Deliverables

- `dabrowski/PROVENANCE.md`, `dabrowski/paper/`, `dabrowski/lean/` (sparse)
- `dabrowski/docs/01`–`05`, lemma ledger, this log
- `dabrowski/docs/Dabrowski_HS_Audit.pdf`
- Root `README.md` two-proof index; `docs/POST_DRAFTS.md` MO rewrite
