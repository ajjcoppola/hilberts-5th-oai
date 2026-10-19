# Sherlock Session: HM-6 Dranishnikov–Williams Bullseye

**Date:** 2026-10-18  
**Repo:** Hilberts-5th-OAI  
**Mode:** Sherlock + `/loop` (symbolic harness + Lean)

## Question

Can a free $A_p$-action exist on a compact connected $\mathbb{Z}$-cohomology $n$-manifold $X$ with $\dim_{\mathbb{Z}}X=n<\infty$ and $\dim X=\infty$ (HM-6), escaping OpenAI ENR rephrase, Dabrowski $k$-tower, and bounded-dimension Euler obstruction?

## Step 1 — Candidate mechanisms (7)

1. Williams $K\Delta_q X$ splicing (1967 Part II torus no-go under $n$-skeleton retraction).
2. Edwards–Walsh $EW(K,\mathbb{Z},n)$ killing $H^{>n}$ with growing topological dim.
3. Dranishnikov / DFW $K$-theory cup-length forcing $\dim U=\infty$.
4. Essential lens sequences / rough classifying space $E=\varprojlim S^{2n_i-1}$.
5. Local $clc_{\mathbb{Z}}$ / $H^n$ preservation under pro-acyclic bonding.
6. BRW constraint: any gm over $\mathbb{Z}$ still has $\dim_{\mathbb{Z}}(X/A_p)=n+2$.
7. Bypass of Williams Part II by dropping $n$-skeleton retraction.

## Step 2 — Distilled targets (3)

- **T1:** Bypass Williams Part II via EW $(n+2)$-cells (Gate G1).
- **T2:** Equivariant pro-acyclic bonding preserving local $H^n$ via Borel join with free $S^{2m-1}$ (Gates G2–G3 + BJ).
- **T3:** Unbounded $K$-theory cup-length on every neighborhood (Gate G4).

## Step 3 — Code / harness path

- Wrote `scripts/hm6_equivariant_ew_harness.py` (G1–G4 + BJ).
- Iteration 1: G4/BJ failed under naive `min(conn_F,2m-2)` and bad Prop. 3.3 schedule.
- Iteration 2: free-sphere Borel join uses connectivity $2m-2$; Prop. 3.3 with $k=m+1$, $k-l=1$.
- Iteration 3–4: `/loop` grid all PASS (`HM6_LOOP_LOG.md`).
- Lean: `lean/CoppolaHS/CoppolaHS/DranishnikovHM6.lean` builds (`lake build` clean).
- Paper: §1.5 seven contributions + §8 Borel-join architecture; `main.pdf` compiled.

## Step 4 — Analysis

Finite-stage algebraic gates hold. BRW $n+2$ orbit jump is a *constraint*, not a contradiction. The sole outstanding geometric step is continuous-limit $clc_{\mathbb{Z}}$ Poincaré duality gluing across simplex boundaries when pulling EW blocks over the Yang $(n+2)$-orbit space. HM-6 remains **EDGE / open candidate**, not a claimed HIT.

## Step 5 — Artifacts

| Artifact | Path |
|----------|------|
| Harness | `scripts/hm6_equivariant_ew_harness.py` |
| Loop | `counterexamples/hilbert-smith/HM6_LOOP_LOG.md` |
| Lean | `lean/CoppolaHS/CoppolaHS/DranishnikovHM6.lean` |
| Paper | `papers/padic-homology-manifolds/main.pdf` |
| Pack | `presentations/padic-homology-2026/padic-homology-2026-pack.zip` |
| Catalog | E4 in `counterexamples/models/CATALOG.md` |

## Step 6 — Logs

No temporary debug logs were added to production Lean/paper sources beyond the intentional harness report JSON. No cleanup approval needed.
