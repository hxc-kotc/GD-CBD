# Collaborator epilepsy figures (source for Figure 3)

Source: `CRS2025SpeakerSlides_CBD_data_2026-07-02.pptx`, uploaded by the user 2026-10-15. Speaker slides from a CRS 2025 presentation, pilocarpine/mecp2 model (KO/Het), 7/2/25 draft — the collaborator's own words: "not fully updated, more data to come later, but these are the key figures."

- `epilepsy_slide3_seizure_duration.png` — full composite image from slide 3, extracted from the pptx at original resolution (10017x4267, converted from the embedded TIFF). 3 panels: % total duration seizing, % duration generalized seizures, % duration generalized seizures over time.
- `epilepsy_slide4_survival_severity.png` — full composite image from slide 4 (12534x4167, converted from the embedded TIFF with alpha composited onto white — the source TIFF was RGBA). 4 panels: % survival at 48h, Kaplan-Meier survival curve, % duration of seizure stages (stacked), % duration stage 6.
- `s3_panel*.png`, `s4_panel*.png` — the above two images cropped into their 7 individual panels (whitespace-gap detection, not hand-eyeballed boundaries). These are what `figures/mockups/build_fig3_real.py` assembles into `fig3_box_layout.png` (Figure 3, panels a-g).

Colors in all of these are the collaborator's own scheme (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD) — not our house palette, since these are the collaborator's real plots, not generated here.

**This is a draft panel set, not final.** The collaborator said more data is coming. Treat n's and exact panel composition as provisional until they send an update.
