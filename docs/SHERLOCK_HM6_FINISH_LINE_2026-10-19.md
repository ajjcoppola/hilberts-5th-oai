# Sherlock: HM-6 finish line — solenoid + cyclic towers

**AI disclaimer:** This session log is AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola.

**Date:** 2026-10-19  
**Repo:** hilberts-5th-oai @ `checkpoint/hm6-2026-10-18`  
**Goal:** Effective $A_p$ (or solenoidal) action on a $\mathbb{Z}$-cohomology $n$-manifold, built one complex at a time.

## Where we are (one screen)

| Layer | Status |
|-------|--------|
| Classical manifold / ENR (HM-3..HM-5) | Exclusion relative to OpenAI/Dabrowski; bounded-dim inverse limits blocked (Thm G) |
| Explicit weak counterexamples | HM-1 (coeff), HM-2 (necklace) — **not** $clc_{\mathbb{Z}}$ $n$-cms |
| HM-6 architecture | Borel-join EW + Williams: gates G1–G4 **PASS** (symbolic) |
| Finish line | Continuous $clc_{\mathbb{Z}}$ Poincaré **glue** across $\partial\sigma$ over Yang $(n+2)$ orbit space — **OPEN** |

We are **not** missing “another exclusion theorem.” We are missing one geometric assembly step that turns a compatible inverse system of (growing-dim) complexes into a single $clc_{\mathbb{Z}}$ $n$-manifold with a free/effective $A_p$-action.

## Step 1 — Reflect (7 construction choices)

1. **Pure solenoid (fixed odd sphere dim):** $S^{2m-1}\xleftarrow{\times p}S^{2m-1}\to\cdots$ → free $A_p$, but $\check{H}^{2m-1}\cong\mathbb{Z}[1/p]$ ⇒ not $\dim_{\mathbb{Z}}=n$ (paper Prop. drw-blueprint (b)).
2. **Circle-bundle / $S^1$-action tower:** lens spaces $L^{2m-1}(p^k)$ with $\times p$ on universal covers — Floyd / Dranishnikov essential lens sequence; free $A_p$ on cell-like continuum $E$, orbit rough $BA_p$.
3. **Finite recursive cyclic:** compatible free $C_{p^i}$ on finite complexes $E_i$, bonding equivariant under $C_{p^{i+1}}\twoheadrightarrow C_{p^i}$ — Williams / Raymond–Williams style.
4. **Bounded-dim $n$-skeleton retraction:** forces Williams Part II torus no-go (G1 without EW).
5. **Growing-dim + Edwards–Walsh kill of $H^{>n}$:** keeps $\dim_{\mathbb{Z}}\le n$, allows $\dim=\infty$ (HM-6 escape).
6. **Borel-join free sphere:** $EW\times_{C_{p^{i+1}}}S^{2m-1}$ supplies free action + $(2m-2)$-connectivity without Smith $\chi=1$ (gates BJ/G2).
7. **ENR / finite-dim ANR target:** blocked for free $A_p$ by relative E/F + Thm G — wrong finish line if we want an *example*.

## Step 2 — Distill (3 paths to run)

| Rank | Path | Why |
|------|------|-----|
| **P1 (primary)** | **Cyclic recursive + growing dim + EW** — one finite complex $E_i$ per stage | Matches harness; escapes Thm G Case 2; gates already green |
| **P2 (parallel)** | **Solenoid / lens / circle-bundle trunk** — essential lens sequence with *increasing* $m_i$, then EW-kill integral tops | Closest to “construct like a solenoid”; Dranishnikov 2016 program |
| **P3 (finish)** | **$clc_{\mathbb{Z}}$ glue** of either trunk over Yang $(n+2)$ orbit | Sole remaining geometric gate (Rem. hm6-remaining) |

Run **P1 and P2 in parallel** as two trunks that share the same glue (P3).

## Step 3 — Investigate (what the repo already proves vs models)

- **Blocked:** fixed-dim $\times p$ on $S^{2m-1}$ alone → solenoid, not $n$-cm (`main.tex` ~940–948).
- **Blocked:** force bonding into $n$-skeleton → Williams torus (`main.tex` ~975–991; harness G1 without EW).
- **Open but scaffolded:** $E_{i+1}=(E_i\Delta_q EW_d)\times_{C_{p^{i+1}}}S^{2m_{i+1}-1}$ with $d_i\uparrow$ — G1–G4 PASS on grid (`HM6_LOOP_LOG.md`).
- **Must hold in limit:** BRW $\dim_{\mathbb{Z}}(X/A_p)=n+2$ with $R_p(1)$ top — constraint, not contradiction (G3).
- **Harness honesty:** G3/G4 are *symbolic* models of local duality / Prop. 3.3, not a geometric simplicial construction yet.

## Step 4 — Analysis: dual finish-line constructions

### Trunk A — Solenoid / circle-bundle style (P2)

Proceed **one odd sphere / lens stage at a time**:

```text
Stage i:  S^{2m_i-1}  --free C_{p^{k_i}}-->  L^{2m_i-1}(p^{k_i})
Bonding:  S^{2m_{i+1}-1} --φ_i (deg p^{…})--> S^{2m_i-1}   (nullhomotopic on spheres; essential on lenses)
Grow:     m_{i+1} > m_i   so fiber dim > n+1
Kill:     route through EW / K(Z, ·) so lim H^{>n} = 0 over Z
Limit:    E = lim S^{2m_i-1}   (cell-like / UV^{n-1} continuum, free A_p)
          B = lim L^{…}        (orbit; K-theory cup-length → dim B = ∞)
```

- **Circle action view:** each stage is an $S^1$-quotient of a free linear circle action on $S^{2m_i-1}$; $C_{p^k}\subset S^1$ is the finite recursive piece; inverse limit of the circle quotients is the $p$-adic / solenoidal dynamics.
- **Pitfall:** if $m_i$ stays fixed → classical solenoid, fails $\dim_{\mathbb{Z}}=n$.
- **Dranishnikov link:** essential lens sequence + Prop. 3.3 cup-length (already Gate G4 schedule).

### Trunk B — Finite recursive cyclic complexes (P1)

Proceed **one finite simplicial complex at a time** (current harness architecture):

```text
E_0 = n-sphere or n-cm polyhedron, trivial / C_1
E_{i+1} = (E_i  Δ_{q_i}  EW_{d_i}(E_i, Z, n))  ×_{C_{p^{i+1}}}  S^{2m_{i+1}-1}
π_{i+1}: E_{i+1} → E_i   equivariant for C_{p^{i+1}} ↠ C_{p^i}
X = lim E_i ,   A_p = lim C_{p^i} acts effectively (∩ ker = 0)
```

- Each step: attach EW cells (kill $H^{>n}$), Borel-join free odd sphere (free $C_{p^{i+1}}$, acyclic through $n+1$), optional Williams splice on stars.
- **Infinite-dim complex option:** replace finite $EW_{d_i}$ truncation by a longer Postnikov skeleton when needed; dimension still grows stagewise.

### Shared finish (P3) — the only open gate

For either trunk, after bonding maps are defined:

1. Verify **pro-$clc_{\mathbb{Z}}$** / Vietoris–Begle through degree $n$ on fibers.
2. Glue local orientation classes across $\partial\sigma$ when the block sits over the **orbit** complex of dim$_{\mathbb{Z}}=n+2$.
3. Check limit is **connected, locally connected**, $H^*(X,X\setminus\{x\};\mathbb{Z})\cong H^*(\mathbb{R}^n,\mathbb{R}^n\setminus 0)$.
4. Check action of $A_p$ is **jointly continuous and effective** (standard for inverse limits of compatible free $C_{p^i}$).

Success ⇒ HM-6 example. Failure modes: local $H_{<n}$ junk (necklace), solenoid tail (forgot EW kill), or Part II if someone re-imposes $n$-skeleton retraction.

## Step 5 — Suggestions (concrete next work)

| # | Action | Trunk | Test |
|---|--------|-------|------|
| 1 | Implement **geometric** stage-0→1: explicit lens / EW cell attachment in a small simplicial model (e.g. $n=3$ or $5$, $p=3$) | A+B | Compare cohomology to harness G2/G3 |
| 2 | Extend harness with a **solenoid trunk** mode: fixed vs growing $m_i$; assert FAIL on fixed, PASS schedule on growing+EW | A | New gate `G0-solenoid-tail` |
| 3 | Formalize glue hypotheses as Lean `Prop`s (statement layer) before geometry | P3 | `DranishnikovHM6.lean` extension |
| 4 | Recruit CD/EW coauthor for P3 (see `OUTREACH_COLLABORATORS.md`) | P3 | Human review of Rem. hm6-remaining |
| 5 | Do **not** chase ENR/BFMW free $A_p$ as the example — wrong class | — | Matrix HM-5 vs HM-6 |

**Recommended order:** (2) solenoid diagnostic in harness → (1) one explicit geometric stage → (3)+(4) glue.

## Step 6 — Cleanup

No temporary diagnostic instrumentation added this session. No cleanup approval needed.

## Verdict

Finish line = **build Trunk A (lens/solenoid) and Trunk B (cyclic $E_i$) stage-by-stage with growing dimension + EW kill, then close $clc_{\mathbb{Z}}$ glue (P3).** Algebraic scaffolding is green; geometry of one real stage + glue is the remaining research.
