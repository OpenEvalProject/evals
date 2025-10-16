# Peer review - Round 1

Editors:
- Jun Ding, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72549.sa0](https://doi.org/10.7554/eLife.72549.sa0)

Using advanced live brain imaging techniques, the authors studied the activities of neurons in the primary motor cortex of mice during a classical conditional task, in which a tone is paired with a water reward. They found that distinct types of neurons respond differently to the auditory cue or the reward, and the responses evolve differentially as learning proceeds. This work reveals an interesting role of the motor cortex beyond its well-recognized function in motor control and suggests distinct functions of pyramidal neurons as well as various interneurons in reinforcement learning.


---

# Peer review - Round 1

Editors:
- Jun Ding, https://ror.org/00f54p054 Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72549.sa1](https://doi.org/10.7554/eLife.72549.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cell-Type Specific Responses to Associative Learning in the Primary Motor Cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jerry L Chen (Reviewer #1); Hyung-Bae Kwon (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewers think that additional control experiments are needed for the revision. In addition, additional data analysis and clarification are needed to strengthen the paper. The following are essential revisions:

1. To address the question of whether changes are specifically associated with learning, a critical control experiment is missing. The behavioral study lacks a non-paired control – it would be more compelling if there was a CS of the same modality that was not paired with the US so we can be sure that the effects are not cue-specific but specific to conditioning. Then those cues would need to be counterbalanced across animals. This would be important for us to conclude the neural effects reflect associative learning vs some other impact of the cue over time.

2. Please examine the motor-related activity in the data set and address the following questions raised by Reviewer #1 and Reviewer #2, (a) As a control, can you quantify the number of licking-related neurons across cell types and confirm that they do not change with learning? (b) Are there neurons that show mixed responses to cue and licking? Do those responses change at all during learning? (c) Are there neurons show mixed responses to licking and reward? Do those responses change at all during learning?

3. The 2.5s period chosen for analysis covers both tone presentation and delay. Will the conclusions in Figure 2E-H change if the analysis is restricted to the 1s of tone presentation? In addition, it seems better to use the actual duration of reward presentation (see Q2) for analysis. As the statistical analysis is done by random shuffling, there seems no need to match the period for tone and reward analyses.

4. In Activity Analysis and Tuning Coefficients Calculation, the authors performed a resampling of mice with replacement, and the size of the random sample equals that of the original set of mice. Please clarify why this is done this way. Can the authors simply take all mice into analysis?

5. Both Reviewer #2 and Reviewer #3 pointed out the importance of plotting calcium signals over days without resorting. The authors conclude that "PV-INs that began as highly reliable maintained their reliability to the CS, …, while PV-INs that began as low reliability became significantly more reliable." However, Figure 4F only shows how the percentage of neurons in the high- or low-reliability category changes overtraining. To draw this conclusion, the authors need to track individual neurons and compare the same neuron's reliability on d1 and d7.

Reviewer #1 (Recommendations for the authors):

I would encourage the authors to examine the motor-related activity in their data set, to help shed light on the following questions. Do the cue and reward related changes really reflect local circuit changes as the authors seem to suggest? Or could they potentially reflect changes outside of M1 that are then inherited and readout by M1 cell type? If local circuit changes are occur, one might expect to see changes in the conjunctive responses of cue, reward, and motor activity within individual cells. Changes in network activity between cue, reward, and motor cells may also be observed. It should be possible and worth examining these relationships to tease apart potential mechanisms and impact of non-motor changes in M1.

Reviewer #2 (Recommendations for the authors):

1. It is helpful to provide further details about the genetic background of the transgenic animals. Are they homozygous or heterozygous? What genetic background are they maintained in? Also, it would be helpful to indicate the number of neurons imaged per mouse.

2. A question about the behavioral setup. How long is the water reward presented? How many licks does it take the mouse to consume the 10 ul water reward? It seems from Figure 1B that most licks occur when water is no longer available. Also, the example in Figure 2C suggests that post-cue licking is far fewer on d7 than on d1, suggesting that the mouse has learned to inhibit non-rewarded licking. This seems not to agree with Figure 1C.

3. As imaging is conducted in M1, how is the response of the cells related to licking? Can the authors make a licking-triggered average of Ca traces for comparison?

4. In Figure 2B: is the scale bar 10% or 10, i.e., 1000%? Many transients show a very slow onset, which is not consistent with the rapid rising phase of GCaMP6f signals as shown in many previous publications. Also, previous publications show that PV and SOM interneurons have very synchronized activity in mPFC (Pinto and Dan, 2015 Neuron) and secondary motor cortex (Garcia-Junco-Clemente et al., 2019 Cell Report). Is it true in M1? Can the authors give some examples of Ca traces of each type of the interneurons? If Ca transients in M1 interneurons exhibit different kinetics from those in pyramidal neurons, how would that affect the choice of analysis criteria?

5. The 2.5s period chosen for analysis covers both tone presentation and delay. Will the conclusions in Figure 2E-H change if the analysis is restricted to the 1s of tone presentation? In addition, it seems better to use the actual duration of reward presentation (see Q2) for analysis. As the statistical analysis is done by random shuffling, there seems no need to match the period for tone and reward analyses.

6. In Activity Analysis and Tuning Coefficients Calculation, the authors performed a resampling of mice with replacement, and the size of the random sample equals that of the original set of mice. What is the reason to do this? Can the authors simply take all mice into analysis?

7. Figure 3A-B: a little clarification is needed. (1) Is each trace a single trial or the average over trials? (2) What does it mean that "each trace is from the same neuron on d7?" Are the five traces from one neuron, or five neurons? If they are from five neurons, are these the same five neurons in A and B? (3) Why does the color of a single trace change with time?

8. The authors conclude that "PV-INs that began as highly reliable maintained their reliability to the CS, …, while PV-INs that began as low reliability became significantly more reliable." However, Figure 4F only shows how the percentage of neurons in the high- or low-reliability category changes over training. The authors need to track individual neurons and compare the same neuron's reliability on d1 and d7 to draw this conclusion. The same issue applies to the analysis of all cell types.

Reviewer #3 (Recommendations for the authors):

First of all, the work is great. Analyzing calcium activity from each interneuron cell type is quite difficult, but authors elegantly performed the experiments. I wonder whether you can plot calcium signals over days (day 1 to day 7) without resorting. I understand it is very difficult, but if you have a good imaging quality enough to trace calcium activity from the same cells over several days, it would be nicer to show. Another concern is the lack of control experiments that show no such changes presented in training groups. Otherwise, it is quite good.
