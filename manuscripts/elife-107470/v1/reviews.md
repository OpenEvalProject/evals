# Peer review - Round 1

Editors:
- Martin Graña, Institut Pasteur de Montevideo Uruguay

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.107470.3.sa0](https://doi.org/10.7554/eLife.107470.3.sa0)

This important study presents a sequence-based method for predicting drug-interacting residues in intrinsically disordered proteins (IDPs), addressing a significant challenge in understanding small-molecule:IDP interactions. The findings have solid support through examples underscoring the role of aromatic interactions. While predicted binding sites remain coarse, validation was done on a total of 10 IDPs at varying depths. The method builds on the authors' previous work and, with ad hoc modifications, is poised to benefit this emerging field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107470.3.sa1](https://doi.org/10.7554/eLife.107470.3.sa1)

Summary:

The authors developed a sequence-based method to predict drug-interacting residues in IDP, based on their recent work, to predict the transverse relaxation rates (R2) of IDP trained on 45 IDP sequences and their corresponding R2 values. The discovery is that the IDPs interact with drugs mostly using aromatic residues that are easy to understand, as most drugs contain aromatic rings. They validated the method using several case studies, and the predictions are in accordance with chemical shift perturbations and MD simulations. The location of the predicted residues serves as a starting point for ligand optimization.

Strengths:

This work provides the first sequence-based prediction method to identify potential drug-interacting residues in IDP. The validity of the method is supported by case studies. It is easy to use, and no time-consuming MD simulations and NMR studies are needed.

Weaknesses:

The method does not depend on the information of binding compounds, which may give general features of IDP-drug binding. However, due to the size and chemical structures of the compounds (for example, how many aromatic rings), the number of interacting residues varies, which is not considered in this work. Lacking specific information may restrict its application in compound optimization, aiming to derive specific and potent binding compounds.

Comments on revised version:

I'm satisfied with the authors' response and the public review does not need further changes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107470.3.sa2](https://doi.org/10.7554/eLife.107470.3.sa2)

Summary:

In this work, the authors introduce DIRseq, a fast, sequence-based method that predicts drug-interacting residues (DIRs) in IDPs without requiring structural or drug information. DIRseq builds on the authors' prior work looking at NMR relaxation rates, and presumes that those residues that show enhanced R2 values are the residues that will interact with drugs, allowing these residues to be nominated from the sequence directly. By making small modifications to their prior tool, DIRseq enables the prediction of residues seen to interact with small molecules in vivo.

Strengths:

The preprint is well written and easy to follow.
