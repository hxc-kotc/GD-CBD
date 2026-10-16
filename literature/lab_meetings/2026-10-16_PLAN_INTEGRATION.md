---
title: "Integrating the 2026-10-16 lab update into the GD-CBD plan"
subtitle: "Source: literature/lab_meetings/2026-10-16_lab_update_full_notes.md (So lab group update, Spencer presenting, 56 min). This doc covers only the GD-CBD-relevant parts (section 2 of the source notes). The noribogaine (section 3) and AI Lab Partner material is out of scope for this repo — see the note at the end."
---

# How to read this

Proposed diffs to `GD-CBD_PUBLICATION_PLAN_2026-10-09.md` and the figure set, grouped by how settled each one is. Nothing below has been applied yet — this is the plan to review before I start editing, because two items (C and part of D) touch work from the last several rounds and one touches the submission date itself.

# A. Already matches the plan — no action needed

- **Combined epilepsy+pain paper.** Our plan's default strategy already is this (`# Strategy`, "Default: combined epilepsy-plus-pain paper"). The lab meeting confirms it as the group's actual decision, not just our working assumption. No change, but worth noting in the plan that this is now PI-group-confirmed, not just proposed.
- **Pain cohort size.** Notes: "N of 6 now... shooting for 9." Our cohort is already specced at 9 (4 GD-CBD + 3 vehicle + 2 free CBD). Consistent.
- **Epilepsy framed as proof-of-concept, not a targeting claim.** Notes: "a lot of GD-Cy5 work in epilepsy is already published, so this is a proof of concept... say previously shown that the dendrimer targets epileptic neurons and microglia, and that CBD acts on this." This matches our plan's existing "Claims to avoid" (no neuronal-targeting claim) and Figure 3's framing around the collaborator's real data.
- **In vitro: macrophages, not both microglia and macroglia.** Notes: C says pick one; F says macrophages "for sure" for the pain indication. Our Figure 2a already uses THP-1 (human macrophage-like), not microglia. Consistent, no change.
- **Mechanism: don't over-claim.** Notes: "CBD has several vague mechanisms, so just show some efficacy." Matches our plan's existing restraint (no mechanism figure committed).

# B. New additions the notes call for — not in the plan yet

1. **Formulation gets its own figure and section — the lead value of the paper.** This is the single clearest instruction in the notes: Kannan says explicitly not to underplay it ("we often don't do this for other drugs"), C says it's what the medical community will find most exciting. Specific content: **amount of CBD that dissolves in water/saline, and room-temperature solution stability over time, free CBD vs. GD-CBD, side by side.** This is new work (Kannan proposed the stability test as simple, unassigned as of the meeting) and a new figure — currently our Figure 1 panel b (physicochemical table) has size/zeta/loading/purity but nothing on solubility or stability. **Proposed: add a Figure 1 panel (or expand into its own figure) with solubility (mg/mL in water/saline) and a stability-over-time curve, free vs. conjugated — mirroring the release-profile convention we already built for 1c.**

2. **Liver microsome metabolism (free vs. GD-CBD) is real, near-term work — our plan currently says "do not do now."** Notes: done once already, Kavi repeating in triplicate, in one batch (not piecemeal). This directly contradicts the `Minimum viable package` table's "Do not do now" column, which lists "microsomes." **Proposed: move microsome metabolism from "do not do now" to "must have" (or "nice to have" if Kavi's repeat isn't done in time), and add a placeholder panel to Figure 2 (or a new 2d) for it.**

3. **CB1/CB2 binding curves need a named source and an open question flagged.** Notes: C asked Narendra directly for CB1 and CB2 curves, and separately asked whether direct radioligand binding (vs. the current indirect approach) is possible — unresolved in the meeting. Our Figure 2b already exists as a placeholder; **proposed: update its status note to name Narendra as the source and flag the radioligand-vs-current-method question as unresolved, matching the real open item instead of just "may not happen."**

# C. Direct conflict with what we already built — needs your call

**Safety arm: the lab explicitly decided against one.** This is the one that matters most, because we spent two rounds adding exactly this.

- Notes, section 2.4, are unambiguous: *"there is nothing on safety right now"* (C and Spencer); *"cannot show much because CBD itself is safe"* (Kannan); a proposal to bleed a few high-dose animals for liver/kidney chemistry was discussed and **explicitly not pursued** — Kannan and C: "that would use up the good conjugate," Spencer agreed. The agreed handling: **a general safety argument in the Discussion only** (cite the GD-Ket paper, argue GD's therapeutic-index improvement lets CBD's known negative effects — sedation, hepatotoxicity — be diminished), **not a figure.**
- That's close to the opposite of what we built in the last two rounds: Figure 4g (ALT/AST from terminal serum) and Figure 1e (hemocompatibility/CARPA), both added specifically to preempt CBD-field reviewer questions about safety.
- These aren't necessarily wrong to have *built* — they're still honest, grounded placeholders, clearly marked "not yet a planned assay." But given the room's explicit decision, presenting them as part of the real figure set risks exactly what Kannan warned about: "saying anything gives reviewers something to poke," and burns scarce Batch 4 conjugate the group already declined to spend on this.
- **Options, your call:**
  a. **Pull Figure 4g and 1e from the main figure set entirely**, fold their content into one Discussion paragraph (GD-Ket precedent argument, as the notes specify) instead of a figure, and keep the panel-build scripts in the repo as historical record (same as the other superseded scripts).
  b. **Demote them to Supplement-only**, kept as "if a reviewer asks" material rather than main-text figures, so they exist but don't visually signal "safety arm" to anyone skimming the figure list.
  c. **Keep them as-is** if you want insurance against a CBD-field reviewer's question regardless of the room's cost/scope call — your reasoning in that case would be worth logging, since it knowingly diverges from the group decision.

**IVIS compound choice: GD-CBD-Cy5 (what Figure 6 assumes) vs. existing GD-Cy5 data (what C argued is "good enough").** Also unresolved in the meeting itself, so this isn't something I got wrong — the room didn't settle it either. Kannan wants one clean, newly planned IVIS experiment with GD-CBD-Cy5 and proper control/injured arms; C says existing GD-Cy5 imaging (a different, already-available compound, not the CBD conjugate) is sufficient for a flank incision and "if a reviewer asks, we'll think about it"; Spencer sided with C's version in the room ("That's exactly what I agree," "we will get the minimum dataset needed"). Our Figure 6 is built entirely around a new Cy5-GD-CBD dosing study (QC ~Oct 30, material ~Nov 6). **If the lab actually goes with C's "use existing GD-Cy5" route, Figure 6 as built doesn't correspond to what will really happen** — it would need rebuilding around existing GD-Cy5 (non-CBD-conjugated) imaging data instead of a new dosing study. Worth getting a real answer before investing more in this figure.

**Submission timeline: Kannan wants it submitted in about a month; our plan targets 2026-12-29.** Notes: "needs it submitted in the next month, or it will count as one of the 20" (his paper-count bet with Durga). Our plan's own timeline has Gate 3 (pain result) on 11-14 and submission on 12-29 — roughly six weeks past Kannan's stated deadline, and the full draft/PI-review/revise cycle (11-28 through 12-29) alone is about the length of the deadline Kannan wants. Spencer's own words in the room: "stretching it to get there." This is a real, acknowledged-in-the-room tension, not a new problem — but it's not reflected anywhere in our plan's Timeline or Risks sections yet. **Proposed: add a Risks row naming this gap explicitly**, since it's exactly the kind of thing that should be visible rather than quietly absorbed.

# D. Smaller items worth one line each

- **Epilepsy N is still ambiguous in the room itself** (8-9 total vs. 4-5 after excluding a failed batch) — not something to resolve on our end, just worth a placeholder note in Figure 3's status until Preeti/Kannan settle it (notes say "assemble everything," not "use N=X").
- **Preeti's frozen brains (possible biochemical mechanism assay)** — notes say "not decided." No action; don't add a mechanism panel speculatively.
- **No staged preprints.** Matches our plan's silence on preprints (we never proposed one) — just confirms no change needed, and rules out a preprint as a "minimum dataset" workaround if the Dec 29 date slips.
- **PCT patent / tech-transfer timing** — notes don't add anything beyond what our plan already flags (`Action: loop in Hopkins tech transfer or patent counsel`). No change.

# Out of scope for this repo

Sections 3 (noribogaine/ibogaine, Paper 2) and 5.1/5.3 (AI Lab Partner aside, neuroplasticity work, grant framing) of the source notes concern a different project this session has no repository for. The full notes file is saved verbatim either way (`2026-10-16_lab_update_full_notes.md`) so nothing is lost, but no GD-CBD-repo changes are proposed for that material. If you want those integrated somewhere (a GD-nori-KB-style repo, if one exists), say so and I'll either attach that repo or hand off a similarly-structured digest.
