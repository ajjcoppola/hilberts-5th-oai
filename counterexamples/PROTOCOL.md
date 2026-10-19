# Protocol: find the counterexample, then read the proof

Use this for any AI-assisted proof of an open or recently claimed theorem. Hilbert–Smith is the first instance ([`hilbert-smith/CAMPAIGN.md`](hilbert-smith/CAMPAIGN.md)).

## Step 1 — Reflect (wide net)

Write 5–7 places a false argument can hide. For a transformation-group or topology claim, start from this list and add proof-specific ones:

1. **Proves too much.** Drop “manifold” and the same lemmas still conclude “no faithful \(\mathbb{Z}_p\)” on a Menger compactum, a solenoid, or a Raymond–Williams space.
2. **Sanity.** The argument also rules out a finite Lie group, a trivial action, or a discontinuous action that the hypotheses were supposed to allow.
3. **Statement gap.** The PDF, the Lean type, and the classical conjecture are three sentences. A counter-model of the *formal* sentence need not be a counter-model of the conjecture.
4. **Algebraic lemma with no geometry left in it.** A WEAK step whose hypotheses are purely homological, sheaf-theoretic, or \(L\)-theoretic may apply on wild compacta even after the chart step has failed.
5. **Sign / decoration / negative \(K\).** The invariant that is supposed to be integral is only integral after an unproved comparison, so the contradiction \(1\in p\mathbb{Z}\) or \(4/p^k\notin L^{-1}\mathbb{Z}\) is about a different group.
6. **Certificate gaming.** The kernel accepts a proof of a shadowed, `sorry`-admitted, or axiom-smuggled statement. Compilation is not faithfulness.
7. **Decomposition trap.** Small Cantor fibers of a manifold (Walsh) are not a \(\mathbb{Z}_p\)-action. An argument that only uses the fibers has not touched Hilbert–Smith.

## Step 2 — Distill

Keep the two or three items that are both likely and testable. Rank them. For Hilbert–Smith the standing order is:

1. A WEAK lemma whose writeup already drops a dimension or manifold hypothesis (testable on a catalog model).
2. The PDF sentence versus the Lean type versus `#print axioms` (testable without new geometry).
3. An EDGE class (ANR, homology manifold) only after (1) leaks. Do not lead with an open existence question.

## Step 3 — Investigate

For each load-bearing lemma, fill one row of the ledger.

1. Copy the lemma’s hypotheses as written, not the theorem statement.
2. Delete the strongest hypothesis (usually “\(M\) is a topological manifold”).
3. Ask whether a catalog model still satisfies what remains.
4. If yes, run the lemma’s *conclusion* on that model. A false conclusion is a **HIT**. A hypothesis that fails is **SCOPED**. An unknown model is **EDGE**.

Stop at the first HIT. Do not grade later lemmas on that model until the hit is written down.

Compare the two Hilbert–Smith arguments on the same row. A lemma that is shared in substance (Haar averaging, integral signature, small open subgroups) only needs one counterexample.

## Step 4 — Analysis

Record, in this order:

- The model (name, citation, what is false about it).
- The lemma (label, file, the hypothesis that was supposed to keep the model out).
- The conclusion the lemma still gives, and the true fact it contradicts.
- Whether the hit kills the claimed theorem or only a stronger intermediate claim. Ščepin’s pattern is the second: the intermediate claim is false, so the writeup is not a proof, even if the conjecture is true.

## Step 5 — What to log next

If there is no HIT:

- Name the hypothesis that blocked every catalog model. That hypothesis is the real theorem.
- Say which EDGE class would become a HIT if a faithful action were found there.
- For a Lean certificate: `#print axioms`, search `sorry` / `sorryAx` / `native_decide` / `axiom` / `@[csimp]`, and diff the formal statement against the classical one.

If there is a HIT: write the model and the lemma in the campaign file before any further reading.

## Step 6 — Cleanup

No temporary diagnostics are part of this protocol. If a later session adds scratch computations, remove them only after the ledger row is filled.

## External constraints on the method

These are the sources for the method, not for Hilbert–Smith geometry (that catalog is separate).

| Source | What it contributes |
|--------|---------------------|
| [MO 32656](https://mathoverflow.net/questions/32656), Belegradek on McAuley [arXiv:math/0103215](https://arXiv.org/abs/math/0103215) | Template: a false HS proof dies because it proves a stronger false statement. The Istanbul / Ščepin account is a community report, not a published erratum located in this session. |
| [arXiv:2604.19459](https://arXiv.org/abs/2604.19459) | Formalization gaming: a compiling Lean proof need not formalize the intended statement. One model fabricated axioms; another mistranslated hypotheses so the error was invisible inside the proof. |
| [arXiv:2606.29493](https://arXiv.org/abs/2606.29493) | `sorry` admits an axiom. A downstream proof can cite it. Specification errors (dropped hypotheses, vacuous claims) inflate “solved”. |
| [arXiv:2610.00885](https://arXiv.org/abs/2610.00885) | Check syntax, frozen statement, name shadowing, elaboration, and `#print axioms`. Redefining a predicate can delete a hypothesis while the theorem name looks unchanged. |
| Lean issue #7463, as used in the TCB-expansion note | `#print axioms` can miss an axiom hidden behind `@[csimp]` and `native_decide`. A clean axiom list is not yet a counterexample, and it is not yet an all-clear. |

## Rules that keep the harness honest

- A sponge does not refute Hilbert–Smith. It refutes an argument that never used “manifold”.
- SCOPED on the first geometric lemma does not clear later WEAK lemmas. Those lemmas may be stated in a category the sponge still belongs to.
- Do not construct a \(\mathbb{Z}_p\)-action on a manifold. That is the open problem.
- Do not score Walsh decompositions as actions.
- Quote the lemma’s hypotheses. Paraphrases drift into the claimed theorem and hide the hit.
