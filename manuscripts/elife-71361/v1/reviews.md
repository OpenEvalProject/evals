# Peer review - Round 1

Editors:
- Stephen CJ Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71361.sa0](https://doi.org/10.7554/eLife.71361.sa0)

The authors generated embryoid bodies (EBs) from induced pluripotent stem cells (iPSCs) using a strong mixed-pool study design and performed scRNA-seq profiling. From this data, they identify dozens of cell types and infer differentiation trajectories that align well with known developmental gene expression dynamics. This system is likely to be a good platform for larger eQTL studies that interrogate new cell states.


---

# Peer review - Round 1

Editors:
- Stephen CJ Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71361.sa1](https://doi.org/10.7554/eLife.71361.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Human embryoid bodies as a novel system for genomic studies of functionally diverse cell types" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There seems to be a disconnect between what the study should be about and what it is about. Consequently, the message is a bit confusing, and the relevance of the findings is not so clear. The abstract and introduction are both focused on the potential use of EBs for the mapping of genetic variants affecting gene expression. However, the current manuscript is not an eQTL mapping study, but rather a characterization of EBs by single cell RNA-seq. It would be important to write the abstract, Introduction and title in order to make them more relevant to the data presented. For example, a major difficulty for the authors is the identification of different cell types, this should be discussed in the Introduction, rather than the difficulty in mapping genetic variants.

2) line 104: "we found that every replicate in our experiment, regardless of the individual, includes cells from all three germ layers (Figure 1E, Figure 1G)".

Actually, Figure 1G shows that all 18858 samples contain almost exclusively pluripotent cells (cluster 0). More in general, the characterization of the embryoid bodies used for the study is insufficient. The entire study is based on the analyses of embryoid bodies collected after 3 weeks, generated from 3 iPS cell lines. However, 1 line has clear differentiation defects, or that embryoid bodies differentiation experiment was problematic.

Although this reviewer appreciates that the focus of the study is the generation and analysis of single cell data, if the biological material analysed is of poor quality, the entire study could be questioned. To address this point the authors should perform additional experiments (immunostaining, qPCR) at different days of embryoid body differentiation to make sure that the procedure is correct, that all lines can efficiently differentiate. If they confirm with independent techniques that the 18858 line is almost unable to differentiate, I would suggest to remove it from the analyses, as it simply is a faulty line that cannot be called pluripotent and would not be used by others. For example, the conclusions of lines 324-325 "Replicates of 18858 often cluster together and rarely clustered with the other individuals, suggesting that not only did 18858 have poor differentiation efficiency, but cells that did differentiate show a distinct pattern of expression dynamics" would suggest that such line is problematic and should not be used.

3) With so few samples multiplexed together, demuxlet may not be able to detect all likely doublets. It may be helpful to run an independent doublet finder on the pass-QC cells to make sure there are no same-sample doublets (that demuxlet would miss).

Reviewer #1:

Rhodes and colleagues generated a dataset of single cell RNA-seq of embryoid bodies from 3 iPS cell lines and analysed them with the aim of identifying different cell type and also to partition the variance among biological and technical. The authors propose also to use in the future such system to map genetic variants affecting gene expression, but this interesting aspect is not fully explored in the current manuscript.

The different strategies used to identify different cell types in the dataset are very interesting and could be used for the study of organoids or other tissues by single cell RNA-seq.

The data and analyses pipelines could be useful to other colleagues, but some points need to be clarified.

In line 104: "we found that every replicate in our experiment, regardless of the individual, includes cells from all three germ layers (Figure 1E, Figure 1G)".

Actually, Figure 1G shows that all 18858 samples contain almost exclusively pluripotent cells (cluster 0). More in general, the characterization of the embryoid bodies used for the study is insufficient. The entire study is based on the analyses of embryoid bodies collected after 3 weeks, generated from 3 iPS cell lines. However, 1 line has clear differentiation defects, or that embryoid bodies differentiation experiment was problematic.

Although this reviewer appreciates that the focus of the study is the generation and analysis of single cell data, if the biological material analysed is of poor quality, the entire study could be questioned.

Reviewer #2:

Here the authors generated embryoid bodies (EBs) from iPSCs from three individuals, with three replicates each, and performed scRNA profiling yielding a total of 42,488 cells. The QC performed to get this collection of cells is strong, especially in using the demuxlet approach. From this data, they identify dozens of cell types and infer differentiation trajectories that align well with known developmental gene expression dynamics. They propose this system is therefore an ideal platform for larger eQTL studies.

Much of the introduction motivates this study by using GWAS and eQTL studies and their corresponding gaps. The idea is to capture unexplored cell states using the EB model and in a later study scale up to enable eQTL scans. Thus, the EB platform should represent convincingly novel cell state space compared to existing data. The pseudotime results seem to indicate this with concordance across reference markers for three different lineages. The power calculations are nice to see, but are an exercise in setting expectations for a future study. Overall, this is a strong paper that represents the initial survey of a potentially exciting eQTL platform.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Human embryoid bodies as a novel system for genomic studies of functionally diverse cell types" for further consideration by eLife. Your revised article has been evaluated by Patricia Wittkopp (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The addition of five more samples to bolster the conclusions observed in the initial three samples is good. However, these additional five samples are not mentioned in the introduction (only the original three are mentioned) and the new results are only presented in supplementary figures. This presents the odd scenario in which the main figures depict less samples (three) than the supplementary figures (five). We therefore recommend combining data from all samples and presenting in main figures, whenever possible. Further, the GEO accession (GSE178274) looks like it only includes the initial three samples. We recommend sharing all data and request that the GEO accession be updated to include the five additional samples (all eight samples total).
