# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26801.026](https://doi.org/10.7554/eLife.26801.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Effects of dopamine on reinforcement learning and consolidation in Parkinson's disease" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Travis Baker (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study follows a number of previous studies that explored the relationship between dopaminergic medication and learning, including examining in more detail the main effect described by Frank and colleagues in 2004. As the authors note, it is not clear from that original study whether the effects of dopamine were related to learning during a probabilistic selection task (PST), or rather to the consolidation and retrieval of the learned values. Here they use three separate experiments to test how medication influences both memory and learning from positive and negative feedback. The most striking result is a failure to replicate the primary findings from Frank and colleagues. They also present a novel finding showing that patients on mediation during learning had increases in memory accuracy after waiting 24 hours for testing, suggesting a role for dopamine in memory consolidation but not necessarily on reinforcement learning.

The reviewers agree that this is a highly worthwhile and well-executed study, and the manuscript is well written. The authors use sound methods but fail to reproduce a highly cited study. As such, this study has the potential to help move the field forward by better understanding the exact conditions in which dopamine affects learning, memory, and decision-making behavior. That said, the reviewers also agree that there are several major issues that must be addressed, detailed below.

Essential revisions:

1) Given in particular the lack of learning by participants in Experiment 3, it would be useful to have a more thorough analysis and discussion of the differences in performance between the testing and training phase for all of the experiments. It may be worthwhile to use certain learning models (e.g., Q-learning) to characterize learning behavior under the various conditions to better understand the lack of overall learning in Experiment 3 and more generally relationships between performance in the training and testing phases of the experiments.

2) Given the positive findings about memory consolidation, it would also be useful to include a more thorough analysis and discussion of the relationship between task performance and working memory. Are there behavioral patterns in the train/test and on/off conditions that can be related more directly to working memory function (e.g., win-stay/lose-shift)? How does their interpretation relate to other findings that relate dopamine signaling to memory formation? These kinds of results might be interpreted in the context of findings showing projections of midbrain dopamine neurons to the hippocampus and to the surrounding MTL cortices (Samson et al., 1990; Gasbarri et al., 1994) and may contribute to successful binding between experiences separated by time (Cohen and Eichenbaum, 1993; Shohamy and Wagner, 2008). Such binding, mediated by tonic dopamine signals (Niv et al., 2007), begins before the experiences and continues into a temporal window of hours or days (Shohamy and Adcock, 2010). Foerde and Shohamy (2011), in an fMRI study of healthy young adults performing a probabilistic learning task, demonstrated the recruitment of the striatum during learning with immediate feedback, and increased activation of the hippocampus with delayed feedback. Data from the same authors showed that individuals with Parkinson's disease, whose striatum is known to be degraded, were impaired in learning from immediate but not delayed feedback (Foerde and Shohamy, 2011). Conversely, individuals with MTL damage exhibited impaired learning with delayed but not immediate feedback (Foerde et al., 2013).

3) In general, the paper could benefit from a more thorough vetting of the statistical analyses and claims, including:

a) specifying error bars in all of the figures;

b) appropriately interpreting "borderline" significance for the effect of day 1 medication state (also, do non-parametric tests yield the same results?);

c) clarifying (and possibly re-interpreting) the claim that "both day 1 ON conditions (blue bars) increased in memory scores," which is also repeated in the Discussion but seems to run counter to the OnOn data presented in Figure 2 (which does not seem to differ significantly from zero, given the error bars shown);

d) clarifying statements in Results ("The pattern of day 1 ON patients showing more avoid-B than day 1 OFF patients is in the opposite direction to predictions from previous work") and Discussion ("day 1 ON conditions having the highest amount of avoid-B selections") that appear to be contracted by the actual findings ("There were no significant effects of day 1 or day 2 medication state, or any interactions (p >.28). This suggests that […] medication on day 1 or day 2 had no effect.").

4) To effectively compare the results with previous findings, the claim that "our samples were very closely matched in age, gender and disease severity to the PD patients tested ON medication in Frank et al. (2004)" needs to be fleshed out more. What, exactly, were the comparisons? How well did they match, particularly disease severity?

5) It would be useful to include a more thorough discussion of the limitations of the PST task, including what future directions might help either validate the task as an effective way to study mechanisms of reinforcement learning, or point the way to new, more effective task designs.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Effects of dopamine on reinforcement learning and consolidation in Parkinson's disease" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved greatly but there is one remaining issue that needs to be addressed before acceptance, as outlined below:

The Q-learning fits are a welcome addition and do a nice job of showing that, among the models tested, the one that uses learning rates separated for positive and negative reinforcement but not ON versus OFF medication best fit the data. However, the fits also suggest that the model fits the HC data much better than the patient data (substantially lower BIC values). This suggests that HC and PD patients might be using different strategies – a point that should be noted, and its implications discussed.
