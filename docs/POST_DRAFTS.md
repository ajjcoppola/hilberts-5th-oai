# Post drafts (updated 2026-10-20)

Repo: https://github.com/ajjcoppola/hilberts-5th-oai  
Checkpoint tags: `checkpoint/hm6-2026-10-18`, `checkpoint/invariants-deck-2026-10-19`  
Archive paper PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/papers/padic-homology-manifolds/main.pdf  
Invariants slides: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/presentations/invariants-quinn-witt-dabrowski/index.html  
OpenAI audit PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
Dabrowski audit PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/dabrowski/docs/Dabrowski_HS_Audit.pdf  
Outreach / collaborators: [`OUTREACH_COLLABORATORS.md`](OUTREACH_COLLABORATORS.md)

Closed MO question to edit/reopen: https://mathoverflow.net/questions/515824

**Do not** ask whether a proof is correct or to finish a verification. The body below is a research question about Euclidean structure; the two preprints are motivation.

---

## MathOverflow (paste-ready rewrite)

Paste the title and body below into the MathOverflow form. MathJax there renders `$...$` (including `\mathbb`). It does not render `\(...\)` in the title, and markdown can swallow `_` inside `\mathbb{Z}_p` before MathJax runs.

**Title:** Which local Euclidean properties block continuous $\mathbb{Z}_p$-actions? (OpenAI vs Dabrowski signature arguments)

**Tags:** `gt.geometric-topology` `at.algebraic-topology` `transformation-groups` `lie-groups`

**Body:**

The Hilbert–Smith conjecture is equivalent to $p$-adic exclusion: the additive group $\mathbb{Z}_p$ admits no faithful jointly continuous action on a connected finite-dimensional topological manifold. (Manifolds Hausdorff, second countable; actions jointly continuous.) Classical partial results include Lipschitz and quasiconformal actions, and Pardon’s theorem in dimension 3. The remaining problem is often described as a rigidity property of Euclidean charts under small subgroups of $\mathrm{Homeo}$.

Two recent arguments appear to use the **same obstruction class** — integrality versus $p$-divisibility of a signature / Witt invariant — with different packaging:

- OpenAI (2026-09-23): after Newman chart reduction to a faithful open subgroup $G\cong\mathbb{Z}_p$ on $O\subset\mathbb{R}^n$, odd-stabilize into $S^d$, Haar-average a degree-one pinch through the orbit space, and split an integral Witt/signature class on $E_d(S^d)$ into $p^k$ equal pieces summing to $4\overline{u}_d$. A comparison lattice $L_d^{-1}\mathbb{Z}\,\overline{u}_d$ with $L_d=2^{e_d}$ independent of $k$ then yields a contradiction for $p^k>4L_d$.  
  https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026

- Dabrowski (2026-10-08): Haar-average coordinates in a Euclidean chart to get a degree-one pinch on $S^n$; a character detector supplies a compact free $C_p$-space $T$; a duality-compatible homotopy idempotent on $S^n\times\mathbb{CP}^2$ forgets to a scalar germ whose iterated Karoubi localization boundaries recover one copy of $\mathbb{CP}^2$. The resulting class in $L_4(A_G(T))$ has integer signature tail constantly $1$. Independently, permutation-tensoring $\tau=\mathbb{Q}[G_i/P_i]$ is locally $p$ copies of the identity and is nilpotent after controlled Mayer–Vietoris, so every such class has eventually $p$-divisible ordinary signatures. Hence $1\in p\mathbb{Z}$.  
  https://github.com/adbrw/HS_proof

I am **not** asking whether either manuscript is correct, complete, or ready to referee. I want to isolate the **Euclidean input**.

Both writeups seem to need four local properties of $\mathbb{R}^n$ (or of topological manifolds):

1. **Newman rigidity.** A compact Lie group acting continuously and displacing every point of a small ball by less than some $\varepsilon>0$ acts trivially.

2. **Local Euclidean charts + orientation collapse.** An effective $\mathbb{Z}_p$-action produces a free point and an invariant chart that compactifies (or odd-stabilizes) into a sphere $S^d$, or into a Poincaré pair such as $S^n\times\mathbb{CP}^2$, carrying a degree-one (or signature-one) class.

3. **Local duality / an integral signature lattice.** Either a sheaf Witt group with a uniform denominator bound, or ultimate quadratic $L_4$ of an asymptotic category with integer ordinary signatures (a “tail”).

4. **Arbitrarily small open subgroups of $\mathrm{Homeo}$.** Haar averaging / transfer along a nested sequence of open tails $p^j\mathbb{Z}_p$ produces a degree coprime to $p$ (OpenAI: degree one through the orbit space; Dabrowski: signature tail $1$) while finite quotients become unbounded $p$-powers.

**Question.** Which of (1)–(4) is essential to blocking continuous $\mathbb{Z}_p$-actions, and which can fail independently? In particular: is the obstruction the existence of an integral signature (Witt or $L$-theory tail) that cannot be infinitely $p$-divisible, or is it the combination of Newman charts with small subgroups of $\mathrm{Homeo}$?

**Sponge probe.** Faithful continuous $\mathbb{Z}_p$-actions exist on Menger compacta $\mu^n$ (Dranishnikov), on the $p$-adic solenoid, and on Raymond–Williams compacta. On those spaces the theorem is false, so a correct manifold proof must fail some hypothesis. Both of the arguments above appear to break at (1)–(2) (no Euclidean chart / no combinatorial dual cells), not at the arithmetic of (3). Is that the right diagnosis — i.e., is the obstruction Euclidean rather than purely dynamical? Where would (3) or (4) fail first on ENR homology manifolds, if a free $\mathbb{Z}_p$-action existed there?

Background notes (not the question):  
OpenAI reverse-read: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
Dabrowski reverse-read: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/dabrowski/docs/Dabrowski_HS_Audit.pdf

---

## Reopen comment (after editing 515824)

Edited to a research question about which local Euclidean properties (Newman, charts/orientation, integral signature lattice, small subgroups of Homeo) block continuous $\mathbb{Z}_p$-actions, using two recent signature-style arguments as motivation rather than asking for verification. Please consider reopening.

---

## X (Twitter / Bluesky-ready)

**Short (recommended):**

Two 2026 Hilbert–Smith claims, same obstruction family: integrality vs $p$-divisibility of a signature.

OpenAI (Sep 23): Witt lattice on $S^d$, equal parts $4/p^k$.  
Dabrowski (Oct 8): $L_4$ tail + $\mathbb{CP}^2$, then $1\in p\mathbb{Z}$.

Neither is Yang dim-raising. Sponges break both at charts/Newman.

https://github.com/ajjcoppola/hilberts-5th-oai

**Even shorter:**

OpenAI and Dabrowski both try Hilbert–Smith via signature integrality vs $p$-divisibility (Witt sheaves vs $L_4$ tails). I reverse-read both. Question: which Euclidean properties actually block $\mathbb{Z}_p$?

https://github.com/ajjcoppola/hilberts-5th-oai

---

## Follow-up announcement (2026-10-20) — GitHub WIP

Frame as a **follow-up** to the reverse-read posts, not a new “HS is proved” claim. Pitch: the public repo now has a homology-manifold boundary map + an open HM-6 construction program.

### X / Bluesky (recommended, ~280–400 chars)

Follow-up to the OpenAI / Dabrowski Hilbert–Smith reverse-reads.

Public WIP on GitHub: relative boundary map of those 2026 signature arguments across homology-manifold classes HM-1..HM-6 (Quinn index, Lean k-tower, inverse-limit no-go). Open construction target: dim_Z = n but dim = ∞.

Not a classical HS proof. Coauthors welcome on the clc_Z glue.

https://github.com/ajjcoppola/hilberts-5th-oai

### X thread (3 posts)

1/ Follow-up. I reverse-read the two 2026 Hilbert–Smith signature arguments (OpenAI Witt lattice; Dabrowski L4 tails). Same obstruction family: integrality vs p-divisibility after a Euclidean germ.

Repo: https://github.com/ajjcoppola/hilberts-5th-oai

2/ WIP update: a relative map of those engines across homology / cohomology manifolds HM-1..HM-6.

Polyhedral + resolvable ENRs reduce. BFMW with Quinn I(X)≠1 is the ENR crown jewel (single-p arithmetic gap; k-tower repair in Lean). Bounded-dim inverse limits are blocked.

3/ Remaining bullseye is HM-6: finite cohomological dim, infinite covering dim. Borel-join Edwards–Walsh + Williams scaffolding is in the repo; the clc_Z glue is still open.

Draft paper + slides + library in the README. Not claiming classical HS. Help welcome.

https://github.com/ajjcoppola/hilberts-5th-oai

### LinkedIn

Follow-up to my reverse-reads of the two 2026 Hilbert–Smith arguments (OpenAI; Dabrowski).

The public GitHub repo now has a **WIP geometric-topology layer**: a relative boundary map of those signature machines across homology and cohomology manifolds (classes HM-1 through HM-6). Polyhedral and resolvable ENRs reduce to the manifold case. On Bryant–Ferry–Mio–Weinberger ENRs the Quinn index is the local signature that the 2026 packagings try to kill; Dabrowski’s single-p cyclotomic step has a gap when p divides I(X), repaired by a k-step tower (Lean 4). Bounded-dimension inverse limits are blocked by an Euler / Smith trichotomy.

The remaining open target is HM-6: compact Z-cohomology n-manifolds with finite cohomological dimension and infinite covering dimension. The repo has a Borel-join Edwards–Walsh + Williams construction program, a literature library, and slides on the shared geometry (unit-producing germ + cyclic covers) behind Quinn, Witt characters, and L4 tails.

This is **not** a standalone classical Hilbert–Smith proof. Seeking collaborators in ENR / cohomological dimension / Lean.

https://github.com/ajjcoppola/hilberts-5th-oai

### Mastodon / longer X alt

WIP follow-up on Hilbert–Smith + homology manifolds.

After reverse-reading OpenAI (Witt / equal parts) and Dabrowski (L4 signature tails), I posted a public boundary map: where those arguments extend, where they fail, and what is still constructible. Six classes HM-1..HM-6. Open candidate is infinite covering dimension with dim_Z still finite.

Repo (paper draft, Lean, harness, slides):
https://github.com/ajjcoppola/hilberts-5th-oai

---

## Archive paper + HM-6 (2026-10-18)

**Do not** claim a classical Hilbert–Smith proof. Pitch a *relative boundary map* and an open construction question.

### MathOverflow (follow-up research question — new post or reopen edit)

**Title:** Can $\dim_{\mathbb{Z}}X=n<\infty$ with $\dim X=\infty$ host a free $A_p$-action? (HM-6 after 2026 signature arguments)

**Tags:** `gt.geometric-topology` `at.algebraic-topology` `cohomological-dimension` `transformation-groups`

**Body (condensed):**

Assume for motivation the 2026 signature-style $p$-adic exclusion arguments on topological manifolds (OpenAI; Dabrowski). Independently of whether those manuscripts are correct, their Euclidean/ENR packaging appears not to apply to compact $\mathbb{Z}$-cohomology $n$-manifolds with finite cohomological dimension but infinite covering dimension (Edwards–Walsh / Dranishnikov / Dydak–Walsh).

Bounded-dimension inverse limits with free step-kernel $C_p$ on bonding fibers face a trichotomy (Cantor fibers / Euler–Smith / local $H_n$ destruction). A Borel-join Edwards–Walsh + Williams splicing architecture is proposed so that $\dim_{\mathbb{Z}}X=n$ while every neighborhood has $\dim U=\infty$, with finite-stage algebraic gates checked computationally.

**Question.** What is the precise obstruction (if any) to gluing local $clc_{\mathbb{Z}}$ degree-$n$ Poincaré duality across simplex boundaries when Edwards–Walsh blocks are pulled back over the Yang $(n+2)$-dimensional orbit space? Does Bredon–Raymond–Williams ($\dim_{\mathbb{Z}}(X/A_p)=n+2$) already forbid the limit, or only constrain it?

Background (not the question):  
https://github.com/ajjcoppola/hilberts-5th-oai (tag `checkpoint/hm6-2026-10-18`)  
Paper draft: `papers/padic-homology-manifolds/main.pdf`

### X / Bluesky

Relative boundary map of OpenAI + Dabrowski Hilbert–Smith arguments across homology-manifold classes HM-1..HM-6, plus an open HM-6 target ($\dim_Z=n$, $\dim=\infty$) with Lean $k$-tower + symbolic gates.

Not a classical HSC claim. Coauthors welcome on the $clc_Z$ glue.

https://github.com/ajjcoppola/hilberts-5th-oai

### LinkedIn

I posted reverse-reads of the two 2026 Hilbert–Smith signature arguments (OpenAI / Dabrowski) in a public GitHub audit repo. New checkpoint: a draft geometric-topology note that (i) frames exclusion results as *relative* to those engines, (ii) isolates Dabrowski’s single-$p$ Quinn-index gap and a $k$-tower repair (Lean 4), and (iii) opens a construction program for infinite-covering-dimension cohomology manifolds (HM-6). Seeking collaborators in ENR / cohomological dimension / Lean — details in the repo’s `docs/OUTREACH_COLLABORATORS.md`.

https://github.com/ajjcoppola/hilberts-5th-oai

### Lean Zulip / formal-conjectures comment (one paragraph)

Pointing at `lean/CoppolaHS` in https://github.com/ajjcoppola/hilberts-5th-oai (`checkpoint/hm6-2026-10-18`): cyclotomic $k$-tower arithmetic and an HM-6 escape shell from ENR packaging hypotheses. Looking for feedback on expanding beyond statement-level geometry; related to formal-conjectures Hilbert–Smith statement issues.

---

## Superseded (2026-10-07 work-checking draft — do not repost)

Closed as off-topic. Kept only for history.

**Old title:** Independent reverse-read of OpenAI’s Hilbert–Smith preprint (all finite dimensions)

OpenAI’s Math Release includes a preprint claiming the Hilbert–Smith conjecture in every finite dimension. I posted an independent reverse-verification note. That framing (is it correct / finish my verification) is what MO rejected.
