# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75090.sa0](https://doi.org/10.7554/eLife.75090.sa0)

This study identifies a mechanism based on context-dependent plasticity of inhibitory receptive fields that likely plays a role in suppression of reverberation signals in hearing. This new mechanism is a very interesting starting point to describe the biological circuit underpinnings of reverberation suppression, a complex signal processing ability of the auditory system.


---

# Peer review - Round 1

Editors:
- Brice Bathellier, https://ror.org/02feahw73 CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75090.sa1](https://doi.org/10.7554/eLife.75090.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cortical adaptation to sound reverberation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nima Mesgarani (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The manuscript is mainly focused on the adaptation of inhibition parameters, and there is no assessment of the efficiency of the dereverberation by cortex. The authors should quantify the similarity of cortical responses for the same sounds with and without reverberation. This measure should be compared to the performance of the dereverberation model (see also comment 4. of reviewer #3).

2. The controls of figure 3 are crucial and should be put in a new main figure, not in the supplements. Especially figure 3 suppl. 2&3.

3. The authors show that a linear receptive field model is not biased by reverberation statistics. However, many papers have shown that auditory processing is non-linear. Therefore, the authors should test this again in a non-linear model (e.g. filterbank followed by a quadratic non-linearity as in the Shamma lab) and improve the cochlear model for example by applying the auditory periphery model described in: Bruce, I. C., Erfani, Y., and Zilany, M. S. A. (2018). "A phenomenological model of the synapse between the inner hair cell and auditory nerve: Implications of limited neurotransmitter release sites," Hearing Research 360:40-54. This and other alternatives are readily available as part of the Auditory Modeling Toolbox (https://www.amtoolbox.org).

Also, it is important to note that dereverberation requires highly nonlinear acoustic processing. The dereverberation algorithms that have been used in speech processing typically try to mask the spectrogram as a method to recover the "direct path" and remove the "reflections." While the resulting "high-pass" filter found in the linear filtering attempts to approximate this nonlinear operation, it is not very effective when used in realistic conditions. While the linear modeling framework here allows the authors to perform a straightforward comparison with auditory receptive fields, this limitation should be noted so the readers are aware of the true difficulty of this task and hence, unexplained mechanisms that remain to be found.

4. The authors should show the energy time curves of the BRIRs at different frequencies and derive the expected adaptation mechanisms already from there. This would greatly simplify the overall concept.

5. A big issue is the differences between the stimuli used to find the receptive field in different reverberant scenarios. While the authors do a good job to show that the differences are not merely due to the statistics of the stimuli, particularly by showing a different response to the probe sound, they cannot claim that "all" of the observed changes are due to adaptation. It is likely reflecting a mix of both, some due to the change in the stimulus correlation and some due to adaptation. Currently, this inherent limitation is not acknowledged.

6. Regarding the discussion of the feedforward/feedback nature of the adaptation to changing background statistics, Khalighinejad et al. also showed that the suppression of background noise is the same when the subject is actively performing speech-in-noise perception and when the subject is distracted by a visual task (Figure 5). Perhaps this observation can strengthen the argument regarding the anesthetized/awake conditions and the nature of the adaptation (lines 447-451). Also, it should be made clear in the discussion that the adaptation phenomenon may not be appearing in cortex, but rather subcortically.

Reviewer #1 (Recommendations for the authors):

1. It should be better discussed why the cortex has a much larger variability in adaptation time constants, than the dereverberation model. The authors suggest that it is because cortical neurons are performing other computations. But an alternative explanation could be that there is more noise in the data than in the model.

2. Related to 1, the manuscript is mainly focused on the adaptation of inhibition parameters, and there is no assessment of the efficiency of the dereverberation by cortex. The authors should quantify the similarity of cortical responses for the same sounds with and without reverberation. This measure should be compared to the performance of the dereverberation model.

3. The controls of figure 3 are crucial and should be put in a new main figure, not in the supplements. Especially figure 3 suppl. 2&3.

4. The authors show that a linear receptive field model is not biased by reverberation statistics. However, many papers have shown that auditory processing is non-linear. Therefore, the authors should test this again in a non-linear model.

5. It should be made clear in the discussion that this phenomenon may not be appearing in cortex, but rather subcortically.

Reviewer #2 (Recommendations for the authors):

I recommend to show the energy time curves of the BRIRs at different frequencies and derive the expected adaptation mechanisms already from there. This would greatly simplify the overall concept.

As a replacement for the cochleagram, I can recommend to apply the auditory periphery model described in: Bruce, I. C., Erfani, Y., and Zilany, M. S. A. (2018). "A phenomenological model of the synapse between the inner hair cell and auditory nerve: Implications of limited neurotransmitter release sites," Hearing Research 360:40-54. This and other alternatives are readily available as part of the Auditory Modeling Toolbox (https://www.amtoolbox.org).

l.610: How was the "low threshold" defined that was applied to limit the log power values?

l.620: This definition of RT10 is inconsistent with the nomenclature used in ISO standards. There, reverberation time is defined as the time it takes the sound energy to decay by 60 dB, denoted as RT60. To estimate this metric, one can also assume a linear decay and measure only the time it takes to decay, for instance, by 20 dB and then multiply by 3. Still, RT20 is then the result of this extrapolation, not the 20-dB-decay time itself. According to that definition, your reverberation times would need to be multiplied by six. Hence, your large room had a reverberation time of about 2.6 s, similar to a small cathedral.

Reviewer #3 (Recommendations for the authors):

This is a very interesting study that tests how the auditory system adapts to reverberant acoustic scenes. The paper is written well, and the results are overall compelling. I have a few comments that hopefully can strengthen the claims of the study.

1. It is important to note that dereverberation requires highly nonlinear acoustic processing. The dereverberation algorithms that have been used in speech processing typically try to mask the spectrogram as a method to recover the "direct path" and remove the "reflections". While the resulting "high-pass" filter found in the linear filtering attempts to approximate this nonlinear operation, it is not very effective when used in realistic conditions. While the linear modeling framework here allows the authors to perform a straightforward comparison with auditory receptive fields, this limitation should be noted so the readers are aware of the true difficulty of this task and hence, unexplained mechanisms that remain to be found.

2. A big issue which the authors are well aware of is the differences between the stimuli used to find the receptive field in different reverberant scenarios. While the authors do a good job to show that the differences are not merely due to the statistics of the stimuli, particularly by showing a different response to the probe sound, they cannot claim that "all" of the observed changes are due to adaptation. It is likely reflecting a mix of both, some due to the change in the stimulus correlation and some due to adaptation. Currently, this inherent limitation is not acknowledged.

3. Related to 2, I think the control experiments that were done to show the changes in the response to the probe sound in different reverberant conditions are worthy of inclusion in the main figures. Perhaps a summary of that can be added to Figure 3, as this is a very important result, without which the observed changes are not very compelling.

4. On the same point, while it is an important observation that the responses to the probe stimulus (non-reverberant) are different in different reverberation contexts, a complementary observation that is missing is the similarity of the cortical responses to varying degrees of reverberation. In other words, if the STRFs change as suggested to produce a less variable response to reverberation, then the responses to the same sound with different reverb should stay constant and similar to the anechoic sound. While invariant cortical responses have been shown in other studies (including ferrets), it will strengthen this study if they can also confirm the presence of that effect which is the subject of this study.

5. Regarding the discussion of the feedforward/feedback nature of the adaptation to changing background statistics, Khalighinejad et al. also showed that the suppression of background noise is the same when the subject is actively performing speech-in-noise perception and when the subject is distracted by a visual task (Figure 5). Perhaps this observation can strengthen the argument regarding the anesthetized/awake conditions and the nature of the adaptation (lines 447-451).
