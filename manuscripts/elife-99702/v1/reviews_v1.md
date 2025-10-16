# Peer review - Round 1

Editors:
- Anna Panchenko, Queen's University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99702.3.sa0](https://doi.org/10.7554/eLife.99702.3.sa0)

This important study demonstrates that combining AlphaFold2 with the author's sampling method AF2-RAVE improves protein-ligand docking for three protein kinases and their inhibitors. The evidence is compelling and the results will be of interest to researchers who work on computer-aided drug design.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99702.3.sa1](https://doi.org/10.7554/eLife.99702.3.sa1)

The development of effective computational methods for protein-ligand binding remains an outstanding challenge to the field of drug design. This impressive computational study combines a variety of structure prediction (AlphaFold2) and sampling (RAVE) tools to generate holo-like protein structures of three kinases (DDR1, Abl1, and Src kinases) for binding to type I and type II inhibitors. Of central importance to the work is the conformational state of the Asp-Phy-Gly "DFG motif" where the Asp points inward (DFG-in) in the active state and outward (DFG-out) in the inactive state. The kinases bind to type I or type II inhibitors when in the DFG-in or DFG-out states, respectively.

It is noted that while AlphaFold2 can be effective in generating ligand-free apo protein structures, it is ineffective at generating holo structures appropriate for ligand binding. Starting from the native apo structure, structural fluctuations are necessary to access holo-like structures appropriate for ligand-binding. A variety of methods, including reduced multiple sequence alignment (rMSA), AF2-cluster, and AlphaFlow may be used to create decoy structures. However, those methods can be limited in the diversity of structures generated and lack a physics-based analysis of Boltzmann weight critical to their relative evaluation.

To address this need, the authors combine AlphaFold2 with the Reweighted Autoencoded Variational Bayes for Enhanced Sampling (RAVE) method, to explore metastable states and create a Boltzmann ranking. With that variety of structures in hand, grid-based docking methods Glide and Induced-Fit Docking (IFD) were used to generate protein-ligand (kinase-inhibitor) complexes.

The authors demonstrate that using AlphaFold2 alone, there is a failure to generate DFG-out structures needed for binding to type II inhibitors. By applying the AlphaFold2 with rMSA followed by RAVE (using short MD trajectories, SPIB-based collective variable analysis, and enhanced sampling using umbrella sampling), metastable DFG-out structures with Boltzmann weighting are generated enabling protein-ligand binding. Moreover, the authors found that the successful sampling of DFG-out states for one kinase (DDR1) could be used to model similar states for other proteins (Abl1 and Src kinase). The AF2RAVE approach is shown to result in a set of holo-like protein structures with a 50% rate of docking type II inhibitors.

Overall, this is excellent work and a valuable contribution to the field that demonstrates the strengths and weaknesses of state-of-the-art computational methods for protein-ligand binding. The authors also suggest promising directions for future study, noting that potential enhancements in the workflow may result from the use of binding site prediction models and free energy perturbation calculations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99702.3.sa2](https://doi.org/10.7554/eLife.99702.3.sa2)

This manuscript explores the utility of AlphaFold2 (AF2) and the author's own AF2-RAVE method for drug discovery. As has been observed elsewhere, the predictive power of docking against AF2 structures is quite limited, particularly for proteins like kinases that have non-trivial conformational dynamics. However, using enhanced sampling methods like RAVE to explore beyond AF2 starting structures leads to a significant improvement.

Comments on revised version:

I'm happy with the changes made.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99702.3.sa3](https://doi.org/10.7554/eLife.99702.3.sa3)

In this manuscript, the authors aim to enhance AlphaFold2 for protein conformation-selective drug discovery through the integration of AlphaFold2 and physics-based methods, focusing on improving the accuracy of predicting protein structures ensemble and small molecule binding of metastable protein conformations to facilitate targeted drug design.

The major strength of the paper lies in the methodology, which includes the innovative integration of AlphaFold2 with all-atom enhanced sampling molecular dynamics and induced fit docking to produce protein ensembles with structural diversity. Moreover, the generated structures can be used as reliable crystal-like decoys to enrich metastable conformations of holo-like structures. The authors demonstrate the effectiveness of the proposed approach in producing metastable structures of three different protein kinases and perform docking with their type I and II inhibitors. The paper provides strong evidence supporting the potential impact of this technology in drug discovery. However, limitations may exist in the generalizability of the approach across other structures, especially complex structures such as protein-protein or DNA-protein complexes.

The authors largely achieved their aims by demonstrating that the AF2RAVE-Glide workflow can generate holo-like structure candidates with a 50% successful docking rate for known type II inhibitors. This work is likely to have a significant impact on the field by offering a more precise and efficient method for predicting protein structure ensemble, which is essential for designing targeted drugs. The utility of the integrated AF2RAVE-Glide approach may streamline the drug discovery process, potentially leading to the development of more effective and specific medications for various diseases.

Comments on revised version:

The revised manuscript looks great to me. I have no further comments.
