# Peer review - Round 1

Editors:
- Daeyeol Lee, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55490.sa1](https://doi.org/10.7554/eLife.55490.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents a novel explanation for lapses in perceptual decision making. Using precise computational models to analyze the data from a click-rate discrimination task, the authors show that lapses might be due to the rats' uncertainty-dependent exploration strategy rather than inattention or motor errors.

Decision letter after peer review:

Thank you for submitting your article "Lapses in perceptual decisions reflect exploration" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Long Ding (Reviewer #1); Alex C Kwan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents an interesting explanation for lapses in perceptual decision making. The authors showed that rats showed imperfect performance on a click-rate-discrimination task. They showed that the amount of lapse depended on whether the decision was based on uni- or multi-sensory stimulus, whether the reward associations were equal or asymmetric for the two choices, and whether M2/pStr was intact. Using precise computational models, they proposed that these lapses were due to the rats' uncertainty-dependent exploration strategy. The results are somewhat consistent with the uncertainty-dependent exploration strategy, but some features that are inconsistent with this strategy appear to be ignored. A critical analysis to directly relate uncertainty and lapse across sessions was also missing. Therefore, although the manuscript has the potential of establishing the uncertainty-dependent exploration strategy as one of the factors contributing to lapses, additional analyses/explanations are needed.

Essential revisions:

1) The contrast between regular multisensory trials and "neutral" trials is a clever design. However, the results did not convincingly support the uncertainty-dependent exploration model. As the authors stated "the lapse parameter on neutral trials should match those on auditory trials, since these conditions have comparable levels of perceptual uncertainty". Judging from Figure 3—figure supplement 1E, this prediction did not hold for the example rat. It is unclear how well it held for the other four rats.

2) Model comparison results in Figure 3—figure supplement 3C suggest that the inattention model performed as well as the Exploration model for fitting uni/multi-sensory data. However, the results of the model fitting should be more fully disclosed. The results in Figure 3—figure supplement 3G were not conclusive. Namely, the inattention model seemed to outperform the Exploration model for rat#4; both models performed similarly for rat #5, and the Exploration model was better for the other three rats. The example rat in Figure 3—figure supplement 1E also showed other behavioral patterns that are puzzling. When reward was increased for the Right choice, there appeared to be a leftward bias (comparing the "Multisensory" curve in the left panel and the "Increased Right" curve in the right panel). The "equal reward" curve in the right panel showed significantly worse performance than other curves. How representative were these behavioral patterns? Do these patterns invalidate the uncertainty-dependent exploration model?

3) The two models (inattention and fixed error) used to compare against the exploration model are simplistic and may not serve as a fair comparison. In particular, based on prior literature on similar rodent task, it seems that another model based on motivation + inattention might be a more relevant and reasonable explanation, and should be compared against the exploration model. There is evidence that in sensory discrimination tasks, rodent's behavior exhibits serial choice bias. Specifically, if the last trial yielded a reward, then that could influence the current decision (Busse et al., 2011; Siniscalchi et al., 2019). One reasonable interpretation is that this is a motivational component that is dependent on the prior trial's outcome. Given this, one model that may be worthwhile to try is an outcome-dependent inattention model, where the amount of inattention differs depending on whether the last trial was rewarded or not. Namely, if the last trial was rewarded, then animal has fewer lapses, whereas if the last trial was not rewarded, then animal has more lapses. There is indication that some aspects of the current data support this idea (Figure 4F). How would this type of model contrast with the exploration model? One specific question is, similar to Figure 4F, but if we additionally plot previous L success and previous L failure, then does the reward history for prior L choices influence the proportion of choosing R at high stimulus rate?

The premise is that the exploratory choices would resemble lapses. This is true in a task design involving two choice options, but probably should be considered as a caveat of the task design. If the task has more than two choices, then one may more confidently distinguish these processes and identify periods of exploration. Some considerations as to how such a task design (or the fact that the current finding only has two options) influences the conclusions should be added in the Discussion.

4) The claim is that there is uncertainty-driven exploration that could explain the lapse rate. However, the task always employs the same criterion boundary for the discrimination problem, and the stimulus set is fixed across sessions. The animals are presumably over-trained and expert in this task, so it is unclear why they would be incentivized to update values for the stimuli in this sensory discrimination task. The authors presented some data to suggest they continuously learn. Is there a normative explanation for why they should be doing this in the current experiments?

5) Although the data in Figure 4C appear to support the uncertainty-dependent exploration model, it is possible that, on equal reward trials, the three rats trained for the "increased rRight" condition performed much worse than the three rats trained for the "decreased rRight" condition. The difference in "Proportion choose high" at 16Hz between the two cohorts for equal reward trials appeared as large as the effects of changing reward. The differences between equal reward trials and "increased/decreased rRight" trials might be due to some factors beyond value associations (e.g., how the two cohorts were trained).

6) There are many variants of models in the manuscript, but they were not presented in sufficient details, making it hard to track what parameters were fixed or fitted separately for different types of trials in a given experiment. For example, for the data in Figure 5, the legend says that the model fits scaled all contralateral values by a single parameter. Does it mean that this scaler was the only free parameter for the inactivation data, after fitting the control data? Or the model was fitted to both control and inactivation data simultaneously, with all but the scaler fixed between the two datasets? If a single scaling parameter can account for the inactivation effects, similar effects would be expected for auditory, visual and multi-sensory decisions for a given rat. But this does not seem to be the case. For example, Rats 8,9,10 in Figure 5—figure supplement 3 showed very different effects between auditory and visual decisions for M2-low rate side inactivation. Similarly, rats 2,3,6 in Figure 9—figure supplement 4 for pStr-low rate side inactivation. It would be helpful to have a table with the fitted parameter values for each experiment/rat, so that readers can better track how the model fitting was done and develop a better sense of how changes in model parameters affect the psychometric curves.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Lapses in perceptual decisions reflect exploration" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Long Ding (Reviewer #1); Alex C Kwan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript presents an interesting explanation for lapses in perceptual decision making. The authors showed that rats showed imperfect performance on a click-rate-discrimination task. They showed that the amount of lapse depended on whether the decision was based on uni- or multi-sensory stimulus, whether the reward associations were equal or asymmetric for the two choices, and whether M2/pStr was intact. Using precise computational models, they proposed that these lapses were due to the rats' uncertainty-dependent exploration strategy. The authors have addressed most of the concerns raised by the reviewers appropriately, but there is one issue that requires additional clarification.

Revisions for this paper:

The original figure of concern actually showed example neutral/auditory trials from different rats. The authors generated new figures showing both types of trials from 5 rats separately (Figure 3—figure supplement 1E and Author response image 2C). In three out of the five rats, for the LOW choice, the lapse was larger for neutral trials; for the HIGH choice, the lapse was larger for auditory trials. This kind of asymmetric difference in lapse appears similar to the predictions for effort manipulation in Figure 4—figure supplement 2. If there was no category-specific value/effort manipulation between neutral and auditory trials, it is not intuitive how the uncertainty-dependent exploration model can account for this asymmetry. An explanation would be helpful.
