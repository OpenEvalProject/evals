# Peer review - Round 1

Editors:
- Sacha B Nelson, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69825.sa1](https://doi.org/10.7554/eLife.69825.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This excellent manuscript combines molecular, anatomical and behavioral methods to characterize neuron types in the mouse superior colliculus. It will likely be a significant resource to those who study how these circuits integrate sensory information to promote motor output. A diverse set of experiments supports the conclusion that the superior colliculus includes separate circuit modules involved in distinct behaviors: prey capture and predator escape.

Decision letter after peer review:

Thank you for submitting your article "Transcriptomic encoding of sensorimotor transformation in the midbrain" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Reviewing Editor Sacha Nelson and Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Feldheim (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We have included the full reviews below so as to preserve the clarity of the requested changes. However the required changes are those involving new analyses and textual clarifications as requested by Reviewer # 2.

After consultation, there was agreement that additional suggested experiments, such as the additional manipulations and recordings suggested by reviewer #1 and the in situ experiments suggested by reviewer #2 would strengthen the manuscript, but are not required for acceptance.

Please do, however, complete each of the additional analyses and clarifications requested in items 1.1, 1.2, 1.3, 2.1, 2.3 and 3.2 as outlined by reviewer #2 and consider the suggestion made in item 3.1.

Reviewer #1 (Recommendations for the authors):

My only question is if the medial and laterally labeled Cbln2 neurons have similar properties. For example in FigS4, the receptive field mapping of Cbln2 Cre mice using Ca imaging, it looks like the field of SC being imaged is medial. Therefore it would be expected that these cells would detect dorsal stimuli based on their position in the SC. It would be interesting to see if the more lateral neurons also had dorsal RFs.

A similar question comes up when assaying the behaviors are medial SC neurons being selectively stimulated/ablated in these experiments.

Reviewer #2 (Recommendations for the authors):

1. Single-cell RNA sequencing data

1.1 There is a large fraction of excitatory cells that were not assigned to a layer ("other neuron" in figure 1H, mostly Ex-2). This is a large fraction of the excitatory neurons. The data presented here suggest at least two possibilities: either these cells are widely distributed in the superior colliculus, across layers, or these are low-quality cells. If there is any evidence that these are low-quality cells, that should be clearly indicated in the paper. It would be useful to show in the supplementary data quality control plots (for example, a tSNE with cells color-coded by number of genes/cell). Why there are no cells mapping to the deep gray layer?

1.2. Neurons from the superior colliculus were sequenced by Zeisel et al. (Cell 2018). That study reported a comparable number of excitatory and inhibitory clusters. How do these new data compare to the Zeisel data? A Sankey plot or some other analysis showing the correspondence between these two datasets will help readers connecting the two resources.

1.3. How does SPACED compare to previous methods for mapping single-cell transcriptomes on the Allen Brain Atlas data? For example, are the results of mapping with SPACED consistent with the results obtained with the mapping method proposed by Zeisel et al. 2018? How does the method perform if the number of genes selected for mapping changes? How was the method benchmarked?

2. Morphological reconstructions and Patch-Seq

2.1. For the data shown in Figure 2A-G, the text refers to the injection of an unspecified "AAV mixture". Please describe in the main text what mixture was injected and what is the rationale of the experiment

2.2. The integration of molecular and projection data relies entirely on the Patch-seq experiments. Figure 2J, however, shows that there are neurons retrogradely labeled from InG-ZI and Op-LPTN that do not express neither Cbln2 not Pitx2. Is it possible that these neurons belong to another excitatory type? In these experiments, retrograde tracing from LPTN and ZI is not cell type specific, therefore the existence of an excitatory type that projects to these two brain areas and does not express neither Cbln2 nor Pitx2 cannot be excluded. I suggest performing FISH for Cbln2 and Pitx2 on vGlut-IRES-Cre animals injected with AAV2-retro-DIO-EGFP in the LPTN or ZI.

2.3. Related to the previous point, the Methods mention that the Patch-seq data and the scRNAseq data are integrated using the CCA method in Seurat. However, here only a correlation matrix is shown (Figure 2K). A tSNE or UMAP showing the integrated scRNAseq and Patch-seq data would be much more informative.

3. Anterograde tracing

3.1 I would consider describing the experiments in Figure 6 earlier in the manuscript, after Figure 2. That seems the most logical place. Furthermore, figure S6 deserves to be part of one of the main figures. These are beautiful experiments showing very clearly that Cbln2 and Pitx2 neurons project to different brain areas. However, the narrative of the paper is prone to mislead the reader, because it emphasizes the projections to LPTN and ZI.

3.2 Related to the previous point, it would be helpful to expand the Discussion by mentioning how the different brain areas innervated by Cbln2 and Pitx2 neurons may participate to predator escape and prey capture behaviors.

4. Calcium imaging

It is good to see representative traces from the fiber photometry data. However, it would be even nicer to show a raster plot or a heat map encompassing all the neurons that were recorded. I could not find anywhere in the manuscript how many neurons were recorded and from how many animals. Information on the data analysis pipeline for these data is also missing (or at least I could not find it easily). All this information should be included in the manuscript.
