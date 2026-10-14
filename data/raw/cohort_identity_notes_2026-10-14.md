# Cohort identity notes, 2026-10-14

Working notes reconciling the `prism_exports_2026-10-14/` raw files against the user's own recollection. Not yet folded into the main plan or a Table S1 draft — several items below are still open.

## Confirmed

- **V23:** GD-CBD 3 & 10 mg/kg, n=3, females. File: `GD-CBD (3 & 10 mg:kg) (n=3) V23 April 2026 - Med + Lat AVERAGE.txt`. User recalls March 2026; file says April 2026 — unreconciled, low priority.
- **V24 (real):** GD-CP 55,940 pilot (0.3 mg/kg) + GD-CBD 40 mg/kg, June 2026. File: `GD-CBD (40 mg:kg) GD-CP 55,940 (0 3 mg:kg) (n=3) V24 June 2026 - Med + Lat AVERAGE.txt`.
- **"V24 April 2026" file is a misnamed duplicate of V23**, confirmed by the user and by a byte-level diff (identical values, only the asterisk/selection flags differ). File: `GD-CBD (40 mg:kg) (n=3) V24 April 2026 - Med + Lat AVERAGE.txt`. Treat as non-data — adds nothing beyond V23.
- **V16:** cohort tested CBD 10 & 30 mg/kg (micelle formulation, this file, n=3 per dose) **and** GD-ketorolac 15 mg/kg (separate arm, not uploaded, not needed for this paper). File: `CBD 10 & 30 mg:kg (n=3) V16 (micelle formulation) Mar 2025.txt`.
- **V18:** cohort tested CBD 10 & 30 mg/kg (ACN vehicle, this file, n=2 per dose) **and** GD-CBD 3 mg/kg + GD-ket 10 mg/kg (separate arms, not uploaded, not needed for this paper). File: `CBD 10 & 30 mg:kg (n=2) V18 (ACN; strange animals) May 2025.txt`.
  - Resolved 2026-10-14: the apparent conflict with the user's cohort descriptions was a wrong assumption on my part — these files are each just the free-CBD slice of a larger multi-arm cohort, not the full cohort export. Both files' own CBD-dose data are correctly labeled and reliable.
  - The "(ACN; strange animals)" note in the V18 filename is the researcher's own flag on that cohort and should be preserved in any future write-up regardless.

## Open — confirmed data-quality problem (not resolved by the above)

- **The three COMBINED master files mislabel V18's free-CBD data as "V16."** Now that both V16 and V18's own files are confirmed distinct and correctly labeled (previous section), this is unambiguous: COMBINED.txt / COMBINED +4.txt / COMBINED w: extra control + V24.txt all have a column labeled "CBD (10/30 mg/kg) V16" whose values are byte-identical to V18's file (7.530, 31.390, ... at the early post-surgery timepoints), not to V16's own file (406.440, 30.425, 82.455, ... at the same timepoints — genuinely different numbers, confirmed much higher and more variable). Whoever rebuilds the combined/master sheets for the manuscript needs to pull V16's real data into that column, or relabel it V18. Do not use the COMBINED files' "V16" column for anything until this is fixed at the source.

## Not yet addressed

- V22's two files (Cremophor CBD 3/15 mg/kg + GD-CBD 15 mg/kg vs. GD-CBD 3 mg/kg + CBD 3 mg/kg, 72h-only) appear to share identical baseline values across different arm groupings — need to confirm whether this is one cohort's shared baseline pool split into two dosing views, or something else.
- Von Frey ceiling/cutoff constant differs by era (447 in 2024-2025 cohorts, 282 in 2026 cohorts) — needs a cohort-specific value for any censoring-sensitivity analysis, not one global constant.
- V24's mid-study "new drug" redose at 168.5h — not a clean single-dose design; affects how any 40 mg/kg "partial positive" claim should be worded (pre- vs. post-redose).
