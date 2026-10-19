import Mathlib.Data.Int.ModEq

/-!
# Abstract Quinn resolution index (statement layer)
-/

namespace CoppolaHS

structure QuinnIndex where
  val : ℤ
  mod8 : val ≡ 1 [ZMOD 8]

namespace QuinnIndex

def isResolvable (I : QuinnIndex) : Prop := I.val = 1

def isNonResolvable (I : QuinnIndex) : Prop := I.val ≠ 1

def productFormula (IX IY IXY : QuinnIndex) : Prop :=
  IXY.val = IX.val * IY.val

theorem ne_neg_one (I : QuinnIndex) : I.val ≠ -1 := by
  intro h
  have hm : (-1 : ℤ) ≡ 1 [ZMOD 8] := by simpa [h] using I.mod8
  have heq : (-1 : ℤ) % 8 = 1 % 8 := Int.ModEq.eq hm
  have hne : (-1 : ℤ) % 8 ≠ 1 % 8 := by decide
  exact hne heq

theorem product_preserves_nonresolvable
    (IX IY IXY : QuinnIndex)
    (hprod : productFormula IX IY IXY)
    (hx : IX.isNonResolvable)
    (hy : IY.val = 1) :
    IXY.isNonResolvable := by
  intro hxy
  have : IX.val = 1 := by
    have hmul : IX.val * IY.val = 1 := by
      simpa [productFormula, hxy] using hprod.symm
    simpa [hy] using hmul
  exact hx this

end QuinnIndex

def quinnIndexOf (n : ℤ) (h : n ≡ 1 [ZMOD 8]) : QuinnIndex :=
  ⟨n, h⟩

end CoppolaHS
