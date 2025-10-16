# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54014.sa1](https://doi.org/10.7554/eLife.54014.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Phasic arousal suppresses biases in mice and humans across domains of decision-making" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Marcus Grüschow (Reviewer #1); R Becket Ebitz (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study builds on a previous eLife paper ("Dynamic modulation of decision biases by brainstem arousal systems") that showing that phasic pupil responses predict reduced conservative accumulation biases in humans performing perceptual tasks. Here the authors show that the biases: 1) are reduced in both directions (liberal/conservative), 2) are comparable in both mice and humans, and 3) occur in both in memory-based and perceptual decisions There was general agreement that the new work is a useful and substantial extension of the previous work.

Essential revisions:

1) There is a consistent conflation of measured correlations/predictions with what seem to be much stronger claims about causality; e.g., in the title, along with many places in the text, that claim that "phasic arousal suppresses…" (or "reduces", "affected", etc). These points should be disentangled and clarified.

2) Several questions/concerns were noted regarding the DDM fits. In particular:

a) It seems that the core feature captured by the accumulation bias term in the DDM (the growing bias with longer RTs) might also be explained by a starting point bias in combination with an urgency signal (e.g., as bounds decay, the relative bias in the starting point becomes more and more important). Are the authors making a strong claim about the exact process model that they have chosen? And if so, could they rule out the alternative model above using model comparison?

b) Popular theories of arousal and decision-making argue that the role of enhanced arousal is to enhance the representation of task-relevant variables (Mather GANE), which would seem to argue for an enhanced drift rate under high arousal. It would thus be important to provide the model comparison (BIC, DIC) between the DDM provided by the authors and a model that does not contain the additive bias term, possibly with a fixed or variable starting point. To be more precise, traditionally, in the sequential sampling framework, response biases have been modeled as a shift in starting point. If one claims that response biases are implemented as a "drift criterion", it would be good to explicitly show that this is a better model of the data. Mulder et al., 2012 (JoN, their Figure 2) present a qualitative distinctive test for these two models: if the choice bias is implemented as a drift rate bias, the response time patterns for validly/invalidly biased trials should be the same for correct and incorrect responses. However, if the choice bias is implemented as a starting point bias, there should be opposite effect for correct and incorrect trials: for correct trials, invalidly biased trials should be slower than validly biased trials, whereas for incorrect trials, this pattern should reverse: invalidly biased trials should be *faster* than validly biased trials. Could the authors plot the averaged (over subjects) median response times of correct/incorrect x validly/invalidly biased trials for their second experiment, where subjects are biased due to the probabilistic nature of the environment, just as in Figure 2 of Mulder et al., 2012? Furthermore, for all experiments where there are two choice options (so not the go/no-go tasks, where the DDM is under-constrained), could they formally compare (a) a model where only starting point is allowed to implement response biases, (b) a model where only drift criterion is allowed to implement the response biases, and (c) a model where both starting point and drift criterion are allowed to implement the response biases?

3) Given that phasic pupil changes are sensitive to baseline pupil diameter, it would be useful to have more information about the statement "Variation in pre-trial pupil size causes floor and ceiling effects on phasic dilations, shaped by light conditions.” What exactly do the authors mean here? Where do the differential light conditions come from in auditory detection tasks? Moreover, how did you account for pre-trial spill-over effects on pupil; e.g., pre-trial-difficulty (loudness), response (yes/no), pupil dilation/derivative, tonic level, etc.

4) The choice of pupil change measure differs across tasks, due to differences in motor demands. However, every task has a stimulus onset and it does look like there were substantive differences in the stimulus-aligned pupil responses in all three experiments. It would be helpful to know if stimulus-aligned pupil responses are predictive in experiments 2 and 3. Our sense is that the attentional literature would likely predict changes in stimulus-aligned pupil responses, rather than motor aligned (and probably in stimulus-aligned dilation for auditory stimuli and stimulus-aligned constriction for visual stimuli).

Relatedly, many studies have looked at the relationship between stimulus attention and the transient pupil response to both visual and auditory stimuli, in both humans and non-human primates (in whom some mechanistic work has been done). This literature is not discussed here, which is striking given that it would seem that some of the results reported here explained by a decrease in attention paid to sensory evidence and previous studies have shown that attention can scale DDM drift.

5) We admire the combination of mice and men in this work however, the entire manuscript features only 5 mice in the first experiment. We believe it would be beneficial if the authors could justify this small sample size for other non-animal researchers.

6) It would be useful validate that the measure of bias in Figure 1 is not sensitive to the number of trials in each loudness condition, as this will clearly differ across pupil bins. We are not sure about the total number of trials in some of the loudness conditions, but we worry a bit that if there are very few trials in a given loudness condition, the measure could be misleading.

7) It would be useful to flesh out in a bit more detail why the observation of non-linear vs. linear arousal state modulation would indicate distinct functional roles for tonic vs. phasic arousal respectively. First, a linear relationship could just represent the increasing part of the inverted u-shape and secondly the original cited papers by Aston-Jones and Cohen, 2005; Yerkes and Dodson, 1908, used pupil size, while I believe the current work focuses on the speed of dilation. It would be important to clarify as to how these measures are related or how they may reflect activity of distinct neuromodulators or modulatory receptors as the authors pointed out in the final paragraph of subsection “In humans and mice, phasic arousal tracks a reduction of choice bias in an auditory detection task”.

8) The authors argue that experiment 3 shows reduced sampling from memory, but the idea that mnemonic decisions are based on samples from memory is still an early theory. Further, to our knowledge we don't know that the DDM does recover information about this memory sampling process (i.e. we do not know whether DDM drift biases reflect sampling from memory, sampling from the stimulus, or some other time-varying decisional process like response competition). It would be helpful to be more circumscribed in the interpretation of these results as reflecting a change in sampling from memory.

9) What distribution was used to determine the length of mini-blocks? The Materials and methods say that miniblocks were never more than 7 trials, which suggests that the hazard rate for a signal trial was not constant across the miniblock. Also, the hazard rate for the reference trial is presumably zero, were these trials included in analysis? Elsewhere the authors note that the hazard for signal trials was kept approximately flat. How approximately? Were phasic pupil responses related to changes in hazard across miniblocks?
