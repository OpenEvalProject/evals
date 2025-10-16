# Peer review - Round 1

Editors:
- Joni Wallis, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31507.027](https://doi.org/10.7554/eLife.31507.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Covert Shift of Attention Modulates the Value Encoding in the Orbitofrontal Cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Guest Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Camillo Padoa-Schioppa (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study is a novel attempt to bring together two broad threads of cognitive and systems neuroscience – value representation and attentional mechanisms. It also adds to the literature addressing serial mechanisms of evidence evaluation and choice, a topic of growing interest (e.g. Shohamy and Shadlen, 2015). An additional strength of this study is that the experiment attempts to explicitly control the two major variables that are often entangled: reward expectation and attention; the use of a non-choice paradigm also removes another potentially confounding variable. The overall statistical approach is appropriate, and the graphical and written presentation is clear. However, there were a number of issues that reviewers would like to see addressed before deciding on the suitability of the manuscript for publication.

Main comments:

1) All reviewers were concerned about the weak neural effects. It is particularly important that rigorous statistical methods are employed to determine whether the effects are real. For example, all reviewers were in agreement that one-tailed tests could not be justified. In addition, there was concern that the effects in Figure 4 are apparent before the stimulus was rotated. This might potentially be a smoothing artifact, but the smoothing window is not reported, making it difficult to determine whether this is indeed the case.

2) Reviewers were not convinced by the modeling component of the manuscript. One possibility is that the neural effects arise as a consequence of dividing attention to the two stimuli when the lower value is perturbed. Thinking of the effect as resulting from divided attention, the firing rate in the rotation trials would simply equal the (possibly weighted) average between those associated with the two cues. This account would not need any free parameter (or at most one capturing the weights) and it is very consistent with the data. This would be a simpler model than the selective attention model with four free parameters. The authors should do a formal model comparison with their chosen model against these potentially simpler models, to show that the more complex model is a better predictor of neural activity.

3) Several points made in the Discussion were unconvincing or problematic.

a) "Although the observed attentional modulation of the neural responses in the OFC in this study was relatively modest, it represented a worst-case scenario." One could make the opposite claim: If the behavioral task had required using values computed or represented in the OFC, monkeys would have considered both options more evenly. In other words, contrary to the authors speculation, the attentional modulation might have been smaller had the monkeys been engaged in a choice task.

b) The authors discuss the neuronal effects described here as "explained by attention". However, the effects recorded here differ in fundamental ways from the attentional effects often described in sensory regions. Normally, the effect of attention on the activity of a neuron is understood as a gain modulation on a sensory response. For example, neurons in visual areas have receptive fields; if the animal pays attention to a particular location, the visual responses of neurons whose RF coincides with that location are enhanced. Concurrently, the visual responses of neurons with different RFs are somewhat reduced. In contrast, OFC cells are not spatially selective – that is, they don't have a receptive field at all. (This is fundamental difference between OFC and V4, MT, etc. Hence, the first paragraph of the subsection “OFC and the visual system” is incorrect.) Thus the neuronal effects found here may have to do more with mental focus than with attention as defined in the context of sensory systems, even though at the behavioral level the effects are driven by a shift of attention.

c) The authors re-interpret previous findings of neurons coding the chosen value as neurons coding the value the animal was focusing on. This may be an acceptable interpretation. Then they write "Our results suggest that the OFC encodes the value information one item at a time even when multiple items are presented" and "our results suggest that value-based decision making is a sequential process in which the value of each option is evaluated one at a time, guided by attention". These statements are completely speculative and they seem at odds with previous results. Along with neurons coding the chosen value, several studies found neurons coding the value of individual offers, or offer values. Furthermore, these cells have low noise correlations and low choice probabilities (Conen and Padoa-Schioppa, 2015). If trial-by-trial fluctuations in the activity of these neurons and behavioral choice variability were both driven by attention, one would expect much higher measures for both noise correlation and for choice probability. Thus it might be the case that only some of the value coding neurons in OFC are subject to the effects described here.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Covert Shift of Attention Modulates the Value Encoding in the Orbitofrontal Cortex" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), a Guest Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. We do not ordinarily invite multiple rounds of revision so please consider this the last opportunity you will have to respond to the concerns expressed below.

In general, there is agreement that the manuscript's findings are potentially important, but there are serious concerns about the statistical analysis that underlies the main findings of the paper. Since the size of the effects is on the smaller side, it is critical that rigorous statistical tests are used (two-tailed and corrected for multiple comparisons) and that the potential artifact can be satisfactorily explained, otherwise we will not be able to accept the paper.

Reviewer #1:

My thanks to the authors for addressing many of the concerns. While this manuscript is improved, there are still very serious issues that have not been resolved.

The most significant issues concern Figure 4A, B which shows how neural activity changes around the time of cue rotation. In brief: there is a lack of explanation for early onset of the effects; there is still a lack of statistical rigor in the significance testing; and there is a glaring data discrepancy between the primary and supplemental figures. Given these issues, I don't have confidence in these data, which are the main results of the paper. All three of these deficiencies – the first being the most critical – must be addressed. In more detail:

1) The original version of Figure 4A, B showed spurious neural activity changes before rotation. While the pre-rotation effects have largely disappeared, there are still neural effects during rotation, and these are still too early to be caused by the rotation. The authors must offer some plausible explanation for this. While they claim it could be due to noise, this is unlikely, as the effect is evident in both monkeys (Figure 4—figure supplement 1), for both positive and negative coding neurons.

To elaborate: In Figure 4A, the latency to a significant effect is 30ms, which the authors attribute to a "bottom-up" process. However, the initial response to cue onset (presumably also a bottom-up process) occurs at a much slower latency of approximately 70-80ms. The situation is even worse in Figure 4B, where the effects are significant at the onset of cue rotation at t=200ms. This first significant bin spans from t=175 to t=225ms, meaning that it includes data from the first 25ms after rotation begins. This is far too little time for rotation-induced attentional effects to appear, given that minimum visual response latencies within the lateral geniculate nucleus are approximately 20ms (Schroeder CE et al. Brain Res. 1989 Jan 16;477(1-2):183-95.).

If this were my data, I would strongly suspect an artifact of some kind. For example, if the trial conditions were insufficiently randomized, it is possible that the monkeys could anticipate which stimulus was going to be rotated on some trials, so that they could shift attention before the rotation begins.

2) In Figure 4A, B a one-tailed test is not justified. If this were a follow-on study looking to confirm a previously documented effect, then the authors could claim a priori justification for using a one-tailed test. But this study is an investigation of a novel phenomenon, and so the threshold for rejecting the null hypothesis must be suitably strong. While Figure 4—figure supplement 5 uses a two-tailed test, it does not, according to the legend, correct for multiple comparisons. For this analysis to be credible, it must be performed with two-tailed tests, with some form of p-value or FDR correction.

3) In Figure 4 there is a discrepancy between the main and supplemental figures. The same data are supposedly plotted in Figure 4A, B and Figure 4—figure supplement 5A, B the only difference being the use of two-tailed tests to draw the significance indicators at the top of the plot. However, the means are clearly different between the two figures. For example, in Figure 4A, the red and blue lines overlap at ~850ms, but in Figure 4—figure supplement 5A they do not. These are clearly different data.

Reviewer #2:

I have reviewed the revised manuscript. For the most part, I believe the authors have addressed concerns raised in the first review. My major outstanding concern is that the 1-tailed tests in Figure 4 are still not appropriate. In panels C-F the authors report neurons with significant effects in directions opposite of their a-priori hypothesis, therefore they are in fact testing both sides of the distribution, but using a 1-sided significance threshold. The authors have the relevant 2-tailed stats and figures in the supplement, and should use these in the main paper.

I think the addition of alternative models has strengthened their results. However, in the table of model parameters, it says that models 1 and 2 have 1 and 2 free parameters respectively. I'm not sure this is correct. For example, model 1 fits a and b, and in the calculation of AICs, the intercept should be included as a parameter, so there should be 2. This shouldn't change the outcome, but stands out as a potential error.

On this note, it seems odd to include the constant, b, in these models at all, when FRs of each neuron are being directly fit from their own FRs. In other words, the underlying hypothesis is that a neuron's FR in the double-cue condition is some mixture of its own FRs in the two single-cue conditions – not that mixture with a constant offset. So why include the constant?

Reviewer #3:

The manuscript was significantly improved. However, a couple of points raised in the first review require additional clarification. Numbers refer to those in the first review.

3a) Apropos the idea that the attentional modulation observed in this study represented a "worst-case scenario": In the initial review, it was noticed that one could make the opposite speculation. In a choice setting, which requires using values computed in OFC, monkeys would have considered both options more evenly. Hence, contrary to the authors assertion, had the monkeys been engaged in a choice task, the attentional modulation might have been smaller, not larger. The authors did not take this issue at heart, but they should. Let me note that this is more than a simple discussion point: As the authors make clear in their response to point (1), the worst-case scenario argument is part of why they think the small effects described in this paper are real. Again, I don't see any a-priori reason to think that in a choice setting the attentional modulation would be stronger. If this claim is so important, and if it relies on unpublished data, the data should be described in this paper and we should be given the opportunity to review the evidence. If this claim is not so important, the authors should drop it here and make it elsewhere, when they present the appropriate evidence. In the latter case, they might want to provide a different response to point (1).

3c) If I understand correctly, the authors speculate that offer value cells provide an indirect input to the decision circuit, which operates with working memory mechanisms. However, the fact that offer value cells exist (i.e., the fact that in choice settings some neurons are associated to individual offers), and the fact that noise correlations between them are small implies that these cells are not modulated by attention in the sense described in this manuscript. Do the authors agree on this point? The was the sense of my previous comment, not whether the contribution of offer value cells to the decision is direct or indirect.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Covert Shift of Attention Modulates the Value Encoding in the Orbitofrontal Cortex" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below. We do not ordinarily invite multiple rounds of revision so please consider this the last opportunity you will have to respond to the concerns expressed below.

In general, there is agreement that the manuscript's findings are potentially important, but there are serious concerns about the statistical analysis that underlies the main findings of the paper. Since the size of the effects is on the smaller side, it is critical that rigorous statistical tests are used (two-tailed and corrected for multiple comparisons) and that the potential artifact can be satisfactorily explained, otherwise we will not be able to accept the paper.

Reviewer #1:

My thanks to the authors for addressing many of the concerns. While this manuscript is improved, there are still very serious issues that have not been resolved.

The most significant issues concern Figure 4A, B which shows how neural activity changes around the time of cue rotation. In brief: there is a lack of explanation for early onset of the effects; there is still a lack of statistical rigor in the significance testing; and there is a glaring data discrepancy between the primary and supplemental figures. Given these issues, I don't have confidence in these data, which are the main results of the paper. All three of these deficiencies – the first being the most critical – must be addressed. In more detail:

1) The original version of Figure 4A, B showed spurious neural activity changes before rotation. While the pre-rotation effects have largely disappeared, there are still neural effects during rotation, and these are still too early to be caused by the rotation. The authors must offer some plausible explanation for this. While they claim it could be due to noise, this is unlikely, as the effect is evident in both monkeys (Figure 4—figure supplement 1), for both positive and negative coding neurons.

To elaborate: In Figure 4A, the latency to a significant effect is 30ms, which the authors attribute to a "bottom-up" process. However, the initial response to cue onset (presumably also a bottom-up process) occurs at a much slower latency of approximately 70-80ms. The situation is even worse in Figure 4B, where the effects are significant at the onset of cue rotation at t=200ms. This first significant bin spans from t=175 to t=225ms, meaning that it includes data from the first 25ms after rotation begins. This is far too little time for rotation-induced attentional effects to appear, given that minimum visual response latencies within the lateral geniculate nucleus are approximately 20ms (Schroeder CE et al. Brain Res. 1989 Jan 16;477(1-2):183-95.).

If this were my data, I would strongly suspect an artifact of some kind. For example, if the trial conditions were insufficiently randomized, it is possible that the monkeys could anticipate which stimulus was going to be rotated on some trials, so that they could shift attention before the rotation begins.

2) In Figure 4A, B a one-tailed test is not justified. If this were a follow-on study looking to confirm a previously documented effect, then the authors could claim a priori justification for using a one-tailed test. But this study is an investigation of a novel phenomenon, and so the threshold for rejecting the null hypothesis must be suitably strong. While Figure 4—figure supplement 5 uses a two-tailed test, it does not, according to the legend, correct for multiple comparisons. For this analysis to be credible, it must be performed with two-tailed tests, with some form of p-value or FDR correction.

3) In Figure 4 there is a discrepancy between the main and supplemental figures. The same data are supposedly plotted in Figure 4A, B and Figure 4—figure supplement 5A, B, the only difference being the use of two-tailed tests to draw the significance indicators at the top of the plot. However, the means are clearly different between the two figures. For example, in Figure 4A, the red and blue lines overlap at ~850ms, but in Figure 4—figure supplement 5A they do not. These are clearly different data.

Reviewer #2:

I have reviewed the revised manuscript. For the most part, I believe the authors have addressed concerns raised in the first review. My major outstanding concern is that the 1-tailed tests in Figure 4 are still not appropriate. In panels C-F the authors report neurons with significant effects in directions opposite of their a-priori hypothesis, therefore they are in fact testing both sides of the distribution, but using a 1-sided significance threshold. The authors have the relevant 2-tailed stats and figures in the supplement, and should use these in the main paper.

I think the addition of alternative models has strengthened their results. However, in the table of model parameters, it says that models 1 and 2 have 1 and 2 free parameters respectively. I'm not sure this is correct. For example, model 1 fits a and b, and in the calculation of AICs, the intercept should be included as a parameter, so there should be 2. This shouldn't change the outcome, but stands out as a potential error.

On this note, it seems odd to include the constant, b, in these models at all, when FRs of each neuron are being directly fit from their own FRs. In other words, the underlying hypothesis is that a neuron's FR in the double-cue condition is some mixture of its own FRs in the two single-cue conditions – not that mixture with a constant offset. So why include the constant?

Reviewer #3:

The manuscript was significantly improved. However, a couple of points raised in the first review require additional clarification. Numbers refer to those in the first review.

3a) Apropos the idea that the attentional modulation observed in this study represented a "worst-case scenario": In the initial review, it was noticed that one could make the opposite speculation. In a choice setting, which requires using values computed in OFC, monkeys would have considered both options more evenly. Hence, contrary to the authors assertion, had the monkeys been engaged in a choice task, the attentional modulation might have been smaller, not larger. The authors did not take this issue at heart, but they should. Let me note that this is more than a simple discussion point: As the authors make clear in their response to point (1), the worst-case scenario argument is part of why they think the small effects described in this paper are real. Again, I don't see any a-priori reason to think that in a choice setting the attentional modulation would be stronger. If this claim is so important, and if it relies on unpublished data, the data should be described in this paper and we should be given the opportunity to review the evidence. If this claim is not so important, the authors should drop it here and make it elsewhere, when they present the appropriate evidence. In the latter case, they might want to provide a different response to point (1).

3c) If I understand correctly, the authors speculate that offer value cells provide an indirect input to the decision circuit, which operates with working memory mechanisms. However, the fact that offer value cells exist (i.e., the fact that in choice settings some neurons are associated to individual offers), and the fact that noise correlations between them are small implies that these cells are not modulated by attention in the sense described in this manuscript. Do the authors agree on this point? This was the sense of my previous comment, not whether the contribution of offer value cells to the decision is direct or indirect.
