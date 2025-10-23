# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08445.027](https://doi.org/10.7554/eLife.08445.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Quantitative perturbation-based analysis of gene expression predicts enhancer activity in early Drosophila embryo" for peer review at eLife. Your submission has been favorably evaluated by Naama Barkai (Senior editor), a Reviewing editor, and three reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

Sayal et al. report extensive experimental and computational studies of rho-expression in the dorsal-ventral patterning gene regulatory network of Drosophila. The aim is to understand how rho-expression depends on binding sites of transcription factors (Twist, Snail, Dorsal) in the rho enhancer. To this end, constructs with individual transcription factor binding sites removed are analyzed and the resulting patterns of rho expression fitted to different models of transcription factor binding, cooperation, and activity.

Essential revisions:

1) The reviewers and the BRE are concerned about the multi-model analysis. They all agree that this analysis is unclear and non-standard. The reviewers were also concerned about the procedure over-fitting to the data. Select comments attached below. Clarification and possibly rethinking the mode of analysis is needed for the revision. One of the main claims of the paper is the ability to estimate biophysical parameters, this claim has to be convincingly demonstrated.

A few comments from the reviewers on this issue:

"The concept of ensemble of models is not new and is the subject both of Bayesian statistics (which is essentially about learning how much we can trust each possible model) and non-Bayesian formulations (e.g., mixture-of-experts models). I suspect that employing one of these methodologies would actually lead to a useful predictive rule which might apply on the non-rho enhancers. Right now the discussion that points to the models that support the observations is weak."

"Based on their cross-validation results, the individual models are overfit. They claim that fitting a suite of models addresses this because they can identify trends amongst models. However, the set of models is highly related; they vary only in the particular pair-wise interactions that are allowed and the way that the distance-dependence is encoded. I believe it's more appropriate to address overfitting using sensitivity analysis, which they did. Sensitivity analysis should reveal which subset of parameters are well constrained by the data and which are not. But their conclusion is that cooperativity and quenching parameters show extensive mutual dependence, leaving it unclear precisely which parameters they can interpret across models."

"The authors find extensive "parameter compensation", meaning that the data does not constrain the model parameters, implying generally a good model fit but poor predictive performance (unless the instances where prediction is sought are similar to examples already seen during model training). Given the large number of parameters, one would expect a good fit (and also a good cross-validation on examples similar to training data) even if the overlap between models and properties of the enhancer, or models among themselves is poor."

"Possibly the question how impressive the predictions are can be settled on the basis of the present data. The overlap between predicted and observed expression levels can be plotted on a scatter plot against distance of the enhancer configuration to the most similar configuration in the training set. Results would differ somewhat depending on what distance measure is used, but I expect one can obtain insight into how serious the overfitting is."

2) With regards to the experimental data, rigorous measurement of expression levels by typical in situ is not trivial. The analysis here measured differences in expression level by keeping the acquisition settings on the microscope constant and normalizing maximum expression to a WT stain imaged on the same day. However, there can also be significant error from batch to batch variation in probes and stains, which are not accounted for here. This issue should be addressed by examining batch to batch variability and demonstrating that it's not an issue for their system, or by simulating data with more uncertainty in the levels of expression and see if this qualitatively effects their results.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Quantitative perturbation-based analysis of gene expression predicts enhancer activity in early Drosophila embryo" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior editor), a Reviewing editor, and three reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. This includes in particular the minor comments of reviewer #1. In addition, in response to reviewer #2 comment, please be more explicit about the main result that was learnt from your analysis (beside the general modeling success)

Reviewer #1:

The authors have diligently responded to the previous comments and the manuscript is more clear as a result. Overall, I find the main conclusions – that activators cooperate in a distance independent way while repressors cooperate less and have distance dependent function relative to activators – to be quite interesting. The modeling strategy is somewhat unusual, and while it's presented fairly clearly in the text, I don't find the figures always give great insight. However, for most aspects, I think readers can assess what they did and draw their own conclusions about the validity of the modeling approach and whether it provided useful insights. I do not see any technical errors that would undermine their main conclusions, and I think they are appropriately circumspect. I can therefore support publication.

Reviewer #1 (Minor Comments):

I still have minor concerns about how their imaging data is being analyzed and incorporated into the model. These are mostly issues of clarification and how to make best use of the dataset that they have in hand.

First, in response to my previous concern about the variation in their imaging data, the authors quantified variability in their control embryos, which were stained in different batches and imaged on different days, and used to calibrate the acquisition settings of their microscope, thus serving as the effective normalization for peak expression for their test constructs. They analyze the variation in this full set, reporting that their mean peak expression was 138+/- 36.8, and that background was 52.4 +/- 23.8. They are thus seeing about 2X expression above background for their WT controls across all stains by this metric. This is a useful number and it's good to include (I would leave out the qualitative description of it's meaning that follows, but that's a personal preference for numbers over verbal description).

However, if increases in background and signal are correlated (for example if you have embryos that are brighter or dimmer overall, which is often the case with fluorescent stains), this might be actually be over-estimating their error. Instead, or in addition, they could include the standard error for the WT images used to calibrate the microscope for each construct in Figure 1, instead of plotting only the average WT trace across all of these data without any error. It's possible that they did not collect sufficient data on the WT constructs during each imaging session, in which case this wouldn't be helpful. An alternative would be to plot the standard error for the average WT trace after normalization.

I'm looking for some clarification on the imaging primarily because many of their constructs decrease or move expression moderately and it's helpful to know whether any of those constructs fall within experimental error. In the methods, it states that they imaged each test construct on a single day, so it's not possible to do the bulk analysis of error described above for each construct. The standard error for each construct shown in Figure 1 is therefore representative of the variation in their dataset. Including the error for WT in Figure 1 would largely address this issue.

I appreciate that they introduced noise into their predictions to try to assess how their error in expression measurement might impact their conclusions. This reveals the sensitivity of the top models, and their likely over-fitting, which confirms the utility of not focusing on a single model, but it is not necessary to include this analysis in this already large paper.

Second, to clarify how the expression measurements feed into their models, the authors could include a more explicit description of the inputs, outputs and scoring scheme for their models in the section "Thermodynamic modeling of rho enhancer perturbation dataset". For example, did they use continuous expression data as their input, or select expression levels at specific points? The latter seems to be the case based on Figure 2C where black dots are specific measurements. How/why were these points selected? The output also appears to be at discrete points based on this Figure, where red lines are predictions and I am assuming that the line is from linking together these discrete points. Finally, the RMSE score they use equally weights errors in regions of high expression and low expression. Some alternative scores have been used in other work to emphasize other features of expression patterns (for example the Sinha group has used the weighted Pattern Generating Potential). It is not necessary to score their models differently, but they should discuss the trade-offs of their particular scoring scheme. And how is the RMSE score calculated? Is it done on the continuous data (red lines in Figure 2 vs. continuous expression measurements), or on the point by point data as above? I could not find this information in the main text or the methods. I suggest that it is included in the main text as a verbal description of their procedures, and any additional information be put in the methods. It also seems possible and potentially useful to include their experimental error in Figure 2, to allow comparison of biological variability against their model performance.

Reviewer #2:

The revised version of Sayal et al. has improved in some ways. Overall I am supportive of this type of work, which involves careful experimental measurements followed by an honest attempt to fit the data to a physically inspired model. The strengths of the paper are the quantitative data, and the attempt to validate the model predictions both by testing the activity of enhancers from other species and by using the model to predict the locations of other enhancers, some of which are already known.

The main weakness of the paper remains the decision to center the analysis around a collection of 120 related models rather than attempting to find the best model, or a small number of competing models. This gives the analysis a very unsystematic feel; different models are highlighted and put forward in different parts of the paper. The result is that the claims of the paper are vague (that experiments and models can help reveal regulatory principles) rather than something concrete about the grammar of this system. There is no clear statement of what the authors have learned besides the idea that modeling is a good thing.

In my opinion the issue of over fitting has been dealt with adequately by the experiments in which the activity of orthologous enhancers are predicted and measured and by the demonstration that there is little correlation between the accuracy of new predictions and the similarity of the tested construct to constructs in the training data.

Reviewer #3:

The additional checks requested in the previous round of review alleviate my concern concerning overfitting. My assessment is that this work goes beyond a resource of detailed experimental data, and the statistical analysis unveils aspects of the underlying biology. Detailed analysis of the data can be done in the future and is beyond the scope of this paper. For this reason I recommend publication in eLife.
