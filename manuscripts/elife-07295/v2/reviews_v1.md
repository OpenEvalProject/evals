# Peer review - Round 1

Editors:
- Jean T Greenberg, University of Chicago, United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07295.032](https://doi.org/10.7554/eLife.07295.032)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Negative regulation of ABA signaling is critical for WRKY33-dependent Arabidopsis immunity towards Botrytis cinerea” for consideration at eLife. Your article has been in principle favorably evaluated by Detlef Weigel (Senior editor), a Reviewing editor, and two reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The reviewers agreed that your work identifying new WRKY33 targets during Botrytis infection is very interesting. The work nicely showed that you pinpointed new players in WRKY33-mediated resistance. Specifically, you reported that ABA (not SA) is a major player in WRKY33-activated resistance. While we are in principle supportive, there are some specific issues that need to be addressed to strengthen the work and acceptable for publication.

1) 1684 WRKY33 binding sites from genomic regions were associated with 1567 genes using ChIP-seq. Of them, 76% were W-box motifs which were consistent with previously reported WRKY family TF-binding sites. Moreover, you identified a new motif not previously known to bind WRKY factors, T/GTTGAAT. We think this is one of the major novelties of this study, but additional evidence needs to be provided to determine whether this is mediated by direct binding, or by other factors. If this motif is functionally as important as the W-box motif, the genomic regions containing such motifs should be undergoing evolutionary selection and their sequences should be conserved. We suggest that you compare the genomic regions containing W-box motif and/or T/GTTGAAT motif with the reported conserved DNA elements as described in Haudry et al. (2013)(PubMed ID: 23817568). Important WRKY33 target genes, such as NCED genes, would be expected to be associated evolutionarily conserved DNA elements.

2) For at least a couple of evolutionarily conserved T/GTTGAAT motifs, it is desirable to use a method like EMSA to test for direct binding. Alternatively, the authors might design artificial reporters with multiple tandem motif repeats alone or in combination with W boxes to test their regulatory activities (using constructs with single or double tandem motif repeats or truncated motifs as a control). This could be done as shown in a recent study (Li et al. Plant Cell 2015; PubMed ID: 25691733).

3) It has been known that TF-binding sites have dosage effects. For the TF-binding sites with positive regulation activities, multiple copies of motifs or binding signals on promoter regions are often associated with higher transcriptional induction levels. We suggest the authors to carry out a genome-wide correlation analysis between the binding signals/motif numbers and expression fold-changes for all the WRKY33 positively regulated target genes. This is feasible since the authors already have the ChIP-seq and RNA-seq datasets in hand.

4) Please clarify whether you normalized the gene expression levels on the basis of Per Kilobase of exon model per Million mapped reads (FPKM). Were exon-intron structures considered? If so, please describe this in the Materials and methods section. Otherwise, such expression level analysis may have bias on the genes with longer exons, which may further result in false positive detection during GO enrichment analysis. We suggest the authors use CuffDiff and/or DESeq2 to calculate Per Kilobase of exon model per Million mapped reads (FPKM) for all the TAIR0 genes and normalize their expression levels as described by Trapnell et al. 2012 (PubMed ID: 22383036).
