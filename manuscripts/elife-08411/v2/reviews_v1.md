# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, University of California, Davis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08411.020](https://doi.org/10.7554/eLife.08411.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Multiple abiotic stimuli interact to regulate rice gene expression under field conditions" for peer review at eLife. Your submission has been favorably evaluated by Detlef Weigel (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors (Daniel J Kliebenstein).

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This work begins a new effort to combine modern genomics methodologies with new computational approaches to look at how organisms exist within the environment. This includes an effort to incorporate all of the fluctuations in this environment in an attempt to better parse the transcriptomic response of the organism to this highly changing system.

Overall, this manuscript is highly interesting and begins to extend the genomics effort into more real world settings.

Essential revisions:

There were two fundamental concerns:

1) The first was that it was felt that the new computational approaches should be tested against another independent data set. Specifically it is suggested that the authors create models with their data on the parameter shared with Nagano et al., since the claim is that they have a new pipeline for data analysis/model building. Then, they should test these models with the data from Nagano et al. to demonstrate the added value.

2) Secondly, the writing could use further improvement to help convey to both the biologists and the computational scientists what the inherent novelty of this study is to both groups. Alternatively, it might be suggested to focus solely on one group and provide them with insights that pertain to that group.

Reviewer #1:

My major concern was that it was difficult to parse out what was or was not truly novel in the results and analysis. I understand that these articles are splitting a divide between the computational and the biological communities each with their own and often contrasting expertise. As such, I would suggest an editorial reworking to make the central messages to be as simple and direct as possible.

Reviewer #2:

The main goal of this study is to determine the effects on multiple environmental factors/components on gene expression in natural field conditions for rice. The claim is that computational approach taken after the gathering and assembling the transcriptome profiles (based on RNA-seq) for three rice landraces with two different systems of cultivation (two biological replicates per field type – rainfed and irrigated) in two phases of cultivation (dry and wet), allows establishing conclusions about interacting abiotic stimuli in field environments. The data set consists of expression levels for ~22,300 genes (after preprocessing, to remove invariable transcript profiles and transcripts not detected in majority of samples). In addition, the authors attempted to test the validity/robustness of the proposed approaches on an independent data set.

In the following, I will only focus on detailed review of the shortcoming of the statistical modeling strategy proposed and employed in this study. The workflow is summarized as follows: (1) conduct clustering of transcript profiles, (2) pre-select environmental parameters, (3) build models with all combinations of one and two of the preselected parameters on different partitions of the data from each cluster (e.g., type of field, season, and combinations thereof); here, cluster means were used as responses and (transformations of) environmental factors were treated as predictors, (4) select models based on Bayesian information criterion (BIC) taking into account model complexity, (5) combine selected models, and (6) inspect the congruence of models (with respect to their coefficients) in different partitions to draw conclusions about effects of climatic fluctuations. In addition, enrichment analysis for different functions in the determined clusters was used to provide biological interpretation.

There are numerous technical issues and difficulties with the chosen strategy, some of which could be remedied, and other which are to be deeply questioned. These are present in every step of the workflow, which led me to question the interpretation and conclusions drawn.

For instance, in step (1), no validation for selection of the number of clusters is provided, nor it is assessed how this may affect the results; the authors could use various cluster quality indices to back up their claims; at this point, it is also not clear which distance measure was used in the PAM clustering approach. It is also advisable that the same centering and scaling strategy is used from the beginning of the workflow, so that consistent results are expected.

In step (2), the set of parameters used was first pruned, by arbitrarily removing highly correlated parameters; there are many ways in which this could be done – was the parameter with largest number of high correlations removed first, or was another strategy used? How would this affect the final results obtained and the subsequent biological interpretations? Most critically, the authors only state that the hdi package in R was used, without indicating if they used it with the default setting (lasso) for the variable/parameter selection. At this stage, I do not know if the parameters were selected based on p-values (from cross-validation), since lasso has multiple solutions, which again would affect the preselected parameters! Moreover, centering and scaling was here done on the entire data set, which will certainly affect the findings should this be done differently (e.g., on a subset of the same data, as the authors do later on).

The same lack of robustness checks is present in step (3), where the pre-selection was repeated for step 2, simply because some of the selected models failed the MSE test (< 0.15).

In step (4) it is advisable to determine MSE from cross-validation, and to only use BIC. I do not understand why the combination of MSE and BIC should be used for the selection.

Finally, the combination of models from step (5) is nowhere detailed; are they only inspected for congruence of coefficients or are they summed to make predictions for the additive effects of two environmental stimuli?

In the enrichment analysis, why were the annotations found across the three annotation resources not combined in a weighted fashion, so that GO terms more often encountered are given a higher more weight? The simple combination employed may distort the findings, particularly for the under-representation of classes (if this was tested at all).

Finally, it would have been interesting to see how the models performed in the case of the data from Nagano et al.; rather than building models on the independent data (any strategy could have been used to this end, not only the heuristic suggested by the authors), the transferability of the models should have been assessed and commented on. This is in fact the most challenging part and would shed light on bridging the greenhouse-field gap.

At this stage, I also wonder why the profiles from different genes involved in particular process were not used to derive the models (this would have avoided the enrichment analysis as well as the clustering and might have made it for a more concrete story).

My conclusion is that the authors used lasso (without ever having stated it and in combination with questionable strategies to remove some of the parameters) followed by classical regression techniques to arrive at the conclusion that correlated responses (whatever they may represent) result in similar models – this is an expected finding and it does not address the main aim of the study. Should an existing variable selection method been used as the only strategy or if latent variables were used on their own with simple regression techniques the authors would have had a streamlined and feasible way to assess the uniqueness, quality, and robustness of the findings, which now is almost impossible to objectively assess.

Reviewer #3:

Plessis et al. is a field genomics paper in rice that examines the relationship between environmental variables across cultivars of rice across 2 seasons (one cultivar is represented in each season). The main goal of the paper is to develop a method to find environmental variables that are highly correlated with gene expression. The authors were careful in how the tissue for RNA-seq was collected so as to minimize confounding effects of time between samples and the circadian clock. Additionally, most of the code used to do the analysis was provided which made detailed thought about the method easier. The authors even used previously published rice data to apply their method to. In general, the paper would be of general interest to the readers of eLife.

I have three major criticisms of the paper in its current form:

1) This is a large dataset with many axes of variation with one of the main conclusions being "additive and interactive effects of distinct environmental conditions on gene expression are widespread". While simplicity is nice for interpretation ("In our effort to produce simple models, we limited the number of parameters per linear equation to two"), finding the best two parameters is an arbitrary cutoff. This needs to be justified statistically by either simulations or references. Furthermore, there is discussion of interactions when these simple models do not account for interactions between variables. It is unclear from the analysis and text how interactions are defined and thus interpreted.

2) The number of PAM clusters that were chosen is arbitrary and could influence the interpretation. There is no code provided for the PAM cluster analysis. Additionally, this is a concern because while the original data 240 number of samples were used in PAM clustering with 50 clusters, the revisited Nagano et al. 2012 data had only 52 RNA samples (that were averages across replicates) but 50 clusters was chosen for this data set as well. The risk here is over-fitting the Nagano data. In the same R package that was used to generate the clusters ("cluster"), there are functions (see clusGAP) to calculate the GAP statistic to determine the appropriate number of clusters given the dataset (Tibshirani et al. 2001).

3) In addition to the technical concerns above, as written there is not enough of a comparison between this modeling approach and the one of Nagano et al. 2012 to show what this new approach has to add with respect to predicting gene expression patterns in the field. I think that the paper could benefit greatly from showing how the model selected from simple to complex would compare to using a full model including interactions with all the terms and gradually dropping terms out to compare models like in the Nagano et al. 2012 paper (although Nagano did not deal with interactions). For example, model selection on: lm(gene expression ~ genotype*season*timepoint*treatment). Building on this, I also think there is a missed opportunity here to do some mixed effects modeling (see lme4 R package) that could take into account the correlation of gene expression within and between all the treatment, genotype time of year combinations.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Multiple abiotic stimuli are integrated in the regulation of rice gene expression under field conditions" for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior editor), a Reviewing editor, and two reviewers (Reviewer #2 and Reviewer #3). The manuscript has been improved but there are a few remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers felt that the manuscript nicely shows that even though climate and local field environment have large effects on gene expression, their effects can be captured with relatively simple models. While there are not yet sufficient data to be predictive for climates or field environments that have not been evaluated yet, the finding suggests that a relatively limited amount of such data sets will enable predictive modeling. This should be emphasized in the Abstract, Introduction and Discussion.

Both reviewers also identified a few technical details that need more clarification before final acceptance. All reviewers and editors for this manuscript felt that there still needs to be significantly more effort to reach the biological reader and convey the novel insights. You state at the end of the Abstract: "We show that new insight can be gained from studying the effects of co-occurring abiotic stimuli in complex dynamic environments." Please state more clearly what these are. All efforts to clarify these insights for both a biological and quantitative readership will greatly improve the future impact of this manuscript on the field.

More detailed requests for clarification are found below.

Reviewer #2:

The authors have carefully considered and addressed the comments raised by the reviewers with respect to the selection of number of clusters (already a non-trivial task, given the number of different measures they considered), number of piecewise models (per BIC only), and averaging of profiles. However, the issue with the model simplification by pruning correlated parameters seems to differ between the response and the main text. More specifically, it is not clear how the decision in paragraph two, subheading “Modeling the effect of climatic factors on transcriptomic variation in different field environments” was implemented, as this can be carried out in many ways. This statement does not correspond to the response provided in your letter, whereby the correlation is set to 0.98 and the parameters were averaged (this strategy of averaging provides a deterministic and reproducible outcome).

In paragraph four, subheading “Modeling the effect of climatic factors on transcriptomic variation in different field environments”, it should be included that the BIC is calculated on the joint piecewise models; I suppose the number of parameters corresponds to the number of predictors summed over all models, or does it correspond to the number of unique predictors over all models? This will have effect on the final findings.

The reciprocal analysis of the partial Nagano data (PND) appears to have pulled out the environmental effects predictive for the transcriptomic changes, and I find that it has added some ideas about the difficulty of the problem of model generalizability.

I would suggest that the claim about "designing model selection approach" is toned done, as the authors themselves state in the response letter that "we do not claim to provide any notable advances in this paper for the computational community". While this may be an article aimed for the genomics-enabled biologist, it will be read by computational biologists interested in the large data resource provided.

Finally, while the authors provided a pipeline based on well-established methods, the interested reader may want to know what is the added value with respect to now classical approaches (e.g., mixed effect models), as one of the other reviewers already suggested.

Rephrasing of some key sentences may be needed, to fully match what was stated in the main text and response letter:

1) The statement in the Abstract "we show that new insights can be gained" should indicate what these insights precisely are.

2) The impact statement should be clarified – one can determine a model for any set of variables; however, the pressing problem is to show that the model explains a major part of the variance and can be used for predictive purposed. Therefore, it also needs rephrasing.

3) The statement of the major findings – "Our method allowed for the detection of additive effects of several environmental factors and differences in gene expression patterns between fields, genotypes or seasons" – is not strong enough, since any data analysis method for differential analysis does essentially the same.

Reviewer #3:

1) In re-reviewing this paper the authors have done a great deal to clarify the modeling approach and have provided many details that were requested. I think that they have made great improvements in the technical aspects of this paper. However, now that the modeling details are clearer the manuscript could be vastly improved for readability for a biological audience (as a stated goal in response to reviewer 1's comment) if the biological question was clearly outlined in the Introduction and followed through the Methods, Results and Discussion.

In the Abstract: "We show that new insight can be gained from studying the effects of co-occuring abiotic stimuli in complex dynamic environments."

Now that the technical aspects of the methods are clearer I am struggling to see what new biological insight is gained from this paper. My main criticism of this paper as a whole in this new version is that it reads as a new way to do exploratory data analysis in a large-scale field transcriptomics experiment, but is not framed to ask a direct biological question with the data/analysis.

In my last review I stated: "as written there is not enough of a comparison between this modeling approach and the one of Nagano et al. 2012 to show what this new approach has to add with respect to predicting gene expression patterns in the field." I followed this with some suggestions as ways to approach this using a mixed model approach that could be applied to genes or gene clusters of interest. The authors have done extra work to apply their method to the Nagano et al. 2012 paper, but I still do not see what new biological insight is gained from the cluster method over gene-wise predictions. If the truly novel aspect of this dataset (compared to Nagano et al. 2012) is the drought/non-drought comparison then could the paper focus much more on this comparison?

2) Interactions implied in Introduction and Conclusion, but not tested in models:

Introduction: “In addition to the dynamic nature of field conditions, the interaction between multiple stimuli is another major cause of discrepancies in plant responses/phenotypes between laboratory and field conditions.”

Conclusion: "By working in natural, complex conditions in the field, we can examine interactions between the effects of factors that vary at distinct time-scales, like temperature and water availability."

In the Authors’ response: "We agree that the use of the term "interaction" in the context of linear models can be confusing. We have therefore removed any mention of interactions in the interpretation and discussion of our modeling results to make our meaning clearer."

Although the authors disagreed with me about the including models with interaction terms for the entire dataset, I still think it would be a good approach to make distinct comparisons between genes/gene clusters and how they respond to the drought treatment.

For example, in the subsection “The agricultural field environment strongly affects transcriptional responses to climatic fluctuations”, the authors state: "This result suggests that, in our experiment, a group of abiotic stress response genes responded to a greater extent to high light/heat stress than drought stress, while another group of abiotic stress response was much more sensitive to the effect of drought." Why not subset the data based on this observation and test these comparisons directly with a follow up model that includes an interaction term?

3) Do these gene expression clusters mean anything for the plant as far as other phenotypes are concerned? There is a missed opportunity here to expand what is found in the clusters into a story about how the environment influences gene expression and how that gene expression might influence plant growth/development. The Discussion starts to get at this, but the message is lost in the details about what a few genes from each cluster mean. The clustering/model selection approach is a great way to reduce this complex dataset to fewer significant parameters but as this manuscript is written does not help in biological interpretation of the clusters. This is also where a clear biological goal of the modeling/method/experimental design is necessary and could improve this manuscript.
