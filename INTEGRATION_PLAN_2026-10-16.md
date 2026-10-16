---
title: "Integration plan: 16 Oct 2026 lab meeting → GD-CBD publication plan and figures"
subtitle: "Source: literature/lab_meetings/2026-10-16_SK_lab_update/. This is a plan, not yet executed — see 'What this document is' below."
---

# What this document is

Spencer presented a GD-CBD figure/publication plan to Kannan, Sujatha, and the lab group on 2026-10-16. That plan has real structural differences from what's currently built in this repo (figure numbering, scope, and two figures that don't exist in our plan at all). This document is the diff and a recommended order of operations — **nothing listed below has been executed yet.** Low-risk items (confirmations, renumbering, caption fixes) are recommended for immediate execution; items that mean building new mock figures or cutting existing ones are flagged for a go-ahead first, consistent with how new figures have been added in this repo all along (confirm scope, then build).

# 1. What's now confirmed (no longer "assumed")

- **Combine epilepsy + pain into one paper.** This repo already assumed this; it's now the PI-and-group-agreed plan, not just our working assumption. No change needed, but update the plan doc's framing from "default strategy" to "decided."
- **Formulation is the lead value, not a side note.** Kannan: "dendrimer conjugation significantly improves the formulation... we often don't do this for other drugs," don't underplay it. Sujatha: this is what the medical community will be most excited by. **This has no figure in our current 6-figure plan at all.** See §3.
- **Pain cohort target: n=9** (currently 6, i.e. our pooled GD-CBD arm n=6 — matches the slide's "N of 6 now... shooting for 9"). Consistent with what we already show; just confirms the replication-cohort target isn't arbitrary.
- **No staged preprints.** Settled against. Not relevant to figures, but worth a line in the plan if preprint strategy is ever mentioned there.
- **Safety arm: genuinely open, not settled** — the live discussion rejected one specific design (a dose-matched *conjugate* tox study — too much scarce material) but the slide deck's own Figure 6 proposes a different, cheaper design that's still an open question ("Worthwhile?"). See §4.

# 2. Figure structure: real plan vs. this repo's current plan

The lab's real figure numbering and scope differ from ours in several places:

| # | Real plan (16 Oct slides) | This repo's current figure | Delta |
|:--|:---|:---|:---|
| 1 | Synthesis & Characterization: scheme, NMR, HPLC purity, release/stability, physicochem table, **CB1/CB2 binding**, **liver microsome metabolism** | Figure 1: scheme, table, release, NMR, hemocompatibility (e) | CB1/CB2 binding and microsome stability belong in **Figure 1** in the real plan, not Figure 2. Our hemocompatibility panel (1e) has no counterpart in the real plan — it was our own anticipatory addition, not something the lab asked for (see §6). |
| 2 | In Vitro Uptake & Activity: uptake in **3 cell types** (neurons, microglia, macrophages) + free-vs-GD-CBD efficacy in **3 systems** (injured neurons, LPS-microglia, LPS-macrophages) | Figure 2: TNF-α bar (THP-1), CB1/CB2 dose-response, HU-331 chromatogram | Real Figure 2 is uptake-plus-efficacy across three specific cell types, not a THP-1 cytokine panel. CB1/CB2 moves out (→ Fig 1). **HU-331 isn't mentioned anywhere in the real plan** — the group's own stated priority is minimum dataset; HU-331 was this repo's own addition from the original plan doc, not something raised at this meeting. |
| 3 | Distribution/Localization: **combined** SE + flank incision in one figure (SE: IVIS/sectioning; flank: IVIS/sectioning, periwound ipsi/contra, DRGs/spinal cord/peripheral nerves) | Figure 6: biodistribution, flank-incision only, "conditional, not numbered" | Real plan makes this a numbered **Figure 3**, not a conditional end-figure, and folds in SE biodistribution too (with an explicit note in the SE figure slide: "Biodistribution/localization? (ref previous paper)" — may lean on prior published GD-Cy5 epilepsy work rather than new data). |
| 4 | Status Epilepticus Efficacy (pilocarpine; free CBD vs GD-CBD vs Vehicle) | Figure 3 (collaborator's real data, 8 panels a-h) | Same content, different number. Real plan's panel list (stacked seizure-stage duration, % generalized seizures over time, Kaplan-Meier survival, several secondary measures) matches what's already built. **Just a renumber: our Figure 3 → Figure 4.** |
| 5 | Flank Incision Efficacy (von Frey longitudinal + pooled AUC + ropivacaine validation; wound healing H&E + gross images) | Figure 4 (8 panels a-h, von Frey real data + boxes) | Same content, different number. **Just a renumber: our Figure 4 → Figure 5.** Real plan's explicit framing: "↓ hypersensitivity without affecting wound healing" — our wound-histology panel (4f) is already there as a box; worth stating that framing line in its caption once real data lands. |
| 6 | Toxicity/Safety — **open**, not committed | Not in our plan as a dedicated figure (we built ALT/AST + locomotor as panels 4g/4h, bolted onto the pain figure) | See §4 — real proposed design differs materially from what we mocked. |
| — | **Formulation** — own figure and section | Not in our plan at all | See §3. |

Net: this repo's figures 1-5 all have real counterparts, just two numbering shifts (3→4, 4→5) and some scope moved between Fig 1/Fig 2. Figure 5 (our cytokine/inflammatory-markers figure) has **no counterpart** in the real plan at all (§5). Figure 6 (biodistribution) needs to become a numbered Figure 3, not stay a conditional end-figure, and the compound question (GD-Cy5 reuse vs. new GD-CBD-Cy5 experiment) is explicitly unresolved — Sujatha leans toward reusing existing GD-Cy5 imaging rather than running a new experiment at all (§6).

# 3. New figure needed: Formulation

Not in our current plan. Per the meeting this is the **lead value proposition**, deserves its own figure and section, and the key message is specific: *saline-soluble and stable in solution, while free CBD is neither.*

**Recommended panels** (mock/Box until the actual stability data exists — Kannan described this as new, simple work, not yet run):
- Aqueous/saline solubility: amount dissolved, free CBD vs. GD-CBD (bar or table).
- Room-temperature solution stability over time, free CBD vs. GD-CBD (degradation curve, days).

This slots in as a new **Figure 2** in the real numbering (chemistry → formulation → in vitro → distribution → SE → pain), or could be folded into Figure 1 as additional panels — the slides keep it conceptually separate ("own figure and section" per Kannan), so a standalone figure matches the ask better than folding it in.

# 4. Figure 6 (Toxicity/Safety): reconcile with what we already built

We already built ALT/AST and open-field locomotor panels (4g/4h in the current Figure 4) anticipating a CBD-field safety question — good instinct, but the real proposed design is more specific and differs in ways that matter if this gets built out:

| | What we built (4g/4h) | Real proposed design (slide Fig 6) |
|:--|:---|:---|
| Dose | 3-30 mg/kg (matched to the efficacy study) | **738 or 2460 mg/kg, oral** (literature hepatotoxicity-threshold doses) |
| Animals | The efficacy cohort (injured, flank-incision) | **Healthy animals**, separate single-dose acute study |
| Route | IP (matching the efficacy dosing) | **Oral** |
| Readouts | ALT/AST only; open-field distance | Clinical observation (lethargy, righting reflex, posture, piloerection, tremor, ataxia); body weight over time; **liver:body-weight ratio at 24h**; activity/motor **at 1h and 4h post-dose** (open field **and rotarod**); blood panel: **ALT, AST, and bilirubin** |
| Status | Box, framed as "literature-grounded, not yet planned" | **Explicitly open** — "Worthwhile? vs Oral? Liver histology? Chronic?" — not committed either way |

**Recommendation:** don't just relabel what exists — rebuild this as its own candidate Figure 6 matching the real proposed design (different dose, route, animals, and readouts), explicitly marked as reflecting the PI's own proposed design rather than our predicate-literature anticipation. Keep "Worthwhile?" as an open question in the caption rather than presenting it as decided, since the group hasn't decided it. This is a bigger rebuild than a caption edit — recommend confirming before building.

# 5. Figure 5 (cytokine/inflammatory markers): likely cut

Our current Figure 5 — pain and epilepsy cytokine dot plots plus a combined summary bar chart — has no counterpart anywhere in the real plan or the discussion notes. The real Figure 2 does cover LPS-microglia and LPS-macrophage efficacy, which could include cytokine readouts (TNF-α etc.) as part of *that* figure's panels, but there's no indication the lab wants a dedicated systemic/cross-species marker figure like what we built.

**Recommendation:** fold any real cytokine data into Figure 2's efficacy panels once it exists, and drop the standalone Figure 5 from the plan rather than keep building it out. This is a cut, not a small edit — flagging for confirmation rather than doing it silently.

# 6. Biodistribution: naming and scope are both open

- **Compound:** our Figure 6 is already named/captioned "Cy5-GD-CBD," presented as the planned compound. The real discussion is unresolved: Kannan wants a new, carefully-planned IVIS experiment with GD-CBD-Cy5; Sujatha says existing GD-Cy5 imaging (already covering the DRG pathway from prior flank-incision work) is "good enough" and a new experiment isn't needed unless a reviewer asks. Spencer sided with Sujatha's "minimum dataset" framing in the room.
- **Scope:** should become a numbered Figure 3 covering *both* SE and flank-incision distribution, not a conditional end-of-paper figure gated on a future Cy5 study.
- **Recommendation:** soften the current Figure 6 caption to state the compound question as open rather than settled, and flag — don't yet build — the renumber/merge into a combined Figure 3, since whether any new biodistribution data collection happens at all is still unresolved.

# 7. Items to log in the plan doc as explicitly open (not to build figures for yet)

- CB1/CB2 "why hasn't binding been perfect" — Sujatha's question, Narendra's data pending, direct radioligand binding vs. the current indirect approach undecided.
- Preeti's frozen-brain mechanism/biochemical assay — undecided whether it's used.
- Epilepsy cohort N: 8-9 total vs. 4-5 after exclusion — undecided which number the figure will report; our existing Figure 4 caption already says "draft panel set... not the final n," which already hedges correctly, no change needed there.
- Microsome/liver metabolism repeat (Kavi, in triplicate) — not yet run; candidate new Figure 1 panel once data exists.

# 8. Recommended order of operations

1. **Low-risk, do now:** update `GD-CBD_PUBLICATION_PLAN_2026-10-09.md` — mark epilepsy+pain combination as decided (not assumed), log the pain-cohort n=9 target as confirmed, add the open items from §7 to the existing Risks/Open items sections, note the preprint decision.
2. **Confirm, then build:** new Formulation figure (§3) — cheap, clearly scoped, directly requested. Mock/Box panels following this repo's established convention.
3. **Confirm, then rebuild:** Figure 6 Toxicity/Safety to match the real proposed design (§4), replacing the current 4g/4h panels (which would move out of Figure 4/pain and into their own candidate Figure 6).
4. **Confirm, then cut:** Figure 5 cytokines (§5) — removal, not an edit, so flagging rather than doing it silently.
5. **Confirm, then renumber:** shift current Figure 3→4, Figure 4→5, consolidate Figure 6 into a numbered Figure 3 covering both models (§2, §6), move CB1/CB2 and microsome panels from Figure 2 into Figure 1, and restructure Figure 2 around the real three-cell-type uptake/efficacy scope.

Steps 2-5 touch five of six figures and change the paper's figure count and numbering — bigger than this repo's usual single-figure edits, hence flagged for a go-ahead rather than executed inline with this plan.
