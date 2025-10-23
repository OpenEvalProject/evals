# Peer review - Round 1

Editors:
- Joaquin M Espinosa, University of Colorado Boulder , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06498.020](https://doi.org/10.7554/eLife.06498.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your work entitled "A distinct p53 target gene set predicts for response to NVP-CGM097, a novel and selective p53-HDM2 inhibitor" for consideration at eLife. Your article has been favorably evaluated by Sean Morrison (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This manuscript by Jeay et al. reports the discovery of a 13-gene signature that can predict the sensitivity of tumor cell lines and patient-derived tumor xenografts to small molecule inhibitors of the p53-MDM2 interaction with great accuracy, sensitivity and specificity. The manuscript is conceptually simple yet of very high impact.

The current manuscript not only reports the discovery of two novel inhibitors of the p53-MDM2 interaction, but also describes an experimental tour-de-force to identify the much-needed biomarker. These efforts lead the authors to identify a 13-gene signature that can predict the cellular response in vitro and in vivo, including patient-derived xenografts, with great accuracy, sensitivity and specificity. Remarkably, the gene signature is composed of 13 known direct transcriptional targets of p53 whose expression is strongly elevated in cell lines and tumors prior to MDM2 inhibition. This indicates that the sensitive cell lines harbor a more transcriptionally active form of p53 that 'primes' a fraction of its transcriptional program in proliferating cancer cells. This finding counters the prevalent notion that sensitivity is defined by MDM2 amplification, which would result in very low levels of active p53.

Although the paper does not make great mechanistic insights into p53 biology, its broad applicability makes it of very high impact. If this biomarker works in the clinic, it is likely to profoundly change the course of the current clinical trials and future use of MDM2 inhibitors in cancer therapy. Accordingly, the reviewers agreed on recommending resubmission of a revised manuscript addressing the following major points:

1) It seems like p53WT (mutational status) is a good predictive marker for this compound, why is this information not taken into account when building the naive Bayes classifier? Can the prediction improve when p53 mutational status is taken into account as part of the gene signature? Why not try to build a gene signature based on p53 wild type that is sensitive or insensitive to this compound? It seems like the validation steps of the gene signature are built on the logic that p53 wild type could be used as a feature, as the independent in vitro validation was only performed on the p53WT cell lines, and the PDX models were enriched with p53WT models.

2) The gene selection method based on the Wilcoxon test seems to be a little bit primitive. There are better and more advanced feature selection methods (like lasso type or machine learning approaches). Have the authors tried different approaches and come to the conclusions with the same set of genes? Have the authors tested with different machine learning approaches (e.g. SVM?)

3) The fold-change of the 13 selected genes seems to be modest, some of them even less than 2 fold. Can these changes be validated by other experimental approaches like RT-PCR? It seems like the training of the classifier is based on the full ~52,000 probe sets, not genes. Have the authors found multiple probe sets representing the same genes ranked high in the feature selection step? This may strengthen the inclusion of these genes.

4) How is this gene signature going to translate into a biomarker test in a clinical trial? The hardest part is the RMA normalization of a new sample. In the validation steps, both in vitro and in vivo gene expression profiles were normalized as a batch, and the expression values are normalized with the training set? This is unclear, and how will the authors envision normalizing patient samples? As in a clinical trial, patients will be tested individually, not by batch, therefore, getting the gene expression values normalized to the same scale with the training model needs careful consideration. This is not clearly described in the text.

5) Finally, in the training and testing in vitro cell lines, many of the sensitive cell lines are from the hematopoetic cell lineages, but none of this cell lineage is represented in the PDX Models. How would this affect the predictions of the classifier?
