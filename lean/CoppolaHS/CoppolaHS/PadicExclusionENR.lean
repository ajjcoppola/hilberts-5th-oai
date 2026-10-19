import CoppolaHS.CyclotomicTower
import CoppolaHS.QuinnIndex
import Mathlib.Data.Nat.Prime.Basic

/-!
# Conditional p-adic exclusion on ENR ℤ-homology manifolds

Statement packaging of archive Theorems E–F.  Geometric inputs from
OpenAI / Dabrowski / BFMW are named hypotheses, not constructed here.
-/

namespace CoppolaHS

structure ENRHomologyManifold where
  n : ℕ
  I : QuinnIndex
  hn : 6 ≤ n ∨ I.isResolvable

/-- OpenAI-style equal-parts lattice obstruction (Theorem E). -/
structure OpenAIENRInput (X : ENRHomologyManifold) where
  d : ℕ
  hd_odd : Odd d
  hd_gt : X.n < d
  L_d : ℕ
  hL : 0 < L_d
  c_X : ℤ
  hc : c_X = X.I.val
  /-- Integrality of equal parts for every prime power. -/
  equal_parts_integrality :
    ∀ (p k : ℕ), p.Prime → ((p : ℤ) ^ k) ∣ (4 * c_X * L_d)

/-- Dabrowski-style k-tower obstruction (Theorem F). -/
structure DabrowskiTowerInput (X : ENRHomologyManifold) where
  p : ℕ
  hp : p.Prime
  k : ℕ
  hk : 0 < k
  hk_bound : |X.I.val| < (p : ℤ) ^ k
  signature_divisible : ((p : ℤ) ^ k) ∣ X.I.val

/-- Theorem F shell: Dabrowski k-tower + nonzero Quinn index ⇒ contradiction. -/
theorem no_faithful_padic_of_dabrowski_tower
    (X : ENRHomologyManifold) (hI : X.I.val ≠ 0)
    (inp : DabrowskiTowerInput X) : False :=
  quinn_index_killed_by_tower inp.p inp.k X.I.val hI
    inp.signature_divisible inp.hk_bound

/-- Theorem E shell: if equal-parts integrality holds for a `k` with
`p^k > |4 c_X L_d|`, then a nonzero Quinn index is impossible. -/
theorem no_faithful_padic_of_openai_enr_at
    (X : ENRHomologyManifold) (hI : X.I.val ≠ 0)
    (inp : OpenAIENRInput X) (p k : ℕ) (hp : p.Prime)
    (hlt : |4 * inp.c_X * (inp.L_d : ℤ)| < (p : ℤ) ^ k) : False := by
  have hc0 : inp.c_X ≠ 0 := by simpa [inp.hc] using hI
  have hdvd := inp.equal_parts_integrality p k hp
  have hT0 : (4 * inp.c_X * (inp.L_d : ℤ)) = 0 :=
    abs_lt_pow_of_dvd_eq_zero p k _ hdvd hlt
  have h4 : (4 : ℤ) ≠ 0 := by norm_num
  have hL : (inp.L_d : ℤ) ≠ 0 := by exact_mod_cast (ne_of_gt inp.hL)
  have : inp.c_X = 0 := by
    have h1 := mul_eq_zero.mp hT0
    cases h1 with
    | inl h4c =>
      have h2 := mul_eq_zero.mp h4c
      exact h2.resolve_left h4
    | inr hL0 => exact (hL hL0).elim
  exact hc0 this

end CoppolaHS
