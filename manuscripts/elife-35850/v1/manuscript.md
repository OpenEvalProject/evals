# Viral GPCR US28 can signal in response to chemokine agonists of nearly unlimited structural degeneracy

## Authors

- Timothy F Miles<sup>1</sup> ([ORCID: 0000-0001-6591-3271](https://orcid.org/0000-0001-6591-3271))
- Katja Spiess<sup>3</sup>
- Kevin M Jude<sup>1</sup> ([ORCID: 0000-0002-3675-5136](https://orcid.org/0000-0002-3675-5136))
- Naotaka Tsutsumi<sup>1</sup> ([ORCID: 0000-0002-3617-7145](https://orcid.org/0000-0002-3617-7145))
- John S Burg<sup>1</sup>
- Jessica R Ingram<sup>4</sup>
- Deepa Waghray<sup>1</sup>
- Gertrud M Hjorto<sup>3</sup>
- Olav Larsen<sup>3</sup> ([ORCID: 0000-0001-9054-4690](https://orcid.org/0000-0001-9054-4690))
- Hidde L Ploegh<sup>5</sup>
- Mette M Rosenkilde<sup>3</sup>
- K Christopher Garcia<sup>1</sup> ([ORCID: 0000-0001-9273-0278](https://orcid.org/0000-0001-9273-0278)) †

### Affiliations

1. Department of Molecular and Cellular Physiology Stanford University School of Medicine Stanford United States
2. Department of Structural Biology Stanford University School of Medicine Stanford United States
3. Laboratory for Molecular Pharmacology, Department of Biomedical Sciences, Faculty of Health and Medical Science University of Copenhagen Denmark Europe
4. Department of Cancer Immunology and Virology Dana Farber Cancer Institute Boston United States
5. Program in Cellular and Molecular Medicine Boston Children’s Hospital Boston United States
6. Howard Hughes Medical Institute Stanford University School of Medicine Stanford United States

† Corresponding author

## Abstract

Human cytomegalovirus has hijacked and evolved a human G-protein-coupled receptor into US28, which functions as a promiscuous chemokine 'sink’ to facilitate evasion of host immune responses. To probe the molecular basis of US28’s unique ligand cross-reactivity, we deep-sequenced CX3CL1 chemokine libraries selected on ‘molecular casts’ of the US28 active-state and find that US28 can engage thousands of distinct chemokine sequences, many of which elicit diverse signaling outcomes. The structure of a G-protein-biased CX3CL1-variant in complex with US28 revealed an entirely unique chemokine amino terminal peptide conformation and remodeled constellation of receptor-ligand interactions. Receptor signaling, however, is remarkably robust to mutational disruption of these interactions. Thus, US28 accommodates and functionally discriminates amongst highly degenerate chemokine sequences by sensing the steric bulk of the ligands, which distort both receptor extracellular loops and the walls of the ligand binding pocket to varying degrees, rather than requiring sequence-specific bonding chemistries for recognition and signaling.

## Introduction

Chemokines are small immunomodulatory proteins that act through a large family of G-protein-coupled receptors (GPCR) (Charo and Ransohoff, 2006; Proudfoot, 2002). More than 40 chemokines and over 20 chemokine receptors are encoded in the human genome, and there is extensive receptor-ligand cross-reactivity, which can manifest as preferential signaling via either G protein or β-arrestin, a process called biased agonism (Steen et al., 2014). Human cytomegalovirus (CMV) has ‘hijacked’ a relatively ligand-specific human GPCR, and repurposed it through evolution to serve as a highly cross-reactive ‘chemokine sink’ as a mechanism to subvert host immunity (Randolph-Habecker et al., 2002). US28 binds with high affinity to many CC-type chemokines, in addition to CX3CL1 (Kledal et al., 1998). The molecular mechanisms for how US28 can engage and respond to such a wide range of chemokines are not understood; indeed, most receptor-ligand interactions are characterized by a high degree of specificity. Furthermore, it remains unclear to what extent, and how, US28 has the capacity to signal differentially in response to these chemokines.

A crystal structure of CX3CL1 bound to US28 (Burg et al., 2015) showed that the chemokine bound through a two-site interaction mechanism (Allen et al., 2007; Monteclaro and Charo, 1996; Thiele and Rosenkilde, 2014) that is generally shared by other chemokine GPCRs (Wu et al., 2010; Wescott et al., 2016; Zheng et al., 2017). At Site 1, the receptor N-terminal region binds a groove on the globular body of the chemokine. At Site 2, the chemokine N-terminal peptide binds within a deep pocket formed by the receptor transmembrane helices (TMs) that is believed to function as the receptor activation switch. The structure also revealed extensive contacts with receptor extracellular loops (ECLs), coined Site 1.5, of unknown function. Given that US28 has a unique capacity to bind many diverse chemokines with high affinity (Kledal et al., 1998), we sought to determine: 1- the breadth of ligand promiscuity that can be accommodated, 2- how sequence differences impact signaling, and 3- the structural properties of this interaction that enable such cross-reactivity.

## Results and discussion

### Chemokine-induced US28 signaling

Radioligand studies reveal a complex network of noncompetitive binding by these chemokines (Figure 1a). Whereas CX3CL1 (Fractalkine) and vMIP-II (a broad-spectrum CC-chemokine antagonist encoded by Kaposi’s sarcoma-associated herpes virus (KSHV) [Kledal et al., 1997]), bind US28 competitively, CCL3 (MIP1α) and CCL5 (RANTES) are only competitive with themselves. This manner of ‘orthosteric allostery’ is well established among chemokine receptor antagonists and suggests significant differences in the nature of receptor engagement, with the potential for differences in chemokine modulation of US28 activity (Kufareva et al., 2017). Although isolated studies have attempted to delineate the signaling effects of individual chemokines at US28, no comprehensive effort has been made to compare chemokine-induced activity among US28’s many ligands or to determine whether they act as biased ligands. US28 signals constitutively via the G protein Gq (Casarosa et al., 2001), and cells expressing US28 exhibit constitutive cell migration (Streblow et al., 1999), which is thought to principally occur through β-arrestin signaling (DeFea, 2007). We sought to establish the capacity of natural and chimeric chemokine ligands of US28 to modulate this constitutive activity. We tested CX3CL1, CCL5, CCL3, and vMIP-II, as well as N-terminal chimeric chemokines, for their effects on Gq-mediated calcium flux and cell migration, which serves as a proxy for β-arrestin signaling.

![Figure 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig1-v1.jpg)

**Figure 1.:** (a) Radioligand binding competition experiments with labeled CX3CL1, CCL3, and CCL5. (b) CX3CL1-induced IP3 turnover is US28 and cell type specific. Dotted line indicates US28 basal activity; all statistics are relative to this. (c) US28-induced calcium responses of 100 nM natural and chimeric chemokines. Dotted line indicates US28 basal activity; all statistics are relative to this. (d) US28 basal β-arrestin recruitment leaves narrow dynamic range in which to observe ligand effects. (e) Migration effects of 100 nM natural and chimeric chemkines at US28. Dotted line indicates US28 basal activity; all statistics are relative to this. All data are given as mean ± s.e.m. of at least three independent biological replicates. * p<0.05, ** p<0.01, *** p<0.001, **** p<0.0001 with respect to basal activity using one sample t-test, two-tailed.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** All data are given as mean ± s.e.m. of at least three independent biological replicates.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** All data are given as mean ± s.e.m. of at least three independent biological replicates.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** top, CCL5 and CX3CL1 Ca2+ responses at a given log concentration decrease as vMIP-II concentration increases. bottom, Representative traces. All data are given as mean ± s.e.m. of at least three independent biological replicates.

These chemokines (four natural and two chimeric) produce a broad range of ligand-induced signaling activities, on top of the receptors’ constitutive activity. The high levels of constitutive signaling and β-arrestin recruitment (Figure 1b and d) complicate precise quantitation and leave a narrow dynamic range in which to directly observe ligand effects, but nevertheless we were able to detect significant changes in US28 activity upon addition of chemokine. Comparing Gq-mediated calcium flux and migration responses, we find that US28 is capable of highly plastic but ligand-specific signaling activities that qualitatively suggest capacity for biased signaling (Figure 1c and e and Figure 1—figure supplements 1 and 2). vMIP-II binds US28 with high affinity while having no effect on the receptor’s activity, acting as a neutral antagonist (Figure 1c and e and Figure 1—figure supplement 3). CCL3 increases Ca2+ signaling while migration remains unaffected, thus appearing to be a G-protein-biased agonist. CCL5 and CX3CL1 potentiate both Ca2+ signaling and cell migration, with CX3CL1 exhibiting more prominent cell migration. Despite prior reports of Gq inverse agonism by CX3CL1 (Tschammer, 2014; Waldhoer et al., 2003), we observe US28-mediated CX3CL1 inverse agonism only in IP3 assays with COS-7 cells (Figure 1b). Chimeric chemokines in which the globular body of CX3CL1 was appended to the N-terminus of vMIP-II (NVF) or CCL5 (N5F) displayed weak calcium flux and moderate cell migration, diminishing the effects of CCL5 while converting vMIP-II from an antagonist to an agonist (Figure 1c and e). It is unclear whether this signaling behavior arises from direct contacts by the chemokine globular body or indirect contacts that arise from the manner in which the globular body drapes the chemokine N-terminus within the receptor binding pocket. The chemokine N-terminus thus serves an instructive, although not solely determinative, role in dictating signaling through US28. In sum, these studies establish the plasticity of ligand-dependent US28 signaling.

### The sequence space of chemokine agonism

We next explored the structural diversity of chemokine N-terminal sequences compatible with US28 engagement to uncover sequence hallmarks that correlate with particular signaling pathways and downstream functions, such as induction of cell migration. We used a yeast-displayed library of diverse chemokine variants to map the sequence specificity of receptor engagement and activation by the Site 2 N-terminal peptide. Single chain fusions of US28 with intracellularly directed nanobodies (Burg et al., 2015) (Nb7 or Nb11) enable purification of stable, apo-US28 (Figure 2—figure supplement 1) that can be used to stain yeast cells displaying chemokine on their surface (Figure 2a), thereby solving the general problem of structural instability of GPCRs purified in apo form (Handel, 2015; Rosenbaum et al., 2009; Wu et al., 2010). The alpaca nanobodies were raised against the US28/CX3CL1 complex, and, importantly, structures of CX3CL1-bound US28 with and without Nb7 reveal no significant differences in receptor conformation. This confirms that the nanobody does not deform US28 but merely selects a subset of pre-existing, stable, active-like conformations. Thus, these nanobody fusions serve as ‘molecular casts’ with which to screen yeast displayed chemokine libraries using purified recombinant US28. Interestingly, we found that the two nanobodies endow US28 with different chemokine binding pharmacologies: US28Nb7 was permissive for binding of all tested chemokines, whereas US28Nb11 showed impaired binding of CCL5 and CCL3 (Figure 2b). This finding conforms with radioligand competition experiments and suggests that the two nanobodies are stabilizing partially non-overlapping US28 conformational subsets.

![Figure 2.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig2-v1.jpg)

**Figure 2.:** (a) Illustration of yeast-displayed chemokine and nanobody-stabilized receptors. (b) Effect of intracellular nanobody 7 or 11 on US28 binding to yeast-displayed chemokines. All data points are normalized to binding at 1 µM US28Nb7 (c) Increase in binding at 1 nM US28 after selection with either US28Nb7 or US28Nb11. (d) Clustering of CX3CL1 N-terminal sequences revealed by deep-sequencing after selection. Each point is a unique N-terminus and sequences sharing 6 of 7 amino acids are connected. (e) Degree of amino acid convergence at each position of the CX3CL1 N-terminus. Amino acids with >3% abundance after selection are considered allowed and the size of a shaded region corresponds to that amino acid’s frequency (PDB: 4xt1).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** left, Structure of nanobody7 bound to US28 with a dashed line showing a linker creating a fusion construct. right, Size exclusion chromatograms of US28 and US28Nb7. SDS-PAGE gels depict the elution fractions between vertical hashes.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** ΔN US28 is US28Nb7 which has been engineered to delete the receptor N-terminus up to Cys22 (See methods for details). All data points are normalized to binding at 1 µM US28Nb7.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** top left, CX3CL1 amino acids included in library design are highlighted (PDB: 4xt1). bottom left, Codons used and amino acids included at each position of the library (wild-type amino acid identity in red). right, Enrichment of amino acid frequency by chemokine N-terminal position after selection with either US28Nb7 or US28Nb11 as compared to the naive, unselected CX3CL1 library as determined by deep sequencing of the respective samples.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** CX3CL1 in which the 7 N-terminal residues are all mutated to glycine is yeast-displayed and stained with US28Nb7. All data points are normalized to binding at 1 µM US28Nb7 with wild-type CX3CL1.

A version of US28Nb7 was created that deletes the receptor N-terminus, thereby precluding Site 1 interaction with chemokines. Surprisingly, CX3CL1 and CCL5 show virtually unchanged affinity in the absence of Site 1 interaction (Figure 2—figure supplement 2). This result stands in contrast to analogous experiments in the absence of nanobody (Casarosa et al., 2005) and suggests that nanobody7 selectively potentiates the affinity of CCL5 and CX3CL1 for US28 via Site 2, as has been observed in other GPCRs (Staus et al., 2016).

Having seen the importance of Site 2 for US28Nb7 engagement, a CX3CL1 library was constructed in which the seven N-terminal residues of the chemokine were randomized (Figure 2—figure supplement 3). This library was displayed on the surface of yeast and selected with increasing stringency for affinity to each of the nanobody-stabilized receptors (Figure 2c). Following selection, the remaining pools of yeast were deep-sequenced to identify CX3CL1 sequences compatible with binding either US28Nb7 or US28Nb11. This sequencing data showed that tens of thousands of unique chemokine N-termini are able to bind US28 with high affinity (Figure 2d). While the US28Nb11 selected chemokines appear slightly more converged, the most abundant unique variants comprise only a small fraction of the total sequence count. To visualize these broad sequence landscapes, pairs of N-termini that differ at only one of the seven randomized residues were clustered; to ensure significance we limited our analysis to sequences that appeared more than 10 times within the pool. 794 unique US28Nb7-selected N-termini met these criteria, with each connected to an average of 2.7 related sequences. Partitioning of these sequences into distinct subpopulations is not observed. After US28Nb11 selection, 11,415 unique N-termini had at least one partner that differed at only one position and each sequence connected to an average of 9.6 relatives.

A residue-by-residue analysis of the combinatorial chemokine N-termini from the library selections shows that sequence promiscuity extends along the full length of randomized positions (Figure 2e and Figure 2—figure supplement 3). Despite this diversity, CX3CL1 with a polyglycine amino terminus shows minimal binding to US28Nb7, confirming the necessity of certain N-terminal contacts (Figure 2—figure supplement 4). While the CX3CL1 wild type amino terminus appears in the sequencing, the wild-type identity rarely emerges among the most abundant amino acids at a given position. For example, hydrophobic amino acids enrich over the wild-type glutamine at position 1, while arginine enriches over the wild-type histidine at position 2. As the same hydrophobic amino acids score the worst in computational signal sequence cleavage site recognition, it is unlikely that this result is simply due to biases in processing or expression (Nielsen, 2017).

A collection of highly diverse sequences was chosen from each of the two different nanobody selections for further signaling characterization (Figure 3a and b and Figure 3—figure supplements 1 and 2). These chemokines bound US28Nb7 with affinities akin to wild-type CX3CL1 on yeast, yet revealed comparatively weak competition with wild-type CX3CL1 in radioligand binding studies (Figure 3—figure supplement 3). This behavior is reminiscent to that of US28’s natural chemokine repertoire reported above. Because the high basal signaling of US28 results in a narrow dynamic range in which to measure differences between agonists, we can only make qualitative conclusions about signaling bias. Nevertheless, nearly all these chemokines induce some level of cell migration, though none surpass that of wild-type CX3CL1 (Figure 3b). Conversely, G protein activation stronger than wild-type CX3CL1 was elicited by LLPHANY (CX3CL1.35) (Figure 3a). To determine if the LLPHANY sequence contained particular hallmark residues that correlate with G protein signaling, homologous sequences to CX3CL1.35 that emerged from the deep sequencing were tested (Figure 3c and d). These sequences include variants with mutations throughout the CX3CL1.35 N-terminus. Surprisingly, despite the substantial sequence differences of these variants, most induced G protein signaling in a qualitatively similar fashion to CX3CL1.35. Similarly, none of the CX3CL1.35 family members showed significantly decreased cell migration. This result demonstrates that for a given ligand sequence motif, signaling effects are relatively insensitive to individual sequence substitutions.

![Figure 3.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig3-v1.jpg)

**Figure 3.:** (a) Calcium and, (b) migration responses of diverse chemokines revealed by deep sequencing at 100 nM ligand. Dotted lines indicate wild-type CX3CL1 activity (red); all statistics are relative to this. CX3CL1.35, selected for further study, is indicated in green. (c) Calcium and, (d) migration responses of CX3CL1.35-related sequences from deep sequencing at 100 nM ligand. Dotted lines indicate CX3CL1.35 (green) activity; all statistics are relative to this. All data are given as mean ± s.e.m. of at least three independent biological replicates. * p<0.05, ** p<0.01, *** p<0.001 by one-way ANOVA (Dunnett’s test).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** All data are given as mean ± s.e.m. of at least three independent biological replicates.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** All data are given as mean ± s.e.m. of at least three independent biological replicates.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** top, Dose-response plots of yeast displayed CX3CL1 library variants stained with US28Nb7. bottom, Radioligand competition plots of cold, recombinant CX3CL1 library variants with I125-wild-type CX3CL1.

### Structural basis for US28’s chemokine promiscuity

We determined the crystal structure of the US28 fusion to nanobody7 in complex with the engineered chemokine CX3CL1.35 to 3.5 Å resolution (Figure 4a). Crystallization of the CX3CL1.35 complex by Lipidic Cubic Phase required an additional nanobody, raised by alpaca immunization against apo-US28Nb7 (Figure 4—figure supplement 1a,b). CX3CL1.35 contacts a symmetry-related nanobody B1 (Figure 4—figure supplement 2a and b) raising the question of whether the native conformation of the complex enables lattice contacts or, conversely, whether lattice contacts induce a non-native conformational change in the complex. The former explanation is supported by the fact that exhaustive attempts to crystallize other CX3CL1 library variants with US28Nb7 and nanobody B1 fail to yield crystals.

![Figure 4.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-v1.jpg)

**Figure 4.:** (a) CX3CL1.35-US28 and CX3CL1-US28 structural alignment based on US28 transmembrane helices (PDB:4xt1). (b) Wild type and engineered chemokine N-termini trace different paths in US28’s binding pocket. (c) Cutaway image of US28 with chemokine contacts highlighted for CX3CL1.35 (teal), CX3CL1 (purple), or both (yellow). (d) CX3CL1.35 fills the entire binding pocket. (e) CX3CL1 hugs the TM2 side of US28. (f) US28 side chains contacted by CX3CL1.35 in the receptor binding pocket. (g) US28 side chains contacted by CX3CL1 in the receptor-binding pocket.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (a) top, Selections increased US28Nb7 binding of the yeast-displayed nanobody library and yielded promiscuous binders (population B in round 3), including B1, and those specific to US28Nb7 (population A in round 3) like A6. bottom, On-yeast titration of the selected nanobodies against US28Nb7 (red). Single concentration staining of the nanobodies against US28Nb11 (blue) was performed to confirm specificity. (b) Details of the CX3CL1.35-US28Nb7-Nanobody B1 structure showing the interface between nanobodies 7 and B1. Nanobody B1 recognizes the conserved nanobody tail with the scar of a 3C protease site.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (a) Crystal lattice packing of the CX3CL1.35-US28Nb7-nanobody B1 complex. (b) The crystal lattice is stabilized by contact between CX3CL1.35 (cyan) and a symmetry-related nanobody B1 (slate blue). (c) In CX3CL1-US28-Nb7, CX3CL1 doesn’t make any crystal contacts. (d) In CX3CL1-US28, the C-terminus of CX3CL1 contacts a symmetry-related copy of itself (slate blue).

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-figsupp3-v1.jpg)

**Figure 4—figure supplement 3.:** left, Side view of structural alignment based on US28 transmembrane helices showing CX3CL1 (purple)- and CX3CL1.35 (teal)-bound US28 structures. middle, Top-down view. right, Alignment of the identical globular cores (residues 8–62) of CX3CL1 and CX3CL1.35 with the N-terminal peptide of US28 (purple: CX3CL1-bound, teal: CX3CL1.35-bound).

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-figsupp4-v1.jpg)

**Figure 4—figure supplement 4.:** left, Top-down view of CX3CL1 (purple) interactions with US28 ECL2 (gray). right, Top-down view of CX3CL1.35 (teal) interactions with US28 ECL2 (gray).

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig4-figsupp5-v1.jpg)

**Figure 4—figure supplement 5.:** (a) mFo-DFc simulated annealing omit map (green) is contoured at 3.0 sigma around the N-terminal residues of CX3CL1.35. (b) ‘Site 2’ contacts between US28 and wild-type CX3CL1 (purple), CX3CL1.35 (teal), or both chemokines (yellow).

The chemokine globular body sits atop the receptor in a very similar disposition as wild type CX3CL1, albeit CX3CL1.35 is rotated by 16.8° (Figure 4a and Figure 4—figure supplement 3), contributing to reduced interaction between the chemokine N-loop and US28 ECL2 (Figure 4—figure supplement 4). This rotation is markedly greater than the 3° distortion in wild-type CX3CL1 bound to US28 in structures with and without such lattice contacts (Burg et al., 2015)(Figure 4—figure supplement 2c and d), further supporting the notion that this pose is not artefactual. The chemokine N-termini trace markedly different paths within the ligand-binding pocket of US28 (Figure 4b, Figure 4—figure supplement 5, and Figure 4—source data 1). The interaction chemistries and structural environments for how CX3CL1 versus CX3CL1.35 engage US28 are distinct, with each chemokine occupying both overlapping and spatially segregated regions of the US28 orthosteric pocket (Figure 4c). CX3CL1 forms extensive contacts with US28’s minor pocket at TM1, TM2, TM3, and TM7 and ECL2 (Figure 4e and g). The N-terminus of CX3CL1.35 also fills the minor pocket sharing contacts with Glu2777.39 (Figure 4d and f; Figure 4—source data 1), which is also commonly contacted by small molecule chemokine ligands (Lückmann et al., 2017; Rosenkilde and Schwartz, 2006), as well as Trp892.60 and Phe1113.32 [superscripts refer to the Ballesteros-Weinstein nomenclature (Ballesteros and Weinstein, 1995). Chemokine interaction at these three residues is broadly conserved across receptors and strongly affects ligand affinity (Arimont et al., 2017). Recent shotgun mutagenesis of CXCL12 with CXCR4 also implicates these residues in the initiation of receptor signaling (Wescott et al., 2016). Unlike the wild-type chemokine, CX3CL1.35 also projects into the major pocket of the receptor toward TM5 and TM6, contacting Asn1895.39, Leu1925.42, Tyr2446.51, Leu2486.55, and Asp2516.58 (Figure 4d and f). These residues superficially surround the Trp2416.48 rotamer switch that is implicated in the transition between inactive and active GPCR structures (Arimont et al., 2017; Latorraca et al., 2017). CX3CL1.35 loses the extensive direct contacts to TM2 and ECL2 evident in the structure of the wild-type chemokine (Figure 4b and Figure 4—figure supplement 4). Indirect contacts between CX3CL1.35 and US28 ECL2 are mediated by the sulfonate moiety of a MES ion from the crystallization buffer (Figure 4b).

Re-examining the signaling activity of the specific CX3CL1.35 sequence family members (Figure 3c and d) in light of this structure demonstrates that signaling for either pathway is largely unaffected by even drastic changes to the interactions within the receptor binding cavity. Calcium signaling and migration are robust to disruption of receptor contacts throughout the binding pocket suggesting either that specific side chain contacts are largely unimportant or that significant conformational rearrangements of the chemokine amino terminus are made to preserve contacts. The most prosaic explanation for the relative lack of sequence selectivity imposed by the US28 pocket, yet ability of unrelated chemokine sequences to elicit differential signaling outputs, would be that the steric bulk of the ligand is more important than specific bonding chemistries. If steric bulk, which would apply strain to the walls of the US28 binding pocket, were the principal determinant of signaling output, an almost unlimited number of sequences could elicit similar signaling outputs, which is consistent with our data.

### Extracellular rearrangements upon chemokine binding

To assess the impact of ligand binding on the structure and dimensions of the US28 ligand binding pocket, we determined the crystal structure of apo-US28Nb7 without an extracellular ligand to 3.5 Å resolution (Figure 5—figure supplement 1a). Together, the CX3CL1-bound, CX3CL1.35-bound, and apo-US28 structures allow direct comparisons among the basal and qualitatively β-arrestin- and G-protein-biased states of the same GPCR, with the caveat that the bound nanobodies prevent us from reaching conclusions about structural differences in the intracellular regions of US28 (Figure 5—figure supplement 1b). In contrast to the chemokine-bound structures, access to the extracellular binding cavity of US28 is significantly constricted in apo-US28, where ECL1 and ECL2 collapse inward (Figure 5a). Each chemokine elicits distinct conformational changes in US28 in order to gain access to the binding pocket. CX3CL1 displaces ECL1 and ECL2 away from the receptor core, uncovering the binding pocket but causing minimal overall distortion (Figure 5b). Conversely, CX3CL1.35 distorts TM1, TM6, and TM7 away from the receptor core, resulting in an expanded binding pocket.

![Figure 5.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig5-v1.jpg)

**Figure 5.:** (a) Top-down and side views of apo-, CX3CL1-, and CX3CL1.35-bound US28 showing expanded access to the receptor binding pocket when chemokine is present. (b) Structural alignment based on US28 transmembrane helices showing unique US28 conformational changes caused by each chemokine. (PDB: 4xt1). Crystallographic data and refinement statistics are summarized in Figure 5—source data 1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/35850/elife-35850-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Overall structure of apo-US28Nb7. (b) Intracellular view of US28 in apo-, CX3CL1-bound, and CX3CL1.35-bound structures aligned on US28 transmembrane helices.

By way of comparison, small molecule agonists induce subtle contraction of the binding pocket, drawing in TM5 (as in the ß2-adrenergic receptor [Rasmussen et al., 2011; Ring et al., 2013]), TM6 (as in the M2 muscarinic receptor [Kruse et al., 2013]), or TM3 (as in the µ-opiod receptor [Huang et al., 2015]) (Latorraca et al., 2017). Recent structures of endothelin B (ETb) suggest that peptide agonists may behave more like chemokines. Apo and ET1-bound structures show that activation results in large inward translations of the extracellular ends of TM6 and TM7 toward TM3 (Shihoya et al., 2016).

The pronounced differences in ECL conformation and contacts with chemokine raise the possibility that chemokines may function as bitopic ligands via site 1.5 and site 2 interactions, with both interaction sites working in concert to determine a chemokine’s precise signaling profile. This notion is supported by the unique signaling profiles of chimeric chemokines NVF and N5F. ECL stabilization is a common mechanism of allosteric modulation among group A GPCRs (Christopoulos, 2014; Kruse et al., 2013) and recent mutagenesis studies suggest a role for ECL2 in chemokine receptor signaling (Ziarek et al., 2017). Indeed, toggling ligand interactions between ECL2 and TM5 has recently been proposed as a general mechanism of inducing signaling bias within aminergic class A GPCRs (McCorvy et al., 2018).

### Conclusions

Our approach using chemokine libraries has revealed that US28 can accommodate at least thousands of chemically diverse chemokine N-termini, perhaps many more, indicating an astonishing degree of ligand cross-reactivity for a cell surface receptor. Without apparent sequence patterns, these engineered chemokines induce the full spectrum of signaling bias at US28. Natural chemokine sequences merely represent a subset of local minima in a broad signaling fitness landscape. The combined structural and deep sequencing data suggest that G protein activation is elicited as a consequence of steric bulk distorting the walls the major pocket of the receptor, dilating the receptor’s extracellular face, rather than highly specific and sequence-specific bonding chemistries. This relative sequence-insensitive mechanism, which is highly unusual for protein-protein interactions, is likely enabled by the N-terminal chemokine sequence binding within a capsule-shaped US28 pocket, affording numerous opportunities for adventitious bonding interactions between the walls of the pocket and alternative conformations of the N-terminal peptide. This is as opposed to the generally broad and exposed interfaces seen in protein-protein interactions, which are generally much less tolerant to substitution. The properties exhibited by US28 explain how the virus evolved a human GPCR to be highly promiscuous in order to promote viral survival and offer the broader possibility that GPCR signaling can be activated by surrogate agonists that are unrelated to the natural ligands and activate new signaling pathways.

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
      <td>Gene (human cytomegalovirus)</td>
      <td>US28 (unique short region)</td>
      <td>PMID 7961796</td>
      <td></td>
      <td>strain TOWNE</td>
    </tr>
    <tr>
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>EBY100</td>
      <td>Gift from Prof. Dane Wittrup (PMID 17406305)</td>
      <td></td>
      <td>Yeast cells</td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>SF9</td>
      <td>ATCC</td>
      <td>CTL-1711</td>
      <td>Insect cells used for baculovirus production</td>
    </tr>
    <tr>
      <td>Cell line (Trichoplusia ni)</td>
      <td>Hi5</td>
      <td>Invitrogen</td>
      <td>BTI-TN-5B1-4</td>
      <td>Insect cells used for baculovirus expression of NbB1</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293</td>
      <td>ATCC</td>
      <td>CRL-1573</td>
      <td>Mammalian cells used for Ca2+ signaling assay</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293-US28 wt</td>
      <td>PMID 23303826</td>
      <td></td>
      <td>Mammalian cells used for Ca2+ signaling assay and IP3 assays</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>HEK293S GnTI-</td>
      <td>Gift from Prof. H. Gobind Khorana (PMID 12370423)</td>
      <td></td>
      <td>Mammalian cells used for baculovirus expression of US28 variants and chemokines</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Flp-In TREx 293</td>
      <td>Invitrogen</td>
      <td>R78007</td>
      <td>Hamster cells used for β-arrestin assay</td>
    </tr>
    <tr>
      <td>Cell line (Chinese hamster ovary)</td>
      <td>CHO-K1 EA-arrestin</td>
      <td>DiscoverixRx</td>
      <td>93–0164</td>
      <td></td>
    </tr>
    <tr>
      <td>Transfected construct (β-arrestin recruitment)</td>
      <td>US28 wt/ProLink/b-galactose</td>
      <td>This report</td>
      <td></td>
      <td>Vector provided by DiscoverixRx</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-protein C (mouse IgG1)</td>
      <td>ATCC</td>
      <td>HB-9892</td>
      <td>Antibody used for staining yeast bound to protein C tagged target proteins. Purified from HPC-4 MOUSE HYBRIDOMA for Alexa647 labeling.</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-FLAG M1 (mouse IgG2a)</td>
      <td>Gift from Prof. Brian Kobilka (PMID 17962520)</td>
      <td></td>
      <td>Antibody used for US28 purification. Purified from M1 HYBRIDOMA to prepare anti-FLAG M1 affinity resin</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Myc-Tag (9B11) Mouse mAb (Alexa Fluor 488 Conjugate)</td>
      <td>Cell Signaling Technology</td>
      <td>2279</td>
      <td>Antibody used for staining yeast properly displaying proteins of interest with Myc-tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>BestBac Linearized Baculovirus DNA 2.0, Exp ression Systems, 91–002</td>
      <td>Expression Systems</td>
      <td>554739</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CCL3</td>
      <td>Peprotech</td>
      <td>300–08</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CCL5</td>
      <td>Peprotech</td>
      <td>300–06</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>CX3CL1</td>
      <td>Peprotech</td>
      <td>300–31</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PathHunter β-arrestin assay</td>
      <td>DiscoverixRx</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MiSeq v2 2 × 150</td>
      <td>Illumina</td>
      <td>MS-102–2002</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MiSeq v2 2 × 250</td>
      <td>Illumina</td>
      <td>MS-102–2003</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Alexa Fluor 647 NHS Ester (Succinimidyl Ester)</td>
      <td>Thermo Fisher Scientific</td>
      <td>A37573</td>
      <td>Labeling reagent for anti-protein C antibody</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>monoolein</td>
      <td>Sigma</td>
      <td>M7765</td>
      <td>For LCP</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>cholesterol hemisuccinate tris salt</td>
      <td>Anatrace</td>
      <td>CH210</td>
      <td>For membrane protein purification and yeast staining buffer</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>cholesterol</td>
      <td>Sigma</td>
      <td>C8667</td>
      <td>For LCP</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-dodecyl-β-D-maltoside</td>
      <td>Anatrace</td>
      <td>D310</td>
      <td>For membrane protein SEC buffer</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>n-dodecyl-β-D-maltoside</td>
      <td>Anatrace</td>
      <td>D310S</td>
      <td>For membrane protein solubilization buffer, affinity column buffer, and yeast staining buffer</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism7</td>
      <td>GraphPad</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>XDS</td>
      <td>PMID 20124692</td>
      <td></td>
      <td>Data integration, scaling, space-group assignment and merging</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phaser</td>
      <td>PMID 19461840</td>
      <td></td>
      <td>Molecular replacement</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Phenix suite</td>
      <td>PMID 20124702</td>
      <td></td>
      <td>Structure refinement</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Coot</td>
      <td>PMID 20383002</td>
      <td></td>
      <td>Structural model building</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PyMol</td>
      <td>Schrödinger</td>
      <td></td>
      <td>Structural visualization/ figure preparation</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Pandaseq</td>
      <td>PMID 22333067</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious</td>
      <td>Biomatters</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Matlab</td>
      <td>Mathworks</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cytoscape</td>
      <td>PMID 14597658</td>
      <td></td>
      <td>Cluster analysis visualization</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cytobank</td>
      <td>Cytobank, Inc.</td>
      <td></td>
      <td>Flow cytomettry visualization</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>KaleidaGraph</td>
      <td>Synergy Software</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Clustering algorithm</td>
      <td>PMID 24855945</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>CNBr-Activated Sepharose 4 Fast Flow</td>
      <td>GE Healthcare</td>
      <td>17098101</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>LS columns</td>
      <td>Miltenyi</td>
      <td>130-042-401</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Anti-Cy5/Anti-Alexa Fluor 647 MicroBeads</td>
      <td>Miltenyi</td>
      <td>130-091-395</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>MidiMACS Magnetic Separator</td>
      <td>Miltenyi</td>
      <td>130-042-302</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Design and purification of US28-nanobody fusions

US28 was truncated by 10 amino acids at the N-terminus and 44 amino acids at the C-terminus. Examination of the CX3CL1-US28-nanobody7 structure (PDB: 4xt1) allowed for the design of a linker between the C-terminus of US28ΔNΔC and the N-terminus of nanobody7 composed of two thrombin recognition sites and a six residue Gly-Ser linker. This construct, termed US28Nb7, was decorated with HA signal peptide, an N-terminal FLAG epitope tag and a C-terminal 3C protease site, as well as C-terminal protein C and 8xHis tags. The same design was used to make a single-chain construct between US28 and nanobody11 (previously demonstrated to be competitive with nanobody7 [Burg et al., 2015]), termed US28Nb11.

US28Nb7 and US28Nb11 were expressed in HEK293S GnTI- cells using BacMam baculovirus transduction. Baculovirus was added to cells at a density of 2 × 106 cells ml−1 and culture bottles were shaken for 24 hr at 37˚C with 5% CO2. After harvesting, cells were washed with PBS supplemented with 5 mM EDTA and 1:1000 protease inhibitor cocktail (PIC, Sigma Aldrich, St. Louis MO) and stored at −20˚C. Cell pellets were thawed and lysed with a Dounce homogenizer in a solution composed of 20 mM Tris-Cl pH 8.0, 5 mM EDTA, 2 mg ml−1 iodoacetamide, and 1:1000 PIC. The lysate was centrifuged at 40,000 x g for 1 hr and the membrane pellet was resuspended and rotated for 2 hr in a solubilization buffer consisting of 10 mM HEPES pH 7.4, 150 mM NaCl (HBS), 1% (w/v) dodecylmaltoside (DDM), 0.2% (w/v) cholesterol hemisuccinate (CHS), 10% (v/v) glycerol, 2 mg ml−1 iodoacetamide, and cOmplete PIC (Roche, Basel Switzerland).

After centrifugation, 5 ml Ni-NTA resin (Qiagen, Hilden Germany ) per L of initial culture was added and stirred at 4˚C overnight. The resin was then collected in a column; washed with HBS with added 0.1% (w/v) DDM, 0.02% (w/v) CHS, 10% (v/v) glycerol, and 20 mM imidazole (wash buffer); and eluted in wash buffer supplemented to 200 mM imidazole. The eluate was then adjusted to 2 mM CaCl2 and further purified over an anti-FLAG M1 affinity column. The receptor was eluted with 0.2 mg ml−1 FLAG peptide and 5 mM EDTA and further purified by size exclusion chromatography using a buffer containing HBS, 0.02% (w/v) DDM and 0.004% (w/v) CHS.

US28Nb7 and US28Nb11 ‘competitor’ constructs (used in kinetic selections) were digested with 1:10 (w/w) 3C protease for 2 hr at room temperature to remove the protein C epitope tag prior to size exclusion chromatography. In ΔN US28Nb7 (used in nanobody selections and chemokine-binding assay (Figure 2—figure supplement 2)), the thrombin sites in the linker between US28 and nanobody7 were replaced with Gly-Ser linkers of equal length and a thrombin site was introduced with a three amino acid Gly-Ser linker N-terminal to Cys22 of US28. This construct was purified as above, digested with 1:100 (w/w) thrombin at 4˚C overnight and cleared over an anti-FLAG M1 affinity column prior to size exclusion chromatography. In all cases, the final protein was concentrated, aliquoted, and stored frozen before staining experiments.

### Creation and staining of yeast display constructs

Chemokines were synthesized as N-terminal fusions to the yeast surface protein Aga2p (IDT, San Jose CA). Constructs were cloned into the vector pYAL with the Aga2p leader sequence, leaving the chemokine N-terminus free. The plasmid vector contains a Gly-Ser linker and a Myc epitope tag between the chemokine and Aga2p. Constructs were then electroporated into electrocompetent EBY-100 yeast, passaged in synthetic defined medium (SDCAA) and protein expression was induced in SGCAA pH 4.5 media at 20˚C for 24–60 hr as described (Chao et al., 2006), until maximum Myc epitope tag staining was observed (typically 40–70% of total population).

A CX3CL1 N-terminal library was prepared by assembly PCR with oligonucleotide primers containing degenerate codons at the first seven amino acids of the chemokine (contiguous with the first cysteine) (Figure 2—figure supplement 2). The amplicon contained 50 base pairs of homology to pYAL. The mutagenic CX3CL1 DNA and linearized pYAL vector were co-electroporated into EBY100 yeast to yield a library with 2.0 × 108 transformants.

Induced yeast displaying chemokine were washed with HBS with added 2 mM CaCl2, 10 mM maltose, 0.1% (w/v) BSA, 0.02% (w/v) DDM and 0.004% (w/v) CHS (Staining Buffer) and stained with varying concentrations of the desired receptor construct for 2 hr at 4˚C. The yeast were then washed with staining buffer and stained with Alexa-647 conjugated anti-protein C antibody and Alexa-488 conjugated anti-Myc antibody (Cell Signaling, Danvers MA) for 15 min at 4˚C. After a final wash, mean cell fluorescence was measured using FL-1 and FL-4 channels of an Accuri C6 flow cytometer (BD Biosciences, Franklin Lakes NJ).

### Chemokine selection by yeast surface display

For the first round of selection, 2.0 × 109 yeast (10x the library diversity to ensure full coverage) induced with SGCAA medium were washed with staining buffer and negatively selected to eliminate any yeast clones against selecting reagents and magnetic column. Yeast were stained with Alexa-647 conjugated anti-protein C antibody for 15 min at 4˚C, washed with staining buffer and magnetically labeled with 50 μl anti-Alexa-647 microbeads (Miltenyi, Bergish Gladbach Germany) in staining buffer for 15 min at 4˚C. Yeast were again washed with staining buffer and unlabeled yeast were isolated by clearing through an LS column (Miltenyi) pre-equilibrated with staining buffer. These cleared yeast were then washed with staining buffer and stained with 3 nM US28Nb7 or 30 nM US28Nb11 for 2 hr at 4˚C. These concentrations were chosen so that ~10% of the yeast would be bound. The yeast were then washed with staining buffer and stained with Alexa-647 conjugated anti-protein C antibody for 15 min at 4˚C. Yeast were washed again with staining buffer and magnetically labeled with 250 μl anti-Alexa-647 microbeads (Miltenyi) in staining buffer for 15 min at 4˚C. Yeast were again washed with staining buffer and labeled yeast were isolated by magnetic selection with an LS column (Miltenyi) pre-equillibrated with staining buffer. Magnetically sorted yeast were resuspended in SDCAA and cultured at 30˚C.

A second round of magnetic selection was performed for US28Nb11 selected yeast at a concentration of 3 nM target (~10% of post-R1 yeast were now bound at this concentration) so that the same stringency of selection was now achieved for US28Nb11 as for the first round of US28Nb7 selections. For the final round of selection, a kinetic selection was performed to isolate clones with the slowest off-rates. Yeast equaling 10x the post-selection diversity after the previous round were induced in SGCAA medium. Non-specific antibody binders were again cleared as described above and the yeast were again stained with 3 nM US28Nb7 or US28Nb11 (matching the previous round) for 2 hr at 4˚C. Following this, the yeast were washed with staining buffer and resuspended in 3 μM of the nanobody-matched ‘competitor’ construct that lacks a protein C tag (and thus will be dark in the selection). The yeast were incubated at room temperature for 90 min, after which time they were washed in staining buffer and stained with Alexa-647 conjugated anti-protein C and Alexa-488 anti-Myc antibodies for 15 min at 4˚C. Yeast were washed with staining buffer and Alexa-647 positive yeast with the highest Alexa-647/Alexa-488 ratios were purified using a FACS Jazz cell sorter (BD Biosciences). Post-sorted yeast were resuspended in SDCAA medium and cultured at 30˚C. Chemokine cDNA was prepared from each of the post selection library samples, transformed into E. coli and sequenced, to confirm sequence convergence.

### Deep sequencing of chemokine libraries

Deep sequencing was performed as previously described (Birnbaum et al., 2014). Briefly, pooled plasmids from 2 × 107 yeast from each round of selection were isolated via yeast miniprep (Zymoprep II kit, Zymo Research, Irvine CA) and used as PCR template to prepare Illumina samples. Amplicon libraries were designed as follows: Illumina P5-Truseq read 1-(N8)-Barcode-Chemokine-(N8)-Truseq read 2-IlluminaP7. N8 was added immediately after both sequencing primers to generate diversity for low-complexity sequencing reads. The adaptor and barcode sequences were appended via nested cycles of PCR of the purified plasmids using Phusion polymerase (NEB, Ipswich MA). The number of cycles for each round of PCR was determined by quantitation on a Bioanalyzer (Agilent, Santa Clara CA) to protect against over-amplification. Primers were proximal to the library region of the chemokine to ensure high-quality sequence reads with double coverage. Final PCR products were run on a 2% agarose gel and purified via gel extraction (QIAGEN). Purified PCR products were then quantitated, normalized for each barcoded round of selection to be equally represented, doped with 5–50% PhiX DNA to ensure sufficient sequence diversity for high-quality sequence reads and run on an Illumina Miseq with 2 × 150 nt Paired End reads (Illumina, San Diego CA).

To analyze the sequence data, contigs were generated for each paired end read using PANDAseq software. The contigs were then deconvoluted into individual rounds of selection and trimmed to the chemokine sequence using Geneious version 6. The numbers of reads for each unique sequence were then summed. Sequences were then translated into peptides and any reads that contained stop codons, frameshifts, or mutations outside the library design were omitted from further analysis. Amino acid frequencies were then calculated for those unique sequences that appear with 10 or greater counts as previously described. Clustering of selected CX3CL1 amino termini was performed for US28Nb7 and US28Nb11 samples after the final kinetic selection for all sequences appearing greater than 10 copies and connected by a Hamming distance of 6 (1 position variable allowed) into a network.

### Chemokine purification

Individual CX3CL1 library variants (CX3CL1.##) selected for signaling analysis were designed and expressed as reported previously. Constructs comprised the natural CX3CL1 signal peptide, library amino acid residues 1–7, and CX3CL1 residues 8–77 under the control of the CMV promoter in the vector pVLAD6. The C-terminal mucin-like stalk was replaced with a flexible linker (SGSGSAAA) followed by a 3C protease site (LEVLFQGP) and human Fc.

CX3CL1.##−3C-Fc were expressed in HEK293S GnTI- cells with BacMam baculovirus transduction. Baculovirus was added to the cells at a density of 2 × 106 cells ml−1 and culture bottles were shaken for 72 hr at 37˚C with 5% CO2. Cells were removed by centrifugation, and the culture supernatant was filtered and then stirred at 4°C overnight with 3 ml Ni-NTA resin (Qiagen) per L of supernatant. The Ni-NTA was then collected by filtration, washed with 20 mM imidazole HBS, and eluted with 200 mM imidazole HBS. To liberate the chemokine from the Fc, 1:50 (w/w) 3C protease was added to the eluate and incubated at 4˚C overnight. The sample was then diluted 10x with HBS to 20 mM imidazole and run twice through a Ni-NTA column to clear the Fc and protease. The flow-through containing the final protein was concentrated, aliquoted, and stored frozen before signaling experiments.

### Cell lines

HEK293 cells were obtained from ATCC (Manassas VA) (CRL-1573), CHO-K1 EA-arrestin cell line from DiscoverX (Fremont CA) and the Flp-In TREx 293 cell line from Invitrogen (Carlsbad CA). Hi5 cells were from Invitrogen (BTI-TN-5B1-4), SF9 cells were from ATCC (CTL-1711), HEK293GnTI- cells were provided by Prof. H.G. Khorana, and EBY100 yeast cells were provided by Prof. Dane Wittrup. Cell line authentication was guaranteed by the sources where the cells were bought. All eukaryotic cell lines used for signaling and functional assays were tested negative for mycoplasma on a regular basis, before and during tissue culture.

### Cell culture, US28 constructs, and data analysis for signaling assays

HEK293 cells were grown in Dulbecco´s modified Eagle´s Medium (DMEM) supplemented with 10% fetal bovine serum (v/v), 180 units mL−1 penicillin and 45 µg mL−1 streptomycin. The CHO-K1 EA-arrestin2 cells were grown in Ham´s F-12 medium containing 10% fetal bovine serum, 2 mM glutamine, 180 units mL−1 penicillin, 45 µg mL−1 streptomycin and 250 µg mL−1 hygromycin. The stable clones of inducible US28wt- (parental virus strain TOWNE) HEK293 cells were generated previously described (Hjortø et al., 2013) and were grown as the following the manufacturer’s protocol for maintenance of parental and inducible clones (flp-in-t-Rex system, Invitrogen).

The ligands were tested in at least three individual biological replicates, each with at least two technical replicates. Three biological independent experiments was considered as the minimum required to see if the results were internally consistent. If the results from one experiment were not consistent with the two other experiments, the experiment was repeated to gain a minimum of three independent experiments showing similar results. All experiments were included in the final sum, except for cases where the controls indicated experimental problems. Experiments were excluded if the controls indicated experimental problems for example negative data for the positive controls. Data points were excluded when there was a technical mistake during the procedure of the experiment.

### Radioligand competition binding assay

Stable inducible clones of the US28-cells were seeded in poly-D-lysine (Invitrogen) coated 96-well tissue culture plates (clear plates, Costar). The number of cells seeded was determined by the apparent expression of receptors and was aimed at obtaining 5–10% binding of the added radioactive ligand. US28 receptor expression was induced by tetracycline one day after seeding the cells (0.25 µg mL−1; Invitrogen). 48 hr post seeding, cells were washed twice in ice-cold binding buffer (50 mM HEPES pH 7.4, supplemented with 1 mM CaCl2, 5 mM MgCl2 and 0.5% (w/v) bovine serum albumin) and assayed by competition binding for 3 hr at 4˚C using 10–15 pM 125I-CX3CL1, 125I-CCL5, or 125I-CCL3 as well as unlabeled ligand (10 pM to 100 nM in binding buffer). After incubation, cells were washed twice in ice-cold binding buffer, supplemented with 0.5 M NaCl.

### Ca2+ mobilization assay

US28- and HEK293 cells (as a negative control) were seeded at 2 × 104 cells per well in poly-D-lysine coated 96-well plates (black, clear bottom, Costar). US28-expression was induced 1 day after seeding by addition of 0.25 µg ml−1 tetracycline. After 24 hr, cells were loaded for 1 hr at 37˚C (5% CO2) in the dark with 0.2% Fluo-4 (Invitrogen) in loading buffer (19.6 mM HEPES pH 7.4, 1.25 mM probenecid, 1 mM CaCl2, and 1 mM MgCl2). After 1 hr incubation, cells were washed in pre-warmed loading buffer and 100 µl of the loading buffer was added to each well as a final volume. Intracellular Ca2+ mobilization was monitored upon stimulation with various concentrations of chemokines at 37˚C as fluorescence at excitation and emission wavelengths of 485 and 520 nm, respectively. The measurements were performed using a FlexStation3 (Molecular Devices, San Jose CA). If used, the antagonist was incubated in 100 µl loading buffer 10 min prior to the addition of the agonist.

### β-arrestin2 recruitment assay

The recruitment of β-arrestin2 was measured using the PathHunter β-arrestin assay (DiscoverX) as described previously (Daugvilaite et al., 2017). Briefy, cDNA encoding US28wt was fused to the ProLink C-terminal protein tag and the small fragment ofβ-galactose and cloned into pcDNA3.1+. Assays were performed using the CHO-K1 EA-arrestin cell line with the stable expression of β-galactosidase coupled to the β-gal large fragment. Cells were seeded at 2 × 104 cells per well and transfected the next day with 50 ng DNA using Fugene6 reagent (0.15 µl per well, Promega, Madison WI). 48 hr post transfection cells were stimulated with various concentrations of the chemokine for 90 min (as positive control CCR5 transient transfected cells were included, stimulated with CCL5). β-arrestin2 recruitment was detected as β-gal activity using the PathHunter detection kit (DiscoverX). Chemiluminescent substrate composed of Galacton Star Substrate, Emerald II Solution and PathHunter Cell Assay Buffer in a ratio of 1:5:19, respectively, was added to the cells (50 µL per well). The luminescent signal was determined after 60 min incubation at ambient temperature using the EnVision Multilabel Plate Reader (PerkinElmer, Waltham MA).

### Cell migration assay

Migration of serum-starved (2 hr) tetracycline induced (16 hr) US28-HEK293 was assessed using Transwell membranes (Costar; 8 μm pore size). Filters were coated for 30 min at room temperature on the lower side with 10 μg mL−1 fibronectin (dissolved in PBS; Sigma). The fibronectin solution was removed and the filters rinsed once with PBS before they were allowed to air-dry. The filters were placed in a 24-well dish that contained low serum (0.2%) DMEM supplemented with agonists or control buffer. US28-HEK293 cells suspended in 0.2% serum DMEM (with tetracycline) were added to the upper chamber (1 × 105 cells per well). Cells were allowed to migrate for 6 hr at 37˚C. Non-migrated cells were removed from the top filter surface with a damp cotton swab. Migrated cells, attached to the bottom surface, were fixed in 3.7% formaldehyde (in PBS) and dyed with crystal violet. Transmigrated cells were counted in five predefined areas on the membrane using a converted light microscope (20x objective; Leica, Wetzlar Germany).

### Alpaca immunization

A 3-year-old male alpaca (Lama pacos) was maintained in pasture, and immunized following a protocol authorized by the Camelid Immunogenics (Belchertown, MA) and MIT IACUC committees. The alpaca was immunized by subcutaneous injection of a 1:1 mixture of Imject alum (Thermo Scientific, Waltham MA) and 800 μg of recombinant US28Nb7 reconstituted in phospholipid vesicles. After a total of four injections (200 μg each) spaced 2 weeks apart, 50 mL of blood was harvested by venipuncture and collected into heparinized tubes.

### Alpaca nanobody yeast display library construction

Peripheral blood lymphocytes were isolated from total blood by Ficoll-Paque gradients (Ficoll-Paque Plus, GE Healthcare, Little Chalfont United Kingdom). Total RNA was isolated from ~2×106 fresh peripheral blood lymphocytes (PBLs) using the RNeasy Plus Mini Kit (QIAGEN), following the manufacturer’s guidelines. First strand cDNA synthesis was performed using SuperScript III reverse transcriptase (Life Technologies, Carlsbad CA) and a combination of oligo dT, random hexamer or the immunoglobulin-specific primers AlCH2 and AlCH2.2 (Maass et al., 2007). Nanobody sequences were then amplified by PCR in two steps for the generation of a yeast display library. PCR products were ethanol precipitated, and 160 μg of resulting PCR product and 40 μg linearized pCTCON2 vector (Colby et al., 2004) were co-transformed into electrocompetent EBY100 yeast (Invitrogen). Following transformation, cells were recovered in 1 L SDCAA at 30˚C. Ten-fold serial dilutions were plated onto SDCAA, grown for 3 days at 30˚C, and colonies were counted to determine library size. The resulting library was determined to contain 4.8 × 106 transformants. The library was grown at 30˚C until it reached ten-fold increase over the initial calculated diversity, then pelleted at 3000 x g, and stored in 10% glycerol at −80˚C.

### Nanobody selection by yeast surface display

For the first round of selection, 5 × 107 yeast displaying the nanobody library were cleared of non-specific binders to Alexa-647 conjugated anti-protein C antibody as described above for the yeast-displayed chemokine library. These cleared yeast were then washed with staining buffer and stained with 1 μM US28Nb7 for 2 hr at 4˚C. Magnetic selection then proceeded as described above for the yeast displayed chemokine library.

For the second round of selection, two-color FACS was performed. 1 × 107 induced yeast were washed with staining buffer and stained with 200 nM US28Nb7ΔN for 2 hr at 4˚C. The yeast were then washed with staining buffer and stained with Alexa-647 conjugated anti-protein C and Alexa-488 conjugated anti-Myc antibodies (Cell Signaling) for 15 min at 4˚C. Yeast were washed again with staining buffer and the Alexa-647 and −488 double-positive cells were purified using a FACS Jazz cell sorter (BD Biosciences). Post-sorted yeast were resuspended in SDCAA medium and cultured at 30˚C.

The third round of selection also employed two-color FACS. 1 × 107 induced yeast were washed with staining buffer and stained with 10 μM US28Nb11 for 2 hr at 4˚C. The yeast were then washed with staining buffer and stained with Alexa-647-conjugated anti-protein C and Alexa-488-conjugated anti-Myc antibodies for 15 min at 4˚C. Yeast were washed again and both double-positive cells and Alexa-488 singly positive cells were purified separately to distinguish nanobodies that bind both US28Nb7 and US28Nb11 from those that are selective. Nanobody cDNA was prepared from each of the post Round three library samples, transformed into E. coli and sequenced, yielding nanobody B1.

### Nanobody purification

Nanobody B1 was cloned into pAcGP67A insect expression vector (BD Biosciences) with a C-terminal 6xHis tag. Baculovirus was added to High Five cells at a density of 2 × 106 cell ml−1 and incubated for 60 hr at 28˚C. Collected culture media was conditioned with 50 mM Tris-HCl pH 8.0, 1 mM NiCl2, 5 mM CaCl2 and the subsequent precipitate was cleared via centrifugation. The media was then incubated with Ni-NTA resin (QIAGEN) at room temperature for 3 hr and eluted in HBS with 200 mM imidazole. The elution was further purified by size exclusion chromatography before it was concentrated and aliquoted for future protein complex formation.

### CX3CL1.35-US28Nb7-Nb B1 complex purification

CX3CL1.35 was expressed as described for chemokines above. After the initial centrifugation, the HEK293S GnTI- culture supernatant was filtered and stirred at 4˚C overnight with 10 ml protein A agarose (Sigma). The protein A agarose was then collected by filtration and washed with HBS.

US28Nb7 was expressed and solubilized as described above. Following centrifugation, protein A-immobilized CX3CL1.35–3C-Fc was added to the solubilized lysate and mixed by rotating overnight at 4˚C. The protein A resin was collected by filtration, washed with HBS and incubated at room temperature for 90 min with ~400 ng 3C protease per liter of initial culture to release the CX3CL1.35-US28Nb7 complex. Anti-FLAG M1 affinity resin was used to further purify the complex and remove excess CX3CL1.35. The complex was eluted from the anti-FLAG M1 affinity resin with 0.2 mg ml−1 FLAG peptide and 5 mM EDTA.

Nanobody B1 was added to the CX3CL1.35-US28Nb7 complex at a molar ratio of 1.25:1. The ternary complex was isolated and desalted by size exclusion chromatography using a buffer containing HBS, 0.02% (w/v) DDM, and 0.004% (w/v) CHS. Complex formation was confirmed by SDS-PAGE. The complex was then concentrated to 28 mg ml−1, aliquoted, and flash-frozen before crystallization trials.

### US28Nb7 purification

US28Nb7 purification for crystallization proceeded as described above for staining experiments. The protein was concentrated to 28 mg ml−1, aliquoted, and flash-frozen before crystallization trials.

### Crystallization, data collection and structure determination

Crystallization was performed by in meso method with the Gryphon LCP robot (Art Robbins Instruments, ARI, Sunnyvale CA). In the case of CX3CL1.35-US28Nb7-Nb B1, 1:150 (w/w) carboxypeptidases A and B (Sigma-Aldrich) were added to each protein aliquot and the mixture was incubated for 30 min at room temperature to truncate disordered C-terminal residues in situ.

US28Nb7 and CX3CL1.35-US28Nb7-Nb B1 were then reconstituted into LCP by mixing with prepared and pre-warm 10:1 (w/w) monoolein:cholesterol (Sigma-Aldrich) mixture in a 1:1.5 (w/w) protein:lipid ratio. All samples were mixed with the coupled ARI syringes at least 100 times.

The resulting LCP was dispensed in 20–50 nL onto a glass plate with a 96-well double-sided spacer tapes. The drops were then overlaid with 650 μL of crystallization buffers summarized in Figure 5—source data 1 and sealed with a cover glass. Crystals grown at 16˚C or 20˚C in 4–7 days were harvested using MicroMesh loops (MiTeGen, Ithaca NY) together with the LCP drop, flash frozen and stored in liquid nitrogen. X-ray data collection was performed at Advanced Photon Source GM/CA beamline 23ID-D. The datasets were initially processed with XDS (Kabsch, 2010). The phases were determined by molecular replacement using Phaser (McCoy et al., 2007) with the US28-Nb7 complex and Nb7 with truncation of complementarity determining regions (both are from PDB: 4xt1) as search models. The structures were further built and fixed using Coot (Emsley et al., 2010) and refined with Phenix (Adams et al., 2010; Afonine et al., 2012; Echols et al., 2012) using individual atomic displacement parameters. In the early stages of refinement, reference torsion restraints were generated (Headd et al., 2012) from the CX3CL1/US28/Nb7 crystal structure (PDB: 4xt1). Data collection and refinement statistics are also summarized in Figure 5—source data 1. Atomic contacts were analyzed and structural figures were prepared using PyMol (Schrodinger, 2010) and structural alignments of the US28 transmembrane helices and other atomic coordinate transformations were performed using LSQMAN. Software used in this project was installed and configured by SBGrid (Morin et al., 2013).
