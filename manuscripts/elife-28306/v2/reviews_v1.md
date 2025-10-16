# Peer review - Round 1

Editors:
- Danny Reinberg, Howard Hughes Medical Institute, New York University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28306.058](https://doi.org/10.7554/eLife.28306.058)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Defining the location of promoter-associated R-loops at near-nucleotide resolution using bisDRIP-seq" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As stated by the reviewers the new method to map the position of R-loops at higher resolution than existing techniques is important to the field. The approach entails converting cytosines to uracils in the displaced DNA strand with bisulfite, while the cytosines in the opposite strand are protected by RNA. However all reviewers felt that it is crucial to include an RnaseH control. In addition since this is a methods paper it is necessary to discuss the differences and advantages of the reported method to those that have been previously developed and how the method and/or results represent a significant advance over the literature. We look forward to see an improved manuscript.

Reviewer #1:

R-loops are three-stranded structures consisting of a DNA-RNA hybrid and a displaced single-stranded DNA. R-loops are involved in multiple cellular processes, including mitochondria DNA replication, immunoglobulin class switch recombination, and transcription regulation. However, when dysregulated, R-loops could challenge genome integrity by introducing mutations, single-strand breaks, stalled replication forks and double-strand breaks. Precise genome-wide mapping of R-loops may provide insights into their functions and dynamics.

In this manuscript, the authors developed a new method to map R-loops at near-nucleotide resolution. Their new method, named bisDRIP-seq, takes advantage of the unique three-stranded structures of R-loops. After fragmentation, RNA-DNA hybrids are pulled down using antibody S9.6, and cytosines in the displaced single-stranded DNA are converted to uracils by bisulfite. The cytosine-uracil-conversions can be mapped to the genome at near-nucleotide resolution. While this reviewer finds the approach novel, it does not appear to provide significantly higher resolution over the existing DRIPc-seq method developed recently by Chedin and coworkers (PMID: 27373332). Major concerns are listed below. In particular, baseline cytosine-uracil-conversions without S9.6 pull-down should be performed for the purpose of background elimination. Furthermore, as stated below, RNase H treatment prior to immunoprecipitation should be performed to validate the specificity of the bisDRIP-seq signals.

Major concerns:

1) It is crucial to confirm signals from bisDRIP-seq are indeed R-loop dependent. Simple bisDRIP-seq and DRIP-seq correlation is not sufficient. BisDRIP-seq with in vitro RNase H treatment should be performed.

2) In bisDRIP-seq, signals not only come from R-loops, but also from promoter single-stranded structures. Therefore it is important to include non-denatured cytosine-uracil-conversions (without S9.6 pull-down) as bisDRIP-seq input.

3) Template-strand bisDRIP-seq scores were subtracted from non-template-strand bisDRIP-seq scores to artificially recover R-loop signals. However, no assay was used to prove the validity of such a method.

4) Since previously reported DRIPc-seq already provides strand-specific, near base-pair resolution (PMID: 27373332), basic comparisons should be performed to test whether bisDRIP-seq outperforms DRIPc-seq in a significantly manner.

Reviewer #2:

The authors describe a new method to map the position of R-loops at higher resolution than existing techniques. The approach entails converting cytosines to uracils in the displaced DNA strand with bisulfite, while the cytosines in the opposite strand are protected by RNA. To minimize the amount of sequencing they focus on regions immunoprecipitated by the S9.6 antibody specific for RNA-DNA hybrids. After bioinformatic processing the authors obtain a genome-wide "bisDRIP-score" which measures the frequency of single-stranded DNA present at a given locus. Asymmetric single-stranded regions are considered R-loops. R-loops are correlated with transcription and enriched in the promoter region of active genes. The high resolution of bisDRIP-seq allowed the authors to identify the TSS as a 5' boundary and the first exon-intron junction as a 3' boundary. Finally, they report that histone genes and lncRNAs MALAT1 and NEAT1 have a particularly strong R-loop signature.

R-loops are believed to play important roles in gene regulation and the manuscript by Dumelie et al. describes a creative strategy to better map their genomic localization. The results are well presented and the methods are described clearly and in much detail. Overall I support publication in eLife. There are some major issues that need to be addressed, mostly ensuring that the authors are truly measuring R-loops and that no biases are skewing their analyses.

– BisDRIP score: I find the explanation of how this score was calculated rather convoluted. The choice of using the sum of the bisDRIP-score for cumulative anlayses seems questionable. This makes it impossible to compare axes when different number of regions are analyzed. For example 3C vs. 3E. Why not using the average?

– Validations: because bisDRIP-seq is a new genome-wide technique a high level of confidence in its measurements is required before it can be employed for new discoveries. 1) The authors show significant correlation genome-wide between DRIP-seq (the established technique) and their new bisDRIP-seq, but the correlation is obviously not perfect. Can the authors identify examples in which their new technique and the old technique differ and independently verify that the new mapping is more accurate? 2) To validate DRIP-seq typically RNaseH is used to remove RNA-DNA hybrids and prove the specificity of the signal. I believe this would be a more convincing control than triptolide also for bisDRIP-seq.

– Boundaries: the authors state that the TSS and the first exon-intron junction form 5' and 3' boundaries for R-loop formation, respectively, yet in several figures (e.g. Figure 3A, Figure 4A-B) I see signal above background upstream and downstream of these boundaries. Is this because bisDRIP-seq is not exactly single-base resolution, because of smoothing artifacts, or because these are not hard boundaries? Also, it was reported that restriction enzyme digestion can lead to overrepresentation of ORFs and first exon bias (László Halász et al., Genome Res 2017). It is important that the authors exclude this possibility in their own analyses.

– Methylcytosines: it seems that the presence of methylated cytosines would make it difficult to detect R-loops in heavily methylated areas of the genome. Is this a problem? It should be discussed.

– Genes with strong R-loop signals: the authors conclude that not having introns is a reason why some of the genes make in the top 25 list shown in Table 1 but alternative possibilities should be considered: 1) MALAT1, NEAT1 and histone RNAs are not terminated canonically; has that anything to do with R-loops? 2) What is the relationship between steady state RNA levels and formation of R-loops? GRO-seq measures transcription levels, and a weak correlation is visible in Figure 5B, but what about total RNA levels? Ribominus RNA-seq to measure steady-state levels of nuclear RNAs might be more suitable for this.

Reviewer #3:

In this manuscript, Dumelie et al. develop a new method, Bis-DRIP Seq, to identify the genomic localization of R loops at near-nucleotide resolution. Given the growing interest in understanding the function of R loops, this new method will benefit research in this area. Using this technique authors show that R loops are associated with the promoter regions of genes with or without introns. However, in genes with introns, 1st exon-intron junction defines the boundary of the R loop. We suggest a few minor experiments before publication of this manuscript.

Specific comments:

1) The authors highlight that BisDRIP-Seq provides more information about R loop boundaries as compared to previous DRIP-Seq datasets. This new method is an extension of the previously established DRIP-Seq and in theory it is understandable why it is an improvement. But since this is a 'methodology paper', the authors must provide comparative evidence that it is better. A figure showing how their dataset compares with a DRIP-Seq dataset will be beneficial.

2) The authors show that the 1st exon-intron junction serves as the 3' R-loop boundary (Figure 4A-D) which they suggest might be due RNA splicing (Figure 7A-B). To extend the biology a little more, the authors should look at a few genes that are known to have alternative splice forms to test if R loop boundaries show differences in genes that are known to have alternative splicing versus those that do not.
