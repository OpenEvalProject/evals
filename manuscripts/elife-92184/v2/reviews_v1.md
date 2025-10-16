# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92184.3.sa0](https://doi.org/10.7554/eLife.92184.3.sa0)

This study presents a useful deep learning-based inter-protein contact prediction method named PLMGraph-Inter which combines protein language models and geometric graphs. The evidence supporting the claims of the authors is solid. The authors show that their approach may be used in cases where AlphaFold-Multimer performs poorly. This work will be of interest to researchers working on protein complex structure prediction, particularly when accurate experimental structures are available for one or both of the monomers in isolation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92184.3.sa1](https://doi.org/10.7554/eLife.92184.3.sa1)

Summary:

Given knowledge of the amino acid sequence and of some version of the 3D structure of two monomers that are expected to form a complex, the authors investigate whether it is possible to accurately predict which residues will be in contact in the 3D structure of the expected complex. To this effect, they train a deep learning model which takes as inputs the geometric structures of the individual monomers, per-residue features (PSSMs) extracted from MSAs for each monomer, and rich representations of the amino acid sequences computed with the pre-trained protein language models ESM-1b, MSA Transformer, and ESM-IF. Predicting inter-protein contacts in complexes is an important problem. Multimer variants of AlphaFold, such as AlphaFold-Multimer, are the current state of the art for full protein complex structure prediction, and if the three-dimensional structure of a complex can be accurately predicted then the inter-protein contacts can also be accurately determined. By contrast, the method presented here seeks state-of-the-art performance among models that have been trained end-to-end for inter-protein contact prediction.

Strengths:

The paper is carefully written and the method is very well detailed. The model works both for homodimers and heterodimers. The ablation studies convincingly demonstrate that the chosen model architecture is appropriate for the task. Various comparisons suggest that PLMGraph-Inter performs substantially better, given the same input, than DeepHomo, GLINTER, CDPred, DeepHomo2, and DRN-1D2D_Inter.

The authors control for some degree of redundancy between their training and test sets, both using sequence and structural similarity criteria. This is more careful than can be said of most works in the field of PPI prediction.

As a byproduct of the analysis, a potentially useful heuristic criterion for acceptable contact prediction quality is found by the authors: namely, to have at least 50% precision in the prediction of the top 50 contacts.

Weaknesses:

The authors check for performance drops when the test set is restricted to pairs of interacting proteins such that the chain pair is not similar *as a pair* (in sequence or structure) to a pair present in the training set. A more challenging test would be to restrict the test set to pairs of interacting proteins such that *none* of the chains are separately similar to monomers present in the training set. In the case of structural similarity (TM-scores), this would amount to replacing the two "min"s with "max"s in Eq. (4). In the case of sequence similarity, one would simply require that no monomer in the test set is in any MMSeqs2 cluster observed in the training set. This may be an important check to make, because a protein may interact with several partners, and/or may use the same sites for several distinct interactions, contributing to residual data leakage in the test set.

The training set of AFM with v2 weights has a global cutoff of 30 April 2018, while that of PLMGraph-Inter has a cutoff of March 7 2022. So there may be structures in the test set for PLMGraph-Inter that are not in the training set of AFM with v2 weights (released between May 2018 and March 2022). The "Benchmark 2" dataset from the AFM paper may have a few additional structures not in the training or test set for PLMGraph-Inter. I realize there may be only few structures that are in neither training set, but still think that showing the comparison between PLMGraph-Inter and AFM there would be important, even if no statistically significant conclusions can be drawn.

Finally, the inclusion of AFM confidence scores is very good. A user would likely trust AFM predictions when the confidence score is high, but look for alternative predictions when it is low. The authors' analysis (Figure 6, panels c and d) seems to suggest that, in the case of heterodimers, when AFM has low confidence, PLMGraph-Inter improves precision by (only) about 3% on average. By comparison, the reported gains in the "DockQ-failed" and "precision-failed" bins are based on knowledge of the ground truth final structure, and thus are not actionable in a real use-case.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92184.3.sa2](https://doi.org/10.7554/eLife.92184.3.sa2)

This work introduces PLMGraph-Inter, a new deep learning approach for predicting inter-protein contacts, which is crucial for understanding protein-protein interactions. Despite advancements in this field, especially driven by AlphaFold, prediction accuracy and efficiency in terms of computational cost still remains an area for improvement. PLMGraph-Inter utilizes invariant geometric graphs to integrate the features from multiple protein language models into the structural information of each subunit. When compared against other inter-protein contact prediction methods, PLMGraph-Inter shows better performance which indicates that utilizing both sequence embeddings and structural embeddings is important to achieve high-accuracy predictions with relatively smaller computational costs for the model training.
