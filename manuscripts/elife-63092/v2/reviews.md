# Peer review - Round 1

Editors:
- Genevieve Konopka, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63092.sa1](https://doi.org/10.7554/eLife.63092.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript is an excellent resource for comparing gene expression in dendrites versus soma in hippocampal neurons. It contains important information regarding dendritic RNA localization in the two major classes of neurons.

Decision letter after peer review:

Thank you for submitting your article "Subcellular sequencing of single neurons reveals the dendritic transcriptome of GABAergic interneurons" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Genevieve Konopka as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Eran A Mukamel (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

All three reviewers were very position about this Tools and Resources article and feel that the dataset and approach will be very valuable for the community. This manuscript details the transcriptome of hippocampal neurons at single cell resolution, comparing transcripts in the soma with transcripts in the dendrites. Comparisons of glutamatergic and GABAergic neurons are also carried out.

Essential revisions:

Each reviewer had distinct suggestions for improving the manuscript including additional analyses of the datasets. Please refer to the individual reviews below and address as many of these comments as possible. If a particular comment cannot be addressed, please state the reason.

Reviewer #1:

This manuscript from Perez and colleagues is a great resource for comparing dendritic versus somatic transcripts in hippocampal neurons at single cell resolution. The authors do an excellent job of describing their experimental details, interpretations of the data, associated caveats, and carry out reasonable confirmations of genomic data using smFISH as well as data supporting local protein synthesis in the dendrites of GABAergic neurons. I was excited to see comparisons of dendritic vs. somatic transcripts within individual cells as well as comparisons of dendritic transcriptomes between cell types. The relative lack of differentiation of the dendritic transcriptome between cell types was somewhat surprising and even though careful downsampling and other means were carried out to account for lower depth in these transcriptomes and the authors discuss potential reasons why this may be, I do wonder if future studies with greater depth will confirm these results and/or if such results might be the case in other brain regions. It might be worthwhile for the authors to compare their data to a study published last year that carried out somatic vs. dendritic profiling in hippocampal neurons: Middleton, Eberwine and Kim, 2019.

Although that study did not differentiate between neuronal cell types, presumably one could examine this using the raw data. It should probably be cited in this manuscript as well.

While I am enthusiastic about the manuscript and the data it will provide to the field, there are some issues that could be addressed to improve the manuscript.

1) In the very first figures the authors should describe how many dendrites are from which category of neurons or maybe highlight them with a different color in the UMAP plot (Figure 1C).

2) A potential deep comparison of the dendritic transcriptome of different cell types seemed exciting to me but was only superficially examined. The authors do mention the DEG list between the different groups, but only name a few genes and then validate them. It would be great to discuss the functional consequence of these differences in how the local dendritic transcriptome difference determines the functioning of these cells during signal transmission. Also, when comparing and integrating the data with published tissue scRNA-seq, why not include the dendritic data too? Such comparisons could be important for others in the field to "deconvolute" their scRNA-seq data to look for dendritic-enriched transcripts.

Reviewer #2:

This paper is excellent with a wealth of data. Some points to consider:

1) In the first Results section they look at hippocampal cultures. The control is empty cuts. Could they perform an axon cut as a control?

2) They give the number of transcripts in the dendritic and somatic compartments. Although discussed in the Introduction and later in the manuscript, did they mention the total RNA extracted in each compartment and look for a selective loss of low abundance dendritic mRNAs normalized to total RNA in the beginning of the paper when making the simple comparisons to transcript numbers in the two compartments?

a) It seems one way they addressed the above issue was by down sampling which is certainly reasonable. But could they determine whether dendritic mRNAs are selectively reduced in the mRNAs from the low abundance tail of somatic mRNAs? This analysis performed at some threshold would offer a simple and quick high level look.

3) The work superbly addresses quantitative comparisons-for example in the Poisson generalized linear model, but some greater to attention to functional differences would enhance the paper. This topic is not ignored-they have a section on "function associations" but that section is very descriptive and not completely as satisfying as one would expect for such profound differences and such an interesting problem. In this vein, their data would be very suitable for a bipartite community detection algorithm. It seems some of the points they want to make concerning dendritic and somatic mRNAs might become more revealing by identifying bipartite modules.

4) They should address parvalbumin cells in some detail.

Reviewer #3:

The paper by Perez and colleagues uses laser capture microdissection of dendrites and somata of cultured rat hippocampal neurons followed by single cell RNA-seq to assess the localization of mRNA transcripts in the somatic and dendritic compartments. This study addresses an important gap in our understanding of the cell type-specific regulation of dendritic RNA localization. Capturing mRNA from dendrites of single cells is challenging, and the dataset and analysis they present convincingly demonstrate that both glutamatergic and GABAergic cell types localize specific mRNA species to the dendrites in support of dendritic protein synthesis.

Overall I found the paper to be well organized and clearly presented. Although the number of cells/dendrites and the number of transcripts per cell/dendrite are modest compared with scRNA-seq studies, due to the challenge of manual LCM, the data quality appears to be sufficient to clearly separate at least ~2 glutamatergic and 3 GABAergic cell types.

1) The authors compare rat cultured neurons, derived from P0 animals, with large-scale scRNA-seq datasets from adult mouse primary hippocampus samples. What are the caveats from the species difference and also the difference between cultured and primary neurons? This should be at least mentioned.

2) – Data about gene expression are presented without any units (e.g. Figure 2A, B – y-axis; Figure 3A, B, Figure 4A-C). Are these values TPM, FPKM, CPM, or something else? In the axes with log units, is it showing log2 or log10?

3) – In the differential expression analysis, the authors explain that they used an adjusted p-value (i.e. FDR control) for somatic cell type differences, but they chose an uncorrected p-value cutoff (p<.02) for the dendrites. The reasoning they provide is that the FDR-control is "overly punitive" (meaning conservative) and would cause a high rate of false negatives, which they demonstrate by downsampling the somatic datasets. This is not a statistically sound justification for omitting any correction for multiple comparisons, as it essentially allows an arbitrarily high rate of false positives.

One way the authors could validate the potential rate of false positives would be to shuffle the dendrite labels (i.e. randomly re-assign dendrites to each of the cell types) and re-run the analysis with the same statistical thresholds (i.e. p<0.02). Any genes that pass the significance threshold are by definition false positives, and the number of such genes can be compared with the number that are detected in the original (non-shuffled) analysis. This issue is critical because it affects the central claim of the paper that there are differentially expressed dendritic RNAs between cell types. As shown in Figure 3A, only ~2-30 such genes were detected even with the uncorrected p<.02 threshold, and it is thus conceivable that this number is strongly affected by false positives.
