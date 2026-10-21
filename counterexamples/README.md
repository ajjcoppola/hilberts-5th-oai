# Counterexamples to AI-assisted proofs

**AI disclaimer:** These notes are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola. See [`../docs/AI_DISCLAIMER.md`](../docs/AI_DISCLAIMER.md).

Seminar rule: **ask for the counterexample before the proof.**

A claimed proof of an open theorem is not refuted by rereading it. It is refuted when the argument still runs on a space where the conclusion is already false. That is how Ščepin treated McAuley’s 2001 Hilbert–Smith preprint: the writeup proved something stronger, and that stronger claim had a known counterexample (community account: [MathOverflow 32656](https://mathoverflow.net/questions/32656)).

This directory is the harness for that test. The first campaign is Hilbert–Smith.

## What a hit is

| Grade | Meaning |
|-------|---------|
| **HIT** | A named lemma still applies on a model where its conclusion is false. That model is a counterexample to the *argument*, not necessarily to the conjecture. |
| **SCOPED** | The lemma’s hypotheses fail on every known false model. The proof refuses to run. This is not a hit. |
| **EDGE** | The false model is not known to exist (homology manifolds, compact ANRs, small Hölder). A construction target, not a counterexample. |
| **TRAP** | Looks like a group action and is not (Walsh Cantor decompositions of manifolds). Do not score these as hits. |

No faithful continuous \(\mathbb{Z}_p\)-action on a manifold is known. Do not try to build one. The counterexamples live one hypothesis weaker than the claimed theorem.

## Layout

- [`PROTOCOL.md`](PROTOCOL.md) — how to extract, weaken, and score an AI proof
- [`models/CATALOG.md`](models/CATALOG.md) — spaces where a nearby claim is already false, with citations
- [`hilbert-smith/CAMPAIGN.md`](hilbert-smith/CAMPAIGN.md) — executed campaign: OpenAI (2026-09-23), Dabrowski (2026-10-08), McAuley (2001), and Coppola (1980)
- [`hilbert-smith/LEDGER.md`](hilbert-smith/LEDGER.md) — executed lemma × model grid (C1, C2, C3) with file:line citations
- [`hilbert-smith/HOMOLOGY_MANIFOLDS.md`](hilbert-smith/HOMOLOGY_MANIFOLDS.md) — counterexamples vs. proofs across all five types of homology manifolds (HM-1..HM-5)

Prior sponge notes (first-gate only, not this campaign): [`docs/03_sponge_stress_test.md`](../docs/03_sponge_stress_test.md), [`dabrowski/docs/03_sponge_stress_test.md`](../dabrowski/docs/03_sponge_stress_test.md).
