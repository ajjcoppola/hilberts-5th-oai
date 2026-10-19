import Mathlib.RingTheory.Polynomial.Cyclotomic.Roots
import Mathlib.RingTheory.Polynomial.Cyclotomic.Eval
import Mathlib.Data.Nat.Prime.Basic

/-!
# Cyclotomic k-tower arithmetic (Theorem F upgrade)
-/

noncomputable section

namespace CoppolaHS

open Polynomial

/-- Single-step Dabrowski arithmetic (same shape as `HSFormal.AlgebraicReduction`). -/
theorem prime_dvd_eval_one_of_primitive_root
    (p k : ℕ) (hp : p.Prime) (ζ : ℂ)
    (hζ : IsPrimitiveRoot ζ (p ^ (k + 1))) (F : ℤ[X])
    (hzero : aeval ζ F = 0) : (p : ℤ) ∣ F.eval 1 := by
  let : Fact p.Prime := ⟨hp⟩
  have hpos : 0 < p ^ (k + 1) := pow_pos hp.pos _
  have hdiv : cyclotomic (p ^ (k + 1)) ℤ ∣ F := by
    rw [cyclotomic_eq_minpoly hζ hpos]
    exact minpoly.isIntegrallyClosed_dvd (hζ.isIntegral hpos) hzero
  obtain ⟨Q, hQ⟩ := hdiv
  rw [hQ, eval_mul, eval_one_cyclotomic_prime_pow k]
  exact dvd_mul_right _ _

/-- Each factor in the tower evaluates to `p` at 1. -/
theorem eval_one_cyclotomic_tower_factor
    (p a i : ℕ) (hp : p.Prime) (hi : i ≤ a) :
    (cyclotomic (p ^ (a + 1 - i)) ℤ).eval 1 = (p : ℤ) := by
  let : Fact p.Prime := ⟨hp⟩
  have heq : a + 1 - i = (a - i) + 1 := by
    rw [Nat.add_comm a 1, Nat.add_sub_assoc hi, Nat.add_comm]
  rw [heq]
  exact eval_one_cyclotomic_prime_pow (a - i)

/-- Product of `k` prime-power cyclotomics evaluates to `p^k` at 1. -/
theorem eval_one_cyclotomic_prime_pow_tower
    (p a k : ℕ) (hp : p.Prime) (hak : k ≤ a + 1) :
    (∏ i ∈ Finset.range k, cyclotomic (p ^ (a + 1 - i)) ℤ).eval 1 = (p : ℤ) ^ k := by
  let : Fact p.Prime := ⟨hp⟩
  rw [eval_prod]
  have hconst : ∀ i ∈ Finset.range k,
      (cyclotomic (p ^ (a + 1 - i)) ℤ).eval 1 = (p : ℤ) := by
    intro i hi
    have hi' : i < k := Finset.mem_range.mp hi
    have hi_le_a : i ≤ a := Nat.lt_succ_iff.mp (lt_of_lt_of_le hi' hak)
    exact eval_one_cyclotomic_tower_factor p a i hp hi_le_a
  convert Finset.prod_const (s := Finset.range k) (b := (p : ℤ)) using 1
  · exact Finset.prod_congr rfl hconst
  · simp [Finset.card_range]

/-- If that product divides `F`, then `p^k` divides `F(1)`. -/
theorem pow_prime_dvd_eval_one_of_cyclotomic_tower
    (p a k : ℕ) (hp : p.Prime) (hak : k ≤ a + 1)
    (F : ℤ[X])
    (hprod : (∏ i ∈ Finset.range k, cyclotomic (p ^ (a + 1 - i)) ℤ) ∣ F) :
    ((p : ℤ) ^ k) ∣ F.eval 1 := by
  obtain ⟨Q, hQ⟩ := hprod
  rw [hQ, eval_mul, eval_one_cyclotomic_prime_pow_tower p a k hp hak]
  exact dvd_mul_right _ _

/-- If `p^k` divides `σ` and `|σ| < p^k` then `σ = 0`. -/
theorem abs_lt_pow_of_dvd_eq_zero
    (p k : ℕ) (σ : ℤ)
    (hdvd : ((p : ℤ) ^ k) ∣ σ) (hlt : |σ| < (p : ℤ) ^ k) : σ = 0 := by
  obtain ⟨m, hm⟩ := hdvd
  subst hm
  by_cases hm0 : m = 0
  · simp [hm0]
  · have hp0 : 0 ≤ (p : ℤ) := Nat.cast_nonneg _
    have hle : (p : ℤ) ^ k ≤ |(p : ℤ) ^ k * m| := by
      rw [abs_mul, abs_pow, abs_of_nonneg hp0]
      exact le_mul_of_one_le_right (pow_nonneg hp0 _) (Int.one_le_abs hm0)
    exact (not_le_of_gt hlt hle).elim

/-- Theorem F arithmetic shell. -/
theorem quinn_index_killed_by_tower
    (p k : ℕ) (I : ℤ) (hI : I ≠ 0)
    (hdvd : ((p : ℤ) ^ k) ∣ I) (hlt : |I| < (p : ℤ) ^ k) : False :=
  hI (abs_lt_pow_of_dvd_eq_zero p k I hdvd hlt)

end CoppolaHS
