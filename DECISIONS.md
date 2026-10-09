# Decisions log

Append-only. Each entry is one planning session. Keep entries short; the plan document holds current state, this holds why it changed.

---

## 2026-10-09 — plan v1 → v2, review session with user

**v1 drafted** from nine source files (`sources/`) read in full (lab-update PDF rendered as images), plus a literature check (`literature/search_notes_2026-10-09.md`, search summaries only, not full text — paper hosts blocked in this environment).

**v1 → v2 changes, by topic, with the reasoning:**

- **Strategy.** v1 unifying line was neuronal hyperexcitability. Epilepsy collaborator has a multi-figure dataset (biochemical + several seizure measures) and wants in. New unifying line: **inflammation**, same cytokine panel (TNF-α, IL-6, IL-1β, IL-10) measured in both species. Combined paper is now default; pain-only short report is the fallback if the other PIs don't approve the combined paper or the pain cohort fails outright.
- **Replication framing.** User: two original positive cohorts = cohort 1 replicates cohort 2 already; the new cohort is the *third* replicate, not "the only independent test." Accepted — reframed as "two preparations, three cohorts" rather than disputing the pooling itself. The only thing that stays firm: a claim of "replicated" needs the new, independent-material cohort to show it, not just the pool.
- **Cohort groups.** Went through 5/4/3 → 3/3/3 → 4/3/2 → settled 4/3/2 with GD-CBD 4 / vehicle 3 / free CBD 2 (I flipped user's proposed vehicle-2/CBD-3 — vehicle is the primary comparator and needs the larger n; free CBD already has n=6 historical at this dose). User agreed to let total n flex later (bump-up menu added in v2 §3) rather than lock small.
- **Primary endpoint.** Fixed, at user's request to just decide: per-animal AUC 24–168h as % of baseline, rank-based test, absolute grams as backup.
- **Biodistribution.** Dropped the uninjured-control arm (user: ipsi/contra in the same animal is an adequate internal control, IVIS "not our friend lately"). Landed on Level 1 (5 rats: n=3 Cy5-GD-CBD + n=2 vehicle), tissue fluorescence as primary readout, whole-body IVIS kept only as optional kinetics. DRG: collect in all 5 animals including vehicle (need background to threshold against) but process only if the easy tissues are positive.
- **In vitro additions** (from epilepsy collaborator's input): CB1/CB2 binding, full cytokine panel instead of TNF-α alone, viability control added on every plate (HU-331 is a cytotoxic quinone — a dying-cell signal looks like an anti-inflammatory one otherwise).
- **HU-331/oxidation.** Downgraded from a must-resolve chemistry problem to: LC-MS the CBD *starting material* (bypasses the NMR-masking problem entirely, since there's no dendrimer in the way yet) + viability control on cytokine assays. No longer a go/no-go gate for the paper.
- **Inflammatory markers added to the pain cohort.** Added a 72h satellite group (n=3 GD-CBD + n=3 vehicle, unlabeled) because day-7 endpoint tissue likely misses the inflammatory signal (effect is already fading by 144–168h). Day-7 tissue (wound skin + plasma) still collected from the main cohort as the first pass; DRG/cord/contralateral skin banked, run only if that's informative.
- **Literature check (this session, 6 web searches, summaries only — see `literature/search_notes_2026-10-09.md`):**
  - Free CBD 3 mg/kg IP has published efficacy in other labs' incision models (PMC12844942; 2023 Behav Brain Res; 2017 Front Pharmacol). **Changed the paper's claim** from "free CBD is inactive" to "no sustained effect with dose-matched free CBD in our formulation" — must show the 2–6h window honestly since it does not separate from free CBD there.
  - 2023 study: CBD's effective dose in female rats is estrous-phase dependent. Promoted from a generic "single sex" limitation to a specific, better-supported one — and a plausible partial explanation for this program's cohort-to-cohort heterogeneity (inference, not shown).
  - No peer-reviewed dendrimer-CBD pain paper exists anywhere; only the lab's own conference slides (already public, already claim 5-day efficacy, patent filed per the deck). Paper must not claim more than those slides already do; check patent status before submission.
  - No published DRG/pain-model biodistribution for glucose dendrimers — Sharma 2024 supports neuron uptake in epilepsy only. Reinforces why no neuron-targeting claim is allowed from this program's pain data.
- **Schedule, fixed to real dates** (today = Fri 2026-10-09): order rats Tue Oct 13 → arrive Oct 20 → facility acclimatization to Oct 27 → habituation to Nov 2 → surgery Tue Nov 3 → final behavioral read Nov 10 → Gate 3 (unblind, track decision) Nov 13. Biodistribution dosing moved to Nov 11 / terminal Nov 12 (next-day-after-surgery dissection collided with the main cohort's own 72h work — one team can't do both).
- **Rat order: 21** (9 efficacy + 6 satellite + 5 biodistribution + 1 spare), up from the 12–16 discussed earlier in the session, once user said total rat count isn't the binding constraint (work/time is) and the satellite group was approved.

**Still open / not resolved this session (carried into plan §"Open items"):**
- Original-cohort age/weight/habituation-length (needed before the Oct 13 rat order)
- Other PIs' sign-off on the combined-paper framing
- Epilepsy data-lock date and confirmation the cytokine panel/platform matches
- Batch 4 real loading % (currently assumed ~10% for dosing-mass arithmetic)
- Whether release and CB1/CB2 assay data already exist from the May plan
- Patent status check before submission

**Not done this session:** no register entries, no lab work, no commitments made on the user's behalf. This is planning documentation only.
