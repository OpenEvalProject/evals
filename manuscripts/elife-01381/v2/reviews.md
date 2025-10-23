# Peer review - Round 1

Editors:
- Philipp Khaitovich, Partner Institute for Computational Biology , China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01381.038](https://doi.org/10.7554/eLife.01381.038)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Genetic interactions affecting human gene expression identified with variance association mapping” for consideration at eLife. Your article has been favourably evaluated by a Senior editor, a Reviewing editor, and 2 peer reviewers.

The only substantive concern is that the paper should be re-written because the concepts and methods need to be better explained for non-specialist readers. In particular, it should be made clearer why showing that two loci (SNPs) contributing non-additively to genotype-specific variance is direct evidence of epistasis. There are also presumably specific assumptions in the models, such as the dependence of variance on scale, the type of interaction, or the complex effects of LD, and these should be made clearer.

In terms of methodology, Step 1, the identification of v-eQTL, does not appear to leverage the twin design (“GRAMMAR was used to remove correlations between individuals”) and this should be explained more clearly. Step 2, “Epistasis” does use the twin structure and is based on a LRT comparing linear mixed models with and without an interaction term. What is the form of the interaction term? There are many ways to encode it which can involve more than one parameter for SNPs not in D'=1. Why use a non-parametric test for v-eQTL discovery and then a LMM for interaction? Although the data are quartile normalised, are the squared residuals and what is the effect of outliers? The conditional analysis presumably includes SNPs one-by-one to check the association holds – does imputation uncertainty matter here? Please also clarify why the influence of a second eQTL doesn't have an impact on the result.

In the main text: after identification of v-eQTL “to search for epistasis we scanned the cis windows for a second variant statistically interacting with each of the peak v-eQTL”. It would be helpful to include a mathematical description of the model.
