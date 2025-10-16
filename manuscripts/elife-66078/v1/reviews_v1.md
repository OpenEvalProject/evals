# Peer review - Round 1

Editors:
- Lilianna Solnica-Krezel, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66078.sa1](https://doi.org/10.7554/eLife.66078.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript investigates specification and differentiation of the neural crest, a migratory population of stem-like cells that contribute to multiple tissues, including the bones of the skull, pigment, and peripheral nervous system. This work presents a single-cell RNAseq dataset from zebrafish trunk neural crest cells during the early stages of migration that identifies the subpopulations of trunk neural crest cells, new genetic markers and a subset of Rohon-Beard neurons. The paper generates a dataset for further investigations and reports expression of differentiated pigment cell markers in the pre-migratory neural crest populations.

Decision letter after peer review:

Thank you for submitting your article "Single cell RNA analysis identifies pre-migratory neural crest cells expressing markers of differentiated derivatives" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard White as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor who also read the manuscript, has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should more clearly state how this study advances their past work that demonstrated the presence of HNK1+ (NV migratory marker) RB neurons in a well-characterized pdrm1 mutant (Hernandez-Lagunas et al., 2014).

2. Reviewers were also concerned that such an analysis performed at a single stage and at a relatively late time point cannot be used to infer common developmental origin or path. This raises questions about the identification of both sox10+ and sox10- RB neurons – both of which are lost in pdrm1 mutant – this finding should be more fully addressed appropriately.

3. Reviewers felt that there is a disconnect between the title and what forms the bulk of the discussion and figures in this paper. The authors should either change the title or put more emphasis on the findings that premigratory NCCs express markers of differentiated derivatives.

4. A stronger attempt should be made to compare/integrate their limited dataset with other more extensive existing datasets (Wagner et al.,2018) to investigate whether markers (fgf13a, cxcr4b) are expressed at earlier time points to help support the authors' hypothesis? Similarly, the authors do not seek to utilize single-cell datasets at later time points obtained using the same transgenic line to verify whether these markers are expressed (Aubrey et al., 2021). Further mining and integration with available datasets would help strengthen the authors' point.

5. When discussing their finding that some premigratory cells already express differentiated genes as a novelty but, the authors should cite studies that have shown this in the neural crest in zebrafish and other models (Soldatov et al., 2019, Ling et al., 2019).

6. The "unknown" cluster 7 described by the authors as a potential new NCC lineage cluster is most likely (authors should verify this) a previously reported mesenchymal cluster expressing a wealth of collagen genesl; this should be verified and rectified.

7. The claim 'Some of 156 cells (Cluster 5) are presumably neural tube tissue' is unclear, as sox10 found in Cluster 5 does not label neural tube. What are the Cluster 5 marker genes; they should be shown as Supp. Figure 1. Cluster 5 also seems to be split into two subclusters. Do different genes mark these regions? The authors should elaborate on the differential split of sox10-expressing and non-expressing cells within the cluster (feature plots in 1F indicate that sox10 is downregulated in the top left portion of this cluster and the RB cluster).

8. One of the primary novelty points emphasized by the authors is the subset of RB neurons. If this is to be confirmed, the authors should perform KO of some of the known marker genes specific to this cell population to show their relevance to RB cell development? What role do these subsets of NCC-RB cells play? While this experimental work is not essential, in the time of CRISPR/Cas9, querying such candidates in F0 generation would significantly strengthen the manuscript.

9. Important technical points: The study lacks sufficient information to verify the data quality and level of rigour in the analysis. For instance, information such as the number of embryos used to get 607 cells should be provided (this is important for defining genetic heterogeneity). What proportion of embryos were 20hpf and 24hpf? How many cells were loaded into the channel? What was the mean number of genes and UMI's were found per cell? How was the analysis performed, what were the parameters/cut-offs used? How many cells are found within each cluster? Furthermore, the data is not always of the highest quality, and figure annotations should be improved. In general, figures need better annotation and precision – indicating developmental stages on HCR images, the section's location, and clarifying the number of sections used for quantification. Also, figure legends should clearly describe annotation detail.

10. Figure 1 Supplement 1 while very visually appealing, it could have a stronger information content. The authors might consider presenting these results in the form of a dot plot (see Seurat function DotPlot), which in addition to conveying the 10 strongest markers of each of these clusters, would also provide information about (a) their expression level and (b) how specific they are to a particular population that might be helpful to readers. Additionally, the authors might consider adding something that presentation about which of those markers are novel, versus which are well established markers of these cell types. This could even be suitable for promotion into main figure 1, as it would add a lot of information content for readers interested in the neural crest and would clarify the novelty of the authors' findings.

11. The presentation and validation of the pair of novel markers for both the xanthophores and Rohon-Beard neurons are very compelling. However, it seems like there is a missed opportunity here to present more of the novel expression findings in a way that is accessible to a broader audience. While it would certainly be unrealistic to validate them all, it seems like it would be very valuable to provide a broader presentation of the convincing novel markers identified in these populations via differential expression as a figure (or figure panel) – perhaps dot plots or some other format.

12. Lines 217-218 "While we cannot rule out that RB neurons are represented in our dataset due to the proximity of RBs and NCCs to each other in the neural tube". Whereas the presentation in Figure 3g, h that sox10::RFP labels some Rohon Beard neurons is convincing, the authors could go one step further – as they point out, the most likely other potential explanation would be that some of these represent doublets, where an RB neuron and another cell ended up in a droplet together perhaps due to imperfect dissociation. A fairly simple analysis that would help further exclude this possibility would be to simply check whether any of the cells identified as RB neurons express markers that are exclusive markers of another cell type in the dataset that is expected to be sox10+. If they do not, then they are unlikely to represent a combination of two cells. (This could be done in fancy ways, but also simply by checking in scatter plots or some other format the expression of the best markers of other clusters in the RB neurons.) It would provide an additional piece of strong evidence that some RB neurons must have expressed sox10 at some point in their developmental history.

13. That some cells prior to migration express markers of pigment cells is convincingly demonstrated. One is left wondering – do the authors think that ALL pigment cells begin to express their markers prior to migration? Are all of the migrating tNCCs that are not expressing cell-type specific markers bound to become PNS derivatives? If there are data from sox10 lines that perhaps estimate the percentage of cells that give rise to these different cell types. The authors could make statements in the Discussion section to help clear this up.

14. The authors note expression of fgf13a in the RB neuron cluster and comment that "FGF and chemokine signaling are critical for proper morphogenesis.." and later "The RBs are apparently sources of and responsive to morphogens important for development. The authors need to reconsider this interpretation of fgf13 expression in RBs, as Fgf13 belongs to the class of intracellular FGF, iFGFs, which are not secreted and have no identified interaction with signaling FGFRs (Ornitz DM, Wires Dev Bio, 2015).

15. Discussion could have more explanation or speculation about why only NCCs expressing pigment cell markers are observed prior to migration.
