# Sponge / non-manifold stress test (Dabrowski)

**Goal:** Can the argument be run on spaces where faithful continuous \(\mathbb{Z}_p\)-actions **exist**, thereby “proving too much”? If every lemma’s hypotheses hold on such a space, that is a candidate gap. If a manifold-specific hypothesis fails early, the proof is correctly scoped.

**Framing:** A Menger sponge where Hilbert–Smith is false does **not** refute a theorem about manifolds. It is a probe for overclaiming.

---

## Sanity: finite \(\mathbb{Z}/p\) on \(\mathbb{R}^2\)

| Step | Status |
|------|--------|
| Chart / free point | OK for a free rotation (or fails faithfulness differently) |
| Unbounded tail \(K_i=p^{\ell_i}\mathbb{Z}_p\) with displacements \(\to 0\) | **FAILS** (group is finite) |
| Haar degree-one pinch through a proper open subgroup | **FAILS** |
| \(L_4\) tail divisibility / \(\mathbb{CP}^2\) realization | Not reached |

**Why the tail fails.** Realization needs a sequence of kernels \(K_i\subset H'\subset H\cong\mathbb{Z}_p\) with \(\ell_i\to\infty\), so that \(G_i=H/K_i\) has unbounded \(p\)-power order while displacements on a chart ball tend to zero. A finite cyclic group has no such nested open subgroups. Separately, any invariant map through a free \(\mathbb{Z}/p\)-orbit space has degree divisible by \(p\) (transfer), so there is no degree-one averaged pinch.

**Conclusion:** The proof does not incorrectly rule out finite cyclic actions. Break is at §8 geometric data, before Theorem 4.3. **Sanity PASS.**

---

## Break-point matrix

For each model: first lemma/hypothesis that fails when one tries to copy the proof.  
`—` means the step still makes sense; the chain stops at the first **BREAK**.

| Model | Faithful \(\mathbb{Z}_p\)? | First BREAK | Later notes |
|-------|---------------------------|-------------|-------------|
| Topological \(n\)-manifold (theorem setting) | Conjecturally no; paper claims no | *(none — target of proof)* | Full chain |
| Finite \(\mathbb{Z}/p\) on \(\mathbb{R}^2\) | N/A (finite) | Unbounded tail \(K_i\); no deg-1 Haar pinch | Transfer degree |
| \(\mathbb{Z}_p\times\mathbb{R}^n\) (left translation on \(\mathbb{Z}_p\)) | Yes | **Not a manifold** / no Euclidean chart (Lemma 8.1 chart) | Locally \(\mathbb{Z}_p\times\mathbb{R}^n\not\simeq\mathbb{R}^{n+k}\) |
| \(p\)-adic solenoid \(\Sigma_p\) | Yes (standard free action; orbit \(S^1\)) | **Not a manifold**; no chart ball in \(\mathbb{R}^n\); no \(S^n\times\mathbb{CP}^2\) from a coordinate compactification | Averaging to \(S^1\) exists; Poincaré–Lefschetz dual blocks of Lemma 7.4 need a combinatorial manifold |
| Menger compactum \(\mu^n\) (Dranishnikov 1989) | Yes — free action of any zero-dimensional compact group | **Not a manifold**; Newman fails; no chart; Lemma 7.4 triangulation fails | Orbit dim can equal \(n\); irrelevant because chart already fails |
| Menger sponge / curve \(\mu^1\) | Yes | Same as \(\mu^n\) | Classic Cantor-like 1-dimensional universal curve |
| Raymond–Williams compactum | Yes; \(\dim X=n\), \(\dim X/\mathbb{Z}_p=n+2\) | **Not a manifold**; chart / PL dual cells fail | Historically tied to Yang dim-raising; this paper does not use that obstruction |
| ENR homology \(n\)-manifold (Bryant–Ferry–Mio–Weinberger; Bing dogbone \(\times\mathbb{R}\)) | **Unknown** whether faithful \(\mathbb{Z}_p\) can exist | **OPEN EDGE** | Local duality may partially survive; paper’s Lemmas 7.3–7.5 and 12.1–12.2 use **combinatorial triangulations of manifolds**. Homology manifolds need not be triangulable in this sense |

---

## Detailed sponge notes

### 1. Dranishnikov Menger actions (including the sponge)

**Fact:** Every Menger manifold (in particular \(\mu^n\)) admits a free continuous action of \(\mathbb{Z}_p\) (Dranishnikov, *Math. USSR Izv.* 32 (1989)).

**Why the Dabrowski argument stops:**

1. \(\mu^n\) is not locally Euclidean \(\Rightarrow\) Lemma 8.1’s chart (image containing \(B(0,4)\)) is undefined.
2. Haar coordinate average \(F_0\) is an average of points in \(\mathbb{R}^n\), not an abstract barycenter on a compactum.
3. \(W=S^n\times\mathbb{CP}^2\) is built from the **compactified coordinate sphere**. There is no such sphere for a Menger chart.
4. Lemma 7.4 needs a finite combinatorial triangulation of a compact oriented manifold with dual blocks. Menger compacta are not manifolds.
5. Newman’s theorem (used in Corollary 1.2, not in Theorem 1.1’s realization) is a manifold theorem.

The divisibility half (Theorem 4.3) is stated for an abstract compact free \(C_p\)-space \(T\). That half **could** be copied on a Menger free action, producing \(p\)-divisible tails in \(L_4(A_G(T))\). The contradiction never fires because realization of signature \(1\) never starts. **“Proves too much?”** No.

### 2. Solenoid

The inverse-limit circle \(\Sigma_p=\varprojlim(S^1\xrightarrow{\times p}S^1)\) carries a free \(\mathbb{Z}_p\)-action with orbit space \(S^1\).

- Orbit space is a manifold; the **total space** is not.
- One can average maps to circles, but the paper’s degree-one pinch is a compactified Euclidean chart map \(s_\rho\circ F_0\).
- Break: chart + \(S^n\times\mathbb{CP}^2\) + dual-block Poincaré–Lefschetz.

### 3. Raymond–Williams

These examples show dim-raising for \(\mathbb{Z}_p\) actions on **compacta**. The Dabrowski proof **does not use** Yang’s cohomological-dimension relation. On RW spaces the Euclidean PL pipeline never starts. They neither confirm nor refute the \(L\)-theory steps; they only show that wild orbit spaces exist — which the paper already allows, since it never bounds \(\dim Y\).

### 4. Homology manifolds (edge)

Topological manifolds \(\Rightarrow\) ENR homology manifolds, but not conversely in high dimensions. Local Čech duality and orientation sheaves can exist without Euclidean charts.

| Paper ingredient | Homology manifold? |
|------------------|--------------------|
| Newman | Partial analogues exist; not automatic |
| Open \(O\subset\mathbb{R}^n\) containing \(B(0,4)\) | **Fails** without resolution/chart |
| Haar coordinate average | Needs vector space structure |
| Combinatorial dual blocks (Lemma 7.4) | **Fails** without a triangulation of a manifold |
| Abstract \(L_4(A_G(T))\) divisibility | Could make sense for a free \(C_p\)-space \(T\) |
| \(\mathbb{CP}^2\) evaluation | Needs the product Poincaré manifold \(S^n\times\mathbb{CP}^2\) |

If a free \(\mathbb{Z}_p\) action on an ENR homology manifold were found, one would check whether some substitute for Lemmas 7–12 still produces a signature-one tail. That is a **stress region**, not a present counterexample to the written theorem.

---

## Shared Euclidean ingredients (why sponges fail the same way as OpenAI)

Both proofs need, in some packaging:

1. Newman rigidity (corollary / reduction).
2. Local Euclidean charts.
3. An integral signature (Witt sheaf vs \(L_4\) tail / \(\mathbb{CP}^2\)).
4. Arbitrarily small open subgroups of \(\mathrm{Homeo}\) (Haar averaging / unbounded finite quotients).

Sponges break (1)–(2) immediately, so they do not test (3)–(4). That is the correct scope for a manifold theorem. See [`05_vs_openai.md`](05_vs_openai.md).
