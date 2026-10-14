# Cohort identity notes, 2026-10-14

Working notes reconciling the `prism_exports_2026-10-14/` raw files against the user's own recollection. Not yet folded into the main plan or a Table S1 draft — several items below are still open.

## Confirmed

- **V23:** GD-CBD 3 & 10 mg/kg, n=3, females. File: `GD-CBD (3 & 10 mg:kg) (n=3) V23 April 2026 - Med + Lat AVERAGE.txt`. User recalls March 2026; file says April 2026 — unreconciled, low priority.
- **V24 (real):** GD-CP 55,940 pilot (0.3 mg/kg) + GD-CBD 40 mg/kg, June 2026. File: `GD-CBD (40 mg:kg) GD-CP 55,940 (0 3 mg:kg) (n=3) V24 June 2026 - Med + Lat AVERAGE.txt`.
- **"V24 April 2026" file is a misnamed duplicate of V23**, confirmed by the user and by a byte-level diff (identical values, only the asterisk/selection flags differ). File: `GD-CBD (40 mg:kg) (n=3) V24 April 2026 - Med + Lat AVERAGE.txt`. Treat as non-data — adds nothing beyond V23.
- **V16:** free CBD 10 & 30 mg/kg, micelle formulation, Mar 2025, n=3 per dose. Matches its own file's header (`CBD 10 & 30 mg:kg (n=3) V16 (micelle formulation) Mar 2025.txt`) and the user's confirmation.

## Open — unresolved conflict

- **V18's labeled content doesn't match the user's recollection.** User states V18 tested **GD-CBD 1 & 3 mg/kg**. The file `CBD 10 & 30 mg:kg (n=2) V18 (ACN; strange animals) May 2025.txt` has header columns "CBD 30 mg/kg" / "CBD 10 mg/kg" — free CBD, not GD-CBD; 10/30 mg/kg, not 1/3 mg/kg.
  - Leading hypothesis: the file is mislabeled at export — wrong Prism table saved under the V18 filename.
  - This file's numbers are also what the three COMBINED master files use under a "V16" label (confirmed by exact value match against the real V16 file) — so whatever this file actually is, it has now been mislabeled twice (once as "V18," once folded into COMBINED as "V16").
  - Needs: either the real V18 (GD-CBD 1 & 3 mg/kg) file if it exists separately, or confirmation that the file on hand is misattributed free-CBD data that should carry neither the V16 nor V18 label.
  - The "(ACN; strange animals)" note in the filename is the researcher's own flag and should be preserved regardless of which cohort ID this data turns out to belong to.

## Not yet addressed

- V22's two files (Cremophor CBD 3/15 mg/kg + GD-CBD 15 mg/kg vs. GD-CBD 3 mg/kg + CBD 3 mg/kg, 72h-only) appear to share identical baseline values across different arm groupings — need to confirm whether this is one cohort's shared baseline pool split into two dosing views, or something else.
- Von Frey ceiling/cutoff constant differs by era (447 in 2024-2025 cohorts, 282 in 2026 cohorts) — needs a cohort-specific value for any censoring-sensitivity analysis, not one global constant.
- V24's mid-study "new drug" redose at 168.5h — not a clean single-dose design; affects how any 40 mg/kg "partial positive" claim should be worded (pre- vs. post-redose).
