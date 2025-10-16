# Peer review - Round 1

Editors:
- Nikos Konstantinides, https://ror.org/02c5gc203 Institut Jacques Monod France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78511.sa0](https://doi.org/10.7554/eLife.78511.sa0)

This study presents a valuable single-cell sequencing dataset of fruitless-expressing neurons in the male and female Drosophila nervous system. The quality data and convincing analyses allowed the authors to conclude that most neuronal types are present in both Drosophila sexes, suggesting that sex-specific versions of the transcription factor Fruitless can modify neural function in a sex-specific way without completely altering core neural identity. This work will be of interest to developmental biologists and neuroscientists with a focus on sex-specific differences.


---

# Peer review - Round 1

Editors:
- Nikos Konstantinides, https://ror.org/02c5gc203 Institut Jacques Monod France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78511.sa1](https://doi.org/10.7554/eLife.78511.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single-cell transcriptome profiles of Drosophila fruitless-expressing neurons from both sexes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Claude Desplan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The reviewers have raised concerns regarding the "sex-specific" versus "shared but sexually dimorphic" cell types. They recommend a careful re-analysis of the data to address this exact question. In particular, they recommend generating a single atlas with both male and female cells under different integration or merging conditions. This would include:

a) a careful parameter selection, such as resolution, that will allow for evaluation of subclusters. They also recommend a comparison between integration and merging of male and female datasets

b) doublet elimination using appropriate algorithms (e.g. DoubletFinder or other)

c) elimination of cell cycle influence

After generating such an atlas, an experimental validation of differences in cell number or sex-specific markers in a few well-known clusters would be necessary to address the question of sex-specificity of clusters.

2) The reviewers have noticed that, in multiple cases, there are discrepancies between the paper's conclusions and established knowledge or previous datasets. There has to be a clear discussion of the reasons or experimental resolution.

3) The paper is long and detailed and the reviewers feel that there has to be a Conclusion Section that summarizes the most interesting observations and makes the paper accessible to a broader audience.

4) In many cases, the reviewers noticed images that were of low quality or resolution. This also has to be addressed.

Reviewer #2 (Recommendations for the authors):

I have some concerns about the way neuron number was normalized per cluster per sex. I do not have a better way to do this analysis but would instead like to see a specific example cell type/cluster pinned down via counting the number of real neurons. This could perhaps be done using a known cell type and antibody stains for a marker protein or a GAL4-reporter combination, to determine whether the difference in neural number between sexes for a particular cluster is real. This approach was used to evaluate female-specific cluster 107, but not to validate any differences in neuron number in a cluster that is present in both sexes. The conclusion that so many clusters contain different numbers of neurons between the sexes is an important finding and additional "ground truthing" would help support the authors conclusions.

Many of the figure panels that contain antibody stains are not of sufficiently high quality to really see what is going on, even in the separate higher res version of the Figure. This is true in several places. For example, for Figure 7E, please consider cropping or including a second set of panels with insets showing the region with expression. Many brains, exe. all of Figure 10, are not high enough resolution to see what the tiny arrows are pointing at.

I was not able to evaluate a section of Figure 5: there are no panels after 5S. The text refers to experiments in 5T and 5U that are not shown.

"However, we do not find broad expression of ChAT at 48hr 478 APF, which is not consistent with our single cell data that shows extensive expression of ChAT." I was hoping for some discussion of this discrepancy, or an experimental resolution. mRNA expression does not always match protein (or reporter protein) expression. This can be especially true for terminal genes like neurotransmitters or Rhodopsins, where there are cases of high mRNA expression long before protein expression. I would love to see HCR in situs for ChAT vs. an antibody stain or protein reporter. This examination could potentially be restricted to a specific cell type for clarity. Comparing the two would be an interesting addition, especially given such a distinct difference that is otherwise unexplained in the manuscript. At the very least, this result should be discussed.

I'm not entirely sure I understand the link between the section on circadian rhythm and the rest of the paper. The authors were able to identify and label DN1p in the scSeq data, but unless I misunderstand, do not focus on DN1p in the experiments on sexually dimorphic roles of activation of a subset of circadian rhythm neurons.

Reviewer #3 (Recommendations for the authors):

In addition, we have some comments and questions about the data analysis that could impact some of these "big picture" conclusions.

A. One of the big findings the authors report from their single cell analysis is the apparent detection of male-specific and female-specific neuron populations, a finding that would be of wide interest to those interested in sex differences. However, we feel that support from a further analysis would help make this result more convincing. The authors currently infer sex-specificity in some of their clusters based on the absence of cells from one sex after merging the datasets. This raises an obvious question – to what extent does this inference depend on clustering parameters, and how do you know what the optimal clustering strategy is? For example, in the combined-sex analysis, clusters 12/5/16 are considered separate clusters (Figure 1), and cluster 12 is designated as strongly male-biased and clusters 5 and 16 as strongly female-biased (Figure 2B). On the other hand, clusters 3 and tachykinin-1 are each considered a single cluster (Figure 1) and are considered sexually monomorphic (Figure 2B), but a look at Figure 2A shows that each of these clusters has a male half and a female half. Is there an objective reason for deciding when we are looking at a single monomorphic cluster with sex-biased gene expression, and when we are looking at a closely related pair of sex-limited clusters? The authors describe their statistical approach to determine the number of clusters; but that is going to be affected by sequencing depth, variation in staging, batch effects, cell cycle differences, etc. What is the most biologically significant clustering strategy, and how do you determine that? How do you decide, as a neurobiologist, whether you are under- or over-clustering your data, and when you hit that Goldilocks spot where your clusters are most likely to correspond to biologically meaningful cell types? These issues are worth discussing. (On a technical note, please use different colors in Figure 2B – the color for strong male bias looks almost the same as the color from strong female biased, which confused us until we figured that out).

There is a technical approach that could help with this. Merging combines the raw count matrices from different datasets, but an alternative is to integrate them (implemented through Seurat), which uses common anchors between cells across datasets to promote the identification of shared cell types. We think it would be worth seeing if this sex-specificity holds after integration. If it does, then that's two independent pipelines that identify sex-specific populations. We think that integrating, rather than merging, might help tighten up some of the sex difference analyses too. Looking at Figure 2A, it's clear that many of the clusters don't merge particularly well. The authors use this as evidence of variation in the extent of sexual dimorphism between populations (as labelled in Figure 2B). But we worry that this creates fuzzy boundaries between male and female populations of what may be the same neuron type. And this fuzziness could affect where the cluster boundaries are called. Comparing the bottom part of Figure 1F and 2A, we can see a cluster 6 that is called as a single cluster despite clearly separating into male and female populations in Figure 2A. This contrasts with Octopamine_1, which seems to be largely/entirely female-biased, while Octopamine_2 is male-biased. There are other examples like that. We wonder whether integration (rather than merging) will do a better job of identifying homologous cell types. The authors could then ask what is differentially expressed between male and female cell-types within a cluster.

B. A general conclusion the authors reach is that male and female fru+ neurons 'share common gene expression repertoires with sex-specific information overlaid on these core patterns' (lines 145-149; see also 1057). This conclusion rests on their observation that 'nearly all clusters are comprised of male and female neurons'. On the one hand, this is what UMAP does – it clusters cells by expression similarities. How do we know that a cluster containing both male and female cells on a UMAP actually corresponds to the same population in male and female brains? On the other hand, taken alongside the small number of 'sex-specific' clusters they resolve, it seems that the authors are arguing that the vast majority of the neurons are shared between the sexes, but that these shared types generally show sexual dimorphism in their expression. This is an interesting result, but it rests exclusively on the distribution of cells in UMAP space and the cluster identification boundaries. For the reasons outlined above, these features of the UMAP/clustering are heavily dependent on the input parameters. Without some sort of orthogonal validation, it's hard to know how robust this result is.

C. A potential problem with the sex difference analyses, which the authors themselves recognize (line 249), is how to exclude the possibility that much of the difference is driven by sex differences in development time and/or cell cycle phase. The data discussed on lines 970-974 seems to confirm that the differences in developmental timing could be a significant contributor to male- and female-specific gene expression. The authors show some of their stainings at two different time points, which helps for those specific genes, but it's a potential issue that limits the interpretation of the transcriptomic data itself and the authors should probably highlight it. On the analysis side, there's not much that can be done about development time, but have the authors tried to account for cell cycle?

D. Organizing the section on transcription factors (starting at line 1023) by TF superfamily may not be the most informative approach, since the type of DNA binding domain is not directly related to developmental function. It may be better to organize this section by the degree of specificity: start with which TFs, regardless of their family, are the most specific to candidate cell types – and which TFs are specific to particular clusters that were singled out for detailed analysis in previous sections (e.g. KC cells, clock neurons, which TFs show correlation with particular neurotransmitters, etc). Better biological insights are likely to be obtained this way. Figure 12 and its supplements are near-impossible to take in. It would be better to replace the main-text figure with examples of highly specific TFs mapped on UMAPs, perhaps in relation to cluster annotation developed previously in this paper and move the big grid to the supplement. Showing a separate panel with 5-10 most sex-biased TFs for each sex would be more informative than annotating them on the large cluster*TF grid.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Single-cell transcriptome profiles of Drosophila fruitless-expressing neurons from both sexes" for further consideration by eLife. Your revised article has been evaluated by Claude Desplan (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

When comparing the merged and integrated dataset, the authors argue that they are highly concordant. Nevertheless, based on Figure 1 and Figure Supplement 5C-D, it is pretty obvious that integration worked better since there are a number of library-specific groups of datapoints in the merged UMAP. It would make it easier to visualise the integration of the libraries, even if the points are shuffled. In R, this is implemented in DimPlot of Seurat, by the option shuffle=TRUE.

We appreciate that the authors do not want to repeat the analysis, but they should definitely compare how the two approaches affect their analysis and not only rely on the visual (which, furthermore, is not convincing).

This can indeed lead to serious misinterpretations of the data when clusters that are library-specific are simply the product of batch effect. For example, the authors identify more mushroom body subtypes (9 or 13 depending on the clustering) than what has been reported in the literature (7). Are these clusters reliable? Or do they result from batch effect? Comparing Figure 1, Figure Supplement 5C-D, and Figure 4A, it seems very plausible that cluster γ_KCs_3 is library-specific. This problem might also occur in other neuronal structures, where the cell type composition is not as well known as the mushroom bodies.
