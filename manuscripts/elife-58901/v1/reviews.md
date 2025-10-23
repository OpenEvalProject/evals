# Peer review - Round 1

Editors:
- Joel K Elmquist, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58901.sa1](https://doi.org/10.7554/eLife.58901.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

These studies provide a single-cell transcriptomic analysis of the ventral posterior hypothalamus and were validated using fluorescent in situ hybridization. These data sets will be a valuable resource to the field of hypothalamic biology.

Decision letter after peer review:

Thank you for submitting your article "Cellular taxonomy and spatial organization of the murine ventral posterior hypothalamus" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The reviewers have opted to remain anonymous. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data. Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Mickelsen and colleagues describe results from a series of studies using single cell sequencing to access the molecular identity of both neuronal and non-neuronal cell types of the mammillary body. The authors report 18 transcriptionally distinct non-neuronal cell types, and 20 transcriptionally distinct neuronal subtypes corresponding to cells residing in the premammillary, supramammillary, tuberomammillary, and arcuate nuclei as well as the lateral hypothalamic area and mammillary bodies. Furthermore, they performed projection mapping studies using anatomically-specific genetic markers for subdivisions of the mammillary bodies to demonstrate distinct projection patterns to the anterior thalamic nuclei. The study is well designed incorporating two independent, batch-corrected replicates and independent samples from both males and female mice in the analysis.

Essential revisions:

1) The paper leaves a considerable amount of work for a potential user of this information to understand what level of selectivity and specificity would be attained with combinations of the marker genes described in the paper. Based on the scRNA-Seq data, how well can different transcriptional clusters be separated at the level of individual cells in the dataset? How many genes are needed to achieve optimal separation?

2) A general criticism of the manuscript is that the authors have clearly captured neurons from multiple subnuclei of the ventral posterior hypothalamus (PM, SUM, TMN, ARC, LHA, and MB), but have not subclustered the cells from these different subnuclei. Given that marker genes are identified by a "one-versus-rest" methodology, the markers found for each of these subnuclei will broadly mark neurons within these regions, but it will be difficult to identify unique cell types within a subnucleus. Thus, a more rigorous approach of isolating and reclustering some of their cell groups corresponding to a specific subnucleus should be undertaken (similar to what was already done for cluster 8, SUM neurons). At a minimum, reclustering PM and MB neurons on their own seems reasonable; however, reclustering of ARC (Campbell et al., 2017) and LHA (Mickelsen et al., 2019; Rossi et al., 2019) neurons is unnecessary as previous publications have gone into detail for these structures.

3) Although the authors discuss at length the possibility the Slc17a6+ / Slc32a1+ neurons of VPHGLUT cluster 8 might represent SUM neurons know to project to dentate gyrus and corelease glutamate and GABA. If this cannot be addressed experimentally, the authors need to temper the conclusions that can be drawn here.

4) There is a remaining question about the dynamic range of the data used for classification. In neurons, Figure 2E (note: this is mislabeled as Figure 3E in the text) indicates that there are only a small multiple of UMIs over the number of detected genes. A histogram that summarizes the number of UMIs/gene in this dataset would be helpful. The authors should discuss the significance of the fairly low number of UMIs for most genes. In addition, do the authors know if this presumed low coverages extends to the marker-genes.

5) The authors could perform FISH analysis with combinations of marker genes to attempt to assess if they have a substantial false negative rate in detected genes. This could be established by measuring marker-gene co-expression ratios from FISH and comparing this values to the co-expression ratios predicted with their scRNA-seq datasets. Short of this, the technical issues need to be discussed in more detail.
