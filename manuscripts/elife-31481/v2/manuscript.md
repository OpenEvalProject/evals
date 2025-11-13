# The conformation of the histone H3 tail inhibits association of the BPTF PHD finger with the nucleosome

## Authors

- Emma A Morrison<sup>1</sup> ([ORCID: 0000-0001-6722-7961](https://orcid.org/0000-0001-6722-7961))
- Samuel Bowerman<sup>2</sup> ([ORCID: 0000-0003-0753-4294](https://orcid.org/0000-0003-0753-4294))
- Kelli L Sylvers<sup>1</sup> ([ORCID: 0000-0003-0711-402X](https://orcid.org/0000-0003-0711-402X))
- Jeff Wereszczynski<sup>2</sup> †
- Catherine A Musselman<sup>1</sup> ([ORCID: 0000-0002-8356-7971](https://orcid.org/0000-0002-8356-7971)) †

### Affiliations

1. Department of Biochemistry Carver College of Medicine, University of Iowa Iowa City United States
2. Department of Physics Illinois Institute of Technology Chicago Illinois
3. Center for Molecular Study of Condensed Soft Matter Illinois Institute of Technology Chicago Illinois

† Corresponding author

## Abstract

Histone tails harbor a plethora of post-translational modifications that direct the function of chromatin regulators, which recognize them through effector domains. Effector domain/histone interactions have been broadly studied, but largely using peptide fragments of histone tails. Here, we extend these studies into the nucleosome context and find that the conformation adopted by the histone H3 tails is inhibitory to BPTF PHD finger binding. Using NMR spectroscopy and MD simulations, we show that the H3 tails interact robustly but dynamically with nucleosomal DNA, substantially reducing PHD finger association. Altering the electrostatics of the H3 tail via modification or mutation increases accessibility to the PHD finger, indicating that PTM crosstalk can regulate effector domain binding by altering nucleosome conformation. Together, our results demonstrate that the nucleosome context has a dramatic impact on signaling events at the histone tails, and highlights the importance of studying histone binding in the context of the nucleosome.

## Introduction

Eukaryotic DNA is packaged into the cell nucleus in the form of chromatin. This DNA/histone complex contributes to DNA compaction and restricts its accessibility, also providing a mechanism for regulating the genome. Dynamic modulation of chromatin structure is vital in all DNA-templated processes. The basic subunit of chromatin is the nucleosome, comprised of an octamer containing two copies each of histones H2A, H2B, H3, and H4, around which ~ 147 bp of DNA is wrapped. The N-termini of all four histones, as well as the C-terminus of H2A, protrude to the exterior of the nucleosome core and are commonly referred to as histone tails. These tails can be extensively post-translationally modified, which is thought to be critical in regulation of chromatin structure. Genome-wide studies have revealed that particular post-translational modifications (PTMs) are correlated with specific genomic states and/or elements, and notably, strong correlations have led to the suggestion that it is patterns of PTMs that are functionally important (Zentner and Henikoff, 2013). Though some histone tail PTMs have been found to directly affect chromatin array compaction (Kan et al., 2009; Wang and Hayes, 2008; Zhou et al., 2012; Dhall et al., 2014; Mishra et al., 2016), most are thought to act through indirect mechanisms, by recruiting regulatory complexes to modified nucleosomes or modulating their activity once there. Modified histone tails are recognized by effector domains, often referred to as histone readers. A large number of families of histone effector domains have been identified over the past two decades including bromodomains, chromodomains, and PHD fingers, and these often exist in multiples within chromatin regulators (Musselman et al., 2012; Andrews et al., 2016). A wealth of studies have examined the structural determinants of effector domain specificity (Musselman et al., 2012; Andrews et al., 2016). However, due to difficulties in crystalizing these domains in complex with modified nucleosomes, the mechanism of histone binding has largely been studied with peptides corresponding to segments of the histone tails.

Biochemical studies suggest that the histone tails are highly solvent accessible, and the large majority of crystal structures of the nucleosome do not resolve the tails, suggesting a high degree of conformational heterogeneity (Böhm and Crane-Robinson, 1984; Rosenberg et al., 1986; Luger et al., 1997). This is further supported by nuclear magnetic resonance (NMR) spectroscopy studies, in which the histone tails are found to have a high degree of conformational flexibility (Zhou et al., 2012; Gao et al., 2013). Together, this has led to a model of the nucleosome where the tails are extended into solution and fully accessible. If correct, this would suggest that effector domain binding to a nucleosome versus a histone tail peptide should be largely similar. However, there is also ample evidence that the histone tails stabilize nucleosome structure and alter DNA binding. In particular, histone tails have been shown to alter transcription factor accessibility (Lee et al., 1993; Polach et al., 2000; Yang et al., 2005), thermal stability of the nucleosome (Ausio et al., 1989; Iwasaki et al., 2013), and DNA wrapping/unwrapping rates (Andresen et al., 2013). There has also long been evidence that the tails can interact with DNA (Cutter and Hayes, 2015) (in some studies quite robustly), including a recent study in which it was found that the tails transiently interact with linker DNA, inhibiting the activity of histone modifying enzymes (Stützer et al., 2016). Notably, in the one crystal structure of the nucleosome where the tails are resolved, several of them are associated with the DNA of crystallographic symmetry mates (Davey et al., 2002). In addition, in silico all-atom studies of the nucleosome have repeatedly suggested that the histone tails collapse onto core DNA (Biswas et al., 2013; Li and Kono, 2016; Shaytan et al., 2016; Ikebe et al., 2016; Chakraborty and Loverde, 2017), and tail dynamics have been correlated with the DNA unwinding process through free energy calculations (Kenzaki and Takada, 2015). Thus, our current understanding of the histone tail conformation within the nucleosome is incomplete, and we know very little about how effector domains recognize histone tails in the context of the nucleosome.

Here, we utilize NMR spectroscopy to investigate the interaction of a PHD finger with the nucleosome, specifically, the BPTF (bromodomain PHD finger transcription factor) PHD finger. The BPTF PHD finger is a well-characterized histone effector domain that recognizes the first 6 residues of the histone H3 tail, with specificity for tri-methylated lysine 4 (H3K4me3) (Li et al., 2006). We find that in the context of the nucleosome, the PHD finger association with the methylated H3 tail is inhibited. Using NMR and molecular dynamics (MD) simulations, we demonstrate that this inhibition is due to the conformation of the H3 tail within the nucleosome. Our data support a model where the H3 tails are collapsed onto the nucleosome core through robust interaction with DNA. However, they adopt an ensemble of heterogeneous DNA-bound conformations that are in fast exchange between one another, reconciling that they can be both DNA bound and have a high level of conformational flexibility. Furthermore, we find that modification or mutation of H3 tail residues outside the PHD finger binding region weakens tail association with DNA and increases accessibility to the PHD finger. This suggests that PTM cross-talk may be mediated by histone tail conformation within the nucleosome. Altogether, our data reveal a far more complex interface for effector domain binding as compared to histone peptides, and demonstrates that it is critical to characterize these associations in the proper context.

## Results

### The nucleosome inhibits association of the BPTF PHD finger with the H3 tail

In order to determine how the context of the nucleosome may affect the association of PHD fingers with the histone H3 tail, we utilized NMR spectroscopy to compare binding of the BPTF PHD finger to histone tail peptide and the nucleosome core particle (NCP). Specifically, we collected sequential 1H-15N heteronuclear single quantum coherence (1H-15N HSQC) spectra on 15N-PHD upon titration of increasing concentrations of a methylated histone tail peptide or a methylated nucleosome.

Addition of a peptide corresponding to H3 residues 1–10 methylated at lysine 4 (H3(1–10)K4me3) (Figure 1A, left, and Figure 1—figure supplement 1A and 2C) to 15N-PHD resulted in extensive chemical shift perturbations (CSPs) in resonances for residues in the binding pocket (Figure 1C) as previously determined by NMR and crystallographic studies (Li et al., 2006). The pattern of CSPs observed as a function of peptide concentration denotes low μM affinity and is consistent with previously reported affinities (Li et al., 2006). The methylated nucleosome was generated using a methyl lysine analogue (MLA) at histone H3 lysine 4 (H3KC4me3-NCP) using human histones and the 147 base pair (bp) Widom 601 DNA sequence. Importantly, mass spec analysis of the H3KC4me3 protein demonstrated that alkylation at position four was complete, with no evidence of over-alkylation, or carbamylation due to refolding in urea (Figure 1—figure supplement 3A,B). Addition of H3KC4me3-NCP to 15N-PHD led to CSPs indicating binding (Figure 1A, center). Compared to the peptide, the same set of resonances is perturbed, and the majority of resonances track along the same trajectory (Figure 1A–C). This demonstrates that the mode of interaction between the PHD finger and H3 tail in the context of the NCP is the same as observed for free histone tail peptide and that the PHD finger does not make any significant contacts with other histone tails or the NCP core. The latter is further confirmed by demonstration that binding is dependent on methylation, as seen by titration of unmodified NCP into 15N-PHD, which does not result in any significant CSPs (Figure 1—figure supplement 4).

![Figure 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-v2.jpg)

**Figure 1.:** (A) Overlay of a region of the 1H-15N HSQC (or TROSY-HSQC) spectra of 50 μM 15N-BPTF PHD upon titration of H3(1–10)K4me3 (left), H3KC4me3-NCP (center), or H3(1–44)KC4me3 (right). Spectra are color-coded according to ligand concentration, with apo spectra in black and shades of salmon for increasing concentrations of ligand. Spectra were collected at molar ratios (PHD:total H3KC4me3 mark) of: 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, and 1:5 for H3(1–10)K4me3, 1:0, 1:0.2, 1:0.5, 1:1, 1:2, 1:4 and 1:6 for H3KC4me3-NCP, and 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, 1:5 and 1:10 for H3(1–44)KC4me3. Dashed arrows track the trajectory between the apo and bound states for the two peptide titrations (in black). The H3(1–44)KC4me3 trajectories are shown (in grey) to compare titration trajectories. To account for the TROSY effect, the displayed region for the NCP titration is shifted by JNH/2 Hz. Data was collected at 37°C in 150 mM KCl. (B) Surface representation of the structure of H3K4me3-bound BPTF PHD finger (PDB ID 2F6J) with residues that are significantly perturbed upon binding to H3(1–44)KC4me3 or H3KC4me3-NCP colored in shades of salmon (average +2, +1, +1/2 standard deviations colored in raspberry, deep salmon, and wheat, respectively). The H3 tail peptide is colored pale gold and shown in stick representation. (C) CSPs (Δδ) corresponding to (A) are plotted as a function of residue for H3(1–10)K4me3 (open bars), H3KC4me3-NCP (filled black bars), or H3(1–44)KC4me3 (grey bars) for the highest ligand concentration reached in each of the titrations. As expected, the largest CSPs were observed for residues within and neighboring the aromatic cage (Y2876-E2878, F2881, Y2882, and W2891) where the K4me3 group binds, and the binding pockets for H3A1 (D2908) and H3R2 (R2887-Q2889). Note that the titration with H3KC4me3-NCP did not reach saturation. The * indicates a residue that broadens beyond detection in the fully bound state. The *** indicates a residue that is significantly perturbed along the course of the titration but broadens beyond detection in the fully bound state. An ‘X’ indicates that a residue is either not observable or not assigned. The Δδ for the H3KC4me3-NCP titration is shown re-scaled below for ease of visualization.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The full titrations from Figure 1 are shown for H3(1–10)K4me3 (A), H3(1–44)KC4me3 (B), and H3KC4me3-NCP (C). The coloring guide is displayed on the spectra. Note that the ligand ratios are listed with respect to NCP concentration in this figure but the concentration of the H3KC4me3 mark in the main text figures.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Overlay of 1H-15N HSQC spectra of 15N-BPTF PHD apo (black) and saturated with H3(1–10)K4me3 (red) or H3(1–44)KC4me3 (purple). (B) Differences between CSPs (ΔΔδ) for 15N-BPTF PHD binding to H3(1–10)K4me3 or H3(1–44)KC4me3 as a function of PHD finger residue. For the majority of residues, the chemical shift difference between the apo and bound states is larger for H3(1–10)K4me3-bound than H3(1–44)KC4me3-bound PHD. (C) Representative binding curves for NMR titrations of 15N-BPTF PHD with H3(1–10)K4me3, H3(1–44)KC4me3, and H3KC4me3-NCP. For the H3(1–10)K4me3 titration, these are the significant residues with signal visible in ≥6 of the seven collected titration points. For the H3(1–44)KC4me3 and H3KC4me3-NCP titrations, these are the significant residues that were used to fit binding constants.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** ESI mass spectrometry data is shown for unmodified and alkylated versions of histone H3 to confirm the lack of carbamylation and the proper alkylation for the MLA. The constructs are: unalkylated and alkylated full length H3K4C (A,B) and unalkylated and alkylated H3(1–44) K4C (C,D). After the alkylation reaction, the full-length histone was dialyzed into H2O + 2 mM β-ME after running over PD-10 desalting columns to remove trace salts and buffer components after the alkylation reaction. Due to the smaller size of the H3(1–44), desalting after alkylation was more difficult. The H3 peptide was de-salted using a Superdex 75 10/300 GL column, taking only fractions with minimal conductivity reading. Small amounts of HEPES buffering component remained in these samples, which shows up much stronger in the ESI mass spectrometry. The lower intensity charged states of the peptide were detected among the HEPES cluster ions, and this allowed for the determination of the alkylated H3 peptide molecular weight.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** (A) Overlay of a region of the 1H-15N TROSY-HSQC spectra of 50 μM 15N-BPTF PHD upon titration of H3KC4me3-NCP (left, same as in Figure 1A for direct comparison) or unmodified NCP (right). Spectra are color-coded according to ligand concentration, with apo spectra in black and shades of salmon for increasing concentrations of ligand. Spectra were collected at molar ratios (PHD:NCP) of 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, and 1:3. The H3(1–44)KC4me3 trajectories are shown (in dashed grey arrows) to compare titration trajectories as in Figure 1A. Data was collected at 37°C in 150 mM KCl. (B). Full spectra for the titration of unmodified NCP in (A).

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** (A) Processed BLI data set for experiment conducted using avitag-PHD loaded onto streptavidin-coated sensor. The association and dissociation phases are displayed for increasing concentrations of H3(1–44)KC4me3. The data were collected with a double reference set of ‘loading’ only buffer onto the sensor (no avitag-PHD) and collecting association/dissociation data with the sample peptide wells, which was subtracted. (B) The average of 20 s (275–295 s shown in (A)) near the end of the association phase was taken to represent the equilibrium response. This equilibrium response was plotted as a function of peptide concentration and fit to determine an estimated equilibrium Kd value, displayed with the error in the fit. (C) A data set was collected similar to in (A) but using H3KC4me3-NCP as the ligand (or ‘analyte’ in BLI terminology). These data were also collected with a double reference set of ‘loading’ buffer-only, which was subtracted. The NCP solution causes a change in response signal when sensors loaded with either avitag-PHD or buffer-only are dipped into the NCP sample wells, which becomes very large with the 230 μM NCP. This was interpreted as a change in the optical properties of the solution, which was likely caused by the viscosity of NCP samples. The double-referenced BLI data collected with avitag-PHD-loaded sensors associating with 20 μM H3(1–44)KC4me3 is overlaid. At ~20 μM, H3(1–44)KC4me3 shows significant association and dissociation curves. At the same ‘analyte’ concentration, H3KC4me3-NCP (which should result in a significantly larger BLI response signal upon binding due to the significantly larger size) elicits minimal response. At 10-fold higher concentration of H3KC4me3-NCP, there is still minimal response signal. This is consistent with binding that is too weak to be measured via the given technique under the given conditions. All data displayed in this figure were collected at 37°C.

Surprisingly, though the binding pocket was the same, the magnitude of CSPs upon titration of H3KC4me3-NCP was significantly smaller as compared to an equivalent addition of histone peptide (Figure 1A,C), and the titration with NCP does not reach saturation (i.e. a fully bound state) at the same molar ratios as does the peptide (Figure 1—figure supplements 1C and 2C). If the mode of interaction between the PHD finger and NCP is identical to the PHD-H3(1–10)K4me3 complex, as is suggested by the equivalent CSP trajectories, then the chemical shift values of the fully bound state should be identical. Under this assumption, the small shift towards the bound state seen for the NCP indicates that binding in the context of the NCP is dramatically weaker.

In general, the MLAs are robust mimetics of methylated lysines, but in some cases, they bind substantially weaker (Seeliger et al., 2012). A recent study extensively compared the interaction of the BPTF PHD finger with a histone peptide containing a true methylated lysine versus one containing the MLA. Though a crystal structure revealed the mechanism of association is largely the same, the authors reported a loss in binding affinity of about an order of magnitude for the MLA (Chen et al., 2018). Thus, we first sought to ensure that the weaker binding observed for the H3KC4me3-NCP was not simply due to the analogue itself. To do this, we produced an MLA version of the histone tail alone, H3(1–44)KC4me3 (which we will refer to as H3KC4me3-Tail). Titration of the analogue-containing H3KC4me3-Tail into 15N-PHD resulted in large CSPs (Figure 1A, right), immediately suggesting that the analogue is not the sole cause of the minor CSPs observed for H3KC4me3-NCP. Consistent with Chen et al., binding to the MLA-containing peptide was moderately weaker as denoted by the pattern of CSPs for a subset of residues changing from intermediate (seen with the true methylated lysine) to fast exchange on the NMR time-scale (Figure 1A, and Figure 1—figure supplement 1B). Importantly, the residues perturbed are identical between the two peptides (Figure 1B,C), though comparison of spectra of the PHD finger saturated with either H3(1–10)K4me3 or H3KC4me3-Tail reveals that the bound states are not quite identical (Figure 1A, and Figure 1—figure supplement 2A). Though for the majority of residues the resonances progress along the same trajectory from apo to bound, the difference in chemical shift (Δδ) between the free and fully bound states of the PHD is generally greater for H3(1–10)K4me3 as compared to H3KC4me3-Tail (Figure 1A,C, and Figure 1—figure supplement 2B).

Fitting CSPs as a function of ligand concentration indicates that the PHD finger binds H3KC4me3-Tail with a low micromolar Kd of 12 ± 1 μM (Figure 1—figure supplement 2C, center). As saturation is not reached during the NMR titration with the H3KC4me3-NCP, a robust binding affinity cannot be determined. However, the CSPs as a function of H3KC4me3 mark suggest a dissociation constant in the low millimolar range (Figure 1—figure supplement 2C, right). Thus, the NMR data indicate that binding to the NCP is substantially weaker than binding to the free histone tail peptide. To confirm this, we utilized biolayer interferometry (BLI). A biotin-PHD construct was immobilized on streptavidin-coated sensors, and experiments were carried out with H3KC4me3-Tail or H3KC4me3-NCP under similar solution conditions as the NMR experiments. Clear association and dissociation curves were observed for binding to the H3KC4me3-Tail with strong response signal (Figure 1—figure supplement 5A). Fitting the equilibrium response at the end of the association phase, the binding affinity was determined to be 7.0 ± 0.1 μM (Figure 1—figure supplement 5B). This is slightly higher affinity than that determined via NMR, likely due to the fact that the PHD finger is immobilized for BLI. In contrast, no association was detected with the H3KC4me3-NCP at the highest concentrations used for the H3KC4me3-Tail, even though it is expected to elicit a larger BLI response signal due to its significantly larger size. Even at a ten-fold higher concentration, H3KC4me3-NCP produces minimal response signal (Figure 1—figure supplement 5C).

Together, these data demonstrate that the BPTF PHD finger adopts the same bound state with the H3 tail in the context of the nucleosome as with the free histone tail peptide, making no direct interaction with the nucleosome core. However, association is substantially inhibited in the context of the nucleosome. Though moderate effects are seen from the use of the MLA versus true methylated lysine, these do not account for the dramatically weaker association observed for the NCP. Thus, it is possible that the conformation of the nucleosome itself is causing a reduction in the observed binding affinity.

### The H3 tail experiences distinct conformations in isolation or in the native context of the NCP

To further investigate the conformation of the H3 tail (Figure 2A) and its potential effect on PHD finger binding, 15N-H3-NCPs were prepared by refolding octamer with 15N-labeled H3, and unlabeled H2A, H2B, and H4, and reconstituting this with the 147 bp 601 Widom DNA. Similar to previous NMR spectra on the Drosophila nucleosome reconstituted with 167 bp DNA and X. laevis nucleosome reconstituted with 187 bp DNA (Zhou et al., 2012; Stützer et al., 2016), the 1H-15N HSQC spectrum of the 15N-H3-NCP shows only 32 of the possible 129 non-proline peaks for H3. Assignments were performed using traditional triple resonance experiments and confirm that these correspond to residues 3–36 of the N-terminal tail. The majority of these resonances have 1H chemical shifts in the range of 8.0–8.5 ppm (Figure 2B, left), consistent with an unstructured region, and chemical shift analysis using CSI3.0 (Hafsa et al., 2015) (Figure 2—figure supplement 1A) confirms a random coil conformation, consistent with previous studies (Zhou et al., 2012; Stützer et al., 2016). The single set of peaks observed implies that the two H3 tails within the NCP are identical. Due to the large size (~200 kDa) and resultant slow tumbling of the NCP, it is expected that the residues in the core would not be observable using this isotope labeling scheme. Thus, the observation of the H3 tail suggests that this region experiences greater intrinsic conformational dynamics than do the residues in the core. This is consistent with previous structural and biochemical studies that suggest that the histone tails are largely solvent exposed.

![Figure 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig2-v2.jpg)

**Figure 2.:** (A) Cartoon depiction of the NCP with extended histone tails. H3 is colored gold, and the sequence for the H3 tail is displayed. (B)1H-15N HSQC or SOFAST HMQC spectra of 15N-H3-NCP (in gold) shown on the left and overlaid with 15N-H3(1–44) (black) shown on the right. Spectra were collected at 25°C in 150 mM KCl. (C) Chemical shift differences (Δδ) between the H3 tail in the context of the NCP and the isolated peptide, shown as a function of H3 tail residue. Residues labeled in grey are not observable in the 1H-15N HSQC/HMQC, either because they correspond to proline or are otherwise unobservable. Though differences in chemical shift are expected for residues at the C-terminus of the tail just adjacent to the core, significant chemical shift differences are seen for the vast majority of observable residues along the entire length of the tail. Chemical shift values for both the peptide and the NCP are consistent with an intrinsically disordered conformation, suggesting that the change is not one of secondary structure. Notably, differences are largest around tandem arginine-lysine as well as serine and threonine residues.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Plot of the secondary structure for the H3 tail predicted by CSI3.0 as entirely random coil based on chemical shift values. (B) 1H-15N HSQC spectra collected on 55 μM 15N-H3-NCP at 10 (blue), 25 (green), and 37°C (red) at 0 mM added KCl. (C) 1H-15N HSQC spectra collected on 55 μM 15N-H3-NCP at 10 (red), 25 (blue), and 37°C (orange) at 150 mM added KCl. (D) 1H-15N HSQC spectra collected on 55 μM 15N-H3-NCP at 37°C in the presence of increasing concentrations of KCl, color coded according to legend. (E) 1H-15N HSQC spectra collected on 55 μM 15N-H3-NCP at 37°C and 150 mM KCl in the presence of increasing concentrations of MgCl2, color coded according to legend. The initial spectrum (0 mM MgCl2) was collected with 2 mM EDTA. (F) 1H-15N SOFAST HMQC spectra collected on 110 μM 15N-H3(1–44) at 10°C. Spectra were collected at increasing concentrations of added KCl, as indicated in the figure. The titration was carried out at 10°C because the peptide signal is significantly attenuated at 25 and especially 37°C. (G) Overlay of 1H-15N HSQC/HMQC spectra for 15N-H3-NCP at 0 mM (green) and 150 mM (gold) added KCl and 15N-H3(1–44) at 150 mM added KCl (purple). These spectra were all collected at 25°C to bridge the KCl titrations shown in (D) and (F). There are several confounding factors (e.g. temperature and salt-sensitivity of the free and bound states and differential amide exchange rates) that complicate these spectral overlays, but comparison of these three spectra at 25°C shows a number of residues that are consistent with the idea that KCl can shift the population of collapsed vs. extended tails. An increase in salt concentration is expected to cause an increase in the population of nucleosomal H3 tails that are released (or partially released) from the core DNA. Some of these residues are labeled, with arcs connecting the three states.

The ability to detect NMR resonances for the H3 tail within the nucleosome has been interpreted to reflect a disordered and predominantly accessible conformation (Zhou et al., 2012; Gao et al., 2013). However, a recent NMR study on the X. laevis nucleosome reconstituted with 187 bp DNA revealed differences in the nucleosomal H3 tail as compared to a histone tail peptide, and ultimately concluded that this was due to transient interactions with the linker DNA (Stützer et al., 2016). Here, there is no linker DNA present, thus we sought to investigate the conformation of the H3 tail in the context of the minimal NCP. Consistent with a solvent exposed conformation, changes in solution conditions, specifically temperature, KCl, and MgCl2, result in global perturbations in the 1H-15N HSQC spectra (Figure 2—figure supplement 1B–G), though notably, none of the conditions tested structure the H3 tail. However, similar to studies with the 187bp-nucleosome (Stützer et al., 2016), comparison of the 1H-15N HMQC/HSQC spectra for an isolated peptide corresponding to residues 1–44 of the H3 tail (15N-H3-Tail) and for the 15N-H3-NCP reveals significant chemical shift differences between the free peptide and NCP states along the full length of the H3 tail (Figure 2B right, 2C).

Together these data are consistent with nucleosomal H3 tails that are unstructured and highly mobile. However, chemical shift data indicate that the entire H3 tail (not just residues near the core) has a distinct conformation in the context of the NCP, consistent with an interaction within the NCP itself.

### The H3 tail robustly interacts with the nucleosome core

To determine if the H3 tail can interact with the NCP under physiological conditions, we titrated NCPs into the isolated tail (Figure 3A, and Figure 3—figure supplement 1A). Upon an initial addition of a 0.2:1 molar ratio of unlabeled NCP into 15N-H3-Tail, the sample severely aggregated, and signal was lost within the 1H-15N HSQC spectrum. However, subsequent addition of NCP to a ratio of 0.5:1 led to a partial re-appearance of signal, with significant CSPs as compared to apo. Further addition of NCP resulted in an increase in peak intensity without perturbation in chemical shift (Figure 3—figure supplement 1C,D). This pattern is characteristic of a slow exchange process on the NMR timescale and indicates a robust association. Note that for slow exchange, generally a decrease in the intensity of the apo state is observed in conjunction with an increase in intensity for the bound state. However, due to the initial aggregation, only the bound species is observed. The origin of the aggregated or phase-separated state is uncertain at this point.

![Figure 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig3-v2.jpg)

**Figure 3.:** (A) Overlay of 1H-15N HSQC or SOFAST HMQC spectra for 70 μM 15N-H3(1–44) (black), 70 μM 15N-H3(1–44) in the presence of unlabeled NCP at a 1:3 ratio (green), and 55 μM 15N-H3-NCP (gold). (B) Same as in (A), except that the 15N-H3(1–44) is bound to unlabeled tlNCP at a 1:3 ratio (green). These spectra indicate that H3(1–44) binds to the nucleosome core in-trans. (C) CSPs (Δδ) as a function of H3 tail residue corresponding to the difference between 15N-H3(1–44) apo and bound to tlNCP. (D) Chemical shift differences (Δδ) as a function of H3 tail residue corresponding to the difference between the native, nucleosomal H3 tail and H3(1–44) peptide bound to tlNCP. In (C) and (D), residue letters colored in grey are not observable in the 1H-15N HSQC/HMQC, either because they correspond to proline or are otherwise unobservable. (E) Representative snapshot from one of the NCP simulations showing the H3 tails (gold), as well as the remaining histone tails (grey), collapsed onto the core DNA surface (blue).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Overlay of 1H-15N SOFAST HMQC spectra of 70 μM 15N-H3(1–44) apo and upon addition of NCP (A) or tlNCP (B). Spectra are color-coded according to protein:NCP molar ratio, with apo spectra in black and shades of green for increasing concentrations of NCP/tlNCP. Spectra were collected at molar ratios (PHD:NCP/tlNCP) of 1:0, 1:0.2, 1:0.5, 1:1, 1:2 and 1:3. 1H-15N HSQC of 55 μM 15N-H3-NCP is overlaid in gold for comparison. Spectra were collected at 25°C in 150 mM KCl. Upon addition of NCP/tlNCP, signal initially disappears and then reappears at the bound state chemical shift and increases in intensity upon further addition of ligand. (C) 1D 1H spectra extracted from 1H-15N SOFAST HMQC spectra of 15N-H3(1–44) apo and at increasing concentration of NCP/tlNCP in (A) and (B) for residue Thr22. These spectra are slices taken through the 15N-center of the apo (point 714) and bound (point 734) states and overlaid to compare the peak intensity as a function of 15N-H3(1–44):NCP/tlNCP ratio. (D) Resonance intensity as a function of NCP/tlNCP ratio for residues K4 (squares), T22 (tall diamonds), A24 (triangles), T32 (squat diamonds), and V35 (circles). Closed symbols and solid lines correspond to titration of tlNCP while open symbols and dashed lines correspond to titration of NCP.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Time points of the trypsin digest of reconstituted NCPs were run on 18% SDS-PAGE gels. NCPs were first incubated with TPCK Trypsin immobilized on magnetic beads at room temperature for 30 min in 0.5xTE, which resulted in little digestion (left gel). The sample was then incubated for an additional 70 min with 75 mM KCl (right gel).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Radius of gyration timeseries for the unmodified NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

This titration was repeated using tailless NCPs (tlNCPs) generated through treatment of reconstituted NCPs with trypsin (Figure 3B, and Figure 3—figure supplements 1B and 2). Upon addition of tlNCP into 15N-H3-Tail, the same initial loss of signal was observed as for the NCP. Subsequent addition of tlNCPs led to re-appearance of signals with identical chemical shifts to those observed upon binding NCP (containing tails). This reveals that the tlNCP-bound state of H3-Tail is identical to the NCP-bound state (Figure 3A vs. B, and Figure 3—figure supplement 1A–C), and indicates that the H3-Tail-NCP interaction is not mediated through tail-tail interactions but instead through components within the core. Plotting the intensity of H3 tail bound-state resonances as a function of NCP/tlNCP concentration shows greater intensity in binding to tlNCP than to NCP throughout the titration. In addition, peak intensities plateau (indicating saturation) with tlNCP but not NCP over the concentration range tested (Figure 3—figure supplement 1C,D). Together, this indicates that the H3-Tail binds tlNCP tighter than NCP. This is consistent with a mechanism in which free H3 tail peptide must compete with tethered tails to associate with the core, providing additional evidence that nucleosomal H3 tails are associating with the NCP core. Plotting the CSPs as a function of residue for association with the NCP/tlNCP reveals that residues along the entire H3 tail are affected by binding (Figure 3C).

The structure of the isolated H3 tail peptide, the H3 tail peptide bound to the NCP in-trans, and the native H3 tail in the context of the NCP can be compared through overlay of the corresponding 1H-15N HSQC/HMQC spectra (Figure 3A,B). As noted previously, there are large differences in the spectra of H3-Tail and H3-NCP (Figure 3A, compare black vs. gold). In contrast, the spectra for H3-Tail bound in-trans to the NCP or tlNCP much more closely resembles H3-NCP (Figure 3A,B). In fact, the majority of resonances for H3-Tail bound in-trans to the NCP/tlNCP lie along a linear or nearly linear trajectory between the corresponding resonances for apo H3-Tail and H3-NCP. This suggests that the in-trans NCP-bound state of the H3 tail peptide closely reproduces the environment of the native H3 tail, consistent with the native tail associating with the NCP core. Differences between the in-trans bound and native histone tails likely arise because the H3 tail is uniquely tethered to the NCP in the native state, and when binding in-trans, the tail is likely to associate with regions inaccessible to the restricted tail binding in-cis. Indeed, when comparing the chemical shift of the H3 tail peptide bound to the NCP in-trans and the native H3 tail, the greatest differences are in the C-terminal half of the H3 tail (Figure 3D). One of the largest differences is seen for lysine 36, which is immediately adjacent to where the H3 tail connects to the core histone fold and protrudes from between the DNA gyres. Additionally, there are significant differences observed for residues 24–28 and Thr32.

Notably, these data indicate that the interaction between the tails and core is quite robust, yet the fact that the resonances are detectable indicates that the tails are also conformationally dynamic. To investigate this further, MD simulations of the complete NCP were carried out. Simulations were conducted on NCPs containing unmodified H3 tails (un-NCP). Each NCP was initiated from three different H3 tail conformations: one based on the 1KX5 crystal structure (the only crystal structure that resolves all H3 histone tail residues), another in which the H3 tails were extended linearly from residues 1 to 40, and a third based on de novo modeling of the tails. Consistent with the robust interaction between the H3 tail and the NCP core seen by NMR, simulations show that the H3 tail consistently collapses onto the NCP regardless of the initial conformation (Figure 3E, Video 1). This is measured quantitatively through calculation of the radius of gyration (Rg) of the full histone H3 protein, which reduced from a maximum of 45 Å to ~26 Å upon tail collapse (Figure 3—figure supplement 3, Table 1). Notably, the average root mean square deviation (RMSD) of H3 tail conformations calculated between the final frames of all simulations, after aligning NCP core conformations, is 50.0 Å, suggesting that there exists a wide range of potential conformations available to the H3 tail. If only simulations of the same initial tail conformation are considered, then this value is reduced by varying degrees to values between 30.0 Å and 41.2 Å. This reduction of 10–20 Å suggests that the final conformation of the H3 tail is influenced somewhat by the choice of initial tail structure, but that the ensemble of final states is still extensive for a single initial conformation. In addition, since the tail compacts onto the outer surface of the NCP core, a significant amount of surface area of the tails is still exposed to solvent (>2600 Å2), which is in agreement with data suggesting high solvent-accessibility.

**Table 1.**
 Measured quantities for the NCP simulations conducted in this study.


<table>
  <thead>
    <tr>
      <th>Modification</th>
      <th>Initial tails</th>
      <th>Rg (Å)</th>
      <th>ΔGDNA-tail (kcal/mol)</th>
      <th>% Helicity</th>
      <th>% Sheet</th>
      <th>Solvent exposed area (Å2)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">Unmodified</td>
      <td>1KX5</td>
      <td>24.8 ± 0.6</td>
      <td>−76.8 ± 6.2</td>
      <td>6.1%</td>
      <td>2.3%</td>
      <td>2514 ± 61</td>
    </tr>
    <tr>
      <td>linear</td>
      <td>25.1 ± 0.6</td>
      <td>−62.5 ± 7.1</td>
      <td>6.8%</td>
      <td>4.0%</td>
      <td>2674 ± 83</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>25.6 ± 0.6</td>
      <td>−73.1 ± 6.6</td>
      <td>3.0%</td>
      <td>2.3%</td>
      <td>2680 ± 62</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>25.2 ± 0.3</td>
      <td>−70.8 ± 4.0</td>
      <td>5.3%</td>
      <td>2.9%</td>
      <td>2623 ± 42</td>
    </tr>
    <tr>
      <td rowspan="4">H3K4me3</td>
      <td>1KX5</td>
      <td>25.0 ± 0.5</td>
      <td>−82.2 ± 5.8</td>
      <td>4.7%</td>
      <td>0.5%</td>
      <td>2562 ± 83</td>
    </tr>
    <tr>
      <td>linear</td>
      <td>24.9 ± 0.4</td>
      <td>−76.3 ± 7.1</td>
      <td>5.0%</td>
      <td>1.1%</td>
      <td>2697 ± 76</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>26.1 ± 0.6</td>
      <td>−57.6 ± 5.3</td>
      <td>7.8%</td>
      <td>3.3%</td>
      <td>2888 ± 60</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>25.3 ± 0.3</td>
      <td>−72.0 ± 4.0</td>
      <td>5.8%</td>
      <td>1.7%</td>
      <td>2716 ± 48</td>
    </tr>
    <tr>
      <td rowspan="4">quadAc</td>
      <td>1KX5</td>
      <td>26.5 ± 0.5</td>
      <td>−54.8 ± 2.8</td>
      <td>5.3%</td>
      <td>3.2%</td>
      <td>2914 ± 62</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>25.5 ± 0.6</td>
      <td>−53.8 ± 5.9</td>
      <td>5.0%</td>
      <td>2.9%</td>
      <td>3002 ± 68</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>26.4 ± 0.4</td>
      <td>−47.6 ± 4.3</td>
      <td>7.3%</td>
      <td>3.9%</td>
      <td>2867 ± 78</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>26.1 ± 0.3</td>
      <td>−52.1 ± 2.7</td>
      <td>5.9%</td>
      <td>3.3%</td>
      <td>2928 ± 42</td>
    </tr>
    <tr>
      <td rowspan="4">4xK-Q</td>
      <td>1KX5</td>
      <td>26.0 ± 0.4</td>
      <td>−59.3 ± 4.3</td>
      <td>6.6%</td>
      <td>1.4%</td>
      <td>2666 ± 58</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>24.6 ± 0.5</td>
      <td>−52.3 ± 5.1</td>
      <td>6.1%</td>
      <td>3.7%</td>
      <td>2736 ± 44</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>25.4 ± 0.5</td>
      <td>−57.6 ± 5.3</td>
      <td>4.5%</td>
      <td>3.3%</td>
      <td>2733 ± 71</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>25.3 ± 0.3</td>
      <td>−55.2 ± 2.9</td>
      <td>5.7%</td>
      <td>2.8%</td>
      <td>2712 ± 34</td>
    </tr>
    <tr>
      <td rowspan="4">H3K4me3/4xK-Q</td>
      <td>1KX5</td>
      <td>25.5 ± 0.5</td>
      <td>−65.4 ± 5.6</td>
      <td>8.0%</td>
      <td>0.9%</td>
      <td>2744 ± 55</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>25.3 ± 0.5</td>
      <td>−57.3 ± 5.6</td>
      <td>5.9%</td>
      <td>3.7%</td>
      <td>2798 ± 88</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>26.6 ± 0.5</td>
      <td>−50.3 ± 6.1</td>
      <td>3.6%</td>
      <td>4.3%</td>
      <td>2784 ± 59</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>25.8 ± 0.3</td>
      <td>−57.7 ± 2.7</td>
      <td>5.8%</td>
      <td>2.9%</td>
      <td>2775 ± 40</td>
    </tr>
    <tr>
      <td rowspan="4">H3K4me3/3xR-A</td>
      <td>1KX5</td>
      <td>25.3 ± 0.6</td>
      <td>−55.1 ± 3.9</td>
      <td>7.8%</td>
      <td>1.9%</td>
      <td>2461 ± 52</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>25.1 ± 0.6</td>
      <td>−38.9 ± 3.9</td>
      <td>10.6%</td>
      <td>1.7%</td>
      <td>2567 ± 79</td>
    </tr>
    <tr>
      <td>MODELLER</td>
      <td>25.7 ± 0.6</td>
      <td>−41.4 ± 4.2</td>
      <td>8.0%</td>
      <td>2.4%</td>
      <td>2574 ± 60</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>25.4 ± 0.6</td>
      <td>−45.7 ± 2.7</td>
      <td>8.8%</td>
      <td>2.0%</td>
      <td>2534 ± 39</td>
    </tr>
  </tbody>
</table>

![Video 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-video1.mp4.jpg)

**Video 1.:** Protein backbone arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

Together, these data show that the H3 tail binds robustly to the nucleosome core. The MD simulations suggest a heterogenous ‘bound state’ comprised of an ensemble of conformations of the H3 tail bound to the core. The fact that resonances are visible in the HSQC spectrum, and that there is only one resonance per residue, suggests that there is a fast, dynamic transition between these core-associated states.

### The H3 tail interaction with DNA mimics the chemical environment within the NCP

Several previous studies have identified an interaction between histone tails and DNA (Cutter and Hayes, 2015), including a recent NMR study that demonstrated interaction of the H3 tail with linker DNA in the nucleosomal context (Stützer et al., 2016). To test if the interaction observed here between the H3 tail and the nucleosome core is driven by DNA, we compared spectra of the H3 tail bound to a 21 bp double-stranded DNA fragment to those of the H3 tail bound to the nucleosome in-trans and also in its native state within the nucleosome. Comparison of the corresponding 1H-15N HMQC/HSQC spectra for the DNA-bound H3-Tail with the H3-NCP reveals marked similarities (Figure 4—figure supplement 1). As was seen for NCP/tlNCP-bound H3-Tail, the majority of resonances for the DNA-bound H3-Tail lie along a linear or near-linear trajectory between the chemical shift values for the apo H3-Tail and the H3-NCP (Figure 4A). This strongly suggests that the interaction of the H3 tail with the nucleosome core is driven through contacts with DNA. This is very similar to previous observations for the X. laevis 187bp-nucleosome containing linker DNA (Stützer et al., 2016) and reveals that, even in the absence of accessible linker DNA, the native histone H3 tails are DNA bound. Notably, the chemical shift values for the tlNCP-bound state are more similar to the native H3 tail than those for the 21bp-DNA-bound state (Figure 4B). This is most notable for arginine residues and, to a lesser extent, their neighboring residues (see residues 5–9, 17–18, and 24–27), which still deviate considerably in chemical shift between the DNA-bound and native H3 tails whereas binding to tlNCP much better reproduces the native NCP chemical shift. It is possible that the arginines, which fit into the minor groove of DNA, are more sensitive to DNA shape (linear vs. bent).

![Figure 4.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig4-v2.jpg)

**Figure 4.:** (A) Overlay of 1H-15N HSQC or SOFAST HMQC spectra of 15N-H3(1–44) (black), 15N-H3(1–44) bound to DNA (blue) or tlNCP (green), and 15N-H3-NCP (gold). Expanded regions of the overlay are shown for selected residues for comparison of histone tail states. Arrows connect the apo 15N-H3(1–44) to the native 15N-H3-NCP. (B) Chemical shift differences (Δδ) as a function of H3 tail residue corresponding to the difference between the native, nucleosomal H3 and H3(1–44) either apo (black), DNA-bound (blue), or tlNCP-bound (green). Residue letters colored in grey are not observable in the 1H-15N HSQC/HMQC, either because they correspond to proline or are otherwise unobservable. The * indicates that a residue is unobservable.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Overlay of 1H-15N SOFAST HMQC spectra of 110 μM 15N-H3(1–44) apo and at increasing concentrations of 21 bp dsDNA. Spectra are color-coded according to ligand concentration, with apo spectra in black and shades of blue for increasing concentrations of DNA. Spectra were collected at molar ratios (PHD:DNA) of 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2 and 1:4. 1H-15N HSQC of 55 μM 15N-H3-NCP is overlaid in gold for comparison. Significant CSPs are observed in this titration. Saturation is reached at a 1:1 molar ratio, indicating robust binding. (B) Same as (A), but in the presence of 1 mM MgCl2. Comparison of the titrations in (A) and (B) indicates that 1 mM MgCl2 does not have an effect on the interaction between DNA and H3(1–44). (C) CSPs (Δδ) as a function of H3 tail residue corresponding to the difference between H3(1–44) apo and bound to DNA. This plot reveals that residues along the entire H3 tail are perturbed by binding. Residues labeled in grey are not observable in the 1H-15N HMQC, either because they correspond to proline, are unassigned, or are otherwise unobservable.

Consistent with the experimental data, the three-dimensional distribution of tail atoms in the MD simulation of the un-NCP shows that tails package primarily onto the core DNA surface (Figure 5A). MM-GBSA analysis on a per residue basis suggests that association is driven by arginines and, to a lesser extent, lysines, which is aligned with the NMR CSP data (Figure 5C). By calculating the sum of contributions from H3 tail residues for the Gibbs free energy (ΔG) of DNA binding, it is observed that the tails bind to DNA at a ΔG of −70.8 ± 4.0 kcal/mol. In contrast, the interaction energy between H3 tail residues and other histone components is a disfavorable 5.2 ± 0.9 kcal/mol. We note that the MM/GBSA analysis method presented here involves several approximations, including a mean-field solvent model and the lack of the solute configurational entropy change, therefore the free energy change values presented should only be interpreted qualitatively (Hou et al., 2011; Rastelli et al., 2010; Genheden et al., 2011). Despite these limitations, our results demonstrate that interactions between the H3 tails and the NCP core are robust and favorable, and driven by preference for the DNA surface.

![Figure 5.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig5-v2.jpg)

**Figure 5.:** Three-dimensional probability distribution of the locations of heavy atoms within H3 N-terminal tails for the unmodified (A) and H3K4me3-NCP (B) simulations, superimposed upon the crystal structure (PDBID 1KX5). Histones are shown in gold and DNA is shown in blue. Darker regions represent areas of higher probability, and lighter regions depict areas of lower probability. (C) MM-GBSA analysis of the per-residue contributions to DNA binding of H3 tail residues in the unmodified (gold) and H3K4me3 (raspberry) NCP simulations. (D) Overlay of 1H-15N HSQC spectra of 15N-H3-NCP (gold) and 15N-H3KC4me3-NCP (raspberry), which indicates that the MLA installed at K4 only causes local perturbations to the H3 tail. Residues are labeled based on assignments for 15N-H3-NCP.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Percentage of simulation frames where each residue is in β-sheet (blue), α-helix (green), turn (purple), or random coil (grey) configurations. For each residue, results are shown for (left to right): un-NCP, quadAc-NCP, and 4xK-Q-NCP. Locations of modifications/mutations are identified by ‘*”. Every residue was in a random coil configuration in over 50% of simulated frames, regardless of chemical composition.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Radius of gyration timeseries for the H3K4me3-NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

While some previous simulations, secondary structure predictions, and circular dichroism studies have suggested that the H3 tail adopts distinct α-helical portions (Banères et al., 1997; Wang et al., 2000; Li and Kono, 2016; Ikebe et al., 2016; Potoyan and Papoian, 2011), others present a tail that is largely unstructured (Shaytan et al., 2016; Erler et al., 2014; Roccatano et al., 2007). Here, consistent with the NMR analysis (see above), simulation results also suggest that the H3 tails are largely unstructured when bound to the nucleosome core, as determined by a DSSP characterization. This reveals that, on average, tail residues in the un-NCP are only 5.5% α-helical and 2.9% β-strand (Table 1). Inspecting on a per-residue basis shows that random coil is the preferred state of the entire tail (Figure 5—figure supplement 1). Identical calculations were also performed for NCPs containing H3K4me3 (H3K4me3-NCP). Notably, a nearly identical three-dimensional distribution is observed for tails containing H3K4me3 (Figure 5B, Figure 5—figure supplement 2 and Video 2). The ΔG of DNA binding of the H3 tails was also not significantly altered by the presence of the tri-methyl modification (ΔG = −72.0 ± 4.0 kcal/mol), and there were no effects on secondary structure, with 6.0% α-helical and 1.6% β-strand configurations. In agreement with this, an 1H-15N HSQC spectrum of the 15N-H3KC4me3-NCP only demonstrates perturbations in residues around lysine 4, whereas the remainder of the tail is not perturbed, confirming that methylation of lysine four does not substantially alter the interaction of the H3 tail with the nucleosome core (Figure 5D).

![Video 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-video2.mp4.jpg)

**Video 2.:** Protein backbone arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

Together, these data reveal that the H3 tail is binding the DNA component within the context of the NCP. NMR and MD simulations demonstrate that the H3 tail is robustly associated with the nucleosomal DNA. The interaction is driven largely by basic residues suggesting an electrostatic interaction. Consistent with this, spectra recorded on 15N-H3-NCP upon increasing concentrations of mono-valent ions results in CSPs that follow a trajectory roughly towards the free peptide (Figure 2—figure supplement 1G). Notably, methylation of lysine four does not release the H3 tail from the DNA.

### The H3 tail-DNA interaction inhibits binding by effector domains, mirroring nucleosomal conditions

To test if the interaction between the H3 tail and DNA is the cause of the decreased association between the BPTF PHD finger and H3KC4me3-NCP, we probed the interaction between the PHD finger and H3 tail peptide in the presence of DNA. To this end, 1H-15N HSQC spectra were collected on 15N-labeled PHD finger upon titration of unlabeled H3 tail peptide (H3(1–10)K4me3 or H3KC4me3-Tail) that was pre-bound to a 21 bp DNA at a 1:2 molar ratio. The titration of DNA-bound H3(1–10)K4me3 into 15N-PHD yielded very similar CSPs as were observed upon titration of H3(1–10)K4me3 alone (Figure 6A). CSPs are observed along the same trajectories from apo to bound between the two titrations, indicating that the presence of DNA does not alter the binding mode. Comparison of the CSP as a function of molar ratio of ligand between histone tail alone and histone tail pre-bound to DNA reveals only a slightly lower population in the bound state when DNA is present (Figure 6A). In contrast, a large effect was observed for the full-length tail peptide, H3KC4me3-Tail. Titration of H3KC4me3-Tail pre-bound to DNA into 15N-PHD leads to CSPs that, similar to the shorter peptide, progress along the same trajectories from apo to bound as compared to H3KC4me3-Tail alone. However, with the longer peptide, comparison of the CSPs as a function of ligand indicates a much smaller population of PHD in the bound state for each PHD:peptide ratio when the peptide is pre-bound to DNA than for the peptide alone (Figure 6B). Fitting the CSPs as a function of peptide concentration yields an apparent Kd of 180 ± 30 μM for H3KC4me3-Tail, which is 15-fold weaker than peptide alone (12 ± 1 μM), revealing that the interaction between the H3 tail and PHD is decreased due to competitive binding of the H3 tail to DNA (Figure 6C). Peak broadening suggests the possibility of a ternary complex, where the PHD finger and DNA could be simultaneously binding to different regions of H3KC4me3-Tail, but this would require further investigation to confirm.

![Figure 6.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig6-v2.jpg)

**Figure 6.:** (A) Overlay of a region of the 1H-15N HSQC spectra of 50 μM 15N-BPTF PHD upon titration of H3(1–10)K4me3 (left, as shown in Figure 1A), or H3(1–10)K4me3 pre-bound to DNA at a ratio of 1:2 (right). (B) Same as in (A) but for the H3(1–44)KC4me3 peptide. Spectra are color-coded according to peptide concentration, with apo spectra in black and shades of salmon for increasing concentrations of peptide. Spectra are shown for molar ratios (PHD:peptide) of: 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, and 1:5 for H3(1–10)K4me3 and 1:0, 1:0.25, 1:0.5, 1:1, 1:2, 1:5 and 1:10 for H3(1–44)KC4me3. Dashed arrows track the trajectory between apo and bound states for peptide alone and are shown as visual aids for titrations where peptide was pre-bound to DNA. Binding affinities determined from the NMR data as described in Materials and methods are displayed. (C) Cartoon model to depict the linked equilibria of H3 tail peptide-DNA binding and PHD finger-H3 tail peptide binding. It is possible that the H3 tail could partially release from DNA and interact with the PHD finger, but the existence of this type of ternary complex is not conclusively shown from the data. The competitive H3 tail peptide-DNA binding is significantly greater with the longer tail peptide.

Together these data demonstrate that association of the H3 tail with DNA does indeed inhibit association of the PHD finger. A significant effect is only seen with the full length H3 tail, indicating that multiple contacts along the length of the tail are required for a high avidity interaction with DNA. Although the effect is not as strong as that observed for the H3KC4me3-NCP (Figure 1A, center), it is expected that in the context of the nucleosome, where the tail is tethered close to the DNA, the greatly increased effective local concentration would increase the apparent affinity between the histone tail and DNA and thus its competition for PHD finger binding.

### Modification or mutation of the H3 tail weakens binding to DNA

Our results show that the H3 tail is stabilized on the nucleosomal DNA through multiple contacts along the entire length of the tail. Given this, it is possible that a variety of PTMs may alter this interaction and thus the H3 tail conformation and accessibility. Notably, our results reveal that H3K4me3 does not significantly alter the H3 tail-DNA interactions (discussed above, Figure 5), which is likely due to the fact that methylation of lysine does not alter the side-chain charge. However, there are a number of PTMs, such as lysine acetylation and other acylations, arginine citrullination, and serine/threonine/tyrosine phosphorylation, that alter the side-chain charge of histone residues and thus might perturb the electrostatic interaction between the histone tails and nucleosomal DNA.

Acetylation neutralizes the positive charge on the lysine side-chain. To investigate how acetylation along the H3 tail alters the tail-DNA interaction we conducted MD simulations of NCPs containing acetylation on lysines 14, 18, 23, and 27 along the H3 tail (quadAc-NCP) (Figure 7—figure supplement 1). Interestingly, the H3 tails in the quadAc-NCP compact to a similar extent as in the un-NCP and H3K4me3-NCP, with an Rg of 26.5 ± 0.4 Å for H3 (Table 1). Also, similar to the un-NCP and H3K4me3-NCP the quadAc-H3 tails compact primarily onto the nucleosomal DNA (Figure 7A, Video 3). The quadAc-H3 tail shows no change in secondary structure, with an average helicity of 5.9% and an average β-strand content of 3.3% (Figure 5—figure supplement 1, Table 1). However, the interaction energies between the DNA and H3 tail are significantly weakened (ΔG = −52.1 + /- 2.7 kcal/mol, p-value of 0.0003) in the quadAc-NCP (Figure 7B, Table 1). This is in-line with previous studies using UV-induced laser-crosslinking, in which it was proposed that the histone tail-DNA interaction persists even upon acetylation, but is weakened (Mutskov et al., 1998). We note that the acetylated lysines only account for 33% of the total change in free energy (6.2 kcal/mol of the total 18.9 kcal/mol disfavorable shift), while the immediate neighbors of the acetylated lysines combine to contribute an additional 37% of the difference (6.9 kcal/mol). Other residues that experience significant drops in binding strength include A1 (ΔΔG = 1.7 kcal/mol, 9% of total), K4 (ΔΔG = 1.8 kcal/mol, 9% of total), and S10 (ΔΔG = 0.9 kcal/mol, 5% of total). Additionally, the average amount of solvent-exposed surface area of the H3 tails is increased in the quadAc-NCP to 2928 ± 42 Å2 (Table 1), in part due to the increased size of the acetylated side chains. This increase in solvent-accessibility may provide a larger site for interaction with binding partners. Together, these results show that acetylation of lysines 14, 18, 23, and 27 reduce the strength of H3 tail interactions with DNA by removing not only direct interactions formed by these residues, but also by consequentially weakening the interactions of neighboring cationic and polar residues with the DNA.

![Figure 7.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-v2.jpg)

**Figure 7.:** (A) Three-dimensional probability distribution of the locations of heavy atoms within H3 N-terminal tails for the quadAc-NCP (left) and H3K4me3/3xR-A-NCP (right) simulations, superimposed upon the crystal structure (PDBID 1KX5). Histones are shown in gold and DNA in blue. Darker regions represent areas of higher probability, and lighter regions depict areas of lower probability. (B) MM-GBSA analysis of the per-residue contributions to DNA binding of H3 N-terminal tail residues in the unmodified (gold), quadAc (dark purple), and 4xK-Q (lavender) NCP simulations. (C) MM-GBSA analysis of the per-residue contributions to DNA binding of H3 N-terminal tail residues in the H3K4me3 (raspberry), H3K4me3/4xK-Q (lavender), and H3K4me3/3xR-A (dark green) NCP simulations.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Radius of gyration timeseries for the quadAc-NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Radius of gyration timeseries for the H3K4me3/3xR-A-NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Percentage of simulation frames where each residue is in β-sheet (blue), α-helix (green), turn (purple), or random coil (grey) configurations. For each residue, results are shown for (left to right): H3K4me3-NCP, H3K4me3/4xK-Q-NCP. H3K4me3/3xR-A-NCP. Locations of mutations are identified by ‘*”. Every residue was in a random coil configuration in over 50% of simulated frames, regardless of chemical composition.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** Radius of gyration timeseries for the 4xK-Q-NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp5-v2.jpg)

**Figure 7—figure supplement 5.:** Radius of gyration timeseries for the H3K4me3/4xK-Q-NCP initialized in the (A) 1KX5, (B) linear, and (C) MODELLER-predicted tail conformations. Plots are separated between the 1KX5 nomenclature of the two H3 chains, A-chain (left) and E-chain (right).

![Figure 7—figure supplement 6.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp6-v2.jpg)

**Figure 7—figure supplement 6.:** Three-dimensional probability distribution of the locations of heavy atoms within H3 N-terminal tails for the 4XK-Q-NCP (top) and H3K4me3/4xK-Q-NCP (bottom) simulations, superimposed upon the crystal structure (PDBID 1KX5). Histones are shown in gold and DNA in blue. Darker regions represent areas of higher probability, and lighter regions depict areas of lower probability.

![Figure 7—figure supplement 7.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig7-figsupp7-v2.jpg)

**Figure 7—figure supplement 7.:** Comparison of solvent-accessible surface area of modified/mutated lysine residues within quadAc- and 4xK-Q-NCP.

![Video 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-video3.mp4.jpg)

**Video 3.:** Protein backbone arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

While results show that neutralization of lysines substantially weakens tail-DNA binding, simulations also reveal that interactions between arginines and DNA provide the largest individual residue contributions. To probe the effects of arginine neutralization, we conducted simulations of modified NCPs where the arginine residues that are not implicated in PHD binding (R8, R17, and R26) were mutated to alanine in the presence of K4me3 (H3K4me3/3xR-A-NCP). As was seen with acetylation of lysine, the H3 tails in these simulations compacted to a similar extent as was seen for the unmodified NCP (H3 Rg = 25.4 + /- 0.3 Å), though notably, they collapsed at a slower rate than the other NCPs (Figure 7—figure supplement 2). The H3K4me3/3xR-A tails occupy a similar volume of the DNA surface as compared to K4me3 alone (Figure 7A, right vs. Figure 5B, Video 4). There was a small increase in the average helical content (Table 1), however each residue was still disordered in over 50% of the simulations (Figure 7—figure supplement 3). In comparison to the unmodified NCP, the mutated tails have a decreased level of solvent exposed surface area (2534 ± 39 Å2), largely due to the decreased size of the alanine side-chain. Most notably, however, is that the strength of DNA binding by the mutated tail is the lowest of all NCPs tested (ΔG = −45.1 + /- 2.7 kcal/mol), and this decrease in interaction strength can be almost entirely attributed directly to the alanine mutations (Figure 7C), with contributions from neighboring lysines only modestly affected by the mutations. This is in stark contrast to the quadAc-NCP, which displayed a correlation between PTMs at lysine sites and a reduced interaction strength of neighboring residues with the nucleosomal DNA.

![Video 4.](https://cdn.elifesciences.org/articles/31481/elife-31481-video4.mp4.jpg)

**Video 4.:** Protein arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

Together this reveals that mutation or modification along the H3 tail weakens, but does not abolish, the H3 tail interaction with DNA, which is mediated by a number of contacts along the tail. This suggests that modifications outside of an effector domain binding site might alter accessibility to interaction with an effector domain, mediating cross-talk between PTMs.

### Modification and mutation of the H3 tail increase accessibility to the PHD finger

To determine if these mutations and modifications increase accessibility for PHD finger binding, we used NMR. Specifically, we tested PHD finger binding to three distinct H3KC4me3-NCPs: one in which R8, R17, and R26 were mutated to alanine (H3KC4me3/3xR-A-NCP), one in which K14, K18, K23, and K27 were mutated to glutamine (H3KC4me3/4xK-Q-NCP), and one in which S10 and S28 were phosphorylated using Aurora B kinase (H3KC4me3/phos-NCP). Note that glutamine is a commonly used acetyl-lysine mimetic because the polar side chain of glutamine mimics that of the neutralized lysine. To confirm the validity of this mimic, we compared the simulations of NCPs containing acetylated lysine with those containing glutamine at the same positions (with and without K4me3) and found that they were in good agreement with one another for the Rg value for H3, secondary structure, and interaction energy with DNA (Figure 7—figure supplements 4–6, Videos 5 and 6). The only difference was in the solvent exposed surface area, but this is entirely accounted for by the acetylated lysine being physically larger than its glutamine counterpart (Figure 7—figure supplement 7).

![Video 5.](https://cdn.elifesciences.org/articles/31481/elife-31481-video5.mp4.jpg)

**Video 5.:** Protein backbone arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

![Video 6.](https://cdn.elifesciences.org/articles/31481/elife-31481-video6.mp4.jpg)

**Video 6.:** Protein arrangement is shown in dark blue, while sidechains are represented as orange sticks. Sidechains interact with both DNA backbones (cyan and turquoise), as well as within both the major and minor grooves (grey), through a variety of conformations.

Sequential 1H-15N HSQC spectra were recorded on 15N-PHD upon titration of H3KC4me3/4xK-Q-, H3KC4me3/3xR-A-, or H3KC4me3/phos-NCP (Figure 8A, and Figure 8—figure supplement 1–3). Compared to titration of H3KC4me3-NCP containing no additional modifications, the same set of residues is perturbed, and the resonances track along the same trajectories. However, at equivalent concentrations of NCP, PHD finger resonances have progressed farther towards the H3KC4me3-Tail-bound state in binding to H3KC4me3/4xK-Q-, H3KC4me3/3xR-A-, and H3KC4me3/phos-NCP as compared to binding to H3KC4me3-NCP. This indicates that the PHD finger is binding the H3 tail with the same molecular mechanism between all NCP samples, but that when additional tail residues are modified or mutated, the observed binding affinity is higher. Failure to reach saturation precludes the ability to determine exact Kd values; however, plotting the CSPs as a function of concentration of the H3KC4me3 mark indicates that the binding trends in the order of the weakest to tightest binding to H3KC4me3-NCP, followed by H3KC4me3/4xK-Q- and H3KC4me3/phos-NCP, with the tightest binding to H3KC4me3/3xR-A-NCP (Figure 8B, Figure 8—figure supplement 4). Thus, neutralizing the charge of basic residues or introducing negative charges results in an increase in accessibility to PHD finger binding. This is consistent with the smaller computed binding energy observed between the H3 tail and nucleosomal DNA in the MD simulations of H3K4me3/quadAc-, H3K4me3/4xK-Q- and H3K4me3/3xR-A-NCP (see above), and the computed binding energies trend in the same order as the experimental data (see Table 1). Neutralization of arginine appears to have a greater effect than neutralization of lysine, especially when taking into account that only 3 arginine but four lysine residues were mutated. This is consistent with the computed greater favorable energetic contribution of the arginine than lysine residues (Figure 7C).

![Figure 8.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig8-v2.jpg)

**Figure 8.:** (A) Overlay of a region of the 1H-15N TROSY HSQC spectra of 50 μM 15N-BPTF PHD upon titration of H3KC4me3-NCP containing no additional modifications, four lysine mutated to glutamine as acetyl-lysine mimetics, three arginine mutated to alanine, or phosphorylated serine on the H3 tail. Spectra are color-coded according to ligand concentration, with apo spectra in black and shades of salmon for increasing concentrations of ligand. Spectra were collected at molar ratios (PHD:H3KC4me3 mark) of 1:0, 1:0.2, 1:0.5, 1:1, 1:2 and 1:4 and additionally 1:6, 1:5.5, and 1:5.4 for H3KC4me3-, H3KC4me3/4xK-Q-, and H3KC4me3/3xR-A-NCP. Dashed, grey arrows track the trajectory between the apo and bound states for the H3KC4me3-Tail titration and are shown as visual aids for titrations with NCP, which are predicted to have the same end state. (B) CSPs (Δδ) are plotted for each H3KC4me3-NCP titration in (A) for the representative residue R2887 as a function of the concentration of the H3KC4me3 mark. The H3KC4me3-Tail titration is plotted for comparison.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** The full titrations from Figure 9 are shown for H3KC4me3/4xK-Q-NCP (A), H3KC4me3/3xR-A-NCP (B), and H3KC4me3/phos-NCP (C). The coloring guide is displayed on the spectra. Note that the ligand ratios are listed with respect to NCP concentration in this figure but the concentration of the H3KC4me3 mark in the main text figures.

![Figure 8—figure supplement 2.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig8-figsupp2-v2.jpg)

**Figure 8—figure supplement 2.:** ESI mass spectrometry data is shown for unmodified and alkylated versions of histone H3 to confirm the lack of carbamylation and the proper alkylation for the MLA. The constructs are: unalkylated and alkylated H3K4C/4xK-Q (A,B), unalkylated and alkylated H3K4C/3xR-A (C,D), 15N-H3 (E), and 15N-H3K4C (F).

![Figure 8—figure supplement 3.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig8-figsupp3-v2.jpg)

**Figure 8—figure supplement 3.:** (A) A representative 18% SDS-PAGE gel on NCP samples is shown. The 18% tris gel was run in Tris/glycine/SDS running buffer. Spectra Multicolor Broad Range Protein Ladder (ThermoFisher Scientific) was run alongside NCP samples. The histones are labeled. The H3KC4me3/4xK-Q and H3KC4me3/3xR-A histone mutants migrate faster on the gel (likely due to the change in charge composition) and are not resolved from H2A. A small amount of high molecular weight contaminants from the histone preps is visible and marked (*). Additionally, a representative 5% 75:1 acrylamide/bisacrylamide native gel run is shown. The gel was made and run in 0.2x TBE with TrackIt 100 bp DNA ladder (ThermoFisher Scientific) for reference. The gel was run on ice for 50 min at 125V and visualized via ethidium bromide staining. The NCP prepared with different H3 mutants and modifications are not distinguishable under these conditions. A small amount of free 601 DNA (which stains better than DNA within NCP) always remains after the sucrose gradient purification. (B). Native gels run on different NCP samples before and after NMR titrations show that the NCP remains intact over the course of the experiments. Note that different amounts of NCP were loaded on the left-most gel. Equal amounts of NCP were loaded before and after the NMR titration for the unmodified NCP (center gel). A denaturing gel run with the unmodified NCP shows that the histones were not degraded over the course of the NMR titration. (C). An 18% SDS-PAGE gel was prepared with 50 μM Zn2+-Phos-tag acrylamide AAL-107 in order to assess the degree of phosphorylation by AurB. The Spectra BR ladder is simply provided for reference; proteins are known to run slower and differently using Phos-tag acrylamide such that molecular weight estimation is no longer possible. The Phos-tag gel appears to smear and accentuate the high molecular contaminants (*), which might also be due to the 601 DNA present in the sample and running at a similar position as the contaminants. See the comparison with the standard 18% SDS-PAGE gel in (A). The gel indicates that the majority of the H3 component was phosphorylated by AurB in the H3KC4me3/S10ph/S28ph-NCP sample. The different NCP samples are numbered as shown in the legend.

![Figure 8—figure supplement 4.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig8-figsupp4-v2.jpg)

**Figure 8—figure supplement 4.:** CSPs (Δδ) are plotted as a function of the concentration of H3KC4me3 mark for the titrations of H3KC4me3-NCP (raspberry diamonds), H3KC4me3/4xK-Q-NCP (lavender triangles), H3KC4me3/3xR-A-NCP (dark green squares), and H3KC4me3/S10ph/S28ph-NCP (black circles) into 15N-BPTF PHD shown in Figure 9 and Figure 8 and Figure 8—figure supplement 1. The plots show that the trend in binding holds for all 13 significantly perturbed residues.

It is clear that altering the charge of several H3 tail residues is not sufficient to fully release the H3 tail from the nucleosomal DNA and recover the full binding potential of the PHD finger-H3KC4me3 interaction. This further supports that many contacts along the length of the tail, albeit dominated by the basic residues, are involved in a high avidity interaction with the nucleosomal DNA.

## Discussion

In this study, we find that the nucleosome inhibits binding of the BPTF PHD finger to the methylated histone H3 tail. This adds to a growing body of evidence that the nucleosome context can have a significant effect on chromatin signaling events, including histone tail binding and modification (Stützer et al., 2016; Wang and Hayes, 2007; Munari et al., 2012; Gatchalian et al., 2017). We show that inhibition of PHD finger binding is due to the conformation of the tail in the context of the nucleosome core particle. Our data indicate a robust, but conformationally heterogeneous interaction of the H3 tail with the nucleosome core, driven by contacts with DNA (Figure 9A). The interaction with DNA is competitive with respect to PHD finger binding. As this collapsed conformation is favored under physiological conditions, this inhibits association of the PHD finger with the H3 tail in the context of the nucleosome (Figure 9B).

![Figure 9.](https://cdn.elifesciences.org/articles/31481/elife-31481-fig9-v2.jpg)

**Figure 9.:** (A) Conglomeration of histone tail conformations (gold) from all simulations of the unmodified NCP compacted upon the core DNA surface (blue). (B) Cartoon model depicting the simplified linked equilibria between the collapsed, autoinhibited state (favored) and extended, accessible state that is permissive to PHD finger binding. The extended and collapsed states are ensembles of conformations as denoted by n, m, and m’. Note that each histone tail is likely in equilibrium between collapsed, partially extended, and extended conformations. We do not intend to indicate cooperativity between the equilibria of individual tails as this is unknown; distinct ensembles are depicted only for simplicity. We expect that the energetics of these ensembles may be perturbed by a number of nuclear factors, including histone PTMs. (C) The data provided predicts that higher order PTM crosstalk, or the modification of residues remote from the region directly recognized by the histone effector domain, can perturb the energetics of the system, thereby shifting the conformational pre-equilibrium and altering the observed binding affinity. Specifically, the neutralization of lysine or arginine side chains or the addition of negatively charged groups such as by phosphorylation of serine or threonine side chains result in a tighter observed binding affinity.

The classical model of the nucleosome depicts the tails as extended and accessible to binding. Indeed, the tails are highly susceptible to protease degradation and generally not resolved in crystal structures, and NMR data indicates substantial conformational dynamics within the tails (Zhou et al., 2012; Böhm and Crane-Robinson, 1984; Rosenberg et al., 1986; Luger et al., 1997; Gao et al., 2013). However, many biochemical and biophysical studies have also suggested that the histone tails interact with DNA and have an effect on nucleosome stability. Molecular dynamics studies also widely show that the histone tails collapse onto DNA during the course of a simulation (Li and Kono, 2016; Shaytan et al., 2016; Ikebe et al., 2016; Erler et al., 2014; Bowerman and Wereszczynski, 2016). Moreover, a CHIP-exo study suggests that the H3 tails associate with linker DNA in vivo (Rhee et al., 2014). Here we develop a model that is consistent with both (Figure 9B). We find that the H3 tails associate robustly with DNA in the context of the nucleosome, but with substantial conformational flexibility. Notably, DNA binding is independent of the presence of available linker DNA, as we find here that it also robustly associates with the core DNA. Our simulations reveal that there exists a plethora of energetically similar but structurally heterogeneous DNA-bound states of the H3 tail. Though simulations show that these binding modes remain highly stable up to the 100ns timescale, the fact that there is only a single peak observed for each residue by NMR suggests that movement between these collapsed conformations is fast on the NMR timescale. Fast exchange on the NMR timescale indicates dynamic transitions on the order of sub-microseconds. Movement between collapsed conformations could involve partially or fully released/extended conformations as intermediates or could take the form of a ‘tethered diffusion’ of the H3 tail along the surface of the core DNA.

Given current computing power, it is highly unlikely that individual MD simulations can rigorously sample a representative region of the H3 tail ensemble when bound to the NCP. These findings support previous studies, which showed that multiple trajectories must be collected and/or enhanced sampling approaches implemented in order to robustly simulate the bound state of the H3 tails (Li and Kono, 2016), and that caution should be exercised when drawing conclusions regarding the role of the tails in NCP stability and dynamics. The equilibrium of states is likely determined by a balance of the extended and collapsed modes, the former of which is driven by conformational entropy and the latter of which is driven by the enthalpy of tail-DNA interactions. At first glance, it may seem that the extended state should dominate due to its high flexibility and inherently large entropy. However, our results suggest that the collapsed tail state is actually more favorable. Specifically, our MM-GBSA calculations indicate that there is a significant enthalpic advantage to compacted configurations due to strong Coulomb interactions that overwhelm the loss of configurational entropy upon tail collapse. Furthermore, the large variability in compacted tail configurations observed in our simulation trajectories suggests that the collapsed state likely has a significant configurational entropy of its own, which may also alleviate some of the entropic cost of compaction.

Our results align with a recent study by Stützer et al., 2016. on the X. laevis 187bp-nucleosome. Similar to what we show here with inhibition of PHD finger binding, they found that acetylation and methylation of the H3 tail by a subset of histone acetyltransferases (Gcn5, p300, CBP) and methyltransferases (G9a, PRC2, PRMT5, Set7/9), respectively, is inhibited by the nucleosome. Using NMR, they determined this to be due to a transient interaction of the tail with linker DNA. We suggest a robust yet dynamic interaction not only with linker DNA but also with DNA in the nucleosome core. It is likely that all histone tails are associated in some manner with nucleosomal DNA. An NMR analysis of the histone H4 tail found that the small basic patch within the tail (residues 16–20) is associated with the nucleosome core, as evidenced by the complete lack of signal in an 1H-15N HSQC (Zhou et al., 2012). The contrast to observable signals for H3 could represent either a different exchange regime between states or even a single stable state for the H4 tail, as suggested by a recent computational study (Erler et al., 2014). In addition, a number of biochemical studies have shown through chemical reactivity and cross-linking that the N- and C-terminal tails are associated with the nucleosome core (for a review see [Pepenella et al., 2014]). This collapsed conformation presents a much more complex binding interface to histone effector domains than would an extended tail, and many effectors will likely be inhibited as seen here with the BPTF PHD finger. In fact, studies of fluorescein 5-maleimide reactivity towards single cysteine mutants of the H2B tail in the context of the nucleosome suggest that effector domain binding should be 10- to 50-fold weaker than binding to an H2B tail peptide (Wang and Hayes, 2007). A modest decrease in binding to the H3K9me3-NCP as compared to peptide was also observed for the chromodomain containing HP1β (Munari et al., 2012). This nucleosomal inhibition is less than that observed here for the BPTF PHD finger, but regions flanking the chromodomain are thought to interact with DNA, which could somewhat counter the inhibition. Another recent study reported on binding of the tandem CHD4 PHD fingers to the histone H3 tail unmodified at lysine 443. Similar to our results, the individual CHD4 PHD fingers bound too weakly to the NCP to accurately measure binding affinity. Though the linked PHD fingers also bound more weakly to the nucleosome than to histone peptides, there was only a ~ 6 × difference in affinity (Gatchalian et al., 2017). The increase in affinity for the dual domain as compared to the individual PHD fingers is purportedly due to the multivalent activity of the tandem PHD fingers as well as contributions to histone binding by the region linking the two PHD fingers (Gatchalian et al., 2017).

There are many mechanisms by which the inhibitory conformations of the histone tails could be regulated. We show here that neutralization of lysine or arginine along the H3 tail, as occurs with several types of lysine acylation and arginine citrullination, weakens the association with DNA and promotes PHD finger binding. We also observe an increase of binding upon phosphorylation of serine. This is in agreement with recent studies showing that acetylation or phosphorylation of H3 tails promotes subsequent additional modification of the H3 tail (Stützer et al., 2016). Notably, there are many additional modifications including ADP-ribosylation and certain acylations that not only neutralize lysine, but add negative charge to the side-chain. In addition, modification by the small proteins ubiquitin and SUMO would likely lead to large steric hindrance. This suggests that cross-talk between histone PTMs is not only mediated through effector domains themselves (i.e. recognition of multiple PTMs by multiple domains, or antagonism between neighboring PTMs by direct inhibition of binding) but can also be mediated by the integrated effects of PTM recognition and nucleosome structure (Figure 9C). It is also possible that DNA-binding domains could displace the histone tail and increase accessibility. There are now several examples of histone effector domains that also harbor DNA-binding ability and have been found to bind tighter to nucleosomes than to histone peptides alone (Charier et al., 2004; Kim et al., 2010; Qiu et al., 2012; Eidahl et al., 2013; Musselman et al., 2013; van Nuland et al., 2013; Savitsky et al., 2016; Miller et al., 2016; Morrison et al., 2017). This could result from a combination of additional contacts with the nucleosome and displacement of the histone tail. A similar effect could be seen with adjacent DNA binding domains as suggested previously (Pilotto et al., 2015).

Altogether our data not only supports a model of the nucleosome where the tails are collapsed rather than extended, but also suggests many higher order regulatory mechanisms within chromatin signaling cascades, and highlights the importance of understanding the molecular mechanism of effector complexes at the nucleosome.

## Materials and methods

### BPTF PHD finger construct

A codon optimized BPTF PHD finger gene fragment (residues 2865–2924 of UniProt entry Q12830) was obtained from Integrated DNA Technologies (IDT, Coralville, IA) and cloned into the pDEST15 vector using Invitrogen Gateway recombination cloning technology (ThermoFisher Scientific, Waltham, MA) with an engineered N-terminal PreScission Protease cleavage site.

BL21 (DE3) Chemically Competent E. coli (ThermoFisher Scientific or New England Biolabs, Ipswich, MA) were used for expression. E. coli was grown in LB media or M9 minimal media supplemented with vitamin (Centrum, New York City, NY), 1 g L-1 15NH4Cl, and 5 g L−1 D-glucose to produce unlabelled or 15N-isotopically enriched protein, respectively. Media was supplemented with 100–200 μM ZnCl2. Bacteria was grown to an OD600 ~1.0 and induced with 0.3 mM IPTG at 18°C for 16–20 hr.

For purification of the GST-fusion PHD finger, cells were lysed in 20 mM Tris pH 7.5, 500 mM NaCl, 3 mM DTT, 0.5% Triton X-100, 0.5 mg mL−1 lysozyme with DNaseI and Pierce EDTA-free Protease Inhibitor Tablets (ThermoFisher Scientific) using an Avestin (Canada) EmulsiFlex or sonication. The soluble portion of the lysate was incubated with glutathione agarose resin (ThermoFisher Scientific) and washed extensively with buffer (20 mM MOPS pH 7.0, 150 mM KCl, 1 mM DTT). Samples were cleaved from the GST tag overnight with PreScission Protease and further purified using anion exchange (Source 15Q, GE Healthcare Life Sciences, Pittsburgh, PA) and size exclusion chromatography (Superdex 75 10/300, GE Healthcare Life Sciences). The final buffer for all samples was 20 mM MOPS pH 7.0, 150 mM KCl, and 1 mM DTT. Note that 20 mM MOPS buffers were adjusted to pH 7 by adding 7 mM NaOH. The concentrations of PHD finger samples were determined via UV-vis spectroscopy using the absorbance (calculated ε280 = 12,950 M−1cm−1).

### Histone purification and NCP reconstitution

Unmodified human histones (H2A.1 uniprot accession P0C0S8, H2B.1C uniprot accession P62807, H4 uniprot accession P62805 with T71C) were expressed out of pET3a vectors. A codon-optimized version of H3.2 (uniprot accession Q71DI3) was obtained from IDT and cloned into pET3a. Codon and non codon-optimized versions of H3 were made with a cysteine-free background (C110A), and the non codon-optimized version also carries the common G102A mutation. The Q5 mutagenesis kit (New England Biolabs) was used to introduce additional mutations. The H3 mutants generated were: 1) K4C, 2) K4C/K14Q/K18Q/K23Q/K27Q (referred to as H3K4C/4xK-Q), and 3) K4C/R8A/R17A/R26A (referred to as H3K4C/3xR-A). The K4C mutation was made to the non codon-optimized H3 and the K4C/K14Q/K18Q/K23Q/K27Q and K4C/R8A/R17A/R26A mutations were made to the codon-optimized H3. Rosetta 2 (DE3) pLysS (Novagen, Burlington, MA) or BL21 (DE3) (New England Biolabs) chemically competent E. coli were used for expression. Unlabelled growths were carried out in either LB or M9 media and were induced at OD600 ~ 0.4 with 0.2 mM (for H4) or 0.4 mM (for H2A, H2B, and H3) IPTG for 3–4 hr. 15N- and 13C/15N-isotopically enriched H3 was grown in M9 minimal media supplemented with vitamin (Centrum), 1 g L-1 15NH4Cl, and 5 g L−1 unlabelled or 3 g L-1 13C D-glucose. Histones were extracted from inclusion bodies following (Qiu et al., 2012) and purified via ion exchange chromatography.

The trimethyl lysine analogue was installed using alkylation of H3K4C following (Simon, 2010). Briefly, H3K4C was dissolved at 10 mg/mL in alkylation buffer (4M guanidine hydrochloride, 1M HEPES pH 7.8, 10 mM DL-methionine) with 20 mM fresh DTT by incubating at 37°C for 1 hr. (2-Bromoethyl) trimethyl ammonium bromide was added as the alkylating agent at 100 mg/mL and incubated at 50°C for 2.5 hr. An additional 10 mM of fresh DTT was added, followed by another 2.5 hr incubation. Each 1 mL reaction was quenched with 50 μL β-mercaptoethanol, and H3KC4me3 was de-salted using a PD10 column (GE Healthcare Life Sciences) and dialyzed against 2 mM β-mercaptoethanol in H2O.

Unmodified, H3KC4me3, H3KC4me3/4xK-Q, and H3KC4me3/3xR-A octamers were prepared as described in (Qiu et al., 2012). Briefly, equimolar ratios of histones were mixed in 20 mM Tris pH 7.5, 6M Guanidine HCl, 10 mM DTT, dialyzed into 20 mM Tris pH 7.5, 2M KCl, 1 mM EDTA, 5 mM β-ME, and purified over a sephacryl S-200 column (GE Healthcare Life Sciences) via FPLC.

A plasmid containing 32 repeats of the 147 bp Widom 601 sequence (ATCGAGAATCCCGGTGCCGAGGCCGCTCAATTGGTCGTAGACAGCTCTAGCACCGCTTAAACGCACGTACGCGCTGTCCCCCGCGTTTTAACCGCCAAGGGGATTACTCCCTAGTCTCCAGGCACGTGTCAGATATATACATCCGAT) was amplified in E. coli and purified via alkyline lysis methods, largely as outlined in (Qiu et al., 2012). The 601 repeats were released by cleavage with EcoRV and purified from parent plasmid by polyethylene glycol precipitation, and further purified over a source 15Q column (GE Healthcare Life Sciences) via FPLC.

Unmodified, H3KC4me3, H3KC4me3/4xK-Q, and H3KC4me3/3xR-A NCPs were reconstituted with the 147 bp Widom 601 sequence via desalting methods (Qiu et al., 2012). Briefly, octamer and 601 DNA were mixed at a 1:1 molar ratio and desalted using a linear gradient from 2M to 150 mM KCl over ~48 hr. NCPs were heat-shocked at 37°C for 30 min to obtain uniform positioning and then purified using a 10–40% sucrose gradient. Proper nucleosome formation was confirmed via native polyacrylamide gel electrophoresis and by the sucrose gradient profile.

Nucleosome concentrations were determined via UV-vis spectroscopy using the absorbance from the 601 DNA (calculated ε260 = 2,312,300.9 M−1cm−1). Before measuring the concentration, samples were diluted into 2M KCl in order to promote nucleosome disassembly for more accurate concentration determination.

In order to produce tailless NCPs (tlNCPs), reconstituted NCPs were treated with TPCK Trypsin immobilized on magnetic beads (Takara Bio, Japan). NCPs were incubated with the beads at room temperature for 30 min in 0.5xTE (which resulted in little digestion) and then for 70 min with 75 mM KCl (see Figure 3—figure supplement 2 for time points). The digestion and final sample resembled (Ausio et al., 1989).

The H3KC4me3-NCP sample was treated with Aurora B kinase in order to phosphorylate serine 10 and 28 on H3 (H3KC4me3/S10ph/S28ph-NCP, referred to as H3KC4me3/phos-NCP). After titrating the H3KC4me3-NCP sample into 15N-BPTF PHD, the H3KC4me3-NCP sample was recovered and ~1 mM EDTA was added to unfold the PHD finger. This recovered NCP was treated with recombinant human Aurora B (AurB) protein (abcam product ab51435, Cambridge, MA). The NCP was treated with 3 μg of AurB for 4.2 hr at 30°C (4.4 mM MgCl2, 0.6 mM EGTA, 0.7 mM EDTA, 1.5 mM β-glycerophosphate, 2 mM ATP, 0.6 mM benzamidine, 20 mM MOPS pH 7, 150 mM KCl, 0.7 mM DTT). Following the incubation, an additional 4 mM EDTA was added to chelate the free Mg2+. The treated NCP was separated from PHD finger and kinase reaction buffer components by purifying it over a Superdex 75 10/300 column (GE Healthcare Life Sciences). Phosphorylation of H3KC4me3 was confirmed via an 18% SDS-PAGE gel prepared using Zn2+-Phos-tag acrylamide AAL-107 (Wako Pure Chemical Industries, Japan, see Figure 8—figure supplement 3). The gel was prepared and run according to recommendation as outlined in the Wako Pure Chemical Industries manual for Zn2+-Phos-tag for SDS-PAGE using a neutral-pH buffer system, using 50 μM Zn2+-Phos-tag acrylamide AAL-107, including ZnCl2 at a final concentration of 0.3 mM in all gel samples (including the ladder and empty wells), and running the gel on ice.

### Histone peptides

The histone peptide H3(1–10)K4me3 was obtained from Anaspec (Fremont, CA). Concentrated peptide stocks were prepared in H2O based on the weight provided by the company. The pH of stock solutions was adjusted to pH ~7 with NaOH.

The H3(1–44) construct (ARTKQTARKS TGGKAPRKQL ATKAARKSAP ATGGVKKPHR YRPG) was expressed out of pET3a after inserting two stop codons (TAATAA) between codons for residues 44 and 45 into the pET3a plasmid containing codon-optimized H3 using the Q5 mutagenesis kit (New England Biolabs). This kit was also used to generate the K4C mutant. Unlabeled, 15N- or 13C/15N-isotopically enriched H3(1–44) or H3K4C(1-44) were expressed in BL21 (DE3) chemically competent E. coli (New England Biolabs) in the same manner as for the full length H3 (see above), except that cells were grown to OD600 ~1.0 prior to induction. To purify H3(1–44) constructs, cells were lysed in 50 mM Tris pH 7.5, 100 mM NaCl, 1 mM benzamidine, 2 mM EDTA, 0.5% Triton X-100, 0.5 mg mL−1 lysozyme with DnaseI and Pierce Protease Inhibitor Tablets (ThermoFisher Scientific) using an Avestin EmulsiFlex. The soluble portion of the lysate was purified using cation exchange resin and size exclusion chromatography (Superdex 30, GE Healthcare Life Sciences) in 50 mM KPi pH 7, 50 mM KCl, 0.5 mM EDTA. Samples were then desalted by purifying over a Superdex 75 column (GE Healthcare Life Sciences) and lyophilized. Final samples were prepared in 20 mM MOPS pH 7.0, 150 mM KCl, and 1 mM DTT (and with 1 mM EDTA for samples that would not be used with the BPTF PHD finger). Note that 20 mM MOPS buffers were adjusted to pH 7 by adding 7 mM NaOH. The H3(1–44) K4C sample was alkylated following the same protocol elaborated above for the full length H3K4C, and the proper alkylation (trimethyl lysine analogue) was confirmed via ESI mass spectrometry (see Figure 1—figure supplement 3). The concentrations of H3(1–44)KC4me3 stocks were determined via UV-vis spectroscopy using the absorbance from the native tyrosine Y41 (using the calculated ε280 = 1490 M−1cm−1).

### Mass spectrometry on histone samples

ESI mass spectrometry was used to analyze the full length H3 histones and histone tails, to confirm the removal of the N-terminal methionine, check that there was no carbamylation, and confirm proper alkylation of the MLAs. A Waters Q-Tof Premier instrument (Milford, MA) was used with positive electrospray ionization (ESI). Samples were diluted 1:2 or 1:4 in water/acetonitrile (1:1) with 0.1% formic acid. The acquisition and deconvolution software used during data collection and analysis were MassLynx and MaxEnt, respectively.

### DNA samples

Oligos for use in NMR studies were obtained from IDT with the following sequences: 5′-CTCAATTGGTCGTAGACAGCT-3’ and 5′-AGCTGTCTACGACCAATTGAG-3′. Double stranded oligos were annealed at a concentration of 350 μM by heating to 94°C for 10 min followed by a slow cooling to room temperature. The annealed duplexes were purified by size exclusion chromatography (Superdex 75 10/300, GE Healthcare Life Sciences) in NMR buffer (20 mM MOPS pH 7.0, 150 mM KCl, 1 mM DTT, and 1 mM EDTA in samples not used with the PHD finger) and concentrated. Concentration of DNA stocks was determined via UV-vis spectroscopy using the extinction coefficient predicted by the IDT Biophysics UV spectrum tool for duplex DNA at 260 nm (http://biophysics.idtdna.com/cgi-bin/uvCalculator.cgi), which is 333,804.5 M−1cm−1 for this DNA.

### NMR spectroscopy and data analysis with the BPTF PHD finger

Assignments for the BPTF PHD finger were transferred from (Li et al., 2006). Data was compared between buffer conditions and temperature titrations were performed to ensure proper transfer of assignments.

Titrations of H3 tail peptides and NCPs into 15N-PHD were carried out by collecting 1H-15N HSQC spectra on 15N-PHD in the apo state and with increasing concentrations of substrate, using TROSY with NCP substrates. 15N-PHD samples were at 50 μM in 20 mM MOPS pH 7, 150 mM KCl, 1 mM DTT, and 7% D2O. Titrations were collected at PHD:peptide ratios of 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, 1:5, and additionally 1:10 with H3(1–44)KC4me3. For titrations with H3 tail peptides pre-bound to DNA the peptide and DNA were mixed at a ratio of 1:2, and this stock was titrated into the 15N-PHD at the same PHD:peptide ratios (without the 1:0.1 point for H3(1–44)KC4me3). Titrations with H3KC4me3-, H3KC4me3/4xK-Q-, H3KC4me3/3xR-A-, and H3KC4me3/phos-NCP were collected at PHD:NCP ratios of 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, and 1:2 and additionally a final point at 1:3, 1:2.8, and 1:2.7 for H3KC4me3-, H3KC4me3/4xK-Q-, and H3KC4me3/3xR-A-NCP. The NCPs were stable over the course of all titrations, as supported by native gels (see Figure 8—figure supplement 3 for examples of gels). Data was collected at 37°C on an 800MHz Bruker (Billerica, MA) spectrometer with a cryogenic probe, collecting 24 scans for titrations with the H3 tail peptides and 32 scans for titrations with the NCPs.

Titration data were processed in NMRPipe (Delaglio et al., 1995) and analyzed using CcpNmr Analysis (Vranken et al., 2005). Binding curves were fit using a nonlinear least-squares analysis in Igor (Wavemetrics, Portland, OR) to a single-site binding model under ligand-depleted conditions:

$$
Δ\delta=Δ\delta_{max}(([L]+[P]+K_{d})−\sqrt{([L]+[P]+K_{d})^{2}−4[P][L]})/(2[P])
$$

where [P] is the concentration of protein, [L] is the concentration of histone peptide or DNA, Δδmax is the chemical shift difference at saturation. The combined chemical shift difference (Δδ) at each point in the titration is calculated by:

$$
Δ\delta=\sqrt{(Δ\delta_{H})^{2}+(0.154Δ\delta_{N})^{2}}
$$

where ΔδH and ΔδN are the changes in the 1H and 15N chemical shift, respectively, at each titration point with respect to the apo chemical shifts. Binding curves were fit using two independent variables (ligand and protein concentrations, to account for dilution) for residues that were significantly perturbed upon binding. Residues were determined to be significantly perturbed if the Δδ was larger than the average plus one-half standard deviation of the Δδ values for all residues. (The relatively low cutoff of one-half standard deviation was chosen for the PHD finger because the binding interface of such a small domain represents a relatively large portion of the domain.) Reported Kd values were determined by fitting Kd values for the significantly perturbed individual residues, calculating the average and standard deviation of the Kd values for these residues, and removing residues with fit Kd values not within the average ±two standard deviations (which was never more than a single residue). This resulted in using 14 residues for H3(1–44)KC4me3 and 15 residues for H3(1–44)KC4me3 pre-bound to DNA.

### NMR spectroscopy and data analysis with the H3 tail

Assignments on nucleosomes reconstituted using 167 or 187 bp 601 DNA have been published (Zhou et al., 2012; Stützer et al., 2016). We confirmed assignments with NCP reconstituted using 147 bp 601 DNA because assignments have not been published with this construct. To obtain backbone assignments for native H3 within the context of the NCP, HNCACB, CBCAcoNH, and HNCO spectra were collected on a 320 μM 13C/15N-H3-NCP sample (i.e. 640 μM of H3 component) using a 600MHz Varian spectrometer at 45°C. Data was processed in NMRPipe (Delaglio et al., 1995) and analyzed using CcpNMR Analysis (Vranken et al., 2005). The HNCACB and CBCAcoNH were collected with 32 and 24 scans, respectively, and 56 and 36 complex increments in the 13C- and 15N-dimensions, respectively. The HNCO was collected with 8 scans and 36 complex increments in both the 13C- and 15N-dimensions, respectively. Temperature titration was used to transfer assignments to 25°C and 37°C. 1H-15N HSQC spectra collected on an H3KC4me3-NCP sample were used to help confirm assignments of degenerate sections.

Backbone assignments were made for DNA-bound 13C/15N-H3(1–44). The DNA-bound state was chosen to resolve degeneracy observed in the apo state. Data was collected on a sample containing 1.1 mM 13C/15N-H3(1–44) and 1.4 mM DNA in 20 mM MOPS pH 7, 150 mM KCl, 1 mM EDTA, 8% D2O using a 500 Bruker spectrometer at 10°C. Assignments were made based on HNCACB (40 scans with 43 and 40 complex increments in the 13C- and 15N-dimensions, respectively) and HNcoCACB (8 scans with 40 complex increments in the 13C- and 15N-dimensions) spectra. Temperature and DNA titrations were used to transfer assignments between conditions.

1H-15N HSQC spectra were collected on 15N-H3(1–44) and 15N-H3-NCP samples at a range of KCl and MgCl2 concentrations and temperatures on an 800MHz Bruker spectrometer with cryogenic probe.

Titrations of 21 bp DNA (see above), NCP, and tlNCP into 15N-H3(1–44) were carried out by collecting sensitivity enhanced (SE) SOFAST 1H-15N HMQC spectra on 15N-H3(1–44) in the apo state and with increasing concentrations of substrate. Buffer conditions were 20 mM MOPS pH 7, 150 mM KCl, 1 mM DTT, and 1 mM EDTA. The DNA titration was repeated with 1 mM MgCl2 and no EDTA to test for the effect of Mg2+. Titrations were collected at H3(1–44):DNA ratios of 1:0, 1:0.1, 1:0.25, 1:0.5, 1:1, 1:2, and 1:4 and H3(1–44):NCP/tlNCP of roughly 1:0, 1:0.2, 1:0.5, 1:1, 1:2, and 1:3. The titrations were collected at 25°C on an 800MHz Bruker spectrometer with cryo probe.

Titration data were processed in NMRPipe (Delaglio et al., 1995) and analyzed using CcpNmr Analysis (Vranken et al., 2005). The composite chemical shift difference (Δδ) at each point in the titration is calculated by:

$$
Δ\delta=\sqrt{(Δ\delta_{H})^{2}+(0.154Δ\delta_{N})^{2}}
$$

where ΔδH and ΔδN are the changes in the 1H and 15N chemical shift, respectively, at each titration point with respect to the apo chemical shifts.

### Biolayer interferometry (BLI) data collection and analysis

An N-terminal biotin tag was added to the BPTF PHD finger for BLI experiments. The Q5 mutagenesis kit (New England Biolabs) was used to introduce an AviTag and an additional linker (GLNDIFEAQKIEWHEGSGS). The AviTag-PHD construct was grown and purified as described above, with the exception that this version of the BPTF PHD finger was not codon optimized and expression was done out of Rosetta 2(DE3)pLysS competent cells (Novagen). The AviTag-PHD construct was biotinylated in vivo by endogenous BirA (and confirmed via western blot, data not shown). Cells were grown in LB media, and 100 μM biotin was added at induction. All of the experiments were performed using biotin-PHD from a single protein prep so the population of biotinylated protein was constant between experiments.

Experiments were run using an Octet RED96 Biolayer Interferometry (BLI) System (Pall ForteBio, Menlo Park, CA). All samples were prepared in 20 mM MOPS pH 7, 150 mM KCl, 1 mM DTT, 0.2 mg/mL BSA (RPI albumin, bovine fraction V, molecular biology grade). Dip and Read Steptavidin Biosensors (Pall ForteBio) were used for all experiments and were hydrated in buffer for at least 30 min preceding data collection. Experiments were performed at 37°C in black 96-well plates (Greiner Bio-One, Monroe, NC), shaking at 1000 rpm. Data were collected at 10 Hz with a scheme of 10 min temperature pre-equilibration followed by 180 s buffer equilibration, 300 s biotin-PHD loading, 120 s buffer baseline, 300 s analyte association, and 300 s analyte dissociation steps. Two data sets were collected with H3(1–44)KC4me3 as analyte. For one of the data sets, double referencing was performed. This consisted of the standard single reference sensor that was loaded with biotin-PHD with the association phase performed using buffer alone and additionally a second set of sensors, not loaded with biotin-PHD, that were run through the same protocol for all analyte concentrations to test for optical property changes and non-specific binding. As no difference was observed between either referencing, the second data set was obtained with only the single reference of biotin-PHD against buffer. H3(1–44)KC4me3 analyte concentrations used were 20, 10, 5, 2.5, 1.3, and 0.6 μM, and the double referenced experiment additionally used 0.3 μM. Separate peptide dilutions were prepared for each experiment. Two data sets were also collected with H3KC4me3-NCP as analyte. Note that double referencing was needed for the NCP as a large offset in response signal was seen independent of the PHD finger, likely due to changes in the optical properties of the solution. H3KC4me3-NCP analyte concentrations used were 183, 21, and 10 μM for one experiment and 230, 23, and 11 μM for the other experiment.

Data were analyzed using the Octet Analysis software. Data were processed by subtracting the single or double reference data, aligning to the last 5–10 s of the baseline, and applying a Savitzky-Golay smoothing filter. Fast kinetics precluded the use of kinetic fits to determine binding affinity. Instead, equilibrium dissociation values were calculated by taking the average of the last 20 s of the association phase (req) and plotting this against the analyte concentration (x). This curve was fit to obtain the Kd value using a simple single-site binding equation:

$$
r_{eq}=r_{0}+r_{max}-r_{0}\frac{x}{K_{d}+x}
$$

Data were fit using a nonlinear least-squares analysis in Igor (Wavemetrics).

### Molecular dynamics simulations

Simulations of nucleosomes containing six modification states of the H3 tail were performed: an unmodified tail (denoted un-NCP), H3K4me3 (H3K4me3-NCP), and H3K14,18,23,27ac (quadAc-NCP), H3K14,18,23,27ac (4xK-Q-NCP), a combination of H3K4me3 and H3K14,18,23,27Q (H3K4me3/4xK-Q-NCP), and a combination of H3K4me3 and H3R8,17,26A (H3K4me3/3xR-A-NCP). For each system, NCP simulations were initiated from three different initial H3 tail conformations: one based on the 1KX5 crystal structure, one in which the H3 tails were extended linearly from residues 1 to 40, and one de novo structure predicted with the MODELLER software package (Shen and Sali, 2006). In the MODELLER calculations, a set of 25 possible H3 tail structures was created and used to construct a collection of 625 potential NCP models by substituting one of the 25 generated tail states for each copy of H3 in the 1KX5 NCP. These 625 conformations were then energy minimized in an implicit solvent environment (Onufriev et al., 2004), and the initial conformation used for simulations was taken as the one with the most favorable energetics for the un-NCP. In all systems, the missing three residues of H2B (1PEP3) were extended linearly from the histone N-terminus using tLeap. By considering each of these three H3 tail conformations, simulations were conducted on a total of nine different systems.

Protein and DNA parameters were based on the Amber14SB and bsc1 forcefields (Maier et al., 2015; Ivani et al., 2016), and PTM parameters were previously determined by Papamokos et al. (Papamokos et al., 2012). All systems were neutralized and solvated in a TIP3P solution of 150 mM KCl (Jorgensen et al., 1983; Joung and Cheatham, 2009). Heavy atom masses were repartitioned to their associated H atoms so that, in conjunction with SHAKE restraints, a four fs time-step could be used (Hopkins et al., 2015; Ryckaert et al., 1977). Simulations were conducted in the CUDA-enable pmemd engine (v16) (Salomon-Ferrer et al., 2013; Le Grand et al., 2013), and five separate simulations for each combination of NCP system and tail conformation were performed, for a total of ninety independent simulations. For each simulation, energy minimization was performed for 5000 steps with solute heavy atoms restrained by a 10 kcal/mol/Å2 harmonic potential, followed by 5000 steps with no restraints. Then, each simulation was heated from 10 K to 300 K over 50 ps in the NVT ensemble with the restraints reinstated. Next, the restraints were gradually released over 250 ps in the NPT ensemble, using a Monte Carlo barostat with a target pressure of 1 atm and a relaxation time of 3 ps. Temperature was regulated using a Langevin thermostat (Loncharich et al., 1992) with a collision frequency of 3.0 ps−1. Simulations were then conducted for 150 ns in the NPT ensemble with no restraints, yielding a cumulative sum of 13.5 µs of simulation time across all systems. Trajectories were recorded every 10 ps, and frames were visualized using VMD (Humphrey et al., 1996) and PyMol. Since 100 ns of simulation was required for the systems to equilibrate, only the last 50 ns of each simulation was used in the computational analysis (750 ns net for each NCP system).

### Simulation analysis

Interaction energies between the H3 tails and DNA in each system were determined from the sum of tail residue contributions to DNA binding according to an MM-GBSA (Molecular Mechanics Generalized Born Surface Area) analysis (Miller et al., 2012). Reported energies are the average of all results from each single simulation of a set (i.e., tail chemistry or initial tail conformation). Each tail within a simulation is considered a separate observation of the H3 tail ensemble, thereby producing two samples per simulation. Errors in the calculations are presented as the standard error of the mean from the simulation set, which corresponds to the standard deviations within the 10 samples of each initial tail conformation for a particular tail chemistry (a cumulative of 30 samples per tail chemistry).

Residue secondary structures were calculated using the DSSP algorithm (Kabsch and Sander, 1983), as implemented in cpptraj (Roe and Cheatham, 2013). For simplicity, secondary structures are reported as one of four categories: helix (DSSP types ‘G’, ‘H’, and ‘I’), sheet (‘E’, ‘B’), turn (‘T’), or unstructured coil (none of the above). Total tail helicity or sheet values are reported as the average over all tail residues of each residue’s percentage of frames in the respective structure. The global H3 tail structure was monitored through the radius of gyration (Rg) of the whole H3 histone such that reduced values in Rg can be directly interpreted as tail compaction upon the core. Furthermore, the 3-D coordinates of heavy atoms in the tails are visualized as average occupancy within a grid of 1.0 Å3 voxels, in a method similar to the counter-ion condensation observations made by Materese et al (Materese et al., 2009). Solvent exposure was calculated using the LPCO method, as implemented in cpptraj (Weiser et al., 1999). Lastly, a comparative analysis of the root mean square deviation (RMSD) of tail residues in the final frame of each simulation was conducted. In this analysis, translations and rotations were removed by least squares fitting the backbone of H3 core residues, and the subsequent RMSD values consider only the H3 tail residue backbone atoms.
