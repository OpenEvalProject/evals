# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68393.sa0](https://doi.org/10.7554/eLife.68393.sa0)

This work examined a long-standing technical and conceptual question in systems neuroscience: can artificial perturbation of primary sensory cortex (in this case V1) mimic the perceptual effects of natural sensory stimulation? This technically impressive work combined optogenetics and visual psychophysics in monkeys to show that certain controlled patterns of V1 simulation can recapitulate a relatively simple visual perceptual effect involving visual masking. The results provide a proof-of-concept for a new set of approaches for studying the neural basis of visual perception.


---

# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68393.sa1](https://doi.org/10.7554/eLife.68393.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Similar neural and perceptual masking effects of low-power optogenetic stimulation in primate V1" for peer review at eLife. Your article is being evaluated by 2 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

Essential revisions:

1. There were concerns about your interpretation of your results in terms of "a sublinear interaction between visual and optogenetic evoked V1 responses" without knowing/considering the relationship between the calcium signals you measured and the underlying spiking activity. You will see that one reviewer requests additional imaging experiments with simultaneous electrophysiological recordings to measure a) the linearity of the relationship between the calcium signal and spiking activity and b) what fraction of cells show network-mediated suppression (as opposed to expected excitation). Upon discussion, the reviewers agreed that such measures would be helpful but are not necessarily crucial. Instead, there may already be information about this particular calcium indicator in the literature, and it was felt that only a small fraction of neurons were likely to be inhibited by the excitatory opsins. It is requested that you consider these factors (particularly the calcium/spiking relationship) more explicitly in your analyses.

2. Show the results of the neural and behavioral data for the power titration experiments.

3. Present the behavioral data with and without the bias-correction and include a figure with the false-alarm rates.

4. Include details about the receptive field properties of the stimulated neurons.

5. Expand the descriptions of the various methodological details (virus injections, behavioral bias-correction methods, etc.).

6.Consider the possibility that the behavioral impairment involves higher-level processing (e.g., where an optogenetically induced percept interferes with visual processing).

7. Consider addressing more directly the nature of the visual percept produced by the optogenetic stimulation. For example, it was suggested that it would be useful to compare the optogenetically induced mask with a purely visual mask. We are not requiring such additional experiments but raise them as a possibility to consider, because it was thought that they would be extremely helpful in providing an approximate measure for the brightness of the optogenetically induced visual percept.

Please see below for more details.

Reviewer #1:

The monkeys were trained to detect a target with or without optostimulation of neurons of which the receptive field overlapped the target. The optostimulation impaired target detection and strongly reduced the Ca population response to the visual target (assessed by the difference between the response to the combined opto- and visual stimulation and optostimulation-only). They interprete the reduced visual response with optostimulation in terms of a nonlinear masking effect. Basically, it is the same effect as described previously in terms of divisive normalization in a combined recording- optostimulation study (Nassi et al., Neuron, 2015). However, several issues make the interpretation of the current data difficult. First, it is unclear to me to what extent the relationship between the spiking responses and the measured Ca signal is linear. If this relationship is nonlinear, then it is not straightforward to assess the non/sub-linearity of the spiking activity using the Ca signal. Second, previous optogenetic studies in visual cortex showed that some neurons are excited by optostimulation while others show inhibition, likely resulting from inhibition by interneurons receiving excitatory input from the optostimulated pyramidal neurons. The population Ca signal in the present study may thus reflect a quite heterogeneous set of different responses to the optostimulation and visual stimulus, which makes an assessment of the response of neurons to the different stimulation conditions and linking it with behavior not trivial. Both these concerns can be addressed by having single unit ephys recordings in addition to the Ca population signal. Third, the title of the paper suggests a similar behavioral and neural effect of optogenetic stimulation. Indeed, both read-outs show an impairment of visual responses with optogenetic stimulation, but the similarity ends when making a quantitative comparison of the two read-outs since the behavioral effect is weaker than the neural one. The authors discuss the possible reasons of this incongruency of the behavioral and neural effects. Again, to sort this out laminar ephys would help, e.g. to see whether neurons not affected by the optostimulation, e.g deeper than those generating the Ca signal, could support the behavior.

In sum, this work presents a technical advance in nonhuman primate neurophysiology but its conceptual advance is limited.

1. More information about the data analysis of the behavioral results should be provided. The authors employ a go- nogo task which is known to suffer from response biases, which can differ between animals. The authors present bias-corrected % correct values in Figures 3 & 4 but do not explain how these were computed. In fact, I find it difficult to understand how monkey L can have bias corrected values of 100% at contrasts below 20% when the hits and correct rejections are lower than 100%. Please explain. Also, the same Figures show normalized detection thresholds. I assume that these were normalized to the detection threshold for the visual-only condition, but what do the error bars then represent for that condition (since all normalized thresholds for the visual-only condition are 1)? Please clarify. How was d’ computed (to obtain criterion bias values) when correct rejections were 100% (or false alarms 0%)? Please provide more details. Why was the β (steepness) parameter fixed for the optostim and visual-only conditions when fitting the psychometric curves?

2. I applaud the use of the control in which the visual stimulus was presented at the GCaMP-only site. Were these tests done interleaved with the sessions in which the C1V1-site was stimulated with the visual target? If the control measurements were run after the C1V1 site experiments, can the authors then exclude that the smaller behavioral effects were because the monkeys learned to ignore or were less distracted – to some extent – by the optostimulation?

3. The authors should provide the size of the fixation window.

4. A statistical clarification: the authors write that "Statistical comparisons in Figures 3 and 4 are made between bootstrapped distributions, using two-tailed, unpaired Student's t-test.". But the bootstrapped distributions are distributions of means and thus how can one employ than a Student-t test?

5. Supplementary Figure 5: I am confused about the legend and what is represented in this Figure: are blank trials meant to be visual-only trials?

Reviewer #2:

This study is commendable for the high degree of technical difficulty in executing the experiments to demonstrate an all optical interface to both record and modulate neural activity in awake, behaving non-human primates. They combine widefield fluorescence imaging and optogenetic stimulation while monkeys perform a visual task. The authors claim that their use of low opto power is novel, but this has been done at least once before in monkeys (Ju et al., 2018; ref [4] in the manuscript; a direct comparison with Ju et al. 2018 would be helpful).

The authors ask two main questions. First, whether low-power optogenetic stimulation ("optostim") of primary visual cortex will produce a psychophysical masking effect similar to a visual mask of increased background luminance. Second, they ask whether the interaction between the optostim and the visual stimulus interact sublinearly, consistent with contrast responses in V1.

Monkeys performed a visual detection task while optogenetic stimulation and optical read-out of neural activity was performed, and were rewarded for correctly detecting the visual stimulus, regardless of the optogenetic stimulation condition. On optostim trial blocks, animals had to report the trials in which a visual stimulus was present. Optostim was applied in blocks of trials, rather in a randomized manner. The main findings of the study are that indeed, activation of a population of neurons in V1 does interfere with perceptual reports of a visual stimulus and that stimulus responses are reduced in the presence of optogenetic stimulation. The strong behavioral effect produced using optogenetics in NHPs is important and novel, and has generally been difficult to achieve. This aspect, however, is unconvincing and, unfortunately, buried under the less novel finding of sublinear combination of visual and optogenetic stimulation.

While technically adventurous, the composition of this manuscript is problematic on several scales ranging from the writing to the interpretation of data and the absence of critical information to support their conclusions. Structurally, I am unsure whether this paper is intended to be a methodological description of a novel "toolkit" in NHPs or the report of a scientific finding. It seems to walk the line between both genres, but leaves out crucial information necessary for the detailed understanding of each aspect. The authors might consider writing this as two manuscripts – one that describes the novel toolkit in detail (and how it compares with Ju et al. 2018), which would be helpful to anyone trying to implement it, and another that describes the findings, building upon the group's recent study of the masking effects of natural backgrounds (Bai et al., 2021). Most importantly, however, there are several missing pieces of information that are necessary to evaluate whether the study's conclusions are adequately supported by the data.

1. Why is low-power stimulation used? The rationale is not clearly explained at the start of the paper, but appears to be due to the fact that the wavelength used for GCaMP excitation can also activate C1V1 – the "read" channel is also "writing". To reduce this crosstalk, the light power was reduced from about 1mW/mm^2 to 0.01mW/mm^2, deduced from pilot experiments.

"Pilot detection experiments revealed that, due to the broad excitation spectra of C1V1 [14], the blue GCaMP excitation light can affect the monkey's detection performance. We therefore minimized the blue light level to ~0.01mW/mm2 by running the camera at a low frame rate (20 Hz) and at very low saturation level (see Methods). At this low light level, we did not observe any perceptual effects of blue light illumination… Therefore, under the conditions tested here, the cross-talk between the optical "read" and optical "write" components in our system is negligible."

This is a critical issue, and it is unfortunate the authors do not include any supplementary figures showing the results of these pilot experiments used for the power titration. For this to be a viable tool, it is imperative to demonstrate that the 'read' channel is not also inadvertently 'writing', and to show the threshold at which this is no longer an issue. The authors also need to show (or at the very least quantify) how the behavioral detection performance was affected prior to the power reduction.

2. The authors conclude that "Concurrent optostim and GCaMP imaging revealed that the decline in behavioral detection sensitivity could be attributed to sublinear interaction between the optogenetically and visually driven neural responses in V1; i.e., responses evoked by the visual target decrease significantly when riding on top of an optostim-driven response pedestal."

Does the optogenetic stimulation produce a visual percept, similar to electrical microstimulation of V1? An alternative explanation that cannot be ruled out based on the provided information is that the optogenetic stimulation is producing a phosphene (a visual percept due to the direct stimulation of cortex), and that interferes with perceiving the visual stimulus. The perceptual impact of optogenetic stimulation can be inferred by the false alarm rate associated with optogenetic stimulation in the absence of a visual stimulus (0% contrast). Unfortunately, the authors never show or quantify the false alarm rates for either animal. These data points are also puzzlingly absent from the psychometric curves for contrast 0%. On page 12, the authors write "In this monkey (monkey T), optostim caused mainly an increase in the false alarm rate and a smaller drop in hit rate, and a significant reduction in the monkey's detection criterion." This increase in false alarm rate suggests the monkeys are seeing something in addition to the visual stimulus that could be confusing or distracting. Further, there is no comparison of the saccade trajectories between the optostim and visual stimulus only trials. This could provide some clue as whether/how the optogenetic stimulation is subjectively perceived by the monkey.

I don't see it as a problem if the data suggest that optogenetic stimulation induces a visual percept – this is quite interesting in fact – but it does pose a problem for the authors claim that the change in detection performance is attributable to the reduced stimulus response in the optostim condition. This issue is further complicated by the results of stimulating the GCaMP-only site (Figure 4), which also seems to show significant changes in detection thresholds (Figure 4D,I). This suggests that distraction/confusion could underlie some of the behavioral effects at the C1V1 site as well. To substantiate the argument that the behavioral effects are spatially specific, the authors should directly compare the threshold and criterion changes between the C1V1 and GCaMP-only sites. If the data suggests a phosphene, it would be helpful to attempt to delineate the possible size of such a percept given the receptive field boundaries of the stimulated sites, and then to compare it to the size and location of the visual stimulus.

Particularly since the authors are interested in the implications for neural prosthetics, there should be a more nuanced and careful consideration of all the possible reasons for the changes in detection performance, including evidence for and against the possibility of a phosphene. It would also be useful to see the raw behavioral data to better gauge the strength of the detection impairment the effect of the bias adjustment (i.e.Figure 3C,H).

3. The viral injection methods are inadequately described. What was the total volume of virus and spatial arrangement of injections? This is needed for approximating how many neurons are being activated by the stimulation to produce the psychophysical mask.

4. Similarly, basic stimulus response properties (receptive field location, optimal stimulus properties) of the activation and control sites are minimally described but critical to interpreting the results. It would be helpful to the reader to make these properties as obvious as possible, particularly since there are substantial differences in the individual monkeys' behavior that might be attributable to these factors.

5. Surprisingly, there appears to be no direct comparison of the optostim "mask" to a visual luminance mask. Since the scientific question here is whether optostim can produce the same effects as a visual mask, it seems fundamental to compare the behavioral and neural changes produced by the optostim with a visual pedestal. This comparison would also help elucidate whether the sublinear interactions produced by the visual and optostim are generated by similar mechanisms as that of the visual stimulus pedestal.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Similar neural and perceptual masking effects of low-power optogenetic stimulation in primate V1" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior and Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

I am including the full comments from two reviewers, below, because they will hopefully be of use for this round of revisions. You'll see that the first reviewer is satisfied with the revisions (although their comments suggest that you might try to more clearly describe how your results relate to past studies).

The second reviewer raised more substantive points. Point 1 involves adding details that I assume will be straightforward. Several of the other points suggest new control behavioral measurements. It seems worth considering seriously the benefit/cost ratio of these measurements -- the reviewer obviously thinks they are worth doing, but I also think that perhaps citing other studies and addressing these concerns more directly in the paper could suffice.

Reviewer 1:

I have reviewed the rebuttal of the authors and the revised manuscript. I am satisfied with their replies to my comments and the revisions they made to the manuscript. There is still the somewhat puzzling result that the effects of combined optostimulation and visual stimulation have a different effect on the behavioral choices of the two animals: one animal shows a decrease in hit rate while the other animal an increase in false alarm rate. Both effects result in a decrease in percent correct with optostimulation. The authors argue that the difference in behavioral effect between the animals is due to the different criterion levels without optostimulation, but I am not sure whether that can explain all.

As in my initial review, I believe that the study is from a technical point of view impressive, but its theoretical impact is less since other studies, e.g. Nassi et al., Neuron, 2015, have already shown sub additive effects of optostimulation in the visual cortex. The present study shows a similar effect at lower power densities and provides also behavioral data.

Reviewer 2:

First off, I must say that this was an unnecessarily difficult revision to review, mostly due to figure labeling. The response letter figure labels (i.e., "Figure S8") do not match the labels in the revised manuscript (i.e., "Figure 6-supplement 2", etc.). In the end I was left to count figure legends in order to decipher which figure the authors were referring to in the letter. This may seem minor, but it was very time-consuming.

The authors have improved somewhat their manuscript with this revision. The descriptions of the animals' behavioral responses and methodological details are improved, and replacing "pedestal" with "mask" was a good choice. The additions to the discussion are also helpful.

More importantly, however, the revision does not adequately address several of my original major concerns. For instance, I understand that the original recording chambers are no longer available, however, at least 3 concerns (#2-4 below) could have been addressed with purely behavioral experiments. Disappointingly, the authors did not attempt to perform these simpler experiments, or even cite comparable studies to substantiate their conclusions. Overall, I believe that while their study is technically impressive, it is not particularly novel for the broad readership of eLife. There is a large amount of overlap with previous studies (Ju et al. 2018, Nassi et al. 2015), as originally pointed out. This study could greatly benefit from additional analysis to unravel the sublinear interactions mechanistically. As it stands, I cannot be supportive of this manuscript.

1) Overall comment 1 response: Figure 6 —figure supplement 2: I appreciate that the authors conducted another experiment to address overall comment 1. However, there is insufficient information to allow for an adequate interpretation of this figure. For example, they do not mention how this recording was performed, how many cells are included in this analysis (or is it just 1 multi-unit response?), how many trials were averaged, does the depth of the electrode correspond to the area directly stimulated by the light, etc., etc.? Was there a simultaneous GCaMP recording? Without these details the figure raises more questions than it answers.

2) Overall comment 2. Show the results of the neural and behavioral data for the power titration experiments. The authors show one additional behavioral plot, with no error estimate. They say: "we have not done a systematic comparison of performance with and without blue light. Our impression was that the monkeys' behavioral thresholds with the low-level blue light were comparable to their thresholds during training without blue light. While we cannot rule out that the blue light had some effect on the monkeys' performance, if such effect existed, it was small." This is inappropriate. I appreciate that the chambers are no longer available, but the authors could have performed purely behavioral experiments in the same animals showing that in the absence of blue light, their detection performance is equal to that of low power blue light (without optostim). The authors need to show evidence that blue light alone does not affect performance ("…, if such effect existed, it was small.").

3) Overall comment 6. Address more directly the nature of the visual percept produced by the optogenetic stimulation. The authors now emphasize in the discussion that a distinguishing feature of their study is that animals were only rewarded for detecting a visual stimulus, and not the optogenetic stimulation of V1 itself. However, this aspect is not unique to their study. Rather given Monkey T's unique behavior on the task (see point 5 below), the authors probably could have made a more direct comparison between the optostim and a visual mask.

4) Overall comment 7: regarding comparing their optostim results with a visual mask was not addressed. It is unfortunate that the authors did not perform an additional behavioral control experiment using a visual mask. In their reply they mention the discussion paragraph "Perceptual consequences of optogenetic stimulation in V1", but there is no mention other studies that used a visual mask and compare the behavioral results. This missing, obvious comparison is surprising given that one of their stated experimental questions is "(1) Can we substitute a visual mask with low-power ((<1 mW/mm2) direct optostim of the visual cortex…".

5) The asymmetry in behavioral responses between the two animals (one shows an increase in false alarms, the other a decrease in the hit rate) does stand out more in this version of the manuscript. The authors' interpretation, attributing this to differences in criterion levels across monkeys, makes sense and seems sufficient to explain the asymmetry. The main problem is that Monkey T has an unstable criterion across different experimental blocks. There are more false alarms on low vs. high contrast control trial blocks suggesting that he was adjusting his criterion level across the different trial blocks to closer match the visual stimulus (smart monkey). This problem could have been avoided had the authors chosen to randomize trials with visual contrasts, rather than presenting individual contrasts in blocks.

6) Page 14, line 272 – this sentence is incomplete: "the monkeys do not seem to be able to 272 learn to compensate for the presence of the optogenetic (Figure 2-S2)."
