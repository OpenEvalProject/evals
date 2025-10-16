# Peer review - Round 1

Editors:
- Mingjie Zhang, Hong Kong University of Science and Technology Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73218.sa0](https://doi.org/10.7554/eLife.73218.sa0)

This is an impressive study providing solid evidence for a molecular mechanism by which two related, high-affinity growth factors, binding in exactly the same site, can achieve differential signaling outputs through a dimerized receptor tyrosine kinase, and represents an important advance in the field.


---

# Peer review - Round 1

Editors:
- Mingjie Zhang, Hong Kong University of Science and Technology Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73218.sa1](https://doi.org/10.7554/eLife.73218.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A molecular mechanism for the generation of ligand-dependent differential outputs by the epidermal growth factor receptor" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Stevan R Hubbard (Reviewer #1); Xiao-chen Bai (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Cryo-EM 3D classification was widely used to analyze the dynamics of protein complexes. It could be efficient in probing new intermediate states. But it is not strictly a quantitative method unless certain "unbiased" procedures are applied throughout the complete workflow of image processing. For example, the authors only showed classification results of one dataset (Figure 2). The particles appeared to be evenly distributed in the ten classes, which was a sign that the classification was not efficient and the resulting reconstructions are still mixtures of multiple states. To support the main conclusion of the manuscript, the authors should show the classification results of all datasets: (1) To our knowledge, cryoSparc is less efficient in separating particles into different conformations compared to Relion. The authors could try Relion and multiple rounds of 3D classification could be implemented. (2) Mask-based classification should be applied. (3) The authors could provide an analysis on the changes of particle distribution among different datasets.

2. Although the mutations introduced into EGFR (W492G, etc.) that mitigate the phosphorylation differences between EGF and TGF-αt are strong evidence for the authors' hypothesis, it is important to show (through a ligand-concentration series) that saturating amounts of TGF-α cannot achieve the same EGFR phosphorylation level as saturating amounts of EGF. The authors used a single concentration of EGF or TGF-α (16 µM in vitro, 16 nM in-cell) in the results shown in Figure 9 and Figure 9-supplement 1. Any differences in affinity and/or ligand solubility/delivery, etc. between EGF and TGF-α could explain the difference in phosphorylation levels in the experiments with wild-type EGFR.

3. For the cell-based phosphorylation results shown in Figure 9C and E, the authors have already performed at least three biological replicates. It would be useful for the readers if the authors could include densitometry analysis and appropriate statistics on the biological replicates to show the effect of mutations and different types of ligand binding on EGFR activity in a more quantitative way.

4. What is rationale to use 16.7 nM as the ligand concentration in the cell-based assay? Has this been commonly used in EGFR activity assay in previous work? Have the authors tried other ligand concentration?

5. Related to previous two points, have the authors tested the effect of L834R mutation on the activity of EGFR using similar cell-based phosphorylation experiment? This is just to confirm that L834R is indeed a gain-of-function mutation. It also would be interesting to check whether EGFR-L834R also has different activities when responding to EGF or TGF-α.

6. The authors need to prepare similar figures as Figure3A to show the cryo-EM image processing workflows for EGFR/TGF-α and EGFR-L834R/EGF datasets.

7. The authors claimed that conformations between ECD, TM and ICD are coupled within ligand-bound EGFR. But the TM and kinase domains are not resolved at all in any of the classes. Could the authors provide a brief explanation for this issue?

Reviewer #1:

The manuscript by Huang et al. reports the cryo-EM structures of EGF and TGFalpha bound to full-length EGFR. As for other receptor tyrosine kinases like the insulin and IGF1 receptors, the transmembrane helices and cytoplasmic kinase domains are not resolved in the cryo-EM maps.

3D classification of EGF-EGFR revealed multiple, closely-related conformational states of the ligand-bound ectodomain, in which a "scissor-like" rotation of the EGF binding portion of the ectodomain (D1-3) was correlated with a separation of the ends of the membrane-proximal domain (D4); the larger the scissor angle (~25{degree sign}), the closer the ends of D4 (~5 Å), and vice versa. For the smaller scissor angle of ~10{degree sign}, the two-fold symmetry of the EGF+EGFR complex breaks down, such that one of the D4 domains pivots from D1-3 further than the other one, resulting in a D4 separation of ~20 Å.

The authors utilized previous NMR data on the isolated TM helices of EGFR, which indicated that there are two mutually exclusive crossovers points between the TM helices, one closer to the N-termini of the helices and one closer to the C-termini. Molecular dynamics simulations performed by the authors showed that, in general, the "tips-separated" configuration of the D4 domains was correlated with the N-terminal apposition of the TM helices, and the "tips-juxtaposed" configuration was correlated with the C-terminal apposition.

Previous biochemical data had indicated/suggested that the N-terminal dimerization of the TM helices results in higher kinase activity (through formation of the asymmetric kinase dimer) than the C-terminal dimerization, even though the C-terminal dimerization places the cytoplasmic juxtamembrane (JM) regions (leading into the kinase domains) closer together.

The authors determined cryo-EM structures of EGF bound to an EGFR mutant, L834R, which is a gain-of-function substitution in the activation loop of the kinase domain, and found that D4 in the tips-separated conformation was stabilized vs. in wild-type EGFR, indicating that a stabilized asymmetric kinase dimer is conformationally coupled to the tips-separated ectodomain conformation.

The authors determined cryo-EM structures with TGFalpha bound to EGFR and found that, in this ensemble of structures, D4 in the tips-separated conformation was destabilized (vs. in the EGF-EGFR structures) because of slight differences in the ligand-binding head of EGFR induced by TGFalpha vs. EGF binding.

All of these data - theirs and others - led to the hypothesis that EGF is a higher activity ligand than TGFalpha (despite both being high-affinity binders to EGFR) because of the conformational coupling between the ligand-binding head of EGFR, the distal tips of D4, the TM helices, the cytoplasmic JM region, and the asymmetric kinase dimer. To test this hypothesis, the authors performed in vitro and in-cell activity assays and, indeed, found that the level of EGFR phosphorylation was higher when stimulated with EGF vs. TGFalpha.

To provide evidence that the conformational coupling described above was responsible, the authors generated mutant EGFRs -a point mutation in D4 (W492G) and insertion in and replacement of the extracellular JM region - and measured phosphorylation levels upon stimulation with EGF or TGFalpha. These data showed that increasing the flexibility in these regions (through mutation) abrogated the phosphorylation difference in the two cases (EGF vs. TGFalpha), consistent with their hypothesis.

In summary, this is an impressive study providing solid evidence for a molecular mechanism by which two related, high-affinity growth factors, binding in exactly the same site, can achieve differential signaling outputs through a dimerized receptor tyrosine kinase, and represents an important advance in the field.

Although it is surprising that the small conformational differences in the ligand-binding head of EGFR resulting from either EGF or TGFalpha binding can be "faithfully" propagated through the D4 domains into the TM helices and then into the cytoplasmic region to affect asymmetric kinase dimer formation, the data are quite convincing, especially the mutagenesis data.

Specific Points:

1) Although the mutations introduced into EGFR (W492G, etc.) that mitigate the phosphorylation differences between EGF and TGFalpha are strong evidence for the authors' hypothesis, it is important to show (through a ligand-concentration series) that saturating amounts of TGFalpha cannot achieve the same EGFR phosphorylation level as saturating amounts of EGF. The authors used a single concentration of EGF or TGFalpha (16 µM in vitro, 16 nM in-cell) in the results shown in Fig. 9 and Fig. 9-supplement 1. Any differences in affinity and/or ligand solubility/delivery, etc. between EGF and TGFalpha could explain the difference in phosphorylation levels in the experiments with wild-type EGFR.

2) In Fig. 2, it would be instructive for the reader to know exactly what the high and low map contour levels are (e.g., number of sigmas).

Other concerns:

1. As stated in line 266, the EM density for one domain IV leg in the tips-separated conformation of EGFR: TGF-α was poorly defined. The residual EM density seemed to suggested a "juxtaposed" conformation rather than "separated" state in in EGFR(L834R):EGF and EGFR(L834R):EGF (Figure 7, top panels).

2. Line 197-201. The MD simulation could be done with the TM region plus extracellular module.

3. Figure 9, panel E does not have a WT control.

Reviewer #2:

EGFR can be activated by several extracellular ligands. The molecular mechanisms of EGFR in differentiating extracellular signals from these ligands and transforming them into distinct intracellular signaling outputs are not fully understood. In this manuscript, Huang et al. carried out structural analysis of the full-length human EGFR (with ligand EGF or TGF-α) using cryo-EM and MD simulation. The authors reported that the dimeric structure of the two extracellular modules is not rigid at the dimeric interface, resulting in conformational fluctuations of individual domains. One interesting observation was the membrane-proximal tip of the extracellular module in representative two conformations, "separated" and "juxtaposed" states. The authors next tried to correlate the structural dynamics of EGFR to its signaling outputs.

Cryo-EM 3D classification was widely used to analyze the dynamics of protein complexes. It could be efficient in probing new intermediate states. But it is not strictly a quantitative method unless certain "unbiased" procedures are applied throughout the complete workflow of image processing. For example, the authors only showed classification results of one dataset (Figure 2). The particles appeared to be evenly distributed in the ten classes, which was a sign that the classification was not efficient and the resulting reconstructions are still mixtures of multiple states. To support the main conclusion of the manuscript, the authors should show the classification results of all datasets: (1) To our knowledge, cryoSparc is less efficient in separating particles into different conformations compared to Relion. The authors could try Relion and multiple rounds of 3D classification could be implemented. (2) Mask-based classification should be applied. (3) The authors could provide an analysis on the changes of particle distribution among different datasets.

Reviewer #3:

This will be a landmark work in the RTK and EGFR fields. Huang et. al reported a series of cryo-EM structures of full-length EGFR/EGF complexes in different conformations. The major difference among these structures is the distance between the membrane proximal domains IV of EGFR. Although the TM and kinase domains of EGFR were not resolved in the cryo-EM maps, through comprehensive structural analysis and MD simulations, the authors proposed that, the EGFR/EGF complex with separated domains IV would induce N-terminal associated dimeric TM domain and high activity; whereas the EGFR/EGF complex with juxtaposed domains IV would promote C-terminal associated dimeric TM domain and low activity. Such claim is strongly supported by two structure evidences: (1) In the cryo-EM structure of EGFR L834R mutant/EGF complex (a mutant that is supposed to have higher activity than EGFR WT), the separated domains IV is captured in a more stable state. (2) In the cryo-EM structure of EGFR with a weaker ligand TGF-a bound, the separated domains IV is in a more flexible conformation. In addition, the authors also introduced some mutations to EGFR, designed to break the structural coupling between domain IV and TM domain. These EGFR mutants can't response to EGF and TGF-a differently, which further supports the major conclusion of this work that the conformation of ECD determines the conformation of TM as well as the downstream signaling. Overall, the experiments were well designed, and the structural and functional works are of great quality.
