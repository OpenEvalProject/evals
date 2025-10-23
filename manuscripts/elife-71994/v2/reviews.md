# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71994.sa0](https://doi.org/10.7554/eLife.71994.sa0)

In this revised manuscript, Noureen and collaborators benchmark five methods that are used in single-cell RNA sequencing data analyses, including single sample gene set enrichment analysis (ssGSEA), Gene Set Variation Analysis (GSVA), AUCell, Single Cell Signature Explorer (SCSE), and a newly developed method, Jointly Assessing Signature Mean and Inferring Enrichment (JASMINE). The authors test these in distinct cancer datasets and conclude that caution should be exercised when using bulk sample-based methods in single-cell data analyses, and cellular contexts should be taken into consideration. As a rapidly developing field in need of method benchmarking, we believe that this paper will be of great interest to the bioinformatics and single-cell data analysis communities.


---

# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71994.sa1](https://doi.org/10.7554/eLife.71994.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Signature-scoring methods developed for bulk samples are not adequate for cancer single-cell RNA sequencing data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Leng Han (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In this manuscript, Noureen and collaborators benchmark four methods that are used in single-cell RNA sequencing data analyses, including single sample gene set enrichment analysis (ssGSEA), AUCell, Single Cell Signature Explorer (SCSE), and a newly developed method, Jointly Assessing Signature Mean and Inferring Enrichment (JASMINE). The authors test these in distinct cancer datasets and conclude that caution should be exercised when using bulk sample-based methods in single-cell data analyses, and cellular contexts should be taken into consideration. Although interesting and informative, reviewers have raised a number of essential considerations that need to be addressed before publication.

Essential revisions:

Major Points

1. A reviewer comments, "The main analysis performed by the authors was identifying gene sets that significantly distinguish between cancer cells and the rest of the cells in the tumor. This a problematic comparison, since the cancer cells are epithelial cells (in most of the studies used) and the "normal" cells are stromal cells, mostly immune. Those are not comparable "normal" cells, and therefore it is expected that all immune-related pathways will be significant. The authors find much more down-regulated gene sets in ssGSEA compared to the other methods, but why are they wrong? If they are all immune related, I would actually conclude that ssGSEA is better than the other methods." They continue, "The comparison of cancer cells to normal microenvironment cells is meaningless. If looking at cancer, a relevant comparison would be cancer cells and normal adjacent cells. But cancer in general is not the best, as there would be way too many significant signatures, and its hard to understand what makes sense and what not". – Can the authors address this crucial observation please?

2. Can the methodology by which each method identifies signatures be explained? This would help identify why these methods perform differentially. Specifically, reviewers strongly suggest understanding what in ssGSEA makes it output different results. Gene dropouts could be the root cause, but this is something that needs proof. Empirically, reviewers suggest that this can be studied by comparing different scRNA-seq methods with different gene dropouts rates – compare 10X to SMART-seq. Do the authors have an idea of how this affects results?

3. The new method the authors propose (JASMINE) is not thoroughly explained and includes formulations which, in a reviewer's evaluation, lead to unintended mathematical behavior and hamper interpretation. Can the explanation on this method be expanded, please? Specifically, reviewers have raised the following points:

a. The four variables (a,b,c,d) considered when calculating the odds ratio make sense. However, the authors claim that "For smaller signatures b can be occasionally 0. In that case we replace it with 1." In a reviewer's words, "this is not a coherent and principled approach. I recommend the authors reconsider the mathematical formulation of this quantification to avoid the necessity of this unprincipled workaround."

b. A reviewer commented that "It is not clear why the average is the best way to combine the Vmean and OR to obtain the JASMINE score". Can this be specified, please?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Signature-scoring methods developed for bulk samples are not adequate for cancer single-cell RNA sequencing data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Leng Han (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In this revised manuscript, Noureen and collaborators benchmark five methods that are used in single-cell RNA sequencing data analyses, including single sample gene set enrichment analysis (ssGSEA), Gene Set Variation Analysis (GSVA), AUCell, Single Cell Signature Explorer (SCSE), and a newly developed method, Jointly Assessing Signature Mean and Inferring Enrichment (JASMINE). The authors test these in distinct cancer datasets and conclude that caution should be exercised when using bulk sample-based methods in single-cell data analyses, and cellular contexts should be taken into consideration. The majority of the reviewers have found the answers to their initial points to be thorough and satisfactory, and so we would only ask the authors to address the points of one new reviewer, who replaced a previous reviewer for this round of revisions.

Essential revisions:

1. It is unclear how calibrated any of these methods are from the analysis presented in this manuscript. To help clarity, please address:

a) Can the authors please detail, in the Methods section, which thresholds are used on each program?

b) Is any test statistic is derived from the JASMINE method?

c) How is the final statistic is derived? That is, what is the range that the statistic is scaled by? In particular, in the eyes of a reviewer, the math for Vmean is unclear. They write, "As written, it is computed only over a fixed index g? The range on the sum is a bit confusing as well. Shouldn't it be over all the cells? If I were to guess, Vmean appears to be Vmean = \sum_{g=1}^{m}\sum_{c=1}^{total cells} R_{g,c}/(m*N). Is this correct?". Please clarify these points in the Methods section.

2. This manuscript infers that the main advantage of methods specific for single-cell data is to account for dropouts. However, in the view of a reviewer, the work presented here does not explicitly compare the differences between the bulk and single-cell methods, and they note that there might be factors that influence the results besides dropouts in real data. They argue that it is inconclusive to attribute poor performance of bulk methods to dropouts, especially when there is only one bulk method included in the analysis. For example, it is unclear how the authors ran ssGSEA, as there are some missing details in the Methods section. In particular, it is common practice to 'pre-filter' RNA-seq data before running any analysis on it. Did the authors do this for the real data analysis? Please add an introduction to each method, and add the details missing so readers can recapitulate the test conditions.

3. From Figure 1D, the authors reveal that the non-cycling tumor cells exhibit higher scores than non-cycling normal cells by ssGSEA. However, it is also noticeable that ssGSEA scores have a much higher variance than the other three methods, and results from SCSE and AUCell scores do not show a significant difference between cycling and non-cycling cells. Are there any explanations and/or intuition for such a result?

4. In the "Dropouts affect ssGSEA scores" section (Line 167), the "dummy expression matrix of 1000 genes and nine columns" is not clearly described. Is it for each cell? Is the ranking of genes the same for each dropout rate? Besides, Figure 3B is not fully explained: Could the authors please explain why the black line has a curvy feature towards the end of x axis while the blue line is linear? How about other dropout rates? There should be nine lines in the figure according to the matrix.
