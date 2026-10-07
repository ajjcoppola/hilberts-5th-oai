# Sponge / non-manifold stress test

**Goal (plan):** Can the argument be run on spaces where faithful continuous \(\mathbb{Z}_p\)-actions **exist**, thereby “proving too much”? If every lemma’s hypotheses hold on such a space, that is a candidate gap. If a manifold-specific hypothesis fails early, the proof is correctly scoped.

**Framing:** A Menger sponge where Hilbert–Smith is false does **not** refute a theorem about manifolds. It is a probe for overclaiming.

---

## Sanity: finite \(\mathbb{Z}/p\) on \(\mathbb{R}^2\)

| Step | Status |
|------|--------|
| Chart / Newman | OK for finite cyclic rotation (or fails faithfulness differently) |
| `lem:averaged-test` degree-one through orbit space | **FAILS** |
| Lattice / equal parts | Not reached |

**Why averaging fails.** For \(G=\mathbb{Z}/p\) acting (nearly) freely, any \(G\)-invariant continuous map \(W^+\to S^d\) that descends through \(Y=W^+/G\) has degree divisible by \(p\) (transfer / covering degree of the regular orbits). There is no open subgroup smaller than \(G\) to average over while preserving degree 1.  
**Conclusion:** The proof does not incorrectly rule out finite cyclic actions. Break is exactly at `lem:averaged-test`. **Sanity PASS.**

---

## Break-point matrix

For each model: first lemma/hypothesis that fails when one tries to copy the proof.  
`—` means the step still makes sense; the chain stops at the first **BREAK**.

| Model | Faithful \(\mathbb{Z}_p\)? | First BREAK | Later notes |
|-------|---------------------------|-------------|-------------|
| Topological \(n\)-manifold (theorem setting) | Conjecturally no; paper claims no | *(none — target of proof)* | Full chain |
| Finite \(\mathbb{Z}/p\) on \(\mathbb{R}^2\) | N/A (finite) | `lem:averaged-test` | Degree divisible by \(p\) |
| \(\mathbb{Z}_p\times\mathbb{R}^n\) (left translation on \(\mathbb{Z}_p\)) | Yes | **Not a manifold** / no Euclidean chart (`prop:chart-reduction`) | Locally \(\mathbb{Z}_p\times\mathbb{R}^n\not\simeq\mathbb{R}^{n+k}\) |
| \(p\)-adic solenoid \(\Sigma_p\) | Yes (standard free action; orbit \(S^1\)) | **Not a manifold**; no open \(O\subset\mathbb{R}^n\); `lem:collapse` needs \(W\subset\mathbb{R}^d\) | Averaging on solenoid can produce maps to \(S^1\); orientation form \(u_d\) of chart type absent |
| Menger compactum \(\mu^n\) (Dranishnikov 1989) | Yes — free action of any zero-dimensional compact group | **Not a manifold**; Newman fails; no chart in \(\mathbb{R}^n\); collapse into \(S^d\) fails | Orbit dim can equal \(n\); cohomological dim may jump — irrelevant here because chart already fails |
| Menger sponge / curve \(\mu^1\) (“Munger sponge”) | Yes (special case of Dranishnikov) | Same as \(\mu^n\) | Classic Cantor-like 1-dimensional universal curve |
| Raymond–Williams compactum (Ann. of Math. 1963; arXiv:1909.12660) | Yes; \(\dim X=n\), \(\dim X/\mathbb{Z}_p=n+2\) | **Not a manifold**; chart/collapse fail | Historically motivated by Yang’s dim-raising obstruction for *manifolds* |
| ENR homology \(n\)-manifold (e.g. Bryant–Ferry–Mio–Weinberger; Bing dogbone \(\times\mathbb{R}\)) | **Unknown** whether faithful \(\mathbb{Z}_p\) can exist | **OPEN EDGE** | Local duality / orientation may partially survive; Newman-type results are subtler. Paper’s hypotheses require topological manifolds (charts to \(\mathbb{R}^n\)). If a free \(\mathbb{Z}_p\) action on an ENR homology manifold were found, one must check whether `prop:chart-reduction` + orientation pairing still apply — potential stress region, **not** a present counterexample to the written theorem |

---

## Detailed sponge notes

### 1. Dranishnikov Menger actions (including the sponge)

**Fact:** Every Menger manifold (in particular \(\mu^n\)) admits a free continuous action of \(\mathbb{Z}_p\) (Dranishnikov, *Math. USSR Izv.* 32 (1989)).

**Why the OpenAI argument stops:**

1. \(\mu^n\) is not locally Euclidean → `prop:chart-reduction` hypotheses false.
2. There is no open embedding \(W\hookrightarrow\mathbb{R}^d\) → continuous collapse \(c:S^d\to W^+\) of §5 is undefined in the paper’s form.
3. Newman’s theorem is a **manifold** theorem; fixed-point-open ⇒ identity fails for sponges.
4. No orientation class of an open set in \(\mathbb{R}^d\) to push into \(E_d(S^d)\) via \(tqc\).

The lattice theory on \(S^d\) itself remains fine — it never sees the sponge. The action never produces the character classes on \(S^d\) through a degree-one chart test.

**“Proves too much?”** No. Manifold hypotheses fail at the first geometric step.

### 2. Solenoid

The mapping torus / inverse-limit circle \(\Sigma_p=\varprojlim(S^1\xrightarrow{\times p}S^1)\) carries a free \(\mathbb{Z}_p\)-action with orbit space \(S^1\).

- Orbit space is a manifold, but the **total space** is not.
- One can average maps to spheres, but the paper’s degree-one test is built from a pinch in an open Euclidean \(W\), not from abstract averaging on a solenoid.
- Break: chart + collapse + orientation of \(W\subset\mathbb{R}^d\).

### 3. Raymond–Williams

These examples show dim-raising for \(\mathbb{Z}_p\) actions on **compacta**, historically tied to: *if* a manifold admitted a faithful \(\mathbb{Z}_p\) action then Yang’s cohomological dimension relation would force \(\operatorname{cd}_{\mathbb{Z}}(M/\mathbb{Z}_p)=\dim M+2\).

The OpenAI proof **does not use** that obstruction. It uses signature lattices on \(S^d\). On Raymond–Williams spaces the signature-chart pipeline never starts. So RW examples neither confirm nor refute the algebraic steps; they only show that “wild orbit spaces exist” — which the paper already allows for manifolds’ orbit spaces without bounding their dimension.

### 4. Homology manifolds (edge)

Topological manifolds ⇒ ENR homology manifolds, but not conversely in high dimensions (with exotic examples). Local Čech duality and orientation sheaves can exist without Euclidean charts.

| Paper ingredient | Homology manifold? |
|------------------|--------------------|
| Newman | Partial analogues exist in literature; not automatic |
| Open \(O\subset\mathbb{R}^n\) | **Fails** without resolution/chart |
| Orientation pairing on \(W\subset\mathbb{R}^d\) | Needs Euclidean (or at least locally dualizable oriented) open set inside \(S^d\) |
| Averaging / sheets / characters | Could make sense abstractly |

**Verdict:** The written proof uses **Euclidean charts** essentially (`prop:chart-reduction`, \(W\subset\mathbb{R}^d\), collapse from \(S^d\)). It does not claim Hilbert–Smith for homology manifolds. No known counterexample on that class was used to break the argument. Flag for future work, not as a current FAIL.

---

## Q5 answer (sponges as \(\mathbb{R}^n\) replacements)

Through the Menger/Cantor-sponge lens:

1. Hilbert–Smith is **false** if “manifold” is replaced by “Menger compactum / sponge.”
2. The OpenAI proof **correctly refuses** to run there: it needs Newman + Euclidean chart + orientation collapse into \(S^d\).
3. The algebraic lattice on \(E_d(S^d)\) is a statement about spheres/polyhedra, not about \(\mathbb{R}^n\) alone; the manifold enters by manufacturing a degree-one test through a \(\mathbb{Z}_p\)-orbit space from a chart action.
4. Therefore sponges are **consistency checks**, not disproofs. They show the geometric hypotheses are sharp.
5. The only alarming outcome would have been: a sponge satisfying every cited lemma while admitting free \(\mathbb{Z}_p\). **That did not occur.**

---

## “Proves too much” summary

| Test | Result |
|------|--------|
| Finite \(\mathbb{Z}/p\) | Breaks at averaging — good |
| Menger / sponge / solenoid / RW | Break at manifold/chart/collapse — good |
| Homology manifolds | Outside scope; open edge |
| Candidate gap from sponge pass-through | **None found** |

Combined with the audit ledger: **no sponge-based disproof of the preprint; no FAIL in targeted algebraic steps; WEAK items remain for expert review.**
