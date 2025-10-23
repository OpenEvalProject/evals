# Peer review - Round 1

Editors:
- Yousin Suh, Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59201.sa1](https://doi.org/10.7554/eLife.59201.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Levine et al. present a DNA methylation-based clock trained on rat chronological age, using longitudinal whole blood samples from a cohort of male rats. This represents the first clock for predicting rat aging, which is an important advance in the aging research field as rats offer important practical advantages over mice, particularly the ability to draw recurring sizable blood samples without harm to the animal. This longitudinal sampling, combined with the proposed model, will enable longitudinal studies of aging biology and potential evaluation of interventions.

Decision letter after peer review:

Thank you for submitting your article "A rat epigenetic clock recapitulates phenotypic aging and co-localizes with heterochromatin" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Peter Laird (Reviewer #1); Bjorn Schumacher (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The manuscript by Levine et al. presents a DNA methylation-based clock trained on rat chronological age, using longitudinal whole blood samples from a cohort of male F344 rats. This represents the first epigenetic clock for predicting rat aging, and thus a significant extension of what have been defined in mice and humans. In particular, rat models provide a number of advantages over mouse models especially with respect to the possible recurring measurement of blood profiles without harm to the animals. The authors show that the rat DNAmAge derived from the longitudinal sampling and a Principal Component-based modeling also correlates with phenotypic aging in mice and rejuvenation-related phenotypes conferred by an age intervention such as calorie restriction in mice as well as in fibroblast-derived iPSCs. This longitudinal study design, combined with the proposed model, is powerful with the demonstrated potential to evaluate the effects of aging interventions. Thus this study will certainly be of broad interest to the community of researchers studying the biology of aging. However, as detailed below, a number of concerns were also raised, relating in large part to insufficient clarity in the current version with respect to the authors' presentation of methods and data.

Essential revisions:

1) Abstract:

Is the number behind physical functioning a p-value?

2) Subsection “Age differences in DNAm”

i) There are 27 age groups; they chose 32 animals for the test set, the exact age distribution should be indicated.

ii) They should mention the panel number in the text, not just Figure 1.

iii) The order of the panels is different from the appearance in the text. Reorder.

iv) Paragraph three, a plot for the first principle components, maybe also color coded for age, should be included so that the reader can see it for themselves.

v) The statement “PC1 captures 6.7 % of variance” is not directly clear from the plot and should instead to visible in Figure 1A. On the plot it looks like PC1 is at ~0.48. Is the y-axis here in percent? Also the axis in the plot should be changed so that the axis spans the whole data.

vi) The authors mention that PC1 explains 87 % of the variance in age, but it is not clear how this was computed. It also was not really clear how they computed this (Figure 1C). Clarify.

vii) They used regression to get the relationship between the PC1 and age. But then how did they use this to compute the age in the test sample? The authors should explain this further.

viii) In the figure legend they write: “multiplying the coefficient by PC1 and adding the constant in the test sample”. Do they mean they multiply the coefficients of the regression line by PC1? Which constant do they mean and how and what exactly do they add?

3) Materials and methods:

i) It is not clear what the text "Next PCA was run using the rats in the training set and elastic net was used to train and predictor of age based on PCs rather than individual CpGs" means. It sounds like the authors used all PCs instead of just PC1. Clarify.

ii) They mention that including more PCs into the predictor does not improve the prediction. Show a plot or table for this claim.

iii) For the DNAm associations with FACS and Phenotypic variables:

a) Table S1 in Supplementary file 1: Explain what exactly the β coefficient is (the degree of change in the outcome variable, i.e. DNAmAge, for every unit of change in the predictor variable, i.e. Age, or Pheno PC1,.)

b) Why is the β coefficient between phenotypic PC1 and DNAmAge increasing, when taking more PCs of the FACS PCA into account? Shouldn't it decrease? Clarify.

c) In Figure 1—figure supplement 2 and Table S1 in Supplementary file 1, include the original data.

4) Validation in C57BL/6 Mice:

i) A correlation line in Figure 2 (as they did before) should be added.

ii) Figure 2—figure supplement 1: Verify whether the y-axis label is correct. It might be the difference between the true and the DNAmAge, and not the DNAmAge itself.

5) Deconstruction of epigenetic aging measures:

i) It would be interesting to do the same analysis for the whole rat dataset, instead of the smaller rat-mice dataset.

ii) Why did they choose a power of 1? Usually the smallest power is chosen so that the network is scale-free.

iii) In the text they write Figure S3, but mean S4.

iv) The order of the text and the panels in the figure is not the same.

v) Should the axis be scaled the same?

vi) The correlation coefficients for the pink module in the text and the plot are different

vii) They write “using a fully adjusted linear model ([…] Table S2)”, but Table S2 is not for the specific modules.

viii) They reference the table again, maybe they forgot to include the right table? otherwise this is confusing.

6) Genomic Features of Methylation Modules:

i) Include a figure for the overlaps.

ii) What supplemental material?

7) Discussion:

i) Paragraph one: Horvath's recent paper: Reversing age: dual species measurement of epigenetic age with a single clock (biorxiv 08.05.2020) reports an epigenetic aging clock in rats and should be cited here accordingly.

ii) Paragraph six: “using PCA, rather than elastic net”: in the Materials and methods they write: “PCA was run using the rats in the training set and elastic net was used to train and predictor of age based on PCs”, so it is a combination of both.
