# Peer review - Round 1

Editors:
- Richard Amasino, University of Wisconsin Madison United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61894.sa1](https://doi.org/10.7554/eLife.61894.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your paper describes the global epigenomic and transcriptomic changes that occur during Arabidopsis pollen development and provide a first glimpse of the genomic changes associated with the diploid-to-haploid transition in plants. This paper will be of particular interest to scientists working on plant reproduction, but also to a wider audience in the context of studies of sexual reproduction.

Decision letter after peer review:

Thank you for submitting your work entitled "Distinct epigenetic reprogramming events rewire transcription during life cycle transitions in Arabidopsis" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Richard Amasino as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Christian Hardtke as the Senior Editor.

The reviewers and Reviewing Editor have discussed the work with one another. Your paper is a high-quality study that addresses the important question of cell-type specific differences in gene expression using differential accessibility as a probe. However, there are some major issues that would need to be addressed for this work to be suitable for eLife.

One is to define the changes in chromatin accessibility during pollen development by including ATAC-seq data from bicellular microspores rather than focusing on comparisons with sister somatic cells.

The second is to perform chromatin accessibility assays in cells from dme2/+ pollen because the role of DME in rendering accessible the regulatory regions of genes that regulate pollen tube growth is currently based on correlations not supported by any experimental data.

The third is that the interpretations often extend beyond what is warranted by the data.

Below we provide more details on these issues, and we hope you find the efforts of the reviewers helpful.

As the editors have judged that your manuscript is of interest, but that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Essential revisions:

1) The study is incomplete as the most critical stage in pollen development – the bicellular microspore stage (which encapsulates the initials of the two germ cell lineages), has not been included in this analysis. This is surprising considering that this stage is critical for male gamete and pollen development (as the authors also state in the manuscript), and that this experiment is technically feasible.

2) Comparing chromatin dynamics between two epidermal root cells and two pollen cells is not a valid argument to support the view that "haploid development" is not a result of cell differentiation. To address this point, authors should conduct a detailed analysis of all cell types at the three stages of pollen development.

3) The role of DME in poising accessible regulatory regions for the transcriptional events that regulate pollen tube growth should be validated experimentally. Authors should also perform chromatin accessibility assays in VN and SN using dme2/+ plants to confirm their hypothesis.

Similarly, the impact of DNA methylation at transcription factor binding sites that overlap with DME targeted ACRs should also be experimentally tested. Some of the correlations are weak and without experimental validation, their hypotheses are largely speculative.

4) The most significant comment is the conclusion that "epigenetic reprogramming" is deterministic instead of differentiation. The evidence to support this claim is that thousands of differential ACRs are identified in the VN, MN or the SN, but not between root hair and non-hair datasets. This is a strawman argument, that is built upon a negative result. Although it is true that the "hair" and "non-hair" datasets do not show differences in accessibility, it is likely a reflection of the lack of purity of these cells. Two recent single cell ATAC-seq studies using Arabidopsis somatic tissues were published on bioRxiv (Dorrity et al., 2020 and Farmer et al., 2020) and both show substantial variation of cell type specific differential accessibility. Furthermore, published studies comparing maize tissues from a couple of labs have shown thousands of regions of differential accessibility. Therefore, selecting to compare root hair and non-hair to support this major claim in the study is not advised. I believe focusing on what the data do show is actually significant enough for publication, without overinterpreting the results.

5) The evidence that regions that become accessible in the VN lose H3K9me2, siRNAs and DNA methylation requires additional analysis. Currently, the data are averaged for all regions. How many VN ACRs have H3k9me2, siRNAs, DNA methylation in somatic cells? What proportion of these actually lose H3k9me2, siRNAs and/or DNA methylation. One way to show this result is to take Figure 2C and create a heatmap where all the VN ACRs are rows and the columns are data for H3K9me2, CG, CHG, CHH, 20, 21, 22, 23 and 24 nt siRNAs. This would allow the reader to evaluate how many actual regions are enriched for these data.

6) Figure S2A does show high reproducibility, but correlations of 1.0 should not exist. These correlations show that read coverage per window is the same. If the windows are large enough the actual peaks do not have much influence over the result. For all replicates, please report the number of ACRs identified and their overlap of ACRs between each replicate. You could also consider using IDR.

7) The y-axis for enrichment in 2C is very small indicating enrichment is not as prevalent at these loci as the authors have presented.

8) The pollen data in 2G doesn't show enrichment of siRNAs. 20 nt siRNAs are not known to have a function, yet they are accumulating to greater levels than 22-24 nt siRNAs.

9) Evaluate if the siRNAs are siRNAs and not mRNA degradation products. This can be done be showing the siRNAs from individual regions are aligning to both strands of DNA instead of being derived from a single strand. This would explain the lack of enrichment of expected siRNA sizes and the over enrichment of classes that are not known to have function (20 and 25 nt siRNAs).

10) I really like the section of TF motif enrichment in these cell type specific ACRs. Given the purity and high-quality nature of the data, the authors should consider using DNA footprint analysis, which usually plagues bulk tissue data. It might provide more specificity that using the entire ACRs.

11) What are the negative controls used to identify TF motif enrichment in ACRs?

12) Figure 5A needs to control for gene length. Long genes will show more discrete H3K4me3, whereas short genes will short more enrichment over gene bodies.

13) The idea that chromatin accessibility in sperm is poised for sporophyte development has been previously proposed by the authors (Borg et al.,2020) but the data presented in this manuscript does not provide direct evidence to support this hypothesis.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting the revised manuscript of your work entitled "Distinct epigenetic reprogramming events rewire transcription during life cycle transitions in Arabidopsis" that addresses most of the issues raised in the first submission. There are a few more items from the review of your revised manuscript, that we would like for you and your co-authors to consider and respond to.

It would be a more useful contribution to literature if you would provide the Venn diagrams of ACRs between the individual samples prior to merging the replicate data. Your reason for not showing this was that the Spearman correlations were so high that it was unnecessary. However, adding the data for each replicate would permit the reader to appreciate the variability in the data. The addition of the FRIP scores in Figure S3 shows quite a bit of variation between samples. Although this doesn't invalidate the major conclusions of this study, the variability should be better acknowledged. Showing overlap of ACRs from individual replicates with and between samples is one way to do so.

The addition of the heatmap to Figure 2 is much appreciated. However, it shows that the majority of ACRs do not possess H3K9me2 and/or siRNAs in leaf tissue. This result does not invalidate conclusions, but this is important to note in the main text. In particular, note how many ACRs overlap and H3K9me2 region and make it clear to the reader that only a minor number of ACRs in the VN are affected.

The conclusion that there are thousands of differential ACRs during this developmental progression as compared to somatic tissues based on published ATAC-seq data is not likely to hold up over time. Published studies are limited in their data analyses preventing accurate identification of cell-type-specific ACRs. The limits of other published studies are in contrast to your work and perhaps you do not want to appear critical of other studies, but your work would be a better contribution to the field if it was made clear that the major rewiring of cis-regulatory elements that you have observed in the haploid phase of the life cycle may very well occur in other phases of development when cell-type-specific methods and more sophisticated data analyses are applied.
