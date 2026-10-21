# Trunk B — Finite recursive cyclic + Edwards–Walsh Borel-join

**AI disclaimer:** These construction notes are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola.

**Plan:** [`../../plans/HM6_FINISH_LINE.md`](../../plans/HM6_FINISH_LINE.md)  
**Primary PDFs:** [`../pdfs/1909.12660.pdf`](../pdfs/1909.12660.pdf) (Levin/RW), [`../pdfs/1102.2225.pdf`](../pdfs/1102.2225.pdf) (EW)  
**Harness:** [`../../scripts/hm6_equivariant_ew_harness.py`](../../scripts/hm6_equivariant_ew_harness.py)

## Idea

Proceed **one finite simplicial complex** $E_i$ at a time with compatible free $C_{p^i}$-actions. Grow topological dimension; kill $H^{>n}$ by Edwards–Walsh; keep free action via Borel join with an odd sphere.

## Stage recipe

\[
E_{i+1}
=
\bigl(E_i\,\Delta_{q_i}\,EW_{d_i}(E_i,\mathbb{Z},n)\bigr)
\times_{C_{p^{i+1}}}
S^{2m_{i+1}-1},\qquad
d_{i+1}>d_i,\quad 2m_{i+1}-1>n+1.
\]

1. Start from $E_0$ an $n$-sphere or polyhedral $n$-cm.  
2. Williams splice $\Delta_q$ optional on simplex stars (building blocks).  
3. Attach EW / Postnikov cells killing $H^{q}$ for $q>n$.  
4. Borel-join free $S^{2m-1}$ ⇒ $(2m-2)$-connected free $C_{p^{i+1}}$-space (Smith $\chi=0$).  
5. Bonding $\pi_{i+1}$ equivariant for $C_{p^{i+1}}\twoheadrightarrow C_{p^i}$.  
6. $X=\varprojlim E_i$, $A_p=\varprojlim C_{p^i}$.

## FAIL modes

| Mistake | Symptom |
|---------|---------|
| Force bonding into $n$-skeleton | Williams 1967 Part II torus (G1 without EW) |
| Bounded $\dim E_i$ + free $C_p$ on $\mathbb{Q}$-acyclic fibers | Euler $\chi\equiv 0\pmod p$ vs $\chi=1$ (Thm G Case 2) |
| Skip EW kill of integral tops | Solenoid / high $\dim_{\mathbb{Z}}$ |

## Status

Symbolic gates G1–G4 + BJ **PASS**. Geometric cell-by-cell stage still **TODO** (plan N2).
