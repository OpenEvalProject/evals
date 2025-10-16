# Peer review - Round 1

Editors:
- Erin L Rich, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63490.sa0](https://doi.org/10.7554/eLife.63490.sa0)

This is a timely and important study that systematically assesses the relationships between neuronal activity in the locus coeruleus (LC) and the anterior cingulate cortex (ACC) in non-human primates. The LC is a major source of cortical norepinephrine that has reciprocal connectivity with the ACC, and the authors have convincingly shown that LC spiking is associated with changes in ACC spike correlations. Further, these changes have consistent phase relationships with pupil size. This is a rare data set that is technically challenging to acquire, and the results are an important advance toward understanding a circuit that is likely to play a role in regulating brain states such as arousal or attention.


---

# Peer review - Round 1

Editors:
- Erin L Rich, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63490.sa1](https://doi.org/10.7554/eLife.63490.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Relationships between Locus Coeruleus Firing Patterns and Coordinated Neural Activity in the Anterior Cingulate Cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tirin Moore as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tobias H Donner (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below primarily address clarity and presentation.

Summary:

This is a monkey neurophysiology study into the neuronal basis of arousal in the primate brain. The authors systematically assess the relationship between neuronal activity in an important neuromodulatory center of the brainstem, the locus coeruleus (LC), and a reciprocally connected cortical region, the anterior cingulate cortex (ACC). LC is a major source of cortical norepinephrine (NE), so LC spikes may predict momentary changes in cortical NE. Pupil size, also measured here, is sometimes used as a peripheral index of NE levels in the cortex, though this is also correlated with a variety of other factors, including other neuromodulators. The authors have three main conclusions. First, spikes in LC neurons predicted a decrease in the Fano factor in ACC and a decrease in the pair-wise correlations (rsc) between highly correlated ACC neurons. Second, both LC spikes and ACC rsc appeared to have a consistent phase relationship with pupil size, with the troughs in ACC rsc lagging LC spikes. Third, LC spikes predicted changes in the relationship between surprising stimuli and ACC rsc, as well as the relationship between the pupil response to surprising stimuli and ACC rsc. The authors also mention that these changes are independent of the relationship of LC activity and ACC firing rates.

Overall, the reviewers felt that this is a timely and important study, particularly because the LC-ACC circuit is under-characterized in primates. The major strengths of the study include the rarity of the data set, the technical sophistication of the analyses, and the investigation of LC-ACC relationships across multiple timescales. However, it was felt that revisions are needed to make some points convincingly, and in other cases the inherent limitations in the analyses should be more thoroughly acknowledged. The specific comments on these points are outlined below.

Essential revisions:

1. The analyses in this study do not directly assess causality or directionality of the interactions reported. This was noted my multiple reviewers, with specific points in the comments below. In addition to these points, in light of the difficulty in claiming causality or directionality from recording data, and it was agreed that there should be a general restructuring of the interpretation to reflect this limitation.

a. While the data are very interesting and compelling in their current form. I think that some limitations of the current analyses should be acknowledged. Specifically, the analyses do not allow for inferences about the directionality of effects. So, it remains open if the changes of LC firing rate cause the changes in spike-count correlations in ACC (as seems likely), or vice-versa; or if a third variable causes the effects in both brain regions? Even without causal manipulations, inferences of this kind could be based on an assessment of the temporal relationships of changes in the local signal properties. It could also be based on statistical assessments (e.g. using multivariate autoregressive modeling) of "Granger causality".

b. Related to "Single-neuron activity during passive fixation"/Figure 2. I'm curious to understand the direction of this effect – does variance in ACC predict spike counts in LC or do spikes in LC predict variance in ACC? Is it possible to look at spike-evoked Fano factor in the ACC (i.e. before and after an LC spike)? Figure 6 is described as implying that these LC spikes and ACC rsc are temporally related, but this is only analyzed as mediated by the relationship between each and pupil size, but this temporal relationship appears not to be investigated directly ("relatively fixed temporal relationships to pupil fluctuations and therefore to each other").

c. The authors do nice internal controls testing not only LC-ACC effects, but also ACC-LC effects. They describe that LC-ACC are significant, while the ACC-LC effects are less reliable. This is important for their claims but also as a validation of the analyses. Did the authors formally compare whether there are significant differences between ACC-LC and LC-ACC effects? Showing that ACC-LC is not significant does not address this per se. Slopes (Figure 5) can definitely be tested for LC-ACC vs ACC-LC. (e.g., is the slope more negative in one versus the other).

d. Figure 6A, in the legend is described as evidence that LC spikes have a consistent phase relationship with pupil fluctuations that have a period of 600 ms. In the text, this result is taken as evidence that LC peaks 270 ms in advance of the "relevant pupil change" (I'm not entirely clear what pupil phase is being referenced by this phrase). Are these different interpretations? Do LC spikes have a fixed relationship to one component of the pupil fluctuations (like dilation or the cresting at peak size) or are they entrained to the oscillation? Also, it would be good to cite Pong and Fuchs 2000 J Neurophysiol in addition to Joshi, 2016 as evidence for hippus in the monkey at this 1.67 Hz frequency.

e. Related, in Figure 6B, it looks (to my eye) like ACC rsc is also peaking in advance of the trough highlighted in this figure. This would suggest an alternative model, where high rsc in ACC predicts spontaneous LC spiking, and then lower rsc in ACC. This alternative might more in line with Alla Karpova's work that focuses on the effects of ACC on LC activity, rather than the LC-ACC relationship that is the focus of this paper.

2. A major caution in interpreting these results is that the paper performs a lot of multiple comparisons in nested bins, and it is not clear that the multiple comparison problem is appropriately controlled for. Many effects appear obvious in the plots suggesting that the three major results would survive correction (i.e. Figure 2G), but for some of the latter analyses it is not clear that effects would survive correction. This problem is complicated by the fact that the tests are strongly interdependent, so it's not clear that a simple correction would be sufficient. It may be more appropriate to conduct permutation tests, or directly ask how independent variables alter how the dependent variable scales with bin sizes.

3. There was some confusion surrounding the motivation for the study as stated in the Introduction. Specifically, the tonic/phasic dichotomy is mentioned in the introduction, but it appears that this was not directly investigated in the rest of the manuscript. Moreover, it was noted that this dichotomy may not be so clear-cut. There may be some overlap with the ideas of ongoing/evoked activity, as in the Aston-Jones and Cohen (2005) framework, however the links between these perspectives are not explored. Reviewers recommend either describing in more detail how the tonic/phasic perspectives motivated the study, or removing this from the introduction and better explaining why one might be curious about the relationship between LC spikes and ACC activity. In the same vein, it would also be helpful to motivate the specific analyses that were performed. Later analyses were well motivated, but the rationale behind the first few were less clear.

4. The authors claim that the firing rate changes in ACC are not reliably related to LC activity, yet the effects appear significant when monkeys are combined? As the authors know, short times scale firing rate correlations (and cross correlations) even in anatomically connected areas are very hard to detect but nonetheless could be real. I think the authors need to take these effects into account to make a convincing case that the other effects they focus on cannot be explained by small population level shifts in rate (or also particularly in fano factor which is highly relevant to population level correlations). I believe this is in their data but it should be fleshed out and the above points should be discussed.

5. Two conceptual points were raised that should be addressed in the discussion or elsewhere:

a. It is reported that LC phasic activity related to bottom up salient cues (e.g. "surprise" or "startle") increases correlations in ACC, so does this mean the ACC is able to encode less information during surprising events as would be predicted by most theories of correlated activity and information coding in cortex? This has interesting implications for ACC functions, if true.

b. The current literature on LC is very preliminary and theoretic. Precisely, while strong assumptions exist about what it encodes, we don't know if it encodes RPEs, surprises, intense sensory events, higher order RPEs (e.g. some belief state violation related signal), etc. It looks like it is likely complex, however the present task is very simple and may miss important nuances in the LC-ACC network. It is important to point this out and explicitly indicate early in the paper that the procedure is meant to "elicit" LC firing states, rather than test what Lc encodes.

6. It was concluded that LC activity has a context-dependent effect on ACC rsc, increasing it during passive viewing, but not changing it with LC activity is evoked by a surprising event. However, this conclusion is based on comparing post-stimulus ACC rsc to the pre-stimulus baseline, which does not rule out the alternative interpretation that ACC activity before a surprising event predicts the likelihood of an LC spike. To elaborate, it seems like there is largely a change in the pre-beep, baseline ACC rsc in this data. This would imply that elevated ACC rsc before beep trials predicts no phasic response in LC. If so, the decrease in ACC rsc after LC might be a simple homeostatic effect (i.e. due to the tendency to return to baseline), rather than a context-dependent effect of LC spikes on ACC rsc. Did the authors consider this alternative model? Further, the paper does not show that the pattern of ACC rsc after a surprising beep is any different following an LC spike than it is in the absence of an LC spike.

7. In Figure 8, it's not clear if the effects are due to the fact that beep-evoked changes are happening over longer time scales or if they're happening at different latencies relative to the beep (i.e. the longer bin sizes are ambiguous here). The latter seems most likely, given that there's no change in the peak of the quenching with LC spikes, but it would be helpful to clarify this point.
