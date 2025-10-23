# Peer review - Round 1

Reviewers:
- Sam Gershman, Harvard University , United States

## Review text

DOI: [10.7554/eLife.16127.014](https://doi.org/10.7554/eLife.16127.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Bayesian model of context-sensitive value attribution" for consideration by eLife. Your article has been favorably evaluated by Sabine Kastner (Senior Editor) and three reviewers, one of whom, Sam Gershman (Reviewer #1), also served as Guest Reviewing Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work develops a Bayesian theory of context effects in decision making, and tests it in a behavioral experiment. The proposed model goes beyond previous efforts by introducing multiple levels of hierarchy. The reviewers agree that this is an interesting and important topic, but have concerns about the analysis methodology, presentation of the model/results, adequacy of the experimental data, and relation to previous work.

Essential revisions:

1) Analysis methodology: please address the points raised by Reviewers 1 and 3 concerning statistical analyses and model comparison.

2) Presentation of the model/results: all the reviewers suggested ways in which the presentation could be improved, including clarification of modeling details and task description.

3) Adequacy of experimental data: Reviewer 2 raised important concerns about whether the reported experiment provides a strong test of the theory (particularly the precision-weighting component), and Reviewer 3 pointed out a number of confounds in the design. The reviewers are in agreement that the paper should include new experimental data that addresses the confounds and ideally also provides a stronger test of the theory.

4) Relation to previous work: Reviewer 1 points out several other theoretical frameworks for certain context effects. Please address these in the revision.

Reviewer #1:

1) I didn't see what would seem to be the most obvious analysis of the choice data, namely comparing the LV vs. HV bars (as well as 5 vs. 9 bars) in Figure 4B. The authors report correlations but shouldn't the model predict a difference in means as in Figure 2?

2) The simulation details were unclear to me. Did the authors simulate a synthetic dataset many times and then average the correlations, or did they just run a single simulation? I think the former procedure is better justified, since we don't know whether the results found with the simulations are idiosyncratic or reliable.

3) Some researchers, such as Rangel & Clithero (2012) and Louie, Glimcher & Webb (2015), have drawn connections between context effects and efficient coding, appealing to the idea that divisive normalization is a mechanism for removing statistical redundancies. A Bayesian theory like BCV enables but does not require efficient coding; a given distribution could be coded with varying degrees of efficiency. However, BCV also appears to make some claims about mechanistic implementation which might be relevant to the question of efficiency. How do the authors see the relationship between these theories and BCV? More generally, the authors could deepen their contribution by considering the realization of BCV across Marr's levels.

4) Showing that BCV can account for earlier value normalization results would also bolster the theory. In addition, there is a rich literature on context/decoy effects that would be relevant to at least mention here. Relatedly, work in economics has studied the idea that reference points depend on expectations (e.g., Koszegi & Rabin, 2006), and there have been a number of important recent papers on range effects and relativistic choice processes (e.g., Bordalo et al., 2012; Cunningham, 2013,; Bushong, Rabin & Schwartzstein, 2015). It would be illuminating to better understand how these frameworks relate to BCV.

Reviewer #2:

My major reservation about the paper is that the human data offers only partial confirmation for the Bayesian context model. In its full specification (in the Appendix), the BCV model predicts that incentive value will depend on a divisive scaling term (implementing precision weighting dependent on relative reward variance) and subtractive prediction error terms (low and high context reward predictions, weighted by their relative contextual cue variances). However, the effects of precision – which are a key element of Bayesian approaches – are untested in the analysis of the experimental data. As the authors state in the paper, reward variance is not manipulated and the divisive term (K) cannot be examined. In addition, the subtractive terms should also be precision-weighted by terms relating posterior and prior variances (denoted by tau_LO and tau_HO). However, the results only speak to overall context effects, essentially asking whether there is an overall effect of low and high context on gambling (population regression effects in Figure 5, and the chi-square tests showing positive tau_LO and tau_HO parameters).

The issue is that adaptive effects to average rewards are well known (for example, successive contrast effects in the animal literature and reference point models like prospect theory); without validating the precision-dependent predictions of their model, I'm not sure that the authors can convincingly argue that BCV is a more appropriate model – particularly as other models are not tested. Given the experimental setup, testing the divisive weighting term is not possible in this dataset; however, can the authors make any predictions about not just the significance but the relative magnitude of the weighting factors tau_LO and tau_HO (predicted and fit to data)?

Reviewer #3:

1) Behavioural effects of reward context on incentive value are already well-established and even the specific paradigm used here has already been published by the same authors. Is there any new, surprising behavioural effect that follows from the new model?

2) The Bayesian model presented in the manuscript is not formally compared to other well-established models that may similarly account for the behavioural effects. The authors should show with formal model comparisons that their model outperforms other classic (non-Bayesian) models commonly employed to model context effects on value-based choice.

3) The model is not biologically realistic. This is not always a problem; in fact, there are many elegant demonstrations that Bayesian frameworks can account for optimal performance in various domains better than other accounts. However, in the specific context of reward-guided decision-making, it is unclear why and how a Bayesian framework should apply, and to what degree it is more consistent with behaviour and the underlying neural computations. Please provide a lot more information on how this model may be implemented by neural computations. In particular, it would help if there was any empirical evidence for the hierarchical representation of reward context.

4) The Abstract claims that the model "generates new empirical predictions and may help explain important phenomena in psychopathologies such as addiction." I found the corresponding text in the Discussion rather vague. Please provide explicit predictions for specific experimental effects that follow from this model and please explain much more concretely which important phenomena in psychopathologies are explained by it.

5) The manuscript claims in several places that a reward's incentive value corresponds to the (precision-weighted) prediction error. This is misleading. By definition, the incentive value is the property of a stimulus/expected reward that triggers approach behaviour and choice of the corresponding option. This representation must therefore be computed before the choice is taken and the reward is obtained. The prediction error, by contrast, is the deviation of the reward obtained as a consequence of the choice from the reward expected prior to the choice. This post-choice representation can therefore not be the incentive value guiding choice. The authors need to clarify their terminology and ensure that they remain consistent with established definitions in the literature.

In addition to the conceptual points listed above, the manuscript also has shortcomings with respect to methodology and results presentation that will need to be addressed:

6) The behavioural task was not designed to allow proper tests of the full model. Some of these problems are listed by the authors themselves and have led to adaptations of the model so that it could be fit to the data. For instance, reward variance in the different decks is not varied, is heavily constrained (there are only 3 different reward values per deck), and is perfectly correlated with average reward magnitude. To properly test whether the precision of reward prediction errors established by the different contexts really plays an important role, the authors should fit the full model to datasets with contexts that differ substantially in their reward variance and that disentangle reward magnitude from reward variance. Moreover, the contexts should be associated with a lot more than just three possible reward values so that the form of the expected reward distributions can be properly approximated (see below).

7) The model specification does not match the environment established by the behavioural task. The decks were associated with 3 equiprobable values per deck. Therefore, "smart" subjects would employ a flat discrete expectation of the three possible values within the given context. In contrast, the modelling solution is based on continuous (Gaussian) distributions that are not restricted by the bounds imposed by each context. There are two problems with this: (1) If we assume that the subjects indeed optimally integrate all information, then a flat prior belief bounded by the context's minimum and maximum reward would be accurate. This cannot be modelled by the presented specification. (2) Even if subjects employed continuous Gaussian priors to model reward expectations, such distributions would probably not be narrow enough with respect to the context bounds (i.e., the priors would wrongly lead to expectations of rewards that are outside of the bounded scale). These problems will probably be evident if the authors report the values of the latent variables after fitting the model to the empirical data. Please include such a table to allow the reader to inspect this issue.

In my view, if the authors really wanted to maintain a Bayesian optimal observer model, then they should examine how the prior (potentially flat, but can also be modelled if the authors like) is combined with the likelihood of the actual numeric representation to obtain a posterior estimate that should naturally occur within the actual numeric bounds of the context (for an example on how to formally deal with Bayesian problems of this kind, i.e. bounded contexts, see Jazayeri and Shadlen 2010, Nature Neuroscience). This formal specification can then be expanded to the interesting contextual hierarchical framework that the authors propose in their study.

8) The authors rescaled the contextual averages and reward values to perform their model fits. Why? A correctly specified model should be able to take as inputs the actual values of the contexts and rewards of their behavioural paradigm (which are all single-digit numbers after all). This would help to assess the model's explanatory power.

9) The authors perform model comparison by summing log-likelihoods across participants. I find the selection of this approach for model comparison surprising, given that several of the co-authors have pushed the use of precise Bayesian model selection methods that properly account for the complexity and variability of the model fits across trials and participants. The authors should employ such methods and should provide values quantifying the quality of the model fits after penalizing for model complexity.

10) The behavioural task is described in a fashion that makes it hard to replicate. For instance, is it true that on every trial, a card was drawn from the blue deck? If so, how were the different deck contexts varied across the different colours? Please make sure the task described in sufficient detail so that another person could program it.
