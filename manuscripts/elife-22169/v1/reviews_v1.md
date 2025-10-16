# Peer review - Round 1

Editors:
- Naoshige Uchida, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22169.033](https://doi.org/10.7554/eLife.22169.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Catecholaminergic challenge uncovers distinct Pavlovian and instrumental mechanisms of motivated (in)action" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Naoshige Uchida (Reviewer #3), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sam Gershman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, the authors tested human subjects in a novel motivational Go/NoGo task (an extension of Guitart-Masip et al., 2012 task) in order to disentangle the impact of reward and punishment on instrumental learning from Pavlovian bias. Although the previous study had only one type of go response, the present study included two types of go responses (left versus right buttons), in order to test how reward and punishment affected specific instrumental behaviors. The authors tested a large number of subjects (N>100) in this task and also examined the effect of catecholamine uptake inhibitor (methylphenidate) on behavior.

All the reviewers found this study interesting and important. The multiple Go options and the pharmacological manipulation (MPH) are indeed potentially very powerful to further disentangle the Pavlovian system from the instrumental learning system. This is important because the previous study (Guitart-Masip et al., 2014) did not explicitly distinguish Pavlovian versus instrumental effects because the observed effect could be explained by reinforcement of a specific action (instrumental effect).

However, the reviewers pointed out various concerns that may affect the interpretation of the results. We would like to see your response to the following points:

Major points:

1) There appears to be a discrepancy between the best fitted model's simulation results (Figure 3D) and the behavioral data (Figure 2D). It is not clear whether the model's key predictions are supported by the data (although the authors performed extensive model comparisons).

1A) The key prediction of the biased instrumental learning model (the best fitted model; M4 with κ) is "faster learning for Go-to-Win" and "slower learning for Go-to-Avoid", as the former is driven by Go-Reward and the latter is driven by No-Go-Punishment. Is this right? This can be seen in the model simulation results (Figure 3D), but not clear in the data (Figure 2D). In fact, the overall difference in data (Figure 2F) appears to be largely due to the initial difference (t=0, Figure 2D), rather than the difference in learning rates. The learning for Go-to-Avoid looks a little faster than for Go-to-Win. Why?

1B) Shouldn't the initial difference between Win and Avoid in data (Difference between Green and Red at t=0 in Figure 2D) be captured by the Pavlovian bias term (π) in the model? However, the initial difference in the simulation seems to be significantly smaller (Figure 3D). In fact, the impact of the Pavlovian bias (πV(s) =0.2*0.5=0.1 --- Equation 3) seems to be much smaller than the impact of rewards due to the large reward sensitivity.

2) One very strange thing about the best fitted parameters (Figure 3B, Figure 5B) is the very large sensitivity (ρ=40 or more), in contrast to what previous similar studies suggest (e.g. Huys et al., 2011, where they reported sensitivity = 3). This could suggest that the behavior is in fact extremely deterministic (one reward can swing the decision probability from 0 to 1). If this is the case, the stochastic feature of the model results (Figure 2D) is not driven by the usual sense of learning but the stochasticity of the reward contingency (80% vs 20%), or even possibly by the sum of step functions (Gallistel et al., 2004). This very large sensitivity makes the model results very hard to interpret. It would be nice if the individual simulation traces are shown, in addition to the mean, so that we can see how the model actually behaves.

3) The authors perform their model selection by comparing different models that gradually incorporate additional parameters but they do so in one particular order. To establish the main conclusion, it is important to demonstrate the existence of both Pavlovian and instrumental effects. To do this, the authors should demonstrate the following. First, the authors should show that the model that includes all the parameters (model 4) is significantly better than the model that lacks only the Pavlovian or instrumental bias parameter (i.e. the model that lacks either b or κ). The current analysis only addresses this for κ. In other words, the authors should show that the model that does not include the b parameter performs worse than the full model (model 4) in order to prove the significance of b (Pavlovian effect).

4) There is a potential confound, due to a previously reported asymmetry between the reward and the punishment sensitivities (e.g. Huys et al., 2011). Since that the learning rate and the sensitivity are closely related with each other, and that the authors did not explore the asymmetric sensitivity, the assumed learning asymmetry (Equation.4) could be better altered by the previously reported asymmetric sensitivity that is independent of actions.

5) Reverse inference from working memory capacity and trait impulsivity to dopamine seems problematic, since these individual differences are presumably multi-factorial. One reviewer was surprised that the authors did not use something that is potentially less ambiguously related to baseline dopamine levels, such as spontaneous eyeblink rates. Relatedly, one of the authors (Frank) has suggested that working memory may instantiate a separate learning mechanism linked to prefrontal dopamine levels (Collins & Frank, 2012; Collins et al., 2014). This appears to complicate the interpretation of working memory capacity in this task, and at least requires some comment. We could also see the value of doing more modeling in this vein, using the models developed by Anne Collins, but since the modeling in this paper is quite extensive, we would be happy with leaving this as a task for future work.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Catecholaminergic challenge uncovers distinct Pavlovian and instrumental mechanisms of motivated (in)action" for further consideration at eLife. Your revised article has been favorably evaluated by Sabine Kastner (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

All the reviewers thought that the authors have done a great job addressing the previous concerns and the manuscript is greatly improved. However, Reviewer #1 found that some clarifications are necessary. We therefore would like to see your response before proceeding for publication. Please respond to the two remaining points raised by Reviewer #1, as appended below:

Reviewer #1:

I appreciate the authors' effort to address our concerns. I think the paper became more informative and accessible. I am just a bit confused with a couple of points. It would be nice if the authors could clarify them in the final version.

I detail my confusions and then I write a suggestion.

1) In new Figure 3, the authors show that "The impact of the Pavlovian bias (π) on choice decreases over time." And then "We note that the initial difference in Go responding between Win and Avoid trials is somewhat underestimated (trial 1-2). This is likely the result from the decreasing impact of the Pavlovian bias over time (B).". This logic confuses me. If the impact of the Pavlovian bias is the largest in the first few trials, how should we expect the underestimation in those trials? I understand the argument of the likelihood reflecting the fitting performance of all trials; but it is not clear to me how the decreasing impact justifies the initial underestimation. Also it is not clear to me how Author response image 4 supports that " This discrepancy (p(Go)Win-Avoid) is largely constrained to the first two trials and is absent in later trials." For example, p(Go)Win and p(Go)Avoid seem to become smaller over trials in the data, but in the model it doesn't seem to be. (I think the discrepancy on each trial is easy to quantify if authors wish to)

2) In response to our point 2, the authors claim that "the effective updating of the Q-value is the same order of magnitude as the Pavlovian influence on the action weights" However, I am not sure about this, because "The effective updating of the Q-value would be +.34 and +.55 for a rewarded NoGo and a rewarded Go response respectively" and the Pavlovian bias is 0.06 (-0.06) for Win (Avoid) trials (Equation 3). I don't think the relative effect is relevant here, because only one of them appears on each trial. Then I think it would be fair to say at least that the update +0.55 is an order of magnitude larger than the Pavlovian bias -0.06. (For the other point of the large sensitivity, I understand the authors response. The learning rate now became much smaller than the original version thanks to the median.)

For both points 1 and 2 above, I think what has been confusing me is that we don't see strong effects of the Pavlovian bias in the mean traces (or comparing the mean estimates). But what it really matters is the wide distribution of the Pavlovian bias (Figure 3—figure supplement 2). In fact, Figure 3—figure supplement 2A seems to clarify my confusions 1 and 2. So if the authors agree with my interpretation, I would suggest to stress in the paper that 1) the Pavlovian bias doesn't appear to be strong in the mean estimates (mean traces), but 2) the bias is so strong for a significant number of subjects (Figure 3—figure supplement 2) that it improved the overall fitting. It'd be nice if the authors could clarify the wide distribution of Pavlovian bias is consistent with previous studies.

Reviewer #2:

I think the authors have done a very thorough job addressing the issues raised in the reviews.
