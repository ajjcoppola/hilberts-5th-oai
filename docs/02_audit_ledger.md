# Targeted audit ledger (Sherlock targets A–C)

**Scope:** line-by-line on load-bearing lemmas only (plan: targeted audit).  
**Grades:** `PASS` = argument appears complete and correctly cited; `WEAK` = plausible but citation gap, omitted routine detail, or hypothesis that needs expert check; `FAIL` = identified break.  
**Overall targeted verdict:** **No FAIL found.** Several `WEAK` items remain the natural places for independent expert / Lean scrutiny. The proof does **not** “prove too much” on known sponge models (see [`03_sponge_stress_test.md`](03_sponge_stress_test.md)).

---

## Target A — Homotopy invariance + bounded lattice

### `thm:homotopy` — Homotopy invariance  
**File:** [`paper/sections/02-categories.tex`](../paper/sections/02-categories.tex) ~701–739  
**Grade: PASS (with WEAK dependence on cylinder signs)**

- Builds on `cat:endpoint-forms` (neutral cylinder form with opposite endpoint signs) and `prop:test-pushforward`.
- Correctly notes that the homotopy need not be proper: objects have compact support in \(I\times K\).
- Implements Woolf’s interval argument inside the *generated* continuous category \(\mathcal{T}\), without requiring constructible images.
- **Residual risk:** absolute normalization of the cylinder scalar \(c\) is deferred to the appendix (`app:duality-signs`). Sign bookkeeping is historically delicate; appendix exists and is cited, so not FAIL.

### `thm:bounded-comparison` — Bounded \(\mathcal{P}\to\mathcal{T}\) comparison on spheres  
**File:** [`paper/sections/04-lattice.tex`](../paper/sections/04-lattice.tex) ~125–185  
**Grade: PASS**

- Inducts on sphere dimension via pole covers \(U,V\), localization sequences, `prop:open-cover` density, and `thm:dense-doubling` (exponent 2).
- Finite diagram chases (`lat:finite-chases`) give a uniform \(2\)-power annihilating ker/coker in every degree.
- Exponent bookkeeping (`lat:exponent-bookkeeping`) is explicit (\(e_j=3(9^j-1)/4\)); only existence of some fixed \(e_d\) is used later.
- **Why this is load-bearing:** without a *uniform* denominator independent of later \(k\), the equal-parts arithmetic cannot contradict.

### `prop:sphere-rank` — Rational sphere calculation  
**File:** `04-lattice.tex` ~203–251  
**Grade: PASS**

- Mayer–Vietoris / localization induction shows
  \(G_r(S^j)\otimes\mathbb{Q}\simeq (G_r(\mathrm{pt})\oplus G_{r-j}(\mathrm{pt}))\otimes\mathbb{Q}\)
  for both \(F=W(\mathcal{P})\) and \(E=W(\mathcal{T})\).
- For odd \(d\), \(E_d(S^d)\otimes\mathbb{Q}\) is 1-dimensional.
- Dense doubling supplies rational isomorphism of relative groups; no claim of integral isomorphism \(\mathcal{P}\to\mathcal{T}\) is needed here.

### `thm:sphere-lattice` — Fixed sphere lattice  
**File:** `04-lattice.tex` ~370–398  
**Grade: PASS**

- Combines rational 1-dimensionality with `prop:generic-signature` (semialgebraic local signature \(\mathbb{Z}\overline{u}_{F,d}\)) and the \(2^{e_d}\) cokernel bound.
- Result: \(\operatorname{im}(E_d(S^d)\to E_d(S^d)\otimes\mathbb{Q})\subseteq L_d^{-1}\mathbb{Z}\overline{u}_d\) with \(L_d=2^{e_d}\) **independent of action, \(p\), and \(k\)**.
- **Key meta-point:** rational equivalence alone would lose the denominator bound (remarked in §1); the paper’s integral comparison is essential.

### `prop:generic-signature` (supporting)  
**Grade: PASS**

- Hardt triviality ⇒ dense open where cohomology is finite locally constant; local signature on small balls is integral and respects Witt relations.
- Standard semialgebraic topology; correctly limited to \(\mathcal{P}\), then transferred.

---

## Target B — Germs, localization, dense doubling

### `thm:germs` — Germ description of quotient Homs  
**File:** [`paper/sections/03-localization.tex`](../paper/sections/03-localization.tex) ~165–219  
**Grade: PASS**

- Cutoff (`lem:cutoff`) + compact-support characterization (`prop:compact-support`) produce roofs representing germs.
- Fullness/faithfulness for summand sources handled carefully.
- This is the device that lets character projectors live on \(X\setminus\{b\}\) while classes live in \(E_d(X)\).

### `thm:witt-localization` — Balmer–Walter LES  
**File:** `03-localization.tex` ~227–293  
**Grade: WEAK (citation-correct, hypothesis-heavy)**

- Invokes Balmer–Walter 2002, Theorem 2.1.
- Checks: thick duality-stable kernel, essential smallness, \(2\) invertible in Hom groups (real vector spaces), \(\mathrm{TR4}^+\), duality preserves \(S\).
- **Why WEAK not PASS:** correctness reduces to whether Balmer–Walter applies verbatim to these *generated* subcategories of \(D^b(\mathrm{Sh}_{\mathbb{R}}(X))\). The checklist looks complete; an independent reader should still verify against the published hypotheses (the paper notes BW removes the earlier weak-cancellation assumption).

### `prop:open-cover` — Dense inclusion from open covers  
**File:** `03-localization.tex` ~301–334  
**Grade: PASS**

- Germs identify the two quotient Hom groups; cutoff proves every object is a summand of an extended object.
- Feeds the sphere induction in Target A.

### `thm:dense-doubling` — Explicit \(d\) with \(\iota d=d\iota=2\)  
**File:** `03-localization.tex` ~344–460  
**Grade: WEAK**

- Constructs \(D(q)=q\perp q\perp H(x[1])\) in the smaller category via \(y\oplus y[1]\in\mathcal{A}\).
- Neutrality descent: builds a large lagrangian \(L\) and argues \(L\in\mathcal{A}\) by successive cones/split triangles.
- Parallel to Hornbostel–Schlichting cofinality, but self-contained.
- **Why WEAK:** the lagrangian membership argument (`L` via cones of \(a\oplus 0\), etc.) is the longest purely formal stretch in §3; easy to hide a category-membership slip. No concrete contradiction found on reading; recommend Lean or second-human check.

### `prop:contractible-quotient` — Integral iso after killing contractible open  
**File:** `04-lattice.tex` ~487–529  
**Grade: PASS**

- For odd \(d\geq 3\), \(E_d(U)=0\) on contractible \(U\); \(E_{d-1}(U)\to E_{d-1}(X)\) split-injective via point projection (handles both \(d\equiv 1,3\pmod{4}\)).
- Localization LES ⇒ integral isomorphism \(E_d(X)\xrightarrow{\sim}W_d(\mathcal{T}(X)/\mathcal{T}(U))\).
- Used to lift character involution classes without splitting quotient idempotents.

---

## Target C — Character classes and equal parts

### `lem:character-coproduct`  
**File:** [`paper/sections/06-character-classes.tex`](../paper/sections/06-character-classes.tex) ~37–99  
**Grade: WEAK**

- \(Rq_*\underline{\mathbb{C}}\simeq\bigoplus_\lambda\mathcal{H}_\lambda\) via vanishing of higher cohomology on zero-dimensional orbits + eigenspace decomposition of finite cyclic representations.
- Derived pushforward of finite character subsum isomorphic to sum of pushforwards, using soft resolutions and compactness of fibers.
- **Why WEAK:** infinite character support / commuting of \(Rt_*\) with infinite sums is subtle; the paper addresses it via soft sheaves on compact Hausdorff spaces. Expert sheaf check recommended.

### `lem:orthogonality`  
**File:** `06-character-classes.tex` ~150–203  
**Grade: PASS**

- \(G\)-action by orientation-preserving isometries; complex structure \(J\) with \(J^\dagger=-J\); cross pairings between distinct character summands vanish.
- Implies self-adjointness of finite partition projectors on the punctured target.

### `def:character-classes` / `prop:sum-classes`  
**File:** `06-character-classes.tex` ~225–291  
**Grade: PASS**

- Classes defined as
  \(\ell_U(z_i)=[A,\alpha]+[A,\alpha\circ(2e_i-\mathrm{id})]\)
  in the quotient Witt group — **without** requiring images of idempotents in \(\mathcal{T}(X)\).
- Matrix isometry \(S\) proves \(\sum z_i=2[A,\alpha]\) integrally.
- Elegant and appears correct; this is where the paper avoids a common false step (splitting continuous projectors over \(b\)).

### `prop:equal-parts`  
**File:** `06-character-classes.tex` ~411–443  
**Grade: WEAK**

- On a concentrated test, locally constant \(\beta\) of modulus 1 multiplies coefficients and cyclically permutes character summands; induces quotient isometries conjugating \(e_i\mapsto e_{i-1}\).
- **Why WEAK:** must check that \(M_\beta\) is an isometry of the *restricted manifold* pairing \(\alpha_h\), that it matches under \(A_h|_{X^\circ}\simeq Rt_*\mathcal{H}|_{X^\circ}\), and that the germ theorem places the conjugation in \(\mathcal{Q}_U(X)\). The sketch is coherent; this is the sharpest geometric–algebraic interface in §6.

### `prop:move-test`  
**File:** [`paper/sections/05-local-tests.tex`](../paper/sections/05-local-tests.tex) ~478–517  
**Grade: PASS (topology); WEAK dependence on `lem:orbit-injectivity`**

- Pullback of orientation class vanishes on \(F=Y\setminus V\) by moving the pinch into \(q^{-1}(V)\) and using orbit-injectivity of rational Čech.
- Odd-sphere lemma (`lem:odd-sphere-null`) + Tietze neighborhood extension concentrate \(D_sa\).
- Odd-sphere telescope \(\to K(\mathbb{Q},d)\) is classical (Serre; also used by Dranishnikov–Ferry–Weinberger).
- **`lem:orbit-injectivity` WEAK residual:** claims injectivity of \(r^*\colon\check H^*(E/G;\mathbb{Q})\to\check H^*(E;\mathbb{Q})\) with **no covering-dimension bound**, via vanishing of higher cohomology on zero-dimensional orbits and Haar averaging of locally constant \(\mathbb{Q}\)-functions. Argument looks carefully written; still a place specialists may probe because \(Y\) can be infinite-dimensional.

---

## Cross-cutting residual risks (not graded FAIL)

1. **Generated continuous category \(\mathcal{T}\)** is larger than constructible/Woolf settings; duality restriction (`prop:test-duality`) is argued via simplex generators — appears sound, not fully re-audited line-by-line outside Targets A–C.
2. **No Lean formalization** of this preprint found in the Oct 2026 release materials (see [`04_public_responses.md`](04_public_responses.md)).
3. **Homology-manifold edge case** is outside the theorem’s hypotheses; see sponge doc.

## Suggested expert / Lean priorities

| Priority | Object | Why |
|----------|--------|-----|
| 1 | `thm:dense-doubling` neutrality descent | Long formal Witt argument |
| 2 | `prop:equal-parts` + germ isometry of \(M_\beta\) | Action enters here |
| 3 | `thm:witt-localization` vs Balmer–Walter hypotheses | Citation bridge |
| 4 | `lem:orbit-injectivity` on wild compacta | No dim bound |
| 5 | Cylinder signs appendix | Historical foot-gun |

## Sanity check (finite \(\mathbb{Z}/p\))

See [`03_sponge_stress_test.md`](03_sponge_stress_test.md) §Sanity: failure is exactly at `lem:averaged-test` (no degree-one invariant pinch). The arithmetic steps are not reached. **Sanity PASS.**
