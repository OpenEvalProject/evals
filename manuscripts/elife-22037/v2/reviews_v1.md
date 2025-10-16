# Peer review - Round 1

Editors:
- Rachel Green, Johns Hopkins School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22037.023](https://doi.org/10.7554/eLife.22037.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Operon mRNAs are organized into ORF-centric structures that influence translation efficiency" for consideration by eLife. Your article has been favorably evaluated by Detlef Weigel (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

The three reviewers of this manuscript are generally enthusiastic about the data and the potential explanation that mRNA structure in bacteria occurs in modules or blocks that correspond to ORFs, and that these structural units dictate to some significant extent TE. Despite overall enthusiasm, there are several key statistical issues that need to be addressed (see reviewer 2 comments) including an evaluation of the statistical significance of the comparisons in correlations (which were done for different sets of genes). The reviewers also agreed in consultation that the ideal approach to take would be to perform a multiple regression analysis (reviewer 2, point 5) to explain TE using the various parameters (mRNA structure, codon bias, SD sequence, structure around start codons, etc.). These statistical analyses should be reasonably straightforward and would significantly increase the impact of the manuscript.

Reviewer #1:

This manuscript seeks to explain how the translational efficiency of E. coli genes within operons can vary as much as 100-fold even though they are found on a single polycistronic mRNA. Using a genome-wide RNA structural probing method (DMS-Seq) the authors have made a major discovery, that mRNA structure occurs in modules or blocks corresponding to ORFs, where adjacent ORFs often have very different levels of structure. mRNA structure is strongly anti-correlated with translational efficiency. While they offer a sophisticated discussion about the role of translating ribosomes in opening up mRNA structure, they argue that the structure is to a large extent encoded within the mRNA sequence itself on the basis of structural probing experiments in cells where translation is inhibited, with in vitro refolded RNA, and in silico analyses of the thermodynamics of folding. Finally, they argue forcefully that for endogenous E. coli genes, mRNA structure is a more reliable predictor of translational efficiency than codon adaptation (tAI) or the recently published codon influence metric. The experiments are well controlled, clearly explained, and compelling, and their findings have important implications for gene expression in bacteria.

Reviewer #2:

This manuscript reports experiments that compare in vivo mRNA structure to translation efficiency in E. coli. The authors find a negative correlation between these measures for 1,100 genes. They then make similar comparisons to mRNA structure in vivo after treating with a drug that blocks translation initiation (700 genes), and in vitro denatured / refolded mRNA (400 genes), and find somewhat lower correlations. They found smaller correlations between translation efficiency and tAI, Shine-Dalgarno strength, and measures of codon usage from Boel et al. They also provide compelling evidence that reporter overexpression induces expression of corresponding amino-acid synthesis pathways. The topic is important and timely, the paper is very well written, and the results are interesting. However, correlation is not causation, and the authors don't provide statistical comparisons of the correlations. This and several other issues decrease my enthusiasm.

1) The crux of the authors argument is that rho values are higher for in vivo mRNA measures than they are for tAI, Boel codon values, etc. In the first paragraph of the subsection “Translation efficiency is less correlated with other mRNA features” they say these are "significantly" different. The authors need to provide statistical tests that show the differences are significant if they want to make this argument. I'm not sure if that's possible with Spearman's rho. Pearson's R values allow comparisons via Fisher's z-test, but may not be appropriate because TE isn't normally distributed. Also, they used different genes for each correlation (see #2), which might affect their results and complicates comparisons. The results would be stronger if they could compare these correlations more directly (same genes, statistical significance in differences).

2) The authors say their mRNA structure analysis is "genome-wide" (Abstract), "global" (subsection “Development of global RNA secondary structure determination in E. coli”, first paragraph), and covers "all" genes (subsection “Translation efficiency is highly correlated with ORF mRNA structure”, second paragraph, e.g.). This isn't accurate, as they only use 13% to 30% of the genes because they have a 15 read / nt threshold on DMS-seq. A careful reader will spot this in the figure legend; a casual reader will miss this. This should be more explicit in the text.

3) Using all genes with TE > 0.01 in their supplemental table (3,358 genes) gives correlations of rho = -0.42 (Gini_WT vs TE), 0.26 (tAI vs TE), 0.31 (Boel-multiple vs. TE) and 0.36 (Boel-ordinal vs. TE). The point is that when one does a genome-wide analysis using the authors data, the correlations are much closer.

4) The supplemental table makes it difficult to reproduce the authors results, as they don't show which genes were picked for each correlation test. This should be simple to address, by including the reads/nt for each experiment and / or using multiple sheets in the excel file.

5) Overall, the study would be more compelling if the authors developed a multiple regression model to explain TE using mRNA structure, codon bias, SD sequence, SD pause sites (from their 2012 Nature paper), structure around start codons, etc. This approach would allow comparisons between these features, at least in terms of what makes a better predictor, and would result in a useful model for the community.

Reviewer #3:

In this study, structural probing of mRNA (DMS-seq) is combined with ribosome profiling to address the question of how translation initiation rate is normally tuned in E. coli. The authors find compelling evidence that each ORF within a given polycistronic mRNA represents an independent structural module, and the degree of structure inversely correlates with translation efficiency. In fact, ORF-wide secondary structure is a much better predictor of TE than other parameters (SD, tAI). This work draws important distinctions between the parameters that influence the efficiency of translation of exogenous (overexpressed) genes and those that govern translation of endogenous genes. The paper will be an eye-opener for many in the field.

Critique:

The experiments of Figure 6 show that a mutation that causes formation of an intergenic RNA structure inhibits translation of the downstream gene, due to occlusion of its start codon. While this lends strong support to the ORF domain model, it also begs the question of whether start codon occlusion helps tune initiation normally (in WT cells). The metagene analysis indicates that nucleotides near the start codon tend to be unpaired. The authors should address whether pairing probability of this region (start codon and immediate vicinity) is related to TE (even if the answer is no).

In the title, change "influence" to "predict" or "reflect." As the authors point out in the Discussion, whether the ORF structure determines initiation rate (via increased standby sites, for example) or plays another role (protects unoccupied mRNA from endonucleases) remains unclear. The latter idea would more readily explain why the entire ORF exhibits structure.
