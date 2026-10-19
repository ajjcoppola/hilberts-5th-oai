# Hilbert–Smith counterexample ledger (executed 2026-10-16)

Status values: **SCOPED**, **HIT**, **EDGE**, **TRAP**, **PASS (static)**, **REPHRASED**.

Models are defined in [`../models/CATALOG.md`](../models/CATALOG.md). Full homology-manifold proofs and counterexamples are in [`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md).

---

## C1 — OpenAI (`paper/sections/03-localization.tex`, `04-lattice.tex`, `05-local-tests.tex`, `06-character-classes.tex`)

| Lemma | M1 Menger $\mu^n$ | M2 solenoid $\Sigma_p$ | M3 Raymond–Williams $X_n$ | M5 finite $\mathbb{Z}/p$ | E1 compact ANR | E2 homology manifold |
|-------|-----------|-------------|---------------------|----------------------------|--------|----------------------|
| `lem:orbit-injectivity` (`05-local-tests.tex:209–276`) | **SCOPED (True)** — hypotheses hold (`05-local-tests.tex:211`); conclusion $\check{H}^j(E/G;\mathbb{Q})\hookrightarrow \check{H}^j(E;\mathbb{Q})$ is true by the Bredon–Raymond–Williams / Coppola $p$-adic transfer | **SCOPED (True)** — $E/G=S^1$, $r^*:\check{H}^1(S^1;\mathbb{Q})\xrightarrow{\sim}\check{H}^1(\Sigma_p;\mathbb{Q})=\mathbb{Q}$ | **SCOPED (True)** — Yang jump $\dim_{\mathbb{Z}}(X_n/A_p)=n+2$ is $p$-torsion ($R_p(1)$); over $\mathbb{Q}$, $\dim_{\mathbb{Q}}(X_n/A_p)=n$ and $r^*$ is injective | **SCOPED (True)** — finite average $(1/p)\sum_{g\in C_p} g^*$ splits $r^*$ over $\mathbb{Q}$ | **SCOPED (True)** — holds on every compact metrizable $G$-space | **SCOPED (True)** — holds on every compact metrizable $G$-space |
| `lem:character-coproduct` (`06-character-classes.tex:36–99`) | **SCOPED (True)** — uses only compact metrizable $G$-space (`06-character-classes.tex:54`) and soft sheaves on compact Hausdorff fibers (`:74–98`) | **SCOPED (True)** | **SCOPED (True)** | **SCOPED (True)** ($\Lambda=\mu_p$) | **SCOPED (True)** | **SCOPED (True)** |
| `thm:dense-doubling` (`03-localization.tex:344–460`) | **SCOPED (Space-independent)** — purely categorical on $\mathcal{A}\subset\mathcal{C}$; applied only to target spheres $S^j$ (`04-lattice.tex:125`) | **SCOPED (Space-independent)** | **SCOPED (Space-independent)** | **SCOPED (Space-independent)** | **SCOPED (Space-independent)** | **SCOPED (Space-independent)** |
| `prop:equal-parts` + `def:character-classes` + `lem:orthogonality` (`06-character-classes.tex:108–250, 411–443`) | **SCOPED (Blocked at `:128–134`)** — requires `char:open-identification` ($c:S^d\to W^+$ homeomorphism over $X_t^\circ$ and $\omega_W\simeq\underline{\mathbb{R}}_W[d]$) | **SCOPED (Blocked at `:128–134`)** | **SCOPED (Blocked at `:128–134`)** | **SCOPED (Arithmetic consistent)** — gives $\overline{z}_i(a)=\frac{4\deg(aqc)}{p}\overline{u}_d$, which lies in $4\mathbb{Z}\overline{u}_d$ because transfer forces $p\mid\deg(aqc)$ (`lem:averaged-test`) | **EDGE** — ANR lacks $\omega_W\simeq\underline{\mathbb{R}}_W[d]$ | **REPHRASED PROOF** — extends to polyhedral HM and (via idempotent-complete $\mathcal{T}(S^d)$ + Quinn index $I(X)\neq 0$) to ENR $\mathbb{Z}$-HM; see [`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md) |
| `lem:averaged-test` (`05-local-tests.tex:135–185`) | **SCOPED (Blocked at `:153`)** — requires Euclidean ball $B(z,r)\subset W\subset\mathbb{R}^d$ | **SCOPED (Blocked at `:153`)** | **SCOPED (Blocked at `:153`)** | **SCOPED (Sanity pass)** — no open subgroup $H\subsetneq C_p$; any $C_p$-invariant map has degree $\in p\mathbb{Z}$ | **EDGE** | **REPHRASED** — odd-sphere telescope (`05-local-tests.tex:330`) + Hopf degree give a degree-one pinch on $\widehat{M}=X\times S^{d-n}$ |

---

## C2 — Dabrowski (`dabrowski/paper/HSproof.pdf` + `dabrowski/lean/`)

| Lemma | M1 Menger $\mu^n$ | M2 solenoid $\Sigma_p$ | M3 Raymond–Williams $X_n$ | M5 finite $\mathbb{Z}/p$ | E2 homology manifold |
|-------|-----------|-------------|---------------------|----------------------------|----------------------|
| Theorem 4.3 (divisibility on a free $C_p$-space, `HSproof.pdf:191–227`) | **SCOPED (True)** — $T=\mu^n/p\mathbb{Z}_p$ is a compact free $C_p$-space; every $\alpha\in L_4(A_G(T))$ has $p$-divisible signature tail. No contradiction because M1 has no $\sigma_{\mathrm{tail}}=1$ class | **SCOPED (True)** on $T=\Sigma_p/p\mathbb{Z}_p\cong S^1$ | **SCOPED (True)** on any free $C_p$-quotient | **SCOPED (True)** — for $G_i=C_p$, $P_i=\{1\}$, ordinary signature of a free $C_p$-Poincaré complex is $\in p\mathbb{Z}$ | **SCOPED (True)** on detector $T=S^{2m-1}$ |
| Lemmas 7.3–7.5 (triangulation, dual blocks, `HSproof.pdf:414–508`) | **SCOPED** — applied in manuscript only to fixed $W=S^n\times\mathbb{CP}^2$ (`HSproof.pdf:580`); fails if applied directly to $\mu^n$ | **SCOPED** | **SCOPED** | **SCOPED** | **REPHRASED** — Lemma 7.4 (`HSproof.pdf:456–463`) uses only $H_*(J_\sigma;\mathbb{Q})\cong H_*(\mathrm{pt};\mathbb{Q})$, which holds on every polyhedral $\mathbb{Q}$-HM; fails on untriangulable BFMW ENR $\mathbb{Z}$-HM |
| Proposition 13.1 (signature tail $1$, `HSproof.pdf:510–577, 932–946`) | **SCOPED (Blocked at `:518–550, 603–615`)** — chart $B(0,4)\subset\mathbb{R}^n$, vector Haar average $F_0$, and linear tracks $L_{g,h}$ fail | **SCOPED (Blocked at `:518–550`)** | **SCOPED (Blocked at `:518–550`)** | **SCOPED (Sanity pass at `:572`)** — no nested open tails $K_i=H_{\ell_i}$ with $\ell_i\to\infty$ | **SPLIT VERDICT**: **EXTENDS** to polyhedral HM and resolvable HM ($I(X)=1$); **FAILS** on non-resolvable BFMW ENR $\mathbb{Z}$-HM whenever an odd prime $p$ divides Quinn's index $I(X)\equiv 1\pmod 8$ (because Lemma 3.1 gives only $p^1\mid\sigma$, and $p\mid I(X)$ satisfies $I(X)\in p\mathbb{Z}$!) |

---

## C3 — Certificate audit (`adbrw/HS_proof` at `abb0c44` + `TauCeti` at `c7af81f0`)

| Check | Status | Evidence |
|-------|--------|----------|
| Classical statement vs `Challenge.lean` / `Solution.lean` / `Statement.lean` (M6–M8 remarks) | **SCOPED (Exact match)** | Comment-stripped `theorem hilbert_smith` in `Challenge.lean:84–118` and `Solution.lean:17–34` are character-for-character identical. `[ConnectedSpace M]`, `[LocallyCompactSpace G]`, `[ContinuousSMul G M]`, `[FaithfulSMul G M]` block M6–M8 (`Challenge.lean:59–65`). Boundary and universe-polymorphic forms are in `HilbertSmithNegK.lean:30` and `HSFormal/Universe.lean:45`. |
| `sorry` / `sorryAx` / `native_decide` / `axiom` / `constant` / `opaque` / `partial` / `unsafe` / `@[csimp]` / `@[extern]` / `@[implemented_by]` in import closure | **PASS (Static scan: 0 hits across 365 modules)** | Scanned all **239** `HSFormal` modules transitively imported by `Solution.lean` (plus `HSFormal/Universe.lean`) and all **126** `TauCeti` modules in the `public import` closure at `c7af81f0`. Only `Challenge.lean:119` (not imported by `Solution.lean`) has `sorry`. Zero kernel-bypass attributes (`@[csimp]`, `native_decide`, `trustCompiler`, `ofReduceBool`) and zero declaration shadowings of manifold/group typeclasses. |
| `#print axioms HSFormal.hilbertSmith` via live `lake build` | **UNTESTED (Environment only)** | `elan`/`lean` `v4.35.0-rc3` not installed locally (~15 GB build). Source-level audit confirms `HilbertSmithNegK.lean:21–37` discharges `NegKHighAll` with no remaining theorem hypotheses. |

---

## HM-6 — Borel-join Edwards–Walsh + Williams (executed 2026-10-18)

| Gate / check | Status | Evidence |
|--------------|--------|----------|
| G1 Williams torus bypass via EW $(n+2)$-cells | **PASS** | `scripts/hm6_equivariant_ew_harness.py`; classical Part II blocks without EW, bypasses with EW |
| G2 Pro-acyclicity degrees $>n$, growing $\dim E_i$ | **PASS** | Loop grid all PASS; `HM6_LOOP_REPORT.json` |
| G3 Local $\mathbb{Z}$-cm + BRW $n+2$ / $R_p(1)$ | **PASS** | Same harness |
| G4 Dranishnikov Prop. 3.3 cup-length $\Rightarrow\dim U=\infty$ | **PASS** | Schedule $k=m+1$, $k-l=1$; cups grow |
| Borel-join connectivity $(2m-2)\ge n+1$ | **PASS** | Free-sphere refinement (Iteration 2) |
| Lean `DranishnikovHM6.lean` | **PASS (build)** | `lake build` on `v4.35.0-rc3` |
| Continuous $clc_{\mathbb{Z}}$ glue | **EDGE (open)** | Catalog **E4**; paper Rem. `hm6-remaining` |

---

## Historical benchmark — McAuley (2001) (`arXiv:math/0103215v8`)

| Target | Status | Exact break |
|--------|--------|-------------|
| Lemmas 5–8 (`0103215v8.pdf:572–1790`) + page 33 generalization (`:1906–1908`) | **HIT (Proves too much / non-equivariant cover projection)** | Interposes a cover $U^m$ of order $n+1$ (`:578, 675`) to force $H_n(U^m;\mathbb{Z}_p)=Z_n(U^m;\mathbb{Z}_p)$, then assumes in Lemma 6 (`:1460–1466`) that $z_m^n(\Delta)=\beta_m^*\pi_{U^m}(\Delta)$ is $A_p$-equivariant on the $n$-skeleton $N(V^m_n)$. Because $\dim_{\mathbb{Z}}(M/A_p)=n+2$ (Yang 1960; Coppola 1980 [28]; Raymond–Williams `Examples_of_-adic_transformation_groups.pdf:80–86`), $U^m$ cannot be $A_p$-invariant, and the homology between $g^s(z)$ and $z$ lives in $(n+1)$-chains of $N(V^m)$, not in $N(V^m_n)$. Furthermore, Case (b) of Lemma 8 (`:1714–1790`, $k=1$) as written would rule out prime-period $C_p$-actions with small orbits. |
