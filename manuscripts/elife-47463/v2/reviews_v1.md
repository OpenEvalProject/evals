# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- Jan Gläscher
- Marieke Jepma
- Rui Ponte Costa, University of Bristol United Kingdom

## Review text

DOI: [10.7554/eLife.47463.sa1](https://doi.org/10.7554/eLife.47463.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Reinforcement learning models come in two flavors: with and without eligibility traces. Whereas the former require multiple repetitions, the latter models enable reinforcement of entire sequences of actions from a single experience (i.e., one-shot learning). In this paper, the authors use a novel experimental design to explore one-shot learning and eligibility traces during human decision-making. Using pupillary and behavioral responses, as well as computational modeling, the authors show evidence for the existence of one-shot learning and that eligibility traces are a plausible computational mechanism by which this is accomplished. These findings will have broad implications for learning mechanisms that support human decision making.

Decision letter after peer review:

Thank you for submitting your article "One-shot learning and behavioral eligibility traces in sequential decision making" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jan Gläscher (Reviewer #1), Marieke Jepma (Reviewer #2), and Rui Ponte Costa (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents behavioral and psychophysiological evidence for eligibility traces in human reinforcement learning (RL). The experimental paradigm used here provides a novel way to discriminate between RL with vs. without eligibility traces. The key results show that behavioral and pupillometry responses are in line with eligibility traces, which is supported by computational modeling. These main results are replicated across three different experiments.

All reviewers agreed that this is a well-written paper that addresses an interesting and important question. They also found the approach clean and hypothesis-driven, the results convincing, and the modeling comprehensive. After discussion, the reviewers also agreed on a number of issues that would need to be addressed. These are summarized below under “Essential revisions”. Most importantly, all reviewers agreed that the previous literature should be discussed more comprehensively and that some of the results and analytical choices require more discussion. There was some disagreement among reviewers whether an additional control experiment would be necessary, however, all reviewers agreed that adding such data would substantially strengthen the paper.

Essential revisions:

1) The study does a good job in ruling out alternative explanations of the primary finding of one-shot learning. However, one crucial question is left unanswered. Does one-shot learning occur because of the experienced reward or because of the specific action sequence in the first trial? In other words, could one-shot learning occur without a reinforcer at the end of the first trial? The role of reward is essential for the eligibility trace argument because eligibility traces work on the reward prediction error (RPE) and if there is no reward, there is no RPE, and hence nothing to learn (with or without eligibility traces). The cleanest way to answer this question is to run a small control experiment in which some subjects get rewarded at the end of the first trial and others do not get a reward. The behavioral prediction from this experiment would be that if there is no reward, there is no bias in action selection at D2. This additional control experiment would be the most appropriate way to address this point. However, the authors might find another clever way to answer the question convincingly. (Some reviewers noted that reaching the end of a trial in itself may act as a reinforcer and that in this case the suggested control experiment may not work as intended.) At the very least this issue needs a thorough discussion.

2) The authors pooled the data of all participants into one data set before fitting the models, and used cross-validation to deal with potential individual differences. A hierarchical Bayesian approach seems a better way to deal with individual differences. However, redoing the modeling analyses was not considered essential to support the main conclusions, but it would be good if the authors could discuss why they chose to pool the data.

3) For the novelty of the present work to be properly evaluated, the authors need to better contrast their work with previous work in the Introduction and Discussion. Also, parts of this study could be better presented and made more solid to improve its readability by a general audience and further support the results. Suggestions in this direction are given below.

3.1) The authors state that their work provides "clear.… signatures" and that it "solves a long-standing question in human reinforcement learning for which so far only indirect evidence was available" and that "a direct test between the classes of RL models with and without eligibility traces has never been performed". This claim is perhaps too strong. Specially given that there are a number of studies (e.g. Walsh and Anderson, 2011, 2012; Weinberg et al., 2012 and Pan et al., 2005) that have touched (maybe not as directly) on this issue, performing both behavioral studies and comparing different computational models. These studies should be briefly reviewed in the Introduction and clearly stated what is novel in this new study. Also, please tone down the conclusions regarding "clear" and "solves" a problem.

3.2) Previous studies have looked at more direct signals such as ERPs and single-unit recordings (Pan et al., 2005), which provide a more direct measurement of putative eligibility traces. Pupil dilation is an interesting signal to look at, but it is known to correlate with many behavioral signals as discussed by the authors (e.g. expected reward, reward prediction error, surprise and risk). So it is not clear how this signal can directly or clearly support the claims. The authors do a good job in showing that pupil dilation is better correlated with TD-error than with other factors, but how these results relate to ERP and single unit recordings should be discussed.

3.3) Central to this work is comparing models with and without eligibility traces. This comparison should be better illustrated. At present this is done in Table 1 and in schematic form in Figure 1B, rather than exact results from the models. Given how central this is to the paper, it would be better to use a figure for this: illustrating the different model predictions, explicitly, and plotting the model selection scores. For the model selection scores, please show the score as an evidence ratio (or similar; see for use cases Costa et al. 2013 Frontiers; Turkheimer et al. 2003 J. Cereb. Blood Flow Metab; Nakagawa and Hauber, 2011 Neurosci. Biobeh. Rev), which is a relative ranking of the AIC weights.

4) Participants were allowed to solve more than two episodes, however, the paper only highlights the first two. Is the reason for this that only the first two episodes are clearly testing for eligibility traces? In any way, eligibility trace models predict that learning decays as function of time from the reward (older actions would exhibit weaker learning). As the authors may already have some of this data in place, it would be interesting to show them to further support the point, or at least discuss it.

5) It would be important to also show the results without removing some of the pupil responses as indicated in the Materials and methods (or with a less strict method). For instance, the authors could gradually vary the two exclusion criteria that they use (<50% eye-tracker data, z-values outside +/-3) and show how their key results vary as a function of that. This could be a new supplementary figure. The results seem robust enough, but this would make the study more complete.
