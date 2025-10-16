# Peer review - Round 1

Editors:
- David D Ginty, Harvard Medical School United States

Reviewers:
- Gordon Fishell, Harvard Medical School United States
- Bernardo L Sabatini, Howard Hughes Medical Institute, Harvard Medical School United States
- Matthew Ryan Banghart, Harvard Medical School United States

## Review text

DOI: [10.7554/eLife.47889.sa1](https://doi.org/10.7554/eLife.47889.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The impressive study by Smith and colleagues tackles in unprecedented fashion the relationship between the expression of neuropeptides and their cognate GPCRs. Using the same two cortical regions that the Allen institute has previously used for comparison (the visual and ALM cortices), Smith and colleagues compare the cell type specificity of peptide and receptors across the cortex. A number of fundamental observations are made: 1) virtually every neuronal type expresses multiple discrete types of NPP and associated receptors; 2) GABAergic cells show more NPP diversity while; 3) Glutamatergic cells show more diversity in receptor expression; 4) the 47 pairs of peptides and receptors can uniquely define cell types with high precision; 5) the relationships between peptides and receptors in stereotyped in a region specific manner. These are all observations of first rate importance, and I'd like to congratulate the authors for taking on a complex problem and discussing the underlying logic so systematically.

Decision letter after peer review:

Thank you for submitting your article "Single-cell transcriptomic evidence for dense intracortical neuropeptide networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Gordon Fishell (Reviewer #1); Bernardo L Sabatini (Reviewer #2); Matthew Ryan Banghart (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Smith et al. performed analyses on a publicly available single-cell transcriptomic dataset from Tasic et al., 2018, to generate testable hypotheses regarding local neuropeptide signaling between neuronal cell types in the mouse cortex. Their main findings are: (1) 18 neuropeptides (NPs) and their receptors are highly expressed in most neurons across cortical areas, (2) most cells have multiple NPs and NP receptors, and (3) 18 NPs and their receptors are differentially expressed between neuronal cell types. These results highlight the importance of elucidating local neuropeptide signaling and their consequences on circuit and network activity. The study also provides a potentially useful framework for predicting intercellular signaling networks and generating experimental hypotheses from transcriptomic datasets. The study is timely, the manuscript is well written, and the results are interesting. For the revision, while no wet lab experiments are requested, the reviewers agree that additional data analysis, methodological explanations and discussion points, as described below, are warranted.

Essential revisions:

1) Table 1: Since the dataset is enriched for certain cell types including Vip, Sst and Ndnf (partly Npy) cells, it is not surprising that these peptides appear high up in the list. The FACS sorting process probably even selects cells with higher peptide expression within these subtypes based on FACS sorting threshold criteria. How would the analysis change if the dataset represented natural proportions of cell types? Presenting the data in this way can be confusing. Is there a way to present the data so that it becomes independent of how many cells per cell type are included? Would Npy, Sst, Vip for example have much lower peak FPKM and pFPKM percentile/rank? Similarly, Figure 1B and Table 3 (Fraction of pairs) do not represent biological distributions but are strongly influenced by enrichment of certain cell types. Table 3: would it be better to present fraction of cell type pairs rather than fraction of cell pairs for same reason?

2) Figure 4: Analysis of the transcriptomic data using the autoencoder was central to many of the main findings, but there was an overall lack of discussion of both the methodology and details of the features learned by the autoencoder. We have listed several areas for further discussion below:

How was the autoencoder architecture chosen, and why is there an increase rather than a decrease in the number of dimensions for the NP autoencoder (47 to 50 vs. 6,083 to 100)? Were there other architectures tested that did not perform as well as the one presented in this study? Please discuss this. Related, it was unclear why the authors chose to use the HE gene set instead of the 4,000 differentially expressed (DE) genes for WGCNA in Tasic et al., 2018. Did using the HE genes perform better or worse than taking the most variable or differentially expressed genes? Also, for the sets of 47 random genes, the authors could have matched these "random" sets to the NP gene set by measures of variability or differential expression instead of matching expression levels. This would make for a more interesting comparison than the random 47-gene sets drawn from all genes in the Tasic et al., 2018, dataset, since many of these randomly drawn genes might not be differentially expressed.

3) What do the features in the 5-d latent space of the autoencoder networks look like in terms of gene weights, and how do these dimensions/vectors compare to the principal components? This will also potentially help with clarifying/understanding the nature of the input used by the GMM classifier for classifying the cells that may subsequently affect the resolution index.

4) Figures 6, 7, and supplements to Figure 6: The coupling scores and matrices in these figures were important for inferring or predicting neuropeptide signaling between neuronal cell types. However, the authors provided little discussion of any significant trends or differences beyond their presentation of the individual coupling matrices for single cognate pairs. The study will be more impactful if the authors could provide more detailed discussion regarding the structure within these coupling matrices, with examples of specific differences or generalized trends observed from that structure to generate specific experimental hypotheses. Some specific points for further discussion are listed below:

Why was the threshold set to 50th percentile? Why not at certain CPM? The reasoning and method here is not completely clear. It seems that this strict threshold produces too many false negatives that may unnecessarily discard biologically plausible interactions to be evaluated.

The coupling matrices are all presented at the cell type level and not at the subclass or "family" level (branches/clades between subclass and type), although there is clearly some clustering or block structure at these higher levels along the hierarchical tree. Is NP signaling more type-specific or generalizable to a family/subclass? Perhaps a heatmap visualization at varying levels besides cell types/leaves more similar to Figure 5 will help.

5) The authors could provide more details on which cognate pairs are region-specific vs. "conserved" across regions based on the sparsity of the corresponding coupling matrix, and to compare this to the known properties of the corresponding NP-expressing cell type/family/subclass (e.g. the disinhibitory action of Vipinterneurons via inhibition of Sst/Pvalb interneurons). Do the 47 pairs distribute in a laminar specific pattern and does this perhaps suggest whether they are used to augment bottom up, top-down or recurrent cortical activity? Also, the authors could comment more on the density/sparsity for each NP. Are there NPs that seem to have very specific signals (almost one-to-one), and which ones are much broader? For example, Trh->Trhr appears sparse/type-specific, whereas Adcyap1 appears to have a broad range of targets via multiple receptors and Crh->Crhr1/2 appears to act at an intermediate scale. Please provide more discussion of the variation in the sparsity of coupling for the cognate pairs analyzed.

6) Related to point 5, could the authors also provide more discussion of autocrine vs. paracrine NP signaling since there seem to be low coupling scores along the diagonal. This may suggest that there are very specific NPs that may act specifically in an autocrine manner, perhaps for autoinhibition in the case of Gi/o coupled pathways.

7) The presentation of the coupling matrices for single cognate pairs makes it difficult to appreciate structure/trends by the predominant coupling of downstream pathways. Are there preferred/predominant couplings for each subclass/family/type, e.g. mostly Gi-coupled for Sstinterneurons?

8) In Figure 7, it would be helpful if the authors could provide an example of a network graph diagram depicting their inferred NP signaling for a particular cell type or subclass, such as the VISp Vipinterneurons.
