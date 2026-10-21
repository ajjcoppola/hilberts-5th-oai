# Hilbert–Smith reverse verification + homology-manifold boundary

Sherlock-mode audits of two 2026 preprints claiming the Hilbert–Smith conjecture in every finite dimension, plus a **relative** geometric-topology program that maps those arguments across homology / cohomology manifolds (HM-1..HM-6) and isolates an open construction target when $\dim_{\mathbb{Z}}X=n$ but $\dim X=\infty$.

Both 2026 arguments sit in the same family — **integrality versus $p$-divisibility of a signature / Witt invariant** after a Euclidean chart and Haar averaging — not Yang dim-raising and not Pardon’s 3-manifold mapping-class theorem.

**Author:** Alan J. Coppola  
**AI disclaimer:** This work is AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the author’s direction. See [`docs/AI_DISCLAIMER.md`](docs/AI_DISCLAIMER.md).  
**Repo:** https://github.com/ajjcoppola/hilberts-5th-oai

---

## Homology manifolds (HM-1..HM-6)

**Paper:** Alan J. Coppola, *p-Adic Transfer, Signature Tails, and Homology Manifolds* (18 Oct 2026 draft) —  
[`papers/padic-homology-manifolds/main.pdf`](papers/padic-homology-manifolds/main.pdf)

| Class | What it is | Faithful continuous $\mathbb{Z}_p$? |
|-------|------------|--------------------------------------|
| **HM-1** | Non-$clc$ / coefficient-mismatch Čech cohomology manifolds | Counterexample *mechanism* (outside 2026 scopes) |
| **HM-2** | Shrinking necklace / junction $\mathbb{Z}$-homology manifolds | **Explicit** counterexample (local homology fails) |
| **HM-3** | Connected polyhedral $L$-homology manifolds | **No** — reduces to manifold case (Thm C) |
| **HM-4** | Resolvable ENR / nonempty manifold stratum | **No** — chart or $X\times\mathbb{R}^2$ (Thm D) |
| **HM-5** | BFMW ENR, $X_{\mathrm{man}}=\varnothing$, Quinn $I(X)\neq 1$ | **No** (relative to OpenAI ENR rephrase or Dabrowski $k$-tower); bounded-dim inverse limits blocked |
| **HM-6** | Non-ENR: $\dim_{\mathbb{Z}}X=n<\infty$, $\dim X=\infty$ | **Open candidate** — escapes E/F/G(2); Borel-join EW+Williams scaffolding; $clc_{\mathbb{Z}}$ glue still open |

**Honesty:** Exclusion on manifolds/ENRs is **relative** to OpenAI/Dabrowski geometric engines. This repo does **not** claim a standalone classical Hilbert–Smith proof. HM-6 is a construction program, not a claimed existence theorem.

### Homology-manifold deliverables

| Deliverable | Path |
|-------------|------|
| Paper PDF / TeX | [`papers/padic-homology-manifolds/`](papers/padic-homology-manifolds/) |
| Main slides | [`presentations/padic-homology-2026/index.html`](presentations/padic-homology-2026/index.html) |
| Invariants deck (Quinn / Witt / Dabrowski + geometric germ) | [`presentations/invariants-quinn-witt-dabrowski/index.html`](presentations/invariants-quinn-witt-dabrowski/index.html) |
| Reviewer checklist / pack | [`presentations/padic-homology-2026/`](presentations/padic-homology-2026/) |
| Campaign + ledger + HM notes | [`counterexamples/hilbert-smith/`](counterexamples/hilbert-smith/) ([`HOMOLOGY_MANIFOLDS.md`](counterexamples/hilbert-smith/HOMOLOGY_MANIFOLDS.md), [`CAMPAIGN.md`](counterexamples/hilbert-smith/CAMPAIGN.md)) |
| Model catalog (incl. E4 = HM-6) | [`counterexamples/models/CATALOG.md`](counterexamples/models/CATALOG.md) |
| CoppolaHS Lean | [`lean/CoppolaHS/`](lean/CoppolaHS/) (`CyclotomicTower`, `QuinnIndex`, `DranishnikovHM6`, …) |
| HM-6 harness / loop | [`scripts/hm6_equivariant_ew_harness.py`](scripts/hm6_equivariant_ew_harness.py), [`HM6_LOOP_LOG.md`](counterexamples/hilbert-smith/HM6_LOOP_LOG.md) |
| Finish-line plan (Trunks A/B + glue P3) | [`plans/HM6_FINISH_LINE.md`](plans/HM6_FINISH_LINE.md) |
| Literature library (arXiv PDFs + construction notes) | [`library/README.md`](library/README.md) |
| Outreach / collaborators | [`docs/OUTREACH_COLLABORATORS.md`](docs/OUTREACH_COLLABORATORS.md) |
| Post drafts (MO / X / LinkedIn) | [`docs/POST_DRAFTS.md`](docs/POST_DRAFTS.md) |
| Development-story blog (Substack / Medium paste) | [`docs/BLOG_HILBERT_SMITH_DEV_STORY.md`](docs/BLOG_HILBERT_SMITH_DEV_STORY.md) |

### Checkpoints (git tags)

| Tag | Contents |
|-----|----------|
| [`checkpoint/hm6-2026-10-18`](https://github.com/ajjcoppola/hilberts-5th-oai/releases/tag/checkpoint/hm6-2026-10-18) | Archive paper, CoppolaHS Lean, HM-6 harness/loop, counterexample campaign |
| [`checkpoint/invariants-deck-2026-10-19`](https://github.com/ajjcoppola/hilberts-5th-oai/releases/tag/checkpoint/invariants-deck-2026-10-19) | Quinn / Witt / Dabrowski invariants slides (KaTeX + geometric germ narrative) |

Notes: [`docs/CHECKPOINT_HM6_2026-10-18.md`](docs/CHECKPOINT_HM6_2026-10-18.md).

### HM-6 construction sketch

Open frontier where OpenAI ENR rephrase, Dabrowski $k$-tower, and bounded-dimension Euler obstruction all fail:

- **Trunk A:** growing lens / solenoid / circle-bundle stages ([`library/constructions/trunk_A_lens_solenoid.md`](library/constructions/trunk_A_lens_solenoid.md))
- **Trunk B:** finite recursive $C_{p^i}$ + Edwards–Walsh Borel-join ([`library/constructions/trunk_B_cyclic_EW.md`](library/constructions/trunk_B_cyclic_EW.md))
- **Shared finish P3:** $clc_{\mathbb{Z}}$ Poincaré glue ([`library/constructions/glue_P3_clc.md`](library/constructions/glue_P3_clc.md))

Finite-stage algebraic gates G1–G4 **PASS** symbolically; continuous glue remains **EDGE / open**.

---

## 2026 preprint audits

| Proof | Date | Packaging | Audit PDF |
|-------|------|-----------|-----------|
| [OpenAI](https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026) | 2026-09-23 | Witt/signature lattice on $S^d$; equal parts $4/p^k$ | [`docs/Hilbert_Smith_Audit.pdf`](docs/Hilbert_Smith_Audit.pdf) |
| [Dabrowski](https://github.com/adbrw/HS_proof) | 2026-10-08 | Integral tail in $L_4(A_G(T))$; $\mathbb{CP}^2$ realization vs $p\mathbb{Z}$ | [`dabrowski/docs/Dabrowski_HS_Audit.pdf`](dabrowski/docs/Dabrowski_HS_Audit.pdf) |

Side-by-side: [`dabrowski/docs/05_vs_openai.md`](dabrowski/docs/05_vs_openai.md).  
Geometric packaging of the invariants: [`presentations/invariants-quinn-witt-dabrowski/`](presentations/invariants-quinn-witt-dabrowski/).

Counterexample protocol: [`counterexamples/README.md`](counterexamples/README.md).

---

## OpenAI (2026-09-23)

**Upstream:** https://github.com/openai/math (vendored at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`)

**Quick answers**

| Q | Answer |
|---|--------|
| 1. Near-id exclusion | Small open $\mathbb{Z}_p$ subgroups + Haar averaging give a degree-1 test through the orbit space; finite groups cannot. |
| 2. Geometric vs algebraic | Mostly Witt/signature lattice arithmetic; thin geometric shell (Newman, chart, Serre). |
| 3. Public responses | Process news only (2026-10-07); no technical rebuttal; no Lean for this proof. |
| 4. Structure of $\mathbb{R}^n$ | Signature-rigid under continuous $\mathbb{Z}_p$ orbit factorization after odd stabilization into $S^d$. |
| 5. Menger sponges | Theorem false for sponges; proof breaks at chart/Newman — correctly scoped, does not overclaim. |
| 6. Orbit factoring? | Necessary but not the whole story; contradiction is equal parts vs fixed denominator lattice. |

**Targeted audit:** no `FAIL`; several `WEAK` (dense doubling, Balmer–Walter bridge, character coproducts, equal-parts isometry).

- [`paper/`](paper/) — vendored LaTeX + PDF + provenance
- [`docs/01_proof_overview.md`](docs/01_proof_overview.md) — Q1, Q2, Q4, Q6
- [`docs/02_audit_ledger.md`](docs/02_audit_ledger.md) — lemma grades
- [`docs/03_sponge_stress_test.md`](docs/03_sponge_stress_test.md) — Q5 + sanity
- [`docs/04_public_responses.md`](docs/04_public_responses.md) — Q3
- [`docs/lemma_dependency_ledger.md`](docs/lemma_dependency_ledger.md)
- Rebuild: `python3 scripts/build_audit_pdf.py`

---

## Dabrowski (2026-10-08)

**Upstream:** https://github.com/adbrw/HS_proof (vendored at `abb0c44d58d711235f20b666ef422a4ea87b9add`)

**Quick answers**

| Q | Answer |
|---|--------|
| 1. Near-id exclusion | Small open tails of $\mathbb{Z}_p$ Haar-average a degree-1 pinch in a chart; unbounded finite quotients feed an $L_4$ tail of signature $1$, which divisibility forces into $p\mathbb{Z}$. |
| 2. Geometric vs algebraic | Mostly ultimate quadratic $L$-theory (Karoubi / Ranicki); thin Euclidean shell (chart, PL dual cells, $\mathbb{CP}^2$). |
| 3. Public responses | None technical as of 2026-10-08 morning; claimed Lean 4 certificate not rerun here. |
| 4. Structure of $\mathbb{R}^n$ | Signature-tail rigid: a Euclidean germ realizes $\mathbb{CP}^2$ with $\sigma=1$, which cannot be eventually $p$-divisible. |
| 5. Menger sponges | Breaks at chart / combinatorial dual cells — correctly scoped. |
| 6. Orbit factoring? | Necessary but not sufficient; contradiction is $\sigma_{\mathrm{tail}}=1$ vs eventual $p$-divisibility. |

**Targeted audit:** no `FAIL` on load-bearing PDF lemmas; `WEAK` on NegK/tail extraction, Mayer–Vietoris nilpotence, the graph corner, $\mathbb{CP}^2$ evaluation, and Lean `#print axioms`.

Local `#print axioms HSFormal.hilbertSmith` (optional palomar clone): `propext`, `Classical.choice`, `Quot.sound` — see [`dabrowski/PROVENANCE.md`](dabrowski/PROVENANCE.md), [`dabrowski/lean-extension/BUILD_STATUS.md`](dabrowski/lean-extension/BUILD_STATUS.md).

- [`dabrowski/paper/`](dabrowski/paper/) — vendored `HSproof.pdf` + Challenge/Solution + lake files
- [`dabrowski/lean/`](dabrowski/lean/) — sparse load-bearing modules (not the full 238)
- [`dabrowski/docs/01_proof_overview.md`](dabrowski/docs/01_proof_overview.md)
- [`dabrowski/docs/02_audit_ledger.md`](dabrowski/docs/02_audit_ledger.md)
- [`dabrowski/docs/03_sponge_stress_test.md`](dabrowski/docs/03_sponge_stress_test.md)
- [`dabrowski/docs/04_public_responses.md`](dabrowski/docs/04_public_responses.md)
- [`dabrowski/docs/05_vs_openai.md`](dabrowski/docs/05_vs_openai.md)
- Rebuild: `python3 scripts/build_dabrowski_audit_pdf.py`

---

## MathOverflow / posts

Paste-ready Euclidean-structure rewrite and HM-6 research question (not work-checking): [`docs/POST_DRAFTS.md`](docs/POST_DRAFTS.md).
