# Peer review - Round 1

Editors:
- Shahragim Tajbakhsh, Institut Pasteur France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51576.sa1](https://doi.org/10.7554/eLife.51576.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors have done an impressive work in revising the manuscript substantially, adding a substantial number of human samples that allowed a more comprehensive analysis of human muscle satellite cells. Of note, human satellite cell subpopulations are described that are Cav1+ and Cav1-, and transplantations of these cells in mice showed a greater engraftment potential of the Cav1+ subclass. In summary, these findings provide a valuable resource for the community.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Functionally heterogeneous human satellite cells identified by single cell RNA sequencing" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Bradley B Olwin (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews, we regret to inform you that your work will not be considered further for publication in eLife.

In this study, the authors combine single cell RNA sequencing and flow cytometry to analyze human satellite cells isolated from skeletal muscles. A single sample from a middle-aged adult (56y old) and from an aged adult (86y old) were subjected to single cell sequencing. They report that the SCs contains transcriptionally distinct subpopulations. Using pseudotime analysis, they show that myogenic cells can be ordered into various state, from quiescent stem cells to more differentiated progenitor cells. Genes such as DLK1, ICAM1, CYCS and VCAM1 are differentially expressed in human SCs and VCAM1 expression is increased in human SC isolated from aged muscle. They also identify Caveolin1 (CAV1) as a cell surface marker to sort the more quiescent human SCs (CAV1+) and following their transplantation in immunodeficient mice, report a better regeneration compared to CAV- cells.

Therefore, this study identifies some differentially expressed markers and properties that bring some new knowledge to the field. However, some of the analysis and interpretation of the results needs attention (see below). The reviewers understand the challenges involved in analyzing human samples, however, given the small sample size and the fact that only a portion of a muscle is taken for analysis, it is unclear how widely applicable these observations will be. The reviewers feel that the amount of work that will be required to verify these findings will not reasonably fit within the context of a revision. Therefore, publication of the study in its current form in eLife is not recommended.

Essential revisions:

1) The study comes from analysis of one individual (1 – 84-year old, 1 – 56-year old), therefore, 84-year old specific clusters should not be generalized to aging muscles. The authors are also comparing 2 different muscles between adult and aged (rectus femoris and vastus lateralis) which impact the interpretation of the results due to known inter-muscle heterogeneity.

2) In 2 recent papers (Vartanian et al., 2019; Scaramozza et al., 2019), Pax3 was shown to be expressed and enriched in a minor subset of murine Pax7+ SC, conferring functional heterogeneity in SC population. Have the authors evaluated Pax3 expression in the distinct subpopulation of human SCs? Such data could be added in Figure 1 or at least mentioned in the Discussion section.

3) It was shown (Machado et al., 2017) that quiescent muscle stem cells undergo major transcriptomic alterations during the isolation process, enough to induce biochemical changes. The use of the term "quiescent" throughout the paper should be qualified, since the authors do not address the issue of quiescence of freshly isolated human SC, or show that SCs are in G0.

4) Concerns regarding heterogeneity: one might expect heterogeneity in the SC population as some would respond to exercise or injury and some part of the population would be quiescent. None of the data provided disproves that what the authors observe is simply a continuum of SC behavior and the heterogeneity is a result of cells in continuous flux. Biological replicates, perhaps obtained from the same individual and different muscle groups, would help to address this issue. The data as presented in the manuscript imply that separable and heterogeneous SC pools are present, while a counter argument is that this is simply a continuum in constant flux.

5) Also, are SCs present that are not isolated as their relative expression of CD56 and CD29 are low? Does single cell sequencing of the entire mononuclear cell population from muscle corroborate the heterogeneity data presented? How does flow cytometry affect gene expression in SCs? It is possible and even likely that the heterogeneity observed could in part be derived from the isolation and sorting of SCs.

6) The scale is lacking in all the immuno-fluorescent pictures shown in Figure 2, Figure 3, Figure 4 and Figure 5 and/or in the figure legends.

7) The method used to merge the data might be problematic: normally, when data come from the same 10x chip and from the same sequencing lane (which is the case in the experiment) the Seurat MergeSeurat function is sufficient. However, in Figure 3E, there is a clear separation by individual. Specifically, subsection “VCAM1 is differentially expressed on satellite cells of aged muscle in single cell transcriptomes and in vivo”, there is mention of a batch effect correction without mentioning which one was used. Authors should also try the MNN (Mutual Nearest Neighbors) and/or the CCA (Canonical Correlation Analysis) algorithms to see if these could help in correcting the batch effect.

8) Cluster 4 in the 84 year-old individual looks like it contains a little bit of everything, which can fit what we know about evolution of transcriptome regulation during ageing. But it can also arise from bad quality barcodes i.e, no cell, specially knowing that the authors chose to set a very low number (200) of expressed genes in their analysis, these can also correspond to barcodes with too many genes expressed (information about this cutoff is missing) which can correspond to doublets.

9) Figure 1D and Figure 3C: According to the size of the dots on the Dotplot (showing normalized proportions, and not% of Expression as indicated), only 20-40% of satellite cells seem to express Pax7. The authors should comment on this point to place the work in the context of the mouse and could provide a tSNE plot of Pax7 expression across all 5062 cells. Is this due to a possible lack of sensitivity in the sequencing?

10) Figure 1G and H: Pseudotime is used to compute artificially the progression of a lineage through differentiation (during embryonic development or adult stem cells). Monocle 2 analysis here brings confusion to the results: cells belonging to the "satellite cells" clusters appear on the same "branch" as mesenchymal cells and have a lower pseudotime, as if they were progenitors of these cells. By representing their data in this fashion, the authors imply that these cells belong to the same lineage in human resting muscle (satellite cells differentiating into mesenchymal cells). If the authors want to show progress through myogenesis, they need to perform this analysis on myogenic cells only, excluding fibroblastic cells (clusters 0,1,2,3,4,6).

11) The authors claim a progression through myogenesis from cluster 0,1,2 to 4 and 6. However the t-SNE plot shows a very nebular distribution of these populations, especially a closer transcriptomic proximity of clusters 1, 4 and 6 as opposed to 3. Removing fibroblastic cells in this representation could allow better highlight of intra-myogenic transcriptomic diversity and similarity.

12) Figure 1C is hard to read (and not convincing). Combining Figure 1D and E would be more informative.

13) Figure 3D: How was this correlation performed? The correlations of cluster 4 of the aged are quite similar to the correlations found in clusters 0, 1, 2 and 3.

14) Figure 3E: The merged data shows multiple clusters primarily made of either Aged (clusters 4,6) or Adult (2,3 and 5) cells. How do the authors explain such differences when correlations shown in Figure 3D seem so high? Why did the authors focus on cluster 6 specifically when numerous clusters do not match? Displaying the proportion of cell origin for each cluster would be informative here to assess this mismatch.

15) In Figure 3G, please provide a better image for Pax7/VCAM1 expression to support the conclusion that VCAM1 is express more frequently in SC of aged muscle (images at lower magnification).

16) Can the authors provide measurements of UMI counts, gene counts and cycling score for each cluster? These variables are often found to influence clustering analysis and did not seem to have been regressed out during scaling of the data, judging by the Material and methods section.

17) Figure 4B violin plots seem to suggest a high expression of Myod1 and Myf6 in the Hey1+/Spry1+ population which is the opposite of what the authors claim.

18) Given that the isolation strategy the authors used also captures mesenchymal cells, Cav1 may be expressed preferentially in myogenic cells, thus enriching the myogenic yield of the isolation approach, independently of a more "quiescent" state of satellite cells. The authors need to show that Cav1 does not preferentially select the myogenic compartment.

19) The point concerning the robust engraftment of CAV1+ human SC should be extensively discussed in regard to the numerous papers describing human myogenic stem cell engraftment after in vivo implantation in immunodeficient mice. Could you also clarify if injected human SC are isolated from the same donor? By flow cytometry, the CAV1+ SC represent 51.6% of the CD29/CD56 population (Figure 5). It would be interesting to know the percentage of the CAV1+ SC related to the live cell population (FSC/SSC gated population) obtained after muscle dissociation.

20) Also, regarding the CAV1+ population, in Figure 4D, this population appears to be 80% of the SCs. When sorted, the percentage drops, which is not surprising due to the harsh conditions encountered when sorting cells. Thus, this population simply represents most SCs with a subset exhibiting poor engraftment. There have been a number of publications demonstrating that good engraftment can be achieved even with low numbers of SCs by sorting for specific markers, by transplanting intact myofibers, by transplanting SCs in engineered gels, or by the use of specific inhibitors to maintain SCs in quiescence upon isolation. They should refer to Arpke and Kyba, 2016 and 2012 which demonstrate that small numbers of cells are effective for transplantation.

21) The images provided in Figure 5E where few of the human spectrin lamin a/c+ cells appear as SCs, the majority appear interstitial in the provided image. Few are Pax7+ and thus, it is difficult to determine how the quantification was performed. Insufficient experimental detail is provided to assess which cells were transplanted and how the cells were derived. Are the biological replicates referred to in the figure from 3 different human individuals or are these 3 samples from one individual? If from one individual, then these are not biological replicates but technical transplantation replicates. The figure title states transplantation is robust and the data show the numbers of transplanted myofibers that are dystrophin+. However, if the data were plotted as a percentage of the total myofiber number in the TA muscle it is unclear how robust the transplantation is as 75 dys+ myofibers/~3500 myofibers per TA is ~2% of the total. If plotted as a percentage of the total myofibers per TA muscle or as a total of the SC number per myofiber are the data sufficient to establish that they are significantly different between the samples?
