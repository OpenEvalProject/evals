# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54474.sa1](https://doi.org/10.7554/eLife.54474.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work demonstrates that chemogenetic inactivation in the secondary motor cortex (M2) impairs the performance of mice in perceptual decision making when a decision boundary is dynamically shifted but not when the task is stable, thus revealing a specific role of M2 in adaptive decision-making. This work will be of great interest to those who study the neural mechanisms of decision making.

Decision letter after peer review:

Thank you for submitting your article "Control of adaptive action selection by secondary motor cortex during flexible visual categorization" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex C Kwan (Reviewer #2); Carl CH Petersen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, Wang and colleagues examined the role of secondary motor cortex (M2) in flexible decision making. Mice were trained to categorize visual stimuli based on spatial frequency, designed after the task developed by Jaramillo, Zador and their colleagues. The position of decision boundary along the spatial frequency was shifted across blocks of trials. Mice biased their choice depending on the position of decision boundary. The behavior was consistent with a model in which animals' choices were guided by the stimulus history but not by the reward history. The authors then demonstrate that chemogenetic inactivation of M2 impaired flexible changes in the animals' decision boundary although it did not impair the performance without boundary shifts.

All the reviewers thought that this study addresses an important question, uses a good task, and provides important results. However, the reviewers thought that there are various technical and interpretational concerns that need to addressed before publication of this work in eLife.

Essential revisions:

1) The effect of chemogenetic inactivation is rather small, and the results and the data analysis do not appear to be very robust. Given that DREADD likely results in partial inactivation, it is difficult to interpret negative results for mPFC and OFC. Although the reviewers commend that these experiments were done, the results need to be interpreted more carefully, and tests using more complete inactivation (e.g. muscimol) would be preferable.

2) The authors use model-based analysis and conclude that the animal's choices are guided by stimulus history but not by reward history. Although this is a very important effort, the reviewers identified several issues that need to be addressed.

2a) The manuscript emphasizes changes in the decision boundary (task contingency) but the model analysis indicated that the animals were not reacting to reward history but stimulus history. It seems that this is mainly due to an unusual choice of stimuli (a majority of stimuli were chosen from right next to the decision boundary) used for each block, concurrently with shifting decision boundary. This unusual choice of stimuli might have masked the effect of reward history in behavior or data analysis. This task design needs to be explained more clearly in the Results section and preferably some figures representing it. Furthermore, the motivation of this task design, as opposed to shifting decision boundary without changing the stimulus statistics, needs to be explained.

2b) The validity of model-based analysis depends on whether the model was able to fit the data reasonably well in the first place. Please provide the evidence (quantification and visualization) of goodness of fit.

2c) The authors conclude that the animals' choices were not affected by reward history based on the observation that the model that depends on stimulus history fit the data better than a reinforcement learning (RL) model. The reviewers thought that it is impossible to make such a conclusion just by a comparison with a particular RL model. The authors need to explore more thoroughly what alternative RL models may fit the data well. The current RL model that the authors used computes action values for left versus right choices without considering stimuli. A simple possibility is an RL model that computes action values specifically for each stimulus (corresponding to "states" in RL).

3) The reviewers thought that the electrophysiological recording data are not thoroughly analyzed nor presented in an informative way. The reviewers make various suggestions to improve (see below). One possibility is to remove this part altogether (Reviewer 1) but we would like to see more informative presentations and insightful analyses of the electrophysiology data.

More detailed explanations of the above points from individual reviewers are included in the following. The manuscript will be re-evaluated based on your responses to these concerns and suggestions.

Reviewer #1:

The paper by Wang et al. developed a task which requires mice to indicate whether a visual stimulus was higher or lower in spatial frequency (SF) than a boundary SF value. The boundary SF was altered between two values in two different blocks, requiring mice to adjust an internal decision criterion to obtain maximum reward.

Using a logistic regression model, the paper estimates the dependence of decisions on the stimulus, and on trial history. In doing so, it demonstrates that mouse decisions after a block switch was primarily accounted for by stimulus history (which differed between the block types) rather than the experience of errors on the stimulus condition positioned between the boundary values.

The paper demonstrates that chemogenetic inactivation in M2 impairs choice behaviour during the switching period but not during the stable period. By applying the behavioural model, the paper finds that M2 inactivation during the switch period reduces the behavioural dependence on stimulus history (for non-reversing stimuli), suggesting that M2 plays a causal role in stimulus-action remapping based on stimulus history. Interestingly, the paper shows that M2 doesn't seem to play a role during stable stimulus-choice trials, and it shows that the effect on switching trials is specific to M2 and not nearby frontal regions such as mPFC or OFC. The paper also includes results from electrophysiological recording of M2 during the task.

Overall, the behavioural experiment and the inactivation results are very interesting. Nevertheless, the electrophysiological results are hard to understand, and seem to add little to the paper. The conclusion of the paper, that M2 plays a role in flexible stimulus-choice association based on stimulus history is novel. However we have several questions and concerns:

Major concerns:

Many of the conclusions hinge on the model quality. However, there is no indication anywhere that the behavioural model is actually fitting the behavioural data well. Only comparisons between different models are presented. It is necessary and useful to visualise the model fits using psychometric curves.

The stable period is conceptualised as a period when the decision criterion is stable. Yet the model shows that the DC is affected by stimulus history and lose-shift effects (Figure 2). Thus, the stable period is not so stable by these parameters. Given this, and the fact that blocks are short (60 trials), fitting the models separately on the stable and switch period might be problematic. This is particularly the case because the paper is then performing separate model comparison for the stable and the switching period trials. As such, a better approach might be to fit models on all trials, select the best model accordingly, and fit this best model separately on different sections of the data, if necessary. Or add a new parameter to the model that can indicate stable vs. switch epochs, and fit the model once using all trials.

Related to separate model fitting and in the case of inactivation data, why not fit a model to the CNO and Saline data together, and estimate a δ parameter which estimates how much the α/β/γ parameters are changed by inactivation?

The paper relies on fitting the model separately to saline and CNO sessions, to identify specific parameters that are affected by inactivation. But the model itself could be under-constrained, meaning the parameter estimates are not stable. It would be useful to simulate data with known parameter changes, and then see if it is possible to recover those parameter changes from the model based on the number of trials that were obtained.

The comparison with the RL model: it appears that the RL model performs as good as the best regression model in the stable period but not in the switching period. What was the learning rate of the fitted RL in the switching period compared to stable period? Was there any constraints on learning rate when fitting? More generally, since the paper is considering a learning situation, the comparison with the RL model seems important and should be explained further. The class of RL model tested here can be reformulated to be analogous to the regression with dynamic decision criterion (prediction error-mediated changes in Q values can be adjusted to be analogous to changes in decision criterion). As such, it is unclear how these two models are testing competing hypotheses.

The model only allows stimulus history effects after trials of non-reversing stimuli. Surely the mouse would be adjusting the DC for stimulus history even if that stimulus was the reversing stimulus. How do the result changes if considering these stimuli?

The data shows that M2 inactivation does not affect the correct rate for non-reversing stimulus. This is surprising and interesting given many of the studies the paper cites do find robust behavioural effect of M2 inactivation across stimulus conditions (Goard et al., 2016 visual detection, Guo et al., 2015 whisker detection). In these studies, the mice are presumably in a “stable” condition regarding stimulus-choice association. Why do you think there's this discrepancy? Does this relate to using chemogenetic (here) vs. trial by trial optogenetic used in those studies?

It would be necessary and informative to see example of psychometric curves or learning curves in the inactivation condition vs. control, rather than only relying on model fits.

The results from electrophysiology experiments are cryptic and hard to follow. It might be easier and more convincing to illustrate example neurons before introducing the other analyses. For instance, Figure 5—figure supplement 2 is an interesting result and should probably be the first one mentioned for the ephys analysis. Overall, the electrophysiological experiments do not seem to add to the paper, and it might be best to be removed from the paper.

Related to electrophysiological data, it is hard to understand the need to use three different analysis methods: regression, ANOVA, and ROC analysis, each doing slightly different things.

There are several instances of statistical tests not correcting for multiple comparisons. For instance, in Figure 4D, the effect of M2 inactivation on the percent correct for reversing stimuli seems to be statistically significant primarily due to data from 4 mice. Does this effect stay after correcting for multiple comparisons?

Reviewer #2:

This paper by Tian-Yi Wang and colleagues describes a series of experiments to study the role of mouse M2 in adaptive action selection. The strength of this paper is the rigor. The experiments were based on a well-designed task involving flexible stimulus categorization (that have been pioneered in rodents by Zador, Jaramillo, et al.). The authors also did a great job putting together a computational model that provides considerable insights into the mouse's behavioral strategy. This led to an intriguing behavioral conclusion that mice are doing the task by using sensory history but not reward-based learning.

In terms of the neural conclusion that M2 is involved in adaptive sensory-motor selection, there are a few other studies now suggesting that M2 is involved in driving sensory cue-guided choices following a switch in contingencies. Nevertheless, there is still substantial value here because the study is excellent and provides arguably the strongest evidence to date. There is also additional conceptual novelty in looking at region differences, comparing M2 with mPFC and OFC.

The manuscript is well-written, and very easy to follow and understand.

Overall, the study is technically sound and conceptually important.

Major comments:

– The neural activity analysis, correlating ROC selectivity value for previous stimulus preference (non-reversing stimulus trial) and current left-right choice preference (reversing stimulus trial) (Figure 5D), is taken as evidence that M2 neurons use sensory history to influence current choice. The analyses were done for a particular time window of a trial. What happens if this analysis was applied to a sliding window starting from last trial to current or even next trial? When does this sensory-choice coupling emerge and when does it end? This is different from the decoding analysis is Figure 6, because it speaks to the interaction rather than decoding of choice or stimulus alone.

– Again, because Figure 5D is important – currently this analysis was done for cases when current trial was the reversing stimulus and the prior trial was the non-reversing stimulus. What about for other trial conditions? Do we still see the correlation in the sensory and motor related neural signals? In particular, what about the case when the current trial was the reversing stimulus and the prior trial was also a reversing stimulus?

– The comparison between M2 and mPFC and OFC is important. The results were presented as Figure 4—figure supplement 5 for mPFC and figure supplement 6 for OFC. I feel that these are exciting results demonstrating regional differences. At least some parts of each should be moved to be a main figure.

Reviewer #3:

Wang, Liu and Yao study the role of M2 in mice during a visual categorization task. Mice were trained to obtain water reward on left vs. right depending upon the spatial frequency of a visual grating with a variable decision boundary. Through modeling of decision criteria, chemogenetic inactivation and electrophysiological recordings, the authors conclude that M2 contributes to flexible stimulus-action coupling.

I think the behavior is well-designed and mice seem to perform well. I also like the quantitative modeling of the behavior.

1) I find the overall effect of the DREADD inactivation of M2 on behavior to be small. It is not obvious to me that DREADD inactivation is being applied in a useful way here. Given that there is no cell-type-specific manipulation, it would probably have been simpler and better to use pharmacological inactivation (e.g. muscimol). This would likely give a complete inactivation of M2 rather than the reduction to ~30% activity currently shown in Figure 4B. Perhaps larger effects upon behavior might have been observed. The small effect size reported for M2, also means that the negative effects for mPFC and OFC inactivation are less impressive, although it is very good that the authors carried out these further experiments.

2) The electrophysiological data are summarized in Figure 5 as correlations, but the overall description of the data is rather limited. I think the authors could give a more extended analysis of spiking activity across trial time, including showing example neurons. I imagine that similar effects might be found in multiple other brain regions, if they were recorded.

3) I am somewhat concerned by the choice of stimuli presented to the mice. I read that the type of visual stimulus depends upon the boundary frequency. For example: "For the low boundary block, gratings at 0.03 and 0.095 cycles/o were presented for 90% of trials, gratings at the other frequencies were presented for 10% of trials, and the boundary frequency was between 0.065 and 0.095 cycles/o. For the high-boundary block, gratings at 0.095 and 0.3 cycles/o were presented for 90% of trials, and the boundary frequency was between 0.095 and 0.139 cycles/o." I think the statistics of presented stimuli will change perceptual thresholds. Why not use the same stimulus set throughout? This would seem to be fairer.
