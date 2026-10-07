# Hilbert–Smith reverse verification (OpenAI preprint)

Sherlock-mode audit of OpenAI’s 2026-09-23 preprint claiming the Hilbert–Smith conjecture in every finite dimension.

**Author:** Cursor(Opus 5.5/Grok), driven by: Alan Coppola

**Upstream:** https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026  
**Vendored at:** `adc7f1241b42e322a6451854ab7e4b4c146bf78a`

**Main deliverable:** [`docs/Hilbert_Smith_Audit.pdf`](docs/Hilbert_Smith_Audit.pdf)

## Quick answers

| Q | Answer |
|---|--------|
| 1. Near-id exclusion | Small open \(\mathbb{Z}_p\) subgroups + Haar averaging give a degree-1 test through the orbit space; finite groups cannot. |
| 2. Geometric vs algebraic | Mostly Witt/signature lattice arithmetic; thin geometric shell (Newman, chart, Serre). |
| 3. Public responses | Process news only (2026-10-07); no technical rebuttal; no Lean for this proof. |
| 4. Structure of \(\mathbb{R}^n\) | Signature-rigid under continuous \(\mathbb{Z}_p\) orbit factorization after odd stabilization into \(S^d\). |
| 5. Menger sponges | Theorem false for sponges; proof breaks at chart/Newman — correctly scoped, does not overclaim. |
| 6. Orbit factoring? | Necessary but not the whole story; contradiction is equal parts vs fixed denominator lattice. |

**Targeted audit:** no `FAIL`; several `WEAK` (dense doubling, Balmer–Walter bridge, character coproducts, equal-parts isometry).

## Layout

- [`paper/`](paper/) — vendored LaTeX + PDF + provenance
- [`docs/01_proof_overview.md`](docs/01_proof_overview.md) — Q1, Q2, Q4, Q6
- [`docs/02_audit_ledger.md`](docs/02_audit_ledger.md) — lemma grades
- [`docs/03_sponge_stress_test.md`](docs/03_sponge_stress_test.md) — Q5 + sanity
- [`docs/04_public_responses.md`](docs/04_public_responses.md) — Q3
- [`docs/lemma_dependency_ledger.md`](docs/lemma_dependency_ledger.md) — dependency graph

- [`docs/Hilbert_Smith_Audit.pdf`](docs/Hilbert_Smith_Audit.pdf) — combined audit report with TeX-rendered math  
  Rebuild (needs `pandoc` + `tectonic`): `python3 scripts/build_audit_pdf.py`

Interactive canvas (open beside chat):  
[`hilbert-smith-audit.canvas.tsx`](/Users/ajjc/.cursor/projects/Users-ajjc-proj-Hilberts-5th-OAI/canvases/hilbert-smith-audit.canvas.tsx)
