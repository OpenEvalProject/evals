# Peer review - Round 1

Editors:
- Daniel Zilberman, John Innes Centre United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50541.sa1](https://doi.org/10.7554/eLife.50541.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper elucidates the mechanism and evolution of imprinted gene regulation in the endosperm by examining the binding pattern of the type I MADS-box transcription factor PHE1 in Arabidopsis seeds and the role of PHE1 in mediating triploid block, the phenomenon where pollination with diploid pollen causes endosperm proliferation defects and seed abortion. PHE1 preferentially binds near transcription factor genes, especially of the type I MADS-box family, and imprinted genes – those preferentially expressed from either the maternal allele (MEGs) or paternal allele (PEGs). PHE1 binding sites are also frequently associated with Helitron TEs. DNA methylation of the paternal allele prevents PHE1 binding at MEGs, restricting binding to the maternal allele. PHE1 binding is associated with genes that are overexpressed due to triploid block and mutation of PHE1 rescues triploid block-induced seed abortion and reduces the expression of some overexpressed genes. Helitron transposition is proposed to have created a network of PHE1 regulated genes, including imprinted genes, that regulate endosperm development. This paper establishes PHE1 as an important regulator of imprinted genes and endosperm development.

Decision letter after peer review:

Thank you for submitting your article "The MADS-box transcription factor PHERES1 controls imprinting in the endosperm by binding to domesticated transposons" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

This is an important and interesting paper that elucidates the mechanism and evolution of imprinted gene regulation in the endosperm. However, the reviewers were concerned that the paper's core claim, that PHE1 "is a master regulator of paternally expressed imprinted genes, as well as of non‐imprinted key regulators of endosperm development" is not strongly supported. Several aspects of the analysis and data presentation should be improved and clarified, as outlined below. The most important revisions relate to points 6-9, as these directly influence the paper's main conclusions. In particular, all reviewers requested the inclusion of RNA-seq data that would evaluate how PHE1 affects transcription (point 7).

This paper addresses a complex topic and a great deal of important data (and the model) are relegated to supplementary figures. We feel that the paper would benefit from a less compressed presentation of the results and a separate Discussion section and should therefore be recast as a Research Article.

Presentation of ChIP-seq data and association with Helitron TEs:

1) PHE1 ChIP-seq data are central to this paper but are described only very briefly in Supplementary file 1. This table should be included as a supplement to Figure 1 (a similar table for H3K27me3 should also be included as a supplement to Figure 4), and other data and analyses would be helpful. Is PHE1 binding enriched near transcriptional start sites (TSSs), as for other plant TEs? What do PHE1 binding peaks look like near important genes examined in this paper?

2) It is not clear if the motifs in Figure 1A occur separately or are found together. Also, are the authors proposing that both are CArG-boxes? Only motif 2 looks like a bona fide CArG-box: CC(A/T)6GG.

3) It is not clear if there is an orientation to the meta-gene plot in Figure 2C with respect to the associated gene annotations. From the graph, it looks like H3K27me3 is accumulating 5' and 3' of the PHE1 binding site, but it would be informative to show the alignment according to the associated gene orientation. The figure appears to show that PHE1 binding takes place in a H3K27me3-depleted island within a H3K27me3-dense region (5' and 3'), which is also shown in the schematic model in Figure 2—figure supplement 3. Is this correct?

4) Related to the above, the authors state that "Interestingly, we observed biallelic binding in PEG targets (Figure 2E). Even though the maternal PHE1 binding sites in PEGs were flanked by H3K27me3 (Figure 2B-C), correlating with transcriptional repression of maternal alleles, the absence of this mark within the binding site centres seems to be permissive for maternal PHE1 binding." This is indeed unexpected and very interesting, and this point would be more convincing if the authors examine additional loci to confirm the biallelic binding. Have the authors performed ChIP-seq on the crosses used in Figure 2E?

5) In the expression profile in Figure 1D, the inclusion of PHE1 targets without flanking TEs would be helpful to judge the extent to which the presence of the TE impacts the expression level of the nearby gene.

Definition of PHE1 target genes and the effects of PHE1 on transcription:

6) The concept of a "PHE1 target" is central to the paper. According to the Materials and methods, PHE1 targets are genes with "binding sites located less than 3 kb away from the […] transcription start site" – genes with a PHE1 peak within a 6 kb window around the TSS. Most functional TF binding sites are much closer to the TSS. For example, conserved Arabidopsis TF binding sites peak sharply at -50 bp from the TSS and are not significantly enriched outside a 600 bp window (-400 bp to +200 bp) around the TSS (Yu et al., 2016). ChIP-seq data for Arabidopsis TFs shows similar patterns. Unless PHE1 is very different, expanding the window 10-fold will introduce a great deal of false-positive noise. This will not fundamentally affect conclusions based on analyses of large numbers of PHE1 "targets", but it will affect the validity of designating specific genes or groups of genes (as in 12% of MEGs, 31% of PEGs, 50% of highly upregulated genes in 3x seeds) as PHE1 targets. The authors should evaluate how a more conservative designation of PHE1 target affects their results and conclusions. Because this is so important, how PHE1 targets are designated should also be described in the Results.

7) The authors claim that PHE1 "is a master regulator of paternally expressed imprinted genes, as well as of non‐imprinted key regulators of endosperm development." However, this claim is based mostly on PHE1 binding data. In the vast majority of cases, the authors do not know that PHE1 regulates any of its target genes. Considering the permissive approach for designating genes as PHE1 targets described above, the lack of functional data for most genes means that the authors' claim is not strongly supported. The authors' claims would be much stronger if they could designate PHE1 targets based on transcriptional activation (or repression) as well as PHE1 binding. This would also allow the authors to evaluate if PHE1 is generally a transcriptional activator, and if PHE1 binding further from a gene (outside a putative promoter) is associated with transcriptional effects. RNA-seq of the RNA samples used in Figure 4—figure supplement 1F (wt x wt, wt x osd1, wt x phe1 phe2, wt x phe1 phe2 osd1) would allow a much better designation of PHE1 targets when cross-analysed with the ChIP-seq data.

Association with imprinted genes:

8) According to the Materials and methods, "To determine which imprinted genes are targeted by PHE1, a custom list consisting of the sum of imprinted genes identified in different studies was used (Figure 1—source data 1) (Gehring et al., 2011; Hsieh et al., 2011; Pignatta et al., 2014; Schon and Nodine, 2017; Wolff et al., 2011)." Schon and Nodine determined that earlier published lists of imprinted genes were substantially affected by maternal contamination and came up with high-confidence lists of MEGs and PEGs. Why did the authors not use these presumably more robust (but smaller) lists? It is concerning that in analyses comparing PHE1 targets with imprinted genes, both datasets likely contain many false-positives.

9) The significant enrichment of PEGs and MEGs noted in the fifth paragraph of the Results and Discussion section is based on the comparison with the total number of genes in the genome. A better reference set would be genes expressed in the endosperm (for instance: Belmonte et al., 2013), which would reduce the control set to approximately 12,000 instead of 27,400 genes.

10) The presence of RC/Helitrons in orthologs is very interesting and should be evaluated on a meta-genomic scale in addition to showing a few examples. Is this really an evolutionary conserved phenomenon and to which extent does it correlate with imprinting? Addressing this question would significantly strengthen this work, as the implication of the shown examples for the evolution of imprinting and gene regulation via Helitron TE insertion is not clear.
