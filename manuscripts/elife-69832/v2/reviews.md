# Peer review - Round 1

Editors:
- Patricia Bassereau, Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69832.sa0](https://doi.org/10.7554/eLife.69832.sa0)

Although the role of membrane potential in cell-penetrating peptide (CPP) translocation has been consistently described in artificial systems, this multi scale study combining cell biology, genetics and in silico approaches further extends this topic to a live cell context where it shows that internalization stops when the membrane polarization is decreased by the removal of potassium channels. It proposes an original mechanism of CPP translocation based on transient water pore formation, which should be of interest for biophysicists, cell biologists and for applications such as drug deliver.


---

# Peer review - Round 1

Editors:
- Patricia Bassereau, Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69832.sa1](https://doi.org/10.7554/eLife.69832.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Genetic, cellular and structural characterization of the membrane 1 potential-dependent cell-penetrating peptide translocation pore" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alain Joliot (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We believe that your study is original and brings new data to the field. The additional data that we ask should strengthen your paper and should be feasible in about 2 months.

1) Data analysis:

Quantification of CPP uptake that takes into account the intracellular localization of the CPP (cytosolic versus vesicular) is a critical issue in cellular models. In this study, quantification relies either on the toxicity induced by the cytosolic accumulation of the Tat-RasGAP peptide or on the direct visualization of fluorescently-labelled CPPs. In the latter case, the choice made by the authors to define 3 categories for quantification has to be justified. More precisely, merging the low and strong cytosolic signal categories into a single one is questionable as these two categories might correspond to distinct functional fates due to the highly variable cytosolic staining (much more than between vesicular and low cytosolic). Indeed, the water pore mechanism invoked by the authors might correspond to an "all or none" mechanism for the cytosolic delivery that thus, to low and high cytosolic contents, respectively. It would be then relevant to determine how each category (low and high) is affected by the membrane potential.

In order to link functional (toxicity) and live imaging analysis assays, one possibility would be to analyze the remaining living cells following long incubation (16-24h) with FITC-TAT RasGAP to estimate which staining category is actually killed (ideally with or without hyperpolarization). The non-toxic mutant TatRASGAP (W317A) could be used as control.

Optional: To check whether the very large heterogeneity in the translocation efficiency within a same cell culture could be related to heterogeneities in membrane potential among cells, the membrane potential of each cell could be measured (using DiBAC4(3) labelling or any genetically encoded membrane potential sensor) together with CPP translocation (labelled TMR if using DiBAC).

2) Ectopic expression of the potassium channel in "heterologous" context.

Although distinct types of potassium channels have been characterized in the screen, the authors only consider their action on the membrane potential, supported by the effects of specific drugs. However, translocation efficiency does not strictly correlate with membrane potential (e. g. KCNJ2 expression in WT and KCNN4 KO Hela figure 3B). It would be interesting to evaluate if KCNQ5 expression would rescue or even increase internalization (additive effect) in SW6.4 and HeLa cells (WT and KCNN4 KO) and vice versa (KCNN4 expression in Raji). This would also avoid any potential interference of the CRISPR system on ectopic expression. Indeed, the kinetic of CPP uptake significantly differs between cell lines (Figure 1B, almost 100% negative cells for Raji at 20 minutes and only 20% for the 2 others), suggesting partially distinct mechanisms.

On the simulations:

3)The limitations of the simulations should be discussed. The main limitation is the structure of peptides because the Martini forcefield (the version should be mentioned) is not able to properly capture peptide folding, which can be important in membrane adsorption/translocation. Thus, the in silico results should be viewed only as an indication (not proof), the folding issue should be mentioned in the manuscript and the authors should more clearly specify what the peptide structures are.

4) Current simulations seem to mainly capture the effect of simple electrostatics; i.e. more charges, more penetration. To test this, the authors could do simulations with K9 and compare it to R9, which is known experimentally to translocate better than K9. Such comparison would show what simulations actually detect.

Optional:

– Further check experimentally the physical mechanism related to the membrane potential: compare the uptake effectiveness for different lengths of poly-arginines. If the mechanism is correct, the effectiveness will increase with increasing length.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Genetic, cellular and structural characterization of the membrane potential-dependent cell-penetrating peptide translocation pore" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alain Joliot (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer #1 (Recommendations for the authors):

The authors responded to all the raised issues and modified the manuscript accordingly. The manuscript represents an important contribution to the field of CPP translocation into cells. Based on the experiments and simulations CPP, they propose a mechanism that CPPs enter the cell thanks to the electrostatic membrane potential. The data are well presented, however, it seems to me that the authors overinterpret the data because the presented mechanism and its discussion have few flaws:

On page 21: The authors state: "However, it has been determined that, once embedded into membranes, lysine residues tend to lose protons (Armstrong et al., 2016; Li et al., 2013). This will thus dissipate the strong membrane potential required for the formation of water pores and leave the lysine-containing CPPs stuck within the phospholipids of the membrane."

Lysine can indeed get neutral in the membrane, and the deprotonated state is the most favorable state in the middle of the membrane hydrophobic core (see MacCallum et al., 2008 for free energy profiles of lysine insertion). However, it is energetically unfavorable for lysine to be inside the membrane even when deprotonated. The most favorable state for lysin is to be protonated in solution (around neutral pH), i.e., lysine residue is hydrophilic, not hydrophobic. Therefore, lysine residues preferentially leave the membrane and not get stuck inside the membrane, as the authors state. Moreover, the proton will dissociate during the lysine insertion into the membrane, and thus it most likely stays outside of the cell. Note that when peptides are in the pore, they are not in the hydrophobic core of the membrane.

Page 22: "…water pores created by megapolarization have a diameter of about 2(-5) nm. Molecules larger than 2 nm are therefore less efficiently transported through these water pores. Polyarginine peptides of 20 amino acids or more have a predicted spherical diameter greater than 2 nm and would travel less efficiency through the water pores than shorter peptides. The efficiency of direct translocation is therefore likely modulated by the number of positive charges of the peptide and the size of the peptides (not mentioning the role of the secondary structures adopted by the CPPs)."

I agree with the general statement that the uptake of large molecules could be hindered or even prevented by the limited size of the pore size. However, the PEPFOLD-3 server, which the authors used for the prediction of peptide structures fixed in all simulations, predicts helical structure for polyarginine peptides with lengths 9 and even 20. Such helix has a diameter smaller than 2 nm along the helical axes and thus can easily get through the pore. Therefore, the presented data/discussion is not consistent with simulations.

Finally, the authors correctly state that arginine residues could be replaced by tryptophan residues in CPPs leading to similar translocation in cells. This possibility clearly demonstrates that there is more into the CPP translocation mechanism than the electrostatic membrane potential. The used explanation "It appears that loss of positive charges that contribute to water pore formation can be compensated by acquisition of strengthened lipid interactions when arginine residues are replaced with tryptophan residues." is strange because the use of more residues with less hydrophobic character would then have the same effect (e.g., two phenylalanine residues instead of arginine or tryptophan). In addition, the membrane potential does not explain the experiments on GUVs. Therefore, despite a nice demonstration of the importance of the membrane potential for the CPP translocation into cells, the mechanism seems to be more complex.

Reviewer #2 (Recommendations for the authors):

I really appreciate the efforts of the authors to provide new experimental data in response to the comments, which reinforce the quality of the manuscript. I fully agree that the time component should be critical at the level the whole cell population, which is not incompatible with an all or none mechanism at the single cell level, i.e.once reaching the favorable membrane potential. Surprisingly, fluorescent median intensity rather than the percentage of cells with high intensity signal seems to increase over time (Figure 1 sup4, error in axis title panel D) at least in HeLa cells. Inherent to most original studies, this work raises some interesting questions which remain unanswered or unclear but this would be part of another study. In particular, the use of genetic sensor instead of diBac to measure membrane potential might greatly help to dissect the translocation process on a single-cell basis.

In conclusion I would recommend the publication of this manuscript in its revised version
