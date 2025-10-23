# The innate immune sensor IFI16 recognizes foreign DNA in the nucleus by scanning along the duplex

## Authors

- Sarah A Stratmann<sup>1</sup>
- Seamus R Morrone<sup>2</sup>
- Antoine M van Oijen<sup>1</sup> †
- Jungsan Sohn<sup>2</sup> †

### Affiliations

1. University of Groningen Groningen Netherlands
2. Johns Hopkins University School of Medicine Baltimore United States
3. University of Wollongong Wollongong Australia

† Corresponding author

## Abstract

10.7554/eLife.11721.001 The ability to recognize foreign double-stranded (ds)DNA of pathogenic origin in the intracellular environment is an essential defense mechanism of the human innate immune system. However, the molecular mechanisms underlying distinction between foreign DNA and host genomic material inside the nucleus are not understood. By combining biochemical assays and single-molecule techniques, we show that the nuclear innate immune sensor IFI16 one-dimensionally tracks long stretches of exposed foreign dsDNA to assemble into supramolecular signaling platforms. We also demonstrate that nucleosomes represent barriers that prevent IFI16 from targeting host DNA by directly interfering with these one-dimensional movements. This unique scanning-assisted assembly mechanism allows IFI16 to distinguish friend from foe and assemble into oligomers efficiently and selectively on foreign DNA. DOI: http://dx.doi.org/10.7554/eLife.11721.001

## Introduction

The host innate immune system detects infection by directly recognizing molecular signatures associated with pathogens (Janeway and Medzhitov, 2002; Medzhitov and Janeway, 2000). Remarkably, such signatures include universal building blocks of all life, such as DNA and RNA (Janeway and Medzhitov, 2002; Orzalli and Knipe, 2014; Paludan and Bowie, 2013). In the cytoplasm, the immune system relies on the absence of endogenous DNA, and thus marks all detected DNA as 'foreign' (nonself) (Orzalli and Knipe, 2014; Paludan and Bowie, 2013). However, DNA viruses often evade the cytosolic detection machineries, as their genomes are not exposed until reaching the nucleus (Orzalli and Knipe, 2014; Paludan and Bowie, 2013). The host counters this infection strategy in the nucleus by directly assembling supramolecular signaling platforms that trigger inflammatory responses on invading foreign DNA, but not on its own genomic material (Johnson et al., 2013; Li et al., 2012; Kerur et al., 2011). Although key players that target foreign dsDNA in the host nucleus have been identified (Orzalli and Knipe, 2014; Paludan and Bowie, 2013), the molecular mechanisms by which these sensors distinguish self from nonself dsDNA remain unknown.

The interferon-inducible protein 16 (IFI16) is a key innate immune sensor that detects foreign dsDNA and uses it as a scaffold to assemble supramolecular signaling platforms in both the host nucleus and cytoplasm (

![Figure 1.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig1-v2.jpg)

**Figure 1.:** (A) Top: IFI16 is composed of three functional domains flanked by unstructured linkers, namely one pyrin domain (PYD) and two dsDNA-binding Hin domains (HinA and HinB; Hin: hematopoietic interferon-inducible nuclear antigen). Bottom: IFI16 detects foreign dsDNA from invading pathogens in both the host nucleus and cytoplasm. (B) Top: a cartoon scheme for FRET experiments. The two differentially colored ovals represent fluorescently (Dylight-550 and Dylight-650) labeled IFI16. Bottom: The time-dependent changes in the emission ratio between FRET donor and acceptor labeled IFI16 (50 nM) were monitored at 33 µg/ml of each dsDNA (e.g. sixfold higher than the dissociation constant for 39-bp dsDNA [Morrone et al., 2014]). Lines are fits to a first-order exponential equation (see Figure 1—figure supplement 1 for 25 nM protein). All shown representative experiments were performed at least three times. (C) A plot of observed assembly rates (kassms) vs. dsDNA-sizes (see also Figure 1—figure supplement 1). (D) 1D-diffusion assisted assembly mechanism can explain the observed assembly profile of IFI16. 1. At the same mass-concentrations, the number of individual dsDNA fragments present in each assay is inversely proportional to the length of dsDNA. 2. Individual IFI16 molecules initially bind dsDNA at random positions and diffuse one-dimensionally while searching for other respective protomers; the number of IFI16 residing on the same dsDNA fragment should be proportional to the length of dsDNA (e.g. there are four times more individual 150-bp fragments than 600-bp fragments) 3. IFI16 fails to assemble into an oligomer on dsDNA shorter than 60 bp (indicated by a red arrow pointing left). The saturating rates can be explained if the final FRET signals arise from formation of distinct optimal oligomers.DOI: http://dx.doi.org/10.7554/eLife.11721.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Figure 1B.Shown is a representative of three experiments, and the calculated rates are listed in Supplementary file 1A.DOI: http://dx.doi.org/10.7554/eLife.11721.004

## Results and discussion

To identify the mechanisms underlying assembly of IFI16 signaling platforms on DNA, we monitored the oligomerization kinetics of FRET donor and acceptor labeled IFI16 on naked dsDNA (FRET: fluorescence resonance energy transfer; Figure 1B and Figure 1—figure supplement 1). Previous work demonstrated the existence of such oligomers and reported on their equilibrium binding properties but did not provide insights into the assembly mechanisms (Morrone et al., 2014). Using various dsDNA fragment sizes present in excess, we observe that the assembly rate increased non-linearly and by 50-fold from 60 to 200 bps dsDNA, above which it stayed constant (up to 600 bps; Figure 1B,C). With a dsDNA-binding footprint of ~15 bp for one IFI16 (Morrone et al., 2014), our results indicate that about 4 copies are required to initiate assembly, and about 10 IFI16 molecules are required for optimal oligomeric assembly (Figure 1C). Further, the assembly rate constants scaled linearly with the IFI16 concentration for all measured DNA lengths (Figure 1—figure supplement 1 and Supplementary file 1A), indicating that a purely cooperative assembly mechanism is unlikely. In line with this observation, previous work reported relatively small contributions of cooperativity in oligomerization with Hill constants near 2 for DNA substrates up to 2000 bp (Morrone et al., 2014).

Our ensemble-averaged, solution-phase observations of the faster assembly on longer dsDNA suggest a model in which IFI16 scans along dsDNA to increase the probability of encountering other IFI16 molecules (

![Figure 2.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig2-v2.jpg)

**Figure 2.:** (A) Illustration of the TIRF setup. λdsDNA is anchored to the pegylated coverslip surface by either one or two biotinylated oligonucleotide linkers. Single-biotinylated λdsDNA is constantly stretched by flow during measurements and used for the clustering and nucleosome experiments, whereas double-biotinylated λdsDNA is stably attached whilst being stretched and used without flow for single-molecule diffusion coefficient analysis. (B) Double-biotinylated λdsDNA is anchored to the surface and Cy5-labeled IFI16 molecules (800 pM) are visualized in near TIRF while bound to DNA. Top: Mean-square displacement (msd) trajectories are fitted within their linear regime to calculate the 1D-diffusion coefficient. Bottom: A sample kymograph of a single molecule stably bound for tens of second to DNA and exerting Brownian motion. (C) Elevated IFI16 concentrations result in clustering along λdsDNA. Top: A sample kymograph of multiple IFI16 molecules (3 nM) diffusing along λdsDNA. IFI16 molecules display a net motion along the flow direction. Bottom: Time-resolved clustering is accompanied by a decrease in diffusion coefficients and increase in the number of molecules per cluster. (D) The diffusion coefficient inversely correlates with the number of IFI16 per cluster, resulting in immobile, stable oligomers. (E) Cluster formation is IFI16-concentration dependent.DOI: http://dx.doi.org/10.7554/eLife.11721.006

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (i) IFI16: The median of D increases from 0.017 to 0.18 μm2s-1 with increasing ionic strength from 0.07 to 0.31 M concomitant with decreasing binding times to DNA. (ii) HinAB: The median increases from 0.010 to 0.027 μm2s-1 with increasing ionic strength from 0.07 to 0.017 M.DOI: http://dx.doi.org/10.7554/eLife.11721.007

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (Right) Intensities per particle are shown for 1 nM (single molecules) and 5 nM (clusters of IFI16). The mean particle intensity for single molecules serves as basis for calculating the number of IFI16 molecules within clusters (Figure 2—figure supplement 3).DOI: http://dx.doi.org/10.7554/eLife.11721.008

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Figure 2—figure supplement 2).The mean cluster size amounts to 8 IFI16 molecules within a cluster. Clusters are almost immobile, represented by a significant reduction in the diffusion coefficient D compared to that of single molecules of IFI16.DOI: http://dx.doi.org/10.7554/eLife.11721.009

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** (A) Constant flow (20 µl/min) is applied for the clustering experiments with elevated IFI16 concentrations, corresponding to a drag force of 1-2 fN on the DNA substrate and bound IFI16 molecules. The median measured diffusion coefficient D for single molecules increases from 0.026 µm2s-1 (no flow) to 0.031 µm2s-1 (with flow). (B) As described in the supplementary material, we calculated the drag velocity v on single molecules, with which we can define the effect of flow on D. Exemplarily shown here is a single diffusion trace, uncorrected and corrected for v. (C) Monte-Carlo simulation of IFI16 dimerization on λDNA that is occupied by varying amounts of 1D-diffusing IFI16s. The presence of a drag velocity v does not significantly alter the median search time.DOI: http://dx.doi.org/10.7554/eLife.11721.010

The 1D diffusion of IFI16 on dsDNA explains why the assembly rates increase with the DNA length in the bulk experiments (Figure 1C). With the longer dsDNA acting as an antenna, it allows binding of more IFI16 while 1D diffusion facilitates dynamic association (Figure 1D). The saturation of the assembly rate (Figure 1C) can be explained by the square dependence of the diffusional search time on length: at a sufficiently long dsDNA length, the dissociation rate of an individual IFI16 will be faster than the time needed to scan along the entire length of the DNA. In addition, longer DNA substrates work no longer as antennae, but as traps, since individual IFI16 molecules are farther apart and thus less likely to encounter one another (Hu et al., 2006; Turkin et al., 2015; 2016). Overall, the results of our bulk and single-molecule experiments are consistent with the dsDNA-size dependent binding in vitro(Morrone et al., 2014), which also correlates with the IFI16-induced inflammatory responses in vivo(Unterholzner et al., 2010). Thus, we propose that the 1D-diffusion mediated assembly plays a key role in regulating the overall IFI16-mediated immune responses.

It has long been speculated that chromatinization acts as the key feature that allows IFI16 to distinguish host from foreign DNA in the nucleus (

![Figure 3.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig3-v2.jpg)

**Figure 3.:** (A) A cartoon of di-nucleosome constructs with varying dsDNA-spacers. (B) Competition binding assays using IFI16 bound FAM-labeled 70-bp dsDNA against various di-nucleosomes and naked dsDNA. The lines are fits to: 1/(1+([DNAcompetitor]/IC50)^Hill constant), where IC50 indicates the concentration of competitor at 50% efficiency. The mass-concentration of each competitor was calculated using dsDNA, but not histones. (C) The time-dependent changes in the emission ratio between the FRET donor and acceptor labeled IFI16 (50 nM) were monitored at 33 µg/ml of each nucleosome or naked dsDNA. The lines are fits to a first-order exponential equation.DOI: http://dx.doi.org/10.7554/eLife.11721.012

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Purified dinucleosomes for the bulk FRET assays.DOI: http://dx.doi.org/10.7554/eLife.11721.013

To test whether the inhibitory effect of chromatin directly arises by interfering with the 1D diffusion of IFI16, we visualized the movement of individual IFI16 molecules on DNA with nucleosomes. We introduced randomly localized nucleosomes in λdsDNA using recombinant human histone octamers and tagged nucleosome positions with fluorescent antibodies against the N-terminal tail of histone H4 (

![Figure 4.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig4-v2.jpg)

**Figure 4.:** (A) Kymographs of Cy5-labeled IFI16 (magenta) binding to λdsDNA with varying numbers of nucleosomes tagged with anti-H4-Atto488 (blue). The number of nucleosomes per λdsDNA were estimated by quantifying IFI16 clustering sites for the lowest nucleosome/λdsDNA ratio (Figure 4—figure supplement 3C), yielding ~2 nucleosomes/ λdsDNA. At low nucleosome concentrations (~2 to 6 nucleosomes/DNA), IFI16 binds to λdsDNA and diffuses with the flow direction, until encountering a nucleosome. At higher concentrations (~20 nucleosomes per λdsDNA), individual IFI16 show only very short diffusive movements upon binding. (B) On naked λdsDNA, IFI16 travels with the flow to the free tip (top), whereas it oligomerizes along the path on nucleosome-loaded λdsDNA (bottom). (C) The overall travel distance of single IFI16 on nucleosome-loaded λdsDNA is reduced compared to bare λdsDNA (nucleosomal λdsDNA: N = 167, bare λdsDNA: N = 141).DOI: http://dx.doi.org/10.7554/eLife.11721.014

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** DOI: http://dx.doi.org/10.7554/eLife.11721.015

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** 601-nucleosomes do not provide sufficient exposed dsDNA for IFI16 binding, whereas on λdsDNA IFI16 molecules travel until encountering nucleosome obstacles.DOI: http://dx.doi.org/10.7554/eLife.11721.016

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/11721/elife-11721-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** (A) Example kymographs of IFI16-Cy5 on bare λdsDNA with long processivities to the free DNA tip and on nucleosomal λdsDNA with reduced run lengths. (B) Analysis of the number of IFI16 aggregation sites along DNA templates (including the free DNA tip) points to 1–3 nucleosomes per λdsDNA for the chosen reconstitution ratio DNA:histones, as it was used for run length measurements (Figure 4B,C).DOI: http://dx.doi.org/10.7554/eLife.11721.017

The molecular mechanism by which innate immune sensors distinguish self from foreign dsDNA in the host nucleus has been a major unresolved question in innate immunology (Kerur et al., 2011; Unterholzner and Bowie, 2011; Li et al., 2012; 2013; Orzalli et al., 2012; 2013; Johnson et al., 2014). The oligomerization of IFI16 on under-chromatinized foreign DNA plays a key role not only in initiating inflammatory and antiviral responses, (Monroe et al., 2014; Orzalli et al., 2012; Kerur et al., 2011), but also in regulating the hetero-chromatinization and silencing of viral dsDNA (Johnson et al., 2014; Orzalli et al., 2013). By using time-resolved bulk and single-molecule fluorescence assays, we demonstrate here that IFI16 ID scans along exposed dsDNA to assemble into distinct clusters and that chromatinization is sufficient to inhibit IFI16 from targeting host dsDNA for assembly. In vivo, this 1D scanning mechanism allows a limited number of IFI16 molecules to allocate each other on large genomes of invading pathogens. In combination with 3D sampling of binding sites on a collapsed DNA molecule, this process optimizes the oligomerization and downstream signaling time. While the clustering on dsDNA presents a tempting explanation for the role of IFI16 in viral gene silencing, future in vivo experiments await to test this. IFI16 belongs to the family of AIM2-like receptors, which include other nuclear and cytosolic foreign dsDNA-sensors. It will be interesting to determine whether and how these other related sensors use exposed dsDNA as a 1D 'digital ruler' to regulate their signaling platform assembly. This family of sensors is implicated in a number of autoimmune disorders (Mondini et al., 2007; 2010; Choubey et al., 2010; Gugliesi et al., 2013; Smith and Jefferies, 2014); how regulation of assembly is disrupted may provide insights into these afflictions.

## Materials and methods

## Protein expression and purification

Human full-length IFI16 and IFI16HinAB were cloned and expressed using E. coli T7 express cells (NEB) as a C-terminally His6-tagged protein as described in Morrone et al. (Morrone et al., 2014).

## DNA ligand preparation

dsDNA shorter than 90-bp were obtained from Integrated DNA Technologies (IDT) as described in Morrone et al. (Morrone et al., 2014). The complementary strands were dissolved and mixed in 1:1 molar ratio, melted at 95°C for 10 min, and the temperature was lowered to 25°C at a rate of 1°C/min. Ligands of greater length were obtained by polymerase-chain reaction (PCR) using the Maltose Binding Protein fusion tag cloning sequence as template and primers of appropriate sequence for a final length as indicated in the paper. Plasmids containing the Widom-601/603 sequence with indicated linker lengths were a kind gift of Dr. Gregory Bowman. The nucleosomal DNA was obtained by PCR from these constructs with appropriate primers. All substrates were gel-purified.

## Fluorescent labeling

DyLight-550, DyLight-650, or Cy5 fluorophore was incorporated to IFI16 using maleimide chemistry (purchased from Thermo Scientific and Invitrogen) and was performed as described in Morrone, et al. (Morrone et al., 2014). The label to protein ratio was ~ 1:1. Fluorescein-labeled dsDNA72 was obtained from IDT.

## Octamer refolding and nucleosome reconstitution

Lyophylized Xenopus laevis histones H1A, H2A, H3, and H4 were a kind gift of Dr. Cynthia Wolberger. Octamer refolding and nucleosome reconstitution was performed as described in Luger et al. (Luger et al., 1999), at a 2:1 molar ratio of octamer:DNA. An agarose gel of reconstituted nucleosomes is shown in Figure 3—figure supplement 1.

## Bulk biochemical assays

All absorption, fluorescence anisotropy, and fluorescence excitation/emission experiments were performed in a Tecan Infinite M1000. All experiments were performed at least three times and the fits to data were generated by Kaleidagraph software (synergy).

## Competition binding assays

All reactions were performed in 40 mM HEPES pH 7.4, 160 mM KCl, 5% glycerol, 1 mM EDTA, 0.1% triton-X-100, 5 mM DTT (Reaction Buffer). Here, 300 nM IFI16 and 4.5nM fluorescein-labeled dsVACV72 were incubated together at room temperature for 20 min. Increasing concentrations of competing DNA were added to the reaction to a final concentration of 100 nM IFI16 and 1.5 nM dsVACV72, and the changes in fluorescence anisotropy were recorded as indicated in Morrone et al. (Morrone et al., 2014).

## FRET time dependence assays

All reactions were performed in reaction buffer. 66 µg/ml of each dsDNA or di-nucleosomes was placed in the plate wells, and the reaction was initiated by adding an equivalent volume of IFI16-550 and IFI16-650 (1:1 molar ratio) to the indicated final concentration. The dead time between addition of IFI16 and the first measurement was 15-20 s. The final dsDNA molar-concentrations are at least sixfold higher than their determined binding constants by fluorescence anisotropy assays described in Morrone, et al. (Morrone et al., 2014), and the FRET ratio for each time point was calculated by dividing the acceptor emission (678 nm) by the donor emission (574 nm) (Morrone et al., 2014).

## Fluorescence microscopy assays

Microscope coverslips (Corning) were plasma-cleaned and activated with 100 mM KOH, silanized with 3-Aminopropyl-triethoxysilane in acetone and functionalized with PEG-NHS and biotin-PEG-NHS (Laysan-Bio) in sodium bicarbonate with a 1:3 mass ratio (Tanner and van Oijen, 2010). Streptavidin (Sigma Aldrich) was used for anchoring the biotinylated DNA substrates to the coverslip surface. Flow channels were constructed with custom-made PDMS chips to obtain dimensions of 10 mm length, 100 µm height, and 1 mm width, and connected to a syringe pump to allow constant flow during the measurements.

Single-molecule assays were performed in 40 mM HEPES (pH 7.4), 160 mM KCl, 1 mM EDTA, 2 mM DTT, 10% glycerol, 0.1% Triton-X100, 250 µg/ml BSA, 1 mM Trolox, 40 mM glucose, 250 nM glucose oxidase, 60 nM catalase, unless otherwise stated. All assays were performed at room temperature. We applied 100 nM YoPro-1 iodide (Life Technologies) at the end of the measurements to visualize the DNA substrates.

Reactions were illuminated with a 488-nm and 641-nm laser (Coherent), and images were acquired with an EMCCD camera (Hamamatsu). We used MetaVue imaging software (Molecular Devices) for data acquisition and ImageJ and R for analysis.

## λ-DNA templates for microscopy

Lambda-DNA (New England Biolabs) was biotinylated at one or both ends by ligation of the respective complementary biotinylated oligos according to Tanner et al. (Tanner and van Oijen, 2010) (oligo sequences are given in Supplementary file 1B; purchased from IDT). Single-biotinylated DNA templates were stretched by constant flow (20 µl/min) throughout the experiments (IFI16 clustering and nucleosome assays). Double-biotinylated DNA templates were applied to the flow cell at high flow velocity (100 µl/min). This allowed binding of the DNA to two biotin moieties, while the DNA was stretched. Free DNA was washed out, IFI16 applied to the flow cell, and flow was then stopped for acquisition of the single molecule diffusion traces.

To reconstitute nucleosomes, recombinant histone H2A/H2B dimers and H3/H4 tetramers (New England Biolabs) were assembled on biotin-λ-DNA and biotin-601 sequence (Epicypher) by salt-gradient dialysis (2 M to 0.3 mM NaCl in 5 steps, each step with an incubation time of at least 2 hr) in 10 mM Tris/HCl, pH 7.4, 0.1 mM EDTA, 0.5 mM DTT. We tested nucleosome reconstitution by an EMSA assay on digested λ-DNA (Figure 4—figure supplement 1). For this, we generated DNA fragments by digestion with EcoRI (NEB), purified them (Qiagen DNA spin columns) and reconstituted nucleosomes in the concentration ratios that we also used for full-length λ-DNA.

## Single molecule co-localization of IFI16 with nucleosomes tagged with antibodies

Antibodies against human histone H4 and H2B were chosen to target the N- terminal histone tails (Santa Cruz, sc-8657 and sc-8650), and labeled with Atto488-NHS (Life technologies) in PBS at pH 7.0. Labeled antibodies were negatively tested against bare DNA and Ifi16 clusters in the microscopy assay, and showed high specificity for nucleosomal DNA preparations only.

λ-DNA templates, loaded with nucleosomes and tagged with anti-H4, were constantly stretched in the flow channel. Ifi16 co-localized strongly with the nucleosome signal (Video 3, Figure 3—figure supplement 1). In contrast, biotinylated 601-sequence prepared with nucleosomes and tagged with anti-H4-Atto488, hardly showed co-localization with Ifi16, indicating, that there is not sufficient exposed dsDNA available for binding (Figure 4—figure supplement 2).

## Drift correction

For the clustering experiments, we applied a flow of 0.02 ml/min to our flow cell design of 0.1 mm height and 1 mm width, giving a volumetric flux of 0.33 cm/s. We expect the DNA molecules to be on average 0.2 µm away from the surface (Tafvizi et al., 2008), giving a velocity at this distance y of (Tafvizi et al., 2011):vy=32vavghy-y2h24=40 μm/s,   with   vavg=23vmax

The Stokes drag force that acts on the DNA and bound IFI16 molecules is then described by F=6πηrv1+9r16y=1.5fN,

with viscosity η, radius r and distance y.

We can define this force within the diffusion coefficient D by using the drift velocity v, calculated from single-molecule trajectories (Leith et al., 2012):with v=∑jall traj.xj,final-xj, initial∑jall traj.tj,final-xj, initial≈0.127 μm/s.

In order to evaluate the effect of flow on the clustering mechanism, we implemented a 1D-random walk Monte-Carlo simulation (Figure 2—figure supplement 4). Here, we calculated the expected search time for two IFI16 molecules (with D=0.026 µm2/s) to allocate each other on a λ-DNA molecule congested with a varying amount of other diffusing IFI16 molecules (10, 50, 100 molecules). As all particles are equal, we segmented the DNA according to the total number of molecules bound and calculated the effective distance between two particles by using the absolute distance modulo the segment length in order to take the periodic boundaries into account.

We allowed a maximum distance of 10 nm to consider two particles having met and dimerized. To simulate flow similar to our experimental conditions, to each random step the term vdt was added (The Python code is found in Source code 1).
