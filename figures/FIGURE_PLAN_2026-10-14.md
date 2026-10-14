---
title: "GD-CBD figure plan"
subtitle: "Prepared 2026-10-14, revised to match the main plan's figure list. Status markers: Have / Partial / Box (placeholder)."
---

Each figure cites the comparator paper (`literature/comparator_papers/`) its layout is modeled on. Built for Friday: show what's buildable now, leave literal boxes for the rest.

**Numbering and figure count match `GD-CBD_PUBLICATION_PLAN_2026-10-09.md`'s "Main figures" list exactly** (chemistry, in vitro, epilepsy, pain efficacy, markers) — five main figures. Biodistribution is **not** a numbered main figure; it stays conditional per that plan's own rule ("Supplement: ... biodistribution if it passes," "omit entirely" on failure). It's included below as its own section so the panels are ready either way, but it does not get a figure number until the QC and effect size actually justify one.

**If the pain cohort doesn't replicate and the paper falls back to epilepsy-led or pain-only** (per the main plan's strategy table), this figure list forks: epilepsy-led drops Figure 4 and the pain half of Figure 5; pain-only drops Figure 3 and the epilepsy half of Figure 5.

# Figure 1 — Chemistry and characterization of GD-CBD

Modeled on: Porterfield & Sharma 2023 Fig. 1 + Scheme 1 (structure + physicochemical table); Sharma 2024 Figs. 1–3, 10a-b (synthesis scheme, stacked NMR, HPLC purity).

| Panel | Content | Status |
|:---|:---|:---|
| 1a | Synthesis scheme (GD → linker → CBD click chemistry) | **Box** — need chemist's confirmed Batch 4 route |
| 1b | Physicochemical table (size, zeta, loading %, purity, MW) — Porterfield Fig. 1b format | **Box** — Batch 4 identity due ~Oct 23 |
| 1c | Release profile — **template: Sharma 2024 Fig. 10c**, two curves (lysosomal/esterase pH 5.5 vs. plasma PBS pH 7.4) over ~170h, inset zoom on early timepoints | **Box** |
| 1d | Representative NMR/HPLC/MALDI spectra — **template: Sharma 2024 Fig. 10a-b**, stacked traces (free CBD, intermediate, final conjugate), new peak confirming conjugation called out by arrow; single HPLC chromatograph with purity % annotated | **Box** |

# Figure 2 — In vitro activity

No direct lab precedent for this exact panel type (none of the four comparator papers run a cytokine panel). Visual convention: Porterfield Fig. 6d (bar graph with individual points, asterisk significance).

| Panel | Content | Status |
|:---|:---|:---|
| 2a | TNF-α/cytokine panel: GD-CBD vs free CBD vs GD alone vs original batch, viability overlay | **Partial** — some prior TNF-α data exists per batch notes; new-batch panel due ~Oct 23 |
| 2b | CB<sub>1</sub>/CB<sub>2</sub> binding or functional assay | **Box** — open item, may not exist |
| 2c | HU-331 stability-indicating chromatogram (likely supplement) | **Box** |

# Figure 3 — Epilepsy

Externally supplied by the collaborator. Likely follows Sharma 2024 Fig. 11's own structure (severity/duration/latency bars + categorical SE-onset outcome bars), since that's the platform paper this figure inherits from. Full box until the collaborator sends something.

| Panel | Content | Status |
|:---|:---|:---|
| 3a–3x | Collaborator's figure, structure TBD | **Box** |

# Figure 4 — Flank-incision efficacy

Modeled on: Porterfield Fig. 6 (timeline diagram + survival/outcome curve + histology quantification); existing lab convention (the "Standard (g), Avg & SEM" von Frey time-course plot already in use).

| Panel | Content | Status |
|:---|:---|:---|
| 4a | Study design/timeline schematic | **Have** |
| 4b | Time course of 50% withdrawal threshold, all arms, cohort-coded — **keep the existing von Frey time-course convention**; Sharma 2024's categorical seizure-grade bar panels don't map onto continuous mechanical-threshold data, don't switch to that style here | **Have** historical (V12/V13), plottable now; new cohort overlays in Nov |
| 4c | AUC, individual animals shown | **Have** historical; **Box** for new cohort |
| 4d | Per-cohort forest plot (replication tiering) — standard clinical/meta-analysis convention, no lab-specific precedent needed | **Have** enough historical cohorts to compute now; **Box** for new cohort's entry |
| 4e | Responder analysis — **template: Sharma 2024 Fig. 11b**, compact bar chart of animal counts per outcome category (e.g., "recovered to ≥50% baseline" vs. "did not"), count fraction labeled on each bar | **Box** |
| 4f | Ropivacaine validation | **Have** some historical (V21); **Box** for new cohort |
| 4g | Wound histology — **template: Porterfield Fig. 6c-d**, H&E/IHC images + injury-marker quantification bar graph | **Box** |

# Figure 5 — Inflammatory markers across indications

Modeled on: Gusdon 2022 Fig. 5 — per-patient dot plots of marker rate-of-change by treatment arm, Wilcoxon rank-sum. Best available template for the shared cytokine-panel figure.

| Panel | Content | Status |
|:---|:---|:---|
| 5a | Pain: wound/plasma cytokine panel, per-animal dots by arm | **Box** |
| 5b | Epilepsy: matched cytokine panel | **Box** — entirely dependent on collaborator's data lock |
| 5c | Combined/side-by-side summary, two species, same analytes | **Box** |

# Biodistribution — conditional, not a numbered main figure

Only promoted to a main-text figure if the go/no-go QC passes and the result is strong (per the main plan's "Claims by outcome" table). If modest: one Limitations sentence, no figure. If negative/uninterpretable: omitted entirely. Panels below are prepared either way so there's no scramble if it does pass.

Modeled on: Porterfield Figs. 4–5 (organ IVIS, flow cytometry % cells, confocal colocalization, organ PK bar graph); Sah 2023 Fig. 1 (Cy5 colocalization with cell markers, **no n reported** — representative images only); Sharma 2024 Figs. 5/6/8 (quantified uptake as mean fluorescence intensity, **n stated per cell/neuron**, not just per animal).

| Panel | Content | Status |
|:---|:---|:---|
| Bio-a | Study design schematic | **Have** — design is set |
| Bio-b | Ex vivo tissue fluorescence, ipsilateral vs contralateral, paired per animal | **Box** — Nov dosing, conditional on Cy5 QC |
| Bio-c | Confocal colocalization, wound/DRG/cord with cell markers | **Box** |
| Bio-d | Quantified uptake, Sharma-style (mean fluorescence intensity, n cells stated) | **Box**, conditional on whether DRG gets processed |

**Claim-level note:** Sah's biodistribution figure has no n at all. This design (n=3, paired, directional-consistency claim only) is already more rigorous than that precedent — don't let the claim creep past what the design supports just because a looser precedent exists.

# Supplement

| Item | Status |
|:---|:---|
| Table S1 — full historical cohort record | **Can build substantially now** — real per-animal data across 19 source files already in `data/raw/` |
| Table S2 — batch QC | **Box** |
| Raw NMR/HPLC/MALDI spectra | **Box** |
| Sensitivity analyses | **Box** — analysis plan already written |
| Biodistribution, if it doesn't earn a main figure (modest result) | Conditional, see above |

# Comparator-paper cross-reference

| Paper | What it's the template for |
|:---|:---|
| Sah et al. 2023, *Dev Neurosci* | Biodistribution claim-level ceiling (no carrier-only control, biodistribution with no n) |
| Porterfield & Sharma et al. 2023, *Bioeng Transl Med* | Fig. 1 layout, biodistribution panels, Fig. 4g histology |
| Sharma et al. 2024, *Bioeng Transl Med* | Fig. 1c-d (release, spectra), biodistribution-d (quantified uptake convention), Fig. 4e (responder-bar convention) |
| Gusdon et al. 2022, *Sci Transl Med* | Fig. 5 (per-patient marker dot plots) |
