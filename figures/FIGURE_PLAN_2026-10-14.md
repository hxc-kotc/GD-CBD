---
title: "GD-CBD figure plan"
subtitle: "Prepared 2026-10-14, revised to match the main plan's figure list. Status markers: Have / Partial / Box (placeholder)."
---

Each figure cites the comparator paper (`literature/comparator_papers/`) its layout is modeled on. Built for Friday: show what's buildable now, leave literal boxes for the rest.

**Each numbered figure is one composite, multi-panel page** — this is consistent across all four comparator papers (e.g. Porterfield Fig. 4 has 8 panels on one page, Sharma 2024 Fig. 11 has 7), not a separate image per chart. Mockups in `figures/mockups/` follow this: `fig4_composite.png` is the actual Figure 4 mockup (all panels a-g on one page); `fig4b/c/d_*.png` are the same content at larger size, kept as source material, not a substitute for the composite.

**Numbering and figure count match `GD-CBD_PUBLICATION_PLAN_2026-10-09.md`'s "Main figures" list** (chemistry, in vitro, epilepsy, pain efficacy, markers) — five main figures, plus biodistribution as Figure 6, built assuming the Cy5-GD-CBD dosing study succeeds (QC ~Oct 30, material ~Nov 6).

**If the pain cohort doesn't replicate and the paper falls back to epilepsy-led or pain-only** (per the main plan's strategy table), this figure list forks: epilepsy-led drops Figure 4 and the pain half of Figure 5; pain-only drops Figure 3 and the epilepsy half of Figure 5.

# Figure 1 — Chemistry and characterization of GD-CBD

Modeled on: Porterfield & Sharma 2023 Fig. 1 + Scheme 1 (structure + physicochemical table); Sharma 2024 Figs. 1–3, 10a-b (synthesis scheme, stacked NMR, HPLC purity).

| Panel | Content | Status |
|:---|:---|:---|
| 1a | Synthesis scheme (GD → linker → CBD click chemistry) | **Box** — need chemist's confirmed Batch 4 route |
| 1b | Physicochemical table (size, zeta, loading %, purity, MW) — Porterfield Fig. 1b format. **Mock values calibrated to Sharma 2024's GD2-VPA** (same GD platform, same CuAAC click linker as GD-CBD): 4.4 nm, near-neutral zeta, 6 wt% loading, 99% purity — not arbitrary placeholders | **Box** — Batch 4 identity due ~Oct 23 |
| 1c | Release profile — **template: Sharma 2024 Fig. 10c**, two curves (lysosomal/esterase pH 5.5 vs. plasma PBS pH 7.4) over ~170h, inset zoom on early timepoints. **Mock curve shaped to that paper's own GD2-VPA numbers**: ~80% release by day 7 at pH 5.5, <6% by day 7 (minimal to 48h) at pH 7.4 — same linker chemistry, not a generic sigmoid | **Box** |
| 1d | Representative NMR/HPLC/MALDI spectra — **template: Sharma 2024 Fig. 10a-b**, stacked traces (free CBD, intermediate, final conjugate), new peak confirming conjugation called out by arrow; single HPLC chromatograph with purity % annotated | **Box** |
| 1e | Hemocompatibility/complement activation (hemolysis, C3a, platelet activation), GD alone vs. GD-CBD — anticipates a standard nanomedicine preclinical question (CARPA), not currently a planned assay. **No comparator paper runs this assay**; mock values set to published hydroxyl-dendrimer biocompatibility ranges instead, not paper-specific | **Box**, not yet scheduled — added 2026-10-15 per "Anticipated predicate-literature questions" |

# Figure 2 — In vitro activity

No direct lab precedent for this exact panel type (none of the four comparator papers run a cytokine panel). Visual convention: Porterfield Fig. 6d (bar graph with individual points, asterisk significance).

| Panel | Content | Status |
|:---|:---|:---|
| 2a | TNF-α/cytokine panel: GD-CBD vs free CBD vs GD alone vs original batch, viability overlay. **Direction grounded in published free-CBD/LPS-macrophage data**; GD-CBD's greater mock potency reflects the activated-macrophage preferential dendrimer uptake mechanism reported in Gusdon 2022, not an arbitrary assumption | **Partial** — some prior TNF-α data exists per batch notes; new-batch panel due ~Oct 23 |
| 2b | CB<sub>1</sub>/CB<sub>2</sub> binding or functional assay. **Free-CBD mock EC<sub>50</sub> (0.3 µM) set within the published CB<sub>2</sub> potency range for CBD** (~0.3-4 µM across assays) | **Box** — open item, may not exist |
| 2c | HU-331 stability-indicating chromatogram (likely supplement) | **Box** |

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

**Six panels, a-f, contiguous** (2026-10-14 revision: cut from seven). Per the user's decision, V12 and V13 (same preparation) are pooled with no cohort distinction anywhere in the figure, not even in panel titles — that detail lives in Methods and Table S1 only. The former panel d (a discovery-vs-new-cohort forest plot) is cut entirely rather than emptied: once the new cohort's data pools in, there is no separate "old" and "new" left to plot against each other. The replication finding (whether the new cohort reproduced the effect) is reported in text/Results, not as a figure panel.

| Panel | Content | Status |
|:---|:---|:---|
| 4a | Study design/timeline schematic | **Have** |
| 4b | Time course of 50% withdrawal threshold, all arms, individual animals, pooled across cohorts with no cohort distinction drawn — **keep the existing von Frey time-course convention**; Sharma 2024's categorical seizure-grade bar panels don't map onto continuous mechanical-threshold data, don't switch to that style here | **Have** V12+V13 pooled; new cohort pools in once dosed |
| 4c | AUC, individual animals shown, pooled | **Have** V12+V13 pooled; new cohort pools in once dosed |
| 4d | Responder analysis — **template: Sharma 2024 Fig. 11b**, compact bar chart of animal counts per outcome category (e.g., "recovered to ≥50% baseline" vs. "did not"), count fraction labeled on each bar | **Box** |
| 4e | Ropivacaine validation | **Have** some historical (V21); **Box** for new cohort |
| 4f | Wound histology — **template: Porterfield Fig. 6c-d**, H&E/IHC images + injury-marker quantification bar graph | **Box** |
| 4g | Hepatic transaminases (ALT/AST), terminal serum — anticipates the most common CBD-field safety question | **Box**, conditional on whether terminal serum is banked — added 2026-10-15 |
| 4h | Open-field locomotor activity — rules out a motor-confound explanation for the von Frey result | **Box**, not yet scheduled — added 2026-10-15 |

# Figure 5 — Inflammatory markers across indications

Modeled on: Gusdon 2022 Fig. 5 — per-patient dot plots of marker rate-of-change by treatment arm, Wilcoxon rank-sum. Best available template for the shared cytokine-panel figure.

| Panel | Content | Status |
|:---|:---|:---|
| 5a | Pain: wound/plasma cytokine panel, per-animal dots by arm | **Box** |
| 5b | Epilepsy: matched cytokine panel | **Box** — entirely dependent on collaborator's data lock |
| 5c | Combined/side-by-side summary, two species, same analytes | **Box** |

# Figure 6 — Biodistribution of Cy5-GD-CBD

Modeled on: Porterfield Figs. 4–5 (organ IVIS, flow cytometry % cells, confocal colocalization, organ PK bar graph); Sah 2023 Fig. 1 (Cy5 colocalization with cell markers, **no n reported** — representative images only); Sharma 2024 Figs. 5/6/8 (quantified uptake as mean fluorescence intensity, **n stated per cell/neuron**, not just per animal).

| Panel | Content | Status |
|:---|:---|:---|
| 6a | Study design schematic | **Have** — design is set |
| 6b | Ex vivo tissue fluorescence, ipsilateral vs contralateral, paired per animal | **Box** — Nov dosing |
| 6c | Confocal colocalization, wound/DRG/cord with cell markers | **Box** |
| 6d | Quantified uptake, Sharma-style (mean fluorescence intensity, n cells stated) | **Box**, pending whether DRG gets processed |

**Claim-level note:** Sah's biodistribution figure has no n at all. This design (n=3, paired, directional-consistency claim only) is already more rigorous than that precedent — don't let the claim creep past what the design supports just because a looser precedent exists.

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
| Sah et al. 2023, *Dev Neurosci* | Biodistribution claim-level ceiling (no carrier-only control, biodistribution with no n) |
| Porterfield & Sharma et al. 2023, *Bioeng Transl Med* | Fig. 1 layout, biodistribution panels, Fig. 4g histology |
| Sharma et al. 2024, *Bioeng Transl Med* | Fig. 1c-d (release, spectra), biodistribution-d (quantified uptake convention), Fig. 4e (responder-bar convention) |
| Gusdon et al. 2022, *Sci Transl Med* | Fig. 5 (per-patient marker dot plots) |
