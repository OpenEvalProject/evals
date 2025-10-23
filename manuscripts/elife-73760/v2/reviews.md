# Peer review - Round 1

Editors:
- Aleksandra M Walczak, https://ror.org/02feahw73 CNRS LPENS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73760.sa0](https://doi.org/10.7554/eLife.73760.sa0)

This paper aims to address the current gap in the efficient analysis of large-scale multiparameter flow cytometry and other datasets. The authors offer a software toolkit with an efficient algorithm for comparing numerous samples at once. The study is well presented and is relevant to single cell analysis research.


---

# Peer review - Round 1

Editors:
- Aleksandra M Walczak, https://ror.org/02feahw73 CNRS LPENS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73760.sa1](https://doi.org/10.7554/eLife.73760.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Comprehensive and unbiased multiparameter high-throughput screening by compaRe finds effective and subtle drug responses in AML models" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Aik Choon Tan (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please address all the reviewers comments. The reviewers agree it is a strong paper that is well written but certain improvements can still be made. Especially please give the reader more context in the introduction and compare your method with other existing methods.

Reviewer #1:

Comprehensive and unbiased multiparameter high-throughput screening by compaRe finds effective and subtle drug responses in AML models by Hajkariim et al. introduces a pipeline for pre-processing and analyzing data from multiplex flow cytometry and other technologies. Preprocessing steps include algorithms for correcting common sources of bias in such data. Another key feature is a robust approach to measuring cell similarity across samples. Among the strengths are that the manuscript is well-written, the analysis pipeline is well-motivated, and illustrated with apt examples. The similarity measure is very interesting as well.

There are a few weaknesses as well. It is not completely clear to me how this pipeline agrees and disagrees with common practice in the field. References 1-3, cited to document ongoing analytic challenges, are all at least 5 years old. Comparisons to other approaches, including the use Jensen-Shannon Divergence for similarity, make a convincing case that the proposed method is both effective and computationally efficient, but it is not clear if the comparators represent true standard of practice, or mere straw men. Methodologies are complex and can be difficult to follow, especially the similarity measure.

I would like to see the current state of the field described more clearly in the introduction, as context for the current effort. What makes this unique and important today? This type of clustering is common in single cell sequencing analysis, is it also commonly done in multiplex flow etc, maybe with less computationally demanding tools than JSD? If not, why not?

I think I understand how the similarity measure here works, though its hard to follow the details. Its very interesting, but to be honest, I can't decide if I think its a good solution or needlessly complex. The key, as I understand it, is the binning into "relative" expression groups. This is, after all, how 2-dimensional flow data is commonly interpreted – with plots treated as a visual 2 X 2 table, with row and column boundaries existing largely in the eye of the beholder. The methods need to be clearer throughout, esp. this part. It might help to add another author, a third party who has to understand the method from scratch, and who, having not lived with the details as long, might be expected to provide a more user friendly sense of the overall approach.

Reviewer #2:

In this manuscript, Hajkarim et al. developed compaRe, a user friendly software suite (written in R) for analyzing high-throughput, multi-parameter screening data. There are several modules included in the compaRe toolkit, which can be individually invoked to perform specific tasks, such as quality control, bias correction, pairwise comparisons, clustering and data visualization. All of these modules are available as command-line version and a GUI version for users to use in data analysis, visualization and results interpretation. The authors showed the utility of their toolkit in analyzing multiparameter mass and flow cytometric data from AML and MDS patient samples. Through this analysis using compaRe, the authors showed that they can identify patient heterogeneity and drug response profiles. Overall, this is a well organized and written manuscript describing the development of the new compaRe toolkit. The method is clearly described, and the user manual/tutorial is easy to follow. It seems like compaRe will be a useful toolkit for the research community, which is eager for a one-stop pipeline for analyzing high-throughout multiparameter screening data.

et al.

Strengths:

1. All of these modules are available as command-line version and a GUI version for users to use in data analysis, visualization and results interpretation.

2. The authors showed the utility of their toolkit in analyzing multiparameter mass and flow cytometric data from AML and MDS patient samples. Through this analysis using compaRe, the authors showed that they can identify patient heterogeneity and drug response profiles.

3. Overall, this is a well organized and written manuscript describing the development of the new compaRe toolkit. The method is clearly described, and the user manual/tutorial is easy to follow.

4. It seems like compaRe will be a useful toolkit for the research community, which is eager for a one-stop pipeline for analyzing high-throughout multiparameter screening data.

Weaknesses:

1. The current manuscript didn't compare with some other existing programs/software in analyzing flow and mass cytometry data. It will be important to compare compaRe with existing tools, to show the strengths and weaknesses of compaRe with other tools.

2. The authors could think about adding an additional module to integrate other "omics" data (e.g. such as mutational or gene expression/signatures or pathways), this could be useful for doing the clustering step or to identify patients having the same mutational profiles.

Reviewer #3:

Hajkarim et al. implement an algorithm in their presented toolkit compaRe to compare samples based on the similarities of samples, distinct from the more commonly used meta-clustering approaches, such as PhenoGraph, or dimensional reduction with Jenssen-Shannon Divergence analysis. Similarities among samples are calculated based on the proportions of cells within a sample belonging to an n-dimensional "hypercubes" (or "hypergridding" that is actually mass-aware and not blind) that are stratified by expression levels for n number of markers. The authors demonstrate that this method is much more time-efficient, obviates subsampling, and is robust to batch effects. This method is particularly appropriate for large-scale datasets, facilitating the comparison of numerous samples which would be helpful in screening efforts. The manuscript is written and presented well.

Major strengths:

1. The study demonstrates sufficiently strong support for the toolkit's ability to determine similarity across samples and its computing efficiency with Figure 2, an important advantage of this tool.

2. Compared to other approaches, the method is advantageous for identifying groups of samples that may be similar in a very large-scale dataset. CompaRe does not require (or make use of) manual expert annotation of meta-clusters. The workflow is efficient and unbiased.

Major weakness:

A major weakness of the current presentation of the study is that it has not clearly demonstrated the toolkit's utility in exploring specific phenotypes in-depth within a high-parameter dataset. The following are two examples in which this limitation is relevant, and the authors may address this to strengthen this paper, if in fact detailed phenotyping is considered by the authors as an important feature of the toolkit. If not, the authors should revise the manuscript as such.

First, the authors stated that their approach can be used to "optimize true cytometric n-dimensional immunophenotypic characterization" even in the setting of multi-panel workflow. However, the demonstration was based on samples that seem to have predominant phenotypes that are almost mutually exclusive. It is unlikely that this toolkit would be useful for reliable phenotypic characterization in a largely heterogeneous population of cell types, e.g. even in normal peripheral blood, unless a high number of parameters was concurrently acquired within the dataset. This is an inherent limitation. Nonetheless, a revision to demonstrate how compaRe can evaluate specific clusters of phenotypes with biological significance from a high-parameter dataset (20-30 marker cytometry) would be very helpful.

Second, the authors refer to the method's ability to include all rare cell subsets in the analysis, i.e. the ability to forego any subsampling. The work does not, however, demonstrate clearly how the presence of a rare cell subset in a given sample influences its similarity to other samples. Thus, the toolkit's value of being able to include such a rare subset in the analysis remains unestablished. It would be beneficial to include such a test to see whether the algorithm is sensitive to such changes.
