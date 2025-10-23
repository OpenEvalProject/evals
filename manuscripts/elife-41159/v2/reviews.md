# Peer review - Round 1

Editors:
- Stephen P Goff, Howard Hughes Medical Institute, Columbia University United States

Reviewers:
- Yutaka Enomoto, Institute of Molecular and Cellular Biosciences, The University of Tokyo Japan

## Review text

DOI: [10.7554/eLife.41159.064](https://doi.org/10.7554/eLife.41159.064)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "MicroRNA-122 supports robust innate immunity in hepatocytes by targeting the RTKs/STAT3 signaling pathway" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yutaka Enomoto (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this complex manuscript, Xu et al. report that miR-122, the most highly expressed miRNA in hepatocytes, increases the activation of the interferon response in response to RNA PAMPs by down regulating the phosphorylation of STAT3, reducing IRF1 function. The primary effect of miR-122 is to down regulate several receptor tyrosine kinases (RTKs), including MER, FGFR1 and IGF1R, that are responsible for phosphorylation of STAT3.

Essential revisions:

Our reviewers have a number of criticisms that need to be addressed.

1) A concern is that the identification of the mRNA targets for miR-122 has involved some cherry picking. The hit list is long, and only a few are examined further. Other important hits may have been missed, and this should be acknowledged. It would be better to directly identify mRNAs targeted by miR-122 by performing some form of RISC CLIP experiment, such as iCLIP or PAR-CLIP, in the presence and absence of miR-122 using a pan-Ago specific antibody. This will identify all seed target sites for miR-122 occupied in vivo. I would not insist on this last experiment but it would strengthen the paper.

2) The average cell expresses ~50,000 miRNAs or so and miRNA function is dependent on expression level, with miRNAs expressed at <100 copies per cell being essentially non-functional (Mullokandov et al., 2012). Moreover, only RISC associated miRNAs are functional. In Figure 1B, the authors claim that human primary hepatocytes express 81,858 times more miR-122 that HepG2 cells and that transfection of the miRNA mimic into HepG2 increases miR-122 expression by 57,969 fold. What does this really mean, if the average cell only contains 50,000 miRNAs? These numbers should be admitted as being soft. Firstly, we really need to know the actual, not relative, number of copies of miR-122 per cell. They can be estimated – or if the authors can work quickly, they can get better numbers with small RNAseq. Secondly, as the authors have simply transfected their miRNA mimic into the HepG2 cells, it is likely that the vast majority is actually not loaded into RISC. If they want to really argue for meaningful numbers of the mimic, they would need to do RISC IP, using a pan-Ago antibody, followed by small RNAseq on the pulled down miRNAs. Or back off on the numbers.

3) HepG2 cells were used in most of these studies because ectopic supply of miR-122 to HepG2 cells resulted in a miR-122 abundance that was similar to its abundance in human liver (Figure 1B). However, it is unclear whether miR-122 displays similar roles in innate immunity in other liver cell lines, such as Huh7. Several players in cell growth and differentiation, such as p53, are expressed differently in HepG2 and Huh7 cells. Thus, the authors should repeat a few of the key experiments, such as suppression of STAT3 phosphorylation by miR-122 and inhibition of IRF1 by STAT3, in liver cells other than HepG2.

4) In Figure 1C-F, the authors don't show the results of IFN expression without stimulation. The data of IFN expression without stimulation are required as control. For example, since the difference of IFN-β expression between miR-NC and miR-122 is not huge in Figure 1D, F, the authors should examine if over-expression of miR-122 affects the expression of IFN or not.

5) In Figure 5, the authors use 293FT cells with over-expression of STAT3 for several reporter assays. But revealing the relationship between STAT3 and the expression of IRF1 in hepatocytes is supposed to be the core of the authors' conclusions. The authors should examine the promoter activity of IRF1 in HepG2 cells with or without si-STAT3. A more significant effort would be to examine the promoter activity of P1-M and P4-M in HepG2 cells. This would be helpful but perhaps not essential.

6) In Figure 5F, mutation of STAT3 binding sites within P1 and P4 did not completely abolish the repressing effect of STAT3. And the authors mention the possibility that STAT3 still binds mutant P1 and P4. The authors should perform ChiP experiments to reveal the possibility. In addition, the authors should perform reporter assays with control vectors such as pGL3-control or pGL3-promoter vector in order to examine if STAT3 affects the expression or activity of the reporter gene.

7) In this study, the authors analyze the function of miR-122 by over-expression of miR-122, but they don't perform experiments with inhibiting miR-122. Blocking the function of miR-122 in Huh7 cells and examining of phosphorylation of STAT1/STAT3 or IFN expression would strengthen the authors' conclusions.

References:

Mullokandov G, Baccarini A, Ruzo A, Jayaprakash AD, Tung N, Israelow B, Evans MJ, Sachidanandam R, Brown BD. High-throughput assessment of microRNA activity and function using microRNA sensor and decoy libraries. Nat Methods. 2012 Jul 1;9(8):840-6. doi: 10.1038/nmeth.2078.
