# Homology Manifolds: Counterexamples vs. Proofs for $p$-Adic Actions

**AI disclaimer:** These notes are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola. See [`../../docs/AI_DISCLAIMER.md`](../../docs/AI_DISCLAIMER.md).

This document executes the second phase of the campaign: rephrasing the Hilbert–Smith $p$-adic exclusion problem across **all classes of homology and cohomology manifolds**, testing where **counterexamples** exist and where **proofs** (classical Smith–Yang–Coppola, OpenAI 2026, and Dabrowski 2026) hold or break.

Primary references used:
- **Alan J. Coppola (1980)**, *On $p$-adic Transformation Groups*, Ph.D. Thesis, SUNY at Binghamton (advised by L. F. McAuley; summarized in McAuley 2001 [28], p. 3).
- **Frank Raymond & R. F. Williams (1960/1963)**, *Examples of $p$-adic transformation groups*, Bull. AMS 66 (1960), 392–394 (`/Users/ajjc/Downloads/Examples_of_-adic_transformation_groups.pdf`) and Ann. of Math. 78 (1963), 92–106.
- **G. E. Bredon, F. Raymond, & R. F. Williams (1961)**, *$p$-adic groups of transformations*, Trans. AMS 99 (1961), 488–498.
- **Frank Raymond (1961, 1965)**, *The orbit spaces of totally disconnected groups of transformations on manifolds*, Proc. AMS 12 (1961), 1–7; *Some remarks on the coefficients used in the theory of homology manifolds*, Pacific J. Math. 15 (1965), 1365–1376.
- **Louis F. McAuley (2001)**, *A Proof Of The Hilbert–Smith Conjecture*, `arXiv:math/0103215v8` (`/Users/ajjc/Downloads/0103215v8.pdf`).
- **J. Bryant, S. Ferry, W. Mio, & S. Weinberger (1993/1996)**, *Topology of homology manifolds*, Bull. AMS 28 (1993), 324–328; Ann. of Math. 143 (1996), 435–467.
- **OpenAI (2026-09-23)** (`paper/`) and **A. Dabrowski (2026-10-08)** (`dabrowski/paper/HSproof.pdf`).

---

## 1. Summary Matrix across All Five Types of Homology Manifolds

| Class of Homology / Cohomology Manifold | Faithful continuous $\mathbb{Z}_p$-action? | Verdict & Mechanism |
|---|---|---|
| **HM-1: Non-$clc$ Čech cohomology $n$-manifolds over $L$ ($\mathrm{char}(L) \neq p$, e.g. $L = \mathbb{Q}, \mathbb{F}_\ell$) without $\mathbb{F}_p$-regularity** | **COUNTEREXAMPLE CLASS** | By Coppola's $p$-adic transfer / Bredon–Raymond–Williams Lemma 5.1, $\mathbb{Z}_p$-fibers are $\mathbb{Q}$-acyclic ($H^*(B\mathbb{Z}_p;\mathbb{Q})=\mathbb{Q}$). Dropping $lc^n$ over $\mathbb{Z}$ or $\mathbb{F}_p$-cohomology-manifold regularity allows Cantor-fibered spaces (Raymond 1961 Thm 2; Raymond 1965 p. 1376). |
| **HM-2: Disconnected or $0$-dimensional-junction $\mathbb{Z}$-homology $n$-manifolds** ($X = \bigsqcup_{i=1}^\infty S^n$ or one-point compactification / shrinking necklace at $x_\infty$) | **EXPLICIT COUNTEREXAMPLE** | Let $\mathbb{Z}_p$ act on the $i$-th piece $S^{2m-1}$ via $\mathbb{Z}_p \twoheadrightarrow C_{p^i} \subset S^1$ with piece diameter $2^{-i}$. The action is continuous everywhere and faithful ($\bigcap_i p^i\mathbb{Z}_p = \{0\}$), but global Newman fails across components (or local homology $H_*(X,X\setminus\{x_\infty\})$ fails at the junction $x_\infty$). |
| **HM-3: Connected Polyhedral (Simplicial / PL) $L$-Homology $n$-Manifolds** (over $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{Z}[1/p]$, or any $L\neq 0$, e.g. $\Sigma(S^{2m-1}/C_p)$ or $\Sigma H^3$) | **PROOF EXTENDS (Both OpenAI & Dabrowski work)** | **Theorem 3.1 below**: $X_{\mathrm{man}} = X \setminus \|K^{(n-2)}\|$ is a connected, dense, open, $\mathrm{Homeo}(X)$-invariant topological $n$-manifold. Moreover, Dabrowski's dual-block carrier acyclicity (Lemma 7.4, `HSproof.pdf:456–463`) holds directly on any polyhedral $\mathbb{Q}$-homology manifold. |
| **HM-4: Connected Resolvable ENR $\mathbb{Z}$-Homology $n$-Manifolds** (Quinn index $I(X)=1$, or any connected $\mathbb{F}_p$-cm with $X_{\mathrm{man}}\neq\varnothing$) | **PROOF EXTENDS (Both OpenAI & Dabrowski work)** | **Theorem 3.2 below**: Newman's Theorem holds globally on any connected $\mathbb{F}_p$-cohomology $n$-manifold (Smith 1941; Conner–Floyd 1959). If $X_{\mathrm{man}}\neq\varnothing$, a small open subgroup $p^j\mathbb{Z}_p$ acts faithfully on a Euclidean chart $O\subset X_{\mathrm{man}}$. |
| **HM-5: Nowhere-Euclidean Non-Resolvable ENR $\mathbb{Z}$-Homology $n$-Manifolds** ($n\ge 6$, Bryant–Ferry–Mio–Weinberger 1993, $X_{\mathrm{man}}=\varnothing$, Quinn index $I(X)\equiv 1\pmod 8$, $I(X)\neq 1$) | **OPENAI EXTENDS (rephrased); DABROWSKI BREAKS WHEN $p \mid I(X)$** | **Theorem 4.1 & Theorem 4.2 below**: Because $\mathcal{T}(S^d)$ is idempotent-complete (`02-categories.tex:38–39`), OpenAI's sheaf Witt machine accepts any compact ENR $\widehat{M}=X\times S^{d-n}$ and divides $4 I(X)$ by $p^k$ for arbitrarily large $k$, killing every $I(X)\neq 0$. Dabrowski's Lemma 3.1 (`HSproof.pdf:139`) divides by **only a single $p$** ($\Phi_{p^a}(1)=p$), which **fails to contradict** whenever an odd prime $p$ divides Quinn's index $I(X)$ (e.g. $I(X)=9, p=3$ or $I(X)=25, p=5$). |

---

## 2. Coppola (1980), Raymond–Williams (1960), and the Exact Break in McAuley (2001)

In `0103215v8.pdf` (p. 3, ref. [28]), L. F. McAuley summarizes **Alan J. Coppola's 1980 SUNY Binghamton dissertation, *On $p$-adic Transformation Groups***:

1. **$p$-Adic Transfer Homomorphism & Algorithmic Smith–Yang Sequences**:
   Coppola constructed a $p$-adic transfer homomorphism for inverse systems of finite cyclic actions $\mathbb{Z}_{p^r} = A_p / p^r A_p$ and used it to derive the system of Smith–Yang exact sequences governing $\mathbb{Z}_{p^r}$-actions on compact metric spaces.
   - Over a field $L$ of characteristic $\neq p$ (such as $\mathbb{Q}$), the transfer $(1/p^r)\sum_{g\in \mathbb{Z}_{p^r}} g^*$ is a projection at every finite stage, so passing to the limit identifies $\check{H}^*(X/A_p; \mathbb{Q}) \xrightarrow{\sim} \check{H}^*(X; \mathbb{Q})^{A_p}$. This is why OpenAI's `lem:orbit-injectivity` (`05-local-tests.tex:209–276`) is true on every compact metrizable $A_p$-space without any covering-dimension hypothesis.
   - Over $\mathbb{Z}$ and $\mathbb{F}_p$, however, the composite of transfer and projection is multiplication by $p^r \equiv 0 \pmod p$, creating the Bockstein / Smith–Gysin connecting homomorphisms that raise cohomological dimension.
2. **Homologically Uncomplicated Spaces ($lc^n$, $\dim_H X \le n$)**:
   Coppola proved that if $X$ is a compact metric $A_p$-space of homological dimension $\le n$ that is homologically locally connected ($lc^n$), then $H_{n+3}(A) = 0$ for every closed subset $A \subset X/A_p$. Thus the cohomological dimension of the orbit space is bounded by $n + 2$, and on an $n$-manifold (or $\mathbb{Z}$-homology $n$-manifold) $M$, Yang's theorem and Bredon–Raymond–Williams Theorem 3 show that this bound is achieved:
   $$\dim_{\mathbb{Z}}(M/A_p) = n + 2, \qquad H^{n+2}_c(M/A_p; \mathbb{Z})/K \cong \mathbb{Z}[1/p]/\mathbb{Z}.$$
   In `Examples_of_-adic_transformation_groups.pdf` (§§2–4, pp. 392–394), Raymond and Williams realized this exact $(n+2)$-dimensional jump on an $n$-dimensional compact metric space $X_n = \varprojlim E_i$ by building $(n+2)$-complexes $E_i$ with period-$p^i$ homeomorphisms $h_i$ that retract to $n$-skeleta ($r_i : X_i \to X_i(n)$, property (2e)) while keeping $H^{n+2}(E_i/h_i; \mathbb{Z}_p) \twoheadrightarrow H^{n+2}(E_{i-1}/h_{i-1}; \mathbb{Z}_p)$ surjective (property (3.2)).
3. **Why McAuley (2001) (`0103215v8.pdf`) Fails (and Proves Too Much)**:
   - On page 33 (`0103215v8.pdf:1906–1908`), McAuley notes that his argument uses of $M$ only that $(X, d)$ is locally compact, connected, $lc^n$, and has domains $D$ with $H_n(X, X - D; \mathbb{Z}_p) \cong \mathbb{Z}_p$.
   - Because $\dim(M/A_p) = n + 2$, McAuley's saturated covers $V^m$ pulled back from $M/A_p$ have order $> n + 1$ (`0103215v8.pdf:638–641`). Consequently, the nerve $N(V^m)$ has $(n+1)$- and $(n+2)$-simplices, and an $n$-homology class in $H_n(N(V^m); \mathbb{Z}_p)$ is **not** a unique $n$-cycle on the $n$-skeleton $N(V^m_n)$.
   - To force unique $n$-cycles so he can apply a Černavskiĭ sum $\sigma_m(\delta^n) = \sum_{s=0}^{p-1} g^s(\delta^n)$ to individual $n$-simplices (`0103215v8.pdf:207–211`), McAuley interposes a refinement $U^m$ of **order $n + 1$** (`0103215v8.pdf:578, 675`) with nerve maps $N(V^{m+1}) \xrightarrow{\alpha_m} N(U^m) \xrightarrow{\beta_m} N(V^m)$ and sets $z_m^n(\Delta) = \beta_m^*(\pi_{U^m}(\Delta)) \in Z_n(N(V^m_n); \mathbb{Z}_p)$.
   - **The break (`0103215v8.pdf:1460–1488`, Lemmas 6–8)**: Because $\mathrm{order}(U^m) = n + 1$ while $\dim(M/A_p) = n + 2$, the cover $U^m$ **cannot be $A_p$-invariant**, and $\beta_m^* \pi_{U^m}$ is **not $A_p$-equivariant** at the chain level on $N(V^m_n)$. For $g \in A_p \setminus H_1$, $g(z_m^n(\Delta))$ and $z_m^n(g_*\Delta) = z_m^n(\Delta)$ are homologous in the **full nerve** $N(V^m)$ via an $(n+1)$-chain boundary $\partial c_{n+1}$, **not** equal as $n$-chains in the $n$-skeleton $N(V^m_n)$! That missing $(n+1)$-chain is precisely where the Coppola / Smith–Yang transfer cocycle lives.

---

## 3. Counterexamples on Weakened Homology Manifolds (HM-1 & HM-2)

### Proposition 3.0 (Explicit Counterexamples When $lc^n$, $\mathbb{F}_p$-Regularity, or Connectedness is Dropped)
1. **Disconnected / Junction Counterexample (HM-2)**:
   Fix $m \ge 1$ and let $S^{2m-1} \subset \mathbb{C}^m$. On the $i$-th copy $M_i = S^{2m-1}$ ($i \ge 1$), let $\mathbb{Z}_p$ act via the quotient $\mathbb{Z}_p \twoheadrightarrow \mathbb{Z}_p / p^i\mathbb{Z}_p = C_{p^i} \subset S^1$, $z \mapsto \exp(2\pi\mathrm{i} a / p^i) z$.
   - On the disjoint union $X = \bigsqcup_{i=1}^\infty M_i$ (a second-countable Hausdorff topological $(2m-1)$-manifold without boundary, lacking only connectedness), the action of $\mathbb{Z}_p$ is jointly continuous and **faithful** because $\bigcap_{i=1}^\infty p^i\mathbb{Z}_p = \{0\}$.
   - Embed $M_i$ in $\mathbb{R}^{2m}$ as a sphere of radius $2^{-i}$ tangent to the origin $x_\infty = 0$ (or take the one-point compactification of $\bigsqcup_{i=1}^\infty (S^{2m-1} \times (0,1))$). Then $X$ is **compact, connected, and metrizable**, $X \setminus \{x_\infty\}$ is a smooth manifold, and the $\mathbb{Z}_p$-action extends continuously by fixing $x_\infty$ (since displacements on $M_i$ are $\le 2^{1-i} \to 0$).
   - **Why it is not a manifold/$\mathbb{Z}$-hm hit**: $X \setminus \{x_\infty\}$ has infinitely many connected components, and at $x_\infty$ the local homology $H_{2m-1}(X, X\setminus\{x_\infty\})$ has infinite rank.
2. **Coefficient-Mismatch Counterexample Mechanism (HM-1, Raymond 1961 Thm 2 / 1965 p. 1376)**:
   Suppose a space $X$ is only required to have $\mathbb{Q}$-cohomology dimension $n$ or Čech local $\mathbb{Q}$-cohomology of $\mathbb{R}^n$ without $lc^n$ over $\mathbb{Z}$ and without $\mathbb{F}_p$-cohomology-manifold regularity. Because $\check{H}^*( \mathbb{Z}_p; \mathbb{Q}) = \mathbb{Q}$ in degree $0$ and $0$ in degrees $> 0$, a Vietoris map over $\mathbb{Q}$ can have Cantor-set $\mathbb{Z}_p$-fibers (Wilder's monotone mapping theorem over $\mathbb{Q}$, noted by Raymond 1961, p. 2, and Raymond 1965, p. 1376). Both OpenAI and Dabrowski require local connectedness and either $\mathbb{F}_p$-Newman rigidity or a free point with a contractible neighborhood, so neither proof leaks onto HM-1.

---

## 4. Unconditional Proofs on Polyhedral and Resolvable Homology Manifolds (HM-3 & HM-4)

When can we prove that $\mathbb{Z}_p$ **cannot** act faithfully on a homology manifold?

### Theorem 3.1 (Reduction & Proof on Connected Polyhedral $L$-Homology Manifolds)
Let $L \neq 0$ be any commutative ring with unit (including $L = \mathbb{Z}$, $L = \mathbb{Q}$, $L = \mathbb{Z}[1/p]$, or $L = \mathbb{F}_\ell$ for any prime $\ell$), and let $X = |K|$ be a connected second-countable polyhedral $L$-homology $n$-manifold ($n \ge 1$). Then:
1. The open manifold stratum $X_{\mathrm{man}} = \{x \in X : x \text{ has a neighborhood homeomorphic to } \mathbb{R}^n\}$ contains $X \setminus |K^{(n-2)}|$ and is a **connected, dense, open, $\mathrm{Homeo}(X)$-invariant topological $n$-manifold without boundary**.
2. Every faithful continuous action of $\mathbb{Z}_p$ on $X$ restricts to a faithful continuous action of $\mathbb{Z}_p$ on the connected topological $n$-manifold $X_{\mathrm{man}}$.
3. Consequently, **both the OpenAI (2026) proof and the Dabrowski (2026) proof exclude faithful continuous $\mathbb{Z}_p$-actions on $X$**.

**Proof.**
In a simplicial complex $K$ that is an $L$-homology $n$-manifold, the link of every $(n-1)$-simplex $\tau$ has $\tilde{H}_0(\mathrm{link}_K(\tau); L) \cong H_n(|K|, |K| \setminus \mathrm{int}(\tau); L) \cong L$, so $\mathrm{link}_K(\tau)$ consists of exactly two vertices. Thus the open star in $|K| \setminus |K^{(n-2)}|$ of every $n$-simplex and every $(n-1)$-simplex is homeomorphic to $\mathbb{R}^n$, so $X \setminus |K^{(n-2)}| \subset X_{\mathrm{man}}$ is open and dense.
If $X \setminus |K^{(n-2)}|$ were disconnected, a union of $(n-1)$- and $n$-simplices would be separated from its complement entirely along $|K^{(n-2)}|$, contradicting the connectivity of the dual $(n, n-1)$-gallery graph of a connected homology $n$-manifold (equivalently, $\dim(|K^{(n-2)}|) \le n - 2$ cannot separate a connected $L$-homology $n$-manifold by local duality).
Since $X_{\mathrm{man}}$ is defined purely topologically, every homeomorphism of $X$ preserves $X_{\mathrm{man}}$. Because $X_{\mathrm{man}}$ is dense in $X$ and $X$ is Hausdorff, restriction $\mathrm{Homeo}(X) \to \mathrm{Homeo}(X_{\mathrm{man}})$ is injective. Applying either OpenAI (`thm:main`) or Dabrowski (Theorem 1.1) to the connected topological $n$-manifold $X_{\mathrm{man}}$ completes the proof. $\blacksquare$

> **Remark (Direct $L$-theory proof on polyhedral $\mathbb{Q}$-homology manifolds without deleting $|K^{(n-2)}|$).**
> Even if one runs Dabrowski's §7 directly on a finite combinatorial triangulation $K$ of a compact oriented $\mathbb{Q}$-homology $m$-manifold $A$ (such as the suspension $\Sigma(S^{2m-1}/C_p)$ of a lens space), Lemma 7.4 (`HSproof.pdf:456–463`) still holds verbatim! The proof of Lemma 7.4 identifies the dual-block carrier $C_r(J_\sigma)$ with the shifted rational cochain complex of $\mathrm{link}_K(\sigma)$ and uses only that $H_r(J_\sigma; \mathbb{Q}) = \mathbb{Q}$ ($r=0$) and $0$ ($r>0$)—which is the definition of a polyhedral $\mathbb{Q}$-homology manifold.

### Theorem 3.2 (Connected $\mathbb{F}_p$-Cohomology Manifolds with a Single Manifold Point)
Let $X$ be a connected Hausdorff second-countable $\mathbb{F}_p$-cohomology $n$-manifold of finite covering dimension (in particular, any connected $\mathbb{Z}$-homology $n$-manifold). If the manifold stratum $X_{\mathrm{man}}$ is **nonempty** (even if $X_{\mathrm{man}}$ is not dense or is a single tiny open ball), then any faithful continuous $\mathbb{Z}_p$-action on $X$ induces a faithful continuous action of an open subgroup $p^j\mathbb{Z}_p \cong \mathbb{Z}_p$ on a connected Euclidean open set $O \subset X_{\mathrm{man}} \hookrightarrow \mathbb{R}^n$, so both OpenAI and Dabrowski apply verbatim.

**Proof.**
By Newman's Theorem for connected $\mathbb{F}_p$-cohomology manifolds of finite covering dimension (Smith 1941; Conner–Floyd 1959, Cor. 6.2; Bredon 1960; Mj 2012, Thm 1.17), no periodic homeomorphism of $p$-power order on $X$ can fix a nonempty open subset of $X$ pointwise unless it is the identity on all of $X$.
Choose a point $x_0 \in X_{\mathrm{man}}$ and a coordinate ball $B \subset \overline{B} \subset C \subset X_{\mathrm{man}}$ around $x_0$. By the exact argument of OpenAI `prop:chart-reduction` (`05-local-tests.tex:31–67`), if every open subgroup $p^j\mathbb{Z}_p$ fixed a neighborhood of $x_0$ pointwise, then $F_j = \mathrm{int}_X \mathrm{Fix}(p^j\mathbb{Z}_p)$ would be nonempty and clopen in $X$ by Newman's theorem on connected $\mathbb{F}_p$-cohomology manifolds, forcing $F_j = X$ and contradicting faithfulness. Thus for small $H = p^j\mathbb{Z}_p$, $O = HB \subset C \subset \mathbb{R}^n$ is a connected $H$-invariant open Euclidean subset on which $H \cong \mathbb{Z}_p$ acts faithfully. $\blacksquare$

---

## 5. The Crown Jewel: Nowhere-Euclidean ENR $\mathbb{Z}$-Homology Manifolds (HM-5) and the Quinn-Index Separation Between OpenAI and Dabrowski

By Theorem 3.2, the **only** connected $\mathbb{Z}$-homology $n$-manifolds not immediately reduced to a Euclidean chart are those with **$X_{\mathrm{man}} = \varnothing$** (nowhere locally Euclidean).
Such spaces **exist** for every $n \ge 6$: **Bryant, Ferry, Mio, and Weinberger (1993/1996)** constructed compact connected ENR $\mathbb{Z}$-homology $n$-manifolds $X$ with $X_{\mathrm{man}} = \varnothing$ and arbitrary **Quinn resolution index**
$$I(X) \equiv 1 \pmod 8, \qquad I(X) \in \{ \dots, -15, -7, 1, 9, 17, 25, \dots \}, \qquad I(X) \neq 1.$$
By Quinn (1987), $I(X)$ is the local symmetric signature of $X$ (obtained by cutting $X$ down to a point along $n$ transverse codimension-$1$ homology-manifold hypersurfaces).

### Theorem 4.1 (Why Dabrowski's Arithmetic Engine Breaks on Non-Resolvable ENR $\mathbb{Z}$-Homology Manifolds When $p \mid I(X)$)
Suppose one replaces the compactified coordinate sphere $S^n$ in Dabrowski §§8–13 (`HSproof.pdf:580–946`) by a compact connected orientable non-resolvable ENR $\mathbb{Z}$-homology $n$-manifold $X$ ($n \ge 6$) with Quinn index $I(X) \equiv 1 \pmod 8$.
1. After $n$ iterated Karoubi localization boundaries cutting $X \times \mathbb{CP}^2$ to $S^0 \times \mathbb{CP}^2$ and projecting to one point component (`HSproof.pdf:806–822`, Prop. 12.4), the scalar germ is $I(X) \cdot [\mathbb{CP}^2]$, whose ordinary signature is
   $$\sigma_{\mathrm{tail}}(\alpha) = [(I(X), I(X), I(X), \dots)].$$
2. However, Dabrowski's divisibility theorem (Theorem 4.3, `HSproof.pdf:218`, via Lemma 3.1, `:139`, and `AlgebraicReduction.lean:24`) uses only that the cyclotomic polynomial $\Phi_{p^{a_i}}(t)$ satisfies
   $$\Phi_{p^{a_i}}(1) = p \quad \text{for every } a_i \ge 1,$$
   which forces **only single-$p$ divisibility** $\sigma_{\mathrm{tail}}(\alpha) \in p\mathbb{Z}^{\mathbb{N}}/\mathbb{Z}^{(\mathbb{N})}$, **never** $p^2$- or $p^k$-divisibility!
3. Therefore, for **every odd prime $p$ dividing $I(X)$** — for instance $p = 3$ on a BFMW homology manifold with $I(X) = 9 \equiv 1 \pmod 8$, or $p = 5$ with $I(X) = 25 \equiv 1 \pmod 8$, or $p = 7$ with $I(X) = -7 \equiv 1 \pmod 8$ — the relation
   $$I(X) \in p\mathbb{Z}$$
   **is true and produces NO CONTRADICTION!**

### Theorem 4.2 (How OpenAI's Proof Rephrases to Exclude $\mathbb{Z}_p$-Actions on All Compact ENR $\mathbb{Z}$-Homology Manifolds, For All $I(X) \neq 0$)
Let $X$ be a compact connected orientable ENR $\mathbb{Z}$-homology $n$-manifold ($n \ge 1$) with a continuous action of $\mathbb{Z}_p$. Rephrase OpenAI's construction (`paper/sections/05-local-tests.tex` and `06-character-classes.tex`) by setting $\widehat{M} = X \times S^{d-n}$ ($d > n$ odd, $d \ge 3$) in place of the source sphere $S^d$, while keeping the **target** test space as the standard sphere $S^d$:
1. **Newman & Free Orbit Sheets (`prop:chart-reduction`, `lem:finite-sheets`)**:
   Because $X$ is a connected $\mathbb{F}_p$-cohomology $n$-manifold of covering dimension $n$, Newman's theorem holds on $X$. Passing to $G = 2\mathbb{Z}_p \cong \mathbb{Z}_p$ preserves orientation on $X$. Choose a point $x_0 \in X$ where no open subgroup fixes a neighborhood, a small open neighborhood $O \subset X$ of $x_0$, and set $W = O \times \mathbb{R}^{d-n} \subset \widehat{M}$, with collapse $c : \widehat{M} \to W^+$ and orbit map $q : W^+ \to Y = W^+/G$.
2. **Idempotent-Complete Category Membership (`def:test-categories`, `02-categories.tex:30–40`)**:
   Because $X$ is a compact ENR, $\widehat{M} = X \times S^{d-n}$ is a **retract of a compact finite polyhedron $B$** ($i : \widehat{M} \hookrightarrow B$, $r : B \to \widehat{M}$, $r \circ i = \mathrm{id}_{\widehat{M}}$). Hence for every continuous test map $t : Y \to X_{\mathrm{test}}$ and $f_t = t \circ q \circ c : \widehat{M} \to X_{\mathrm{test}}$, the derived pushforward
   $$A_t = Rf_{t*} \underline{\mathbb{C}}_{\widehat{M}}$$
   is a **direct summand** of the polyhedral generator $R(f_t \circ r)_* \underline{\mathbb{C}}_B \in \mathcal{T}_0(X_{\mathrm{test}})$. Because $\mathcal{T}(X_{\mathrm{test}})$ is defined as the **direct-summand closure** of $\mathcal{T}_0(X_{\mathrm{test}})$ (`02-categories.tex:38–39`), **$A_t$ belongs to $\mathcal{T}(X_{\mathrm{test}})$ without any triangulation of $\widehat{M}$!**
3. **Verdier Duality & Orientation Form (`prop:test-duality`, `lem:orthogonality`)**:
   Because $\widehat{M}$ is a closed oriented $\mathbb{Z}$-homology $d$-manifold of finite $c$-soft dimension (embedded in $\mathbb{R}^N$), its dualizing complex over $\mathbb{R}$ is $\omega_{\widehat{M}} = a_{\widehat{M}}^!\mathbb{R} \simeq \underline{\mathbb{R}}_{\widehat{M}}[d]$ with invertible biduality $\eta : \underline{\mathbb{R}}_{\widehat{M}} \xrightarrow{\sim} \mathbb{D}_{\widehat{M}}^2 \underline{\mathbb{R}}_{\widehat{M}}$ (Borel–Moore 1960; Raymond 1965). Proper pushforward (`02-categories.tex:168`) supplies the symmetric form $\alpha_t : A_t \xrightarrow{\sim} \mathbb{D}_{X_{\mathrm{test}}, d} A_t$ in $\mathcal{T}(X_{\mathrm{test}})$, and over $X_{\mathrm{test}}^\circ = X_{\mathrm{test}} \setminus \{b_t\}$, $G$ acts on $f_t^{-1}(X_{\mathrm{test}}^\circ) \subset W$ by orientation-preserving homeomorphisms, hence by isometries of $\alpha_t|_{X_{\mathrm{test}}^\circ}$.
4. **Moving the Test Without Sliding Euclidean Balls (`prop:move-test`, `05-local-tests.tex:479–517`)**:
   For any nonempty open $V \subset Y \setminus \{y_\infty\}$ and $F = Y \setminus V$, the closed set $q^{-1}(F) = W^+ \setminus q^{-1}(V)$ misses the nonempty open subset $q^{-1}(V)$ of the connected orientable homology $d$-manifold $W$. By Poincaré–Alexander duality on $W$ (Raymond 1965, Eq. (4.1); cf. McAuley Lemma 9, `0103215v8.pdf:1792`),
   $$\check{H}^d(q^{-1}(F); \mathbb{Q}) \cong H_0(W, q^{-1}(V); \mathbb{Q}) = 0.$$
   Hence $(a \circ q|_{q^{-1}(F)})^*\gamma_d = 0$ automatically (without needing the sliding Euclidean round-ball homotopy $P_{z(t), r(t)}$ of `05-local-tests.tex:492–504`!). By `lem:orbit-injectivity` (Coppola's rational $p$-adic transfer), $(a|_F)^*\gamma_d = 0$, and `lem:odd-sphere-null` + `top:neighborhood-extension` produce $s > 0$ and $h \simeq D_s a$ constant on $F$.
5. **Killing Every Nonzero Quinn Index $I(X)$ (`thm:contradiction`, `06-character-classes.tex:445–500`)**:
   On the target sphere $S^d$, the denominator bound $L_d = 2^{e_d}$ of `thm:sphere-lattice` (`04-lattice.tex:371`) is a property of $\mathcal{T}(S^d)$ on the **standard sphere $S^d$** and does not depend on $X$.
   Given the nonvanishing of the pushed orientation class $\overline{[A_a, \alpha_a]} = 2 c_X \overline{u}_d \neq 0$ in $E_d(S^d) \otimes \mathbb{Q}$ for the degree-one averaged pinch $a \circ q \circ c : \widehat{M} \to S^d$ (where $c_X \in \mathbb{Z}\setminus\{0\}$ is the local signature / Quinn index, evaluated via the $d$-fold pole-cover localization boundary $E_d(S^d)\otimes\mathbb{Q}\xrightarrow{\sim}E_0(\mathrm{pt})\otimes\mathbb{Q}=\mathbb{Q}$ of `prop:sphere-rank`, `04-lattice.tex:203–251`), the character classes $z_0(a), \dots, z_{p^k-1}(a) \in E_d(S^d)$ satisfy
   $$\overline{z}_i(a) = \frac{4 c_X}{p^k} \overline{u}_d \in L_d^{-1}\mathbb{Z}\overline{u}_d.$$
   Choosing $p^k > 4 |c_X| L_d$ yields $0 < \frac{4 |c_X| L_d}{p^k} < 1$, a contradiction for **every** prime $p$ — even when $p \mid c_X$!

---

## 6. Publishable Extension vs. Inverse-Limit Simplicial Counterexample

### 6.1 Why the Extension to Compact ENR $\mathbb{Z}$-Cohomology Manifolds is Non-Trivial and Publishable
By Raymond (1965, Theorem 2), a compact ENR $\mathbb{Z}$-cohomology $n$-manifold $X$ is identical to a compact ENR $\mathbb{Z}$-homology $n$-manifold (a **generalized $n$-manifold** in Bryant–Ferry–Mio–Weinberger, *Ann. of Math.* 143 (1996), 435–467).
- **The Resolvable Case ($I(X) = 1$) Reduces by Stabilizing with $\mathbb{R}^2$**:
  If $I(X) = 1$ (even if $X_{\mathrm{man}} = \varnothing$ due to failure of the Disjoint Disks Property, as in Daverman–Walsh ghastly generalized manifolds), Daverman's theorem (*Topology Appl.* 11 (1980)) implies that $X \times \mathbb{R}^2$ has the Disjoint Disks Property and $I(X \times \mathbb{R}^2) = I(X) = 1$. By the **Edwards–Quinn Characterization Theorem**, $X \times \mathbb{R}^2$ is a genuine **topological $(n+2)$-manifold**. Thus any faithful $\mathbb{Z}_p$-action on $X$ extends (trivially on $\mathbb{R}^2$) to a faithful $\mathbb{Z}_p$-action on the topological $(n+2)$-manifold $X \times \mathbb{R}^2$, which is immediately excluded by the topological-manifold theorem.
- **Why the Non-Resolvable BFMW Case ($I(X) \equiv 1 \pmod 8$, $I(X) \neq 1$) Cannot Be Reduced by Any Product**:
  By Quinn's product formula (`5bb351bb` Theorem 3.1(iii), p. 443),
  $$I(X \times Y) = I(X) \cdot I(Y)$$
  for every generalized manifold $Y$. Since the only units in $\mathbb{Z}$ are $\pm 1$ and $I(Y) \equiv 1 \pmod 8$ (so $I(Y) \neq -1$), **$I(X) \neq 1 \implies I(X \times Y) \neq 1$ for every manifold or generalized manifold $Y$**. Thus $X \times Y$ is **never** a topological manifold ($X_{\mathrm{man}} = \varnothing$ persists under all finite products!), and neither OpenAI's `prop:chart-reduction` nor Dabrowski's §8 applies as written because both begin by choosing a Euclidean chart $O \hookrightarrow \mathbb{R}^n$.
- **Two Publishable Routes for Non-Resolvable BFMW Spaces ($I(X) \neq 1$)**:
  1. **Via OpenAI (Theorem 4.2 above)**: Replace the source sphere $S^d$ by $\widehat{M} = X \times S^{d-n}$ while keeping the target sphere $S^d$. Use (i) Conner–Floyd / Smith Newman on connected $\mathbb{F}_p$-cohomology manifolds, (ii) Hopf–Whitney degree-one pinch on $O^+ \wedge S^{d-n} \to S^d$, (iii) ENR retract summand membership $A_t = Rf_{t*}\underline{\mathbb{C}}_{\widehat{M}} \in \mathcal{T}(X_{\mathrm{test}})$, and (iv) Poincaré–Alexander duality $\check{H}^d(W^+\setminus q^{-1}(V);\mathbb{Q}) \cong H_0(W, q^{-1}(V);\mathbb{Q}) = 0$ in `prop:move-test`. Because $a : Y \to S^d$ is fixed before $k$ varies, $\overline{[A_a, \alpha_a]} = 2 c_X \overline{u}_d$ cannot be divided into $p^k$ equal parts in $L_d^{-1}\mathbb{Z}\overline{u}_d$ once $p^k > 4|c_X|L_d$.
  2. **Via a $k$-Step Tower Upgrade of Dabrowski's Cyclotomic Lemma**:
     As shown in Theorem 4.1, Dabrowski's single-$C_p$ detector $H/H' = H_j / H_{j+1} \cong C_p$ only gives $\Phi_{p^{a_i}}(1) = p$, which fails when $p \mid I(X)$ (e.g. $I(X) = 9, p = 3$).
     **The Fix**: Replace the single index-$p$ subgroup $H_{j+1} \subset H_j$ in Dabrowski §8 by a **$k$-step filtration**
     $$H_j \supset H_{j+1} \supset H_{j+2} \supset \cdots \supset H_{j+k}$$
     with $k$ equivariant sphere detectors $e_{\rho, r} : Z^+ \to T_r = S^{2m_r-1}$ for the free $C_p$-quotients $H_{j+r-1}/H_{j+r} \cong C_p$ ($r = 1, \dots, k$), and control over the product $T = T_1 \times \cdots \times T_k$. Then the $k$ commuting nilpotent operators $\nu_r = p\,\mathrm{id} - \tau_{G_i/P_{i,r}} \otimes (-)$ satisfy $\nu_r^{s_r} = 0$, so their product annihilates $\mathrm{Sign}_{G_i}(V_i, b_i)(g_i^{p^{r-1}})$ at primitive roots of unity of **$k$ distinct orders** $p^{a_i}, p^{a_i-1}, \dots, p^{a_i-k+1}$. In Lemma 3.1, the integer multiplicity polynomial $F(t) \in \mathbb{Z}[t]$ is then divisible by the product of $k$ distinct cyclotomic polynomials:
     $$\prod_{r=0}^{k-1} \Phi_{p^{a_i-r}}(t) \,\Big|\, F(t) \quad \text{in } \mathbb{Z}[t] \implies p^k = \prod_{r=0}^{k-1} \Phi_{p^{a_i-r}}(1) \,\Big|\, F(1) = \sigma(V_i, b_i)!$$
     Choosing $k$ so that $p^k > |I(X)|$ upgrades Dabrowski's contradiction from $I(X) \in p\mathbb{Z}$ to **$I(X) \in p^k\mathbb{Z}$**, killing every $I(X) \equiv 1 \pmod 8$ for every prime $p$ (once combined with BFMW's $\varepsilon$-Poincaré polyhedral approximations $X_i \to X$, `5bb351bb` Step IV, in place of a fixed triangulation).

---

### 6.2 Theorem 6.1 (No-Go Trichotomy for Inverse-Limit-of-Simplicial-Complexes Counterexamples)
Suppose one attempts to construct a counterexample as an inverse limit of finite $n$-dimensional simplicial complexes
$$X = \varprojlim (E_i, \pi_i)$$
with compatible simplicial actions of $C_{p^i} = \mathbb{Z}_p / p^i\mathbb{Z}_p$ on $E_i$ ($\pi_i \circ h_i = h_{i-1} \circ \pi_i$, as in Raymond–Williams `Examples_of_-adic_transformation_groups.pdf:59–86` or McAuley's $p$-adic polyhedra `0103215v8.pdf:83–87`).
Let $K_i = \ker(C_{p^i} \to C_{p^{i-1}}) \cong C_p$ be the step kernel, which preserves every point-inverse fiber $F_x = \pi_i^{-1}(x) \subset E_i$ ($x \in E_{i-1}$). Then at every regular orbit where $C_{p^i}$ acts freely on $E_i$, $K_i \cong C_p$ acts **freely** on the compact fiber $F_x$, forcing an inescapable **three-way obstruction**:

1. **Case 1 — Zero-Dimensional Fibers ($\dim F_x = 0$, $|F_x| = p$ discrete points)**:
   This is the unbranched covering tower (e.g. $S^1 \xleftarrow{z^p} S^1$ or lens-space towers $L^{2m-1}(p^i)$). In the inverse limit $X = \varprojlim E_i$, the $p^i$-point fibers accumulate into Cantor sets $\mathbb{Z}_p$, so $X$ is locally $\mathbb{Z}_p \times \mathbb{R}^n$, which **fails $lc^0$ (local connectedness)** and has infinite-dimensional $\check{H}^0(U; L)$ for small neighborhoods $U$. Thus $X$ is **never** a cohomology manifold over any ring $L$.
2. **Case 2 — Cell-Like / $\mathbb{Q}$-Acyclic Connected Fibers ($\tilde{H}^*(F_x; \mathbb{Q}) = 0$)**:
   To preserve local cohomology $H^*(X, X\setminus\{x\}; L) \cong H^*(\mathbb{R}^n, \mathbb{R}^n\setminus\{0\}; L)$ across the inverse limit via Wilder's monotone mapping theorem (or Vietoris–Begle), one wants connected fibers $F_x = \pi_i^{-1}(x)$ that are at least $\mathbb{Q}$-acyclic ($\tilde{H}^*(F_x; \mathbb{Q}) = 0$) or $\mathbb{F}_p$-acyclic ($\tilde{H}^*(F_x; \mathbb{F}_p) = 0$).
   - **$\mathbb{F}_p$-acyclic is impossible by P. A. Smith's Fixed Point Theorem (1938)**: No finite-dimensional compact space $F_x$ with $\tilde{H}^*(F_x; \mathbb{F}_p) = 0$ admits a free $C_p$-action.
   - **$\mathbb{Q}$-acyclic is impossible for finite subcomplexes by the Euler Characteristic Obstruction**:
     If $F_x$ is a finite subcomplex with a free $C_p$-action, the Lefschetz / Euler characteristic formula over $\mathbb{Q}$ gives
     $$\chi(F_x) = \sum_{q \ge 0} (-1)^q \dim_{\mathbb{Q}} H^q(F_x; \mathbb{Q}) = p \cdot \chi(F_x / C_p) \equiv 0 \pmod p,$$
     whereas $\tilde{H}^*(F_x; \mathbb{Q}) = 0 \implies \chi(F_x) = 1 \not\equiv 0 \pmod p$, a contradiction ($1 \in p\mathbb{Z}$)!
3. **Case 3 — Connected Fibers with $\chi(F_x) \equiv 0 \pmod p$ and $\tilde{H}^*(F_x) \neq 0$ (Raymond–Williams 1960/1963 & Dranishnikov Menger $\mu^n$)**:
   To make $F_x$ connected while carrying a free $C_p$-action, $F_x$ must carry nontrivial positive-dimensional cycles (for instance, a graph of Euler characteristic $1 - \beta_1 \equiv 0 \pmod p$ with $\beta_1 \equiv 1 \pmod p$, or the Raymond–Williams building blocks $X_i$ retracting onto their $n$-skeleton $X_i(n)$ in `Examples_of_-adic_transformation_groups.pdf:29`). Splicing these non-acyclic fibers into $E_{i-1}$ at each stage kills local homology $H_n(X, X\setminus\{x\}) \cong \mathbb{Z}$ along the splicing locus, turning $X$ into a Menger sponge or Raymond–Williams compactum rather than a cohomology manifold.

> **Bottom Line on Constructible Inverse-Limit Counterexamples**:
> Because of the Euler characteristic obstruction $\chi(F_x) \equiv 0 \pmod p$ (Case 2) and Smith's theorem, **the only way an inverse limit of simplicial complexes $X = \varprojlim (E_i, \pi_i)$ can avoid destroying local manifold homology on the open strata is if $K_i \cong C_p$ acts with fixed points on the bonding-map necks** — i.e., $E_i$ is a finite necklace/wedge of manifolds or lens spaces $S^{2m-1}/C_{p^j}$ joined along $C_{p^i}$-fixed singular points, converging to our **HM-2 shrinking-necklace counterexample** where local homology fails at the accumulation point $x_\infty$!

---

## 7. HM-6 Frontier: $\dim_{\mathbb{Z}} X = n < \infty$, $\dim X = \infty$ (2026-10-18)

Bounded-dimension towers are blocked by §6.2.  Relaxing *topological* covering dimension while keeping finite cohomological dimension reopens the construction door (class **HM-6**).

| Item | Status | Pointer |
|------|--------|---------|
| Escapes OpenAI ENR rephrase / Dabrowski $k$-tower / Euler Case 2 | **EDGE (architecture)** | Paper Thm `dranishnikov-escape`; dims $d_i\to\infty$ |
| Williams 1967 Part II torus obstruction | **BYPASSED (conditional on EW cells)** | Harness Gate G1; paper Rem. `williams-depends-on-skeleton` |
| Borel-join $E_{i+1}=(E_i\Delta_q EW_d)\times_{C_{p^{i+1}}}S^{2m-1}$ | **GATES PASS (finite stages)** | `scripts/hm6_equivariant_ew_harness.py` G1–G4 + BJ; `HM6_LOOP_LOG.md` |
| Lean formalization (connectivity, cup-length, ENR escape) | **BUILDS** | `lean/CoppolaHS/CoppolaHS/DranishnikovHM6.lean` |
| Continuous-limit $clc_{\mathbb{Z}}$ Poincaré glue across $\partial\sigma$ | **OPEN** | Paper Rem. `hm6-remaining` — not claimed as existence |

**Honesty:** HM-6 is an *open construction candidate*. Finite-stage algebraic gates pass; geometric existence of a free $A_p$-action on a $\mathbb{Z}$-cohomology $n$-manifold with $\dim U=\infty$ everywhere remains contingent on the glue step.

