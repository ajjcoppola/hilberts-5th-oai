# Post drafts (2026-10-07)

Repo: https://github.com/ajjcoppola/hilberts-5th-oai  
PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf

---

## MathOverflow

**Title:** Independent reverse-read of OpenAI’s Hilbert–Smith preprint (all finite dimensions)

**Tags:** `gt.geometric-topology` `at.algebraic-topology` `transformation-groups` `lie-groups`

**Body:**

OpenAI’s Math Release includes a preprint claiming the Hilbert–Smith conjecture in every finite dimension:

https://github.com/openai/math/tree/main/preprints/The-Hilbert-Smith-conjecture-in-every-finite-dimension-September-23-2026

I posted an independent reverse-verification note (not a formal referee report):

- PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
- Repo: https://github.com/ajjcoppola/hilberts-5th-oai  

**Mechanism (as I read it).** The argument is not Yang’s orbit-dimension raising. After Newman chart reduction to a faithful open subgroup \(G\cong\mathbb{Z}_p\) on \(O\subset\mathbb{R}^n\), one odd-stabilizes into \(S^d\), averages a degree-one pinch through the orbit space near the identity, and builds equal Witt/signature character classes. Faithfulness supplies arbitrarily fine \(p^k\)-sheet regions; the classes are forced equal and sum to \(4\overline{u}_d\), contradicting a fixed denominator lattice \(L_d^{-1}\mathbb{Z}\,\overline{u}_d\) once \(p^k>4L_d\).

**Audit status.** Targeted check of load-bearing lemmas found no outright break. Items I marked weak for expert/Lean scrutiny include dense doubling, the Balmer–Walter localization bridge, character coproducts, and the equal-parts \(M_\beta\) isometry. On Menger/solenoid/Raymond–Williams spaces (where free \(\mathbb{Z}_p\) actions exist), the writeup correctly fails at Newman/chart hypotheses rather than “proving too much.”

**Questions for specialists.**

1. Does Balmer–Walter 2002, Thm 2.1 apply verbatim to the generated continuous categories \(\mathcal{T}(X)\) used here?
2. Is the germ/isometry step for the character multiplier \(\beta\) in the equal-parts proposition airtight?
3. Has anyone begun a Lean formalization of the lattice comparison or the final contradiction?

I am not claiming a refutation—only a structured first-pass map of the argument and its stress points.

---

## X (Twitter / Bluesky-ready)

**Short (recommended):**

Independent reverse-read of OpenAI’s claimed Hilbert–Smith proof (all finite dims).

Not Yang dim-raising — it’s an integrality-vs-divisibility Witt/signature argument on \(S^d\) after averaging a deg-1 test near id.

No outright FAIL in the load-bearing lemmas; several WEAK spots for experts. Menger sponges break the proof at Newman/chart (correctly scoped).

PDF: https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf  
Repo: https://github.com/ajjcoppola/hilberts-5th-oai

**Even shorter:**

OpenAI claimed Hilbert–Smith in all finite dimensions. I reverse-audited it.

TL;DR: Witt/signature lattice vs \(p^k\) equal parts — not Yang. No hard FAIL yet; a few WEAK lemmas. Sponges don’t break the writeup.

https://github.com/ajjcoppola/hilberts-5th-oai/blob/main/docs/Hilbert_Smith_Audit.pdf
