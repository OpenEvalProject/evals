# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37272.047](https://doi.org/10.7554/eLife.37272.047)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fitness effects of altering gene expression noise in Saccharomyces cerevisiae" for consideration by eLife. Your article has been reviewed by Naama Barkai as the Senior Editor, a Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Kevin J Verstrepen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

As you will see below, both reviewers liked the work. They appreciated the concept and recommended the experiments. Regarding the conclusions, the reviewers felt that they were rather expected, somewhat reducing enthusiasm.

The most important shared concern is whether the mutants used in this study offer a fair comparison to natural variants with different noise levels. The potential discrepancy between artificial and natural variants seems difficult to avoid, but at the very least, it should be acknowledged and critically discussed. We do recommend that you will perform the experiments suggested which relate to this point (in particular, measuring single-cell growth). Both reviewers felt that they will significantly upgrade the work, although they did not consider it as a must for publication. Critical discussion of this point was considered to be essential.

Reviewer #1:

The manuscript by Duveau et al. examines the impact of expression levels and noise in synthetic mutants of TDH3. This group has previously demonstrated that noise in TDH3 expression is under purifying selection in wild yeast (Metzger et al., 2015), and this paper follows up on this finding by showing that, at least for synthetic mutants in a stable environment, the fitness effect of expression noise depends on the mean expression level and vice versa. Higher noise is generally beneficial when TDH3 expression level is far from the optimum, but deleterious when near the optimum. The study is technically rigorous and carefully performed, and the results, although expected from previous theoretical and experimental work in expression noise and bet hedging, do experimentally demonstrate the important interdependence between mean expression level and noise on fitness in a stable environment.

Essential revisions:

1) The authors select 43 of 171 constructs generated to study further based on the expression level and expression noise profiles. However, the reader never sees the data for the full set and it is difficult to determine if the chosen set is representative. This should be included in a supplemental figure.

2) Naturally occurring variants of in the TDH3 promoter were not studied here because the authors report that they strongly co-vary, making it difficult to separate the fitness effects of mean expression level and noise. Shouldn't the relationship of covariance of these variants, which have seen natural selection, be different from the designed mutations used here? Based on the results presented here, one would predict that the LOESS curves of the relationship between median expression and noise would have different patterns, with few naturally occurring variants displaying both low expression and low noise. Along similar lines, it appears from previous work (Metzger et al., 2015) that naturally occurring variation appears to only increase expression noise. Is this only happening when TDH3 expression is far from the optimum?

3) More generally, I am having trouble connecting the results presented here to naturally occurring expression noise. The authors have convincingly demonstrated that higher noise is favored in a stable environment when the mean expression is far from the optimum. Based on previous theoretical and experimental work, this was expected. However, does this have anything to do with why expression noise varies across genotypes or genes? At least two other possibilities exist: (1) the fitness effects of changes in noise are not strong enough to be subject to selection (Metzger et al., 2015, shows this is likely not to be true for TDH3), or (2) higher noise is more fit in fluctuating environments. A reasonable hypothesis is that optimal expression levels of TDH3 (involved in glycolysis and gluconeogenesis) would be highly dependent on nutrient availability of the environment, and that nutrient availability could change quickly, making high noise in expression adaptive. This hypothesis is supported by a number of studies that find bet-hedging-like mechanisms are playing out during nutrient shifts. Yet, this possibility is not directly addressed in this manuscript, rather the entire manuscript assumes that a stable environment with respect to TDH3 expression can be reached. Thus, beyond careful experimental validation of an expected result, I am unsure what I have learned from this work. Comparisons between synthetic mutants and naturally occurring variation or across environmental fluctuations may be needed to increase impact.

Reviewer #2:

This study measures the fitness effect of a set of 236 mutant alleles of the TDH3 promoter in S. cerevisiae. YFP fusions were used to estimate TDH3 transcriptional activity and expression noise. Some of the mutants showed a different average expression of TDH3, some showed a different noise level, and most showed a combination of these effects. Comparing the fitness effects and transcription phenotype of different mutants indicates that high expression noise is detrimental when the average expression is close to the optimum/wild-type level, whereas increased noise has a positive fitness effect when the average expression levels deviate from the optimal/wild-type levels. Together, these results further confirm earlier studies that suggest that noise can help to diminish the negative fitness effects associated with a suboptimal (average) expression level because a fraction of the population will have a more optimal expression level (and this faster-growing fraction drives the average growth rate up), while on the other hand, noise may be selected against in populations where average expression is near-optimal.

Despite a few issues that merit a response from the authors (indicated below), I really like this study because its elegant and simple design provides leads to a clear conclusion that helps to answers an important question. Specifically, I appreciate the efforts to provide solid experimental data and the fair discussion of the results. Moreover, the text is particularly well-written.

I see four issues that perhaps should be addressed or at least acknowledged in the Discussion section.

Firstly, one can never be completely sure that the promoter variants that are generated offer a good and fair comparison to naturally-occurring variation in expression noise. For example, in theory, it is possible that some promoter/TATA box mutations might have pleiotropic fitness effects. I understand that this is difficult to avoid, and that the use of many different mutants at least partly mitigates this worry, but perhaps it should be acknowledged in the Discussion section.

Second, whereas widely accepted as a good method to measure expression noise, using promoter-YFP fusions as a proxy for expression/mRNA abundance inevitably has some shortcomings. I don't think it necessary to directly measure RNA levels in single cells across all the mutants, but perhaps a few mutants could be assayed to confirm that expression is accurately estimated? Moreover, the YFP fusions may also not perfectly align with Tdh3 protein levels (for example if Tdh3 levels would also be controlled post-transcriptionally). Making Tdh3-YFP fusions would only partly resolve this issue, as the YFP tag may influence Tdh3 stability. While these effects are again difficult to avoid and are unlikely to cause serious artefacts, it would be good to mention the issue in the discussion.

Third, it is a pity that the authors do not directly link single-cell expression levels with fitness. Instead, they use a model that tried to link a cell's TDH3 expression to its replicative fitness. Using Tdh3-YFP protein fusions combined with single-cell monitoring technologies (e.g. simply using time-lapse microscopy to evaluate the growth rate a few single cells as they grow into microcolonies or using flow cells such as the commercially available CellAsic system), it should be relatively easy to directly measure the replication rate of cells and correlate this with the individual TDH3 expression level (as estimated by YFP fluorescence). This would really tie the study together and allow linking noise to individual fitness to population-level fitness (as also suggested by the authors in the Conclusions section).

Fourth, is the number of cells with average (population-level) expression close to the optimum large enough to draw reliable conclusions? Given the considerable variation in the relation between fitness and mean expression level observed in the (much larger) set of mutants where average expression is not optimal, my gut feeling dictates some caution.
