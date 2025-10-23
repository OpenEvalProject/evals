# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65495.sa0](https://doi.org/10.7554/eLife.65495.sa0)

This study investigates the question of whether distinct brain areas differentially encode time during the learning of a simple motor timing task. The key novel result is that early in training the dynamics of the medial prefrontal cortex provides the best code for time, but later in training the striatum provides a better code. In addition, the article reports that the inactivation of medial prefrontal cortex produces a delayed learning effect, while the inactivation of the striatum after learning led to impairment of performance. Thus, the observation that temporal coding and the necessity of brain area for task performance transfers from medial prefrontal cortex to the striatum during learning is an important observation for the field.


---

# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65495.sa1](https://doi.org/10.7554/eLife.65495.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Time-Encoding Migrates from Prefrontal Cortex to Dorsal Striatum During Learning of a Self-Timed Response Duration Task" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Hugo Merchant as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen Richard Ivry as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

We have also prepared an Evaluation Summary and Public Reviews of your work below, which are designed to transform your manuscript into a preprint with peer reviews.

Essential revisions:

We have the following recommendations about the data set and methods in order to critically evaluate the robustness of their results.

1) Decoding analysis.

a. Please report the number of units recorded in each animal/session. All statistics were performed on data resulting from a decoder applied to neural data, and thus the degrees of freedom reflected in the reported F statistics of their ANOVAs would appear to correspond to folds in a cross validation procedure. It would be important to know more precisely how the differences in decodability of certain variables relates to the number of units recorded.

b. All analyses of neural data are performed on data pooled across animals. This makes it difficult to determine whether the effects they observe are consistent across animals. The authors are attempting to analyze data from single sessions, and thus they may have small amounts of data from single animals. In the present form it is difficult to critically evaluate the consistency and robustness of their observations. Within-animal analyses would go a long way towards resolving this issue.

c. In Figure 3 the statistical analyses shows highly significant group effects and an interaction (F(1,99) = 374). But the stats seem to be done on a per trial basis? If this is the case it is not clear to me if this is correct, as opposed to relying on the mean correlation across trials for each animal? Perhaps the authors did it this way because they collapsed neurons across animals? Either way it is necessary to clarify theses analyses and perhaps perform additional analyses depending on the answer to the questions above.

d. Given that the authors are highlighting changes in decodability within a session, it is important to assess that recording quality was constant over the session, for example determining whether they observed non-stationarity in firing rates during the sessions and/or changes in spike waveform shape. Ideally this would be applied to baseline activity outside of a trial. Indeed, more information about steps taken to guarantee good unit isolation would be useful.

e. It seems that both areas encode the beginning and end of the trials, with high densities in the diagonal only on the initial and final bins (Figure 3B and E), rather than the elapsed time across all the trials. These results could be related with learning of non-temporal factors discussed below.

f. The decoding of elapsed time both areas went down from early to late trials in the experiment of one session (Figure 3C and D), supporting the notion that the striatum does not take over, although the rats learned to time the interval (Figure 1B and C). Which potential brain areas are involved in this short learning process then?

2) Learning Process. It is difficult to dissociate the role of mPFC and the striatum linked with a better representation of elapsed time with learning from the operational learning aspects of the task. The latter include the increase in attention of sensory inputs associated with the nosepoke, an increase in precision of movement kinematics (less body and face movements during the nose poke), and a more developed reward expectation from learning to time the 1.5 s. The authors should perform careful analysis to try to dissociate the learning of temporal and non-temporal factors and the involvement of the two areas.

Recommendations for the authors.

1) How did the authors define "early" and "late" periods of sessions? I may have missed it, but I could not find this information in the paper. I assume also that "early" and "late" correspond to the "moment" factor that they include in their statistical tests. Relatedly, it would be useful to define clearly in Figure 1B the division between early and late trials.

2) It was not clear how the climbing activity was quantified, and what the N values on lines 63-63 mean (and why the units seem to be in seconds?).

3) The striatum shows an increase in decoding on the second day experiment, is this an effect of the total number of trials executed by the animals? Which brain areas could be linked to the one day learning of 1.5 timing then?

4) The unimodal distributions in Figure 1B are replaced by bimodal distributions in Figure 4C. Is this an effect of changing the effector from nosepoke to lever press?

5) Figure 2 rasters are fine, but PSTHs seem to be a bit misleading… PSTH heights drop towards the center of the plots because there are fewer and fewer trials with data in those bins. Avg sp/s should be normalised based on the number of trials with data in each bin.

6) What is the relation between early decoding of session 2 and the late decoding of session 1? In the behavior there is a clear carry over of learning (Figure 1C).

7) The split positive/negative time axes in Figure 2C-J need to be explained better.

8) Please report the posterior probabilities of decoded times, are they above chance level?

Is the decoding more accurate with SVMs than the used Linear Discriminant Analysis?

9) Please perform the decoding on incorrect trials below 1.5 seconds. Are the results different from those reported in Figure 3?

10) Figures 3C,D and F should have the same scale.

11) Please state why the physiology and pharmacology experiments were performed in different behavioral boxes, employing nose port withdrawal or lever press as an operant response, respectively.

12) Mu2 and Sigma2 can be the behavioral fingerprints for time accuracy and precision. Is peculiar the animals become more accurate on timing 1.5s but not more precise with training. Please discuss.

13) All the literature cited on timing neurophysiology is on the rodent. Some references on non-human primates should be included.

14) The general observation that task-dependence shifts from cortex to striatum over learning would seem to be consistent with a series of studies from the laboratory of Bence Olveczky starting with Kawai et al. Neuron, 2015. Though they focus more on motor cortex, these studies should probably be cited.

15) Overall, the methods would benefit from a careful screen through the manuscript to make sure that any approaches and terms used in the paper are clearly defined in the methods.

16) The authors are using "moment" to refer to the early and late stages of training within a session. This is a bit confusing; I might recommend just using "stage".

17) The first sentences of the Discussion are a bit confusing … "previously reported" will make it clearer.
