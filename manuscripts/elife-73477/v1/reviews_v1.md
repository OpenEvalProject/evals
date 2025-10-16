# Peer review - Round 1

Editors:
- Lois Smith, Boston Children's Hospital/Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73477.sa0](https://doi.org/10.7554/eLife.73477.sa0)

Using single nucleus RNA sequencing, the authors have characterized all major cell types in the mouse iris and ciliary body, defined new types of iris stromal and sphincter cells, and shown cell-specific transcriptome responses in the resting, constricted, and dilated states. They have identified and validated antibodies and in situ hybridization probes for visualization of major iris cell types. This work will be a valuable reference for investigations of iris development, disease, and pharmacology.


---

# Peer review - Round 1

Editors:
- Lois Smith, Boston Children's Hospital/Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73477.sa1](https://doi.org/10.7554/eLife.73477.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "A transcriptome atlas of the mouse iris at single cell resolution defines cell types and the genomic response to pupil dilation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Lois Smith as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Marianne Bronner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bo Chen (Reviewer #2); Chenxi Qiu (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) 10x platform was used in this study. The authors need to include: 1) If all the samples were collected in a single round of experiment on the same day. If not, how the batch effect was minimized. 2) For the three groups (untreated, dilated, constricted) of samples, what steps were used to minimize the potential transcriptional change and variation during the sample preparation. 3) How long after dilation or constriction were the sample taken?

2) Although only 6-8-week old female mice were used for single cell analysis, were the validation also conducted in male mice?

3) Does the duration of pupil dilation and constriction affect the transcriptome analysis? How did the authors choose seven hours as the duration for the dilation and constriction, any preparatory analysis to determine this time point?

4) Some missing labeling in the text, including Figure 2A, Figure 3A, and Figure 7A.

5) Could the authors provide some thoughts on why only dilation has effects on the gene expression changes, but not constriction? Some discussion on this might be helpful. No experimental proof required.

6) The methodological details for the differential gene expression analyses are not discussed in the manuscript. In addition, the authors should provide the full list of differentially expressed genes instead of top 25 genes and discuss the cutoff of differentially expressed genes where they are confident. The adjusted p-values for the top differentially expressed genes are small and may not provide true value into the analyses.

7) The figure legends could have more details on the replicates shown on the quantitation of immunofluorescence images. Example1 : In figure 8, I am assuming each dot here represents one nucleus. How many mice are in this plot? Is there systematic variation among different mice? It would help if the authors color code the data points by the mouse each nucleus is from. Example2: In supplemental figure 4, is each data point here is from one mouse or one image for a given area, and how many mice were used.

8) The choice of snRNA-seq over single-cell RNA-seq is well justified, as uniform sampling of diverse cell types is more critical for defining major cell types. However, the authors should discuss limitations of snRNA-seq in case future studies are built upon this work. For example, in cases where cells are enzymatically digestible and cytoplasmic mRNAs are of interests, scRNA-seq is a more relevant approach. It's also worth noting that the snRNA-seq approach in this work could still provide a roadmap for future scRNA-seq analyses.

9) The library preparation method should be expanded. The authors cited the 10X Genomics Chromium single cell 3' v3 kit, which may not be sufficient. Different RNA species are largely sensitive to the library preparation methods, especially for snRNA-seq. This is an essential section in the methods section that needs to be expanded.

10) In the differential gene expression analyses, is each cell treated as a replicate? If so how did the authors account for the biological replicates from different mice? How did the authors account for the dissection variation among different mice? Was there any quality controls done among different mice in the same group in terms of dissection variation?

11) Dotplots in the supplemental figure 3 lacks statistical tests and could be sometimes misleading, as the color of each dot is Z-score normalized if performed using the default setting of Seurat and could unnecessarily exaggerate an effect. The readers will benefit from some indication of adjusted p-values on the figure (e.g. asterisks). However, the authors should first clarify how different gene expression analyses were done. It would be helpful to show how a small effect size as validated in supplemental figure 4 could have so much statistical confidence as shown in the supplemental table 3.

Reviewer #1:

This study establishes fundamental information on the mouse iris and its function. Using single nucleus RNA sequencing, the authors have characterized all major cell types in the mouse iris and ciliary body, defined two types of iris stromal cells and two types of iris sphincter cells, and shown cell-specific transcriptome responses in the resting, constricted, and dilated states. They have identified and validated antibody and in situ hybridization probes for visualization of the major iris cell types. They have quantified distortions in nuclear morphology associated with iris dilation and clarified the neural crest contribution to the iris by showing that Wnt1-Cre-expressing progenitors contribute to nearly all iris cell types, whereas Sox10-Cre expressing progenitors contribute only to stromal cells. This work will be a valuable reference for investigations of iris development, disease, and pharmacology, for the isolation and propagation of defined iris cell types, and for iris cell engineering and transplantation.

This paper was a pleasure to read. It is well written, thorough, and will provide tools to study the iris and ciliary body for the research community. I had no major concerns.

Reviewer #2:

Major strengths of the manuscript:

1) Using single nucleus RNA sequencing technology had several advantages over single cell RNA sequencing with minimum disturbance of the native transcriptional profiles.

2) This research revealed major cell types in the mouse iris and provided valuable and verifiable markers for each of the iris cell types. This research generated great resources for future studies on normal and diseased irises.

3) The study showed very interesting changes in the transcriptome and nuclear morphology associated with iris dilation, and the most upregulated genes identified could be great candidates for studying iris function and malfunction in diseases.

4) The study provided definitive experimental proof showing the neural crest contribution to the various iris cell types.

Overall, the study was well designed and precisely executed, the data analysis was clear and scientifically stringent, the results are comprehensive and revealing novel molecular correlates of cellular responses.

Reviewer #3:

This work defines the mouse iris transcriptomic atlas by single-nucleus RNA-seq (snRNA-seq), an approach that captures nuclear transcripts without enzymatic cell dissociation and processing. The major cell types defined/revealed are independently and rigorously validated by immunofluorescence and fluorescence in-situ hybridization. Immunofluorescence and fluorescence in-situ hybridization experiments further confirmed distinction between sphincter and dilator muscles and revealed distinct distribution of subtypes of sphincter and stromal cells. More importantly, the snRNA-seq approach they have undertaken, though only capturing the nuclear transcripts, is sufficient to profile the transcriptomic changes during constriction and dilation, and some of the expression changes were confirmed by immunofluorescence. The identification of transcription factors associated with defined cell types also allows tests of an unexplored question- does nuclear morphology change along with known changes in the cell plasma during dilation? The authors assessed the nuclear morphology of each cell type by immunofluorescence of cell-type specific transcription factors they identified from snRNA-seq in this study, and found cell-type specific changes of nuclear morphology during dilation. Finally, the authors revisited a partially conflicting result on the neural crest cells contribution to iris cell types, with characterized transcription factors in this study to increase resolution.

Overall, this is a rigorous study and could have broad interests. This version of manuscript could benefit from more details in statistics and methodology in some analyses. Despite the insufficient technical/statistical details in some figures, the authors' major claims and the identified sub-celltypes are justified by their data.
