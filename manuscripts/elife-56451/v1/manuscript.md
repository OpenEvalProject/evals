# Characterization of the kinetic cycle of an ABC transporter by single-molecule and cryo-EM analyses

## Authors

- Ling Wang<sup>1</sup>
- Zachary Lee Johnson<sup>2</sup>
- Michael R Wasserman<sup>1</sup>
- Jesper Levring<sup>2</sup>
- Jue Chen<sup>2</sup> ([ORCID: 0000-0003-2075-4283](https://orcid.org/0000-0003-2075-4283)) †
- Shixin Liu<sup>1</sup> ([ORCID: 0000-0003-4238-7066](https://orcid.org/0000-0003-4238-7066)) †

### Affiliations

1. Laboratory of Nanoscale Biophysics and Biochemistry, The Rockefeller University New York United States
2. Laboratory of Membrane Biology and Biophysics, The Rockefeller University New York United States
3. Howard Hughes Medical Institute, The Rockefeller University New York United States

† Corresponding author

## Abstract

ATP-binding cassette (ABC) transporters are molecular pumps ubiquitous across all kingdoms of life. While their structures have been widely reported, the kinetics governing their transport cycles remain largely unexplored. Multidrug resistance protein 1 (MRP1) is an ABC exporter that extrudes a variety of chemotherapeutic agents and native substrates. Previously, the structures of MRP1 were determined in an inward-facing (IF) or outward-facing (OF) conformation. Here, we used single-molecule fluorescence spectroscopy to track the conformational changes of bovine MRP1 (bMRP1) in real time. We also determined the structure of bMRP1 under active turnover conditions. Our results show that substrate stimulates ATP hydrolysis by accelerating the IF-to-OF transition. The rate-limiting step of the transport cycle is the dissociation of the nucleotide-binding-domain dimer, while ATP hydrolysis per se does not reset MRP1 to the resting state. The combination of structural and kinetic data illustrates how different conformations of MRP1 are temporally linked and how substrate and ATP alter protein dynamics to achieve active transport.

## Introduction

Multidrug resistance protein 1 (MRP1) is an ATP-binding cassette (ABC) transporter that harnesses the energy of ATP to extrude substrates from the cytosol to the extracellular space (Cole, 2014a). Native substrates of MRP1 include a variety of antioxidants, pro-inflammatory molecules, and hormones (Cole and Deeley, 2006; Deeley and Cole, 2006; Deeley et al., 2006; Leslie et al., 2005). MRP1 also transports a number of chemotherapeutic agents, thereby conferring drug resistance in acute myeloblastic and lymphoblastic leukemia, non-small-cell lung cancer, prostate cancer, breast cancer, and neuroblastoma (Berger et al., 2005; Cole, 2014b; Filipits et al., 2005; Haber et al., 2006; Winter et al., 2013; Zalcberg et al., 2000).

MRP1 is a single polypeptide comprising three transmembrane domains (TMD0, TMD1, and TMD2) and two cytosolic nucleotide-binding domains (NBD1 and NBD2). Structures of bovine MRP1 (bMRP1) have been determined by electron cryo-microscopy (cryo-EM) in three functional states (Johnson and Chen, 2017; Johnson and Chen, 2018): an apo form in the absence of substrate and ATP, a complex with the native substrate leukotriene C4 (LTC4) in the absence of ATP, and a structure of the hydrolysis-deficient E1454Q mutant determined in the presence of both LTC4 and ATP (Figure 1A). These structures, in accord with decades of functional analysis (Cole, 2014a) bring about the following understanding of the transport cycle. In the absence of ATP, MRP1 adopts an inward-facing (IF) conformation, in which the two NBDs are widely separated and the translocation pathway is open to the cytoplasm. Binding of LTC4 at the center of the membrane, between TMD1 and TMD2, brings the two halves of the transporter closer together. Upon binding of ATP, the transporter adopts its fully NBD-closed configuration concurrent with opening of the translocation pathway to the outside. Meanwhile, the LTC4-binding pocket becomes deformed, no longer competent to bind substrate. In this outward-facing (OF) conformation, two ATP molecules are occluded at the NBD dimer interface: one in the catalytically inactive, degenerate site and the other in the active consensus site, poised for hydrolysis (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig1-v1.jpg)

**Figure 1.:** (A) Structures of bMRP1 captured in ligand-free (left), LTC4-bound (middle), and ATP-bound (right) conformations (PDB accession numbers: 5UJ9, 5UJA, and 6BHU). The positions of tag insertions for site-specific labeling are highlighted in green (FRET donor; peptide sequence substituted following NBD1 residue 867) and red (FRET acceptor; peptide sequence inserted at the C-terminus following NBD2 residue 1530). The distances shown correspond to the separations between residues 867 and 1530 rather than the inter-probe distances. TMD0 is shown in red, the lasso motif in purple, TMD1/NBD1 in green, and TMD2/NBD2 in blue. Flexible linkers not observed in the cryo-EM maps are represented by dotted lines. (B) ATPase activity of unmodified wild-type (WT), FRET-labeled WT, and E1454Q mutant bMRP1, either without or with LTC4 (10 µM). Data are represented as mean ±95% confidence intervals (from 3 to 6 independent measurements) and fitted to Michaelis-Menten equations. (C) Catalytic constants for ATP turnover by unmodified WT, FRET-labeled WT, and E1454Q bMRP1 in the absence and presence of 10 µM LTC4. Data are represented as mean ± SEM. Comparisons were made by one-way ANOVA (****p<0.0001; ns, not significant). The residual ATP turnover seen in the E1454Q sample did not respond to LTC4 stimulation, and was thus most likely due to spontaneous ATP hydrolysis independent of MRP1 activity.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Schematic of the surface immobilization and single-molecule imaging strategy. Labeled bMRP1 molecules were immobilized on a glass surface and imaged at room temperature with total-internal-reflection fluorescence microscopy. (B) SDS-PAGE gel showing fluorescent labeling of bMRP1 with Sfp/AcpS synthases and dye-CoA conjugates. Modified WT stands for MRP1 with inserted peptide sequences for site-specific labeling. (C) Size-exclusion chromatography for generating dual-labeled bMRP1. The AcpS synthase and excess free LD655 dye were removed by gel filtration (top), followed by the removal of Sfp synthase and excess free Cy3 dye (middle). The bottom graph depicts the final dual-labeled sample used in single-molecule experiments.

While a wealth of structural characterizations of ABC transporters provide atomistic details of these proteins in specific conformations (Oldham et al., 2008; Srikant and Gaudet, 2019), they do not inform us of how these structural snapshots are temporally linked. On the other hand, single-molecule techniques are well suited for tracking dynamic processes and have been applied to study a number of membrane proteins (Akyuz et al., 2013; Dyla et al., 2017; Goudsmits et al., 2017; Husada et al., 2018; Wang et al., 2016; Zhao et al., 2010). In this study, we took a combined single-molecule and structural approach to investigate the kinetic mechanism that governs the transport cycle of MRP1. Based on prior structural information, we designed single-molecule fluorescence resonance energy transfer (smFRET) experiments to track the conformational changes of bMRP1 in real time. Guided by the smFRET results, we then used cryo-EM to capture the most abundant structural configuration of wild-type (WT) MRP1 during active turnover. The synergy between the smFRET and cryo-EM studies has enabled us to determine the rate-limiting mechanism of MRP1 and how substrate and ATP modulate the kinetics of this important drug transporter.

## Results

### smFRET design

Cryo-EM structures indicate that in the MRP1 transport cycle the two NBDs undergo large motions of association and dissociation (Figure 1A). To monitor the conformational dynamics of bMRP1 at the single-molecule level, we introduced two fluorophore labeling sites at the distal ends of NBD1 and NBD2. A 12-residue S6 peptide replaced residues 868–879, and a 12-residue A1 peptide was added to the C-terminus following residue V1530. Cy3 (donor) and LD655 (acceptor) fluorophores were orthogonally conjugated to bMRP1 using Sfp and AcpS synthases, respectively (Figure 1—figure supplement 1). In addition, a His10-tag was added at the N-terminus of TMD0 for surface immobilization. In solution, the fluorescently labeled bMRP1 hydrolyzed ATP at rates virtually identical to those of the unmodified WT protein (Figure 1B and C), indicating that insertion of the peptide tags and incorporation of the fluorophores did not alter the kinetics of bMRP1.

### Conformational distributions of MRP1

Using total-internal-reflection fluorescence (TIRF) microscopy, we measured the steady-state distribution of FRET efficiency (E) for WT bMRP1 under five different conditions (Figure 2A). In the absence of ATP and substrate (apo), the FRET histogram showed a broad distribution of E values spanning from 0.2 to 0.9. Saturating concentrations of LTC4 (10 µM) or ATP (5 mM) shifted the FRET distribution towards higher E values. When both LTC4 and ATP were present, a predominant high FRET peak emerged. Addition of ATP and LTC4 together with orthovanadate (Vi), a hydrolysis transition-state analogue, further promoted the high FRET state (Figure 2A). We then used the same labeling strategy to attach the FRET dye pair to the catalytically inactive E1454Q mutant bMRP1. The FRET distribution for the E1454Q mutant in the presence of ATP and LTC4 was also dominated by a high FRET state (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig2-v1.jpg)

**Figure 2.:** (A) Contour plots (top) and histograms (bottom) of FRET distributions obtained with WT bMRP1 in the following conditions (from left to right): apo, + LTC4 (10 µM), + ATP (5 mM), + ATP/LTC4 (5 mM/10 µM), + Vi/ATP/LTC4 (1 mM/5 mM/10 µM). Shown in the right column are data for the E1454Q mutant in the presence of ATP/LTC4 (5 mM/10 µM). The time-dependent changes in the contour plots were due to fluorophore photobleaching, which depopulated FRET-active molecules over time. Time points after photobleaching were excluded from subsequent analysis. The histograms represent the cumulative FRET distributions over the entire 1.25 s time window. Overlaid on the histograms are fitted distributions by the five-state model with mean FRET values of 0.92 (magenta, OF), 0.80 (yellow, IF1), 0.63 (green, IF2), 0.42 (blue, IF3), and 0.23 (orange, IF4). n denotes the number of molecules analyzed. (B) Relative occupancy of the IF1 state in the presence of increasing concentrations of LTC4. Data are fitted to a dose-response function with the Hill equation, yielding an EC50 of 0.32 ± 0.17 µM. (C) Relative occupancy of the OF state in the presence of increasing concentrations of ATP. Data are fitted to a dose-response function with the Hill equation, yielding an EC50 of 0.05 ± 0.02 mM. Data are represented as mean ± SEM.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Evidence lower bound determined by ebFRET, which was used to determine the number of non-zero FRET states and provide initial estimates of model parameters. (B–F) Models with two (B), three (C), four (D), five (E), and six (F) non-zero FRET states were implemented in SPARTAN using the initial parameters generated by ebFRET. FRET trajectories were then idealized through segmental k-means optimization of each model. The raw FRET histogram (gray, from WT MRP1 with 5 mM ATP and 10 µM LTC4) is overlaid with histograms of the assigned states (shown in colors). (G) Example single-molecule trajectories fitted by four non-zero FRET states (magenta line) versus five non-zero FRET states (orange line). The four-state model fails to recognize obvious FRET transitions.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** (A) FRET contour plots (top) and histograms (bottom) obtained at varying concentrations of LTC4. n denotes the number of molecules analyzed for each condition. (B) FRET contour plots and histograms obtained at varying concentrations of ATP. (C) Relative occupancies of states other than IF1 at different LTC4 concentrations. IF1 occupancy is shown in Figure 2B. (D) Relative occupancies of all IF states at different ATP concentrations. OF occupancy is shown in Figure 2C. Data are represented as mean ± SEM.

To quantitatively characterize the FRET distributions, we applied the empirical Bayesian method implemented in ebFRET (van de Meent et al., 2014) and identified a common set of five FRET states, with mean E values of 0.23, 0.42, 0.63, 0.80, and 0.92. We then used a hidden Markov modeling (HMM) algorithm (Qin, 2004) to idealize the smFRET time trajectories to these discrete states. The FRET distributions obtained under all above experimental conditions can be described as combinations of the five states (Figure 2A, lower panel). A four-state model is insufficient to describe transitions observed in the FRET trajectories (Figure 2—figure supplement 1). Increasing the number of states to six only resulted in an additional unpopulated state, indicative of overfitting (Figure 2—figure supplement 1).

Next we sought to correlate these five FRET states with existing structural information. To identify the LTC4-bound conformation, we collected smFRET data with a series of LTC4 concentrations and analyzed the FRET distributions using the five-state model (Figure 2—figure supplement 2A). The occupancy of the E = 0.80 state increased monotonically as the LTC4 concentration was raised, whereas those of the other states did not (Figure 2B and Figure 2—figure supplement 2C), consistent with the peak position of 0.8 from the overall FRET distribution collected at saturating LTC4 (Figure 2A). The half-maximal effective concentration (EC50) of LTC4 for the E = 0.80 state occupancy is 0.32 ± 0.17 µM, in agreement with the LTC4 concentration required for half-maximal stimulation of ATP hydrolysis measured in a bulk ATPase assay (0.35 ± 0.09 µM) (Johnson and Chen, 2017). Therefore we rationalized that the E = 0.80 state (termed IF1) corresponds to the inward-facing cryo-EM structure determined in the presence of saturating LTC4 (Figure 1A, middle).

The highest FRET state (E = 0.92) indicates a conformation in which the NBDs are in closer proximity than that of the LTC4-bound structure. Its occupancy increased as a function of ATP concentration, but those of the lower FRET states did not (Figure 2C, Figure 2—figure supplement 2B and D), consistent with visual inspection of the overall FRET distribution (Figure 2A). Moreover, the E1454Q mutant predominately occupied the E = 0.92 state at saturating concentrations of ATP and LTC4 (Figure 2A), similar to the condition under which the cryo-EM structure of the outward-facing conformation was determined (Johnson and Chen, 2018). These observations support a direct correspondence between the E = 0.92 state and the OF conformation.

The three lowest FRET states (i.e., E = 0.63, 0.42, and 0.23) indicate conformations in which the NBDs are further separated than in the LTC4-bound structure, and thus are presumably ligand-free and inward-facing (termed IF2, IF3, and IF4, respectively). The presence of multiple apo states underscores the conformational flexibility of MRP1 in the absence of ligand, a well-documented characteristic of many ABC transporters (Husada et al., 2018; Timachi et al., 2017; Ward et al., 2007; Ward et al., 2013). In the cryo-EM structure of apo bMRP1, the local resolution of the NBDs was poorer compared to other regions, suggesting that the NBDs are relatively mobile (Johnson and Chen, 2017).

From the idealized smFRET trajectories we extracted the lifetimes of each state and transition frequencies between each pair of states. In the absence of ATP, the vast majority of transitions occurred among the four IF states (IF1, IF2, IF3, and IF4) (Figure 3A, Figure 3—figure supplements 1 and 2). The lifetime of each IF state was on average around 1 s (Figure 3B). Addition of LTC4 increased the lifetime of IF1 by about 30%, lending further support to its assignment as the substrate-bound state, whereas ATP did not produce statistically significant changes in the lifetime of any IF state (Figure 3B).

![Figure 3.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig3-v1.jpg)

**Figure 3.:** (A) Representative single-molecule donor (green) and acceptor (red) fluorescence trajectories, and the corresponding FRET trajectories (blue) obtained at a frame rate of 25 ms. Idealized FRET states are overlaid in orange lines. Arrows indicate fluorophore photobleaching events, after which the data were excluded from further analysis. The following conditions were analyzed: apo, + LTC4 (10 µM), + ATP (5 mM), and + ATP/LTC4 (5 mM/10 µM). (B) Average lifetimes of each IF state under different conditions. Data are represented as mean ± SEM.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Idealized FRET states are overlaid in orange.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Dashed lines represent the mean values for the five discrete FRET states.

### Determinants of IF-to-OF transitions

Estimation of the lifetime of the OF state was not possible at a temporal resolution of 25 ms. At this time resolution and corresponding laser power, molecules often remained in the OF state in the presence of ATP until fluorophore photobleaching occurred (Figure 3—figure supplement 1). In order to capture the complete duration of the OF state, we lowered the time resolution to 300 ms and decreased the laser power. Under these imaging conditions, the average lifetime of the fluorophores was approximately 100 s. This allowed us to observe multiple cycles of IF-OF interconversions, albeit with the drawback of missing some fast transitions.

To better understand the mechanism of IF-to-OF transitions, we performed real-time perturbation experiments, in which ATP was delivered into the sample chamber containing apo MRP1. Upon examining individual smFRET trajectories, we observed two distinct populations of MRP1: one population showed clear transitions from the IF to the OF state after ATP injection and then cycled between IF and OF states (Figure 4A), while the other population only transitioned among different IF states and never reached the OF state during the observation period (Figure 4—figure supplement 1A). Molecules in the latter group were presumed to be biochemically inactive, as ATP hydrolysis only occurs in the NBD-dimerized OF conformation. Prior to ATP injection, both groups of molecules were predominantly in the IF conformations but exhibited distinct FRET distributions (Figure 4—figure supplement 1B). Addition of ATP substantially increased the occupancy of the OF state within the active group (Figure 4B and Figure 4—figure supplement 1B), whereas the FRET distribution of the inactive group did not change upon ATP injection (Figure 4—figure supplement 1B). These inactive molecules must also exist in the steady-state experiments described in Figure 2. However, due to the short observation window with a 25 ms frame rate it was not possible to identify these molecules.

![Figure 4.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig4-v1.jpg)

**Figure 4.:** (A) Representative smFRET trajectories of active molecules from the perturbation experiments obtained at a frame rate of 300 ms. A limiting (10 µM) or saturating (5 mM) concentration of ATP with or without LTC4 (10 µM) was injected into the imaging chamber at 10 s (dashed lines). The wait time until the onset of the first OF state (twait) and the lifetime of the subsequent OF states (tOF) and IF states (tIF) are shaded in orange, dark gray, and light gray, respectively. (B) Contour plots of smFRET trajectories for active molecules under each perturbation condition. n denotes the number of active molecules analyzed. (C) Average twait for different perturbation conditions. (D) Average tIF for different perturbation conditions. The values have been corrected for the photobleaching rate. Data are represented as mean ± SEM.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Representative fluorescence and FRET trajectories of the inactive molecules. These molecules transitioned among distinct IF states but never visited the OF state before photobleaching. (B) Occupancy of each FRET state before and after the injection of 5 mM ATP for the inactive (left) and active (right) population. Data are represented as mean ± SEM.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Contour plots (top) and corresponding transition density plots (bottom) of smFRET trajectories aligned at the appearance of the first OF state from the perturbation experiments in which 10 µM ATP, 10 µM ATP + 10 µM LTC4, 5 mM ATP, or 5 mM ATP + 10 µM LTC4 (from left to right) was injected into the imaging chamber during data acquisition. (B) Additional representative smFRET trajectories for the perturbation experiments. Dashed lines indicate the time of injection. The wait time until the onset of the first OF state (twait) and the lifetimes of the subsequent OF states (tOF) and IF states (tIF) are shaded in orange, dark gray and light gray, respectively.

Using the trajectories of active molecules only, we measured the wait time (twait) from the point of ATP injection to the onset of the first OF state (Figure 4A). This duration is a compound function of several events including ATP binding and NBD dimerization. Increasing the ATP concentration from 10 µM to 5 mM shortened twait by approximately twofold (Figure 4C), consistent with the understanding that ATP binding promotes NBD dimerization. The presence of LTC4 reduced twait at both limiting and saturating ATP concentrations (Figure 4C), indicating that substrate accelerates the transition from the IF to OF state. Moreover, we found that the vast majority of transitions into the OF state originated from IF1 or IF2 (Figure 4—figure supplement 2A), suggesting that the substrate-bound configuration IF1 is not an obligatory intermediate en route to the OF state.

After the active MRP1 molecules made the first IF-to-OF transition, they continued to cycle between IF and OF states (Figure 4A and Figure 4—figure supplement 2B). Given that the 300 ms time resolution obscured a fraction of fast transitions among different IF states, we used the composite time that molecules spent in the IF states before converting into the OF state (tIF; Figure 4A) to describe the kinetics of IF-to-OF transitions. As expected from the notion that ATP drives the IF-to-OF isomerization, increasing the ATP concentration shortened tIF (Figure 4D). LTC4 further reduced the average tIF by approximately threefold (Figure 4D).

### Determinants of OF-to-IF transitions

To investigate how the reverse transition (i.e., from the OF to IF state) is influenced by ATP and LTC4, we measured the lifetime of OF states (tOF; Figure 4A). In control experiments where the molecules were incubated with buffer or LTC4 alone in the absence of ATP, spontaneous transitions into the OF state were occasionally observed (Figure 5A), but the resultant OF states on average only lasted a few seconds (Figure 5B and Figure 5—figure supplement 1). In comparison, the average OF lifetime measured in the presence of saturating ATP was longer than 20 s (Figure 5B and Figure 5—figure supplement 1), indicating that ATP stabilizes the OF conformation.

![Figure 5.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig5-v1.jpg)

**Figure 5.:** (A) Example smFRET trajectories for apo and LTC4-only conditions showing spontaneous transitions into the OF state independent of ATP. (B) Average lifetime of the OF states under different conditions. The values have been corrected for the photobleaching rate. Data are represented as mean ± SEM.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The corresponding time constants (τOF) are reported.

LTC4 had only a minor effect on the kinetics of OF-to-IF transitions (Figure 5B and Table 1), consistent with the structural observation that LTC4 is readily released in the ATP-bound OF conformation prior to ATP hydrolysis (Johnson and Chen, 2018), hence not affecting the subsequent isomerization back to the IF state.

**Table 1.**
 Kinetics of the transitions between IF and OF conformations


<table>
  <thead>
    <tr>
      <th>Condition</th>
      <th>tIF (s)</th>
      <th>tOF (s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>WT, 5 mM ATP</td>
      <td>16.1 ± 2.2</td>
      <td>28.8 ± 4.8</td>
    </tr>
    <tr>
      <td>WT, 5 mM ATP + 10 µM LTC4</td>
      <td>4.7 ± 0.8</td>
      <td>30.8 ± 5.2</td>
    </tr>
    <tr>
      <td>E1454Q, 5 mM ATP + 10 µM LTC4</td>
      <td>7.7 ± 1.5</td>
      <td>31.7 ± 5.5</td>
    </tr>
  </tbody>
</table>

_Shown are the average lifetimes (mean ± SEM) of the composite IF state and the OF state for WT and E1454Q MRP1 with indicated ATP and substrate concentrations. The effect of dye photobleaching on the apparent IF/OF lifetime has been corrected for._

When saturating concentrations of ATP and LTC4 were present, the transition from the OF to the IF conformation was much slower than the IF-to-OF transition (tOF vs. tIF, Table 1), also evident from the single-molecule trajectories (Figure 4A and Figure 4—figure supplement 2B). Therefore, it is likely that under physiological conditions where ATP is saturating, MRP1 spends the majority of its time in the OF conformation. The total cycle time measured from the single-molecule data (tOF + tIF, Table 1) is 4–6 times longer than that deduced from the bulk ATPase assay (Figure 1C). A number of factors could contribute to this difference. The temperature differed between the two assays (23°C for smFRET vs. 30°C for bulk assay). It is also possible that surface immobilization of MRP1 may affect its activity. Finally, some fast transitions between IF and OF states may escape detection at the 300 ms time resolution of smFRET measurements.

### Cryo-EM structure of MRP1 under active turnover conditions

Next we pursued cryo-EM studies to further discern the rate-limiting step in the MRP1 transport cycle. Based on the smFRET data (Figures 2A and 4A), we anticipated that most particles would adopt an OF conformation in the presence of saturating LTC4 and ATP. Further, if ATP hydrolysis were rate limiting, the predominant species would be the pre-hydrolysis state with ATP molecules bound at both ATPase sites. Otherwise, we would expect to observe a dominant structure in which ATP in the catalytically competent, consensus site has already been hydrolyzed.

To prepare the sample for cryo-EM, WT bMRP1 (30 µM) was incubated with 80 µM LTC4 and 10 mM ATP-Mg2+ on ice for 10 min before plunge freezing in liquid ethane. If the sample had been prepared at room temperature, approximately 3 mM ATP would have been hydrolyzed during this incubation (Figure 1C). On ice, we expect a slower turnover rate and thus even less depletion of ATP. This approximates an ‘active turnover’ condition where ATP hydrolysis has reached steady state.

We first used all 1,143,729 particles from the cryo-EM dataset to calculate a 3.4 Å reconstruction that represents the dominant structure under the active turnover condition (Figure 6—figure supplement 1 and Table 2). Consistent with the single-molecule data, the resulting map shows an NBD-dimerized conformation, with an ATP molecule in the degenerate site and an ADP molecule in the consensus site (Figure 6—figure supplement 2A and B). To improve the resolution of the structure, we also carried out 3D classification and obtained a higher quality map at 3.2 Å from a subset of the particles (Figure 6—figure supplements 1 and 2), which unambiguously shows an ADP molecule at the consensus site (Figure 6). This structure strongly suggests that ATP hydrolysis is a fast step in the transport cycle, whereas dissociation of the NBD dimer constitutes a kinetic bottleneck, thereby limiting the rate of the overall cycle.

![Figure 6.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig6-v1.jpg)

**Figure 6.:** (A) The structure of WT bMRP1 in the presence of saturating ATP and LTC4 shown in blue, overlaid with the structure of the non-hydrolyzing bMRP1-E1454Q mutant in the presence of saturating ATP and LTC4 (PDB 6BHU) shown in salmon. The structures are shown in cartoon representation viewed from within the plane of the membrane with ATP/ADP shown as sticks and Mg2+ shown as spheres. (B) The same structural overlay as in (A), rotated 90° to view the NBD dimer from the cytoplasmic side. (C) Cryo-EM density for the degenerate ATPase site (left) and the ATP-Mg2+ from the degenerate site alone (right, rotated 90°). NBD1 is shown in green, NBD2 in blue, ATP as yellow sticks colored by heteroatom, and Mg2+ as a magenta sphere. (D) Cryo-EM density for the consensus ATPase site (left) and the ADP-Mg2+ from the consensus site alone (right, rotated 90°). In the left panel, the position of the missing γ-phosphate is demarcated with a gray dotted oval. The color code is the same as in (C).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** The number of particles used in each step is indicated next to the arrow associated with that step. After initial classification and refinement in RELION, two separate routes were taken to generate each of the final maps. To generate the 3.2 Å map from a subset of particles, the data were further processed in RELION. To generate the 3.4 Å map from all particles, the data were refined using Frealign.

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (A) Cryo-EM density in the degenerate ATPase site from the Frealign map using all particles, displayed in the same way as Figure 5C. (B) Cryo-EM density in the consensus ATPase site from the Frealign map using all particles, displayed in the same way as Figure 5D. (C) Cryo-EM density for the transmembrane helices from the RELION map using a subset of the particles. (D) Fourier shell correlation (FSC) curve for the two half maps used in the final reconstruction of the RELION map using a subset of the particles. (E) Local resolution of the RELION map using a subset of the particles. Local resolution was estimated using cryoSPARC.

**Table 2.**
 Summary of EM data and structure refinement statistics


<table>
  <thead>
    <tr>
      <th colspan="3">Data collection</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">Microscope</td>
      <td>Titan krios (FEI)</td>
    </tr>
    <tr>
      <td colspan="2">Voltage (kV)</td>
      <td>300</td>
    </tr>
    <tr>
      <td colspan="2">Detector</td>
      <td>K2 Summit (Gatan)</td>
    </tr>
    <tr>
      <td colspan="2">Pixel size (Å)</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td colspan="2">Defocus range (μm)</td>
      <td>0.7 to 2.4</td>
    </tr>
    <tr>
      <td colspan="2">Movies</td>
      <td>3604</td>
    </tr>
    <tr>
      <td colspan="2">Frames/movie</td>
      <td>50</td>
    </tr>
    <tr>
      <td colspan="2">Dose rate (electrons/pixel/s)</td>
      <td>8.0</td>
    </tr>
    <tr>
      <td colspan="2">Total dose (electrons/Å2)</td>
      <td>75</td>
    </tr>
    <tr>
      <td colspan="2">Number of particles</td>
      <td>1,143,729</td>
    </tr>
    <tr>
      <td colspan="3">Model composition</td>
    </tr>
    <tr>
      <td colspan="2">Non-hydrogen atoms</td>
      <td>9684</td>
    </tr>
    <tr>
      <td colspan="2">Protein residues</td>
      <td>1210</td>
    </tr>
    <tr>
      <td colspan="2">Lipids/Detergents/Ligands</td>
      <td>3 CHS/1 ATP/1 ADP/2 Mg2+</td>
    </tr>
    <tr>
      <td colspan="3">Refinement</td>
    </tr>
    <tr>
      <td colspan="2">Resolution (Å)</td>
      <td>3.23</td>
    </tr>
    <tr>
      <td colspan="2">Rwork</td>
      <td>0.265</td>
    </tr>
    <tr>
      <td colspan="2">Rfree</td>
      <td>0.276</td>
    </tr>
    <tr>
      <td colspan="2">RMS deviations</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Bond lengths (Å)</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td colspan="2">Bond angles (°)</td>
      <td>1.297</td>
    </tr>
    <tr>
      <td colspan="2">Validation</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Molprobity score</td>
      <td>1.11</td>
    </tr>
    <tr>
      <td colspan="2">Clashscore, all atoms</td>
      <td>1.07</td>
    </tr>
    <tr>
      <td colspan="2">Favored rotamers (%)</td>
      <td>97.7</td>
    </tr>
    <tr>
      <td colspan="2">Ramachandran plot (%)</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Favored</td>
      <td>95.7</td>
    </tr>
    <tr>
      <td colspan="2">Allowed</td>
      <td>4.3</td>
    </tr>
    <tr>
      <td colspan="2">Outliers</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>

Other than ADP occupying the consensus site in place of ATP, the overall structure of this post-hydrolysis conformation is essentially identical to that of the pre-hydrolytic structure solved with the hydrolysis-deficient E1454Q mutant (Johnson and Chen, 2018; Figure 6A and B). In both structures, the intracellular gate is closed and the substrate-binding site is pulled apart such that LTC4 is no longer bound. Thus, for MRP1, ATP hydrolysis per se and the subsequent release of inorganic phosphate (Pi) do not induce conformational rearrangements.

## Discussion

Previously, using cryo-EM and mutagenesis, we captured three snapshots of MRP1, demonstrating the conformational changes induced by LTC4 and ATP (Johnson and Chen, 2017; Johnson and Chen, 2018). Guided by these structures, here we employed single-molecule fluorescence spectroscopy to characterize the dynamics of MRP1 to understand the connectivity of these conformations. The kinetic results from these single-molecule experiments prompted us to solve the dominant MRP1 structure under active turnover conditions, which revealed the rate-limiting mechanism of the MRP1 transport cycle. Such a synergistic approach enabled us to obtain new insights into the kinetic cycle of MRP1, depicted in Figure 7.

![Figure 7.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig7-v1.jpg)

**Figure 7.:** MRP1 is intrinsically dynamic, transitioning between multiple IF conformations both in the absence and presence of ATP. Under physiological conditions, ATP rapidly binds to the IF state, promoting NBD dimerization and formation of the OF state. LTC4 accelerates the IF-to-OF transition (k1) but not the other transitions, yielding a faster overall ATPase turnover rate. The reverse isomerization (k-1) resulting from ATP dissociation occurs at a much slower rate than the forward reaction. ATP hydrolysis in the consensus site (k2) is fast and results in an asymmetric post-hydrolytic OF state with ATP in the degenerate site and ADP in the consensus site. This represents the predominant conformation determined by cryo-EM under active turnover conditions. The entire transport cycle is limited by the rate of dissociation of the NBD dimer (k3) after ATP hydrolysis.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/56451/elife-56451-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) FRET contour plot for the perturbation experiment in which 5 mM ATP and 10 µM LTC4 were delivered to bMRP1-E1454Q at 10 s. (B) Representative smFRET trajectories for the above experiment. (C) Histogram of the OF state lifetimes extracted from the above experiment and its fit to a single-exponential decay function (blue line).

By monitoring the separation of the two NBDs, we showed that MRP1 is intrinsically dynamic: in the absence of any ligand, MRP1 transitions among multiple IF conformations. It also spontaneously accesses the OF conformation, albeit with lower frequency and shorter lifetime in the absence of nucleotides. Similarly, a recent smFRET study showed that the E. coli peptide transporter McjD also samples an NBD-dimerized state without nucleotides (Husada et al., 2018). Whether all of these ground-state conformations are functionally important requires further investigation.

When ATP is present, as in physiological conditions, the MRP1 transport cycle is a nonequilibrium process coupled to ATP hydrolysis. ATP binding accelerates the IF-to-OF transition (k1) and slows down the reverse OF-to-IF transition (k-1) by stabilizing the OF conformation. Substrate, such as LTC4, stimulates the ATPase activity through acceleration of the IF-to-OF transition (k1), but not ATP hydrolysis (k2) or the subsequent OF-to-IF transition (k3). In this model, the same high FRET value (E = 0.92) is produced by two distinct NBD-dimerized states: the pre-hydrolytic state in which two ATP molecules are bound and an asymmetric post-hydrolytic state bound with one ATP and one ADP. Still, the lifetime distributions of the E = 0.92 state can be fit with single-exponential decay functions (Figure 5—figure supplement 1), indicating a single slow step governing the OF lifetime. This is probably because ATP hydrolysis (k2) is a fast step followed by a comparatively slow NBD dissociation step (k3). The cryo-EM data further support that at physiological ATP concentrations (1–10 mM), the rate-limiting step is the dissociation of the NBD dimer subsequent to ATP hydrolysis (Figure 7). Recent studies of P-glycoprotein (Bársony et al., 2016), TmrAB (Hofmann et al., 2019), and TM287/288 (Hutter et al., 2019) also indicated that in their respective transport cycles, the OF-to-IF transition is rate limiting.

The cryo-EM structure of MRP1 shows that the ATP hydrolysis step per se does not induce any conformational change (Figure 6). One might then ask, what is the role of ATP hydrolysis in the transport cycle? Thermodynamically, the energy provided by ATP hydrolysis is necessary for uphill substrate translocation. Without energy dissipation, the system can only reach equilibrium, in which the substrate concentration is equal on both sides of the membrane. Kinetically, ATP hydrolysis provides directionality to the transport cycle: because k2 is much greater than the reverse isomerization rate k-1, estimated from the E1454Q cycling traces (Figure 7—figure supplement 1), the majority of molecules proceed to ATP hydrolysis upon NBD dimerization, followed by isomerization back to the IF conformation with a rate of k3. Although the E1454Q mutant is catalytically deficient, it displayed transitions between IF and OF conformations with kinetics similar to the WT transporter (Table 1). This apparent paradox can be explained by our kinetic model (Figure 7): WT MRP1 predominantly takes the irreversible, hydrolysis-driven route (k1 → k2 → k3), while the E1454Q mutant takes the reversible pathway (k1 ↔ k-1) that does not involve hydrolysis. The relative IF/OF occupancy is similar between WT and E1454Q MRP1 because k-1 and k3 share similar values, even though the E1454Q mutant cannot power uphill substrate transport.

When correlating smFRET and cryo-EM data, one must keep in mind that each technique has its own limitations and is carried out under very different experimental conditions. For example, multiple apo states were detected by smFRET but our previous cryo-EM study revealed only one ligand-free structure (Johnson and Chen, 2017). This discrepancy suggests that smFRET could be more sensitive in detecting sparsely populated species than cryo-EM. Furthermore, the FRET experiments were carried out at 23°C, whereas the cryo-EM structure was determined at cryogenic temperature. We do not fully understand how the conformational distribution of molecules on the EM grids might change upon rapid freezing. However, it seems possible that the occupancy of the lowest energy state may become more dominant as a result of a smaller kBT in the Boltzmann distribution.

The kinetics of another ABC protein, the cystic fibrosis transmembrane conductance regulator (CFTR), have been well characterized through functional studies (Csanády et al., 2019). CFTR is closely related to MRP1 as both belong to the ABCC subfamily of ABC transporters. However, it functions as an ion channel instead of an active transporter and is thus considered to be a ‘broken’ ABC transporter. The gating cycle of CFTR is generally similar to the transport cycle of MRP1: ATP binding stabilizes an NBD-dimerized conformation in which the pore is open to allow ion conduction, and ATP hydrolysis is followed by NBD separation and channel closure. However, the kinetic properties of CFTR, characterized through single-channel recordings, are markedly different from those of MRP1. In the CFTR gating cycle, the rate-limiting step is the formation of the NBD-dimerized conformation (equivalent to k1 in Figure 7), and ATP hydrolysis occurs much slower than NBD dissociation (Csanády et al., 2010; Vergani et al., 2003). Do these differences reflect the general distinction between an active transporter and a passive channel? The answer awaits detailed kinetic characterization of other ABC transporters.

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
      <td>Antibody</td>
      <td>Biotinylated 6x-His Tag monoclonal antibody</td>
      <td>Invitrogen</td>
      <td>Cat# MA1-21315-BTIN</td>
      <td>Molar ratio of 2:1 (antibody:bMRP1)</td>
    </tr>
    <tr>
      <td>Cell line</td>
      <td>Sf9</td>
      <td>ATCC</td>
      <td>CRL-1711</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line</td>
      <td>HEK293S GnTI-</td>
      <td>ATCC</td>
      <td>CRL-3022</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>bovine MRP1 in pUC57 vector</td>
      <td>Bio Basic</td>
      <td></td>
      <td>Codon-optimized</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>bovine MRP1 in a modified pEG BacMam vector</td>
      <td>Johnson and Chen, 2017</td>
      <td></td>
      <td>Suitable for expression in mammalian cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>bovine MRP1 with S6/A1 peptides for site-specific labeling</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>bovine MRP1 E1454Q with S6/A1 peptides for site-specific labeling</td>
      <td>This paper</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Sfp pet29b C-terminal His Tag</td>
      <td>(Worthington and Burkart, 2006)</td>
      <td>Addgene Plasmid# 75015</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET15b-ACPs (from S. pneumoniae)</td>
      <td>Gift from Michael Johnson</td>
      <td>Addgene Plasmid# 63687</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cy3 maleimide mono-reactive dye</td>
      <td>GE Healthcare</td>
      <td>Cat# PA23031</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>LD655 maleimide mono-reactive dye</td>
      <td>Lumidyne Technologies</td>
      <td>Cat# LD655-MAL</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Trolox</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 238813</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>4-Nitrobenzyl alcohol (NBA)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# N12821</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Cyclooctatetraene (COT)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 138924</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>3,4-Dihydroxybenzoic acid (PCA)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# 37580</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Digitonin</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# D141</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Protocatechuate 3,4-Dioxygenase (PCD)</td>
      <td>Sigma-Aldrich</td>
      <td>Cat# P8279</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Leukotriene C4</td>
      <td>Cayman Chemical</td>
      <td>Cat# 20210</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>NHS-activated Sepharose 4 Fast Flow resin</td>
      <td>GE Healthcare</td>
      <td>Cat# 17-0430-01</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Superose 6, 10/300 GL</td>
      <td>GE Healthcare</td>
      <td>Cat# 17-5172-01</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SPARTAN</td>
      <td>(Juette et al., 2016)</td>
      <td>https://www.scottcblanchardlab.com/software</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ebFRET</td>
      <td>(van de Meent et al., 2014)</td>
      <td>http://ebfret.github.io</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MATLAB</td>
      <td>MathWorks</td>
      <td>https://www.mathworks.com/products/matlab.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Origin</td>
      <td>OriginLab</td>
      <td>https://www.originlab.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad</td>
      <td>https://www.graphpad.com/scientific-software/prism/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION 1.4</td>
      <td>(Scheres, 2012)</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/relion</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Frealign</td>
      <td>(Grigorieff, 2016)</td>
      <td>https://grigoriefflab.janelia.org/frealign</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>(Emsley and Cowtan, 2004)</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PHENIX</td>
      <td>(Adams et al., 2010)</td>
      <td>https://www.phenix-online.org</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>REFMAC</td>
      <td>(Brown et al., 2015)</td>
      <td>https://www.ccp4.ac.uk/html/refmac5.html</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MolProbity</td>
      <td>(Chen et al., 2010)</td>
      <td>https://molprobity.biochem.duke.edu</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Chimera</td>
      <td>(Pettersen et al., 2004)</td>
      <td>https://www.cgl.ucsf.edu/chimera</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMOL</td>
      <td>PyMOL</td>
      <td>https://www.pymol.org</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cryoSPARC</td>
      <td>(Punjani et al., 2017)</td>
      <td>https://cryosparc.com</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>R1.2/1.3 400 mesh Au holey carbon grids</td>
      <td>Quantifoil</td>
      <td>Cat# 1210627</td>
      <td>1 µg/mL</td>
    </tr>
  </tbody>
</table>

### Cell culture

Sf9 cells were cultured in sf-900 II SFM medium (GIBCO) supplemented with 5% FBS at 27°C. HEK293S GnTI- suspension cells were cultured in Freestyle 293 medium (GIBCO) supplemented with 2% FBS at 37°C with 8% CO2 and 80% humidity.

### Protein expression, purification, and site-specific labeling

All bMRP1 constructs were expressed and purified as described previously (Johnson and Chen, 2017). Briefly, baculovirus with each bMRP1 construct was generated and used to infect HEK293S GntI- suspension cells. All constructs contained a C-terminal PreScission-Protease-cleavable GFP tag. Cell pellets were solubilized by adding 2% lauryl maltose neopentyl glycol (LMNG) supplemented with 0.2% cholesteryl hemisuccinate (CHS). After removal of the insoluble fraction by centrifugation, supernatants were batch bound to GFP-nanobody-conjugated Sepharose 4 Fast Flow resin (GE Healthcare). The resin was then packed into a column, washed with buffer containing 0.06% digitonin, and protein was eluted by digestion with PreScission Protease. After elution, protein was concentrated and applied to a Superose 6 10/300 GL column (GE Healthcare) equilibrated in 0.06% digitonin, 150 mM KCl, 50 mM Tris-HCl pH 8.0, 2 mM MgCl2, and 2 mM DTT. Peak fractions were pooled and concentrated, and either used immediately to prepare cryo-EM samples or flash-frozen in liquid nitrogen and stored at −80°C for future FRET and ATPase assays.

For site-specific fluorescence labeling, the 12-residue S6 peptide (GDSLSWLLRLLN) was substituted at linker residues 868–879, and the 12-residue A1 peptide (GDSLDMLEWSLM) was added to the C-terminus immediately following V1530 (Yin et al., 2006; Zhou et al., 2007). A His10-tag was also added at the N-terminus of bMRP1 for surface immobilization. Fluorescent labeling of the A1 site was carried out after elution off the GFP nanobody column by adding 5 µM AcpS, 25 µM LD655-CoA, and 10 mM MgCl2 and incubating for 1 hr at room temperature. Excess dye was removed by size-exclusion chromatography as described above. The S6 site was then labeled by adding 5 µM Sfp, 25 µM Cy3-CoA, and 10 mM MgCl2 and incubating for 1 hr at room temperature. The doubly labeled protein was cleaned up by size-exclusion chromatography. The labeling efficiencies were estimated to be ~30% for Cy3 and ~80% for LD655 from the respective extinction coefficients of the protein and fluorophores. Sfp and AcpS synthases, as well as dye-CoA conjugates, were purified as described previously (Yin et al., 2006; Zhou et al., 2007).

### ATPase assay

ATP hydrolysis was monitored using an NADH-coupled ATPase assay (Scharschmidt et al., 1979). The reaction contained 800 nM bMRP1, 60 µg/mL pyruvate kinase, 32 µg/mL lactate dehydrogenase, 9 mM phosphoenolpyruvate, and 150 µM NADH in a buffer containing 50 mM Tris-HCl pH 8.0, 150 mM KCl, 2 mM MgCl2, 2 mM DTT, and 0.06% digitonin. ATP-Mg2+ was added to initiate the reaction and the consumption of NADH was measured at 30°C by monitoring the fluorescence at λex = 340 nm and λem = 445 nm using an Infinite M1000 microplate reader (Tecan). LTC4 stimulation experiments were performed by pre-incubating 10 µM LTC4 with the reaction mix for 15 min before initiating the reaction.

### Single-molecule fluorescence imaging

Single-molecule experiments were performed at room temperature (23 ± 1°C) on an objective-type total-internal-reflection fluorescence microscope (Olympus IX83 cellTIRF). Microfluidic imaging chambers were passivated with a mixture of PEG and biotin-PEG (Laysan Bio), and incubated with 0.8 µM streptavidin (Invitrogen) followed by 2 nM fluorescently labeled, His-tagged bMRP1 that had been preincubated with biotinylated anti-His6 antibodies (Invitrogen) for 1 hr on ice in a buffer containing 50 mM Tris-HCl pH 8.0, 150 mM KCl, 2 mM MgCl2, 0.06% digitonin, 0.5 mg/mL BSA, 10 mM phosphocreatine (Sigma), and 0.1 mg/mL creatine kinase (Sigma). A triplet-state quenching cocktail (Dave et al., 2009) of 1 mM cyclooctatetraene (Sigma), 1 mM 4-nitrobenzyl alcohol (Sigma), and 1 mM Trolox (Sigma), as well as an oxygen scavenging system (Aitken et al., 2008) containing 10 nM protocatechuate-3,4-dioxygenase (Sigma) and 2.5 mM protocatechuic acid (Sigma) were supplemented to the imaging buffer. ATP and/or LTC4 were included in the imaging buffer at concentrations specified in the text. Fluorescence signals were split with a W-View Gemini-2C (Hamamatsu), directed to two CMOS cameras (Flash 4.0 v3, Hamamatsu), and acquired by MetaMorph software (Molecular Devices) at a frame rate specified in the text.

### Analysis of smFRET data

Single-molecule fluorescence-time trajectories were extracted and subsequently analyzed using the SPARTAN software (Juette et al., 2016) in MATLAB (MathWorks). The FRET efficiency (E) was calculated as IA/(ID+IA), where ID and IA represent the donor and acceptor fluorescence intensities, respectively. Aberrant and/or noisy traces were filtered by applying the following criteria: single-step donor photobleaching, SNRBackground ≥8,<4 donor blinking events, and FRET efficiency above 0.1 for at least 15 frames.

The remaining traces were idealized using hidden Markov modeling (HMM) (Qin, 2004) implemented in SPARTAN. Initial model parameters were obtained by running ebFRET (van de Meent et al., 2014) with single-molecule trajectories for WT MRP1 with 5 mM ATP and 10 µM LTC4 collected at 25 ms resolution to ensure that all functionally relevant states were readily sampled. Potential models containing two to six non-zero FRET states with initial model parameters generated from ebFRET were applied to raw FRET trajectories from each condition using the segmental k-means algorithm (Qin, 2004) in SPARTAN, yielding optimized model parameters and idealized trajectories. A five-state model was chosen based on the following: (1) the lower bound evidence from ebFRET; (2) FRET state assignment histograms showing populated, symmetric peaks centered at each model-assigned FRET value; and (3) visual inspection of idealized trajectories from models with 2–6 non-zero FRET states. A set of five FRET states with mean E values of 0.23, 0.42, 0.63, 0.80, and 0.92 was finally chosen and fixed to describe data across all conditions.

HMM analysis of the smFRET trajectories identified transitions between each idealized state and was subsequently used to construct the corresponding transition density plots (McKinney et al., 2006). Well-separated peaks in the transition density plots lent further support for a five-state model (Figure 3—figure supplement 2). FRET contour plots and histograms were built from the first 50 or 200 frames of each trajectory with a bin size of 0.03 and plotted in Origin (OriginLab). Occupancies of each state were plotted with GraphPad Prism 7.

### Kinetic analysis of smFRET data

HMM analysis yielded the dwell times in each IF state from the idealized traces collected at a 25 ms frame rate. With this imaging condition, the effective FRET observation window is 4.1 ± 0.5 s limited by dye photobleaching. At a 300 ms frame rate, the observation window increased to 101 ± 13 s due to lower laser intensities required to achieve the same signal-to-noise ratio. However, the lower time resolution obscured fast transitions among IF states. Therefore, we grouped the four IF states (IF1, IF2, IF3, and IF4) as a composite IF state and extracted the time that molecules spent in the IF (tIF) and OF (tOF) state from active molecules taken with a 300 ms frame rate. Active molecules were defined as those that successfully transitioned to the OF state after ATP injection and represent ~60% of the whole population. The remaining molecules (~40%) never visited the OF state before photobleaching, thus were assigned as the inactive group. The tOF histograms were fit by single-exponential functions, yielding characteristic decay constants τOF. Mean values of tIF were used to describe the lifetimes of the composite IF state. These values are reported after correction for dye photobleaching (kphotobleaching = 0.010 ± 0.001 s−1). The reported errors represent the propagated SEM from the observed IF/OF lifetimes and fluorophore lifetimes.

### Cryo-EM sample preparation and data collection

Purified WT bMRP1 was mixed with 10 mM ATP and 80 µM LTC4 in DMSO (2.5% final concentration) and incubated on ice for 10 min. Immediately before freezing grids, 3 mM fluorinated Fos-choline-8 was added, yielding a final protein concentration of 5.3 mg/mL. Sample was applied to freshly glow-discharged Quantifoil R1.2/1.3 400-mesh Au Holey Carbon Grids and frozen in liquid ethane using a Vitrobot Mark IV (FEI).

Cryo-EM data were collected using a Titan Krios system (FEI) with a K2 Summit camera (Gatan) in super resolution mode at a pixel size of 0.515 Å/pixel. The electron dose rate was eight electrons/pixel/sec for an exposure time of 10 s divided into 50 frames. A total of 3993 movies were collected (Table 2).

### Cryo-EM image processing, model building, and refinement

Movie frames were corrected for gain reference and binned by two to yield a pixel size of 1.03 Å/pixel. Sub-frame alignment was carried out using MotionCor2, and the contrast transfer function (CTF) was estimated using Gctf (Zhang, 2016; Zheng et al., 2017). From 3604 micrographs, 1,143,729 particles were selected using Gautomatch (http://www.mrc-lmb.cam.ac.uk/kzhang/). 2D classification was carried out in RELION (Zivanov et al., 2018), and the best class averages contained 644,840 particles. Nearly all 2D class averages appeared to be in the outward-facing, NBD-dimerized conformation (Figure 6—figure supplement 1). 3D classification with four classes was performed in RELION using the OF bMRP1-E1454Q map low-pass-filtered to 60 Å as a reference model. All four classes appeared to contain a closed NBD dimer. The best class of 257,107 particles was then subjected to a two-stage masked 3D refinement (initiated with a mask that included the micelle and entire protein and continued with a mask that excluded the micelle and TMD0), yielding a map at 3.8 Å. Iterative cycles of CTF refinement, Bayesian polishing, and masked 3D refinement in RELION were then performed. After several cycles of this process, masked 3D classification without alignment (using the angles from the most recent 3D refinement) was performed, yielding a best class of 81,078 particles. This subset was further subjected to iterative cycles of CTF refinement, Bayesian polishing, and masked 3D refinement in RELION, yielding a final map at 3.2 Å (Figure 6—figure supplement 1).

To generate a reconstruction using all 1,143,729 particles, refinement was performed in Frealign (Grigorieff, 2016) using the map generated in the first stage of RELION refinement as the reference model. A global search was first performed using information to 8 Å, followed by several rounds of local search.

Model building and refinement were carried out as previously described (Johnson and Chen, 2018). The OF E1454Q model (PDB 6BHU) was rigid-body fit into the map using UCSF Chimera (Pettersen et al., 2004) and real-space refined in PHENIX (Adams et al., 2010). The model was then subjected to iterative cycles of refinement in Refmac (Brown et al., 2015) and manual rebuilding in COOT (Emsley and Cowtan, 2004). MolProbity (Chen et al., 2010) was used to assess the quality of the final model (Figure 6—figure supplement 2 and Table 2). The final model contains residues 203–268, 311–635, 641–870, and 942–1530, as well as one molecule of ATP, one molecule of ADP, two Mg2+ ions, and three partial cholesteryl hemisuccinate molecules. Rwork and Rfree values were calculated by generating a mask from the model with 2 Å padding, applying it to each of the half maps, and running zero cycles of refinement in Refmac against the working map (half-map 1, Rwork) and the free map (half-map 2, Rfree). Figures were prepared using UCSF Chimera and PyMOL (Schrödinger, LLC).

### Statistical analysis

Comparisons between conditions were made in GraphPad Prism seven using unpaired two-tailed Student’s t-tests unless specified otherwise. A threshold of p<0.05 was chosen to determine statistical significance (*p<0.05; **p<0.01; ***p<0.001; ****p<0.0001; ns, not significant). The number of single molecules analyzed is indicated in the figure panels. Data for each condition were collected in multiple batches across different days. Unless otherwise noted, errors reported in this study represent the approximated standard error of the mean determined from 10,000 bootstrapped samples.
