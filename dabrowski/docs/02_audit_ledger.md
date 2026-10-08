# Targeted audit ledger (Sherlock targets A–C)

**Scope:** line-by-line on load-bearing lemmas only (plan: targeted audit).  
**Grades:** `PASS` = argument appears complete and correctly cited; `WEAK` = plausible but citation gap, omitted routine detail, hypothesis that needs expert/Lean check, or certificate not independently rerun; `FAIL` = identified break.  
**Overall targeted verdict:** **No FAIL found on the PDF’s load-bearing lemmas.** Several `WEAK` items remain — especially **Target C** (Lean certificate vs published theorem), which this audit did **not** compile. The proof does **not** “prove too much” on known sponge models (see [`03_sponge_stress_test.md`](03_sponge_stress_test.md)).

---

## Target A — Signature-tail lattice / integer signatures independent of \(p\)-power

The arithmetic engine is coarser than OpenAI’s \(L_d^{-1}\mathbb{Z}\) lattice: ordinary signatures of rational symmetric forms are **integers**, and the tail map lands in \(\mathbb{Z}^{\mathbb{N}}/\mathbb{Z}^{(\mathbb{N})}\). The “bounded denominator” claim is just integrality of \(\sigma\), plus that two lifts of an \(L_4(V_G)\) class agree eventually.

### Lemma 3.1 — Cyclic arithmetic  
**PDF:** §3, p. 3  
**Lean:** [`AlgebraicReduction.lean`](../lean/AlgebraicReduction.lean), [`EquivariantSignature.lean`](../lean/EquivariantSignature.lean)  
**Grade: PASS**

- If \(G=C_{p^a}=\langle g\rangle\) and \(\mathrm{Sign}_G(V,b)(g)=0\), then \(p\mid\sigma(V,b)\).
- Write \(\mathrm{Sign}_G=\sum m_j\chi_j\); \(F(t)=\sum m_j t^j\) is divisible in \(\mathbb{Z}[t]\) by \(\Phi_{p^a}\), so \(F(1)=\sigma\) is divisible by \(\Phi_{p^a}(1)=p\).
- Standard cyclotomic fact; Lean proves the polynomial form (`prime_dvd_eval_one_of_primitive_root`) and the character form. No residual risk here.

### Proposition 3.2 — Tail extraction  
**PDF:** §3, pp. 3–4  
**Grade: WEAK (depends on negative \(K\) of \(\mathbb{Q}[G]\))**

- Semisimple rings \(\mathbb{Q}[G_i]\) have vanishing negative \(K\)-groups [Wei13, III.4]; Bass’s polynomial definition commutes with the finite-support subcategory \(S\), so \(K_{-k}(S)=0\) for \(k\ge 1\).
- Rothenberg comparison \(\Rightarrow L_j(S)=\bigoplus_i L^p_j(\mathbb{Q}[G_i])\). Karoubi filtration by finite index sets lifts every \(L_4(V_G)\) class to \(L_4(P)\); two lifts differ by \(L_4(S)\), so coordinate classes agree eventually.
- **Why WEAK:** this is exactly the `NegKHighAll` / decoration-map bijectivity package that occupies most of `HSFormal/LTheory/` (\(\sim\)104 modules). The PDF cites Weibel as a black box for \(K_{-k}(\mathbb{Q}[G])=0\). If that comparison fails for the *asymptotic sequence category* (not just a single group ring), the tail map is not well-defined as a homomorphism to the product-modulo-sum. Lean claims to prove the iterated bounded-category form; this audit did not check those modules line-by-line.

### Theorem 4.3 — Integer tail divisibility  
**PDF:** §4, p. 4  
**Grade: PASS (with WEAK dependence on Lemma 4.2 and Prop. 3.2)**

- Extract forms \((V_i,b_i)\). Nilpotence \(\Rightarrow (p-\tau_i)^s[V_i,b_i]=0\) in \(L^p_4(\mathbb{Q}[G_i])\) for large \(i\).
- Character of \(\tau_i\) at a generator \(g_i\) vanishes, so \(p^s\,\mathrm{Sign}_{G_i}(V_i,b_i)(g_i)=0\), hence that character is zero (complex numbers), and Lemma 3.1 gives \(p\mid\sigma\).
- The arithmetic implication is clean (`character_vanishes_of_prime_power_annihilation` in Lean). Load-bearing gaps sit in the geometric nilpotence and in tail extraction, not here.

### Proposition 13.1 / Prop. 12.4 — Realization of signature 1  
**PDF:** §§12–13, pp. 15–16  
**Grade: WEAK**

- After \(n\) localization boundaries, one component of \(T\times S^0\) retains exactly one copy of \(\mathbb{CP}^2\), sign \(\varepsilon\in\{1,-1\}\) independent of \(i\). Middle form \(\langle 1\rangle\); half-unit quadratic lift has signature \(1\).
- Identity-character trace identifies ordinary signatures of equivariant forms with those of their scalar images, so \(\sigma_{\mathrm{tail}}(\alpha)=[(1,1,\ldots)]\).
- **Why WEAK:** (i) sign bookkeeping through \(n\) cuts, one ordered diagonal, and component projection is the same class of foot-gun as OpenAI’s cylinder signs; (ii) “point control + subdivision identifies the constant model” is sketched rather than expanded; (iii) the half-unit comparison \(\varphi/2\) on rational Poincaré complexes is standard Ranicki but must survive every exterior quotient. No contradiction found on reading; this is the geometric–algebraic interface of realization.

---

## Target B — Transfer / averaging multiplies by \(p\) without leaving the integral lattice

Here “integral lattice” means: \(\tau\otimes(-)\) and \(p\cdot\mathrm{id}\) act on the same ultimate \(L\)-groups of \(A_G(T)\), and Haar averaging produces a **degree-one** (hence signature-one after \(\mathbb{CP}^2\)) class rather than a \(p\)-multiple.

### Lemma 4.1 — Local triviality of \(\tau\)  
**PDF:** §4, p. 4  
**Grade: PASS**

- On a compact \(U\subset T/C_p\) inside a covering trivialization, a sheet function \(c:L\to C_p\) gives an orthogonal equivariant isometry \(\tau\otimes(-)\cong\mathrm{id}^{\oplus p}\) of propagation zero.
- Compact positively separated sheets \(\Rightarrow\) controlled morphisms eventually preserve them. Standard covering-space linear algebra. Appears complete.

### Lemma 4.2 — Nilpotence \(\nu^s=0\)  
**PDF:** §4, p. 4  
**Grade: WEAK**

- Finite compact cover of \(T/C_p\) of size \(s\), independent of \(i\). Induct via support Mayer–Vietoris from Lemma 2.2: \(\nu=0\) on \(A\cap B\) \(\Rightarrow\) \(\partial(\nu x)=0\) \(\Rightarrow\) \(\nu x\) comes from \(L_*(A_A)\oplus L_*(A_B)\); induction kills the first summand by \(\nu^{s-1}\), local triviality kills the second.
- **Why WEAK:** the argument assumes the support filtration of Lemma 2.2 induces a genuine localization / Mayer–Vietoris sequence in **ultimate** \(L\)-theory, with \(\nu\) acting naturally on the sequence. Carlsson–Pedersen [CP95, Thm 4.2] is cited later for boundaries; here the MV sequence is called “natural” from Lemma 2.2 without repeating the \(L\langle-\infty\rangle\) hypotheses (functoriality, additivity, Karoubi localization with connecting maps — listed as conventions on p. 2). Specialists should check that \(\nu\) commutes with \(\partial\) strictly enough for the nilpotence induction, including at \(s=1\).

### Lemma 2.2 — Support calculus  
**PDF:** §2, pp. 2–3  
**Grade: PASS (with residual on “equality means eventual equality”)**

- Duality-invariant Karoubi filtration; \(A_A\cap A_B=A_Y\); quotient equivalences; \(A_G(S)\simeq A_S\); fully faithful when \(d(S,Z)>0\).
- Compactness of \(X\) is used to send labels approaching both \(A\) and \(B\) into \(Y\). Relabeling by nearest-point projection has propagation \(\to 0\).
- Residual: asymptotic categories identify morphisms only eventually. The filtration splits must be **uniform in the sequence index** for later nilpotence. The writeup addresses this via null sequences \(r_i\) and filtered orthogonal splits; looks carefully written.

### Lemma 8.1 + Haar pinch (8.1)–(8.6)  
**PDF:** §8, pp. 9–10  
**Grade: PASS**

- Free point: nonzero closed subgroups of \(\mathbb{Z}_p\) are the tails \(H_j\); if all stabilizers were nonzero, discrete \(\mathbb{Z}\) would have finite orbits, hence finite image by [Rob75], contradicting effectivity.
- Haar average \(F_0\) is continuous, invariant, \(|F_0(x)-x|\le 2D\); compactified pinch \(f\) has degree one by straight-line homotopy to the identity pinch \(s_\rho\).
- Same geometric idea as OpenAI’s `lem:averaged-test`, done in coordinates rather than as a map \(S^d\to Y\to S^d\). Finite \(\mathbb{Z}/p\) cannot produce a sequence \(K_i\) with displacements \(\to 0\) while remaining a proper open subgroup of a finite group. **Sanity:** see sponge doc.

### Graph idempotent / Lemma 5.1–5.2 / Prop. 10.2  
**PDF:** §§5, 10–11  
**Grade: WEAK**

- Homotopy action of \(G_i\) on \((C,\varphi)\) produces \(E=q_i^{-1}\sum_g A_g\otimes R_{g^{-1}}\) with \(E^2\simeq E\) and \(E\Phi\simeq\Phi E^*\) in the **exterior quotient**.
- Balmer–Schlichting [BS01] splits \(E\) in \(K^b(\mathrm{Kar}\,Q)\); normalized corner \(\varphi_D=q^{-1}r\Phi r^*\). Scalar normalization (Lemma 5.2) says that after forgetting, the corner is isometric to \((C,\varphi)\).
- Compression (Prop. 10.2) kills defects through an exterior band around radius \(t\); detector cancellation \(\chi(sg^{-1})\chi(g)=\chi(s)\) is the reason free sheets work.
- **Why WEAK:** (i) all homotopies, including products of \(\sim q_i^2\) terms, are claimed to be uniformly controlled independent of rank — the paper emphasizes “uniform control rather than a bound on the number of summands,” which is the right slogan but easy to under-prove; (ii) splitting “once in the sequence category” must produce asymptotically small representatives; (iii) signs in (5.1) and the double dual identification are spelled out, but the graph-type calculus of §9–10 is the longest formal stretch. Lean’s `CornerClass.lean` / `GraphCorner` is the matching formal target.

---

## Target C — Lean certificate vs published theorem

**Grade: WEAK (certificate not rerun; statement alignment looks good)**

| Claim (upstream README) | What this audit checked |
|-------------------------|-------------------------|
| `Challenge.lean` states classical HSC, proof `sorry`, Mathlib only | **PASS.** Boundaryless topological \(n\)-manifold; locally compact second-countable Hausdorff group; joint continuity; faithful action; conclusion \(C^\infty\) Lie in the **given** topology. |
| `Solution.lean` = `HSFormal.hilbertSmith n M G` | **PASS** as text: same type signature, one-line call. |
| `HSFormal.hilbertSmith` proved in `HilbertSmithNegK.lean` from `NegKHighAll` | **Text PASS, compile unchecked.** `negKHighAll := negKHighAll_of theoremB Reg.regKarStatement`, then `hilbertSmith_all.1`. Earlier comments in `HilbertSmithModel.lean` still describe `NegKHighAll` as “being formalized on the v4.35 port”; the terminal file `HilbertSmithNegK.lean` claims that induction is now a theorem. |
| Axioms used: `propext`, `Classical.choice`, `Quot.sound` | **UNVERIFIED.** This environment did not run `lake env lean` / `#print axioms`. A garbled third-party paste of the README listed `HilbertSmithNegK.lean` and even `HSproof.pdf` as axioms; the **vendored** README does **not**. Treat the three-axiom claim as a hypothesis until printed. |
| 238 modules, import closure of `HilbertSmithNegK.lean` | **PASS** as a file count (`find HSFormal -name '*.lean' \| wc -l` = 238). Full tree not vendored. |
| Comparator / SafeVerify “solution is okay” | **UNVERIFIED.** Scripts live upstream under `verify/`; not rerun (Linux Landlock, \(\sim\)15 GB). |
| PDF \(\leftrightarrow\) Lean statement | **Mostly PASS.** Lean `Challenge` is boundaryless; paper Theorem 1.1 allows boundary and proves it by interior restriction. Lean also packages `HilbertSmithWithBoundary` and `PadicExclusionWithBoundary` in `Statement.lean`. Paper uses rational chain coefficients throughout; Lean builds a concrete `LowerLTheory` model. Residual: whether every PDF lemma is in the import closure, vs a weaker model with leftover `LowerLTheory` hypotheses. The **terminal** theorem `hilbertSmith` has no remaining hypothesis in the source text. |

**PDF vs Lean packaging.** The PDF is 17 pages of controlled \(L\)-theory. The Lean tree is an engineering expansion: Newman, Gleason–Yamabe, Tao’s Lemma 7, a colimit model of lower \(L\)-theory, and a high negative-\(K\) induction. That is expected. The risk is not “too many files”; it is that a `sorry` or extra axiom hides in `LTheory/Model/NegK/High/` after the README’s axiom list was written.

**Suggested axiom-print command (not run here):**
```
lake env lean --stdin <<< 'import HSFormal.HilbertSmithNegK
#print axioms HSFormal.hilbertSmith'
```

---

## Cross-cutting residual risks (not graded FAIL)

1. **Ultimate decoration \(L^{\langle-\infty\rangle}\)** is used everywhere; projective-to-ultimate maps and idempotent-completion invariance are listed as required properties rather than proved in the PDF.
2. **Signs** in Poincaré–Lefschetz dual blocks (Lemma 7.4) and iterated boundaries (Prop. 12.4).
3. **Homology-manifold edge** is outside the theorem’s hypotheses; see sponge doc.
4. **No independent `#print axioms`** in this session.

## Suggested expert / Lean priorities

| Priority | Object | Why |
|----------|--------|-----|
| 1 | `#print axioms HSFormal.hilbertSmith` on a clean `lake build` | Distill C |
| 2 | Lemma 4.2 nilpotence vs [CP95] MV in ultimate \(L\) | Distill B |
| 3 | Prop. 3.2 tail extraction / `NegKHighAll` | Distill A/C |
| 4 | Prop. 10.2–11.6 graph corner + detector cancellation | Realization |
| 5 | Prop. 12.4 iterated boundary \(\to\varepsilon[\mathbb{CP}^2]\) | Signs / evaluation |

## Sanity check (finite \(\mathbb{Z}/p\))

See [`03_sponge_stress_test.md`](03_sponge_stress_test.md). Failure is at the **unbounded tail** \(K_i\) with displacements \(\to 0\): a finite group has no such sequence. Degree-one Haar averaging over a proper open subgroup also fails. Arithmetic of Theorem 4.3 is not reached. **Sanity PASS.**
