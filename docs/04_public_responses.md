# Public responses to the OpenAI Hilbert–Smith preprint (Q3)

**Search date:** 2026-10-07  
**Paper:** OpenAI, *The Hilbert–Smith conjecture in every finite dimension*, 2026-09-23, in [openai/math](https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026).

## Executive finding

As of 2026-10-07 there is **no published technical rebuttal or confirmation** of this specific proof’s correctness. Coverage is almost entirely about the **release process** of OpenAI’s large math dump (hundreds of manuscripts), verification norms (Lean / Leiden / Palomar / Hexagon), and community reaction — not a line-by-line reading of the Hilbert–Smith argument.

**Lean status for this preprint:** No Lean formalization of the full Hilbert–Smith proof was found in the OpenAI math release materials. Related Lean activity exists only for *stating* the conjecture or Pardon’s 3D theorem (DeepMind `formal-conjectures`), and for other OpenAI results (`openai/ten-proofs`), not this manuscript.

---

## News / commentary (process, not proof audit)

| Source | Date (approx.) | Substance re: Hilbert–Smith |
|--------|----------------|------------------------------|
| [New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/) | ~2026-10 | Lists Hilbert–Smith among claimed results; Buzzard caution on which number-theory items look impressive / Lean-verified; notes AGMAI guidelines largely not followed |
| [Scientific American](https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock/) | ~2026-10 | Dump will take months to parse; many results Lean-checked but **not all**; company mathematicians may not yet understand all releases |
| [It Does What Now?](https://itdoeswhatnow.com/m/2026-10-06-openai-publishes-hundreds-of-ai-written-proofs-of-open-maths-problems/) | 2026-10-06 | Explicitly names Hilbert–Smith among claimed settlements; early reaction focuses on release ethics (Kra, Guillen, Litt, Bubeck); “nobody had yet had time to judge” correctness |
| [OfficeChai](https://officechai.com/ai/openai-releases-over-300-mathematical-results-produced-by-an-internal-model/) | ~2026-10 | Topology row lists Hilbert–Smith; stresses verification as the open question; Tao warning on superficially flawless AI proofs |
| AGI Hunt / aggregator posts | 2026-10-07 | Mentions Mahler, Unique Games, Hilbert–Smith, etc., as claimed in the batch |

## Expert / community technical venues

| Venue | Finding |
|-------|---------|
| MathOverflow | No hit on this OpenAI Hilbert–Smith preprint / Witt-sheaf argument (searches returned unrelated Witt-vector / prismatic posts) |
| arXiv | Paper appears to live on GitHub `openai/math`, not as a standard arXiv submission under that title (as of search) |
| Tao / Buzzard blogs | Commentary on AI math release practices in general; no dedicated Hilbert–Smith erratum/endorsement found in search |
| Palomar / Hexagon / Leiden | News notes OpenAI was encouraged to use these and largely did not for this dump |

## Lean / formalization adjacency

| Item | Relation |
|------|----------|
| [google-deepmind/formal-conjectures #2188](https://github.com/google-deepmind/formal-conjectures/issues/2188) | Issue to **formalize the statement** of Hilbert–Smith (pre-dates / independent of OpenAI proof) |
| [formal-conjectures PR #4599](https://github.com/google-deepmind/formal-conjectures/pull/4599) | Draft formalization of **Pardon’s 3D** p-adic exclusion statement |
| [openai/ten-proofs](https://github.com/openai/ten-proofs) | Lean for a *different* OpenAI package (sphere packing, codes, etc.) — not Hilbert–Smith |

## What to watch next

1. Expert notes from geometric topology / transformation groups (Pardon, Dranishnikov school, Raymond–Williams lineage).
2. Sheaf / Witt specialists reading §§2–4 (Woolf, Balmer–Walter users).
3. Any Lean port of `thm:dense-doubling`, `thm:sphere-lattice`, or `thm:contradiction`.
4. Journal submission / referee reports if the manuscript is submitted outside the GitHub dump.

## Implication for this Sherlock session

Public silence on *technical* content means this repo’s targeted audit and sponge stress test are **independent first-pass verification**, not a digest of an existing consensus. Grades in [`02_audit_ledger.md`](02_audit_ledger.md) should be read as provisional expert-prep, not as community acceptance.
