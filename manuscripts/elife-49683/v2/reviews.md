# Peer review - Round 1

Editors:
- Ross L Levine, Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49683.sa1](https://doi.org/10.7554/eLife.49683.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Improving drug discovery using image-based multiparametric analysis of the epigenetic landscape" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Although the reviewers found aspects of the work to be of merit, there were substantive concerns relating to the overall impact of the new technology and the broad relevance of this technique to drug discovery. Despite interest in the work, these concerns were substantive enough to preclude publication in eLife.

Reviewer #1:

In this manuscript, Farhy and coworkers developed an image-based analysis to examine epigenetic landscapes. This method was developed from a prior multivariate image analysis (Collins et al., 2015) in the context of epigenetic modulation. Here the core idea is to rely on a set of structural features of epigenetic marks (H3K27me3, H3K9me3, H3K27ac and H3K4me) as readouts of epigenetic modulation. These structural features were extracted via machine-learning algorithms described previously. To demonstrate the utility of this method, the authors first showed that the current approach is more sensitive than prior "intensity"-based approaches to detect the effects of small-molecule epigenetic modulators. The authors then showed that the multi-variate readouts correlate with treatment doses and the compounds sharing common targets in the context of multiple cell lines. With this approach, the authors further identified the epigenetic modulators that synergistically work with TMZ and radiation and distinguished the cell fates/differentiation of several types of cells. Novelty of this work mainly lies in the machine-learning-based algorithm to extract a set of structural features of chromatin as readouts. However, the reviewer feels that this work is largely an incremental data analysis method with multiple limitations as detailed below.

1) To examine epigenetic modulation, many robust approaches such as ATAC-seq/ChIP-seq have been developed as noted by the authors. Their methods provide rich information with terrific resolution. In contrast, various Western-blot assays or image-intensity-based assays have been developed to examine the global levels of certain epigenetic marks (H3K27me3, H3K9me3, H3K27ac and H3K4me). Merits of the MIEL largely lies between the two conventional approaches. However, the challenge of data collections (three or four sets of data for a treatment condition) and the complexity of data processing (feature extraction and combination) significantly limited the broad use of this approach.

2) In contrast with the conventional image-intensity-based assays, MIEL only revealed around 10 additional compounds among >200 candidates that alter the epigenetic landscape (data of Figure 1B). However, it is not clear about the mechanism that the "10" additional compounds cannot be identified with the conventional image-intensity-based assays but can be revealed with MIEL. It is not clear how the authors ruled out the possibility that the changes of epigenetic landscapes associated with the indirect outcomes of off-target effects of the 10 compounds. If it is the case, the positive readouts become irreverent to the primary targets of these compounds.

3) The underlying molecular mechanism of MIEL is not clear. The altered structural features are very descriptive and may not link to perturbation in a casual manner. As a result, it is likely that the effects of many epigenetic modulators may not be readily detected with MIEL; the MIEL-detectable changes may not be directly relevant to epigenetic biology. As a result, MIEL needs to be fully validated before its implementation in a specific context. Meanwhile, ATAC-seq/ChIP-seq, Western-blot assays and image-intensity based assays are often developed on the basis of molecular mechanisms of epigenetic modulation. The latter are thus more robust given the direct causal relationship between the targets of interest and their function-related readouts.

In short, in the context of many alternative conventional approaches, the complexity and limitations of MIEL outweigh its merits. The reviewer doesn't feel that the quality of this manuscript reaches the standard of eLife in terms of novelty and broad impact.

Reviewer #2:

Chen Farhy and colleagues report on an elegant high-throughput way to use image analysis that can identify epigenetically active drugs, classify them by molecular function, and assess candidate drugs for their ability to increase sensitivity to chemotherapeutic agents. This is a really understudied area that has traditionally required expensive plate reader based tools to quantify. The manuscript is very detailed and thorough and has addressed the utility of the MIEL tool in a wide range of drug screening settings.

The two major concerns are the lack of certain control conditions necessary to support the authors claims.

1) The authors call their phenotypic screening platform "Microscopic Imaging of Epigenetic Landscape (MIEL)", and the imaging is solely based on texture features of four immunolabeled epigenetic marks. However, the texture of those histone modifications can be correlated to the general structure and texture of the DNA. The authors exclude compounds that lead to a cell count > 50 nuclei/ well, however, if a compound induces significant apoptosis with ~50% cell death, the texture features could pick up chromatin condensation and thereby potentially generate false-positive hits.

It would be helpful to see if there is a correlation between nuclei count and MIEL z-scores.

Furthermore, the authors claim that they can use MIEL to analyse dose-dependent effects from drug treatment. Yet, in light of the concern above, they cannot be sure whether they detect the pharmacological effect or a toxic effect that is not related to epigenetic changes. Concerning is the fact that the initial screen was conducted for just 24h and still was sufficient to separate the drug classes in clusters. However, later in the manuscript the authors increased the treatment times to 2 or 3 days, which reflects much more the time frame required to induce detectable epigenetic changes.

It would be great if the authors could put a few cytotoxic drugs through their pipeline that act not via epigenetic mechanisms but rather are inducers of apoptosis, necrosis, DNA damage, or cell-cycle arrest, and see whether they cluster with any of the epigenetic modifier classes or form separate clusters.

2) The second major concern is that, for many of the analyses it seems almost irrelevant whether all four histone modifications are taken into account, or just either of the two pairs, or just one of the four marks. This could be an indicator, that the texture features that are being extracted are not specific to the histone modifications, but rather general changes to DNA structure.

To clarify this, it would be recommended to stain just for DNA structure (DAPI) and overall Histone structure (H3), treat with representative compounds of the drug screen, and extract the same/ comparable texture features that were used for MIEL. Using DAPI and H3 texture, is it then also possible to discriminate between the compounds?

The second experiment to confirm that the changes in texture are due to a change in Histone modification landscape and not due to non-specific alteration of DNA structure, is to add a second detection method for the specific Histone modifications. ATAC sequencing after treatment with and without representative compounds of the drug screen should provide biological evidence for the phenotypic results of the image analysis.
