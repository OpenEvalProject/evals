# Activation of polycystin-1 signaling by binding of stalk-derived peptide agonists

## Authors

- Shristi Pawnikar<sup>1</sup>
- Brenda S Magenheimer<sup>2</sup>
- Keya Joshi<sup>4</sup> ([ORCID: 0009-0001-8139-478X](https://orcid.org/0009-0001-8139-478X))
- Ericka Nevarez-Munoz<sup>2</sup>
- Allan Haldane<sup>5</sup> ([ORCID: 0000-0002-8343-1994](https://orcid.org/0000-0002-8343-1994))
- Robin L Maser<sup>2</sup> †
- Yinglong Miao<sup>4</sup> ([ORCID: 0000-0003-3714-1395](https://orcid.org/0000-0003-3714-1395)) †

### Affiliations

1. Center for Computational Biology and Department of Molecular Biosciences, University of Kansas Lawrence United States ([ROR:001tmjg57](https://ror.org/001tmjg57))
2. Clinical Laboratory Sciences, University of Kansas Medical Center Kansas City United States ([ROR:036c9yv20](https://ror.org/036c9yv20))
3. The Jared Grantham Kidney Institute, University of Kansas Medical Center Kansas City United States ([ROR:036c9yv20](https://ror.org/036c9yv20))
4. Department of Pharmacology and Computational Medicine Program, University of North Carolina Chapel Hill United States ([ROR:0130frc33](https://ror.org/0130frc33))
5. Department of Physics, and Center for Biophysics and Computational Biology, Temple University Philadelphia United States ([ROR:00kx1jb78](https://ror.org/00kx1jb78))
6. Department of Biochemistry and Molecular Biology, University of Kansas Medical Center Kansas City United States ([ROR:036c9yv20](https://ror.org/036c9yv20))

† Corresponding author

## Abstract

Polycystin-1 (PC1) is the protein product of the PKD1 gene whose mutation causes autosomal dominant Polycystic Kidney Disease (ADPKD). PC1 is an atypical G protein-coupled receptor (GPCR) with an autocatalytic GAIN domain that cleaves PC1 into extracellular N-terminal and membrane-embedded C-terminal (CTF) fragments. Recently, activation of PC1 CTF signaling was shown to be regulated by a stalk tethered agonist (TA), resembling the mechanism observed for adhesion GPCRs. Here, synthetic peptides of the first 9- (p9), 17- (p17), and 21-residues (p21) of the PC1 stalk TA were shown to re-activate signaling by a stalkless CTF mutant in human cell culture assays. Novel Peptide Gaussian accelerated molecular dynamics (Pep-GaMD) simulations elucidated binding conformations of p9, p17, and p21 and revealed multiple specific binding regions to the stalkless CTF. Peptide agonists binding to the TOP domain of PC1 induced close TOP-putative pore loop interactions, a characteristic feature of stalk TA-mediated PC1 CTF activation. Additional sequence coevolution analyses showed the peptide binding regions were consistent with covarying residue pairs identified between the TOP domain and the stalk TA. These insights into the structural dynamic mechanism of PC1 activation by TA peptide agonists provide an in-depth understanding that will facilitate the development of therapeutics targeting PC1 for ADPKD treatment.

## Introduction

PC1 is the protein product of the PKD1 gene that is mutated in the majority of cases (~85%) of ADPKD (Harris and Torres, 2014). ADPKD is a potentially lethal disease, affecting >0.6 million individuals in the US. It causes renal cyst formation that could consequently lead to kidney failure. Currently, the only approved treatment for ADPKD is Jynarque, a small-molecule antagonist of the arginine vasopressin receptor 2, V2R, whose signaling, and production of cAMP has been shown to be increased in PKD. This drug targets one of the aberrant pathways downstream from the PKD gene mutation but is inadequate due to its limitations in only slowing disease progression and causing adverse side effects (Ingelfinger, 2017). ADPKD severity is dependent on the functional level of PC1, and as such, therapies designed to increase the level of PC1 protein, and its functionality are currently being pursued (Hopp et al., 2012; Cai et al., 2014; Hofherr et al., 2016; Krappitz et al., 2016; Lakhia et al., 2022). Approximately one-third of PKD1 mutations are non-truncating and could encode partially functional PC1 protein (Hopp et al., 2012; Tan et al., 2011; Rossetti et al., 2009; Heyer et al., 2016). As such, therapeutic treatments that directly target and activate PC1 may represent a promising approach for the treatment of ADPKD. However, this approach remains difficult due to incomplete knowledge of the proximal-most functions of PC1.

PC1 shares characteristics with the Adhesion class of GPCRs (ADGRs), including a conserved GPCR autoproteolysis inducing (GAIN) domain that directs autocatalytic cleavage at an embedded GPCR proteolysis site (GPS) motif (Araç et al., 2012). Intramolecular cleavage at the GPS motif generates two non-covalently attached fragments - the extracellular N-terminal fragment (NTF) and the membrane-embedded C-terminal fragment (CTF) (Qian et al., 2002; Kurbegovic et al., 2014). Similar to ADGRs, the PC1 NTF consists of multiple adhesive domains that promote interactions between cells and with the extracellular matrix (Kim et al., 2016; Weston et al., 2001; Sandford et al., 1997; Ibraghimov-Beskrovnaya et al., 2000; Weston et al., 2003), while the PC1 CTF is composed of 11 transmembrane (TM) helices and a short C-terminal tail (C-tail) (Nims et al., 2003) that has been shown to interact with G proteins for signaling activation or regulation (Maser and Calvet, 2020; Maser et al., 2022) and has thus led to description of PC1 as an atypical GPCR. Previous studies demonstrated the critical importance of cleavage at the PC1 GPS site to prevent renal cystogenesis in mouse models (Cai et al., 2014; Yu et al., 2007). For the ADGRs, a TA model has been proposed for activation of G protein signaling. After dissociation of the NTF, the N-terminal stalk of the ADGR CTF interacts with its membrane-embedded TM domains to induce conformational rearrangements that mediate activation of G protein signaling (Liebscher et al., 2014; Schöneberg et al., 2015; Demberg et al., 2015; Stoveken et al., 2015). Exogenous synthetic peptides consisting of various lengths of the N-terminal sequence of the stalk have been shown to function as soluble agonists in the activation of signaling by full-length and CTF mutants for numerous ADGRs (Maser and Calvet, 2020; Xiao et al., 2022).

In previous studies of the PC1 CTF, we revealed a stalk TA-dependent molecular mechanism underlying CTF-mediated activation of an NFAT promoter luciferase reporter through complementary in vitro cell signaling experiments and all-atom Gaussian accelerated Molecular Dynamics (GaMD) simulations (Pawnikar et al., 2022). GaMD is an unconstrained enhanced sampling method that works by adding a harmonic boost potential to reduce large biomolecular energy barriers (Miao et al., 2014) and has been used successfully to capture multiple complex biological processes (Miao et al., 2015; Miao and McCammon, 2016; Pang et al., 2017; Miao and McCammon, 2017; Wang and Chan, 2017; Liao and Wang, 2019; Miao et al., 2018; Chuang et al., 2018; Sibener et al., 2018; Park et al., 2018; Miao and McCammon, 2018; Ricci et al., 2019; Palermo et al., 2017; Bhattarai et al., 2020; Pawnikar and Miao, 2020) including GPCR activation (Miao and McCammon, 2016). Expression constructs encoding a stalkless PC1 CTF (a nonbiological mutant with deletion of the first 21 N-terminal residues of CTF) and three ADPKD-associated missense mutants within the stalk region (G3052R, R3063C, and R3063P) were shown to be defective in reporter activation as compared to wild-type PC1 CTF. GaMD simulations revealed a novel allosteric transduction pathway for activation of PC1 CTF signaling that involves initiation by the Stalk interacting with a large extracellular loop between TM segments S1/TM6 and S2/TM7, called the TOP domain, followed by close interactions between the TOP and a putative pore loop (PL) domain between the final 2 TM domains. GaMD simulations of the wild-type PC1 CTF also identified a ‘Closed/Active’ low-energy state related to the large number of Stalk-TOP contacts and the R3848-E4078 ionic interaction between the TOP and PL domains that was not present in the stalkless CTF (Pawnikar et al., 2022).

Here, we have utilized in vitro cell signaling assays to identify peptide agonists targeting PC1 in combination with in silico studies to investigate their binding mechanisms for activation of PC1 signaling. Synthetic peptides of 7–21 residues in length derived from the N-terminus of the PC1 CTF stalk sequence were tested for their ability to re-activate signaling of the stalkless CTF expression construct. Peptide docking and simulations with the recently developed Peptide GaMD (Pep-GaMD), which is able to characterize peptide-protein binding processes more efficiently (Wang and Miao, 2020), were combined for selected peptide agonists p9, p17, and p21 to gain insight into their binding mechanism to the stalkless PC1 CTF. Pep-GaMD was able to successfully refine the docking conformations of the peptides bound to the extracellular TOP domain of PC1. In further Pep-GaMD simulations, the key salt bridge interaction between R3848 and E4078 from the TOP domain and PL, respectively, was observed upon binding of the peptides to stalkless PC1 CTF. Using Potts covariation analysis, in which a protein fitness model is inferred based on observed mutational covariation patterns in multiple sequence alignments (MSAs) of homologous proteins (Levy et al., 2017), we identified residues in the PC1 stalk with direct mutational covariation with residues in the TOP domain, which were strikingly consistent with the binding interfaces identified in docking and simulation studies. Overall, these analyses yielded mechanistic insights underlying the stalk peptide agonist-mediated signal re-activation of stalkless PC1 CTF. Such insights provide significant contributions toward the future design and development of peptide modulators targeting PC1 for an effective ADPKD therapeutic treatment.

## Results

### Synthetic, stalk-derived peptides re-activate NFAT reporter by CTF∆st in trans

Our previous study utilized expression constructs of human PC1 CTF. However, in order to prepare for eventual in vivo experiments in mouse models, we generated expression constructs of mouse (m) PC1 consisting of the signal peptide sequence of the T cell surface glycoprotein CD5 (MPMGSLQPLATLYLLGMLVASVLG) fused in frame with the stalk sequence of wild-type mCTF beginning with residue T3041, or with a ‘stalkless’ CTF lacking the first 21 residues of the stalk (mCTF∆st) beginning with residue S3062 (Figure 1A). The CD5 signal peptide coding sequence was added to the wild-type mCTF and stalkless mCTF∆st expression constructs in order to ensure their translation at the endoplasmic reticulum for plasma membrane localization.

![Figure 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig1-v1.jpg)

**Figure 1.:** (A) Alignment of CTF stalk sequences from human (h) and mouse (m) PC1. CTF∆st has a 21-residue deletion from the N-terminal end of the stalk region. Arrow, GPCR proteolysis site (GPS) cleavage site. Non-identical residues are shown in bolded blue. (B) Activation of the NFAT-luc reporter by transfected mCTF or mCTF∆st expression constructs shown relative to empty expression vector (ev) as means (+ standard deviation, SD) of three wells/construct from each of seven independent experiments. (C) Representative Western blot of total cell lysates from one of the experiments in (B), probed with antisera A19 against mouse PC1 C-tail. ns, non-specific. (D) Summary of the total expression levels (means + SD) of CTF∆st relative to CTF from the experiments in (B). (E) Stalk peptide treatment of expression vector (ev)- or mCTF∆st-transfected cells. Sequences of stalk-derived peptides p7-p21 are shown. Graph represents the fold NFAT-luc activation for both ev- (gray bars) and CTF∆st- (blue bars) transfected cells relative to the CTF∆st control after 24 hr treatment with or without peptide. Results are the means (+ SD) of three separate experiments, each with three wells/conditions. *p<0.05; ***p=0.0001; ****p<0.0001. Analysis by one-way ANOVA with Tukey-Kramer post-test.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Representative Western blot of a surface biotinylation experiment with mCTF and mCTF∆stk. (A) ‘- biotin’ control was included using CTF-transfected cells for which the NHS-biotin reagent was omitted from the procedure. Aliquots of the total cell lysate (input; after biotinylation and before neutravidin pulldown), supernatant (sup; following neutravidin bead removal), and biotinylated cell surface proteins bound to neutravidin beads (beads) representing 10%, 10%, and 70% of each sample, respectively, were analyzed. Blots were probed with A19 and then stripped and reprobed for NaKATPase or the resident ER protein, TRAM2. (B) Summary of cell surface expression levels of CTF∆stk relative to CTF (means + SD) from two separate experiments.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Sequences of the p17 stalk peptide derived from human polycystin-1 (PC1) and the solubility tag peptide (sol tag). Residues differing from the mouse PC1 stalk sequence are shown in blue. (B–D) HEK293T cells were transfected with an empty expression vector (ev) or the CTF∆st expression construct from either mouse (B) or mouse PC1, and transfected cells were treated either without (negative control; culture medium only) or with human p17 peptide (positive control) or sol tag peptide. Graphs show the NFAT-luc activity for ev- (gray bars) and CTF∆st- (blue bars) transfected cells after 24 hr treatment with or without peptide for each experiment. Results are the means (+ SD) of reporter activity from three wells/conditions in each experiment. *p<0.05, **p<0.01, ***p<0.001; ****p<0.0001; ns = not significant. Analysis by one-way ANOVA with Tukey-Kramer post-test. In each of the experimental replicates, treatment with the sol tag peptide led to a nominal ~2 fold increase in reporter activity with CTF∆st- versus ev-transfected cells (2.24-, 1.60-, and 2.02-fold for B-D, respectively). Although the level of NFAT reporter activity stimulated by the positive control p17 in CTF∆st-transfected cells varied between the three experiments, the effect of the sol tag peptide on CTF∆st- (and ev-) transfected cells was consistent and differed significantly in comparison to CTF∆st-transfected cells with p17 treatment in all three experiments (regardless of PC1 origin). Furthermore, the NFAT-luc activity of CTF∆st+ sol tag-treated cells did not differ from ev + p17-treated cells for each experiment, suggesting that the ‘background’ reporter activation observed with ev + stalk peptide versus ev + no peptide control may be due to the solubility tag. Altogether, these results support the rescue of CTF∆st signaling by certain stalk-derived peptides is specific to the stalk sequence itself.

Transient transfection of HEK293T cells with either empty expression vector (ev), CTF or CTF∆st showed that the CTF∆st mutant exhibited a dramatic loss of NFAT reporter activation that was essentially reduced to ev control levels (Figure 1B). Both total (Figure 1C–D) and cell surface (Figure 1—figure supplement 1A–B) expression levels of CTF∆st were comparable to CTF, which suggests that neither protein stability nor membrane trafficking was responsible for the inability of CTF∆st to activate the NFAT reporter. These results are consistent with those obtained using expression constructs of human PC1 that demonstrated the stalk region of PC1 CTF acts as a tethered peptide agonist (Pawnikar et al., 2022).

To further investigate the agonistic property of the CTF stalk, we synthesized peptides (p) consisting of the N-terminal 7, 9, 11, 13, 15, 17, 19, or 21 residues from the stalk sequence of mPC1. All peptides were appended with a C-terminal, 7-residue hydrophilic sequence (GGKKKKK) to increase solubility. HEK293T cells were transiently transfected with empty expression vector or mCTF∆st plasmids along with the NFAT luciferase reporter and then treated with stalk peptides p7 through p21 or with the addition of culture medium only (‘no peptide’ control). The NFAT reporter was significantly activated in CTF∆st-transfected cells by treatment with p7, p9 or p17 as compared to their corresponding ev + peptide treatment controls. These stalk peptides also significantly increased reporter activity in comparison to the CTF∆st with no peptide treatment control (Figure 1E). Treatment of CTF∆st-transfected cells with p19 or p21 also significantly increased reporter activation in comparison to the CTF∆st + no peptide control; however, reporter activation occurred in both ev- and CTF∆st-transfected cells treated with either p19 or p21, suggesting that p19- and p21-mediated activation was not dependent on exogenous expression of mouse CTF∆st and could be activating the endogenous human PC1 protein. Treatment of ev- and CTF∆st-transfected cells with a peptide consisting of the hydrophilic sequence alone (i.e., solubility peptide) showed that the solubility tag was not responsible for the rescue of CTF∆st-mediated reporter activation by stalk peptides such as p17 (Figure 1—figure supplement 2). Altogether, these results were consistent with soluble stalk-derived peptides acting as PC1 CTF agonists in trans, and provided additional support for the PC1 CTF stalk region harboring TA activity (Pawnikar et al., 2022). We hypothesized that the soluble, activating peptides bind to the TOP domain of PC1 in a manner mimicking the tethered stalk in order to reactivate the signaling of the stalkless CTF∆st mutant. From among the active stalk-derived peptides, we selected p9, p17, and p21 that exhibited the highest agonist activity in CTF∆st reporter activation (Figure 1E) for in silico simulation studies.

### Docking and Pep-GaMD simulations of peptide agonist binding to stalkless PC1 CTF

We chose to use the stalkless CTF (∆Stalk CTF) as representing the least complex system in which the binding of exogenous peptides could be studied. ∆Stalk CTF is not a biological form or a mutant protein of PC1 observed in ADPKD. However, in our previous study, it mimicked the ADPKD-associated stalk mutants by being defective in cell signaling assays and rarely formed the R3848-E4078 salt bridge that was frequently seen in GaMD simulations with wild-type CTF (Pawnikar et al., 2022). Therefore ∆Stalk CTF served as the negative control for the following studies.

The cryo-EM structure of the human PC1-PC2 complex (PDB: 6A70) (Su et al., 2018) was used to build the computational model for ΔStalk PC1 CTF after deleting the first 21 residues (3049–3069) from the CTF (Pawnikar et al., 2022). We successfully docked the p9, p17, and p21 stalk peptides to the ∆Stalk CTF model with HPEPDOCK (Zhou et al., 2018) (See Materials and Methods). The peptides are all bound to the TOP domain and the interface between the TOP domain and extracellular loop 1 (ECL1) of CTF (Figure 2—figure supplement 1A–B). In particular, peptide p21 occupied a closely similar binding region as the stalk in wild-type CTF as observed in the previous study (Pawnikar et al., 2022). We then performed five independent 500 ns Pep-GaMD simulations on each of the three stalk peptide agonists p9, p17 and p21 bound to ΔStalk CTF to refine their HPEPDOCK docking conformations (See Materials and Methods).

With the Pep-GaMD simulation frames, we performed structural clustering of each peptide using the hierarchical agglomerative algorithm in CPPTRAJ (Roe and Cheatham, 2013). The top-ranked conformations of each peptide bound to ΔStalk CTF were compared to their initial docking conformations. Next, we calculated 2D free energy profiles of the peptides-bound ΔStalk CTF by reweighting the Pep-GaMD simulations. The R3848-E4078 residue distance and the number of contacts between the peptides (p9, p17, and p21) and the TOP domain were selected as the reaction coordinates. The number of contacts was calculated between any atom pairs within 4 Å distance of the peptide and extracellular domains of the PC1 protein. In the subsequent analyses, stalk and peptide residues are numbered relative to the N terminus of the stalk as starting from 1, while residues of the ∆stalk CTF are numbered according to the human PC1 protein sequence.

### Active conformation of peptide p9-bound PC1 CTF

From the free energy profile of the p9-bound ΔStalk CTF, we identified ‘Unbound’ and ‘Bound’ low-energy states (Figure 2A). In the docking conformation, peptide p9 bound to the interface between the TOP and ECL1 of ΔStalk CTF (Figure 2—figure supplement 1A–B). In Pep-GaMD simulations, the p9 peptide dissociated from the TOP-ECL1 binding pocket and rebound to the TOP domain in a slightly different region (Figure 2B–C). The p9 peptide sequence is mostly composed of hydrophobic residues. Polar interactions between the main chain atoms of peptide-protein residues were observed in the top-ranked representative conformation of the p9-bound ΔStalk CTF. Protein residues R3892 and H3864 formed hydrogen bonds with p9 residues A2 and A5, respectively (Figure 2D). These interactions were also highlighted in the protein contact map between peptide p9 and the extracellular domains of CTF in the representative ‘Bound’ state (Figure 2—figure supplement 2). The distance between the TOP domain residue R3848 and PL residue E4078 was 3.9 Å (Figure 2E), suggesting that the top-ranked representative conformation of the p9-bound ΔStalk CTF was in the ‘Closed/Active’ low-energy state. In addition, the 2D free energy profile of each individual simulation was calculated and the ‘Bound’ low-energy state was consistently identified in the 2D free energy profiles of peptide p9 (Figure 2—figure supplement 3).

![Figure 2.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig2-v1.jpg)

**Figure 2.:** (A) Free energy profile of the p9-bound ΔStalk CTF regarding the number of atom contacts between p9 and extracellular domains of CTF and the distance between the CZ atom of R3848 and the CD atom of R4078 in CTF. (B–C) Comparison of HPEPDOCK docking (cyan) and Pep-GaMD refined (magenta) conformations of peptide p9 in ΔStalk CTF. (D) Polar interactions between peptide-protein residues were observed in the top-ranked representative conformations of p9. Peptide residues are numbered relative to the N terminus of the stalk with the peptide starting from 1, while residues within ∆Stalk CTF are numbered according to the standard polycystin-1 (PC1) residue number. (E) Distance between the TOP domain residue R3848 and pore loop (PL) residue E4078 observed in p9-bound ΔStalk CTF.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A–B) Docking conformations of p9, p17, and p21 to ΔStalk CTF. (C) Pep-GaMD simulation system of ΔStalk polycystin-1 (PC1) C-terminal fragment (CTF) (blue cartoon) embedded in a palmitoyl-oleoyl-phosphatidyl-choline (POPC) lipid bilayer (orange sticks) solvated in 0.15 M NaCl solution.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Contacts were defined by a distance less than 4 Å between any atom in each residue pair. The secondary structure annotation is colored as in Figure 5, and the sequence is annotated with amino acids in ‘Taylor’ color scheme. For p9, an additional cluster of contacts with residues in helix S3 are not shown.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Important low-energy conformational states are identified, including the ‘Unbound’ and ‘Bound’.

### Active and intermediate conformational states of peptide p17-bound PC1 CTF

The free energy profile of the p17-bound ΔStalk system allowed us to identify three low-energy states - ‘Unbound,’ ‘Intermediate,’ and ‘Bound’ (Figure 3A). In the docking conformation, peptide p17 bound to the interface between the TOP and ECL1 of ΔStalk CTF (Figure 2—figure supplement 1A–B). In the Pep-GaMD refined ‘Bound’ state, a folded antiparallel ß-strand conformation was observed for the peptide p17 at the interface of ECL1 and the TOP domain (Figure 3B–C). Peptide residues T1, F3, A5, F8, F16, and V17 formed hydrophobic interactions with the protein residues H3311, R3314 and Y3307 from ECL1, and E3708, S3711, Q3707, A3704, R3700, and L3701 from the TOP domain (Figure 3D). These interactions were also highlighted in the protein contact map between peptide p17 and the extracellular domains of CTF in the representative ‘Bound’ state (Figure 2—figure supplement 2). The distance between the TOP domain residue R3848 and PL residue E4078 was 4.1 Å (Figure 3E), suggesting that the top-ranked representative conformation of the p17 bound ΔStalk CTF was in the ‘Closed/Active’ low-energy state.

![Figure 3.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig3-v1.jpg)

**Figure 3.:** (A) Free energy profile of the p17-bound ΔStalk CTF regarding the number of atom contacts between p17 and extracellular domains of CTF and the distance between the CZ atom of R3848 and the CD atom of R4078 in CTF. (B–C) Comparison of HPEPDOCK docking (cyan) and Pep-GaMD refined (magenta) conformations of peptide p17 in ΔStalk CTF. Hydrophobic interactions (red dashed lines) between peptide-protein residues were observed in the (D) 'Bound’ and (F) 'Intermediate’ low-energy conformations of p17-bound ΔStalk CTF. Distance between the TOP domain residue R3848 and pore loop (PL) residue E4078 observed in the (E) ‘Bound’ and (G) ‘Intermediate’ low-energy conformations of p17-bound ΔStalk CTF.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Important low-energy conformational states are identified, including the ‘Unbound’ ‘Intermediate,’ and ‘Bound’.

In the ‘Intermediate’ state, p17 with a short helical turn was also observed to bind the TOP domain of ΔStalk CTF (Figure 3B–C). Hydrophobic residue interactions were also formed between the peptide and protein. In particular, peptide residues T1, F3, P10, P11, H13, R15, F16, and V17 formed hydrophobic interactions with the protein residues P3859, A3704, S3741, Q3739, Y3734, P3733, H3729, W3726, R3712, and R3856 from the TOP domain (Figure 3F). The distance between the TOP domain residue R3848 and PL residue E4078 was 14.6 Å (Figure 3G), suggesting that this representative conformation (ranked the second among the Pep-GaMD structural clusters) of the p17-bound ΔStalk CTF was in the ‘Intermediate’ low-energy state. In addition, the 2D free energy profile of each individual simulation was calculated. Pep-GaMD simulations were able to refine the peptide conformation from the ‘Unbound’ to ‘Intermediate,’ and ‘Bound’ states in Sim1 and Sim5, while the peptide reached only the ‘Intermediate’ state in the other three simulations (Figure 3—figure supplement 1). The free energy values of 2D PMF minima shown in Figure 3A could differ from those in the 1D PMF minima of peptide structural clusters, especially with the usage of distinct reaction coordinates.

### Active conformational state of peptide p21-bound PC1 CTF

Finally, the free energy profile of the p21-bound ΔStalk CTF allowed us to identify only a broad low-energy well corresponding to the ‘Bound’ state (Figure 4A). The docking conformation of p21-bound ΔStalk CTF was refined through Pep-GaMD simulations, where folding of the peptide was observed on the protein surface of the TOP domain (Figure 4B–C). The p21 peptide occupied a similar binding region as the stalk in wild-type CTF as observed in the previous study (Pawnikar et al., 2022). Hydrophobic contacts were observed between peptide residues L7, F8, P10, S12, H13, V14, V17, P19, E20, and P21 and protein residues L3863, L3701, I3705, L3709, E3708, R3712, F3714, H3729, W3726, V3730, L3732, P3733, N3738, R3856, and S3741 (Figure 4D). These interactions were also highlighted in the protein contact map between peptide p21 and the extracellular domains of CTF in the representative ‘Bound’ state (Figure 2—figure supplement 2). The distance calculated from the top-ranked structural cluster of the system between the TOP domain residue R3848 and PL residue E4078 was 3.8 Å, corresponding to the ‘Closed/Active’ low-energy state (Figure 4E). Furthermore, time courses of the radius of gyration (Rg) and root-mean-square deviation (RMSD) of p21 relative to the starting HPEPDOCK conformation showed large conformational changes of the peptide during Pep-GaMD simulations (Figure 4—figure supplement 1A–C). In addition, the 2D free energy profile of each individual simulation showed that Pep-GaMD was able to refine the peptide docking conformation to the ‘Bound’ state in all the five simulations (Figure 4—figure supplement 2).

![Figure 4.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig4-v1.jpg)

**Figure 4.:** (A) Free energy profile of the p21-bound ΔStalk CTF regarding the number of atom contacts between p21 and extracellular domains of CTF and the distance between the CZ atom of R3848 and the CD atom of R4078 in CTF. (B–C) Comparison of HPEPDOCK docking (cyan) and Pep-GaMD refined (magenta) conformations of peptide p21 in ΔStalk CTF. (D) Polar interactions between peptide-protein residues were observed in the top-ranked representative conformations of p21. (E) Distance between the TOP domain residue R3848 and pore loop (PL) residue E4078 observed in p21-bound ΔStalk CTF.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Time courses of the p21 system regarding the TOP-pore loop (PL) interaction distance between the CZ atom in R3848 and the CD atom in E4078. (B) Time courses of the root-mean-square deviation (RMSD) of p21 relative to the starting HPEPDOCK conformation of the peptide. (C) Time courses of the radius of gyration (Rg) of p21.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Important low-energy conformational state is identified, including the ‘Bound’.

### Peptide binding regions correlated with covarying residue pairs identified between the TOP domain and stalk TA

To provide an independent basis of evidence supporting the observation of ‘Bound’ and ‘Intermediate’ states of agonist peptide binding, we constructed a multiple sequence alignment (MSA) with an effective count of 1022 evolutionarily diverged PC1 homologs (illustrated in Figure 5—figure supplement 1) from which we inferred a Potts statistical model (Figure 5). Columns of the MSA with ‘direct’ statistical interactions, as detected using the Potts inference method, reflect compensatory mutation pairs maintained through evolution supporting a conserved function. We limited our MSA to 394 residues on the extracellular side of PC1 because of the computational challenge of fitting the entire PC1 sequence (Figure 5B and Figure 5—figure supplement 1).

![Figure 5.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig5-v1.jpg)

**Figure 5.:** (A) Potts interaction map based on the Polycystic Kidney Disease 1 (PKD1) multiple-sequence-alignment illustrated in Figure 5—figure supplement 2, showing interactions with the stalk. Gray dots are shown for residue position-pairs with Potts covariation scores above a threshold, colored darker for higher scores, and selected interacting pairs are annotated with the stalk residue (horizontal, numbered from the stalk N-terminus) and other residue (vertical, standard PC1 numbering) with the PC1 residue at each position. The secondary structure as a function of position is annotated along the axes. (B) Cartoon showing the subset of PC1 included in the Potts covariation analysis colored as in the secondary structure in panel A, using a structure predicted by AlphaFold. Gray regions were excluded from the Potts model. (C) Residue Covariation scores for selected position-pairs. The scores reflect the percentage excess frequency of the residue-pair relative to the null expected frequency if the multiple sequence alignment (MSA) columns were uncorrelated, with blue values reflecting excess and red dearth. Only the most common residue types are shown.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** The full alignment includes 4383 sequences, and only six diverse homologs are shown for illustration. The polycystin-1 (PC1) sequence is shown including inserts relative to the alignment (lower case with a gray background, matched with ‘.’ in homologs), inserts are not shown for the six homologs. Gaps characters are indicated as ‘-,’ representing positions included in the alignment which were missing in that sequence. The human PC1 protein sequence residue numbering is indicated at the bottom ends of each aligned region.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/95992/elife-95992-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) Interactions predicted using the Potts model, shaded by interaction strength. Secondary structure elements predicted using an Alphafold structure is annotated along the axes. (B) Contacts observed in the rat latrophilin-1 GAIN domain crystal structure (PDB: 4DLQ Araç et al., 2012), showing contacts where the nearest side-chain heavy atom distance was under 8 Å. (C) Contacts observed in the structure of the Polycystic Kidney Disease 1 (PKD1) GAIN domain were predicted using Alphafold with the same distance criteria. The contacts predicted using the Potts model show correspondence with the structure-based contacts, detecting two antiparallel beta-sheet interactions extending from the diagonal (upper right and middle), plus a possible third antiparallel beta-sheet interface (lower left) not observed in the latrophilin structure as this region may have low similarity.

Figure 5A shows the pairs of positions with strong Potts interaction scores where one position is either in the stalk, the nearby GAIN domain, or the TM1 helix. Some predicted interaction pairs recapitulated beta-sheet contacts within the GAIN domain observed in the homolog rat latrophilin-1 (Araç et al., 2012) as well as predicted by Alphafold (Jumper et al., 2021, Figure 5—figure supplement 2) or between the extracellular ends of the TM2/3 and TM4/5 alpha helices known from cryo-EM structures (Su et al., 2018) or predicted by Alphafold, validating that our model detected biologically functional interactions.

We identified strong interactions between the stalk and other residues from the Potts model. They were not observed in the cryo-EM structure, in which the flexible stalk is missing. For interactions with the TOP domain, out of the 4875 possible pairs (25 stalk residues by 195 TOP domain residues in our Potts model), this analysis detected a stringent set of 6 strongly interacting pairs. Remarkably, multiple positions in this small set were among those relevant to the ‘Intermediate’ binding conformation of p17 and ‘Bound’ conformation of p21 as identified from the Pep-GaMD simulations. These were W3726 and S3741 in the TOP domain, both interacting with T1 of the stalk, and P3859 interacting with N25 at the end of the stalk (Figure 5A). Additionally, we identified E3743 to be strongly interacting with F16 in the stalk, and it was also near the observed binding region in the TOP domain for the peptide p17 in the ‘Intermediate’ state near S3741 (Figure 3F). The remaining two strong interactions between the stalk and the TOP domain involved Q3821 with T1 and L3893 with G4. L3893 is adjacent to R3892 that was identified to interact with the peptide p9 in the ‘Bound’ state (Figure 2D) and mutating it may affect its neighbor’s positioning. Besides the interactions between the TOP domain and the stalk TA, we also found a set of interactions between the stalk and the extracellular ends of TM2-TM3 helices and TM4-TM5 helices, in which stalk residues G4, P10, F16, and E20 interact with W3298, A3296, and S3579, respectively, as well as a strong interaction between V3077, three residues past the end of the stalk, and T3856 in the TOP domain. TOP domain residue T3856 was also identified as relevant to the binding region of peptide p17 in the ‘Intermediate’ state (Figure 3F) and peptide p21 in the ‘Bound’ state (Figure 4D). These interactions could additionally play a role in stalk-TA activation or could be related to other functionality such as cleavage in the GPS motif.

To gain further insight and to validate that these detected ‘direct’ interactions reflect biologically meaningful functional interactions and are not artifacts of the data, we examined the residue-specific covariation observed in the MSA (Figure 5C), which measures the difference between the observed pairwise residue frequency and its null expectation under the assumption of independent variation. Values greater than ~1% are commonly found to be indications of a statistically reliable mutational covariation (see Materials and Methods), and many of the covarying pairs discovered involving the stalk were significantly above this value. We validated that the covarying residue pairings were consistent with biophysical interaction. For example, for the position-pair 20–3579, here annotated such that the first index is the stalk residue numbered relative to the N terminus of the stalk and the second index is the TOP domain residue numbered according to the human PC1 protein sequence, there were excess residue-pair counts in the MSA consistent with opposite-charge or polar pairing such as K20-E3579, N20-Q3579, and others, and a dearth of repulsive like-charge pairs such as E20-E3579. Similarly, position-pair 1–3741 favored certain combinations of polar residues such as T1-S3741. Other position-pairs appeared consistent with hydrophobic packing interactions, such as F16-A3296, G4-W3298, and T1-W3726. A large residue F or W at position 3298 in the extracellular end of TM2 was commonly paired with a G at stalk position 4, while a smaller I or L residue at position 3298 was more commonly paired with a T at stalk position 4.

Molecular Mechanics/Poisson-Boltzmann Surface Area (MM/PBSA) (Rastelli et al., 2010) analysis was further performed to calculate the binding free energies of peptides p9, p17, and p21 to PC1 CTF and decompose the residue-wise energy contributions using the gmx_MMPBSA software (Valdés-Tresanco et al., 2021). The relative rank of the overall peptide binding free energies (Table 1) was consistent with the experimental signaling data, i.e., p21 > p9 > p17, for which p21 showed the largest free energy value of binding (–40.29±6.94 kcal/mol). Furthermore, we performed residue-wise energy decomposition analysis with MM/PBSA using gmx_MMPBSA software (Valdés-Tresanco et al., 2021), which allowed us to identify key residues that contributed the most to the peptide binding energies. These included residues T1 and V9 in p9 (Table 2), residues T1, R15 and V17 in p17 (Table 3), and residues P10, P11, P19, and P21 in p21 and residue W3726 in the PC1 CTF (Table 4). The energetic contributions of these residues apparently correlated to the sequence coevolution predicted from the Potts model.

**Table 1.**
 Summary of MM/PBSA binding free energy analysis for the peptides p9, p17 and p21 and polycystin-1 (PC1) C-terminal fragment (CTF) in the bound state sampled during Peptide GaMD (Pep-GaMD) simulations.


<table>
  <thead>
    <tr>
      <th>System</th>
      <th>ΔG (kcal/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>p21</td>
      <td>–40.29±6.94</td>
    </tr>
    <tr>
      <td>p9</td>
      <td>–17.30±4.50</td>
    </tr>
    <tr>
      <td>p17</td>
      <td>–12.74±5.62</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Summary of residue-wise energy decomposition analysis between the peptide p9 and polycystin-1 (PC1) C-terminal fragment (CTF) in the bound state sampled during Peptide GaMD (Pep-GaMD) simulations.


<table>
  <thead>
    <tr>
      <th>Residue</th>
      <th>ΔG (kcal/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T1</td>
      <td>–10.47±6.92</td>
    </tr>
    <tr>
      <td>A2</td>
      <td>–3.28±2.18</td>
    </tr>
    <tr>
      <td>F3</td>
      <td>–2.62±2.62</td>
    </tr>
    <tr>
      <td>G4</td>
      <td>–0.30±2.38</td>
    </tr>
    <tr>
      <td>A5</td>
      <td>–1.61±2.67</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>–0.59±4.49</td>
    </tr>
    <tr>
      <td>L7</td>
      <td>–0.28±2.96</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>–1.51±1.84</td>
    </tr>
    <tr>
      <td>V9</td>
      <td>–10.14±5.68</td>
    </tr>
    <tr>
      <td>R3891</td>
      <td>–0.14±7.26</td>
    </tr>
    <tr>
      <td>R3892</td>
      <td>–0.31±7.85</td>
    </tr>
    <tr>
      <td>F3888</td>
      <td>–3.24±2.95</td>
    </tr>
    <tr>
      <td>H3864</td>
      <td>–0.03±3.86</td>
    </tr>
    <tr>
      <td>R3970</td>
      <td>–0.94±2.62</td>
    </tr>
    <tr>
      <td>R3968</td>
      <td>–0.27±1.67</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Summary of residue-wise energy decomposition analysis between the peptide p17 and polycystin-1 (PC1) C-terminal fragment (CTF) in the bound state sampled during Peptide GaMD (Pep-GaMD) simulations.


<table>
  <thead>
    <tr>
      <th>Residue</th>
      <th>ΔG (kcal/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T1</td>
      <td>–10.98±2.32</td>
    </tr>
    <tr>
      <td>A2</td>
      <td>–0.36±2.34</td>
    </tr>
    <tr>
      <td>F3</td>
      <td>–0.23±3.82</td>
    </tr>
    <tr>
      <td>G4</td>
      <td>–0.03±3.83</td>
    </tr>
    <tr>
      <td>A5</td>
      <td>–0.86±3.08</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>–0.48±4.06</td>
    </tr>
    <tr>
      <td>L7</td>
      <td>–0.05±2.90</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>–0.21±4.42</td>
    </tr>
    <tr>
      <td>V9</td>
      <td>–0.19±3.41</td>
    </tr>
    <tr>
      <td>P10</td>
      <td>–0.72±2.64</td>
    </tr>
    <tr>
      <td>P11</td>
      <td>–0.09±3.23</td>
    </tr>
    <tr>
      <td>S12</td>
      <td>–0.29±4.92</td>
    </tr>
    <tr>
      <td>H13</td>
      <td>–1.19±7.37</td>
    </tr>
    <tr>
      <td>V14</td>
      <td>–1.25±3.08</td>
    </tr>
    <tr>
      <td>R15</td>
      <td>–10.63±3.76</td>
    </tr>
    <tr>
      <td>F16</td>
      <td>–0.93±5.52</td>
    </tr>
    <tr>
      <td>V17</td>
      <td>–10.20±3.83</td>
    </tr>
    <tr>
      <td>Y3307</td>
      <td>–0.11±2.68</td>
    </tr>
    <tr>
      <td>H3311</td>
      <td>–0.04±3.25</td>
    </tr>
    <tr>
      <td>R3314</td>
      <td>–8.90±1.65</td>
    </tr>
    <tr>
      <td>R3700</td>
      <td>–14.63±7.8</td>
    </tr>
    <tr>
      <td>Q3707</td>
      <td>–0.27±4.96</td>
    </tr>
    <tr>
      <td>S3711</td>
      <td>–0.08±4.06</td>
    </tr>
    <tr>
      <td>E3708</td>
      <td>–10.14±4.15</td>
    </tr>
  </tbody>
</table>

**Table 4.**
 Summary of residue-wise energy decomposition analysis between the peptide p21 and polycystin-1 (PC1) C-terminal fragment (CTF) in the bound state sampled during Peptide GaMD (Pep-GaMD) simulations.


<table>
  <thead>
    <tr>
      <th>Residue</th>
      <th>ΔG (kcal/mol)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T1</td>
      <td>–0.25±1.66</td>
    </tr>
    <tr>
      <td>A2</td>
      <td>–1.02±2.90</td>
    </tr>
    <tr>
      <td>F3</td>
      <td>–0.08±0.10</td>
    </tr>
    <tr>
      <td>G4</td>
      <td>–2.42±2.65</td>
    </tr>
    <tr>
      <td>A5</td>
      <td>–0.11±2.15</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>–0.09±1.31</td>
    </tr>
    <tr>
      <td>L7</td>
      <td>–0.83±1.43</td>
    </tr>
    <tr>
      <td>F8</td>
      <td>–0.68±1.10</td>
    </tr>
    <tr>
      <td>V9</td>
      <td>–8.17±2.10</td>
    </tr>
    <tr>
      <td>P10</td>
      <td>–6.16±1.79</td>
    </tr>
    <tr>
      <td>P11</td>
      <td>–1.22±2.83</td>
    </tr>
    <tr>
      <td>S12</td>
      <td>–0.05±2.56</td>
    </tr>
    <tr>
      <td>H13</td>
      <td>–1.13±3.74</td>
    </tr>
    <tr>
      <td>V14</td>
      <td>–1.16±1.78</td>
    </tr>
    <tr>
      <td>R15</td>
      <td>–0.59±1.02</td>
    </tr>
    <tr>
      <td>F16</td>
      <td>–0.59±1.02</td>
    </tr>
    <tr>
      <td>V17</td>
      <td>–1.59±1.13</td>
    </tr>
    <tr>
      <td>F18</td>
      <td>–0.20±1.37</td>
    </tr>
    <tr>
      <td>P19</td>
      <td>–7.09±1.51</td>
    </tr>
    <tr>
      <td>E20</td>
      <td>–3.76±2.24</td>
    </tr>
    <tr>
      <td>P21</td>
      <td>–8.43±2.01</td>
    </tr>
    <tr>
      <td>L3863</td>
      <td>–0.33±2.28</td>
    </tr>
    <tr>
      <td>L3701</td>
      <td>–0.04±2.39</td>
    </tr>
    <tr>
      <td>I3705</td>
      <td>–0.51±2.16</td>
    </tr>
    <tr>
      <td>E3708</td>
      <td>–1.68±3.11</td>
    </tr>
    <tr>
      <td>R3712</td>
      <td>–3.85±1.56</td>
    </tr>
    <tr>
      <td>F3714</td>
      <td>–0.01±2.28</td>
    </tr>
    <tr>
      <td>W3726</td>
      <td>–2.93±2.11</td>
    </tr>
    <tr>
      <td>H3729</td>
      <td>–0.56±2.00</td>
    </tr>
    <tr>
      <td>L3732</td>
      <td>–0.26±2.49</td>
    </tr>
    <tr>
      <td>P3733</td>
      <td>–0.61±2.33</td>
    </tr>
    <tr>
      <td>N3738</td>
      <td>–0.07±4.91</td>
    </tr>
    <tr>
      <td>S3741</td>
      <td>–0.03±4.27</td>
    </tr>
  </tbody>
</table>

## Discussion

In in vitro, cell-based signaling assays, PC1 CTF-mediated activation of the NFAT reporter is dependent on its N-terminal, extracellular stalk, as shown by the loss of reporter activity with the CTF stalk-deletion expression construct, CTF∆st (Pawnikar et al., 2022, Figure 1B) and by the ability of synthetic, stalk sequence-derived peptides to reactivate signaling by CTF∆st in trans (Figure 1E). A series of synthetic peptides derived from the N-terminal sequence of the mouse PC1 CTF stalk were used to determine their agonistic activity in PC1 CTF∆st-transfected cells. Notably, treatment with stalk peptides p7, p9, p17, p19, and p21 resulted in significant NFAT reporter activity over CTF∆st control (no peptide treatment), wherein the effects of p7, p9, and p17 were specific to mouse CTF∆st-expressing cells. These data are consistent with the stalk peptides acting as soluble TA peptide agonists for PC1 and provide further evidence for the activation of PC1 signaling via an ADGR-like TA mechanism.

In ADPKD, numerous missense mutations reported within the GAIN domain that have been shown to prevent or inhibit cleavage at the GPS (Araç et al., 2012). Loss of PC1 GPS cleavage, which is known to cause ADPKD, would likely sequester the stalk tethered agonist within the interior of the GAIN domain, which would presumably interfere with interactions between stalk tethered agonist residues and the remainder of the CTF and thus loss of the stalk-mediated signaling mechanism. Furthermore, there are 10 single nucleotide polymorphisms reported within the stalk sequence (ADPKD Variant Database; https://pkdb.mayo.edu/welcome), most of which were found to significantly reduce CTF-mediated activation of the NFAT reporter (Magenheimer et al., 2021). In particular, the ADPKD-associated G3052R stalk mutation that was previously analyzed along with the stalkless CTF by GaMD simulations (Pawnikar et al., 2022) has the same reduction in activity as the stalkless CTF in the cellular signaling reporter assays and the same loss of active/closed conformation interactions in GaMD analyses. Therefore, the stalkless CTF was used in our docking and simulation studies as representative of a biologically relevant mutant form of PC1.

To reveal the molecular mechanisms of the soluble stalk-derived peptides, we chose to perform HPEPDOCK docking and novel Pep-GaMD simulations to sample the peptide interactions with the ΔStalk PC1 CTF. Pep-GaMD simulations were able to refine the docking conformations of peptide agonists bound to the ∆Stalk PC1 CTF. It is important to note that the free energy profiles calculated from GaMD simulations of PC1 CTF were not fully converged since certain variations were observed among the individual simulations. Nevertheless, these calculations allowed us to identify representative low-energy binding conformations of the peptides. Pep-GaMD simulations sampled an antiparallel ß-strand and a short helical secondary structure of peptide p17 bound to the ΔStalk CTF. Furthermore, peptides p9 and p21 adopted a more folded structure as compared to their disordered loop conformations in the docking poses. We also observed TOP-PL interactions, particularly the salt bridge between residues R3848-E4078 that is a key feature of the stalk TA-mediated activation of signaling for PC1 CTF (Pawnikar et al., 2022). Signal transduction was initiated upon binding of the stalk (TA) to the TOP domain, which was transmitted to the PL via a salt bridge formation between residue R3848 in the TOP domain and residue E4078 in the PL. The bound peptide agonists p9, p17, and p21 maintained the ΔStalk CTF in its ‘Closed/Active’ conformation as observed in the wild-type PC1 CTF simulations (Pawnikar et al., 2022).

The interacting pairs identified using sequence-based covariation analysis matched the pairs identified by Pep-GaMD simulations, providing complementary evidence of the importance of these interactions and of the existence of the ‘Bound’ and ‘Intermediate’ binding states of the stalk TA and stalk-derived peptide agonist. This suggests that such stalk TA binding states are evolutionarily conserved across PC1 orthologs. Covariation analysis identifies interactions important during any part of the protein lifecycle, and alone cannot be used to distinguish which conformational state an interaction arises in. By comparison to the conformations found in the Pep-GaMD simulations, we found that most of the identified interactions between the stalk TA and the TOP domain were consistent with either the ‘Intermediate’ or ‘Bound’ binding states of the stalk-derived peptides, which are related to CTF inactive and active signaling states, however, it remained possible that other interactions, such as between the start of the stalk-TA and TM2/TM3, may be related to conformational states necessary for cleavage of the GAIN/GPS domain. Additionally, structural contacts may be incompletely detected at some positions when the statistical signal of covariation is masked by high conservation, subfamily specialization, or misalignment. This can explain why some interactions identified in the binding interface through docking are not detected using covariation analysis. Despite this, the specific subset of interactions detected using covariation analysis suggest broader peptide binding interfaces, and we found these to be consistent with the peptide binding interactions observed in the Pep-GaMD simulations and the MM/PBSA binding free energy analysis, and the covarying residue pairings were consistent with functional biophysical interactions.

The proposed binding interactions of the PC1 stalk peptides share some similarities with those observed for the ADGRs. Specifically, Xiao et al., 2022 resolved cryo-EM structures of active ADGRG2 and ADGRG4 in complex with tethered Stachel sequences. The structures showed that the 15 residue Stachel sequence inserts into the TM bundle to form intense hydrophobic interactions. A hydrophobic F/Y/LXφφφXφ motif identified in the ADGR tethered sequences formed five finger-like projections in the hydrophobic pits of the TM bundle (Xiao et al., 2022). In our study, we observed a similar pattern of intense hydrophobic interactions between the peptide agonists p9, p17, and p21 and the hydrophobic pockets in the TOP domain of PC1 CTF. Notably, a closely similar TOP binding pocket was identified for interaction of the tethered agonist (Stalk) in our previous study (Pawnikar et al., 2022) and for binding of peptide agonist p21 in this study. The TOP domain hydrophobic pocket may serve as a significant candidate binding site for designing new synthetic peptides or small molecules to aid in the rescue of PC1 function levels. Moreover, the shorter peptide agonists’ (p9 and p17) binding sites also serve as novel pockets for the design and development of therapeutic approaches for treating ADPKD. While the present study is focused on the identification of initial peptides that are able to activate the PC1 CTF, we shall include further mutation experiments and simulations, peptide SAR, and optimization of the lead peptides in future studies. It is also important to note that we have not tested the selectivity of the peptides for PC1 versus PC2 in the present study primarily because transfection of PC2 does not activate the NFAT reporter. However, it is possible that co-transfection of PC2 with the PC1 CTF could alter the stalk peptide binding. This will be important to consider in future studies.

## Materials and methods

### Experimental procedures

#### Antibodies and peptide synthesis

Primary antibodies used included A19, for detection of mouse PC1 CTF (Sutters et al., 2001), and TRAM2 (Epitomics, 3685–1). Secondary antibodies conjugated to HRP were purchased from Sigma or Jackson ImmunoResearch. Stalk-derived peptides were synthesized by GenScript using the Fmoc method and verified by HPLC-MS analysis.

#### DNA expression constructs and cloning

To produce CTF expression construct of mouse (m) PC1, sequences starting at T3041 and proceeding past the first TM domain were amplified by PCR from PC1-11TM (Puri et al., 2004), respectively, using 5’-mCleavStalkBsm-For and 3’-TMI-EcoRV primers to produce mCleavStk, which was joined via the BsmBI site to a PCR product encoding the signal peptide sequence (MPMGSLQPLATLYLLGMLVASVLG) from the T cell surface glycoprotein CD5 (Nims et al., 2003) in pBlueScript (pBS) to generate pBS-mCD5-cleaved stalk. The EcoRI-EagI fragment containing mCD5-cleaved stalk was joined to a 3.2 kb EagI-NotI fragment from PC1-11TM encoding TM2 through the C-tail to produce the final pCIneo-mCTF expression construct. The stalkless CTF mutant expression construct, pCIneo-mCTF∆st, starting with S3062 of the mouse PC1 stalk was generated by the same scheme except for using the 5’-m∆StalkBsmFor primer for the initial PCR. PCR and mutagenesis primers were synthesized by IDT and sequences are as follows:

5’-CD5 Eco: 5’- TTCTAGAATTCCCTCGACCTCG –3’; 3’-CD5-BsmBI: 5’- GACTAGCGTCTCATGCCTAGCACGGAAGC –3’; mCleavStalkBsm-For: 5’- GACTAGCGTCTCAGGCACTGCCTTCGGTGCC-3’; m∆StalkBsmFor: 5'- GACTAGCGTCTCAGGCAGTGCAAGCATCAACTACATTGTCC –3'; TMI-EcoRV: 5’-GACTAGGATATCCCTCTGGACTCTAGTAAAGCG-3’; BsrGIstalk-Rev: 5’- AGGGTCTGGGTAGAGTGCTT –3’.

PCR and mutagenesis products and their final constructs were confirmed by Sanger sequencing (GeneWiz). Expression constructs of CTF and CTF∆st from human PC1 were made in the pCI vector as described previously (Pawnikar et al., 2022). In the conduct of research utilizing recombinant DNA, the investigator adhered to NIH Guidelines for research involving recombinant DNA molecules.

#### Cell culture and transient transfection

HEK293T cells (ATCC) were maintained and transiently transfected as described previously (Maser et al., 2003). Cells were passaged into 6-well plates (6×105 cells/well; 3 wells/transfection condition) and transfected with a DNA mixture containing either the 4xNFAT or the 7xAP-1 promoter-Firefly luciferase reporter (100 ng; Stratagene), along with Renilla luciferase (50 ng of pGL4.70[hRluc] or 1 ng of pRL-null; Promega), and pCI expression vector encoding either CTF or CTF∆st (75 ng for signaling; 600 ng for surface biotinylation) or an equimolar amount of empty pCI vector as control. pBlueScript (Stratagene) was used to bring the total DNA amount to 8 ug. After 2.5 hr, the DNA mixture was replaced with serum-free culture medium, and after 20–24 hr, cells were lysed in 1 X Passive Lysis buffer (PLB; Promega) supplemented with protease and phosphatase inhibitors. Firefly (Fluc)- and Renilla (Rluc)-luciferase activity in each cell lysate was determined using the Dual Luciferase Assay Kit (Promega) and a Berthold tube luminometer. NFAT-Fluc luminescence was normalized to Rluc for each well within a transfection condition, and then averaged for each condition (n=3 wells/condition). Means of normalized NFAT-Fluc with standard deviation (Dalagiorgou et al., 2013) were graphed. Signaling-transfection experiments were performed a minimum of three times (i.e., >3 biological replicates) each with three technical replicates/condition except where noted.

#### Stalk peptide treatment

Cells were plated into 24-well plates (1.5×105 cells/well) and transfected with CTF∆st or empty pCI expression vectors, along with NFAT-Fluc and Rluc plasmids. Two hours following medium exchange, one-half of the culture medium volume was replaced with an equal volume of either serum-free medium (no peptide control), or stalk-derived or solubility tag peptide (2 mM in serum-free medium) and incubated overnight. In some experiments, an additional 50–100 ul of peptide (1 mM) was added the following morning. Cells were lysed at 24 hr following the initial peptide or control medium addition.

#### Cell surface biotinylation analyses

Surface labeling (Pavel et al., 2014) was performed on intact cells 22–24 hr post-transfection using 1.5 mg/ml PBS of the membrane-impermeable, cleavable biotin cross-linking reagent (Sulfo-NHS-SS-Biotin; Pierce) for 30 min on ice. Crosslinking was inactivated by the addition of 50 mM Tris, pH 8.0. Cells were washed and then lysed in 1 X PLB with protease inhibitors. A 10% aliquot of the total cell lysate was removed and saved as the input sample. NeutraAvidin-agarose beads (Pierce) were added to remove biotinylated surface proteins. The supernatant was removed and saved as the unbound cytosolic fraction (sup). A representative amount of each fraction, i.e., the total lysate (input), cytosolic (sup), and biotinylated surface proteins (beads) was analyzed by SDS-PAGE/Western blot. TRAM2 (ER-resident protein) was used as a cell fractionation marker.

#### Western blot analyses

Gel loading volumes of signaling cell lysates were calculated based on normalization to relative Rluc activity within a condition. Lysate samples were electrophoresed through 7.5% denaturing polyacrylamide gels and transferred to nitrocellulose membrane using the TransBlot Turbo and ReadyBlot transfer buffer (BioRad). Blots were incubated with primary antibody (1:1000 dilution for A19; 1:10,000 for anti-TRAM2) in Tris-buffered saline (TBS; 10 mM Tris pH 7.4, 150 mM NaCl) with 0.1% Tween-20 (TBST) and 5% powdered dry milk for 14–16 hr at 4 °C. Secondary antibodies conjugated to HRP were incubated at 1:5,000 dilution in TBST/5% milk for 1 hr at room temperature. Blots were developed using a chemiluminescent substrate (Clarity; BioRad), and multiple exposures were captured for each blot with the Amersham Imager 600 with the band saturation detection mode enabled. Volume density (minus background) of immunoreactive bands was determined using ImageQuant TL (GE Healthcare). In most cases, duplicate blots were prepared and quantified to obtain an average band density relative to wild-type CTF.

#### Statistical analyses

Statistical analysis was performed using GraphPad Prism 9 (GraphPad Software, San Diego, CA, USA). Data are presented as means + standard deviation (Dalagiorgou et al., 2013) for bar graphs. Multiple comparisons used one-way ANOVA and Tukey’s post-hoc analysis. p≤0.05 was considered statistically significant.

### Computational Methods

#### Gaussian accelerated molecular dynamics (GaMD)

GaMD is an unconstrained enhanced sampling approach that works by adding a harmonic boost potential to smooth the potential energy surface of biomolecules to reduce energy barriers (Miao et al., 2015). Brief description of the method is provided here.

Consider a system with N atoms at positions $r→={r→_{1},…,r→_{N}}$. When potential energy of the system $V(r⃑)$ is less than a threshold energy E, a boost potential $\DeltaV(r⃑)$ is added to the system as follows:

$$
V^{∗}(r→)=V(r→)+ΔV(r→), V(r→)<E
$$



$$
ΔV(r→)=\frac{1}{2}k(E−V(r→))^{2},V(r→)<E,
$$

where k is the harmonic force constant. The two adjustable parameters E and k can be determined by the application of three enhanced sampling principles. First, for any two arbitrary potential values $V_{1}r⃑$ and $V_{2}r⃑$ found on the original energy surface, if $V_{1}(r→)<V_{2}(r→)$, $\DeltaV$ should be a monotonic function that does not change the relative order of the biased potential values, i.e., $V_{1}^{∗}(r→)<V_{2}^{∗}(r→)$. Second, if $V_{1}(r→)<V_{2}(r→)$, the potential difference observed on the smoothed energy surface should be smaller than that of the original, i.e., $V_{2}^{∗}(r→)−V_{1}^{∗}(r→)<V_{2}(r→)−V_{1}(r→)$. By combining the first two criteria and plugging in the formula of $V^{*}(r⃑)$ and $ΔV$, we obtain:

$$
V_{max}\leqE\leqV_{min}+\frac{1}{k}
$$

where $V_{min}$ and $V_{max}$ are the system’s minimum and maximum potential energies. To ensure that Equation 3 is valid, k has to satisfy: $k\leq\frac{1}{V_{max}-V_{min}}$. Let us define $k≡\frac{k_{0}}{V_{max}−V_{min}}$, then $0<k_{0}\leq1$. Third, the standard deviation (SD) of ∆V needs to be small enough (i.e., narrow distribution) to ensure accurate reweighting using cumulant expansion to the second order: $\sigma_{\DeltaV}=k(E-V_{avg})\sigma_{V}\leq\sigma_{0}$, where $V_{avg}$ and $\sigma_{V}$ are the average and SD of ∆V with $\sigma_{0}$ as a user-specified upper limit (e.g. $10k_{B}T$) for accurate reweighting. When E is set to the lower bound $E=V_{max}$ according to Equation 3, $k_{0}$ can be calculated as:

$$
k_{0}=min⁡1.0,k_{0}^{`}=min1.0,\frac{\sigma_{0}}{\sigma_{V}}.\frac{V_{max}-V_{min}}{V_{max}-V_{avg}}
$$

Alternatively, when the threshold energy E is set to its upper bound $E=V_{min}+\frac{1}{k}$, $k_{0}$ is set to:

$$
k_{0}=k_{0}^{”}≡(1−\frac{\sigma_{0}}{\sigma_{V}}).\frac{V_{max}−V_{min}}{V_{avg}−V_{min}}
$$

if $k_{0}^{”}$ is calculated between 0 and 1. Otherwise, $k_{0}$ is calculated using Equation (4).

#### Peptide Gaussian accelerated molecular dynamics (Pep-GaMD)

Peptides often undergo large conformational changes during binding to target proteins, being distinct from small-molecule ligand binding or protein-protein interactions (PPIs). In this regard, Peptide GaMD or ‘Pep-GaMD’ has been developed to enhance the sampling of peptide binding (Wang and Miao, 2020). In Pep-GaMD, we consider a system of peptide L binding to a protein P in a biological environment E. Presumably, peptide binding mainly involves in both the bonded and non-bonded interaction energies of the peptide since peptides often undergo large conformational changes during binding to the target proteins. Thus, the essential peptide potential energy is $V_{L}(r)=V_{LL,b}(r_{L})+V_{LL,nb}(r_{L})+V_{PL,nb}(r_{PL})+V_{LE,nb}(r_{LE})$. In Pep-GaMD, we add boost potential selectively to the essential peptide potential energy according to the GaMD algorithm:

$$
ΔV_{L}(r)={\frac{1}{2}k_{L}(E_{L}−V_{L}(r))^{2},  V_{L}(r)<E_{L}0,  V_{L}(r)\geqE_{L}
$$

where EL is the threshold energy for applying boost potential and kL is the harmonic constant. In addition to selectively boosting the peptide, another boost potential is applied to the protein and solvent to enhance conformational sampling of the protein and facilitate peptide rebinding. This boost represents the total system potential energy without the essential peptide potential energy included:

$$
ΔV_{D}(r)={\frac{1}{2}k_{D}(E_{D}−V_{D}(r))^{2},  V_{D}(r)<E_{D}0,  V_{D}(r)\geqE_{D}
$$

Where VD represents the total system potential energy without the essential peptide potential energy included, ED represents the second boost potential threshold energy and kD represents the harmonic constant. Hence, this contributes to the dual-boost Pep-GaMD as the total boost potential $\DeltaVr=\DeltaV_{L}r+\DeltaV_{D}r$.

#### Energetic reweighting of Pep-GaMD simulations

For energetic reweighting of Pep-GaMD simulations to calculate potential mean force (PMF), the probability distribution along a reaction coordinate is written as $p^{*}(A)$. Given the boost potential $\DeltaV(r)$ of each frame, $p^{*}(A)$ can be reweighted to recover the canonical ensemble distribution $p(A)$, as:

$$
p(A_{j})=p^{∗}(A_{j})\frac{⟨e^{\betaΔV(r)}⟩_{j}}{\sumi=1M⟨p^{∗}(A_{i})e^{\betaΔV(r)}⟩_{i}},j=1,…,M
$$

where M is the number of bins, $\beta=k_{B}T$ and $e^{\beta\DeltaV(r)}_{j}$ is the ensemble-averaged Boltzmann factor of $\DeltaV(r)$ for simulation frames found in the jth bin. The ensemble-averaged reweighting factor can be approximated using cumulant expansion:

$$
e^{\beta\DeltaV(r)}_{j}=exp\sumk=1∞\frac{\beta^{k}}{k!}C_{k}
$$

where the first two cumulants are given by

$$
C_{1}=\DeltaV
$$



$$
C_{2}=\DeltaV^{2}-\DeltaV^{2}=\sigma_{V}^{2}
$$

The boost potential obtained from Pep-GaMD simulations usually follows near-Gaussian distribution. Cumulant expansion to the second order thus provides a good approximation for computing the reweighting factor. The reweighted free energy $FA=-k_{B}Tlnp(A)$ is calculated as

$$
F(A)=F^{∗}(A)−\sumk=12\frac{\beta^{k}}{k!}C_{k}+F_{c}
$$

where $F^{∗}(A)=−k_{B}Tlnp^{∗}(A)$ is the modified free energy obtained from GaMD simulation and $F_{c}$ is a constant.

#### Computational model of peptide agonist-bound ΔStalk PC1 CTF and HPEPDOCK docking

With GaMD simulations of the WT PC1 CTF obtained from the previous study that revealed an active TA/stalk-mediated allosteric signaling (Pawnikar et al., 2022), structural clustering of the extracellular regions of PC1 CTF, including the Stalk, TM2-TM3, and TM4-TM5 loops, TOP domain, S3-S4 loop and pore loop, was performed using the hierarchical agglomerative algorithm in CPPTRAJ (Roe and Cheatham, 2013). The top-ranked representative conformation of PC1 CTF was used for peptide docking after removal of the TA/stalk (ΔStalk). Then the HPEPDOCK (Zhou et al., 2018) webserver was applied to dock the p9, p17, and p21 stalk-derived peptides to ΔStalk CTF.

#### Simulation system setup

We embedded ΔStalk CTF in a palmitoyl-oleoyl-phosphatidyl-choline (POPC) bilayer and solvated the system in 0.15 M NaCl explicit solvent using CHARMM-GUI (Figure 2—figure supplement 1C). Neutral patches (acetyl and methylamide) were added to the protein termini residues. The peptide termini were kept as charged (NH3 + and COO-). The CHARMM36m (Vanommeslaeghe and MacKerell, 2015) force field parameters were used for the protein, peptides, and lipids. CHARMM-GUI output files and scripts were used with default parameters to prepare the systems for Pep-GaMD simulations. Energy minimization was performed for 5000 steps using a constant number, volume, and temperature (NVT) ensemble at 310 K. Further equilibration was done for 375 ps at 310 K using an NPT ensemble. Conventional MD (cMD) simulations was performed on the systems for 10 ns at 1 atm pressure and 310 K temperature. All-atom Pep-GaMD simulations were performed with a short cMD for 10 ns, Pep-GaMD equilibration for 55 ns followed by three independent Pep-GaMD production runs for 500 ns for each system with randomized initial atomic velocities. A cutoff distance of 9 Å was used for the van der Waals and short-range electrostatic interactions, and long-range electrostatic interactions were computed with the particle-mesh Ewald summation method (Darden et al., 1993). The simulation systems were ~90×136×117 Å3 in dimension, containing a total of ~100 K atoms with explicit solvent and lipid molecules.

#### Simulation analysis

Pep-GaMD simulation trajectories were analyzed using CPPTRAJ (Roe and Cheatham, 2013) and VMD (Humphrey et al., 1996) tools. Trajectory analysis showed peptides binding to the TOP domain of PC1 CTF. A previously identified salt bridge formed between the TOP domain R3848 and the pore loop E4078 of the PC1 protein is an important interaction during PC1 signal activation. The number of contacts formed between peptides p9, p17 and p21, respectively, and the R3848-E4078 salt bridge distance were used as reaction coordinates to calculate 2D free energy profiles using the PyReweighting toolkit (Miao et al., 2014). A bin size of 2 Å was used for distances and 10 for the number of contacts. Three independent Pep-GaMD simulations were combined to perform structural clustering using the hierarchical agglomerative clustering algorithm in CPPTRAJ (Roe and Cheatham, 2013). A 3 Å RMSD cutoff was used for each peptide system. PyReweighting (Miao et al., 2014) was then applied to calculate the original free energy values of each peptide structural cluster with a cutoff of 500 frames. The structural clusters were finally ranked according to the reweighted free energy values.

#### Potts sequence covariation model

Using a seed alignment of 189 orthologs of human PKD1 obtained from the Ensemble database (Aoto et al., 2016), we used iterative searching of the UniProt Database using HHblits (Howe et al., 2021) to obtain a multiple-sequence alignment of 4384 homologs, and after filtering using standard methods with an 80% identity threshold (Haldane and Levy, 2021), we obtained 1022 effective sequences of length 853. These sequences had an average of 23% sequence identity reflecting extensive diversity across Eukaryotes. As this number of sequences and sequence length could lead to an overfit model (Haldane and Levy, 2019), we used a subset the MSA to limit to 394 positions on the extracellular side of PKD1 including the GAIN domain, stalk, the TOP domain, and ends of the transmembrane helices. We inferred a Potts model from this reduced MSA using the Mi3-GPU software (Haldane and Levy, 2021). We evaluated the position-pair statistical interactions using the ‘weighted Frobenius norm’ interaction score (Haldane and Levy, 2021), and computed the residue-residue covariation values $C_{ab}^{ij}=f_{ab}^{ij}−f_{a}^{i}f_{b}^{j}$ as the difference between the pair-residue frequency $f_{ab}^{ij}$ of letters a and b at positions i,j and the null expectation under the assumption of site-independence by multiplying the two single-site frequencies, $f_{a}^{i}$ and $f_{b}^{j}$. The maximum possible covariance is 25%. Statistically significant covariations scores will be greater than the expected binomial sampling error given our dataset size of N~1022,, and for bivariate count $f_{ab}^{ij}$ the binomial-sampling standard deviation is $\sqrt{f_{ab}^{ij}(1-f_{ab}^{ij})/N}$ which for the typical bivariate frequency of ~10% corresponds to a ~1% error. To choose a cutoff in Frobenius Norm to distinguish likely contacts from noise, we compared the Potts interactions scores to the contacts predicted using the Alphafold (Jumper et al., 2021) structure, choosing the plotting cutoff at a false-positive rate of 50% relative to the contacts predicted using the Alphafold structure using a 8 Å nearest heavy atom side chain distance.

#### Peptide binding free energy calculations

Molecular Mechanics/Poisson-Boltzmann Surface Area (MM/PBSA) analysis was performed to calculate the binding free energies of peptides p9, p17, and p21 to PC1 CTF. The analysis was performed using the trajectory in which the peptide was bound to the receptor. In MM/PBSA (Wang et al., 2019), the binding free energy of the ligand (L) to the receptor (R) to form the complex (RL) is calculated as:

$$
ΔG_{bind}=G_{RL}−G_{R}−G_{L}
$$

where GRL is the Gibbs free energy of the complex RL, GR is the Gibbs free energy of the molecule R in its unbound state and GL is the Gibbs free energy of the molecule L in its unbound state, respectively.

$ΔG_{bind}$ can be divided into contributions of diﬀerent interactions as (Srinivasan et al., 1998):

$$
ΔG_{bind}=ΔH−TΔS=ΔE_{MM}+ΔG_{sol}−TΔS
$$

in which

$$
ΔE_{MM}=ΔE_{int}+ΔE_{elec}+ΔE_{vdW}
$$



$$
ΔG_{sol}=ΔG_{PB/GB}+ΔG_{SA}
$$



$$
ΔG_{SA}=\gamma.SASA+b
$$

where ΔEMM, ΔGsol, ΔH, and −TΔS are the changes in the gas-phase molecular mechanics (MM) energy, solvation-free energy, enthalpy, and conformational entropy upon ligand binding, respectively. ΔEMM includes the changes in the internal energies ΔEint (bond, angle, and dihedral energies), electrostatic energies ΔEelec, and the van der Waals energies ΔEvdW. ΔGsol is the sum of the electrostatic solvation energy ΔGPB/GB (polar contribution) and the nonpolar contribution ΔGSA between the solute and the continuum solvent. The polar contribution is calculated using either the Poisson Boltzmann (PB) or Generalized Born (GB) model, while the nonpolar energy is usually estimated using the solvent-accessible surface area (SASA) (Gilson and Honig, 1988; Wang et al., 2006) where γ is surface tension coefficient and b is the constant offset. The change in conformational entropy −TΔS is usually calculated by normal-mode analysis (Srinivasan et al., 1998) on a set of conformational snapshots taken from MD simulations. However, due to the large computational cost, changes in the conformational entropy are usually neglected as we were concerned more on relative binding free energies of the similar peptide ligands.

MM/PBSA analysis was performed using the gmx_MMPBSA (Valdés-Tresanco et al., 2021) software with the following command line:

gmx_MMPBSA -O -i mmpbsa.in -cs com.tpr -ci index.ndx -cg 1 13 -ct com_traj.xtc -cp topol.top -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv

Input file for running MM/PBSA analysis:

&general
sys_name="Prot-Pep-CHARMM",
startframe=1,
endframe=200,
# In gmx_MMPBSA v1.5.0 we have added a new PB radii set named charmm_radii
# This radii set should be used only with systems prepared with CHARMM force fields.
# Uncomment the line below to use charmm_radii set
#PBRadii=7,
/
&pb
# radiopt=0 is recommended which means using radii from the prmtop file for both the PB calculation and for the NP
# calculation
istrng=0.15, fillratio=4.0, radiopt=0

Residue-wise interaction energy analysis was performed on peptides p9, p17, and p21 using the trajectory in which the peptide was bound to the PC1 CTF using the gmx_MMPBSA (Valdés-Tresanco et al., 2021) software with the following command line:

gmx_MMPBSA -O -i mmpbsa.in -cs com.tpr -ct com_traj.xtc -ci index.ndx -cg 3 4 -cp topol.top -o FINAL_RESULTS_MMPBSA.dat -eo FINAL_RESULTS_MMPBSA.csv -do FINAL_DECOMP_MMPBSA.dat -deo FINAL_DECOMP_MMPBSA.csv

Input file for running residue-wise energy decomposition analysis:

&general
sys_name="Decomposition",
startframe=1,
endframe=200,
#forcefields="leaprc.protein.ff14SB"
/
&gb
igb=5, saltcon=0.150,
/
#make sure to include at least one residue from both the receptor
#and peptide in the print_res mask of the &decomp section.
#this requirement is automatically fulfilled when using the within keyword.
#http://archive.ambermd.org/201308/0075.html
&decomp
idecomp=2, dec_verbose=3,
print_res="A/854-862 A/1-853”,
/
