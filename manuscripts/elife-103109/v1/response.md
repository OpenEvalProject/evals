# Author response - Round 1

Authors:
- Jenny Chen ([ORCID: 0000-0002-6664-2597](https://orcid.org/0000-0002-6664-2597))
- Phoebe R Richardson ([ORCID: 0009-0008-5650-1556](https://orcid.org/0009-0008-5650-1556))
- Christopher Kirby ([ORCID: 0000-0001-7292-9044](https://orcid.org/0000-0001-7292-9044))
- Sean R Eddy ([ORCID: 0000-0001-6676-4706](https://orcid.org/0000-0001-6676-4706))
- Hopi E Hoekstra ([ORCID: 0000-0003-1431-1769](https://orcid.org/0000-0003-1431-1769))

## Response text

DOI: [10.7554/eLife.103109.3.sa4](https://doi.org/10.7554/eLife.103109.3.sa4)

The following is the authors’ response to the original reviews.

We thank the reviewers for their thoughtful comments.

Based on their suggestions we will:

(1) Use more accurate language to describe the hypothalamus regions under investigation in this study. While we aimed to primarily investigate the medial preoptic area (MPOA), our dissections and sequencing data in fact capture several regions of the anterior hypothalamus including the anteroventral periventricular (AVPV), paraventricular (PVN), supraoptic (SON), suprachiasmatic nuclei (SCN), and more. We will revise the language in our manuscript to reflect that our study in fact investigates the cellular evolution of the anterior hypothalamus across behaviorally divergent deer mice.

(2) Revise our language to clarify that while our study provides a rich dataset for generating hypotheses about which cell types may contribute to behavioral differences, it does not provide any evidence of causal relationships. We hope to investigate this further in future work.

(3) Clarify specific methodological choices for which reviewers had questions, especially about the hypothalamic regions for which we did histology to validate cell abundance differences and methodological choices related to mapping our cell clusters to Mus cell types.

Our responses to each reviewer’s specific comments are below.

Reviewer #1:

The major limitation of the study is the absence of causal experiments linking the observed changes in MPOA cell types to species-specific social behaviors. While the study provides valuable correlational data, it lacks functional experiments that would demonstrate a direct relationship between the neuronal differences and behavior. For instance, manipulating these cell types or gene expressions in vivo and observing their effects on behavior would have strengthened the conclusions, although I certainly appreciate the difficulty in this, especially in non-musculus mice. Without such experiments, the study remains speculative about how these neuronal differences contribute to the evolution of social behaviors.

Yes, we agree the study lacks functional experiments. We hope that the dataset is of value for generating hypotheses about how hypothalamic neuronal cell types may govern species-specific social behaviors, and for these hypotheses to be functionally tested by us and others in future work.

Reviewer #2:

Some methodology could be further explained, like the decision of a 15% cutoff value for cell type assignment per cluster, or the necessity of a multi-step analysis pipeline for gene enrichment studies.

A 15% cutoff value for cell type assignment was chosen to include all known homology correspondences between our dataset and the Mus atlas. For example, i14:Avp/Cck cells from the Mus atlas represent Avp cells from the suprachiasmatic nuclei (SCN). Though only 17.3% of cluster 15 maps to i14:Avp/Cck, we know these two clusters correspond based on the expression of Avp and additional SCN marker genes in cluster 15 (Supp Fig 6). We will further explain this cutoff in the revised manuscript.

Our gene enrichment study includes a multi-step analysis pipeline because we wanted to control for confounders that may be introduced because of gene expression level. Genes that are more highly expressed are more accurately quantified and thus more likely to be identified as differentially expressed. Therefore, we wanted to test for gene enrichments in our set of DE genes against a background of genes with similar expression levels. We will clarify this motivation in the revised manuscript.

The authors should exercise strong caution in making inferences about these differences being the basis of parental behavior. It is possible, given connections to relevant research, but without direct intervention, direct claims should be avoided. There should be clear distinctions of what to conclude and what to propose as possibilities for future research.

Yes, we agree that we are unable to make direct claims about neuronal differences being the basis of parental behavior. We will revise our language to be clearer about which relationships we are hypothesizing and what we propose as possibilities for future research.

Histology is not performed on all regions included in the sequencing analysis.

We apologize that our language describing the hypothalamic regions included in the sequencing analysis and those included in the histology is unclear. We aimed to dissect the medial preoptic region for the sequencing analysis, but additionally captured parts of the anterior hypothalamus including the paraventricular (PVN), supraoptic (SON), and suprachiasmatic nuclei (SCN), and more. Our histology was performed across the entire hypothalamus and includes all regions included in the sequencing data. We will revise the manuscript to more accurately describe the hypothalamic regions for which we investigated.

Reviewer #3:

My primary concern is that the dataset is limited: 52,121 neuronal nuclei across 24 samples, which does not provide many cells per cluster to analyze comparatively across sex and species, particularly given the heterogeneity of the region dissected. The Supplementary table reports lower UMIs/genes per cell than is typically seen as well. Perhaps additional information could be obtained from the data by not restricting the analyses to cells that can be assigned to Mus types. A direct comparison of the two Peromyscus species could be valuable as would a more complete Peromyscus POA atlas.

Our dataset reports ~1,500 genes and ~1,000 UMIs per nuclei which is indeed lower than is typically reported in other single nuclei datasets. Some of this discrepancy is due to a lower quality genome and annotated transcriptome available for Peromyscus compared to Mus musculus, which results in a lower mapping rate than is typically reported in Mus studies. However, our dataset was sufficient to identify known peptidergic cell types (Supp Fig 6) and to map homology to Mus cell types for 34 (64%) of our 53 clusters. Additionally, although some of our clusters contain small numbers of cells, our differential abundance analysis accounts for the variance in cell numbers observed across samples and should be robust against any increase in variance due to small numbers. In fact, even differential abundance of very small cell clusters such as oxytocin neurons (cell type 40) was validated by histology.

We would like to clarify that all analyses were performed on all cell clusters, regardless of whether or not they could be assigned homology to a Mus cell type. All the cell types that we identified as differentially abundant or contained significant sex differences happened to be cell types for which homology to a Mus cell type could be defined. This may arise for a relatively uninteresting reason: cell types that have more distinct transcriptional signatures will be more accurately clustered, leading to more accurate identification of homology as well as more accurate measurements of differential abundance / expression. We will revise language to make this more clear in our manuscript.

In Supplement 7, it appears that most neurons can be assigned as excitatory or inhibitory, but then so many of these cells remain in the unassigned "gray blob" seen in panel 1E. Clustering of excitatory and inhibitory neurons separately, as in prior cited work in Mus POA (refs 31 and 57) may boost statistical power to detect sex and species differences in cell types. Perhaps the cells that cannot be assigned to Mus contain too few reads to be useful, in which case they should be filtered out in the QC. The technical challenges of a comparative single-cell approach are considerable, so it benefits the scientific community to provide transparency about them.

We are not certain about why we are unable to cluster and assign homology to many of our cells (i.e. cells in the unassigned “gray blob”). However, we note that even in the Mus atlas, many cells did not belong to obvious clusters by UMAP visualization and that several clusters lacked notable marker genes and were designated simply as “Gaba” and “Glut” clusters. Therefore, it is unsurprising that our own dataset also contains cells that lack the transcriptional signatures needed to be clustered and/or mapped to Mus cell types. We do know, however, that the median number of reads/nuclei is uniform across cell clusters and does not explain why some clusters could not be assigned to Mus. We will add this information to our revised manuscript.

We do not think that a two-stage clustering (i.e. clustering first by excitatory vs. inhibitory neurons) is expected to gain power to resolve cell types in this case. Excitatory vs. inhibitory neurons are clearly separable on our UMAP (Supp Fig 7) so that information is already being used by our clustering procedure. However, we will explore this further in our revised manuscript to see if doing so will boost statistical power.

The Calb1 dimorphism as observed by immunostaining, appears much more extensive in P. maniculatus compared to P. polionotus (Figures 3 E and F). This finding is not reflected in the counts of the i20:Gal/Moxd1 cluster. The use of Calb1 staining as a proxy for the Gal/Moxd1 cluster would be strengthened if the number of POA Calb1+ neurons that are found in each cluster was apparent. There may be additional Calb+ neurons in the cells that are not annotated to a Mus cluster. This clarification would add support to the overall conclusion that there is reduced sexual dimorphism in P. polionotus.

From the Mus MPOA atlas (which includes both single-cell sequencing data and imaging-based spatial information), it is known that the i20:Gal/Moxd1 cluster comprises sexually dimorphic cells that make up both the BNST and the SDN-POA. These sexually dimorphic cells are well-studied and known to be marked by Calb1, which we used in immunostaining as a proxy for i20:Gal/Moxd1.

However, we would like to clarify that in our study, the immunostaining of Calb1+ neurons and the sequencing counts of the i20:Gal/Moxd1 cluster are not completely reflective of each other because our sequencing dataset only captured the ventral portion of the BNST. Therefore our i20:Gal/Moxd1 counts contain a combination of some Calb1+ BNST cells and likely all Calb1+ SDN-POA cells and is difficult to interpret on its own. Our histology, however, covers the entire hypothalamus and is more reliable for identifying sex and species differences in each region. We will clarify this in the revised manuscript.

The relationship between the sex steroid receptor expression and the sex bias in gene expression would be improved if the sex bias in sex steroid receptor expression was included in Supplementary Figure 10.

We will include this in the revised manuscript.

There is no explanation for the finding that there is a female bias in gene expression across all cell types in P. polionotus.

We also find this observation interesting but don’t have a good explanation for why at this point. We plan to follow this up in future work.
