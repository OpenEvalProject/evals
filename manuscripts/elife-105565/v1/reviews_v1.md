# Peer review - Round 1

Editors:
- Anna Panchenko, Queen's University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105565.3.sa0](https://doi.org/10.7554/eLife.105565.3.sa0)

This valuable work presents an interpretable protein-DNA Energy Associative (IDEA) model for predicting binding sites and affinities of DNA-binding proteins. While the method is convincing, it requires some adaptation for application to different proteins. The IDEA method is available and can be potentially used for predicting genome-wide protein-DNA binding sites.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105565.3.sa1](https://doi.org/10.7554/eLife.105565.3.sa1)

Summary:

Zhang et al. present a methodology to model protein-DNA interactions via learning an optimizable energy model, taking into account a represetative bound structure for the system and binding data. The methodology is sound and interesting. They apply this model for predicting binding affinity data and binding sites in vivo.

Strengths:

The manuscript is well organized with good visualizations and is easy to follow. The methodology is discussed in detail. The IDEA energy model seems like an interesting way to study a protein-DNA system in the context of a given structure and binding data. The authors show that an IDEA model trained on one system can be transferred to other structurally similar systems. The authors show good performance in discriminating between binding-vs-decoy sequences for various systems, and binding affinity prediction. The authors also show evidence of the ability to predict genome-wide binding sites.

Weaknesses:

An energy-based model which needs to be optimized for specific systems is inherently an uncomfortable idea. Prediction of binding affinity is a well-studied domain and many competitors exist, some of which are well used. The usefulness of this method will be a test of time. The methodology is interpretable in a limited sense. The model is dependent on preserved interface geometry which might lead to suboptimal results for novel folds. The model predicts different output for reverse complement sequence (which in reality are the same as far as double helix is concerned). This is unintuitive.

Comments on revisions:

The authors have addressed my points regarding comparisons with existing methods, clarifying discussion terminologies and proper discussion of the existing literature. This resulted in a stronger manuscript with a clearer understanding of applicability.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105565.3.sa2](https://doi.org/10.7554/eLife.105565.3.sa2)

Summary:

Protein-DNA interactions and sequence readout represent a challenging and rapidly evolving field of study. Recognizing the complexity of this task, the authors have developed a compact and elegant model. They applied well-established approaches to address a difficult problem, effectively enhancing the information extracted from sparse contact maps by integrating an artificial decoy sequence set and available experimental data. This has resulted in a practical tool that can be adapted for use with other proteins.

Strengths:

The authors integrate sparse information with available experimental data to construct a model whose utility extends beyond the limited set of structures used for training.

A comprehensive methods section is included, ensuring reproducibility.

The authors provide a well-represented performance comparison between their model and other existing models.

Additionally, the authors have shared their model as a GitHub project, reflecting their commitment to research transparency.

Weaknesses:

The coarse-graining procedure is quite convoluted, but the authors provide reasoning for the proposed scheme. The authors acknowledge discrepancies between data-driven and simulation models.
