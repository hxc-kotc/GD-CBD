# PI data/figure working session, 2 Nov 2026 — GD-CBD

Source: diarized transcript of a working session (Spencer, Sujatha, Durgadas, Preeti; Kristen joined briefly on an unrelated item). No slides — the session was a screen-share walkthrough of real data files, figure by figure. GD-CBD only; nothing in this record covers other programs.

**Speaker-label correction:** the transcript labels one speaker "Kannan / Speaker A." That label is wrong. **Every line attributed to Speaker A in the source file is Sujatha.** All attributions below use the corrected name. Other labels (Durgadas/B, Spencer/C, Preeti/D, Kristen/E) are as given.

**Audited 2026-11-03** by an independent session (Opus) against `transcript_raw.txt` in this folder: speaker attribution and most quotes checked out; two substantive gaps (the 3 existing paw-incision rats, the Lin Peng figure-quality directive) and several stitched/reordered quotes were found and corrected below. See git history for the pre-audit version if needed.

---

## 1. Bottom line

- **Framing narrowed, deliberately.** Sujatha: "this is not a pain paper, this is a CBD paper," and "we are saying this is a compound, this is a paper about GD-CBD. That's it." The claim set: GD-CBD is a better CB<sub>2</sub> agonist than free CBD, better formulated and more soluble, and works in two commonly used models (incision pain, seizures) as examples.
- **Paw incision / paw edema model: cut** — despite 3 existing animals already on hand ("We have the 3 paw incision animals already, the rats" — Sujatha). "I think we're going to just nix the paw edema model, paw incision model." A clean version would need a full new cohort beyond what exists. "I really think we have, we have enough of a story here."
- **No toxicity figure.** Durgadas framed the liver work as about stability, not toxicity, in the first place: "we are looking for the stability of not toxicity because CBD won't show any toxicity." Sujatha agreed and extended it: "We are not going to be able to show toxicity with CBD because CBD itself is not that toxic. All of its toxicity are chronic toxicity and so we're not going to be able to show that."
- **Figure quality standard set explicitly.** Sujatha, after seeing Spencer's placeholder mock-ups: "those graphs are ugly, okay? You're not going to make those... They're not going to look like Excel graphs." **Lin Peng's papers are the named model** for how figures should look (nanomedicine/dendrimer field, not pain-specific — "it doesn't matter whether it's pain space or not... it's only to see how the pictures are going to look"). Preeti to share the paper.
- **Biodistribution scope settled small.** Existing GD-Cy5 images from the flank-incision model only. No SE biodistribution ("we've already done it in 10 different ways in the SE"). No new large study — Spencer: "At one point I think we were planning like a 21-animal biodistribution." Sujatha: "No, no. Never." **IVIS out of the paper entirely:** "We're struggling with IVIS, let's take that out."
- **New required throughline: CB<sub>2</sub> overexpression after insult, in each system used.** In vitro (LPS-microglia, glutamate-injured neurons), DRG (neurons and glia after incision), brain (neurons after seizures). "In some fashion between the 3 models we should kind of show" it. This is what makes a CB<sub>2</sub>-agonist conjugate make sense: "we have to show that the target is there and we're going after the target."
- **New analysis for the flank-incision data:** per-animal slope from baseline to 72 h, added alongside the existing time course and AUC. 72 h is where roughly half the conjugated drug has released.
- **Target:** "I think we can have a decent outline and get the paper ready by December hopefully."

## 2. Decisions made

| Item | Decision | Who |
|---|---|---|
| Paw incision / paw edema model | Cut from the paper, not even supporting, despite 3 existing animals on hand. Durgadas: "the paw edema, are we adding it supporting?" Sujatha: "No." | Sujatha |
| Toxicity / safety data | Not pursued. The liver work is framed as stability (Durgadas's framing, Sujatha agreed), not toxicity; CBD's toxicity is chronic and this design cannot show it. | Durgadas framed it, Sujatha confirmed |
| Figure quality standard | Follow Lin Peng's papers as the visual model; current placeholder graphs explicitly rejected | Sujatha |
| IVIS | Out of the paper | Preeti proposed, Sujatha agreed |
| Biodistribution compound | GD-Cy5, existing flank-incision material. Not GD-CBD-Cy5, no new dosing study | Sujatha |
| SE biodistribution | Not shown — already published several ways | Sujatha |
| In vitro cell type | Microglia only. "I would not do macrophage and microglia. Pick just one" | Sujatha |
| CB<sub>2</sub> overexpression | Required in each model system before the efficacy readout | Sujatha |
| Slope-to-72h analysis | Added as an extra graph; AUC plots stay | Sujatha, Spencer agreed |
| Liver microsome metabolism | Keep, "especially CBD" | Preeti raised, Sujatha agreed |
| Flank-incision cohort | Add about 2 more animals per group; unequal group sizes accepted | Sujatha |
| Delayed-therapy seizure groups | Not in this paper; saved for chronic/TLE models | Sujatha |

## 3. CB<sub>2</sub> binding and potency

- **Durgadas is repeating the CB<sub>2</sub> binding with more concentration points** next week because the current curve is thin. Sujatha: "Is this enough number of points? No, no. We need to do more."
- **GD-CBD is about 6-fold more potent than free CBD on a drug basis.** Sujatha read the EC<sub>50</sub> for free CBD off the plot as 80 and noted GD-CBD is "about 6-fold better... on the drug basis," adding that on a conjugate basis it would look better still. Durgadas confirmed the comparison is drug basis, not conjugate basis.
- **THC is the positive control.** Durgadas: THC binds CB<sub>1</sub> and CB<sub>2</sub> at nanomolar potency, which is also why it carries the psychoactive effects CBD does not.
- **In vitro potency is millimolar, and that is accepted.** Durgadas: GD-CBD had to be used up to 0.5-10 mM before LPS-driven inflammation came back to control; 10 mM is 3.4 mg/mL on a drug basis, about 1 mg/mL already gives "some good efficacy." Sujatha: "Millimolar potency is less exciting, but that is fine, it is what it is." Reproduced twice, with the current batch.
- **Framing of the mechanism:** "even though it's a weak CB<sub>2</sub> agonist, it's better than CBD alone." Also Sujatha on why CBD at all: a plant-derived weak agonist that conjugation improves "may fly better" than a synthetic cannabinoid — the lab's earlier CB<sub>2</sub>-specific agonist (HU-series) failed in both the pain and CP work. The answer to "why CBD," which reviewers have asked repeatedly, is solubility and formulation: "that's what we are completely overcoming... we're also improving the CB<sub>2</sub> activity."

## 4. In vitro plan (LPS / microglia)

- **Microglia, not macrophages.** Sujatha: "I would not do macrophage and microglia. Pick just one." Durgadas: "the microglia would be right." On the pain-model objection that macrophages are the peripheral cell: "In the DRG, they are like microglia... people can consider them as macrophages, it doesn't matter."
- **Cell line is open:** HMC3 or BV2 both acceptable. **One species across the panel** so a single MSD plate can run all cytokines at once.
- **CB<sub>2</sub> overexpression must be shown first, in both cell systems.** "For the microglia, the LPS study is fine, but we need to show that CB<sub>2</sub> is overexpressed with LPS... we will need to do a Western or staining or something." And: "The first thing that we need to show is that CB<sub>2</sub> expression is going up in both of these cell lines with the insult" — microglia with LPS, neurons (HT-22) with glutamate. Either Western or immunostaining is fine. Rationale: "In some fashion, we have to show that the CB<sub>2</sub> expression was low before it got exposed to LPS or glutamate, and after exposure it went up, and therefore our treatment makes sense."
- Efficacy readout after that: inflammatory cytokines (TNF-α and the rest of the panel) in both cell types.
- **Weight of the paper:** "it should be heavy quite a bit on the in vitro stuff."
- **Liver metabolism retained** — free CBD vs GD-CBD, "especially CBD."
- **Synthesis figure assigned.** Sujatha, to Durgadas: "So synthesis, you have all of that, right? This is all set for Durga."

## 5. Candidate addition: computational modeling (Gokul)

- Sujatha: "I can ask Gokul to give that. Gokul had done a modeling to show how the CBD will intracellularly bind to the receptor."
- Why it matters: CB<sub>2</sub> is transmembrane with a cytoplasmic-side binding site, so reviewers will ask how a conjugate that has to be internalized binds at all. The model shows binding is possible once internalized.
- **Honesty constraint stated in the room.** Durgadas called it evidence; Sujatha: "No, no, this is also not direct evidence, this is simulation, that is it."
- Status: not confirmed. Sujatha said she would ask him for a figure.

## 6. Flank-incision von Frey walkthrough

### Batch and cohort structure
- The plotted data is two cohorts from the **first chemistry batch**, which Spencer called the best functioning batch "by far" (Dec 2024 and Jan 2025).
- Program-wide: roughly 4-5 chemistry batches and about 8 rat cohorts. The Dalton-sourced batch failed in every model, free drug included, and has been removed from all analyses. A third batch worked partially, at 40 mg/kg.
- **Nesting by formulation was raised and then dropped** because the plotted data is one batch. Sujatha, across two turns: "this is one batch. So, I don't think we need to do batch variability," then, after confirming with Preeti, "Okay, then maybe we won't nest." Reason given against nesting generally: "we might lose power if we nest things."

### Methodology points
- **Baseline = average of the three pre-surgery days**, not the max. Spencer had tested both; Sujatha: "average will be better. I would not — yeah, the max might just give us a false value."
- Connect the baseline to the post-surgery series rather than drawing a separate segment: "you can just connect it up because it's the same animals anyway, because this piece is a bit confusing." Mark surgery and treatment times on the axis.
- Von Frey up-down protocol walked through in detail. The adaptive protocol cannot be retrospectively corrected — Spencer: "you can't retrospectively really change it or like pull a point. So we're kind of stuck with the data that we have." The remaining option is to exclude a whole animal.
- Sujatha asked for **video review of the outlier time points** ("the ones that are off, we need to do an observation to see if the animal is behaving like a little strange"). Spencer has video of every session.
- Log scale was asked about and had already been tried.
- **Treatment timing:** dosed immediately post-surgery — "I give it immediately after the surgery, so like within— the surgery is 10 minutes, I give it at the end of 10 minutes."

### What the data shows
- **Free CBD: an acute effect only, not significant, and highly variable.** Sujatha: "with CBD alone, it's interesting because you have an acute effect." Spencer: "it's highly variable, but yes... there's something."
- **GD-CBD: some acute effect, mostly delayed, durable to about 120 h, not 168 h.** Sujatha: "it doesn't last up to 168, it lasts up to 120 hours is probably what we're going to have to say."
- **Spread is in the wrong group.** Sujatha: "dendrimer is always very tight. Free drug is the one that is not tight usually... I think it is the conjugate." Spencer's working hypothesis: a behavioral effect of the drug making the animals indifferent to the filaments rather than a threshold change.
- Early time points (2.5 h vs 4.5 h) are internally inconsistent in some animals; later time points look cleaner. "It's super behavioral."
- AUC: significance is there with a spread. Error bars shown are SD; Sujatha noted SEM is defensible and "the stats are not going to change anyway."

### Analysis actions
- **Confirm the AUC is per animal** — Sujatha inferred it from the individual dots, Spencer was not certain and the Python version is not easily recoverable. **Recalculate in Prism, share the data file with Preeti** to cross-check.
- **New: per-animal slope, baseline to 72 h.** Rationale from the release data: Durgadas said little drug releases in the first 6 h and about 50% has released by 72 h, which Sujatha took as the sensible cut point. "If we did a slope from baseline to 72 hours, and we compared the slope per animal... all of these guys would be negative and this would be positive." Spencer: "that's a cleaner plot." Kept as an **additional** graph: "We'll still show this, but we'll add that as an extra."
- The 48-96 h window is a plateau.

## 7. Animal numbers

- **Current incoming cohort: 3 per group, 9 animals** (GD-CBD, free CBD, saline). Rats already arrived; Spencer is starting habituation.
- **Add about 2 more animals per group.** Sujatha's reasoning, in the order given: "if you had to toss out some animals, then, you know, we can probably... if you did 4 GD-CBD and, you know, something didn't work and you wanted to toss [one] so you'll have a little stronger number... one way to think about it is actually you just need to add 2 more animals per group. The others look fine." Purpose is explicitly room to drop a non-responder: "you're always going to have some animals that's going to behave weird. So you just want a little room to be able to toss out one."
- **Unequal group sizes are accepted for GD-CBD.** Sujatha first asked for a scientific justification for running more GD-CBD than free CBD; Preeti's answer was the formulation problem ("we will have higher number of GD-CBD animals here, so that's our forever problem"), and Sujatha accepted it: "Fine, just do it then."
- **Free CBD for the new cohort: optional.** Spencer asked whether to run it; Sujatha would not bother given the formulation difficulty, and in the historical data free CBD "looks pretty tight" already. Historical free-CBD n in the flank data needs checking — Spencer thinks it is lower than he had assumed and will go back through the Prism file.
- **Historical paw-incision numbers (now moot, model cut):** n=2 CBD 3 mg/kg, n=3 CBD 0.3 mg/kg, n=1 saline — on top of the 3 existing paw-incision rats noted in §1. Salines are dedicated per paper, not shared; whether Javier's saline animals are shared across papers was an open question Sujatha took on ("Can you check with him? Okay, I text him."). Before settling on cutting the model, Sujatha floated two cheaper fallback designs: "3 CBD and 1 saline for paw incision and get a sense," or "3 CBDs and... 3 salines for paw incision. No need to do free CBD. This is because that's going to be a final confirmatory model" — i.e., even the cheap version was framed as a confirmatory add-on, not a figure in its own right. Neither was adopted; "I think we're going to just nix" it instead (§1).
- **Epilepsy:** the plotted cohort is 6-7 animals; Preeti has at least 3-4 more per group to add, excluding the partially-working batch ("Do we want to add the one that partially worked or no?" — "No"). Sujatha: "why don't we put that in." Delayed-therapy groups (3-4 per group) exist but stay out of this paper.
- **New batch release curve not yet run.** Durgadas has confirmed release qualitatively, binding (IC<sub>50</sub> match), and TNF-α twice, all matching the first batch, but not the week-long release curve. Sujatha flagged the timing: "How can you do the experiments if we haven't tested it?"

## 8. Biodistribution and localization

- **Keep it phenotypic and small, and don't try to cover every model.** "I wouldn't want — I think we should just keep this heavily phenotypic-based," and, on biodistribution specifically, "we don't need to show everything for everybody, okay." Spencer asked whether more sectioning was needed beyond what exists; the answer was no.
- **Use the existing GD-Cy5 flank-incision images** (Javier's). Sujatha confirmed on screen that these are GD-Cy5 alone, not GD-CBD-Cy5, and that they show DRG neurons and DRG glia. "We'll just show that and say it's getting into the DRG neurons, DRG glia." The equivalent grant figure is the better-looking version of the same material.
- **No SE biodistribution:** "we're not going to show biodistribution here because we've already done it in 10 different ways in the SE... it's not going to give us anything more."
- **No new large study:** "At one point I think we were planning like a 21-animal biodistribution." — "No, no. Never."
- **IVIS dropped from the paper.** Preeti: "For the paper, I will take out the IVIS." Sujatha: "We're struggling with IVIS, let's take that out. We'll just keep the rest of it."
- **What is still needed:** n=3 flank-incision animals with GD-Cy5 sections, which Spencer believes exist; a **no-dendrimer negative control** (Preeti suggested staining saline sections from the efficacy animals); and **a table of what tissue was collected, its status, whether sectioned, and where it is.** "Among that we will pick a few, keep the rest available in case a reviewer comes up with a question... We don't have to extensively image, but we should at least get a sense that we are seeing it in the DRG."
- Context on cost: Spencer called the sectioning and imaging the heaviest part of the whole project, heavier than making the model. Sujatha's conclusion: "this is done, so that's why I don't want to add to it and make this more complicated."
- Historical IVIS and skin-imaging attempts failed in two further cohorts despite full-body shaving; the team attributes that to a Cy5 problem.

## 9. The CB<sub>2</sub>-overexpression throughline (new structural ask)

This is the clearest new structural requirement from the meeting, and it cuts across three figures.

- **Why:** the story only closes if the target is shown to be present where the conjugate goes. Sujatha's full version: "the dendrimer goes into DRG neurons and DRG glia. We already have the biodistribution for that. DRG neurons and DRG glia overexpress CB<sub>2</sub> after the incision, or after injury... Same thing for seizures. Neurons are overexpressing CB<sub>2</sub>. So therefore this, which is a stronger CB<sub>2</sub> agonist, works better than CBD. GD-CBD is a stronger CB<sub>2</sub> agonist, so it's working. That's essentially the story."
- **Where:** in vitro (LPS-microglia, glutamate-neurons — Western or stain), the incision model (DRG sections, existing material), the seizure model (pilocarpine sections, stain for CB<sub>2</sub>).
- **Expected localization:** "on the neurons, the DRG neurons, it may not be going up, but it might be going up in the glia, in the macrophages, and the DRG is probably where the CB<sub>2</sub> receptor is going to be overexpressed."
- **Method: staining on existing sections, not new assays.** ELISA was raised and rejected because it averages across the whole tissue: "if you do ELISA, we're showing it in all of the tissue." Also, deliberately low-effort: "don't try to quantify or do too much, just show like an image and say it's more, it's less, that's good enough."
- **Literature evidence is an acceptable fallback, and the paper is not gated on this.** "I don't think the paper has to be held up for it. If you have evidence, if you're able to get literature evidence that CB<sub>2</sub> goes up, then it's fine." But Sujatha's own read is that the published evidence is thin — "there are bits and pieces here and there" — and showing it in these models would mean "the whole story is like completely tied."
- Related note on CB<sub>2</sub> in neurons, raised in the seizure context: Preeti cited expression in a subpopulation of neurons (CA1, CA2, dentate gyrus); Sujatha's framing was simply that seizing neurons overexpress CB<sub>2</sub>, which is enough for the paper's logic without resolving the mechanism.
- **Mechanistic rationale for CB<sub>2</sub> agonism, stated separately:** "It triggers ionic current changes that shifts the cells to its hyperpolarization. So this decreases neuronal excitability. Okay, so then if you give an agonist, that helps the — so it's essentially a protective mechanism."
- **CB<sub>2</sub>/BV2 expression levels are not an efficacy endpoint — made via a cross-project analogy, not a tangent.** On whether BV2 CB<sub>2</sub> levels need to move for the paper's logic to hold: "it's not going to do anything to the BV2 levels. That's not an efficacy endpoint." Sujatha then drew the comparison explicitly to a different project's COX-2 result (Kristen's): "Which is essentially the same thing as the COX-2 that Kristin was showing... it actually doesn't matter... because the ketorolac is there. Even if it goes up, it's binding it. That's not the endpoint. It's just the endpoint is downstream, so it doesn't matter." The COX-2 project itself is out of scope for this record, but this specific exchange is reasoning about the GD-CBD paper's own logic and is included for that reason.

## 10. Scope of the paper going forward

- **Not an acute-pain development program.** "This is not something that we will develop for acute pain... we shouldn't be hashing it too much for acute pain," and "let's not beat the acute pain model more than it's already beaten." Same for seizures: "we're not going to be doing it for acute seizures."
- **Where the ambition goes instead:** the data strengthens the grant and justifies chronic models — chronic pain, and for seizures TLE or a Dravet-type model. "We have provided the justification that we have a compound that works well. That's all we can do now." Spencer was asked to send the data to Sujatha or Kunal for the grant.
- Spencer's own preference, noted but not acted on: he would feel better about the pain side with an on-surgery (paw incision) model. The answer was that this paper does not need it.

## 11. Open or unresolved

- **Is the AUC per animal?** Not confirmed in the meeting. Needs Prism recalculation and Preeti's cross-check.
- **Historical free-CBD n in the flank-incision data.** Spencer thinks it is lower than the 6-and-6 Sujatha read off the Prism file; he will verify.
- **Whether the n=3 GD-Cy5 flank-incision sections and a no-dendrimer control actually exist.** Spencer believes so; the tissue-location question ("you guys are playing hot potato with it") is unresolved and Milan needs to be asked. The collection table is the deliverable that settles it.
- **Whether Gokul's modeling figure will be provided.** Sujatha to ask.
- **Whether the new batch's week-long release curve will be run before or alongside the in vivo cohort.** Not resolved; the rats are already in habituation.
- **Which cell line for the in vitro redo** (HMC3 vs BV2) and whether the whole panel gets redone in one species.
- **Whether Preeti's 48 h microdissected tissue gets an inflammation readout.** She offered; Sujatha agreed it was "not a bad idea" but it was not assigned.
- **Exact added-animal count for the flank cohort** — "about 2 more per group" was the instruction, not a locked number, and Sujatha noted the extra saline load makes it "a lot of animals."
- **December is a hope, not a dated commitment:** "get the paper ready by December hopefully."

## 12. Transcript caveats

- Speaker A is mislabeled "Kannan" throughout the source file and is in fact Sujatha. Corrected everywhere above.
- Several numbers were read aloud off screen-shared plots without units stated (the CB<sub>2</sub> EC<sub>50</sub> "80," the in vitro millimolar-to-mg/mL conversions). Treat them as read-aloud approximations and confirm against the source data before any of them goes in a figure or manuscript. Do not convert between drug-basis and conjugate-basis concentrations from these numbers by hand.
- A few exchanges about cell-line names, tissue custody, and the "HU" CB<sub>2</sub> agonist are partly garbled in the transcript; the conclusions are clear but individual identifiers are not.
- Short exchanges with no bearing on this paper (scheduling, a brief personal aside, a different rabbit study's logistics) are omitted here. The COX-2 exchange is **not** in that category — it is included in §9 because Sujatha uses it as a direct analogy about CB<sub>2</sub>/efficacy-endpoint logic for this paper, even though the COX-2 project itself is unrelated.
