# Peer review - Round 1

Reviewers:
- Claus O Wilke, The University of Texas at Austin , United States

## Review text

DOI: [10.7554/eLife.22472.119](https://doi.org/10.7554/eLife.22472.119)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Codon optimization underpins generalist parasitism in fungi" for consideration by eLife. Your article has been favorably evaluated by Detlef Weigel (Senior Editor) and three reviewers, one of whom, Claus Wilke, is a member of our Board of Reviewing Editors.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. There were three key issues that prompted us to reach this conclusion:

1) The manuscript is lacking a convincing "why". No convincing theory is presented for why codon bias should differ between generalists and specialists.

2) The main finding of the paper is a correlation between codon bias and host breadth. However, this correlation is confounded by the phylogenetic relationship between species, and whether the correlation would remain after this relationship is controlled for is unclear.

3) The manuscript is not well conceived and structured. A lot of potentially interesting material is presented in supporting information, while some of the information in the main manuscript seems tangential to the overall story. For example, the material in Figure 2 only establishes that codon bias is caused by selection pressure (an observation that is already widely accepted) but does not actually support the main story of the paper (that generalists experience different selection pressures than specialists).

Reviewer #1:

1) I am missing a clear, overarching hypothesis. Why do the authors think that codon bias should differ between specialist and generalist species? What is driving this effect?

2) I am not sure that the work of Figure 2 speaks to the overall hypothesis of the paper. Figure 2 demonstrates that two genomes with different codon biases likely experience different synonymous selection pressures. I think it is widely accepted these days that codon bias is often caused by selection, so we haven't learned much new from this analysis. Importantly, this work does not explain why codon bias patterns might be different in a generalist vs. a specialist.

Technical comments:

3) Results and Discussion, first paragraph: "A total of 22 species showed signatures…" Was this corrected for multiple testing?

4) Results and Discussion, second paragraph, Figure 1B: Spearman correlation assumes that the points are independent. However, they are confounded by phylogeny. The authors should calculate the correlation on phylogenetic independent contrasts. Looking at the figure, I would expect the effect to be much weaker under independent contrasts.

5) Subsection “Codon optimization across the kingdom Fungi”: I don't understand this: "taking the average p value from 100 tests of sample size=500 and n=1000." More explanation is needed. Normally, one would do only one test. How is an average p value from multiple tests to be interpreted?

6) What is the point of Figure 2B? I don't understand what this is meant to show.

7) It is unclear what is shown in Figure 3A. I don't think the quantity shown on the y axis is defined.

Reviewer #2:

The manuscript by Badet et al. aims to describe patterns of codon adaptation in parasitic fungi and how they vary as a function of their host ranges. In addition to performing comparative genomic analyses across 45 species, they generate transcriptomic datasets to measure changes in mRNA and tRNA abundances depending on the host for a subset of species as well as perform simulation studies to estimate elongation times of codons across these species.

Overall it is quite a compelling piece of work and I highly recommend its publication. My primary concern is that the bulk of analyses that the authors have performed is tucked away in the supplement and barely described in the main text. In fact, some supplementary figures are not even cited. I feel the authors are shortchanging themselves by submitting this manuscript as a Short report. I would recommend they elaborate their explanations of the analyses already presented in the supplement and discuss them in more detail.

In terms of specific concerns – I was particularly struck by their Figure 2—figure – supplement 1B. A large number of synonymous mutations are derived from mutations in the first codon position. Only Leu and Arg are capable of such mutations. Does this mean that over half the synonymous mutations were occurring at these two amino acids?

Reviewer #3:

In this study, the authors examine the relationship between gene codon optimization and host range variations in parasitic fungi. The study raised the hypothesis that the degree of gene codon optimization in parasitic fungi is related to the host range variation. Parasitic fungi with high degrees of gene codon optimization are usually generalists while genes in specialist fungi are usually less codon-optimized.

Although this is a very interesting hypothesis, the conclusions, however, are not convincing due to a very problematic methodology used and are not consistent with the known mechanisms of host specificity determination of parasitic fungi.

The conclusions of this paper are heavily dependent on a previously developed method (dos Reis et al., 2004) to determine the degree of codon tRNA coadapation. Such a value called 'S' was assumed to reflect the translation selection of genes by codon usage biases. Such a model, however, is very problematic and its analysis results are not consistent with many known experimental results. For example, in the original 2004 study, among the 126 genomes analyzed by this model, the S values of only 36 genomes were found to be statistically different from zero, suggesting that for most genomes, there is no sign of translational selection by codon usage acting on their genomes. Obviously, this is very different from known experimental. For example, while S values of human and Drosophila indicating lack of selection, there are now very strong experimental evidence demonstrating a role for translation selection by codon usage biases. Same for Bacillus. As acknowledged by the authors of the 2004 paper, their model has severe limitations and cannot explain much of the variation observed. In the case of human and mouse genome, which should exhibit a very similar degree of translation selection by codon biases, has quite a big difference in S values. In the context of this paper, three of the non-parasitic fungi analyzed by the 2004 study, S. cerevisiae, S. pombe, and N. crassa, all have very high S values, which are not consistent with the conclusion of this paper. All these indicate that the S value model used is very problematic and do not reflect much of the known experimental results.

A brief reading of the original 2004 method calculating the optimized s-values show that although adenosine deamination was taken into account when calculating base pairing between tRNA and codons, the I:U base pairing was set to be more preferred than I:C based pairing. Obviously, this is not consistent with current knowledge that inosine preferentially base pairs with cytosine. On the other hand, the simple assumption that tRNA copy number will truthfully reflect tRNA expression will certainly introduce additional variations of the model (human vs. mice for example). Current tRNA sequencing methods do not help here due to cloning and sequencing biases. Obviously, there can be more issues with the model.

The host specificity determination of parasitic fungi is mostly known to be determined by expression of different effectors, which frequently are not conserved. Although the codon optimization of genes related to infection was examined in two species, effector genes was not studied. Even if codon optimization may affect the expression of effectors, it should only affect the degree of infection but not the host range. Based on my knowledge, the expression levels of many known effectors are usually low.

Because of these two major deficiencies, I feel that the current study is premature for publication.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Codon optimization underpins generalist parasitism in fungi" for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Our major remaining concern with the manuscript lies in the "why" question brought up during the previous review. The arguments made are weak and hand-wavy. You claim that since generalists have longer genes than specialists and as a result might take longer to translate, there is stronger selection to improve their codon usage. This begs the question, what evolutionary forces are influencing gene lengths? Are gene-lengths in specialists under stronger selection to reduce in size or in generalists to increase their sizes and why?

Further, the results in Figure 5 suggest that codon optimization of secreted proteins may explain the host range of fungal parasites. However, the host range can simply be determined by robustness of overall cell metabolism/growth. To strengthen your conclusions, we suggest that you perform pathway-specific analysis and compare to that of the secreted proteins.

2) We appreciate that you have pursued several different approaches to correct for phylogeny, and we consider your results now reliable. However, throughout the manuscript there remain several places where you provide standard correlations, with uncorrected p values. All these should be replaced with correlations over phylogenetic contrasts. Specifically, these are in subsection “Codon optimization correlates with fungal parasites host range”, first paragraph and second paragraphs.

3) In several places throughout the manuscript, you list p values but don't state the test that was performed. Please state the test every time. Also, you are inconsistent in when you do and don't run a test. For example, in the first paragraph of the subsection “Long proteins encoded by the genome of generalist fungi likely increase natural selection on codon optimization” you list a p value but you don't do so in any of the other length comparisons in the following lines.
