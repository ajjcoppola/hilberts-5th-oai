# From Binghamton in 1980 to two 2026 Hilbert–Smith arguments

**AI disclaimer.** This essay, and the papers and notes it points to, are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under my direction. Errors remain mine.

**A development story, not a proof.**  
Alan J. Coppola · 20 October 2026  
For Substack (Alan Coppola) or Medium (@ajjcoppola)

---

I wrote a dissertation on *p*-adic transformation groups at SUNY Binghamton in 1979–80, with Louis F. McAuley as advisor. The problem I lived with then is the same problem that two 2026 manuscripts now claim to settle on Euclidean manifolds: can the additive group of *p*-adic integers act continuously and faithfully on a connected finite-dimensional topological manifold?

Last month OpenAI included such a claim in a large public dump of AI-written mathematics. A few days later another argument appeared, by A. Dabrowski’s agents, using a different algebraic packaging of what looks to me like the same geometric idea. I have spent the weeks since then reverse-reading both writeups, mapping them across homology and cohomology manifolds, and putting the work into a public GitHub repository.

I am not announcing that Hilbert–Smith is proved. I am writing down what I think I understand, where the 2026 arguments sit relative to the 1980 transfer machine, and what construction I still do not know how to finish.

Repository: https://github.com/ajjcoppola/hilberts-5th-oai

---

## What the conjecture actually asks

Hilbert’s fifth problem, in the compact transformation-group form, asks which locally compact groups can act continuously and effectively on manifolds. Gleason, Montgomery, and Zippin answered the connected case: the group must be a Lie group. The remaining compact obstruction is usually stated as *p*-adic exclusion. Finite cyclic groups of *p*-power order act freely on manifolds — that is what lens spaces are for. The additive *p*-adic integers, written ℤ_p, are the inverse limit of those finite groups. They have an infinite descending chain of open subgroups. The conjecture says that this infinite chain cannot act faithfully and jointly continuously on a connected finite-dimensional manifold.

If such an action existed, Newman’s theorem would produce a small open subgroup that still acts faithfully on a Euclidean chart. Everything after that is an attempt to extract a contradiction from “arbitrarily small continuous motion of Euclidean space.”

---

## What I proved in 1980

The tool I built was a *p*-adic transfer homomorphism for the inverse system of finite cyclic groups ℤ_{p^r}. With it one can write down Smith–Yang exact sequences for actions on compact metric spaces.

Two facts were already clear, and they still organize the subject.

Over the rationals, or over any field whose characteristic is not *p*, the transfer is a projection at every finite stage. Passing to the limit, the rational Čech cohomology of the orbit space is just the invariant cohomology of the space. There is no rational dimension jump.

Over the integers, and over the field with *p* elements, transfer composed with projection is multiplication by a power of *p*, which is zero modulo *p*. That is where Bockstein and Smith–Gysin maps appear, and that is why cohomological dimension can go up. On a compact *n*-manifold, Yang’s theorem and the Bredon–Raymond–Williams calculation give

dim_ℤ(M / A_p) = n + 2,

with a *p*-torsion top class. The jump is *p*-torsion. It is not a rational phenomenon.

Raymond and Williams, in 1960 and 1963, already realized that same (*n*+2)-dimensional jump on an *n*-dimensional compactum, by inverse limits of complexes with period-*p*^i homeomorphisms. Those examples are not locally Euclidean, and they are not locally connected in the cohomology-manifold sense. They are the standing reminder that “dimension goes up” is not, by itself, a proof that the space was a manifold.

---

## McAuley’s 2001 manuscript, and the break

In 2001 McAuley posted an arXiv manuscript that attempted a full proof of Hilbert–Smith. He uses of the space only local compactness, connectedness, local connectedness in dimension *n*, and local homology of a ball. Because the orbit space has dimension *n*+2, saturated covers pulled back from the orbit space have order greater than *n*+1. To force unique *n*-cycles he interposes a refinement of order *n*+1. That cover cannot be invariant under the *p*-adic group. The resulting chain maps fail to be equivariant on the *n*-skeleton of the nerve. The missing (*n*+1)-chain is exactly where the Smith–Yang transfer cocycle lives.

I record this as a historical diagnosis, not as a replacement proof. The lesson I took from it, and from Ščepin’s community account of the episode, is a seminar rule I have tried to follow this month: ask for the counterexample before you read the proof. A claimed proof of an open theorem is not refuted by rereading it. It is refuted when the same lemmas still run on a space where the conclusion is already false.

---

## October 2026: I woke up to a dump

On 6 October 2026 OpenAI published hundreds of manuscripts produced by an internal model, among them a 23 September preprint titled *The Hilbert–Smith conjecture in every finite dimension*. There is no Lean formalization of that argument in the release. Coverage in the press was about the dump as a social event, not about Newman charts or Witt lattices.

I have worked on this problem in the way-past. I asked Cursor, using Grok, Anthropic, and OpenAI models under my direction, to help me reverse-read the manuscript against my own background. The first public artifact was an audit PDF, not a referee report.

The OpenAI argument is not Yang’s dimension-raising. After Newman’s theorem produces a small faithful *p*-adic action on a Euclidean chart, the action is odd-stabilized into a sphere. Haar averaging of a degree-one pinch through the orbit space manufactures an integral Witt, or signature, class. Character projectors then split that class into *p*^k equal rational pieces. A comparison lattice on the sphere has a denominator bound that does not grow with *k*. For large *k* the pieces no longer fit. Integrality fights unbounded *p*-divisibility.

I posted a MathOverflow question asking how verification of this kind of manuscript should proceed. It was closed as work-checking, which was the right close for the question I actually asked. I have since rewritten it as a research question about which local Euclidean properties do the blocking. That rewrite is in the repository. I still have not claimed that the OpenAI proof is correct, and I still have not asked anyone to finish my verification.

Two days later a second argument appeared: A. Dabrowski, *Integral tail signatures and the Hilbert–Smith conjecture*, with a claimed Lean 4 certificate. I vendored the PDF, reverse-read it the same way, and later compiled the palomar Lean tree locally. The axioms that print for the formalized corollary are the usual Lean ones: propositional extensionality, classical choice, and quotient soundness. That is not the same as a human understanding of the geometry.

Dabrowski’s packaging is different and, to my eye, the same obstruction class. Haar averaging in a Euclidean chart produces a degree-one pinch. A character detector supplies a compact free cyclic space. A duality-compatible homotopy idempotent on the product of a sphere with complex projective plane forgets to a scalar germ whose iterated Karoubi localization recovers one copy of complex projective plane. The resulting class in an L-theory group has integer signature tail constantly 1. Independently, permutation modules that look locally like *p* copies of the identity, after controlled Mayer–Vietoris, force every such tail to be eventually *p*-divisible. Hence 1 lies in *p*ℤ.

So: OpenAI splits a unit into equal parts inside a fixed lattice. Dabrowski keeps a tail of signature 1 and proves eventual *p*-divisibility. Both need a Euclidean chart, Newman rigidity, orientation, and arbitrarily small open subgroups of the homeomorphism group. On Menger compacta, on the *p*-adic solenoid, and on Raymond–Williams spaces — where faithful continuous *p*-adic actions exist — both arguments appear to break at the chart, not at the arithmetic. That is what “correctly scoped” means. It is also why emptiness of the manifold stratum is not a license to build an action.

---

## Homology manifolds: six classes, one open target

Once the Euclidean shell is visible, the natural question is not “is Hilbert–Smith true?” It is: on which spaces does this shell still make sense?

I organized the answer as six classes of homology and cohomology manifolds.

1. If you drop local connectedness, or mismatch coefficients, you are already outside the 2026 scopes. Counterexample mechanisms live here; they are not manifold theorems.

2. A shrinking necklace, or a junction space, can be a integer-homology manifold and still fail local homology at a point. I treat that as an explicit counterexample to a too-strong claim, not as a counterexample to Hilbert–Smith.

3. Connected polyhedral homology manifolds reduce to the topological-manifold case.

4. Resolvable Euclidean neighborhood retracts, and spaces with a nonempty manifold stratum, likewise reduce: you get a chart, or you stabilize and get a chart.

5. The crown jewel is a Bryant–Ferry–Mio–Weinberger Euclidean neighborhood retract with empty manifold stratum and Quinn index not equal to 1. Quinn’s index is a local signature that asks whether the duality comes from genuine manifold charts, up to cell-like collapse. It is not a cobordism classification of Euclidean space. On these spaces OpenAI’s equal-parts lattice, once rephrased without a source sphere, still kills every nonzero index. Dabrowski’s single-*p* cyclotomic detector does not: if an odd prime *p* divides the Quinn index, a single index-*p* step only puts the index in *p*ℤ, which is not a contradiction. A *k*-step cyclotomic tower restores *p*^k-divisibility. I formalized that arithmetic in Lean 4. Bounded-dimension inverse limits are blocked by a trichotomy: Cantor fibers, an Euler–Smith obstruction, or destruction of local homology.

6. Drop finite covering dimension while keeping finite cohomological dimension. Local duality can still look *n*-dimensional over the integers, but every neighborhood can have infinite covering dimension. Edwards–Walsh resolutions and Dranishnikov’s work on compact group actions live here. The 2026 Euclidean-neighborhood-retract packaging does not apply. This is the remaining construction I have tried for: an effective *p*-adic action on a compact integer-cohomology manifold of finite cohomological dimension and infinite covering dimension.

Classes 3 through 5, as I currently understand them, give exclusion *relative* to the 2026 geometric engines. Class 6 is not an existence theorem. Finite-stage algebraic gates in a Borel-join Edwards–Walsh plus Williams scaffolding pass a symbolic harness. The continuous glue of locally connected integer Poincaré duality across simplex boundaries, pulled back over a Yang (*n*+2)-dimensional orbit space, is still open.

---

## How I have been working

I am not a twenty-year-old formalizer, and I am not pretending to be one. I directed the work in Cursor. The models that drafted, typeset, searched, and compiled with me were Grok, Anthropic, and OpenAI models. I kept a counterexample ledger, a sponge test, two audit PDFs, an archive manuscript, two slide decks, and a small Lean library sitting on top of Dabrowski’s arithmetic rather than reimplementing his L-theory. When a MathOverflow close reason told me that “AI-generated verification” was the wrong ask, I changed the ask.

The slide decks try to make the algebra geometric. Quinn’s index, OpenAI’s Witt characters, and Dabrowski’s L-theory tails are three bookkeeping languages for the same picture: a neighborhood that can produce a degree-one or signature-one unit, together with finite cyclic covers that split that unit by covering degree.

If you only remember one honesty sentence, remember this one. This repository does not claim a standalone classical Hilbert–Smith proof.

---

## What I would like

Collaborators who already speak Euclidean neighborhood retracts, Quinn index, cohomological dimension, or Lean 4. Comments on the remaining glue, not endorsement of OpenAI or Dabrowski. Readers who will open the HTML slides in a browser, because GitHub’s file view will not render the mathematics.

I have chosen to put the work in one place so that a post can point at a checkpoint instead of a private folder.

- Repository: https://github.com/ajjcoppola/hilberts-5th-oai
- Draft paper: `papers/padic-homology-manifolds/main.pdf`
- Invariants slides: `presentations/invariants-quinn-witt-dabrowski/index.html`
- Homology-manifold slides: `presentations/padic-homology-2026/index.html`
- OpenAI reverse-read: `docs/Hilbert_Smith_Audit.pdf`
- Dabrowski reverse-read: `dabrowski/docs/Dabrowski_HS_Audit.pdf`

Checkpoints: `checkpoint/hm6-2026-10-18` and `checkpoint/invariants-deck-2026-10-19`.

I am still trying to construct the class-six example. Until the glue is verified, that sentence is a research program, not a theorem.

---

*Alan J. Coppola, Ph.D. SUNY Binghamton 1979/80. Email: ajjc@optngn.com.*
