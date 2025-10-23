# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35788.102](https://doi.org/10.7554/eLife.35788.102)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A promoter interaction map for cardiovascular disease genetics" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Daan Noordermeer (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript presents PCHi-C data for iPSCs and CMs with the goal to identify target genes of non-coding loci identified in GWAS. They find that for 19% of LD SNPs identified in GWAS they find significant long-range interactions with distal genes that are likely candidates for genes mis-regulated in CVD. The manuscript presents two main datasets: capture data for promoters in iPSC and CM, and also RNAseq and H3K27ac ChIP. The bulk of the paper is dedicated to showing that the iPSCs and CM cells are indeed what they are supposed to be, and to show that the capture Hi-C data is good. The last part of the paper is focused on showing that a set of significant interactions connect GWAS SNPs to putative target genes. This can be a useful resource for the community.

Essential revisions:

1) Throughout the paper you have shown arcs indicating significant interactions. These should be replaced, or complemented with tracks showing the real underlying data, e.g. "4C-style" plots.

2) Place significant interactions in the context of TADs: are these mostly within TADs or do they also connect loci in separate TADs? Do the significant interactions provide additional information over and above TAD-based enhancer-promoter predictions?

3) The analysis in Figure 3 needs to be re-evaluated. Whereas the authors claim positive correlations, the reported Spearman correlations ranging from 0.09 – 0.2 suggest a very weak trend at best, with a large degree of variation within each category (as confirmed by the box-plots). Very significant P-values are reported to support the correlation, but the approach based on genome-wide randomization of H3K27ac-peaks is not appropriate. If anything, the current analysis confirms the tendency of active genes and their regulatory elements to cluster together in the genome (see e.g. RIDGES (Caron et al., 2001) and Hi-C compartment A (Lieberman-Aiden et al., 2009)). Further, the claim that number of H3K27ac and H3K4me1 peaks surrounding a promoter alone is a good predictor of gene activity does not take into account which peaks are contacted by promoters, which may constitute a large fraction. To improve the analysis, the authors should take a similar approach as Schoenfelder et al., (2015; Figure 3H), where for different interaction counts the distribution of expression groups is compared. Subsequently, more relevant p-values can be determined by randomizing the expression groups for all genes (without changing the position of genes). Taking this approach, the authors should be able to get similar correlations for interaction numbers as reported by Schoenfelder et al., (r = 0.98), whereas it will be interesting to see if similar correlations can be obtained by looking at the number of surrounding H3K27ac peaks, taking into account if they are contacted or not.

4) The paper would be further strengthened by providing examples that some of the predicted long-range interactions are functional. Are any of the predicted target genes affected in disease, e.g. reduced or increased in expression in individuals carrying the distal variant?
