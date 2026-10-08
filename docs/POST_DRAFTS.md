# Post drafts (updated 2026-10-08)

Repo: https://github.com/ajjcoppola/hilberts-5th-oai  
OpenAI PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
Dabrowski PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/dabrowski/docs/Dabrowski_HS_Audit.pdf

Closed MO question to edit/reopen: https://mathoverflow.net/questions/515824

**Do not** ask whether a proof is correct or to finish a verification. The body below is a research question about Euclidean structure; the two preprints are motivation.

---

## MathOverflow (paste-ready rewrite)

**Title:** Which local Euclidean properties block continuous \(\mathbb{Z}_p\)-actions? (OpenAI vs Dabrowski signature arguments)

**Tags:** `gt.geometric-topology` `at.algebraic-topology` `transformation-groups` `lie-groups`

**Body:**

The Hilbert–Smith conjecture is equivalent to \(p\)-adic exclusion: the additive group \(\mathbb{Z}_p\) admits no faithful jointly continuous action on a connected finite-dimensional topological manifold. (Manifolds Hausdorff, second countable; actions jointly continuous.) Classical partial results include Lipschitz and quasiconformal actions, and Pardon’s theorem in dimension 3. The remaining problem is often described as a rigidity property of Euclidean charts under small subgroups of \(\mathrm{Homeo}\).

Two recent arguments appear to use the **same obstruction class** — integrality versus \(p\)-divisibility of a signature / Witt invariant — with different packaging:

- OpenAI (2026-09-23): after Newman chart reduction to a faithful open subgroup \(G\cong\mathbb{Z}_p\) on \(O\subset\mathbb{R}^n\), odd-stabilize into \(S^d\), Haar-average a degree-one pinch through the orbit space, and split an integral Witt/signature class on \(E_d(S^d)\) into \(p^k\) equal pieces summing to \(4\overline{u}_d\). A comparison lattice \(L_d^{-1}\mathbb{Z}\,\overline{u}_d\) with \(L_d=2^{e_d}\) independent of \(k\) then yields a contradiction for \(p^k>4L_d\).  
  https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026

- Dabrowski (2026-10-08): Haar-average coordinates in a Euclidean chart to get a degree-one pinch on \(S^n\); a character detector supplies a compact free \(C_p\)-space \(T\); a duality-compatible homotopy idempotent on \(S^n\times\mathbb{CP}^2\) forgets to a scalar germ whose iterated Karoubi localization boundaries recover one copy of \(\mathbb{CP}^2\). The resulting class in \(L_4(A_G(T))\) has integer signature tail constantly \(1\). Independently, permutation-tensoring \(\tau=\mathbb{Q}[G_i/P_i]\) is locally \(p\) copies of the identity and is nilpotent after controlled Mayer–Vietoris, so every such class has eventually \(p\)-divisible ordinary signatures. Hence \(1\in p\mathbb{Z}\).  
  https://github.com/adbrw/HS_proof

I am **not** asking whether either manuscript is correct, complete, or ready to referee. I want to isolate the **Euclidean input**.

Both writeups seem to need four local properties of \(\mathbb{R}^n\) (or of topological manifolds):

1. **Newman rigidity.** A compact Lie group acting continuously and displacing every point of a small ball by less than some \(\varepsilon>0\) acts trivially.

2. **Local Euclidean charts + orientation collapse.** An effective \(\mathbb{Z}_p\)-action produces a free point and an invariant chart that compactifies (or odd-stabilizes) into a sphere \(S^d\), or into a Poincaré pair such as \(S^n\times\mathbb{CP}^2\), carrying a degree-one (or signature-one) class.

3. **Local duality / an integral signature lattice.** Either a sheaf Witt group with a uniform denominator bound, or ultimate quadratic \(L_4\) of an asymptotic category with integer ordinary signatures (a “tail”).

4. **Arbitrarily small open subgroups of \(\mathrm{Homeo}\).** Haar averaging / transfer along a nested sequence of open tails \(p^j\mathbb{Z}_p\) produces a degree coprime to \(p\) (OpenAI: degree one through the orbit space; Dabrowski: signature tail \(1\)) while finite quotients become unbounded \(p\)-powers.

**Question.** Which of (1)–(4) is essential to blocking continuous \(\mathbb{Z}_p\)-actions, and which can fail independently? In particular: is the obstruction the existence of an integral signature (Witt or \(L\)-theory tail) that cannot be infinitely \(p\)-divisible, or is it the combination of Newman charts with small subgroups of \(\mathrm{Homeo}\)?

**Sponge probe.** Faithful continuous \(\mathbb{Z}_p\)-actions exist on Menger compacta \(\mu^n\) (Dranishnikov), on the \(p\)-adic solenoid, and on Raymond–Williams compacta. On those spaces the theorem is false, so a correct manifold proof must fail some hypothesis. Both of the arguments above appear to break at (1)–(2) (no Euclidean chart / no combinatorial dual cells), not at the arithmetic of (3). Is that the right diagnosis — i.e., is the obstruction Euclidean rather than purely dynamical? Where would (3) or (4) fail first on ENR homology manifolds, if a free \(\mathbb{Z}_p\)-action existed there?

Background notes (not the question):  
OpenAI reverse-read: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
Dabrowski reverse-read: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/dabrowski/docs/Dabrowski_HS_Audit.pdf

---

## Reopen comment (after editing 515824)

Edited to a research question about which local Euclidean properties (Newman, charts/orientation, integral signature lattice, small subgroups of Homeo) block continuous \(\mathbb{Z}_p\)-actions, using two recent signature-style arguments as motivation rather than asking for verification. Please consider reopening.

---

## X (Twitter / Bluesky-ready)

**Short (recommended):**

Two 2026 Hilbert–Smith claims, same obstruction family: integrality vs \(p\)-divisibility of a signature.

OpenAI (Sep 23): Witt lattice on \(S^d\), equal parts \(4/p^k\).  
Dabrowski (Oct 8): \(L_4\) tail + \(\mathbb{CP}^2\), then \(1\in p\mathbb{Z}\).

Neither is Yang dim-raising. Sponges break both at charts/Newman.

https://github.com/ajjcoppola/hilberts-5th-oai

**Even shorter:**

OpenAI and Dabrowski both try Hilbert–Smith via signature integrality vs \(p\)-divisibility (Witt sheaves vs \(L_4\) tails). I reverse-read both. Question: which Euclidean properties actually block \(\mathbb{Z}_p\)?

https://github.com/ajjcoppola/hilberts-5th-oai

---

## Superseded (2026-10-07 work-checking draft — do not repost)

Closed as off-topic. Kept only for history.

**Old title:** Independent reverse-read of OpenAI’s Hilbert–Smith preprint (all finite dimensions)

OpenAI’s Math Release includes a preprint claiming the Hilbert–Smith conjecture in every finite dimension. I posted an independent reverse-verification note. That framing (is it correct / finish my verification) is what MO rejected.
