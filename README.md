# Hilbert–Smith reverse verification

Sherlock-mode audits of two 2026 preprints claiming the Hilbert–Smith conjecture in every finite dimension. Both arguments sit in the same family — **integrality versus \(p\)-divisibility of a signature / Witt invariant** after a Euclidean chart and Haar averaging — not Yang dim-raising and not Pardon’s 3-manifold mapping-class theorem.

**Author:** Cursor(Opus 5.5/Grok), driven by: Alan Coppola

## Archive paper + HM-6 program (checkpoint inside this repo)

**Published host for MO / X / LinkedIn posts:** this repository  
(`https://github.com/ajjcoppola/hilberts-5th-oai`).  
**Git tag:** [`checkpoint/hm6-2026-10-18`](docs/CHECKPOINT_HM6_2026-10-18.md) · outreach: [`docs/OUTREACH_COLLABORATORS.md`](docs/OUTREACH_COLLABORATORS.md)

**Alan J. Coppola**, *p-Adic Transfer, Signature Tails, and Homology Manifolds* (18 Oct 2026 draft):

| Deliverable | Path |
|-------------|------|
| Paper PDF | [`papers/padic-homology-manifolds/main.pdf`](papers/padic-homology-manifolds/main.pdf) |
| Paper TeX | [`papers/padic-homology-manifolds/main.tex`](papers/padic-homology-manifolds/main.tex) |
| Slides | [`presentations/padic-homology-2026/index.html`](presentations/padic-homology-2026/index.html) |
| Reviewer checklist | [`presentations/padic-homology-2026/checklist.pdf`](presentations/padic-homology-2026/checklist.pdf) |
| Sendable pack | [`presentations/padic-homology-2026/padic-homology-2026-pack.zip`](presentations/padic-homology-2026/padic-homology-2026-pack.zip) |
| CoppolaHS Lean | [`lean/CoppolaHS/`](lean/CoppolaHS/) (incl. `DranishnikovHM6.lean`) |
| HM-6 harness / loop | [`scripts/hm6_equivariant_ew_harness.py`](scripts/hm6_equivariant_ew_harness.py), [`HM6_LOOP_LOG.md`](counterexamples/hilbert-smith/HM6_LOOP_LOG.md) |
| Lean build status | [`dabrowski/lean-extension/BUILD_STATUS.md`](dabrowski/lean-extension/BUILD_STATUS.md) |

Relative boundary map of OpenAI/Dabrowski 2026 across HM-1..HM-6, Quinn-index $k$-tower (Lean), bounded-dim inverse-limit no-go, and open Borel-join Edwards–Walsh HM-6 target ($\dim_{\mathbb{Z}}X=n$, $\dim X=\infty$). **Does not claim a standalone classical HSC proof.** Optional local Dabrowski palomar clone for `#print axioms` is documented in [`dabrowski/PROVENANCE.md`](dabrowski/PROVENANCE.md) (not vendored here).

| Proof | Date | Packaging | Audit PDF |
|-------|------|-----------|-----------|
| [OpenAI](https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026) | 2026-09-23 | Witt/signature lattice on \(S^d\); equal parts \(4/p^k\) | [`docs/Hilbert_Smith_Audit.pdf`](docs/Hilbert_Smith_Audit.pdf) |
| [Dabrowski](https://github.com/adbrw/HS_proof) | 2026-10-08 | Integral tail in \(L_4(A_G(T))\); \(\mathbb{CP}^2\) realization vs \(p\mathbb{Z}\) | [`dabrowski/docs/Dabrowski_HS_Audit.pdf`](dabrowski/docs/Dabrowski_HS_Audit.pdf) |

Comparison: [`dabrowski/docs/05_vs_openai.md`](dabrowski/docs/05_vs_openai.md).

Counterexamples (ask for the counterexample before the proof): [`counterexamples/README.md`](counterexamples/README.md). Hilbert–Smith campaign: [`counterexamples/hilbert-smith/CAMPAIGN.md`](counterexamples/hilbert-smith/CAMPAIGN.md).

---

## OpenAI (2026-09-23)

**Upstream:** https://github.com/openai/math (vendored at `adc7f1241b42e322a6451854ab7e4b4c146bf78a`)

**Quick answers**

| Q | Answer |
|---|--------|
| 1. Near-id exclusion | Small open \(\mathbb{Z}_p\) subgroups + Haar averaging give a degree-1 test through the orbit space; finite groups cannot. |
| 2. Geometric vs algebraic | Mostly Witt/signature lattice arithmetic; thin geometric shell (Newman, chart, Serre). |
| 3. Public responses | Process news only (2026-10-07); no technical rebuttal; no Lean for this proof. |
| 4. Structure of \(\mathbb{R}^n\) | Signature-rigid under continuous \(\mathbb{Z}_p\) orbit factorization after odd stabilization into \(S^d\). |
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

Interactive canvas (open beside chat):  
[`hilbert-smith-audit.canvas.tsx`](/Users/ajjc/.cursor/projects/Users-ajjc-proj-Hilberts-5th-OAI/canvases/hilbert-smith-audit.canvas.tsx)

---

## Dabrowski (2026-10-08)

**Upstream:** https://github.com/adbrw/HS_proof (vendored at `abb0c44d58d711235f20b666ef422a4ea87b9add`)

**Quick answers**

| Q | Answer |
|---|--------|
| 1. Near-id exclusion | Small open tails of \(\mathbb{Z}_p\) Haar-average a degree-1 pinch in a chart; unbounded finite quotients feed an \(L_4\) tail of signature \(1\), which divisibility forces into \(p\mathbb{Z}\). |
| 2. Geometric vs algebraic | Mostly ultimate quadratic \(L\)-theory (Karoubi / Ranicki); thin Euclidean shell (chart, PL dual cells, \(\mathbb{CP}^2\)). |
| 3. Public responses | None technical as of 2026-10-08 morning; claimed Lean 4 certificate not rerun here. |
| 4. Structure of \(\mathbb{R}^n\) | Signature-tail rigid: a Euclidean germ realizes \(\mathbb{CP}^2\) with \(\sigma=1\), which cannot be eventually \(p\)-divisible. |
| 5. Menger sponges | Breaks at chart / combinatorial dual cells — correctly scoped. |
| 6. Orbit factoring? | Necessary but not sufficient; contradiction is \(\sigma_{\mathrm{tail}}=1\) vs eventual \(p\)-divisibility. |

**Targeted audit:** no `FAIL` on load-bearing PDF lemmas; `WEAK` on NegK/tail extraction, Mayer–Vietoris nilpotence, the graph corner, \(\mathbb{CP}^2\) evaluation, and Lean `#print axioms`.

- [`dabrowski/PROVENANCE.md`](dabrowski/PROVENANCE.md)
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

Paste-ready Euclidean-structure rewrite (not work-checking): [`docs/POST_DRAFTS.md`](docs/POST_DRAFTS.md).
