# Structural and functional properties of a magnesium transporter of the SLC11/NRAMP family

## Authors

- Karthik Ramanadane<sup>1</sup> ([ORCID: 0000-0001-7188-0250](https://orcid.org/0000-0001-7188-0250))
- Monique S Straub<sup>1</sup> ([ORCID: 0000-0002-7721-5048](https://orcid.org/0000-0002-7721-5048))
- Raimund Dutzler<sup>1</sup> ([ORCID: 0000-0002-2193-6129](https://orcid.org/0000-0002-2193-6129)) †
- Cristina Manatschal<sup>1</sup> ([ORCID: 0000-0002-4907-7303](https://orcid.org/0000-0002-4907-7303)) †

### Affiliations

1. Department of Biochemistry, University of Zurich Zurich Switzerland

† Corresponding author

## Abstract

Members of the ubiquitous SLC11/NRAMP family catalyze the uptake of divalent transition metal ions into cells. They have evolved to efficiently select these trace elements from a large pool of Ca2+ and Mg2+, which are both orders of magnitude more abundant, and to concentrate them in the cytoplasm aided by the cotransport of H+ serving as energy source. In the present study, we have characterized a member of a distant clade of the family found in prokaryotes, termed NRMTs, that were proposed to function as transporters of Mg2+. The protein transports Mg2+ and Mn2+ but not Ca2+ by a mechanism that is not coupled to H+. Structures determined by cryo-EM and X-ray crystallography revealed a generally similar protein architecture compared to classical NRAMPs, with a restructured ion binding site whose increased volume provides suitable interactions with ions that likely have retained much of their hydration shell.

## Introduction

Divalent cations constitute important factors in numerous biological processes and they are thus essential nutrients that need to be imported into cells in the required amounts. From a chemical perspective, we distinguish the alkaline earth metals Ca2+ and Mg2+ from transition metal ions such as Fe2+ and Mn2+, which show distinct properties owing to their size and electronic structure. As major constituent of bone, Ca2+ has to be taken up by vertebrates in high amount. Although its largest part is immobilized within the body, free Ca2+ is present in the extracellular medium in low millimolar concentrations. In contrast, cytoplasmic Ca2+ serves as second messenger and its distribution in the cell thus requires tight control (Carafoli and Krebs, 2016). Mg2+ on the other hand is a ubiquitous ligand of nucleotides and nucleic acids (de Baaij et al., 2015; Maguire and Cowan, 2002). Despite the similar extracellular concentration, its abundance in the cytoplasm is several orders of magnitude higher compared to Ca2+. In their interaction with other molecules, these alkaline earth metal ions are coordinated by electronegative hard ligands, preferentially oxygens, which compensate their positive charges by either full or partial countercharges (Carafoli and Krebs, 2016; Payandeh et al., 2013). In contrast to Ca2+ and Mg2+, which both constitute minor elements in the human body, transition metals are trace elements that are found at much lower concentration, as they are required for specialized processes. Transition metals are distinguished by their incompletely filled d-orbitals. This property permits coordinative interactions with soft ligands containing free electron pairs and allows them to change their oxidation state, which makes them important cofactors in redox reactions. The transition metal ion Fe2+ plays a central role in oxygen transport and, together with Mn2+, it is a cofactor of enzymes catalyzing redox reactions. Due to their low abundance in the extracellular environment, the uptake of transition metals has thus to proceed with high selectivity to prevent competition with several orders of magnitude more abundant alkaline earth metals, which would prohibit their efficient accumulation. This challenge is overcome by specific transmembrane transport proteins, which catalyze the accumulation of transition metal ions inside cells. Among these proteins, members of the SLC11/NRAMP family play an important role. They are expressed in all kingdoms of life where they facilitate the transmembrane transport of different transition metal ions by a secondary active process that involves the cotransport of H+ as energy source (Courville et al., 2006; Nevo and Nelson, 2006). In animals, these proteins are used for the transport of Fe2+ (Montalbetti et al., 2013), whereas in prokaryotes the primary substrate is Mn2+ (Makui et al., 2000). Besides the transport of both transition metals, plant NRAMPs are also involved in detoxification processes by transporting noxious metal ions such as Cd2+ (Huang et al., 2020a).

The transport properties of SLC11/NRAMP proteins have been investigated in numerous functional studies (Gunshin et al., 1997; Mackenzie et al., 2006; Makui et al., 2000), supported by the structures of prokaryotic transporters determined in different conformations (Bozzi et al., 2016b; Bozzi et al., 2019b; Ehrnstorfer et al., 2014; Ehrnstorfer et al., 2017). With respect to its fold, the family is distantly related to other secondary active transporters that include the amino-acid transporter LeuT (Ehrnstorfer et al., 2014; Yamashita et al., 2005), although there is little relationship on a sequence level, SLC11/NRAMP structures provide detailed insight into substrate preference and transport mechanisms. Characterized family members show an exquisite selectivity for transition metals over alkaline earth metal ions, but they poorly discriminate between transition metals (Ehrnstorfer et al., 2014; Gunshin et al., 1997). This is accomplished by a conserved ion binding site that is located in the center of the protein (Ehrnstorfer et al., 2014). Several residues coordinate the largely dehydrated metal ion with hard, oxygen-containing ligands, which would equally well interact with other divalent cations. Additionally, the site allows interaction with the free electron pair of the thioether group of a conserved methionine residue, which serves as soft ligand that permits coordinative interactions with transition metal- but not alkaline earth metal ions (Ehrnstorfer et al., 2014). The mutation of this methionine to alanine in one of the bacterial homologues had a comparably small effect on transition metal ion transport but instead converted Ca2+ into a transported substrate, which emphasizes the role of the residue in conferring ion selectivity (Bozzi et al., 2016a).

Although, throughout kingdoms of life, the majority of SLC11/NRMP transporters share similar functional properties, there are few family members that were described to transport with distinct substrate preference. Among these family members are prokaryotic proteins, termed NRAMP-related magnesium transporters (NRMTs), that were identified as uptake systems for Mg2+. In the bacterium Clostridium acetobutylicum, the prototypic NRMT (CabNRMT) has permitted growth at limiting Mg2+ concentrations, even in absence of any alternative transport pathways (Shin et al., 2014). The altered substrate preference is remarkable since, owing to its small ionic radius and the consequent high charge density, the interaction of Mg2+ with its surrounding solvent is unusually strong, which makes the dehydration of the ion energetically costly and therefore requires unique features for its transport (Chaudhari et al., 2020; Maguire and Cowan, 2002). The uptake of Mg2+ into cells is thus accomplished by few selective transport systems (Payandeh et al., 2013) that include the bacterial proteins CorA (Lunin et al., 2006), CorC (Huang et al., 2021), MgtE (Hattori et al., 2007) and their eukaryotic homologues (Schäffers et al., 2018; Schweigel-Röntgen and Kolisek, 2014), the TRP channel TRPM7 (Huang et al., 2020b) and Mg2+-selective P-type pumps (Maguire, 1992). In the present study, we became interested in the mechanism of Mg2+ transport by SLC11 proteins and we thus set out to investigate the functional and structural basis of this process by combining transport experiments with structural studies. We identified a biochemically well-behaved NRMT, which allowed us to characterize its transport behavior using in vitro transport experiments. Structure determination by cryo-electron microscopy and X-ray crystallography revealed an expanded substrate binding site that binds the divalent cation as complex with most of its hydration shell, which permits selection against the larger Ca2+, which is not a transported substrate.

## Results

### Phylogenetic analysis of NRAMP transporters

In light of the proposed altered substrate preference of certain prokaryotic SLC11 proteins, we became interested in the phylogeny of the family. For that purpose, we have identified numerous SLC11 homologues in BLAST searches of pro- and eukaryotic sequence databases using human DMT1, the prokaryotic Mn2+ transporters EcoDMT and ScaDMT, the putative NRAMP-related aluminium transporter (NRAT) from Orzya sativa and the proposed Mg2+ transporter CabNRMT as queries. In this way, sequences of 1100 eukaryotic and 447 prokaryotic NRAMP proteins and 745 prokaryotic NRMTs were aligned and subjected to phylogenetic characterization. The resulting phylogenetic tree displayed in Figure 1 shows a distributed organization with different family members clustering into separated clades. Branches of this phylogenetic tree group proteins from the animal kingdom including human DMT1 and NRAMP1, which both function as H+ coupled Fe2+ transporters (Forbes and Gros, 2003; Gunshin et al., 1997), prokaryotic homologues including proteins of known structure such as ScaDMT (Ehrnstorfer et al., 2014), EcoDMT (Ehrnstorfer et al., 2017) and DraNRAMP (Bozzi et al., 2019b), whose primary function is H+ coupled Mn2+ transport and plant proteins ascribed to be involved in the transport of various transition metal ions such as the toxic metal Cd2+ (Huang et al., 2020a). Within the plant kingdom, a small but separated branch encompasses putative Al3+ transporters classified as NRATs (Chauhan et al., 2021; Xia et al., 2010). Finally, a large and distant clade of the family containing homologues of the prototypic CabNRMT defines a group of transporters which, although clearly being part of the family, appear to have evolved to serve a different purpose (Figure 1B; Shin et al., 2014). The proposed functional distinction between different clades is manifested in the sequence of the substrate binding site that was identified in structural studies of prokaryotic SLC11 family members to coordinate divalent transition metals (Ehrnstorfer et al., 2014; Figure 1A, Figure 1—figure supplement 1). This site is defined by a signature containing a DxxN motif in the unwound center of α-helix 1 and an A/CxxM motif in the unwound center of α-helix 6. The signature is fully conserved in animal Fe2+ transporters, bacterial Mn2+ transporters and most transporters of plant origin, which all exhibit a strong selectivity against alkaline earth metal ions but poor discrimination between transition metal ions. Conversely, the motif is replaced by a DxxN-AxxT motif in NRATs and a DxxG-TxxA/T motif in NRMTs thus indicating that latter clades would exhibit a different substrate preference (Figure 1—figure supplement 1).

![Figure 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig1-v2.jpg)

**Figure 1.:** (A) Model of the consensus ion binding site of NRAMP transporters as obtained from the X-ray structure of ScaDMT (PDBID 5M95) in complex with Mn2+. Regions of α1 and α6 are shown as Cα-trace, selected residues coordinating the ion as sticks. (B) Phylogenetic tree of SLC11 residues with different clades of the family highlighted. Selected family members are indicated. The consensus sequence of the respective ion binding site of each clade is shown.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Residues constituting the ion binding site are highlighted in green. Secondary structure elements are indicated on the top. Prokaryotic NRAMPSs (prNRAMP): 1 D. radiodurans (Uniprot: Q9RTP8), 2 S. capitis (Uniprot: A0A4U9TNH6), 3 E. coelocola (Uniprot: E4KPW4), 4 E. coli (UniProt: sp|P0A769|MNTH_ECOLI), 5 M. tuberculosis (UniProt: sp|P9WIZ5|MNTH_MYCTU), 6 B. subtilis (UniProt: sp|P96593|MNTH_BACSU), 7 S. typhimurium (Uniprot: sp|Q9RPF4|MNTH_SALTY), 8 P. aeruginosa (Uniprot: sp|Q9RPF3|MNTH1_PSEAE). Animal NRAMPs (anNRAMP): 1 H. sapiens NRAMP2 (NCBI: NP_001366375.1), 2 P. paniscus NRAMP2 (NCBI: XP_008949491.1), 3 C. sabaeus NRAMP2 (NCBI: XP_037853046.1), 4 R. roxellana NRAMP2 (NCBI: XP_010383634.1), 5 M. mulatta NRAMP2 (NCBI: EHH20731.1), 6 E. caballus NRAMP2 (NCBI: XP_023499318.1), 7 C. canadensis NRAMP2 (NCBI: XP_020035491.1), 8 H. hyaena NRAMP2 (NCBI: XP_039097283.1), 9 C. ferus NRAMP2 (NCBI: XP_032348726.1), 10 B. indicus NRAMP2 (NCBI: XP_019816126.1). Plant NRAMPs (plNRAMP): 1 P. vulgaris (NCBI: XP_007155869.1), 2T. subterraneum (NCBI: GAU12542.1), 3 G. max (NCBI: NP_001344702.1), 4 C. arietinum (NCBI: XP_004511877.1), 5 D. chrysotoxum (NCBI: KAH0462125), 6T. cacao (NCBI: XP_007047433.1), 7 V. unguiculata (NCBI: XP_027914252.1), 8 G. soja (NCBI: KAG4933418.1), 9 M. truncatula (NCBI: XP_003611648.1), 10 A. annua (NCBI: PWA53748.1). Plant NRATs (plNRAT): 1 O. sativa (NCBI: XP_015625418.1), 2 D. oligosanthes (NCBI: OEL35611.1), 3 S. italica (NCBI: XP_004952002.1), 4 S. bicolor (NCBI: XP_002451480.2), 5 P. miliaceum (NCBI: RLM80353.1), 6 P. virgatum (NCBI: XP_039819678.1), 7 Z. mays (NCBI: PWZ19830.1). Prokaryotic NRMTs (prNRMT): 1 P. propionicus (NCBI: WP_011735082.1), 2 M. australiensis (NCBI: WP_013780282.1), 3 C. saccharolyticus (NCBI: WP_011916762.1), 4 A. bacterium (NCBI: PYS45348.1), 5 G. bemidjiensis (NCBI: WP_012531668.1), 6T. narugense (NCBI: PMP85905.1), 7 C. acetobutylicum (NCBI: WP_034583260.1), 8 M. paludicola (NCBI: BAI61876.1), 9 S. aciditrophicus (NCBI: WP_011418107.1), 10 S. usitatus (NCBI: WP_011688372.1), 11 E. laentae (NCBI: WP_009305646.1).

### Functional characterization of EcoDMT mutants

To gain further insight into the presumed substrate preference, we investigated how mutations of ion binding site residues would alter the selectivity of a classical NRAMP protein by characterizing the functional properties of the bacterial Mn2+ transporter EcoDMT. To do so, we employed previously established proteoliposome-based transport assays with appropriate fluorophores to detect the uptake of specific ions into vesicles (Ehrnstorfer et al., 2017, Figure 2—figure supplement 1). All transport experiments were carried out in in presence of a 100-fold outwardly directed K+ gradient, which after addition of the ionophore valinomycin establishes a membrane potential of –118 mV, to enhance the sensitivity of the applied assays.

Classical NRAMP proteins efficiently transport divalent transition metal ions with low micromolar affinity, while discriminating against alkaline earth metal ions such as Ca2+ and Mg2+ (Ehrnstorfer et al., 2017; Mackenzie et al., 2006). These functional properties are reflected in transport studies of EcoDMT, which employ the fluorophore calcein as efficient reporter to monitor micromolar concentrations of Mn2+ whereas it is not responsive to either Ca2+ or Mg2+ even at much higher concentrations. In our experiments, we find a concentration-dependent quenching of the fluorescence due to Mn2+ influx into vesicles containing the trapped fluorophore (Figure 2A and B, Figure 2—figure supplement 1A), which is neither inhibited by the addition of Ca2+ nor Mg2+ to the outside solution (Figure 2C and D). Latter would be expected if these ions would compete for the binding of Mn2+. As suggested from previous studies (Bozzi et al., 2016a; Ehrnstorfer et al., 2014), we expected a key role of the methionine (Met 235) in the binding site of the protein as major determinant of this pronounced selectivity. We thus initially investigated whether it was possible to alter the substrate preference of EcoDMT by shortening the methionine side chain in the mutant EcoDMT M235A. This construct was still capable of transporting Mn2+ with a threefold increase of its Km (Figure 2A, B, E and G), whereas now also Ca2+ became a permeable substrate as illustrated by the competition of the ion with Mn2+ transport (Figure 2F and G) and the direct detection of Ca2+ transport using the fluorophore Fura2 (Figure 2H, Figure 2—figure supplement 1B). A similar result was previously obtained for the equivalent mutation of the homologue DraNRAMP (Bozzi et al., 2016a). In contrast to Ca2+, we were not able to detect any interaction with Mg2+ (Figure 2I), indicating that the energetic requirements to transport this smaller divalent cation are higher than for Ca2+.

![Figure 2.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig2-v2.jpg)

**Figure 2.:** (A) EcoDMT-mediated Mn2+ transport into proteoliposomes. Data display mean of three experiments from three independent reconstitutions. (B) Mn2+ concentration dependence of transport. Initial velocities were derived from individual traces of experiments displayed in (A), the solid line shows the fit to a Michaelis–Menten equation with an apparent Km of 13.5  μM. (C) Mn2+ transport in presence of Ca2+. Data display mean of seven experiments from two independent reconstitutions, except for the measurement without divalent ions (0/0, green, mean of two experiments). (D) Mn2+ transport into EcoDMT proteoliposomes in presence of Mg2+. Data display mean of 3 (0/0, green), 4 (50/0, blue) and nine experiments (50/500, orange and 50/2000, red) from three independent reconstitutions. (E) Mn2+ transport into proteoliposomes containing the EcoDMT mutant M235A. Data display mean of eight experiments from three independent reconstitutions. (F) Inhibition of Mn2+ transport in the mutant M235A by Ca2+ (3 experiments from three independent reconstitutions). (G) Mn2+ concentration dependence of transport into M235A proteoliposomes. For Mn2+, initial velocities were derived from individual traces of experiments displayed in (E), for Mn2+ in presence of 2 mM Ca2+, data show mean of three experiments from three independent reconstitutions. The solid lines are fits to a Michaelis–Menten equation with apparent Km of 41  μM (Mn2+) and 107 uM (Mn2+ in presence of 2 mM Ca2+). (H) Ca2+-transport into M235A proteoliposomes assayed with the fluorophore Fura-2. Data display mean of tree experiments from three independent reconstitutions. (I) Mn2+ transport in presence of Mg2+. Data display mean of 6 experiments from three independent reconstitutions. (J) Mn2+ transport into proteoliposomes containing the EcoDMT triple mutant M235A/N54G/A232T. Data display mean of three experiments from three independent reconstitutions. (K) Inhibition of Mn2+ transport in the mutant M235A/N54G/A232T by Mg2+ (six experiments from three independent reconstitutions). (L) Mn2+ concentration dependence of transport into M235A/N54G/A232T proteoliposomes. For Mn2+, initial velocities were derived from individual traces of experiments displayed in (J), for Mn2+ in presence of 2 mM Mg2+, data show mean of three (without Mg2+, red) and six experiments (with Mg2+, blue) from three independent reconstitutions. The solid lines are fits to a Michaelis–Menten equation with apparent Km of 31  μM (Mn2+) and 38 µM (Mn2+ in presence of 2 mM Mg2+). (A, C, D, E, F, I, J, K) Uptake of Mn2+ was assayed by the quenching of the fluorophore calcein trapped inside the vesicles. (A, C, D, E, F, H, I, J, K) Averaged traces are presented in unique colors. Fluorescence is normalized to the value after addition of substrate (t = 0). Applied ion concentrations are indicated. (A–L), Data show mean of the indicated number of experiments, errors are s.e.m.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Non-specific leak into protein-free liposomes in assay conditions used for the detection of different divalent cations. The respective fluorophores are trapped inside the liposomes. (A) Mn2+ transport assayed by the quenching of the fluorophore calcein. (B) Ca2+ transport assayed by the fluorescence increase of the fluorophore Fura-2. (C) Mg2+ transport assayed by the fluorescence increase of the fluorophore Magnesium Green. Traces show experiments at the highest concentration of divalent cations used in the study. The signal of protein-free liposomes (no protein) is shown in gray, the specific transport mediated by the indicated protein constructs is shown for comparison (pink for Mn2+ and Ca2+ red for Mg2+). Dots show mean values of independent replicates (A, no protein n = 12, EcoDMT n = 3; B, no protein n = 13, EcoDMT M235A n = 3; C, no protein n = 13, EleNRMT n = 3) errors are s.e.m.

Finally, we attempted to confer Mg2+ transport properties to EcoDMT by creating the triple mutant M235A/N54G/A232T, which converts its entire binding site to the residues found in prokaryotic NRMTs. As for the mutant M235A, this construct folded into a stable protein that retained its capability of Mn2+ transport while remaining unable to interact with Mg2+ (Figure 2J–L). In summary, the mutation of the binding site residues of EcoDMT towards an NRMT was well tolerated with the resulting constructs retaining their capability for Mn2+ transport. This suggests that the structural and energetic requirements for interactions with this transition metal are lower than for alkaline earth metals. We also confirmed the role of the binding site methionine as an important determinant for the counterselection of Ca2+, which due to its much higher concentration would outcompete Mn2+ transport in a physiological environment. However, neither the replacement of the methionine nor the conversion of the binding site to residues observed in NRMTs was sufficient to facilitate Mg2+ transport, demonstrating that structural features beyond the immediate binding site residues are required to transport this small divalent cation. Consequently, we decided to turn our attention towards the characterization of prokaryotic NRMTs to gain further insight into Mg2+ transport by SLC11 homologues.

### Functional characterization of EleNRMT

Initially, our attempts toward the characterization of NRMTs were focused on the identification of a suitable candidate for structural and functional studies. Towards this end, we cloned and investigated the expression properties of 82 representative homologues selected from the pool of 745 sequences of putative NRMTs identified in BLAST searches (Figure 1B). Within this subset, we were able to single out a candidate from the bacterium Eggerthella lenta termed EleNRMT with promising biochemical properties (Figure 3—figure supplement 1). After expression and purification in the detergent n-dodecyl-beta-D-Maltoside (DDM), we found this protein to elute as monodisperse peak from a size exclusion chromatography column. (Figure 3—figure supplement 2A). Although much better behaved than the other investigated homologues, EleNRMT was still comparably instable in detergent solution and difficult to reconstitute into liposomes. We thus attempted to improve its stability by consensus mutagenesis (Cirri et al., 2018) by converting 11 positions identified in sequence alignments to their most abundant residues in NRMTs to create the construct EleNRMTts (Figure 3—figure supplement 1A). This approach improved the thermal stability of the monomeric protein and the efficiency of reconstitution without affecting its functional properties (Figure 3, Figure 3—figure supplement 2B-D). Due to the sensitivity of the assay and the fact that binding site mutants of EcoDMT retained their ability to transport Mn2+, we initially investigated transport properties of EleNRMT for this divalent transition metal ion and found robust concentration-dependent activity that saturates with a Km of around 120 µM for either WT or the thermostabilized mutant (Figure 3A, B, D and E). For both constructs, we found Mg2+ to inhibit Mn2+ transport in a concentration-dependent manner, thus indicating that Mg2+ would compete with Mn2+ for its binding site (Figure 3C and F). We subsequently quantified binding of either ion to detergent solubilized protein by isothermal titration calorimetry and found a Kd of around 100 µM for Mn2+, which corresponds well with the measured Km of transport of the same ion and a somewhat lower affinity of around 400 µM for Mg2+ (Figure 3G and H, Figure 3—figure supplement 2E, F). Together, transport and binding experiments demonstrate the capability of EleNRMT to interact with Mg2+ thus providing evidence that it might indeed catalyze Mg2+ uptake into bacteria.

![Figure 3.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig3-v2.jpg)

**Figure 3.:** (A) EleNRMT mediated Mn2+ transport into proteoliposomes. Data display mean of three experiments from two independent reconstitutions. (B) Mn2+ concentration dependence of transport. Initial velocities were derived from individual traces of experiments displayed in (A), the solid line shows the fit to a Michaelis–Menten equation with an apparent Km of 119  μM. (C) Mn2+ transport in presence of Mg2+. Data display mean of 3 (0/0, green), 6 (50/0, blue), 5 (50/500, orange), and 9 (50/2000, red) experiments from two independent reconstitutions. (D) Mn2+ transport into proteoliposomes mediated by the thermostabilized mutant EleNRMTts. Data display mean of four experiments from two independent reconstitutions, except for the measurement with 25 μM Mn2+ (mean of three experiments). (E) Mn2+ concentration dependence of transport. Initial velocities were derived from individual traces of experiments displayed in (D), the solid line shows the fit to a Michaelis–Menten equation with an apparent Km of 124  μM. (F) Mn2+ transport in presence of Mg2+. Data display mean of 4 (0/0, green), 9 (50/0, blue), 11 (50/500, orange), and 8 (50/2000, red) experiments from two independent reconstitutions. A, C, D, F. Uptake of Mn2+ was assayed by the quenching of the fluorophore calcein trapped inside the vesicles. Averaged traces are presented in unique colors. Fluorescence is normalized to the value after addition of substrate (t = 0). Applied ion concentrations are indicated. (A–F), Data show mean of the indicated number of experiments, errors are s.e.m. (G–H), Binding isotherms obtained from isothermal titrations of Mn2+ (G) and Mg2+ (H) to EleNRMTts. The data shown for two biological replicates per condition was fitted to a model assuming a single binding site with the binding isotherm depicted as solid line. Errors represent fitting errors.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Sequence of EleNRMT (NCBI: WP_009305646.1) with secondary structure elements indicated below. Residues mutated in the thermostabilized EleNRMTts are highlighted with replacements shown on top. (B) Comparison of functionally relevant regions of EleNRMT and the Mn2+ transporter ScaDMT (Uniprot: A0A4U9TNH6) with secondary structure elements shown below. Dots indicate ion binding site (red), a residue interacting with the ion in an occluded state (orange) and positions relevant for H+ transport in NRAMPs on α6 (blue) and α3, 9 (green).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Gel filtration profiles on a Superdex 200 column of WT EleNRMT (A) and the thermostabilized construct of ElenRMTts (B). Insets show SDS-PAGE gel of peak fractions with molecular weight marker indicated (kDa). (C) Thermal stability of EleNRMT and EleNRMTts as determined by fluorescence-based size-exclusion chromatography (Hattori et al., 2012). Data show averages of four technical replicates, errors are s.e.m. (D) SEC/MALS experiment of purified EleNRMTts with obtained molecular weight corresponding to a monomeric transporter (measured molecular weight of 45.6 kDa versus theoretical molecular weight of 46.9 kDa). Thermograms of Mn2+ (E) and Mg2+ (F) binding to EleNRMTts obtained from isothermal titration calorimetry experiments shown in Figure 3G and H. (E, F) Panels show titration against buffer (left) and traces of two biological replicates (center, right).

To further characterize Mg2+ transport by EleNRMT, we have quantified Mn2+ uptake into proteoliposomes in presence of Mg2+ and found a strong interference (Figure 4A and B). By directly assaying Mg2+ with the selective fluorophore Magnesium Green, we observed a concentration-dependent increase of the transport rate (Figure 4C, Figure 2—figure supplement 1C), with the lack of saturation at high substrate concentrations, reflecting the poor affinity of the dye for the ion. Since our experiments have confirmed Mg2+ as substrate of EleNRMT, we wondered whether the protein would also transport Ca2+ and thus investigated the inhibition of Mn2+ uptake by Ca2+ and the import of Ca2+ into proteoliposomes monitored with the fluorophore Fura-2 (Figure 4D and E). However, in contrast to Mg2+, we did in no case find strong evidence for the recognition of this larger alkaline earth metal ion, which has become a transported substrate for EcoDMT mutants lacking a conserved methionine in the binding site (Figure 2F–H). Latter finding is remarkable since the presumed metal ion binding site only consists of hard ligands that would also coordinate Ca2+ and it thus emphasizes the presence of distinct structural features of the pocket facilitating Mg2+ interactions (Figure 3—figure supplement 1B).

![Figure 4.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig4-v2.jpg)

**Figure 4.:** (A–E) Metal ion transport by EleNRMTts. (A) EleNRMTts mediated Mn2+ transport into proteoliposomes in presence of 2 mM Mg2+. Data display mean of eight experiments from three independent reconstitutions, except for the measurement with 200 μM Mn2+ (mean of seven experiments). (B) Mn2+ concentration dependence of transport into EleNRMTts proteoliposomes. For Mn2+, data are as displayed in Figure 3E, for Mn2+ in presence of 2 mM Mg2+, initial velocities were derived from individual traces of experiments displayed in (A). The solid lines are fits to a Michaelis–Menten equation. (C) Mg2+-transport into EleNRMTts proteoliposomes assayed with the fluorophore Magnesium Green. Data display mean of 5 (0 μM Mg2+), 8 (800 μM and 1250 μM Mg2+), 4 (2500 μM Mg2+), and 3 (5000 μM Mg2+) experiments from two independent reconstitutions. (D) Mn2+ transport in presence of Ca2+. Data display mean of 4–11 experiments from three independent reconstitutions. (A, D) Uptake of Mn2+ was assayed by the quenching of the fluorophore calcein trapped inside the vesicles. (E) Ca2+-transport into EleNRMTts proteoliposomes assayed with the fluorophore Fura-2. Data display mean of 3 (0 μM Ca2+), 12 (200 μM Ca2+) and 9 (2000 μM Ca2+) experiments from 2 independent reconstitutions. The small increase of the fluorescence at high Ca2+ concentrations likely results from non-specific leak into proteoliposomes. (F–H) Assay of H+ transport with the fluorophore ACMA. Experiments probing metal ion coupled H+ transport into proteoliposomes containing EleNRMTts upon addition of Mn2+ (eight experiments from two independent reconstitutions) (F) and Mg2+ (eight experiments from two independent reconstitutions) (H) do not show any indication of H + transport. Mn2+ coupled H+ transport into EcoDMT proteoliposomes (three experiments from three independent reconstitutions and for the negative control [no protein, 400 μM Mn2+], 4 measurements) is shown for comparison (I). A, C-H Averaged traces are presented in unique colors. Fluorescence is normalized to the value after addition of substrate (t = 0). Applied ion concentrations are indicated. (A–H), Data show mean of the indicated number of experiments, errors are s.e.m.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Sequence alignment of the three EleNRMT binders Nb1-Nb3. Secondary structure is shown above. The location of complementary determining regions (CDRs) are indicated, residues in Nb1 and Nb2 making contacts with EleNRMTts are highlighted in green. SEC profiles of purified (B) Nb1, (C) Nb2, and (D) the EleNRMTts-Nb1,2 complex assembled with a stoichiometric excess of both nanobodies. Inset shows SDS-PAGE gel with molecular weights (kDa) indicated.

After confirming the capability of EleNRMT to specifically transport Mn2+ and Mg2+, we were interested whether the uptake of metal ions would be coupled to H+ as observed for previously characterized transition metal ion transporters of the family. To this end we employed the fluorophore ACMA to monitor pH changes that are induced by metal ion symport (Figure 4F–H). Whereas such concentration-dependent changes are readily observed for EcoDMT (Figure 4H), there was no acidification of proteoliposomes containing EleNRMT as a consequence of either Mg2+ or Mn2+ uptake (Figure 4F and G), thus suggesting that metal ion transport by EleNRMT is not coupled to H+. Collectively our functional experiments confirm the role of EleNRMT to function as uncoupled Mg2+ transporter. Due to the high-sequence conservation in this subclade of the SLC11 family, it is safe to assume that this property would likely also be shared by other NRMTs.

### Structural characterization of EleNRMT

Following the characterization of the transport properties of EleNRMT, we became interested in the molecular determinants underlying its distinct selectivity and thus engaged in structural studies by X-ray crystallography and cryo-EM. Since the monomeric protein, with a molecular weight of only 47 kDa and lacking pronounced domains extending from the membrane, is itself not a suitable target for cryo-EM, we initially attempted structural studies by X-ray crystallography but were unable to obtain crystals, despite extensive screening. To enlarge the size of the protein and facilitate crystallization, we generated specific nanobodies by immunization of alpacas with purified EleNRMTts followed by the assembly of a nanobody library from blood samples and selection by phage display. These experiments allowed us to identify three distinct binders recognizing the protein termed Nb1-3EleNRMT (short Nb1-3) (Figure 4—figure supplement 1A). Despite the increase of the hydrophilic surface, which was frequently found to facilitate crystallization, all attempts to obtain crystals of EleNRMTts in complex with a single nanobody were unsuccessful. Similarly, efforts toward the structure determination of the same complexes by cryo-EM did not permit a reconstruction at high resolution. We thus attempted to further increase the size of the complex and found that Nb1 and either one of the two closely related nanobodies Nb2 or Nb3 were able to bind concomitantly to the protein to assemble into a ternary complex (Figure 4—figure supplement 1B-D). This complex showed improved crystallization properties and was of sufficient size to allow structure determination by single particle averaging. The structure of the tripartite EleNRMTts nanobody complex was determined by cryo-EM in absence of additional Mg2+ (EleNRMTts-Nb1,2) and in buffer containing 10 mM Mg2+ (EleNRMTtsMg2+-Nb1,2). Datasets collected from respective samples allowed the 3D-reconstruction of a map at 3.5 Å for EleNRMTts-Nb1,2 and at 4.1 Å for EleNRMTtsMg2+-Nb1,2 (Figure 5—figure supplements 1 and 2, Table 1). Both maps display equivalent conformations of the complex and permitted its unambiguous interpretation by an atomic model defining the features of an NRMT (Figure 5A and B, Figure 5—figure supplement 3). The structures show a protein complex consisting of the transporter EleNRMTts and two nanobodies binding to non-overlapping epitopes on the extracellular side (Figure 5A and B, Figure 5—figure supplement 4). This complex structure was subsequently used as search model for molecular replacement for a dataset collected from a crystal of the EleNRMTts-Nb1,2 complex grown in presence of 50 mM Mg2+ and extending to 4.1 Å (Figure 5—figure supplement 5A, Table 2). In the X-ray structure, both copies of the complex in the asymmetric unit closely resembled the cryo-EM model, thus providing an ideal system to determine the location of bound ions by anomalous scattering experiments (Figure 5—figure supplement 5A-C). Toward this end, we have soaked our crystals in solutions where Mg2+ was replaced by Mn2+ in the expectation that latter would occupy the binding site as suggested from functional experiments (Figure 3) and collected data at the anomalous absorption edge of the transition metal ion. This data allowed the unambiguous localization of Mn2+ in the anomalous difference density, which showed a single strong peak per complex located in the equivalent position as previously identified for the binding site of ScaDMT (Ehrnstorfer et al., 2014, Figure 5C, Figure 5—figure supplement 5B, C,). In similar location, we find residual density in our cryo-EM datasets thus suggesting that Mg2+ and Mn2+ would both occupy the same site of the transporter (Figure 5—figure supplement 5D, E).

![Figure 5.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-v2.jpg)

**Figure 5.:** (A) Cryo-EM density (contoured at 5 σ) of EleNRMTts in complex with Nb1 and Nb2 at 3.5 Å viewed from within the membrane with the extracellular side on top and (B), ribbon representation of the complex in the same view. Proteins are shown in unique colors. (C) Anomalous difference density of Mn2+ obtained from the crystal structure of the EleNRMTts-Nb1-Nb2 complex (calculated at 5 Å and displayed as black mesh contoured at 4.5 σ). Model of EleNRMTts encompassing the unwound center of helices α1 and α6 is shown as ribbon.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) Representative micrograph (out of a total of 22 117 images) of the complex acquired with a Titan Krios G3i microscope equipped with a K3 camera. (B) 2D class averages of the EleNRMTts-Nb1-Nb2 dataset. (C) Data processing workflow. After extraction and one round of 2D classification, a single ab initio reconstruction with four classes was performed. The particle distribution is indicated in %. The two most promising classes, together with a decoy class were subjected to nine rounds of heterogeneous refinement. Non-uniform (NU) refinement, local CTF-refinement and a second round of NU-refinement with C1 symmetry yielded a map at a resolution of 3.5 Å. (D) Angular distribution of particle orientations. The heatmap displays the number of particles for a given viewing angle. (E) Directional and global FSC plots. The global FSC is shown in black. Dashed line indicates 0.143 cut-off and the resolution at which the FSC curve drops below 0.143 is indicated. The directional FSC curves providing an estimation of anisotropy of the dataset are shown for directions x, y, and z. (F) Final 3D reconstruction of the EleNRMTts-Nb1-Nb2 complex in indicated orientations, colored according to the local resolution, estimated in cryoSPARC v.3.2.0.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Cryo-EM reconstruction of the EleNRMTts-nanobody complex in presence of Mg2+. (A) Representative micrograph (out of a total of 12,427 images) of the complex acquired with a Titan Krios G3i microscope equipped with a K3 camera. (B) 2D class averages of the EleNRMTts-Nb1-Nb2 dataset. (C) Data processing workflow. After extraction and one round of 2D classification, a single ab initio reconstruction with four classes was performed. The particle distribution is indicated in %. The particles from the two most promising classes, together with a decoy class were subjected to 22 rounds of heterogeneous refinement. Non-uniform (NU) refinement, local CTF-refinement and a second round of NU-refinement with C1 symmetry yielded a map at a resolution of 4.1 Å. (D) Angular distribution of particle orientations. The heatmap displays the number of particles for a given viewing angle. (E) Directional and global FSC plots. The global FSC is shown in black. Dashed line indicates 0.143 cut-off and the resolution at which the FSC curve drops below 0.143 is indicated. The directional FSC curves providing an estimation of anisotropy of the dataset are shown for directions x, y, and z. (F) Final 3D reconstruction of the EleNRMTts-Nb1-Nb2 complex in indicated orientations, colored according to the local resolution, estimated in cryoSPARC v.3.2.0.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** (A) EleNRMTts-nanobody complex in absence of Mg2+ at 3.5 Å. Electron density (contoured at 6σ, gray mesh) is shown superimposed on indicated protein regions. (B) EleNRMTts-nanobody complex in presence of Mg2+ at 4.1 Å. Electron density (contoured at 6σ, gray mesh) is shown superimposed on indicated protein regions.

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A) Contact region of EleNRMTts and nanobodies Nb1 and Nb2. (B) Binding interface of Nb2. (C) Binding interface of Nb1. (B, C), Side chains of residues mediating binding interactions between the transporter and the nanobodies are displayed as sticks. (A–C) Proteins are shown as ribbons with respective regions labeled.

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A) Structure of the EleNRMTts-Nb1-Nb2 complex in Mg2+ at 4.1 Å (B) Structure of the EleNRMTts-Nb1-Nb2 complex soaked in Mn2+ at 4.6 Å. A, B 2Fo-Fc density (contoured at 1 σ) is shown as green mesh superimposed on the model. (B, C), Anomalous difference electron density (calculated at 6 Å and contoured at 4 σ) from the dataset displayed in B is depicted as black mesh. (A-C), shown is one of two complexes in the asymmetric unit as Cα trace with protein chains displayed in unique colors. Phases for 2Fo-Fc and anomalous difference density maps were obtained from molecular replacement using the cryo-EM model improved by constrained minimal refinement. Residual density in the cryo-EM maps of the EleNRMTts-Nb1-Nb2 complex in vicinity to the Mn2+ binding position (indicated by black sphere) in absence (D) and presence of Mg2+ (E). Protein is represented as sticks, water (red) or Mg2+ (green) as spheres. Maps are as displayed in Figure 5—figure supplement 3.

**Table 1.**
 Cryo-EM data collection, refinement and validation statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Dataset 1EleNRMT-NB(EMDB-13985)(PDB 7QIA)</th>
      <th>Dataset 2EleNRMT-NB Mg2+ complex(EMDB-13987)(PDB 7QIC)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection and processing</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Microscope</td>
      <td>FEI Titan Krios</td>
      <td>FEI Titan Krios</td>
    </tr>
    <tr>
      <td>Camera</td>
      <td>Gatan K3 GIF</td>
      <td>Gatan K3 GIF</td>
    </tr>
    <tr>
      <td>Magnification</td>
      <td>130’000</td>
      <td>130’000</td>
    </tr>
    <tr>
      <td>Voltage (kV)</td>
      <td>300</td>
      <td>300</td>
    </tr>
    <tr>
      <td>Electron exposure (e–/Å2)</td>
      <td>69.725 / 61 / 69.381</td>
      <td>69.554</td>
    </tr>
    <tr>
      <td>Defocus range (μm)</td>
      <td>–1.0 to –2.4</td>
      <td>–1.0 to –2.4</td>
    </tr>
    <tr>
      <td>Pixel size* (Å)</td>
      <td>0.651 (0.3255)</td>
      <td>0.651 (0.3255)</td>
    </tr>
    <tr>
      <td>Initial number of micrographs (no.)</td>
      <td>22,117</td>
      <td>12,427</td>
    </tr>
    <tr>
      <td>Initial particle images (no.)</td>
      <td>4 139 894</td>
      <td>2 582 066</td>
    </tr>
    <tr>
      <td>Final particle images (no.)</td>
      <td>453 950</td>
      <td>100 176</td>
    </tr>
    <tr>
      <td>Symmetry imposed</td>
      <td>C1</td>
      <td>C1</td>
    </tr>
    <tr>
      <td>Map resolution (Å)FSC threshold</td>
      <td>3.50.143</td>
      <td>4.10.143</td>
    </tr>
    <tr>
      <td>Map resolution range (Å)</td>
      <td>2.9–7.0</td>
      <td>3.3–8.3</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Model resolution (Å)FSC threshold</td>
      <td>3.50.5</td>
      <td>4.10.5</td>
    </tr>
    <tr>
      <td>Map sharpening b-factor (Å2)</td>
      <td>–184.4</td>
      <td>–159.2</td>
    </tr>
    <tr>
      <td>Model vs Map CC (mask)</td>
      <td>0.80</td>
      <td>0.79</td>
    </tr>
    <tr>
      <td>Model compositionNon-hydrogen atomsProtein residuesLigandWater</td>
      <td>4,84363903</td>
      <td>4,8416391 (Mg)0</td>
    </tr>
    <tr>
      <td>B factors (Å2)ProteinLigandWater</td>
      <td>20.0509.12</td>
      <td>46.5236.240</td>
    </tr>
    <tr>
      <td>R.m.s. deviationsBond lengths (Å)Bond angles (°)</td>
      <td>0.0030.600</td>
      <td>0.0030.650</td>
    </tr>
    <tr>
      <td>Validation MolProbity score Clashscore Poor rotamers (%)</td>
      <td>2.0611.630</td>
      <td>2.1012.860.2</td>
    </tr>
    <tr>
      <td>Ramachandran plot Favored (%) Allowed (%) Disallowed (%)</td>
      <td>92.107.900</td>
      <td>92.267.740</td>
    </tr>
  </tbody>
</table>

_*Values in parentheses indicate the pixel size in super-resolution._

**Table 2.**
 X-ray data collection and refinement statistics.


<table>
  <thead>
    <tr>
      <th></th>
      <th>EleNRMT-Nb complex(PDB 7QJI)</th>
      <th>EleNRMT-Nb complex Mn2+-soak(PDB 7QJJ)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data collection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Space group</td>
      <td>P21</td>
      <td>P21</td>
    </tr>
    <tr>
      <td>Cell dimensions</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>a, b, c (Å)</td>
      <td>93.3, 122.2, 149.1</td>
      <td>92.9, 115.9, 149.1</td>
    </tr>
    <tr>
      <td>α,β,γ (°)</td>
      <td>90, 107.8, 90</td>
      <td>90, 107.6, 90</td>
    </tr>
    <tr>
      <td>Wavelength (Å)</td>
      <td>1.000</td>
      <td>1.896</td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>50–4.1 (4.2–4.1)</td>
      <td>50–4.6 (4.7–4.6)</td>
    </tr>
    <tr>
      <td>Rmerge</td>
      <td>12.5 (166.8)</td>
      <td>15.4 (147.6)</td>
    </tr>
    <tr>
      <td>I / σI</td>
      <td>11.6 (2.4)</td>
      <td>10.8 (1.8)</td>
    </tr>
    <tr>
      <td>Completeness (%)</td>
      <td>99.1 (98.9)</td>
      <td>99.8 (99.6)</td>
    </tr>
    <tr>
      <td>Redundancy</td>
      <td>25.1 (27.1)</td>
      <td>14.0 (14.1)</td>
    </tr>
    <tr>
      <td>Refinement</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resolution (Å)</td>
      <td>12–4.1</td>
      <td>12–4.6</td>
    </tr>
    <tr>
      <td>No. reflections</td>
      <td>23,749</td>
      <td>15,764</td>
    </tr>
    <tr>
      <td>Rwork / Rfree</td>
      <td>26.7 / 31.5</td>
      <td>28.4 / 32.8</td>
    </tr>
    <tr>
      <td>No. atoms</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>9,632</td>
      <td>9,632</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <td>B-factors</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Protein</td>
      <td>287.3</td>
      <td>270.8</td>
    </tr>
    <tr>
      <td>ligands</td>
      <td>-</td>
      <td>192.0</td>
    </tr>
    <tr>
      <td>R.m.s deviations</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Bond lengths (Å)</td>
      <td>0.003</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>Bond angles (°)</td>
      <td>0.60</td>
      <td>0.60</td>
    </tr>
  </tbody>
</table>

_Values in parentheses are for highest-resolution shell._

### EleNRMT structure and ion coordination

The structure of EleNRMTts shows a transporter that displays the general organization of the SLC11 family. It encompasses 11 membrane-spanning segments, with the first 10 segments organized as two structurally related repeats of five α-helices that are inserted in the membrane with opposite orientations (Figure 6A, Figure 3—figure supplement 1). The protein adopts an inward-facing conformation that is illustrated in the comparison with the equivalent conformations of the transporters ScaDMT and DraNRAMP, which both superimpose with RMSDs of 2.2 and 2.0 Å, respectively (Figure 6B). This structure contains a large and continuous water-filled cavity that extends from the cytoplasm and leads to a pocket located in the center of the protein at the unwound parts of α-helices 1 and 6, which together form the ion binding site (Figures 5C and 6C). The location of the bound ion is defined in the anomalous difference density of Mn2+ and its position presumably also corresponds to the binding position of Mg2+ (Figure 5C, Figure 5—figure supplement 5B-E). Although the bound ion is found at an equivalent position as in the transporter ScaDMT, the binding pocket of EleNRMT is expanded as a consequence of the about 1.5 Å shift in the location of backbone atoms and differences in the volume of interacting side chains (Figure 7A–C). In both, Mg2+ and Mn2+ transporters, an aspartate on α-helix 1 and a main chain interaction at the site of the unwound part of α-helix 6 remain a common feature of their binding sites, whereas the replacement of an alanine (Ala 223) in ScaDMT by a threonine (Thr 224) in EleNRMT introduces a side chain containing a hydroxyl group whose oxygen atom serves as additional ligand for ion interactions (Figure 7B). Further changes of other residues of the binding site alter its shape and volume. In ScaDMT, the bound ion is to a large extent excluded from the aqueous environment and instead tightly surrounded by residues of the binding site, whereas in EleNRMT the replacement of the asparagine side chain on α1 with a glycine and the methionine residue on α6 to alanine in conjunction with differences in the main chain positions widen the cavity to leave sufficient space for interacting water molecules (Figure 7A–C), suggesting that Mg2+ binds to the transporter in a partly solvated state retaining much of its first hydration shell. Thus, the EleNRMT structure implies that it is a combination of both, changes in the local environment conferred by the chemical nature of side chains and more delocalized changes causing an expansion of the binding site, which together are responsible for the altered selectivity.

![Figure 6.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig6-v2.jpg)

**Figure 6.:** (A) Ribbon representation of EleNRMT viewed from within the membrane with α1-α5 colored in beige, α6- α10 in blue and α11 in magenta. The position of a bound ion is indicated by a black sphere. (B) Superposition of EleNRMT and ScaDMT (based on PDBID:5M94 with modeled α1a), both showing equivalent inward-open conformations. Ribbon representation of ScaDMT is shown in gray, the representation of EleNRMT is as in A. (C) Ribbon representation of EleNRMT with surface of the aqueous cavity leading to the ion binding site displayed as mesh. Left, view from the cytoplasm and, right, from within the membrane. A bound ion is represented by a black sphere whose position is indicated with a red asterisk. A-C Selected helices are labeled. Membrane boundaries (A, C) and relationship between views (A–C) are indicated.

![Figure 7.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig7-v2.jpg)

**Figure 7.:** (A) Superposition of the metal ion binding regions of EleNRMT and ScaDMT (PDBID:5M95). The coloring is as in Figure 6B. The relationship between views is indicated. (B) Metal ion binding sites of EleNRMT (B) and ScaDMT (C). (B, C), inset (right) shows molecular surface surrounding the bound ion with indicated relationship. Whereas the ion in EleNRMT is located inside the aqueous cavity, its location in ScaDMT is outside of the cavity, tightly surrounded by coordinating residues. (D) Region of EleNRMT on α3 and α9 implicated in proton transport in NRAMPs and corresponding region in ScaDMT (E). (D, E) The bound ion with the conserved binding site aspartate on α1 and a residue corresponding to the first α6b histidine in NRAMPs, which was identified as potential H+ acceptor, are shown for reference. (A-E) The proteins are depicted as Cα-trace, selected residues as sticks. The position of bound metal ions is represented as a black sphere. (B-E) Selected secondary structure elements and residues are indicated.

Similar to the altered substrate preference, also the second functional hallmark of EleNRMT concerning the absent coupling of metal ion transport to protons, is manifested in its structure (Figure 7D and E). Proton transport in classical NRAMP transporters was proposed to be linked to structural features extending from the ion binding site (Bozzi et al., 2019a; Bozzi et al., 2020; Bozzi et al., 2019b; Ehrnstorfer et al., 2017; Mackenzie et al., 2006; Pujol-Giménez et al., 2017). These include the conserved aspartate involved in the coordination of metal ions, two conserved histidines on α-helix 6b downstream of the binding site methionine and a continuous path of acidic and basic residues on α-helices 3 and 9 surrounding a narrow aqueous cavity, which together appear to constitute an intracellular H+ release pathway. Apart from the binding site aspartate (Asp 55) and glutamate on α-helix 3 (Glu 133) close to the metal ion binding site, all other positions in EleNRMT are altered to residues that cannot accept protons. The two histidines on α-helix 6b are substituted by a tryptophane and an asparagine, respectively, and the polar pathway residues on α-helix 3 and 9 are replaced by hydrophobic residues and a threonine (Figure 7B and D. Figure 3—figure supplement 1B).

### Functional properties of EleNRMT binding site mutants

After identifying the structural determinants of ion interactions in NRMTs, we were interested in the consequence of mutations of residues of the binding site on selectivity and thus investigated the transport properties of mutants. Consistent with experiments on other family members, the mutation of the aspartate in the binding site (Asp55), which is a universally conserved position in all SLC11 proteins, strongly compromises transport (Figure 8A and B). Similarly, the mutation of Gln 379 on α10, a conserved position that was proposed to be involved in ion coordination in the occluded state of DraNRAMP (Bozzi et al., 2019b), exerts a similarly strong effect (Figure 8A and C, Figure 3—figure supplement 1B), thus suggesting that EleNRMT undergoes an equivalent conformational change. In contrast, the mutation of Thr 224 to alanine, the amino acid found in the equivalent position of NRAMP transporters, has smaller but still detectable impact on Mn2+ transport, which is reflected in an at least two-fold increase of its Km (Figure 8A, D and E). In contrast to Mn2+, this change has a much more pronounced effect on Mg2+ interactions, which is manifested in the absence of appreciable inhibition of Mn2+ transport in presence of increasing Mg2+ concentrations and the non-detectable Mg2+ transport when directly assaying this alkaline earth metal ion (Figure 8F and G). Finally, by replacing Gly 58 to asparagine in the background of the T224A mutant, we create an EleNRMT construct with a similar binding site signature as the EcoDMT mutant M235A, which showed increased Ca2+ permeability. We thus investigated whether an equivalent conversion would also change the properties of EleNRMT with respect to its ability to transport Ca2+, which is not a substrate of the WT protein (Figure 4D and E). In line with the pronounced effect already observed for T224A (Figure 8D and E), we see a further reduction of Mn2+ transport in the double mutant T224A/G58N (Figure 8H). In contrast to the compromised Mn2+ transport properties, this double mutant shows detectable Ca2+ transport activity, thus illustrating that the conversion has introduced structural determinants that facilitate Ca2+ interactions and that change the properties of the binding site to more closely resemble NRAMP proteins.

![Figure 8.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig8-v2.jpg)

**Figure 8.:** (A) Model of the ion binding site of EleNRMT with ion (black sphere) showing bound Mn2+. Regions of α1 and α6 are shown as Cα-trace, selected residues coordinating the ion as sticks. (B–D) Mn2+ transport mediated by EleNRMTts binding site mutants. (B) D55A (2 (0 μM Mn2+), 6 (50 μM Mn2+), and 7 (400 μM Mn2+) experiments from two independent reconstitutions), (C) Q379A (2 (0 μM Mn2+), 6 (50 μM Mn2+), and 7 (400 μM Mn2+) experiments from two independent reconstitutions), (D) T224A (5 experiments from two independent reconstitutions). (E) Mn2+ concentration dependence of transport of T224A. Initial velocities were derived from individual traces of experiments displayed in (D), the solid line shows the fit to a Michaelis–Menten equation with an apparent Km exceeding 290  μM. (F) Mn2+ transport into T224A proteoliposomes in presence of Mg2+ (4 experiments from two independent reconstitutions). (G) Mg2+-transport into T224A proteoliposomes assayed with the fluorophore Magnesium green (4 experiments from two independent reconstitutions). (H-I) Transport mediated by the EleNRMTts binding site mutant T224A/G58N. (H) Mn2+ transport into proteoliposomes containing T224A/G58N (2 (0 μM Mn2+), 6 (50 μM Mn2+), and 7 (400 μM Mn2+) experiments from two independent reconstitutions). (I) Ca2+-transport into T224A/G58N proteoliposomes assayed with the fluorophore Fura-2 (9 (0 μM Ca2+), 10 (50 μM Ca2+), 11 (150 μM Ca2+), and 10 (500 μM Ca2+) experiments from two independent reconstitutions). (B-D), (F- H) Uptake of Mn2+ was assayed by the quenching of the fluorophore calcein trapped inside the vesicles. (B-D), (F-I) Averaged traces are presented in unique colors. Fluorescence is normalized to value after addition of substrate (t = 0). Applied ion concentrations are indicated. (B–I), Data show mean of the indicated number of experiments, errors are s.e.m.

## Discussion

In our study, we have investigated the mechanistic basis of ion selectivity in the SLC11/NRAMP family. Whereas the bulk of the family efficiently transports divalent transition metal ions such as Fe2+ or Mn2+ from a high background of alkaline earth metal ions, there is an extended clade of the family in prokaryotes that has evolved as transport systems of the divalent cation Mg2+ and that were thus termed NRAMP related Mg2+ transporters (NRMTs) (Shin et al., 2014, Figure 1). These proteins are characterized by a distinct signature of residues constituting the ion binding site, located in the center of the protein in the unwound parts of the pseudo-symmetry related transmembrane helices α1 and α6 (Figures 1 and 7). We thus initially investigated whether we would be able to confer the capability to transport Mg2+ to a transition metal ion transporter by mutation of its ion binding site.

The most striking difference in the ion binding site of both clades of the NRAMP family concerns the position of a conserved methionine that serves as a soft ligand for the interaction with transition metal ions, which is replaced by an alanine in NRMTs (Figure 1). The mutation of this residue in the classical NRAMP EcoDMT only moderately affected its capability to transport Mn2+ and instead exerted its pronounced effect by converting Ca2+ into a transported substrate (Figure 2A–H). This emphasizes the primary role of this residue to disfavor binding of this ubiquitous alkaline earth metal ion, which was already proposed in a previous study (Bozzi et al., 2016a). Similarly, an EcoDMT mutant where all three deviating residues of the binding site were mutated to their correspondents found in NRMTs was still efficient in Mn2+ transport (Figure 2E), thus suggesting that, among divalent cations, the transport of transition metal ions might not depend on stringent structural prerequisites. In contrast to Ca2+, neither of the mutants converted EcoDMT into a Mg2+ transporter (Figure 2D and K), thus suggesting that the transport of latter might require specific features to cope with the unique chemical properties of this ion. Among divalent cations of biological relevance, Mg2+ is distinguished by its small ionic radius, which results in an unusually strong interaction with the surrounding water molecules that would render its dehydration during transport energetically costly (Persson, 2010). The first hydration shell of Mg2+, which coordinates the ion in an octahedral geometry (Figure 9A), was thus suggested to remain bound to the ion in its initial encounter with the binding site and probably also during transport. A similar feature was indeed observed in the structures of the unrelated bacterial Mg2+ transport proteins MgtE (Takeda et al., 2014) and CorA (Guskov et al., 2012) whereas protein interactions in the membrane-inserted domain of the transporter CorC are established with a fully dehydrated ion (Huang et al., 2021).

![Figure 9.](https://cdn.elifesciences.org/articles/74589/elife-74589-fig9-v2.jpg)

**Figure 9.:** Schematic depiction of (A), the octahedral coordination of the first hydration shell surrounding a Mg2+ ion and (B), the same octahedral coordination within the binding site of a NRMT with five of the six water molecules remaining bound to the ion and where the bulk of protein interactions with the ion are mediated via coordinated water. (C) Model of Mg2+ bound to the site of EleNRMT in the inward-facing conformation. The coordinates of the hydrated Mg2+ were obtained from the high-resolution structure of the Mg2+ transporter MgtE (PDBID 4U9L). The Mg2+ ion was placed on the position of Mn2+ obtained from the anomalous difference density defined in the X-ray structure. A single water molecule with a backbone oxygen atom was removed and the remaining complex was oriented to maximize interactions of coordinating waters with protein residues. Regions of the binding site are represented as Cα-trace and selected interacting residues as sticks. (D) Schematic depiction from an inward-facing to an occluded conformation of a NRMT with bound hydrated Mg2+ indicated. (E) Hypothetical model of the transition of EleNRMT from an inward-facing (gray) to an occluded conformation (colored) that was based on the occluded conformation of DraNRAMP (PDBID: 6C3I). (F) Close-up of the binding pocket of the hypothetical model of the occluded conformation with bound Mg2+–5H2O complex.

The distinct requirements for Mg2+ transport are reflected in the properties of EleNRMT investigated in this study. Its capability to transport Mn2+ (Figure 3A–D and G) underlines the described promiscuity of this ion in its interaction with proteins. In contrast, our studies have shown transport of Mg2+ but not Ca2+ (Figures 3E, F, H ,, 4A–E) thus illustrating that both ions rely on distinct features of the protein which mediate their interaction. These are illustrated in the structure of EleNRMT in an inward-facing conformation determined by cryo-EM (Figures 5 and 6). In this structure, a wide aqueous cavity leads to an ion binding site whose spacious volume would preclude simultaneous interaction with a completely dehydrated ion (Figures 6C, 7B and C). The larger size of the site is an immediate consequence of the decreased side chain-volume of the surrounding residues concomitant with local differences in the backbone positions (Figure 7A and B), which explains why it was impossible to convert EcoDMT into a Mg2+ transporter upon mutation of respective residues (Figure 2D, I, K). The position of a Mn2+ ion bound to EleNRMT was defined by its anomalous difference density in a crystal structure of the protein (Figure 5C). Since Mn2+ shows a similar octahedral coordination as Mg2+, although with weaker affinity to the surrounding waters, we assume Mg2+ to bind in an equivalent manner, which is also reflected in the presence of residual density in a dataset determined at high Mg2+ concentration by cryo-EM (Figure 5—figure supplement 5E). Although the limited resolution of our structures does not permit assignment of water molecules, an octahedral Mg2+-water complex model placed in the binding site suggests that only one of the solvent molecules would be substituted by a direct interaction with the oxygen of the amide backbone group of Thr 224, whereas other interactions with the conserved binding site would be mediated by coordinating waters (Figure 9B and C). The detailed structural properties of this cavity are expected to change upon a transition from an inward-open into an occluded intermediate conformation, which was observed in the corresponding structure of DraNRAMP, where the access of the binding site to the cytoplasm is closed (Bozzi et al., 2019b). However, in contrast to DraNRAMP, where the bound ion becomes tightly encircled by protein residues, the distinct structural features of EleNRMT and the lower side chain volume of residues of its binding site suggest that this cavity would be sufficiently big for Mg2+ to retain much of its surrounding water during transport (Figure 9D–F) thus emphasizing that it is the larger hydrated complex of Mg2+ rather than the naked ion that is relevant for transport.

A second pronounced feature that distinguishes EleNRMT and likely other NRMTs from classical SLC11 proteins concerns the absent coupling of metal ion transport to an energy source, which in case of NRAMPs is conferred by the cotransport of protons (Ehrnstorfer et al., 2017; Gunshin et al., 1997; Figure 4F–H). This property is reflected in the location of ionizable residues that are conserved within the proton-coupled part of the family and that are absent in EleNRMT (Figure 7E and F). It thus appears that in light of the high extracellular Mg2+ concentration and the inside negative membrane potential such coupling may not be required for efficient uptake in the natural habitat of the bacterium.

Collectively, the presented study has provided detailed mechanistic insight into the structural basis of Mg2+ transport in homologues of the SLC11/NRAMP family and it has confirmed previous results that have proposed this role based on biochemical considerations (Shin et al., 2014). Our work also illustrates the promiscuity of transition metal ion transport, which contrasts the tight requirements for the alkaline earth metal ions such as Ca2+ and Mg2+, latter of which is transported in a largely hydrated state. The observation that the previously investigated NRMT homologue did not permit growth upon Mn2+ -limitation (Shin et al., 2014) could be a consequence of the lower affinity to this ion, the competition with abundant Mg2+ and the absence of an energy source, which might be mandatory for efficient accumulation of the scarce substrate. Our study illustrates the specific requirements for the transport of Mg2+ which are not met by classical NRAMP transporters. In this respect, it appears unlikely that the human transporter SLC11A1, which resides in the phagosomes of macrophages and is involved in the immune response against invading microbes, would itself permit Mg2+ transport as suggested in a recent study (Cunrath and Bumann, 2019).

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
      <td>Chemical compound, drug</td>
      <td>1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-(1'rac-glycerol) (18:1 06:0 POPG)</td>
      <td>Avanti Polar Lipids</td>
      <td>840457 C</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>E. coli polar extract</td>
      <td>Avanti Polar Lipids</td>
      <td>100600 P</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>1-palmitoyl-2-oleoyl-sn-glycero-3-phosphoethanolamine (18:1 06:0 POPE)</td>
      <td>Avanti Polar Lipids</td>
      <td>850757 C</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Triton X-100</td>
      <td>Sigma</td>
      <td>Cat#T9284</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Lysozyme</td>
      <td>Applichem</td>
      <td>Cat#A3711</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Benzamidine</td>
      <td>Sigma</td>
      <td>B6506</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Chloroform</td>
      <td>Fluka</td>
      <td>25,690</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DM</td>
      <td>Anatrace</td>
      <td>D322</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DDM</td>
      <td>Anatrace</td>
      <td>D310S</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Diethyl ether</td>
      <td>Sigma</td>
      <td>296,082</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>DNase I</td>
      <td>AppliChem</td>
      <td>A3778</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>glycerol 99%</td>
      <td>Sigma</td>
      <td>G7757</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HCl</td>
      <td>Merck Millipore</td>
      <td>1.00319.1000</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>HEPES</td>
      <td>Sigma</td>
      <td>H3375</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Imidazole</td>
      <td>Roth</td>
      <td>X998.4</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>L-(+)-arabinose</td>
      <td>Sigma</td>
      <td>A3256</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Leupeptin</td>
      <td>AppliChem</td>
      <td>A2183</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Pepstatin</td>
      <td>AppliChem</td>
      <td>A2205</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Valinomycin</td>
      <td>Thermofischer Scientific</td>
      <td>V1644</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Calcimycin</td>
      <td>Thermofischer Scientific</td>
      <td>A1493</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Ionomycin</td>
      <td>Thermofischer Scientific</td>
      <td>I24222</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Fura2</td>
      <td>Thermofischer Scientific</td>
      <td>F1200</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Magnesium Green</td>
      <td>Thermofischer Scientific</td>
      <td>M3733</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>ACMA</td>
      <td>Thermofischer Scientific</td>
      <td>A1324</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>CCCP</td>
      <td>Sigma</td>
      <td>C2759</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Calcein</td>
      <td>Thermofischer Scientific</td>
      <td>C481</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Phosphate buffered saline</td>
      <td>Sigma</td>
      <td>D8537</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PEG400</td>
      <td>Sigma</td>
      <td>91,893</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Manganese acetate</td>
      <td>Sigma</td>
      <td>330,825</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Magnesium acetate</td>
      <td>Fluka</td>
      <td>63,047</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Calcium Chloride</td>
      <td>Sigma</td>
      <td>223,506</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Manganese Chloride</td>
      <td>Fluka</td>
      <td>31,422</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Magnesium Chloride</td>
      <td>Fluka</td>
      <td>63,065</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>PMSF</td>
      <td>Sigma</td>
      <td>P7626</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Potassium chloride</td>
      <td>Sigma</td>
      <td>746,346</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium chloride</td>
      <td>Sigma</td>
      <td>71,380</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Terrific broth</td>
      <td>Sigma</td>
      <td>T9179</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>4%–20% Mini-PROTEAN TGX Precast Protein Gels, 15-well, 15 µl</td>
      <td>BioRad Laboratories</td>
      <td>4561096DC</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Amicon Ultra-4 Centrifugal Filters Ultracel 10 K, 4 ml</td>
      <td>Merck Millipore</td>
      <td>UFC801096</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Amicon Ultra-4 Centrifugal Filters Ultracel 50 K, 4 ml</td>
      <td>Merck Millipore</td>
      <td>UFC805096</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Amicon Ultra-4 Centrifugal Filters Ultracel 100 K, 4 ml</td>
      <td>Merck Millipore</td>
      <td>UFC810024</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Biobeads SM-2 adsorbents</td>
      <td>BioRad Laboratories</td>
      <td>152–3920</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Avestin Extruder kit</td>
      <td>Sigma</td>
      <td>Cat#Z373400</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>400 nm polycarbonate filters</td>
      <td>Sigma</td>
      <td>Cat#Z373435</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>96-well black walled microplates</td>
      <td>Thermofischer Scientific</td>
      <td>Cat#M33089</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Ni-NTA resin</td>
      <td>ABT Agarose Bead Technologies</td>
      <td>6BCL-NTANi-X</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuantiFoil R1.2/1.3 Au 200 mesh</td>
      <td>Electron Microscopy Sciences</td>
      <td>Q2100AR1.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superdex 200 10/300 GL</td>
      <td>Cytiva</td>
      <td>17517501</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superdex 200 Increase 3.2/300</td>
      <td>Cytiva</td>
      <td>28990946</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superdex 200 Increase 5/150 GL</td>
      <td>Cytiva</td>
      <td>28990945</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Superdex 75 10/300 GL</td>
      <td>Cytiva</td>
      <td>17517401</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>BioQuantum Energy Filter</td>
      <td>Gatan</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HPL6</td>
      <td>Maximator</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>K3 Direct Detector</td>
      <td>Gatan</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Titan Krios G3i</td>
      <td>ThermoFisher Scientific</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Viber Fusion FX7 imaging system</td>
      <td>Witec</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>TECAN M1000 Infinite</td>
      <td>TECAN</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Vitrobot Mark IV</td>
      <td>ThermoFisher Scientific</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>μDAWN MALS Detector</td>
      <td>Wyatt Technology</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>gDNA Eggerthella lenta</td>
      <td>DSMZ</td>
      <td>2,243</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>gDNA Eremococcus coleocola</td>
      <td>DSMZ</td>
      <td>15,696</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Bacterial expression vector with C-terminal 3 C cleavage site, GFP-tag and His-tag</td>
      <td>Dutzler laboratory</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Bacterial expression vector with N-terminal His-tag and 3 C cleavage site</td>
      <td>Dutzler laboratory</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Bacterial expression vector with N terminal pelB sequence, His-tag, MBP, 3 C cleavage site</td>
      <td>Dutzler laboratory</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant protein</td>
      <td>HRV 3 C protease</td>
      <td>Expressed (pET_3 C) and purified in Dutzler laboratory</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>3DFSC</td>
      <td>Tan et al., 2017</td>
      <td>https://3dfsc.salk.edu/</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ASTRA7.2</td>
      <td>Wyatt Technology</td>
      <td>https://www.wyatt.com/products/software/astra.html</td>
      <td>RRID:SCR_016255</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Chimera v.1.15</td>
      <td>Pettersen et al., 2004</td>
      <td>https://www.cgl.ucsf.edu/chimera/</td>
      <td>RRID:SCR_004097</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ChimeraX v.1.1.1</td>
      <td>Pettersen et al., 2021</td>
      <td>https://www.rbvi.ucsf.edu/chimerax/</td>
      <td>RRID:SCR_015872</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot v.0.9.4</td>
      <td>Emsley et al., 2010</td>
      <td>https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/</td>
      <td>RRID:SCR_014222</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>cryoSPARC v.3.0.1/v.3.2.0</td>
      <td>Structural Biotechnology Inc.</td>
      <td>https://cryosparc.com/</td>
      <td>RRID:SCR_016501</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DINO</td>
      <td></td>
      <td>http://www.dino3d.org</td>
      <td>RRID:SCR_013497</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EPU2.9</td>
      <td>ThermoFisher Scientific</td>
      <td>NA</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix</td>
      <td>Liebschner et al., 2019</td>
      <td>https://www.phenix-online.org/</td>
      <td>RRID:SCR_014224</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>RELION 3.0.7</td>
      <td>Zivanov et al., 2018</td>
      <td>https://www3.mrc-lmb.cam.ac.uk/relion/</td>
      <td>RRID:SCR_016274</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>JALVIEW</td>
      <td>Waterhouse et al., 2009</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Muscle</td>
      <td>Edgar, 2004</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (E coli)</td>
      <td>E. coli MC1061</td>
      <td>ThermoFisher Scientific</td>
      <td>C66303</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Phylogenetic analysis of the SLC11 family

The protein sequences of ScaDMT (UniprotKB A0A4U9TNH6), EcoDMT (UniprotKB E4KPW4), hDMT1 (UniprotKB P49281), OsNRAT1 (Uniprot KB Q6ZG85), CabNRMT-c0685 (UniprotKB Q97L77), and CabNRMT-c3329 (UniprotKB Q97DZ1) were respectively used as query sequences in BLASTp searches in diverse sequence databases. In that manner, 1100 eukaryotic and 447 prokaryotic standard SLC11 transporters and 745 prokaryotic NRMTs were selected and aligned with CLC Main Workbench (QIAGEN). The identity of the 745 prokaryotic NRMTs was confirmed by individual inspection of the proposed ion binding site. A multiple sequence alignment was used to generate a phylogenetic tree using the neighbor joining cluster generation method. Protein distances were measured using a Jukes-Cantor model and a Bootstrapping analysis was performed with 100 replicates.

### Expression and purification of EcoDMT

EcoDMT and its mutants were expressed and purified as described previously (Ehrnstorfer et al., 2017). Briefly, the vector EcoDMT-pBXC3GH (Invitrogen) was transformed into E. coli MC1061 cells and a preculture was grown in TB-Gly medium overnight using ampicillin (100 μg/ml) as a selection marker for all expression cultures. The preculture was used at a 1:100 volume ratio for inoculation of TB-Gly medium. Cells were grown at 37 °C to an OD600 of 0.7–0.9, after which the temperature was reduced to 25 °C. Protein expression was induced by addition of arabinose to a final concentration of 0.004% (w/v) for 12–14 hr at 18 °C. Cells were harvested by centrifugation for 20 min at 5,000 g, resuspended in buffer RES (200 mM NaCl, 50 mM KPi pH 7.5, 2 mM MgCl2, 40 μg/ml DNAseI, 10 μg/ml lysozyme, 1 μM leupeptin, 1 μM pepstatin, 0.3 μM aprotinin, 1 mM benzamidine, 1 mM PMSF) and lysed using a high pressure cell lyser (Maximator HPL6). After a low-speed spin (10,000 g for 20 min), the supernatant was subjected to a second centrifugation step (200,000 g for 45 min). The pelleted membrane was resuspended in buffer EXT (200 mM NaCl, 50 mM KPi pH 7.5, 10% glycerol) at a concentration of 0.5 g of vesicles per ml of buffer. The purification of EcoDMT and its mutants was carried out at 4 °C. Isolated membrane fractions were diluted 1:2 in buffer EXT supplemented with protease inhibitors (Roche cOmplete EDTA-free) and 1% (w/v) n-decyl-β-D-maltopyranoside (DM, Anatrace). The extraction was carried out under gentle agitation for 2 hr at 4 °C. The lysate was cleared by centrifugation at 200,000 g for 30 min. The supernatant supplemented with 15 mM imidazole at pH 7.5 was subsequently loaded onto NiNTA resin and incubated for at least 1 hr under gentle agitation. The resin was washed with 20 column volumes (CV) of buffer W (200 mM NaCl, 20 mM HEPES pH 7, 10% Glycerol, 50 mM imidazole pH 7.5, 0.25% (w/v) DM) and the protein was eluted with buffer ELU (200 mM NaCl, 20 mM HEPES pH 7, 10% Glycerol, 200 mM imidazole pH 7.5, 0.25% (w/v) DM). Tag cleavage proceeded by addition of HRV 3 C protease at a 3:1 molar ratio and dialysis against buffer DIA (200 mM NaCl, 20 mM HEPES pH7, 10% Glycerol, 0.25% (w/v) DM) for at least 2 hr at 4 °C. After application to NiNTA resin to remove the tag, the sample was concentrated by centrifugation using a 50 kDa molecular weight cut-off concentrator (Amicon) and further purified by size exclusion chromatography using a Superdex S200 column (GE Healthcare) pre-equilibrated with buffer SEC (200 mM NaCl, 20 mM HEPES pH 7, 0.25% (w/v) DM). The peak fractions were pooled, concentrated, and used directly without freezing.

### Expression screening of NRMT homologues

The DNA coding for NRMTs from 82 bacterial and archaeal strains were cloned from gDNA (obtained from DSMZ) into pBXNHG3 or pBXC3H vectors (Invitrogen) using FX cloning (Geertsma and Dutzler, 2011) providing a final construct where an NRMT contains a 10-His tag, a GFP and a HRV 3 C protease cleavage site fused to its N-terminus (pBXNHG3) or a HRV 3 C protease cleavage site and a 10-His tag fused to its C-terminus (pBXC3H). Both vectors contain an arabinose promoter and an ampicillin resistance gene. Consequently, all cultures were supplemented with 100 μg/ml ampicillin as selection marker. The vectors were transformed into E. coli MC1061 cells and precultures were grown in Terrific Broth (TB) medium overnight. The small-scale expression was performed in 24-well plates with gas permeable adhesive covers in TB medium supplemented with 0.5% glycerol (TB-Gly). Each culture was inoculated at a 1:100 volume ratio. The cells were grown at 37 °C to an OD600 of 0.7–0.9, before the temperature was reduced to 25 °C. The expression was induced by addition of arabinose to a final concentration of 0.001% (w/v) for 12–14 hr at 18 °C. Cells were harvested by centrifugation for 20 min at 5,000 g, resuspended in 400 μl of lysis buffer (200 mM NaCl, 50 mM KPi pH 7.5, 2 mM MgCl2, 40 μg/mL DNAseI, 1 μM leupeptin, 1 μM pepstatin, 0.3 μM aprotinin, 1 mM benzamidine, 1 mM PMSF). Cells were lysed by disruption using sharp 500 μm glass beads. The supernatant was supplemented with DDM at a final concentration of 1% (w/v) and incubated for 1 hr at 4 °C under gentle agitation. The whole-cell extract was clarified by centrifugation at 200,000 g for 15 min and expressed proteins not containing a fusion to a fluorescent protein were detected by western blots. Constructs fused to a fluorescent protein were detected by in-gel fluorescence imaging (Geertsma et al., 2008a) and fluorescence size exclusion chromatography (FSEC) (Kawate and Gouaux, 2006) using a Superdex S200 column connected to an Agilent HPLC system (GE Healthcare) (λex=489 nm / λem=510 nm). The NRMT homologue (WP_114552427.1) from the prokaryote Eggerthella lenta (DSM 2243, EleNRMT) was selected as the biochemically best-behaved homologue based on the profile of the eluted peak. The stability of EleNRMT was further improved by mutagenesis. To this end, consensus amino acids were identified using JALVIEW (Waterhouse et al., 2009) from aligned sequences of representative NRMT homologs, using Muscle (Edgar, 2004), and reported criteria (Cirri et al., 2018).

### Expression and purification of EleNRMT

For large-scale overexpression, the DNA coding for the NRMT from the prokaryote Eggerthella lenta (EleNRMT) was cloned into the pBXNH3 vector (Invitrogen) using the FX cloning technique (Geertsma and Dutzler, 2011) providing a construct where EleNRMT contains a 10-His tag and a HRV 3 C protease cleavage site at its N-terminus. All mutants were generated using the Quickchange site-direct mutagenesis method (Agilent). The vector was transformed into E. coli MC1061 cells and a preculture was grown in TB-Gly medium overnight using ampicillin (100 μg/ml) as a selection marker for all expression cultures. The preculture was diluted at 1:100 volume ratio into TB-Gly medium. The cells were grown at 37 °C to an OD600 of 0.7–0.9, before the temperature was lowered to 25 °C. The expression was induced by addition of arabinose to a final concentration of 0.0045% (w/v) for 12–14 hr at 18 °C. Cells were harvested by centrifugation for 20 min at 5,000 g, resuspended in buffer RES and disrupted using a high-pressure cell lyser (Maximator HPL6). After low spin centrifugation (10,000 g for 20 min) to remove cell debris, the supernatant was subjected to an ultracentrifugation step (200,000 g for 45 min) and the pelleted membrane was resuspended in buffer EXT at a concentration of 0.5 g of vesicles per ml of buffer. The purification of EleNRMT and its mutants was carried out at 4 °C. Suspended membrane vesicles were diluted 1:2 in buffer EXT supplemented with protease inhibitors (Roche cOmplete EDTA-free) and 1% (w/v) detergent, depending on the purpose of the experiments. DDM (Anatrace) was used as detergent for proteoliposome-reconstitution and cryoEM sample preparation and DM (Anatrace) for ITC and crystallization. The extraction was carried out under gentle agitation for 2 hr at 4 °C. The lysate was cleared by centrifugation at 200,000 g for 30 min. The supernatant supplemented with 15 mM of imidazole at pH 7.5 was loaded onto NiNTA resin and incubated for at least 1 hr under gentle agitation. During later stages of purification, the detergent concentration was reduced to 0.04% (w/v) for DDM or 0.25% (w/v) for DM. The resin was washed with 20 CV of buffer W and protein was eluted with buffer ELU, both containing the respective detergent. The tag was cleaved by addition of HRV 3 C protease at a 3:1 molar ratio and dialyzed against buffer DIA containing the respective detergent for at least 2 hr at 4 °C. After addition of NiNTA resin to remove the cleaved tag, the sample was concentrated by centrifugation using a 50 kDa molecular weight cut-off concentrator (Amicon) and further purified by size exclusion chromatography on a Superdex S200 column (GE Healthcare) pre-equilibrated with buffer SEC containing the respective detergent. The peak fractions were pooled, concentrated, and used immediately for further experiments.

### Thermal stability assay using fluorescence-detection size-exclusion chromatography

The assay was performed following a published protocol (Hattori et al., 2012). Aliquots of 50 μl at 1 μM of EleNRMT and EleNRMTts in 200 mM NaCl, 20 mM HEPES pH7, 0.04% DDM were incubated at temperatures up to 75 °C for 10 min. Aggregated protein was removed by centrifugal filtration (0.22 μm) and 25 μl of the sample was subsequently loaded onto a Superdex S200 column (GE Healthcare) equilibrated in 200 mM NaCl, 20 mM HEPES pH7, 0.04% DDM and coupled to a fluorescence detector (Agilent technologies 1200 series, G1321A). The proteins were detected using tryptophan fluorescence (λex=280 nm; λem=315 nm) and stability was assessed by measuring the peak height of the monomeric peaks. The peak heights were normalized to the corresponding value from samples incubated at 4 °C (100% stability) and melting temperatures (Tm) were determined by fitting the curves to a sigmoidal dose-response equation.

### Reconstitution of EleNRMT and EcoDMT into proteoliposomes

EleNRMT, EcoDMT and all of their mutants were reconstituted into detergent-destabilized liposomes (Geertsma et al., 2008b). The lipid mixture made of POPE, POPG (Avanti Polar Lipids) at a weight ratio of 3:1: was washed with diethylether and dried under a nitrogen stream followed by exsiccation overnight. The dried lipids were resuspended in 100 mM KCl and 20 mM HEPES at pH7. After three freeze-thaw cycles, the lipids were extruded through a 400 nm polycarbonate filter (Avestin, LiposoFast-BAsic) and aliquoted into samples with a concentration of 45 mg/ml. The extruded lipids were destabilized by adding Triton X-100 and the protein was reconstituted at a lipid to protein ratio (w/w) of 50. After several incubation rounds with biobeads SM-2 (Biorad), the proteoliposomes were harvested the next day, resuspended in 100 mM KCl and 20 mM HEPES pH7 and stored at –80 °C.

### Isothermal titration calorimetry

A MicroCal ITC200 system (GE Healthcare) was used for Isothermal titration calorimetry experiments. All titrations were performed at 6 °C in buffer SEC (200 mM NaCl, 20 mM HEPES pH7, 0.25% DM). The syringe was filled with 3 mM MnCl2 or MgCl2 and the titration was initiated by the sequential injection of 2 μl aliquots into the cell filled with EleNRMT or mutants at a concentration of 70 μM. Data were analyzed with the Origin ITC analysis package and fitted assuming a single binding site for metal ions and a stoichiometry of N = 1. Each experiment was repeated twice from independent protein purifications with similar results. Experiments with buffer not containing any protein were performed as controls.

### Fluorescence-based substrate transport assays

Proteoliposomes were incubated with buffer IN (100 mM KCl, 20 mM HEPES pH 7) containing either 250 μM Calcein (Invitrogen), 100 μM Fura-2 (ThermoFischer Scientific), or 400 μM MagGreen (ThermoFischer Scientific) depending on the assayed ion. After three cycles of freeze-thawing, the liposomes were extruded through a 400 nm filter and the proteoliposomes were centrifuged and washed three times with buffer IN not containing any fluorophores. The proteoliposomes at a concentration of 25 mg/ml were subsequently diluted 1:100 to a final concentration of 0.25 mg/ml in buffer OUT (100 mM NaCl, 20 mM HEPES pH7) and aliquoted in 100 μl batches into a 96-well plate (ThermoFischer Scientific) and the fluorescence was measured every 4 s using a Tecan Infinite M1000 fluorimeter. A negative membrane potential of –118 mV was established after addition of valinomycin to a final concentration of 100 nM as a consequence of the 100-fold outwardly directed K+ gradient. After 20 cycles of incubation, the substrate was added at different concentrations. The transport reaction was terminated by addition of calcimycin or ionomycin at a final concentration of 100 nM. The initial rate of transport was calculated by linear regression within the initial 100 s of transport after addition of the substrate. The calculated values were fitted to a Michaelis-Menten equation. Fura-2 was used to assay the transport of Ca2+. For detection, the ratio between calcium bound Fura-2 (λex=340 nm; λem=510 nm) and unbound Fura-2 (λex=380 nm; λem=510 nm) was monitored during kinetic measurements. Calcein was used to assay the transport of Mn2+ (λex=492 nm; λem=518 nm) and Magnesium Green was to assay the transport of Mg2+ (λex=506 nm; λem=531 nm).

For assaying coupled proton transport, a proteoliposome stock of 15 mg/ml in 100 mM KCl, 5 mM HEPES pH 7, 50 μM ACMA was prepared. After clarification by sonication, the proteoliposomes were diluted 1–100 to a concentration of 0.15 mg/ml in 100 mM NaCl, 5 mM HEPES pH7 and aliquoted into batches of 100 μl into a flat black 96-well plate (ThermoFischer Scientific). The fluorescence was measured every 4 s using a fluorimeter Tecan Infinite M1000 (λex=412 nm; λem=482 nm). The transport reaction was initiated after addition of the substrate and valinomycin at a final concentration of 100 nM resulting in the same negative membrane potential of –118 mV as applied in assays that monitor transport of the metal ions. The reaction was terminated by addition of CCCP at 100 nM.

### Generation of nanobodies specific to EleNRMT

EleNRMT specific nanobodies were generated using a method described previously (Pardon et al., 2014). Briefly, an alpaca was immunized four times with 200 µg of detergent solubilized EleNRMTts. Two days after the final injection, the peripheral blood lymphocytes were isolated and the total RNA fraction was extracted and converted into cDNA by reverse transcription. The nanobody library was amplified and cloned into the phage display pDX vector (Invitrogen). After two rounds of phage display, ELISA assays were performed on the periplasmic extract of 198 individual clones. Three nanobodies were identified. For all steps of phage display and ELISA, an enzymatically biotinylated version of EleNRMT with an additional Avi tag on its N-terminus (Avi-10His-3C) was used (Fairhead and Howarth, 2015) and bound to neutravidin coated plates. The biotinylation was confirmed by total mass spectrometry analysis.

### Expression and purification of nanobodies and preparation of the EleNRMTts-Nb1,2 complex

All nanobodies were cloned into the pBXNPHM3 vector (Invitrogen) using the FX cloning technique. The expression construct contains the nanobody with a fusion of a pelB sequence, a 10-His tag, a maltose-binding protein (MBP) and a HRV 3 C protease site to its N-terminus. The vector was transformed into E. coli MC1061 cells and a preculture was grown in TB-Gly medium overnight using ampicillin (100 μg/ml) as a selection marker in all expression cultures. The preculture was used for inoculation of TB-Gly medium at 1:100 volume ratio. Cells were grown to an OD600 of 0.7–0.9 and the expression was induced by addition of arabinose to a final concentration of 0.02% (w/v) for 4 hr at 37 °C. Cells were harvested by centrifugation for 20 min at 5000 g, resuspended in buffer A (200 mM KCl, 50 mM KPi pH 7.5, 10% Glycerol, 15 mM imidazole pH 7.5, 2 mM MgCl2, 1 μM leupeptin, 1 μM pepstatin, 0.3 μM aprotinin, 1 mM benzamidine, 1 mM PMSF) and lysed using a high pressure cell lyser (Maximator HPL6). The purification of all nanobodies was carried out at 4 °C. The lysate was cleared by centrifugation at 200,000 g for 30 min. The supernatant was loaded onto NiNTA resin and incubated for at least 1 hr under gentle agitation. The resin was washed with 20 CV of buffer B (200 mM KCl, 20 mM Tris-HCl pH 8, 10% Glycerol, 50 mM imidazole, pH 7.5). The protein was eluted with buffer C (200 mM KCl, 20 mM Tris-HCl pH 8, 10% Glycerol, 300 mM imidazole, pH 7.5). The tag was cleaved by addition of HRV 3 C protease at a 3:1 molar ratio and dialyzed against buffer D (200 mM KCl, 20 mM Tris-HCl pH 8, 10% Glycerol) for at least 2 hr at 4 °C. After application of NiNTA resin to remove the tag, the sample was concentrated by centrifugation using a 10 kDa molecular weight cut-off concentrator (Amicon) and further purified by size exclusion chromatography using a Superdex S200 column (GE Healthcare) pre-equilibrated with buffer E (200 mM KCl, 20 mM Tris-HCl pH 8). The peak fractions were pooled, concentrated and flash-frozen and stored at –20 °C for subsequent experiments.

Following the purification of EleNRMT in DDM (for cryoEM data collection) or DM (for crystallization) as described, the purified membrane protein and nanobodies Nb1 and Nb2 were incubated at a 1:1.3:1.3 molar ratio for 30 min and the complex was further purified by size exclusion chromatography on a Superdex S200 column (GE Healthcare), pre-equilibrated in the same SEC buffer as used for EleNRMT purification. The sample was subsequently concentrated to 3.5 mg/ml (for cryoEM) or 8–12 mg/ml (for crystallization).

### Cryo-EM sample preparation and data collection

For sample preparation for cryo-EM, 2.5 μl of the complex were applied to glow-discharged holey carbon grids (Quantifoil R1.2/1.3 Au 200 mesh). Samples were blotted for 2–4 s at 4 °C and 100% humidity. The grids were frozen in liquid propane-ethane mix using a Vitrobot Mark IV (Thermo Fisher Scientific). For the dataset in presence of Mg2+, the sample was supplemented with 10 mM MgCl2 and incubated on ice for 20 min before grid preparation. All datasets were collected on a 300 kV Titan Krios (ThermoFischer Scientific) with a 100 μm objective aperture and using a post-column BioQuantum energy filter with a 20 eV slit and a K3 direct electron detector in super-resolution mode. All datasets were recorded automatically using EPU2.9 with a defocus ranging from –1–2.4 μm, a magnification of 130,000 x corresponding to a pixel size of 0.651 Å per pixel (0.3255 Å in super resolution mode) and an exposure of 1.01 s (36 frames). Three datasets were collected for EleNRMT-Nb1,2 without Mg2+with respective total doses of 69.725, 61 and 69.381 e-/Å2 and for EleNRMT-Nb1,2 with Mg2+ one dataset with a total dose of 69.554 e-/Å2.

### Cryo-EM data processing

Datasets were processed using Cryosparc v3.2.0 (Punjani et al., 2017) following the same processing pipeline (Figure 5—figure supplements 1 and 2). All movies were subjected to motion correction using patch motion correction with a fourier crop factor of 2 (pixel size of 0.651 Å/pix). After patch CTF estimation, high quality micrographs were identified based on relative ice thickness, CTF resolution and total full frame motion and micrographs not meeting the specified criteria were rejected. For the EleNRMTts-Nb1,2 complex, a partial dataset (981 micrographs) was used to generate a low-resolution 3D ab initio model. For this purpose, particles were selected using a blob picker with a minimum particle diameter of 160 Å and a minimum inter-particle distance of 64 Å. The selected particles were extracted with a box size of 360 pixels and binned 4 x (pixel size of 2.64 Å per pixel). These particles were initially used to generate 2D classes and later for template-driven particle picking. After extraction and 2D classification, an initial 3D ab initio model was generated in Cryosparc. This model was subsequently used to generate 2D templates for particle picking on the remainder of the dataset.

The 2D classes generated from particles selected from the entire dataset were extracted using a box size of 360 pix and down-sampled to 180 pixels (pixel size of 1.32 Å/pix). These particles were used for generation of 4 ab initio classes. Promising ab initio models were selected based on visual inspection and subjected to heterogenous refinement using one of the selected models as ‘template’ and an obviously bad model as decoy model. After several rounds of heterogenous refinement, the selected particles and models were subjected to non-uniform refinement (input model filtering to 8 Å) followed by local CTF refinement and another round of non-uniform refinement. Finally, the maps were sharpened using the sharpening tool from the Cryosparc package. The quality of the map was evaluated validated using 3DFSC (Tan et al., 2017) for FSC validation and local resolution estimation.

### Cryo-EM model building and refinement

Model building was performed in Coot (Emsley and Cowtan, 2004). Initially, the structure of ScaDMT (PDB 5M94) was rigidly fitted into the densities and served as template for map interpretation. The quality of the map allowed for the unambiguous assignment of residues 43–438. The structure of Nb16 (PDB 5M94) was used to build Nb1 and Nb2. The model was iteratively improved by real space refinement in PHENIX (Afonine et al., 2018) maintaining secondary structure constrains throughout. Figures were generated using ChimeraX (Pettersen et al., 2021) and Dino (http://www.dino3d.org). Surfaces were generated with MSMS (Sanner et al., 1996).

### Crystallization and X-ray structure determination of the EleNRMTts-Nb1,2 complex

The EleNRMTts-Nb1,2 complex was purified in DM as described before, supplemented with E. coli polar lipids solubilized in DM to a final concentration of 100 µg/ml and used for the preparation of vapor diffusion crystallization experiments in sitting drops by mixing 150 nl of the concentrated protein with 150 nl of the mother liquor containing 50 mM MgAc, 50 mM HEPES pH 7.2–7.6 and 25–30% PEG400. Crystals grew after 4 days and reached a maximum size of 0.2 × 0.3 x 0.3 mm after 12 days. The crystals were fished, cryoprotected by soaking into mother liquor supplemented with PEG400 to a final concentration of 35% and flash frozen into liquid nitrogen.

All data sets were collected on frozen crystals on either the X06SA or the X06DA beamline at the Swiss Light Source of the Paul Scherrer Institute (SLS, Villingen) on an EIGER 16 M or PILATUS 2 M-F detector (Dectris), respectively. Anomalous data were collected at the absorption edge of manganese (1.896 Å). Integration and scaling was performed using XDS (Kabsch, 1993) and data were further processed with CCP4 programs (CCP4, 1994). Phases were obtained by molecular replacement in Phaser (McCoy et al., 2007). For the ternary complex EleNRMT- Nb1-Nb2, the refined cryoEM structure was used as search model for the respective datasets. Structures were refined in PHENIX (Liebschner et al., 2019) maintaining tight coordinate restraints and models were inspected and modified in Coot (Emsley and Cowtan, 2004).
