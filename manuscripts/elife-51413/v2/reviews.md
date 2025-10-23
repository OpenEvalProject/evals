# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51413.sa1](https://doi.org/10.7554/eLife.51413.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this study, the authors have uncovered a complex organ-specific transcriptional pattern in the vasculature. Interestingly, endothelial cells were found to express genes that normally are associated with the parenchyma cells of the organ examined, speaking for a high degree of plasticity. In the revised version, the authors have addressed the remaining comments and criticisms. A key improvement is the inclusion an extensive comparison between their data and two published scRNA-seq data sets. The paper will be a useful resource for scientists interested in vascular biology.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Endothelial heterogeneity across distinct vascular beds during homeostasis and inflammation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers, who were uniform in their view. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Though the reviewers recognized the importance of endothelial heterogeneity and the utility of the RiboTag approach, the potential cross contamination issue raised by reviewer 3 was a particular key concern for all three reviewers.

Reviewer #1:

The authors have used RiboTag purification of protein encoding RNA to characterize bulk gene expression in Cdh5-Cre expressing endothelial cells from the brain, heart and lung. The methodology is sound and the results nicely presented. The major question raised is simply what is the value of this study for the field? There are technical and conceptual limitations that argue the value is limited. First, while the study addresses general, inter-organ endothelial heterogeneity between heart, lung and brain, the approach of bulk RNAseq fails to address the high level of intra-organ heterogeneity, i.e. differences between endothelial cells in arteries, veins, capillaries, venules etc. Given the strength of single cell sequencing to address both of these issues simultaneously, the value of this approach seems limited. Second, the authors do not draw significant new biological insights from the data they have harvested. They discuss general points such as the top 10 genes expressed in the bulk endothelial populations from the different organs, but what this means for organ function or organ-specific vascular function is not pursued or validated in any specific manner. Finally, the inflammatory studies are limited to responses to LPS, a stimulus that is certainly inflammatory but laboratory-based and not easily translated to actual disease states. Overall, this study could provide some value as a resource if an excellent and highly accessible website were designed to do this (e.g. the Betsholtz site for brain endothelial gene expression (http://betsholtzlab.org/VascularSingleCells/database.html); otherwise its value does not seem adequately significant compared to existing single cell-based databases that already exist.

Reviewer #2:

The manuscript addresses the theme of heterogeneity of the tumor vasculature in lung, brain and heart. The authors sought to isolate cell-type specific ribosomes by Ribo-Tag methodology (Sanz et al., 2009), followed by RNA-seq. They uncovered a complex organ-specific transcriptional pattern in the vasculature. Interestingly, endothelial cells were found to express genes that normally are associated with the parenchyma cells of the organ examines, speaking for a high degree of plasticity. The authors also examined the transcriptional pattern following LPS administration and slow found interesting signatures.

The study seems technically well executed, addresses a timely and important topic, and some of the findings are interesting. Unfortunately, the manuscript, in the present form, is like many papers already published using single cell RNA-Seq, entirely descriptive and providing lists of genes without any functional data.

If the authors were able to provide functional validation some their signature and show that their analysis is informative in some disease models, the manuscript would be much more interesting.

Reviewer #3:

The authors have used genetically controlled RiboTag sequencing to analyze and compare the transcription profile of endothelial cells (ECs) from different organs. The RiboTag approach circumvents intrinsic limitations of other gene expression analysis strategies, such as alterations due to tissue dissociation or flow cytometric sorting, but it involves immunoprecipitation, which can result in noise caused by pull-down of unspecific RNAs especially when expression of the tagged ribosomal protein is confined to a small fraction of cells. In this context, it is certainly critical to assess whether ECs indeed share the expression of genes with cells from the surrounding organ. The authors suggest that this applies to metabolic signatures and transporters but, for the example of brain ECs, also to genes related to "neurotransmitter transport" or "synapse organization". Here, it is obviously puzzling that completely different cell types, namely neurons and ECs, would share very specialized transcripts relating to neuronal function. Fortunately, single cell RNA sequencing, which has its own limitations, can be used to confirm the observations made by the authors in an independent fashion and exclude cross-contamination effects seen in bulk sequencing or RiboTag data. Performing this test to the top RiboTag brain EC signature genes (Figure 3C) with the single cell database for heart and lung (http://betsholtzlab.org/VascularSingleCells/database.html; Vanlandewijck et al., 2018) shows that Ptgds is expressed by oligodendrocytes and fibroblasts but not ECs in brain. Atp1a2 is expressed by mural cells and fibroblasts but not by ECs. Ptn and Actb are widely expressed by many different cell types. Apoe, Apoe and Igf2 expression is absent from ECs, whereas Bsg and Spock2 show indeed substantial endothelial expression. Thus, even at the level of this superficial validation, EC expression can be only confirmed for 4 out of 10 genes.

As the Betzholtz database includes lung data, I have performed a similar test for the lung EC signature genes listed in Figure 4C. No or only very low endothelial expression can be seen for Sftpc (an epithelial marker), Ager, Wfdc2, Muc1, and Lyz1. Retnla and Hoxa5 are not covered by this dataset, while the other 3 genes show spurious endothelial expression.

Even if one takes into account that the authors have performed some computational tests (see Figure 2A) and tried to exclude that contamination is the cause of their organ-influenced EC signatures, the comparison with scRNA-seq data indicates that the opposite is the case. It has to be taken into account that the RiboTag is not protected against cross-contamination similar to immunoprecipitation experiments with proteins, which easily pull down highly abundant cytoskeletal proteins irrespective of the primary antibody used. During tissue lysis in the RiboTag protocol, certain transcripts from surrounding non-ECs may more easily end up as contamination than others, which might reflect differences in RNA structure, stability or association with RNA-binding proteins.

It is noted that the authors have used EC single cell data from the Tabula muris compendium in their analysis. Here they see some similarity with their own RiboTag data on the level of GO terms, but, unfortunately, the analysis stops here and individual signature genes are not validated.

Taken together, I am not convinced that the RiboTag data presented in the manuscript offers new and unexpected insights into organ and EC-specific gene expression. Instead, the purity of the RNA-seq data and its interpretation appear highly problematic so that I cannot recommend publication of this manuscript.
