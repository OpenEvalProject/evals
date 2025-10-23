# Peer review - Round 1

Editors:
- Michael R Green, Howard Hughes Medical Institute, University of Massachusetts Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23268.024](https://doi.org/10.7554/eLife.23268.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Copy-number and gene dependency analysis reveals partial copy loss of wild-type SF3B1 as a novel cancer vulnerability" for consideration by eLife. Your article has been favorably evaluated by Charles Sawyers (Senior Editor) and three reviewers, one of whom, Michael R Green (Reviewer #1), is a member of our Board of Reviewing Editors. One other reviewer, Robert K Bradley (Reviewer #3), has agreed to reveal his identity.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting manuscript which identifies that cancer cells with partial copy number loss of essential genes appear to be preferentially sensitive to further depletion of these genes. These so-called CYCLOPS genes appear to be enriched in genes encoding essential proteins, including spliceosomal proteins. The authors focus on cells with copy number loss of SF3b1 and suggest that these cells are more sensitive to loss of SF3B1. This is an exciting result because it potentially expands the number of malignancies that could be treated with SF3B1 inhibitors. The experiments are generally well performed but some clarifications as described below would help improve the study as listed below. The greatest weakness of the paper is that the specificity of the deubiquitinase inhibitor for SF3B1 is not clear and the efficacy of SF3B1 binding drugs in SF3B1 partial loss cells should be studied in more detail.

Essential revisions:

1) It is unclear in Figure 5 if partial copy number of loss of SF3B1 reduces levels of U2 snRNP and/or if this occurs only following further depletion of SF3B1. It is also not clear why partial reduction of SF3b1 would reduce expression of other U2 snRNP components and U2 snRNA (unless the cells experience reduce levels of these components simply due to reduced viability upon further SF3B1 suppression).

2) The lack of efficacy of SF3B1 inhibitor drugs on cells with or without partial loss of SF3b1 is not clear from the data shown. Knockdown efficiency of the single shRNA used in Figure 5—figure supplement 1B is not shown, only 2 cell lines are studied (as opposed to the larger number of lines shown in Figure 2A), and the authors have not tested the isogenic Cal51 CRISPR SF3b1 loss cell line in this experiment (only the parental Cal51 cells).

3) In Figure 6, it is not clear why intron retention is specifically focused on given that loss of SF3B1 in SFB1 copy number deleted cells should cause failure of constitutive splicing and all classes of alternative splicing. In fact, this point is suggested by the single RT-PCR example shown (MCL1 splicing; Figure 6D) is a cassette exon-skipping event and not due to a change in intron retention or 3' splice site selection. Evaluating the splicing in these cells in more detail from the RNA-seq data and representative RT-PCR events would be helpful.

4) In Figures 2–3 the authors suggest that cells with partial loss of SF3B1 are more susceptible to SF3B1 downregulation however qRT-PCR data for Figure 2A are either not shown in an ideal manner to make this point and no Western blot is provided for this Figure (which may be understandable given that suppression of SF3B1 is lethal). Figure 2—figure supplement 1A gives the suggestion that SF3B1 is similarly suppressed across these cell lines following shRNA treatment but this is not the case. It would also be helpful to show the effects of complete SF3B1 downregulation on cell growth across all cell lines as these data may give the impression that knockdown of SF3B1 is tolerated in some cell types (which is not the case).

5) The selectivity of b-AP15 for SF3B1 versus other substrates is not clear. It is possible that this compound exhibits preferential effects on SF3B1 partial loss cells due to effects on SF3B1 ubiquitination in addition to ubiquitination of other substrates that are not known. Although the authors acknowledge this point, it will be important to at least examine the effect of b-AP15 on splicing/gene expression compared to knockdown of SF3B1 (as in point above) to determine whether there is a similar "signature" of altered splicing to that obtained with SF3B1 inhibition. Moreover, if it were possible to see if SF3B1 re-expression could rescue the effects of b-AP15 that would be helpful as well.

6).Figure 3E is underexposed relative to Figure 3C. SF3B1 is readily visible in BT549 cells in Figure 3C but not in Figure 3E.

7) The cell lines analyzed in Figure 3F should be labeled in the figure.

8) A direct comparison of SF3B1 mRNA and protein levels could be informative and help readers to understand whether reductions in mRNA levels fully explain the observed differences in protein level. The authors could illustrate this with a scatter plot or similar illustration.

9) There are several issues with the statistical analyses that should be addressed:

The authors use Fisher's exact test when testing for a difference in proportion. However, the assumptions of the test are not met, because the margins are not fixed. The authors should use the binomial proportion test instead, which does not assume that the margins are fixed. (This is a common mistake and may not change any conclusions; however, it is a statistical error that should be addressed).

The "novel statistical framework" that was used to analyze the RNA-seq data needs further explanation. Since the method is new and relevant to interpreting the data, it should be at least partially described in the main text. The description in the supplementary should also be fleshed out. For example, the authors should describe how the "risk of intron retention" relates to the more standard "psi" value (fraction of mRNAs of the parent gene containing the retained intron) in terms comprehensible to a non-statistically minded reader. An explanation of why a β-binomial distribution is superior to the more standard binomial distribution would also be helpful (e.g., from a biological perspective, the binomial distribution assumes that the probability of intron retention is fixed, while the β-binomial distribution instead assumes that the probability varies).
