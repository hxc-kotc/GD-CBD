---
title: "GD-CBD figure plan"
subtitle: "Prepared 2026-10-14, revised to match the main plan's figure list. Status markers: Have / Partial / Box (placeholder)."
---

Each figure cites the comparator paper (`literature/comparator_papers/`) its layout is modeled on. Built for Friday: show what's buildable now, leave literal boxes for the rest.

**Each numbered figure is one composite, multi-panel page** — this is consistent across all four comparator papers (e.g. Porterfield Fig. 4 has 8 panels on one page, Sharma 2024 Fig. 11 has 7), not a separate image per chart. Mockups in `figures/mockups/` follow this: `fig4_composite.png` is the actual Figure 4 mockup (all panels a-g on one page); `fig4b/c/d_*.png` are the same content at larger size, kept as source material, not a substitute for the composite.

**Updated 2026-11-03** after the 2026-11-02 PI working session (`literature/lab_meetings/2026-11-02_PI_meeting/`, `INTEGRATION_PLAN_2026-11-02.md`). Figure count is now **five**: chemistry, in vitro, epilepsy, pain efficacy, biodistribution. The former Figure 5 (cytokines across indications) is cut — no counterpart in what was actually discussed. Figure 6 (biodistribution) is no longer conditional on a new Cy5-GD-CBD dosing study; it's built around existing GD-Cy5 material, settled at the meeting. A new cross-model CB<sub>2</sub>-overexpression panel row exists (`fig_cb2_throughline.png`) with no figure number assigned yet — see its own section below. Figure numbering itself (collapsing the gap left by the Figure 5 cut, and where the CB<sub>2</sub> content lands) is a pending renumbering pass, deliberately not done in the same pass as these cuts (per the integration plan's own recommendation).

**If the pain cohort doesn't replicate and the paper falls back to epilepsy-led or pain-only** (per the main plan's strategy table), this figure list forks: epilepsy-led drops Figure 4; pain-only drops Figure 3. (The old fork language about "the pain/epilepsy half of Figure 5" no longer applies — Figure 5 is cut.)

# Figure 1 — Chemistry and characterization of GD-CBD

Modeled on: Porterfield & Sharma 2023 Fig. 1 + Scheme 1 (structure + physicochemical table); Sharma 2024 Figs. 1–3, 10a-b (synthesis scheme, stacked NMR, HPLC purity).

| Panel | Content | Status |
|:---|:---|:---|
| 1a | Synthesis scheme: CBD + azido-PEG4-COOH → bifunctional PEG linker-CBD; GD2 (OH96) + propargyl bromide → GD2-acetylene; CuAAC click → GD-CBD. **Real scheme from the chemist** (user-supplied image, 2026-10-15), cropped from their own 3-panel figure — not a mockup | **Have** |
| 1b | Physicochemical table (size, zeta, loading %, purity, MW) — Porterfield Fig. 1b format. **Mock values calibrated to Sharma 2024's GD2-VPA** (same GD platform, same CuAAC click linker as GD-CBD): 4.4 nm, near-neutral zeta, 6 wt% loading, 99% purity — not arbitrary placeholders | **Box** — Batch 4 identity due ~Oct 23 |
| 1c | Release profile — **template: Sharma 2024 Fig. 10c**, two curves (lysosomal/esterase pH 5.5 vs. plasma PBS pH 7.4) over ~170h, inset zoom on early timepoints. **Mock curve shaped to that paper's own GD2-VPA numbers**: ~80% release by day 7 at pH 5.5, <6% by day 7 (minimal to 48h) at pH 7.4 — same linker chemistry, not a generic sigmoid | **Box** |
| 1d | Representative NMR/HPLC/MALDI spectra — **template: Sharma 2024 Fig. 10a-b**, stacked traces (free CBD, intermediate, final conjugate), new peak confirming conjugation called out by arrow; single HPLC chromatograph with purity % annotated | **Box** |

**Panel 1e (hemocompatibility/CARPA) cut 2026-11-03.** Never discussed at the 2026-11-02 PI session; this repo's own anticipatory addition, and it sat oddly next to a paper that session settled firmly against making any safety claims for. Cut on explicit confirmation, not inference.

# Figure 2 — In vitro activity

No direct lab precedent for this exact panel type (none of the four comparator papers run a cytokine panel). Visual convention: Porterfield Fig. 6d (bar graph with individual points, asterisk significance).

**Scope change pending, not yet executed.** The 2026-11-02 PI session confirmed several things about this figure that aren't reflected in the panel table below yet: **microglia, not macrophages** (confirmed, matches the direction already here); the binding discussion has moved entirely to **CB<sub>2</sub>** (not CB<sub>1</sub>/CB<sub>2</sub>), with more concentration points being added and a real number in hand — **GD-CBD ~6-fold more potent than free CBD on a drug basis**, THC as a nanomolar positive control; and **CB<sub>2</sub> overexpression after LPS/glutamate must be shown before the efficacy readout** for the panel to make narrative sense ("otherwise it won't make sense"). HU-331 was not mentioned at the meeting at all. None of this has been rebuilt yet — restructuring Figure 2 is item C12 in `INTEGRATION_PLAN_2026-11-02.md`, still awaiting a go-ahead.

| Panel | Content | Status |
|:---|:---|:---|
| 2a | TNF-α/cytokine panel: GD-CBD vs free CBD vs GD alone vs original batch, viability overlay. **Direction grounded in published free-CBD/LPS-macrophage data**; GD-CBD's greater mock potency reflects the activated-macrophage preferential dendrimer uptake mechanism reported in Gusdon 2022, not an arbitrary assumption | **Partial** — some prior TNF-α data exists per batch notes; new-batch panel due ~Oct 23 |
| 2b | CB<sub>1</sub>/CB<sub>2</sub> binding or functional assay. **Free-CBD mock EC<sub>50</sub> (0.3 µM) set within the published CB<sub>2</sub> potency range for CBD** (~0.3-4 µM across assays). **Superseded by real data**: a real CB<sub>2</sub> binding curve now exists (~6-fold potency improvement, drug basis, THC positive control) — this panel should be rebuilt around that number, not left as a mock EC<sub>50</sub>, once confirmed | **Box** — rebuild pending |
| 2c | HU-331 stability-indicating chromatogram (likely supplement) | **Box** — not mentioned at the 2026-11-02 session; may not belong in the main figure |

# Figure 3 — Epilepsy

Supplied by the collaborator (CRS 2025 speaker slides, 7/2/25 draft), pilocarpine/mecp2 model. Eight panels, a–h, cropped from three of the collaborator's own slide images (one schematic, two composite data images) and relettered to match this figure set's convention. Colors are the collaborator's own (red=Pilo/Sal, green=Pilo/CBD, blue=Pilo/GD-CBD), not redrawn in house palette. The collaborator says more data is still coming — this is a draft panel set, not the final n or final figure.

| Panel | Content | Status |
|:---|:---|:---|
| 3a | Dosing and recording timeline (pilocarpine model schematic) | **Have** |
| 3b | % total duration seizing | **Have** |
| 3c | % duration of generalized (stage 3-6) seizures | **Have** |
| 3d | % duration of generalized seizures over time (15-min bins) | **Have** |
| 3e | % survival at 48h post-SE | **Have** |
| 3f | Kaplan-Meier probability of survival, 48h | **Have** |
| 3g | % duration of seizure stages, stacked | **Have** |
| 3h | % duration of stage 6 (most severe) seizure activity | **Have** |

# Figure 4 — Flank-incision efficacy

Modeled on: Porterfield Fig. 6 (timeline diagram + survival/outcome curve + histology quantification); existing lab convention (the "Standard (g), Avg & SEM" von Frey time-course plot already in use).

**Seven panels, a-g, contiguous** (2026-11-03 revision: panels g/h — ALT/AST, open-field — cut and replaced with a single real panel g; see below). Per the user's decision, V12 and V13 (same preparation) are pooled with no cohort distinction anywhere in the figure, not even in panel titles — that detail lives in Methods and Table S1 only. The former panel d (a discovery-vs-new-cohort forest plot) is cut entirely rather than emptied: once the new cohort's data pools in, there is no separate "old" and "new" left to plot against each other. The replication finding (whether the new cohort reproduced the effect) is reported in text/Results, not as a figure panel.

| Panel | Content | Status |
|:---|:---|:---|
| 4a | Study design/timeline schematic | **Have** |
| 4b | Time course of 50% withdrawal threshold, all arms, individual animals, pooled across cohorts with no cohort distinction drawn — **keep the existing von Frey time-course convention**; Sharma 2024's categorical seizure-grade bar panels don't map onto continuous mechanical-threshold data, don't switch to that style here | **Have** V12+V13 pooled; new cohort pools in once dosed |
| 4c | AUC, individual animals shown, pooled — **primary endpoint** | **Have** V12+V13 pooled; new cohort pools in once dosed |
| 4d | Responder analysis — **template: Sharma 2024 Fig. 11b**, compact bar chart of animal counts per outcome category (e.g., "recovered to ≥50% baseline" vs. "did not"), count fraction labeled on each bar | **Box** |
| 4e | Ropivacaine validation | **Have** some historical (V21); **Box** for new cohort |
| 4f | Wound histology — **template: Porterfield Fig. 6c-d**, H&E/IHC images + injury-marker quantification bar graph | **Box** |
| 4g | Per-animal slope, baseline to ~72h — **prespecified secondary readout** (added 2026-11-03 per the PI session), not a replacement for the AUC primary. 72h chosen because ~50% of conjugated drug has released by then and the behavioral time course plateaus 48-96h | **Have** — computed from real pooled V12+V13 data |

**Panels g/h (ALT/AST, open-field) cut 2026-11-03.** The 2026-11-02 PI session settled against any toxicity/safety figure — "we are not going to be able to show toxicity with CBD because CBD itself is not that toxic." Replaced by the slope panel above, which the same meeting actually asked for.

# Figure 5 — cut 2026-11-03

Was: inflammatory markers across indications (pain + epilepsy cytokine dot plots, combined summary). Had no counterpart in the 2026-11-02 PI session — cytokines came up only as the in vitro efficacy readout (one MSD plate, one species) inside Figure 2, not a standalone cross-indication marker figure. `build_fig5_mock.py` kept as historical record (marked superseded); `fig5_box_layout.png` removed.

# Figure 6 — Biodistribution: GD-Cy5 localization

**Rebuilt 2026-11-03** around the real, settled design — see `build_fig_bio_mock.py`'s own header for the full account. The old version (modeled on Porterfield/Sah/Sharma's quantified-uptake conventions, built around a new Cy5-GD-CBD dosing study) no longer applies: compound is **GD-Cy5** (dendrimer alone, not the CBD conjugate — the paper makes no CBD-localization claim), material is **existing** flank-incision cryosections (not a new dosing study), **no IVIS**, and **no quantification** ("just show like an image... that's good enough").

| Panel | Content | Status |
|:---|:---|:---|
| 6a | Study design: existing GD-Cy5 cryosections, n=3 target, plus a no-dendrimer negative control. Localization only | **Have** — design is real and settled |
| 6b | Representative positive section, DRG neurons and glia | **Box** — schematic cartoon, real confocal images not yet provided to this repo |
| 6c | Representative no-dendrimer negative control | **Box** — same |

**Open:** whether the n=3 sections and negative control are actually confirmed in hand (vs. needing to be located — tissue custody was unclear in the room) is logged in the main plan's Open items, not assumed.

# CB<sub>2</sub> overexpression after insult — new, unnumbered

**Added 2026-11-03.** The single biggest structural addition from the 2026-11-02 PI session: show CB<sub>2</sub> goes up after the insult in each of the three systems the paper uses (microglia, DRG neurons/glia, seizure neurons), so a CB<sub>2</sub>-agonist conjugate is mechanistically justified rather than asserted. Built as one cross-model panel row (`fig_cb2_throughline.png`, `build_fig_cb2_throughline.py`) per the user's choice over scattering this content into the three main figures. Deliberately not quantified or powered — "just show like an image and say it's more, it's less, that's good enough" — and not a gate on the paper. **No figure number assigned yet**; where it lands is part of the pending renumbering pass.

| Panel | Content | Status |
|:---|:---|:---|
| a | Microglia (BV2/HMC3), naive vs. +LPS | **Box** — no stain/blot run yet |
| b | DRG neurons + glia, naive vs. injured (incision model) | **Box** — same |
| c | Hippocampal/cortical neurons, naive vs. post-SE | **Box** — same |

# Supplement

| Item | Status |
|:---|:---|
| Table S1 — the three disclosed cohorts (V12, V13, new) | **Have** V12/V13; **Box** for the new cohort |
| Table S2 — batch QC | **Box** |
| Raw NMR/HPLC/MALDI spectra | **Box** |
| Sensitivity analyses | **Box** — analysis plan already written |

# Comparator-paper cross-reference

| Paper | What it's the template for |
|:---|:---|
| Sah et al. 2023, *Dev Neurosci* | Biodistribution claim-level ceiling (no carrier-only control, biodistribution with no n). **No longer the Figure 6 template** since the 2026-11-03 rebuild — real design is simpler than even this precedent (representative images only, no quantification at all) |
| Porterfield & Sharma et al. 2023, *Bioeng Transl Med* | Fig. 1 layout, Fig. 4g histology. **Biodistribution-panel template no longer used** (see above) |
| Sharma et al. 2024, *Bioeng Transl Med* | Fig. 1c-d (release, spectra), Fig. 4e (responder-bar convention). **Biodistribution-d quantified-uptake convention no longer used** — the real design explicitly rejects quantification |
| Gusdon et al. 2022, *Sci Transl Med* | **No longer used** — was the template for the cut Figure 5 (per-patient marker dot plots) |
