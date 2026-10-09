# **Title Page**

* Title: *A single post-operative dose of glucose dendrimer-cannabidiol provides significant and durable pain relief."*  
*  Authors and affiliations  
* Corresponding author information  
* Keywords \- cannabidiol, dendrimer, postoperative pain

# 

# **Abstract** 

* Background: Post-operative pain burden and current treatment limitations  
* Objective: Evaluate dendrimer-conjugated CBD efficacy in rat incision model \+ paw edema?  
* Methods: Brief description of model, treatment groups, and assessments  
* Results: Key findings with statistics  
* Conclusions: Main interpretation and significance

# 

# **1\. Introduction**

## **1.1 Clinical Context**

* Post-operative pain epidemiology and impact  
* Current analgesic limitations and unmet needs  
* Rationale and need for new therapeutic approaches  
* 

## **1.2 Drug Background**

* Chemical classification and structure  
* Mechanism of action  
* Previous preclinical/clinical data (if any)  
* Limitations for clinical/commercial translation  
* 

## **1.3 Study Rationale**

* Background and rationale on dendrimer platform and glucose dendrimer specifically  
* Model selection justification  
* Hypothesis and specific aims

# 

# **2\. Materials and Methods**

## **2.1 Synthesis and characterization of D-Cy5 and GD-CBD conjugates**

* Chemical sourcing  
* Step 1: Glucose dendrimer synthesis  
* Step 2.1: Dendrimer-linker attachment  
  * Dendrimer partially functionalized with linker molecules using protection/deprotection chemistry  
* Step 2.2: CBD-linker attachment  
* Step 3: CBD conjugation  
  * click  
  * Reaction performed under appropriate conditions  
  * Purification via dialysis.  
* Characterization by:  
  * ¹H NMR (CBD loading).  
  * HPLC  
  * MS  
  * DLS  
  * Zeta potential  
  * solubility  
* Formulation and stability  
  * Release   
* Vehicle composition (ACN discussion?)  
* Dose selection rationale

**2.2 Flank Incision Model**  
Animals

* Rat, Sprague Dawley, Male, 8-10 weeks old, 250-300g  
* Inotiv, housed in animal facility with 12‐h light and 12‐h dark cycle under controlled temperature and humidity (temperature: 21 ± 0.5°C; humidity: 55% ± 5%).   
* Standard rodent chow provided ad libitum.  
* RA24M356 (February 28, 2025\) approved by the JHH IACUC  
* Sample size calculation and randomization

Structured habituation protocol prior to experiments to minimize stress and variability.

* Day 1: acclimation to testing room for 1 hour.  
* Days 2–3: exposed to testing enclosure (without stimulation) for 10 minutes each day.  
* Subsequent 5 days: gradual introduction to von Frey filament testing with starting filaments of increasing stiffness (starting at filament 4.56).  
* Baseline mechanical withdrawal thresholds established using standardized up-down method.  
* Each von Frey testing session:  
  * 20 minutes acclimation in fibering room with cage lids open.  
  * Individual transfer from home cage to testing enclosure.  
  * 5 minutes acclimation in testing enclosure.  
  * Video recorded during both acclimation and testing for independent validation if needed.

Surgical Procedure:

* Anesthetized with 2% isoflurane via inhalation.  
* Maintained on heated surgical platform to ensure normothermia.  
* Left flank shaved and disinfected with povidone-iodine and 70% ethanol.  
* 2 cm longitudinal incision made along flank, starting near dorsal iliac crest and extending anteriorly.  
* Only skin incised; underlying muscle and connective tissue preserved.  
* Wound closed immediately with simple interrupted sutures using 3-0 nylon.  
* Sutures placed at 2-3 mm intervals, 5-7 sutures total.  
* Postoperative monitoring until full recovery.  
* Daily evaluations for health, wound integrity, and signs of distress or infection.

Treatment protocol

* A single dose of CBD (3, 10, & 30 mg/kg) and GD-CBD (3 mg/kg) in 1 mL saline \+ 5% ACN was given IP immediately following wound closure, under anesthesia.  
* Rats were divided into 3 cohorts  
* n=6-9  
* Experimenters were blinded to drug/dose; chemistry team delivered code-labeled drug 

Behavioral Assessments:

* Mechanical sensitivity evaluated daily for 7 days post-surgery using von Frey filaments.  
* Testing sites marked 3-4 mm from incision on dorsal and ventral sides.  
* Withdrawal thresholds recorded using standardized up-down method.  
* On final day: local anesthesia validation with ropivacaine (0.25%, 200 µL) perilesionally.  
* Subsequent von Frey testing confirmed transient reduction in mechanical sensitivity.

Tissue Collection and Histological Analysis:

* Euthanasia by CO₂ inhalation in accordance with AVMA guidelines, followed by cervical dislocation.  
* Skin around incision excised and fixed in 10% formalin.  
* Tissue processed, paraffin-embedded, sectioned at 10 µm, stained (e.g., H\&E).  
* Assessed for cellular responses and inflammatory profiles related to sutures and drug treatments.

Experimental Design and Data Collection:

* Animals randomly assigned to treatment groups.  
* Behavioral assessments and data collection performed by blinded experimenters.  
* Sample sizes determined via prior power analyses.  
* Environmental conditions and protocols standardized to minimize confounding variables.

## **2.6 Statistical Analysis**

Prism 10 and [Python](https://colab.research.google.com/drive/1dWCiEqarjD6SfKxaqNPxICdo6n1kKjor?usp=sharing) ([raw data](https://docs.google.com/spreadsheets/d/1I_zkZTlqUG-5qiZ0-plFni-K40oTVIQl-ZWctefjRmk/edit?usp=sharing))  
Area Under the Curve (AUC) Calculation

* Calculated the area under the curve (AUC) of the 50% withdrawal threshold for each animal.  
* Used trapezoidal integration.  
* Incorporated timepoints from 0 hours onward to focus on post-treatment effects.  
* Excluded the baseline measurement at \-24 hours.  
* Resulting AUC values included in dataset for subsequent statistical analyses.

Statistical Analysis

* Three statistical approaches employed to investigate treatment effects on 50% withdrawal threshold, accounting for group differences, temporal dynamics, and repeated measures.

ANOVA and Tukey HSD for AUC

* One-way ANOVA used to evaluate differences in AUC across treatment groups.  
* Tested null hypothesis of equal group means.  
* Normality of residuals assessed using quantile-quantile (Q-Q) plots.  
* Following significant ANOVA, Tukey’s HSD test applied for post-hoc pairwise comparisons.  
* Family-wise error rate controlled at α \= 0.05.

Linear Mixed Model (LMM)

* Linear mixed model used to examine effects of treatment group and timepoint on 50% withdrawal threshold.  
* Included group-by-timepoint interaction to capture group-specific temporal trends.  
* Fixed effects: group, timepoint, group-by-timepoint interaction.  
* Random intercept for each animal to account for within-subject correlation.  
* Random slopes for timepoint initially explored but abandoned due to model instability.  
* Significant fixed effects (p \< 0.05) identified and interpreted to highlight key findings.

Tukey HSD for Group Differences Across All Timepoints

* Tukey’s HSD applied to 50% withdrawal threshold values pooled across all measurement times.  
* Assessed overall group differences independent of specific timepoints.  
* Controlled error rate at α \= 0.05.  
* Complements time-sensitive insights from LMM.

# 

# **3\. Results**

## **3.1 Characterization of GD-CBD Conjugate**

1. Physicochemical properties  
   1. CBD loading per dendrimer (¹H NMR quantification)  
   2. Size and charge (DLS and zeta potential)  
   3. Purity confirmation (HPLC, MS)  
2. Formulation advantages  
   1. Aqueous solubility comparison: GD-CBD vs free CBD  
   2. Stability in vehicle (saline \+ 5% ACN)  
3. In vitro release kinetics  
   1. CBD release profile over 7 days  
   2. Correlation with in vivo efficacy duration  
4. In vitro uptake & binding  
   1. CB1/CB2 binding assays comparing GD-CBD vs CBD  
   2. Cellular uptake in relevant cell types  
   3. Stability of conjugate in physiological conditions  
   4. Functional activity in cannabinoid receptor assays  
   5. Anti-inflammatory activity in stimulated macrophages

## **3.2 Validation of Refined Flank Incision Model**

1. Baseline characteristics (n=2-3 per group across X cohorts)  
   1. Pre-surgical mechanical thresholds following habituation protocol  
   2. Consistency across cohorts  
2. Post-surgical hypersensitivity development  
   1. Vehicle group: Peak sensitivity at 48h, gradual resolution over more than 7 days  
   2. Withdrawal threshold changes at marked sites (3-4mm from incision)  
3. Model validation  
   1. Ropivacaine responsiveness on day 7 confirms ongoing sensitization  
   2. Reproducibility across cohorts

## **3.3 Single-Dose GD-CBD Produces Sustained Analgesia Superior to Free CBD**

1. Primary outcome: Mechanical withdrawal thresholds  
   1. Time course data (baseline, 24h, 48h, 72h, 96h, 120h, 144h, 168h)  
   2. GD-CBD (3 mg/kg) vs CBD (3, 10, 30 mg/kg) vs vehicle  
   3. Statistical analysis: Linear mixed model with group × time interaction  
2. Area under the curve analysis  
   1. AUC calculation from 0-168h post-treatment, potentially other timepoints  
   2. One-way ANOVA with Tukey HSD post-hoc  
   3. GD-CBD significantly greater AUC than all other groups  
3. Effect magnitude and duration  
   1. GD-CBD maintains \>X% reversal of hypersensitivity for Y days  
   2. Free CBD shows dose-dependent but transient effects  
   3. Percentage of animals returning to baseline thresholds  
4. Reproducibility analysis  
   1. Effect demonstrated in X/X cohorts (3?)  independently  
   2. Forest plot of effect sizes across cohorts  
   3. Leave-one-cohort-out sensitivity analysis

## **3.4 Biodistribution of Cy5-GD-CBD Demonstrates Targeted Delivery**

1. Temporal distribution pattern at 4h, 24h, and 7d post-injection  
   1. 4 hours: Rapid target engagement  
      1. Peak accumulation at incision site  
      2. Initial uptake in DRG and spinal cord  
      3. Minimal off-target distribution  
   2. 24 hours: Cellular uptake and redistribution  
      1. Enhanced accumulation in DRG neurons  
      2. Dorsal horn localization in spinal cord  
      3. Clearance from systemic circulation  
   3. 7 days: Persistent retention in pain-processing tissues  
      1. Continued detection at therapeutic sites  
      2. Correlation with sustained analgesic effect  
      3. Minimal signal in clearance organs  
2. Tissue-specific accumulation patterns  
   1. Incision site quantification (MFI) across timepoints  
   2. DRG accumulation and retention kinetics  
   3. Spinal cord dorsal horn (laminae I-II) targeting  
3. Cellular colocalization analysis  
   1. Neuronal uptake (NeuN/β-III tubulin colocalization)  
      1. Quantification at each timepoint  
      2. Pearson's correlation coefficients  
   2. Macrophage accumulation (CD68/Iba1 colocalization)  
      1. Time-dependent uptake pattern  
      2. Correlation with anti-inflammatory effects  
4. Biodistribution-efficacy correlation  
   1. Tissue retention half-life calculations  
   2. Overlay of D-Cy5 signal with behavioral analgesia timeline  
   3. Comparison with expected clearance of free CBD

## **3.5 Histological Assessment of Wound Healing and Inflammation**

1. H\&E staining of incision sites  
   1. Inflammatory cell infiltration across groups  
   2. Wound healing progression  
   3. Suture-related tissue responses  
2. Gross images \- wound healing progression  
3. Comparison of GD-CBD vs CBD vs vehicle  
   1. Reduced inflammatory profiles in GD-CBD group  
   2. Normal wound healing preserved

## **3.6 Statistical Validation and Effect Sizes**

1. Model assumptions and validation  
   1. Q-Q plots confirming normality  
   2. Random effects accounting for within-animal correlation  
2. Effect sizes (Cohen's d)  
   1. GD-CBD vs vehicle at peak effect (day 2-3)  
   2. Clinical relevance of effect magnitude  
3. Power analysis confirmation  
   1. Achieved power with n=6-9 per group

## **Claude’s critiques:**

1\. Mechanistic Gap 

* Why does conjugation extend duration by 5x? (BIODISTRIBUTION)  
* Consider adding: Tissue CBD levels, CB receptor expression, inflammatory mediators from banked tissue

2\. Missing Control

* Need dendrimer-only group (without CBD)  
* This is critical to prove CBD is the active component

3\. Sex Bias

* Single sex study limits impact  
* Add strong justification in limitations

4\. Biodistribution-Behavior Correlation

* D-Cy5 studies appear separate from behavioral cohorts  
* Need to show D-Cy5 retention correlates with analgesia duration

# 

# **4\. Discussion**

## **4.1 Summary of Main Findings**

* Key results interpretation  
* Comparison to hypothesis

## **4.2 Mechanism Insights**

* How findings relate to drug mechanism  
* Structure-activity relationships (if multiple compounds)  
* How the dendrimer uniquely enables and synergizes with drug mechanism

## **4.3 Clinical Translation Potential**

* Relevance to human post-operative pain  
* Advantages over current therapies and differentiation from previous literature.  
* Potential therapeutic window

## **4.4 Study Limitations**

* Model limitations  
* Single modality assessment  
* Species differences  
* Duration of follow-up

## **4.5 Future Directions**

* Additional pain modalities to test  
* Combination therapy potential  
* Mechanistic studies needed  
* Path to clinical development

# 

# **5\. Conclusions**

* Main finding statement  
* Clinical significance  
* Novel contribution to field

# 

# **References**

* 30-50 references typical

# 

# **Figures and Tables**

## **Figure 1: Drug Structure and Chemistry**

* Chemical structure  
* Key physicochemical properties table

## **Figure 2: Experimental Timeline**

* Schematic of surgery, treatment, and assessment schedule

## **Figure 3: Mechanical Threshold Time Course**

* Von Frey data over 7 days  
* All treatment groups with error bars

## **Figure 4: Dose-Response Analysis**

* Key timepoint(s) showing dose-dependent effects

## **Table 1: Animal Demographics and Baseline Data**

## **Table 2: Statistical Summary of Treatment Effects**

# 

# **Supplementary Materials**

* Detailed surgical technique  
* Additional behavioral data  
* Raw data tables  
* Chemical characterization spectra

