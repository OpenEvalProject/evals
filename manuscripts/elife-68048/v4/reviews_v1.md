# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68048.sa0](https://doi.org/10.7554/eLife.68048.sa0)

In this study, Izgi et al. investigated age-dependent gene expression pattern changes in male mice by analysing a new bulk RNA-seq data from four different tissues collected at different ages covering postnatal development and ageing. Gene expression patterns observed before sexual maturity show inter-tissue divergence, whereas convergence of gene expression profiles is observed after sexual maturity and during ageing, in a pattern that the authors call divergence-convergence or ‘DiCo.’ This observation may suggest that ageing results in at least a partial loss of tissue identity acquired developmentally.


---

# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68048.sa1](https://doi.org/10.7554/eLife.68048.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Inter-tissue convergence of gene expression and loss of cellular identity during ageing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Matt Kaeberlein as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission.

Essential revisions:

1. The reviewers noted some potential issues with the normalization of the RNA-seq data that could affect the results, including the use of FPKM normalization, which may drive some of the observations due to lack of inter-sample-normalization (see specific comments by Reviewers #2 and 3). The authors would need to show that using appropriate count-based methods yields similar conclusions.

2. The authors often support their conclusions on low effect sizes and significance above usual thresholds. It would be important to explicitly discuss these as caveats, as well as strongly tone down these conclusions (including in the title.). More generally, the reviewers felt that potential alternative hypotheses needed to be clearly laid out, and potential ruled out, for the manuscript to stand more strongly (see specific comments by Reviewers #1, 2 and 3.)

3. In general, the reviewers felt that additional information on methods was required for reproducibility (see individual reviewer reports for specific points).

Reviewer #1 (Recommendations for the authors):

1. "Such "runaway development" phenomena may be due to insufficient natural selection pressure to optimise regulation after sexual reproduction starts." As stated, this sentence suggests that maladaptive traits that could lower an organism's total reproductive success would not be selected against as long as they only appear after the beginning of reproduction. I would perhaps ask that here the authors cite, not a general review of evolutionary theories of aging, but a publication that specifically proposes that alleles that are deleterious as early as the beginning of sexual reproduction nevertheless are not selected against.

2. Lines 84-91, 145-153, 229-240, 245-250, etc. Here the font size changes in the manuscript which I assume is not intended.

3. Figure 1 caption. "Similarities were calculated using Spearman correlations coefficient between expression-age correlations across tissues." Here I suspect that "Spearman correlations coefficient" was intended to be "Spearman's correlation coefficient".

Reviewer #2 (Recommendations for the authors):

Although the authors report an intriguing finding, there are major issues in the manuscript as it stands, notably concerning the clarity and rigor of the data analysis and manuscript.

1. For the analysis of their RNA-seq dataset across samples, the authors describe using the FPKM framework (methods, line 438). This is very problematic for a number of reasons – use of FPKM for differential gene analysis across samples is deprecated because it poorly controls for inter-sample variability [PMID: 22988256; PMID: 32284352]. FPKM are not comparable between samples because the normalization is sample-specific – thus, since no cross-library normalization step is performed, it should never be used for between sample comparison. Thanks to community benchmarking efforts, TMM or VST normalized counts are widely believed to be the superior choice for DGE analysis [PMID: 22988256; PMID: 32284352]. Thus, it is crucial that the authors correct their analysis to avoid the use of FPKM, and show that their conclusions would hold with an analysis on TMM or VST normalized counts.

2. There are issues regarding consistency in analytical choices throughout the paper.

a. Application of significance cutoffs vary widely in the manuscript when selecting specific gene sets. Reasoning should be provided for each case in which significance cutoff was (or not) applied (e.g. Line 111). For example, it is rather concerning that in Figure 1d, no gene was significantly up-regulated with age in the muscle (significance cutoff applied), but in Figure 1f, a large proportion of genes are shown to increase in expression with age in the muscle (significance cutoff not applied).

b. Authors are not consistent with the FDR threshold applied (e.g. FDR < 10% in Line 123, FDR 20% in Line 127). The reasoning for the chosen thresholds, as well as the different choices should be provided for cases in which higher than standard FDR is applied.

c. In Figure 1, authors show that the muscle presents with the least number of significantly changed gene expression patterns (up and down) with age. Additionally, in the manuscript, the authors explain that the lack of genes that show statistically significant change in the muscle is supported by a previous study that also showed "weak ageing transcriptome signature across multiple datasets (Line 137)." Thus, it is rather concerning that excluding the cortex, a tissue with a large number of differentially expressed genes, for CoV calculation resulted in greater significance.

d. The authors use a mix of multiple correction methods without clear explanations as to why a consistent measure isn't used (i.e. FDR/BH, BY) – BY test is justified for GO analysis line 472, but why BY was not used for DGE analysis is not clear (line 462).

e. A number of statistical analyses performed in the manuscript do not pass the standard significance thresholds (FDR < 5% or p < 0.05). The standard applied in the field is usually p-value or FDR < 5%, although relaxing this threshold can be done when dealing with noisier datasets. When using more relaxed FDR or p-value thresholds, the authors should also be careful to strongly tone down statements proportionally to the lower statistical support for their claims (eg. Line 240: "a SIGNIFICANT divergence-convergence pattern).

3. The authors use a dataset from exclusively male mice. Since aging is known to be extremely sex-dimorphic [PMID: 27304504], the authors need to explicitly discuss this caveat/limitation in the main text (i.e. these observations may not hold in female animals). If the authors wish to make a more general statement, a suggestion would be to reanalyze data from the recent Tabula Muris Senis Companion paper Schaum et al., [PMID: 32669715], which includes similar tissues, "developmental" time points (1 vs 3 months) and aging course (3 to 27 months), and both sexes to extend the findings. In addition, the Schaum dataset is also RNA-seq, and thus more directly comparable to the author's dataset compared to the microarray Jonker dataset used for partial validation (Figure 2 – supplement 8).

4. The authors should consider revising the title, since the current form seems to indicate that the work discovered s significant loss of cellular identity during aging. This statement is too strong based on the analyses of the paper. We suggest toning down the title, for instance to "Transcriptomic analyses suggest inter-tissue convergence of gene expression and loss of cellular identity during ageing".

Reviewer #3 (Recommendations for the authors):

Authors only analyze the gene sets that are correlated with age i.e. linearly go up or down with age. However, ageing trajectories for different genes can be very dynamic. This is the likely reason why only a few age-related changes were detected in some tissues. To assess the robustness of some of the key observations, authors should consider an orthogonal and unbiased clustering analysis similar to Figure 2 supplement to get the patterns for gene expression changes with age and to what extent DiCo is observed with different clusters.

Some of the key observations have either low effect size or are not statistically significant. For example, inter-tissue expression similarity during ageing and development (lines 115-119), the expression reversal (lines 158-161), changes in coefficient of variation with age (lines 202-207) etc. Authors clearly mention these in the manuscript, but it raises concerns on the extent to which some of these observations might be random, or due to idiosyncrasies of RNA-seq itself. These caveats should also be discussed.

In the global PCA based analysis for figure 1 and 2 combining both development and ageing data, the variance can be driven by one of the two states. For example, transcription divergence analysis in PCA in figure 1 based on development alone is not significant which suggests that the divergence of the developmental samples is driven in-fact by ageing. For PCA based analysis using separate PCAs for development and ageing will be more statistically sound.

Are there any known gene categories that have stronger expression reversal trends? For example, do known transcription factors or pathways that regulate development show DiCo if analyzed separately? Or is this trend only seen at the genome-wide level and completely stochastic?

For functional enrichment analyses authors only mention some selected functions in the text but GO terms have a lot of redundancy and it is unclear if there is any emerging functional trends looking beyond the redundancy or selected examples. It will be useful to thoroughly analyze and summarize the enriched GO terms to assess for any functional patterns that connect functional decline with ageing and convergent expression or DiCo.

Is there a significant overlap between mouse and human ageing related changes at the gene or pathway level?

Line 299 – linking the functional categories with cellular identity appears a bit hand-wavy. Stronger support would be needed to make this conclusion.

Some of the aspects need more methodological details:

For RNA-seq analysis, were all the samples normalized together, or were development and ageing samples normalized separately? It should be clarified in the methods.

Were the mouse perfused? The details should be added in methods. If the mouse were not perfused, a significant shared proportion of gene expression can be due to blood components. Also, the possibility that some of the shared changes could be due to infiltration of immune and other cell types in tissues should be mentioned.

More details for single cell deconvolution should be added in methods.

It is unclear to me how how the age related gene expression and PC correlation was performed. Was the loadings underlying PC axes used for correlation analysis? It should be elaborated in methods.

Some of the supplemental figures are missing.
