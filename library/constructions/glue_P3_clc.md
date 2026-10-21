# Shared finish P3 — $clc_{\mathbb{Z}}$ Poincaré glue

**AI disclaimer:** These construction notes are AI-assisted and AI-generated using Cursor, with Grok, Anthropic, and OpenAI models, under the direction of Alan J. Coppola.

**Plan:** [`../../plans/HM6_FINISH_LINE.md`](../../plans/HM6_FINISH_LINE.md)  
**Paper:** Rem. `hm6-remaining` in `papers/padic-homology-manifolds/main.tex`

This is the **only open geometric gate** shared by Trunks A and B.

## Checklist (limit $X=\varprojlim E_i$)

- [ ] Fibers of $\pi_{i+1}$ are pro-acyclic / UV$^{n-1}$ (or Vietoris–Begle) through degree $n$ over $\mathbb{Z}$.  
- [ ] No new local homology in degrees $\le n-1$ along splicing loci.  
- [ ] Local orientation class in degree $n$ survives and glues across $\partial\sigma$.  
- [ ] Orbit side realizes BRW: $\dim_{\mathbb{Z}}(X/A_p)=n+2$ with $R_p(1)$ injection (constraint).  
- [ ] $X$ connected, locally connected, compact metrizable.  
- [ ] $A_p$ action jointly continuous and effective ($\bigcap_i\ker(A_p\to C_{p^i})=\{0\}$).  
- [ ] Every nonempty open $U$: $\dim_{\mathbb{Z}}U=n$ and $\dim U=\infty$ (cup-length / G4).

## What is *not* required for an HM-6 example

- Finite covering dimension  
- ENR / ANR structure  
- Empty manifold stratum is automatic if $\dim=\infty$

## Suggested proof pattern

1. Establish finite-stage relative isomorphism  
   $H^k(\pi^{-1}U,\pi^{-1}\partial U;\mathbb{Z})\cong H^k(U,\partial U;\mathbb{Z})$ for $k\le n$.  
2. Pass to inverse limit with Mittag-Leffler / pro-isomorphism control.  
3. Identify Čech local groups with $\mathbb{R}^n$ local groups.  
4. Only then claim “$\mathbb{Z}$-cohomology $n$-manifold.”
