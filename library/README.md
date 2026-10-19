# Literature & construction library (HM-6 / $p$-adic actions)

Supporting the finish-line plan [`plans/HM6_FINISH_LINE.md`](../plans/HM6_FINISH_LINE.md).

| Path | Contents |
|------|----------|
| [`pdfs/`](pdfs/) | Freely downloadable PDFs (mostly arXiv) |
| [`constructions/`](constructions/) | Stage-by-stage construction notes (Trunks A & B) |
| [`BIBLIOGRAPHY.md`](BIBLIOGRAPHY.md) | Full catalog: local PDF / DOI / paywall |

**Policy:** Prefer arXiv / author-hosted PDFs. Classic AMS/Annals items are listed with DOI only (no piracy). Our own draft and the OpenAI/Dabrowski audits live elsewhere in this repo (linked below).

## Quick map: paper → trunk

| Local PDF | Role | Trunk |
|-----------|------|-------|
| [`pdfs/1504.07277.pdf`](pdfs/1504.07277.pdf) | Dranishnikov: essential lens sequence, weak HS reductions | **A** (primary) |
| [`pdfs/1909.12660.pdf`](pdfs/1909.12660.pdf) | Levin: simpler Raymond–Williams inverse-limit example | **B** |
| [`pdfs/math_0212329.pdf`](pdfs/math_0212329.pdf) | Dranishnikov–West: compact group actions raising dim to ∞ | A/B context |
| [`pdfs/1102.2225.pdf`](pdfs/1102.2225.pdf) | Edwards–Walsh resolution without EW CW-complexes | A/B (kill $H^{>n}$) |
| [`pdfs/math_0611004.pdf`](pdfs/math_0611004.pdf) | Dranishnikov–Ferry–Weinberger (flexibility / KO vanishing lineage) | A/B (dim ∞) |
| [`pdfs/1612.09567.pdf`](pdfs/1612.09567.pdf) | Weak HS from Borsuk–Ulam-type conjecture | Context (orbit method) |

## In-repo (not duplicated here)

| Artifact | Path |
|----------|------|
| Archive paper (relative + HM-6) | [`../papers/padic-homology-manifolds/`](../papers/padic-homology-manifolds/) |
| OpenAI audit | [`../docs/Hilbert_Smith_Audit.pdf`](../docs/Hilbert_Smith_Audit.pdf) |
| Dabrowski audit | [`../dabrowski/docs/Dabrowski_HS_Audit.pdf`](../dabrowski/docs/Dabrowski_HS_Audit.pdf) |
| HM-6 harness | [`../scripts/hm6_equivariant_ew_harness.py`](../scripts/hm6_equivariant_ew_harness.py) |

## Construction notes

- [`constructions/trunk_A_lens_solenoid.md`](constructions/trunk_A_lens_solenoid.md) — circle / lens / growing solenoid  
- [`constructions/trunk_B_cyclic_EW.md`](constructions/trunk_B_cyclic_EW.md) — finite recursive $C_{p^i}$ + EW Borel-join  
- [`constructions/glue_P3_clc.md`](constructions/glue_P3_clc.md) — shared finish-line glue checklist  

## Refresh PDFs

```bash
cd library/pdfs
# example
curl -fsSL -o 1504.07277.pdf https://arxiv.org/pdf/1504.07277.pdf
```
