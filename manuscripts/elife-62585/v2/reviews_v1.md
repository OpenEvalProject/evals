# Peer review - Round 1

Editors:
- Jing-Dong Jackie Han, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62585.sa1](https://doi.org/10.7554/eLife.62585.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The co-profiling of proteomic and transcriptomic changes of kidney aging in genetically diverse mice at different ages generated a rich resource for aging research. The common and unique mRNA and protein changes associated with kidney aging provides a more comprehensive picture of the aging processes.

Decision letter after peer review:

Thank you for submitting your article "Proteomic and transcriptomic profiling reveal different aspects of aging in the kidney" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Steve Horvath (Reviewer #2).

Summary:

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In this work, the authors measured kidney mRNA and protein levels in 188 genetically diverse mice at ages 6, 12, and 18 months. They found age-related changes in both mRNA and protein were associated with increased immune infiltration and decreases in mitochondrial function. In addition, they observed some age-related changes in protein showed no corresponding changes in mRNA. Therefore, the authors concluded that examination of changes in proteins is essential to understand aging processes that are not transcriptionally regulated. Overall the experiments are well designed and provides the research community a new dataset of both gene expression and protein expression data to study murine kidney aging.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Essential revisions:

1) The figure legends were often too brief and did not provide sufficient information to help readers to understand the figure. For example, in Figure 6, it was not clear each dot's meaning, and the figure legend was not very helpful in general.

2) Some of the analyses were not well described. For example, DEseq2 is most commonly used to compare differential gene expressions under two conditions; however, in this experiment, there were three time points. Additional description will be helpful to demonstrate how the trend test was performed and what exactly was tested. It seems that there were way many more up-regulated genes than down-regulated genes from this analysis. However, using a different model, when authors compared gene expression with protein expression, there were comparable numbers of up-regulated genes vs. down-regulated genes. Would non-linear changes be captured by this analysis, e.g., up- regulation in the second time point then down-regulation in the third time point?

3) In the subsection “Age-related changes in Protein Expression”, the authors tried to identify proteins/genes from enrichment categories that were associated with specific cell types as illustrated in Figure 3. However, it is not clear how accurate such cell type inference was. Additional information such as how cell type specific marker genes were derived will be helpful to understand what the authors did to decompose the proteomic changes into cell-type specific changes as suggested in the aforementioned subsection and Figure 3.

4) The authors observed essentially no change in the significance of correlations between protein and age when mRNA expression was considered or excluded from the regression model. Therefore they concluded that the age-related components of change in protein abundance occurred independently of the mRNA. This is not fully anticipated, as I would expect that for some proteins, their age-related changes depend on mRNA. It seems to me that a conditional independence test would be more appropriate, i.e., to test if protein and age are still correlated when condition on mRNA expression.
