import CoppolaHS.PadicExclusionENR
import CoppolaHS.ChallengeENR

/-!
# Solution wrapper for the ENR challenge

Does not claim a complete geometric proof.  Records that the archive arithmetic
shells (`no_faithful_padic_of_dabrowski_tower`, `no_faithful_padic_of_openai_enr_at`)
discharge the conclusion once OpenAI / Dabrowski geometric inputs are supplied.
-/

namespace CoppolaHS

/-- Relative solution note: Dabrowski tower input implies exclusion. -/
theorem solution_via_dabrowski_tower
    (X : ENRHomologyManifold) (hI : X.I.val ≠ 0)
    (inp : DabrowskiTowerInput X) : False :=
  no_faithful_padic_of_dabrowski_tower X hI inp

/-- Relative solution note: OpenAI equal-parts at a large `k` implies exclusion. -/
theorem solution_via_openai_enr
    (X : ENRHomologyManifold) (hI : X.I.val ≠ 0)
    (inp : OpenAIENRInput X) (p k : ℕ) (hp : p.Prime)
    (hlt : |4 * inp.c_X * (inp.L_d : ℤ)| < (p : ℤ) ^ k) : False :=
  no_faithful_padic_of_openai_enr_at X hI inp p k hp hlt

end CoppolaHS
