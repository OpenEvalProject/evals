# Regulation of EGFR signal transduction by analogue-to-digital conversion in endosomes

## Authors

- Roberto Villaseñor<sup>1</sup>
- Hidenori Nonaka<sup>1</sup>
- Perla Del Conte-Zerial<sup>1</sup>
- Yannis Kalaidzidis<sup>1</sup>
- Marino Zerial<sup>1</sup> †

### Affiliations

1. Max Planck Institute of Molecular Cell Biology and Genetics Dresden Germany
2. Faculty of Bioengineering and Bioinformatics Moscow State University Moscow Russia

† Corresponding author

## Abstract

An outstanding question is how receptor tyrosine kinases (RTKs) determine different cell-fate decisions despite sharing the same signalling cascades. Here, we uncovered an unexpected mechanism of RTK trafficking in this process. By quantitative high-resolution FRET microscopy, we found that phosphorylated epidermal growth factor receptor (p-EGFR) is not randomly distributed but packaged at constant mean amounts in endosomes. Cells respond to higher EGF concentrations by increasing the number of endosomes but keeping the mean p-EGFR content per endosome almost constant. By mathematical modelling, we found that this mechanism confers both robustness and regulation to signalling output. Different growth factors caused specific changes in endosome number and size in various cell systems and changing the distribution of p-EGFR between endosomes was sufficient to reprogram cell-fate decision upon EGF stimulation. We propose that the packaging of p-RTKs in endosomes is a general mechanism to ensure the fidelity and specificity of the signalling response.

## Introduction

Cells respond to various signals by activating different types of RTKs and committing to specific cell-fate decisions (Katz et al., 2007). A remarkable property of this system is that different RTKs can elicit distinct cellular responses through the same signal transduction machinery (Marshall, 1995; Kholodenko et al., 2006). In several cases, signalling specificity results from differences in amplitude and duration of the intracellular signalling cascades (Marshall, 1995; Maroun et al., 2000; Nagashima et al., 2007). For example, in PC12 cells, EGF stimulation of EGFR leads to transient Erk phosphorylation and cell proliferation, whereas NGF binding to TrkA leads to sustained Erk phosphorylation and cell differentiation (Marshall, 1995). Differences in signalling amplitude and duration can arise from positive or negative feedback loops within the same signalling pathway (Santos et al., 2007) or activation of additional signalling components (York et al., 1998). To explain such differences, it has been proposed that both EGF and NGF stimulation induce a specific ‘molecular context’ that determines the topology of the signal transduction network (Santos et al., 2007). How such a topology is determined for different RTKs and whether it is the sole determinant of signal specificity is unclear (Kholodenko, 2007).

Insights into this problem may be provided by the spatio-temporal distribution of RTKs along the endosomal system. The detection of phosphorylated receptors and signalling adaptors in endosomes (Di Guglielmo et al., 1994; Vieira et al., 1996; Sorkin, 2001; Teis et al., 2002; Lampugnani et al., 2006; Galperin and Sorkin, 2008; Schenck et al., 2008; Coumailleau et al., 2009) led to the concept that signalling is initiated at the plasma membrane but continues in endosomes (Di Guglielmo et al., 1994). Indeed, inhibition of endocytosis by blocking Dynamin function causes significant alterations in signalling specificity (Vieira et al., 1996). However, recent studies challenged this concept arguing that EGFR signalling occurs primarily at the plasma membrane (Damke et al., 1994; Brankatschk et al., 2012; Sousa et al., 2012). Interestingly, a recent systems survey of endocytosis (Collinet et al., 2010) revealed an unexpected tight control in the number, size, and cargo content for EGF-positive endosomes, raising the question of why is EGF packaging in endosomes so accurately controlled? Here, we hypothesized that the tight control of the endosomal distribution of EGF could serve to regulate signal transmission. We tested this hypothesis by quantitatively analysing the endosomal distribution of EGFR as an RTK model system in endosomes and evaluating its impact on cell-fate decisions.

## Results

To measure the content of p-EGFR in individual endosomes, we used two independent assays (for a detailed description see ‘Materials and methods’ and Figure 1—figure supplement 1). First, we modified a FRET-FLIM microscopy assay previously used to measure the spatial distribution of p-EGFR at the plasma membrane (Wouters and Bastiaens, 1999; Verveer et al., 2000). The assay measured the FRET signal between EGFR-GFP and an anti-phospho-tyrosine antibody (p-Tyr-ab) labelled with AlexaFluor 555. Since FLIM microscopy lacks the spatial resolution to analyse the receptor activation at a sub-cellular level, we modified the assay into a high-resolution FRET microscopy assay. However, instead of the total cell signal, we measured the distribution of EGFR and p-EGFR at the level of individual endosomes resolved by high-resolution confocal microscopy and quantitative automated image analysis (Rink et al., 2005; Collinet et al., 2010) (Figure 1—figure supplement 2). To avoid artefacts of overexpression, we used HeLa cells transfected with a bacterial artificial chromosome (BAC) transgene stably expressing EGFR-GFP under its endogenous promoter (Poser et al., 2008). In these cells (Figure 1—figure supplement 3A), the uptake of EGF was only ∼twofold higher compared to endogenous (Figure 1—figure supplement 3B). However, the transport kinetics were similar (Figure 1—figure supplement 3C). Second, we measured p-EGFR with an antibody against a specific phospho-tyrosine residue (Tyr1068). Both assays gave very similar results (Figure 1—figure supplement 4). As the FRET assay is not restricted to a single phosphorylation site that can change over time (Morandell et al., 2008), we used it as a primary assay in further experiments. Under the fixation conditions used, we observed no significant difference in the morphology (Figure 1—figure supplement 5A) or area (Figure 1—figure supplement 5B) of EGFR-positive endosomes (Video 1). For every time point, ∼15,000 endosomes from over 200 cells were analysed.

![Video 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-media1.mpg.jpg)

**Video 1.:** HeLa EGFR-GFP BAC cells were imaged with a spinning disk microscope after 1 minute of EGF stimulation with 10 ng/ml EGF. Movie shows maximal projection of 3 z-slices of 0.8 mm thickness.

Continuous stimulation with EGF triggered the internalization of EGFR into endosomes (Figure 1 and Figure 1—figure supplement 2). The total amount of endosomal EGFR peaked after 15 min and decreased, reflecting (1) down-regulation of surface receptors (Wiley et al., 1991) and (2) their degradation (Dunn and Hubbard, 1984) over time (Figure 1A, green curve). On the other hand, the total p-EGFR levels reached a maximum already at 10 min, followed by a phase of decay (Figure 1A, red curve). Comparison of decay kinetics for both curves after 15 min showed that de-phosphorylation of p-EGFR occurred faster than degradation (τdecay EGFR = 88.13 ± 14.49, τdecay p-EGFR = 30.97 ± 1.69, for details see ‘Materials and methods’). Our FRET measurements are thus consistent with previously reported EGFR transport and phosphorylation kinetics determined by biochemical and microscopic methods (Di Guglielmo et al., 1994; Burke et al., 2001).

![Figure 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-v2.jpg)

**Figure 1.:** (A) Time course of total integral intensity of EGFR (green) and p-EGFR (red) in endosomes measured by a FRET microscopy assay in HeLa EGFR BAC cells after continuous stimulation with 10 ng/ml EGF. The total integral intensity is defined as the sum of integral intensities of all endosomes in an image normalized by the area covered by the cells (for details see ‘Materials and methods’ and Supplementary information). (B) Time course of mean integral intensity per endosome for total EGFR (green curve) and p-EGFR (red curve) as in (A). Intensity curves (A–B) were normalized to the intensity value at 10 min. Crosses show the corresponding values after 1 min of EGF stimulation and incubation in ligand-free medium for 10 or 30 min (pulse-chase). (C) Time course of histogram distributions of the total EGFR integral intensity per endosome upon EGF stimulation as in (A). (D) Time course of histogram distributions of the p-EGFR integral intensity per endosome upon EGF stimulation as in (A). In both graphs, receptors in CCVs are responsible for the width of the distribution at 3 min (red curves in C and D). For comparison, histogram amplitude in B and C were normalized by each curve integral. In each graph, the integral intensity values were scaled by the mode of the histogram at 10 min. The experimental points from all histograms were fitted with a log-normal distribution. (E–F) Distribution of p-EGFR in endosomes as a function of EGF concentration after continuous stimulation for 30 min. Mean number of endosomes with EGFR (green curve) and p-EGFR (red curve) per 1000 μm2 of the area covered by cells (E) and mean integral intensity of EGFR (green curve) and p-EGFR (red curve) per endosome (F). On panel (F) curves were normalized to the intensity value at 10 ng/ml EGF. Lines are hyperbolic fits (E) or least square fits (F) to the experimental points. In both cases insets show the same graphs in linear scale. The different magnitude of the error bars in (E) and (F) is due to the averaging by the total number of images (E) or the total number of endosomes (F). In all cases, points show mean ± SEM. All measurements were done in three independent experiments with a total of ∼150 cells per time point or condition.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) Representative image of HeLa cells with no EGFR-GFP expression stained with an anti-p-Tyr antibody directly labelled with AlexaFluor 555 used to quantify the amount of fluorescence bleed-through. Scale bars, 10 μm. (B) Distribution of the ratio of FRET-p-Tyr maximum intensities of individual colocalized objects in the FRET and p-Tyr channel. Since there is no GFP fluorescence, these objects give an estimation of fluorescence bleed-through (filled circles). The continuous black line is the fit of three Gaussian components (shown in coloured dashed lines). The mean and variance of the red and blue curves were used for image corrections (see ‘Materials and methods’ for details). (C) Mean FRET-p-Tyr intensity distribution before (black curve) and after correction (red curve).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Representative images of HeLa EGFR-GFP BAC cells after continuous stimulation with 10 ng/ml EGF for the indicated time points. EGFR-GFP fluorescence is shown in green, the corrected p-EGFR intensity is shown in red, and DAPI-stained nuclei are shown in blue. Measurements from each individual endosome were used for all quantifications. Scale bars, 10 μm. (B–C) Time course of histogram distributions of the total p-EGFR (B) or EGFR (C) integral intensity per endosome upon EGF stimulation as in Figure 1. The histogram shows the number of vesicles per 1000 μm2 of the area covered by cells. Intensity values were scaled by the mode of the histogram at 10 min. In all graphs, experimental points were fitted with a log-normal distribution. Points show the mean from three independent experiments with a total of ∼150 cells per time point or condition.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Representative Western blot of comparing the expression of EGFR and EGFR-GFP in HeLa Kyoto and HeLa EGFR-GFP BAC cells. The lower band corresponds to the untagged receptor, whereas the upper band corresponds to EGFR-GFP, which is absent in HeLa Kyoto cells. (B) Time course of EGF integral intensity in endosomes in HeLa Kyoto (black curve) and HeLa EGFR-GFP BAC cells (red curve). Intensity curves were normalized to the intensity value at 10 min for HeLa Kyoto cells. (C) Comparison of both time courses after dividing the HeLa EGFR-GFP BAC cells by 2. Squares show the difference between both curves. Experimental points show mean ± SEM from one representative experiment with a total of ∼150 cells per time point and condition. Time courses were fitted as in Figure 1.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Representative images of p-EGFR staining by an antibody against a single phospho-tyrosine residue of EGFR after 0, 10, and 30 min of continuous stimulation with 10 ng/ml EGF. Scale bars, 10 μm. Time course of the p-EGFR mean integral intensity per endosome measured by standard immunofluorescence (blue) and by FRET assay (red). For comparison, both curves were normalized to the value at 10 min. Experimental points were fitted as in Figure 1A.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Representative images of HeLa BAC cells expressing EGFR-GFP after 20 min of stimulation with 10 ng/ml EGF before (left panel) or after fixation (right panel). Scale bars, 10 μm. (B) Histogram distribution of EGFR endosome area before (blue) and after fixation (red). The histogram shows the number of EGFR endosomes per 1000 μm2 of the area covered by cells. Measurements were taken from ∼500 cells from one representative experiment.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** Time course of total integral p-EGFR intensity in endosomes (red) and endosomes with p-EGFR (black) per 1000 μm2 of the area covered by cells (black) after stimulation with 10 ng/ml EGF as in Figure 1. Points show mean ± SEM. All measurements were done in three independent experiments with a total of ∼150 cells per time point or condition.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** (A–E) Histogram distributions for the p-EGFR (red) or total EGFR (green) integral intensity per endosome at 5 (A), 10 (B), 15 (C), 30 (D), and 60 (E) min of continuous stimulation with 10 ng/ml EGF. For comparison, the amplitude of all histograms was normalized by the curve integral and the integral intensity was scaled by the mode of each histogram. In all graphs, experimental points were fitted with a log-normal distribution. Points show the mean from three independent experiments with a total of ∼150 cells per time point or condition.

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** (A) Mean integral intensity of EGFR (green curve) and p-EGFR (red curve) per endosome upon stimulation with different EGF concentrations for 30 min (B) Time course of mean integral intensity of p-EGFR per endosome after continuous stimulation with 10 ng/ml (black curve) or 100 ng/ml (red curve) EGF. Curves were normalized by the intensity value at 10 min for 10 ng/ml EGF. Experimental points were fitted as in Figure 1A.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig1-figsupp9-v2.jpg)

**Figure 1—figure supplement 9.:** (A) Mean p-EGFR integral intensity per endosome as a function of endosome area upon 10 (black curve) or 30 min (red curve) of EGF stimulation. Both curves were normalized to the intensity value at 1 μm2 for 10 min stimulation. (B) Histogram distribution of endosome area upon 10 (black curve) or 30 min (red curve) of EGF stimulation. Each histogram was normalized by its respective curve integral. Points show mean ± SEM. All measurements were done in three independent experiments with a total of ∼150 cells per time point or condition.

We next determined the distribution of EGFR and p-EGFR in individual endosomes. The number of endosomes with p-EGFR decayed with similar kinetics as the total p-EGFR signal (τdecay N-p-EGFR = 45.24 ± 11.39 vs τdecay p-EGFR = 30.97 ± 1.69; compare red with black curve in Figure 1—figure supplement 6). The mean content of total EGFR per endosome increased over time and then rapidly decayed reaching steady state, due to the balance of continuous EGF uptake and degradation (Figure 1B, green curve). After a rapid increase, the mean content of p-EGFR in each endosome stabilized to a fairly constant level after ∼20 min (Figure 1B, red curve). Similar results were obtained when EGF was pulsed for 1 min and chased for different periods of time (Figure 1B, blue and black points).

To determine how the endosomal content of p-EGFR originates over time, we compared the distributions of EGFR and p-EGFR content per endosome. The width of distribution of total EGFR increased with time (Figure 1C), due to the fact that, as EGF continues to flow in, it first enters small early endosomes and progressively accumulates in larger ones (Rink et al., 2005). In contrast, the p-EGFR distribution first widened like that of total EGFR but then became almost twofold narrower than that of EGFR (Figure 1—figure supplement 7A–E compare the red and green curves) and stabilized after 30 min (Figure 1D). These results suggest an unexpected behaviour of p-EGFR, which over time stabilizes at a constant mean level per endosome.

Surprisingly, the mean amount of p-EGFR in endosomes was not ligand dependent. We stimulated cells with different concentrations of EGF for 30 min, when the amount of p-EGFR per endosome reached its steady state (Figure 1B,D). Once again, we found that EGFR and p-EGFR behaved very differently. The number of endosomes containing EGFR saturated already at low concentrations of EGF (0.5–1.0 ng EGF; Figure 1E, green curve) whereas the amount of total EGFR per endosome increased almost linearly (Figure 1F, green curve). This is expected because the higher the concentration of EGF, the higher the internalization of EGFR, whereas the number of receiving endosomes does not change significantly. In contrast, the number of endosomes with p-EGFR augmented with increasing EGF concentrations (Figure 1E, see red curve in semi-logarithmic scale, inset in linear scale). Strikingly, the mean amount of p-EGFR per endosome remained fairly constant, despite the EGF concentration varying almost over three orders of magnitude (Figure 1F, red curve). Therefore, increasing concentrations of EGF resulted in an increase in the number of endosomes with the same mean package of p-EGFR. Importantly, such a packaging is saturable because at high EGF concentrations the mean p-EGFR content per endosome was no longer constant with time (Figure 1—figure supplement 8).

The finding that endosomes contain a constant mean level of p-EGFR is striking. We performed several control experiments to verify that this is not an artefact caused by the FRET method or the assay. First, the mean amount of p-EGFR per endosome did increase at EGF concentrations higher than 10 ng/ml (Figure 1—figure supplement 8), indicating that the value measured is not artificially fixed, for example, by limited antigen accessibility. Second, a similar constant mean value of p-EGFR per endosomes was estimated with an independent method using the Tyr1068 antibody (Figure 1—figure supplement 4). Third, the narrow distribution of p-EGFR per endosome may simply reflect the sorting into endosomes of regular size. Whereas at 10 min the p-EGFR amount per endosome increased with the endosome area (Figure 1—figure supplement 9A, black curve), at 30 min (steady state, Figure 1B), the same mean amount was present in small and large endosomes alike (Figure 1—figure supplement 9A, red curve). Therefore, the amount of activated receptors per endosome is independent of endosome area. Finally, we verified that it is not a phenomenon peculiar to HeLa cells but also occurring in non-immortalized, non-cancer cell lines. Using the anti-phosphoTyr1068 antibody, we found that in primary mouse hepatocytes upon EGF stimulation the mean amount of p-EGFR per endosome saturated at ∼20 min whereas the mean amount of EGF continued to grow (data not shown), indicating that the packaging of p-EGFR in endosomes is not peculiar to a signalling-aberrant cancerous cell line.

In which endocytic compartment was p-EGFR packaged so uniformly? Nearly 80% of p-EGFR colocalized with the early endosomal marker EEA1 throughout the time course (Figure 2—figure supplement 1A). Less than 10% of p-EGFR colocalized with APPL1 after 15 min showing that it passed this endosomal compartment (Miaczynska et al., 2004) (Miaczynska et al., submitted). Very little p-EGFR colocalized with LAMP-1, a marker of late endosomes and lysosomes (Figure 2—figure supplement 1C). One possibility is that the packages of p-EGFR may reflect incorporation into intra-luminal vesicles (ILV) of multi-vesicular bodies (MVB). This possibility was ruled out using a previously described differential detergent solubilisation method (Malerød et al., 2007). We could determine that a large fraction of EGFR was not accessible to antibodies upon digitonin permeabilization, reflecting sequestration into ILVs (Malerød et al., 2007; Piper and Katzmann, 2007) (see Suppl. information and Figure 2A,B). In contrast, p-EGFR was always detectable suggesting that it was not within ILVs.

![Figure 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-v2.jpg)

**Figure 2.:** (A) Representative images of total EGFR and p-EGFR after staining with saponin or digitonin permeabilization methods. Immunofluorescence staining of LBPA is shown as a control marker for ILVs in MVBs. Scale bars, 10 μm. (B) Integral intensity of EGFR, p-EGFR, and LBPA (mean ± SEM) after permeabilization with digitonin or saponin. **p < 0.005 by a two-tailed t-test. Measurements were done in three independent experiments with a total of ∼150 cells per condition. (C) Time course of mean integral intensity per endosome for ub-EGFR (blue curve) upon EGF stimulation as in Figure 1A. p-EGFR is included for comparison. (D) Representative STORM images of p-EGFR (red) stained using a rabbit monoclonal anti-p-EGFR (Tyr 1068) antibody overlaid on top of a high magnification confocal image of EGFR (green). Left panels show clusters of p-EGFR upon stimulation with EGF for 10 or 30 min. Right panels show clusters of p-EGFR upon stimulation with EGF for 30 min in Hrs down-regulation or mock treatment. (E) Time course of the mean p-EGFR integral intensity per endosome in Hrs (red), Snf8 (blue), Vps24 (green), or mock-treated cells (black) (using three different siRNA oligonucleotides per gene). All curves were normalized by the intensity value at 10 min for the mock sample. Points show mean ± SEM from three different siRNAs per gene. Scale bar, 1 μm. (F) Integral intensity distribution of p-EGFR per endosome after down-regulation for 72 hr of PTPN11 (red) or in mock treatment (black) after continuous stimulation with 10 ng/ml EGF for 30 min. Red points show the average distribution of three different siRNAs. Experimental points were fitted as in Figure 1A.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Time course of integral intensity of total EGFR (green curve) and p-EGFR (red curve) colocalizing with EEA1 after continuous stimulation with 10 ng/ml EGF for different time points. Intensity curves were normalized to the intensity value at 10 min (B–C) Fraction of the total integral intensity of EGFR (green curve) or p-EGFR (red curve) colocalized with EEA1 (B) or LAMP-1 (C). In all cases, points show mean ± SEM. Measurements were done in three independent replicates with a total of ∼150 cells per time point or condition. Time courses were fitted to obtain the decay half-time τ (for details on the fitting procedure see ‘Materials and methods’).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Representative images of HeLa EGFR-GFP BAC cells after continuous stimulation with 10 ng/ml EGF for the indicated time points. EGFR-GFP fluorescence is shown in green, the corrected ub-EGFR intensity is shown in red. Measurements from each individual endosome were used for all quantifications. Scale bars, 10 μm. (B–C) Heat map of the 2D co-distribution of ub-EGFR and EGFR (B) or ub-EGFR and p-EGFR (C) integral intensity per endosome upon EGF stimulation as in Figure 1 after 10, 30, or 60 min. ub-EGFR and EGFR are well correlated, whereas the distribution of p-EGFR is significantly narrower than ub-EGFR at 30 and 60 min. Heat maps show the result of one representative experiment.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Distribution histogram of the differences in intensity between individual endosomes in consecutive frames during sequential photo-bleaching of EGFR-GFP (see ‘Materials and methods’ for details). (B) Difference between the number of positive and negative events in (A) for each ΔIntensity value. (C) Distribution histogram of the differences in intensity between individual endosomes in consecutive frames during sequential photo-bleaching of p-EGFR (see ‘Materials and methods’ for details). (D) Difference between the number of positive and negative events in (C) for eachΔIntensity value. The local amplitude maxima of the periodic function in (B) and (D) give an estimate of the change in intensity values when 1,2,3, …, n number of molecules are bleached. (E) Distribution of the number of molecules of EGFR-GFP and p-EGFR in individual endosomes after stimulation with 10 ng/ml EGF for 10 min.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A–B) Histogram distributions of the total EGFR (green) or p-EGFR (red) integral intensity per endosome after 30 min of EGF stimulation as in Figure 5 for Hrs (A) or mock-treated cells (B). (C) Representative images of HeLa EGFR BAC cells after continuous stimulation with 10 ng/ml EGF for 30 min and Hrs, Snf8, or Vps24 knock-down. Scale bars, 10 μm. (D) Changes in EGFR at the endosomal surface after knock-down of different ESCRT components measured by the differential permeabilization assay shown in Figure 2A Bar graphs show mean ± SEM. Measurements were done in three independent experiments using three different siRNA oligonucleotides with a total of ∼150 cells. In all graphs, experimental points were fitted with a log-normal distribution. Points show the mean from three independent experiments with a total of ∼150 cells per time point or condition.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** (A) Representative images of HeLa EGFR-GFP BAC cells before (left panel) and after 10 min stimulation with 10 ng/ml EGF (right panel). EGFR fluorescence is shown in green and Shc1 is shown in red. (B) Time course of mean integral intensity of Shc1 per endosome (black curve). The mean intensity of p-EGFR per endosome (red curve) is included for comparison. (C) Mean integral intensity of Shc1 per endosome as a function of EGF concentration. The curve was normalized to the intensity value at 10 ng/ml EGF. The solid line is a least square fits to the experimental points. In all cases, points show mean ± SEM. Measurements were done in three independent replicates with a total of ∼150 cells per time point or condition. Time courses were fitted as in Figure 1.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp6-v2.jpg)

**Figure 2—figure supplement 6.:** Time course of the total p-EGFR integral intensity upon stimulation with 10 (black and green curves) or 100 ng/ml (red and blue curves) of EGF. AG1478 (green and blue curves) was added 10 min after stimulation with EGF and remained in the medium throughout the time course. All curves were normalized by the intensity value at 10 min for the DMSO—10 ng/ml sample. Experimental points were fitted as in Figure 1. Points show mean ± SEM of ∼150 cells per time point and condition from one representative experiment.

![Figure 2—figure supplement 7.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp7-v2.jpg)

**Figure 2—figure supplement 7.:** (A) Representative images of HeLa EGFR BAC cells after continuous stimulation with 10 ngl/ml EGF for 30 min. Inhibitors were added 10 min after stimulation with EGF and remained in the medium throughout the time course. Scale bars, 10 μm. (B) Time course of the mean p-EGFR integral intensity per endosome in AG1478 (red), Gefitinib (blue), Lapatinib (green), or DMSO-treated cells (black). All curves were normalized by the intensity value at 10 min for the mock sample. Experimental points were fitted as in Figure 1. Measurements for AG1478 were done in three independent experiments; measurements from Gefitinib and Lapatinib show a representative experiment with a total of ∼150 cells per time point and condition.

![Figure 2—figure supplement 8.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig2-figsupp8-v2.jpg)

**Figure 2—figure supplement 8.:** (A) Total p-EGFR integral intensity after continuous stimulation with 10 ng/ml EGF in HeLa EGFR-GFP BAC cells and down-regulation of the indicated phosphatase or treatment with transfection reagent only. (B) Mean p-EGFR integral intensity per endosome after continuous stimulation with 10 ng/ml EGF in HeLa EGFR-GFP BAC cells and down-regulation of the indicated phosphatase or treatment with transfection reagent only. In both cases, bars are colour coded according to their respective phosphatase. All phosphatases were down-regulated with at least three oligos. Bars show mean ± SEM of all images for each oligo.

How do the kinetics of p-EGFR endosomal packaging compare with the kinetics of receptor dephosphorylation and ubiquitylation? After 10 min of EGF stimulation, the pool of p-EGFR in EEA1-positive endosomes (Figure 2—figure supplement 1A, red curve) decayed faster than total EGFR (Figure 2—figure supplement 1A, green curve; τdecay EGFR = 56.03 ± 5.72, τdecay p-EGFR = 37.08 ± 4.19), possibly due to de-phosphorylation or preferential removal of p-EGFR from early endosomes. The latter can be excluded since the fraction of p-EGFR in EEA1-positive endosomes remained almost constant throughout the time course (Figure 2—figure supplement 1B). EGFR ubiquitylation is required for its internalization into endosomes, and this is dependent on EGFR phosphorylation and the recruitment of the c-Cbl E3 ligase (Sigismund et al., 2013). To compare the levels of ubiquitylated EGFR (ub-EGFR) with those of p-EGFR within the endosomal system, we modified the FRET assay using an anti-ubiquitin antibody (Figure 2—figure supplement 2A). The kinetics of ub-EGFR were significantly different from those of p-EGFR. Whereas the levels of p-EGFR peaked at 15 min, ub-EGFR reached its maximum at 30 min after stimulation (Figure 2C, compare red with blue curves) and decreased more slowly than p-EGFR at later times, probably reflecting deubiquitylation prior to receptor sequestration into ILVs (Piper and Katzmann, 2007). These results are consistent with the fact that the appearance of p-EGFR precedes that of ub-EGFR (Umebayashi et al., 2008). Moreover, ub-EGFR had a similar distribution to that of EGFR (Figure 2—figure supplement 2B) but significantly wider than p-EGFR (Figure 2—figure supplement 2C), suggesting that the mechanisms responsible for stabilizing the mean levels of p-EGFR per endosome are not correlated with receptor ubiquitylation.

Our data suggest the existence of a saturable mechanism adjusting the amount of p-EGFR in each individual endosome. Such a constant mean amount may be due to the formation of small clusters within early endosomes. To test this possibility, we imaged the spatial distribution of p-EGFR in endosomes using the anti-EGFR phosphoTyr1068 antibody by super-resolution microscopy. Using direct Stochastic Optical Reconstruction Microscopy (dSTORM) (Lampe et al., 2012), we could indeed visualize clusters of p-EGFR (Figure 2D, left panel) that decreased in size between 10 and 30 min of EGF internalization, in agreement with the narrowing of p-EGFR distribution over time (Figure 1D). To determine the number of molecules in the clusters, we used two methods. First, we developed a new method to estimate the number of fluorescent molecules in light microscopy images by measuring the intensity fluctuations during photo-bleaching over time (for details see ‘Materials and methods’ and Figure 2—figure supplement 3). Based on the fluorescence signal from the anti-phosphoTyr1068 antibody and EGFR-GFP, we estimated an average of 102 ± 38 and 76 ± 29 (Mean ± SEM) molecules of EGFR and p-EGFR per endosome 30 min after EGF (10 ng/ml) internalization (Figure 2—figure supplement 3), corresponding to 707 ± 265 and 527 ± 202 molecules per μm3 of endosomal volume (apparent, assessed by light microscopy), respectively. A hundred EGFR molecules would require ∼12 clathrin-coated vesicles for delivery to endosomes (see ‘Materials and methods’). We also estimated the total number of GFP-EGFR per cell and found values (29,000) well in agreement with previous estimates for HeLa cells (see ‘Materials and methods’ and Figure 2—figure supplement 1A,B). Second, based on the size of receptor from the PDB database (structure ID: 3NJP), we calculated that 83 ± 25 (Mean ± SEM, N = 1456) receptors could fit in the apparent area of p-EGFR visualized by dSTORM, a value which is remarkably in agreement with the fluorescence intensities estimates.

To further validate that the constant mean amount of p-EGFR per endosome corresponds to receptor clusters, we performed a focused RNAi screen on established components of the endosomal receptor sorting machinery (CHLCb, CHLCa, Hip1, Hip1R, Htt, Tom1, Tollip, Tom1L1, Tom1L2, Hrs, Snf8, Vps24). We found that only Hrs depletion resulted in a continuous accumulation of p-EGFR in endosomes with time (Figure 2E). At the same time, the p-EGFR intensity distribution widened similar to that of total EGFR (Figure 2—figure supplement 4A,B). The silencing of Hrs also caused an increase in the size of p-EGFR clusters within each endosome as revealed by dSTORM (Figure 2D, right panel). Interestingly, this is not due to the inhibition of ILV formation, as down-regulation of Snf8 and Vps24, members of the ESCRT-II and ESCRT-III complexes, respectively (Piper and Katzmann, 2007), reduced the sequestration of EGFR into the endosomal lumen (Figure 2—figure supplement 4D) but did not have significant effects on the amount of p-EGFR per endosome (Figure 2E, blue and green curves). Thus, the constant mean amount of p-EGFR in endosomes likely corresponds to the receptor clusters observed by super-resolution microscopy. This raises the question of whether p-EGFR can be accessible to downstream signalling components. Therefore, we measured the recruitment of a direct downstream effector of p-EGFR, Shc1. The kinetics of Shc1 recruitment to endosomes precisely mimic the kinetics of p-EGFR (Figure 2—figure supplement 5) arguing that the p-EGFR clusters are signalling competent.

Upon internalization, EGF enters the early endosomal network and, similar to LDL (Rink et al., 2005), following endosome homotypic fusion and fission reactions, accumulates in few large endosomes prior to transfer to late endosomes. A mechanism must exist that prevents the continuous accretion of p-EGFR upon endosome fusion. A simple mechanism could be that the de-phosphorylation rate increases with the increase in p-EGFR per endosome. When two endosomes fuse, the resulting endosome should contain the sum of EGFR and p-EGFR of the original endosomes. However, given such de-phosphorylation rate dependency, the amount of p-EGFR would return to the level prior to fusion, thus stabilizing the mean amount of p-EGFR per endosome. A prediction of this hypothesis is that the kinase activity of EGFR in endosomes controls its own dephosphorylation. To test this, we inhibited the EGFR kinase activity pharmacologically with AG1478, lapatinib or gefitinib 10 min after EGF stimulation (to prevent alterations on receptor internalization) and determined the effects on the receptors already internalized and phosphorylated. We compared low with high concentrations of EGF, that is, under conditions of saturation of p-EGFR packaging in endosomes (Figure 1—figure supplement 8). At low EGF concentrations, when the packaging mechanism is not saturated, the total amount of p-EGFR was not significantly reduced by the inhibitors (Figure 2—figure supplement 6 compare black and green curves). This behaviour argues that the packages of p-EGFR in endosomes are protected from the phosphatases. In addition, the inhibitors caused a continuous accumulation of p-EGFR in fewer and larger endosomes over time (Figure 2—figure supplement 7). In contrast, adding the inhibitor after stimulation with high concentrations of EGF caused a sharp reduction in the total amount of p-EGFR (Figure 2—figure supplement 6 compare red and blue curves), as observed previously (Kleiman et al., 2011). This means that the kinase activity of EGFR is necessary to maintain the levels of p-EGFR in individual endosomes. These results support the idea that the dephosphorylation of p-EGFR in endosomes indeed depends on the EGFR activity within the endosomal packages.

Which phosphatases are responsible for controlling p-EGFR packaging in endosomes? To identify them, we performed a focused RNAi screen against 21 protein tyrosine phosphatases (PTP) expressed in HeLa cells (Tarcic et al., 2009). Hits were defined if silencing satisfied three conditions: (1) it increased the total amount of p-EGFR in endosomes and (2) increased the mean amount of p-EGFR per endosome, and (3) the phenotype was observed with at least two siRNAs per gene. Five phosphatases, PTP4A1, PTPN11, PTPN9, PTPN18, and PTPRK, increased the amount of p-EGFR in individual endosomes (Figure 2F and Figure 2—figure supplement 8). Interestingly, PTPN11 is an EGFR interactor (Deribe et al., 2009) whose activity is enhanced upon tyrosine phosphorylation (Agazie and Hayman, 2003), suggesting a molecular mechanism whereby p-EGFR could regulate its own de-phosphorylation in endosomes.

What are the consequences of such mechanism for signal transduction? To address these questions and generate testable predictions, we developed a mathematical model that describes the amount of total intracellular p-EGFR over time. Previously, excellent models have been developed that quantitatively describe EGFR endocytosis and signalling (Felder et al., 1992; French et al., 1994; Kholodenko et al., 1999; Kholodenko, 2002; Resat et al., 2003). However, although all these models described in detail the dynamics of ligand binding, dimer formation and endocytosis, recycling and degradation of the receptor, they did not consider the trafficking dynamics of the phosphorylated receptors with respect to the dynamics of the endosomal network because these data were not available. Our new experimental data brought two new concepts. First, dephosphorylation and degradation of p-EGFR occur sequentially but are uncoupled. Second, the amount of p-EGFR is controlled at the level of individual endosomes. These new concepts require further development of the existing EGFR mathematical models. Our model was formulated as a set of ordinary differential equations (ODE, see ‘Materials and methods’ and Figure 3) describing (1) the total amount of EGFR and p-EGFR at the plasma membrane as a function of ligand binding, (2) endocytosis of p-EGFR and its indirect effects on EGFR endocytosis, and (3) distribution of cargo between early endosomes at different stages of maturation (e.g., formation of MVB). For this, we considered the processes of receptor internalization, dephosphorylation, degradation, recycling, endosome fusion and fission. As in previous models (French et al., 1994; Resat et al., 2003), we described time course kinetics of total cellular p-EGFR, surface and endosomal EGFR and p-EGFR. Importantly, our model also describes the total number of p-EGFR-positive endosomes and mean amount of p-EGFR per endosome (see ‘Materials and methods’ for details). To account for the observed stabilization of the mean amount of p-EGFR per endosome over time (Figure 1), the dependency of p-EGFR dephosphorylation on EGFR kinase activity (Figure 2—figure supplement 6,7) and the fact that the mechanism is saturable (Figure 1—figure supplement 8), we included a sigmoidal dependency of the p-EGFR dephosphorylation rate on the amount of p-EGFR per endosome. The model was then fitted to the experimental data from the p-EGFR time course (Figure 3A,B). Figure 3C shows that this simple theoretical model can reproduce our observations of a constant mean amount of p-EGFR per endosome in a wide range of EGF concentrations when fitted to the experimental data. Importantly, a model without this non-linear dephosphorylation dependency could correctly describe the total amount of EGFR and p-EGFR in endosomes (Figure 3—figure supplement 1A,B) but did not agree with the measurements for the mean amount of p-EGFR per endosome (Figure 3—figure supplement 1C), thus supporting the sigmoidal dependency of the p-EGFR de-phosphorylation rate on the amount of p-EGFR per endosome (Figure 3). Previous models did not include this non-linear term because data on the distribution of p-EGFR in individual endosomes was not available.

![Figure 3.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig3-v2.jpg)

**Figure 3.:** Parameters of the mathematical model were fitted to the experimentally measured number of p-EGFR endosomes, total integral intensity of p-EGFR, mean integral intensities of p-EGFR per endosome and total vesicular EGFR. The experimental data were obtained in a time course of EGF stimulation at four concentrations (0.5, 1.0, 5.0, and 10 ng/ml, colour coded as indicated). The fit results are presented on panels (A–C). The experimental data and model predictions are drawn as filled circles and solid curves, respectively. (A) Number of p-EGFR endosomes per 1000 μm2 of cell area. (B) Total integral intensity of p-EGFR measured by FRET. The scaling factors that convert arbitrary numbers of the model to the experimental data were found by the least square procedure (see ‘Materials and methods’). (C) Comparison of mean integral intensity of p-EGFR per endosome measured experimentally (filled circles) and mathematical model (solid curves) of the time course of p-EGFR upon EGF stimulation as in Figure 1A. The concentration of EGF is colour coded as presented. (D) Model predictions of the total amount of p-EGFR in endosomes as a function of EGF concentration and in the presence of different homotypic early endosome fusion rates (colour coded as indicated).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Parameters of a mathematical model with a first-order dephosphorylation rate were fitted to the experimental data as in Figure 3. (A) Total integral intensity of EGFR. (B) Total integral intensity of p-EGFR measured by FRET. (C) Mean integral intensity of p-EGFR per endosome. The experimental data and model predictions are drawn as filled circles and solid curves, respectively.

An unexpected prediction of our model is that the total de-phosphorylation rate, and thus the total amount of p-EGFR, is dependent on the fusion/fission rate of the endosomes (Figure 3D). If so, could this have an effect on signal transduction? To test these hypotheses, we reduced early endosome homotypic fusion by lowering the intracellular concentration of established components of the endosome tethering and fusion machinery, EEA1, Rabenosyn5, Vps45 (Christoforidis et al., 1999; Ohya et al., 2010), Syntaxin-6 and Syntaxin-13 (Brandhorst et al., 2006) that play no direct role in signalling. These genes were down-regulated by RNAi in combinations and only partially (∼50–70% depletion for each protein, Figure 4A) to achieve a significant inhibition of endosome fusion and yet prevent or reduce cell toxicity. This procedure caused a mild redistribution of EGFR to endosomes of smaller size (<0.5 μm2 cross-section area, for details see ‘Materials and methods’ and Figure 6—figure supplement 2) (Figure 4C,D). Similar results were obtained upon depletion of a second combination of genes (EEA1, Stx13, Stx6, not shown, see below). Note that these treatments generated a pattern of endosomes similar to that observed in different cell types and under different culture conditions (see below, Figure 6) and neither altered the surface levels of EGFR (Figure 4—figure supplement 1) nor its kinetics of uptake (Figure 4B) and exit from endosomes, that is, recycling and degradation (Figure 4—figure supplement 2). We also excluded potential effects on endosome acidification, because blocking it with bafilomycin did increase both p-EGFR and total EGFR (Figure 4—figure supplement 3). Remarkably, under our experimental conditions of mild down-regulation of the early endosomal fusion machinery the packaging of active receptors was unaffected as shown by both the time course and the steady-state mean (constant) amount of p-EGFR per endosome (Figure 4E; see above, Figure 1B). In contrast, the total number of endosomes with p-EGFR and their life-time augmented (Figure 4F), resulting in a net increase in the total amount and life-time of p-EGFR (Figure 4G). Notably, reduction of the endosome fusion rate in the mathematical model (∼40%, in line with the depletion of tethering proteins, Figure 4A) is sufficient to reproduce fairly well the experimental increase in p-EGFR endosomes observed (Figure 4F). These results support the hypothesis that EGFR activation can be modulated by the endosomal system. Since p-EGFR de-phosphorylation precedes EGFR degradation (see above, Figure 1A, Figure 2—figure supplement 2) and EGFR degradation is unaffected (Figure 4B, Figure 4—figure supplement 2), we deduce that the effect on the life-time of p-EGFR caused by reduced endosomal fusion is primarily due to reduced de-phosphorylation.

![Figure 4.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig4-v2.jpg)

**Figure 4.:** (A) Protein down-regulation of EEA1 and Rabenosyn5 72 hr after siRNA transfection. RT-PCR showed an 80% reduction in Vps45 mRNA levels (data not shown). (B) Time course of EGFR integral intensity in endosomes after partial protein depletion of EEA1, Rabenosyn5, and Vps45 (red curve) or mock treatment (black curve). Cells were given a 1-min pulse of 10 ng/ml EGF, washed and chased for the indicated time points before fixation. (C) Representative images of HeLa EGFR BAC cells after EEA1, Rabenosyn5, and Vps45 knock-down or treatment with transfection reagent only (mock). Scale bars, 10 μm. (D) Shift in the EGFR-endosome area distribution toward smaller endosomes after EEA1, Rabenosyn5, and Vps45 knock-down. The values of the histograms of endosome area distribution for the control and knock-down conditions were normalized and subtracted. The curve shows the relative increase (above zero) or reduction (below zero) in the number of endosomes for each area bin (in logarithmic scale) (for details see ‘Materials and methods’ and Figure 6—figure supplement 2). Experimental points were fitted with two log-normal distributions. (E–G) Changes in p-EGFR endosomes in EEA1, Rabenosyn5, and Vps45 knock-down (red curve) or mock-treated (black curve) cells after continuous stimulation with 10 ng/ml EGF. Time courses of the mean integral intensity of p-EGFR per endosome (E), mean number of p-EGFR endosomes determined experimentally (squares) or predicted by the mathematical model (solid curves) for a 37% endosomes fusion rate (red curve) compared to control (black curve) (F), and total p-EGFR integral intensity in endosomes (G) measured as in Figure 1. Intensity curves were normalized to the intensity value at 10 min for mock-treated cells. Experimental points show mean ± SEM. All measurements were done in three independent experiments with a total of ∼150 cells per time point or condition. Time courses were fitted as in Figure 1.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Cells were stimulated with 100 ng/ml EGF-AlexaFluor 488 for 10 min on ice to prevent receptor endocytosis. The AlexaFluor 488 signal was enhanced by detection with a specific antibody to detect the amount of EGFR at the plasma membrane. Scale bar, 10 μm. (A) Representative images of HeLa EGFR BAC cells after EEA1, Rabenosyn5, and Vps45 knock-down or treatment with transfection reagent only (mock). (B) Total intensity of EGF-AlexaFluor 488 (Mean ± SEM) in knock-down or control cells. The total intensity was normalized to the fraction of the area covered by cells. Measurements were done in three independent replicates with a total of ∼150 cells per time point or condition.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A–B) Time course of EGFR degradation after partial protein depletion of the three endosomal fusion components EEA1, Rabenosyn5, and Vps45 or mock treatment and continuous stimulation with 10 ng/ml EGF for the indicated times in the presence of 10 μg/ml cyclohexamide in HeLa EGFR BAC cells. (A) Representative EGFR and γ-Tubulin Western blots and (B) their quantification for EEA1, Rabenosyn5, and Vps45 knock-down (red curve) or mock-treated (black curve) samples. Points show mean ± SEM from three independent experiments. Lines are linear fits to the experimental points.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Time course of p-EGFR integral intensity in endosomes after incubation with 50 nM BafilomycinA1 (red curve) or 1% DMSO (blue curve) for 30 min and during the remaining of the time course. (B) Time course of EGFR integral intensity in endosomes after incubation with 50 nM BafilomycinA1 (red curve) or 1% DMSO (blue curve) for 30 min and during the remaining of the time course. (C) Time course of the mean p-EGFR integral intensity per endosome after incubation with 50 nM BafilomycinA1 (red curve) or 1% DMSO (blue curve) for 30 min and during the remaining of the time course. Experimental points show mean ± SEM. All measurements were done in three independent experiments with a total of ∼150 cells per time point and condition. Time courses were fitted as in Figure 1.

Increased EGFR phosphorylation results in sustained Erk signalling (Sasagawa et al., 2005; Nakakuki et al., 2010) and this leads to the phosphorylation and stabilization of the immediate early gene product c-Fos (Nakakuki et al., 2010). We asked whether the redistribution of endosomal EGFR could be sufficient to induce sustained Erk activation and c-Fos phosphorylation. Indeed, upon EGF stimulation, both the amplitude and duration of Erk1/2 phosphorylation were increased in the depleted cells compared to control (Figure 5A,B). Consistently, c-Fos phosphorylation was also higher after 30 min of EGF stimulation (Figure 5C,D). The fact that the amount and life-time of total EGFR in endosomes remained unvaried in these experiments (Figure 4B) eliminates the trivial possibility that the observed changes are due to modulation of receptor degradation.

![Figure 5.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig5-v2.jpg)

**Figure 5.:** (A–B) Time course of Erk1/2 phosphorylation after partial protein depletion of the three endosomal fusion components EEA1, Rabenosyn5, and Vps45 or mock treatment and continuous stimulation with 10 ng/ml EGF for the indicated times in HeLa EGFR BAC cells. (A) Representative phospho-Erk1/2 and Erk1/2 Western blots and (B) their quantification for EEA1, Rabenosyn5, and Vps45 knock-down (red curve) or mock-treated (black curve) samples. Points show mean ± SEM from three independent experiments. The time course was fitted as in Figure 1. (C–D) Nuclear c-Fos phosphorylation in EEA1, Rabenosyn5, and Vps45 knock-down or mock-treated cells as in (A) after 30 min of EGF stimulation. (C) Representative images of EEA1 and phospho-c-Fos immunostaining in EEA1, Rabenosyn5, and Vps45 knock-down or mock-treated cells. Scale bars, 20 μm. (D) Total intensity of nuclear phospho-c-Fos in EEA1, Rabenosyn5, and Vps45 knock-down or mock-treated cells. Bar graph shows mean ± SEM. Measurements were done in three independent experiments from a total of ∼1000 cells per condition. *p < 0.05 by a 2-tailed t-test.

The experiments on HeLa cells and the theoretical analysis raise the question of whether modulation of early endosome homotypic fusion is a general mechanism to regulate signal amplitude and duration. If this were the case, we would predict that growth factors with different signalling outputs (amplitude and duration) differentially modulate the endosomal distribution (i.e., endosome number, size, and cargo content). To test this prediction, we examined different growth factors and cellular systems. First, we used primary mouse hepatoblasts where HGF promotes their proliferation (Tanimizu et al., 2003). In these cells, HGF but not EGF elicits a sustained Erk response (Figure 6—figure supplement 1). Indeed as predicted, stimulation of hepatoblasts with HGF caused a strong shift in the distribution of early endosomes toward smaller sizes (Figure 6A, red curve Figure 6B), whereas EGF had the opposite effect (Figure 6A, green curve, Figure 6B). Second, we turned to an in vitro model of reference for cell-fate decisions, PC12 cells. In PC12 cells, EGF stimulation leads to transient Erk phosphorylation and cell proliferation, whereas NGF leads to sustained Erk phosphorylation and cell differentiation (Marshall, 1995). Consistent with our results in primary mouse hepatoblasts, NGF stimulation in PC12 cells caused a significant shift in the distribution of early endosomes toward smaller sizes compared with EGF (Figure 6C,D). Moreover, NGF itself was distributed to a larger number of smaller endosomes in comparison with EGF (Figure 6E,F). Altogether, these data argue that the modulation of endosome fusion, reflected by the changes in endosome number and size, is a general property of growth factors. These data further suggest that signalling amplitude and duration can be regulated by changes in the fusion rate of endosomes (see Table 1).

![Figure 6.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig6-v2.jpg)

**Figure 6.:** (A) Representative images of primary mouse hepatoblasts after stimulation with 10 ng/ml EGF or HGF for 30 min (B) Shift in the EEA1-positive endosome area distribution after stimulation with HGF (red curve) or EGF (green curve). The values of the histograms of endosome area distribution for growth factor stimulated and non-stimulated cells were normalized and subtracted. The curve shows the relative increase (above zero) or reduction (below zero) in the number of endosomes for each area bin (in logarithmic scale). HGF stimulation increased while EGF decreased the proportion of endosomes smaller than 0.2 μm2. (C–F) PC12 cells after stimulation for 30 min with 100 ng/ml EGF or 50 ng/ml NGF. (C) Representative images of EEA1-positive endosomes. (D) Shift in the EEA1-positive endosome area distribution after stimulation with NGF (red curve) or EGF (green curve) measured as in (B). NGF stimulation increased while EGF slightly decreased the proportion of endosomes smaller than 0.2 μm2. (E) Representative images of EGF or NGF. (F) Differences in the area distribution of endosomal NGF and EGF measured as in (B). NGF is enriched in endosomes smaller than 0.2 μm2 relative to EGF. For all graphs points show the mean ± SEM of experimental distributions. Measurements were done in three independent experiments with n ∼150 cells per condition. In all graphs, experimental points were fitted with two log-normal distributions. Image scale bars, 10 μm.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A–B) Time course of Erk1/2 phosphorylation after continuous stimulation with 10 ng/ml HGF or EGF for the indicated times in mouse primary hepatoblasts. (A) Representative phospho-Erk1/2 and Erk1/2 Western blots and (B) its quantification for HGF (red curve) or EGF (black curve) stimulation.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** The differences between two endosome area distributions are measured as follows: (1) The binned histograms of the endosome area are built from the measurements of individual vesicles with bins linear in a logarithmic scale. (2) The histograms are normalized on their integrals, i.e., histograms are scaled to have the sum of values in all bins equal to one. (3) The histogram from the control condition is subtracted from the respective histograms of interest. The relative enrichment (red lines) or depletion (black lines) in the population of vesicles is calculated by the integral over a particular area interval.

**Table 1.**
 Changes in endosome number and area


<table>
  <thead>
    <tr>
      <th>Cell type</th>
      <th>Endosome marker or cargo</th>
      <th>Growth factor</th>
      <th>Endosome number*</th>
      <th>Endosome area (μm2)</th>
      <th>Increase in number of smaller vesicles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HeLa#</td>
      <td>EGFR</td>
      <td>EGF</td>
      <td>22 ± 9</td>
      <td>0.518 ± 0.023 (control = 0.629 ± 0.029)</td>
      <td>9.53% ± 0.014 (&lt;0.4 μm2)</td>
    </tr>
    <tr>
      <td>E14.5 hepatoblast</td>
      <td>EEA1</td>
      <td>EGF</td>
      <td>−6 ± 18</td>
      <td>0.286 ± 0.02 (control = 0.294 ± 0.02)</td>
      <td>−0.91% ± 0.003 (&lt;0.3 μm2)</td>
    </tr>
    <tr>
      <td>E14.5 hepatoblast</td>
      <td>EEA1</td>
      <td>HGF</td>
      <td>18 ± 12</td>
      <td>0.276 ± 0.02 (control = 0.294 ± 0.02)</td>
      <td>2.05% ± 0.002 (&lt;0.3 μm2)</td>
    </tr>
    <tr>
      <td>PC12</td>
      <td>EEA1</td>
      <td>EGF</td>
      <td>3 ± 10</td>
      <td>0.471 ± 0.05 (control = 0.461 ± 0.05)</td>
      <td>−1.03% ± 0.01 (&lt;0.3 μm2)</td>
    </tr>
    <tr>
      <td>PC12</td>
      <td>EEA1</td>
      <td>NGF</td>
      <td>23 ± 16</td>
      <td>0.454 ± 0.05 (control = 0.461 ± 0.05)</td>
      <td>2.2% ± 0.01 (&lt;0.3 μm2)</td>
    </tr>
    <tr>
      <td>PC12</td>
      <td>EGF</td>
      <td>EGF</td>
      <td>316 ± 46</td>
      <td>0.276 ± 0.003</td>
      <td>–</td>
    </tr>
    <tr>
      <td>PC12</td>
      <td>NGF</td>
      <td>NGF</td>
      <td>341 ± 5</td>
      <td>0.245 ± 0.007</td>
      <td>5.15% ± 0.01 (&lt;0.3 μm2, difference from EGF-endosomes)</td>
    </tr>
  </tbody>
</table>

_*Endosome number is expressed as the difference from the control or non-stimulated cells. The value shows the number of endosomes per 1000 μm2 of area covered by cells.#HeLa cells after knock-down of EEA1, Rabenosyn5, and Vps45. All values show mean ± SEM._

Finally, we tested whether the differences in endosomal distribution can be, at least in part, causative of the different cell-fates triggered by EGF and NGF in PC12 cells. If so, we would predict that redistributing EGF to a larger number of small endosomes as seen in PC12 stimulated with NGF would be sufficient to switch signalling specificity and induce differentiation of PC12 cells. Therefore, we applied the same protocol of partial protein depletion previously used for HeLa cells (Figure 4) in PC12 cells and consistently observed a mild redistribution of EGF into smaller endosomes (Figure 7—figure supplement 1A,C,D). Also in this case, the partial depletion did not result in major changes in EGF transport kinetics in PC12 cells (Figure 7—figure supplement 1B), but increased the phosphorylation of both Erk (Figure 7—figure supplement 2A,B) and c-Fos (Figure 7—figure supplement 2C,D) upon stimulation with EGF. Next, we stimulated PC12 cells with EGF or NGF for 24 hr and analysed for neurite formation and β-III tubulin expression as markers of differentiation (Ohuchi et al., 2002) and for EdU incorporation as a measure of proliferation (Figure 7A). Stimulation with NGF increased the number of cells with neurites (Figure 7B, quantification in Figure 7C) and positive for β-III tubulin (Figure 7B, quantification in Figure 7D), and reduced cell proliferation (Figure 7A, quantification in Figure 7E), the opposite of the stimulation with EGF. Remarkably, upon redistribution of endosomes, EGF increased process formation (Figure 7B, quantification in Figure 7C), β-III tubulin expression (Figure 7B, quantification in Figure 7D), and reduced cell proliferation (Figure 7A, quantification in Figure 7E). The type of response was therefore similar to that of NGF, although the efficacy was lower. Nevertheless, these results show that a mild reduction of homotypic early endosome fusion was sufficient to modify cell fate and induce neuronal differentiation of PC12 cells.

![Figure 7.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig7-v2.jpg)

**Figure 7.:** (A–B) Representative images of PC12 cells after partial protein depletion of either EEA1, Rabenosyn5, and Vps45 or EEA1, Syntaxin-6, and Syntaxin-13, or mock treatment and stimulation with 100 ng/ml EGF or 50 ng/ml NGF for 24 hr. Scale bars, 50 μm. (B) A high-resolution image of single cells to highlight the changes in β-III tubulin expression and neurite formation. β-III tubulin is shown in green, nuclei are shown in blue, and EdU-positive nuclei are shown in pink. Scale bars, 10 μm. Note that in Figure 6C,E, the short incubation times did not permit neurite outgrowth. (C) Increase in the number of cells with β-III tubulin-positive processes longer than 1 μm compared to mock-treated cells after EGF stimulation. (D) Increase in β-III tubulin expression measured by the total intensity of the cytoplasmic β-III tubulin immunostaining. The total intensity per image was normalized by the image area covered by cells. (E) Number of proliferating cells measured by EdU incorporation. The number of EdU-positive nuclei was divided by the total number of nuclei. In all cases, data show mean ± SEM. For each parameter, pair-wise comparisons were done against EGF-stimulated mock-treated cells. *p < 0.05, **p < 0.005 by Fisher's LSD test. All measurements were done in three independent experiments with a total of ∼15000 cells per condition.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A) Partial protein depletion of Syntaxin-6 and Syntaxin-13 72 hr after electroporation. Protein reduction of EEA1 and Rabenosyn5 was similar to that in HeLa cells (not shown). (B) Time course of EGF integral intensity in endosomes after EEA1, Rabenosyn5, and Vps45 (red curve) or EEA1, Syntaxin-6, and Syntaxin-13 knock-down (blue curve) or mock treatment (black curve). Cells were given a 1-min pulse of 100 ng/ml of EGF-AlexaFluor 555, washed and chased for the indicated time points before fixation. Curves were normalized to the intensity value at 10 min for mock-treated cells. Points show mean ± SEM. All measurements were done in three independent replicates with a total of ∼150 cells per time point or condition. Time courses were fitted as in Figure 1 (C–D) Shift in the EGF-endosome area distribution after EEA1, Rabenosyn5, and Vps45 (C) or EEA1, Syntaxin-6, and Syntaxin-13 (D) knock-down measured as in Figure 3. Endosomes smaller than 0.2 μm2 (cross-sectional area) are increased after EEA1, Rabenosyn5, and Vps45 (C) or EEA1, Syntaxin-6, and Syntaxin-13 knock-down (D). Points show the mean ± SEM. All measurements were done in four independent replicates with a total of ∼200 cells per time point or condition. Experimental points were fitted with two lognormal distributions.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/06156/elife-06156-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** (A–D) Analysis of MAPK activation in PC12 cells after partial protein depletion of either EEA1, Rabenosyn5, and Vps45 or EEA1, Syntaxin-6, and Syntaxin-13, or mock treatment and stimulation with 100 ng/ml EGF or 50 ng/ml NGF for 30 min (A) Representative images of Erk1/2 activation by immunofluorescence in PC12 cells. phospho-Erk1/2 is shown in green and nuclei are shown in blue. Scale bars, 10 μm. (B) Increase in phospho-Erk1/2 intensity compared to EGF-treated control cells. The total intensity was normalized by the fraction of the area covered by cells. (C) Representative images of c-Fos phosphorylation by immunofluorescence in PC12 cells. phospho-c-Fos is shown in green. Scale bar, 25 μm. (D) Increase in nuclear phospho-c-Fos intensity compared to EGF-treated control cells. In all cases, data show mean ± SEM. For each parameter, pair-wise comparisons were done against EGF-stimulated mock-treated cells. *p < 0.05, **p < 0.005 by Fisher's LSD test. All measurements were done in three independent experiments with a total of ∼500 cells per condition.

## Discussion

Genomic studies have revealed that signalling pathways exert a profound effect on the endosomal system (Pelkmans et al., 2005; Stasyk et al., 2007; Collinet et al., 2010). Parameters such as number of endosomes and size are tightly controlled in the case of EGF endocytosis (Collinet et al., 2010). Our results provide a rationale for such modulation and a novel framework for interpreting and predicting the signalling response of phosphorylated RTKs. In homogeneous assays (e.g., by Western blot), the total levels of active RTKs can be observed to rapidly decay with time in most signalling systems (Dunn and Hubbard, 1984; Burke et al., 2001; Sousa et al., 2012). These methods, however, measure the average steady state of an entire cell population and lack the spatial information. Here, we employed quantitative high- and super-resolution microscopy to resolve details of this process with sub-cellular resolution and high sensitivity. We discovered that the mean amount of p-EGFR per endosome was fairly constant over time and p-EGFR was found in small clusters in early endosomes.

The endosomal network is shaped by the balance of endosome fusion and fission (Foret et al., 2012) and this balance is also necessary for the formation of the endosomal clusters of p-EGFR. Modulation of the endosomal fusion/fission machinery manifests itself as a change in the size of endosomes (Sigismund et al., 2008) (Figure 6). Shifting the balance toward smaller endosomes through inhibition of fusion increased the number and reduced the size of endosomes, consequently expanding the number and life-time of p-EGFR clusters. Although the inhibition of endosome fusion was very mild, we cannot exclude the possibility that it may alter the recruitment and/or activity of signalling components by yet unknown mechanisms. On the other hand, for the interpretation of phenotypes upon perturbations on signalling, it is also important to consider the impact they have on the endosomal network (Collinet et al., 2010).

By analogy with synaptic transmission (Edwards, 2007), the packages of p-EGFR in early endosomes could be considered as quanta of signalling molecules. The concept of phosphorylated RTK quanta is reminiscent of analogue-to-digital communication systems, where a continuous variable (e.g., extracellular growth factor concentration) is transformed into a sequence of binary levels (e.g., phosphorylated RTK quanta in endosomes). An analogue-to-digital switch was described for Ras nanoclusters at the plasma membrane (Tian et al., 2007). In the case of endosomal digital signalling, our mathematical model predicts that it could serve two functions. First, it provides a mechanism to regulate signal amplitude and duration following RTK internalization. As a consequence, the total de-phosphorylation rate becomes dependent on the fusion/fission rate of the endosomes. This is interesting in view of the specific modulation of the endosome fusion/fission rates by growth factors (Figure 6, see below). Second, it acts as a noise dampening system (Ladbury and Arold, 2012), suppressing the noise due to, for example, fluctuations of EGF in the extracellular medium, expression levels of EGFR on the cell surface, etc. An increase in the amount of p-EGFR would result in faster de-phosphorylation rates. In contrast, low concentrations of EGF or EGFR would result in low de-phosphorylation rates. The middle point between the two extremes is the hallmark of signalling resilience. In addition, such a digital system may facilitate the integration of signalling information from different RTKs into a single, correct cell-fate decision. Our results highlight the importance of measuring the spatio-temporal distribution of signalling molecules using quantitative image analysis approaches to gain a deeper understanding of signal transduction regulation.

What is the molecular machinery responsible for the formation of the clusters and how is the number of p-EGFR molecules regulated? Clearly, the clustering mechanism is saturable (Figure 2A,B), as very high concentrations of EGF above some threshold suppress the correct endosomal packaging in addition to changes in the entry routes and signal output (Sigismund et al., 2008). We found that both Hrs and a few phosphatases, notably PTPN11 (SHP2), specifically regulate the amount of receptors within the p-EGFR clusters and their size. Hrs is known to interact with EGFR and regulate its degradation together with other components of the ESCRT machinery (Umebayashi et al., 2008). However, the effect of Hrs on the size of the p-EGFR clusters appears to be independent of the formation of ILVs, as suggested by the fact that Snf8 and Vps24 down-regulation does not produce the same effect.

Our mathematical model revealed that a correlation between p-EGFR dephosphorylation rate and p-EGFR amount per endosome can explain the mean constant size of p-EGFR quanta. We can envisage various non-exclusive mechanisms that can account for this correlation. One possible mechanism is a scaffold with a characteristic size that binds to p-EGFR and protects it from phosphatases. This hypothesis correlates higher total EGFR kinase activity to higher p-EGFR dephosphorylation, but only indirectly. Increasing the concentration of EGF in the medium would lead to a higher rate of delivery of p-EGFR to endosomes through vesicles which have no scaffold. If scaffold formation were rate limiting, the increased flux of p-EGFR into endosomes would reduce the fraction of protected p-EGFR thus exposing it to dephosphorylation. A caveat of this model is that, as the fusion of endosomes proceeds over time, multiple quanta would be expected to be brought together, increasing the mean amount of p-EGFR per endosome. This expectation is in contradiction with our experimental data (Figure 1B,D). With this model, additional factors must thus be taken into account to explain why multiple quanta cannot co-exist on the same endosomes.

The finding that Hrs knock-down increases the levels of p-EGFR suggests a different scaffold-based model. Instead of acting as a p-EGFR protective scaffold (or part of a scaffold), Hrs could exert the opposite function and stabilize the unphosphorylated EGFR, preventing its re-phosphorylation (Kleiman et al., 2011). Since the activity of Hrs is negatively regulated by p-EGFR (Row et al., 2005; Bache et al., 2002), this model is compatible with the data showing loss of quanta and increase in endosomal p-EGFR levels upon Hrs knock-down (Figure 2D,E). However, this hypothesis alone can neither explain the formation of quanta nor the finding that blocking p-EGFR kinase activity does not change the total levels of p-EGFR over time (Figure 2—Figure supplement 6).

Another mechanism is based on Turing Instability (Turing, 1952) (a reaction-diffusion mechanism). This mechanism is perhaps less intuitive but widely spread in biological processes, such as symmetry breaking and pattern formation in morphogenesis (Kondo and Miura, 2010). It is based on the observation that p-EGFR recruits and phosphorylates PTPN11 (SHP2) in a phosphor-tyrosine dependent manner (Deribe et al., 2009), thus enhancing its phosphatase activity (Agazie and Hayman, 2003). Briefly, p-EGFR would recruit and activate the phosphatase SHP2, forming a negative feedback loop. The phosphatase would diffuse on the surface of endosomes, dephosphorylating p-EGFR molecules before being itself inactivated in the absence of further interactions with p-EGFR. Such reaction-diffusion mechanism within a specific parameter range is known to form spatially restricted clusters of active molecular species (Turing Instability) (Turing, 1952), in this particular case quanta of p-EGFR on endosomes. A transient increase in p-EGFR after an endosome fusion event would increase the recruitment and/or activity of SHP2, re-establishing the p-EGFR quanta through dephosphorylation. If the characteristic length of Turing Instability is larger than endosome size, then multiple quanta cannot co-exist within a single endosome. The Turing Instability hypothesis explains the observed increase in p-EGFR quanta size after EGFR kinase inhibition, keeping the total p-EGFR levels unchanged (Figure 2—figure supplement 6,7), as well as the increase in total endosomal p-EGFR upon inhibition of endosome fusion (Figure 4G). However, it does not explain the effect of Hrs knock-down. A combination of the Turing instability and Hrs-mediated (negative) scaffold mechanisms is more consistent with our observations.

The regulation of endosomal packing reported in our study is likely not restricted to EGFR alone but is a general property, as different growth factors affect the endosomal network according to their specific signal output and cellular context (Figure 6). Hrs and SHP2 are also recruited by other RTKs (Agazie and Hayman, 2003; Row et al., 2005). The relative affinity of SHP2 to different receptors could lead to larger or smaller quanta, thus tuning the specificity of the signalling response. RTK quanta with different sizes could also result from differential phosphorylation of Hrs by RTKs (Row et al., 2005), given that the relative amount of Hrs on endosomes depends on its phosphorylation state (Urbé et al., 2000).

By which mechanisms can RTKs regulate the endosomal network? It has been shown that RTKs can modulate the activity of the transport machinery. For example, activation of p38 MAP kinase causes phosphorylation of the Rab5 effectors EEA1 and Rabenosyn-5, enhancing their recruitment to endosomes and consequently stimulating early endosome fusion (Macé et al., 2005; Cavalli et al., 2001). RTK stimulation also modulates the nucleotide cycle of Rab5 via activation of the Rab5 GEF RIN1 (Tall et al., 2001) or inactivation of the Rab5 GAP RN-tre (Lanzetti et al., 2000). Therefore, we predict that in general RTK ligands that stimulate the endosomal fusion machinery (such as EGF) will have a short phosphorylation half-life, whereas ligands that change the fusion/fission balance in favour of smaller endosomes (such as NGF) will have a long phosphorylation half-life. The combined effects of quanta size regulation through Hrs and SHP2 and modulation of fusion/fission will give a specific signalling amplitude and duration in different cell types stimulated with different ligands. We propose that the shape of distribution of the endosomal network can serve as a predictive parameter of the signalling status of the cell.

Our results support the concept of endosomes as signalling platforms (Di Guglielmo et al., 1994), a view recently shared for the β2-adrenoceptor (Irannejad et al., 2013) but opposed by other studies (Brankatschk et al., 2012; Sousa et al., 2012). This apparent contradiction can be explained by the fact that, under normal conditions of endocytosis, only the small fraction of p-RTK in endosomes are protected from inactivation and degradation, and can thus contribute to signal propagation. A feature of the p-EGFR clusters is that, with the increase in the local concentration, the stability of the active EGFR dimer (Chung et al., 2010) and signalling properties (Verveer et al., 2000) would also be increased. By blocking endocytosis, the levels of active receptors are artificially increased at the cell surface (Sousa et al., 2012), bypassing the normal requirement for endosomal regulation.

Our observations raise many more questions concerning the molecular mechanisms of quanta formation and their impact on cell fate decision. Clearly, the variety of models on quanta formation requires future experimental tests to determine the correct mechanism and reveal its molecular details. In addition, it will be important to validate our observations in an in vivo animal model to demonstrate that the dynamics of the endosomal network reflect the signalling activity by RTK under physiological conditions.

## Materials and methods

### p-EGFR FRET microscopy assay

To reduce the consequences of EGFR overexpression, we used HeLa Kyoto cells transfected with a bacterial artificial chromosome (BAC) transgene stably expressing EGFR-GFP under its endogenous promoter (Poser et al., 2008). Cells were incubated for different times in serum-free medium with 10 ng/ml EGF (Invitrogen, California, USA) or for 30 min with 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 7.5, or 10 ng/ml EGF. Cells were then fixed and processed for immunofluorescence as previously described (Collinet et al., 2010) using a mouse monoclonal anti-phospho-tyrosine 4G10 antibody (Millipore, California, USA) directly labelled with AlexaFluor 555 (Molecular Probes, Invitrogen). For colocalization measurements, samples were also incubated with rabbit polyclonal anti-EEA1 (Rink et al., 2005) or mouse monoclonal anti-LAMP-1 (BD Biosciencies, California, USA) antibodies. Images were acquired using a laser-scanning confocal microscope (Duoscan, Zeiss) with a 63×/1.4 oil objective. Multicolour images were acquired in three sequential scans: GFP fluorescence and AlexaFluor 555 fluorescence were detected simultaneously with two different detectors using 488 and 561 nm laser light and a 505/530 band-pass filter or a 593 nm long-pass spectral range in a META detector (Zeiss); FRET signal was detected with 458 nm excitation and a 593 nm long-pass spectral range in a META detector (Zeiss). 10 images per time point were collected, and each image was the maximum projection of four confocal sections of ∼1 μm thickness with 0.5 μm step. For the comparison between live and fixed cells, images were acquired with an automated spinning-disk confocal microscope (OPERA, Evotec Technologies-PerkinElmer) with a 40×/0.9 NA water immersion objective. EGFR-GFP was excited with a 488 nm laser and detected with a 520/35 nm filter. DAPI for nuclei identification was excited in a separate exposure with a 405 nm laser and detected a 450/50 nm filter. Eighty images per condition were acquired. Every image contained on average 20 cells.

Image analysis was performed using custom designed image analysis software (MotionTracking) as previously described (Rink et al., 2005; Collinet et al., 2010). The ‘integral intensity’ corresponds to the integral of fluorescent marker intensity per endosome. The ‘total integral intensity’ is defined as the sum of integral intensities of all endosomes in an image normalized by the area covered by the cells. The ‘endosome cross-sectional area’ was measured as the apparent fluorescent area (in µm2) of an endosome (above the half-maximum value of fluorescence intensity of each structure). Since MotionTracking approximates real image intensity by a sum of analytical functions (Rink et al., 2005), the resulting area and intensity have no pixel granularity.

### High-resolution microscopy FRET-based assay

p-EGFR or ub-EGFR was first identified on the basis of triple colocalization between objects detected by the EGFR (488 nm laser excitation and 505/530 nm bandpath emission filter), anti-p-Tyr antibody p-Tyr-ab for p-EGFR or anti-mono and polyubiquitynilated conjugates (FK2) (Enzo Biosciences, New York, USA) (561 nm laser excitation and a 593 nm long-pass filter), and FRET (458 nm laser excitation and a 593 nm long-pass filter) channels (Figure 1—figure supplement 1A). Colocalization was scored by cross-sectional overlap >30%. The FRET signal was corrected for spectral bleed-through (SBT). Two major processes contribute to the SBT: (1) the GFP fluorescence bleed-through in the FRET channel and (2) direct excitation of AlexaFluor 555 by the 458 nm laser. We performed control experiments to estimate SBT for subsequent correction. To estimate GFP fluorescence bleed-through, we imaged EGFR-GFP BAC HeLa cells in the FRET channel (excitation 458 nm) without p-Tyr-ab staining. The signal in the FRET channel was below our detection limit and, therefore, we omitted correction in the subsequent analysis. The SBT by direct excitation of AlexaFluor 555 was estimated by quantification of FRET vesicles that colocalized with p-Tyr-ab or ub-ab, but not with EGFR (bleed-through control). Following the approach of Gordon et al., (1998), the correction in this case will be,

$$
F=I−k·T,
$$

where F is the corrected intensity in the FRET channel, I is the raw intensity in the FRET channel, T is the intensity in the p-Tyr-ab channel, $k=\frac{<I_{control}>}{<T_{control}>}$ is the bleed-through coefficient (ratio of means) calculated from control vesicles. Unfortunately, this correction method provided a good estimation of the average FRET signal, but when applied to individual endosomes it gave negative intensities for a substantial (30–40%) number of cases, thus precluding the estimation of mean intensity per endosome. In order to identify the source of negative intensities, we calculated the distribution of ratios of intensities in the FRET channel to the intensities in the p-Tyr-ab channel per endosome (Figure 1—figure supplement 1B). This distribution is broad and one can conclude that correction by Equation 1 will inevitably produce negative values in some cases. We fitted the distribution by the sum of three Gaussian components (Figure 1—figure supplement 1B, red, green, and blue dashed lines). By using control cells that did not express EGFR-GFP, we tested that the first two components correspond to SBT (direct excitation of AlexaFluor 555 by the 458 nm laser). Next, we developed a probabilistic model to find the expected FRET signal, given the p-Tyr-ab signal and the constants (µ, σ) of Gaussian distribution of the intensities ratios. The distribution of ratios is $P(m)dm=\frac{1}{\sqrt{2\pi}\sigma}e^{−\frac{(m−\mu)^{2}}{2\sigma^{2}}}dm$. We denoted $m=\frac{I−F}{T}$ the ratio of bleed-through signal in the FRET channel to the signal in the p-Tyr-ab channel for individual endosomes. After this substitution, the probability to obtain a FRET signal F is $P(F)dF=P(m(F))\frac{dm}{dF}dF=\frac{1}{\sqrt{2\pi}\sigmaT}exp(−\frac{(F−(I−\muT))^{2}}{2\sigma^{2}T^{2}})dF$. Since the bleed-through cannot be higher than the measured signal I, we can calculate the expectation of the FRET signal as: $〈F〉=\frac{\int_{0}^{I}F·P(F)dF}{\int_{0}^{I}P(F)dF}$. After substitution and integration, we get:

$$
〈F〉=I−\muT+\sqrt{\frac{2}{\pi}}\sigmaT\frac{(1−e^{−\frac{1}{2}(\frac{\mu}{\sigma})^{2}})−sgn(I−\muT)·(1−e^{−\frac{1}{2}(\frac{I−\muT}{\sigmaT})^{2}})}{erf(\frac{\mu}{\sqrt{2}\sigma})+erf(\frac{I−\muT}{\sqrt{2}\sigmaT})}.
$$

One can see that (a) if I − µT > 0 (i.e., SBT is small relative to the true FRET signal), then the last term in the formula is very small and $〈F〉≈I−\muT$ in agreement with Gordons' formula; (b) even if I − µT < 0 (i.e., SBT is large relative to the true FRET signal or the FRET signal is absent), the Equation 2 always gives small, but positive values. As such, Equation 2 provides a good estimation of the expected FRET intensity given the measured intensities in the FRET and p-Tyr-ab channels.

Next, we developed this approach further by taking into account that the real bleed-through distribution is the sum of two Gaussians with mean values µ1, µ2, standard deviations σ1, σ2 and their contribution in the total distribution a1, a2. Following the same approach as above we get:

$$
〈F〉=I−(a_{1}\mu_{1}+a_{2}\mu_{2})T+\sqrt{\frac{2}{\pi}(a_{1}^{2}\sigma_{1}^{2}+a_{2}^{2}\sigma_{2}^{2})}T\frac{(1−e^{−M})−sgn(N)·(1−e^{−N^{2}})}{erf(\sqrt{M})+erf(N)},
$$

where $M=(\frac{\mu_{1}}{\sqrt{2}\sigma_{1}})^{2}+(\frac{\mu_{2}}{\sqrt{2}\sigma_{2}})^{2}$ and $N=\frac{I−(a_{1}\mu_{1}+a_{2}\mu_{2})T}{\sqrt{2(a_{1}^{2}\sigma_{1}^{2}+a_{2}^{2}\sigma_{2}^{2})}T}$.

The example of FRET correction by Equation 3 is presented on Figure 1C.

To validate the FRET measurements, cells were treated with EGF, stained using a rabbit monoclonal anti-p-EGFR (Tyr 1068) antibody, and imaged using a laser-scanning confocal microscope using the same protocols as described above.

### EGFR and p-EGFR single molecule quantification

EGFR-GFP BAC cells were incubated with 10 ng/ml EGF for 30 min, fixed and stained with the rabbit monoclonal anti-p-EGFR (Tyr 1068) antibody as described above. One field of view was sequentially acquired to record bleaching of GFP and fluorescently labelled secondary antibodies. The resulting time series was segmented with MotionTracking as described above, individual objects were tracked for consecutive frames, and the fluorescence intensity of every endosome between two consecutive frames was subtracted to build the ΔIntensity distribution (Figure 2—figure supplement 3A,C). The width of distribution is mostly determined by the fluctuations of intensities. However, due to bleaching, the distribution is slightly skewed toward negative values. First, the ΔIntensity was binned. Then the difference between frequencies of negative and positive ΔIntensity of equal absolute values was plotted as function of ΔIntensity (Figure 2—figure supplement 3B,D). We named it neg-double-difference function. Since every bin of neg-double-difference function in the vicinity of the first peaks contained ∼2500 events, random fluctuations were strongly suppressed and the averaging revealed the discrete structure of bleaching, that is, bleaching of individual molecules. The local amplitude positive maxima correspond to discrete intensity changes when 1, 2, 3, …, n molecules are bleached (see e.g., arrows on peaks at 280, 560, and 800 integral intensity units in Figure 2—figure supplement 3B). We estimated that one molecule of GFP and alexa555-antibody corresponds to the integral intensity units at the first peak of the neg-double-difference function (280 and 190 integral intensity units for EGFR-GFP and alexa555, respectively). This method estimated directly the number of EGFR-GFP molecules. The total number of EGFR molecules per endosome was corrected for the ratio of endogenous and BAC EGFR-GFP expressions (1.29 ± 0.07, based on WB quantification). Since the method estimated the number of fluorophores, in the case of antibodies with unknown labelling stoichiometry and epitope accessibility, the result has to be corrected for a scaling factor. The scaling factor of antibody labelling was estimated as 1.9 by comparison of EGFR and p-EGFR distributions at 3 and 5 min of EGF stimulation (10 ng/ml), when most internalized EGFR are still phosphorylated (Sorkin and Goh, 2009), with distributions at 30 min.

We used this fluorescence intensity-based method also to estimate the number of EGFR molecules in both clathrin-dependent and independent vesicles. From geometrical calculations, assuming that an uncoated CCV has a diameter of 90 nm and an EGFR dimer has a diameter of ∼15 nm and luminal domain of ∼10 nm, we estimate that a CCV can contain up to 70 EGFR molecules. However, this calculation does not take into account that vesicles contain multiple types of transmembrane proteins and thus, the value can only be an upper limit. Therefore, we estimated the number of EGFR molecules per diffraction-limited, EEA1-negative vesicle that can be observed following 5 min of 10 ng/ml EGF stimulation. Using this method, we estimated 8.5 ± 3.5 molecules/vesicle. Based on this value, we calculated that ∼12 vesicles are required to deliver the 102 EGFR molecules/EEA1-positive endosome.

### Fitting of time course kinetics

Time courses were fitted with the sum of two exponential terms: one for growth and one for decline.

$$
Ae^{−\frac{t}{\tau_{1}}}+Be^{−\frac{t}{\tau_{2}}}
$$

The constant of the decline exponent τ2 was used as an estimation of the decay time of the corresponding process. The fitting of the experimental data was done according to an optimization scheme previously described (Press et al., 1992).

### p-EGFR detection in MVBs

To discriminate p-EGFR exposed on the surface of endosomes from p-EGFR sequestered into ILVs, we used a differential detergent solubilisation method as previously described for protease protection assays (Malerød et al., 2007). Cells were fixed and permeabilized with saponin 0.1% for 10 min or digitonin 0.001% for 1 min. After permeabilization, cells were washed with PBS and stained with a mouse monoclonal anti-phospho-tyrosine-AlexaFluor 555 antibody (Millipore), a mouse monoclonal anti-LBPA (a gift by J Gruenberg, University of Geneva) antibody, or a mouse monoclonal anti-GFP (Roche, Switzerland) antibody together with a goat anti-mouse-AlexaFluor 555 antibody (Molecular Probes, Invitrogen) to reveal the antigen signal.

Membrane permeabilization with saponin allows access of antibodies both to the cytosol and the luminal content of endosomes, whereas digitonin only to the cytosol. Upon digitonin permeabilization, the staining of LBPA, a marker of ILVs and EGF or EGFR was strongly reduced in comparison with saponin permeabilization (Figure 2A), consistent with their localization predominantly within the endosomal lumen. After 30 min of EGF stimulation, the endosomal, but not the plasma membrane EGFR staining was strongly reduced in cells permeabilized with digitonin compared with saponin, probably reflecting the internalization of receptors into ILVs (Figure 2A,B). In contrast, the p-EGFR levels were only moderately reduced upon permeabilization with digitonin compared with saponin extraction (Figure 2A,B), suggesting that the majority of p-EGFR faced the cytosolic surface of endosomes and was not within ILVs. To measure Shc1 recruitment to endosomes, cells were permeabilized with saponin and stained with a rabbit polyclonal anti-Shc1 antibody (BD Biosciences). Image acquisition, correction, and analysis proceeded as described above.

### dSTORM microscopy

Cells were stimulated for different times with 10 ng/ml EGF and fixed as described above. To detect p-EGFR in endosomes, cells were stained using a rabbit monoclonal anti-p-EGFR (Tyr 1068) antibody. For dSTORM microscopy, the samples were mounted on medium optimized for enhanced switching between fluorescent and non-fluorescent states as previously described (van de Linde et al., 2011; Lampe et al., 2012). Imaging was performed using a H3 Andor spinning disk microscope with a 100× objective as previously described (van de Linde et al., 2011; Lampe et al., 2012).

### Calculation of changes in endosome area distributions

First, the binned histograms of endosome area were built with bin widths linear in a logarithmic scale. Then, the histograms were normalized on their integrals, that is, histograms were scaled to have the sum of values in all bins equal to one. Finally, the histogram from the control condition was subtracted from the respective histograms of the different conditions (Figure 6—figure supplement 2).

### Mathematical model of p-EGFR propagation through the endosomal network

To describe the time course of the formation of a mean constant amount of p-EGFR per endosome during endocytosis, we postulated a sigmoidal dependency of the dephosphorylation rate on the amount of p-EGFR per endosome. The rationale for this is that if the amount of p-EGFR per endosome is above a critical value, dephosphorylation is significantly increased, whereas if the amount is lower, dephosphorylation is decreased. The delay between EGF stimulation and onset of internalization of p-EGFR into early endosomes is well documented (Burke et al., 2001; Wiley, 2003). This delay includes EGF binding to receptor (∼3 min), CCV formation (∼1–2 min) and delivery of p-EGFR to early endosomes. In order to keep the model as simple as possible, we described these mechanisms in a coarse grained model by an exponential delay with constant δτ. Since the dephosphorylation rate depends on the amount of p-EGFR per endosome, we expanded the mass flux equation usually applied in these cases with an equation that describes the number of endosomes carrying p-EGFR. Our experimental data suggest a significant redistribution of EGFR from the plasma membrane into endosomes even at very low doses of EGF (see Figure 1E, green curve. Compare 0.5 with 10 ng/ml). A simple mechanism to explain this is the internalization of ligand-unoccupied EGFR upon EGF stimulation, for example by formation of EGFR oligomers at the plasma membrane (Ariotti et al., 2010; Hofman et al., 2010). Another possible mechanism includes transient activation of p38 (Faust et al., 2012) by EGFR signalling that leads to acceleration of unoccupied receptor internalization (Zwang and Yarden, 2006; Faust et al., 2012). Therefore, we modelled the rate of EGFR-positive vesicle formation as $K_{v}=k_{v0}+k_{v1}\frac{S_{p}^{q}}{Q_{v}^{q}+S_{p}^{q}}$, where Sp is p-EGFR on plasma membrane, q is Hill coefficient, $Q_{v}$ is a characteristic constant. We considered that the ratio of EGF loaded/unloaded EGFR in the vesicles is equal to the weighted ratio p-EGFR/EGFR on plasma membrane with weight factor w. Importantly, the use of this term in the model gave the best description of the time course of total EGFR, but was not essential to explain the p-EGFR dynamics in individual endosomes (data not shown).

$$
\frac{dS_{m}}{dt}=−k_{in}·S_{m}·c_{EGF}(1−e^{−(\frac{t}{\delta\tau})^{2}})+k_{out}·S_{mp}−K_{v}·\frac{S_{m}}{S_{m}+w·S_{mp}}·S_{m}+k_{re_out}·S_{re}
$$



$$
\frac{dS_{mp}}{dt}=k_{in}·S_{m}·c_{EGF}(1−e^{−(\frac{t}{\delta\tau})^{2}})−k_{out}·S_{mp}−K_{v}·\frac{w·S_{mp}}{S_{m}+w·S_{mp}}·S_{mp}
$$



$$
\frac{dS_{pe}}{dt}=K_{v}·\frac{w·S_{mp}}{S_{m}+w·S_{mp}}·S_{mp}−(\beta_{1}+\frac{S_{pe}^{r}}{(Q·N_{pe})^{r}+S_{pe}^{r}}(\beta_{2}−\beta_{1}))·S_{pe}
$$



$$
\frac{dS_{e}}{dt}=K_{v}·\frac{S_{m}}{S_{m}+w·S_{mp}}·S_{m}+(\beta_{1}+\frac{S_{pe}^{r}}{(Q·N_{pe})^{r}+S_{pe}^{r}}(\beta_{2}−\beta_{1}))·S_{pe}−k_{re}S_{e}−k_{le}S_{e}
$$



$$
\frac{dS_{re}}{dt}=k_{re}S_{e}−k_{re_out}·S_{re}
$$



$$
\frac{dN_{pe}}{dt}=\frac{K_{v}}{s_{v}}\frac{w·S_{mp}}{S_{m}+w·S_{mp}}·w·S_{mp}−ρ·N_{pe}^{2}+f·N_{pe},
$$

where,

Sm is the amount of non-phosphorylated EGFR on the plasma membrane,

cEGF is the amount of EGF in the extracellular medium,

Smp is the amount of p-EGFR on plasma membrane,

Se is the non-phosphorylated EGFR on early endosomes,

Spe is the amount of non-phosphorylated EGFR on early endosomes,

Sre is the amount of EGFR on recycling endosomes,

Kv is the rate of EGF-stimulated EGFR-positive vesicle formation (see above),

Npe is the number early endosomes with p-EGFR,

kin is the rate of EGF binding to EGFR,

kout is the rate of EGF release from EGFR,

kre is the rate of sorting of EGFR from early to recycling endosomes,

kle is the rate of sorting of EGFR from early to late endosomes,

kre_out is the rate of delivery of EGFR from recycling endosomes to plasma membrane,

sv is the mean amount of p-EGFR per endocytic vesicle,

β1, β2 are minimum and maximum dephosphorylation rates,

r is a Hill coefficient of dephosphorylation rate,

$Q$ is the characteristic amount of p-EGFR at which the dephosphorylation has ½ maximal rate,

ρ is the early endosome homotypic fusion rate (measured as number of events/minute/endosome),

f is the early endosome homotypic fission rate.

Equation 5 describes the total amount of non-phosphorylated EGFR on the plasma membrane (Sm). The first term describes the loss of non-phosphorylated EGFR that becomes phosphorylated upon EGF binding. The second term describes the increase in non-phosphorylated EGFR upon release of EGF from p-EGFR and concomitant dephosphorylation. The third term describes the amount of non-phosphorylated EGFR which is internalized upon EGF-stimulated endocytosis (see above). The last term describes the recycling of EGFR to the plasma membrane.

Equation 6 describes the total amount of p-EGFR on the plasma membrane (Smp). The first term describes the phosphorylation of EGFR upon EGF binding, the second the dephosphorylation following EGF release, and the third its endocytosis.

Equation 7 describes the amount of p-EGFR in EEA1-positive early endosomes (Spe). The first term describes the endocytosis of p-EGFR and the second its dephosphorylation. Note that the equation includes a sigmoidal function $\beta_{1}+\frac{S_{pe}^{r}}{(Q·N_{pe})^{r}+S_{pe}^{r}}(\beta_{2}−\beta_{1})$ for the dephosphorylation rate.

Equation 8 describes the amount of non-phosphorylated EGFR on early endosomes (Se). The first term describes EGF-stimulated endocytosis of ligand-free EGFR. The second term describes the increase in the amount of non-phosphorylated EGFR through dephosphorylation of p-EGFR. The third and fourth terms describe the sorting of EGFR to recycling and late endosomes, respectively.

Equation 9 describes the amount of EGFR on recycling endosomes (Sre). The first term describes the delivery of EGFR from early endosomes and the second its recycling to the plasma membrane.

Equation 10 describes the number of EEA1-positive early endosomes containing p-EGFR (Npe). For simplicity, we considered that the p-EGFR is evenly distributed between endosomes. The first term describes the endocytosis of p-EGFR, the second the homotypic fusion of early endosomes, and the third their homotypic fission.

The model was fitted to the experimental data which included time courses of p-EGFR and EGFR colocalization to EEA1 (Kalaidzidis et al., 2015) upon stimulation with four different concentrations (0.5, 1.0, 5.0, and 10.0 ng/ml) of EGF (Figure 3A,B). Fitting was performed with FitModel software (Zeigerer, 2012) (http://pluk.mpi-cbg.de/projects/fitmodel). Since the amount p-EGFR was measured experimentally in arbitrary FRET intensity units, the modelled amount of p-EGFR was scaled before a comparison with the experimental data. The scaling factor was found by the least square formula $scale=\frac{\sum_{i=1}^{N}\frac{d_{i}·s_{i}}{\sigma_{i}^{2}}}{\sum_{i=1}^{N}\frac{s_{i}^{2}}{\sigma_{i}^{2}}}$, where di, σi; i = 1…N are experimental values and their SEMs; si are model predictions for the respective time points. The model prediction of p-EGFR modulation by reduction of the early endosome homotypic fusion rate is presented on Figure 3C. The model and fit parameters are provided in the text format and in the format of FitModel software in the Source code 1 (Model.zip).

### Knock-down and phenotype characterization in Hela EGFR BAC cells

HeLa EGFR BAC cells were reverse transfected with 5 nM siRNA oligonucleotides per gene using the oligonucleotides given in Table 2.

**Table 2.**
 List of siRNAs used for down-regulation of endosomal proteins


<table>
  <thead>
    <tr>
      <th>Gene name</th>
      <th>siRNA library</th>
      <th>siRNA ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EEA1</td>
      <td>Ambion Silencer</td>
      <td>139147</td>
    </tr>
    <tr>
      <td>Rabenosyn5</td>
      <td>Ambion Silencer</td>
      <td>292470</td>
    </tr>
    <tr>
      <td>Vps45</td>
      <td>Ambion Silencer</td>
      <td>136363</td>
    </tr>
    <tr>
      <td>Hrs</td>
      <td>Qiagen</td>
      <td>SI00067305</td>
    </tr>
    <tr>
      <td>Hrs</td>
      <td>Qiagen</td>
      <td>SI00288239</td>
    </tr>
    <tr>
      <td>Hrs</td>
      <td>Qiagen</td>
      <td>SI02659650</td>
    </tr>
    <tr>
      <td>Vps24</td>
      <td>Invitrogen</td>
      <td>148627</td>
    </tr>
    <tr>
      <td>Vps24</td>
      <td>Invitrogen</td>
      <td>148628</td>
    </tr>
    <tr>
      <td>Vps24</td>
      <td>Qiagen</td>
      <td>SI00760515</td>
    </tr>
    <tr>
      <td>Snf8</td>
      <td>Invitrogen</td>
      <td>140086</td>
    </tr>
    <tr>
      <td>Snf8</td>
      <td>Qiagen</td>
      <td>SI00375641</td>
    </tr>
    <tr>
      <td>Snf8</td>
      <td>Qiagen</td>
      <td>SI00375648</td>
    </tr>
  </tbody>
</table>

Transfection was carried out using Interferin (Polyplus transfection) together with the selected oligonucleotides following the manufacturer's instructions or treated only with Interferin (mock). 72 hr after transfection total protein extracts were prepared to measure down-regulation of the targeted proteins by western blotting using antibodies previously described for EEA1 and Rabenosyn5 (Collinet et al., 2010). To measure the redistribution of EGFR in endosomes, cells were incubated with 10 ng/ml EGF (Invitrogen), fixed, and processed for quantitative microscopy. Image acquisition and analysis were done as described earlier. Measurement of p-EGFR was done using the FRET assay described above. To measure EGFR transport kinetics, cells were incubated in serum-free medium for 1 min with 10 ng/ml EGF (Invitrogen), washed with serum-free medium, and chased for different time points. Cells were then fixed and samples were processed for quantitative microscopy analysis as explained above.

To measure degradation of EGFR, cells were incubated for 1 hr with 10 μg/ml Cyclohexamide before stimulation with 10 ng/ml EGF for different time points. Total protein extracts were prepared and analysed by western blotting using rabbit monoclonal anti-EGFR (Cell Signaling, New England BioLabs, Massachusetts, USA) and mouse anti γ-tubulin (Antibody Facility, MPI-CBG, Germany) antibodies. To measure activated EGFR at the plasma membrane, cells were incubated with 100 ng/ml EGF-AlexaFluor 488 for 10 min on ice to prevent endocytosis, fixed with PFA, stained with a rabbit anti-AlexaFluor 488 antibody fraction (Invitrogen) to enhance the fluorescent signal and imaged as described above.

### Phosphatase siRNA screen

HeLa EGFR BAC cells were reverse transfected with the protocol described above with 5 nM of the oligonucleotides in Table 3. After 72 hr, cells were stimulated with 10 ng/ml EGF for 30 min, fixed with PFA, and stained using a rabbit monoclonal anti-p-EGFR (Tyr 1068) antibody as described above. Images were acquired with an automated spinning-disk confocal microscope (OPERA, Evotec Technologies-PerkinElmer) with a 40×/0.9 NA water immersion objective. Settings were adjusted to minimize pixel-intensity saturation and maximize the dynamic range. Around 30 images for each siRNA oligonucleotide were collected. Images with less than three cells were excluded from analysis. Image analysis was performed with MotionTracking as described above.

**Table 3.**
 List of genes for PTP siRNA screen


<table>
  <thead>
    <tr>
      <th>Gene symbol</th>
      <th>Gene ID</th>
      <th>siRNa ID</th>
      <th>Sequence 5′–3′</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PTPN13</td>
      <td>5783</td>
      <td>5783-HSS108838</td>
      <td>UCACAUUUCUGAACCAACUAGACAA</td>
    </tr>
    <tr>
      <td>PTPN13</td>
      <td>5783</td>
      <td>5783-HSS184076</td>
      <td>CAUCAGACUCUAAGCAACAUGGUAU</td>
    </tr>
    <tr>
      <td>PTPN13</td>
      <td>5783</td>
      <td>5783-HSS184077</td>
      <td>CCAUUGAGGGUAAUCUCCAGCUAUU</td>
    </tr>
    <tr>
      <td>PTPN13</td>
      <td>5783</td>
      <td>5783-NM_080683.1_1459</td>
      <td>GAAACACCCUUUGAAGGCAACUUAA</td>
    </tr>
    <tr>
      <td>PTPRK</td>
      <td>5796</td>
      <td>5796-HSS108869</td>
      <td>CCCAUCCAAGUGGAAUGUAUGUCUU</td>
    </tr>
    <tr>
      <td>PTPRK</td>
      <td>5796</td>
      <td>5796-HSS108870</td>
      <td>GGUCAUUCUUGAAACUGAUACUUCA</td>
    </tr>
    <tr>
      <td>PTPRK</td>
      <td>5796</td>
      <td>5796-HSS184093</td>
      <td>CCGCGCAAAGGAUACAACAUCUAUU</td>
    </tr>
    <tr>
      <td>PTPRK</td>
      <td>5796</td>
      <td>5796-NM_002844.2_975</td>
      <td>CCGCUUCCUUCAGAUUGCAAGAAGU</td>
    </tr>
    <tr>
      <td>PTPRA</td>
      <td>5786</td>
      <td>5786-HSS108844</td>
      <td>CCAGUUCACGGAUGCCAGAACAGAA</td>
    </tr>
    <tr>
      <td>PTPRA</td>
      <td>5786</td>
      <td>5786-HSS108845</td>
      <td>GCAUUCUCAGAUUAUGCCAACUUCA</td>
    </tr>
    <tr>
      <td>PTPRA</td>
      <td>5786</td>
      <td>5786-HSS108846</td>
      <td>GGCACCAACAUUCAGCCCAAAUAUA</td>
    </tr>
    <tr>
      <td>PTPRA</td>
      <td>5786</td>
      <td>5786-NM_080841.2_1383</td>
      <td>CGCCUCAUCACUCAGUUCCACUUUA</td>
    </tr>
    <tr>
      <td>PTPRR</td>
      <td>5801</td>
      <td>5801-HSS108880</td>
      <td>AGUUGAGGUUCUGGUUAUCAGUGUA</td>
    </tr>
    <tr>
      <td>PTPN9</td>
      <td>5780</td>
      <td>5780-HSS108830</td>
      <td>CCCUCAUUGACUUCUUGAGAGUGGU</td>
    </tr>
    <tr>
      <td>PTPRR</td>
      <td>5801</td>
      <td>5801-HSS108882</td>
      <td>GGUACACCUCAUGGCCUGAUCACAA</td>
    </tr>
    <tr>
      <td>PTPN9</td>
      <td>5780</td>
      <td>5780-HSS108831</td>
      <td>ACCUCAUGAGGAACCUCUUCGUUCU</td>
    </tr>
    <tr>
      <td>PTPRR</td>
      <td>5801</td>
      <td>5801-HSS184097</td>
      <td>CAAGAGAGAAGAGGGUCCAACGUAU</td>
    </tr>
    <tr>
      <td>PTPN9</td>
      <td>5780</td>
      <td>5780-HSS184065</td>
      <td>CGCUGUCUUGGAAUGUGGCUGUCAA</td>
    </tr>
    <tr>
      <td>PTPRR</td>
      <td>5801</td>
      <td>5801-NM_130846.1_1022</td>
      <td>CAGUGGCAAGGAGAAAGCCUUCAUU</td>
    </tr>
    <tr>
      <td>PTPN9</td>
      <td>5780</td>
      <td>5780-NM_002833.2_1369</td>
      <td>CAUCCAAGAGUUGGUGGACUAUGUU</td>
    </tr>
    <tr>
      <td>PTPN2</td>
      <td>5771</td>
      <td>5771-HSS108817</td>
      <td>GGAAGACUUAUCUCCUGCCUUUGAU</td>
    </tr>
    <tr>
      <td>PTPN2</td>
      <td>5771</td>
      <td>5771-HSS108818</td>
      <td>GAGCGGGAGUUCGAAGAGUUGGAUA</td>
    </tr>
    <tr>
      <td>PTPN2</td>
      <td>5771</td>
      <td>5771-HSS184039</td>
      <td>GAGAUUCUCAUACAUGGCUAUAAUA</td>
    </tr>
    <tr>
      <td>PTPN2</td>
      <td>5771</td>
      <td>5771-NM_002828.2_1178</td>
      <td>CCGAUGUACAGGACUUUCCUCUAAA</td>
    </tr>
    <tr>
      <td>DUSP2</td>
      <td>1844</td>
      <td>1844-HSS140936</td>
      <td>GCUCUGCCACCAUCUGUCUGGCAUA</td>
    </tr>
    <tr>
      <td>PTPN3</td>
      <td>5774</td>
      <td>5774-HSS108820</td>
      <td>GGCGUGGUACAGACCUUUAAAGUUA</td>
    </tr>
    <tr>
      <td>PTPRE</td>
      <td>5791</td>
      <td>5791-HSS108853</td>
      <td>UCUGGGAAUGGAAAUCCCACACUAU</td>
    </tr>
    <tr>
      <td>DUSP2</td>
      <td>1844</td>
      <td>1844-HSS140937</td>
      <td>GCUGCUGUCCCGAUCUGUGCUCUGA</td>
    </tr>
    <tr>
      <td>PTPN3</td>
      <td>5774</td>
      <td>5774-HSS108821</td>
      <td>GAGCUGUCCGCUCAUUUGCUGACUU</td>
    </tr>
    <tr>
      <td>PTPRE</td>
      <td>5791</td>
      <td>5791-HSS108854</td>
      <td>ACGAGACUUUCUGGUCACUCUCAAU</td>
    </tr>
    <tr>
      <td>DUSP2</td>
      <td>1844</td>
      <td>1844-HSS140938</td>
      <td>GGCAUCACAGCCGUCCUCAACGUGU</td>
    </tr>
    <tr>
      <td>PTPN3</td>
      <td>5774</td>
      <td>5774-HSS108822</td>
      <td>CCACCCGGGUAUUAUUGCAGGGAAA</td>
    </tr>
    <tr>
      <td>PTPRE</td>
      <td>5791</td>
      <td>5791-HSS108855</td>
      <td>GGAACAGUAUGAAUUCUGCUACAAA</td>
    </tr>
    <tr>
      <td>DUSP2</td>
      <td>1844</td>
      <td>1844-NM_004418.3_925</td>
      <td>UGGACGAGGCCUUUGACUUCGUUAA</td>
    </tr>
    <tr>
      <td>PTPN3</td>
      <td>5774</td>
      <td>5774-NM_002829.2_621</td>
      <td>CAAUCAGAAGCAGAAUCCUGCUAUA</td>
    </tr>
    <tr>
      <td>PTPRE</td>
      <td>5791</td>
      <td>5791-NM_130435.2_1499</td>
      <td>GAGCAGGAUAAAUGCUACCAGUAUU</td>
    </tr>
    <tr>
      <td>PTPRF</td>
      <td>5792</td>
      <td>5792-HSS108856</td>
      <td>CCCAUCAUCCAAGACGUCAUGCUAG</td>
    </tr>
    <tr>
      <td>PTPRF</td>
      <td>5792</td>
      <td>5792-HSS108858</td>
      <td>GGACAGCAGUUCACGUGGGAGAAUU</td>
    </tr>
    <tr>
      <td>PTPRF</td>
      <td>5792</td>
      <td>5792-HSS184088</td>
      <td>CAGCUGUGCCCUUUAAGAUUCUGUA</td>
    </tr>
    <tr>
      <td>PTPRF</td>
      <td>5792</td>
      <td>5792-NM_130440.2_6013</td>
      <td>CAGCUUUGACCACUAUGCAACGUAA</td>
    </tr>
    <tr>
      <td>PTP4A2</td>
      <td>8073</td>
      <td>8073-HSS140957</td>
      <td>GAUAACUCACAACCCUACCAAUGCU</td>
    </tr>
    <tr>
      <td>DUSP6</td>
      <td>1848</td>
      <td>1848-HSS176270</td>
      <td>GAGAGCAGCAGCGACUGGAACGAGA</td>
    </tr>
    <tr>
      <td>PTP4A2</td>
      <td>8073</td>
      <td>8073-HSS140958</td>
      <td>GCGUUCAAUUCCAAACAGCUGCUUU</td>
    </tr>
    <tr>
      <td>DUSP6</td>
      <td>1848</td>
      <td>1848-HSS176271</td>
      <td>UGGCAUUAGCCGCUCAGUCACUGUG</td>
    </tr>
    <tr>
      <td>PTP4A2</td>
      <td>8073</td>
      <td>8073-HSS188476</td>
      <td>GGUUCGAGUUUGUGAUGCUACAUAU</td>
    </tr>
    <tr>
      <td>DUSP6</td>
      <td>1848</td>
      <td>1848-HSS176272</td>
      <td>UGGCUUACCUUAUGCAGAAGCUCAA</td>
    </tr>
    <tr>
      <td>PTP4A2</td>
      <td>8073</td>
      <td>8073-NM_080392.2_1123</td>
      <td>UCGAGUUUGUGAUGCUACAUAUGAU</td>
    </tr>
    <tr>
      <td>DUSP6</td>
      <td>1848</td>
      <td>1848-NM_022652.2_1097</td>
      <td>CAUGUGACAACAGGGUUCCAGCACA</td>
    </tr>
    <tr>
      <td>PTPRM</td>
      <td>5797</td>
      <td>5797-HSS108871</td>
      <td>CCGAGUGAGGCUGCAGACAAUAGAA</td>
    </tr>
    <tr>
      <td>PTP4A3</td>
      <td>11156</td>
      <td>11156-NM_007079.2_423</td>
      <td>UCAGCACCUUCAUUGAGGACCUGAA</td>
    </tr>
    <tr>
      <td>PTPN18</td>
      <td>26469</td>
      <td>26469-HSS120076</td>
      <td>GCUGCCUUAUGAUCAGACGCGAGUA</td>
    </tr>
    <tr>
      <td>PTPN14</td>
      <td>5784</td>
      <td>5784-HSS108841</td>
      <td>UCAUGGGAAUGAAGAAGCCUUGUAU</td>
    </tr>
    <tr>
      <td>PTPRM</td>
      <td>5797</td>
      <td>5797-HSS108872</td>
      <td>CAGGCUCUGGUUACAGGGCAUUGAU</td>
    </tr>
    <tr>
      <td>PTP4A3</td>
      <td>11156</td>
      <td>11156-NM_007079.2_460</td>
      <td>UACCACUGUGGUGCGUGUGUGUGAA</td>
    </tr>
    <tr>
      <td>PTPN18</td>
      <td>26469</td>
      <td>26469-HSS120077</td>
      <td>UCGAGAGAUAGAGAAUGGGCGGAAA</td>
    </tr>
    <tr>
      <td>PTPN14</td>
      <td>5784</td>
      <td>5784-HSS108843</td>
      <td>GCCGCUGAUGUUGGCAGCAUUGAAU</td>
    </tr>
    <tr>
      <td>PTPRM</td>
      <td>5797</td>
      <td>5797-HSS108873</td>
      <td>CCCGACGCUUCAUUGCUUCAUUUAA</td>
    </tr>
    <tr>
      <td>PTP4A3</td>
      <td>11156</td>
      <td>11156-NM_007079.2_473</td>
      <td>CGUGUGUGUGAAGUGACCUAUGACA</td>
    </tr>
    <tr>
      <td>PTPN18</td>
      <td>26469</td>
      <td>26469-HSS120078</td>
      <td>CCCACCUGACUUCAGUCUCUUUGAU</td>
    </tr>
    <tr>
      <td>PTPN14</td>
      <td>5784</td>
      <td>5784-HSS184078</td>
      <td>GAUAUCAGUAUUACCUGCAAGUCAA</td>
    </tr>
    <tr>
      <td>PTPRM</td>
      <td>5797</td>
      <td>5797-NM_002845.3_1217</td>
      <td>CCGACGCUUCAUUGCUUCAUUUAAU</td>
    </tr>
    <tr>
      <td>PTP4A3</td>
      <td>11156</td>
      <td>11156-NM_007079.2_678</td>
      <td>CCAUCAACAGCAAGCAGCUCACCUA</td>
    </tr>
    <tr>
      <td>PTPN18</td>
      <td>26469</td>
      <td>26469-NM_014369.2_835</td>
      <td>UCAGUCUCUUUGAUGUGGUCCUUAA</td>
    </tr>
    <tr>
      <td>PTPN14</td>
      <td>5784</td>
      <td>5784-NM_005401.3_3394</td>
      <td>CACGAAGUUUCGAACGGAUUCUGUU</td>
    </tr>
    <tr>
      <td>PTPN1</td>
      <td>5770</td>
      <td>5770-HSS108816</td>
      <td>GAGUGAUGGAGAAAGGUUCGUUAAA</td>
    </tr>
    <tr>
      <td>PTPN1</td>
      <td>5770</td>
      <td>5770-HSS184025</td>
      <td>CAUGAAGCCAGUGACUUCCCAUGUA</td>
    </tr>
    <tr>
      <td>PTPN1</td>
      <td>5770</td>
      <td>5770-HSS184026</td>
      <td>CGAGAGAUCUUACAUUUCCACUAUA</td>
    </tr>
    <tr>
      <td>PTPN1</td>
      <td>5770</td>
      <td>5770-NM_002827.2_507</td>
      <td>CAGAGUGAUGGAGAAAGGUUCGUUA</td>
    </tr>
    <tr>
      <td>PTPRJ</td>
      <td>5795</td>
      <td>5795-HSS108867</td>
      <td>GCGACUUCAUAUGUAUUCUCCAUCA</td>
    </tr>
    <tr>
      <td>PTPRJ</td>
      <td>5795</td>
      <td>5795-HSS184091</td>
      <td>CGGGUUCUUCUUGAAAGCAUUGGAA</td>
    </tr>
    <tr>
      <td>PTPRJ</td>
      <td>5795</td>
      <td>5795-HSS184092</td>
      <td>GAGCAGCCAUGAUGCAGAAUCAUUU</td>
    </tr>
    <tr>
      <td>PTPRJ</td>
      <td>5795</td>
      <td>5795-NM_002843.3_1838</td>
      <td>CGGGUAGAAAUAACCACCAACCAAA</td>
    </tr>
    <tr>
      <td>PTPN12</td>
      <td>5782</td>
      <td>5782-HSS108835</td>
      <td>GCCACAGGAAUUAAGUUCAGAUCUA</td>
    </tr>
    <tr>
      <td>PTP4A1</td>
      <td>7803</td>
      <td>7803-HSS111748</td>
      <td>GCAACUUCUGUAUUUGGAGAAGUAU</td>
    </tr>
    <tr>
      <td>PTPN12</td>
      <td>5782</td>
      <td>5782-HSS108836</td>
      <td>GCCUCUUGAUGAGAAAGGACAUGUA</td>
    </tr>
    <tr>
      <td>PTP4A1</td>
      <td>7803</td>
      <td>7803-HSS111749</td>
      <td>UCAAAGAUUCCAACGGUCAUAGAAA</td>
    </tr>
    <tr>
      <td>PTPN12</td>
      <td>5782</td>
      <td>5782-HSS108837</td>
      <td>UCUGAUGGUGCUGUGACCCAGAAUA</td>
    </tr>
    <tr>
      <td>PTP4A1</td>
      <td>7803</td>
      <td>7803-HSS111750</td>
      <td>CCAACCAAUGCGACCUUAAACAAAU</td>
    </tr>
    <tr>
      <td>PTPN12</td>
      <td>5782</td>
      <td>5782-NM_002835.2_554</td>
      <td>CAGGACACUCUUACUUGAAUUUCAA</td>
    </tr>
    <tr>
      <td>PTP4A1</td>
      <td>7803</td>
      <td>7803-NM_003463.3_1382</td>
      <td>AACCAGAUUGUUGAUGACUGGUUAA</td>
    </tr>
    <tr>
      <td>PTPN11</td>
      <td>5781</td>
      <td>5781-HSS108834</td>
      <td>ACAUGGAACAUCACGGGCAAUUAAA</td>
    </tr>
    <tr>
      <td>PTPN11</td>
      <td>5781</td>
      <td>5781-HSS184068</td>
      <td>CAGACAGAAGCACAGUACCGAUUUA</td>
    </tr>
    <tr>
      <td>PTPN11</td>
      <td>5781</td>
      <td>5781-HSS184069</td>
      <td>GAAAGGGCACGAAUAUACAAAUAUU</td>
    </tr>
    <tr>
      <td>PTPN11</td>
      <td>5781</td>
      <td>5781-NM_002834.3_5519</td>
      <td>CAGGAUGCCUUUGUUAGGAUCUGUA</td>
    </tr>
  </tbody>
</table>

### MAPK signalling measurements

72 hr after transfection, HeLa EGFR BAC cells were stimulated with 10 ng/ml EGF for different time points. Then, total protein extracts were prepared and analysed by western blotting using rabbit monoclonal anti-phospho-Erk1/2 (Thr202/Tyr204) (Cell Signaling, New England BioLabs) and mouse monoclonal anti-Erk1/2 (Cell Signaling, New England BioLabs) antibodies. For quantification, phospho-Erk1/2 intensity values were first normalized by the total Erk1/2 signal to control for differences in lane loading. For every blot, these values were normalized by the mean intensity amplitude per blot and then scaled by the mean difference between knock-down and mock-treated samples per experiment to account for experimental variability. To measure c-Fos activation, cells were stimulated with 10 ng/ml EGF for 30 min, fixed with PFA, and permeabilized with 0.5% Triton in PBS and 5% BSA as a blocking reagent. Cells were stained with a rabbit monoclonal anti-phospho-c-Fos (Ser32) antibody (Cell Signaling, New England BioLabs) and processed for image analysis. To measure Erk1/2 activation in PC12 cells, cells were stimulated with 100 ng/ml EGF or 50 ng/ml NGF and stained with a rabbit monoclonal anti-phospho-Erk1/2 (Thr202/Tyr204) (Cell Signaling, New England BioLabs) using the same protocol as above. 10 images per condition were acquired using a laser-scanning confocal microscope (Duoscan, Zeiss) with a 40×/1.3 oil objective. Image analysis was carried out as described above.

### Animals

All animal studies were conducted in accordance with German animal welfare legislation and in strict pathogen-free conditions in the animal facility of the Max Planck Institute of Molecular Cell Biology and Genetics, Dresden, Germany. Protocols were approved by the Institutional Animal Welfare Officer (Tierschutzbeauftragter), and necessary licenses were obtained from the regional Ethical Commission for Animal Experimentation of Dresden, Germany (Tierversuchskommission, Landesdirektion Dresden).

### Hepatoblast isolation and culture

Foetal hepatic cells were isolated from C57BL/6JOlaHsd mice, maintained in the animal facility of the MPI-CBG. Pregnancies were dated by the presence of a vaginal plug (embryonic day (E) 0.5). Hepatoblasts were prepared from E14.5 liver as described previously (Kamiya et al., 1999). Delta-like 1 (Dlk1) + hepatoblasts were isolated from the E14.5 hepatic cells as described previously with minor modifications (Tanimizu et al., 2003). Briefly, cells were blocked with an anti-mouse CD16/32 (BD Biosciences) and stained with a FITC-conjugated anti-Dlk1 antibody (MBL International, Massachusetts, USA) followed by anti-FITC Microbeads (Miltenyi Biotec GmbH, Germany). The labelled cells were separated using a MACS Cell Separation Column (Miltenyi Biotec). Dlk1+ cells were resuspended in DMEM (PAA Laboratories GmbH, Austria) containing 5% FBS, 2 mM L-glutamine (PAA Laboratories GmbH), 100 μM MEM Non-Essential Amino Acids (PAA Laboratories GmbH), 0.1 μM dexamethasone (Sigma–Aldrich), 100 Units/ml penicillin (PAA Laboratories GmbH), 100 μg/ml streptomycin (PAA Laboratories GmbH), and 4% BD Matrigel Basement Membrane Matrix (BD Biosciences), and seeded on a μ-slide 8-well (Ibidi GmbH, Germany) coated with fibronectin (Sigma–Aldrich, Germany). To measure Erk1/2 activation, cells were starved for 24 hr before stimulation with either 10 ng/ml EGF or HGF (R&D systems, Minnesota, USA). Total cell lysates were prepared and analysed using the same protocol and antibodies described above.

### EEA1 staining after growth factor stimulation in PC12 cells or hepatoblasts

We used a clone of PC12 cells, PC12 Nsc-1 (Cellomics Inc., Maryland, USA) cells, due to their increased growth rate and decreased cell clumping, which facilitate imaging experiments (Hahn et al., 2009). Cells were grown following the manufacturer's instructions. PC12 cells were starved for 36 hr before stimulation either with 100 ng/ml EGF (Invitrogen) or 50 ng/ml NGF (R&D Systems) for 30 min. E14.5 Dlk1+ hepatoblasts were starved for 24 hr before stimulation with either 10 ng/ml EGF or HGF (R&D systems). Then, cells were fixed with 3% para-formaldehyde and stained with a mouse monoclonal anti-EEA1 (BD Biosciences Pharmingen). A fluorescently conjugated goat anti-mouse-AlexaFluor 555 secondary antibody (Molecular Probes, Invitrogen) revealed the antigen signal. Image acquisition and image analysis were performed as described above.

### Triple knock-down and phenotype characterization in PC12 Nsc-1 cells

PC12 Nsc-1 cells were electroporated with 100 nM Stealth Select siRNA oligonucleotides (Invitrogen) (EEA1: 5′—GAA AGC AGC UCA ACU UGC UAC UGA A—3′, 3′—UUC AGU AGC AAG UUG AGC UGC UUU C—5′; Rabenosyn5: 5′—GGG CCU CAC ACU GAU CUU GCC UAU U—3′, 3′—AAU AGG CAA GAU CAG UGU GAG GCC C—5′; Vps45: 5′—GAC CCG GCA UGA AGG UAC UUC UCA U—3′, 3′—AUG AGA AGU ACC UUC AUG CCG GGU C—5′; Syntaxin-13: 5′—CCA AGG UGA UCU GAU UGA UAG CAU A—3′, 3′—UAU GCU AUC AAU CAG AUC ACC UUG G—5′; Syntaxin-6: 5′—GGA UGC UGG AGU GAC GGA UCG AUA U—3′, 3′—AUA UCG AUC CGU CAC UCC AGC AUC C—5′) or electroporated without siRNAs (Mock) using the Amaxa Cell line Nucleofector Kit V (Lonza, Switzerland) following the manufacturer's instructions. 36 hr after electroporation, cells were placed in serum-free medium. 72 hr after electroporation total protein extracts were prepared to measure down-regulation of the targeted proteins by western blotting with a mouse monoclonal anti-Syntaxin-13 (Synaptic Sytems, Germany) or a mouse monoclonal anti-Syntaxin-6 (Transduction Laboratories, BD Biosciences) antibody. To measure EGF transport, cells were stimulated with 100 ng/ml EGF-Alexafluor 555 (Molecular Probes, Invitrogen) for 1 min, washed with serum-free medium, and chased for different times. Then, cells were fixed and processed for microscopy as described above.

### PC12 Nsc-1 differentiation-proliferation assay

Cells were starved for 36 hr and then stimulated in serum-free medium with 100 ng/ml EGF (Invitrogen) or 50 ng/ml NGF (R&D Systems) for 24 hr at 37°C and 5% CO2. During the last 3 hr, 5-ethynyl-2′ –deoxyuridine (EdU) was added at a final concentration of 10 μM. Then, cells were fixed and stained with Click-iT AlexaFluor 647 Azide (Molecular Probes, Invitrogen) following the manufacturer's instructions. Afterwards, cells were stained with a mouse monoclonal anti-β-III tubulin antibody (Chemicon International, Millipore) and a fluorescently conjugated goat anti-mouse-AlexaFluor 555 (Molecular Probes, Invitrogen) to reveal the antigen signal. Nuclei were stained with DAPI. 20 images per condition were acquired using a laser-scanning confocal microscope (Duoscan, Zeiss) with a 20×/0.8 objective. Image processing was carried out as described above. Images were inspected manually for process formation; cells with processes were defined as those having thin β-III tubulin-positive processes longer than 1 μm. The β-III tubulin expression was measured by total immunofluorescence intensity normalized by the frame area covered by cells to account for frame-to-frame variability in cell number.
