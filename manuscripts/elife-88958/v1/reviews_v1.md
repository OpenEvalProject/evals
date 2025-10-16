# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88958.3.sa0](https://doi.org/10.7554/eLife.88958.3.sa0)

In this useful study, a solid machine learning approach based on a broad set of systems to predict the R2 relaxation rates of residues in intrinsically disordered proteins (IDPs) is described. The ability to predict the patterns of R2 will be helpful to guide experimental studies of IDPs. A potential weakness is that the predicted R2 values may include both fast and slow motions, thus the predictions provide only limited new physical insights into the nature of the underlying protein dynamics, such as the most relevant timescale.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88958.3.sa1](https://doi.org/10.7554/eLife.88958.3.sa1)

Qin, Sanbo and Zhou, Huan-Xiang created a model, SeqDYN, to predict nuclear magnetic resonance (NMR) spin relaxation spectra of intrinsically disordered proteins (IDPs), based primarily on amino acid sequence. To fit NMR data, SeqDYN uses 21 parameters, 20 that correspond to each amino acid, and a sequence correlation length for interactions. The model demonstrates that local sequence features impact the dynamics of the IDP, as SeqDYN performs better than a one residue predictor, despite having similar numbers of parameters. SeqDYN is trained using 45 IDP sequences and is retrained using both leave-one-out cross validation and five-fold cross validation, ensuring the model's robustness. While SeqDYN can provide reasonably accurate predictions in many cases, the authors note that improvements can be made by incorporating secondary structure predictions, especially for alpha-helices that exceed the correlation length of the model. The authors apply SeqDYN to study nine IDPs and a denatured ordered protein, demonstrating its predictive power. The model can be easily accessed via the website mentioned in the text.

The authors have adequately addressed the majority of my previous concerns. However, I still wonder if an attempt to fit the individual protein fitting parameter based on temperature and magnetic field strength would be possible. The authors would have 45 data points on which to fit such a parameter, which would only depend on two variables.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88958.3.sa2](https://doi.org/10.7554/eLife.88958.3.sa2)

The revised manuscript adds some new relevant analyses. It still, however, is unclear which timescales of motions the method refers to and there is confusion about whether the model can predict "slower motions". While the authors answer some of my points, others are left unanswered. That is of course the authors' prerogative, and readers will in any case be able to read the reviewer comments. I am not sure it is productive to add further comments at this point.

Below are my comments from the first round of review:

The manuscript by Qin and Zhou presents an approach to predict dynamical properties of an intrinsically disordered protein (IDP) from sequence alone. In particular, the authors train a simple (but useful) machine learning model to predict (rescaled) NMR R2 values from sequence. Although these R2 rates only probe some aspects of IDR dynamics and the method does not provide insight into the molecular aspects of processes that lead to perturbed dynamics, the method can be useful to guide experiments.

A strength of the work is that the authors train their model on an observable that directly relates to protein dynamics. They also analyse a relatively broad set of proteins which means that one can see actual variation in accuracy across the proteins.

A weakness of the work is that it is not always clear what the measured R2 rates mean. In some cases, these may include both fast and slow motions (intrinsic R2 rates and exchange contributions). This in turn means that it is actually not clear what the authors are predicting. The work would also be strengthened by making the code available (in addition to the webservice), and by making it easier to compare the accuracy on the training and testing data.
