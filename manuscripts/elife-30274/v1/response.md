# Author response - Round 1

Authors:
- L Michelle Lewis
- Meredith C Edwards
- Zachary R Meyers
- C Conover Talbot ([ORCID: 0000-0002-3758-2425](https://orcid.org/0000-0002-3758-2425))
- Haiping Hao
- David Blum
- Elizabeth Iorns ([ORCID: 0000-0002-1210-2309](https://orcid.org/0000-0002-1210-2309))
- Elizabeth Iorns
- Rachel Tsui
- Alexandria Denis ([ORCID: 0000-0002-1210-2309](https://orcid.org/0000-0002-1210-2309))
- Nicole Perfito
- Timothy M Errington ([ORCID: 0000-0002-4959-5143](https://orcid.org/0000-0002-4959-5143))

## Response text

DOI: [10.7554/eLife.30274.016](https://doi.org/10.7554/eLife.30274.016)

Essential revisions:

1) The paper of Lin et al. led to a great controversy in the c-Myc field, including the labs of Martin Eilers and Bruno Amati, because it ignored that c-Myc also activates inactive genes and represses active genes. Both labs published 2014 two papers back to back in Nature correcting this biased view of the Lin paper. The biased view of the Lin paper is the result of the definition of small genes sets for the analysis and this issue needs to be explicitly discussed in the reproducibility study.

We agree that the small gene set analyzed in the original study and this replication attempt is more biased than a comprehensive analysis of all genes. We also agree that dichotomizing gene expression (which is a continuous variable) into active and silent genes has additional negative consequences. We have expanded the manuscript to discuss these issues and are including additional supplemental figures that present the gene expression results on a continuous scale, instead of only segmented into silent and active genes. Thus, while this replication study is prone to the small gene set, due to replicating the design of the original study, the additional figures provide additional means to assess the impact c-Myc induction has on gene expression.

2) Expression levels of c-Myc are much lower than those of the original study, although the changes of c-Myc expression are in the same direction as the original study (subsection “Total RNA levels following c-Myc overexpression”). Can the authors please discuss this issue?

Thank you for raising this question. We have expanded the section highlighted to discuss some potential factors that might account for this difference.

3) In this study, 580 silent genes were identified with expression level less than 0.5 transcript/cell with a median expression of 0.032. In the original study, 514 genes were identified as silent genes with a median expression of 0.00. If I understand correctly, the current study uses different criteria for a gene to be classified as silent gene. I am curious whether there is a rationale for using 0.5 transcript/cell as the cutoff. In addition, it would be interesting to know how many silent genes are common between the two studies, and how many active genes are common between the two studies (subsection “Digital gene expression following c-Myc overexpression”, first paragraph). The extent of overlap of genes might play a role on some of the inconsistent results between two studies, as mentioned in the meta analysis section (subsection “Meta-analyses of original and replicated effects”, last two paragraphs).

Both studies used the same criteria to classify a gene as silent (less than 0.5 transcript/cell) and active (greater than 1 transcript/cell) at time 0 hr. The reason for the different number of genes, as well as the median expression at time 0 hr, is because the original study reported a majority of the silent genes as having an expression of 0.00 transcript/cell. We have revised the text to clearly state that the same criteria were used. We are not aware of what the rationale is for using these cutoffs, as it was not included in the original study. As stated above in response to comment 1, there are also negative consequences of dichotomizing continuous variables. To provide another means of displaying the data, we included additional supplement figures to illustrate the distribution of gene expression of all genes analyzed at the different times (Figure 2—figure supplement 2).

We agree that the extent of overlap of genes between the two studies (and the two lots tested in this replication attempt) are of interest. We analyzed what percent of genes were common between the different studies for active and silent genes and have included this in the revised manuscript. There was 88.8% commonality for active genes between serum lot one in this replication attempt and the original study (90.1% for serum lot two) with 96.4% commonality for silent genes between serum lot one in this replication attempt and the original study (95.7% for serum lot two).

4) The authors should make a R package with a R markdown file and all the associated data.

We agree that sharing the Rmd file and associated scripts and data are important. We used the OSF to create a project that stores all files/scripts/methods associated with this study and have a function so the associated data and scripts are downloaded when knitting the Rmd file. This will work now while the project is private as well as when the project, with all the associated files, is made public. The location of the Rmd file is also included in the Materials and methods section of the manuscript (https://osf.io/vdrsh/) and we’ve included it as a ‘Source code file’ during resubmission.
