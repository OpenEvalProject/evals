# Peer review - Round 1

Editors:
- Thomas R Gingeras, Cold Spring Harbor Laboratory , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25125.023](https://doi.org/10.7554/eLife.25125.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mapping the mouse Allelome reveals tissue-specific regulation of allelic expression" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Fiona Watt as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We have sent your manuscript out to two reviewers for their evaluations. Below you will find the reviews provided by these reviewers. As you will see, each of the reviewers agrees that there are potentially important biological insights contained in this manuscript. However, there are several issues relating to clarity and the presentation of the data described. While at this moment we conclude that your manuscript is not ready for publication in eLife, a revised version that addresses the issues raised by the reviewers would be of interest.

Summary:

This manuscript entitled "Mapping the mouse Allelome reveals tissue-specific regulation of allelic expression" Andergassen et al. present a comprehensive analysis of the mouse Allelome. The authors generate RNA-Seq data from 23 different developmental stages including 19 female tissues from F1 crosses between FVB and CAST mice. The results of the authors' analyses show that allele specific expression is highly tissue-specific and also show that this behavior is regulated by tissue-specific enhancers. In so doing, they identify imprinted genes and compare against the current literature. Lastly, they show that the allelic behavior occurs in larger genomic clusters than previously expected.

While the data presented in this manuscript could be an interesting and useful resource describing allelic behavior in the mouse genome there are a number of concerns (listed below) that should be addressed to provide some clarity to the conclusions and to assist readers in their comprehension.

Essential revisions:

1) The authors use the own software Allelome. PRO that has previously been published in NAR to perform their allelic analysis. They are not clear about the parameters and thresholds that they use to perform these analyses. In Figure 1—figure supplement 1C they present the "allelic score cutoff" which is never defined. They use an allelic ratio cutoff of 0.7 (they use a ratio of 0.6 for the XCI analysis on the basis that it is more stringent) which seems somewhat arbitrary and never justify its choice (or the dependence of their results on these parameters).

2) Their definition of bi-allelic expression (BAE) includes genes that have allelic expression ratios of less than 0.7 but also includes genes that are greater than 0.7 but are inconsistent between replicates – shouldn't this second category of genes be called ambiguous rather than biallelic and separated out?

3) Near the start of the paper (Results section) the authors classify genes as strain-biased for either CAST of FVB – these are a different set of genes from the maternal and paternal allele-expressed genes that they also find. They use these sets of genes throughout the manuscript. In looking throughout the paper including the supplemental methods there appears to be no definition as to what the authors mean by strain-biased genes (or define the parameters used to call genes in this category).

4) In their analysis of regulation of allele-specific genes the authors use the H3K27ac signal in a window of +/- 50 kb from the TSS of the target gene. They then use a procedure of computing the enrichment of allelic behavior of H3K27ac windows of 4kb in size compared to randomly shuffled windows. First, H3K27ac signal is localized to the TSS of an active gene, thus why is such a large window around the TSS needed – shouldn't it be localized no more than a kb from the TSS. Additionally, why perform the enrichment compared to a shuffled null? Can't one just compute the allelic signal of a genomic window centered on the TSS and compare the direction of the allelic bias (if there is one) with the target gene being regulated?

More technical issues:

1) In subsection “Escape from X-inactivation is tissue-specific and correlates with increased distance from monoallelic enhancers” they compute the significance of the escapers being further from H3K27ac windows compared to non-escapers and quote a significance of p<1e-20 and refer to the material and methods. In the Material and methods however, the authors present the analysis for this claim and show that the significance using a Fisher's exact test is p<1e-17.

2) In both Figure 3A and Figure 2—figure supplement 2C the use of similar colors such as green, blue and similar shades to correctly distinguish the features of the figures.

3) While "Allelome" seems OK, the use of "Escapome" seems unnecessary and unhelpful.
