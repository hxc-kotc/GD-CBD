# GD-CBD year-end publication plan (2026-10-09)

Scope: smallest credible package to submit a GD-CBD paper by 2026-12-31. Context only for the GD-nori program (CLAUDE.md: GD-X facts are context, not nori experiments). Sources: `30_SOURCES/internal/cbd/` (nine files, all read in full; the lab-update PDF was read as rendered slides). Second-hand numbers read off slide plots are marked `[plot read]`.

## 0. What the files show

### Bottom line

- **The pain dataset is one positive discovery set (n=6 per arm, 2 cohorts) followed by at least four cohorts that did not replicate.** A paper must say so in a supplement table. It does not have to be the centerpiece.
- **"Fully characterized, looks good" did not predict in vivo outcome.** Batches 2 and 3 passed the same screen as Batch 1 and failed (batch notes). The TNF-α assay "good" on Batch 4 is a go signal, not evidence the batch will work. Prior: 1 of 3 characterized batches worked `[inference]`. Plan for the cohort to fail.
- **n=3 and n=4 per arm have the same power under a rank test, and both are weak.** At the realistic effect (d about 1 to 1.7) any feasible cohort has about 25 to 65 percent power. The cohort is a directional replication, not a confirmation. Claims must be sized to that.
- **No epilepsy data is in the attachments.** Section 1 gives decision criteria; I cannot judge the dataset.

### Evidence ledger

**Completed (data seen)**

- **Discovery cohort** (lab update, "Early CBD data"): GD-CBD 3 mg/kg IP vs free CBD 3 mg/kg vs operated control, n=6 per arm, 2 cohorts. 50% threshold about 105 to 115 g at 24 to 120 h vs about 20 g control `[plot read]`. AUC: ** vs vehicle, * vs free CBD. Asterisks on the time course only at 72 to 168 h. At 2 to 6 h GD-CBD is not separated from free CBD (very wide error bars). GD-CBD individual AUCs span about 6,000 to 31,000 `[plot read]`, so the low end overlaps controls: the arm is heterogeneous.
- **Thresholds above baseline.** GD-CBD arm sits above pre-op baseline (about 80 g) at 24 to 120 h. Check filament ceiling and censoring before analysis.
- **Non-replications.** V20 (Dalton GD-CBD, younger males, 3 mg/kg): no effect. V22 (Cayman GD-CBD "5x dose", Cremophor free CBD): no effect. V23 (Cayman GD-CBD, older females, 3 and 10 mg/kg, n=3 each, control n=2): no effect. V24 (Cayman, older females, 40 mg/kg, "von Frey pushing", control n=2): modest, about 55 vs 45 g at 24 to 48 h `[plot read]`, not clearly separated.
- **Baselines differ about 3x between cohorts.** About 80 g in the discovery cohort vs about 25 g in V23 and V24 controls `[plot read]`. A 25 g baseline leaves almost no room to see hypersensitivity. Pooling raw grams across these is invalid.
- **Batch notes.** Batch 1 Cayman: worked. Batch 2 Dalton: failed. Batch 3 Cayman vial #1: failed, "made oxidized, but not at the time of reaction, leads to HU-331". Batch 4 Cayman vial #2: current. The cohort-to-batch map (which of V20 to V24 used which batch) is not in the files. `[inference]` V20 = Batch 2, V23 = Batch 3.
- **Ropivacaine.** V21: n=2 per sex, 0.25%, 400 uL, transient rise. Draft and outline say 200 uL on day 7 in a subset. Reconcile.
- **IVIS.** GD-Cy5 and HD-Cy5 in carrageenan paw edema, 3 h and 24 h (HD also 42 h). Signal is central/abdominal, not evident at the paw. Single images, n not stated. Not publishable as is (you said the same).
- **R01 preliminary values** (no raw data in the files): 6.04 +/- 0.8 nm, 12.5% w/w CBD, about 7 CBD per dendrimer, 17.6 kDa, CB<sub>2</sub> EC<sub>50</sub> 7.8 uM, solubility >200 mg/mL.

**Planned, not shown complete**

- In vitro release, CB<sub>1</sub>/CB<sub>2</sub> binding, THP-1 TNF-α/IL-6/IL-10/IL-1β panel (May plan; only the Batch 4 TNF-α result is reported), blocking studies, 30 mg/kg arm, paw edema dose-response, histology, DRG/dorsal horn colocalization, biodistribution-efficacy correlation, forest plot, power analysis, Cohen's d. The outline sections 3.1 to 3.6 are headings, not results.

**Unsupported or contradicted by the files**

- R01: "onset within 2 hours" (slide shows no separation at 2 to 6 h), "without sedation" (no safety data), "HD-Cy5 and GD-Cy5 label Iba1 and TUJ1 cells in DRG and wound after flank incision" (you say the flank/paw data are unusable).
- Draft: free CBD at 3, 10, 30 mg/kg as a dose-response (30 mg/kg has n=1), "three independent cohorts" (slide says 2), paw thickness endpoint (no data), "plantar incision" in 1.4 vs flank incision in Methods, "established" in the abstract.
- Sex: draft says female, outline says male, V20 was male. State the sex and age of the discovery cohorts from the raw sheet.
- Linker: R01 says releasable, the preclinical plan says non-enzymatic slow release or activity-while-bound. Release data decides which sentence goes in the paper.
- Free CBD arm: 0.9 mg per rat in 1 mL saline with 5% ACN is far above CBD aqueous solubility. Free CBD is likely a suspension. "GD-CBD beats free CBD" is partly a formulation result, and the paper must say so.

## 1. Recommended publication strategy

**Lead with the strongest dataset. Pain is the supporting indication unless it is the only one that qualifies.**

**Epilepsy qualifies as the lead if all hold** (check against the epilepsy raw files):

- **E1 same lineage:** batch IDs, CBD source and synthesis route are on the same Batch table as the pain material, ideally Batch 1.
- **E2 controlled:** concurrent vehicle and free CBD comparator, objective scoring (EEG or blinded seizure scoring).
- **E3 sized:** n of at least 8 per arm or an internal replicate.
- **E4 comparable dosing:** CBD-equivalent mg/kg and route overlap with the pain dose.
- **E5 beats free CBD,** not only vehicle.

**Pain is confirmed if** the new cohort meets the prespecified criteria in section 3 (R1 and R2).

| Epilepsy qualifies | Pain confirmed | Paper |
|---|---|---|
| Yes | Yes | **Cross-indication, epilepsy leads.** One-sentence hypothesis: one GD-CBD preparation reduces neuronal-hyperexcitability phenotypes in two models. Pain is one figure, labeled exploratory. |
| Yes | No | **Epilepsy only.** No pain claim. Pain data stays in the KB and is not mentioned as efficacy. |
| No | Yes | **Pain-only short report** (brief communication tier). Restricted claims, section 5. |
| No | No | **No efficacy paper this year.** Write the batch-dependence and QC lesson as an internal record and decide divestment on that. Do not run a fourth cohort. |

**Coherence test:** if the unifying sentence needs "also", it is a conglomerate. If the epilepsy used a different preparation or a different dose basis, do not combine.

## 2. Minimum viable package

| Module | Must have | Nice to have | Do not do now |
|---|---|---|---|
| **Chemistry and in vitro** | Batch 4 identity file: lot, CBD vial, loading by NMR, free CBD %, HPLC purity, DLS size. Head-to-head THP-1 TNF-α dose-response, one plate, 3 independent runs: Batch 4, Batch 1 remnant, retained Batch 3 if it exists, free CBD, GD alone. Release profile for Batch 4 (and Batch 1 remnant if mass allows). Bounded HU-331 check (below). | CB<sub>2</sub> functional assay, IL-6/IL-1β/IL-10 on the same supernatants, endotoxin (LAL) on the dosing lot. | CB<sub>1</sub>/GPR55/PPAR-γ/TRP panels, microsomes, DDI, blocking studies, new analytical method development beyond one week. |
| **Flank incision** | One concurrent cohort, 12 animals (section 3). | GD-only arm n=3, only if linker-capped GD is already in hand. | 30 mg/kg arm, healthy GD-CBD arm, paw edema, gait, thermal, guarding, other models, oral CBD. |
| **Biodistribution** | Only if QC passes (section 4). | Uninjured control arm. | Chronic-model biodistribution, mouse work, nude mouse. |

**Why the TNF-α head-to-head is the highest-value item.** It is cheap, uses micrograms, and tests whether the assay discriminates a batch that worked from one that failed. If retained Batch 3 looks like Batch 4, the assay does not predict in vivo outcome, and the paper must not use it as a quality claim.

**HU-331 bounded check (one week, then stop).** Chemist to confirm, `[inference]` on my part:

- LC-MS of the CBD starting vial #2 and the CBD-PEG<sub>4</sub>-azide intermediate for m/z about 329 (HU-331, C<sub>21</sub>H<sub>28</sub>O<sub>3</sub>) vs 315 (CBD).
- UV-vis for a quinone band in the visible range.
- Report the result either way. If it stays unresolved, state in Methods and Limitations that CBD oxidation state in the conjugate was not analytically resolved and that batch-to-batch efficacy differed.

**Dendrimer-only group: not essential.** Handle with (a) GD alone in the TNF-α plate and (b) a limitation statement. The claim is then "GD-CBD vs vehicle and dose-matched free CBD", never "CBD is the active component". Add an in vivo GD-only arm only if material exists with zero new synthesis.

## 3. Final flank-incision cohort

**Groups (12 animals): injured vehicle n=4, injured free CBD 3 mg/kg n=3, injured GD-CBD 3 mg/kg CBD-equivalent n=5.**

- **Why 5/4/3 and not 3/3/3:** power for the one contrast that matters (GD-CBD vs vehicle) rises. Exact rank-test power at d=1.5: 3 vs 3 = 0.44, 4 vs 4 = 0.43, 5 vs 4 = 0.51, 5 vs 5 = 0.66 (my simulation, normal data). Free CBD already has n=6 historical at this dose, so it needs the fewest.
- **Capacity for 15:** use 5/5/5. Power at d=1.5 is 0.66.
- **n=3 vs 3 can never give two-sided p below 0.10 by exact rank test** (minimum one-sided p is 0.05).
- **Material:** about 0.9 mg CBD per 300 g rat, about 7 mg conjugate at 12.5% w/w. Confirm Batch 4 loading before dosing. Twelve rats need under 100 mg.

**Match the discovery cohort:** same sex, age (8 to 10 weeks), weight, supplier, vehicle (saline + 5% ACN, 1 mL IP immediately after closure), operator, filaments, up-down method, and the standard (not "pushing") von Frey technique. Same dose basis. Do not change the dose if the batch looks weak. Record the baseline.

**Blinding:** chemistry team code-labels syringes; randomization stratified by cage; testers never see the key; wound photos scored blind; analysis script frozen before unblinding.

**Time points:** baseline on two days, 2, 4, 6 h, then 24 h daily to 168 h. Ropivacaine at 168 h in vehicle animals, with the volume reconciled (200 vs 400 uL).

**Cohort validity (treatment-blind, written before unblinding; values to be fixed from the discovery raw sheet):** vehicle baseline at or above about 40 g `[placeholder]`; vehicle drop to 50% of baseline or lower at 24 and 48 h; ropivacaine reversal. An invalid cohort is reported, not analyzed for efficacy.

**Endpoints**

- **Primary:** linear mixed model on log<sub>10</sub> 50% threshold, 24 to 168 h, fixed effects group, time (categorical), group x time, cohort; random intercept per animal; one prespecified contrast GD-CBD vs vehicle averaged over time, two-sided alpha 0.05, effect with 95% CI.
- **Supporting:** AUC 24 to 168 h (trapezoidal, absolute and percent of baseline), responder rate (at least 50% of baseline threshold recovered at 3 or more consecutive time points), wound score.
- **Secondary window:** 2 to 6 h reported separately. The discovery data show no conjugate advantage there.

**Success criteria (prespecified)**

- **R1 (replication, new cohort alone):** GD-CBD/vehicle AUC ratio at or above 2 and exact one-sided permutation p at or below 0.05, and GD-CBD median above free CBD median.
- **R2 (consistency):** the cohort-level GD-CBD vs vehicle estimate has the same sign as the discovery estimate, and its 95% CI excludes zero or overlaps the discovery CI.
- **R1 met:** "replicated with an independent preparation". **R2 only:** "consistent, not confirmed". **Neither:** failure to replicate; pooled analysis is descriptive only, and section 1 row "No" applies if epilepsy also fails.

**Historical plus new cohort, without claiming one lot**

- **Unit of replication is the cohort.** Preparation is a label, reported in a table (lot ID, CBD source and vial, synthesis date, QC), never "same batch". Because preparation and cohort are collinear, the model cannot separate them. Say so.
- **Tier 1 (confirmatory):** new cohort alone (R1 and R2).
- **Tier 2 (pooled):** cohorts passing the validity rule, stratified by cohort, per-cohort effects shown side by side in a forest plot, no single pooled p value presented as definitive. The validity rule is applied to every 3 mg/kg GD-CBD cohort, including V23.
- **Tier 3 (all cohorts, supplement):** every GD-CBD cohort V20 to V24 and the new one, with dose, preparation, sex, age, baseline, n, outcome. Descriptive only.
- **Sensitivity:** leave-one-cohort-out; rank-based AUC; absolute vs baseline-normalized; censoring at the filament ceiling; responder analysis (Fisher exact).
- **Methods wording:** "GD-CBD was prepared from Cayman CBD in independent syntheses (Preparation A, cohorts 1 to 2; Preparation B, cohort 3). Efficacy was not observed with two other preparations (Table S1)."

## 4. Biodistribution (conditional)

**Go/no-go QC (all must pass, check by 2026-10-23):**

1. **Free dye:** SEC or HPLC shows free Cy5 at or below 2% of total fluorescence after purification, rechecked after 24 h in serum at 37 C.
2. **Labeling stoichiometry:** at most about 1 Cy5 per dendrimer, with the Cy5 dendrimer species checked by HPLC against unlabeled.
3. **Particle behavior:** DLS size and zeta within error of unlabeled GD-CBD; retention time not shifted.
4. **Signal:** a dilution series spiked into vehicle-injected tissue homogenate gives a linear standard curve well above background.
5. **Activity:** Cy5-GD-CBD retains TNF-α activity (within about 3-fold of unlabeled).
6. **Same-lineage:** made from the Batch 4 conjugate, not a new CBD lot.

Any failure means omit biodistribution. Do not spend animals on a likely failed run.

**Design (if QC passes), 10 rats:**

- **Injured + Cy5-GD-CBD, terminal at 6 h n=4 and 24 h n=4.** The IVIS operator's advice (May meeting) was that IP clearance is fast after about 12 h, so 24 h alone may miss signal. Image the organs within 10 minutes of euthanasia.
- **Injured + vehicle n=2** for autofluorescence (low-fluorescence chow).
- **Nice to have:** uninjured + Cy5-GD-CBD n=3 at 24 h.
- **Tissues:** incision skin and contralateral skin, ipsilateral and contralateral DRG (T13 to L2), spinal cord, kidney, liver.
- **Readouts:** ex vivo IVIS plus homogenate fluorescence against the standard curve (per gram tissue), paired ipsilateral vs contralateral within animal. Cryosections for DRG and wound with NeuN/Iba1 only if the quantitative signal is positive, quantified blind.
- **Statistics:** paired, on log signal. With n=4 the exact signed-rank test cannot go below p=0.125, so present 4 of 4 directional consistency and estimates, not significance.

**Claims by outcome**

- **Strong** (ipsilateral > contralateral in at least 4 of 4 per time point, above vehicle, QC clean): "Cy5-labeled GD-CBD signal was higher at the injured site and ipsilateral DRG than contralateral". Label tracks the dendrimer, not CBD.
- **Modest** (renal and liver dominant, small injured-side bias): "distribution consistent with renal clearance of GD, with a small injured-side excess". No targeting claim.
- **Negative or uninterpretable:** omit from the paper, or one sentence in Limitations. No supplement figure.

**Omit entirely if:** QC fails by 2026-10-23, the efficacy cohort is not underway by 2026-11-02, or imaging cannot be completed by 2026-11-27.

## 5. Manuscript framing

**Titles (pain-led, restrained)**

- *Glucose dendrimer conjugation of cannabidiol attenuates incision-evoked mechanical hypersensitivity in rats*
- *A glucose dendrimer-cannabidiol conjugate reduces postoperative mechanical hypersensitivity in a rat flank incision model*
- Cross-indication option: *Glucose dendrimer-cannabidiol in models of neuronal hyperexcitability: seizures and postoperative pain* (only if the section 1 table says so).

Drop "durable" and "significant" from the title and "single post-operative dose" is fine only if stated as one IP dose.

**Central claim:** In female rats, a single IP dose of GD-CBD, at a CBD-equivalent dose where free CBD was inactive, reduced mechanical hypersensitivity after flank incision, in two discovery cohorts and one cohort with an independent preparation `[if R1 or R2 met]`.

**Main figures**

1. Chemistry: structure, loading, size, HPLC, release.
2. In vitro: THP-1 TNF-α, GD-CBD vs free CBD vs GD, with the batch comparison.
3. Study design and cohort-validity data (baseline, vehicle hypersensitivity, ropivacaine).
4. Time course, all arms, individual animals shown, cohorts color-coded.
5. AUC and responder analysis with per-cohort forest plot.
6. Biodistribution `[only if it passes]`, or histology/wound score if not.

**Supplement:** Table S1 (all GD-CBD cohorts and preparations), Table S2 (batch QC), raw per-animal data and analysis script, surgical technique, NMR/HPLC spectra, sensitivity analyses.

**Claims to avoid**

- **Neuronal targeting** or "targeted delivery". No validated labeled conjugate and no usable flank biodistribution.
- **Localization causes analgesia.** No correlation data and no basis for one.
- **Intact conjugate retention.** The label follows the dendrimer; release is unproven here.
- **CBD is the active component.** No dendrimer-only arm.
- **Dose-sparing multiples** (for example 10x). The 30 mg/kg free CBD arm is n=1.
- **Rapid onset, no sedation, "durable", "established".** Not supported.
- **Reproducibility across batches.** Efficacy was batch-dependent.
- **Mechanism** beyond "TNF-α reduction in THP-1 cells".
- **Chronic pain relevance** beyond one sentence in Discussion.

## 6. Timeline (today is 2026-10-09)

| Dates | Work | Gate |
|---|---|---|
| Oct 9 to 16 | Confirm cohort-to-batch map and discovery sex/age. Freeze analysis plan and validity rule in writing. Batch 4 identity file. TNF-α head-to-head. HU-331 check. Order or confirm rats. Retrieve epilepsy batch IDs and design. | **G1 Oct 16:** analysis plan frozen; TNF-α run complete. |
| Oct 16 to 23 | Cy5 labeling attempt and QC (parallel, one person). Release assay. Habituation begins. | **G2 Oct 23:** Cy5 QC pass, else drop biodistribution. |
| Oct 23 to Nov 2 | Habituation, baselines, code labeling. | Cohort starts only if G1 passes. |
| Nov 2 to 9 | Surgery, dosing, 7-day testing, ropivacaine. | |
| Nov 9 to 13 | Unblind, run frozen script, R1/R2. | **G3 Nov 13:** pain confirmed or not; epilepsy E1 to E5 scored; section 1 row chosen. |
| Nov 13 to 27 | Biodistribution cohort (if G2 passed and rats available). Figures and Methods drafted. | **G4 Nov 27:** biodistribution in or out, final. |
| Nov 27 to Dec 11 | Full draft, tables, Table S1. | |
| Dec 11 to 18 | PI and co-author review. | |
| Dec 18 to 29 | Revise, format, submit. | **Submit by Dec 29.** |

If the cohort fails (G3), there is no replacement cohort. The epilepsy-only or no-paper rows apply.

## 7. Risks and mitigation

| Concern | Shortest credible mitigation | Limitation statement |
|---|---|---|
| **Small n** | Individual animals shown, effect sizes with CIs, responder analysis, no definitive p from pooled data. | "Group sizes were small; results are hypothesis-supporting." |
| **Batch history** | Table S1 with every cohort, preparation, QC, outcome. Preparations are named, never merged. | "Efficacy differed between preparations; cause not established." |
| **Reproducibility** | Prespecified replication with a new preparation, report either result. | "One independent preparation was tested." |
| **No dendrimer-only control** | GD alone in the TNF-α plate. Claim limited to GD-CBD vs vehicle and free CBD. | "A carrier-only arm was not included in vivo." |
| **Limited mechanism** | Restrict to the TNF-α result. | "Mechanism was not tested; in vitro anti-inflammatory activity only." |
| **Single sex** | State sex in Methods and title/abstract. | "Only female rats were tested in the efficacy cohorts." (V20 males were negative with another preparation: say so only if V20 is in Table S1.) |
| **Biodistribution uncertainty** | Omit unless QC passes. | "Tissue distribution was not established." |
| **Flank incision vs chronic pain** | One sentence. No chronic claim. | "The model is acute postoperative pain; chronic efficacy was not tested." |
| **ACN vehicle** | Identical vehicle in every arm. Justify in Methods. | "5% acetonitrile was used for solubilizing free CBD." |
| **Free CBD formulation** | Report vehicle and appearance. Note Cremophor free CBD was also inactive (V22). | "Free CBD may have had limited bioavailability as a suspension." |
| **HU-331 / oxidation** | Bounded check, then state the result. | "CBD oxidation state in the conjugate was not analytically resolved." |
| **Ceiling or floor in von Frey** | Censoring sensitivity analysis. | |

## Open items for the user

- Epilepsy dataset: batch IDs, design, n, comparator, and whether a draft exists.
- Cohort-to-batch map for V20 to V24 and the discovery cohorts.
- Sex, age, weight and baseline of the discovery cohorts (raw sheet).
- Batch 4 loading (NMR) and amount of Batch 1 and Batch 3 retained.
- Whether release data and the CB<sub>1</sub>/CB<sub>2</sub> assays from the May plan exist.
- Whether 12 or 15 rats are available for the final cohort.
- Whether the PI accepts that a cohort failure ends the pain efficacy paper.
