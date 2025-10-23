# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95992.3.sa0](https://doi.org/10.7554/eLife.95992.3.sa0)

This joint computational/experimental study demonstrates the ability of synthetic peptides derived from the stalk tethered agonist in polycystin-1 (PC1) to re-activate signaling by a stalkless C-terminal fragment of PC1. The study is valuable as it discovered peptide agonists for PC1 and the integrated in vitro and in silico approach is potentially applicable to the analysis of related systems. Following the revision, the line of evidence presented in the current manuscript is considered convincing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95992.3.sa1](https://doi.org/10.7554/eLife.95992.3.sa1)

Summary:

This research used cell-based signaling assay and Gaussian-accelerated molecular dynamics (GaMD) to study peptide-mediated signaling activation of polycystin-1 (PC1), which is responsible for the majority of autosomal dominant Polycystic Kidney Disease (ADPKD) cases. Synthetic peptides of various lengths derived from the N-terminal portion of the PC1 C-terminal fragment (CTF) were applied to HEK293T cells transfected with stalkless mouse CTF expression construct. It was shown that peptides including the first 7, 9, and 17 residues of the N-terminal portion could activate signaling to the NFAT reporter. To further understand the underlying mechanism, docking and peptide-GaMD simulations of peptides composed of the first 9, 17, and 21 residues from the N-terminal portion of the human PC1 CTF were performed. These simulations revealed the correlation between peptide-CTF binding and PC1 CTF activation characterized by the close contact (salt bridge interaction) between residues R3848 and E4078. Finally, a Potts statistical model was inferred from diverged PC1 homologs to identify strong/conserved interacting pairs within PC1 CTF, some of which are highly relevant to the findings from the peptide GaMD simulations. The peptide binding pockets identified in the GaMD simulations may serve as novel targets for design of therapeutic approaches for treating ADPKD.

Strengths:

(1) The experimental and computational parts of this study complement and mostly support each other, thus increasing the overall confidence in the claims made by the authors.

(2) The use of exogenous peptides and a stalkless CTF in the GaMD is a step forward compared to earlier simulations using the full CTF, CTF mutants, or the stalkless CTF alone. And it led to findings of novel binding pockets.

(3) Since the PC1 shares characteristics with the Adhesion class of GPCRs, the approaches used in this work may be extended to other similar systems.

Weaknesses:

(1) Only results for selective peptides (p9, p17 p21) binding with the protein were shown. It would be interesting to see the interaction between some (if not all) of the other peptides with the protein.

(2) The convergence of the simulations is not very good. The results should be interpreted more qualitatively rather than quantitively because large variations in the free energy profile were seen between different replicates. Although these simulations might have identified representative low-energy binding conformations of the peptides, whether they have explored all possible conformations is still a question.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95992.3.sa2](https://doi.org/10.7554/eLife.95992.3.sa2)

Summary:

This manuscript, "Activation of polycystin-1 Signaling by Binding of Stalk-derived Peptide Agonists", by Miao and coworkers. The autosomal dominant Polycystic Kidney Disease (ADPKD) is a major form of Polycystic Kidney Disease (PKD). To provide better treatment and avoid side effects associated with currently available options, the authors investigated an interesting GPCR, polycystin-1 (PC1), as a potential therapeutic target. In vitro and in silico studies were combined to identify peptide agonists for PC1 and to elucidate their roles in PC1 signaling. Overall, regarding the significance of the findings, this work described valuable peptide agonists for PC1 and the combined in vitro and in silico approach can be useful to study a complex system like PC1. However, the strength of the evidence is incomplete, as more experiments are needed as controls to validate the computational observations. The work appears premature.

Strengths:

(1) This work first described the experimental discovery of short peptides designed to mimic the stalk region of PC1, followed by computational investigation using docking and MD simulations. PC1 is a complex membrane protein and an emerging target for ADPKD, but it can be challenging to study. The knowledge and the peptide discovery can be valuable and useful to understand the mechanism and potential modulation of PC1.

(2) The authors published the mechanistic study of PC1 and identified key interacting residues such as N3074-S3585 and R3848-E4078, using very similar techniques (PNAS 2022, 119(19), e2113786119). This work furthers this research by identifying peptides that are stalk mimics for PC1 activation.

(3) Eight peptides were designed and tested experimentally first; three were computationally studied with docking and GaMD simulations to understand their mechanism (s).

Weaknesses:

(1) The selectivity of the peptides between PC1 and PC2 remains unknown in this revision.

Overall, my comments were mostly addressed properly.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95992.3.sa3](https://doi.org/10.7554/eLife.95992.3.sa3)

Summary:

The authors demonstrate the activation of polycystin-1 (PC1), a G-protein coupled receptor, using small peptides derived from its original agonist, the stalk TA protein. In the experimental part of the study, the authors performed cellular assays to check the peptide-induced reactivation of a mutant form of PC1 which does not contain the stalk agonist. The experimental data is supported by computational studies using state-of-the-art Gaussian accelerated Molecular Dynamics (GaMD) and bioinformatics analysis based on sequence covariance. The computer simulations revealed the mechanistic details of the binding of the said peptides with the mutant PC1 protein and discovered different bound, unbound, and intermediate conformations depending on the peptide size and sequence. Due to the use of reliable and well-established molecular simulation algorithms and the physiological relevance of this protein autosomal dominant Polycystic Kidney Disease (ADPKD) make this work particularly valuable.

Strengths:

This work is exploratory and its goal is to establish that small peptides can be used to probe the PC1 signaling process. The authors have provided sufficient evidence to justify this claim. Their GaMD simulations have produced free-energy landscapes that differentiate the interaction of PC1 with three different synthetic peptides and demonstrate the associated conformational dynamics of the receptor protein. Their trajectory analysis and sequence covariance analysis could identify residue-specific interactions that facilitate this process. The authors also performed residue-wise and total interaction energy calculations to substantiate their findings.

Weaknesses:

The reported free energy landscapes are not fully converged. But they are still sufficient to gain biological insight.
