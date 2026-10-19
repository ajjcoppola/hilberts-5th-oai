# Hilbert–Smith campaign (executed 2026-10-16)

First execution of the counterexample harness on two 2026 Hilbert–Smith writeups (OpenAI 2026-09-23 and Dabrowski 2026-10-08), calibrated against:
- **Alan J. Coppola (1980)**, *On $p$-adic Transformation Groups* (Ph.D. Thesis, SUNY at Binghamton; $p$-adic transfer homomorphism and algorithmic Smith–Yang exact sequences, ref. [28] in McAuley 2001),
- **Frank Raymond & R. F. Williams (1960/1963)** (`/Users/ajjc/Downloads/Examples_of_-adic_transformation_groups.pdf`),
- **Louis F. McAuley (2001)** (`/Users/ajjc/Downloads/0103215v8.pdf`), and
- the five classes of **homology and cohomology manifolds** ([`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md)).

Links:
- Executed ledger: [`LEDGER.md`](LEDGER.md)
- Homology-manifold counterexamples & rephrased proofs: [`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md)
- Model catalog: [`../models/CATALOG.md`](../models/CATALOG.md)

---

## Results of C1, C2, and C3

### C1 — OpenAI (`lem:orbit-injectivity` + equal-parts Witt machine)
- **`lem:orbit-injectivity` (`05-local-tests.tex:209–276`) and `lem:character-coproduct` (`06-character-classes.tex:36–99`)**:
  Both lemmas **leak across the manifold gate** — their hypotheses hold verbatim on M1 (Menger $\mu^n$), M2 (solenoid $\Sigma_p$), M3 (Raymond–Williams $X_n$), M5 (finite $\mathbb{Z}/p$), E1 (compact ANR), and E2 (homology manifolds).
  **However, neither is a HIT**, because their conclusions are **true on all of those models**:
  - By the classical **$p$-adic transfer theorem** (Bredon–Raymond–Williams 1961 Lemma 5.1; Raymond 1961 Lemma 5; Coppola 1980 $p$-adic transfer), $r^* : \check{H}^*(E/G; \mathbb{Q}) \xrightarrow{\sim} \check{H}^*(E; \mathbb{Q})^G$ is split injective for every compact metrizable $\mathbb{Z}_p$-space $E$.
  - On M3 (`Examples_of_-adic_transformation_groups.pdf:80–86`), the Yang jump $\dim_{\mathbb{Z}}(X_n/A_p) = n + 2$ sits entirely in $p$-torsion ($R_p(1) = \mathbb{Z}[1/p]/\mathbb{Z}$ and $\mathbb{F}_p$-cohomology); over $\mathbb{Q}$, $\dim_{\mathbb{Q}}(X_n/A_p) = n$.
- **Where the manifold gate actually locks (`06-character-classes.tex:128–134`)**:
  `prop:equal-parts` requires `char:open-identification` ($A_t|_{X_t^\circ} \simeq (Rt_*\mathcal{H})|_{X_t^\circ}$) and `lem:orthogonality` ($G$ acting by isometries of the orientation pairing $\alpha_t|_{X_t^\circ}$ via $\omega_W \simeq \underline{\mathbb{R}}_W[d]$). That blocks M1, M2, and M3, and on M5 (finite $\mathbb{Z}/p$) the equal-parts identity $\overline{z}_i(a) = \frac{4\deg(aqc)}{p}\overline{u}_d$ is non-contradictory because transfer forces $p \mid \deg(aqc)$.

### C2 — Dabrowski (Theorem 4.3 divisibility vs. §§7–13 realization)
- **Theorem 4.3 (`HSproof.pdf:191–227`)**:
  Applies verbatim to any compact free $C_p$-space $T$ (including $T = \mu^n/p\mathbb{Z}_p$ on M1 and $T = \Sigma_p/p\mathbb{Z}_p \cong S^1$ on M2), where it proves a **true** statement: every class in $L_4(A_G(T))$ has ordinary signatures eventually divisible by $p$.
- **Lemmas 7.3–7.5 (`HSproof.pdf:414–508`) & Proposition 13.1 (`:932–946`)**:
  In the manuscript, Lemmas 7.3–7.5 are applied only to the fixed standard PL manifold $W = S^n \times \mathbb{CP}^2$ (`HSproof.pdf:580`), where $S^n$ is the one-point compactification of a single Euclidean chart of $M$ (`:518`). M1–M3 fail at the Euclidean chart $B(0,4) \subset \mathbb{R}^n$, vector Haar averaging $F_0$, and linear tracks $L_{g,h}$ (`:518–615`).
  - **Surprise on polyhedral $\mathbb{Q}$-homology manifolds**: Lemma 7.4 (`HSproof.pdf:456–463`) only uses that the shifted rational cochain complex of $\mathrm{link}_K(\sigma)$ has $H_r(J_\sigma; \mathbb{Q}) = \mathbb{Q}$ ($r=0$) and $0$ ($r>0$), so dual-block acyclicity holds on every polyhedral $\mathbb{Q}$-homology manifold.
  - **Break on non-resolvable ENR $\mathbb{Z}$-homology manifolds when $p \mid I(X)$**: Because Lemma 3.1 (`HSproof.pdf:139`, `AlgebraicReduction.lean:24`) uses $\Phi_{p^a}(1) = p$, Theorem 4.3 only yields **single-$p$ divisibility** ($p^1 \mid \sigma$, never $p^k \mid \sigma$). On a Bryant–Ferry–Mio–Weinberger non-resolvable ENR $\mathbb{Z}$-homology manifold $X$ with Quinn index $I(X) \equiv 1 \pmod 8$, the local signature is $I(X)$; whenever an odd prime $p$ divides $I(X)$ (e.g. $I(X) = 9, p = 3$ or $I(X) = 25, p = 5$), $I(X) \in p\mathbb{Z}$ **fails to contradict**!

### C3 — Dabrowski Lean Certificate (`adbrw/HS_proof` at `abb0c44` + `TauCeti` at `c7af81f0`)
- **Statement check (`Challenge.lean` vs `Solution.lean`)**: Comment-stripped `theorem hilbert_smith` declarations are character-for-character identical (`EQUAL: True`). M6–M8 are explicitly blocked by `[ConnectedSpace M]`, `[LocallyCompactSpace G]`, and `[ContinuousSMul G M]`.
- **Static TCB / `sorry` / Shadowing scan across 365 modules**:
  Scanned all **239** `HSFormal` modules in the import closure of `Solution.lean` (plus `HSFormal/Universe.lean`) and all **126** `TauCeti` modules in the `public import` closure at `c7af81f0`.
  - Non-comment occurrences of `sorry`, `sorryAx`, `axiom`, `constant`, `opaque`, `partial`, `unsafe`, `native_decide`, `implemented_by`, `extern`, `csimp`, `trustCompiler`, `ofReduceBool`, `lcProof`, `lcErased`: **0** (outside `Challenge.lean:119`).
  - Declaration shadowing of manifold/group typeclasses: **0**.
  - Only live kernel compilation (`lake build` + `#print axioms HSFormal.hilbertSmith`) remains unexecuted locally due to missing `elan` (~15 GB build).

---

## Homology-Manifold Outcome (Summary of [`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md))

1. **Historical HIT diagnosed (`0103215v8.pdf`)**: McAuley (2001) interposes an order-$(n+1)$ refinement $U^m$ (`0103215v8.pdf:578, 675`) to force unique $n$-cycles on the $n$-skeleton $N(V^m_n)$, then treats $z_m^n(\Delta) = \beta_m^*\pi_{U^m}(\Delta)$ as $A_p$-equivariant on $N(V^m_n)$ in Lemma 6 (`:1460–1466`). Because $\dim_{\mathbb{Z}}(M/A_p) = n + 2$ (Yang 1960; Coppola 1980 [28]; Raymond–Williams 1960), $U^m$ cannot be $A_p$-invariant, and the homology between $g^s(z)$ and $z$ lives in $(n+1)$-chains of $N(V^m)$ (the Coppola / Smith–Yang transfer cocycle).
2. **Explicit Counterexamples (HM-1 & HM-2)**: Faithful continuous $\mathbb{Z}_p$-actions exist on countable-component manifolds / shrinking sphere necklaces $X$ (via $\mathbb{Z}_p \twoheadrightarrow C_{p^i}$ on piece $i$, breaking connectedness or local homology at the junction $x_\infty$) and on non-$clc$ $\mathbb{Q}$-cohomology manifolds lacking $\mathbb{F}_p$-regularity (Raymond 1961 Thm 2 / 1965 p. 1376).
3. **Unconditional Proofs (HM-3 & HM-4)**: Both OpenAI and Dabrowski extend unconditionally to all connected **polyhedral $L$-homology $n$-manifolds** ($L \neq 0$, via density and connectivity of $X_{\mathrm{man}} = X \setminus |K^{(n-2)}|$, Theorem 3.1) and to all connected **$\mathbb{F}_p$-cohomology $n$-manifolds with $X_{\mathrm{man}} \neq \varnothing$** (via global Newman on $\mathbb{F}_p$-cm, Theorem 3.2).
4. **Quinn-Index Separation on Nowhere-Euclidean ENR $\mathbb{Z}$-Homology Manifolds (HM-5)**: On Bryant–Ferry–Mio–Weinberger spaces ($X_{\mathrm{man}} = \varnothing$, $I(X) \equiv 1 \pmod 8$), Dabrowski's single-$p$ divisibility ($I(X) \in p\mathbb{Z}$) breaks whenever $p \mid I(X)$ (Theorem 4.1), whereas OpenAI's idempotent-complete category $\mathcal{T}(S^d)$ accepts the ENR retract $\widehat{M} = X \times S^{d-n}$ and divides $4 I(X)$ by $p^k$ for arbitrarily large $k$, killing every $I(X) \neq 0$ (Theorem 4.2).

---

## HM-6 update (executed 2026-10-18)

Sherlock + `/loop` campaign on the infinite-covering-dimension bullseye:

| Deliverable | Result |
|-------------|--------|
| Symbolic harness `scripts/hm6_equivariant_ew_harness.py` | Gates G1–G4 + Borel-join **PASS** on grid $(n,p,\mathrm{stages})\in\{(5,3,4),(7,5,3),(6,3,5),(9,7,4)\}$ |
| Loop log | [`HM6_LOOP_LOG.md`](HM6_LOOP_LOG.md) / [`HM6_LOOP_REPORT.json`](HM6_LOOP_REPORT.json) |
| Lean `DranishnikovHM6.lean` | Builds on Lean `v4.35.0-rc3` (`lake build` clean) |
| Paper §1.5 + §8 expansion | `papers/padic-homology-manifolds/main.pdf` (18 Oct 2026) |
| Remaining gate | Continuous-limit $clc_{\mathbb{Z}}$ Poincaré glue (catalog **E4**, EDGE — not HIT) |

See [`HOMOLOGY_MANIFOLDS.md`](HOMOLOGY_MANIFOLDS.md) §7 and catalog row **E4**.
