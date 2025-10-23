# Peer review - Round 1

Editors:
- Floris de Lange, Donders Institute for Brain, Cognition and Behaviour Netherlands

Reviewers:
- Floris de Lange, Donders Institute for Brain, Cognition and Behaviour Netherlands
- Tristan A Bekinschtein, University of Cambridge United Kingdom

## Review text

DOI: [10.7554/eLife.43410.019](https://doi.org/10.7554/eLife.43410.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neural basis of somatosensory target detection in humans." for consideration by eLife. Your article has been reviewed by two peer reviewers, including Floris de Lange as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tristan A Bekinschtein (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors examine the neural correlates of somatosensory target detection, by applying median nerve stimulation electrical pulses of varying strength to human volunteers (N=27). They go beyond earlier investigations of sensory awareness by controlling for several factors that are associated with sensory awareness, i.e. stimulus uncertainty, behavioral relevance, overt reporting and motor responding. They observe that neural responses that can be specifically linked to target detection reside in secondary somatosensory cortex (SII), arguing for a specific role of sensory systems in generating awareness (instead of a broadcasting signal in fronto-parietal cortex). This is a well motivated, well executed and well written piece on a topic of general interest. It is notoriously difficult to disentangle awareness-related activity modulations from its precursors and consequences. I believe the authors have brought this quest a step further, by controlling for several relevant 'confounding factors' and using Bayesian Model Selection in an attempt to disentangle the respective contributions of several factors to the activity profile of sensory and non-sensory regions.

Essential revisions:

1) Anatomical localization of effects

The neural locus of intensity, P(detection) and detection effects are sometimes incredibly close to each other. There is no mention of the smoothing kernel of the fMRI data (please add!), but this does raise the question of what causes the regions of shared variance (intermixed colors). Are they really sensitive to all these effects, or is the intermixing the result of spatial and/or normalization-induced smoothing?

2) Smooth transformation from sensation to perception

The authors argue that there is a smooth transformation from physical to perceptual representation in the somatosensory system. It would be nice if this could be better visualized, and more formally tested – for example by testing whether peak anatomical coordinates for the different task components have a monotonic progression on the posterior-anterior axis.

3) The title seems a bit general, it read like a review title, please consider some version more accurate that maybe reflects this experiment analysis, and conclusions?

4) Several possible confounding factors were raised that should be at least discussed further, or possibly included in new analyses:

a) Perception of near threshold stimuli is difficult, and resolution of associated uncertainty and introspective processes may differ between detected and undetected targets (de Lafuente and Romo, 2011). How might this affect the interpretation of your results?

b) Target detection is the explicit behavioural goal of the task and therefore, detected targets have higher behavioural relevance than undetected targets (Farooqui and Manly, 2018). How might this affect the interpretation of your results?

c) Target detection is directly mapped to overt reports that allow for assessment of participants' trial-by-trial perception (Tsuchiya, Wilke, Frässle, and Lamme, 2015). Can this be teased apart from a possibly covert perceptual process?

d) Overt reports are often communicated with button presses by one hand while stimulation occurs on the other hand, which may affect cortical excitability in homologue regions of the sensorimotor homunculus (Zagha, Casale, Sachdev, McGinley, and McCormick, 2013).

5) Subsection “Behaviour”, the last phrase "Chi squared tests of independence showed no association of target detection with overt reports for any of the participants (all p > .2), confirming that our task design rendered these variables independent."

In the manner I interpret it seems that the authors are assuming that a lack of significance in the test is evidence for a no association, please either rephrase to say the test did not show enough evidence for an association or that there were not significantly associated; alternatively, run an appropriate test pointing to evidence for the null effect (enough evidence of no association) like a bayes factor.

6) In the subsection “fMRI”, I am happy to see that the activity after the BMS is not enough for the authors to claim neural association, they are also demanding fit to the each model (dichotomous, sigmoideal). In this respect they say: "The lack of such a relationship may suggest that the detection-related response that drives the model fit in these regions does not constitute an all-or-nothing response to target detection but may be restricted to only a subset of trials (see Discussion)". I thought that maybe it was also restricted to a subset of participants. I was thinking in asking if they author could provide of an impression of each subject fit and variability in the fMRI data. I am curious to understand the contribution of the participants to these interesting results and one way to do it is to plot single subject parameters. Would the authors be happy to think of a manner to show the direction and strength of effect per participant for the main results? I understand this may seem like a lot of work, it shouldn't. The fitting parameters per participant are easy to extract and the so are the bold estimates. This would allow for a good understanding of the variability of the 27 and also for the contributions each make.

Uncertainty here is not formal report uncertainty (subjective measure of uncertainty) but a toy model of expected uncertainty, it would be good for the authors to comment and give some details on this. Which concept of uncertainty do they refer to, some closer to the objective aspect of detection or closer to a metacognitive evaluation? I know it is defined later in the Discussion but a short account early on would help. Thanks.

Figure 5 legend, at the end the authors refer again to a lack of effect as "confirming that overt reports were independent of stimulus intensity and target detection." I actually like the result but I am also aware of the language vs. the test. Does the test perform confirms or give evidence for a no effect? It is truly independence or it is a lack of dependence? Apologies if I start to sound like the stats pedant.

7) On the topic of "Considering that interoceptive signals, such as the heartbeat, are often faint signals, it would be interesting to see how explicit control of perceptual uncertainty might affect these interpretations." Some year ago we also investigated the role of the insula in faint signals (heartbeat, Canales-Johnson et al., 2015), and found that both in SI and SII but more importantly in insula, the performance modulated the signal, but not the -subjective- impression of improvement. This is not to ask the authors to cite this piece, it is only to show the complexity of the interoceptive argument. There are many papers tapping into the heartbeat as a faint sensory signal, this is mainly because it might be that it is in fact not interoception but a secondary feeling on the heart pounding in the chest or the blood in the neck, ears, etc.

8) Discussion, seventh paragraph, maybe it does not capture any frontal or parietal cortex because the stimuli is so simple? I know this is borderline on strawman but it might be that the simple zap on the skin creates very little demand for detection and hence we are under-powered to capture the extent of the network involve as the demands are too little? This is just food for thought, not a really strong view that I hold. It is always difficult with these faint stimuli, and with detection task in general. I have not forgotten that the experimental design here is elegant and partially controls for this possible critique… It is in fact commented by the end of the Discussion.
