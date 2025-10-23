# Peer review - Round 1

Editors:
- Deborah Bourc'his, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83364.sa0](https://doi.org/10.7554/eLife.83364.sa0)

This manuscript presents a useful meta-analysis of genes with parent-specific expression from mouse-published RNA-seq datasets, focusing on genes with weak allelic bias. A combination of systematic bioinformatic analysis and experimental validation convincingly shows that the number of parentally biased genes has been overestimated and the few novel ones lie at the periphery of known imprinted loci. The work will be of interest to genomicists with an interest in imprinting and its mechanisms.


---

# Peer review - Round 1

Editors:
- Deborah Bourc'his, https://ror.org/04t0gwh46 Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83364.sa1](https://doi.org/10.7554/eLife.83364.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Weak parent-of-origin expression bias: is this imprinting?" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The three reviewers overall appreciated the work, and the clarification it provides about the genome-wide occurrence of genomic imprinting. In addition, please provide a point-to-point answer to the reviewers.

1) Improve Figure 3 D.

2) Address the question as to why allelic ratios in the pyrosequencing analyses were not systematically normalized by amplification biases of gDNA.

3) Provide expression level comparison between true imprinted genes (confirmed ones) and the ones that were falsely called with (weak) parental bias.

Reviewer #2 (Recommendations for the authors):

Pcdhb12 – "This is not imprinting per se as does not reflect a bias in single cells but rather a population bias within the brain of individuals." This sentence should either have a reference to previous work about random monoallelic expression (if it is convincingly shown there) or it should be softened, since the data of this study doesn't allow making conclusions about population bias.

gDNA amplification bias in the pyrosequencing data – as indicated above, I don't understand (a) why this is not corrected for all loci. Even if the bias is very small, this would feel like the right thing to do, (b) if/when it's corrected, showing the 50-50 ratio in plots is meaningless and I'd suggest omitting it, or showing the original bias.

Reviewer #3 (Recommendations for the authors):

It appears that thresholding is used in calling allelic bias: "Expression was called as biallelic if the mean of the paternal expression from both the C57BL/6 x CastEiJ and CastEiJ x C57BL/6 crosses was between 45 and 55%". At the same time they provide the explanation of an important statistical flaw of such approaches: "expression levels can influence ASE calling: the lack of read depth in lowly expressed genes may erroneously lead to genes being called as biased, because a small difference in read numbers produces larger bias in weakly expressed transcripts". An additional source of FP is overdispersion (i.e. additional variation present compared to statistical model), which might introduce significant changes in width of confidence intervals.
