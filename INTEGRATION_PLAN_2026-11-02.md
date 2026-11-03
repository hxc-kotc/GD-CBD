---
title: "Integration plan: 2 Nov 2026 PI working session → GD-CBD publication plan and figures"
subtitle: "Source: literature/lab_meetings/2026-11-02_PI_meeting/. This is a diff and a plan, not yet executed — see 'What this document is' below."
---

# What this document is

On 2026-11-02 Spencer went through the GD-CBD data and figure plan with Sujatha, Durgadas and Preeti, file by file, on real data. Unlike the 16 Oct lab update (a presentation with slides), this was a working session that **closed several questions `INTEGRATION_PLAN_2026-10-16.md` had to leave open**, cut one model outright, and added one genuinely new structural requirement to the figure set.

This document is the diff and a recommended order of operations. **Nothing below has been executed.** No figure, mockup script, or plan document has been edited — same posture as the 16 Oct integration plan. Low-risk items (confirmations, caption wording, plan-doc status changes) are recommended for immediate execution; items that mean cutting or rebuilding existing mock figures are flagged for a go-ahead first.

**Speaker-label note:** the source transcript mislabels one speaker as "Kannan." Every one of those lines is **Sujatha**. All attributions here are corrected. Where this document quotes the 16 Oct record's attributions, those are left as that record has them.

# 1. Open items from the 16 Oct plan: what this meeting settled

| 16 Oct open item | Status after 2 Nov | How it was settled |
|:---|:---|:---|
| **Biodistribution compound** (§6: GD-Cy5 reuse vs. a new GD-CBD-Cy5 experiment — "not settled") | **Settled: GD-Cy5, existing material** | Sujatha confirmed on screen that the usable flank-incision images are GD-Cy5 alone, showing DRG neurons and DRG glia, and that this is enough: "We'll just show that and say it's getting into the DRG neurons, DRG glia." No new dosing study. Spencer: "At one point I think we were planning like a 21-animal biodistribution." Sujatha: "No, no. Never." |
| **IVIS** (live in the 16 Oct record as a planned retry; Kannan wanted one clean IVIS run) | **Settled: out of the paper** | Preeti: "For the paper, I will take out the IVIS." Sujatha: "We're struggling with IVIS, let's take that out. We'll just keep the rest of it." |
| **Safety / toxicity figure** (§4: three options offered — main figure, supplement-only, or Discussion-only; "Worthwhile?" unresolved) | **Settled against a figure** | Sujatha: "we are not going to be able to show toxicity with CBD because CBD itself is not that toxic. All of its toxicity are chronic toxicity and so we're not going to be able to show that." Durgadas had framed the liver work as stability, not toxicity, and that framing was accepted. |
| **In vitro cell choice** (16 Oct: Sujatha said pick one of microglia/macrophages; this repo's Figure 2 direction was microglia) | **Confirmed: microglia** | "I would not do macrophage and microglia. Pick just one." Durgadas: "the microglia would be right." The pain-model objection was answered rather than reopened: "In the DRG, they are like microglia." Not to be re-litigated. |
| **Liver microsome metabolism** (16 Oct: wanted, in triplicate, Kavi) | **Confirmed, unchanged** | Preeti: "should we do liver metabolism?" Sujatha: "Yeah, yeah. Especially CBD." |
| **SE biodistribution** (16 Oct §2.5 / the real plan's combined Figure 3 folded SE distribution in, with a note to possibly lean on prior published work) | **Settled: not shown at all** | "We're not going to show biodistribution here because we've already done it in 10 different ways in the SE... it's not going to give us anything more." The combined-model distribution figure the 16 Oct plan sketched is now incision-only. |
| **Epilepsy cohort N** (16 Oct: 8-9 total vs. 4-5 after exclusion, undecided) | **Partly settled** | The plotted cohort is 6-7; Preeti has at least 3-4 more per group to add, excluding the partially-working batch ("Do we want to add the one that partially worked or no?" — "No"). Sujatha: "why don't we put that in." Final n still not a number. Delayed-therapy groups (3-4 per group) stay out of this paper. |
| **Preeti's frozen-brain mechanism assay** (16 Oct: undecided) | **Still open, now with a specific use** | Preeti offered an inflammation readout on 48 h microdissected tissue; Sujatha: "it's not a bad idea." Not assigned. Separately, her pilocarpine sections are now wanted for CB<sub>2</sub> staining (§2). |
| **Direct radioligand CB<sub>1</sub>/CB<sub>2</sub> binding** (16 Oct: open) | **Not addressed as such; the practical answer is more points on the existing curve** | Durgadas is repeating the CB<sub>2</sub> binding with more concentrations next week. Sujatha: "Is this enough number of points? No, no. We need to do more." The number now in hand: GD-CBD about **6-fold more potent than free CBD on a drug basis**, with THC as a nanomolar positive control. CB<sub>1</sub> was not discussed; the whole discussion has moved to CB<sub>2</sub>. |

# 2. New in this meeting (not in the 16 Oct plan at all)

## 2.1 CB<sub>2</sub> overexpression as a structural throughline — new required figure element

The single biggest addition. Sujatha wants the paper to show that the target is upregulated by the insult, in **each** of the three systems the paper uses, so that a CB<sub>2</sub>-agonist conjugate is mechanistically justified rather than asserted:

| System | What to show | Material |
|:---|:---|:---|
| In vitro, microglia | CB<sub>2</sub> low before LPS, up after | Western **or** immunostain — "either, either Western or immuno, whichever" |
| In vitro, neurons | CB<sub>2</sub> up after glutamate injury (HT-22) | same |
| Incision model | DRG neurons and DRG glia overexpress CB<sub>2</sub> after injury | **existing** cryosections |
| Seizure model | Neurons overexpress CB<sub>2</sub> after SE | **existing** pilocarpine sections |

- The argument in Sujatha's own words: "we have to show that the target is there and we're going after the target," and the closing logic — "DRG neurons and DRG glia overexpress CB<sub>2</sub> after the incision... Same thing for seizures... So therefore this, which is a stronger CB<sub>2</sub> agonist, works better than CBD."
- **Deliberately cheap.** Staining on existing sections. ELISA was proposed and rejected because it averages the whole tissue. And: "don't try to quantify or do too much, just show like an image and say it's more, it's less, that's good enough."
- **Not a gate.** "I don't think the paper has to be held up for it. If you have evidence, if you're able to get literature evidence that CB<sub>2</sub> goes up, then it's fine." But Sujatha's read is that the literature is "bits and pieces," so showing it in these models is what ties the story.
- **Figure consequence:** this is new content in three different figures (in vitro, incision, epilepsy), or alternatively one small cross-model CB<sub>2</sub> panel row. Neither option exists anywhere in `figures/FIGURE_PLAN_2026-10-14.md`. Recommend deciding **where it lives** before anything is built — a single cross-model panel row reads as the throughline Sujatha described; scattering it into three figures does not.

## 2.2 Slope-to-72h reanalysis of the flank-incision data — new method

- **The method:** per-animal slope from baseline to 72 h, plotted per animal. "If we did a slope from baseline to 72 hours, and we compared the slope per animal... all of these guys would be negative and this would be positive." Spencer: "that's a cleaner plot."
- **Why 72 h:** release kinetics. Durgadas: little drug releases in the first 6 h, and "as glucose, you get nearly 50% released" by 72 h. 48-96 h is a plateau in the behavioral data.
- **It is an addition, not a replacement.** "We'll still show this, but we'll add that as an extra."
- **Conflict to handle, not to paper over.** `GD-CBD_PUBLICATION_PLAN_2026-10-09.md` fixes the primary endpoint as **per-animal AUC, 24-168 h, as percent of baseline**, frozen before unblinding, and that plan's own discipline is what makes the result credible. The slope-to-72h readout therefore enters as a **prespecified secondary/supplementary** analysis added before unblinding, not as a new primary. It should be written into the analysis plan **now**, before this cohort reads out, precisely so it is not a post-hoc endpoint swap.
- **Second conflict:** Sujatha's read of the existing data is that the effect "doesn't last up to 168, it lasts up to 120 hours is probably what we're going to have to say." The plan's AUC window runs to 168 h. Flagging the mismatch rather than changing the window — a 24-120 h window would be a post-hoc narrowing of the primary endpoint and should not be done quietly.
- **Housekeeping from the same discussion:** confirm the existing AUC is per animal (not area of the mean — nobody in the room was sure), recalculate in Prism, share the data file with Preeti to cross-check. Error bars are currently SD; SEM is acceptable and "the stats are not going to change anyway."

## 2.3 Paw incision / paw edema model: cut

- "I think we're going to just nix the paw edema model, paw incision model." And on whether it could survive as supporting data: Durgadas — "the paw edema, are we adding it supporting?" Sujatha — "No."
- **Why:** the existing numbers are too thin (historical: n=2 CBD 3 mg/kg, n=3 CBD 0.3 mg/kg, n=1 saline), so a usable version needs a whole new cohort — "we essentially need to do a full study for it. I would say just remove it."
- **The framing that justifies the cut:** "you have this, you have your flank incision, you have your seizure, so this is not a pain paper, this is a CBD paper."
- **Effect on this repo:** low. The current plan already lists paw edema under "Do not do now," and no figure or mockup here is built on it. This mostly closes a door Spencer had wanted to keep open — he said he would "feel way better about the pain side of it if we did on-surgery," and was told the paper does not need it.

## 2.4 Computational modeling figure (Gokul) — new candidate, not confirmed

- Sujatha: "Gokul had done a modeling to show how the CBD will intracellularly bind to the receptor... so we can maybe put that in, I can ask him."
- **The reviewer question it answers:** CB<sub>2</sub> is transmembrane with a cytoplasmic-side binding site, so "people will always be like, oh, how is it binding outside?" The model shows binding is possible once internalized — which also dovetails with the conjugate's uptake-dependent mechanism.
- **Claim ceiling stated in the room:** Durgadas called it evidence; Sujatha corrected him — "this is also not direct evidence, this is simulation, that is it." Any caption must say simulation.
- **Status: candidate.** Sujatha will ask; nothing has been provided. Do not build a placeholder panel for it yet.

## 2.5 Framing narrowed

- "This is not a pain paper, this is a CBD paper." / "We are saying this is a compound, this is a paper about GD-CBD. That's it."
- The claim set as Sujatha stated it: a GD-CBD compound that is **a better CB<sub>2</sub> agonist than free CBD**, **better formulated and more soluble**, usable across models, demonstrated in **two examples** — pain and seizures.
- **Explicit ceiling on ambition:** "this is not something that we will develop for acute pain... we shouldn't be hashing it too much for acute pain," "let's not beat the acute pain model more than it's already beaten," and the same for acute seizures. The forward path is the grant and chronic models (chronic pain; TLE or a Dravet-type model for seizures).
- **How this differs from the current plan document.** `GD-CBD_PUBLICATION_PLAN_2026-10-09.md`'s strategy section is built on a different unifying claim: "GD-CBD reduces inflammatory markers and disease phenotypes in two models," with inflammation as the throughline and a matched cytokine panel in both species (that was the v2 change, 2026-10-09). The 2 Nov framing replaces inflammation with **CB<sub>2</sub> engagement plus formulation** as the throughline; inflammation becomes an in vitro efficacy readout, not the paper's spine. That is a real framing change to the plan document, not a wording tweak — recommend making it explicitly, with the reason, rather than leaving two framings in the repo.
- The plan's "Chronic-pain relevance beyond one Discussion sentence" claim-to-avoid is **reinforced**, not loosened, by this meeting.

# 3. Figures already built in this repo that this meeting affects

Checked against `figures/mockups/`:

| Built artifact | What it is | What 2 Nov does to it |
|:---|:---|:---|
| **`fig4_composite.png` panels g and h** (`build_fig4_composite.py`) | Hepatic transaminases (ALT/AST) from terminal serum; open-field locomotor activity. Added 2026-10-15 to pre-empt CBD-field safety questions | **Recommend cutting both.** The PI meeting settled against showing toxicity at all. Keeping an ALT/AST panel signals a safety arm the paper is not making and, on Sujatha's reasoning, cannot support with acute dosing. Both become one-line Limitations statements — which the plan document already drafts. This is a real cut to a built figure: flagged, not done. |
| **Candidate "Figure 6 Toxicity/Safety"** (proposed in `INTEGRATION_PLAN_2026-10-16.md` §4 as a rebuild: 738/2460 mg/kg oral, healthy animals, rotarod, bilirubin) | Never built — it was a recommendation pending a go-ahead | **Do not build.** Settled against. The 16 Oct three-option framing (main figure / supplement-only / Discussion-only) collapses to the third option. |
| **`fig6_biodistribution.png`** (`build_fig_bio_mock.py`) | Titled "Biodistribution of Cy5-GD-CBD," panel a describes the 5-rat Cy5-GD-CBD dosing design with vehicle controls | **Needs rebuild, not a caption fix.** The compound is GD-Cy5, the material is existing flank-incision cryosections, the design is "pick a few sections, n=3, plus a no-dendrimer control," and there is no new dosing study to describe. Panel a is now wrong about the real design, which is the one thing it was marked **Have** for. |
| **`fig1_box_layout.png` panel 1e** (`build_fig1_mock.py`) | Hemocompatibility / complement activation (hemolysis, C3a, platelet activation), GD alone vs GD-CBD | **Flag, do not assume.** This is dendrimer hemocompatibility, a different question from CBD toxicity, and it was **not discussed on 2 Nov**. But it is this repo's own anticipatory addition (the 16 Oct plan §2 already noted it has no counterpart in the real plan), and it sits uneasily next to a paper that has just decided not to make safety claims. Recommend asking, not cutting on inference. |
| **`fig5_box_layout.png`** (cytokines across indications) | Pain + epilepsy cytokine dot plots, combined summary | **Cut recommendation from 16 Oct §5 stands and is now better supported.** 2 Nov puts cytokines where the 16 Oct plan said they belonged — as the efficacy readout inside the in vitro figure, on one MSD plate, one species. Nothing in this meeting asks for a cross-indication marker figure, and the paper's throughline is no longer inflammation (§2.5). |
| **`fig2_box_layout.png`** (TNF-α panel, CB<sub>1</sub>/CB<sub>2</sub> dose-response, HU-331 chromatogram) | Current in vitro figure | **Scope changes, direction confirmed.** Microglia confirmed. CB<sub>2</sub> (not CB<sub>1</sub>/CB<sub>2</sub>) is where the discussion now lives, with more concentration points coming. New required content: the CB<sub>2</sub>-overexpression-after-insult panel(s) (§2.1), which must precede the efficacy readout narratively. HU-331 remains unmentioned by anyone outside this repo. |
| **`fig3_real.py` / Figure 3 (epilepsy)** | Collaborator's real data, 8 panels | **Content unchanged; n will grow** (3-4 more per group, excluding the partial batch). Candidate new content: a CB<sub>2</sub> stain on pilocarpine sections (§2.1). The existing caption hedge ("not the final n") is still correct. |

# 4. Animal numbers: mismatches to resolve, not to assume away

The current plan and this meeting are **not describing the same cohort**, and the difference should be settled explicitly:

| | `GD-CBD_PUBLICATION_PLAN_2026-10-09.md` | 2 Nov meeting |
|:---|:---|:---|
| Flank-incision efficacy groups | **GD-CBD 4 / vehicle 3 / free CBD 2** (9 rats), fixed in v2 after explicit deliberation | Read in the room as **3 / 3 / 3** ("3 free CBD, 3 CBD alone, and 3 saline, right? So it's 9 animals") |
| Target n | 9 total for the cohort; 16 Oct recorded a **pooled n=9** target for the GD-CBD arm | **Add about 2 more animals per group**, to allow dropping non-responders: "you just need to add 2 more animals per group" |
| Group balance | Vehicle deliberately given the larger n as primary comparator; free CBD the smaller n | **More GD-CBD than the others is accepted**, on formulation grounds: Preeti — "we will have higher number of GD-CBD animals here, so that's our forever problem"; Sujatha — "Fine, just do it then" |
| Free CBD in the new cohort | n=2, planned | **Optional.** Sujatha would not bother given formulation difficulty; the historical free-CBD data "looks pretty tight" |
| Other rats in the 21-rat order | 6 satellite (markers) + 5 biodistribution + 1 spare | **The 5 biodistribution rats have no study to be in** (§1), and the 6 satellite marker rats feed a figure now recommended for cutting (§3) |

**Recommendations:**
- **Reconcile 4/3/2 vs 3/3/3 before the surgery date**, and state which it is. The plan's reasoning for 4/3/2 (vehicle as primary comparator) is sound and was not argued against — it simply was not what was read off the screen.
- **"Add 2 more per group" is an instruction, not a number.** Sujatha herself noted the extra saline load makes it "a lot of animals." Decide the actual arm sizes and write them into the plan.
- **Dropping non-responders needs a prespecified rule.** The stated purpose of the extra animals is "a little room to be able to toss out one," and "you pick the 2 that seem to be the most responsive" — that is selection on outcome unless the exclusion criterion is written down before unblinding. The plan already has a responder definition and a frozen-script discipline; use them. This is the one item here where following the meeting's words loosely would damage the paper.
- **Unequal group sizes are fine and now sanctioned** — but the reason (formulation-driven losses in the GD-CBD arm) belongs in Methods, since it is also the reason the arm needs a cushion.
- **Reallocate or cancel the 5 biodistribution rats** rather than leaving them in the order with no design attached.
- **Verify the historical free-CBD n.** Sujatha read 6-and-6 off the Prism file; Spencer thinks his free-CBD n is lower and will check. The plan's "n=6 historical at this dose" for free CBD rests on that number.

# 5. Timeline

- **Target restated:** "I think we can have a decent outline and get the paper ready by December hopefully." Consistent with the plan's 2026-12-29 submission target, and softer than the ~1-month push the 16 Oct record logged. The 16 Oct Risks-row recommendation about that tension still applies; this meeting does not resolve it, it just does not repeat it.
- **Schedule check:** the plan has surgery on 11-04 after habituation 10-28 to 11-03. On 11-02 Spencer said "They're here, I'm starting habituation," and separately described baseline as taken "after like a week of habituation." Those do not obviously fit together. **Flag:** confirm the real habituation window and surgery date before treating the plan's downstream dates (Gate 3 on 11-14) as live.
- **Open risk raised by Sujatha:** the new batch has binding, TNF-α and qualitative release confirmed, but **not the week-long release curve** — "How can you do the experiments if we haven't tested it?" The rats are already in habituation. Worth a plan Risks row.

# 6. Recommended order of operations

**A. Low-risk, confirm-only — safe to do now (plan-document and caption edits, no figure rebuilds):**
1. `GD-CBD_PUBLICATION_PLAN_2026-10-09.md`: record the settled items from §1 — biodistribution is GD-Cy5 on existing material, IVIS out, no SE biodistribution, no toxicity figure, microglia confirmed, liver metabolism confirmed. These are status changes, not new content.
2. Same document: change the strategy framing from the inflammation throughline to the CB<sub>2</sub>-plus-formulation framing (§2.5), with the reason, as a dated change-history row. Add "paw incision / paw edema: cut" where that model currently sits under "Do not do now."
3. Add the analysis-plan addendum **before this cohort unblinds**: slope from baseline to 72 h, per animal, as a prespecified secondary readout; AUC 24-168 h stays primary; note the 120-h-vs-168-h question without changing the window (§2.2).
4. Write down the non-responder exclusion rule and the final arm sizes (§4), and reconcile 4/3/2 vs 3/3/3.
5. Add Risks rows: new-batch release curve not yet run; habituation/surgery date mismatch; free-CBD historical n unverified.
6. Ask-and-confirm list (one message, not a work item): does Gokul's modeling figure exist; do the n=3 GD-Cy5 flank sections and a no-dendrimer control exist; where is the tissue (Milan); is the existing AUC per animal.

**B. Needs a go-ahead — cuts to things already built:**
7. **Cut Figure 4 panels g and h** (ALT/AST, open-field). Settled against by the meeting, but this is deleting built mock panels and reflowing the composite — confirm first.
8. **Cut Figure 5** (cytokines across indications), per the 16 Oct recommendation now better supported, folding cytokine readouts into the in vitro figure instead.
9. **Decide on Figure 1e** (hemocompatibility). Not discussed on 2 Nov; do not cut on inference. Ask.

**C. Needs a go-ahead — rebuilds:**
10. **Rebuild Figure 6 (biodistribution)** around GD-Cy5 on existing flank-incision sections: n=3, representative DRG neuron/glia localization, a no-dendrimer negative control, no IVIS, no new dosing design. Panel a needs rewriting, not relabeling, and its **Have** status drops until the real design is written down.
11. **Decide where the CB<sub>2</sub>-overexpression content lives** (§2.1) — recommended as one cross-model panel row rather than scattered across three figures — then build it as Box panels.
12. **Restructure the in vitro figure** around the confirmed scope: CB<sub>2</sub> overexpression after insult first, then efficacy (cytokines, one species, one MSD plate), with the improved CB<sub>2</sub> binding curve once the extra concentration points are in.
13. **Deliverable to request, not to build:** the tissue-collection table Sujatha asked for (what was collected, status, sectioned or not, where it is). The biodistribution figure cannot be rebuilt honestly without it.

**Not recommended:** building any placeholder for the Gokul modeling figure (§2.4) until it is provided, and renumbering figures again. The 16 Oct plan's proposed renumber (3→4, 4→5, biodistribution → a numbered Figure 3) is still unexecuted; doing it in the same pass as these cuts and rebuilds would make the diff unreviewable. Renumber once, after the figure set stops changing.
