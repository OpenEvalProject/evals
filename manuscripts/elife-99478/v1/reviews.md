# Peer review - Round 1

Editors:
- Peter Kok, https://ror.org/02jx3x895 University College London London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99478.3.sa0](https://doi.org/10.7554/eLife.99478.3.sa0)

This study reveals a neural signature of a common behavioural phenomenon: serial dependence, whereby estimates of a visual feature (here motion direction) are attracted towards the recent history of encoded and reported stimuli. The study provides solid evidence that this phenomenon arises primarily during working memory maintenance. The pervasiveness of serial dependencies across modalities and species makes these findings important for researchers interested in perceptual decision-making across subfields.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99478.3.sa1](https://doi.org/10.7554/eLife.99478.3.sa1)

This study uses MEG to test for a neural signature of the trial history effect known as 'serial dependence.' This is a behavioral phenomenon whereby stimuli are judged to be more similar than they really are, in feature space, to stimuli that were relevant in the recent past (i.e., the preceding trials). This attractive bias is prevalent across stimulus classes and modalities, but a neural source has been elusive. This topic has generated great interest in recent years, and I believe this study makes a unique contribution to the field.

Specifically, while previous neuroimaging studies have found apparent reactivations of previous information, or repulsive biases that may indirectly relate to serial dependence, here Fischer at al. find an attractive bias in neural activity patterns that aligns with the direction of the behavioral effect. Moreover, the data show that the bias emerges later in a trial, after perceptual encoding, which speaks to an ongoing debate about whether such biases are perceptual or decisional.

The revised preprint thoroughly addresses many of the initial concerns, but the results are still open to interpretation. For instance, the model training/testing regime allows that some training data timepoints may be inherently noisier than others (e.g., delay period more so than encoding), and potentially more (or differently) susceptible to bias. The S1 and S2 epochs show no attractive bias, but they may also be based on more high fidelity training sets (i.e., encoding), and therefore less susceptible to the bias that is evident in the retrocue epoch. So, the results could reflect that serial dependence is indeed a post-perceptual process, or it may instead be that the WM representations, as detected with these MEG analyses, become noisier and more subject to reveal the attractive bias over time.

The results are intriguing, but the study was not powered to examine whether there is any feature-specificity to the neural bias (e.g., whether it matches the behavioral pattern that biases are amplified within a particular range of feature distances between stimuli). Nor do analyses get at temporally precise information about when attractive and repulsive biases appear, which would help to better reconcile the work with previous findings. As in, the reconstructions average across coarse trial epochs. The S1 and S2 reconstructions show no attractive bias, and appear to show subtle repulsion, but if the timing were examined more precisely, we might see repulsion magnified at earlier timepoints that shift toward attraction at later time points, thereby counteracting the effect. That is to say that the averaging approach, across feature values and timepoints, still leaves these important theoretical questions unresolved.

Nonetheless, the work marks an important step in identifying the neurophysiological bases of serial dependence. Ideally, all of the data, including the eye-tracking, would be made available so that others might try to address some of these follow-up questions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99478.3.sa2](https://doi.org/10.7554/eLife.99478.3.sa2)

Summary:

The study aims to probe the neural correlates of visual serial dependence - the phenomenon that estimates of a visual feature (here motion direction) are attracted towards the recent history of encoded and reported stimuli. The authors utilize an established retro-cue working memory task together with magnetoencephalography, which allows to probe neural representations of motion direction during encoding and retrieval (retro-cue) periods of each trial. The main finding is that neural representations of motion direction are not systematically biased during the encoding of motion stimuli, but are attracted towards the motion direction of the previous trial's target during the retrieval (retro-cue period), just prior to the behavioral response. By demonstrating a neural signature of attractive biases in working memory representations, which align with attractive behavioral biases, this study highlights the importance of post-encoding memory processes in visual serial dependence.

Strengths:

The main strength of the study is its elegant use of a retro-cue working memory task together with high temporal resolution MEG, enabling to probe neural representations related to stimulus encoding and working memory. The behavioral task elicits robust behavioral serial dependence and replicates previous behavioral findings by the same research group. The careful neural decoding analysis benefits from a large number of trials per participant, considering the slow-paced nature of the working memory paradigm. This is crucial in a paradigm with considerable trial-by-trial behavioral variability (serial dependence biases are typically small, relative to the overall variability in response errors). While the current study is broadly consistent with previous studies showing that attractive biases in neural responses are absent during stimulus encoding (prev. studies reported repulsive biases), to my knowledge, it is the first study showing attractive biases in current stimulus representations during working memory. The study also connects to previous literature showing reactivations of previous stimulus representations, although the link between reactivations and biases remains somewhat vague in the current manuscript. Together, the study reveals an interesting avenue for future studies investigating the neural basis of visual serial dependence.

Weaknesses:

The main weakness of the current manuscript is that the authors could have done more analyses to address the concern that their neural decoding results are driven by signals related to eye movements. The authors show that participants' gaze position systematically depended on the current stimuli's motion directions, which, together with previous studies on eye movement-related confounds in neural decoding, justifies such a concern. The authors seek to rule out this confound by showing that the consistency of stimulus-dependent gaze position does not correlate with (a) the neural reconstruction fidelity and (b) the attractive shift in reconstructed motion direction. However, the authors' approach of quantifying stimulus-dependent eye movements only considers gaze angle and not gaze amplitude, and thus potentially misses important features of eye movements that could manifest in the MEG data. Moreover, it is unclear whether the gaze consistency metric should correlate with attractive history biases in neural decoding, if there were a confound. These two concerns could be potentially addressed by (1) directly decoding stimulus motion direction from x-y gaze coordinates and relating this decoding performance to neural reconstruction fidelity, and (2) investigating whether gaze coordinates themselves are history-dependent and are attracted to the average gaze position associated with the previous trials' target stimulus. If the authors could show that (2) is not the case, I would be much more convinced that their main finding is not driven by eye movement confounds.

The sample size (n = 10) is definitely at the lower end of sample sizes in this field. The authors collected two sessions per participant, which partly alleviates the concern. However, given that serial dependencies can be very variable across participants, I believe that future studies should aim for larger sample sizes.

It would have been great to see an analysis in source space. As the authors mention in their introduction, different brain areas, such as PPC, mPFC and dlPFC have been implicated in serial biases. This begs the question which brain areas contribute to the serial dependencies observed in the current study? For instance, it would be interesting to see whether attractive shifts in current representations and pre-stimulus reactivations of previous stimuli are evident in the same or different brain areas.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99478.3.sa3](https://doi.org/10.7554/eLife.99478.3.sa3)

Summary:

The study aims to probe the neural correlates of visual serial dependence - the phenomenon that estimates of a visual feature (here motion direction) are attracted towards the recent history of encoded and reported stimuli. The authors utilize an established retro-cue working memory task together with magnetoencephalography, which allows to probe neural representations of motion direction during encoding and retrieval (retro-cue) periods of each trial. The main finding is that neural representations of motion direction are not systematically biased during the encoding of motion stimuli, but are attracted towards the motion direction of the previous trial's target during the retrieval (retro-cue period), just prior to the behavioral response. By demonstrating a neural signature of attractive biases in working memory representations, which align with attractive behavioral biases, this study highlights the importance of post-encoding memory processes in visual serial dependence.

Strengths:

The main strength of the study is its elegant use of a retro-cue working memory task together with high temporal resolution MEG, enabling to probe neural representations related to stimulus encoding and working memory. The behavioral task elicits robust behavioral serial dependence and replicates previous behavioral findings by the same research group. The careful neural decoding analysis benefits from a large number of trials per participant, considering the slow-paced nature of the working memory paradigm. This is crucial in a paradigm with considerable trial-by-trial behavioral variability (serial dependence biases are typically small, relative to the overall variability in response errors). While the current study is broadly consistent with previous studies showing that attractive biases in neural responses are absent during stimulus encoding (prev. studies reported repulsive biases), to my knowledge, it is the first study showing attractive biases in current stimulus representations during working memory. The study also connects to previous literature showing reactivations of previous stimulus representations, although the link between reactivations and biases remains somewhat vague in the current manuscript. Together, the study reveals an interesting avenue for future studies investigating the neural basis of visual serial dependence.

Weaknesses:

The main weakness of the current manuscript is that the authors could have done more analyses to address the concern that their neural decoding results are driven by signals related to eye movements. The authors show that participants' gaze position systematically depended on the current stimuli's motion directions, which, together with previous studies on eye movement-related confounds in neural decoding, justifies such a concern. The authors seek to rule out this confound by showing that the consistency of stimulus-dependent gaze position does not correlate with (a) the neural reconstruction fidelity and (b) the attractive shift in reconstructed motion direction. However, the authors' approach of quantifying stimulus-dependent eye movements only considers gaze angle and not gaze amplitude, and thus potentially misses important features of eye movements that could manifest in the MEG data. Moreover, it is unclear whether the gaze consistency metric should correlate with attractive history biases in neural decoding, if there were a confound. These two concerns could be potentially addressed by (1) directly decoding stimulus motion direction from x-y gaze coordinates and relating this decoding performance to neural reconstruction fidelity, and (2) investigating whether gaze coordinates themselves are history-dependent and are attracted to the average gaze position associated with the previous trials' target stimulus. If the authors could show that (2) is not the case, I would be much more convinced that their main finding is not driven by eye movement confounds.

The sample size (n = 10) is definitely at the lower end of sample sizes in this field. The authors collected two sessions per participant, which partly alleviates the concern. However, given that serial dependencies can be very variable across participants, I believe that future studies should aim for larger sample sizes.

It would have been great to see an analysis in source space. As the authors mention in their introduction, different brain areas, such as PPC, mPFC and dlPFC have been implicated in serial biases. This begs the question which brain areas contribute to the serial dependencies observed in the current study? For instance, it would be interesting to see whether attractive shifts in current representations and pre-stimulus reactivations of previous stimuli are evident in the same or different brain areas.
