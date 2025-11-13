# Integrated sensing of host stresses by inhibition of a cytoplasmic two-component system controls M. tuberculosis acute lung infection

## Authors

- John A Buglino<sup>1</sup> ([ORCID: 0000-0001-8961-8672](https://orcid.org/0000-0001-8961-8672))
- Gaurav D Sankhe<sup>1</sup> ([ORCID: 0000-0002-5627-2879](https://orcid.org/0000-0002-5627-2879))
- Nathaniel Lazar<sup>2</sup>
- James M Bean<sup>1</sup> ([ORCID: 0000-0001-6733-5794](https://orcid.org/0000-0001-6733-5794))
- Michael S Glickman<sup>1</sup> ([ORCID: 0000-0001-7918-5164](https://orcid.org/0000-0001-7918-5164)) †

### Affiliations

1. Immunology Program Sloan Kettering Institute New York City United States
2. Immunology and Microbial Pathogenesis Graduate Program, Weill Cornell Graduate School New York City United States
3. Division of Infectious Diseases, Memorial Sloan Kettering Cancer Center New York City United States

† Corresponding author

## Abstract

Bacterial pathogens that infect phagocytic cells must deploy mechanisms that sense and neutralize host microbicidal effectors. For Mycobacterium tuberculosis, the causative agent of tuberculosis, these mechanisms allow the bacterium to rapidly adapt from aerosol transmission to initial growth in the lung alveolar macrophage. Here, we identify a branched signaling circuit in M. tuberculosis that controls growth in the lung through integrated direct sensing of copper ions and nitric oxide by coupled activity of the Rip1 intramembrane protease and the PdtaS/R two-component system. This circuit uses a two-signal mechanism to inactivate the PdtaS/PdtaR two-component system, which constitutively represses virulence gene expression. Cu and NO inhibit the PdtaS sensor kinase through a dicysteine motif in the N-terminal GAF domain. The NO arm of the pathway is further controlled by sequestration of the PdtaR RNA binding response regulator by an NO-induced small RNA, controlled by the Rip1 intramembrane protease. This coupled Rip1/PdtaS/PdtaR circuit controls NO resistance and acute lung infection in mice by relieving PdtaS/R-mediated repression of isonitrile chalkophore biosynthesis. These studies identify an integrated mechanism by which M. tuberculosis senses and resists macrophage chemical effectors to achieve pathogenesis

## Introduction

Intracellular bacterial pathogens such as Mycobacterium tuberculosis and Salmonella that infect macrophages have evolved elaborate mechanisms to respond to the toxic environment of the macrophage phagosome and associated endocytic compartments (Olive and Sassetti, 2016; Stallings and Glickman, 2019). Phagosomal pathogens must contend with such host-inflicted stresses as oxidative stress (Bustamante et al., 2011), nitrosative stress (Darwin et al., 2003; Fang and Vázquez-Torres, 2019), iron deprivation, copper and zinc toxicity (Botella et al., 2011; Sheldon and Skaar, 2019; Shi and Darwin, 2015), and low pH (Vandal et al., 2009), among others. The pathogen response to these molecules is multifaceted and must be dynamic and graded to respond both to rapidly changing environments and the prospect of combinations of stresses that vary in intensity and composition over time. When expelled by coughing and inhaled by the naïve host, M. tuberculosis must transition from the nutrient-rich environment of the pulmonary cavity to deposition in the alveolus and engulfment by an alveolar macrophage. Such rapid transitions in environment require rapid changes in gene expression for successful adaptation.

Bacterial two-component systems (TCS) are widespread sensing systems that respond to a wide variety of ligands, including ions, gases, and metabolites. For pathogenic bacteria, TCS promote pathogenesis by modifying bacterial gene expression in response to host-inflicted toxic stresses or metabolic environments (Bretl et al., 2011; Groisman, 2016). The classic TCS sensing system consists of a membrane-bound sensor kinase that senses an extracellular ligand and activates through autophosphorylation on a cytoplasmic histidine. Transfer of this phosphate to an aspartate in the receiver domain of the cognate response regulator (RR) activates the RR to bind DNA of its target genes, thereby controlling gene expression (Sankhe et al., 2018; Zschiedrich et al., 2016).

In addition to TCS signaling, proteolysis is another widespread mechanism of bacterial signal transduction in which membrane-embedded proteases process membrane-embedded proteins, often anti-sigma factors (Schneider and Glickman, 2013; Urban, 2009). The S2P class of intramembrane proteases is widely distributed in bacteria, and several have been implicated in controlling virulence functions of bacterial and fungal pathogens, including Vibrio cholerae (Almagro-Moreno et al., 2015; Matson and DiRita, 2005), Cryptococcus (Bien et al., 2009), and M. tuberculosis. M. tuberculosis Rip1 is an important virulence determinant required for both acute growth in the lung and long-term persistence during chronic infection (Makinoshima and Glickman, 2005). Rip1 controls four independent sigma factor pathways through four anti-sigma factors substrates (Schneider et al., 2014; Sklar et al., 2010), but the virulence function of Rip1 appears to be independent of these pathways (Sklar et al., 2010). Given the importance of this pathway for M. tuberculosis pathogenesis, we sought to determine the virulence pathway(s) controlled by Rip1. These investigations, described below, uncover a new signaling system that integrates the bacterial response to Cu and NO and thereby controls growth in the host lung. The hub of this signaling system is the PdtaS/R cytoplasmic TCS, which constitutively represses virulence gene expression until inactivation by Cu and NO. The NO arm of the pathway is further controlled by titration of PdtaR from its RNA targets by an NO-induced, Rip1-controlled, small RNA, which binds directly to PdtaR and controls expression of isonitrile chalkophores. The ultimate Cu resistance mechanism controlled by Rip1/PdtaS/R is independent of chalkophores and remains to be identified.

## Results

### The Rip1 pathway defends against metal and nitrosative stress

To understand the basis for the severe virulence defect of M. tuberculosis lacking the Rip1 protease (Makinoshima and Glickman, 2005), a phenotype that is independent of the four identified Rip1-controlled sigma factor pathways (Schneider et al., 2014; Sklar et al., 2010), we hypothesized that Rip1 defends against specific host-imposed bactericidal effector molecules. We performed bacterial killing assays of wild-type (WT) M. tuberculosis and Δrip1 with nitric oxide, hydrogen peroxide, copper, zinc, low pH, detergent, lysozyme, and nutrient starvation. We observed no Rip1-dependent sensitization to starvation, lysozyme, oxidative stress, detergent, or low pH (Figure 1—figure supplement 1A–C). However, we observed that Rip1 is required for resistance to copper ions, nitric oxide, and zinc. M. tuberculosis Δrip1 is 10,000-fold more sensitive to copper on agar media than wild-type Mtb, and this phenotype is restored by genetic complementation by a plasmid encoding a wild-type copy of Rip1, but not a proteolytically inactive Rip1 (Figure 1A). Sensitivity was also observed for Δrip1 cells grown in liquid media with Cu supplementation (Figure 1—figure supplement 1D). Similarly, Δrip1 growth is inhibited by 100 μM Zn (Figure 1B), but not iron (Figure 1C). Rip1 is also required for resistance to nitric oxide. Treatment of wild-type Mtb for 3 days with 200 μM of the NO donor diethylenetriamine nitric oxide (DETA-NO) minimally reduced bacterial viability, whereas Δrip1 titers were reduced 100-fold, a phenotype that was also complemented with wild-type Rip1 but not proteolytically inactive Rip1 (Figure 1D). Importantly, similar metal nor NO sensitivity was observed for M. tuberculosis strains lacking individual or any tested combination of Rip1-controlled sigma factor pathways (Figure 1—figure supplement 2A,B), indicating that the Rip1-controlled metal/NO resistance pathway is a previously unrecognized, sigma factor-independent arm of the Rip1 pathway.

![Figure 1.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig1-v1.jpg)

**Figure 1.:** (A) The Rip1 pathway confers resistance to copper. Bacterial colony-forming units (CFUs) of the indicated strains grown on agar plates supplemented with 200 or 500 µM copper sulfate. Relative survival is normalized to untreated controls, which are set at 100 = 1. Each value is the average of technical duplicate measurements for n = 3 biological replicates. Statistical analysis by two-way ANOVA with Tukey’s multi-comparison correction *p<0.01 WT + vector 200 µM vs. Δrip1 +H21A rip1; ***p<0.001 WT + vector 500 µM vs. Δrip1 +vector; WT + vector 500 µM vs. Δrip1 +H21A rip1. (B) The Rip1 pathway confers resistance to zinc. Growth (OD600) of the indicated strains in liquid culture supplemented with 100 µM zinc sulfate. Data plotted is SEM of n = 3 biological replicates. Statistical analysis by ordinary one-way ANOVA with Tukey’s multi-comparison correction. *p<0.05, **p<0.01; day 14 WT + vector vs. Δrip1 + vector p=0.027; day 14 Δrip1 +vector vs. Δrip1 + H21A rip1 p=0.032; day 14 WT + vector vs. Δrip1 + H21A rip1 p=0.002. (C) The Rip1 pathway does not control iron sensitivity. Growth on agar plates supplemented with 300 or 600 µM iron chloride normalized to untreated controls as in (A). Each value is the average of technical duplicate measurements for n = 2 biological replicates. (D) The Rip1 pathway confers resistance to nitric oxide. CFU counts of the indicated strains post treatment with vehicle or 200 µM diethylenetriamine nitric oxide adduct (DETA-NO) for 3 days. Relative survival = CFU day 3 post treatment/CFU at day 0 for each condition n = 8 biological replicates for WT + vector, Δrip1 + vector, and Δrip1 + WT rip1, and n = 2 for Δrip1 + H21A rip1. Statistical analysis by unpaired t-test. *p<0.05; DETA-NO WT + vector vs. Δrip1 + vector p=0.041; DETA-NO Δrip1 + vector vs. Δrip1 + WT rip1 p=0.031. (E) Loss of Rip1 does not affect Cu-induced transcription. RT-qPCR quantitation of known copper-regulated transcripts ctpV, lpqS, and mymT between WT (blue) and Δrip1 (red) cells in resting (filled symbols) or 200 µM copper sulfate (open symbols) conditions for 2 hr. Values are normalized to sigA transcript levels. Values represent average of three technical replicate measurements of three biological replicates. (F) Loss of Rip1 does not affect nitric oxide-regulated gene expression through DosR. RT-qPCR comparison of nitric oxide-induced, DosR-regulated transcripts hspX, rv2625c, and dosR between WT and Δrip1 cells following 3 hr of treatment with vehicle (filled symbols) or 200 μM DETA-NO (empty symbols). Values are normalized to sigA transcript levels. Mean of biological triplicates reported. (G) NO mediates attenuation of M. tuberculosis Δrip1 in mouse lung infection. Bacterial burden (CFU) in lungs of C57bl/6 (broken lines), and age-matched Nos2-/- (solid lines) mice infected with WT M. tuberculosis (blue) or M. tuberculosis Δrip1 (red) at the indicated times (days) post infection. Data plotted is mean and SD of n = 4 biological replicates. ***p=0.0003 by unpaired t-test at 21-day time point for Δrip1 in WT vs. Nos2 -/-. (H) Repeat experiment as in (G), but with lower initial inoculum of Δrip1 M. tuberculosis in WT (open triangles) and Nos2-/- (closed squares) mice. For all strains/host day 1 n = 3 biological replicates; n = 4 biological replicates for all other time points. Statistical significance by unpaired t-test analysis is represented as *p<0.05, **p<0.01, ***p<0.001.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) Phosphate buffered saline (PBS) starvation sensitivity assay. Colony-forming units (CFUs) of the indicated strains were determined at the indicated time points post inoculation into standing flask containing PBS at a seeding density of 0.1 OD600. Relative survival = CFU Day X post inoculation/CFU at D0. n = 3 biological replicates. (B) Lysozyme, hydrogen peroxide, and sodium dodecyl sulfate (SDS) sensitivity assay. CFUs of the indicated strains were determined after treatment with 2.5 mg/mL lysozyme, 10 mM hydrogen peroxide, 0.05% SDS for 3 hr. Relative survival = CFU treatment/CFU matched untreated control. n = 3 biological replicates. (C) pH 4.5 survival assay. CFU of the indicated strains was determined after 7 days of incubation in 7H9 ADS media at the indicated pH. Relative survival = CFU pH 4.5/CFU pH 7.0. n = 3 biological replicates. (D) Loss of Rip1 confers sensitivity to Cu in liquid culture. The indicated strains were grown with or without 200 μM CuSO4 for 3 days and bacterial survival quantitated by culturing on agar media without copper. n = 7 biological replicates for WT + vector, Δrip1 + vector; n = 6 biological replicates for Δrip1 + WT rip1. *p<0.01 by Welch’s t-test.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Agar plate copper sensitivity assay. Colony-forming unit (CFU) of the indicated strains grown on agar plates supplemented with 200 or 500 µM copper sulfate normalized to untreated controls. Relative survival = CFU treatment/CFU untreated (No Addition). For WT and Δrip1, each value is the average of technical duplicate measurements for n = 3 biological replicates. Values for all other strains are the average of technical duplicates measured for n = 2 biological replicates. (B) Nitric oxide sensitivity assay. CFU counts of the indicated strains post treatment with vehicle or 200 µM diethylenetriamine nitric oxide adduct (DETA-NO) for 3 days. Relative survival = CFU day 3 post treatment/CFU at day 0 for each condition. n = 4 biological replicates for WT and Δrip1. n = 2 biological replicates for all other strains.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Rip1 does not control Cu-induced transcription through RicR. Lysates generated from the indicated strains, treated for 2 hr with the indicated concentrations of copper sulfate, were separated by SDS-PAGE and probed with anti-MymT rabbit polyclonal sera (upper panel). Blots were re-probed with rabbit polyclonal sera against CarD (lower panel) to determine relative loading. (B) Immunoblot confirmation of MymT deletion. Lysates generated from the indicated strains treated for 2 hr with 5 mM copper sulfate (+) or without addition of excess copper (-) were separated and probed as described in (A). (C) Rip1 copper sensitivity is independent of CtpV, CsoR, or MymT. Bacterial survival of the indicated strains grown on agar plates supplemented with 200 or 500 µM copper sulfate normalized to untreated controls. Relative survival = CFU treatment/CFU untreated (No Addition). For WT and Δrip1, each value is the average of technical duplicate measurements for n = 3 biological replicates. Values for all other strains are the average of technical duplicates measured for n = 2 biological replicates.

Multiple prior studies have investigated copper and NO response and resistance mechanisms in M. tuberculosis. Copper is sensed by the metal binding repressors RicR and CsoR (Festa et al., 2011; Liu et al., 2007; Marcus et al., 2016; Shi and Darwin, 2015), which control regulons involved in copper binding and export (Rowland and Niederweis, 2012; Shi et al., 2014; Ward et al., 2010). We tested whether relief of RicR or CsoR repression was impaired in Δrip1 by measuring copper-induced transcription of their target genes. We found no defect in the copper-induced transcription of mymT or lpqS (RicR targets; Festa et al., 2011) or CtpV (CsoR target) in Δrip1 cells, indicating functionality of these systems (Figure 1E, and Figure 1—figure supplement 3A,B). To determine whether a Rip1-dependent post-translational modification of copper export or chelation by CtpV (Ward et al., 2010) or MymT (Gold et al., 2008) might explain the copper sensitivity of Rip1, we performed genetic epistasis tests in Δrip1/ΔctpV and Δrip1/ΔmymT. We found minimal copper sensitivity of ΔctpV or ΔmymT, and no enhanced copper sensitivity of Δrip/ΔctpV or Δrip1ΔmymT compared to Δrip1 (Figure 1—figure supplement 3C). Additionally, de-repression of the CsoR regulon in the Δrip1 background (through Δrip1ΔcsoR) had no effect on Δrip1 copper sensitivity (Figure 1—figure supplement 3C). These results indicate that the Rip1 copper sensitivity is not due to known pathways of copper chelation or efflux. We similarly examined known NO response regulons, but found that NO-induced transcription of three DosS/T/R target genes, which controls the dominant transcriptional response to NO (Voskuil et al., 2003), was intact in Δrip1, indicating intact NO sensing at the cell surface through this TCS (Figure 1F). Our results indicate that Rip1 controls a pathway of resistance to Cu and NO, which is likely distinct from previously defined pathways.

### Nitric oxide-dependent attenuation of M. tuberculosis Δrip1

To test the importance of the Rip1-dependent NO resistance pathway in vivo, we infected NOS2-deficient mice. We reasoned that if NO is a significant attenuating pressure for M. tuberculosis Δrip1 in vivo, we would observe some reversal of the Δrip1 virulence defect when NO is removed, as has been reported for other NO-sensitive mutants (Darwin et al., 2003; Darwin and Nathan, 2005). NOS2-deficient mice infected with wild-type Mtb were highly susceptible to Mtb infection, as previously reported (MacMicking et al., 1997; Figure 1G). The impaired growth of M. tuberculosis Δrip1 in the lung was dramatically reversed in the absence of NO, such that Δrip1 lung titers in NOS2-deficient animals were 100-fold higher than in wild-type mice at 3 weeks and 10,000-fold higher at 8–10 weeks post infection (Figure 1G). A repeat infection at a lower inoculum confirmed these findings (Figure 1H). These data establish that the Rip1 pathway defends against NO in vivo during acute lung infection, possibly through a direct antimicrobial effect of NO.

### The PdtaS/PdtaR TCS controls NO and Cu resistance downstream of Rip1

The data presented above indicate that the Rip1 protease controls a pathway that defends against Cu and NO, but that this phenotype is neither attributable to previously identified Rip1-controlled sigma factor pathways nor due to known mechanisms of Cu or NO sensing. To examine the molecular basis for these phenotypes, we executed a genetic suppressor screen for spontaneous chromosomal mutations that revert the Cu sensitivity phenotype of M. tuberculosis Δrip1 (Figure 2A). M. tuberculosis Δrip1 was selected on agar media containing 500 μM CuSO4, and surviving bacteria were clonally purified, and after confirming the acquisition of Cu resistance, examined by whole genome sequencing (Figure 2A). We detected two suppressor strains with distinct mutations in the rv3220 gene, encoding the PdtaS sensor kinase: a frameshift mutation at amino acid 37 of the encoded protein (F37X) and a substitution mutation V54F. Both mutations were confirmed by sequencing of chromosomal segments amplified by PCR from the suppressor strains (Figure 2—figure supplement 1A,B). In contrast to most sensor kinases that are membrane bound, PdtaS is a soluble sensor kinase with a C-terminal histidine kinase domain and N-terminal sensing GAF (in which the suppressor mutations were detected) and PAS domains (Figure 2B). Its structure is known (Preu et al., 2012), but its function is not understood.

![Figure 2.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig2-v1.jpg)

**Figure 2.:** (A) Flow chart of a genetic suppressor screen to isolate reversion mutations of the Rip1 Cu sensitivity and testing their reversion of NO sensitivity. WGS: whole genome sequencing; SNP: single nucleotide polymorphism. (B) Domain structure of PdtaS with GAF, PAS, and kinase domains. Identified suppressor mutations of PdtaS are shown in the N-terminal GAF domain. The reported phosphorylation target of PdtaS is the PdtaR response regulator (RR), which contains a C-terminal ANTAR RNA binding domain. (C) Protein levels of the indicated alleles of pdtaS reintroduced into the Δrip1pdtaS F37X background as C-terminal 10X His fusion proteins with Rpoβ levels as a loading control. For WT, V54F, and H302Q/H303Q, two independent strains are shown, whereas for vector and G443A/G445A, one strain is shown. (D) Loss of pdtaS suppresses copper sensitivity of Δrip1. Relative survival of the indicated strains grown on agar plates supplemented with 200 or 500 µM copper sulfate normalized as in Figure 1. H302Q/H303Q and G443A/G445A are kinase dead alleles. Each value is the average of technical duplicate measurements for n = 3 biological replicates. Statistical analysis by two-way ANOVA with Tukey’s multi-comparison correction. (E) Loss of pdtaR suppresses copper sensitivity of Δrip1. Cu sensitivity assay as noted in (D). PdtaR D65A lacks the receiver aspartate for PdtaS phosphorylation. Each value is the average of technical duplicate measurements for n = 3 biological replicates. (F) Loss of pdtaS suppresses NO sensitivity of Δrip1. Colony-forming unit (CFU) counts of the indicated strains post treatment with vehicle or 200 µM diethylenetriamine nitric oxide (DETA-NO) for 3 days. Color coding of strain genotypes is the same as in (D). n = 8 biological replicates for WT, Δrip1, Δrip1pdtaS F37X; n = 6 biological replicates for Δrip1pdtaS V54F; n = 4 biological replicates for Δrip1pdtaS F37X + pdtaS, Δrip1pdtaS F37X + pdtaS H302Q/H303Q, Δrip1ΔpdtaS, ΔpdtaS; n = 3 biological replicates for Δrip1pdtaS F37X + pdtaS G443A/G445A; n = 2 for Δrip1pdtaS F37X + pdtaS V54F. Statistical analysis by Mann–Whitney test. (G) Loss of pdtaR suppresses NO sensitivity of Δrip1. CFU counts of the indicated strains post treatment with vehicle or 200 µM DETA-NO for 3 days. Color coding of strain genotype is the same as in (E). n = 8 biological replicates for WT, Δrip1, Δrip1 ΔpdtaR; n = 6 biological replicates for Δrip1ΔpdtaR + pdtaR and Δrip1ΔpdtaR +pdtaR D65A; n = 4 biological replicates for ΔpdtaR. Statistical analysis by Mann–Whitney test. For all panels, statistical significance is represented as *p<0.05, **p<0.01, ***p<0.001.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A, B) Chromatograms from seqeuncing of amplified chromosomal segments from two Δrip1 suppressor strains with restored Cu resistance. (A) shows the T insertion at amino acid 37 of PdtaS, creating a frameshift mutation. (B) shows a G>T mutation that encodes V54F in PdtaS. (C) Western blotting with anti-HA antibodies in M. tuberculosis ΔpdtaR complemented with vector, WT PdtaR HA, or PdtaR-D65A-HA in the indicated stress conditions.

To confirm that the PdtaS mutations are the functional variants reverting the Cu sensitivity, we performed complementation tests on the suppressor strains with PdtaS or PdtaS variants predicted to lack kinase activity (Figure 2C). Introduction of PdtaS into either Δrip1pdtaS(F37X) or Δrip1pdtaS(V54F) restored Cu sensitivity to both suppressor strains, indicating that the PdtaS single nucleotide polymorphisms (SNPs) are the functionally important suppressor mutations (Figure 2D). In addition, we constructed a chromosomal deletion of pdtaS (Δrip1ΔpdtaS) and observed the same pattern of PdtaS-dependent Cu sensitivity (Figure 2D). To probe the requirement of PdtaS kinase activity, we mutated histidines 302/303 to glutamines, and glycines 443/445 to alanine, which are required for autophosphorylation and kinase activity respectively (Trajtenberg et al., 2010), and expressed these variants in the Δrip1pdtaS(F37X) strain. Although both kinase dead proteins were expressed to equivalent levels (Figure 2C), neither were able to restore Cu sensitivity (Figure 2D), indicating a requirement for PdtaS kinase activity in controlling Cu resistance.

PdtaS was reported to phosphorylate the RR PdtaR (Morth et al., 2005), which is itself an atypical RR in that it contains an ANTAR RNA binding domain (Ramesh et al., 2012) instead of the DNA binding domain present in many RRs. To validate the participation of PdtaR in the Δrip1 Cu sensitivity, we constructed Δrip1ΔpdtaR and tested Cu sensitivity. We observed that loss of pdtaR reverted the Cu sensitivity (Figure 2E) of Δrip1. Complementation of Δrip1ΔpdtaR with pdtaR restored copper sensitivity (Figure 2E). However, expression of a PdtaR-D65A, which lacks the receiver aspartate phosphorylated by PdtaS, was partially active, partially restoring Cu sensitivity to Δrip1ΔpdtaR at low-dose Cu and completely at higher-dose Cu (Figure 2E). These results suggest that phosphorylation of PdtaR is not absolutely required for its activity in the Cu sensitivity pathway.

The suppressor mutations in PdtaS were identified as suppressors of Cu sensitivity, but the NO sensitivity might be due to a different Rip1-dependent pathway. However, we observed that loss of pdtaS in Δrip1 also reverted the NO sensitivity nearly to the level of WT M. tuberculosis (Figure 2F), with the same requirement for PdtaS kinase activity. In addition, inactivation of pdtaS in wild-type cells conferred a hyperresistance to NO (Figure 2F). We next tested the involvement of PdtaR in the NO sensitivity phenotype of Δrip1 and found the loss of pdtaR reverted to the level of the wild-type strain (Figure 2G). We also observed a partial activity of PdtaR D65A, which partially complemented in comparison to WT PdtaR (Figure 2G). Loss of PdtaR in wild-type Mtb conferred hyperresistance to NO compared to the parental wild-type strain, again indicating that PdtaR suppresses NO resistance (Figure 2G). Taken together, these results demonstrate that the Cu and NO sensitivity conferred by loss of rip1 proceeds through an active PdtaS/R signaling system and that these two sensitivity phenotypes represent an integrated signaling pathway that responds to both stresses.

### NO and Cu directly inhibit PdtaS kinase activity

The data above suggests that PdtaS/PdtaR acts as a negative regulator of Cu and NO resistance, and that this negative regulation is not relieved in the Δrip1 background. Genetic deletion of pdtaS/R relieves this inhibition and restores wild-type stress resistance. Although the PdtaS GAF domain was recently reported to bind cyclic di-GMP (Hariharan et al., 2021), the full set of ligands that interact with the PdtaS sensing domains are not known. To determine whether PdtaS/R directly senses cytosolic metals and/or nitric oxide, we reconstituted the PdtaS/R phosphotransfer reaction using purified proteins. The PdtaS kinase was active for autophosphorylation when assayed with radiolabeled ATP (Figure 3A), as previously reported (Morth et al., 2005), and was also active in phosphotransfer to PdtaR (Figure 3A). PdtaS autophosphorylation was not inhibited by calcium or iron at 1 mM (Figure 3—figure supplement 1A), but we observed strong dose-dependent inhibition of PdtaS autophosphorylation at 10–1000 μM Cu (Figure 3B) or similar zinc concentrations (Figure 3—figure supplement 1B,C). Titrations revealed a dose-dependent inhibition of PdtaS activity by these metals, with inhibition constants (Ki) of 34 μM for Cu and 26 μM for zinc (Figure 3B, F, Figure 3—figure supplement 1C). These data indicate that copper and zinc directly inhibit the kinase activity of PdtaS.

![Figure 3.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig3-v1.jpg)

**Figure 3.:** (A) PdtaS phosphotransfer to PdtaR. Upper panel: phosphorscreen imaging of 32P incorporation; lower panel: Coomassie brilliant blue (CBB) staining to determine total protein. First reaction contains PdtaS alone, second and third lanes contain PdtaS/PdtaR incubated for 10 and 20 min, respectively. Fourth lane (M) is the molecular weight (MW) marker. (B) Cu++ inhibits PdtaS autophosphorylation. Autophosphorylation of PdtaS protein preincubated with increasing concentrations (5 µM to 104 µM) of CuCl2 or 1 mM of CaCl2 (Ca++) as a control. Upper panel: phosphorscreen imaging of 32P incorporation; lower panel: CBB staining to determine total protein. (C) NO inhibits PdtaS autophosphorylation. Autophosphorylation of PdtaS protein preincubated with increasing concentrations (5 µM to 104 µM) of spermine NONOate and 1 mM of spermine NONOate post NO release as control (designated by C). (D) PdtaS GAF domain cysteine 53 is required for copper inhibition. PdtaS-C53A protein preincubated with increasing concentrations (5 µM to 104 µM) of CuCl2 or 1 mM of CaCl2 was assayed for autophosphorylation as described in panel B . (E) PdtaS GAF domain cysteine 53 is required for NO inhibition. PdtaS-C53A protein preincubated with increasing concentrations (5 µM to 104 µM) of spermine NONOate and of 1 mM of spermine NONOate post NO release as control was followed by autophosphorylation. (F) Cu inhibition curve from replicate data represented by (B) and (D) for PdtaS (blue) and PdtaS-C53A (green) proteins yields Ki of (34 ± 8 µM) for PdtaS and (5540 ± 2381 µM) for PdtaS-C53A. Error bars are SEM for n = 3. (G) NO inhibition curve from replicate data represented by (C) and (E) and (Figure 3—figure supplement 2) for PdtaS (blue), PdtaS-C53A (green), or PdtaS-C57A (red) proteins yields Ki of (7 ± 2 µM) for PdtaS and (73 ± 34 µM) for PdtaS-C53A. Error bars are SEM for n = 3 for WT and C53A and n = 2 for C57A.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) PdtaS is not inhibited by calcium or iron. Autophosphorylation of PdtaS protein preincubated with 1 mM CaCl2 or FeCl2. Upper panel: phosphorscreen imaging of 32P incorporation; lower panel: Coomassie brilliant blue (CBB) staining to determine total protein. M: molecular weight marker. (B) Zinc inhibits PdtaS autophosphorylation. Autophosphorylation of PdtaS protein preincubated with increasing concentrations (5 µM to 10 mM) of ZnCl2 or 1 mM of CaCl2 (Ca++) as a control. Upper panel: phosphorscreen imaging of 32P incorporation; lower panel: CBB staining to determine total protein. (C) Zn inhibition curve from replicate data represented by (B) for PdtaS protein. Error bars are SEM for n = 3. (D) PdtaS is not inhibited by H2S. Same assay as in (B), but with escalating concentration of H2S from sodium hydrosulfide hydrate. (E) The PdtaS kinase domain is not inhibited by Cu. PdtaS-kinase (amino acids 277–501) domain was assayed for autophosphorylation with the indicated concentrations of CuCl2. (F) The PdtaS kinase domain is not inhibited by NO. PdtaS-kinase (amino acids 277–501) domain was assayed for autophosphorylation with the indicated concentrations of spermine NONOate. (G) Cu inhibition curve from replicate data represented by (E) for PdtaS-kinase domain protein. The WT PdtaS curve is the same data presented in Figure 3F. Error bars are SEM for n = 3. (H) NO inhibition curve from replicate data represented by (F) for PdtaS-kinase domain protein. The WT PdtaS curve is the same data presented in Figure 3G. Error bars are SEM for n = 3.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Autophosphorylation of the PdtaS protein as in Figure 3 using the PdtaS-C57A protein.

We next asked whether NO has a similar effect on PdtaS. We used spermine NONOate, an NO donor with a half-life of NO release of 40 min. NO had a dose-dependent inhibitory effect on PdtaS activity, but spermine NONOate, which had been exhausted for NO release, had no effect (Figure 3C). The Ki determined from dose titrations was 7 μM. There was no effect of hydrogen sulfide on PdtaS activity (Figure 3—figure supplement 1D). Consistent with the idea that these ligands inhibit signaling without affecting expression or stability of the signaling proteins, we observed no change in PdtaR protein expression or proteolysis in vivo upon treatment with Cu, Zn, or NO (Figure 2—figure supplement 1C). These data indicate that PdtaS directly senses metals and NO and implies that ligand sensing by the sensor kinase inhibits signaling through the PdtaS/R system.

PdtaS contains GAF and PAS domains N-terminal to the kinase domain. PAS domains bind a wide variety of small molecule ligands (Aravind and Ponting, 1997; Henry and Crosson, 2011). As noted above, the two suppressor mutations in PdtaS are in the GAF domain, one a frameshift that inactivates the protein and one (V54F) in close proximity to a dicysteine motif (53-CVAQC-57) (Figure 2B, Figure 2—figure supplement 1). To determine whether these domains are required for NO and Cu inhibition of PdtaS, we purified the PdtaS kinase domain, which was constitutively active (Figure 3—figure supplement 1E,F). However, neither Cu nor NO had a substantial inhibitory effect on the isolated kinase domain (Figure 3—figure supplement 1E,F), indicating that the GAF-PAS are required for the ligand-dependent inhibitory effect. We next mutated each cysteine in the PdtaS GAF in proximity to the V54F suppressor (C53A or C57A) and tested these kinases for Cu and NO inhibition. PdtaS-C53A was refractory to inhibition by both ligands (Figure 3D–G), directly implicating cysteine 53 in the GAF domain in Cu and NO sensing. PdtaS-C57A was also resistant to NO inhibition (Figures 3G, Figure 3—figure supplement 2), but our attempts to determine Cu inhibition of this protein were unsuccessful due to protein aggregation, preventing accurate quantitation (data not shown). These results indicate that the PdtaS sensor kinase is a constitutively active, ligand-inhibited signaling protein that integrates Cu and NO sensing through a dicysteine motif in the GAF domain.

### Rip1/PdtaR jointly control an NO-responsive regulon that includes chalkophore biosynthesis

The data above indicates that PdtaS/R is a negative regulator of Cu and NO resistance and that these ligands directly inhibit PdtaS signaling. The exact function of PdtaR in regulating gene expression is not known. PdtaR-type RRs contain an ANTAR domain in place of the more commonly encountered DNA binding domain of traditional RR. In the few examples that have been examined, ANTAR domains bind to dual hairpin structures at the 5′ ends of mRNA, and thereby influence transcriptional termination (Fox et al., 2009), but the full spectrum of gene regulation conferred by ANTAR domain RNA binding has yet to be elucidated. ANTAR-RRs in Listeria and Enterococcus are also regulated by trans acting small RNAs that compete for ANTAR domain binding and thereby titrate the RR away from other mRNA targets (DebRoy et al., 2014; Mellin et al., 2014). To understand the target genes controlled by Rip1/PdtaS/PdtaR, we performed RNA sequencing under NO stress. We focused on NO stress for several reasons, including (1) the strong phenotypic reversion of Δrip1 in iNOS-deficient mice (Figure 1G), (2) the strong phenotypic reversion of Rip1 NO sensitivity by the pdtaR mutation, and (3) the technical advantages of treating Mtb with carefully titrated NO donors in liquid culture.

RNA sequencing of WT, Δrip1, Δrip1ΔpdtaR, and ΔpdtaR treated with vehicle or DETA-NO revealed that the NO-induced DosR regulon was intact in the Δrip1 strain and unaffected by loss of PdtaR (Figure 4A). However, by clustering gene expression across all strains and conditions, we defined a cluster of NO-induced, Rip1-dependent genes for which the defective expression is restored to WT levels in the Δrip1ΔpdtaR strain, thereby matching the phenotypic pattern seen in our NO sensitivity tests (red box in Figure 4B). Consistent with these genes being negatively regulated by PdtaS/R in wild-type cells and the hyperresistance of the ΔpdtaR strain to NO (Figure 2G), this gene set was hyperinduced in the ΔpdtaR strain by NO (Figure 4). Importantly, there was no effect on basal gene expression with loss of pdtaR, indicating that inactivation of this TCS is not sufficient to activate gene expression in the absence of NO stress (Figure 4B).

![Figure 4.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig4-v1.jpg)

**Figure 4.:** (A) Unsupervised clustering of the diethylenetriamine nitric oxide (DETA-NO) (NO)-induced, DosR-regulated transcripts across the indicated genotypes. The scale bar represents the log2 of the normalized counts for each gene. (B) Unsupervised clustering of gene expression of M. tuberculosis WT, Δrip1, ΔpdtaR, and Δrip1ΔpdaR using the same color coding as in (A) treated with vehicle (V) or DETA-NO (NO) The highlighted cluster indicated by the red box on the left includes PPE1-5′, the PPE1 coding sequences after PPE1 (PPE1-after 5′), and the Rv0097-nrp cluster as independent elements. The scale bar represents the log2 of the scaled expression level for each row. The clustering of the genes and strains/conditions is done on the raw normalized counts. (C) Read coverage tracks across the ppe1-nrp cluster. Boxed areas highlight ppe1-5′ peak at the 5′ end of PPE1 and a region of potential termination at 5′ end of nrp. (D) DETA-NO-induced fold change values (DETA-NO/vehicle) across the same coverage region as in (C). 0097-nrp designates the entire Rv0097-nrp cluster.

Among the most strongly regulated genes controlled by Rip1/PdtaS/R under NO stress is a gene cluster from Rv0096-0101. This gene set encodes the PPE1 protein (rv0096) and five genes (rv0097-0101) that synthesize isonitrile lipopeptide chalkophores (Harris et al., 2017; Wang et al., 2017), which bind copper with high affinity (Wang et al., 2017; Xu and Tan, 2019). Alignment of RNA sequencing reads along the chalkophore cluster revealed low expression in basal conditions, but with a prominent small peak of 210 NT at the 5′ end of the nrp gene, indicating a site of potential termination (Figure 4C). With NO, chalkophore operon expression increased by three- to fivefold across the gene cluster in WT cells, but not in Δrip1 (Figure 4C, D). The defective chalkophore cluster expression is reversed in the Rip1/PdtaR double mutant. RNA reads mapping to the PPE1 locus, in contrast, mapped to a 336NT region that begins in the intergenic region at the reported transcription start site of the PPE1 mRNA and continues 277 nt beyond the PPE1 translational initiation codon (Figure 4C). We defined this element as ‘PPE1-5′’ and calculated its induction ratio with NO in comparison to the PPE1 coding sequence and the rest of the chalkophore operon. PPE1- 5′ is induced 33-fold by NO in wild-type cells, an induction that requires Rip1 (Figure 4D). PPE1-5′ is negatively regulated by PdtaR as evinced by hyperinduction in the ΔpdtaR strain. Loss of PdtaR restores the expression of PPE1-5′ in the Δrip1 background. Similar patterns were observed for each gene in the chalkophore operon and the chalkophore transcriptional unit as a whole (Figure 4D). These results identify a previously unappreciated NO-induced regulon that is subject to dual regulation by a positive transcriptional signal through the membrane-bound Rip1 protease and a negative signal from the cytoplasmic PdtaS/R TCS. Our data also identifies a previously unknown, NO-induced putative small RNA at the 5′ end of the chalkophore operon.

### PPE1-5′ binds directly to PdtaR

The data above indicate that Cu and NO resistance and PPE1-5′ expression in Mtb require a functional Rip1 and inhibition of the PdtaS/R system, which does not occur without Rip1. These cooperating systems jointly control chalkophore operon expression. One mechanism to unify these findings would be that the Rip1-controlled PPE1-5′ RNA binds directly to PdtaR to relieve the negative regulation of PdtaR on target genes such as nrp. As noted above, this mechanism of regulation by trans acting RNAs on ANTAR domain regulators has been reported previously (DebRoy et al., 2014; Mellin et al., 2014) and would explain why Rip1 is required to inactivate PdtaR activity. Inspection of the predicted RNA sequence of PPE-1-5′ for predicted RNA secondary structure that might bind PdtaR revealed three hairpins in the vicinity of the PPE-1 translational initiation codon (Figure 5A). To test whether this RNA may bind PdtaR, we produced a 284 nt PPE1-5′ RNA by in vitro transcription, along with positive (Mehta et al., 2020) and negative control RNAs (Figure 5—figure supplement 1A,B) and tested binding to PdtaR using microscale thermophoresis (MST). PdtaR was phosphorylated in vitro by PdtaS and binding was measured at varying concentrations of RNA. Negative control RNA derived from the dnaK gene did not bind PdtaR detectably (Figure 5B, Figure 5—figure supplement 1C) and the previously reported PdtaR binding RNA from rv3864 (Mehta et al., 2020) bound with a Kd of 2 μM (Figure 5B). We detected strong binding between phosphorylated PdtaR and PPE1-5′ with a calculated Kd of 0.41 μM (Figure 5B). We tested the requirement for PdtaR phosphorylation in the PdtaR-PPE1-5′ interaction by omitting PdtaS. Surprisingly, given the usual requirement for phosphorylation in activating RR function, PdtaR binding to the rv3864 RNA was not affected by phosphorylation (Figure 5C). Unphosphorylated PdtaR still bound PPE1-5′, albeit with threefold lower affinity (Kd0.4 vs. 1.2 μM, Figure 5C), indicating that phosphorylation enhances binding but is not absolutely required.

![Figure 5.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig5-v1.jpg)

**Figure 5.:** (A) Predicted structure of the RNA hairpins in PPE1-5′. The nucleotide numbering refers to distance from the first transcribed nucleotide of the ppe1 RNA. The PPE1 translational initiation codon is indicated within the first hairpin. (B) Phosphorylated PdtaR directly binds to ppe1-5′. Change in the thermophoretic movement of fluorescently labeled and phosphorylated PdtaR was measured as a function of titrant RNA concentration on the X-axis for ppe1-5′, rv3864, and dnaK (ranging from 0.31 nM to 10 µM) as described in Materials and methods yielding binding affinity constants (Kd) for ppe1-5′ = 410 ± 84 nM, rv3864 = 2117 ± 798 nM while dnaK shows no binding. Error bars are SEM for n = 3. (C) RNA binding by PdtaR is partially phosphorylation dependent. Identical assay as in (B) using PdtaR without phosphorylation by PdtaS. Changes in the thermophoretic movement of fluorescently labeled PdtaR were measured as a function of titrant RNA concentration: ppe1-5′ (0.15 nM to 10 µM), rv3864 (0.61 to 10 µM), and dnaK (0.15 nM to 10 µM). Binding affinities (Kd) are ppe1-5′ = 1281 ± 322 nM, rv3864 = 2592 ± 832 nM while dnaK shows no binding. Error bars represent SEM for n = 3. (D) Rip1/PdtaS/PdtaR control of PPE1-5′ and chalkophore biosynthesis controls NO resistance. Constitutive expression of annotated protein coding region of ppe1 alone (+ppe1 ORF hsp60), ppe1 coding region plus 222-nt 5′ of start codon (+ppe1-5′), both C-terminally fused to GFP, or the chalkophore cluster (+rv0097-nrp) in Δrip1 and testing for diethylenetriamine nitric oxide (DETA-NO) sensitivity. Relative survival of the indicated strains post treatment with vehicle or 200 µM DETA-NO. n = 8 biological replicates for WT, Δrip1, Δrip1: PPE1 ORFpHSP60; n = 10 biological replicates for Δrip1:PPE1 ORF +5'pHSP60 and Δrip1: Rv0097-nrppHSP60. Statistical analysis by Mann–Whitney test. (E) Rip1/PdtaS/PdtaR control of PPE1-5′ and chalkophore biosynthesis does not control copper resistance. Relative survival of the same strains as in (D) grown on agar plates supplemented with 0, 200, or 500 µM copper sulfate normalized as in Figure 1. Each value is the average of technical duplicate measurements for n = 3 biological replicates. For all panels, statistical significance by t-test analysis is represented as *p<0.05, **p<0.01, ***p<0.001.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A) RNA sequences of RNAs produced by in vitro transcription and used in binding studies in Figure 5B, C. (B) Gel electrophoresis of purified RNAs produced by in vitro transcription. (C, D) Microscale thermophoresis titrations for dnaK RNA showing no appreciable binding to PdtaR (C) or PdaR-P (D) for the DnaK RNA. This data is represented on the binding curves in Figure 5B, C.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) PPE1 is equivalently expressed independent of PPE-5′. Δrip1 cells transformed with vector, or plasmids encoding C-terminal GFP fused PPE1 ORF (PPE1 GFP), or C-terminal GFP fused PPE1 ORF + PPE1-5′ (PPE1 GFP + 5′UTR), both expressed from the hsp60 promoter, were lysed and blotted as described in Materials and methods. Upper panel: anti-GFP; lower panel: Rpoβ loading control. (B) Loss of chalkophore biosynthesis alone does not confer NO sensitivity. Colony-forming unit (CFU) counts of the indicated strains post treatment with vehicle or 200 µM diethylenetriamine nitric oxide (DETA-NO) for 3 days. Relative survival = CFU day 3 post treatment/CFU at day 0 for each condition. n = 4 biological replicates for WT and Δrip1; n = 2 biological replicates for Δnrp. *p<0.05 by unpaired t-test.

### Chalkophore operon expression is the functional target that mediates Rip1/PdtaS/R-controlled NO resistance

To determine whether Rip1/PdtaS/PdtaR regulation of PPE1-5′ or the chalkophore cluster controls NO sensitivity, we restored expression of either the PPE1 coding sequence lacking the PPE1-5′ (hsp60-PPE1), PPE1 including PPE1-5′, or the chalkophore biosynthetic machinery (hsp60-Rv0097-Rv0101) in the Δrip1 strain. Restored expression of chalkophore biosynthesis (rv0097-nrp) restored NO resistance to a level equivalent to WT cells (Figure 5D). Enforced expression of PPE1 without PPE1-5′ had a minimal effect on NO sensitivity, whereas expression of PPE1 with PPE1-5′ restored NO resistance to the level similar to that observed with chalkophore re-expression (Figure 5D), despite no difference in the protein levels of PPE1 expressed from these two promoter constructs (Figure 5—figure supplement 2A). Despite the strong copper avidity of chalkophores, which might suggest a role in ameliorating Cu toxicity by direct binding, as is the case for other Cu binding molecules such as MymT, restoration of chalkophore production or expression of either PPE-5′ or PPE1 did not rescue the copper sensitivity of the Δrip1 strain (Figure 5E). Deletion of the nrp gene alone did not alter NO resistance, indicating that there are multiple targets downstream of Rip1/PdtaS/R that contribute to NO resistance (Figure 5—figure supplement 2B). These results indicate that NO-induced expression of PPE1-5′ and chalkophore biosynthesis controlled by Rip1/PdtaS/PdtaR signaling are critical determinants of NO resistance in M. tuberculosis.

### Rip1/PdtaS/R control of chalkophore biosynthesis mediates acute lung infection

The model that emerges from the data presented above is that M. tuberculosis utilizes a two-signal mechanism to respond to the combinatorial stresses of the host: Rip1-dependent inactivation of PdtaR through the PPE1 5′ RNA and direct inhibition of PdtaS through the cysteine motif in the PdtaS GAF domain. This combined inhibition of PdtaS/R signaling relieves the negative regulation of this system on chalkophore biosynthesis. This model predicts that the in vivo virulence defect conferred by loss of Rip1, which is reversed by ablation of host NO (Figure 1G), should also be (1) phenocopied by loss of chalkophore biosynthesis (2) reversed in the Δrip1/ΔpdtaR strain. We first tested the phenotype of M. tuberculosis lacking chalkophore biosynthesis (Δnrp). Loss of nrp conferred mild attenuation in the early stages of lung growth such that Δnrp titers were approximately 10-fold lower than wild type at 14 and 21 days after aerosol infection (Figure 6A). Loss of nrp also conferred more severe attenuation of extrapulmonary growth, which persisted during chronic infection (Figure 6B). We next infected mice by aerosol with Δrip1/ΔpdtaR along with WT, Δrip1, and ΔpdtaR. We observed that the severe attenuation of lung growth conferred by loss of Δrip1 was substantially reversed by loss of pdtaR such that bacterial lung titers of Δrip1/ΔpdtaR were 15- and 97-fold higher than Δrip1 at 7 and 14 days post aerosol deposition, respectively (Figure 6C). Although lung titers of Δrip1/ΔpdtaR were significantly lower than ΔpdtaR, which was attenuated compared to wild type, loss of pdtaR reversed the majority of the Rip1-dependent attenuation in the first two weeks of infection (Figure 6C). Importantly, the Rip1/PdtaR axis is only relevant to acute lung infection as loss of pdtaR did not reverse the severe attenuation of Δrip1 during chronic infection (Figure 6C) and had no effect on extrapulmonary tissues (Figure 6D), indicating that other pathways mediate these virulence phenotypes.

![Figure 6.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig6-v1.jpg)

**Figure 6.:** (A, B) Bacterial burden (colony-forming unit [CFU]) of the indicated strains in lungs (A) or spleens (B) of C57bl/6 mice infected with WT (blue circle), Δnrp (red square), or Δnrp +nrp (green triangle) at the indicated time points (days) post aerosol infection. For WT and Δnrp, n = 6 biological replicates on day 1 and n = 8 on all subsequent days. All p values calculated by unpaired t-test. (C, D) Bacterial burden (CFU) of the indicated strains in lungs (C) or spleens (D) of C57bl/6 mice infected with WT (blue circle), Δrip1 (red square), or Δrip1ΔpdtaR (purple inverted triangle) or ΔpdtaR (green triangle) at the indicated time points (days) post aerosol infection. For all strains, n = 5 biological replicates on day 1; n = 12 biological replicates on day 7; n = 8 biological replicates on days 15, 21, and 56; n = 4 biological replicates on days 105 and 156. For all panels, statistical significance by unpaired Welch’s t-test is represented as *p<0.05, **p<0.01.

## Discussion

We have revealed a new branched pathway of signal transduction that integrates M. tuberculosis resistance to multiple host-derived stresses. M. tuberculosis is exposed to a mixture of toxic molecules within the host macrophage that include copper, zinc, and nitric oxide (Botella et al., 2011; Darwin, 2015; Darwin et al., 2003; Darwin and Nathan, 2005; Shi et al., 2014). Although signal transduction systems that respond to each of these molecules have been identified, the true in vivo determinants of M. tuberculosis resistance to these molecules are unknown. Additionally, although stresses are often assayed monolithically in vitro, this approach belies the situation in vivo, which the pathogen must sense and respond to simultaneous chemically distinct stresses that vary in intensity over time. Our studies identify an integrated sensing system that M. tuberculosis uses to directly sense combinations of stresses using a single sensing circuit.

The hub of this signaling system is the PdtaS/R TCS. This TCS is distinct from previously characterized TCS in M. tuberculosis in both structure and mechanism of regulation. The sensor kinase, PdtaS, is cytosolic rather than membrane bound. PdtaS is constitutively active in vitro (Mehta et al., 2020), and our data indicates the mechanism of signal transduction is ligand-induced inhibition of this constitutive activity. Rather than being activated by its ligands, PdtaS is inhibited by copper and NO through a dicysteine motif in the N-terminal GAF domain, defining an integrated mechanism by which two chemical effectors are sensed. The constitutively active PdtaS/R system negatively regulates a subset of genes required for NO resistance and relief of this inhibition by ligand-induced shutoff of PdtaS is necessary, but not sufficient, for expression of genes required NO resistance.

Our data also strongly demonstrates that full inhibition of PdtaS/R signaling requires the transduction of a cell surface signal by the intramembrane protease Rip1. Rip1 was originally identified as a S2P required for both acute growth in the mouse lung and persistence of the bacterium during chronic infection (Makinoshima and Glickman, 2005). Four anti-sigma factor substrates have been identified, but none of these previously identified pathways explain the virulence defects of M. tuberculosis lacking Rip1. The data presented here indicate that critical virulence function of Rip1 is to relieve PdtaR repression through control of a previously unrecognized small RNA at the 5′ end of the PPE1 gene. Rip1-controlled expression of PPE1 5′ is required for NO resistance as re-expression of this element is sufficient to reverse the NO sensitivity of Δrip1 and to re-express the chalkophore operon, itself sufficient to mediate NO resistance. The PPE1-5′ RNA binds directly to PdtaR in vitro, and this binding is enhanced, but does not absolutely require, PdtaR phosphorylation by PdtaS. This data, coupled with our genetic data, indicates that Rip1 control of PPE1-5′ directly inhibits PdtaR and de-represses PdtaR targets, which are ordinarily repressed by the PdtaS/R cascade. This mechanism of RNA-based titration of ANTAR domain RRs away from competitor target RNAs has been described as a mechanism of regulation in Enterococcus and Listeria (DebRoy et al., 2014; Mellin et al., 2014). This model suggests a branched logic of the Rip1/PdtaS/PdtaR system. Two signals are required to fully inactivate the PdtaS/R system and mediate NO resistance. A positive Rip1 transcriptional signal from the membrane to produce PPE1-5′ to sequester PdtaR, and a cytoplasmic inhibitory signal through the PdtaS kinase mediated by direct sensing of NO by the PdtaS GAF domain, which inhibits kinase activity. Our findings that PdtaR phosphorylation is not absolutely required for its function in NO resistance in vivo or RNA binding in vitro supports the model that two signals, PdtaS inhibition and PdtaR titration by the PPE1-5′ RNA, cooperate to titrate the activity of the PdtaS/R system. Our integrated model of this system is presented in Figure 7.

![Figure 7.](https://cdn.elifesciences.org/articles/65351/elife-65351-fig7-v1.jpg)

**Figure 7.:** NO and copper resistance is mediated by cell surface and cytoplasmic convergent signals that inactivate PdtaS/PdtaR. In basal conditions, PdtaS/R is constitutively active, and that activity holds virulence genes, including chalkophore biosynthesis, inactive. NO or copper directly inhibit PdtaS activity through direct sensing by PdtaS N-terminal GAF domain. NO shutoff of PdtaS kinase activity requires C53 and 57, whereas Cu shutoff requires C53 with the role of C57 unknown. Sensing of NO at the cell surface contributes a second signal to relief of PdtaS/R by inducing Rip1-dependent expression of a hairpin containing small RNA at the 5′ end of the PPE1 gene (PPE1-5′), which binds directly to the ANTAR domain containing PdtaR. These signals relieve PdtaS/R repression of virulence gene expression, including chalkophore biosynthesis, to activate NO resistance. Although our data clearly implicates the upstream Rip1/PdtaS/PdtaR cascade in Cu resistance, the downstream targets that mediate Cu resistance are not known (indicated by ?). Despite the high Cu affinity of the isonitriles produced by the nrp locus, these molecules are involved in the NO resistance arm of the pathway rather than Cu. Figure constructed with BioRender.

Our findings also clearly indicate that the coupled Rip1/PdtaS/R circuit controls Cu and NO resistance, but the gene sets downstream of this cascade that mediate resistance to each ligand are distinct. The NO resistance is due to regulation of isonitrile chalkophore biosynthesis. These lipopeptide molecules were recently defined in Streptomyces and Mycobacterium marinum as the products of the Nrp nonribosomal peptide synthase (Harris et al., 2017; Wang et al., 2017). The nrp gene has also been identified in multiple studies as a determinant of virulence (Bhatt et al., 2018), although the mechanism was not defined. The structure of the TB chalkophore is not known, but the Streptomyces molecule binds copper with extremely high affinity (Xu and Tan, 2019). Despite this Cu binding and an expectation that this property would predict a role in Cu resistance, our data instead indicate that these molecules are not acting to diminish copper toxicity and rather that their function is to ameliorate or prevent NO toxicity. The exact mechanisms by which chalkophores contribute to NO resistance in M. tuberculosis are not defined here, but in Methanotrophs chalkophores help maintain the activity of Cu-containing enzymes in the membrane (Kenney and Rosenzweig, 2018). An analogous function in mycobacteria might imply that NO stress displaces Cu from thiol metal centers, an activity that has been shown with MymT (Gold et al., 2008), and that chalkophores may compensate for this toxicity. This hypothesis and others will require further characterization of chalkophore functions in mycobacteria.

Although the Rip1/PdtaS/PdtaR cascade jointly controls NO and Cu resistance, we did not identify the chromosomal targets of PdtaS/R that mediate the Cu arm of the pathway. The Cu resistance controlled by this signaling cascade is distinct from known mechanisms of Cu binding or efflux based on our genetic data. Our data showing that NO-induced transcription of the PPE1-5′ RNA is the second signal in the NO resistance pathway, but not Cu resistance, leads us to hypothesize that as yet unidentified Rip1-controlled small RNA titrates away PdtaR from targets involved in Cu resistance. This model (Figure 7) implies that the target RNAs controlled by PdtaR may be modified based on the activating stress, a hypothesis that will be pursued in future work to determine the full complement of RNAs binding to PdtaR under Cu and NO stress.

In summary, our results identify a previously unrecognized mechanism of bacterial signal transduction that allows Mtb to rapidly adapt to the toxic environment of the host lung. This study opens a window into several important future questions, including the full spectrum of RNAs bound by the PdtaR RR, the ultimate mechanism by which this sensing circuit controls NO resistance, and the mechanisms of PdtaS sensing of ligand. These future questions will add additional detail to the critical mechanisms of TB pathogenesis identified here and potentially identify a critical pathway for therapeutic development against Mtb.

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
      <td>Strain, strain background (Mycobacterium tuberculosis)</td>
      <td>M.tb Erdman (WT, EG2)</td>
      <td>Lab Stock</td>
      <td>ATCC 35801</td>
      <td>Animal passaged</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>DH5α</td>
      <td>Lab Stock</td>
      <td>ATCC SCC2197</td>
      <td>Plasmid maintenance strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>EL350/ phAE87</td>
      <td>Lab Stock</td>
      <td></td>
      <td>Phage packaging strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>Rosetta 2 (DE3)</td>
      <td>Millipore Sigma</td>
      <td>Cat# 71397</td>
      <td>Recombinant protein expression strain</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus) female</td>
      <td>C57BL/6J</td>
      <td>Jackson Laboratory</td>
      <td>Stock no: 000664; RRID:IMSR_JAX:000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus) female</td>
      <td>B6;129P2-Nos2tm1Lau/J</td>
      <td>Jackson Laboratory</td>
      <td>Stock no: 002596; RRID:IMSR_JAX:002596</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>rip1</td>
      <td>ATCC 35801</td>
      <td>Erdman_3146</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>sigK</td>
      <td>ATCC 35801</td>
      <td>Erdman_0488</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>sigL</td>
      <td>ATCC 35801</td>
      <td>Erdman_0808</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>sigM</td>
      <td>ATCC 35801</td>
      <td>Erdman_4291</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>sigD</td>
      <td>ATCC 35801</td>
      <td>Erdman_3735</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>mymT</td>
      <td>ATCC 35801</td>
      <td>Rv0186A</td>
      <td>nt217703-217864 Erdman Genome</td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>ctpV</td>
      <td>ATCC 35801</td>
      <td>Erdman_1076</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>csoR</td>
      <td>ATCC 35801</td>
      <td>Erdman_1074</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>nrp</td>
      <td>ATCC 35801</td>
      <td>Erdman_0118</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>ppe1</td>
      <td>ATCC 35801</td>
      <td>Erdman_0113</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>rv0097</td>
      <td>ATCC 35801</td>
      <td>Erdman_0114</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>fcoT</td>
      <td>ATCC 35801</td>
      <td>Erdman_0115</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>fadD10</td>
      <td>ATCC 35801</td>
      <td>Erdman_0116</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>rv0100</td>
      <td>ATCC 35801</td>
      <td>Erdman_0117</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>pdtaS</td>
      <td>ATCC 35801</td>
      <td>Erdman_3533</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (M. tuberculosis)</td>
      <td>pdtaR</td>
      <td>ATCC 35801</td>
      <td>Erdman_1787</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3206; rip1 KO</td>
      <td>Chromosomal deletion of Erdman_3146 nt5-1212 by double crossover recombination followed by marker excision by LoxP recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigD</td>
      <td>Schneider et al., 2014</td>
      <td>JSS0005; sigD KO</td>
      <td>Chromosomal deletion of Erdman_3735 nt6-622 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigK</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3259; sigK KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigL</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3254; sigL KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigM</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3260, sigM KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis) sigL sigM KO</td>
      <td>ΔsigLΔsigM</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3255; sigL sigM KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigKΔsigLΔsigM</td>
      <td>Schneider et al., 2014</td>
      <td>MGM3256; sigK sigL sigM KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic Reagent (M. tuberculosis)</td>
      <td>ΔsigKΔsigL</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3261; sigK sigL KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigKΔsigM</td>
      <td>Sklar et al., 2010</td>
      <td>MGM3283; sigK sigM KO</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigKΔsigD</td>
      <td>This study, available from corresponding author</td>
      <td>sigK::loxP sigD::hygR; MGM3288</td>
      <td>Chromosomal deletion of Erdman_3735 nt6-622 by double crossover recombination MGM3259 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigLΔsigD</td>
      <td>This study, available from corresponding author</td>
      <td>sigL::loxP sigD::hygR; MGM3289</td>
      <td>Chromosomal deletion of Erdman_3735 nt6-622 by double crossover recombination MGM3254 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔsigMΔsigD</td>
      <td>This study, available from corresponding author</td>
      <td>sigM::loxP sigD::hygR; MGM3290</td>
      <td>Chromosomal deletion of Erdman_3735 nt6-622 by double crossover recombination MGM3260 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔctpV</td>
      <td>This study, available from corresponding author</td>
      <td>ctpV::hygR</td>
      <td>Chromosomal deletion of nt 175-2136 of Erdman_1076 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔcsoR</td>
      <td>This study, available from corresponding author</td>
      <td>csoR::hygR</td>
      <td>Chromosomal deletion of nt 1-360 of Erdman_1074 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔmymT</td>
      <td>This study, available from corresponding author</td>
      <td>mymT::hygR</td>
      <td>Chromosomal deletion of nt 1-162 of mymT by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔctpV</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP ctpV::hygR</td>
      <td>Chromosomal deletion of nt 175-2136 of Erdman_1076 by double crossover recombination MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔcsoR</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP csoR::hygR</td>
      <td>Chromosomal deletion of nt 1-360 of Erdman_1074 by double crossover recombination MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔmymT</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP mymT::hygR</td>
      <td>Chromosomal deletion of nt 1-162 of mymT by double crossover recombination MGM 3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔpdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>pdtaS::hygR</td>
      <td>Chromosomal deletion of nt1-1506 of Erdman_3533 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔpdtaS + Vector</td>
      <td>This study, available from corresponding author</td>
      <td>pdtaS::hygR:pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔpdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>pdtaR::hygR</td>
      <td>Chromosomal deletion of nt 1-576 of Erdman_1787 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>ΔpdtaR + vector</td>
      <td>This study, available from corresponding author</td>
      <td>pdtaR::hygR:pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δnrp</td>
      <td>This study, available from corresponding author</td>
      <td>nrp::hygR</td>
      <td>Chromosomal deletion of nt 21-7515 of Edman_0118 by double crossover recombination</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δnrp + vector</td>
      <td>This study, available from corresponding author</td>
      <td>nrp::hygR: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δnrp + WT nrp</td>
      <td>This study, available from corresponding author</td>
      <td>nrp::hygR: WT nrp</td>
      <td>WT copy of nrp integrated at AttB, Erdman_0116 promoter</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS::hygR</td>
      <td>Chromosomal deletion of nt1-1506 of Erdman_3533 by double crossover recombination MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaS + vector</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS::hygR: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaR::hygR</td>
      <td>Chromosomal deletion of nt 1-576 of Erdman_1787 by double crossover recombination MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaR + vector</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaR::hygR: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaR + WT pdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaR::hygR: WT pdtaR HA</td>
      <td>WT copy of pdtaR integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1ΔpdtaR + D65A pdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaR::hygR: D65A pdtaR HA</td>
      <td>D65A variant of pdtaR integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1Δnrp</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP nrp::hygR</td>
      <td>Chromosomal deletion of nt 21-7515 of Edman_0118 by double crossover recombination MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>WT + vector</td>
      <td>Makinoshima and Glickman, 2005</td>
      <td>EG2: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>WT + vector</td>
      <td>Makinoshima and Glickman, 2005</td>
      <td>EG2:pMV261</td>
      <td>Transformed with empty pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 + vector</td>
      <td>Sklar et al., 2010</td>
      <td>Δrip1: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 + vector</td>
      <td>Sklar et al., 2010</td>
      <td>rip1::loxP: pMV261</td>
      <td>Transformed with empty pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 + WT Rip1</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>rip1::loxP: WT rip1</td>
      <td>Transformed with WT rip1 pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 + H21A Rip1</td>
      <td>Makinoshima and Glickman, 2005</td>
      <td>rip1::loxP: H21A rip1</td>
      <td>Transformed with H21A variant rip1 pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1: PPE1 ORF pHSP60</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP: PPE1 GFP ORF only</td>
      <td>Transformed with PPE1 GFP ORF only pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1: PPE1 ORF + 5' pHSP60</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP: PPE1 GFP ORF + 5' UTR pHSP60</td>
      <td>Transformed with PPE1 GFP + 5' UTR pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1: Rv0097-nrp pHSP60</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP: Rv0097-nrp</td>
      <td>Transformed with Rv0097-nrp pMV261K episomal plasmid</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X</td>
      <td>Isolated spontaneous Erdman_3533 variant in MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X + vector</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X + pdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X: WT pdtaS 10xHis</td>
      <td>WT pdtaS 10xHis integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X + pdtaS V54F</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X: V54F pdtaS 10xHis</td>
      <td>V54F variant of Erdman_3533 10xHis integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X + pdtaS H302Q/H303Q</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X: H302Q/H303Q pdtaS 10xHis</td>
      <td>H302Q/H303Q variant of Erdman_3533 10xHis integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS F37X + pdtaS G443A/G445A</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS F37X: G443A/G445A pdtaS 10xHis</td>
      <td>G443A/G445A variant of Erdman_3533 10xHis integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS V54F</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS V54F</td>
      <td>Isolated spontaneous Erdman_3533 variant in MGM3206 background</td>
    </tr>
    <tr>
      <td>Genetic reagent (M. tuberculosis)</td>
      <td>Δrip1 pdtaS V54F + vector</td>
      <td>This study, available from corresponding author</td>
      <td>rip1::loxP pdtaS V54F: pMV306K</td>
      <td>Empty pMV306K integrated at AttB</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET WT PdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET WT PdtaS</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET WT PdtaS kinase domain</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET WT PdtaS kinase domain</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET C53A PdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET C53A PdtaS</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET C57A PdtaS</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET C57A PdtaS</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET WT PdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET WT PdtaR</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Genetic reagent (E. coli)</td>
      <td>Rosetta 2 DE3: pET D65A PdtaR</td>
      <td>This study, available from corresponding author</td>
      <td>Rosetta 2 DE3: pET D65A PdtaR</td>
      <td>T7lac recombinant expression of C-terminally 10xHis tagged protein</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET SUMO (plasmid)</td>
      <td>Reverter and Lima, 2009</td>
      <td>pET SUMO</td>
      <td>T7lac promoter E. coli expression vector N-terminal 10xHIS Sumo Fusion Protein</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pET (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET</td>
      <td>T7lac promoter E. coli expression vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaS (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET WT PdtaS 10XHIS</td>
      <td>nt 1-1503 of Erdman_3533 fused N-terminal to Enterkinase cleavage site followed by 10xHis tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaS C53A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET C53A PdtaS 10XHIS</td>
      <td>nt 1-1503 of Erdman_3533 C53A variant fused N-terminal to Enterkinase cleavage site followed by 10xHis tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaS C57A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET C57A PdtaS 10XHIS</td>
      <td>nt 1-1503 of Erdman_3533 C57A variant fused N-terminal to Enterkinase cleavage site followed by 10xHis tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaS kinase domain (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET WT PdtaS kinase domain 10XHIS</td>
      <td>nt 678-1503 of Erdman_3533 variant fused N-terminal to Enterkinase cleavage site followed by 10xHis tag</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaR D65A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET Sumo WT PdtaR</td>
      <td>N-terminal 10xHIS Smt3 fused to nt 1-615 of Erdman_1787</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PdtaR D65A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pET Sumo D65A PdtaR</td>
      <td>N-terminal 10xHIS Smt3 fused to nt 1-615 of Erdman_1787 D65A variant</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vector (plasmid)</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>pMV261K</td>
      <td>Episomal M.tb plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Vector (plasmid)</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>pMV306K</td>
      <td>AttB integrating M.tb plasmid</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pMV261K GFP (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV261K GFP</td>
      <td>Episomal M.tb plasmid for C-terminal GFP fusion constructs</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>WT rip1 (plasmid)</td>
      <td>Makinoshima and Glickman, 2005</td>
      <td>pHMG121</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>H21A rip1 (plasmid)</td>
      <td>Makinoshima and Glickman, 2005</td>
      <td>pHMG141</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaS (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K WT PdtaS 10xHis</td>
      <td>nt 1-1503 of Erdman_3533 tagged at C-term with 10x His</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaS V54F (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K V54F PdtaS 10xHis</td>
      <td>nt 1-1503 of Erdman_3533 tagged at C-term with 10x His V54F variant</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaS H302Q/H303Q (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K H302Q/H303Q PdtaS 10xHis</td>
      <td>nt 1-1503 of Erdman_3533 tagged at C-term with 10x His H302Q/H303Q variant</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaS G443A/G445A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K G443A/H445A PdtaS 10xHIs</td>
      <td>nt 1-1503 of Erdman_3533 tagged at C-term with 10x His G443A/G445A variant</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaR (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K WT PdtaR HA</td>
      <td>nt 1-615 of Edman_1787 tagged at C-term with HA epitope</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pdtaR D65A (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306K D65A PdtaR HA</td>
      <td>nt 1-615 of Edman_1787 tagged at C-term with HA epitope D65A variant</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PPE1 ORF pHSP60 (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV261K ORF PPE1 GFP</td>
      <td>nt 1-1389 of Erdman_0113 tagged at C-term with GFP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PPE1 ORF + 5' pHSP60 (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV261K ORF PPE1 GFP + 5'PPE1</td>
      <td>nt -222-1389 of Erdman_0113 tagged at C-term with GFP</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Rv0097-nrp pHRP60 (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV261K Rv0097-nrp</td>
      <td>nt 1 of Erdman_0114 to nt 7539 of Erdman_0118</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>WT nrp (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>pMV306 WT nrp</td>
      <td>nt 1-96 of Erdman_0116 (predicted TSS Wadsworth) + nt 1-7539 of Erdman_0118</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360Hyg (plasmid)</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>pmsg360Hyg</td>
      <td>Phage packaging vector for hygR allelic exchange</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360Zeo (plasmid)</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>pmsg360Zeo</td>
      <td>Phage packaging vector for zeoR allelic exchange</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg318-2 (plasmid)</td>
      <td>Sklar et al., 2010 Makinoshima and Glickman, 2005</td>
      <td>pmsg318-2</td>
      <td>M.tb Cre recombinase expression vector</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360Hyg CtpV flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>ΔctpV targeting vector</td>
      <td>Hyg cassette flanked by 616 bp 5' CtpV nt 175 + 600 bp 3' CtpV nt 2136</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360 Hyg CsoR flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>ΔcsoR targeting vector</td>
      <td>Hyg cassette flanked by 600 bp 5' CsoR start codon + 600 bp 3' of CsoR stop codon</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360 Hyg MymT flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>ΔmymT targeting vector</td>
      <td>Hyg cassette flanked by 600 bp 5' MymT start codon + 600 bp 3' of MymT stop codon</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360 Hyg pdtaS flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>ΔpdtaS targeting vector</td>
      <td>Hyg cassette flanked by 600 bp 5' PdtaS start codon + 579 bp 3' PdtaS stop codon</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360 Hyg pdtaR flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>ΔpdtaR targeting vector</td>
      <td>Hyg cassette flanked by 600 bp 5' PdtaR start codon + 647 bp 3' PdtaR nt 576</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmsg360 Hyg nrp Flanks (plasmid)</td>
      <td>This study, available from corresponding author</td>
      <td>Δnrp targeting vector</td>
      <td>Hyg cassette flanked by 621 bp 5' nrp nt 21+ 621 bp 3' nrp nt 7515</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oSigA-1</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>cgtcttcatcccagacgaaat</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oSigA-2</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>cgacgaagaccacgaagac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oCtpV-1</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gtgtcccatgttcgaggtcaa</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oCtpV-2</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gtcaatgttcttcggtgcttac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oLpqS-1</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gcatcgagttgtccaccag</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oLpqS-2</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>tcaatgtggctcacccaaac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oMymT-1</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gggtgatacgaatgacgaacta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oMymT-2</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>acagtggcatgggacttc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>o2625c-F</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>tcttgatcgcgttgggattg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>o2625c-R</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>cccggcgaattgatgtagag</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oDesR-F</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>tctgatcctcacgtcctacac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oDesR-R</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>agcgcccacatctttgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oHspX-F</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gaattcgcgtacggttccttc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oHspX-R</td>
      <td>Integrated DNA Technologies</td>
      <td>qPCR primer</td>
      <td>gccaccgacacagtaagaatg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_C53A-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>gcgacgacggtgtcctggtggcggttgcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_C53A-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>cgcaaccgccaccaggacaccgtcgtcgc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_C57A-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>gcgcaagcccggccgaacaccgggccgacg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_C57A-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>cgtcggcccggtgttcggccgggcttgcgc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaR_D65A-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>gtgatcatggccgtgaaga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaR_D65A-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>tcttcacggccatgatcac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_H302Q/H303Q-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>gggaaatccagcagcgggtt</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_H302Q/H303Q-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>aacccgctgctggatttccc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_G443A/G445A-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>acgacgcgcttgctctgccg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>oPdtaS_G443A/G445A-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer</td>
      <td>cggcagagcaagcgcgtcgt</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Sense5'PPE1-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>taatacgactcactatagggggccgactaacaccgcgg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Sense5'PPE1-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>ggtttgctcaagccaggc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rv3864-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>taatacgactcactataggcaaaaaattcgtgcaccaacc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Rv3864-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>tttccttacgctcgccgt</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>AntiDNAK-F</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>gatccacctagttctagaatggctcgtgcggtcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>AntiDNAK-R</td>
      <td>Integrated DNA Technologies</td>
      <td>PCR primer; in vitro transcription</td>
      <td>taatacgactcactatagggggcgtcattgaagtaggcg</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti E. coli RNA polymerase B antibody (α-Rpoβ)</td>
      <td>BioLegend</td>
      <td>663903 (RRID:AB_2564414)</td>
      <td>1:10,000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-HA.11 epitope tag antibody (α-HA)</td>
      <td>BioLegend</td>
      <td>901513 (RRID:AB_2565335)</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-CarD (Rabbit)</td>
      <td>Pocono Rabbit Farm</td>
      <td>Stallings et al., 2009</td>
      <td>1:10,000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>α-MymT (Rabbit)</td>
      <td>Gold et al., 2008</td>
      <td></td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP(Rabbit) Antibody (α-GFP)</td>
      <td>Rockland</td>
      <td>600-401-215L (RRID:AB_2612813)</td>
      <td>1:1000 dilution</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Spermine NONOate</td>
      <td>Millipore Sigma</td>
      <td>567703</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Diethylenetriamine/nitric oxide adduct (DETA-NO)</td>
      <td>Millipore Sigma</td>
      <td>D185</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Hydrogen peroxide, 30%</td>
      <td>Fisher Scientific</td>
      <td>H325-100</td>
      <td></td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>Sodium hydrosulfide hydrate</td>
      <td>Fisher Scientific</td>
      <td>AC296200250</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>In-Fusion HD Cloning Kit</td>
      <td>Takara Bio USA</td>
      <td>639650</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Maxima H Minus cDNA Synthesis Master Mix, with dsDNase</td>
      <td>Thermo Fisher Scientific</td>
      <td>M1681</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>DyNAmo Flash SYBR Green qPCR Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>F415F</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>HiScribe T7 High Yield RNA Synthesis Kit</td>
      <td>New England Biolabs</td>
      <td>E2040S</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>Ribo-Zero Magnetic Bacterial Kit</td>
      <td>Epicentre</td>
      <td>MRZB12424</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>TruSeq Stranded Total RNA kit</td>
      <td>Illumina</td>
      <td>20020599</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>KAPA Hyper Prep Kit</td>
      <td>Roche</td>
      <td>7962312001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>TruSeq SBS Kit v3</td>
      <td>Illumina</td>
      <td>FC-401-3002</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>GeneJET RNA Purification Kit</td>
      <td>Fisher Scientific</td>
      <td>FERK0731</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>TURBO DNA-free kit</td>
      <td>Fisher Scientific</td>
      <td>AM1907</td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>Phusion High Fidelity Polymerase</td>
      <td>Fisher Scientific</td>
      <td>F530L</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>GeneJET Plasmid Miniprep Kit</td>
      <td>Fisher Scientific</td>
      <td>FERK0503</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>NanoTemper Technologies Inc PROTEIN LABELING KIT RED-NHS (MOL011)</td>
      <td>Fisher Scientific</td>
      <td>NC1491187</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay, kit</td>
      <td>NanoTemper Technologies Inc Standard capillaries</td>
      <td>Fisher Scientific</td>
      <td>NC1408770</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ViennaRNA Web Services</td>
      <td></td>
      <td>http://www.viennarna.at/forna/; RRID:SCR_008550</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>fastqc</td>
      <td>http://www.bioinformatics.babraham.ac.uk/projects/fastqc</td>
      <td>RRID:SCR_014583</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>bwa mem</td>
      <td>Li et al., 2009</td>
      <td>RRID:SCR_010910</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>samtools</td>
      <td>Li et al., 2009</td>
      <td>RRID:SCR_002105</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Bioconductor Rsubread package</td>
      <td>Liao et al., 2019</td>
      <td>RRID:SCR_016945</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2 R package</td>
      <td>Love et al., 2014</td>
      <td>RRID:SCR_015687</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R</td>
      <td>The R Project for Statistical Computing; https://www.R-project.org/</td>
      <td>RRID:SCR_001905</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GATK</td>
      <td>Broad Institute; https://gatk.broadinstitute.org/hc/en-us</td>
      <td>RRID:SCR_001876</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pheatmap</td>
      <td>https://www.rdocumentation.org/packages/pheatmap/versions/0.2/topics/pheatmap</td>
      <td>RRID:SCR_016418</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>NUPAGE 4-12% BT Gel</td>
      <td>Fisher Scientific</td>
      <td>NPO312BOX/NPO336BOX</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Protran Nitrocellulose Hybridization Transfer Membrane</td>
      <td>Perkin Elmer</td>
      <td>NBA08C001EA</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Immun-Blot PVDF Membrane</td>
      <td>Bio-Rad</td>
      <td>1620177</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>NanoTemper Technologies Premium Capillaries</td>
      <td>Fisher Scientific</td>
      <td>NC1408772</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>HisProbe-HRP Conjugate</td>
      <td>Thermo Fisher Scientific</td>
      <td>15165</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Reagents

Media and salts were purchased from Thermo Fisher, USA. Glycine, imidazole, and ATP from Merck Sigma-Aldrich, USA. Protein marker from Thermo Scientific, USA. Antibiotics, isopropyl β-D-1-thiogalactopyranoside (IPTG) and dithiothreitol (DTT) from GoldBio Inc, USA. Protease inhibitor cocktail from Amresco, USA. Ni2+-NTA resin from Qiagen, GmBH. γ32P-labeled ATP (>3000 Ci/mmol) from Perkin Elmer, USA.

### General growth conditions, strains, and DNA manipulations

M. tuberculosis (Erdman) and derivatives were grown and maintained in 7H9 media (broth) or on 7H10 (agar) supplemented with 10% Oleic Acid-Albumin-Dextrose-Catalase supplement (OADC), 05% glycerol, and 0.05% Tween-80(broth only) (7H9 OADC/7H10 OADC) at 37°C unless otherwise noted below. The wild-type strain used in this study is animal passaged, minimally passaged in vitro, and confirmed to be phthicerol dimycocerosates (PDIM) positive both by metabolic labeling and without mutations in PDIM biosynthesis by whole genome sequencing. Deletion mutations were generated by specialized transduction utilizing the temperature-sensitive phage phAE87. Mutant strains were confirmed by Southern blot or PCR using primers in the Hyg cassette and outside the cloned region, followed by sequencing of the amplified PCR product to confirm the location of chromosomal insertion. For a complete strain list with relevant features, see Supplementary file 1. Plasmids utilized in this study were generated using standard molecular techniques and are listed with their features in Supplementary file 2.

### Metal sensitivity assays

For agar-based assays, duplicate logarithmically growing (OD600 of 0.4–0.6) cultures were centrifuged and washed twice with room temperature phosphate buffered saline (PBS) containing 0.05% Tween-80 (PBS Tween). Resulting washed suspensions were all adjusted to OD600 of 0.2 and serial diluted in PBS Tween. Dilutions were then plated onto control unsupplemented 7H10 OADC agar media, as well as media supplemented with the indicated concentration of copper (II) sulfate or iron (III) chloride. Colony-forming units (CFUs) were enumerated after 28 days of growth at 37°C, 5% CO2. Relative survival was calculated by dividing the average number of CFU on treatment plates by the average number of CFU on control plates. Experiments were repeated a minimum of two biological replicates defined as individual samples treated independently throughout. Where applicable, technical replicate refers to repeated quantification of identical biological samples to account for error during dilutions for agar plate cultures.

Liquid growth curve assays were pre-grown and washed as above. Growth curves were started at an initial OD600 of 0.005 by adding 1 mL of washed culture, at an OD600 of 0.05, to 9 mL of 7H9 OADC supplemented with 100 μM zinc (II) sulfate. Biological replicates defined as individual samples treated independently throughout.

For copper liquid sensitivity CFU assays, 25 mL cultures were pre-grown to an OD600 of 0.8–1.0 in 7H9 OADC media. Cultures were washed twice in 7H9 supplemented with albumin dextrose saline, 05% glycerol, 02% Tween-80 (7H9 ADS), and normalized to an OD600 of 0.1 in four-replicate 10 mL cultures. After equilibration at 37°C for 2 hr, duplicate cultures were treated with 200 µM copper sulfate (Sigma-Aldrich), while control cultures were left untreated. On days 0 and 3 post treatment, aliquots of each culture were removed, washed, and serial diluted in PBS Tween. Dilutions were then plated on 7H10 OADC plates for CFU determination. CFUs were enumerated after 28 days of growth at 37°C, 5% CO2. Relative survival was calculated by dividing the average CFU day 3 by the average number of CFU on day 0. Biological replicates defined as individual samples treated independently throughout.

### Nitric oxide sensitivity assays

Duplicate 25 mL cultures were pre-grown to an OD600 between 0.8 and 1.0 in 7H9 OADC media. Cultures were washed twice in 7H9 ADS and normalized to an OD600 of 1.0 in 10 mL of 7H9 ADS. Four-replicate, 9 mL 7H9 ADS cultures were then inoculated with 1 mL of this suspension for a starting OD600 of 0.1 in 30 mL inkwell bottles (Fisher Scientific Cat# 03-313-89A) with ~2 in. of headspace. After equilibration at 37°C for 2 hr, duplicate cultures were treated with 100 μL of freshly prepared 20 mM DETA-NO, or 0.1 M sodium hydroxide (final concentration 1mM, vehicle for DETA-NO). Treatment was repeated every 24 hr for 3 days. Days 0 and 3 post treatment, aliquots of each culture were removed, washed, and serial diluted in PBS Tween. Dilutions were then plated on 7H10 OADC plates for CFU determination. CFUs were enumerated after 28 days of growth at 37°C, 5% CO2. Relative survival was calculated by dividing the average CFU day 3 by the average number of CFU on day 0. Experiments were repeated a minimum of two times. Biological replicates defined as individual samples treated independently throughout.

### PBS starvation

Cultures of the indicated strains were pre-grown in 7H9 OADC media to an OD of between 0.5 and 0.7. Cells were then collected by centrifugation and washed twice with PBS pH 7.0. Replicate flasks containing 30 mL of PBS were then inoculated to an OD of 0.1. Flasks were incubated standing in an incubator at 37°C with 5% CO2. At the indicated times, aliquots were removed, serially diluted in PBS, and plated onto 7H10 OADC agar plates. CFUs were enumerated after 28 days of incubation at 37°C. Biological replicates defined as individual samples treated independently throughout.

### Lysozyme, hydrogen peroxide, and SDS sensitivity

Cultures of the indicated strains were pre-grown in 7H9 OADC to an OD of between 0.5 and 0.7. Cells were then washed twice with 7H9 ADS media and diluted to an OD of 0.1 in the same media. 1 mL of washed culture was then inoculated into replicate 9 mL bottles of fresh 7H9 ADS media (untreated control) or 7H9 ADS media containing 2.5 mg/mL lysozyme, 10 mM hydrogen peroxide, or 0.05% (v/v) sodium dodecyl sulfate (SDS). Following 3 hr of treatment at 37°C, aliquots from each culture were removed, serial diluted in 7H9 ADS media, and then spread onto 7H910 OADC plates. CFUs were enumerated following 28 days of incubation at 37°C. Biological replicates defined as individual samples treated independently throughout.

### Survival at pH 4.5

Cultures of the indicated strains were pre-grown in 7H9 OADC to an OD of between 0.5 and 0.7. Cultures were then divided in half and washed with either 7H9 ADS-pH 7.0 or 7H9 ADS-pH 4.5. Replicate 10 mL bottles of pH 4.5 or pH 7.0 media were then inoculated with washed culture at on OD of 0.01. Aliquots of each culture were removed immediately after inoculation, and after 7 days of growth at 37°C, serial diluted, and then plated onto 7H10 OADC plates. CFUs were enumerated following 28 days of incubation at 37°C. Biological replicates defined as individual samples treated independently throughout.

### Copper-induced MymT expression

MymT expression was induced as follows: cultures grown in 7H9 OADC to an OD600 of ~0.5 were divided into 20 mL replicate aliquots. Copper sulfate (0–500 µM) was then added to individual replicates followed by 2 hr incubation at 37°C. Following incubation, cells were processed for immunoblot as described in Materials and methods, excepting that the PVDF membrane was used for blotting.

RNA extraction and RT-qPCR mRNA levels were quantified as follows. For copper-stimulated transcripts, triplicate 40 mL cultures grown to an OD600 of 0.4 in 7H9 OADC were divided into two sets of 3, 20 mL cultures. Half were left untreated for quantification of basal transcript level, while the other half were treated with 200 μM copper (II) sulfate for 2 hr.

For nitric oxide-stimulated transcripts, triplicate 40 mL culture grown to an OD600 of 0.4 in 7H9 ADS were divided into two sets of 3X20 mL cultures. Half were then treated with 200 μL of 20 mM DETA-NO dissolved in 0.1 M sodium hydroxide for 3 hr or with vehicle (0.1 M sodium hydroxide)-alone control. Cells were collected by centrifugation, washed once in PBS Tween, and then suspended in 1 mL of Trizol (Invitrogen). Cells were mechanically disrupted with zirconia bead via 3 × 30 s pulses in a BioSpec Mini24 beadbeater. Total RNA was then extracted according to the manufacturer’s instructions. Contaminating genomic DNA was removed using the Turbo DNA-free kit (Invitrogen), and RNA was then further purified utilizing RNeasy Mini spin columns (Qiagen). 1 μg of resulting total RNA was used to synthesize cDNA via random priming utilizing the Maxima H-Minus cDNA Synthesis kit (Thermo Fisher). Real-time qPCR was performed on a 7500 real-time PCR system (Applied Biosystems). Amplification product was detected by SYBR green using the Dynamo Flash qPCR kit (Thermo Fisher). For each gene of interest (GOI)-normalized cycle threshold, C(t) was determined relative to the housekeeping gene sigA. Relative expression level was calculated using the formula 2^-(C(t)GOI-C(t)sigA). Primer sets used to amplify individual GOI are listed in Supplementary file 3.

### Aerosol infection of mice

Mice used in this study were purchased from The Jackson Laboratory. 8–10-week-old C57Bl/6J (stock number 00064) were used. iNOS ko mice were purchased from Jackson, stock number 002609. All purchased mice were rested within our animal facility to normalize microbiota for 2 weeks. Care, housing, and experimentation on laboratory mice were performed in accordance with the National Institute of Heath guidelines and the approval of the Memorial Sloan-Kettering Institutional Animal Care and Use Committee (IACUC). Protocol approval number is 01-11-030.

Strains for infection were grown to an OD600 of 0.5–0.7 in 7H9 OADC. They were then washed twice with PBS Tween followed by brief sonication to disrupt aggregates. Final inoculums were prepared by suspending 8 × 107 CFU in 10 mL of sterile water. Appropriate mouse strains were then exposed to 4 × 107 CFU in a Glas-Col aerosol exposure unit. At the indicated time point post infection, 4–8 individual mice were humanely euthanized and both lungs and spleens were harvested for CFU determination. Organ homogenates were cultured on 7H10 OADC plates, and CFU was enumerated after 28 days of incubation at 37°C, 5% CO2.

### Suppressor screen and whole genome sequencing

Spontaneous copper suppressor mutants were identified by selecting ~3 × 105 CFU of Δrip1 bacteria on each 7H10 OADC agar dish supplemented with 500 μM copper sulfate. A total of approximately 5x107 bacteria were selected. Plates were then incubated at 37°C, 5% CO2 for 28 days. Individual genetic suppressor candidates were picked and expanded to an OD600 of 0.5 in 40 mL of 7H9 OADC without addition of copper followed by confirmation of Cu resistance. Whole genome sequencing was performed acoustically shearing genomic DNA, and HiSeq sequencing libraries were prepared using the KAPA Hyper Prep Kit (Roche). PCR amplification of the libraries was carried out for 10 cycles. 5−10 × 106 50 bp paired-end reads were obtained for each sample on an Illumina HiSeq 2500 using the TruSeq SBS Kit v3 (Illumina). Post-run demultiplexing and adapter removal were performed and fastq files were inspected using fastqc (Andrews S. (2010). FastQC: a quality control tool for high-throughput sequence data; available at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc). Trimmed fastq files were then aligned to the reference genome (M. tuberculosis str. Erdman; GenBank: AP012340.1) using bwa mem (Li and Durbin, 2009). Bam files were sorted and merged using Samtools (Li et al., 2009). Read groups were added and bam files de-duplicated using Picard tools, and GATK best practices were followed for SNP and indel detection (DePristo et al., 2011).

### Immunoblotting

Lysates for immunoblotting were prepared from 40 mL cultures grown in 7H9 OADC to an OD600 of between 0.5 and 0.8. Cells were cooled to 4°C on ice, centrifuged, and washed 1× with PBS. Washed pellets were then suspended in 0.4 mL of PBS, and ~100 μL of zirconia beads were added. Lysis was performed by 3, 45 s pulses in a BioSpec Mini24 beadbeater with 5 min intervening rest periods on ice. Beads were then removed by centrifugation at 1000×g for 5 min, and the resulting supernatant was mixed 1:1 with 2× Laemmli sample buffer supplemented with .1 M DTT. 20 μL of each sample, heated for 10 min at 100°C, was then separated on 4–12% NuPAGE bis-tris poly acrylamide gels. Separated proteins were then transferred to nitrocellulose and probed with the appropriate antibodies. Antibodies used in this study are monoclonal anti-HA.11 (BioLegend), monoclonal anti-E. coli RNA-polymerase β (BioLegend), rabbit polyclonal anti-GFP (Rockland), rabbit polyclonal anti-CarD, and rabbit polyclonal anti-MymT (a kind gift of Dr. Carl Nathan, Gold et al., 2008). His tag fusion proteins were detected using HisProbe-HRP (Thermo Fisher).

### Transcriptional profiling

RNA samples for comparative nitric oxide transcriptional profiling were isolated from cells grown and treated as described above, except that nitric oxide treatment was carried out for 5 hr instead of 3 hr. RNA sequencing was performed as previously reported (Hubin et al., 2017). Full RNAseq dataset is given in Supplementary file 4 and deposited under NCBI BioProject Accession Number PRJNA719428 (https://www.ncbi.nlm.nih.gov/sra/PRJNA719428).

### Recombinant PdtaS/PdtaR purification

Full-length C-terminal 10x His tagged PdtaS and N-terminal 10xHisSmt3 PdtaR fusions were both expressed and purified from Rosetta 2 (DE3) E. coli (Millipore Sigma). Cultures, 2–4 L, grown in Luria–Bertani (LB) media to an OD600 of 1.0 at 37°C were equilibrated to 30°C for 30 min prior to induction. Protein expression was then induced with 1 mM IPTG, and the cultures were allowed to grow for 3–4 additional hours at 30°C. Cells were then collected by centrifugation, resuspended in lysis/wash buffer (350 mM sodium chloride, 20 mM Tris-HCl pH 8.0, 20 mM imidazole, 1 mM β-mercaptoethanol) at a ratio of 2 mL of buffer to 1 g of wet pellet weight, and stored at −80°C. The following day frozen cell pellets were thawed and disrupted by two passes through a French pressure cell at an internal pressure of 14,000 psi (Sim-Aminco, 40,000 psi cell). Crude lysates were clarified by centrifugation at 20,000×g for 30 min in an SS-34 Rotor (Sorvall), and then passed over TALON metal affinity resin (Takara) equilibrated in wash buffer. Columns were then washed with 20 column volumes of Wash buffer. Bound proteins were eluted with two-column volumes of Elution Buffer (Wash Buffer + 250 mM imidazole).

After elution from the TALON column, PdtaS 10XHis was dialyzed and concentrated to ~2 mg/mL in a dialysis buffer containing 50 mM Tris-HCl pH 8.0, 50 mM sodium chloride, 100 µM DTT with 40% (v/v) glycerol. Eluted 10xHis-Smt3-PdtaR was cleaved from PdtaR by overnight treatment with Ulp1 protease at 4°C. Free PdtaR was then recovered in the flow-through fraction of a second round of TALON resin purification. PdtaR was then dialyzed and stored in the dialysis buffer.

### Histidine kinase autophosphorylation and phosphotransfer activity

For autophosphorylation assay, 5 μM of the purified histidine kinase PdtaS (HK) was incubated for 20 min in autophosphorylation buffer (50 mM Tris-HCl at pH 8.0, 50 mM KCl, 10 mM MgCl2) containing 50 μM ATP and 1 μCi of γ32P-labeled ATP at 30°C. In the phosphotransfer assay, 10 μM of RR PdtaR was added to the autophosphorylated HK and incubated for time points described in the figure legends. The reaction was terminated by adding 1× SDS-PAGE sample buffer (2% w/v SDS, 50 mM Tris.HCl, pH 6.8, 0.02% w/v bromophenol blue, 1% v/v β-mercaptoethanol, 10% v/v glycerol). The samples were resolved on 15% v/v SDS-PAGE. After electrophoresis, the gel was washed and exposed to phosphor screen (Fujifilm Bas cassette2, Japan) for 4 hr followed by imaging with Typhoon 9210 phosphorimager (GE Healthcare, USA). Quantitative densitometric analysis was performed with ImageJ.

### PdtaS autophosphorylation inhibition assays

5 μM of the purified HK PdtaS, PdtaSC53A mutant and PdtaSkinase domain (amino acids 277–501) proteins were preincubated for 10 min in the autophosphorylation buffer with copper chloride and zinc sulfate at various concentrations mentioned in the figure legends and with 1 mM of calcium chloride as a negative control. Similarly, the effect of NO and H2S was studied by preincubating 5 μM of PdtaS, PdtaSC53APdtaSC57A, or PdtaSkinase domain protein with spermine NONOate (Cayman Chemical Company, USA) for 40 min and sodium hydrosulfide hydrate (Acros Organics, Belgium) as spontaneous H2S donor for 30 min at various concentrations specified in the figure legends. The negative control (C) for use of spermine NONOate as NO donor was 1 mM of spermine NONOate allowed to exhaust NO release by overnight incubation at room temperature in Tris.Cl buffer at pH = 6.8. The autophosphorylation reaction was then initiated by adding 50 μM ATP along with 1 μCi of γ32P-labeled ATP at 30°C for 20 min. The reaction was terminated by adding 1× SDS-PAGE sample buffer. The samples were resolved on 15% v/v SDS-PAGE and analyzed as above. The dose-response curves were plotted and inhibition constant (Ki) was obtained by fitting the percentage inhibition to concentration plot using one site-specific binding fit using GraphPad Prism software.

### MST determination of binding affinity

Purified HK PdtaS protein (5 μM) was autophosphorylated in autophosphorylation buffer for 20 min at 30°C using 50 μM of ATP to generate phosphorylated HK PdtaS (PdtaS~P). Phosphotransfer reaction was carried out at 30°C for 10 min from HK PdtaS~P to fluorescently labeled RR PdtaR protein (50 nM) prelabeled using amine coupling Monolith Protein Labeling kit RED-NHS 2nd generation (Cat# MO-L011, NanoTemper Technologies GmbH) as prescribed in the manufacturer’s protocol. Binding assays were performed immediately with in vitro transcribed RNAs ppe1-5′, rv3864, and dnaK at concentrations from 0.31 nM to 10 µM diluted with autophosphorylation buffer having 0.025% Tween-20. The sample was then loaded into standard treated capillaries and analyzed using a Monolith NT. 115 (NanoTemper Technologies GmbH). The red laser was used for a duration of 35 s for excitation (MST power = 40%, LED power 100%). The data were analyzed using MO Control software (NanoTemper Technologies GmbH) to determine the apparent KD values represented as fraction bound.

For assays using unphosphorylated PdtaR, 50 nM of the fluorescently labeled PdtaR protein was incubated with 50 μM of ATP for 20 min at 30°C in an autophosphorylation buffer. MST assay was immediately performed post addition with ppe1-5′ (concentration range from 0.15 nM to 10 µM), rv3864 (concentration range from 0.61 nM to 10 µM), and dnaK (concentration range from 0.15 nM to 10 µM) diluted with autophosphorylation buffer having 0.025% Tween-20, and apparent KD values represented as fraction bound were similarly obtained.
