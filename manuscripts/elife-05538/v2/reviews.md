# Peer review - Round 1

Editors:
- Anne C Ferguson-Smith, University of Cambridge , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05538.013](https://doi.org/10.7554/eLife.05538.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Constraint and divergence of global gene expression in the mammalian embryo” for consideration at eLife. Your article has been evaluated by Chris Ponting (Senior editor), a Reviewing editor and three reviewers.

As listed below, the reviewers have communicated quite detailed major concerns about the manuscript. We would like to provide the opportunity for you to address each of the points raised and to provide an extensively revised manuscript before making a final decision. The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Major concerns:

1) The title is provocative, without obvious follow-up. ‘Convergence’ and ‘divergence’ has implications about genetic selection and systems properties. The reviewers expected a definition of what these concepts mean in this context, how the study design would address these questions, and then interpretation of how the results provide insight. This was not evident in this manuscript. The primary reference seems to be in the Introduction, where two definitions of divergence are provided: first, it refers to changes in embryonic development resulting from genotype-specific differences in maternal transcripts present in mature oocytes at fertilization, and second, divergence here seems to be differences in regulatory control between embryos and adults. Both have been extensively studied, first to understand the maternal:zygotic transition in gene expression patterns, and second to characterize differentiation of cells, organs, and tissues. Resolving these and other forms of direct (genetic) and indirect (epigenetic, social factors is beyond the scope of the present study design, except with weak ad hoc arguments.

2A) No mention about whether sex of embryos was determined, and results analyzed separately for males and females. Considerable literature shows that sex affects expression of many genes. If the authors have evidence that embryo sex is not important in this context, evidence and arguments need to be presented (see also comment 10 below).

B) Apparently RNAs from whole embryos were analyzed. But as the authors acknowledge, organogenesis is active at E11.5. So why study whole embryos rather than specific organs and tissues?

C) Paternal stress is an established factor affecting offspring phenotypes and molecular features. Typically these paternal factors are controlled by removing males from mating cages immediately after fertilization. Alternatively, in vitro fertilization is sometimes used. Regardless, these kinds of factors needed to be controlled in order to make strong conclusions about the nature of maternal effects.

3) The aspect of the paper that we found disappointing was the analysis of gene expression dynamics. The reviewers considered that the authors could get much more from this dataset. For example, they don't test for interactions between genotype and time/stage (somite number, this could be done quite easily even using PEER) and there is no consideration of non-motonic time trends etc. In short, we think the authors could likely find much more about how genetic variation influences expression dynamics by implementing something similar to the ideas of Francesconi (Nat 2014).

4) The next recommendation would be to try and get more from the comparison of ASE and eQTLs. The correlation is weak (R^2 =∼34% variance explained). What is the explanation for this? Biological or technical? Likely there is something interesting to say biological here about the causes of the differences between the hybrids and the recombinants.

5) In general, the results are not too surprising; for example, the observation (Results, third paragraph) that the expression of key developmental genes changes through development is to be expected, we are not sure this warrants a main text figure. Moreover, a significant number of eQTL have been found in other tissues/cell lines in mammals (multiple papers from the Dermitzakis and Pritchard labs), the majority of which have been shown to regulate gene expression in cis, so the novelty of this part of the manuscript is small.

6) Care must be taken when defining cis-regulatory variants identified from previous RNA-seq studies (Montgomery et al.; Pickrell et al.), as you have done in the Introduction. In particular, these studies focused on correlating variants near the gene of interest with its expression across individuals. In a number of cases, it was shown that the effect size of the eQTL was correlated with allele-specific expression levels, strongly suggesting that many variants act in cis. However, in most previous eQTL studies, variants that act in cis have typically been defined as variants that are proximal to the gene of interest. Some clarification of this subtle, but important distinction, would be useful here.

7) When you mention, in the Introduction, that, at E11.5, gastrulation has already occurred, and the embryo is already composed of multiple different cell types, how much of a concern is it that, across N2 embryos, the rate of development may differ (perhaps because of the genetic background), which might lead to heterogeneity in the composition of cell types profiled across embryos?

8) Results, second paragraph: Why was a paired t-test as opposed to a binomial test (perhaps with a beta prior to model over-dispersion) employed here? The latter seems a much more natural approach given the data.

9) Results, fourth paragraph: It would be interesting to study the overall expression levels of the genes considered here in a homogeneous genetic background (i.e., in the F0s). In particular, this would allow one to study how the expression of Hbb-b1 and Hbb-b2 differed during development—is it also the case that, in BL6, Hbb-b1 increases in expression during development while Hbb-b2 decreases? This would provide additional mechanistic insight and provide support for the compensatory mechanism alluded to in the last sentence.

10) Figure 3 and Results: What explains the strange patterns in Figure 3B where there seems to be a bimodal pattern of expression (for both alleles) for a subset of the genes (e.g., Zkscan5, Polm, Eif2ak and Rhob)? Is this related to differences in developmental stage and/or sex? To explore the latter, could the expression of genes on the X or Y chromosome be used to sex the embryos? More generally, this is a strange pattern, which provides some concern about the robustness of the selection of these genes as those that display strong maternal effects.

11) Figure 5 and Results: The comparison with previous studies is somewhat troubling. In particular, how were the data normalized to ensure the results were comparable (e.g., batch effects/control for potential confounding factors)? Also, a p-value cutoff, rather than an FDR cutoff, should be used to ensure results are comparable across studies (since the null distribution will differ). Without more information, it is difficult to assess the significance of this result.

12) Results: What functional categories were enriched for in the ASE genes? Also, for the enrichment analysis, did the background control for gene expression levels (i.e., were only expressed genes considered)?
