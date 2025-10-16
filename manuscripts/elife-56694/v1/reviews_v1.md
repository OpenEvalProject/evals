# Peer review - Round 1

Editors:
- Daeyeol Lee, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56694.sa1](https://doi.org/10.7554/eLife.56694.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors showed that heterogeneous activity of neurons in the caudate nucleus reflected all major aspects during perceptual decision with asymmetric rewards. They also found that the effect of electrical stimulation in the caudate nucleus was quantitatively related not only to the behavioral strategy of the animal but also to the functional properties of the neurons recorded in the stimulation site. These results establish the role of the caudate nucleus in mediating the reward bias during perceptual decision making.

Decision letter after peer review:

Thank you for submitting your article "The caudate nucleus contributes causally to decisions that balance reward and uncertain visual information" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Daeyeol Lee as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Chandramouli Chandrasekaran (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that some additional analyses might be required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study examined the role of the caudate nucleus in combining uncertain sensory information with reward bias during decision making by analyzing the effects of electrical stimulation and neural activity within the frame of a drift-diffusion model. In their previous study, the authors have already characterized the biasing effect of unequal reward on perceptual decision making using two parameters corresponding to the change in the drift rate (me) and bound (z). There are at least two important findings in this study. First, they showed that heterogeneous activity of neurons in the caudate nucleus reflected all major aspects of the task, including coherence (i.e., signal-to-noise ratio), choice, and reward bias, and their interactions. Second, they found that the effect of electrical stimulation was quantitatively related not only to the behavioral strategy of the animal but also to the functional properties of the neurons recorded in the stimulation site. While these results seem to firmly establish the role of the caudate nucleus in mediating the reward bias during perceptual decision making, there is a room for improvement in the analyses and presentation. The authors should improve their exposition in the modeling section and to simplify their results where possible to make it easier on the reader. A large number of parameters introduced in the paper makes it difficult to keep track of everything.

Essential revisions:

1) The section that describes the relationship between the effect of microstimulation and the animal's strategy (subsection “Microstimulation caused coordinated adjustments to reward-dependent decision biases that mimicked the monkeys’ voluntary strategy”) was very hard to follow and is not entirely convincing. This section relies heavily on the findings from the previous study by the authors that the negative correlation between the changes in the drift and bound reflected the animal's heuristic strategy for reward maximization. The results in that study also suggest that such adjustment occurred slowly across many sessions. Was it the case then that the effect of stimulation changed similarly during the same period? If so, the observed relationship between the animal's strategy and stimulation effect might be spurious and caused by a slow cross-session drift (any slow changes in the animal's strategy not captured by the model).

2) Microstimulation result in Figure 3 is complex to parse. There are 12 distributions with 6 panels of scatter plots. Might it make sense to perhaps obtain a figure that demonstrates the effect size for rew x estim. Appropriately normalized regressions might allow such a plot. That way, one could understand the magnitude of the effect.

3) The modeling in Figures 4 and 5 are nice. The coordinated additive and scaling hypothesis assume that the monkeys change bound height and drift rate across sessions. Microstimulation has a coordinated effect on Δbound and Δdrift. The data in Figure 5 is largely consistent with the Figure 4E and F. However, the results are not entirely convincing, in part because they entirely depend on the contrasts in the model parameters for reward context dependent and independent components. However, if the underlying parameters (e.g., Paracontra-LR,estim, etc.) are correlated, the results might need a different interpretation. It might be possible to address this, using PCA. For example, if the authors run PCA on the parameters used to quantify the effect of reward without stimulation (e.g., Paracontro-LR,no estim) and PAC on parameters used to quantify ΔPara(estim) and ΔPara(rew x estim), do they find significant correlation for more than one PC?

There are also some discrepancies between the effect of microstimulation presented in Figure 4E, F. First microstimulation leads to a shift diagonally upwards from the line in Figure 5D which is inconsistent with Figure 4C and F. Whereas the coordinated additive and coordinated scaling push it downward. This needs to be better explained to ameliorate concerns for the reader. For example, placing the scatter plots from Figure 4C-F middle and right columns and placing them in Figure 5 might be helpful. The colormap should also be the same between Figures 4 and 5 so that one can compare both of these reliably. They could sacrifice some of the logistic vs. DDM plots to the supplements. There are several additional concerns.

1) Model predicts more lower Δdrift and lower Δbound for the coordinated scaling case, but the data don't seem to show that. Is this important?

2) What happens when you change the size of the noise for Figure 4D, does it show a less steeper change in Figure 4D right panel?

3) Quantitative evidence brought to bear to favor the coordinated scaling over the independent model in Figure 4D right panel would make it more compelling. Currently, one can look at Figure 4F and Figure 5F and see they are similar.

4) The fact that correlation coefficient (slope) between changes in drift and bound (Figure 6E) tends to be negative for Shuffles 3 and 4 is a concern, because this raises the possibility that the observed relationship between the two measures might be also an artifact. Can this be addressed using a simpler approach of shuffling the parameters fit for different stimulation and reward context (e.g., Paracontra-LR,estim), rather than simulating individual trials and re-estimating the model parameters?

5) There are some problems in how neural activity was analyzed using a regression model. For example, the activity during a variable window might be confounded with reaction time (e.g., Epoch 5; subsection “Caudate neurons encode both visual and reward information”, Figure 2—figure supplement 2), which could lead to mis-identification of signals related to coherence. Also, the statement that a majority of the neurons showed at least one of many effects is not particularly meaningful, since the proportion of such neurons is expected to increase with the number of tests when they were not corrected for multiple comparisons. Similarly, the effects of microstimulation on multiple types of behavioral data (subsection “Caudate microstimulation evoked reward context-dependent effects on behavior”) should be reported more carefully.

6) Some of the results reported in this study might require more careful interpretation. For example, the fact that microstimulation effected varied with the reward context by itself might not provide strong evidence that the caudate nucleus is causally involved in balancing visual evidence and reward bias, because such interaction might occur when the magnitude of microstimulation varies with the reaction time (which is in turn influenced by reward context).
