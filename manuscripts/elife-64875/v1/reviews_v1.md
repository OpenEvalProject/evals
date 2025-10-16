# Peer review - Round 1

Editors:
- Paola Bovolenta, CSIC-UAM Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64875.sa1](https://doi.org/10.7554/eLife.64875.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study provides a comparative analysis of the cell variety present in the dorsal lateral geniculate nucleus (dLGN) of mice, non-human primates, and humans using single-cell/single-nucleus RNA-sequencing. The strong and creative bioinformatics analysis used in the study uncovers interesting and subtle cross species links between different types of neurons, providing an extensive characterization of this as yet understudied visual relay nucleus.

Decision letter after peer review:

Thank you for submitting your article "Single-cell RNAseq uncovers shared and distinct axes of variation in dLGN neurons in mice, non-human primates and humans" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Fenna Krienen (Reviewer #1); Tomomi Shimogori (Reviewer #2); Lucas Cheadle (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript provides a comparative analysis of the cell variety present in the dorsal lateral geniculate nucleus (dLGN) of mice, non-human primates, and humans using single-cell/single-nucleus RNA-sequencing (Smart-seq). The study identifies excitatory and inhibitory dLGN cell types in the three species and shows that the different subclasses of inhibitory neurons are relatively similar across species. In contrast, excitatory neurons appear to bear cross-species differences particularly between mouse and primates.

The study provides an extensive description of the dLGN neurons, an important visual relay nucleus that has been so far poorly studied. As such, these data are very welcomed and will likely attract the interest of researcher working in visual function and beyond. The strong and creative bioinformatics analysis has uncovered interesting and subtle cross species links between different types of neurons. Nevertheless, there a number of aspects that needs to be improved as listed below:

Essential revisions:

1) The introduction will benefit from a clearer explanation of why cross species comparison of dLGN neurons is important. Stating that this comparison has been performed because others have done so for other brain regions is simplistic. Better motivations could be underscored, i.e. species differences in visual system organization such as trichromacy or degree of binocular vision etc. Another motivation could be identifying whether there are discrete vs continuous differences across species related to main cell types. Other can be pointed out.

2) Although the authors have validated a few genes emerged from their analysis (Figures 4G and S4E), the study should include a more extensive and rigorous analysis of cell-type-specific gene expression in all species described either by FISH or ISH. Furthermore, data shown in Figure S3G should be better explained in the figure legend: it is difficult to understand if the cells in question fall into the mentioned magno and parvo cell classes. It may be also useful to compare their data with those of NHP LGN available at https://gene-atlas.brainminds.riken.jp/.

3) The data could be presented more effectively by reorganizing both text and figures with cross-species comparisons from the very beginning. For example, one could start with a figure that has the species-integrated clusters, including only the dLGN dissections, and then explore conservation and divergence of gene expression, proportions etc. In the present form, it is difficult to appreciate the main messages. Each species-specific paragraph contains details that are not directly comparable among species (e.g. connectivity, topography and cell size in humans/NHP, direction sensitivity and dendritic morphology in mouse). What is the main outstanding question: how (or whether) the mouse X, Y and W types map to the M, P and K types? Is the question different?

4) The UMAP projections in Figure 1 need to be labelled for clarity. Colours are not sufficient to interpret the data. This should be also revised for Figure 2-4.

5) The manuscript does not explain how the dLGN shell and the core regions have been dissected. This is important given that these regions are not as clearly distinct as the dLGN lamina in other species. Have the authors taken advantage of the fact that the shell receives input from specific RGCs? Have they used any specific line? Confidence in the dissection could be increased by using a fluorescent approach to selectively label the shell, for example by using a transgenic driver line (Cruz-Martin et al., 2014).

6) The columns in Table S2 need to be labelled to allow interpreting the data and understand statements such as that reported in lines 101 – 103 ("..differentially expressed genes between donors were related to neuronal signalling and connectivity etc..). How have the authors determined that these differentially expressed genes are not related to "activity-dependent effects"?

7) Line 206-207. The data are confusing: are GABA2-6 cell types found in both dLGN and adjacent nuclei in mouse but only in dLGN in primates? The beginning of the paragraph (line 187) seems to suggest that only dLGN datasets were included in the 3 species comparison but it is unclear if this is the case. A clearer cross-species analysis of equivalent regions could further clarify what is conserved in the dLGN proper vs what is shared or distinct in other nuclei.

8) Is PVALB barely expressed in macaque cell types? This is surprising and should be verified. Consistent with the human data (Figure 3), PV protein expression in macaques is detected in some interneurons and in M and P projection neurons (https://pubmed.ncbi.nlm.nih.gov/8885200/). There is a new rhesus macaque genome (Mmul_10) that could help resolving this question.

9) Parameters for clustering analysis (using CCA/Seurat) need to be described, because changes in parameters can change the clusters. Did the authors test if the species integration results hold if parameters are changed? Why GABAergic clusters are different in Figure 4B vs Figure S4A?

10) Figure S1. The data indicate that gene detection is higher for human and mouse than for macaque. However, macaque and human gene detection rates look similar in Figure S1. Can the lower gene detection in macaque be the results of sequencing coverage?

11) Data could be exploited more than what is currently done. For example, the results and discussion mention that DEGs are related to neuronal signalling and connectivity but not metabolic factors. The analysis leading to this conclusion should be shown. Are the two M. nemestrina more similar to each other than they are to the M. fascicularis, or are all 3 donors different from each other in similar ways? Also, is there evidence that there is a fresh vs frozen difference in quality or in the type of genes that are differentially expressed? Similarly it would be useful to describe further how the donor effect magnitudes were compared with previous analysis in Hodge et al. (line 244-245).

12) What do the author mean with "gene expression gradient"? Given that there is a clear anatomical border for each layer in human and monkey LGN, it is difficult to imagine that genes might be expressed in a gradient across layers. Lower magnification ISH image need to be provided to show the existence of a gradient of gene expression.

13) The discussion could be improved by discussing the main conclusions first were discussed first. Is the main point that neuronal types in dLGN that have been defined based on other criteria (morphology, ephys, connectivity) in all species are not very transcriptomically distinct?
