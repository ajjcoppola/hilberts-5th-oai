# Plan: HM-6 finish line — effective $A_p$ on a $\mathbb{Z}$-cohomology manifold

**AI disclaimer:** This plan is AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola. See [`../docs/AI_DISCLAIMER.md`](../docs/AI_DISCLAIMER.md).

**Status:** active  
**Date:** 2026-10-19  
**Checkpoint:** `checkpoint/hm6-2026-10-18` on https://github.com/ajjcoppola/hilberts-5th-oai  
**Sherlock source:** [`docs/SHERLOCK_HM6_FINISH_LINE_2026-10-19.md`](../docs/SHERLOCK_HM6_FINISH_LINE_2026-10-19.md)  
**Literature library:** [`library/README.md`](../library/README.md)

---

## Goal

Construct (stage-by-stage) a compact connected $\mathbb{Z}$-cohomology $n$-manifold $X$ carrying an **effective** continuous action of $A_p=\mathbb{Z}_p$ (or a solenoidal inverse-limit action), with

\[
\dim_{\mathbb{Z}} X = n < \infty, \qquad \dim X = \infty
\]

(class **HM-6**). This escapes OpenAI ENR rephrase, Dabrowski $k$-tower, and bounded-dimension Euler obstruction (Thm G).

**Honesty:** Finite-stage algebraic gates G1–G4 PASS symbolically. Continuous $clc_{\mathbb{Z}}$ Poincaré glue remains open — not a claimed existence theorem until P3 closes.

---

## Current state

| Deliverable | State |
|-------------|--------|
| Relative archive paper | `papers/padic-homology-manifolds/main.pdf` |
| Symbolic harness + loop | G1–G4 + BJ PASS (`scripts/hm6_*`, `HM6_LOOP_LOG.md`) |
| Lean shells | `lean/CoppolaHS` incl. `DranishnikovHM6.lean` builds |
| Finish-line gap | Rem. `hm6-remaining`: $clc_{\mathbb{Z}}$ glue over Yang $(n+2)$ orbit |

---

## Dual construction trunks (run in parallel)

### Trunk A — Solenoid / circle-bundle / lens sequence

One odd sphere / lens stage at a time:

- Free linear $S^1$ on $S^{2m_i-1}$ → lens $L^{2m_i-1}(p^{k_i})$
- Bonding $\times p$ on covers; **grow** $m_i$ (fixed $m$ ⇒ classical solenoid FAIL)
- EW / $K(\mathbb{Z},\cdot)$ kill so $\varinjlim H^{>n}=0$ over $\mathbb{Z}$
- Limit: free $A_p$ on continuum $E$; orbit with unbounded $K$-theory cup-length

**Primary refs:** Dranishnikov [arXiv:1504.07277](../library/pdfs/1504.07277.pdf); constructions note [`library/constructions/trunk_A_lens_solenoid.md`](../library/constructions/trunk_A_lens_solenoid.md)

### Trunk B — Finite recursive cyclic complexes

One finite complex per stage (current harness):

\[
E_{i+1}
=
\bigl(E_i\,\Delta_{q_i}\,EW_{d_i}(E_i,\mathbb{Z},n)\bigr)
\times_{C_{p^{i+1}}}
S^{2m_{i+1}-1}
\]

**Primary refs:** Raymond–Williams, Williams 1967 Part II; Levin [arXiv:1909.12660](../library/pdfs/1909.12660.pdf); note [`library/constructions/trunk_B_cyclic_EW.md`](../library/constructions/trunk_B_cyclic_EW.md)

### Shared finish P3 — $clc_{\mathbb{Z}}$ glue

Pro-cell-like / Vietoris–Begle through degree $n$; glue local $H^n$ across $\partial\sigma$ when blocks sit over $\dim_{\mathbb{Z}}=n+2$ orbit space; BRW $R_p(1)$ constraint.

---

## Next steps (ordered)

| ID | Step | Owner / tool | Done when |
|----|------|--------------|-----------|
| **N1** | Add harness gate `G0-solenoid-tail`: fixed $m$ FAIL, growing+$EW$ PASS | `scripts/hm6_equivariant_ew_harness.py` | New gate in loop log |
| **N2** | Build **one explicit geometric stage** ($n=5$, $p=3$): lens or EW cells with recorded cellular cochain maps | `library/constructions/` + new script | Cohomology matches G2/G3 numerically |
| **N3** | Write Lean statement-layer props for glue hypotheses (no geometry claim) | `DranishnikovHM6.lean` | `lake build` clean |
| **N4** | Attack P3 glue (human CD/EW coauthor + paper §8.5 expansion) | paper + outreach | Either glue theorem or precise obstruction |
| **N5** | If N2+N4 succeed: archive existence theorem + update HM-6 matrix to COUNTEREXAMPLE | paper / catalog E4 | Ledger HIT |

**Do not:** chase free $A_p$ on ENR/HM-5 as the example target.

---

## Acceptance criteria (finish line)

1. Inverse system $\{E_i\}$ (Trunk A or B) with compatible free $C_{p^i}$-actions.  
2. $X=\varprojlim E_i$ is a compact connected $clc_{\mathbb{Z}}$ $n$-manifold.  
3. $A_p=\varprojlim C_{p^i}$ acts jointly continuously and effectively on $X$.  
4. $\dim_{\mathbb{Z}}X=n$ and every nonempty open $U\subset X$ has $\dim U=\infty$ (or documented weaker neighborhood statement).  
5. Harness + at least one geometric stage verified; Lean arithmetic shells remain green.

---

## Related docs

- Sherlock finish-line: [`docs/SHERLOCK_HM6_FINISH_LINE_2026-10-19.md`](../docs/SHERLOCK_HM6_FINISH_LINE_2026-10-19.md)  
- Checkpoint: [`docs/CHECKPOINT_HM6_2026-10-18.md`](../docs/CHECKPOINT_HM6_2026-10-18.md)  
- Outreach: [`docs/OUTREACH_COLLABORATORS.md`](../docs/OUTREACH_COLLABORATORS.md)  
- Library: [`library/README.md`](../library/README.md)
