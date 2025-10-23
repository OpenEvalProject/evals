# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63450.sa1](https://doi.org/10.7554/eLife.63450.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your study sets a fine example of high-resolution decoding of transcriptional identity using a combination of single-cell transcriptomics, genetic driver lines, and imaging. It will be a useful resources for the community!

Decision letter after peer review:

Thank you for submitting your article "Temporal evolution of single-cell transcriptomes of Drosophila olfactory projection neurons" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Scott Barish (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This paper from the Luo lab builds upon their previous paper on single cell RNA profiling from developing projection neuron subpopulations in the Drosophila olfactory system. In this paper, the authors expanded their sequence analysis to new populations subsets for projection neuron (PN) classes using new combinations of split GAL4 lines to label new projection neuron subpopulations for cell sorting and sequencing. Each PN class generally innervates a single antennal lobe glomerulus to make connections with a single class of olfactory receptor neurons (ORNs). Different PN classes are born from 3 types of neuroblast lineages in a specific temporal order that form anterodorsal, lateral PN clusters that represent excitatory cholinergic and ventral inhibitory GABAergic PN clusters. Incorporating this new dataset with their previous scRNAseq data, they were able to increase the resolution of the sequence clusters representing different PNs during development, identifying 20 PN classes. In addition, comparing sequence data for each developmental time point, the authors were able to provide developmental trajectories for PN transcriptional profiles and how they change over time. The sequence analysis shows that the transcriptional profiles across PNs are show the highest observable diversity in early to mid-pupal stages when the PNs are differentiating and connecting with appropriate ORN classes within glomeruli. However, this transcriptional diversity across PN populations is dissolved by adult stages in mature PN populations. The authors were also able to show that PNs that are in the same lineage with adjacent birth order were transcriptionally more similar. Even though this paper provides an incremental progress from the previous study from the Luo lab on PN transcriptional profiles during development, it does provide some additional information on how transcriptional diversity and developmental trajectories are influenced by lineage, birth order and birth timing of diverse PN populations during development. The study sets a fine example of high-resolution decoding of transcriptional identity using a combination of single-cell transcriptomics, genetic driver lines, and imaging. A few points to address or add to the manuscript are listed below before the paper can be published in eLife.

1) Some of the wording on the figures are extremely small. Please make them.

2) From Materials and methods, it seems the sequence data and the codes have not been submitted to the public databases yet. Please make sure these are uploaded.

3) The clusters in Figure 2C, F, and J where the new sequence data is overlayed onto the GH146+ PN data at 24 hours: I am not sure why the gray GH146+ cluster patterns appear different in each tSNE graph. Aren't they supposed to be the same? They appear very similar in Figure 2—figure supplement 1.

4) Given that this is a follow up study, It would be good to see as much data as possible that can provide new knowledge about the transcriptional profiles. Could the authors provide a list and a heatmap matrix for PN cluster specific expression of some key gene families like cell surface molecules, transcription factors, neurotransmitter receptors, and ion channels for each developmental time point? Throughout the text there are mentions of these gene groups but it would be good to see it as a figure for each in a supplement.

5) The bioinformatics analyses presented are well explained, and thorough. However, there is an important aspect missing. The 24h cells have the greatest power in clustering, finding all PN subtypes, while the adult is the weakest (transcriptomes converge). Nevertheless, using MARS (alternatives using simple SVM classifiers could have been applied, as benchmarked by Abdelaal et al. 2019, Genome Biology), and followed-up using more in depth analyses, the authors show that the adult cells show similarities to the 24h subtypes. It would be a great added value if the cells could be analysed all together, across time points, using a couple of batch effect removal techniques (Harmony, BBKNN, Scanorama,..). It would follow from the results that the 24h cells would drive the clustering, but that the other time points would co-cluster. This would provide an elegant foundation, finding all subtypes back, with cells from each time point present in each cluster. Next, each subtype can be analysed separately, using trajectory inference, to study the dynamical changes. The current analyses somehow approximate this strategy using an ad hoc combination of methods, which seems reasonable, but would benefit from a comparison with aforementioned batch effect corrections (the batch here would be the time point).

6) A similar study of tracking neuronal subtype development has been carried out for T4/T5 neurons in the optic lobe, as well as other optic lobe subtypes. It would be informative to discuss the current findings in the context of these studies from the Desplan and Zipursky labs.

7) An inference is made to connect developmental trajectories with neuroblast birth order. It seems a missed opportunity to include single-cell transcriptomes of the neuroblasts in this study, for example using scRNA-seq of the larval brain. The authors exploit gene sets from earlier studies – but could the entire data set be used instead? If this is bulk RNA-seq, there are computational techniques to compare them (map them) onto the single-cell data.

8) Ecdysone is mentioned in the manuscript, but there is little investigation into the transcriptome changes that are induced by the ecdysone peak (see also Jain et al., 2020). The dynamic-dynamic and dynamic-stable modules is an intuitive way to identify cell type specific dynamics, but how are these linked to the Ecdyson receptor? Does EcR regulate the same genes in every subtype?
