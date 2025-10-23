# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50240.sa1](https://doi.org/10.7554/eLife.50240.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work emphasizes the importance of controlling for age in microbiome research and provides strategies for adjusting for this confounding factor across multiple disease areas. These results also set the stage for follow-on studies of the mechanisms responsible for these associations and their relevance to health and disease.

Decision letter after peer review:

Thank you for submitting your article "Adjusting for age improves identification of gut microbiome alterations in multiple diseases" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Peter Turnbaugh as the Reviewing Editor and Reviewer #2, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Catherine A Lozupone (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, the authors perform a meta-analysis of publicly available shotgun metagenomics datasets and identify interactions between age and microbiome associates with different diseases. Overall, this work addresses an important question. In addition to yielding insights into microbiome correlates across a variety of diseases when controlling for age in this particular meta-analysis, it provides guidance to other researchers that age is an important component to consider in study design when conducting microbiome/disease research. The manuscript is well written and state-of-the-art analysis techniques are applied. The overall conclusions are interesting in that random forest classifiers in the elderly group do not do a good job classifying the young (and vice versa), and that there are shared microbiome signatures with diseases that are affected by age.

Essential revisions:

1) The evaluation relies on random forests, a tool for classification, when the paper is really more about adjusting for confounders, which RFs don't intrinsically handle. The authors might be better served using an established meta-analytic framework like a mixed effects model. In order to use the RF for their purposes, the authors have to subsample their data extensively and have to perform a lot of pairwise analyses where controls from the same continent are pooled (and differences between countries on the same continent ignored). A hierarchical model should be able to capture and adjust for effects of continent and country in a way that made more efficient use of the available samples, would offer some protection against unbalanced examples, and would have more easily interpretable coefficients. While it's true that random forests have better classifier performance than, e.g. a logistic regression, the resulting models are harder to interpret, and because the methods here are somewhat ad hoc, it is tough to get a sense for how the decisions the authors made in processing the data ended up affecting the results.

1a) In particular, the analyses involve a lot of comparisons of heavily derived summary statistics from random forest models, like AUC and feature importance, but the statistical significance of these differences is not always clear. While Figure 1 does appear to use a statistical test to evaluate AUC differences (for models trained on one age group and evaluated on the same/different age groups), the replication for CRC in Figure 3A does not. I also can't find a description of what test was used and what cutoff was called significant.

1b) The authors also say that the pattern they observe in Figure 3A is "exactly the same" as in Figure 1D, but it is difficult to tell whether this is accurate. In Figure 1D, performance mainly drops for models tested on elderly (E) samples, whereas in Figure 3A, performance mainly drops for models trained on (E) samples, with very little difference in evaluation performance when models trained on young/middle (YM) samples are evaluated on E samples. In fact, the AUCs in the lower panel of Figure 3A are all pretty similar, despite the strong color differences – a more globally consistent color scheme would help, and speaking of color, there seems to be an error in Figure 1D – Cirrhosis (0.97 is shaded darker than 0.95).

1c) In Figure 2, the cutoff (eighty fifth percentile of Gini decrease) is never justified and the subsequent filtering step struck me as unclear. The authors say they performed Mann Whitney U tests of marker scores across at least two age groups, but isn't there only one marker score per age bracket?

2) The authors mainly graph derived measures like AUC and feature importance without ever really visualizing the original data, with the exception of some of the metabolite measurements in the last figure. The closest we get are the name colors in Figure 2. This is important to sanity-check the results based on summary statistics, to show more clearly the extent of the age confounding, and to show what it is specifically about the aging-related markers that is being captured by the model. Visualization could capture whether, for example, in addition to greater loss, E samples had more "noise" or β-diversity compared to YM samples, and whether the aging signal was consistent across continents or driven by different taxa in different locations. Without visualizing, it's hard to get a sense of the scope of the issue.

3) The authors were sensitive to the fact that DNA sequencing/ extraction methodology can affect microbiome profiles which is good. They handled this by excluded some samples from a particular DNA extraction methodology that produced differences in observed diversity. It is strange, however, that after this step to reduce this confounding, addition samples from studies of IBD, CRC and ELDERMET were then added. Why would one add new samples after and not before taking steps to address effects of DNA sequencing/ extraction methodology? Later in the paper it becomes clearer that these other added studies are more validation cohorts and perhaps this is why? This should be clearer. Also, since there still was a minor effect of these factors after removing the samples with a large DNA extraction effect, it might be good to adjust for these differences in methods in the Adonis tests (e.g. DNA extraction + age in the model). Also, is seems that other factors about experimental protocol could also affect observed diversity- e.g. which kit was used to prepare the libraries (Tru-Seq versus others)?

4) It is unclear how the Adonis/PERMANOVA was performed to produce the data show in in Figure 1A. Our impression is that these tests were run independently for each metadata category but that is not completely clear. It seems that taking advantage of being able to control for confounding by running Adonis with more complex models (as suggested above for DNA extraction) might be good.

5) We'd like to see the data presentation and interpretation modified to try to avoid a potential bias towards age as an important covariate. Multiple metrics presented throughout the study are equivocal or even supportive of consistent trends despite age. The authors should be careful to point this out and to present a more nuanced interpretation that only some aspects of the microbiome are associated with aging.

6) The authors need to revise the main text to be more careful about the language used to avoid conflating correlation with causation. Words like "impact", "reinforced by", "influence", etc. imply that there is causal information where none exists.

7) The full dataset analyzed here needs to be made publicly available prior to publication. It's not sufficient to ask readers to re-assemble the full meta-analysis on their own.

8) Add analyses wherein each individual study is analyzed separately, as opposed to the current analysis which involves merging data across all the studies. The current approach has the downside of being influenced by the larger studies, whereas the former would allow for statements about the degree to which associations with age are reproducible across studies. That said, I'm not sure this is possible given the nature of the data. At a minimum, it would help to have some supplemental figures that depict the distribution of ages within and across studies.

9) The Discussion section really nails a critical confounder, drug use, which could explain a lot of what is described here. Diet and lifestyle are also likely contributors to these associations. While I don't think these data can be used to de-couple these factors, it would be good to be more explicit about this issue in the abstract and introduction. As written, the reader might take away the possibly false conclusion that aging itself (independent of diet, drugs, etc) is associated with the gut microbiome.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Adjusting for age improves identification of gut microbiome alterations in multiple diseases" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Peter Turnbaugh as the Reviewing Editor and Reviewer #2, and the evaluation has been overseen by Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Catherine A Lozupone (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have expanded the analyses they originally put forth showing that age is a potential confounder in microbiome association studies. The addition of the PERMANOVA and the linear modeling makes the paper stronger, and the reviewers appreciated the authors making it clearer how they determined significance in the random forest studies.

Essential revisions:

Two remaining concerns about the statistic used need to be addressed prior to publication.

1) We appreciate seeing the distributions of AUCs that the authors generated, and this does help to make their point more convincing. However, now that we understand better what they did, we're not sure that the test they used is appropriate. It seems that the authors are partitioning studies into age groups, training on a randomly-sampled subset of one age group, then testing on the remaining held-out samples from the 1-2 other age groups. This is all good practice so far. The issue is that the authors seem to be doing this repeatedly to get a distribution of AUCs per cohort, then testing for significant differences between the AUC distributions per cohort, using a Mann-Whitney U test. The problem with this is that AUCs within a cohort are not actually independent of each other (which the M-W test requires), because some classifiers will have been trained on the same subsamples. This could make the distribution of AUCs look narrower than it really is. Further, the same classifier is being used on each age group, which means there are also correlated errors across cohorts. Testing for a significant difference between AUCs is actually a pretty subtle and difficult problem, which is another reason we prefer making statements about significance using explicit statistical models like logistic regression, whose properties are better understood.

If the authors really want to test for significant differences between these models, we would encourage them instead to use a permutation test: i.e., shuffle the labels of the age cohorts repeatedly, then use the empirical distribution of differences in AUCs between cohorts to test for significance. This should at least ensure that the correlations introduced by sampling and by testing the same classifier on multiple cohorts will also be present in the null distributions.

2) We also have one more substantive concern with Figure 5. We appreciate the authors did not drop low nominal p-values, but it is also not appropriate to use a fold-change cutoff before applying p-value corrections. Any filtering that uses information about the difference between groups (which includes fold-change cutoffs) is statistical double-dipping and will tend to inflate significance. You can either apply the fold-change cutoff after p-value correction or apply a filter that doesn't depend on knowledge about which samples belong to which groups, like the overall variance or the number of non-zero observations.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Adjusting for age improves identification of gut microbiome alterations in multiple diseases" for further consideration by eLife. Your revised article has been evaluated by Wendy Garrett (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

It is unclear in the main text why 2 different approaches are needed – especially since the last paragraph of subsection “Influence of age on the microbiome and microbiome-disease signatures” only refers to the results of the permutation based strategy. Seems like might be more straightforward to just report the latter, but at the least the results of both and not just one of the approaches should be reported if both are described.

In subsection “Influence of age on the microbiome and microbiome-disease signatures”, where authors say "In summary, in each disease-age-group scenario, we used two different approaches. " They should qualify for what – "e.g. we used two different approaches to assess whether disease classification performance was significantly different between same age group classification and different age group classification".

In subsection “Influence of age on the microbiome and microbiome-disease signatures”: "is significantly different from what would be expected by random (null distribution) " should briefly quality "generated by permuting the age-group labels of the subjects"

There was also a minor concern with the permutation test. The authors seem to be getting one average true or permuted AUC for each of the 100 resampled classifiers, instead of averaging across classifiers and getting one AUC per permutation (comparing the "true" value to this null to get a p-value). Because of non-independence between the training and test samples the classifiers used, the author's procedure should yield narrower AUC distributions, which could inflate significance. A back of the envelope estimate suggests an average overlap between classifiers of around 10-20% of the training + test samples. Given the consistency of the story and the magnitude of the differences the authors observe, though, as well as the computational time cost of doing enough permutations to get an accurate p-value, we leave it up to the authors whether they want to 'inoculate themselves against' this particular criticism.

Several different FDR cutoffs are used (0.15, 0.20, 0.25) with no explanation. Figure 6D seems particularly arbitrary in its use of two different thresholds, neither of which is that common (0.15 and 0.20). For that figure, in the absence of a really good reason to pick those specific cutoffs, it would probably be more transparent to just pick one standard threshold (e.g. 0.25) and to just make it really clear that Figure 6D represents a selection of the most significant of the resulting hits. The authors would of course also need to report how many total hits were significant at this threshold, and to make the full list available.

The authors should pick either one of Spearman or Kendall distances; using both in different places is confusing. (Bray-Curtis is another option for calculating divergence between microbiome abundance profiles.)
