# Allosteric modulation in monomers and oligomers of a G protein-coupled receptor

## Authors

- Rabindra V Shivnaraine<sup>1</sup> ([ORCID: 0000-0002-1478-5422](https://orcid.org/0000-0002-1478-5422)) †
- Brendan Kelly<sup>1</sup>
- Krishana S Sankar<sup>2</sup>
- Dar'ya S Redka<sup>1</sup>
- Yi Rang Han<sup>1</sup>
- Fei Huang<sup>1</sup>
- Gwendolynne Elmslie<sup>3</sup>
- Daniel Pinto<sup>1</sup>
- Yuchong Li<sup>4</sup>
- Jonathan V Rocheleau<sup>2</sup>
- Claudiu C Gradinaru<sup>4</sup> †
- John Ellis<sup>3</sup> †
- James W Wells<sup>1</sup> †

### Affiliations

1. Department of Pharmaceutical Sciences, Leslie Dan Faculty of Pharmacy University of Toronto Toronto Canada
2. Department of Physiology University of Toronto Toronto Canada
3. Departments of Psychiatry and Pharmacology Hershey Medical Center Hershey United States
4. Department of Physics University of Toronto Toronto Canada

† Corresponding author

## Abstract

The M2 muscarinic receptor is the prototypic model of allostery in GPCRs, yet the molecular and the supramolecular determinants of such effects are unknown. Monomers and oligomers of the M2 muscarinic receptor therefore have been compared to identify those allosteric properties that are gained in oligomers. Allosteric interactions were monitored by means of a FRET-based sensor of conformation at the allosteric site and in pharmacological assays involving mutants engineered to preclude intramolecular effects. Electrostatic, steric, and conformational determinants of allostery at the atomic level were examined in molecular dynamics simulations. Allosteric effects in monomers were exclusively negative and derived primarily from intramolecular electrostatic repulsion between the allosteric and orthosteric ligands. Allosteric effects in oligomers could be positive or negative, depending upon the allosteric-orthosteric pair, and they arose from interactions within and between the constituent protomers. The complex behavior of oligomers is characteristic of muscarinic receptors in myocardial preparations.

## Introduction

Muscarinic acetylcholine receptors contain an orthosteric site and a topographically distinct allosteric site (Kruse et al., 2014; May et al., 2007). The latter is located at the extracellular surface within a vestibule to the orthosteric site (Kruse et al., 2013), and that region shows comparatively low sequence homology among the five muscarinic subtypes (M1–M5). The allosteric site therefore is more subtype-specific than the orthosteric site, and allosteric ligands are increasingly of interest for their therapeutic potential (Kenakin2004). Owing to the early demonstration of allosteric interactions in muscarinic systems (Clark et al., 1976; Stockton et al., 1983) and the variety of available modulators (May et al., 2007), the M2 muscarinic receptor has been a prototype for such effects within the broader family of G protein-coupled receptors (GPCRs).

Most studies of the interaction of an allosteric ligand with the allosteric site have been based on the modulation of events at the orthosteric site, typically on receptors in native membranes or detergent-solubilized extracts. Such events may be measured directly, as in the binding of a radiolabeled antagonist (Christopoulos et al., 2002), or they may be inferred from functional consequences such as the turnover of [35S]GTPγS (May et al., 2007). They also may be positive or negative (May et al., 2007), and the data generally have been described in terms of interactions between two binding sites on a monomeric receptor (Christopoulos et al., 2002).

In the case of the M2 receptor, an atomic-level view of the interaction within a monomer has emerged recently from the crystallography-derived structure of a biliganded receptor (Kruse et al., 2013) and from inferences based on molecular dynamics simulations (Dror et al., 2013). Although such results offer an explanation for negative cooperativity at the atomic level, the mechanism of action of positive modulators such as strychnine remains unclear (Dror et al., 2013). That uncertainty relates to questions regarding electrostatic repulsion between highly charged allosteric and orthosteric ligands, steric effects of the former on binding of the latter, and the effect of either ligand on conformational stability at the site of the other (Dror et al., 2013).

The common view that allosteric interactions occur within monomeric receptors is limited in its ability to rationalize complex effects that are seen in the binding of radioligands. For example, dissociation of the antagonist [3H]quinuclidinylbenzilate (QNB) from the M2 receptor is accelerated by gallamine at lower concentrations of the allosteric ligand and slowed at higher concentrations, resulting in a bell-shaped profile (Ellis et al., 1989). At equilibrium, the binding of [3H]QNB and the inverse agonist N-[3H]methylscopolamine (NMS) can display a biphasic and even a triphasic dependence on the concentration of an allosteric modulator (Proska et al., 1994; Shivnaraine et al., 2012). Such effects imply either that a single molecule of the receptor possesses up to four allosteric sites or that allostery occurs via linked sites within an oligomer (Proska et al., 1994; Shivnaraine et al., 2012).

To understand how a multimeric complex might account for allosteric behavior that resists explanation in terms of monomers, we have compared positive and negative allosteric modulators for their effects on oligomers and purified monomers of the M2 muscarinic receptor. Our approach has involved a novel FRET-based sensor of conformation at the allosteric site, mutants that allow only for allosteric modulation between linked protomers, mechanistic modeling, and molecular dynamics simulations. Taken together, the results indicate that intramolecular interactions—i.e., between two sites on a monomer or on the same protomer of an oligomer—are dominated by electrostatic repulsion and result in low-affinity negative modulation by the allosteric ligand. Intermolecular interactions—i.e., between two sites on neighboring protomers of an oligomer—result in high-affinity allosteric modulation that may be positive or negative, depending upon the constraints associated with ligand-binding and the nature and extent of conformational changes transmitted between protomers. The results provide a direct demonstration of how allosteric effects characteristic of M2 receptors arise from interactions between the constituent protomers of an oligomer.

## Results

### Binding of allosteric modulators to monomers

M2 receptors were solubilized as oligomers and purified as monomers in the manner described previously (Redka et al., 2013; 2014). cMyc- and FLAG-tagged receptors were extracted from co-infected Sf9 cells in digitonin–cholate, and oligomers were detected by co-immunoprecipitation (Figure 1A). The solubilized preparation was applied to an affinity resin of immobilized aminobenztropane (ABT), and western blotting of the purified receptor with an anti-M2 antibody indicated that 97% of the immunopositive material migrated as a monomer. Eighty-three percent migrated as a monomer when the sample was cross-linked with BS3 (Figure 1B and Figure 1—source data 1). The affinity of [3H]NMS for the purified monomer (Equation 3, log K = −8.01 ± 0.04, N = 5) and the purity of the sample were the same as reported previously (cf. Redka et al., 2013; 2014).

![Figure 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig1-v2.jpg)

**Figure 1.:** (A) Gels were loaded with samples of FLAG- and c-Myc-tagged receptor extracted from co-infected Sf9 cells (lane 1, 20–30 fmol of receptor per lane) or from the precipitate obtained upon treatment of the extract with an immobilized anti-FLAG antibody (lane 2, 15–35 fmol of receptor per lane). The amount of receptor was determined from the binding of [3H]QNB at the saturating concentration of 10 nM. Following electrophoresis and transfer, the membranes were blotted with anti-c-Myc antibody. (B) Gels were loaded with parallel samples of purified M2 receptor taken before (lane 1) and after cross-linking with BS3 (lane 2). The same amount of receptor was applied to each well (15–25 fmol). The intensities of the immunopositive bands were measured by densitometry, and the area under each densitometric trace was determined in three segments as indicated by the braces (a, 40–75 kDa; b, 75–170 kDa; c, 170–360 kDa) (Figure 1—source data 1, N = 3). The monomeric receptor migrated as a doublet (~44 kDa and 53 kDa). (C) The rate constant for the dissociation of [3H]QNB from purified monomers was measured at graded concentrations of gallamine (kobsd) and normalized to that in the absence of gallamine (k0) to obtain the relative rate constant (kobsd/k0) plotted on the y-axis. The data were analyzed in terms of Equation 2 to obtain the fitted curve shown in the figure (solid line) and the parametric values listed in Figure 1—source data 1. (D) [3H]NMS (10 nM) was mixed with gallamine at the concentrations shown on the x-axis, and binding was measured after incubation of the reaction mixture for 21 hr at 30°C. The solid line represents the best fit of Equation 2 (n = 1), and the fitted parametric values are listed in Figure 1—source data 1. The dashed lines in panels C and D are the fitted curves from similar experiments on preparations in which the M2 receptor is largely or wholly oligomeric (C, Sf9 membranes; D, Sf9 extracts) (Shivnaraine et al., 2012). (E–G) The binding of [3H]NMS (10 nM) to M2 receptors extracted from porcine sarcolemmal membranes (closed symbols) and purified as monomers from Sf9 cells (open symbols) was measured at graded concentrations of strychnine following the simultaneous addition of both ligands (E), the sequential addition of strychnine and [3H]NMS (F), and the sequential addition of [3H]NMS and strychnine (G). The binding profiles obtained following simultaneous addition were identical after incubation of the samples for 3 hr and 21 hr, and the data obtained after 21 hr are shown in the figure. Pretreatment with one ligand was followed after 2 hr by the addition of the other and further incubation for 3 hr. The temperature of incubation was 30°C throughout. The solid lines in each panel depict the best fits of Equation 2 to the data from three experiments taken in concert, and the parametric values are listed in Figure 1—source data 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The binding of [3H]NMS (A) or [3H]QNB (B) to M2 receptor in membranes from CHO cells was measured at the concentrations of strychnine shown on the x-axes. Strychnine and the radioligand were added simultaneously to the receptor, and the reaction mixture was incubated for 3 hr (○, •) and 12 hr (□, ▪) at 30°C. The concentrations of [3H]NMS and [3H]QNB were 0.131 ± 0.003 nM and 0.022 ± 0.005 nM, respectively, and the corresponding affinities (KD) were 0.46 ± 0.03 nM and 0.039 ± 0.008 nM. Data from three (3 hr) or two (12 hr) experiments were analyzed simultaneously according to Equation 2, taken with two terms for [3H]NMS (n = 2) and one term for [3H]QNB (n = 1). The lines depict the best fits of the model, and the parametric values are listed in Figure 1—source data 2.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Total specific binding of the orthosteric ligand (RL + ARL) at graded concentrations of strychnine was simulated according to Figure 6 (Equations 13–17) with the parametric values listed in Figure 1-source data 3. The concentration of NMS was taken as equal to the dissociation constant (i.e., 10 nM). The level of binding was computed for different times after the simultaneous addition of both ligands (A), after the addition of NMS to a system pre-equilibrated with strychnine (B), and after the addition of strychnine to a system pre-equilibrated with NMS (C). The times of incubation were as follows: 5 min (a), 20 min (b), and sufficient time for the attainment of equilibrium (c).

Monomeric M2 receptors retain the interaction between ligands at the allosteric and orthosteric sites. The allosteric modulator gallamine slowed the dissociation of [3H]QNB, and the time-course of the dissociation was mono-exponential under all conditions. The dose-dependence of the decrease in the rate constant was monophasic with a Hill coefficient of 1 (Figure 1C, Figure 1—source data 1). Gallamine therefore appears to slow the release of [3H]QNB from monomers via a single allosteric site. In contrast, two or more allosteric sites can be inferred from the bell-shaped behavior of receptors that are predominantly or wholly oligomeric (Shivnaraine et al., 2012) (Figure 1C, Figure 1—source data 1).

Monomers of the M2 receptor equilibrated slowly with [3H]NMS and either gallamine or the allosteric modulator strychnine when the two ligands were added simultaneously, and incubation for 21 hr was required for the attainment of equilibrium at 30°C. The binding profile upon equilibration was monophasic downward in each case, and the data can be described by a single hyperbolic term (i.e., Equation 2, n = 1) (Figure 1D and E; Figure 1—source data 1). Gallamine and strychnine therefore appear to modulate the equilibrium binding of [3H]NMS to monomers via a single allosteric site.

The monophasic nature of effects observed at purified monomers differs from the triphasic effect of gallamine on the binding of [3H]NMS to M2 receptors in other preparations, including membranes and detergent-solubilized extracts from Sf9 cells, CHO cells, and porcine atria (e.g., Figure 1D, broken line) (Shivnaraine et al., 2012). Those multiphasic curves and the Hill coefficients of the individual components, taken together, are indicative of at least four interacting allosteric sites, which in turn are suggestive of four interacting receptors within a tetramer or larger oligomer. Similarly, the bell-shaped pattern obtained for strychnine in atrial extracts (Figure 1E–G) and in membranes from CHO cells (Figure 1—figure supplement 1, Figure 1—source data 2) is indicative of at least two allosteric sites and also points to an oligomer.

Allosteric ligands bind in a vestibule to the orthosteric site (Kruse et al., 2013), forming a cap that impedes the binding and dissociation of the orthosteric ligand (Figure 6) (Shivnaraine et al., 2012). Interference by one ligand in the binding kinetics of another leads to binding patterns that depend upon the order of mixing in a system that has not attained equilibrium. Such kinetic effects were examined experimentally by varying the sequence in which strychnine and [3H]NMS were added to the receptor. In one protocol, the two ligands were added simultaneously and incubated with the receptor for 21 hr to obtain the pattern at equilibrium. In another, one ligand was pre-equilibrated with the receptor prior to the addition of the second, and the mixture was incubated for a further 3 hr to obtain the pattern at a time prior to equilibrium.

With receptors in atrial extracts, the effect of strychnine on the binding of [3H]NMS was bell-shaped under all conditions (Figure 1E–G, Figure 1—source data 1). With purified monomers, strychnine was strictly inhibitory except when the receptor was pre-equilibrated with [3H]NMS, when there was no effect (Figure 1E–G, Figure 1—source data 1). The patterns observed in experiments on monomers are consistent with the patterns observed in simulations performed according to Figure 6 (Figure 1—figure supplement 2, Figure 1—source data 3), which describes a mechanism for allosteric capping of the orthosteric site in a monomer.

### A FRET-based sensor of allosteric effects

Allosteric effects that produce multiphasic binding profiles such as those illustrated by the dashed lines in Figure 1C,D have been attributed to a combination of inter- and intramolecular interactions within oligomers (Shivnaraine et al., 2012). For more direct information on those interactions and related conformational changes, we developed a sensor based on FRET between FlAsH and mCherry. FlAsH was incorporated via the hairpin-forming sequence FLNCCPGCCMEP (FCM) (Hoffmann et al., 2010), which was inserted after Val166 in the second extracellular loop (ECL2), and mCherry was fused to the amino terminus (i.e., mCh-M2-FCM).

A fluorophore at the N-terminus of the M2 receptor has been shown previously to have no discernible effect on various properties, including transport of the receptor to the plasma membrane, agonist-induced responses, and the binding of muscarinic ligands (Pisterzi et al., 2010). Localization at the plasma membrane also was not affected by the modifications described here, as visualized by fluorescence from either the fused fluorophore or bound FlAsH (Figure 2—figure supplement 1), nor was there any apparent change in the binding properties. The affinity of the receptor for [3H]NMS was essentially the same, as measured in preparations of membrane-bound and detergent-solubilized mCh-M2-FCM from transfected CHO cells (Equation 3: membranes, log K = −9.52 ± 0.10, N = 3; extract, log K = −8.26 ± 0.22, N = 3). The modified receptor also retained the triphasic allosteric effect of gallamine on the binding of [3H]NMS, as measured in membranes from CHO cells expressing mCh-M2-FCM (Figure 2—figure supplement 2).

Molecular models of the native M2 receptor, mCh-M2-FCM, and the FlAsH-bound sensor were rendered from the crystal structures of mCherry (2H5Q) (Shu et al., 2006) and the receptor in an active state (4MQS) (Kruse et al., 2013). A structure of the sensor showing the positions of FlAsH and mCherry is given in Figure 2A. Insertion of the FlAsH-reactive sequence in ECL2 created a rigid extended loop (Figure 2B) without perturbing the conformation of the loop in the region of the adjacent EDGE motif. There was no distortion of the extended loop upon the addition of FlAsH.

![Figure 2.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig2-v2.jpg)

**Figure 2.:** (A) A computed molecular model of the M2 receptor (red) fused at the N-terminus to mCherry (yellow) and labeled with FlAsH (green) at a tetracysteine motif inserted in ECL2 between Val166 and Gly167. (B) Expanded views of ECL2 with the insert FCM and FlAsH. (C) M2 receptor bearing mCherry and the FlAsH-reactive insert (mCh-M2-FCM) was expressed in CHO cells and treated with FlAsH. Images were collected upon excitation at 498 nm and 0.37 µW. The emission spectrum from a single cell is shown in the figure (C). The spectrum was unmixed (Equation 10) to obtain the contributions of donor (kD, green) and acceptor (kA, red) to the fitted sum (black). (D) CHO cells expressing mCh-M2-FCM or the mCherry-tagged wild-type M2 receptor (mCh-M2) were treated with FlAsH and excited at 498 nm. The FRET efficiencies (Eapp) calculated for individual cells are shown as histograms, and the dashed lines depict the best fits of the Gaussian distribution (dark grey bars, mCh-M2-FCM, 31 cells, μ = 59.2 ± 1.2, σ = 7.7 ± 3.0; light grey bars, mCh-M2, 34 cells, μ = 0.50 ± 0.35, σ = 1.8 ± 0.5. (E) mCh-M2-FCM was expressed in CHO cells and reacted with FlAsH, and the value of Eapp was measured before and after addition of the inverse agonist NMS (1 µM, N = 26), the allosteric modulator gallamine (Gal, 10 mM, N = 42), NMS (1 µM) plus gallamine (10 mM, N = 18), the agonist carbachol (Car, 1 mM, N = 19), and the partial agonist pilocarpine (Pilo, 1 mM, N = 19). The ligand-dependent changes in Eapp are plotted in the figure (i.e., ∆Eapp ± S.D.), and the values are listed and compared in Figure 2—source data 1. The mean value of Eapp for cells in the absence of ligand was 60 ± 8% (N = 26).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** CHO cells were transfected with plasmids coding for mCh-M2-FCM (A), mCh-M2(D103A)-FCM (B), M2-FCM (C), eGFP-M2 (D), mCh-M2 (E), and eGFP-M2-mCh (F). Images were recorded on a confocal microscope, as described in Materials and methods, and those shown in the figure were obtained at the middle of the cell in the Z-plane. Cells were labelled with FlAsH and excited at 488 nm to obtain the images in A–C. eGFP was excited at 488 nm to obtain the image in D, and mCh was excited at 561 nm to obtain the images in E and F.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Membranes were prepared from CHO cells expressing M2 receptor bearing mCherry at the N-terminus and the FlAsH-reactive sequence FCM in the second extracellular loop. The binding of [3H]NMS was measured at the concentrations of gallamine (M) shown on the x-axis. Both ligands were added simultaneously, and the reaction mixture was incubated for 16 hr at 25ºC. The line depicts the best fit of Equation 2 to all of the data taken in concert. The values of log Kj were common to all of the data, and the fitted estimates are as follows: log K1 = −6.39 ± 0.10, log K2 = −3.15 ± 0.63, log K3 = −2.60 ± 0.59. The values of nH(j) were indistinguishable from 1, either individually or collectively (p≥0.13), and were fixed accordingly. The mean concentration of [3H]NMS was 3.08 ± 0.05 nM. Points at the left- and right-hand ends of the abscissa (F) depict binding in the absence of unlabeled ligand and in the presence of 3 μM atropine.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** CHO cells expressing the eGFP- and mCherry-tagged M2 receptor were excited at 473 nm at a power of 0.37 µW. The emission spectrum was recorded from the region of the plasma membrane and analyzed to obtain the apparent FRET efficiency. (A) The distribution of FRET efficiencies from 33 cells. The dotted line depicts the best fit of a Gaussian distribution (μ = 9.51, σ = 0.11). (B) The mean FRET efficiency (± S.D.) measured in the absence of ligand, in the presence of NMS (1 µM) (9.1 ± 1.6, 20 cells), or in the presence NMS (1 µM) plus gallamine (1 mM) (9.7 ± 1.0, 18 cells)

To examine the mobility of a fluorophore at the amino terminus, eGFP was fused to the wild-type M2 receptor (eGFP-M2) and to a truncated mutant lacking the first 13 amino acids (eGFP-truncM2). This truncation shortened the link between the fluorophore and the first helical domain and was expected to increase the likelihood that the movement of eGFP would approximate that of the fusion protein as a whole. Each tagged receptor was expressed in CHO cells and extracted in digitonin–cholate, and the rotational correlation time (φ) of the fused fluorophore was estimated from the fluorescence anisotropy according to Equations 4–9. The full-length receptor was examined with and without ligands, and eGFP alone was taken as a control.

Both the fluorescence (Equation 6) and the anisotropy (Equation 9) decayed as a single exponential under all conditions, and the parametric values are listed in Figure 2—source data 1. The value of 18 ns obtained for the correlation time of free eGFP agrees favourably with that of about 20 ns reported previously (Devauges et al., 2012) and was sixfold longer than the fluorescence lifetime of 3 ns. In contrast, values of 30–55 ns were obtained for eGFP-truncM2, eGFP-M2, and the various liganded states of eGFP-M2. Such values are at least 12–22-fold longer than the corresponding lifetimes of 2.5–2.6 ns, and the latter are much shorter than the 12-ns measuring window of the fluorescence decay. The rotational correlation times obtained for receptor-bound eGFP therefore are indistinguishable, and the movement of the fluorophore at the N-terminus of the receptor appears to be determined primarily by the tumbling of the whole protein, with or without ligands.

Excitation of bound FlAsH at 498 nm gave the observed emission spectrum and unmixed components shown for a typical cell in Figure 2C. Fluorescence from the acceptor accounted for most of the total signal at 610 nm, and the corresponding peak derived predominantly from FRET. Only 6% of the emission from the acceptor came from direct excitation, and it was accounted for during spectral unmixing. The apparent FRET efficiency of each cell was calculated from the normalized amplitudes of the unmixed spectra (Equations 10 and 12), and the efficiencies from all cells gave a distribution centered on 60% with a width of 18% at half-maximal amplitude (Figure 2D). Controls in which FlAsH was reacted with mCherry-tagged receptors lacking the FCM sequence gave a narrow distribution centered on 0.5% (Figure 2D), confirming the specificity of the reaction with FlAsH.

The emission spectrum and corresponding FRET efficiency between FlAsH and mCherry was measured for each cell before and after the addition of various ligands. The inverse agonist NMS caused a marked increase in the amplitude of the peak near 610 nm, as illustrated in Figure 3A. Smaller increases were obtained with the partial agonist pilocarpine, the allosteric modulator gallamine, and the combination of gallamine plus NMS. In contrast, the agonist carbachol caused a decrease. The differences in efficiency at individual cells were averaged over all cells to obtain the mean for each ligand (Figure 2E, Figure 2—source data 1), which varied from an increase of 20 percentage points with NMS to a decrease of 22 percentage points with carbachol. The partial agonist pilocarpine caused an increase of 7.3 percentage points. These changes indicate that the sensor can distinguish between agonists and an inverse agonist at the orthosteric site. Gallamine caused an increase of 5.0 percentage points and reduced the increase caused by NMS from 22 to 8.0 percentage points, indicating that the sensor detects the effect of the allosteric ligand on NMS.

![Figure 3.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig3-v2.jpg)

**Figure 3.:** The sensor (mCh-M2-FCM) (A), a mutant thereof that does not bind NMS [mCh-M2(D103A)-FCM] (B), and the mutant plus the wild-type M2 receptor (C) were expressed or co-expressed in CHO cells and reacted with FlAsH. The cultures were irradiated before (– – ◯ – –) and after (— □ —) the addition of NMS (1 μM), and the emission spectra from individual cells were unmixed to determine the contribution of each component (kD and kA, Equation 10) and the corresponding FRET efficiency (Eapp, Equation 12). (D) Ligand-dependent changes in the FRET efficiency (ΔEapp) were averaged over 18–42 cells transfected as described for panels A–C, and the means (± S.D.) are plotted in the figure. The values are listed and compared in Figure 3—source data 1. The value for mCh-M2-FCM is replotted from Figure 2F. (E) A depiction of intermolecular cooperativity within a hetero-oligomer of the M2 receptor in which binding is precluded at the orthosteric site of one mutant (M2-D103A) and the allosteric site of another (M2-ECL2+ve). (F) CHO cells expressing M2-ECL2+ve alone (○) or together with M2-D103A (□) were solubilized in digitonin–cholate, and hetero-oligomers were purified as described in the text. Aliquots of each sample were added to solutions of [3H]NMS (10 nM) and gallamine at the concentrations shown on the x-axis, and binding was measured after incubation of the mixture for 21 hr at 30°C. The solid lines represent the best fits of Equation 2 to the combined data from 3 experiments, and the parametric values are as follows: ○, n = 1, log K = −3.46 ± 0.16; □, n = 3, log K1 = 6.25 ± 0.16, log K2 = 4.29 ± 0.37, log K3 = 3.31 ± 0.29. All values of nH(j) were indistinguishable 1 and fixed accordingly (p≥0.06). The broken line is the difference between the fitted curves for M2-ECL2+ve and the copurified heteromer. [3H]NMS bound to detergent-solubilized M2-ECL2+ve with an affinity of 5.5 nM (Equation 3, log K = −8.26 ± 0.10, nH = 1, N = 3).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) CHO cells were cotransfected with the plasmids coding for eGFP-M2 and mCh-M2(D103A)-FCM. The cells were treated with FlAsh, and those expressing both receptors were identified by the presence of both eGFP and mCherry. (B, C) The emission was recorded in absence of ligand (B) and in the presence of NMS (1 μM) (C), and the spectra were unmixed according to Equation 11 to obtain the contribution of each fluorophore. The circles are the measured spectrum, and the solid lines are the best fits of Equation 11. The dashed lines depict the constituent spectra as follows: eGFP, blue; FlAsH, green; mCherry, red. The FRET efficiency between FlAsH and mCherry was computed from the unmixed contributions according to Equation 12.

A receptor bearing eGFP at the N-terminus and mCherry rather than FlAsH-FCM after Val166 in ECL2 gave a comparatively narrow distribution of FRET efficiencies with a mean of about 10% and a width of about 4% (Figure 2—figure supplement 3A). The effects of NMS and gallamine on FRET were eliminated (Figure 2—figure supplement 3B), suggesting that the insertion of mCherry within ECL2 disrupts the vestibule to the orthosteric site. The distribution of FRET efficiencies was narrower than that obtained with FlAsH and mCherry in the sensor, where the greater width of 40% may arise from differences in the labelling efficiency of FlAsH among different cells.

### Intermolecular modulation of FRET

The substitution of alanine for aspartic acid at position 103 of the M2 receptor removes the counter-ion for positively charged ligands at the orthosteric site (Haga et al., 2012). That mutation has been shown previously to prevent the specific binding of [3H]NMS or [3H]QNB to M2 receptors in HEK293 membranes at concentrations of the radioligand up to 10 nM (Heitz et al., 1999). The same mutation in the sensor prevented the specific binding of [3H]NMS at a concentration of 1 µM, as measured with mCh-M2(D103A)-FCM extracted from transfected CHO cells in digitonin–cholate. It also eliminated the effect of NMS on FRET. There was essentially no change in the emission spectrum at 610 nm (Figure 3B), in contrast to the increase observed with FlAsH-treated mCh-M2-FCM (Figure 3A); also, the NMS-dependent increase in the mean FRET efficiency was reduced from 21.6 ± 11.2 percentage points in mCh-M2-FCM to 0.45 ± 0.55 percentage points in the mutant (Figure 3D, Figure 3—source data 1).

Sensitivity to NMS was recovered when the binding-deficient mutant was co-expressed with the wild-type M2 receptor (Figure 3C and D), resulting in a ligand-dependent change in the mean FRET efficiency of 9.5 ± 1.8 percentage points (Figure 3D, Figure 3—source data 1). The recovery indicates that M2 receptors occur at least partly as oligomers in which the conformation in the region of the allosteric site of one protomer is affected by a ligand at the orthosteric site of another.

In cells such as that represented in Figure 3C, co-existence of the wild-type receptor and FlAsH-reacted mCh-M2(D103A)-FCM is inferred from the effect of NMS on FRET. To confirm the cellular co-localization of the two proteins, cells were co-transfected with the plasmids for mCh-M2(D103A)-FCM and the wild-type receptor fused at the N-terminus to eGFP (eGFP-M2). Those FlAsH-treated cells displaying three fluorophores, and therefore both proteins, were identified by their spectral properties, and those spectra were unmixed to obtain the individual contribution from each fluorophore (Figure 3—figure supplement 1). NMS increased the FRET efficiency between FlAsH and mCherry by 5.3 ± 0.1 percentage points (N = 26) rather than 9.5 percentage points, in a further indication that the conformational change detected by FRET in one protomer derives from the binding of the ligand to another.

### Intermolecular modulation of binding

The first two inflections of the triphasic binding profile exhibited by gallamine have been attributed to intermolecular modulation via allosteric sites on different protomers of an oligomer (Shivnaraine et al., 2012). In a direct test for such interactions, the three negatively charged residues of the EDGE motif in ECL2 were replaced by three positively charged residues (i.e., KRGK) to obtain a mutant in which the binding of a cationic ligand such as gallamine to the allosteric site is precluded by electrostatic repulsion (M2-ECL2+ve). When the mutant was expressed in CHO cells and extracted in digitonin–cholate, the substitution was found to be without effect on the affinity of [3H]NMS for the orthosteric site (Equation 3, log K = −8.26 ± 0.10, N = 3). The triphasic pattern revealed by gallamine at the wild-type receptor was lost, however, and in its place was a single inflection of comparatively low affinity (log K = −3.46 ± 0.16) (Figure 3F).

FLAG-tagged receptors lacking the orthosteric site (FLAG-M2(D103A)) then were co-expressed with hexahistidyl-tagged receptors lacking the allosteric site (His6-M2-ECL2+ve), and purified complexes containing at least one copy of each mutant were obtained by successive passage of detergent-solubilized material on an immuno-affinity column of immobilized anti-FLAG antibody (Santa Cruz Biotechnology) and a chelating resin of Ni2+-NTA (Figure 3E). Binding of [3H]NMS to the purified heteromer displayed a triphasic dependence on the concentration of gallamine (Figure 3F), and the apparent affinities calculated in terms of Equation 2 (Figure 3F, legend) were in good agreement with those reported for the wild-type receptor (Figure 1—source data 1) (Shivnaraine et al., 2012). The magnitude of the inhibitory effect corresponding to the allosteric sites of weakest affinity was much less than that observed with the wild-type receptor (cf. Figure 1D, broken line). It was diminished further when corrected by subtraction of the single inhibitory component observed with M2-ECL2+ve (Figure 3F, broken line).

### Molecular dynamics simulations of the liganded receptor

Allosteric effects were examined in molecular dynamics simulations at the atomic level, starting from the crystal structure of the monomeric M2 receptor occupied by the agonist iperoxo (4MQS) (Kruse et al., 2013). The ligand and accessory proteins were removed, and conformations of the receptor were sampled from a canonical ensemble accessible within a period of 30 ns. Simulations were performed in the absence of membrane and detergent, and ligands were docked prior to initiating the calculation. Interactions between allosteric and orthosteric ligands (Figure 4—figure supplement 1) were found to be affected by the degree of electrostatic repulsion between their positive charges and the conformational changes induced in one site by a ligand at the other, which together determine the positional stability of each ligand in its respective site.

The effect of electrostatic repulsion was evaluated by two correlates (Table 1): the distance between the spatial centers of the cationic nitrogen atoms of the two ligands (e.g., strychnine and NMS, Figure 4A; gallamine and QNB, Figure 4B), and changes in the electrostatic potential of an allosteric ligand upon the addition of an orthosteric ligand. All four allosteric–orthosteric pairs showed a degree of electrostatic repulsion, but steric effects reduced the difference between strychnine and gallamine to less than would be predicted on the basis of charge alone (Table 1). Gallamine has three cationic groups and therefore experiences greater electrostatic repulsion overall, but each group is surrounded by sterically bulky and electron-rich ethyl groups that diminish the repulsive effect (Figure 5—figure supplement 1). Also, the smaller steric load born by the single cationic nitrogen atom of strychnine allows for positioning closer to the orthosteric site.

**Table 1.**
 Correlates of electrostatic repulsion between orthosteric and allosteric ligands. The inter-cationic distance was calculated as that between the cationic nitrogen atom of the orthosteric ligand and the closest cationic nitrogen atom of the allosteric ligand. The difference in electrostatic potential was calculated as the increase in electrostatic energy of an allosteric modulator at a receptor with a vacant orthosteric site over that of the same modulator at a receptor with NMS or QNB at the orthosteric site.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="4">Allosteric–orthosteric pair</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Str_R_NMSa</td>
      <td>Str_R_QNB</td>
      <td>Gal_R_NMS</td>
      <td>Gal_R_QNBa</td>
    </tr>
    <tr>
      <td>Inter-cationic distance (Å)</td>
      <td>13.7</td>
      <td>15.7</td>
      <td>16.5</td>
      <td>16.8</td>
    </tr>
    <tr>
      <td>Difference in electrostatic potential (kcal/mol)</td>
      <td>0.0085</td>
      <td>0.063</td>
      <td>0.096</td>
      <td>0.41</td>
    </tr>
  </tbody>
</table>

_a The distances are shown in Figures 4A and B._

![Figure 4.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig4-v2.jpg)

**Figure 4.:** Models of the liganded receptor were simulated by molecular dynamics as described in Materials and Methods. The region of the ligand-binding sites is shown in the figure, with NMS and strychnine (A, C) or with QNB and gallamine (B, D) at the ortho- and allosteric sites, respectively. (A, B) The electrostatic potential of each ligand is displayed on a molecular surface within 4.5 Å of the constituent atoms (positive potential, blue; negative potential, red). The values and corresponding arrows are the distances between the centers of the cationic ammonium groups of the orthosteric and allosteric ligands. The closest such group is shown in the case of gallamine. (C, D) The bound ligands are shown together with residues involved in receptor-ligand interactions.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The ligands shown are: NMS, N-methylscopolamine; QNB, quinuclidinylbenzilate; Str, strychnine; and Gal, gallamine. Different liganded states of the receptor are identified as X_R_Y, where X and Y are the allosteric and orthosteric ligands, respectively. Occupancy is represented as O for a vacant site or as Str, Gal, NMS, or QNB for a ligand-occupied site.

A network of interactions serves as a conformational link between the allosteric and orthosteric sites. Three tyrosine residues form a hydrogen-bonded aromatic cap over the orthosteric site (i.e., Tyr104, Tyr403, and Tyr426) (Kruse et al., 2013). Between the cap and the allosteric site is a tryptophan residue that interacts with the cationic nitrogen atom of the allosteric ligand (i.e., Trp422). Tyrosine 426 within the aromatic cap and Trp422 are linked via the peptide backbone of helix 7 (Figure 5). In the absence of an orthosteric ligand, the orientation of Trp422 is unfavorable for the interaction with a cationic allosteric ligand (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig5-v2.jpg)

**Figure 5.:** (A) The three residues of the aromatic cap (i.e., Tyr104, Tyr403, and Tyr426) and Trp422 are shown in an overlay of the results of three simulations: a vacant receptor (yellow), a QNB-bound receptor (green), and a receptor occupied by both QNB and gallamine (pink). The ligands are not shown. (B) The receptor with QNB at the orthosteric site. (C) The receptor with QNB at the orthosteric site and gallamine at the allosteric site. Here and elsewhere, different liganded states of the receptor are identified as X_R_Y, where X and Y are the allosteric and orthosteric ligands, respectively. Occupancy is represented as O for a vacant site or as Str (strychnine), Gal (gallamine), NMS, or QNB for a ligand-occupied site.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Strychnine adopts a similar pose at the vacant receptor and in the presence of either NMS (A) or QNB at the orthosteric site. The position of gallamine at a vacant receptor (B) is consistent throughout the simulation. At a QNB-bound receptor (C), gallamine is pushed outward, and its orientation is more variable. The orthosteric ligands are not shown in (A) and (C).

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Changes in the distance between the α-carbon atoms of Tyr177 and Asn419 were taken as a measure of the effect of an orthosteric ligand on the conformation of the allosteric site. The structures of the receptor with QNB (3UON, white) and iperoxo (4MQS, pink) at the orthosteric site are superimposed, and the allosteric site is shown as occupied by strychnine. The perspective is toward the extracellular surface of the receptor.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The distances from all frames of the molecular dynamics simulations over the production period of 30 ns are shown in the figure for a receptor with NMS (A) or QNB (B) at the orthosteric site. In each case, the allosteric site was vacant (red), occupied by strychnine (green), or occupied by gallamine (blue).

Binding of NMS or QNB at the orthosteric site reduces the mobility of the residues of the aromatic cap (e.g., Figure 5A and B) and orients Trp422 to interact with the cationic group of an allosteric ligand. The effect is greater with QNB than with NMS owing to the additional phenyl ring of QNB. Binding of an allosteric ligand draws the aromatic cap outward, leading to destabilization of the orthosteric ligand and greater flexibility in the region of the orthosteric site (e.g., Figure 5A and C). The effect is greater with gallamine than with strychnine, owing to the greater size and charge of gallamine, and it is suggestive of a reduction in the affinity of the receptor for orthosteric ligands.

Gallamine and strychnine affect the conformation of the receptor through interactions between the cationic ammonium group of each allosteric ligand and the side-chains of Trp422 and Tyr177. Gallamine also affects the receptor through π-cation interactions with Tyr80 and Tyr83 and through electrostatic interactions with Glu172 of the EDGE motif. The overall conformational effect of these interactions was tracked by measuring the distance between the α-carbon atoms of Tyr177 and Asn419. That distance is a measure of the width of the vestibule (e.g., Figure 5—figure supplement 2), and it differs among crystal structures of the M2 receptor in different liganded states (Figure 5—source data 1): namely, with QNB in the orthosteric site (3UON) (Haga et al., 2012), with iperoxo in the orthosteric site (4MQS), and with iperoxo in the orthosteric site and LY2119620 in the allosteric site (4MQT) (Kruse et al., 2013).

The width of the vestibule in simulations with NMS or QNB at the orthosteric site was distributed as shown in Figure 5—figure supplement 3. The allosteric site was vacant (e.g., O_R_NMS) or occupied by strychnine or gallamine (e.g., Str_R_NMS or Gal_R_NMS). The mean distances obtained for all nine liganded and unliganded states are listed in Figure 5—source data 2. When the allosteric site is vacant or occupied by strychnine, the vestibule is wider with QNB than with NMS at the orthosteric site. The greater width is due to the additional phenyl ring of QNB, which disrupts the positions of Tyr403, Trp422, and Asn419. The vestibule is narrowest with strychnine and NMS. Other combinations of ligands have little or no effect owing to the bulk of QNB, the charge on gallamine, or both.

Destabilisation of the aromatic cap plus the electrostatic repulsion that exists with all positively charged allosteric–orthosteric pairs seems likely to prevent the simultaneous binding of both ligands to a monomeric receptor. The least disruptive effects of one ligand on the binding of another occurred with NMS and strychnine owing, in part, to conformational flexibility afforded by one ligand at the site of the other. The most disruptive effects occurred with QNB and gallamine owing to interactions involving the second phenyl ring of the former and the additional cationic centers of the latter (Figure 4C and D).

## Discussion

Allostery at the M2 muscarinic receptor generally has been understood in terms of interactions within a monomer (Christopoulos et al., 2002), but that view disregards the tendency of GPCRs to form oligomers (Park et al., 2004). Moreover, the oligomeric nature of the M2 receptor is evident in the multiphasic effects of allosteric ligands on the dissociation rate of orthosteric antagonists and their binding at equilibrium (Shivnaraine et al., 2012) (e.g., Figure 1). Such effects appear to involve at least four allosteric sites in a mix of intra- and intermolecular heterotropic interactions within a complex of receptors that is tetrameric or larger (Shivnaraine et al., 2012).

We show here that all such complexity is lost when the M2 receptor is purified as a monomer (Figure 1). Gallamine and strychnine were strictly inhibitory in their effect on the binding of [3H]NMS and [3H]QNB, and the rate of dissociation of [3H]QNB was decreased at all concentrations of gallamine. In each case, the dose-dependence was monophasic with a Hill coefficient of 1. Ligands therefore bind to monomers in the manner expected for a protein with one allosteric site and one orthosteric site, in contrast to the behavior of M2 receptors in myocardial membranes and unprocessed solubilized preparations.

With either gallamine or strychnine, the potency defined by the single phase observed with monomers is similar to that defined by the weakest of the two or three components of the multiphasic curves observed with oligomers. It follows that effects associated with allosteric sites of higher affinity are a property of oligomers and derive from intermolecular interactions among the constituent protomers. They include the positive effect of gallamine on the rate of dissociation of [3H]QNB (Figure 1C) and varied effects on the binding of [3H]NMS at equilibrium: namely, negative cooperativity at sites of high affinity for gallamine (Figure 1D; log K1 = −5.69, Figure 1—source data 1), apparent positive cooperativity at sites of intermediate affinity for gallamine (Figure 1D; log K2 = −4.59, Figure 1—source data 1), and positive cooperativity at sites of high affinity for strychnine (Figure 1E–G).

In the case of gallamine, two further lines of evidence from CHO cells confirm the existence of heterotropic interactions between neighboring protomers and the relationship between those interactions and the allosteric sites of higher affinity. First, mutants lacking either the allosteric site or the orthosteric site were copurified from cotransfected cells to obtain a heteromer that lacks the capacity for intramolecular interactions. The purified complex retained the sites of high and intermediate affinity for gallamine that are seen in native preparations of the wild-type receptor but not the site of low affinity (Figure 3E,F); whereas the former are associated with oligomers, only the latter is observed in monomers. Second, the orthosteric site was eliminated in an M2 receptor bearing mCherry at the N-terminus and FlAsH in ECL2, which together serve as a FRET-based sensor of conformation at the allosteric site (Figures 2A). The FRET efficiency of the binding-deficient mutant was affected by NMS only when the mutant was co-expressed with the wild-type receptor (Figure 3D).

Three lines of evidence indicate that the FRET-based sensor reports primarily on changes at the allosteric site. A comparison of the fluorescence anisotropies measured for eGFP fused to the N-terminus of the M2 receptor suggests that the region of the fusion is comparatively rigid and unaffected by orthosteric ligands. In contrast, the FRET efficiency of the sensor expressed alone in CHO cells was increased or decreased by orthosteric ligands in a manner that tracked the pharmacological identity of the ligand as an agonist, a partial agonist, or an inverse agonist (Figure 2F). Ligand-dependent changes in FRET between FlAsH and mCherry therefore appear to result from changes in the position of ECL2-bound FlAsH. Finally, NMS increased the FRET efficiency by 20 percentage points. Such a change is consistent with the predictions of molecular dynamics simulations for the effect of NMS on the width of the vestibule to the orthosteric site (Figure 5—source data 1) (Dror et al., 2013).

Allosteric and orthosteric ligands may interact via steric hindrance, conformational changes, or electrostatic effects. In the structure computed for a monomeric M2 receptor, the interaction between gallamine or strychnine on the one hand and NMS or QNB on the other is dominated by electrostatic repulsion (Figure 4, Table 1). That explains why gallamine and strychnine were inhibitory in their effect on the binding of [3H]NMS to purified monomers (Figure 1B and C), and it suggests a molecular basis for the weak affinities of both ligands in those assays. It also suggests that electrostatic repulsion dominates intramolecular cooperativity between allosteric and orthosteric ligands within the constituent protomers of an oligomer.

The molecular dynamics simulations place each allosteric ligand at the extracellular surface, where it caps the vestibule to the orthosteric site and sterically hinders passage of the orthosteric antagonist (Figure 4). This arrangement is consistent with crystallographic data on the location of a positive allosteric modulator, LY2119620 (Kruse et al., 2013), and with the kinetics of allosteric modulation. A kinetically defined model that describes capping in a monomeric receptor (Figure 6) predicts that the rate at which the system equilibrates will depend upon the order in which the ligands are added to the receptor (Figure 1E–G). The predicted effects were observed experimentally with purified monomers of the M2 receptor, in that equilibration was slowest when [3H]NMS preceded strychnine (Figure 1—figure supplement 2).

![Figure 6.](https://cdn.elifesciences.org/articles/11685/elife-11685-fig6-v2.jpg)

**Figure 6.:** Each ligand can bind separately to form AR or RL, but the ternary complex is accessible only via RL. The orthosteric site of the M2 receptor is located within the cluster of helical domains, with access via a vestibule that forms the allosteric site. Occupancy of the latter by an allosteric ligand precludes association and dissociation of the orthosteric ligand. The parameters k−L and k+L are the first- and second-order rate constants for the binding of L to R; similarly, k−A and k+A are the first- and second-order rate constants for the binding of A to R. The parameters k−AL and k+AL are the rate constants for the binding of A to RL.

Allosteric effects in monomers are monophasic, necessarily intramolecular, exclusively negative, and of comparatively low affinity. Those in oligomers may be positive or negative and generally reveal two or more affinities, the weakest of which corresponds to that in monomers. The versatility of oligomers is a consequence of additional mechanistic pathways made possible by intermolecular interactions, which avoid the electrostatic repulsion that dominates intramolecular interactions and enforces negative cooperativity within monomers. Such intermolecular effects presumably are mediated by ligand-sensitive conformational changes transmitted from one protomer of receptor to another.

Although the details of allosteric modulation cannot be determined through simulations based solely on a monomer, some insight into the effects observed with different ligand-pairs may be gained by monitoring the residues that form an aromatic cap over the orthosteric site (i.e., Tyrosines 104, 403, and 426). Positive allosteric modulation by strychnine (Figure 1E), negative modulation by gallamine at sites of high affinity, and apparent positive modulation by gallamine at sites of intermediate affinity (Figure 1D) occurred only with NMS as the radioligand. It appears, however, that the positive modulatory effects of strychnine and gallamine are different in kind. Whereas strychnine caused a net increase in the binding of [3H]NMS, gallamine never raised the level of binding above that in its absence.

The effect of strychnine is a clear example of positive cooperativity, but that of gallamine appears to be an attenuation of negative cooperativity. Strychnine and NMS therefore were the only ligand-pair to display positive cooperativity that was self-evident and unambiguous. They also are the ligand-pair that caused minimal disruption of the aromatic cap in molecular dynamics simulations, and positive cooperativity may be a consequence of attendant conformational flexibility in that region of the receptor. The least flexibility was observed with QNB and gallamine, which engaged only in negative cooperativity.

A similar pattern is seen in the distance between the α-carbon atoms of Tyr177 and Asn419, which is a measure of the width of the vestibule that accommodates the allosteric ligand. Decreases in the width from that in the vacant receptor (11.4 Å) were observed only with NMS at the orthosteric site of an otherwise vacant receptor (10.9 Å) and only with strychnine at the allosteric site of a NMS-liganded receptor (10.1 Å). There was little effect of QNB alone or of other ligand-pairs.

Direct evidence for interactions between the protomers of an oligomer has been obtained by precluding intramolecular effects in studies involving the FRET-based sensor and the binding of [3H]NMS, and molecular dynamics simulations have provided some insight into the underlying conformational effects. Taken together, the results suggest that intermolecular interactions are associated with narrowing of the vestibule and conformational flexibility around the aromatic cap. Such an arrangement would allow an allosteric ligand to bind with high affinity to protomers with a vacant orthosteric site and thereby to increase the binding of an orthosteric ligand to linked protomers with a vacant allosteric site.

The role of oligomers formed by GPCRs of Family 1A is debated, in part because oligomers are not seen to possess a unique or obligatory functionality. Both monomers and oligomers can activate G proteins, and both display allosteric communication between agonists at the receptor and guanylyl nucleotides at the G protein (Redka et al., 2014). In the case of the M2 muscarinic receptor, however, the two forms mediate those effects by different mechanisms. Only oligomers mimic the binding patterns observed in native membranes (Redka et al., 2014). We show here that oligomers of the M2 receptor also are responsible for the high-affinity binding of allosteric ligands and for positive allosteric modulation. Whereas both effects are observed routinely with M2 receptors in natural membranes, neither is expected or observed with monomers. These observations illustrate the cooperative capability of oligomers formed by GPCRs, and they add to the complexity that must be accommodated in a mechanistic understanding of events at the level of the receptor.

## Materials and methods

### Construction of plasmids

Substitutions, insertions, and deletions of bases were performed by site-directed mutagenesis (Quick-Change, Agilent Technologies). PAGE-purified primers were obtained from Integrated DNA Technologies (IDT). Constructs were prepared in pcDNA3.1 for expression in CHO cells and in Bac-N-Blue (Life Technologies) for expression in Sf9 cells. The human M2 muscarinic receptor was used throughout, and all sequences were confirmed by DNA sequencing (Centre for Applied Genomics, Hospital for Sick Children, Toronto).

#### Fluorophore-tagged variants of the M2 receptor

The receptor was fused at the N-terminus to eGFP (eGFP-M2) or mCherry (mCh-M2). To obtain a FRET-based sensor with fluorescein arsenical hairpin binder (FlAsH) as the donor, the second extracellular loop (ECL2) of mCh-M2 was modified by insertion of the FlAsH-reactive sequence MLMCCPGCCMEP (FCM) between Val166 and Gly167(mCh-M2-FCM). Similarly, mCherry was inserted between Val166 and Gly167 in eGFP-M2. To assess the rotational motion of a fluorophore at the N-terminus, eGFP was fused to the full-length receptor (eGFP-M2) and to a truncated mutant lacking the first 13 amino acids (eGFP-truncM2) (forward primer, 5'-GGCATGGACGAGCTGTACAAGAATAGTCCTTATAAGAC-3'). Further details are provided in Appendix 1

#### Binding-defective mutants of the M2 receptor

To preclude binding to the allosteric site, negatively charged residues in the EDGE sequence at positions 172–175 of ECL2 were replaced by positively charged residues (i.e., Lys172Arg173Gly174Lys175). To preclude binding to the orthosteric site, aspartic acid at position 103 was replaced by alanine in the wild-time receptor [M2(D103A)] and the sensor [mCh-M2(D103A)-FCM]. Further details are provided in Appendix 1.

### Expression, extraction, and purification of the M2 receptor

#### Sf9 cells

Human M2 muscarinic receptor bearing the c-Myc or FLAG epitope at the N-terminus was expressed in Sf9 cells as described previously (Redka et al., 2014; Shivnaraine et al., 2012) and in Appendix 1. The cells were harvested and solubilized in digitonin–cholate (0.86% digitonin, Wako Chemicals USA; 0.17% cholate, Sigma-Aldrich), and aliquots of the extract were removed for electrophoresis and binding assays. The receptor was purified in predominantly monomeric form by successive passage on DEAE-Sepharose, ABT-Sepharose, and hydroxyapatite. The final concentrations of digitonin and cholate were 0.1% and 0.02%, respectively. Purified receptor was stored at −75°C. Further details regarding the purification and the nature of the purified receptor have been described previously (Redka et al., 2014).

#### CHO cells

Chinese Hamster Ovary (CHO) cells stably expressing the wild-type human M2 receptor were grown and processed as described previously (Redka et al., 2014; Shivnaraine et al., 2012). Cells for transient transfections were grown and processed as described in Appendix 1.

To obtain membranes for binding assays, thawed cells containing wild-type M2 receptor or mCh-M2-FCM were homogenized and processed as described previously (Redka et al., 2014; Shivnaraine et al., 2012). To obtain extracts for measurements of binding or fluorescence anisotropy, thawed cells containing mCh-M2-FCM, M2-ECL2+ve, M2-ECL2+ve plus M2(D103A), eGFP-M2, or eGFP-truncM2 were washed in buffer A [20 mM HEPES, 20 mM NaCl, 1 mM EDTA, 0.1 mM PMSF, Complete Protease Inhibitor Cocktail tablets (Roche, 1 tablet/50 mL), adjusted to pH 7.40 with NaOH] and centrifuged for 10 min at 3,000 × g and 4°C. The washed cells were resuspended in buffer A, and the mixture was homogenized with three bursts of a Brinkman Polytron (setting 6, 10 s). An aliquot of 100 μL was removed for the determination of total protein. The homogenate then was centrifuged for 30 min at 45,000 × g and 4°C, and the pellet was resuspended in buffer A (5.5 g of protein per L) with three bursts of the Polytron (setting 6, 10 s). Solubilization was initiated by the addition of digitonin and sodium cholate to final concentrations of 0.86% and 0.17%, respectively, and the mixture was agitated on a rocking platform for 15 min at room temperature. The sample then was diluted 1:1 in buffer A and centrifuged for 45 min at 45,000 × g and 4°C. The supernatant fraction was concentrated (Amicon Ultra-4, 30 kDa, Millipore) and divided into aliquots that were stored at −75°C (Redka et al., 2014; Shivnaraine et al., 2012). Such extracts from cells expressing mCh-M2-FCM or M2-ECL2+ve were characterized for the binding of [3H]NMS at graded concentrations of the radioligand.

To obtain purified oligomers containing both FLAG-tagged M2(D103A) and His6-tagged M2-ECL2+ve, the solubilized receptor was applied successively to columns of Ni2+-nitriloacetic acid (NTA)-agarose (Qiagen) and anti-FLAG Sepharose (Sigma-Aldrich). The columns were pre-equilibrated with buffer A supplemented with digitonin (0.1%) and cholate (0.04%), and the receptor was eluted with the same buffer containing imidazole (150 mM) (Sigma-Aldrich) or FLAG peptide (100 μg/mL) (Sigma-Aldrich), respectively.

#### Porcine atria

The M2 receptor is the predominant muscarinic subtype in porcine atria (Wreggett et al., 1995). It was extracted from sarcolemmal membranes according to a two-step procedure in which the membranes were resuspended in buffer B (20 mM imidazole, 1 mM EDTA, 0.1 mM PMSF, 0.02% NaN3, adjusted to pH 7.60 with HCl) supplemented with digitonin (0.36%) and cholate (0.08%) (5.5 g of total protein per L), recovered by centrifugation, and resuspended in buffer B supplemented with digitonin (0.8%) and cholate (0.08%). The soluble fraction from the second resuspension, which contained the M2 receptor, was stored at −70°C until required for binding assays. Further details have been described previously (Shivnaraine et al., 2012) and are summarized in Appendix 1.

### Cross-linking, immunoprecipitation, and electrophoresis

#### Cross-linking

A solution of the cross-linker bis(sulfosuccinimidyl)suberate (BS3, Pierce) in deionized water (20 mM) was added to an aliquot of the receptor to yield a final reagent concentration of 2 mM. The mixture was incubated for 30 min at 24°C, and the reaction was terminated by the addition of Tris-HCl (1 M, pH 8.00) to a final concentration of 20 mM. After further incubation for 15 min at 24°C, the sample was stored on ice prior to electrophoresis. Controls lacking BS3 were prepared in parallel under otherwise identical conditions.

#### Co-immunoprecipitation

An aliquot of the extract (500 μL) from Sf9 cells co-expressing the FLAG- and c-Myc-tagged receptors was supplemented with a 50% slurry (20 µL) of agarose-conjugated anti-FLAG anti-body (Santa Cruz Biotechnology, Inc.). The mixture was shaken overnight at 4°C, and immunoadsorbed receptor was collected by centrifugation. The precipitated beads then were washed 4 times with 3 mL of buffer C (20 mM HEPES, 1 mM EDTA, 0.1 mM PMSF, adjusted to pH 7.40 with NaOH) supplemented with digitonin (1%) and cholate (0.001%), and the entire precipitate was applied to the polyacrylamide gel. Following electrophoresis and transfer, the nitrocellulose membrane (Bio-Rad, 0.45 µm) was blotted with anti-c-Myc antibody (Santa Cruz Biotechnology, Inc.) as described previously (Ma et al., 2007).

#### Electrophoresis and western blotting

Details regarding these procedures are described Appendix 1.

### Labeling of the M2 receptor with FlAsH in live cells

TC-FlAsH was obtained as a kit from Molecular Probes (Invitrogen), and labeling was carried out under reduced light according to a procedure adapted from the manufacturer’s instructions (Hoffmann et al., 2010). Transfected CHO cells growing at 50–75% confluency were washed twice with PBS, and the medium was changed to Opti-MEM reduced serum medium (Life Technologies, Inc.). After further incubation of the cells for 1 hr at 37°C, the medium was removed and replaced by a freshly prepared labeling solution of FlAsH in reduced serum medium (2.5 μM, 1 mL per dish). The culture was incubated for 20 min at 37°C in 5% CO2; the labeling solution then was removed, and the cells were washed twice in a buffer containing 500 µM BAL (Life Technologies, Inc.). During the second wash, the BAL buffer was left for 5 min at 37°C prior to its removal. Washed cells were prepared for imaging by the addition of DMEM (2 mL) supplemented with 50 mM HEPES at pH 7.40 (Gibco Life Technologies, Inc.).

### Binding assays

N-[3H]Methylscopolamine ([3H]NMS, 87 Ci/mmol) and (−)-[3H]quinuclidinylbenzilate ([3H]QNB, 42 Ci/mmol) were purchased from PerkinElmer as a solution in ethanol, which was removed by evaporation prior to use. Strychnine, gallamine, carbachol, pilocarpine, and unlabeled NMS and QNB were purchased from Sigma-Aldrich. All other reagents were from the sources described previously (Shivnaraine et al., 2012).

Binding was measured at pH 7.40 in buffer C or buffer D (Dulbecco’s phosphate-buffered saline, Sigma-Aldrich D5652, supplemented with 1 mM CaCl2 and 1 mM MgCl2). In the case of detergent-solubilized preparations, buffer C was supplemented with digitonin (1%) and cholate (0.02%). The separation of free and bound radioligand was achieved by chromatography on Sephadex G-50 Fine in the case of detergent-solubilized receptor and by filtration on fiberglass filters or microcentrifugation in the case of membrane-bound receptor. Further details have been described previously (Shivnaraine et al., 2012).

The net dissociation of [3H]QNB over time was analyzed in terms of a single exponential according to Equation 1, in which kobsd is the rate constant; Bobsd represents total binding of the radioligand at time t, and Bt=0 and Bt→∞ are the initial and asymptotic levels of binding, respectively.

$$
B_{obsd}=(B_{t=0}−B_{t→∞})e^{−k_{obsd}t}+B_{t→∞}
$$

Time-courses at one or more concentrations of gallamine were accompanied in the same experiment by a control lacking the allosteric ligand. The data from all traces were analyzed in concert with a single value of Bt→∞ and separate values of kobsd and Bt=0. The constraint on Bt→∞ was without appreciable effect on the sum of squares (p>0.05). The value of kobsd measured in the absence of gallamine was designated k0 and used to normalize each value measured in the presence of gallamine (i.e., kobsd/k0).

Dose-dependent effects of an allosteric modulator (A) on the normalized rate of dissociation of the radioligand (kobsd/k0) or on the level of total binding at a specified time (Bobsd) were analyzed empirically in terms of Equation 2.

$$
Y_{obsd}=Y_{[A]→∞}+(Y_{[A]=0}−Y_{[A]→∞})\sumj=1n\frac{F_{j}K_{j}^{n_{H(j)}}}{[A]_{t}^{n_{H(j)}}K_{j}^{n_{H(j)}}}
$$



$$
\sum_{j=1}^{n}F_{j}=1
$$

Estimates of binding at graded concentrations of [3H]NMS were analyzed in terms of Equation 3.

$$
B_{obsd}=B_{max}\frac{([P]_{t}−B_{sp})^{n_{H}}}{K^{n_{H}}+([P]_{t}−B_{sp})^{n_{H}}}+NS([P]_{t}−B_{sp})
$$

The parameter Bmax represents the maximal specific binding of the radioligand (P), and Bobsd and Bsp represent total and specific binding, respectively, at the total concentration [P]t; nH is the Hill coefficient, and K is the concentration of unbound [3H]NMS that corresponds to half-maximal binding. NS is the fraction of unbound radioligand that appears as nonspecific binding. Fitted estimates of the Hill coefficient ranged from 0.93 to 1.03 and were indistinguishable from 1 (p>0.05).

Analyses in terms of Equations 1–3 typically were performed on data from replicate experiments, which were taken in concert to obtain single fitted values of parameters that are expected to be invariant (i.e., kobsd, K, nH). In figures that show the results of such analyses, data from individual experiments have been presented with reference to a single fitted curve. To obtain the values plotted on the y-axis, measured estimates of Bobsd or Yobsd were adjusted according to the equation $Y^{′}=Y[f(x_{i},a¯,b)/f(x_{i},a,b)]$ (Park et al., 2002). The function f represents the fitted equation, and xi represents the independent variable at point i. The vectors a and b represent fitted parameters that were estimated separately for each experiment (a) or as a single value common to all experiments (b); $a¯$ is the corresponding vector in which parametric values that differed among different experiments have been replaced by the means. Individual values of $Y'$ at the same xi were averaged to obtain the mean and standard error plotted in the figure. Details regarding the optimization of parameters and statistical procedures are described in Appendix 1.

### Fluorescence, microscopy, and image-analysis

The rotational flexibility of eGFP fused to the N-termini of the wild-type M2 receptor (eGFP-M2) and a truncated mutant (eGFP-truncM2) was measured by time-resolved fluorescence anisotropy of single molecules in a locally constructed instrument. Each fusion protein was expressed in CHO cells and solubilized at a concentration of 3–10 nM in buffer C supplemented with detergent (0.8% digitonin, 0.04% sodium cholate). Aliquots of the extract were applied to a coverslip and excited at 480 nm with an excitation beam obtained by frequency-doubling the output of a femtosecond laser (Tsunami HP, Spectra Physics, Santa Clara, CA, USA).

The emission from a confocal volume 5 µm above the surface was passed through a Plan-Apochromat oil-immersion objective (100×, Carl Zeiss, Canada) and projected onto an avalanche photodiode (APD). The emission was divided by means of a polarization cube into two beams with orthogonal polarizations and collected on two different detectors (PDM-5CTC, MPD, Milano, Italy). Photon arrival times were recorded at 4 ps resolution using a multichannel counter (PicoHarp300, PicoQuant, Germany).

The fluorescence signals from the two detectors were fit globally in Matlab using custom-written software and a Levenberg-Marquardt algorithm with iterative re-convolution. Repetitive excitation and the color off-set (s) between measurements of the instrument response function (IRF) and the fluorescence were accounted for according to Equations 4 and 5, in which dpar and dperp represent the parallel and perpendicular decays before convolution.

$$
D_{par}=IRF_{par},s⊗d_{par}
$$



$$
D_{perp}=IRF_{perp},s⊗d_{perp}
$$

The fluorescence signal in each plane was summed to obtain the total fluorescence at time t (F(t)), and the lifetime was obtained according to Equation 6.

$$
F(t)=\frac{A}{1−exp(−\frac{T}{\tau})}exp(−\frac{t}{\tau})
$$

The parameter A in Equation 6 is the amplitude, and T is the repetition time of the laser (i.e., 12.5 ns); t is the time bin, and τ is the decay constant. Corrections for collecting the fluorescence emission in the parallel and perpendicular planes through a high numerical-aperture lens were performed according to Equations 7 and 8.

$$
d_{perp}=(\frac{1}{3})F(t)(1+(1−3k_{2})r(t))
$$



$$
d_{par}=G(\frac{1}{3})F(t)(1+(2−3k_{1})r(t))
$$

The correction factors k1 and k2 have values of 0.33 and 0.065, respectively. The correction factor G corrects for the difference in the sensitivity of detection between the two channels and was taken as 1.061, as determined from a solution of rhodamine 110 (10 nM). The rotational correlation time of eGFP (φ) was estimated from the loss of anisotropy (r) over time (t) according to Equation 9, in which r(0) is the amplitude of the decay.

$$
r(t)=r(0)(exp(−\frac{t}{\phi}))
$$

Where r0 is the is the decay amplitude and ϕ is the rotational correlation time.

Confocal imaging of intact CHO cells was performed on a Zeiss microscope (model LSM710) using a Plan-Apochromat oil-immersion objective lens (63×, 1.4 NA). Samples were irradiated at 488 nm and a power of 0.37 μW. An area of 134.7 × 134.7 μm2 was captured through a pinhole of 1 Airy unit, and each pixel in the image represented 0.26 μm2 according to the Nyquist theorem. A stack of 30 images was acquired at 5 nm intervals from 495 nm to 640 nm, and the data were processed through custom-written software in Matlab to obtain the emission spectrum corrected for background.

Individual spectra were unmixed by linear regression according to Equation 10 (two colors) or 11 (three colors), in whichkD, kA, and kB, are the scaling factors for the contributions from FlAsH, mCherry, and eGFP, respectively.

$$
Y=k_{D}Em_{D}+k_{A}Em_{A}
$$



$$
Y=k_{B}Em_{B}+k_{D}Em_{D}+k_{A}Em_{A}
$$

The constants EmD and EmA represent the reference spectra for the donor (FlAsH) and acceptor (mCherry), respectively; EmB represents the reference spectrum for eGFP, which was used as a marker for receptor with an intact orthosteric site when co-expressed with a binding-defective mutant.

The unmixed values of k for the donor (kD) and the acceptor (kA) were used to calculate the apparent FRET efficiency (Eapp) according to Equation 12 (Patowary et al., 2013; Raicu, 2007). In the case of kA, the fitted value from Equation 10 or 11 was reduced by 6% to compensate for the direct excitation of mCherry at 498 nm.

$$
E_{app}=\frac{1}{1+\frac{Q_{A}}{Q_{D}}\frac{k_{D}}{k_{A}}\frac{W_{D}}{W_{A}}}
$$

The constants QD and QA represent the quantum yields, which were taken as 0.70 for the donor and 0.22 for the acceptor (Subach et al., 2009); WD and WA are the corresponding spectral integrals, and the ratio of the regions between 495 and 640 (WD/WA) was computed from the reference spectra to be 0.94.

### Kinetically determined mechanistic modeling

Time-dependent binding of an orthosteric ligand (L) to a monomeric receptor (R) was simulated according to Figure 6, in which access to and egress from the orthosteric site is precluded by an allosteric ligand (A). The system is defined by four ordinary differential equations (Equation 13), which were solved numerically to obtain the amount of bound orthosteric ligand at different times (i.e., [RL] + [ARL]). It was assumed that neither ligand is depleted through binding to the receptor, and the free concentrations in Equation 13 were taken as equal to the total concentrations. The simulations were performed in Matlab 2012b, and the integrals were calculated using the ODE23s subroutine.

$$
\frac{d[RL]}{dt}=(k_{+L}[R][L]−k_{−L}[RL])+(k_{−AL}[ARL]−k_{+AL}[RL][A])\frac{d[AR]}{dt}=(k_{+A}[R][A]−k_{−A}[AR])\frac{d[ARL]}{dt}=(k_{+AL}[RL][A])−(k_{−AL}[ARL])\frac{d[R]}{dt}=(k_{−L}[RL]−k_{+L}[R][L])+(k_{−A}[AR]−k_{+A}[R][A])
$$

The rate constants in Equation 13 were computed from the affinity constants according to Equations 14–16, as described previously (Shivnaraine et al., 2012).

$$
K_{L}=\frac{[R][L]}{[RL]}≡\frac{k_{−L}}{k_{+L}}
$$



$$
K_{A}=\frac{[A][R]}{[AR]}≡\frac{k_{-A}}{k_{+A}}
$$



$$
K_{AL}=\frac{[A][RL]}{[ARL]}≡\frac{k_{-AL}}{k_{+AL}}≡\alphaK_{A}
$$

Values of the cooperativity factor α were partitioned between the rate constants for association and dissociation according to Equation 17. The value of j was 2 throughout.

$$
\frac{k_{-AL}}{k_{+AL}}=\alpha\frac{k_{-A}}{k_{+A}}≡\frac{\alpha^{j+1}k_{-A}}{\alpha^{j}k_{+A}}≡\frac{(\frac{1}{\alpha})^{j}k_{-A}}{(\frac{1}{\alpha})^{j+1}k_{+A}}
$$

### Molecular modeling and dynamics

Simulations were performed in the isothermal-isobaric (NPT) ensemble according to the Nosé-Poincaré-Andersen (NPA) equations of motion with a time-step of 2 fs. A cut-off of 10 Å was applied to non-bonding interactions. Equilibration was for 1 ns (300 K, harmonic restraints of 0.5 kcal mol-1 Å-2 applied to non-hydrogen atoms), and production continued for 30 ns (300 K, no restraints). Water molecules were wrapped, bond-lengths to lone-pairs, and hydrogen atoms were constrained. Systems were sampled, atomic coordinates saved, and snapshots taken every 2.5 ps. Images were rendered using either MOE or VMD.

#### Construction of the model for mCh-M2-FCM

Crystal structures of the M2 muscarinic receptor (4MQS, 4MQT) and mCherry (2H5Q) were obtained from the Protein Data Bank. The FlAsH-reactive sequence (FLNCCPGCCMEP) was incorporated into ECL2 of the receptor by homology modeling (Modeller 9.13). While modeling the loop, the rest of the protein was constrained to the crystallographic conformation. FlAsH was built in MOE 2013.08 (Molecular Operating Environment, 2014) and attached to the insertion sequence (CCPGCC) via covalent bonds between the sulfur atoms of the cysteine residues and the arsenic atoms of FlAsH. The length of the sulfur-to-arsenic bonds was set at 2.275 Å. Unresolved regions at the C-terminus of mCherry, the N-terminus of the receptor, and within the intracellular loop of the receptor between transmembrane domains 5 and 6 were modelled as described in Appendix 2

#### Ligand–receptor and ligand–ligand interactions

The structure of the receptor and the structures of orthosteric and allosteric ligands were computed as described in Appendix 2 . NMS or QNB was inserted at the orthosteric site by induced-fit docking using MOE, and the initial placement was guided by alpha spheres within 5 Å of iperoxo in 4MQS. The conformers generated previously for each ligand were docked using the Triangle Matcher placement method and the London dG initial scoring function. A post-placement force-field refinement then was carried out, allowing the receptor and the ligand to move freely within a cut-off distance of 10 Å for receptor-ligand interactions. Final poses were evaluated according to the GBVI/WSA dG scoring function. Structures were verified by superimposition on the 3UON crystal structure of the M2 receptor with QNB at the orthosteric site (Haga et al., 2012) guided by the essential interactions between the ligand and Asp103, Tyr104, Tyr403, Asn404, and Tyr426, as displayed in 4MQS and 3UON, and by comparison with the results of previous modeling studies (Dror et al., 2013).

Strychnine or gallamine was inserted at the allosteric site in the manner described above for ligands at the orthosteric site. The site was defined by those amino acids in proximity with the allosteric ligand LY2119620 in the 4MQT structure. In the top-ranked poses, the cationic ammonium groups of strychnine and gallamine were oriented to interact with Tyr177 and Trp422. The second ammonium group of gallamine lay in the vicinity of Tyr80 and Tyr83, with the third ammonium group extending into solvent. There was no pose in which cationic groups interacted with the EDGE sequence of ECL2, although this interaction appeared during molecular dynamics simulations. The poses of gallamine and strychnine agreed with those obtained in previous simulations (Dror et al., 2013).

The minimized structures of the vacant receptor and the eight complexes resulting from insertion of the four ligands were used as the starting points for molecular dynamics simulations in MOE. All atoms were represented explicitly using the CHARMM27 force field. Ligand-related parameters were checked using the CGenFF program on the CHARMM ParamChem server. Each system was solvated explicitly in a periodic box of TIP3P water molecules (approximately 12,800 molecules), neutralized with sodium chloride, and minimized to an RMS gradient of <1.0 prior to simulation in MOE. The resulting system had approximately 45,800 atoms and a density of 1.009 g/cm3.

For each allosteric–orthosteric pair, the distance between their cationic nitrogen atoms was estimated according to Coulomb’s law. In the case of gallamine, the nitrogen atom closest to that of the orthosteric ligand was selected. The electrostatic potential of an allosteric ligand in the absence and presence of an orthosteric ligand was calculated using the CHARMM27 force field, and the difference was taken as a measure of the energetic cost of repulsion. A degree of electrostatic repulsion was observed with all four ligand-pairs. The effect was observed throughout the simulations, but it diminished over time as the cations compensated by moving apart. In the case of strychnine and QNB, for example, the average difference in electrostatic potential was 0.7 kcal/mol over the first 10 ns of production and 0.06 kcal/mol over a period of 30 ns. Because the average electrostatic potential of the ligands over time does not scale directly with the degree of repulsion, the result of repulsion was tracked in terms of distance.
