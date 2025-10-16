# Peer review - Round 1

Editors:
- H Efsun Arda, National Cancer Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91994.3.sa0](https://doi.org/10.7554/eLife.91994.3.sa0)

Understanding how genomic regulatory elements control spatiotemporal gene expression is essential for explaining cell type diversification, function, and the impact of genetic variation on disease. This important study provides solid evidence that enhancers generally combine additively to influence gene expression. Moreover, promoters, particularly weaker ones, can exhibit supra-additivity when integrating enhancer effects. These findings highlight the context-dependent nature of enhancer-promoter interactions in gene regulation, and contribute to ongoing discussions about the selectivity and combination of regulatory elements.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91994.3.sa1](https://doi.org/10.7554/eLife.91994.3.sa1)

This manuscript by Martinez-Ara et al investigates how combinations of cis-regulatory elements combine to influence gene expression. Using a clever iteration on massively parallel reporter assays (MPRAs), the authors measure the combinatorial effects of pairs of enhancers on specific promoters. Specifically, they assayed the activity of 59x59 different enhancer-enhancer (E-E) combinations on 8 different promoters in mouse embryonic stem cells. The main claims of the paper are that E-E pairs combine nearly additively, and that supra-additive E-E pairs are rare and often promoter-dependent. The data in this study do generally support these claims.

This paper makes a good contribution to the ongoing discussions about the selectivity of gene regulatory elements. Recent works, such as those by Martinez-Ara et al. and Burgman et al., have indicated limited selectivity between E-P pairs on plasmid-based assays; this paper adds another layer to that by suggesting a similar lack of selectivity between E-E pairs.

An interesting result in this manuscript is the observation that weak promoters allow more supra-additive E-E interactions than strong promoters (Figure 4b). This nonlinear promoter response to enhancers aligns with the model previously proposed in Hong et al. (from my own group), which posited that core promoter activities are nonlinearly scaled by the genomic environment, and that (similar to the trend observed in Figure 5b) the steepness of the scaling is negatively correlated with promoter strength.

My only suggestion for the authors is that they include more plots showing how much the intrinsic strengths of the promoters and enhancers they are working with explain the trends in their data.

Specific Suggestions

Supplementary Figure 4 is presented as evidence for selectivity between single enhancers and promoters. Could the authors inspect the relationship between enhancer/promoter strength and this selectivity? Generating plots similar to Figure 4B and Figure 5B, but for single enhancers, should show if the ability of an enhancer to boost a promoter is inversely correlated to that promoter's intrinsic strength. Also, in Supplementary Figure 4, coloring each point by promoter type would clarify if certain promoters (the weak ones) consistently show higher boost indices across all enhancers. If they do not, the authors may want to speculate how single enhancers can show selectivity for promoters while the effect of adding a second enhancer to an existing E-P has little selectivity. An alternate explanation, based solely on the strength of the elements, would be that when the expression of a gene is low the addition of enhancer(s) have large effects, but when the expression of a gene is high (closer to saturation) the addition of enhancer(s) have small effects.

Can anything more be said about the enhancers in E-E-P combinations that exhibit supra-additivity? Specifically, it would be interesting to know if certain enhancers, e.g. strong enhancers or enhancers with certain motifs, are more likely to show supra-additivity with a given promoter.

Comments on revised version:

The revised manuscript satisfactorily addresses the points I raised in the review. With the addition of the new graphs there is enough data for readers to decide whether the supra-additivity depends only on the strength of the promoter or on some other (undefined) feature of E-P pairs. This manuscript is a solid contribution to the ongoing debate about enhancer-promoter selectivity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91994.3.sa2](https://doi.org/10.7554/eLife.91994.3.sa2)

Summary

This work investigates how multiple DNA elements combine to regulate gene expression. The authors use an episomal reporter assay which measures the transcriptional output of the reporter under the regulation of an enhancer-enhancer-promoter triple. The authors test all combinations of 8 promoters and 59 enhancers in this assay. There are two main findings: (1) enhancer pairs generally combine additively on reporter output (2) the extent to which enhancers increase reporter output over the promoter (individually and as enhancer-enhancer pairs) is inversely related to the intrinsic strength of the promoter. Both of these findings are interesting and are well supported by the data.

This study extends previous results on enhancer-promoter combinations to enhancer-enhancer-promoter triples. For example the near equivalence of Fig. 5b and Fig. S7b is intriguing. This experimental design also provides the ability to investigate the notion of selectivity (also commonly referred to as compatibility) between enhancer-enhancer pairs and promoters.

The authors note many limitations, including the selection of the elements and the size and spacing of the tested elements. Some of the enhancer-enhancer-promoter triples they test were also investigated by a different experimental design in Brosh et al 2023. Brosh et al observed non-additivity between these elements while this study did not. Ultimately we do not know which mechanisms produce the non-additivity that has been observed in native loci and which experimental designs would preserve such mechanisms.

Overall this is a nice experimental design and a great dataset for probing how enhancers and promoters combine to regulate gene expression. I have no major concerns, but I will try to clarify some methodological points I found confusing.

Methodology

The following two comments are meant to help the reader understand the methodology/terminology used in this paper and how it relates to other similar studies.

The interpretation that "promoters scale enhancer signals in a non-linear manner" is potentially confusing. I believe that the authors use "non-linear" to refer to the slopes (represented by the letter 'b' in Fig. 5b) being not equal to 1. Given how the boost index is defined, this implies the relationship

Activity of EEP = (Activity of CCP) * (Average Linear Boost)^b

One potential source of confusion is that the Average Linear Boost term itself depends on the set of promoters that are assayed. Averaging across (many) promoters may alleviate this concern, in which case Average Linear Boost may be considered some form of intrinsic enhancer strength. If so, there is a correspondence between this terminology and the terminology presented in Bergman et al 2022. If b not equal to 1 refers to a non-linear scaling, then the reader may think that b=1 refers to a linear scaling. But if b=1, and the Average Linear Boost term is interpreted as intrinsic enhancer strength, then the equation above implies that the activity of EEP is equal to an intrinsic promoter strength times an intrinsic enhancer strength. This is essentially the relationship that is considered in Bergman et al 2022 and which is referred to in that paper as 'multiplicative'. The purpose of this comment is not to argue for what is the relationship that best explains the data, it is just to clarify the terminology.

Enhancer-promoter selectivity: As a follow-up to a previous study (Martinez-Ara et al, Molecular Cell 2022) the authors mention that the data in this study also shows that enhancers show selectivity for certain promoters. I found the methodology hard to follow, so this section of the review is meant to guide the reader in understanding how the authors define 'selectivity'. The authors consider an enhancer to be not selective if its 'boost index' is the same across a set of promoters. 'Boost index' is defined to be the ratio of the reporter output with the enhancer and promoter divided by the reporter output with just the promoter. Conceptually, I think that considering the boost index is a reasonable way to quantify selectivity. The authors use a frequentist approach to classify each enhancer as selective or not selective. The null hypothesis is that the boost index of the enhancer is equal across a set of promoters. This can be visualized in Fig. 2C where the null hypothesis is that the mean of each vertical distribution is equal. Note that in Figure S4b of this paper (and in Figure 4B of their 2022 paper) the within-group variance is not plotted. Statistical significance is assessed using a Welch F-test.
