# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93695.3.sa0](https://doi.org/10.7554/eLife.93695.3.sa0)

The authors introduce a valuable machine-learning model for predicting binding sites of diverse ligands, including DNA, RNA, peptides, proteins, ATP, HEM, and metal ions, on proteins. The method is freely accessible and user-friendly. The authors have conducted thorough benchmarking and ablation studies, providing convincing evidence of the model's overall performance, despite some imperfections of the comparisons to other methods that arise from intrinsic differences between training methods and data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93695.3.sa1](https://doi.org/10.7554/eLife.93695.3.sa1)

Summary:

The authors aim to address a critical challenge in the field of bioinformatics: the accurate and efficient identification of protein binding sites from sequences. Their work seeks to overcome the limitations of current methods, which largely depend on multiple sequence alignments or experimental protein structures, by introducing GPSite, a multi-task network designed to predict binding residues of various molecules on proteins using ESMFold.

Strengths:

(1) Benchmarking. The authors provide a comprehensive benchmark against multiple methods, showcasing the performances of a large number of methods in various scenarios.

(2) Accessibility and Ease of Use. GPSite is highlighted as a freely accessible tool with user-friendly features on their website, enhancing its potential for widespread adoption in the research community.

Weaknesses:

(1) Lack of significant insights. The paper reproduces results and analyses already presented in previous literature, without providing significant novel analysis or interpretation. However, they show a novel method with an original approach.

The work is useful for the field, especially in disease mechanism elucidation and novel drug design. The availability of genome-scale binding residue annotations GPSite offers is a significant advancement.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93695.3.sa2](https://doi.org/10.7554/eLife.93695.3.sa2)

Summary:

This work provides a new framework, "GPsite" to predict DNA, RNA, peptide, protein, ATP, HEM, and metal ions binding sites on proteins. This framework comes with a webserver and a database of annotations. The core of the model is a Geometric featurizer neural network that predicts the binding sites of a protein. One major contribution of the authors is the fact that they feed this neural network with predicted structure from ESMFold for training and prediction (instead of native structure in similar works) and a high-quality protein Language Model representation. The other major contribution is that it provides the public with a new light framework to predict protein-ligand interactions for a broad range of ligands. It is a convincing outcome of previous efforts to Geometric Deep Learning approaches to model protein-ligand interactions. The authors have demonstrated the interest of their framework with comprehensive ablation studies and benchmarks.

Strengths:

- The performance of this framework as well as the provided dataset and web server make it useful to conduct studies.

- The ablations of some core elements of the method, such as the protein Language Model part, the use of multiple ligands in the same model, the input structure, or the use of predicted structure to complement native structure are very insightful. They can help convince the reader that every part of the framework is necessary. This could also guide further developments in the field. As such, the presentation of this part of the work holds a critical place in this work.

Weaknesses:

- The authors made an important effort to compare their work to other similar frameworks. Yet, the lack of homogeneity of training methods and data from one work to the other makes the comparison slightly unconvincing, as the authors pointed out. Ablations performed by the authors were able to compensate for this general weakness, as well as the focus on several example structures.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93695.3.sa3](https://doi.org/10.7554/eLife.93695.3.sa3)

Summary

The authors of this work aim to address the challenge of accurately and efficiently identifying protein binding sites from sequences. They recognize that the limitations of current methods, including reliance on multiple sequence alignments or experimental protein structure, and the under-explored geometry of the structure, which limit the performance and genome-scale applications. The authors have developed a multi-task network, GPSite, that predicts binding residues for a range of biologically relevant molecules, including DNA, RNA, peptides, proteins, ATP, HEM, and metal ions, using sequence embeddings from protein language models and ESMFold-predicted structures. The reported results showed to be superior to current sequence-based and structure-based methods in terms of accuracy and efficiency.

Strengths

(1) The GPSite model's ability to predict binding sites for a wide variety of molecules, including DNA, RNA, peptides, and various metal ions.

(2) Based on the presented results, GPSite outperforms state-of-the-art methods in several benchmark datasets in terms of accuracy and efficiency.

(3) GPSite adopts predicted structure instead of native structures as input, enabling the model to be applied to a wider range of scenarios where native structures are rare.

(4) The low computational cost of GPSite is beneficial, which enables rapid genome-scale binding residue annotations, indicating the model's potential for large-scale downstream applications and discoveries.

Weaknesses

There are no major weaknesses after the revision.
