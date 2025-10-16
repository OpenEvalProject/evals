# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69431.sa1](https://doi.org/10.7554/eLife.69431.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Inflammation Drives Alternative First Exon usage to Regulate Immune Genes including a New Iron Regulated Isoform of Aim2" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work cannot be considered further for publication in eLife at this time.

There was significant enthusiasm for the work. However, it seems that considerable effort including additional experiments will be required to firm up the conclusions and make the paper suitable for eLife. Accordingly we must reject the paper in its current form. Nevertheless, we encourage you to resubmit if and when you can address the majority of the reviewers' concerns. In this regard, addressing both functional relevance and mechanism would be ideal, but addressing one of these topics will be sufficient.

Reviewer #2:

Our understanding of the transcriptomic impact of innate immune signaling remains incomplete. Here Robinson et al., use both long and short read RNA sequencing to gain further insight into LPS-induced changes to mRNA isoform expression in human and mouse macrophages. Their studies report the novel observation that the most common change in isoform expression is alternative use of the first exon. Such changes are indicative of transcriptional regulation, and is thus consistent with the known impact of innate immune signaling on activation of multiple transcription factors. Despite some minor concerns with details of the study, this is a well-executed and important study that will be of interest and importance to many studying innate immunity, as well as those interested in gene regulation.

1. In some ways this is minor, but the authors should be careful to not describe alternative first exon use as alternative splicing. While a novel splice junction is created, mechanistically this is driven by changing transcriptional regulation, and then splicing occurs in the only pattern available to that TSS. In general this is described appropriately in the manuscript, but at a few points there is confusing terminology.

2. An interesting and somewhat surprising point in the manuscript is that 50% of the AFE events don't show an overall change in gene expression. For Aim2, which does change, the authors show that the AFE change is due to activated use of the unannotated TSS in LPS-stimulated cells. For those genes for which AFE use doesn't correlate with a change in gene expression (e.g. Ncoa7, Rcan1, Ampd3 – Figure S3) is there still transcriptional activation of one TSS and transcriptional silencing of the other? In other words, is there coordinated regulation of the two TSSs to ensure overall message abundance doesn't change, or does activation of one TSS inherently shut off the other (more akin to splice site competition in traditional AS)?

3. The data suggesting that an IRE regulates translation of the induced 5'UTR is compelling, but more work should be done to confirm. Most importantly, the experiment in Figure 4J should be repeated with the deltaIRE version of the unannotated UTR. Also is the IRE regulation controlled upon LPS-stimulation, or just the presence of the IRE element? In other words, what is the distribution of the annotated and unannotated isoforms in the polysome in the absence of LPS (i.e. repeat 4P without LPS)? Can the authors comment on whether the level of iron or the activity of IRP1/2 change in LPS-stimulated cells?

Reviewer #3:

This manuscript by Robinson et al. presents an interesting and timely analysis of a wealth of transcriptome data upon immune stimulation. The unique combination of long-read Oxford Nanopore and short-read Illumina high-throughput sequencing across both human and mouse samples presents an opportunity many interesting inter-species immune response comparisons, as well as elucidation of full-length transcript information. This paper is well-written and has interesting validation and discussions regarding Aim2. My major concern is that the paper seems to narrow in on the characterization of Aim2 and class of RNA processing changes (alternative first exons) quite quickly without really delving into the rest of the data and how they arrived there. Below are my major comments and suggestions:

1. I would have liked the authors to provide more insight into how they honed-in on specifically talking about first exon changes, by discussing more of the other RNA processing changes they found. There is cursory mention in the text and figures of other alternative exon or splice site changes. Firstly, other studies (including those referenced by the authors) have found hundreds RNA processing changes genome-wide upon immune stimulation – especially of cassette exons, alternative splice sites, and last exon/3'UTR changes. However here, the authors only find tens of changes (Figure 1B). Are they underpowered to identify changes and can they do any sort of analyses to show that they are sufficiently powered (# of sequencing reads and junctions, complexity of reads, etc)?

2. Similarly, I would also be interested in seeing an analysis indicating whether the 50 AFE events that overlap between the long-read and short-read sequencing analyses is a statistically significant overlap. Particularly, how many overlapping events would be expected given the difference in quantification power between the two methods? How many real AFE differences might the authors be missing because the long-read sequencing methods often do not have the power to identify them (ie. lower expressed genes in one or the other condition, thus dropout of isoforms and perhaps fewer isoform differences for differentially expressed genes).

3. Second, for the non-AFE changes that they did find, there is very little discussion about what those changes might represent. Specifically: (a) how many changes are validated with long-read data?, (b) is there any insight into specific domains being included/changed, especially using the long-read data?, (c) how many of these non-AFE changes overlap between species? and (d) which types of genes show higher overlap between species and what are their characteristics (binding sites, etc)? To my knowledge, this is the first study that is really designed to properly really look at the conservation of splicing or RNA processing changes after immune activation, so I would love to see more analysis and discussion of this aspect genome-wide.

4. The authors define significant splicing changes as those with a p-value <= 0.25 and |dPSI| >= 10. I'd like some more clarification on whether this is an adjusted p-value (BH, FDR, or some other multiple test-corrected p-value). Especially if this is adjusted, I find it surprising that the authors are choosing such a liberal statistical confidence level and that even with such a liberal threshold, they are only getting tens of significant events. I would like the authors to at least show these same trends across multiple p-value thresholds or with rank threshold analysis (top 5%, top 10%, top 20%) to show biological trends.

5. The authors introduce their long-read sequencing data by mentioning that they wanted to identify "additional splicing events that are not captured using short-read sequencing." They then go onto to only talk about novel first exon events identified with the long-read sequencing data. Did they identify any other non-AFE events in using the long-read that could then be quantified with the short read data? And second, how do they quantify confidence for novel AFE isoforms, when long-read data seems to have lots of issues with properly sequencing the terminal ends of transcripts (particularly the 5' end when polyA primed, as occurs in ONT DirectRNA sequencing)? They mention the use of ATAC-seq data to show putative promoter support, but mention at one point in their methods that ATAC regions within 10kb of AFEs are considered. These seems like it could be a rather large region to be sure that the ATAC peak is specific to a novel AFE – what is the average distance between AFEs? Finally, I would love to also see the incorporation of CAGE-seq data (or other 5'end data) to validate the specific AFEs sites – which I believe the FANTOM consortium has across many human and mouse tissues.

Reviewer #4:

In this manuscript, Robinson et al., identified alternative first exon (AFE) switching events conserved between mouse and human following macrophage inflammation. Using short and long-read sequencing, the authors identified a few unannotated transcription initiation sites (TSS) that are specific of an inflammatory response. Among those, they centered on an unannotated TSS in the Aim2 gene that drives expression of a novel isoform regulated by an iron-responsive element in its 5′UTR.

While previous work had documented crucial AFE switching events in many other biological contexts, Robinson et al. presents here an interesting AFE switching event that can have potential implications for our understanding of the molecular regulation of the innate immune response. For publication in eLife, I would expect further progress on global mechanisms and biological relevance of these AFE switching events, as well as evidence that the AFE are truly first exons/TSSs.

1. Are the AFEs truly first exons/TSS? While both short-read and long-read sequencing detected changes in alternative splicing choices, neither of those are optimal methodologies to analyze first exons. Therefore, I suggest to use a more specialized method to identify (and quantify) more accurately the usage of first exons. Globally, cap analysis of gene expression (CAGE) would be ideal. For validation of specific AFE changes, the qPCR technique has a few issues. First, it does not have nucleotide resolution, so the authors should not refer to TSSs if they used this technique for validation. Second, many downstream first exons are also used as internal exons in other isoforms. There is not a direct technology to analyze specifically first exons/TSSs here. Also, RNA-sequencing technologies, depending on their depth, can definitely miss specific isoforms. Considering a low coverage in 5'end of genes in RNA-seq analysis, this is particularly important for first exons. A qPCR would only analyze the well-known TSSs. Thus, 5'RACE or a similar technology should be perform to assess the relative usage of AFE specifically.

2. Global mechanism. The authors assumed that the mechanism of AFE switching is generated by transcription initiation and looked for transcription factors binding and chromatin structure modifications in promoters. However, they did not ruled out the possibility that the global switching effect is a post-transcriptional regulation, such as differential mRNA stability. A transcription initiation measurement (e.g., 4SU metabolic labelling) is necessary to demonstrate that the changes in AFE usage are co-transcriptional. In addition, in terms of their ATAC-Seq analysis, the chromatin structure changes in promoters can be cause or consequence of transcription initiation. Thus, it should not be listed as one mechanism driving the expression of AFE events (line 145). Also, to demonstrate a mechanism based on transcription factor binding more than 2 transcription factors should be considered. In any case, the expression patterns of the transcription factors considered are not clear. As a minor note, the bioinformatic analysis of the two promoters regions driving the isoforms of Aim2 (line 156) is not explained in the method section.

3. Biological relevance. Could the authors evaluate whether the translation regulation of Aim2 based on its AFE switching is a more generalized phenomenon? Are there any global gene regulation changes triggered by the other genes with significant changes is AFE usage?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Congratulations, we are pleased to inform you that your article, "Inflammation Drives Alternative First Exon usage to Regulate Immune Genes including a Novel Iron Regulated Isoform of Aim2", has been accepted for publication in eLife. Your revised article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Reviewer #1:

I appreciate the authors' efforts to address the issues of global mechanism and biological relevance, as well as other points raised. This new version of the manuscript is significantly stronger and it represents an important contribution to the literature. However, I still have concerns about the evidence the authors present to demonstrate that the AFE are "true" first exons/TSSs.

In my previous report, I suggested the authors use CAGE instead of RNA-seq (either short or long-reads) and 5'RACE instead of qPCR, both specific techniques to analyze first exons/TSSs. In this version, the authors used CAGE data from the FANTOM project to classify their first exon calls as "true" TSS. They found that only 45% of the novel TSS identified overlap with CAGE peaks. In my opinion, this raise the possibility that the other 55% are not "true" TSSs. Further, before publication, I would expect 5'RACE or any other direct method to validate that specific TSS are "true" TSS, at least for Denr, Arhgef7 and Aim2 which they validated using RT-qPCR.

Reviewer #2:

1. While the authors have now included a brief discussion about whether AFEs are regulated by transcription, splicing, or both in their discussion, I still think the authors should tone down the mechanistic implications of the language throughout the rest of the text, perhaps use the term "alternative RNA processing changes" instead of "alternative splicing changes"?

2. The authors mention that they implemented a new parameter in their FLAIR analysis to incorporate a bed file of ATAC annotations to calibrate the identification of novel AFEs. Do the authors plan to release this new parameter as an update to their existing software? I think this would be of great use to the community that analyzes long-read RNA data.

Reviewer #3:

The authors have fully addressed all of the concerns raised by adding additional data. This enhances the significance of the work and strengthens the conclusions.
