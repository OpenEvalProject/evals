# Peer review - Round 1

Editors:
- Wolfram Schultz, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26424.026](https://doi.org/10.7554/eLife.26424.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dopaminergic, neural and computational contributions to probabilistic reward learning in old age" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sabine Kastner as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The attenuation of probabilistic reward learning in older human participants was accompanied by reduced value signals in prefrontal cortex.

Essential revisions:

As you will see from the reviewers comments, which are backed by similar concerns of the Reviewing Editor, the paper is far too complicated as it stands. I would suggest to seriously reduce unnecessary analyses, and focus and streamline the paper, and its text, on the essentials related to the age of the participants. There is nothing wrong with removing parts of the data and/or analysis if that would lead to a much clearer message (note that the Abstract already is tough to read with too many distinct details). It should also be discussed why there were not the usual reward prediction error signals found in the ventral striatum (this is not necessarily a bad thing, in particular when a stringent analysis has been applied as here, but readers want to know why).

We will need to send the paper back to the reviewers, but given their substantial difficulties with reading and commenting on the complex text, we can do this only once. This one-revision-only is also general policy of the Journal, and we will need to adhere to it given the complexity of the report.

Please reply with a succinct, simple, point-to-point text to the reviewers' comments. And please be aware of a general policy at eLife that we do not permit several rounds of revisions. Thus, we sincerely hope that you will be able to successfully revise your manuscript with the next round.

Reviewer #1:

This study examined the behavioral and neural bases of age differences in probabilistic reward learning, using fMRI and PET. A group of young and older adults performed a simple instrumental reward learning task (two-armed bandit) in an fMRI experiment. On each trial, participants chose between two cues, whose reward probabilities changed in Gaussian random-walk processes. DA D1 binding potential (BP) was also assessed in several brain regions. Young adults made more money and more efficient choices. The authors compared two families of behavioral models, one based on reinforcement learning through reward prediction errors (RPEs), and the other on a Bayesian observer, where reward probability is updated after each outcome. The best model was a Bayesian one, which included reward-probability updating for both the chosen and unchosen options, the variance of the option not chosen on the previous trial, and decision confidence. None of the model parameters differed between the young and older adult groups, but using the model's generated expected values the authors show that young adults made more "adaptive switches" – switches to the option of the higher value. The winning model was used in the analysis of the fMRI data. This analysis revealed stronger representation of the expected value of the chosen option in young compared to older adults in several brain areas. In the vmpfc, this parameter predicted earnings, and accounted for age differences in aging. DA D1 BP in NAcc was correlated with the value parameter in vmpfc, but not in NAcc, and accounted for age differences in that parameter. The authors then searched for RPE signals. They did not settle for a simple correlation with RPE, but rather required separate correlations with expected and obtained reward, with opposite signs. This analysis did not identify RPE signals in NAcc in either young or older adults, but the authors show that a reinforcement-learning model fits the BOLD data there better than the Bayesian model. Finally, the authors also report activation in several areas that are related to decision confidence or to switches.

This is an interesting study, which asks an important question. There is evidence for reduced reinforcement learning in aging, but the neural basis of this reduction is not clear. The paper has many strengths, including the use of computational modeling and model comparison, the combination of fMRI and DA D1 BP within subject, and the careful neural analysis. I have relatively minor comments, which are detailed below.

– In its current form the paper is somewhat difficult to follow. There are many questions and analyses, so the writing should be very clear in order to take the reader through the entire story. Sometimes the authors assume knowledge that a wide audience may not necessarily have. For example, will be helpful if there is a brief description of the task either at the end of the Introduction or the beginning of the Results section. Then perhaps some overview of the main questions and the general analysis strategy. Next, the model descriptions should be clarified – the Materials and methods section provides detailed information, but it will be helpful if the brief description in the Results section is clearer – especially important is the definition of all the parameters in each model. Keeping all the parts of the PET analysis together will also be helpful. Finally, it seems that the main finding is the relationships between vmPFC activity and behavior and between NAcc DA BP and vmPFC activity. In both of these analysis correlation with age disappears when the physiological variable is taken into account. This is very interesting and should be clearly stated.

– It was a bit confusing to me that no parameter of the winning model reflected the age-related difference in behavior (unlike the RW model). It seems that the main point of using computational modeling is to uncover latent variables that affect behavior, but cannot be directly observed, in order to understand the differences in computations. Is it possible that the model fails to capture some latent variable that is of the most interest to this particular study? This is supported by the fact that using the switches, instead of the model parameters, yielded more informative results. The authors should clearly explain the utility of model fitting for their behavioral analysis. In particular, did the vmPFC results depend on the particular formulation of Q from the winning model?

– The lack of RPE encoding in NAcc in young adults is presented as an incidental finding, but it is of importance, independently from the aging research question. The authors are right that this may be due to their stringent criterion, but the fact that there was also no correlation with D1 BP, and that an RW model fit the activity better than the winning Bayesian model, makes me wonder if the Q estimates may be off? Also, is there an age difference if you consider the less stringent single-predictor RPE?

Reviewer #2:

In this article, the authors combine behavioral, fMRI, PET, and computational modeling approaches to understand the mechanisms of probabilistic reward learning, and how this learning changes with age. There are definitely some interesting results here. The relationship between D1 binding potential (BP) in NAcc and the neural correlate of chosen value in vmPFC seems particularly notable. However, several of the neural and computational modeling results are not yet as compelling as they could be. Below the major findings are discussed in turn; in some cases the paper might be best served by cutting certain analyses entirely, but suggestions and comments are provided nonetheless.

1) Probably the most novel and central findings concern predicted value (Q) signals in vmPFC. The correlation between Q and vmPFC activity is reduced in older adults and predicted by D1 BP in NAcc, and D1 BP fully accounts for the effect of age. The predicted value response in vmPFC also predicts performance on the task. This is an interesting set of findings. I'm aware of only one other report showing age effects on vmPFC value correlates (Halfmann et al., 2017, SCAN), but that report focused on individual differences within older adults, and the link to dopaminergic signal shown here provides a plausible mechanism for the effect. These findings could be strengthened in a few ways, however:

1a) A formal mediation analysis would further strengthen the claim that D1 BP accounts for the effects of age on value signals in vmPFC.

1b) These results depend on the parameter estimates in vmPFC extracted from the region showing a main effect of predicted value. It would be of interest to replicate these analyses in an independent ROI – e.g., the ROI from the Bartra et al., 2013 meta-analysis on subjective value. Though the age comparison is orthogonal to the original fMRI analysis, it is hard to know if and how the possible inflation of the parameter estimates might interact with other analyses such as the correlation with D1 BP.

1c) The effect of Q in vmPFC on performance in the task is significant when controlling for age and model fit, but does it hold when not controlling for these factors? I understand the need to control for age given differences in value-related vmPFC activity between the two groups, but the results without the control variables should at least be noted in the text.

1d) Given the high correlation between dopamine binding in different ROIs, theorizing of how D1 binding in the NAcc specifically could mediate vmPFC effects (Discussion section) seems somewhat premature.

1e) In these analyses, a negative correlation with predicted value is also noted in several prefrontal and parietal regions. In several previous studies, these regions have been associated with difficult choices, indexed by the absolute difference between chosen and unchosen value. Before concluding that these regions encode the inverse of chosen value, this alternative explanation would need to be ruled out.

2) Another imaging finding was that NAcc tracked received rewards, rather than reward prediction errors, in both young and old adults. This is an interesting finding and the methods here provide a nice warning about making strong conclusions about correlations with prediction error regressors, without examining responsivity to both components of the prediction error.

2a) One possibility, though, is that the lack of a prediction error signal is reflective poor learning – i.e., subjects' expectancies are not accurate. Have the authors looked at the correlation between the representation of expectancy in NAcc and performance on the task?

2b) It looks like two different versions of Figure 4 were uploaded. Which one is correct needs to be clarified.

3) A final neural finding – which is more exploratory – is increased activity in frontoparietal brain regions on switch trials, which predicts performance in the task.

3a) Here again, the possible alternative that these regions respond to more difficult decisions (indexed, for example, but the difference in absolute value, or by reaction time), rather than switches per se, needs to be explored.

3b) In addition, the authors also show that activity in these regions is negatively related to the number of switches made by the subject, which is in turn, negatively related to performance. Does dlPFC or IPL activity predict performance after including the number of switches in the model? Without showing this, it is quite possible that the number of switches modulates both dlPFC/IPL activity and performance (i.e., the relationship between the brain and performance is driven by a third variable).

3c) While the fact that switch-related neural activity independently predicts performance when controlling for Q in vmPFC suggests that including the switch-related activity improves the predictive power of the model, a formal model comparison is needed to support this conclusion. I would like to see a formal model comparison between the following models for predicting performance: 1) age and Q in vmPFC; 2) age and switch-related activity in switch ROIs; and 3) age, Q in vmPFC, and switch-related activity in switch ROIs.

4) The results are not definitive on whether there are age differences in probabilistic learning and if so what the cause of these differences is.

4a) Performance differences between older and younger adults are only significant with a one-tailed t-test. This is weak evidence at best for any age effects in the task.

4b) None of the parameters in the authors' winning model differed between younger and older adults. The authors suggest that "correlated changes in the parameters may explain the age difference". However, if there were correlated changes, there should still be significant differences in the parameters – in fact, wouldn't you expect to see more significant differences? I suppose the authors could use some kind of multivariate analysis to look for age differences in model parameters, but the overall picture seems more consistent with subtle, if any, age effects.

5) There were several aspects of the computational modeling approach that were potentially problematic.

5a) In the authors' winning Bayesian model, Q values are initialized at 0.5 and the forgetting process relaxes these values back to 0.5. In the reinforcement learning models, Q values are initialized at 0 and the forgetting process relaxes these values back to 0. A fair comparison between the two classes of models would eliminate this structural difference. Though unlikely, it is possible that this aspect, rather than the details of updating, accounts for the difference in model performance between RL and Bayesian models.

5b) In the authors' winning model, switching is more likely when there is less uncertainty about the unchosen value and when there is greater relative confidence about the previous choice. These effects are counter-intuitive, and more evidence is needed for them to be convincing.

In the case of switching when there is less uncertainty, this is the opposite of normative exploration, the notion of an "exploration bonus." Wilson et al., 2014, for example, found evidence for directed exploration. Why do the authors think they see the opposite here?

5c) That previous trial relative confidence predicts switching is also surprising. It is hard to see how this could be a good feature for learning to have under general conditions, which makes me wonder if it is a byproduct of some particular aspect of the current task. For example, this behavior could be adaptive if there is a negative correlation between the values of the two options or a tendency for values to reverse over time. If this result is more of a byproduct of the task than a general phenomenon, then I would worry about making too much of this finding.

5d) In both of these cases, it would be very informative if the authors could identify the features of task performance that these two aspects of the model explain. This would increase confidence in the empirical finding, beyond the simple model comparisons. It might also provide further insight and modeling ideas; perhaps once the nature of switching behavior in this task is better understood the authors will discover that it can be even better explained by adding different, less counter-intuitive, features to the model.

5e) The potential interaction between the uncertainty and confidence effects needs to be examined. It would make sense that uncertainty about the unchosen value and relative confidence are negatively correlated, given that the former is one of the inputs needed to calculate the latter. This would seem to complicate any interpretation of the weights on these parameters when both are in the model. At a minimum, the authors should report the goodness of fit statistics and parameter weights for a model where only the relative confidence term, and not the uncertainty term, is included in the model.

5f) The authors refer to the effect of relative confidence as a "grass is greener" effect, but I do not think this analogy captures the effect accurately at all. For example, I could imagine also referring to an effect in the exact opposite direction (more switching when confidence is lower) as a "grass is greener" effect, so obviously the analogy is doing no work, and perhaps obscuring rather than enlightening.

Reviewer #3:

In this work, De Boer and colleagues examined the effects of age and dopamine (D1 receptor availability measured using PET) on the neural mechanisms underlying probabilistic reward learning (explored using fMRI). They isolated two main processes contributing to choice performance: 1) learned estimates of option values, 2) switching behavioral strategy. The first process was notably expressed in vmPFC activity and declined with age, this decline being related to nucleus accumbens dopamine. The second process was underpinned by a frontoparietal activity and was independent of age and dopamine.

The question is not really novel. In particular the last author (Marc Guitart-Masip) contributed to a Nature Neuroscience paper that already established the dopamine-dependency of age-related decline in reward learning. However, this new study brings further insights that help to refine our understanding of this phenomenon. Besides, the study has several strengths: it gathers a large dataset (60 participants) including behavioral, PET and fMRI data and takes a sophisticated analytical approach using computational modeling. Overall, I think this paper would nicely contribute to unraveling the determinants of reward learning in humans. Unfortunately, the number of different analyses and results sort of obscure the reading and dilute the main findings. My main suggestion would be to streamline the analysis so the results description would have a clearer structure.

In that regard, it would help to remove the Bayesian model, which does not seem to bring much to the main conclusions, unless I missed something. I appreciate the amount of effort that the authors must have invested in this modeling work, but I am not convinced it makes sense to keep this model and related analyses of brain activity. My reasons are 1) there is no principle justifying that participants should switch when confidence in the chosen option is high (I suspect this comes from correlation between parameters), 2) when comparison is fair (models without the confidence add-ons) the BIC of Rescorla-Wagner and Bayesian models are similar (compare third lines in Table 1), 3) unlike the RW model, the Bayesian model does not capture the difference in behavioral performance between young and older people, 4) the variables specific to the Bayesian model have only weak links with brain activity, contrary to the RW model-based predictions, on which main conclusions are built.

Besides, I have some other concerns:

– As far as I understand, a unique random walk was used to generate reward probabilities for all participants. From the plot in Figure 1 it looks like a noisy reversal, which raises the issue of possible age-related deficits in reversal per se, and of the anti-correlation between cues that may induce the belief that outcomes inform on both cues (subject might normalize the two option values). These possibilities should be discussed.

– The difference in vmPFC value signal could artificially come from the difference in learning performance. This is because the variance of the value regressor in the GLM used to fit fMRI data depends on how much subjects learn about option values (no learning gives a flat regressor), unless regressors are z-scored (I could not find this info in the Materials and methods). This issue needs to be carefully addressed.

– The absence of (negative) correlation with expectation at outcome onset is interesting given the debate about prediction error encoding in the striatum. Yet I am unsure of how the authors interpret this. Is this an artifact from the design (cue and outcome onsets being too close in time), is it that true prediction errors are encoded in other brain regions, or is it that the brain does not encode prediction error at all? Perhaps the authors could clarify their position in this issue in the discussion.
