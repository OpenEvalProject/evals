# Peer review - Round 1

Editors:
- Elisabeth Busch-Nentwich, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55792.sa1](https://doi.org/10.7554/eLife.55792.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper demonstrates that current RefSeq and Ensembl gene annotations of the zebrafish genome have discrepancies such as mutually exclusive gene models that can affect the interpretation of transcriptional profiling datasets. Moreover, incomplete annotation of 3' untranslated regions impairs gene expression analysis of datasets from increasingly popular single cell RNA-seq techniques due to their inherent 3' bias. To address these problems the authors have produced a new zebrafish gene annotation that improves detection of cell-type specific transcripts.

Decision letter after peer review:

Thank you for sending your article entitled "An improved zebrafish transcriptome annotation for sensitive and comprehensive detection of cell type-specific genes" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Didier Stainier as the Senior Editor.

In this manuscript, Lawson et al. observe that some 3' UTRs in the Ensembl and RefSeq zebrafish gene annotations seem incomplete and gene models are inconsistent between the two annotations. The incomplete 3' UTRs affect their ability to identify differentially expressed genes in an RNA-seq dataset from kdrlpos and kdrlneg cell populations. The authors speculate that this is due to the strong 3' bias in read distribution caused by oligo-dT priming. To remedy this, the authors use Cufflinks and Cuffmerge to produce transcript and gene models from a published RNA-seq dataset covering six developmental stages, guided by RefSeq splice sites, and Ensembl annotation. The resulting annotation (called V4.2) has longer 3' UTRs for a subset of genes. The authors show that this increases the number of genes detected as differentially expressed in their RNA-seq dataset. Similarly, mapping a published single cell 10x Genomics RNA-seq dataset against V4.2 moderately increases the number of detected genes and cell clusters in a tSNE plot. The authors conclude that these results demonstrate that their V4.2 annotation is superior to the Ensembl and RefSeq annotations and recommend using V4.2 for bulk and single cell RNA-seq analysis.

The reviewers agree that the current 3' UTR annotation of the zebrafish genome is incomplete and might affect the interpretation of 3' biased transcriptional profiling data. Therefore, an annotation with more accurate 3' UTRs would be a useful resource. However, as it stands, the annotation presented here would create different problems for anyone using it because of the additional (and in this manuscript undiscussed) gene and transcript models that are based solely on one RNA-seq dataset. A Cufflinks transcript model, even if it produces a BLAST hit, is insufficient evidence that it is a bona fide expressed transcript (see below for details). We would therefore ask that the manuscript focus on the improved 3' UTR annotation of Ensembl and/or RefSeq gene models and show that it provides a considerable advancement for RNA-seq analysis. This focus should also be reflected in the title.

Essential revisions:

1) The case for an improvement rests mostly on the fact that a few genes that the authors had expected to change expression in one of their datasets were only detected as differentially expressed (DE) when using their V4.2 annotation instead of Ensembl or RefSeq annotation. The other test case, a single cell RNA-seq re-analysis using V4.2, shows only minor changes. Crucially, there is no evaluation of the gene overlap with the Ensembl or RefSeq based analyses, so some genes might actually be lost. The bulk RNA-seq dataset in this manuscript is unusual as it uses oligo-dT priming instead of the more common random priming used in, for example, the TruSeq library preparation kits. The resulting 3' bias is extreme. For example, in Figure 1C the read depth drops by 99% from 2750 at the 3' UTR end of the gene to 28 in the coding part of that exon. To demonstrate that V4.2 represents a significant improvement over current annotation, an objective analysis of several datasets is required, including random-primed RNA-seq data. If the advantage is limited to 3' end biased data, this should be shown and discussed.

2) The authors state that new transcripts and genes are present in their V4.2 annotation that are missing in both Ensembl and RefSeq. This is based on transcript and gene model output from cufflinks. Some of these models have BLAST hits, which the authors interpret as evidence that these are bona fide expressed transcripts. This is incorrect. Reads can mis-map to processed pseudogenes and other gene remnants and thus look like separate expressed genes. It is therefore not surprising that some of those have BLAST hits. Of the 6562 genes with an XLOC name in v4.2.1.gtf, 4714 are single exon genes. This indicates that the vast majority are indeed likely to be processed pseudogenes. If these gene models were to be used to map against, they would mop up reads from coding genes and distort results. Taken together these models have not passed the many filtering and validation steps using additional evidence (cDNA, cross species comparisons etc) that Ensembl and RefSeq employ. To avoid over-interpretation of these unverified gene models they should be provided separately from those that have Ensembl and/or RefSeq identifiers. The text needs to acknowledge the limitation of these gene models. Claims of missing genes should be made much more cautiously unless independent evidence beyond BLAST hits is provided.

3) The annotation needs to include existing Ensembl and RefSeq identifiers. Gene symbols are notoriously unreliable and not suitable for comparative analyses.

4) The annotation uses one RNA-seq dataset derived from whole embryos and a limited set of developmental stages. It is possible that the modest improvement is partially due to missing tissue- or stage-specific transcripts and their 3' UTRs. The authors should compare the genes detected in a few tissue-specific datasets with V4.2 to demonstrate sufficient overlap or acknowledge the limitation if a substantial number of genes are absent from the used dataset. Alternatively, the authors could run Cufflinks without Ensembl and RefSeq annotation and then compare how many transcripts overlap Ensembl transcripts. Likewise, alternative polyadenylation and differential 3' end use will affect interpretation of gene expression. This should be discussed.

5) The authors need to provide statistics and numbers in the text instead of qualifiers such as "much lower". For example, the authors state "…the overall number of differentially-expressed transcripts identified when using Ensembl was much lower than that found with RefSeq." The difference is 7%. Another example is "increase in the number of median genes". How many? (It's 842 vs. 761.) Likewise, the authors need to provide statistics of their annotation. How many genes are detected, what is the length/ exon number distribution of known transcripts vs. XLOC transcripts etc.

6) A lot of the analysis methodology is missing and no code is provided. "In-house Perl scripts" need to be made available. What were the criteria for "hand-curation"? The same is true for other methods. For example, the intersection analysis of RefSeq and Ens95 is not clear. What does intersection by gene coordinate mean? Is it exactly matching start/end positions or by interval overlap? The discrepancy of 3000 genes is improbably large.

Other required changes and clarifications:

1) In Figure 5A, there are 7 cartilage and 9 epidermis genes unique to Ens95 vs. V4.2. Could the authors comment on this? Are these genes bona fide markers of these cell types or false positives? Will the missing genes in V4.2 be incorporated?

2) Figure 1A, B should be -log.

3) In Figure 2—figure supplement 1, the 6743 genes from RefSeq only in panel A does not correspond to the 6119 genes (2514+3605) analyzed in panel B. Likewise, the 2514 genes from panel B do not correspond to the 2549 genes (2035+514) in panel C. Please correct or explain these discrepancies in gene number.

4) "Comparison of 3' UTRs for matching genes from the two annotations in those latter cases revealed that the overall differences in length were significant (Figure 2C)." Why has a statistical test been performed here? The authors are not randomly sampling from an underlying population of gene models and then measuring the UTR length. They have selected for the ones that are either longer or shorter in Ensembl 95.

5) Figure 3B: If the Ensembl annotation was merged into V4.2, how can V4.2 have shorter UTRs than Ensembl?

6) The counting against the two annotations seems oddly inconsistent. For slc2a1a (Figure 1E and Figure 5D) the same exon portion gets 16 reads in Ens95, but only 4 reads in RefSeq.

7) It is not clear what is meant by this sentence in the legend for Figure 2—figure supplement 1: "Total numbers of unique genes in each case are not equivalent due to cases there ("where" I assume?) multiple genes from either or both annotations may intersect within a single interval." How many genes does the overlap method fail to distinguish because of this?

8) "…all of these genes appear preferentially expressed in the erythroid-2 cluster (Figure 7A)". slc25a37 and tfr1a are expressed in more cells at higher levels in the erythroid cluster, not erythroid-2.

9) "…mapped onto the RefSeq annotation". Mapping is to the assembly not the annotation, so it should either say "mapped to GRCz11 and counted against the RefSeq annotation" or just "counted against the RefSeq annotation". Same at : "to genome-mapped or ENSEMBL-mapped reads". The reads aren't mapped to the Ensembl annotation, they are counted against it. This needs changing throughout.

10) Figure 3 legend. What do the bars represent in Figure 3C, E and F, median or mean?

11) Legends for Figures 4-7. What do the colour bars in the t-SNE expression plots represent? It will be some kind of count, but what exactly?

12) It would be interesting to see what the RefSeq and Ensembl comparison looks like for other model organisms (not humans, which has MANE https://www.ncbi.nlm.nih.gov/refseq/MANE/).

13) Figure 5C: There are a lot fewer dots than the Venn diagram would suggest. Are they plotted on top of each other? Jitter might help. Also, what do the genes from the Ens95 counting that don't overlap with the V4.2 ones look like?

14) https://www.umassmed.edu/lawson-lab/transcriptome gives a 404 error.

15) Ensembl not ENSEMBL.

16) Median ration => Median ratio.

17) "In this process, we also manually corrected several incorrect gene names assigned by ENSEMBL that resulted from transcripts overlapping two separate genes, causing a single gene ID to be assigned to two genes." Have these been reported to Ensembl?

18) tRNAscan is mentioned in the Materials and methods, but nowhere else.

19) It would be good if the GTF file contained CDS entries.

20) Figure 2: Venn diagram is incomplete, lacks the non-concordant population

21) Figure 2—figure supplement 1: the Venn diagrams should be size proportionate.

22) Figure 3 and text: reorder bud, shield and dome to dome, shield and bud so as to fully maintain sequence of stages

23) Figure 2B: caption should be V4.2

24) Figure 2C: scales of charts should be fixed to 15k for direct comparison and to demonstrate length difference of 3'UTR distribution between annotations

25) "…only genes with matched gene symbols between ENSEMBL (v95) and RefSeq were maintained" and "only V4.2 genes that matched by gene symbol were incorporated into the reference set". Why do genes which have gene symbol discrepancies between Ensembl and RefSeq were excluded from the reference set? If the genome location and sequence are the same, this may be a common naming issue, rather than a reason to suggest difference in gene/transcript.

26) The new annotation is not currently accessible at the website cited. Will the authors make an effort to add an improved annotation to Ensembl?

27) Figure 6: add consistent labelling of cell types and gene symbols throughout.
