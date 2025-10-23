# Peer review - Round 1

Editors:
- Catherine Hartley, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64983.sa1](https://doi.org/10.7554/eLife.64983.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We believe that this examination of the neural and cognitive processes through which social controllability influences decision-making will be of interest to cognitive neuroscientists interested in the computational mechanisms involved in planning and social decision-making. The additional analyses and thorough revisions made to the manuscript have substantially strengthened the paper, and the conclusions and interpretations presented here are well supported by the data.

Decision letter after peer review:

Thank you for submitting your article "Humans Use Forward Thinking to Exploit Social Controllability" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Catherine Hartley as the Reviewing Editor and Reviewer #1, and Christian Büchel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Romain Ligneul (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this manuscript, Na and colleagues the examine the influence of perceived controllability on choice patterns in an ultimatum game task. In a task variant introducing both controllable and uncontrollable conditions, they find that endowing participants with controllability increases rejection rates in a way which enables social transaction to converge towards fairer offers. In order to clarify the cognitive underpinnings of this finding, the authors fit computational models that varied the degree to which the anticipation of future offers – controllable or not – could influence the decisions relative to current offers. Under the best fitting model, social controllability (the influence of current decision on future offers) is used to adjust the expected value of their decision to accept or reject offers, suggesting that subjects used a controllability-dependent forward planning process. The fMRI results suggest that the cognitive operations underlying this forward planning process might depend in part on computations within the ventromedial prefrontal cortex, in which BOLD activation correlated with total (current and future) values computed under such a model.

In most studies using the UG game studies, researchers look at how accept/reject behavior changes conditioned on the offer size, and the UG games are typically one-shot. Na et al., extend this work by looking at how the behavior of receivers could, in turn, affect future offers by the proposer, in an interactive manner. A further strength is that the authors were able to replicate the behavioral and modeling findings in a separate large online sample, and all data and analyses are made available online so that others could make use of them. Overall, the analyses are carefully performed and largely in support of the key conclusions. However, the reviewers felt that some aspects of the analysis could be further developed, refined, or clarified.

Revisions:

1) The background and rationale for the current study could be laid out more clearly in the introduction. The authors should explain what controllability means and why it is important. The introduction would also benefit from inclusion of some important behavioral and neural findings in the literature regarding controllability in non-social contexts. The discussion of "model-based planning" may not be so relevant here. In the 2-step task (Daw et al., 2011), participants need to learn a task transition structure and use this learned knowledge to plan future actions. But in the current task, there is no such abstract structure to learn. A discussion of the role of simulating future events/outcomes (e.g., counterfactual simulation) may be more appropriate than a focus on model-based planning. The authors may also want to include key studies and findings on strategic decision-making and theory of mind. The neural hypotheses should also be introduced, or if the authors didn't have a priori hypotheses, it could be explicitly stated that it is an exploratory study if indeed the case. If the vmPFC is indeed the area of interest a priori, then the authors should provide justification for this hypothesis.

2) It would be helpful to clearly assess and discuss the commonalities and differences in results between the social and non-social versions of the task, and their implications for interpreting the findings. It would be beneficial to see the computational model comparison applied to the non-social control experiment, as well (. Critically, is the 2-step model still favored.

3) The analysis of overall rejection rates (Figure 2b1) is slightly puzzling with respect to the results reported Figure 2a1 and 2b2. Indeed, Figure 2a1 shows that participants encountered a much higher proportion of middle and high offers in the controllable condition (due to their control over offers) and Figure 2b2 shows a very significant increase in rejection rates for these two types of offers but only a modest decrease for low offers. In addition, the offers in the uncontrollable condition seem to vary in a systematic fashion across time and to be very rarely below 3$. In this context, I wonder how mean rejection rates can possibly be equal across controllability conditions. Still regarding rejection rates, it also seems that the uncontrollable condition was associated with a much greater inter-individual variability in rejection rates, hence suggesting that controllability reduced variability in the type of strategy used to solve the task. The authors should (i) clarify how offers of the uncontrollable conditions were generated, (ii) discuss and perhaps try to explain (and relate to other findings) the different inter-individual variability in rejection rates across conditions.

4) In the behavioral analyses, what is the rationale for grouping the offer sizes into three bins rather than using the exact levels of offer sizes? Do the key results hold if exact values are used?

5) It would be helpful to include an analysis of response times. Indeed, one would expect forward planning to be associated with lengthened decision times and correspondingly, for the δ parameter (or strategizing depth, or controllable condition) to be associated with longer decision times (e.g. Keramati et al., Plos Comp. Biol., 2011). Furthermore, it was recently shown that perceived task controllability increases decision times, even in the absence of forward value computations (Ligneul et al., Biorxiv). It is also good practice to include decision times as a control parametric regressor when analyzing brain activities related to a variable potentially correlated with them. Furthermore, one could expect longer reaction times for more conflicting decisions (i.e. closer valuations of reject/accept offers).

6) The authors refer to the δ parameter "modeled controllability", however the model doesn't provide any account of the process of estimating controllability from observed outcomes (see Gershman and Dorfman 2019, Nature Communications or Ligneul et al., 2020, Biorxiv for examples of such models), but only reflects the impact of controllability on value computations, or the monetary amount of "expected influence" in each condition. An augmented model might include a computation of controllability, with the δ parameter controlling the extent to which estimated controllability promotes forward planning. Even if the authors don't fit such a model, they should explicitly acknowledge that their algorithm does not implement any form of controllability estimation, and might consider calling δ a "forward planning parameter". In addition, it is unclear why the authors chose to constrain the δ parameter to fluctuate between -2 and 2$ (rather than between 0 and 2$, in line with their experimental design, or with even broader bounds) and what a negative δ would imply. Also, would it make sense to exclude participants with a negative δ in addition to those with a δ greater than 2? Do all results hold under these exclusions?

7) While the authors performed a parameter recovery analysis, they did not report cross-parameter correlations, which are important for interpreting the best-fitting parameters in each condition. Furthermore, it is good practice to perform model recovery analyses on top of parameter recovery analyses (Wilson and Collins, 2019, eLife; Palminteri et al., 2017, TiCS) in order to make sure that the task can actually distinguish the models included in the model comparison. As a result, the conclusions based on model comparison and parameters values (that is, a significant part of the empirical results) are uncertain. The cross-correlation between parameters and model recovery analysis should be reported as a confusion matrix.

8) The parameters of the adaptive social norm model exhibit fairly poor recoverability, particularly in the controllable condition. The motivation for using this model is that it provided the best fit to subjects data in a prior uncontrollable ultimatum game task, but perhaps such adaptive judgment is not capturing choice behavior well here. It would be helpful to see a comparison of this model with one that has a static parameter capturing each individual's subjective inequity norm.

9) The authors stated that future actions are deterministic (line 576) contingent on the utility following the immediate reward. If so, is Figure 3a still valid? If all future actions are deterministic, there should be only one path from the current to the future, rather than a tree-like trajectory.

10) The MF model, and the rationale for its inclusion in the set of models compared, needs to be explained more clearly. The MF model appears to include no intercept to define a base probability of accepting versus rejecting offers, which makes it hard to compare with the other models in which the initial norm parameter may mimic such an intercept.

11) The fact that the vmPFC encoded total future + current value (2-step) and not current value (0-step) suggests that it might be specifically involved in computing future values but the authors do not report directly the relationship between its activity and future values. How correlated are the values from the 0-step model and the 2-step model? And more importantly, if vmPFC is associated with TOTAL value but not the current value, should that mean the vmPFC is associated with the future value only? It might make more sense to decompose the current value and future value both from the winning 2-step model, and construct them into the same GLM without orthogonalization.

12) The vmPFC result contrast averages across the controllable and uncontrollable conditions (line 629). Why did the authors do so? Wouldn't it be better to see whether the "total value" is represented differently between the two conditions.

13) The analysis of the relation between the vmPFC β weights and the difference between self-reported controllability beliefs and model-derived controllability estimates (Figure 5 d and e) is not adequately previewed. The hypothesis for why vmPFC activity might track this metric is unclear. Moreover, the relation between the two in the uncontrollable condition is somewhat weak. The authors should report the relation between vmPFC β weights and each component of the difference score (modeled and self-report controllability), and clearly motivating their intuition for why vmPFC activation might be related to that metric. If the authors feel strongly that this analysis is important to include, it would be meaningful to see whether the brain data could help explain behavioral data. For example, a simple GLM could serve this purpose: mean_offer ~ β(vmPFC) + self-report_controllability + model_controllabilty. Note that the authors need to state the exploratory nature if they decide to run this type of analysis.

14) The authors might also report the neural correlates of the internal norm and the norm prediction error (line 544). If the participants indeed acquired the social controllability through learning, they might form different internal norms in the two conditions, hence the norm prediction error might also differ.

15) Specific aspects of the experimental design may have influenced the observed results in ways that were not controlled. For example, it is not only the magnitude and controllability of outcomes that differed between the controllable and uncontrollable conditions, but also the uncertainty. It is possible that the less variable offers encountered in the controllable condition may have driven some of the results. The authors should acknowledge that the possible role of autocorrelation and uncertainty on behavioral and modeling results.

16) Moreover, asking participants to repeatedly rate their perception of controllability almost certainly influenced and exacerbated the impact of this factor on choices. It would have been very useful to perform a complementary online study excluding these ratings to ensure that controllability-dependent effects are still evident in such a case.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Humans Use Forward Thinking to Exploit Social Controllability" for further consideration by eLife. Your revised article has been evaluated by Christian Büchel (Senior Editor), Catherine Hartley (Reviewing Editor), and the two original reviewers.

As you will read, the reviewers are in agreement that your manuscript has been substantially strengthened by these revisions, but there are some remaining issues that need to be addressed.

A primary concern is that the manuscript does not provide sufficiently strong support for the claim that the vmPFC supports forward planning, particularly in light of the new neuroimaging analyses performed as part of this revision. Reviewer 3 has a concrete suggestion for how this claim might be strengthened with a model comparison analysis. If further evidence for the claim is not found/provided, it should be tempered. Reviewer 2 also questions whether it is useful and sensible to retain the MF model in the set of compared models, and both reviewers note a few areas where clarification, greater methodological detail, or further interpretation are warranted.

Please carefully consider each of the reviewers suggestions as you revise your manuscript.

Reviewer #2:

The authors have revised their manuscript considerably and addressed a number of concerns raised in the initial review, with their additional analyses and detailed clarification. I particularly appreciate that the authors took the courage to dive into the direct comparison of findings between the social and non-social groups, which provided new insights. Furthermore, the revised Introduction is more thought-provoking with relevant literature included. Now the conclusions are better supported as it stands, and these findings are certainly going to be exciting additions to the literature of social decision neuroscience.

Here I have a few additional points, more for clarification.

(1) In response to comment #2, the authors might unpack the significant interaction result, to explicitly show "that the non-social context reduced the impact of nPE on emotional feelings." Also in the same LME model, I am curious about the significant "Controllable × social task (***)" interaction (β = -5.06). Does this mean, being in the Controllable + Social group, the emotion rating is lower? How would the authors interpret this finding?

(2) In response to comment #5 regarding response time with the additional LME analyses, I wonder which distribution function was used? We know that RT data is commonly positively skewed, so a log-normal or a shifted log-normal should be more accurate.

(3) I retain my initial comment regarding the inclusion of the MF model. The task is deterministic – participants get what appears if they accept and 0 if reject. In fact, the model is making a completely different prediction: according to the Q-value update, if the participant chose an "accept" and then indeed received a reward, then they should repeat "accept". But in the current task design, such a "positive feedback" would make the participants feel they are perhaps too easy to play with, and will be more likely to choose "reject" on the next trial. In essence, the MF model is not even capturing the behavioral pattern of the task, hence it does not seem to be a good baseline model. Rather, the 0-step model is okay enough to be the reference model.

Reviewer #3:

The authors have made very significant efforts to respond to a diversity of concerns and to amend their paper accordingly. The revised version is thus more complete and I believe that the main argument of the paper has been made stronger.

In many cases, the authors have appropriately adjusted their language in order to better align their conclusions with the data (e.g. renaming the δ parameter expected influence parameter) and I think that this paper can constitute an interesting addition to the field.

However, I am still slightly skeptical about the reach of neuroimaging results and I believe that some limitations of the paradigm may be more explicitly discussed.

A. Neuroimaging.

The authors have performed valuable additional analyses regarding the norm and norm prediction errors signals which can be of interest for the field. But I believe that our main concerns about vmPFC effects have not been fully addressed. Indeed, the authors still write that the vmPFC constructs "the total values (both current and future) of current actions as humans engaged in forward planning during social exchange". However, when splitting the analysis of current and future values, the encoding of future values was found in the insula whereas the vmPFC only encoded current values. The authors claim that the lack of encoding of total values derived from the 0-step FT model constitutes evidence in favor of forward planning, but it could be that this lack of evidence is driven by a poorer fit of current (rather than total) values by this simpler model. In order to better substantiate their claim about vmPFC's role, the authors may want to perform a model comparison at the neural level by comparing GLMs (using for example the MACS toolbox) including current value only, current value and future value, future value only or total value. Alternatively, they could analyze the first-level residuals produced by GLMs including alternatively current value, future value and total value (all based on FT-2). If their interpretation is correct, GLMs equipped with a parametric regressor for total value should be associated with smaller residuals in the vmPFC.

Regarding the behavior-belief disconnection analysis, I think that it would be more sensical to study the ratio rather than the difference between behavior and subjective reports, since these two measures are qualitatively different. Finally, it might be worth providing the reader with a brief discussion of the other neural substrates uncovered by the most recent analyses (dmPFC, insula, striatum, etc.).

B. Behavioral paradigm.

I believe that the authors should provide a few more details in the methods and acknowledge a few limitations in their discussion.

First, unless I am mistaking the method used to decide on block order (i.e. C or U first) was not reported. Was the "illusion of control" in the uncontrollable condition driven by the subset of participants who passed the controllable block first? If this is the case, then it might add some plausibility to the interpretation of subjective controllability ratings in the uncontrollable condition as an "illusion of control" (persistence of a control prior). In other words, I think that the authors should refrain from interpreting the raw value of these ratings as an illusion of control (perhaps not all participants understood the meaning of the rating, perhaps they were too lazy to move the cursor until 0, etc.).

While it does not necessarily implies an illusion of control, the fact that participants still relied on on forward planning in the uncontrollable condition (as indexed by the expected value parameter) is presumably what prevented authors to really isolate the neural substrates of strategic controllability-dependent forward planning, and it might thus be mentioned as a limitation of the paradigm.

I believe that it is also important to mention explicitly the fact that a third and a quarter of the data was excluded from the analyses of behavioral and fMRI data (i.e. first and last five trials of each block) respectively and the rationale for this exclusion may be discussed.

The authors wrote that "a task that carefully controls for uncertainty and autocorrelation confounds would help better understanding the accumulative effects of social controllability", which is a good start, but it would be in my opinion important to explicitly acknowledge that change in controllability were confounded with change in uncertainty about upcoming offers.

I would be curious to hear the authors' insight about why participants in the online study (and to some extent in the lab) accepted more often the low offers in the controllable condition. It seems somehow counterintuitive and could mean that participant behaved in a more "automatic" and perseverative way in the controllable condition.

Related to this last point, is it possible that the δ parameter (or expected influence) simply captures a perseverative tendency in rejection/acceptance of offers? This might explain the disconnection between behavior and belief, as well as the positive value of this parameter in the uncontrollable condition, correlated to that of the controllable one. That perseveration increases in the controllable condition would be logical (since that condition allows participants to reach their goal by doing so) and it would therefore still be of interest in the context of this social controllability study. Perhaps the authors could exclude this possibility by running adding a perseveration mechanism to their model, as it is often done in the RL literature?
