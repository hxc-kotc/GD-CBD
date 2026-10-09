---
title: "GD-CBD publication plan, v2"
subtitle: "Prepared 2026-10-09. Target: submission by 2026-12-29."
---

# Read first

- **Strategy:** a combined epilepsy-plus-pain paper built on an **inflammation** story, with a pain-only short report as the fallback. The other PIs' approval on the combined paper is still needed.
- **Pain dataset:** two original cohorts (n=6 per arm, 3 mg/kg IP) showed the effect. A later 40 mg/kg cohort was partially positive. Other cohorts did not reproduce it. Methods were varied and then returned to the original von Frey protocol, and the effect still did not return with other preparations.
- **The new cohort is the third replicate** (three cohorts, two preparations, preparation labels to be confirmed). It is the first with independent material.
- **Characterization did not predict outcome.** The dendrimer masks CBD in the NMR, so the in vitro anti-inflammatory activity is the best available quality evidence. It does not prove the batch will work.
- **Cohort size is small:** 9 rats. Results are descriptive at the cohort level, and the paper leans on the effect size, consistency and the pooled estimate.
- **Free CBD at 3 mg/kg IP has been reported to reduce incision allodynia by other labs** (see section 7). The paper's claim is duration and magnitude after a single dose, not that free CBD is inactive.

# 1. Publication strategy

**Default: combined paper.** Unifying story: GD-CBD reduces inflammatory markers and disease phenotypes in two models, with the same cytokine panel measured in both.

**What the combined paper needs**

- **Same marker panel, same cytokines** (TNF-α, IL-6, IL-1β, IL-10) across epilepsy (mouse) and pain (rat) tissue and in vitro.
- **Epilepsy data lock** by Nov 6. The collaborator's dataset covers biochemical data and several seizure measures.
- **Other PIs' approval** on the combined paper, requested Monday and confirmed by Oct 30.
- **Neutral title** until the marker data are in.

| Pain cohort result | Paper |
|:-------------------------|:----------------------------------------------------|
| **Confirmed (R1)** or **consistent (R2)** | **Combined paper.** Pain is one efficacy figure, exploratory in tone. |
| **Not confirmed** | **Epilepsy-led paper** with chemistry and in vitro. No pain efficacy claim. Pain cohorts stay in the data record. |
| Combined paper not approved by the PIs | **Pain-only short report**, restricted claims. |

Decide at Gate 3 (Nov 13).

# 2. Minimum viable package

| Module | Must have | Nice to have | Do not do now |
|:------------|:-------------------------------|:-------------------|:--------------------|
| **Chemistry and in vitro** | Batch 4 identity: lot, CBD vial, loading (about 10% expected), free CBD %, purity, size, release. THP-1 panel (TNF-α, IL-6, IL-1β, IL-10) with a **viability readout on every plate**. Head-to-head with the original material (use existing data if available). GD alone and free CBD on the same plates. CB<sub>1</sub> and CB<sub>2</sub> assays, GD-CBD vs free CBD. HU-331 spike control. LC-MS of the CBD starting vials (Cayman vial #1 vs #2, any retained Dalton CBD). | Any assay on a failed batch, if retained. | GPR55/PPAR-γ/TRP panels, microsomes, DDI, new analytical method development. |
| **Flank incision** | One concurrent cohort, 9 rats, plus a 72 h satellite marker group of 6. | Bump-up options below. | 30 mg/kg arm, healthy GD-CBD arm, paw edema, gait, thermal, guarding, other pain models, oral CBD. |
| **Biodistribution** | Level 1, 5 rats, only if Cy5 QC passes. | Level 2 and 3 additions below. | Chronic-model biodistribution, mouse work. |

- **Dendrimer-only group in vivo: not essential.** GD alone goes on the in vitro plates, and the limitation is stated. The claim is "GD-CBD vs vehicle and free CBD", never "CBD is the active component".
- **CB<sub>1</sub> and CB<sub>2</sub> interpretation:** CBD is a weak ligand at these receptors (background knowledge, to be verified), and the earlier CB<sub>2</sub> EC<sub>50</sub> was about 7.8 µM. The assays show what the conjugate retains or loses, not a receptor mechanism.
- **HU-331 and viability:** HU-331 forms readily from CBD and is a common impurity in isolates. It is a cytotoxic quinone (background knowledge). A cytotoxic compound lowers cytokine release by killing cells, so every cytokine plate needs a viability readout.
- **Starting-material LC-MS** sidesteps the NMR masking because no dendrimer is present. Vial #1 has aged since use, so a positive result is suggestive, not proof.

# 3. Final flank-incision cohort

**Groups (9 rats): GD-CBD 4, injured vehicle 3, free CBD 3 mg/kg 2.** Free CBD is secondary and already has n=6 historical at this dose. Vehicle is the primary comparator and the check that this cohort behaved like a pain model.

- **Dose:** GD-CBD at 3 mg/kg CBD-equivalent, IP, immediately after closure, in saline + 5% ACN. Same vehicle in every arm.
- **Match the original cohorts:** sex, age and weight at surgery, supplier, operator, filaments, up-down method, and the original von Frey technique.
- **Blinding:** the chemistry team code-labels syringes. Randomize stratified by cage. Testers never see the key. Wound photos scored blind. Analysis script frozen before unblinding.
- **Time points:** baseline on the two days before surgery, then 2, 4, 6 h, then daily from 24 to 168 h. Ropivacaine in vehicle animals after the final test. Reconcile the volume (200 vs 400 µL).
- **Historical vehicle animals:** reference band only, from cohorts using the original method, sex and vehicle. They do not replace the concurrent vehicle.

## Analysis (fixed before unblinding)

- **Primary:** per-animal AUC from 24 to 168 h, expressed as a percent of that animal's baseline. Rank-based exact comparison of GD-CBD vs vehicle within the cohort. Pooled across cohorts with cohort as a stratum.
- **Secondary:** per-time-point comparisons with a multiple-comparison correction (descriptive at this n). Full time course shown. The 2 to 6 h window reported separately.
- **Backup:** absolute grams.
- **Sensitivity:** mixed model on log-transformed thresholds, leave-one-cohort-out, responder analysis (at least 50% of baseline recovered at 3 or more consecutive time points), censoring at the filament ceiling.

## Success criteria

- **R1 (replication):** GD-CBD/vehicle AUC ratio at or above 2 with exact one-sided p at or below 0.05. At 4 vs 3, only complete separation reaches this (p=1/35=0.029; one overlap gives 0.057).
- **R2 (consistency):** same direction as the original cohorts, with the effect estimate overlapping theirs.
- **R1 met:** "replicated with an independent preparation". **R2 only:** "consistent, not confirmed". **Neither:** failure to replicate. Section 1 applies.

## Pooling and wording

- **Unit of replication is the cohort.** Rats in a cohort share a preparation, a day and a tester, so three cohorts count as three tests, not 20 rats.
- **Tiers:** Tier 1 is the new cohort alone. Tier 2 is the pooled estimate with a per-cohort forest plot. Tier 3 (supplement) is every GD-CBD cohort, with dose, preparation, method, sex, age, baseline and outcome.
- **Methods wording:** "GD-CBD was prepared from Cayman CBD in independent syntheses (preparation labels to be confirmed). Efficacy was not reproduced with other preparations (Table S1)."

## Bump-up options (decide before the order, or add rats later if work allows)

| Option | Extra rats | What it buys |
|:----------------------------|:-------|:-----------------------------------------|
| Vehicle 3 to 4, free CBD 2 to 3 | +2 | Better control comparison. |
| GD-CBD 4 to 5 | +1 | Protects against a non-responder or lost animal. |
| Satellite 3 to 4 per arm | +2 | Firmer marker estimates. |
| Biodistribution: add uninjured Cy5-GD-CBD (n=3) | +3 | Whole-body injury effect. |
| Biodistribution: add an injured 3 h group (n=3) | +3 | Terminal kinetics. |

# 4. Inflammatory markers in the pain cohort

- **Satellite 72 h group (6 rats):** GD-CBD n=3 and vehicle n=3, unlabeled, operated and dosed on Nov 3, sampled Fri Nov 6. This is at the peak of the effect, which day-7 tissue may miss.
- **Day-7 tissue from the main cohort:** wound skin (histology) and plasma. Flash-freeze contralateral skin, ipsilateral and contralateral DRG, and spinal cord. Run the panel on wound skin and plasma first. Run the rest only if informative.
- **Panel:** TNF-α, IL-6, IL-1β, IL-10, same platform as the epilepsy and in vitro work.
- **Interpretation:** n=3 per group is descriptive. Present as "consistent with", never mechanism.

# 5. Biodistribution (conditional)

## Go/no-go QC (checkpoint Oct 30; material in hand by Nov 6)

1. **Free dye** at or below 2% of total fluorescence after purification, rechecked after 24 h in serum at 37 °C.
2. **Labeling:** at most about 1 Cy5 per dendrimer, checked by HPLC against unlabeled.
3. **Particle behavior:** size and zeta within error of unlabeled GD-CBD.
4. **Signal:** a spiked tissue-homogenate dilution series is linear and well above background.
5. **Activity:** TNF-α activity retained within about 3-fold of unlabeled.
6. **Lineage:** made from the Batch 4 conjugate.

Any failure means omit biodistribution.

## Design: Level 1, 5 rats

- **Injured + Cy5-GD-CBD, terminal at 24 h, n=3.** **Injured + vehicle, n=2** (background). Dose Wed Nov 11, terminal Thu Nov 12.
- **Internal control:** the contralateral side of each injured animal. It supports "higher on the injured side than the contralateral side in the same animal". It cannot separate real uptake from the leakiness any wound gives any nanoparticle, so "targeted" stays off the claims list.
- **Readouts:** tissue measurements are primary: homogenate fluorescence against a standard curve, plus sections. Live whole-body IVIS at 1, 3, 6 h is optional kinetics only.
- **DRG:** collect ipsilateral and contralateral DRG (T13 to L2) from all 5 animals, including vehicle, for background. Freeze. Process only if wound and spinal cord signal is positive and neuron evidence is wanted.
- **n=3** is the floor: "seen in 3 of 3 animals", not statistics.
- **Material:** about 9 mg of conjugate per rat at about 10% loading and 300 g (planning arithmetic, confirm against Batch 4 loading). About 36 mg for the efficacy cohort and 27 mg for the labeled animals.

## Claims by outcome

- **Strong** (injured side higher in 3 of 3, above vehicle, QC clean): "Cy5 signal was higher at the injured site than the contralateral side." The label tracks the dendrimer, not CBD.
- **Modest:** "consistent with renal clearance, with a small injured-side excess". No targeting claim.
- **Negative or uninterpretable:** omit, or one sentence in Limitations.

**Omit entirely if** QC fails by Oct 30, material is not in hand by Nov 6, or imaging can't finish by Nov 27.

# 6. Timeline and actions

Order: Tue Oct 13. Arrival: Tue Oct 20. Facility acclimatization: Oct 20 to 27. Habituation: Oct 27 to Nov 2. Surgery: Tue Nov 3.

| Dates | Who | Action |
|:-----------|:----------|:--------------------------------------------------|
| **By Mon Oct 12** | You | Talk to the PI. Confirm rat age and weight at surgery from the original cohorts. Confirm habituation length against the original protocol (draft says 10 days, outline 8). Ask the other PIs about the combined paper. |
| **Tue Oct 13** | You | **Order 21 rats** (9 efficacy, 6 satellite, 5 biodistribution, 1 spare), age specified at surgery. |
| **By Oct 16** | You | One-page analysis plan frozen: primary endpoint, script, blinding key held by the chemist. Agree the cytokine panel and platform with the epilepsy collaborator. |
| **By Oct 23** | Chemist | Batch 4 identity (loading, free CBD, size, release). Coded per-rat dose aliquots. |
| **By Oct 23** | In vitro | Cytokine panel with viability, GD alone, free CBD, head-to-head with original, CB<sub>1</sub>/CB<sub>2</sub>, HU-331 spike. LC-MS on CBD starting vials. |
| **Oct 30** | Chemist | Cy5 QC checkpoint. Other PIs' approval on the combined paper confirmed. |
| **Nov 3** | In vivo | Surgery and dosing: main cohort and satellite. |
| **Nov 6** | In vivo | 72 h behavior read. Satellite tissue sampled. Epilepsy data lock. |
| **Nov 10 to 11** | In vivo | 168 h read, ropivacaine, tissue collection. |
| **Nov 11 to 12** | In vivo | Biodistribution dosing (Nov 11) and terminal samples (Nov 12), if QC passed. |
| **Nov 12 to 13** | You | Unblind, run the frozen script. **Gate 3 Nov 13:** pain result, track decision. |
| **Nov 13 to 27** | You | Marker panel runs. Biodistribution analysis. **Gate 4 Nov 27:** biodistribution in or out. Draft figures and Methods. |
| **Nov 27 to Dec 11** | You | Full draft. Integrate epilepsy figure. Table S1. |
| **Dec 11 to 18** | PIs | Review. |
| **Dec 18 to 29** | You | Revise, check patent status, submit. |

If the cohort fails at Gate 3, there is no replacement cohort.

# 7. Manuscript framing

## Working titles (keep neutral until marker data are in)

- *Glucose dendrimer conjugation of cannabidiol attenuates incision-evoked mechanical hypersensitivity in rats*
- *A glucose dendrimer-cannabidiol conjugate in models of seizures and postoperative pain*

## Main figures

1. Chemistry: structure, loading, size, purity, release.
2. In vitro: cytokine panel with viability, CB<sub>1</sub>/CB<sub>2</sub>, comparison with free CBD and GD.
3. Epilepsy (the collaborator's figure).
4. Pain efficacy: time course with individual animals, AUC, per-cohort forest plot.
5. Inflammatory markers across both indications (same panel).

**Supplement:** Table S1 (all GD-CBD cohorts and preparations), Table S2 (batch QC), raw per-animal data and script, surgical technique, spectra, sensitivity analyses, biodistribution if it passes.

## Discussion framing from the literature check

Search summaries only; verify in full text before citing.

- **Other labs report free CBD at 3 mg/kg IP reducing incision allodynia:** dorsum incision in male Sprague-Dawley rats (PMC12844942), plantar incision in Wistar rats (2023 Behavioural Brain Research, with estrous-dependent effects in females; 2017 Frontiers in Pharmacology). Frame the finding as "no sustained effect with dose-matched free CBD in our formulation" and show the 2 to 6 h window honestly.
- **Female-only is a bigger limitation than it looks:** the 2023 study found estrous-phase dependence.
- **No peer-reviewed dendrimer-CBD pain paper found.** The lab's public conference slides already claim five days of reduced post-operative pain sensitivity and mention a filed patent. Keep the paper consistent with them.
- **No published DRG or pain-model biodistribution found** for glucose dendrimers. Sharma 2024 supports hyperexcitable-neuron uptake in epilepsy only.
- **HU-331:** a documented CBD impurity, light sensitive, source-dependent. Plausible, not shown for these lots.

## Claims to avoid

- **Neuronal targeting** or "targeted delivery".
- **Localization causing analgesia.**
- **Intact conjugate retention.** The label follows the dendrimer.
- **"CBD is the active component".**
- **Dose-sparing multiples.** The 30 mg/kg free CBD arm is n=1.
- **Rapid onset, no sedation, "durable", "established".**
- **Reproducibility across batches.**
- **Receptor mechanism** from CB<sub>1</sub>/CB<sub>2</sub> data.
- **Inflammation as a mechanism** for analgesia or anti-seizure effect. Markers are associative.
- **Chronic-pain relevance** beyond one Discussion sentence.

## Unsupported claims in existing documents to fix

- **R01:** "onset within 2 h", "no sedation", flank-incision DRG labeling.
- **Draft:** free CBD dose-response, "three cohorts", paw thickness endpoint, plantar vs flank, female vs male, "established".

# 8. Risks and mitigation

| Concern | Shortest credible mitigation | Limitation statement |
|:-------------|:-----------------------------|:---------------------------|
| **Small n** | Individual animals, effect sizes with CIs, responder analysis, no definitive pooled p. | "Group sizes were small." |
| **Batch history** | Table S1 with every cohort and preparation. | "Efficacy differed between preparations; cause not established." |
| **Reproducibility** | Prespecified replication with a new preparation; report either result. | "One independent preparation was tested." |
| **No dendrimer-only control in vivo** | GD alone on in vitro plates. Narrow claim. | "A carrier-only arm was not included in vivo." |
| **Limited mechanism** | Restrict to markers and in vitro data. | "Mechanism was not tested." |
| **Single sex** | State sex in Methods and abstract. | "Only female rats were used; estrous phase was not tracked." |
| **Biodistribution** | Omit unless QC passes. | "Tissue distribution was not established." |
| **Flank vs chronic pain** | One sentence. | "Chronic efficacy was not tested." |
| **ACN vehicle** | Identical vehicle in all arms. | "5% acetonitrile was used for free CBD solubility." |
| **Free CBD formulation** | Report vehicle and appearance. | "Free CBD may have had limited bioavailability as a suspension." |
| **Oxidation / HU-331** | Starting-material LC-MS and viability controls. | "Oxidation state in the conjugate was not analytically resolved." |
| **Day-7 tissue too late** | 72 h satellite group. | "Markers were measured at defined time points only." |
| **Cross-species markers** | Same cytokines, state species. | "Epilepsy tissue was mouse; pain tissue was rat." |

# Open items

- **Rats:** age and weight at surgery of the original cohorts, and habituation length.
- **Batch 4 loading** (about 10% expected).
- **PI approvals:** your PI and the other PIs, for the combined paper.
- **Epilepsy:** data lock date, and the marker panel and platform agreed.
- **Retained material:** whether any failed batch or the original has material left for the in vitro comparison.
- **Release and CB<sub>1</sub>/CB<sub>2</sub> data:** which exist already.
- **Patent status** before submission.
