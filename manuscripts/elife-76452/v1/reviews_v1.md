# Peer review - Round 1

Editors:
- Supratim Ray, https://ror.org/04dese585 Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76452.sa0](https://doi.org/10.7554/eLife.76452.sa0)

The authors report that neurons in V1 and V4 multiplex information of simultaneously presented objects. A combination of multi-single unit recordings, statistical modelling of neuronal responses and neuronal correlations analyses argues in favor of their claims. Pairs of neurons having similar object preferences tended to be positively correlated when both objects were presented, while pairs of neurons having different object preferences tended to be negatively correlated and these patterns and others suggest that information about the two objects is multiplexed in time. These results are of broad interest to the field, as they shed new light on the "binding" problem and highlight the importance of underexplored features of cortical activity for neural coding.


---

# Peer review - Round 1

Editors:
- Supratim Ray, https://ror.org/04dese585 Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76452.sa1](https://doi.org/10.7554/eLife.76452.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Coordinated multiplexing of information about separate objects in visual cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Ruben Coen-Cagli (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While this paper shows some intriguing results, we feel that there are a lot of open questions that need to be addressed before convincing evidence of multiplexing can be established. These points are discussed below:

1. The best spike count model shown in Figure 2C is confusing. It seems that the number of "conditions" is a small fraction of the total number of conditions (and neurons?) that were tested. Supplementary Figure 1 provides more details (for example, the "mixture" corresponds to only 14% of total cases), but it is still confusing (for example, what does WinProb>Min mean?). From what I understood, the total number of neurons recorded for the Adjacent case in V1 is 1604, out of which 935 are Poisson-like with substantially separated means. Each one has 2 conditions (for the two directions), leading to 1870 conditions (perhaps a few less in case both conditions were not available). I think the authors should show 5 bar plots – the first one showing the fraction for which none of the models won by 2/3 probability, and then the remaining 4 ones. That way it is clear how many of the total cases show the "multiplexing" effect. I also think that it would be good to only consider neurons/conditions for which at least some minimum number of trials are available (a cutoff of say ~15) since the whole point is about finding a bimodal distribution for which enough trials are needed.

2. More RF details need to be provided. What was the size of the V1 RFs? What was the eccentricity? Typically, the RF diameter in V1 at an eccentricity of ~3 degrees is no more than 1 degree. It is not enough to put 2 Gabors of size 1 degree each to fit inside the RF. How close were the Gabors? We are confused about the statement in the second paragraph of page 9 "typically only one of the two adjacent gratings was located within the RF" – we thought the whole point of multiplexing is that when both stimuli (A and B) are within the RF, the neuron nonetheless fires like A or B? The analysis should only be conducted for neurons for which both stimuli are inside the RF. When studying noise correlations, only pairs that have overlapping RFs such as both A and B and within the RFs of both neurons should be considered. The cortical magnification factor at ~3-degree eccentricity is 2-2.5mm/degree, so we expect the RF center to shift by at least 2 degrees from one end of the array to the other.

3. Eye data analysis: the reviewers are concerned that this could potentially be a big confound. Removing trials that had microsaccades is not enough. Typically, in these tasks the fixation window is 1.5-2 degrees, so that if the monkey fixates on one corner in some trials and another corner in other trials (without making any microsaccades in either), the stimuli may nonetheless fall inside or away from the RFs, leading to differences in responses. This needs to be ruled out. We do not find the argument presented on pages 18 or 23 completely convincing, since the eye positions could be different for a single stimulus versus when both stimuli are presented. It is important to show that the eye positions are similar in "AB" trials for which the responses are "A" like versus "B" like, and these, in turn, are similar to when "A" and "B" are presented alone.

Relatedly, more details on the detection of microsaccades and threshold values for inclusion (relative to stimulus and RF sizes) should be provided, given how central a role they might play. In particular, the authors state in Discussion that small residual eye movements would inflate response variability in all stimulus conditions. This is correct, but because of the stimulus design, it is possible (likely?) that the effects are quite different for segregated stimuli versus superimposed and single-stimulus conditions. Furthermore, the difference might be precisely in the direction of the effects reported. That is because segregated stimuli are spatially separate, and each stimulus only covers some receptive fields in the recording, it is possible that eye movements would bring inside the RF a different stimulus in each trial. In addition to producing bimodal response distributions for individual neurons, this would also induce positive correlations for pairs with the same preference and negative correlations for pairs with opposite preferences. On the other hand, in the superimposed condition where the stimulus is large enough to cover all RFs, at most eye movements would bring (part of) the stimulus inside versus outside the RF across trials, therefore contributing to positive noise correlations for all pairs (i.e., to shifts from stimulus-driven to spontaneous activity, in the extreme case). In our opinion, the main concern raised in the public review deserves more in-depth analysis, of the data and/or simulations, for us to be convinced that eye movements truly do not play a role. Conversely, if they do, it may be worth discussing the possibility that they are part of the mechanism underlying the proposed coding scheme.

4. Figures 5 and 6 show that the difference in noise correlations between the same preference and different preference neurons remains even for non-mixture type neurons. So, although the reason for the particular type of noise correlation was given for multiplexing neurons (Figure 3 and 4), it seems that the same pattern holds even for non-multiplexers. Although the absolute values are somewhat different across categories, one confound that still remains is that the noise correlations are typically dependent on signal correlation, but here the signal correlation is not computed (only responses to 2 stimuli are available). If there is any tuning data available for these recordings, it would be great to look at the noise correlations as a function of signal correlations for these different pairs. Another analysis of interest would be to check whether the difference in the noise correlation for simply "A"/"B" versus "AB" varies according to neuron pair category. Finally, since the authors mention in the Discussion that "correlations did not depend on whether the two units preferred the same stimulus or different", it would be nice to explicitly show that in figure 5C by showing the orange trace ("A" alone or "B" alone) for both same (green) and different (brown) pairs separately.

5.We are confused about the nature of Poisson models. If we are correct, the Poisson(a+b) is the sum of the two Poisson(a) and Poisson(b), that is, Poisson(a+b) = Poisson(a) + Poisson(b). Then, the mixture and intermediate models are very similar, identical if a*λ_A and (1-a)*λ_B happen to be integer numbers.

6. It is unclear why the 'outside' model predicts responses outside the range if neurons were to linearly sum the A and B responses.

7. It is also unclear why the 'single' hypothesis would indicate a winner-take-all response. If we understand correctly, under this model, the response to A+B is either the rate A or B, but not the max between λ_A and λ_B. Also, this model could have given an extra free parameter to modulate its amplitude to the stimulus A+B.

8. The concept of "coarse population coding" can be misleading, as actual population coding can represent stimulus with quite good precision. The authors refer to the broad tuning of single cells, but this does not readily correspond to coarse population coding. This could be clarified.

9. As a complement to the correlation analysis, one could check whether, on a trial-by-trial basis, the neuronal response of a single neuron is closer to the A+B response average, or to either the A or B responses. This would clearly indicate that the response fluctuates between representing A or B, or simultaneously represents A+B. I am trying to understand why this is not one of the main analyses of the paper instead of the correlation analysis, which involves two neurons instead of one.

10. In the discussion about noise correlations, the recent papers Nogueira et al., J Neuroscience, 2020 and Kafashan et al., Nat Comm, 2021 could be cited. Also, noise correlations can also be made time-dependent, so the distinction between the temporal correlation hypotheses and noise correlations might not be fundamental.

11. It would be interesting to study the effect of contrast on the mixed responses. Is it reasonable to predict that with higher contrast the mixture responses would be more dominant than the single ones? This could be the case if the selection mechanism has a harder time suppressing one of the object responses. This would also predict that noise correlations will go down with higher contrast.

12. What is the time bin size used for the analysis? Would the results be the same if one focuses on the early time responses or on the late time responses? At least from the units shown in Figure 2, it looks that there is always an object response that is delayed respect to the other, so it would seem interesting to test noise correlations in those two temporal windows.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coordinated multiplexing of information about separate objects in visual cortex" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved and many of the reviewers' concerns have been addressed. However, some major issues remain. Although we typically avoid repeated revise/resubmit cycles, we believe that it is important for these issues to be addressed in a new revision. Specifically, upon discussion the reviewers unanimously remained concerned about the possibility that at least some of your results could be accounted for by subtle differences in eye movements. The new analyses related to that issue were appreciated but considered inadequate.

As detailed below, we would like you to provide:

1. More information about whether the electrodes that show evidence of multiplexing are the ones whose RF straddles the two stimuli, because in that case, small eye movements will bring one of the two stimuli inside the RF.

2. Further analyses of eye position to rule out the possibility described above. In our discussions, it was noted that the new Figure 1 – Supplementary Figure 1 appears to show that numerous V1 RFs straddle the two stimuli, and under those conditions, we really want to know if the "multiplexed" responses are because of small fixational differences/microsaccades that affect which of the two stimuli takes a more dominant position in the RF. To test for this kind of effect, just the STD of eye position per trial for one-stimulus vs two-stimuli conditions does not seem to be sufficient. Instead, it seems important to know whether, in the two-stimuli condition, responses were more "A-like" when gaze put the A stimulus closer to the RF center, and were more "B-like" when gaze put the B stimulus closer to the RF center. So something like a linear regression of spiking response versus "eye position along the axis defined by the centers of the two stimuli, increasing towards the stimulus that alone elicited the larger response" could be useful.

Reviewer #1 (Recommendations for the authors):

The authors have made several changes in the manuscript to address previous concerns. However, the fact that typically only one stimulus spanned the RF makes it difficult to make a case for multiplexing, since the other stimulus is outside the classical RF. The arguments made by the authors in response to the previous RF-related question (point 2) are based on their own hypothesis about some underlying "spatial scale" of multiplexing which is coarser than the RF size of V1, which I do not find particularly convincing and would be extremely difficult to implement in V1. Further, while the authors showed more results related to eye position analysis, they do not show the key comparison that was requested previously.

To better appreciate the spatial scales involved, I refer to figures from the following two studies in V1 where very small stimuli (0.1 – 0.2 degrees) were used to map the RFs: Figure 2 of Xing et al., 2009, JNS, and Figure 2 of Dubey and Ray, 2016, JNP. Typically, the SD of fitted Gaussian is typically no more than 0.25 degrees at an eccentricity of 2-3 degrees (if you consider the radius as 2SD (0.5 degrees), the diameter is about a degree). For such RFs, there is no response if a stimulus is more than a degree away from the RF. For Gabor patches used in this paper, only the "size" is mentioned. Does size refer to the radius or SD? In either case, there is no way to fit two Gabors within the RF. What is the separation between two Gabors? Figure 1 should highlight all these details, including the radius (not just the center) of the V1 units.

Given the concern that one of the stimuli is always outside the RF, how do we explain the findings? One possible answer is in small differences in eye position. Multiplexing is anyway observed in only ~100 out of 1389 units. I suspect these are the units whose RF center is between the two stimuli. For the AB condition (i.e., both stimuli are presented), small jitters in eye position would bring one of the two stimuli in the RF, and therefore the unit would respond like either A or B. To address this, the authors should show the RF centers of the units that show evidence of multiplexing, along with the stimuli.

In addition, it is important to check for possible differences in eye position within AB conditions for trials for which responses were "A like" versus "B like". The authors have compared the AB condition to A and B conditions presented alone, but that is not enough. The argument that the stimuli were presented for a short duration and in pseudorandom order and therefore it is not possible for the animal to have systematically different eye positions for A/B versus AB conditions is obviously true, but that is not the point. The point is that the eye positions have small variations from trial to trial (as shown in Figure 1 – Supp 2) even before stimulus onset, and AB trials in which the position happens to be in one location get classified as "A like" and another location gets classified as "B like". It is in fact very hard to rule out this possibility given the instrument noise which affects the precision of eye positions, but it is crucial to rule this out.

Reviewer #2 (Recommendations for the authors):

The authors have appropriately addressed all comments. In particular, the controls on eye movements are sound.

Reviewer #3 (Recommendations for the authors):

The authors have addressed my concerns and all other concerns raised in the editor's summary. My main concern was whether uncontrolled fixational eye movements (microsaccades) could account in part for the observed multiplexing. I understand now that concern was largely because of missing details about eye position, RF sizes, stimulus sizes, etc, which are now reported. The possibility remains that trial-by-changes in eye position (within the fixation window) would inflate the proportion of single-neuron "mixture" cases for adjacent two-object stimuli (by effectively changing which object is inside the RF in any given trial). But, importantly, this could not explain the observed patterns of noise correlations.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coordinated multiplexing of information about separate objects in visual cortex" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed. We realized we were not as specific as we should have been in the last round of feedback and have tried to clarify here exactly what the reviewers are looking for.

In particular, because the authors claim that ~100 electrodes have mixture responses, the possible influence of eye movements should be tested for all the mixture units, not only 9/100 as done in the previous review. We would therefore like the analyses done for all the mixtures. To avoid ambiguity, we are listing the requested analyses in more detail below:

1. Show the RF centers of ALL the units labeled as mixtures (~100). The best way to do this would be to make a line passing through the centers of the two stimuli, and make five groups of units depending on their RF centers – (i) left of the left stimulus, (ii) on the left stimulus, (iii), between left and right stimulus, (iv) on the right stimulus and (v) right of the right stimulus. Then show what proportion of units in each category are mixtures. The eye movement hypothesis predicts that mixtures will be predominant in (iii). Actually, since 91/100 units have one of the two modes at zero (as far as I could understand the previous analysis), these units could even be at (i) or (v).

2. Do the eye position analysis for ALL mixture units. Since the stimuli are mainly separated along the x-axis, all we are asking is to make a scatter plot of spike counts and average eyeX position for each trial and then check for correlation between the two. This analysis is valid even for units that only respond to one stimulus (i.e. the remaining 91 units). We expect to find a significant correlation (either positive or negative) if the results are due to small eye movements, but not if the firing is due to their multiplexing hypothesis. Or, if you find significant correlations since the RF sizes are comparable to the stimulus sizes, you need to show that these correlations are insufficient to explain the bimodality.

3. In addition, I think the authors should at least show the typical RF radius of the units (make a circle of radius of 0.5 degrees on a few of the units, perhaps the ones shown in Figure 4). We think it is important to show that the RFs do not encompass both stimuli, which is not clear from the plots.

4. The fact that one mode of the bimodal distribution is zero in 91/100 cases should also be made clearer, perhaps in the methods section. Essentially the bimodal response in most cases is not A versus B, but A/B versus zero.
