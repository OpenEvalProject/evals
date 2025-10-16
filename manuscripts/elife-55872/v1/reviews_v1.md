# Peer review - Round 1

Editors:
- Kunlin Wei, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55872.sa1](https://doi.org/10.7554/eLife.55872.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How variability in motor actions changes with learning is not well understood, and the area is waiting for advances in both computational theorization and related neural underpinnings. The present study contributes by investigating a motor timing task in which reward-dependent learning and timing variability interact. Importantly, the observed behavioral signatures enable new modeling of motor reinforcement learning and characterizing the underlying neural substrate in the cortico-basal ganglia circuit.

Decision letter after peer review:

Thank you for submitting your article "Reinforcement regulates timing variability in thalamus" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Kunlin Wei as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bruno B Averbeck (Reviewer #2).

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments/analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

How variability in motor actions changes with learning is not well understood. The present study starts off with a motor timing task where monkeys and human participants were required to produce timing intervals on the scale of hundreds of milliseconds. Two behavioral features emerge: one is strong correlations of timing produced intervals within effectors and intervals, the other is increased timing variability when the produced intervals were away from the target or mean interval. The first feature is interpreted as a slow drift of timing memory, and the second feature is interpreted as from strategic use of exploratory variance to guard against undesirable variability, i.e., the memory drift. The study provided a computational model to incorporate continuous rewards in the framework of reinforcement learning. Furthermore, the study also correlated the direct recording from the thalamus, DMFC, and caudate to the two behavioral findings, and found that the thalamus showed reward-dependent neural activities with clear effector-specificity. The authors conclude that the nervous system strategically regulates the variability based on reinforcement to reduce the detrimental effect of undesirable variability in the system in the exploration-exploitation framework.

There was agreement among the reviewers that these results will be of interest to the audience of eLife. However, there are critical issues that need to be addressed before the paper being considered for acceptance. The first major concern is essential, given that it is about whether the current data can be interpreted as the way it is.

Essential revisions:

1) The main message of the paper is to explain the non-stationarity in the timing variance in the exploration-exploitation framework, but this is questionable. As the reward follows a specific function of timing error, the first derivative of the reward feedback could effectively guide the trial-by-trial modulation of timing behaviors. For example, a decrease in reward would signal a departure from the target interval, which can be used to guide an appropriate response in the next trial. In this case, there is no need to crank up noise with a decrease in reward, as the exploration-exploitation framework would predict. Thus, the observed changes in variance can be explained by trial-by-trial learning based on the explicit reinforcement feedback signal, without invoking the idea of random exploration as in the exploration-exploitation framework. Recent theoretical approaches to model exploration-exploitation behaviors have emphasized both random vs. directed exploration (Wilson et al., 2014), but the current study appears to assume that all exploration should be random. Considering that the task has a 1-D continuous reward function, directed exploration is well possible. This is a critical question given that the main implication of the study is about "…the nervous system makes strategic use of exploratory variance…". In fact, the whole paper is framed as probing reinforcement-guided exploration as opposed to trial-by-trial supervised learning.

In a similar vein, the non-stationarity in the variance is caused by the reward magnitude (the specific reward function used here), not necessarily a refutation of stationarity of interval time. It has been acknowledged by the author that this is not a rejection of the interval timing model, but the paper continues to imply it in the Abstract and in the Results.

Did the subjects not use information from the first derivative of the reward to update their produced intervals? It is not even clear that how many produced intervals fell within the rewarded range, and how many were simply unrewarded. The details of the reward magnitude and the monkey's behavioural adaptations to these changes in reward need to be clarified. To make the original claims of the paper hold, the authors need to clarify whether the results can be explained by simple trial-by-trial adjustments based on the first derivative of the reward function.

2) The human task with a probabilistic reward has not been directly compared with the monkey experiment, though both are displayed in Figure 5. Related to question 1), can the findings with probabilistic rewards suffice to rule out the possibility that the first derivative of reward feedback is the driving force for the observed variance changes?

3) The asymmetry of interval variance was evident for both monkeys when the target interval of 1500ms was produced (Figure 1D), but it was left unexplained. This asymmetry shows a much higher variance for the shorter intervals, i.e., skewed to the 800ms target interval. Was this caused by a trivial fact that the monkeys were producing the wrong interval? The data from Monkey D (Figure 1B) appear to suggest this is possible (a few intermediate intervals with the 1500ms target interval). This can be further verified by raw data from Monkey A, which is currently absent in Figure 1. Furthermore, if you use decoding on the neural activity, can you predict whether the monkeys are indeed trying to produce long intervals, in the trials in which they produce long intervals that are too short?

4) Figure 8—figure supplement 6 shows that speed variability differed between rewarded and unrewarded trials for DMPC and caudate, but not for the thalamus. Does this contradict the implied role of the thalamus in reinforcement learning?

5) The study highlights the role of the thalamus in reward-based learning; recent studies have hypothesized that fronto-thalamic circuits are necessary for quick processing of complex task-relevant information. Given the task investigated here is also complex (associating reward size to task performance across trials), it is well possible that several areas of frontal cortex are also involved. How to link the current findings to the hypotheses of fronto-thalamic circuits?
