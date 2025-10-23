# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99602.4.sa0](https://doi.org/10.7554/eLife.99602.4.sa0)

This study presents data on sex differences in gene expression across organs of four mice taxa. The authors have generated a unique and convincing dataset that fills a gap left by previous studies. They claim that sex-biased expression in the soma can overlap between genetic males and females, and that the relevant patterns both turn over quickly over short evolutionary times and do so faster in somatic than gonadal tissues. These conclusions could largely have been predicted by extrapolating from previous findings in the field, but nevertheless demonstrating them directly is a fundamental advance.

[Editorial note: The work was originally assessed by colleagues who are active in the field of evolution of sex differences or in areas adjacent to this field (see initial assessment at https://doi.org/10.7554/eLife.99602.2). The appeals process involved consultation with experts working in other areas of evolutionary biology. The above assessment synthesises the opinions of both sets of reviewers.]


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99602.4.sa1](https://doi.org/10.7554/eLife.99602.4.sa1)

The paper by Xie et al. investigates the micro-evolutionary dynamics of sex-biased gene expression across somatic and gonadal tissues in four mouse taxa, with comparative analyses in humans. The study introduces a new metric, the Sex-Bias Index (SBI), to quantify individual-level variation in sex-biased gene expression, and explores the evolutionary turnover, variance, and adaptive evolution of these genes.

These strengths of the paper are not in dispute:

Novelty: The study is among the first to systematically analyze sex-biased gene expression at a micro-evolutionary scale in outbred animals, using closely related mouse taxa. This contrasts with most previous work, which focused on macro-evolutionary comparisons between distant species.

Controlled Sampling: The use of age-matched, outbred individuals raised under standardized conditions minimizes environmental confounders, allowing for robust within- and between-taxon comparisons.

Somatic vs. Gonadal Focus: Unlike many earlier studies that emphasized gonadal tissues, this work provides a detailed analysis of somatic organs, revealing rapid evolutionary turnover and mosaicism in sex-biased gene expression.

Sex-Bias Index (SBI): The SBI offers a cumulative, individual-level measure of sex-biased gene expression, facilitating visualization of variance and overlap between sexes within tissues. While one can argue about whether a new metric is necessary (as the authors argue), the combination of fold-change cutoffs, non-parametric Wilcoxon tests, and FDR correction reduces false positives, addressing concerns raised in the field about inflated detection of sex-biased genes.

Evolutionary implications: The study demonstrates that sex-biased gene expression in somatic tissues evolves more rapidly than in gonads, and that this turnover is often accompanied by signatures of adaptive protein evolution. The lack of correlation in SBI across tissues within individuals supports a mosaic model of sex-biased gene expression, challenging binary models of sexual differentiation.

The weaknesses are already listed by previous rounds of review but I will add one more: in an attempt to be comprehensive, the writing is quite dry and the main conclusions sort of get hidden within the less important observations.

Since the debate is mostly about what words to use to describe the importance and the strength of evidence, I thought it would be useful to directly compare this study to other studies that address the same topic:

Naqvi et al. Science 2019 (David Page lab): Conservation, acquisition, and functional impact of sex-biased gene expression in mammals

Oliva et al. Science 2020 (Stranger lab): The impact of sex on gene expression across human tissues

Rodríguez-Montes et al. Science 2023 (Kaessman, Cardoso-Moreira labs)

Let's start with the fact that all three peer studies have had a major impact. Second, although Naqvi et al. (2019) and Oliva et al. (2020) provided foundational cross-species and cross-tissue analyses of sex-biased gene expression, but did not address micro-evolutionary turnover or individual-level variance. Third, Rodríguez-Montes et al. (2023) focused on developmental and evolutionary patterns of sex-biased expression, but at a broader phylogenetic scale and without the individual-level or module-based analyses presented here. None of the peer studies addressed the possibility of mosaicism within individuals, none of them addressed the relations between expression bias and adaptive evolution. So the comparison is really a bit of an apples to oranges comparison: the peer studies are about patterns in deep phylogeny, whereas the present study is an amazing (to me) analysis of inter-individual mosaicism, which is at the heart of this kind of variation, which would totally be missed or worse misinterpreted in deep phylogenetic analyses. Having said that, in my subjective opinion, all three related papers are better written than the present one, but to me there is no question this belongs in the same pedestal as all of them.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99602.4.sa2](https://doi.org/10.7554/eLife.99602.4.sa2)

Xie et al. present a data set of impressive size to study changes in sex-biased gene expression. A clear strength that sets the study apart from previous work is the use of age-matched outbred individuals raised in the same environment, which minimizes non-genetic variance, and the comparison of closely related taxa. Also in contrast to many previous studies, while gonads, which have often been the focus of sex-biased gene expression studies, are not ignored, multiple gonadal tissues are being compared to an array of somatic tissues. The study design therefore can offer a particularly rich and nuanced view of how sex differences change across tissues and over short evolutionary times.

I liked the idea of summarizing over the mean expression of gene sets, instead of just using numbers of DEGs for comparisons, even though the introduction of the term "Sex-Biased Index (SBI)" seems somewhat of an overkill. The summary analyses are definitely useful to visualize variability in sex-biased gene expression programs. The authors find that the expression patterns of sex-biased genes change faster than those of non-sex-biased genes - but only in somatic tissues. They also provide some evidence that this correlates with higher rates of potentially adaptive coding sequence changes in the taxa where expression is sex-biased, with the proviso that a stronger modeling framework would have made these inferences more robust.

I was most surprised by the finding that the fast change in expression patterns is linked to different gene expression modules becoming sex-biased in the different taxa studied. This is in my eyes a remarkable observation that could not have been predicted from previous knowledge.

The use of human GTEx and patient scRNA-seq data is a nice addition, although there are known confounding issues with these resources, given that these are not random samples and environmental conditions are uncontrolled. Nevertheless, as the human data echo the trends seen with the much more rigorous mouse data set, I do not have principal objections to this addition. Furthermore, the human data do allow the authors to conclude that only very few genes with sex-biased expression are shared in the soma of mice and humans.

In summary, I believe that this contribution has the potential to fundamentally change how we see sex-biased gene expression differences in vertebrates, given that the author's conclusions are grounded in a data set of compelling quality and size.
