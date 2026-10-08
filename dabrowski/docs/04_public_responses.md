# Public responses to the Dabrowski Hilbert–Smith preprint (Q3)

**Search date:** 2026-10-08  
**Paper:** A. Dabrowski’s AI agents, *Integral tail signatures and the Hilbert–Smith conjecture*, 2026-10-08, in [adbrw/HS_proof](https://github.com/adbrw/HS_proof).

## Executive finding

As of the morning of 2026-10-08 there is **no published technical rebuttal or confirmation** of this proof’s correctness. The repository is hours old (`created_at` 2026-10-07T08:08:15Z; paper commit 2026-10-08 09:06:46 UTC). Coverage, if any, is announcement-level. This Sherlock pass is therefore an independent first read, not a digest of consensus.

**Lean status claimed by the author:** a Lean 4 / Mathlib formalization of Corollary 1.2 (`HSFormal/`, 238 modules), with `Challenge.lean` / `Solution.lean` for comparator and SafeVerify. Claimed axioms: `propext`, `Classical.choice`, `Quot.sound`. **This audit did not rerun the checkers.**

---

## Sources checked (2026-10-08)

| Venue | Finding |
|-------|---------|
| GitHub [adbrw/HS_proof](https://github.com/adbrw/HS_proof) | Public repo; 0 stars at vendor time; README states Thm 1.1 / Cor 1.2 and the Lean claims |
| MathOverflow | No hit on this preprint as of search (OpenAI Hilbert–Smith thread [515824](https://mathoverflow.net/questions/515824) was closed as work-checking; unrelated to Dabrowski) |
| arXiv | No matching submission found under this title at search time; paper lives on GitHub as `HSproof.pdf` |
| Wikipedia / Tao 2011 blog / classical MO 32656 | Background on the conjecture only; no 2026 Dabrowski discussion |
| Third-party HTML paste of the README | A garbled copy listed `HilbertSmithNegK.lean` and `HSproof.pdf` among “axioms.” The **vendored** README does not. Treat that paste as unreliable; settle the axiom list by `#print axioms` |

## What the upstream README claims (not independently verified)

- Lean `v4.35.0-rc3`; mathlib `1a547d8…`; TauCeti `c7af81f`.
- `lake env lean` axiom print of `HSFormal.hilbertSmith`.
- Comparator last line: “Your solution is okay!”; SafeVerify: “SafeVerify check passed.”
- Resource needs: Linux \(\ge\) 5.19 with Landlock, \(\sim\)15 GB disk, 16 GB RAM.

## Disclaimer in the PDF (p. 16)

The paper states that various LLMs (Anthropic, OpenAI, open-source) were used under human guidance at every stage; “the core idea and Lean4 formalization were obtained by Claude Opus 5.5 agents”; budget “below US$1,000.” That is process context, not a correctness argument.

## What to watch next

1. An independent `#print axioms HSFormal.hilbertSmith` from a clean `lake build`.
2. Expert notes from controlled topology / L-theory (Ranicki, Carlsson–Pedersen users) on §§2–6 and §§10–12.
3. Comparison with the OpenAI Witt-sheaf argument (same obstruction class; different packaging) — [`05_vs_openai.md`](05_vs_openai.md).
4. Any MathOverflow / arXiv appearance under a non-announcement title.

## Implication for this Sherlock session

Public silence on *technical* content means grades in [`02_audit_ledger.md`](02_audit_ledger.md) are provisional expert-prep. Target C is `WEAK` primarily because the Lean certificate was not rerun here, not because a false axiom was found in the PDF.
