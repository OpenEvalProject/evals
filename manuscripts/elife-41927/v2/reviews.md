# Peer review - Round 1

Editors:
- Alexis Battle, John Hopkins School of Medicine United States

Reviewers:
- Dan Arking

## Review text

DOI: [10.7554/eLife.41927.025](https://doi.org/10.7554/eLife.41927.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Nuclear Genetic Regulation of the Human Mitochondrial Transcriptome" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a guest Reviewing Editor and Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Dan Arking (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. As you can see, we have listed a set of "essential revisions" that represent the consensus assessment of the editors and reviewers.

Summary:

The manuscript describes a study of the regulation of the mitochondrial transcriptome, in particular identifying nuclear genetic variants that are associated with expression of mitochondrial transcripts. They identify such associations for fourteen out of fifteen mitochondrial genes and a total of 64 trans-genome associations. Replication between studies is observed, and they discuss the role of genetic variation affecting mitochondrial gene expression in complex disease.

The reviewers appreciated the importance of the findings for understanding mitochondrial gene expression and found the manuscript generally clear. However, to support the findings, some additional analyses are desired along with adding to the biological interpretation of the results and the discussion of some caveats.

Essential revisions:

1) In order to achieve a higher level of biological understanding and impact of the results, it is necessary to more fully characterize the discoveries, particularly those that are not previously implicated in known mitochondrial regulatory processes. This could include an analysis of the variability in expression of those factors; a more systematic analysis of whether those factors are shuttled back to the nucleus or localized with the mitochondria; and analysis of the 45 QTLs that are not missense mutations. For instance, are they in known enhancer regions that may have impacts on multiple mt-regulatory factors? Are the same QTLs (either SNPs or linked SNPs) also associated with nuclear encoded mitochondrial genes that have interconnected signaling pathways with mt encoded genes. Are the gene expression levels of these two sets of mt genes associated with each other across individuals and could there be any regulatory feedback mechanisms across these sets of genes? Not every one of these questions will necessarily yield an interesting result, but some further expansion on biological interpretation is necessary.

2) Replication rate overall is low, which merits exploration. Is this due to power, technical variability, biological variability, or a higher false discovery rate than originally estimated? It is necessary to show analysis attempting to disentangle this through power calculation, simulation, and any relevant demonstration of biological or technical confounders. Could it be driven by differences in mt copy number, or cell state (leading to differences in mt-liked metabolic activity)?

Given low replication rates and other concerns, it is noted that FDR may be susceptible to artifacts, and in general it is necessary to demonstrate that the FDR is well calibrated. The suggested method is to use permutation analysis (permuting a trait, leaving linkage disequilibrium intact) to establish an empirical null. In addition, please include raw p-values along with FDR for detected associations.

3) In order to rule out false positive trans associations due to alignment error, it is necessary to evaluate whether there is sequence similarity between the candidate mt eQTL target genes and the nuclear regions of the genome, particularly for regions near the candidate eQTL variants. If there is sequence similarity, these could represent cis-eQTLs or nuclear eQTLs for genes that simply have some reads mis-mapping to mt. This is a similar problem to probe cross-hybridization observed for microarrays, and has been observed for RNA-seq false positive trans-eQTLs in GTEx and other studies.

4) It is necessary to address questions regarding ancestry and linkage disequilibrium, particularly considering diverse ancestries represented in the RNA-seq data and potential differences with those in the GWAS data used. The manuscript evaluates SNPs in NHGRI GWAS catalogue in strong LD with the SNPs that control mtDNA gene expression. What LD reference is used? Is it the European LD reference calculated from 1000 genomes, or is it the in-sample LD from the datasets with RNAseq data? What were the populations (ancestries) in which the GWAS was performed? In other words, is the LD between SNPs calibrated for the GWAS or for the eQTL analyses? While it may not be possible to match LD perfectly between GWAS and eQTL analyses, these potential issues should be mentioned and some attempt made to determine if they are problematic. If the individual data is available, it is necessary to discuss single/per population analysis to show that their results are real and not artifacts of population structure and also likely consistent across populations. This would involve simply sectioning out the samples from each single population, and rerunning their analysis. The associations are not expected to be significant in the single population analysis since they'll have much smaller sample sizes, but the effect sizes and directions should be correlated. If this is not possible, then caveats of population structure need to be mentioned and the claims toned down accordingly.
