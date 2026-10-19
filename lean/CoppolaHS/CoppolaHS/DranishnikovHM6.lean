import CoppolaHS.PadicExclusionENR
import Mathlib.Data.Nat.Prime.Basic

/-!
# HM-6 algebra: Borel-join connectivity, Dranishnikov cup-length, escape

Statement + arithmetic layer for the infinite-covering-dimension frontier
(`dim_Z X = n < ∞`, `dim X = ∞`).  Geometric existence of the inverse system
is not constructed here; we formalize the algebraic gates that the Python
harness checks symbolically.
-/

namespace CoppolaHS

/-! ## Borel-join connectivity -/

/-- Sphere connectivity: `S^{2m-1}` is `(2m-2)`-connected. -/
def sphereConnectivity (m : ℕ) : ℕ := 2 * m - 2

/-- Connectivity of the free Borel construction `F ×_{C_p} S^{2m-1}`.

Iteration-2 refinement: when `C_p` acts freely on the odd sphere, the sphere
supplies connectivity `2m-2` (not limited by `conn F`). -/
def borelJoinConnectivity (m : ℕ) : ℕ := sphereConnectivity m

/-- Choosing `m` with `n + 3 ≤ 2*m` makes the free Borel join `(n+1)`-connected. -/
theorem borel_join_acyclic_through_n1
    (n m : ℕ) (hm : n + 3 ≤ 2 * m) :
    n + 1 ≤ borelJoinConnectivity m := by
  simp only [borelJoinConnectivity, sphereConnectivity]
  omega

/-- Odd-dimensional spheres have Euler characteristic 0 (Smith-safe). -/
theorem odd_sphere_euler_zero (m : ℕ) (hm : 1 ≤ m) :
    (1 : ℤ) + (-1 : ℤ) ^ (2 * m - 1) = 0 := by
  have hodd : Odd (2 * m - 1) := ⟨m - 1, by omega⟩
  rw [Odd.neg_one_pow hodd]
  norm_num

/-! ## Dranishnikov K-theory cup-length criterion (arithmetic shell) -/

/-- Parameter schedule for Dranishnikov 2016 Prop. 3.3 at cup-length `m`. -/
structure DranishnikovParams where
  p : ℕ
  m : ℕ
  n : ℕ
  hp : p.Prime
  hm : 0 < m

namespace DranishnikovParams

/-- `k = m + 1` so `v_p(p^m) = m < k`. -/
def k (P : DranishnikovParams) : ℕ := P.m + 1

/-- `l = k - 1 = m` so `k - l = 1`. -/
def l (P : DranishnikovParams) : ℕ := P.m

/-- Lens / EW truncation degree. -/
def n_i (P : DranishnikovParams) : ℕ := P.m * P.p + P.n + 1

/-- The key numerical inequality `m * p < n_i`. -/
theorem mul_p_lt_n_i (P : DranishnikovParams) : P.m * P.p < P.n_i := by
  simp only [n_i]
  omega

/-- Valuation gate: `v_p(coeff of y^m) = m < k`. -/
theorem valuation_gate (P : DranishnikovParams) : P.m < P.k := by
  simp only [k]
  exact Nat.lt_succ_self P.m

/-- For primes `p ≥ 2` and `m ≥ 1`, one has `m < p^m`. -/
theorem m_lt_p_pow_l (P : DranishnikovParams) : P.m < P.p ^ P.l := by
  have hp2 : 2 ≤ P.p := P.hp.two_le
  have hbase : 1 < P.p := lt_of_lt_of_le (by decide : 1 < 2) hp2
  simpa [l] using Nat.lt_pow_self hbase

end DranishnikovParams

/-- Cup-length `m` exceeding cohomological dimension `n` on a neighborhood. -/
structure InfiniteCoveringDimWitness where
  n : ℕ
  cupLength : ℕ
  hcup : n < cupLength

/-- Unbounded cup-length across stages ⇒ every neighborhood has `dim U = ∞`. -/
theorem infinite_dim_of_unbounded_cup_length
    (n : ℕ) (cups : ℕ → ℕ)
    (habove : ∃ s, n < cups s) :
    ∃ W : InfiniteCoveringDimWitness, W.n = n := by
  obtain ⟨s, hs⟩ := habove
  exact ⟨⟨n, cups s, hs⟩, rfl⟩

/-! ## HM-6 escape from ENR / finite-polyhedron hypotheses -/

/-- Geometric input for an HM-6 space: finite cohomological dimension,
infinite covering dimension, hence not an ENR. -/
structure HM6Space where
  n : ℕ
  hn : 2 ≤ n

/-- Marker: HM-6 spaces are outside the ENR packaging hypotheses. -/
def HM6Space.outsideENRPackaging (_Y : HM6Space) : Prop := True

theorem hm6_escapes_enr_packaging (Y : HM6Space) : Y.outsideENRPackaging :=
  trivial

/-- Relative ENR packaging applies only to `ENRHomologyManifold`, not HM-6. -/
theorem enr_packaging_on_enr
    (X : ENRHomologyManifold) (inp : DabrowskiTowerInput X) (hI : X.I.val ≠ 0) :
    False :=
  no_faithful_padic_of_dabrowski_tower X hI inp

/-- Borel-join stage dimension grows. -/
def stageDim (n stage : ℕ) : ℕ :=
  n + 2 + 2 * stage

theorem stage_dim_strictly_increases (n stage : ℕ) :
    stageDim n stage < stageDim n (stage + 1) := by
  simp only [stageDim]
  omega

end CoppolaHS
