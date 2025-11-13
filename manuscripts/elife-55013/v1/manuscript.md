# Spatially compartmentalized phase regulation of a Ca2+-cAMP-PKA oscillatory circuit

## Authors

- Brian Tenner<sup>1</sup>
- Michael Getz<sup>3</sup> ([ORCID: 0000-0001-9886-8454](https://orcid.org/0000-0001-9886-8454))
- Brian Ross<sup>2</sup> ([ORCID: 0000-0001-9020-627X](https://orcid.org/0000-0001-9020-627X))
- Donya Ohadi<sup>4</sup>
- Christopher H Bohrer<sup>1</sup>
- Eric Greenwald<sup>2</sup>
- Sohum Mehta<sup>2</sup> ([ORCID: 0000-0003-4764-8579](https://orcid.org/0000-0003-4764-8579))
- Jie Xiao<sup>1</sup> ([ORCID: 0000-0003-1433-5437](https://orcid.org/0000-0003-1433-5437))
- Padmini Rangamani<sup>3</sup> ([ORCID: 0000-0001-5953-4347](https://orcid.org/0000-0001-5953-4347)) †
- Jin Zhang<sup>2</sup> ([ORCID: 0000-0001-7145-7823](https://orcid.org/0000-0001-7145-7823)) †

### Affiliations

1. Department of Biophysics and Biophysical Chemistry, The Johns Hopkins University School of Medicine Baltimore United States
2. Department of Pharmacology, University of California, San Diego La Jolla United States
3. Chemical Engineering Graduate Program, University of California, San Diego La Jolla United States
4. Department of Mechanical and Aerospace Engineering, University of California, San Diego La Jolla United States
5. Department of Chemistry and Biochemistry, University of California, San Diego La Jolla United States

† Corresponding author

## Abstract

Signaling networks are spatiotemporally organized to sense diverse inputs, process information, and carry out specific cellular tasks. In β cells, Ca2+, cyclic adenosine monophosphate (cAMP), and Protein Kinase A (PKA) exist in an oscillatory circuit characterized by a high degree of feedback. Here, we describe a mode of regulation within this circuit involving a spatial dependence of the relative phase between cAMP, PKA, and Ca2+. We show that in mouse MIN6 β cells, nanodomain clustering of Ca2+-sensitive adenylyl cyclases (ACs) drives oscillations of local cAMP levels to be precisely in-phase with Ca2+ oscillations, whereas Ca2+-sensitive phosphodiesterases maintain out-of-phase oscillations outside of the nanodomain. Disruption of this precise phase relationship perturbs Ca2+ oscillations, suggesting the relative phase within an oscillatory circuit can encode specific functional information. This work unveils a novel mechanism of cAMP compartmentation utilized for localized tuning of an oscillatory circuit and has broad implications for the spatiotemporal regulation of signaling networks.

## Introduction

Cyclic adenosine monophosphate (cAMP) and Ca2+ act as essential second messengers in almost every cell type and regulate many functional pathways within a cell, such as hormonal signal transduction, metabolism, and secretion (Clapham, 2007; Sassone-Corsi, 2012). In some cell types, including neurons, cardiomyocytes, and pancreatic β cells, these messengers’ concentrations oscillate intracellularly (Dupont et al., 2011; Dyachok et al., 2006), and the oscillations encode critical signaling information (e.g. signal strength, duration, and target diversity) into parameters such as frequency and amplitude (Berridge et al., 1998; De Pittà et al., 2008; Parekh, 2011). This phenomenon is perhaps best exemplified in β cells, where oscillations of Ca2+ drive pulsatile insulin secretion (Rorsman and Ashcroft, 2018) and oscillating cAMP levels (Nesher et al., 2002; Tengholm, 2012). Furthermore, Ca2+, cAMP, and the downstream cAMP-dependent kinase protein kinase (PKA) constitute a highly coordinated oscillatory circuit responsible for integrating metabolic and signaling information (Ni et al., 2011). In addition to temporal control, biochemical pathways are also spatially organized within the cell (Smith and Scott, 2002; White and Anderson, 2005). Both Ca2+ and cAMP are highly spatially compartmentalized and form signaling microdomains or nanodomains (Calebiro and Maiellaro, 2014; Petersen, 2002). While Ca2+ levels are locally controlled by channels, pumps, and intracellular buffering systems (Clapham, 2007; Stern, 1992), cAMP is thought to be regulated via controlled synthesis by adenylyl cyclases (ACs) and degradation by phosphodiesterases (PDEs) (Bender and Beavo, 2006; Defer et al., 2000). Despite extensive studies on cAMP compartmentation, the mechanisms that spatially constrain this mobile second messenger await to be fully elucidated (Saucerman et al., 2014; Lohse et al., 2017; Musheshe et al., 2018; Bock et al., 2020; Zhang et al., 2020). Furthermore, it is not clear how the spatial regulation of a second messenger influences its dynamic behaviors in the context of coordinated oscillations.

In this study, we investigated the spatiotemporal organization of the Ca2+-cAMP-PKA oscillatory circuit in MIN6 β cells and discovered that the relative oscillatory phase between cAMP/PKA and Ca2+ is spatially regulated within signaling nanodomains. By combining dynamic live-cell imaging, super-resolution microscopy, and computational modeling, we further found that fine-scale, compartment-specific perturbations of this precise phase regulation impact Ca2+ oscillations in β cells. These findings suggest that the relative phase in oscillatory signaling circuits, like the amplitude and frequency, represents yet another mode of informational encoding and processing, which is subjected to spatiotemporal regulation within the cell.

## Results

### The relative phase of β cell cAMP and Ca2+ oscillations is compartmentalized

In order to study the spatiotemporal relationship between key players of the Ca2+-cAMP-PKA circuit, we chose to focus our attention on an important class of molecular scaffolds, A-kinase anchoring proteins (AKAPs), which are responsible for recruiting PKA to specific substrates at distinct subcellular locations. In several excitable cell types, the plasma membrane (PM)-localized scaffold protein AKAP79 (rodent ortholog AKAP150) has been shown to organize a macromolecular complex with binding partners that include PKA, the voltage-gated Ca2+ channel CaV1.2, Protein Kinase C (PKC), the Ca2+/calmodulin-dependent protein phosphatase calcineurin, Ca2+-sensitive ACs, AMPA receptors, and many others (Gold et al., 2011). Due to the extensive and multivalent nature of AKAP79/150 (as the scaffold is commonly referred) and a report describing the functional impairment of glucose-stimulated insulin secretion (GSIS) in pancreatic β cells upon its knock-out (Hinke et al., 2012), we hypothesized that the AKAP79/150 scaffold might play an important role in the spatiotemporal regulation of the Ca2+-cAMP-PKA oscillatory circuit. Specifically, we were interested in testing if AKAP79/150 is able to create a spatially-distinct compartment in which recruitment of signaling effectors can locally fine-tune and reshape signaling dynamics within the circuit (Beene and Scott, 2007; Greenwald and Saucerman, 2011).

To test this hypothesis, we monitored intracellular cAMP and Ca2+ using the FRET-based cAMP biosensor (Ci/Ce)Epac2-camps (Everett and Cooper, 2013) and the red Ca2+ indicator RCaMP (Akerboom et al., 2013). We measured cAMP concentration changes in the immediate vicinity of AKAP150 in mouse MIN6 β cells by using (Ci/Ce)Epac2-camps fused to the full-length AKAP79 scaffold (gene AKAP5) (Figure 1a). Although human AKAP79 and the rodent AKAP150 share only 53% sequence identity overall, the interaction motifs and association between the AKAP scaffold and other key signaling players such as PKA, the voltage-gated calcium channel, adenylyl cyclases, and calcineurin are highly conserved (Willoughby et al., 2010; Zhang et al., 2016). The primary difference between these two closely related scaffolds is the presence of an internal repetitive amino acid sequence of unknown function in AKAP150 (Robertson et al., 2009). The functional equivalence of AKAP79 and AKAP150 has been demonstrated in several reciprocal knock-out and recovery experiments in which AKAP79 or AKAP150 was knocked out and expression of the other was shown to rescue a measured phenotype (Hoshi et al., 2005; Zhang et al., 2011). As a control, we also targeted the cAMP probe to the general plasma membrane by adding a lipid modification domain (Wachten et al., 2010). These targeted biosensors allowed us to compare the dynamics within the AKAP79/150-specific compartment versus the general plasma membrane compartment (Figure 1a).

![Figure 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig1-v1.jpg)

**Figure 1.:** (a) Depiction of the AKAP79/150 and plasma membrane compartments, including the targeted cAMP biosensor (Ci/Ce)Epac2-camps to measure the compartment-specific cAMP signaling. Schematics of the lyn-(Ci/Ce)Epac2-camps and AKAP79-(Ci/Ce)Epac2-camps sensors are shown above. (b) Network diagram describing the key players in the β cell Ca2+-cAMP-PKA oscillatory circuit. (c) Representative single-cell trace of in-phase oscillating responses of AKAP79-(Ci/Ce)Epac2-camps and RCaMP, whole-cell fluorescence measured. Red trace is cAMP (cyan direct channel divided by CY-FRET channel) and black trace is Ca2+ (RFP). (d) Representative single-cell trace of out-of-phase oscillating responses of lyn-(Ci/Ce)Epac2-camps and RCaMP, whole-cell fluorescence measured. Blue trace is cAMP (cyan direct channel divided by CY-FRET channel) and black trace is Ca2+ (RFP). (e) Cross-correlation between the oscillatory Ca2+ and cAMP signals from the representative in-phase AKAP79 (red) and out-of-phase plasma membrane (PM, blue) responses from c, d. Time lag (sec) between the cAMP and Ca2+ signals for the two compartments (AKAP79/150, red, is 13 ± 3 sec n=60 and PM, blue, is 47 ± 4 s n=24). ****p<0.0001; unpaired two-tailed Student’s t-test.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Confocal image of lyn(Ci/Ce)Epac2camps showing efficient localization of the probe at the PM in MIN6 cells (YFP channel, scale 5 μm). (b) Confocal image of AKAP79-(Ci/Ce)Epac2camps also depicting localization of the scaffold-fused biosensor at the PM in MIN6 cells (YFP channel, scale 5 μm).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Representative single-cell traces showing that cytosolic cAMP (red, measured with R-FlincA sensor) oscillations are anti-correlated with cAMP oscillations at AKAP79 (blue, measured with AKAP79-(Ci/Ce)Epac2-camps) within individual MIN6 β cells ( n = 25 cells total). (b) Violin plot summarizing the time lag (sec) between the cytosolic and AKAP79-localized cAMP oscillations within all of the cells analyzed (n = 25).

Although both targeted sensors were trafficked to and distributed along the plasma membrane (Figure 1—figure supplement 1a,b), we observed notable differences in their respective cAMP signals relative to Ca2+ oscillations after triggering the circuit (Figure 1b) with tetraethylammonium chloride (TEA, 20 mM), a potent K+ channel blocker. cAMP oscillations measured within the AKAP79/150 compartment were in-phase with oscillating Ca2+, such that each transient spike in intracellular Ca2+ was closely associated with a transient increase in cAMP (Figure 1c) (n = 60 cells). This was in sharp contrast to cAMP oscillations measured within the general plasma membrane compartment, where each local Ca2+ peak corresponded to a local trough in cAMP (n = 24), followed by a slow reversal of both signals to a pre-stimulated baseline (Figure 1d). While these out-of-phase cAMP-Ca2+ oscillations were consistent with those observed in the cytoplasm of β cells (Landa et al., 2005; Ni et al., 2011), in-phase cAMP-Ca2+ oscillations had not previously been observed under these conditions. To quantify the cAMP-Ca2+ phase relationship, we measured the lag time by calculating the cross-correlation between the two normalized, oscillatory signals and finding the shortest delay yielding the maximum correlation (see Appendix 1 for details) (Figure 1e). In-phase cAMP oscillations corresponded to short lag times (typically <20 s), while out-of-phase oscillations mostly possessed longer lag times. Within the AKAP79/150 compartment, cAMP lagged behind Ca2+ by an average of only 13 ± 3 s (mean ± SEM, n = 60); however, cAMP within the general plasma membrane compartment oscillated with a lag time of 47 ± 4 s (n = 24) behind Ca2+ (Figure 1e). In order to measure these different cAMP dynamics within the same cells, we transfected MIN6 cells with two cAMP sensors of different targeting sequences and colors, AKAP79-(Ci/Ce)Epac2-camps and the red cytosolic cAMP sensor R-FlincA (Ohta et al., 2018). After stimulating the signaling circuit, we observed anti-correlated cAMP oscillations, indicating that cAMP oscillates with different phases between the cytosol/plasma membrane and the immediate vicinity of AKAP79/150 within the same cell (n = 25) (Figure 1—figure supplement 2). This stark difference in the cAMP-Ca2+ phase relationship suggests that the relative phase of this oscillatory circuit is compartmentalized and hints at differential regulation of the circuit between the AKAP79/150 compartment and the general plasma membrane compartment.

### Oscillatory phase is regulated by balanced activities of Ca2+-sensitive ACs and PDEs

Given that in-phase cAMP oscillations were only observed within the AKAP79/150 compartment (Figure 1c) and that out-of-phase cAMP oscillations were observed in the general plasma membrane compartment (Figure 1d) and the cytoplasm (Ni et al., 2011), we hypothesized that Ca2+ oscillations are coupled to cAMP oscillations by a ubiquitous mechanism throughout the cell, while additional mechanisms specifically regulate the phase relationship within the AKAP79/150 compartment. We first sought to identify the component that is responsible for coupling cAMP dynamics to Ca2+ dynamics globally. Since TEA induces continuous Ca2+ oscillations, we determined the temporal relationship between Ca2+ and cAMP at the general plasma membrane more precisely by measuring the impulse response of the circuit following a transient membrane depolarization. After the addition of KCl (15 mM) followed by a subsequent washout to elicit a transient influx of Ca2+ (Dou et al., 2015), we observed a synchronous cAMP decrease (n = 20) followed by a return to baseline (Figure 2a). These data suggest that increasing cytosolic Ca2+ was coupled to a decrease in cAMP at the plasma membrane through Ca2+-sensitive AC or PDE activities. Given that Ca2+-inhibited ACs (AC5, AC6) have low specific activity in both the presence and absence of physiological Ca2+, as well as relatively low expression in the pancreas (Defer et al., 2000), we instead focused on probing the role of PDEs. The Ca2+-dependent PDE1 family in β cells, specifically PDE1C, has been implicated in modulating GSIS (Han et al., 1999). Indeed, acute addition of 8MM-IBMX (100 μM), a relatively selective PDE1 inhibitor, effectively uncoupled cAMP dynamics from Ca2+ oscillations (Figure 2b, Figure 2—figure supplement 1a) (n = 18), indicating that Ca2+-triggered activation of PDE1 mediates the transient cAMP decreases. We also observed that the overall increase in cAMP led to an increase in the Ca2+ oscillation frequency, consistent with the previously identified role of cAMP/PKA in regulating the Ca2+ oscillations (Ni et al., 2011). We tested the roles of two additional families of abundant PDEs in pancreatic β cells, PDE3 and PDE4, by acute pharmacologic inhibition. While treating cells with either milrinone (PDE3 inhibitor, 10 μM, n = 12) or rolipram (PDE4 inhibitor, 1 μM, n = 15) slightly increased cAMP levels, neither inhibitor had an effect on cAMP-Ca2+ coupling or relative phase (Figure 2—figure supplement 1b,c). These data suggest that PDE1 is the key component that couples Ca2+ and cAMP oscillations within this signaling circuit.

![Figure 2.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig2-v1.jpg)

**Figure 2.:** (a) Impulse response of plasma membrane cAMP (blue) to a spike in Ca2+ entry (black), triggered by KCl-mediated membrane depolarization (wash in/out). The transient decrease in PM-cAMP is coupled to the transient increase in intracellular Ca2+. (b) Acute inhibition of Ca2+-sensitive PDE1 decouples the out-of-phase PM-cAMP oscillations from Ca2+ oscillations, as observed in this representative cell trace (Ca2+ – black, PM-cAMP – blue). (c) The oscillatory phase of cAMP can be manipulated by tuning the relative activity of Ca2+-sensitive PDE and AC, as demonstrated by a simplified mathematical model. The schematic shows the network architecture. The relative activities of AC and PDE, denoted as v(AC) and v(PDE), control the delay between Ca2+ and cAMP. Point (i), with high AC activity and low PDE, shows in phase oscillations of Ca2+ and cAMP, whereas point (ii), with high PDE and low AC activity shows out of phase oscillations. These dynamics are shown in the line graphs. (d) Knocking down AC8 is correlated with an increase in the time lag for oscillatory cAMP at the AKAP79/150 microdomain (37 ± 9 s, n = 11), indicating more cells exhibiting out-of-phase cAMP oscillations (representative cell trace, Ca2+ – black, AKAP79/150-cAMP – red). (e) Over-expressing AC8 is sufficient to reverse the phase at the PM to in-phase (23 ± 2 s, n = 56) (representative cell trace, Ca2+ – black, PM cAMP – blue). **p=0.0014, ****p<0.0001; unpaired two-tailed Student’s t-test.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) Representative single cell traces depicting the decoupling of oscillating cAMP at the PM (measured by lyn-(Ci/Ce)Epac2-camps, blue trace) from oscillating Ca2+ (black trace) upon inhibition of PDE1 with 8MM-IBMX. Representative single cell traces showing cAMP still oscillates at the PM (blue trace) together with Ca2+ (black trace) upon inhibition of PDE3 (milrinone) (b) and PDE4 (rolipram) (c), respectively.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (a) Plot depicting a dose-dependence between the time lag of cAMP at the PM and the amount of plasmid-encoded AC8 co-transfected (n = 56). (b) Violin plots depicting the relationship between estimated cellular AC8 expression levels and the amount of GFP-AC8 plasmid transfected into cells (50 ng: n = 68 cells, 250 ng: n = 116 cells, 1000 ng: n = 91 cells). p=0.00001, 50 ng vs 1000 ng; Kruskal-Wallis test followed by Dunn's multiple comparisons test. (c) Representative single cell trace of an oscillating β cell control with no AC8 co-expression, illustrating an out-of-phase cAMP-Ca2+ phase relationship. Blue trace is cAMP at PM and black trace is Ca2+. (d) Representative single cell trace of an oscillating β cell with 1 μg of an AC8 expression vector co-transfected, illustrating an in-phase cAMP-Ca2+ phase relationship. Blue trace is cAMP at PM and black trace is Ca2+.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** (a) Average intensity per AC8-stained MIN6 cell, expressing AKAP79-(Ci/Ce)Epac2-camps (AKAP79), lyn-(Ci/Ce)Epac2-camps (Lyn), or no sensor (control). AC8 intensity does not significantly differ between the three populations. ns, p=0.2525; ordinary one-way ANOVA. (b) Representative Western blot quantifying endogenous expression of AC8 and expression of transfected biosensor (AKAP79-(Ci/Ce)Epac2-camps (AKAP79), Lyn-(Ci/Ce)Epac2-camps (Lyn), or Cerulean (Cer) only) in MIN6 cells. A small increase in AC8 expression was observed between sensor-expressing populations compared to Cerulean alone (AKAP79 vs. Cer, *p=0.0134; Lyn vs. Cer, p=0.0979; ordinary one-way ANOVA followed by Tukey’s multiple comparisons test). However, no significant difference in AC8 expression was measured between the AKAP79- and Lyn-tagged sensor-expressing populations (AC8 band intensity normalized to β tubulin, n = 4 replicates, p=0.4373).

How is the phase relationship between Ca2+- and cAMP-regulated within distinct signaling compartments? In order to gain a more quantitative understanding of the regulation of the cAMP-Ca2+ phase relationship, we created a simplified well-mixed mathematical model involving Ca2+, cAMP, and Ca2+-driven PDE and AC activity components (Cooper et al., 1995; Figure 2c, see Appendix 1 for details). This simple circuit represents the key aspects of the oscillatory cAMP-Ca2+ circuit and is applicable to different signaling compartments. Opposite to the Ca2+-stimulated PDE1 (Ang and Antoni, 2002) is the Ca2+-stimulated AC8 (gene Adcy8) (Masada et al., 2009; Masada et al., 2012), an abundant Ca2+-sensitive transmembrane AC isoform in β cells that has been shown to mediate sustained insulin secretion and associate with the AKAP79/150 scaffold (Dou et al., 2015; Willoughby and Cooper, 2006; Willoughby et al., 2010). By computationally manipulating the activity of each arm, we found that cAMP can oscillate either out-of-phase or in-phase when a Ca2+ pulse train is used as an input (Figure 2c). In particular, when the relative activity of PDE1 is greater than the activity of AC8, Ca2+-driven cAMP degradation dominates, resulting in an out-of-phase cAMP-Ca2+ relationship. On the other hand, if the relative activity of AC8 is greater than that of PDE1, Ca2+-stimulated cAMP production is favored, and an in-phase relationship is observed, consistent with previous modeling studies (Fridlyand et al., 2007; Peercy et al., 2015).

Thus, our simplified model indicates that the phase relationship can be tuned by altering the relative strength between Ca2+-sensitive ACs and PDEs (Figure 2c). This model provided a blueprint for understanding the interplay between the Ca2+-stimulated AC/PDE balance and the cAMP-Ca2+ phase relationship within the AKAP79/150 compartment. Based on the findings from our model, we predicted that decreasing the relative contribution of AC8 will shift the cAMP-Ca2+ phase relationship from in-phase to out-of-phase. To test this prediction, we knocked down endogenous AC8 in MIN6 cells as previously done (Raoux et al., 2015) and observed that most cells exhibited out-of-phase cAMP oscillations within the AKAP79/150 compartment (average lag time 37 ± 9 s, n = 11) (Figure 2d), indicating an AC8-specific role in mediating the cAMP-Ca2+ phase signature.

Conversely, increasing the relative contribution of AC8, for example, by increasing the concentration of AC8 throughout the PM, should shift the cAMP-Ca2+ phase relationship from out-of-phase to in-phase. To test this prediction, we overexpressed full-length AC8 and examined the effect in the general plasma membrane compartment. Interestingly, we found that AC8 overexpression reversed the out-of-phase cAMP-Ca2+ phase relationship in a titratable manner, where the percentage of in-phase oscillating cells correlated with increasing amounts of co-transfected AC8 (average lag time 23 ± 2 s, n = 56) (Figure 2e, Figure 2—figure supplement 2a–d). In order to examine the effects of the targeted cAMP biosensors on AC8 expression, we also measured endogenous AC8 levels in cells transfected with either lyn-(Ci/Ce)Epac2-camps or AKAP79-(Ci/Ce)Epac2-camps and observed no significant difference (Figure 2—figure supplement 3a,b). These data demonstrate that higher levels of AC8 are sufficient to reverse the cAMP phase at the plasma membrane. In summary, these phase-manipulation experiments suggest that the cAMP-Ca2+ phase relationship is representative of a sensitive, compartmentalized balance between the Ca2+-stimulated activities of PDE1 and AC8.

### Membrane-localized AKAP150:AC8 nanoclusters regulate cAMP-Ca2+ oscillatory phase

The close spatial juxtaposition between the AKAP79/150 and general plasma membrane compartments presents a significant challenge for cAMP compartmentation, in that cAMP oscillations must be distinctly regulated within these adjacent signaling domains. Indeed, how cAMP, a rapidly diffusing small molecule, is spatially compartmentalized in cells is not yet completely understood, especially given the relatively low catalytic efficiency of a single cAMP-producing AC and degrading PDE (Conti et al., 2014; Lohse et al., 2017; Bock et al., 2020; Zhang et al., 2020). Given that AKAP79/150 exists in nanoclusters at the plasma membrane in multiple cell types (Mo et al., 2017; Zhang et al., 2016) and associates with AC8 in β cells (Willoughby et al., 2010), we hypothesized that AC8 could form nanoclusters on the plasma membrane of MIN6 cells and compartmentalize cAMP dynamics. To test this hypothesis, we examined the spatial organization of AC8 and AKAP150 at the membrane using Stochastic Optical Reconstruction Microscopy (STORM). We found that AKAP150 molecules were organized in clusters with a mean radius of 127 ± 9 nm and an average nearest-neighbor spacing of 313 ± 20 nm between cluster centers (n = 20) (Figure 3a and Figure 3—figure supplement 1), consistent with several recent reports demonstrating AKAP79/150’s tendency to form nanoclusters in other cell types (Mo et al., 2017; Purkey et al., 2018; Tajada et al., 2017; Zhang et al., 2016). Thus, the AKAP79/150 compartment-specific cAMP phase is likely representative of the balanced cAMP generation and degradation within these AKAP clusters.

![Figure 3.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig3-v1.jpg)

**Figure 3.:** (a) Representative super-resolution STORM image of the AKAP150 scaffold (scale 5 μm, inset 500 nm). Ripley-K analysis measures the average radii of the nanoclusters and indicates that AKAP150 forms clusters of 127 ± 9 nm, n = 20 (uniform random distribution control in inset). The nearest-neighbor distance distribution describes the distance between nanoclusters (average distance for AKAP150 is 313 ± 20 nm). (b) Representative super-resolution STORM image of Ca2+-sensitive AC8 (scale 5 μm, inset 500 nm) depicts AC8 nanoclusters of average radius 88 ± 8 nm and average nearest-neighbor distance 292 ± 16 nm, n = 16.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Histogram showing the size distribution (area, nm2) for AKAP150 (green) and AC8 (magenta) clusters derived from STORM imaging.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (a) A representative two-color STORM image of AKAP150 (green) and AC8 (magenta) in a MIN6 cell with specific examples of AKAP150/AC8 co-clusters to the right (scale 1 μm, inset 200 nm). Representative 1 x 1 μm scatter plot showing molecular localizations for AKAP150, color-coded with the values of L(200) (b) or Lcross(200) (c), which reflect the number of localizations of its own species or of the AC8 species, respectively, within a 200 nm radius of each AKAP150 localization. (d) Scatter plot of Lcross(200) and L(200) is shown for the representative ROI. AKAP150 localizations with a Lcross(200) score above 150 were considered co-clustered with AC8. (e) Summary of Getis-Franklin co-clustering analyses of the two-color STORM images identifying populations with different AKAP150/AC8 cluster relationships. A majority of AKAP150 localizations (72%) are co-clustered with AC8 localizations (n = 5 cells).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** FRAP curve for EGFP-tagged AC8 in MIN6 cells. AC8 diffuses slowly with an apparent diffusivity of 0.019 ± 0.002 μm2/s and an average immobile fraction of approx. 42.3% (n = 16, extrapolated).

Due to the known interaction between AKAP79/150 and AC8 (Willoughby et al., 2010) and diffusion of membrane-localized signaling complexes, we next probed the spatial organization and mobility of AC8. We found AC8 also distributes non-uniformly at the plasma membrane and forms clusters with a mean radius of 88 ± 8 nm and an average nearest-neighbor spacing of 292 ± 16 nm between cluster centers (n = 16) (Figure 3b; Figure 3—figure supplement 1). In order to measure the degree of colocalization between AKAP150 and AC8 nanoclusters, we also performed 2-color STORM and observed 72% of AKAP150 localizations were co-clustered with AC8 localizations, suggesting the presence of AKAP150:AC8 co-clustered nanodomains (Figure 3—figure supplement 2a–e). Next, to determine the mobility of AC8 molecules within the timescale of the oscillatory circuit’s period, we performed Fluorescence Recovery After Photobleaching (FRAP) with EGFP-tagged AC8 and found AC8 diffuses slowly at the membrane, and that there exists a significant immobile fraction (DAC8 = 0.019 ± 0.002 μm2/s, avg. % immobile = 42.3%, n = 16) (Figure 3—figure supplement 3).

With the evidence of the nanoscale organization of AKAP150 and AC8 on the plasma membrane, we further hypothesized that the increased spatial density of Ca2+-driven cAMP sources within the AKAP150 clusters, in conjunction with dispersed PDE1 in the cytosol (Bender and Beavo, 2006; Goraya et al., 2008), is important in compartmentalizing cAMP production and mediating the in-phase cAMP signal. To test this idea, we sought to build a mathematical framework to describe the spatial compartmentalization of the in- and out-of-phase cAMP-Ca2+ oscillations. Briefly, we expanded our network motif model (Figure 2c) by including a 3D spatial component with cAMP diffusion (DcAMP = 60 μm2/s; Agarwal et al., 2016) and incorporating our previously published well-mixed β cell model (Ni et al., 2011). We used the AKAP79/150:AC8 cluster pattern measurements from the STORM imaging to set model parameters in a hexagonal prism domain (200 nm edge, 600 nm depth), with one immobile AKAP79/150:AC8 cluster centered in the domain for simulation (Figure 4a, see Appendix 1 for model development details). By localizing AC8 within the AKAP79/150:AC8 cluster on the plasma membrane face and leaving PDE1 well-mixed throughout the volume, we could simulate Ca2+-driven cAMP oscillations that were in-phase within the immediate vicinity of a cluster, but sharply transitioned out-of-phase outside the cluster. Specifically, during a Ca2+ influx event, Ca2+-triggered cAMP production dominated at the center of the AKAP79/150 cluster while Ca2+-triggered cAMP degradation was favored outside the cluster at the PM and in the center of the unit volume (Figure 4a). Not surprisingly, the regime that recapitulates this phase relationship is sensitive to the spatially-restricted AC8/PDE1 balance and the diffusivity of cAMP. For example, by increasing the AC8 concentration within the cluster, the Ca2+-driven cAMP generative flux could exceed the rate of cAMP degradation by PDE1 and thus cAMP and Ca2+ oscillations could exist in-phase within both compartments (Figure 4—figure supplement 1). Alternatively, assuming that AC8 clustering is driven by AKAP150:AC8 interactions, weakening this interaction would then reduce the AC8 cluster stabilization and lead to a redistribution of AC8 away from the nanoclusters and a decrease in the local concentration of AC8 within the clusters (Figure 4b). Without the high local concentration of AC8 driving a net positive cAMP production within an AKAP79/150 cluster, the spatial domain where cAMP oscillates in-phase with Ca2+ is predicted to shrink while the out-of-phase regime expands and can reverse the phase at the cluster center (Figure 4c).

![Figure 4.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig4-v1.jpg)

**Figure 4.:** (a) 3D reaction-diffusion model with a single AKAP79/150:AC8 co-cluster positioned at the PM in the β cell in a hexagonal prism volume. cAMP oscillates in-phase immediately within the AKAP79/150:AC8 nanocluster due to the high effective concentration of AC8, but out-of-phase at the PM or cytosol due to the presence of PDE1 (cAMP – red, Ca2+– blue). (b) Disruption of the AKAP79/150:AC8 interaction can redistribute AC8 from within the cluster to the PM, shown by the half-Gaussian cross-sections and representative AC8 concentration heatmaps at the PM. (c) Heatmap depicting the time lag (s) for AC8 distribution (% Gaussian) and spatial distance (nm) from cluster center along PM.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Spatial simulations of cAMP (red) and calcium (black) when AC8 concentration is increased within the nanocluster. Entrainment of cAMP and calcium oscillations (in-phase) occurs globally at the plasma membrane (edge - top right, cluster center - bottom right).

To test this prediction, we overexpressed the amino terminus of AC8 (AC81-106) required for interaction with AKAP79/150 (Willoughby et al., 2010) to compete with the binding of endogenous AC8 to the endogenous AKAP150 scaffold. The disruption of the AKAP150:AC8 interaction was validated using a proximity ligation assay (PLA) to visualize the AKAP150:AC8 interaction in situ. Compared to non-transfected cells, cells expressing the AC81-106 peptide had a 39 ± 4% reduction in the PLA signals, indicating a decrease in the AKAP150:AC8 interaction (Figure 5—figure supplement 1a,b). Furthermore, STORM imaging showed that overexpression of the AC81-106 peptide led to a decrease in the percentage of AC8 single-molecule localizations within AC8 nanoclusters (n = 9) (Figure 5a), consistent with the predicted redistribution of AC8 molecules (Figure 4b). To test the impact of loss of AC8 molecules from the nanoclusters on the oscillation phase, we measured AKAP79/150-localized cAMP in the presence of AC81-106 and observed a significant increase in the average lag time (43 ± 6 s, n = 33) (Figure 5b). This is due to a higher proportion of cells exhibiting out-of-phase cAMP oscillations, indicating that the AKAP79/150:AC8 competitor peptide was sufficient in reversing the phase relationship in the AKAP79/150 compartment. Interestingly, we also observed many cells displaying irregular Ca2+ oscillations, as indicated by a disruption in the periodic timing of individual cells’ Ca2+ peaks (Figure 5b, left). This nanoscale perturbation establishes the regulatory role of the AKAP79/150:AC8 interaction in mediating the compartmentalized cAMP-Ca2+ phase relationship.

![Figure 5.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig5-v1.jpg)

**Figure 5.:** (a) Over-expression of the N-terminus of AC8, which is necessary and sufficient for mediating the AKAP79/150:AC8 interaction, redistributes AC8 from within nanoclusters to the general PM, as seen in the STORM image (scale 5 μm, inset 500 nm) and measured by the percent of localizations that fall into nanoclusters. (b) Disruption of the AKAP79/150:AC8 interaction lengthens the time lag between the cAMP (red) and Ca2+ (black) signals at the AKAP79/150 compartment (avg. time lag in absence of disruptor is 13 ± 3 s, n = 60, and in presence of disruptor 43 ± 6 s, n = 33) due to more cells displaying out-of-phase cAMP oscillations. *p=0.0341, ****p<0.0001; unpaired two-tailed Students t-test.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Widefield maximum intensity projections of a proximity ligation assay to depict the extent of interactions between AC8 and AKAP150 in MIN6 β cells (scale 10 μm). Expression of EGFP-tagged AC81-106 results in less PLA puncta per cell. (b) Number of PLA puncta per AC81-106-expressing cell is significantly decreased compared to non-transfected control (n = 142 and 57 cells, respectively) (****p<0.0001; unpaired two-tailed Student’s t-test).

### AKAP79/150-mediated phase relationship is critical for regulating oscillatory Ca2+

Next we systematically examined the impact of perturbing the precisely regulated phase relationship within the AKPA79/150 compartment. Due to the modulatory role of PKA in the Ca2+-cAMP-PKA oscillatory circuit and the interaction between PKA and AKAP79/150, we wondered how the in-phase cAMP oscillations with respect to Ca2+ are translated into PKA activities and if spatial compartmentalization of the phase relationship is also maintained at the PKA activity level. Therefore, we extended our 3D model to include AKAP79/150-associated PKA (see Appendix 1 for model details). In this extended model, PKA activity oscillations exhibit distinct phase relationships with respect to Ca2+ within and outside of the AKAP79/150 compartment (Figure 6—figure supplement 1a). To test this prediction, we fused our FRET-based biosensor for PKA activity (AKAR4) (Depry et al., 2011) to either full-length AKAP79 or the PM-targeting motif and expressed the sensors in MIN6 cells. Upon TEA stimulation, PKA activity was observed to oscillate with a lag time of 25 ± 6 s (n = 15) within the AKAP79/150 compartment but with a lag time of 55 ± 8 s (n = 12) (Figure 6—figure supplement 1b–e) at the general plasma membrane, indicating that the compartmentalized phase relationship is preserved from cAMP to PKA.

Spatiotemporal organization of PKA signaling and its phosphorylation targets via AKAPs have been implicated in regulating several important pathways. For example, PKA has been shown to phosphorylate CaV1.2 in an AKAP79/150-dependent manner, and this modification can influence the open probability of the channel (Murphy et al., 2014), suggesting a mechanistic link between local cAMP/PKA activity and global oscillatory Ca2+. Thus, we sought to study the functional role of the spatially compartmentalized cAMP-Ca2+ phase relationship in regulating intracellular Ca2+ dynamics. We measured Ca2+ oscillations by RCaMP in the presence of either the EGFP-tagged AKAP79/150:AC8 disruptor peptide, AC81-106, or EGFP alone as a control. Population-wide differences in Ca2+ dynamics, such as strength and timing, were observed in AC81-106-transfected cells and visualized in heat maps depicting the normalized Ca2+ signal per cell versus time (Figure 6a). Interestingly, we found that the expression of the disruptor peptide was correlated with a significant decrease in the peak ratio between the second Ca2+ peak and the first Ca2+ peak (control average −1.6%, n = 270; AC81-108 average −10.8%, n = 562) post TEA addition, indicative of less sustained oscillations (Figure 6b,c). In addition to intracellular Ca2+ concentration, the precise timing of internal oscillatory events is critical for modulating β cell functions such as glucose homeostasis and pulsatile insulin secretion (Fridlyand et al., 2010). In the presence of the disruptor peptide, cells also exhibited a longer elapsed time between oscillatory Ca2+ peaks (control average 3.9 ± 0.1 min, n = 270; AC81-108 average 4.6 ± 0.1 min, n = 562), suggesting that the timing of the signaling circuit was disturbed (Figure 6b,c). It is well established that besides the precise timing, the regularity of cytoplasmic Ca2+ in β cells is crucial in mediating pulsatile insulin secretion from the pancreas (Gilon et al., 2002; Schmitz et al., 2002). By stratifying the disruptor peptide-expressing cell population into ‘low, ‘medium,’ and ‘high’ expressers and performing a blinded classification of responding cells based on the regularity of the Ca2+ oscillation (see Appendix 1 for details), we found a positive correlation between the percentage of cells exhibiting irregular oscillations and the expression level of the disruptor peptide (42% for low-expressing vs. 68% for high-expressing AC81-106 disruptor) (Figure 6d). Taken together, these data signify that the compartmentalized cAMP-Ca2+ phase relationship regulates the oscillatory Ca2+ signal and plays an important role in determining the pace, regularity, and sustainability of the Ca2+ oscillations.

![Figure 6.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig6-v1.jpg)

**Figure 6.:** (a) Heatmaps depicting Ca2+ oscillations for 220 randomly selected cells co-expressing EGFP alone (control, left) or EGFP-tagged AC81-106 (AKAP79/150:AC8 disruptor, right), ordered by a mixed parameter describing the time lag between the first two Ca2+ peaks and the avg. timelag between all Ca2+ peaks. (b) Schematic describing two Ca2+ oscillatory parameters: the ratio between the first two Ca2+ peaks (R = P2 / P1) and the interpeak timing (t). (c) The peak ratio R is decreased in the presence of the AKAP79/150:AC8 disruptor (left), indicating less of a sustained Ca2+ oscillatory response. Over-expression of the disruptor also lengthens the timing between peaks (right). (d) The level of disruptor peptide expression is correlated with an increase in the percentage of cells exhibiting irregular oscillations (total n = 562). p=0.0054, ordinary one-way ANOVA.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (a) PKA activity is predicted to oscillate near the center of the AKAP79/150:AC8 cluster with a short time delay and a longer delay outside of the cluster, relative to Ca2+. (b) Experimentally-measured time lag between PKA activity oscillations and Ca2+ for AKAP79 (orange) and the general PM (teal) compartments (n = 15 and 12, respectively). **p=0.0063, unpaired two-tailed Student’s t-test. (c) Representative single cell trace showing in-phase PKA activity within the AKAP79 compartment. Orange trace is PKA activity at AKAP79 (CY-FRET channel divided by cyan donor channel) and black trace is Ca2+ (RFP). (d) Representative single cell trace showing out-of-phase PKA activity within the general PM compartment. Teal trace is PKA activity at PM (CY-FRET channel divided by cyan donor channel) and black trace is Ca2+ (RFP).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/55013/elife-55013-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** Stochastic simulations were performed for high and low AC8 counts of 200 (a) and 10 (b). (c) Reducing the AC8 count shifts the solution from in-phase to out-of-phase with respect to Ca2+, as predicted in the previous four component model. (d) Increasing the AC8 count suppresses cAMP noise within the system, relative to the mean.

## Discussion

Biological oscillations represent a rich way of encoding information using the amplitude and frequency. Here, we show the phase in an oscillatory signaling circuit represents a novel mode of informational encoding for which the phase itself can be spatiotemporally regulated. In the case of the Ca2+-cAMP-PKA circuit, the oscillatory cAMP/PKA phase relative to a widespread Ca2+ signal is distinctly regulated within two adjacent membrane compartments through intracellular organization of scaffolds and signaling effectors. Localized perturbation of this spatial phase signature disrupts global Ca2+ oscillations and thus has far-reaching consequences on the functional landscape of the β cell.

Compartmentalization of cAMP/PKA signaling is instrumental in processing a diverse set of inputs and mediating specific cellular functions; however, the mechanistic details of compartmentalization await to be fully elucidated (Musheshe et al., 2018). Given the measured kinetic rates of most ACs and PDEs, the generation of local cAMP gradients around single enzymes appears unfeasible (Conti et al., 2014). Context-dependent discrepancies in some of the kinetics (i.e. differences between in vitro and in vivo measurements) and slower cAMP diffusion due to buffering have been shown to be important for cAMP compartmentalization (Bock et al., 2020; Zhang et al., 2020). Here, we propose the nanoscale organization of key cAMP effectors and regulators as a novel mechanism for cAMP compartmentation. Despite the slow rates measured for individual ACs, we computationally and experimentally describe conditions in which the generation of compartmentalized cAMP can emerge from the clustering of many relatively immobile AC8 enzymes at the membrane and bulk distribution of PDE1 in the cytoplasm. Alterations to this nanoscale organization lead to dysregulated Ca2+ oscillations, demonstrating the functional importance of maintaining this organization. This system also serves as a nanoscale demonstration of how a cell can translate a global signal (Ca2+) into a compartmentalized signal (cAMP/PKA activity) by local activation and global inhibition, a strategy that is likely utilized in many other cellular contexts (Levchenko et al., 2000; Purvis and Lahav, 2013).

In order to understand the functional impact of the nanoscale architecture, it is important to also consider the discrete scale of such signaling organization. According to our rough estimates, approximately 15–150 individual AC8 molecules comprise AKAP150:AC8 nanoclusters (see Materials and methods for STORM-based estimation). To investigate the role of small molecule numbers, we recast our previous network motif model as a stochastic system and simulated the impact of changing initial conditions of PDE1 and AC8. We found that even in these discrete simulations, the previously noted phase relationships are preserved. As the balance between PDE and AC is perturbed, the system moves from an in-phase to an out-of-phase cAMP response with respect to Ca2+. Interestingly, we also noted that increasing the number of AC8 molecules leads to a reduction of the noise in the cAMP response. Thus, we predict that tuning AC8 cluster size might be a biological design strategy of nanoclusters to maintain accurate responses to perturbations (Figure 6—figure supplement 2a–d).

The interplay between Ca2+ and cAMP is very intricate, and multiple mechanisms could contribute to the observed dysregulated signaling effects upon perturbation of the AKAP79/150-compartmentalized cAMP-Ca2+ phase (Figure 6a–d). AKAPs can recruit PKA to regulate channel activities (Dell'Acqua et al., 2006; Mo et al., 2017; Torres-Quesada et al., 2017), such as in the regulation of voltage-mediated Ca2+ entry via PKA-dependent phosphorylation of CaV1.2 (Murphy et al., 2014) or the modulation of store-operated Ca2+ entry by both PKA-dependent STIM1 and Orai1 phosphorylation (Thompson and Shuttleworth, 2015; Zhang et al., 2019). Additional levels of regulatory feedback within the Ca2+-cAMP-PKA oscillatory circuit have also been identified, such as a negative feedback loop involving PKA phosphorylation of AC8, thereby fine-tuning the circuit dynamics (Willoughby et al., 2012).

The precisely regulated Ca2+ and cAMP oscillations are likely functionally important as insulin secretion requires coordination between Ca2+, cAMP, and PKA. Localized cAMP/PKA signaling at the AKAP79/150 scaffold and the in-phase oscillations of cAMP and Ca2+ within this compartment might play a critical role in regulating insulin secretion due to close interactions between AKAP79/150 and insulin secretory granules via CaV1.2 (Barg et al., 2001). Several important processes and components of the secretory machinery have been identified as targets of PKA signaling here, such as PKA-dependent mobilization of granules (Renström et al., 1997) and modulation of the synaptosomal protein SNAP25 (Gao et al., 2016). These PKA phosphorylation events may be highly coordinated with oscillations of Ca2+, which drive the exocytosis process for pulsatile insulin secretion. In addition to PKA-dependent secretory control, cAMP has recently been implicated to play a direct role in fusion pore formation via the cAMP-regulated guanine exchange factor Epac (Guček et al., 2019). Compartmentalized phase regulation of the Ca2+-cAMP-PKA oscillatory circuit at the AKAP79/150 macromolecular complex is likely involved in the regulation of many β cell processes, in addition to insulin secretion, and more work will be needed to further establish the mechanisms involved in decoding the information embedded in the local phase relationship.

The Ca2+-cAMP-PKA oscillatory circuit in pancreatic β cells integrates many important regulators of cellular function, and the precise coordination of each is required for proper signaling control. Here, we have uncovered a spatiotemporal organization of the circuit where the oscillatory phase between cAMP/PKA and Ca2+ depends on the spatial proximity of the AKAP79/150 scaffold protein and AC8. The construction principles of this signaling nanodomain, including the spatial distributions of sinks and sources, likely represent a generalized strategy for the generation of other compartmentalized signals and provide a unique modality in which cells embed, process, and produce signaling information.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>MIN6</td>
      <td>Dr. Jun-Ichi Miyazaki, Osaka University</td>
      <td>RRID:CVCL_0431</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Tetraethylammonium chloride (TEA)</td>
      <td>Sigma</td>
      <td>T2265</td>
      <td>20 mM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>8-Methoxymethyl-3-isobutyl- 1-methylzanthine (8MM-IBMX)</td>
      <td>Sigma-Aldrich</td>
      <td>M2547</td>
      <td>100 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Milrinone</td>
      <td>Alexis</td>
      <td>Cat# ALX-270–083 M005</td>
      <td>10 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Rolipram</td>
      <td>Alexis</td>
      <td>Cat# ALX-270–119</td>
      <td>1 μM</td>
    </tr>
    <tr>
      <td>Chemical compound, Drug</td>
      <td>KCl</td>
      <td>Sigma-Aldrich</td>
      <td>P9541</td>
      <td>15 mM</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Lipofectamine-2000</td>
      <td>Invitrogen</td>
      <td>11668019</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pCDNA3 AKAR4</td>
      <td>PMID:20838685</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>(Ci/Ce)Epac2-camps</td>
      <td>Dr. Dermot Cooper, University of Cambridge</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>AKAP79 (AKAP5, Homo sapiens)</td>
      <td>Dr. John D. Scott, University of Washington</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>AC8 (Adcy8, Rattus norvegicus)</td>
      <td>Dr. Dermot Cooper, University of Cambridge</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>ShAdcy8 Plasmid</td>
      <td>Dr. Jochen Lang, University of Bordeaux</td>
      <td>ShAdcy8 #2</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>RCaMP</td>
      <td>Dr. Loren Looger, Janelia Farms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>R-FlincA</td>
      <td>Dr. Kazuki Horikawa, Tokushima University Graduate School</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Duolink in situ red starter kit</td>
      <td>Sigma</td>
      <td>DUO92101</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Duolink in situ Probemaker MINUS</td>
      <td>Sigma</td>
      <td>DUO92010</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Duolink in situ Probemaker PLUS</td>
      <td>Sigma</td>
      <td>DUO92009</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AC8, rat polyclonal</td>
      <td>Abcam</td>
      <td>ab196686</td>
      <td>1:2000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AKAP150, rat polyclonal</td>
      <td>Millipore Sigma</td>
      <td>07–210</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-AKAP79, mouse monoclonal</td>
      <td>BD</td>
      <td>610314</td>
      <td>1:500</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-rabbit AlexaFluor647</td>
      <td>ThermoFisher Scientific</td>
      <td>A21245</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-mouse AlexaFluor568</td>
      <td>ThermoFisher Scientific</td>
      <td>A11031</td>
      <td>1:1000</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FIJI</td>
      <td>https://imagej.net/Fiji</td>
      <td>RRID:SCR_014294</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MetaFluor</td>
      <td>https://www.moleculardevices.com/</td>
      <td>RRID:SCR_002285</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>https://www.mathworks.com/</td>
      <td>RRID:SCR_001622</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>https://www.graphpad.com/ scientific-software/prism/</td>
      <td>RRID:SCR_002798</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>COPASI</td>
      <td>http://copasi.org/ Hoops et al., 2006</td>
      <td>RRID:SCR_014260</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Virtual Cell</td>
      <td>https://vcell.org/ Cowan et al., 2012</td>
      <td>RRID:SCR_007421</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Gene construction

For AKAP79-(Ci/Ce)Epac2-camps, AKAP79 (gene AKAP5, from Dr. John D. Scott) was PCR amplified to have HindIII/BamHI digestion sites, and (Ci/Ce)Epac2-camps (from Dr. Dermot Cooper) was PCR amplified to have BamHI/EcoRI digestions sites. Both fragments were inserted into a pcDNA3 (Invitrogen) backbone for mammalian expression (cAMP sensor is C-terminal to AKAP79). For AKAP79-AKAR4, a similar approach was taken where AKAR4 was dropped between BamHI/EcoRI. For AC8 (gene Adcy8, from Dr. D. Cooper), AC81-108, Gibson Assembly was used to insert the genes into the pcDNA3 mammalian expression vector. The ShAdcy8 construct for Adcy8 knockdown was previously verified and a gift from Dr. Jochen Lang. RCaMP was a gift from Dr. Loren Looger.

### Cell culture

MIN6 cells (a mouse insulinoma β cell line, gift from Dr. Jun-Ichi Miyazaki) were plated onto sterilized glass coverslips in 35 mm dishes and grown to 50–90% confluency in DMEM (10% FBS, 4.5 g/L glucose) at 37°C with 5% CO2. Identity was verified by phenotype (Ca2+ oscillations, morphology, and insulin secretion). Recurrent mycoplasma testing was performed and results were negative. Cells were transfected using Lipofectamine 2000 (Invitrogen) for 20–48 hr before imaging.

### Imaging

Cells were washed twice with Hank’s balanced salt solution buffer and maintained in the dark at room temperature. Cells were imaged on a Zeiss Axiovert 200M microscope with a cooled charge-coupled device camera (MicroMAX BFT512, Roper Scientific, Trenton, NJ) controlled by METAFLUOR 6.2 software (Universal Imaging, Downingtown, PA). Dual cyan/yellow emission from FRET used a 420DF20 excitation filter, a 450DRLP dichroic mirror, and two emission filters [475DF40 for CFP and 535DF25 for YFP]. RFP fluorescence was imaged using a 568D55 excitation filter, a 600DRLP dichroic mirror, and a 653DF95 emission filter. GFP fluorescence was imaged using a 480DF30 excitation filter, a 505DRLP dichroic mirror, and a 535DF45 emission filter. YFP fluorescence was imaged using a 495DF40 excitation filter, a 515DRLP dichroic mirror, and a 535DF25 emission filter. These filters were alternated by a filter-changer Lambda 10–2 (Sutter Instruments, Novato, CA). Exposure time was 50–500 ms, and images were taken every 10–30 s.

For confocal imaging, images were collected with a C2 plus on a Nikon Ti2 inverted microscope equipped with a Plan Apo lambda 60x oil immersion objective NA 1.4. YFP fluorescence was excited with the 488 nm line from a LU-N4 laser. Images were acquired with a DUVB detector collecting emission from 495 nm to 600 nm with a virtual spectral GaAsP detector controlled by NIS Elements software. The pinhole was set at 30 μm. Frame size was 1024 × 1024 pix.

For FRAP acquisition, cells were imaged using a C2 plus mounted on a Nikon Ti2 with a 488 nm laser (LU-N4 laser engine, Nikon Instruments) and sensitivity PMT detector (C2-DU3, Nikon) with 525/50 nm bandpass filter. The excitation light is reflected by a dichroic mirror 405/488/561/640 and focused through an Apo 100 × 1.49 NA objective. Image stacks were acquired in Galvano mode with unidirectional scanning with a 488 nm laser at 1.5% laser power with frame size 512 × 512 at scan zoom 2, one frame per second and 97.1 µm pinhole size. Small stimulation ROIs were drawn at the plasma membrane. The total FRAP series contained three images before bleaching (obtained with 2 s intervals), two cycles of ROI bleaching with the 488 nm laser at 100% laser power (5 frames at one frame per second), and two minutes of continuous acquisition to monitor fluorescence recovery.

### Image analysis

Fluorescence images were background-corrected by subtracting the fluorescence intensity of background with no cells from the emission intensities of cells expressing fluorescent reporters. Cells for experiments using the targeted biosensors were manually segmented from microscopy images based on emission intensity (YFP) and RCaMP (RFP) using custom-written Java and MATLAB scripts and whole-cell fluorescence emission was measured. The ratio of yellow/cyan emission (AKAR4) or cyan/yellow emission (Epac2-camps) and RFP intensity were then calculated at different time points using MATLAB scripts. The values of all-time courses were normalized by dividing each by the average basal value before drug addition. FRAP measurements were background-subtracted, bleach-corrected, and normalized, and fit to a previously described diffusion-dominant model (Ellenberg et al., 1997; Phair et al., 2004). For the AKAP150:AC8 disruption experiments, cells were segmented with custom CellProfiler (Broad Institute) pipelines based on RCaMP (RFP) fluorescence emission, and both RFP and GFP fluorescence intensities (EGFP-AC81-106) per cell were measured every 30 s. Graphpad Prism eight was used for visualization and statistical analysis. Custom-written MATLAB scripts were used for correlation analysis and regularity classification.

### Super-resolution imaging (STORM)

For fixed-cell stochastic optical reconstruction microscopy (STORM) imaging, cells were fixed with 4% paraformaldehyde (PFA) and 0.2% glutaraldehyde (GA) for 20 min and then washed with 100 mM glycine in HBSS to quench the free PFA. Cells were permeabilized and blocked in a permeabilization solution with 0.1% Triton X-100, 0.2% bovine serum albumin, 5% goat serum, and 0.01% sodium azide in HBSS. The cells were then incubated overnight at 4°C with an anti-AC8 antibody (Abcam, ab196686) at a 1:2000 dilution or an anti-AKAP150 (Millipore Sigma, 07–210) antibody at a 1:500 dilution, followed by 1 to 2 hr with goat anti-rabbit Alexa 647–conjugated antibody (ThermoFisher Scientific, A21245) at 1:1000 dilution. For the 2-color STORM experiments, cells were incubated with both the anti-AC8 antibody (1:2000 dilution) and an anti-AKAP79 antibody that recognizes a conserved epitope in AKAP150 (BD, 610314; raised against the C-terminal 248 residues of AKAP79 which shares 70% similarity with a region in AKAP150; 1:500 dilution), followed by a 2 hr incubation with a goat anti-rabbit Alexa 647-conjugated antibody (1:1000 dilution) and a goat anti-mouse Alexa 568-conjugated antibody (ThermoFisher Scientific, A11031; 1:1000 dilution). The cells were then post-fixed again in 4% PFA and 0.2% GA, quenched with 100 mM glycine in HBSS, and washed with HBSS to prepare for imaging. Immediately before imaging, the medium was changed to STORM-compatible buffer (50 mM Tris-HCl, pH 8.0, 10 mM NaCl, and 10% glucose) with glucose oxidase (560 μg/ml), catalase (170 μg/ml), and mercapto-ethylamide (7.7 mg/ml). STORM images were obtained using a Nikon Ti total internal reflection fluorescence (TIRF) microscope with N-STORM, an Andor IXON3 Ultra DU897 EMCCD, and a 100 × oil immersion TIRF objective. Photoactivation was driven by a Coherent 405 nm laser, while excitation was driven with a Coherent 647 nm laser or Coherent 561 nm laser.

All image analysis and image reconstruction were performed using both Nikon Elements analysis software and custom-written MATLAB scripts. Blinking correction was performed by implementing the pairwise Distance Distribution Correction (DDC) algorithm (Bohrer et al., 2019). Cluster property measurements were performed using Ripley-K analysis and custom mean-shift MATLAB code for segmentation, as described before (Mo et al., 2017). Co-clustering measurements were made using custom MATLAB scripts implementing Getis-Franklin pattern analysis, as described previously (Getis and Franklin, 1987; Mo et al., 2017). Briefly, we first calculated the degree of local clustering of AKAP150 molecules using the L(r) spatial statistic at r = 200 nm which counts the number of AKAP150 localizations within 200 nm (length scale of nanoclusters) of each AKAP150 localization, normalized appropriately. We then calculated Lcross(r) at r = 200 nm which counts the number of AC8 localizations within 200 nm of each AKAP150 localization, normalized appropriately. Plots of Lcross(200) vs. L(200) were generated and an L threshold of 150 was chosen based on the proportion of localizations found within clusters from the mean-shift segmentation analysis, and used to divide the plot into quadrants to calculate the proportion of AKAP150 localizations co-clustered with AC8 as previously described (Mo et al., 2017).

We obtained a very rough estimate of AC8 molecules within nanoclusters from our blink-corrected STORM datasets by assuming background localizations outside the cell are due to single secondary antibodies with conjugated dyes. We measured an average of 2 localizations per secondary antibody outside the cell and approximately 50 localizations per AC8 nanocluster within the cell. Estimating a labeling stoichiometry of 0.4–1.5 secondary antibodies per primary antibody and 0.4–1.5 primary antibodies per AC8 molecule (Zanacchi et al., 2017; Nieuwenhuizen et al., 2015), we can roughly approximate the number of AC8 molecules per nanocluster to be between 15 and 150 molecules/cluster (N = 3 cells).

### Proximity ligation assay

Antibodies for AC8 and AKAP150, mentioned in STORM section, were buffer exchanged into DPBS and conjugated with MINUS or PLUS oligos, following the Sigma DuoLink in situ Probemaker kits. PLA experiments were performed using the Duolink in situ red kit for PLAs according to the provided protocol. The only protocol modification was to extend the amplification time by 50 min. Briefly, cells were fixed and permeabilized as in the STORM experiments before incubation with PLUS and MINUS oligo-conjugated primary antibodies for 30 min at 37°C each, with washes after each step. Ligation of the nucleotides and amplification of the strand occurred sequentially by incubating cells with first ligase then polymerase and detection solution. PLA experiments with AKAP95 antibodies from different species were used as positive controls in HEK293T cells, and experiments with just one oligo-labeled primary antibody or the other were our negative control. Images were acquired on a Nikon Ti Eclipse epifluorescence scope with z-control and maximum intensity projections were created. A cross section of the DAPI-stained nucleus (3.6–5 μm) was also acquired and the number of dots per cell was counted using the nucleus as reference.

### Statistical analysis

Statistics, such as means, SEMs, and comparisons were calculated using Graphpad Prism 8 software. Experiments comparing multiple conditions were analyzed using one-way ANOVA or unpaired t-tests. Statistical significance was assessed using p<0.05 as a cutoff. Experiments were repeated >3 times. Individual cells with high expression of the AKAP79/150-fused biosensors were removed from analysis (see Appendix 1 for details).
