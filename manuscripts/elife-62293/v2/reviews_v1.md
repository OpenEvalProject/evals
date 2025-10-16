# Peer review - Round 1

Editors:
- Jing-Dong Jackie Han, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62293.sa1](https://doi.org/10.7554/eLife.62293.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work presents a highly refined and validated global aging (GAG) score, as well as establishing category-specific murine aging genes, which together provide a comprehensive angle to understand aging at different scales. The GAG score enables capture of tissue-cell-type specific effects, setting more focus on the tissue- and cell type-specific aging status, and enables assessment of the general aging status.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Mouse Aging Cell Atlas Analysis Reveals Global and Cell Type Specific Aging Signatures" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lei Hou (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Reviewer #1:

The proposed studies aims to in-depth analyses of aging transcriptomic signatures in mouse both at tissue-cell type and global level from single-cell data. It is an important perspective to understand aging not only for specific tissue-cell type but also the differences among them. One of the main contributions is a novel aging score metric, based on which aging process is compared across tissue-cell type pairs. However, I have several concerns about this aging score and would prefer a revision from the authors.

1. I am confused about the method you used to calculate the aging score.

In main text, the aging score is calculated for each cell, then averaged at tissue-cell type level, and regress out age and sex; while in method for each cell, after adjusting the background, age and sex are regressed out from the raw aging score, then the scores are averaged at tissue-cell type level.

2. For either case, the name of the aging score is misleading, as the residuals after regressing out age and sex, it is not a predictor of aging. Instead, it represents how a specific tissue-cell type is off from the average aging effect across all conditions.

3. If it is actually what authors would love to show, the random effect in each tissue-cell type should be taken into consideration: for cells from different tissue-cell type, their intercepts of the regression model exp~ age+sex+ age*sex could be different, and thus a linear mixed model should be more appropriate in this case. It may explain why in supplementary Figure 9, aging scores from immune cells compared to other cell types of this study show even weaker correlation with that based on blood samples from Peters' work (pvalue 5.4e-4, 0.08, compared to 1.8 e-5).

4. For comparing aging effects purpose, I don't understand why aging scores of cells from the young time point should be included in the final aging score for each tissue-cell type. Firstly, it doesn't represent the aging effect if you also include scores from young cells; Secondly, the scores for each tissue-cell type may be confounded by different percentages of young cells.

Reviewer #2:

In the manuscript titled "Mouse Aging Cell Atlas Analysis Reveals Global and Cell Type Specific Aging Signatures", Zhang and et al. systematically explored the aging-related genes in 76 tissue-cell types from 23 tissues in 10 male and 6 female mice from the Tabula Muris Senis single-cell transcriptomic dataset. The authors used a linear regression model to identify a set of up-/down-regulated aging-related genes, found a general down-regulation of gene expression in most tissue-cell types and revealed sets of aging regulated genes that shared by different tissue-cell types or that specifically enriched in some tissue-cell types. The authors further leveraged the average expression difference in the up- and down-regulated global aging genes, and proposed an aging score defined as a correlated factor that determines the change in different tissue-cell types without effects of age and sex. The manuscript is well organized, the results presented are impressing and the conclusions are pretty attractive. However, the data analyses need substantial revisions to draw any convincing conclusions, specifically, I have a list of concerns as below:

1. General concerns:

a. The sample size may be insufficient (10 males, 6 females) to build linear regression model to determine reliable correlations between certain gene expression with the two factors of age and sex in single-cell level.

b. Since the TMS datasets are curated from a collaboration program with different labs, confounding batch effects should be explicitly evaluated and resolved before any further analysis.

c. Though many platforms and technologies may have built-in strategies to deal with uncertainty of RNA copy number, normalization of single cell transcriptome are still highly recommended in the data processing to control technical inconsistency and calculation of DGE. The MAST package is aware of the problem and use the CDR calculation as alternatives of normalization, which, however, was omitted by the authors when using the package.

d. Beside the validation of the aging score, parallel analyses of droplets datasets should be performed in the same tissue-cell types to validate their findings.

2. Identification of aging-related genes:

a. In the linear model of DGE with age and sex, it is unclear what the observations were in the model, whether the statistical test performed in individual cells across different tissue-cell types; how to deal with missing data; and how to control the effect of cell numbers if the tests are performed in tissue-cell types level.

b. FDR calculation is highly depend on simultaneous consideration of comparisons in multiple tests. It is also unclear what the exact number of comparisons considered in each FDR test.

c. Figure 1B shows number comparison between up- and down-regulated genes related to age regardless of sex, however the authors should clarify whether the sex has effect on the result and a new figure of the comparison considering sex is highly recommended.

3. Tissue-cell level global aging markers:

a. The definition of global aging genes is based on an arbitrary cutoff of half of tissue-cell types without considering the data structure, tissue-cell similarities or proportions of cells determined in mice, which may be conceptually confusing if change happened as data accumulating and new tissue-cell types identified.

b. For those up- or down-regulated genes in specific tissue-cell types, a pickup top 20 genes is not convincing and it is necessary to evaluate the significance of the involvement of those genes in shared biological progresses or functions.

4. Aging score based on global aging genes:

a. The aging score is defined based simply on the potential determinants in the average expression changes between up- and down-regulated global aging genes without the effects from age and sex, which is not intuitively straightforward and confusing, given the ambiguous involvement in biological functions or regulations of the list of genes.

b. The authors claim that aging score is correlated with the cell turnover but failed to show any solid evidence.

5. Tissue-cell-specific aging genes:

a. The authors grouped tissue-cell types into 6 categories based on annotated functionality, and then identified over-represented genes in each category as tissue-cell-specific aging genes. I am wondering why not define the tissue-cell-specific aging genes in original tissue-cell types; the arbitrary grouping may be inaccurate and inevitably reduced the resolution of the tissue-cell specificity.

b. Again, the author failed to establish solid connection between these tissue-cell-specific aging genes and the tissue-cell specific functions or aging progress, which makes the result less reliable.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Mouse Aging Cell Atlas Analysis Reveals Global and Cell Type Specific Aging Signatures" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lei Hou (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

You have made great efforts to refine and validate their global aging (GAG) score, as well as establish category-specific aging genes, which together provide a comprehensive angle to understand aging at different scales. Still, we have some concerns as below.

Essential changes:

1. GAG score aims to capture common aging states across all cell types. Though authors tried to validate it from different datasets, it would be more convincible if they could show how well GAG score is fitted for GAG score ~ chronological age + sex + tissue-cell-type with both scatter plot and proportion of explained. Alternatively, will it fit better for GAG score ~ chronological age + sex + tissue-cell-type + tissue-cell-type * chronological age, where tissue-cell-type could also affect the slope of age.

2. GAG score, due to its nature of capturing global pattern, may lose the power to identify the aging state of those cell types with the specific program associated with aging. It may be the reason for observations mentioned in line 135-138 and 146-148, specifically in Sup.Figure 11, for Brain.Non-Myeloid. neuron, liver.hepatocyte, mamary_glad.bascal cells, cells of 24 months even have a smaller GAG score than cells of 18 month. However, This may be potentially explained by catogery-specific aging genes later identified. Would tissue-cell type with more category-specific aging genes be more likely to show this heterogenous aging state pattern? Further, an accurate aging score for a specific cell type may be better consisting of two parts, global aging score, and specific aging score.

3. Last session of tissue-level section is not interesting to me, since differential genes at cell type are already accurately defined, and there's no reason to go back to bulk differential signal, which may be confounded by other factors such as cell-type proportions.
