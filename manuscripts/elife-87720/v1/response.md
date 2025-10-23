# Author response - Round 1

Authors:
- Yumeya Yamamori ([ORCID: 0000-0001-5508-7965](https://orcid.org/0000-0001-5508-7965))
- Oliver J Robinson ([ORCID: 0000-0002-3100-1132](https://orcid.org/0000-0002-3100-1132))
- Jonathan P Roiser ([ORCID: 0000-0001-8269-1228](https://orcid.org/0000-0001-8269-1228))

## Response text

DOI: [10.7554/eLife.87720.4.sa4](https://doi.org/10.7554/eLife.87720.4.sa4)

The following is the authors’ response to the previous reviews

Reviewer #1:

Comment on revised manuscript: Thank you for your responses - they have addressed most of my concerns.

We thank the reviewer again for their assistance in improving our manuscript.

Reviewer #2:

Additional context:

The sex differences between the samples are interesting as effects of sex are commonly found in AAC tasks. It would be interesting to look at the main model comparison with sex included as a covariate.

Firstly, we thank the reviewer for their re-evaluation of our manuscript.

To the reviewer’s comment, we apologise for the lack of clarity. The analyses included in our revision were indeed based on the main logistic regression model of choice, including sex and age as covariates. We have clarified this in the manuscript as follows:

While sex was significantly associated with choice in the hierarchical logistic regression in the discovery sample (β = 0.16 ± 0.07, p = 0.028) with males being more likely to choose the conflict option, this pattern was not evident in the replication sample (β = 0.08 ± 0.06, p = 0.173), and age was not associated with choice in either sample (p > 0.2).

As it is difficult to include sex as a covariate in the reinforcement learning models in the classical sense as in a linear regression, we assessed sex effects on the individual parameters produced by these models instead, as follows:

Comparing parameters across sexes via Welch’s t-tests revealed significant differences in reward sensitivity (t289 = -2.87, p = 0.004, d = 0.34; lower in females) and consequently reward-punishment sensitivity index (t336 = -2.03, p = 0.043, d = 0.22; lower in females i.e. more avoidance-driven). In the replication sample, we observed the same effect on reward-punishment sensitivity index (t626 = -2.79, p = 0.005, d = 0.22; lower in females). However, the sex difference in reward sensitivity did not replicate (p = 0.441), although we did observe a significant sex difference in punishment sensitivity in the replication sample (t626 = 2.26, p = 0.024, d = 0.18).

Could the authors double check the mean/SD of approach in each group for typos? The numbers are identical.

Thank you for spotting this – the means were indeed similar (discovery: 0.521, replication: 0.516), but the standard deviations were marginally different (discovery: 0.140, replication: 0.148). We have amended the manuscript to reflect this, as follows:

Across individuals, there was considerable variability in overall choice proportions (discovery sample: mean = 0.52, SD = 0.14, min/max = [0.03, 0.96]; replication sample: mean = 0.52, SD = 0.15, min/max = [0.01, 0.99]).

Reviewer #3:

The revised paper commendably adds important additional information and analyses to support these claims. The initial concern that not accounting for participant control over punisher intensity confounded interpretation of effects has been largely addressed in follow-up analyses and discussion.

I commend the authors on their revisions. My initial concerns have been largely addressed. Minor suggestions below.

We thank the reviewer again for their assistance in improving our analyses and manuscript.

Changing the visualisation of the logistic regression model in Figure 2 to tertiles instead of quartiles seems expedient, and does not properly address the points raised by the other reviewers. The argument that non-linear trends in the extreme bins are due to less data is plausible, but unsatisfying given how reliable the pattern seems to be (across samples, with small standard error) and . It is possible, albeit perplexing, that the influence of punishment probability on choice is non-linear. I think the current figure with tertiles is acceptable, but I would suggest including the figures with non-linear data as a supplementary figure, for sake of transparency and reader interest.

We agree that this is likely more complex than a simple linear effect (in the logistic space), especially given the concurrent reward probabilities which also fluctuate in the task. We also agree that the non-linear figures should be made available in the interests of transparency, and have included them in the Supplementary Materials.

We direct interested readers to the relevant section from the figure legend as follows:

"Figure 2. Predictors of choice in the approach-avoidance reinforcement learning task. … We show linear curves here since these effects were estimated as linear effects in the logistic regression models, however the raw data showed non-linear trends – see Supplementary Figure 15."

We have included the non-linear figures in Supplementary Section 9.11 Effects of outcome probabilities on choice in the task: non-linear effects as Supplementary Figure 15.

As an aside, the argument that approach-avoidance joystick tasks do not have a non-human counterpart misconstrues the translational root of these tasks, which was (at least in part) an attempt to model (successfully or not) general approach/avoidance processes measured in non-human tasks, e.g. appetitive/aversive runway tasks using rodents.

Our aim in this manuscript was to develop a task that was closely matched to non-human counterparts in both the experimental procedure (choice over reward/punishment outcomes) and cognitive process involved (simultaneous reward/punishment learning). With this in mind, we wanted to convey that non-human and human measures of approach/avoidance processes were historically distinct in terms of the procedures (e.g. using a joystick vs navigating a runway, due to ethological differences), and that this was potentially problematic with respect to computational validity. However, at this early point in the introduction, it was unnecessary to make a strong distinction between these tasks, which as the reviewer duly notes, follow similar approach/avoidance principles and share similar experimental roots. Therefore, we have opted to omit the reference to translational similarity in the relevant text, as follows:

In humans, on the other hand, approach-avoidance conflict has historically been measured using questionnaires such as the Behavioural Inhibition/Activation Scale (Carver and White 1994), or cognitive tasks that rely on motor/response time biases, for example by using joysticks to approach/move towards positive stimuli and avoid/move away from negative stimuli (Guitart-Masip, Huys et al. 2012, Phaf, Mohr et al. 2014, Kirlic, Young et al. 2017, Mkrtchian, Aylward et al. 2017).
