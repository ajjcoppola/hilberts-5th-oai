# HM-6 Symbolic /loop Log

- Timestamp (UTC): `2026-10-18T23:09:20.439745+00:00`
- Architecture: `E_{i+1} = (E_i Δ_q EW_d(E_i, Z, n)) ×_{C_{p^{i+1}}} S^{2m_{i+1}-1}`
- Overall: **PASS**

## Iterations

### iter1-baseline — [PASS] (n=5, p=3, stages=4)

- [PASS] `G1`: Classical Williams Part II blocks all i≠0 mod p under n-skeleton retraction; EW (n+2)-cells bypass for every i.
- [PASS] `G2`: dim_Z lim ≤ 5 (high degrees killed); dims [10, 12, 14, 16] grow.
- [PASS] `G3`: Local H^k ≅ δ_{k,5} Z preserved; orbit dim_Z = n+2 with R_p(1) tower.
- [PASS] `G4`: Polynomial criterion holds at each stage; cup-length forces dim U = ∞ on every neighborhood while dim_Z U = n.
- [PASS] `BJ`: F ×_{C_p} S^{2m-1} is (2m-2)-connected ≥ (n+1) at every stage (free-sphere Borel join; Smith χ=0).

### iter2-borel-join — [PASS] (n=7, p=5, stages=3)

- [PASS] `G1`: Classical Williams Part II blocks all i≠0 mod p under n-skeleton retraction; EW (n+2)-cells bypass for every i.
- [PASS] `G2`: dim_Z lim ≤ 7 (high degrees killed); dims [12, 14, 16] grow.
- [PASS] `G3`: Local H^k ≅ δ_{k,7} Z preserved; orbit dim_Z = n+2 with R_p(1) tower.
- [PASS] `G4`: Polynomial criterion holds at each stage; cup-length forces dim U = ∞ on every neighborhood while dim_Z U = n.
- [PASS] `BJ`: F ×_{C_p} S^{2m-1} is (2m-2)-connected ≥ (n+1) at every stage (free-sphere Borel join; Smith χ=0).

### iter3-cup-growth — [PASS] (n=6, p=3, stages=5)

- [PASS] `G1`: Classical Williams Part II blocks all i≠0 mod p under n-skeleton retraction; EW (n+2)-cells bypass for every i.
- [PASS] `G2`: dim_Z lim ≤ 6 (high degrees killed); dims [10, 12, 14, 16, 18] grow.
- [PASS] `G3`: Local H^k ≅ δ_{k,6} Z preserved; orbit dim_Z = n+2 with R_p(1) tower.
- [PASS] `G4`: Polynomial criterion holds at each stage; cup-length forces dim U = ∞ on every neighborhood while dim_Z U = n.
- [PASS] `BJ`: F ×_{C_p} S^{2m-1} is (2m-2)-connected ≥ (n+1) at every stage (free-sphere Borel join; Smith χ=0).

### iter4-large-prime — [PASS] (n=9, p=7, stages=4)

- [PASS] `G1`: Classical Williams Part II blocks all i≠0 mod p under n-skeleton retraction; EW (n+2)-cells bypass for every i.
- [PASS] `G2`: dim_Z lim ≤ 9 (high degrees killed); dims [14, 16, 18, 20] grow.
- [PASS] `G3`: Local H^k ≅ δ_{k,9} Z preserved; orbit dim_Z = n+2 with R_p(1) tower.
- [PASS] `G4`: Polynomial criterion holds at each stage; cup-length forces dim U = ∞ on every neighborhood while dim_Z U = n.
- [PASS] `BJ`: F ×_{C_p} S^{2m-1} is (2m-2)-connected ≥ (n+1) at every stage (free-sphere Borel join; Smith χ=0).

## Refinement notes (plan Phase 2)

1. **Iteration 1:** Williams $K\Delta_q X$ + EW Postnikov cells — G1–G3 pass; classical torus obstruction bypassed.
2. **Iteration 2:** Borel-join connectivity uses free-sphere $(2m-2)$-connectivity (not limited by `conn(F)` of the EW skeleton).
3. **Iteration 3:** Dranishnikov Prop. 3.3 schedule with $k=m+1$, $k-l=1$ so $v_p(\mathrm{coeff}_m)=m<k$; cup-length grows.
4. **Iteration 4:** Large-prime sanity check ($p=7$, $n=9$).

## Lean formalization

See `lean/CoppolaHS/CoppolaHS/DranishnikovHM6.lean` (Borel-join connectivity, K-theory cup-length criterion, HM-6 escape from `OpenAIENRInput` / `DabrowskiTowerInput`).

