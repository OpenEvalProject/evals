# Peer review - Round 1

Editors:
- Brice Bathellier, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66112.sa1](https://doi.org/10.7554/eLife.66112.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This article details a new open source setup and protocol for automated training of mice to a challenging sensory discrimination task. This tool brings a level of automation (no human intervention) never achieved in a context that also allows targeted manipulation brain areas, in a non-invasive manner. Both these aspects and the potential for combined optical imaging will be extremely useful for the neuroscience community.

Decision letter after peer review:

Thank you for submitting your article "Fully autonomous mouse behavioral and optogenetic experiments in home-cage" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Philippe Faure (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

While the referees recognize the solidity of this work, a number of revisions are needed to better highlight its novelties with respect to previous publications on behavior during voluntary head-fixation, to reinforce the description of optogenetic silencing results and to help the reader grasp motivation aspects in this self-initiated behavior.

1. Due to the authors' choice of plotting performance in optogenetics, it is not possible to know if the mice reach chance level during silencing. However, appreciating if the chance level is reached during silencing is important to evaluate if the silencing method leads to complete or partial impairments. The authors should thus also provide plots in which performance during optogenetics is express as the distance to chance level (e.g. 60% correct for a balanced binary task is 10% above chance level). Depending on the outcome of this re-plotting, the author should comment, based on the literature, whether incomplete effects are due to incomplete silencing or due to partial involvement of the target region in the task.

2. The comparison to other methods is important. As it stands, these seem marginal. This should be strengthened. It would be also important to highlight what types of questions, qualitatively, can be answered that are not possible (or difficult) otherwise.

3. The task structure needs to be clarified. The sample period (1.3 sec) is followed by a delay epoch (1.3 sec), an auditory go cue and the response epoch. It is indicated that "Mice were free to respond by licking at any time during the trial, but only the first lick after the 'go' cue were registered as choice". The question is what exactly is a trial ? Is it: (i) a sequence sample-delay – response, with only the first lick taken as a response. That is, 1 head fixation = a trial and is associated with a maximum of 1 water reward (2-3 µL). (ii) a succession of sample-delay -1 response sequences during 30 or 60 sec. That is, 1 head fixation is associated with more than one water reward (2-3 µL). I suspect that the first proposal is the correct one, but this should be clearly stated in the manuscript. Along that line, Figure 3B is confusing. Authors should may be indicate the first lick, the one registered as choice in full color and the additional one as transparent?

4. The authors should provide information about the daily water consumption (2-3 µL per lick number of correct trials per days) and whether it is stable during the protocol. Considering that a mouse drinks about 3-5 mL daily if it weighs more than 30 grams, it would correspond to 2000 correct trials more than 16 h of 30 sec head fixed session, if the above interpretation of a trial is correct.

5. In a paper (Torquet et al. 2018) which describes mouse behavior in an automated T-maze task (left or right to access water versus water + sugar), mice showed a decreased return time after choosing the less-rewarded side. This indicated an increased motivation after a failure, but also the fact that some trial can be associated with low motivation for the reward and engagement in the test just for exploration. Here, the authors showed a distribution of inter-fixation interval, with a long tail. Are these inter-fixation intervals correlated with the success or failure in the last trial which could indicate different motivation depending on the intervals?

6. In the contingency reversals task, do the animals adapted their inter-fixation intervals just after the reversal?

7. The position of the pole with respect to the head (stimulation of the left or right whiskers) is not clearly indicated in the method, information seems to be shown only in Figure 3A. This should be indicated clearly. Along the same lines, on line 498, replace "Photoinhibition of S1" by "Photoinhibition of left S1".

8. The statistics used in the optogenetic experiment is based on bootstrap and unilateral testing (one tail test). It is indicated that "In each round of bootstrap, we replaced the original behavioral dataset with a re-sampled dataset in which we re-sampled with replacement from: (1) mice, (2) sessions performed by each mouse, (3) trials within each session. We then computed the performance change on the re-sampled dataset. Repeating this procedure 10,000 times produced a distribution of performance changes that reflected the behavioral variability." It is not clear what 'sessions' means for "unsupervised optogenetic experiments". It is not clear why there are replacements from mice in the bootstrap method. Optogenetic experiment allow quantifying effect at the level of individuals: Test should be paired test and authors have to estimate individual distribution of performance changes under the null hypothesis. Finally, the authors used a unilateral test. This is fine, but the hypothesis should then be clearly stated. It is clearly expected that photo-stimulation of left S1 will reduce performance (with stimulation of the right whisker). The justification for a unilateral should be better justified for the other regions, and in particular the subcortical regions. The sentence l.560 "We next tested if the striatal optogenetic manipulation was sufficient to bias behavior" does not correspond to an unilateral test.

9. Finally, to obtain a proper control group, it is certainly better to use a control-AAV instead of no AAV. Could it be mentioned?
