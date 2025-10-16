# Peer review - Round 1

Editors:
- L Stirling Churchman, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54603.sa1](https://doi.org/10.7554/eLife.54603.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript provides substantial value for the splicing community through demonstrating that previous reports of binary splicing in single cells largely result from technical limitations of single-cell RNA-seq (scRNA-seq). Importantly, the findings provide a path forward for future analysis of alternative splicing regulation in single cells.

Decision letter after peer review:

Thank you for submitting your article "Coverage-dependent bias creates the appearance of binary splicing in single cells" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Najar et al. demonstrate that previous reports of binary splicing in single cells largely result from technical limitations of single-cell RNA-seq (scRNA-seq). The authors challenge the rigorousness of prior published conclusions related to the occurrence of "bimodal" splicing among isogenic cells based on single-cell RNA sequencing – bimodal referring to a situation in which individual cells express either one or the other of two mRNA isoforms, with few cells expressing both isoforms. While previous studies observed frequent bimodal splicing, this study concludes that bimodal patterns arise almost entirely from technical limitations of single cell RNA-seq library preparation and sequencing, particularly the limited fraction of mRNA molecules that are captured by these approaches. The authors develop a filtering approach that allows to identify exons that can be accurately analyzed for splicing in single cells.

This manuscript has important implications for the analysis of alternative splicing regulation in single cells. The analyses described are thoughtful and carefully done, the Materials and methods are very clearly described, and the data presented are fairly convincing. However, there are a few issues that need to be addressed for a fully satisfactory treatment of this subject.

Essential revisions:

1) The authors analyze five previously published scRNA-seq datasets (Chen, Lescroart, Trapnell, Song and Fletcher). The authors should explain why these specific datasets were chosen, and the analysis should be extended to the dataset described in Shalek et al., 2013), which was the first report of widespread bimodality in splicing. A table should be included listing how many examples of bimodal splicing were reported in each original paper, how many examples pass the authors' filters, and how many of these are bimodal. In the examples shown in Figure 3F and J, bimodal splicing appears to occur between cells in different states but not between cells in the same state. Additional discussion should be included related to the fundamental issue of whether or not the authors' analysis supports the existence of any authentic examples of bimodal splicing in isogenic cells which are in the same cell state.

2) A few other sources of variability that could impact the inference of splicing patterns in individual cells should be considered by the authors:

a) "We assume that in each cell, the expected number of reads covering a splice junction is the same as the number of reads expected to cover each nucleotide." This ignores the fact that alternative splicing junctions may have a lower fraction of mappable, because the exclusion junction shares sequence with each of the inclusion junctions, potentially yielding an increased frequency of multi-mapping (or mis-mapping) of reads deriving from alternative isoforms. How does this phenomenon impact detection of bimodal splicing?

b) "We assume that the distribution of reads is expected to be uniform across the transcript." This is another assumption that needs to be explored, since the density of RNA-seq reads along transcripts is notoriously variable. The authors could model the empirical variability in read density along constitutive portions of transcripts in each dataset and apply this model to address how this variability impacts inference of splicing levels.

c) Mammalian gene expression is intrinsically bursty (e.g., PMID 30602787). The authors should discuss whether their analysis captures this effect or how burstiness might impact splicing detection.

d) The amount of pre-mRNA varies across genes and conditions in scRNA-seq datasets (e.g., PMID 30089906). How might this variability influence the results?

3) The authors' validation of their filtering procedure is underdeveloped. The main approach is based on the intuition that genes with truly bimodal splicing should display a higher degree of coregulation, for which the covariance structure of the data is used as a proxy. In Figure 3I, some of the controls are not discussed in the text. Furthermore, the random control appears to perform nearly as well as the true filter in the Trapnell and Song datasets, while in the Chen dataset it is not clear that the filtering leads to much improvement compared to no filter. If this line of argument is to be pursued, a more rigorous analysis and interpretation of the filter's performance relative to controls (perhaps relating to cell subtypes) is needed in the text. Below are specific questions regarding this analysis:

a) In Figure 3I, the authors observe that "the combined filter recovered more evidence of co-regulation than the simple read-based filter". However, the difference between the combined filter and the random filter is not very pronounced. Is this statistically significant?

b) Could the difference between the combined filter and the read-based filter result in part from the lower number of observations?

c) In addition, can the authors justify why this analysis was performed on only 3/5 datasets?

d) It would be helpful to indicate in the text how many exons pass the filters in each dataset and/or what proportion of exons covered this represents.
