# Peer review - Round 1

Editors:
- Ruth Loos, The Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48376.sa1](https://doi.org/10.7554/eLife.48376.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Polygenic scores are being generated for an increasingly large number of traits, and are beginning to be used outside of a narrow research context. However many questions remain about how and when it is appropriate to use them. One oft-discussed concern is whether polygenic scores are "portable" between ancestry groups. But this study demonstrates that polygenic scores are often not even portable within ancestry groups when stratified on the basis of common demographic parameters. This and other results discussed in the paper raise important questions about the use of polygenic scores, and should be read and considered carefully by anyone designing, carrying out or applying the results of large-scale human genetic analyses.

Decision letter after peer review:

Thank you for submitting your article "Variable prediction accuracy of polygenic scores within an ancestry group" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Paul O'Reilly (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript in its current form would not, even with minor revision, be suitable for the journal. However, we would consider an extensively revised manuscript that addresses the following key concerns of the reviewers.

1) The paper will benefit from a clearer focus; while the authors aim was to simply establish the variable of portability between strata, they went quite further from this with the topics of assortative matting, sex balance, parents' effects, etc. Just achieving their main aim would make this paper very worthy as it points to issues that those already thinking in applying PRS in clinical practice right now need to urgently appreciate.

2) In focusing on the main aim, a deeper exploration of the causes that drive the lack of portability would increases the informativeness of the study. It was pointed out that the difference in portability across strata might be due to differences in power, sample size, heritability, phenotypic variance, phenotype distribution, influence of environment, insights in how these and potentially others affect portability would be helpful. This should also include a discussion on how is it that different strata can generate even higher predictive power than using the same stratum (in base and target) and why the PRS based on the full sample size, in the provided examples, always has a better "predictive ability" (highest R2), than PRS based on any of the strata.

3) Analysis of disease outcomes, here e.g. (extreme) obesity and hypertension, will be useful to translate findings to more clinical settings, including calculation of ROC-AUC, a standard easy-to-interpret predictive statistic.

Reviewer #1:

In this study, the authors examine the portability of polygenic scores within a homogeneous, generally healthy population of white British unrelated adults, living across the UK. They show that the PGS performance is influenced by age, sex, socio-economic status and study designs. The reduced accuracy of PGS is not (only) caused by environmental influences, the authors show that also the magnitude of the genetic effects among groups, and indirect effects of assortative mating affect the performance of the PGS.

While these findings raise important consideration with reference to the use of PGSs, it would have been interesting if they had gone a little deeper with their analyses; e.g. to also identify the features (distribution, prevalence of disease, effects of environment) of outcomes and covariates that impact the prediction performance the most.

It seems that for all traits, even though there are differences in R2 for sex-specific, age-specific and SES-specific PGSs, the highest R2 (still low) is achieved when the PGS is generated in the full population. Thus, isn't the conclusion then simply that stratification lowers the PGS performance and that a (blunt) PGS, based on the most comprehensive possible population performs best?

The authors only considered continuous outcomes for "prediction"; it would be informative to also include dichotomous/disease outcomes (related to the continuous risk factors), such as (extreme) obesity, hypertension, etc. That would also allow calculation prediction statistics such as AUC-ROC (sensitivity, specificity, PPV, NPV), which are easier to interpret in the context of clinical relevance.

The PGS was generated based on LD-based clumping, but it seems only one threshold was used; r2<0.1. From experience, it seems that higher LD threshold results in better performance of the PGS. Thus, it might be worth testing higher LD threshold for better performing PGSs.

Reviewer #2:

The manuscript of Mostafavi discusses a timely and important question: how accurate are polygenic risk scores (PRS) derived from GWAS studies and first validated in large, but single cohorts, when predicting risk in populations different to those used in their derivation. Recently GWAS studies have achieved sample sizes of a million subjects. In addition, the UK biobank has released rich datasets close to half a million people genotyped, extensively phenotyped, and followed so far for about 10 years. These resources have spurred the development of PRS for many traits ranging from complex disease onset, quantitative phenotypes, and even to sociological predictions. Furthermore, a number of direct to consumer companies have started to provide their customers PRS for medical traits. Therefore, the urgent question is how reliable are these scores and how well they port to other populations and people around the world.

Mostafavi work starts with the recent publications suggesting that PRS port poorly to populations other than European descent (the population object of most of the data available), in particular to African populations. There have been recent calls to expand GWAS and biobank style cohorts to include people from other ancestries around the world. However, Mostafavi analyzes now show that problems with portability are not just evident in different ancestries, but also to different strata from samples from European decent participants. If this is correct, this raises the urgency to hold off implementations of these scores in to healthcare settings until we truly understand how and when these scores can be applied across groups of people.

The authors provide a meticulous dissection of the situations when the PRS are not portable within people of the same Ancestry. They perform careful QC of the UK Biobank data, use reasonable methods to adjust the sample strata, perform the GWAS, and construct and test the PRS. The authors state that their main goal was to demonstrate how differences in the composition of the GWAS cohorts affect portability for different traits of interest within the same ancestry, and they achieve this. However, they do a good work exploring the possible factors involved in the reduced portability and leave us with important lessons on how our assumptions about GWAS data may be wrong at times. Their data and simulations add important information on how sex ratios, indirect effects, GxE, assortative mating and other factors confound the data and contribute to poor performance in subsets of the UK biobank subjects. The manuscript is well written and extensive details is provided on the methods and simulations. The main text is accompanied by extensive supplemental results of importance, which are referred at appropriate places in the text.

I have a number of questions that I would like the authors consider and when appropriate clarify in their final manuscript:

1) Throughout the manuscript the term "portability" is used and metrics that measure the performance of the PRS are used to judge whether portability is feasible or reduced. While this term has been used in prior literature w.r.t to the reduced ability of a PRS developed in cohorts of European descent people when applied to populations of different ancestry, this term is jargon. In statistics and machine learning the term that describes this poor performance is overfitting and the ability of a model, or in this case a PRS, to preform equally well in other samples, is termed generalization. Would it not be "overfitting" the term that more accurately describe the lack of "portability"?

2) The author's use R2 to measure the reduced generalization of the PRS to the different cohorts' strata, and they concede that is not clear what would be the best metric to use for this analysis. However, many publications use the AUC as a metric to decide the best model and threshold of SNPs to pick and to describe how the PRS augments other predictor bases on covariates or other factors. It is not intuitive how R2 correlates with AUC, and therefore it would be best if the authors try in at least one analysis to compare R2 to AUC.

3) Recent publications have used the LDPred method that uses as input summary statistics rather than genotypes to develop PRS based on UK Biobank data. Some of these have shown generalization to others cohorst. Can the author's comment whether LDpred features distinguished it from the methods used in their analysis conferring an advantage? PRS derived from LDpred also tend to include many more SNPs to achieve a greater AUC. The author's explore P-value cut-offs (and hence number of SNPS) in some analysis, but it was not clear whether this suggested more SNPs increases overfitting. Do the results from the author's suggest that including more SNPs increases overfitting?

Reviewer #3:

The generalisability of polygenic scores is an important issue given the possibility of them being incorporated in to healthcare soon. This paper makes excellent use of the UK Biobank resource to present two sets of interesting results relating to the predictive power of PRS. However, I'm not sure if the way in which the primary results are framed in relation to portability is quite right.

The first set of results appear to highlight how GWAS are better powered in certain subgroups of the population (eg. GWAS of DBP are better powered in women, BMI in those in middle age, years of schooling in lower SES groups). Years of schooling is better predicted in SES 4 by GWAS on SES 1 than by SES 4 itself – this shows hyper-portability, not limited portability as discussed throughout the article. This is also true for BMI and DBP (to a lesser extent DBP). The bivariate LD Score results showing genetic correlations close to 1 seems to support this being principally a power (rather than portability) issue, in which there are different relative contributions of genetics and the environment across the groups, making some better-powered to capture – largely the same – genetics. Based on the results (inc. those of Figure 2), I'd have thought that this is most likely due to the environment resulting in convergence and genetics resulting in divergence (at least in the case of BMI and education) – eg. BMI converges to low values in old age, irrespective of genetic predisposition (relatively), while education levels of those in the top SES are forced to be similar due to the qualification requirements of professional jobs. Thus, the highest phenotypic variance, heritability, and thus PRS predictive power for BMI is from the lower age group and schooling from the lowest SES. How specific this pattern of results is to these particular traits is unclear, and certainly there seems to be a somewhat different cause for the DBP results. However, in general I see these results as being analogous to eg. how GWAS on Alzheimer's is perhaps being best-powered to detect common genetic variants when applied to individuals in their 70s, GWAS on blood pressure best-powered when applied to individuals in their 30s, and lung cancer GWAS being optimised when applied to non-smokers.

While the downstream impact of variable GWAS power in different sub-groups on PRS prediction is extremely valuable to see here, I think the implications of these results may be missed unless discussed in the context of differential GWAS power in different sub-groups – eg. in relation to ancestry, the consensus is that portability will be optimised by expanding GWAS sampling to non-European populations, but the analogy is not true here – the consequence of these results (at least for these traits) is that portability will be optimised if GWAS sampling is restricted to those sub-groups for which heritability is highest (since, otherwise, the portability in fact seems high).

The second set of results expand on similar analyses by Kong et al., 2018 and Selzam et al., 2019, showing that the indirect effects of familial genetics, and potentially assortative mating, could contribute to standard PRS predictive power. Any impact on portability is not explicitly demonstrated here, but the point is made that differences in culture (family structures etc) could lead to significant differential portability given the strong influence of indirect effects on standard PRS for some traits. These are great results to see, and will add to the literature on the topic of indirect genetic effects nicely.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Variable prediction accuracy of polygenic scores within an ancestry group" for further consideration by eLife. Your revised article has been evaluated by Mark McCarthy (Senior Editor) and a Reviewing Editor.

The manuscript has been improved and reviewers were generally satisfied with the changes made. However, while discussing the revisions some remaining issues were noted that need to be addressed before acceptance, as outlined below:

1) As sample size is an important determinant of the accuracy of the association effect sizes and thus also of the prediction accuracy, the sample sizes of each stratum needs to be clearly stated. Currently, the use of "unstratified" and "all" is misleading as it would suggest it include the data of strata combined. However, this seems not the case; the "unstratified" or "all" have now been ("artificially") reduced to match the sample size of the strata, which is not intuitive. After all, when data for multiple strata is available, one would be better off combining all data, rather than using the strata. We suggest to clearly report sample sizes, and to choose a more precise terminology to describe the "unstratified" or "all" group. Including an "all" group, that combined strata, as before, would seem informative to illustrate that sample size trumps population-specificity.

2) One of the reviewers noted difference between the original Figure 1 and the new Figure 1, and wondered whether the data changed (slightly) compared to their previous version because the results are slightly different (easiest to see by comparing median/boxes of young/old in BMI plot between original and new versions). It would be worth checking that this is just updated UKB data rather than an error. Furthermore, the R2 for DBP in the "mixed GWAS" is just less than half than for the "total GWAS" (again comparing original Vs new figures), while for education there's a 10-fold difference (ie. doubling GWAS N has led to 10x greater R2).. This can be the case ('inflection points' and all), but it would be worth checking that there's no error here because it seems a little surprising.

Reviewer #1:

The authors have addressed all concerns and the revised version is more focused and conveys a clearer message.

While they now present the "all" GWAS for the same sample size as for the stratified GWAS, this has not been presented in a very clear way. In the text, L179 they state they use the same sample size, but it would be good to report what this sample size is. Intuitively, one would not expect that an "all" GWAS had the same sample size as a stratified GWAS.

I suggest to clarify this in the legends of the figures, and also more clearly in the text.

Reviewer #2:

Motafavi et al. have updated their manuscript based on reviewer's feedback and answered all the questions and comments posed during the review process of the first submission.

In my opinion their rebuttal and responses are satisfactory and their new and improved manuscript reflect their responses to reviewers. The author's maintained the focus of their manuscript in demonstrating that within ancestry there are a number of possible confounders and study design considerations that impact the prediction accuracy of PGS and put in question its immediate implementation in the clinic as some propose. In addition, and without going overboard expanding hugely the manuscript to explore all possible avenues to explain these effects, their perform a number of analyses that reject the simple idea than environment variance among strata is solely responsible for these effects, but in fact more complex phenomena are at play, including indirect effects, assortative mating, etc. These studies would be the starting point for future studies by the authors and others in the field. I thank the authors to indulge us by adding several interesting analyses suggested by reviewers, such as the inclusion of results by LDpred, a method gaining traction, and showing that as more markers are included in the PGS portability may be more difficult. The comprehensiveness of the supplementary material and clarity of explanations are superb.

After reading the new material in its entirety (apologies that took some time for me to go over this again), I find it a significant contribution to the field, and I do not have any other significant comments to offer recommending its acceptance for publication.

Reviewer #3:

I am satisfied with the revisions that the authors have made and have no further comments to make on the manuscript. Nice work!

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Variable prediction accuracy of polygenic scores within an ancestry group" for consideration by eLife. Your article has been discussed by Ruth Loos, the Reviewing Editor, and Mark McCarthy as the Senior Editor.

While you have been very responsive to the reviewers comments and concerns, we remain concerned that some of the presentation of findings remains counter-intuitive and could lead to mistaken inference. We would like you to consider one final set of revise your paper to include the following:

1) Include strata-combined analyses; i.e. a "full" analysis that combines the stratum-specific sample sizes into one large population. The current study shows that the stratum-specific PRSs perform better than strata-combined PRS, but only if the strata-combined (e.g. men+women) PRS is based on GWAS of the same size as the individual strata (e.g. men, women).

In the very first version of the paper, it was clear that the strata-combined PRS (based on combined stratum-specific data) performs much better than any of the stratum-specific PRS: it seems that the larger sample size overcomes any advantage of stratum-specific analyses (in these examples at least). In response to the reviewers' comments, the authors "reduced" the sample size of the strata-combined analyses to the size of that of the individual strata. However, reducing a strata-combined analyses to the same sample size as the stratum-specific sample sizes is not an intuitive comparison (i.e. a combined analyses indicated that samples are merged into a bigger sample), as stratum-specific implies that these are a subset of the strata-combined. The current version does not address this issue: the labeling of the (sub)groups has been changed, but that has the potential to mislead the reader to infer that stratum-specific analyses will provide the best prediction, whereas a strong predictor is also sample size.

2) Discuss the role of sample size in prediction in the Discussion section;

i.e. put the impact of stratum-specificity in prediction in comparison to the impact of sample size in the (this relates to the comment above). It is important that readers understand that both contribute to prediction, and that possibly sample size is even more important than stratum-specificity. It would be good if the authors can speculate on any circumstances in which the strata-combined analysis would not provide better overall prediction than the stratum-specific subsets.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Variable prediction accuracy of polygenic scores within an ancestry group" for further consideration by eLife. Your revised article has been evaluated by Mark McCarthy (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before we move to final acceptance. These relate to the discussion about the trade-off between sample size and stratum-specific effects on PRS performance that have been the subject of the recent revision requests. Thank you for adding additional information and figures that address this issue. However, as per the last round of revision requests, we do not feel that this question has been adequately addressed in the Discussion, and that some explicit text on this matter forms an essential part of the paper. As you will have seen from the to and fro over the revisions, this is an issue that has exercised several of the editors and reviewers, and I can’t imagine that it will be any less important to the readers of the paper. Put simply, the question is this: based on the data you have generated, are there any real world situations where researchers would be better off splitting a data set into its component strata (eg by gender) and proceeding on the basis of stratum specific risk scores, rather than using the whole data set? The data in the additional figure, suggest not (at least in the models and situations you tested), which is why this is important to place into context.
