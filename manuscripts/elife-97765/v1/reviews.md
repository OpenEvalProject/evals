# Peer review - Round 1

Editors:
- Maria Chait, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97765.3.sa0](https://doi.org/10.7554/eLife.97765.3.sa0)

In this valuable study, Li et al., set out to understand the mechanisms of audiovisual temporal recalibration - the brain's ability to adjust to the latency differences that emerge due to different (distance-dependent) transduction latencies of auditory and visual signals - through psychophysical measurements and modeling. The analysis and specification of a formal model for this process provide convincing evidence to support a role for causal inference in recalibration.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97765.3.sa1](https://doi.org/10.7554/eLife.97765.3.sa1)

This study asks whether the phenomenon of crossmodal temporal recalibration, i.e. the adjustment of time perception by consistent temporal mismatches across the senses, can be explained by the concept of multisensory causal inference. In particular they ask whether the explanation offered by causal inference better explains temporal recalibration better than a model assuming that crossmodal stimuli are always integrated, regardless of how discrepant they are.

The study is motivated by previous work in the spatial domain, where it has been shown consistently across studies that the use of crossmodal spatial information is explained by the concept of multisensory causal inference. It is also motivated by the observation that the behavioral data showcasing temporal recalibration feature nonlinearities that, by their nature, cannot be explained by a fixed integration model (sometimes also called mandatory fusion).

To probe this the authors implemented a sophisticated experiment that probed temporal recalibration in several sessions. They then fit the data using the two classes of candidate models and rely model criteria to provide evidence for their conclusion. The study is sophisticated, conceptually and technically state-of-the-art and theoretically grounded. The data clearly support the authors conclusions.

I find the conceptual advance somewhat limited. First, by design the fixed integration model cannot explain data with a nonlinear dependency on multisensory discrepancy, as already explained in many studies on spatial multisensory perception. Hence, it is not surprising that the causal inference model better fits the data. Second, and again similar to studies on spatial paradigms, the causal inference model fails to predict the behavioral data for large discrepancies. The model predictions in Figure 5 show the (expected) vanishing recalibration for large delta, while the behavioral data don't' decay to zero. Either the range of tested SOAs is too small to show that both the model and data converge to the same vanishing effect at large SOAs, or the model's formula is not the best for explaining the data. Again, the studies using spatial paradigms have the same problem, but in my view this poses the most interesting question here.

In my view there is nothing generally wrong with the study, it does extend the 'known' to another type of paradigm. However, it covers little new ground on the conceptual side.

On that note, the small sample size of n=10 is likely not an issue, but still it is on the very low end for this type of study.

Comments on revision:

The revision has addressed most of these points and makes for a much stronger contribution. The issue of sample size remains.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97765.3.sa2](https://doi.org/10.7554/eLife.97765.3.sa2)

Summary:

Li et al.'s goal is to understand the mechanisms of audiovisual temporal recalibration. This is an interesting challenge that the brain readily solves in order to compensate for real-world latency differences in the time of arrival of audio/visual signals. To do this they perform a 3-phase recalibration experiment on 9 observers that involves a temporal order judgment (TOJ) pretest and posttest (in which observers are required to judge whether an auditory and visual stimulus were coincident, auditory leading or visual leading) and a conditioning phase in which participants are exposed to a sequence of AV stimuli with a particular temporal disparity. Participants are required to monitor both streams of information for infrequent oddballs, before being tested again in the TOJ, although this time there are 3 conditioning trials for every 1 TOJ trial. Like many previous studies, they demonstrate that conditioning stimuli shift the point of subjective simultaneity (pss) in the direction of the exposure sequence.

These shifts are modest - maxing out at around -50 ms for auditory leading sequences and slightly less than that for visual leading sequences. Similar effects are observed even for the longest offsets where it seems unlikely listeners would perceive the stimuli as synchronous (and therefore under a causal inference model you might intuitively expect no recalibration, and indeed simulations in Figure 5 seem to predict exactly that which isn't what most of their human observers did). Overall I think their data contribute evidence that a causal inference step is likely included within the process of recalibration.

Strengths:

The manuscript performs comprehensive testing over 9 days and 100s of trials and accompanies this with mathematical models to explain the data. The paper is reasonably clearly written and the data appear to support the conclusions.

Comments on revision:

In the revised manuscript the authors incorporate an alternative model (the asynchrony contingent model), and demonstrate that the causal inference model still out performs this. They provide additional analysis with Bayes factors to perform model comparisons, and provide significant individual subject data in the supplementary materials. Overall they have addressed most of the key points that my original review raised, including a demonstration of the conditions under which recalibration effects do not delay to zero over long delays. The number of subjects remains rather low, but at least we can now appreciate the heterogeneity within them. I still have some reservations about the magnitude of the conceptual advance that this study makes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97765.3.sa3](https://doi.org/10.7554/eLife.97765.3.sa3)

Summary:

Li et al. describe an audiovisual temporal recalibration experiment in which participants perform baseline sessions of ternary order judgments about audiovisual stimulus pairs with various stimulus-onset asynchronies (SOAs). These are followed by adaptation at several adapting SOAs (each on a different day), followed by post-adaptation sessions to assess changes in psychometric functions. The key novelty is the formal specification and application/fit of a causal-inference model for the perception of relative timing, providing simulated predictions for the complete set of psychometric functions both pre and post adaptation.

Strengths:

(1) Formal models are preferable to vague theoretical statements about a process, and prior to this work, certain accounts of temporal recalibration (specifically those that do not rely on a population code) had only qualitative theoretical statements to explain how/why the magnitude of recalibration changes non-linearly with the stimulus-onset asynchrony of the adaptor.

(2) The experiment is appropriate, the methods are well described, and the average model prediction is a good match to the average data (Figure 4). Conclusions are supported by the data and modelling.

(3) The work should be impactful. There seems a good chance that this will become the go-to modelling framework for those exploring non population-code accounts of temporal recalibration (or comparing them with population-code accounts).

(4) Key issues for the generality of the model, such as recalibration asymmetries reported by other authors that are inconsistent with those reported here, are thoughtfully discussed.

Weaknesses:

(1) Models are not compared using a gold-standard measure such as leave-one-out cross validation. However, this is legitimate given lengthy model fitting times, and a sensible approximation is presented.

(2) The model misses in a systematic way for the psychometric functions of some participants/conditions. In addition to misses relating to occasional failures to estimate the magnitude of recalibration, some of the misses are because all functions are only permitted to shift in central tendency (whereas some participants show changes better characterized at one or both decision criteria). Given the fact that the modelling in general embraces individual differences, it might have been worth allowing different kinds of change for different participants. However, this is not really critical for the central concern (changes in the magnitude of recalibration for different adaptors) and there is a limit to how much can be done along these lines without making the model too flexible to test.

(3) As a minor point, the model relies on simulation, which may limit its take-up/application by others in the field (although open access code will be provided).
