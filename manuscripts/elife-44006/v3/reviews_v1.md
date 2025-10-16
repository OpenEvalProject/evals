# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute United States

Reviewers:
- Adi Mizrahi, The Hebrew University of Jerusalem Israel
- Anthony Holtmaat, University of Geneva Switzerland

## Review text

DOI: [10.7554/eLife.44006.021](https://doi.org/10.7554/eLife.44006.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Context-dependent signaling of coincident auditory and visual events in primary visual cortex" for consideration by eLife. Your article has been reviewed by three reviewers and the evaluation has been overseen by a Reviewing Editor andAndrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Adi Mizrahi (Reviewer #1); Anthony Holtmaat (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Psychophysical data suggest that the auditory and visual systems are intimately connected. This paper is about the circuit mechanisms that support these multimodal interactions. Deneux and colleagues perform an elegant set of experiments characterizing neuronal responses in specific cell types in both auditory and visual cortex to reveal a circuit that could support context-dependent integration of both modalities in the visual cortex. They find that neurons in auditory cortex that project to visual cortex are more likely to be responsive to loud sounds (and to loud sounds getting quieter). They show that these same sounds preferentially modulate the activity of neurons in the visual cortex, but that they do so in a context-dependent and layer-specific manner which depends on the ambient luminance. Some of the data are of high quality and the authors perform a range of controls that lend rigor and confidence to their study. This will be of great interest to a wide audience interested in sensory integration and cortical circuits.

However, the reviewers noted some major concerns that need to be addressed before publication. The reviewers believe that these issues can be addressed in a couple of months.

Conceptual issues:

Specificity for "loud onsets sounds" has not been demonstrated. Although the effects they describe may be stronger for loud onsets than for quiet onsets, the results seem more of a bias within a continuous distribution rather than true specificity.

Another major concern relates to the strong conclusion that the gating of context must occur in the visual cortex instead of in the inputs from the auditory cortex to the visual cortex. This does not seem supported by the data.

These concerns can be addressed by toning down the conclusions in the paper.

Essential revisions:

The concerns listed below require some changes in analysis or data presentation and possibly some experiments that can be done rapidly.

1) The authors state that the majority of V1-projecting neurons in AC originate in L5. However, when they image neurons in AC to monitor sound-evoked responses they compare these responses to L2/3 neurons. What was the rationale behind this comparison? Wouldn't it have been more interesting to compare with the 'overall' population in L5? It is critical to provide images and fluorescence traces in L5 neurons. Along similar lines, the authors do not describe all differences in the response types between V1-projecting AC neurons and the control population. It seems that cluster 7 (OFF-response type) is not present in V1-procting neurons. More histological data needs to be provided to sow which other targets the AC neurons have. This needs to be cleared up.

Also, in the realm of image analysis, the hierarchical clustering should be unpacked in a supplemental figure. How similar are neurons in each cluster? How much variance do the clusters explain etc.

It would have been more convincing to show data from mice where both V1-projecting and those that do not are imaged in the same mice (you already have the tools to do this). Imaging separate neurons in separate experiments (with and without specificity) is less compelling. It’s not absolutely necessary, but if possible, such an experiment (even for a limited number of example) could strengthen these results.

2) The new aspects of the modulation described here relate to the inhibition in darkness vs excitation in light, and the supralinear responses between perceptually matching stimuli. Therefore, the inhibitory responses need to be understood well, especially given that the 'switch' in the model strongly hinges on this finding.

However, the inhibitory effects of sound in darkness are a bit enigmatic and not very well supported by the figures. The authors provide mean deconvolved traces, but these are difficult to digest in the context of these types of responses, as this assumes that there is high baseline activity in V1 in darkness. Either there is a general but very consistent small decrease in all neurons, or a decreased response in a few neurons that are highly active under darkness – but then why the low variance.

For negative responses it is important to exclude the possibilities that technical issues have seeped in. For example, can the authors rule out changes due to vertical movements; and how much does the neuropil signal subtraction affect these responses? 0.7Fnp is a general and accepted rule for neuropil subtraction. However, neutral responses (i.e. no change) might be very sensitive to the 0.7x threshold (especially in densely labeled populations). Could the authors 'play' with these parameters to see how they affect the outcome (e.g. same analysis with and without NP correction or varying thresholds), and convincingly show at the level of individual neurons that their responses were indeed reduced?

Altogether, it is essential to provide example images of groups of neurons (preferably time lapse images) and traces of individual neurons. They should also compare baseline neuronal activity of those neurons that are inhibited versus those who are not, and possibly perform movement (z-plane) correction in images in which they have neurons labeled in red.

3) The authors try and exclude the possibility that a difference in arousal state between the dark and light trials could explain the V1 sign switching. However, it is unclear that closing one eye could simply test the influence of arousal, as this would by itself represent yet a different state of arousal. It is not simply a matter of being in light or darkness, as there are many factors in an experimental setup that determine arousal.

4) In Figure 4, the authors inhibited AC to test whether auditory responses in V1 are caused by AC projections. Where are the statistical comparisons for the DREADD experiments (n=3)? The authors report that this showed a "similar effect, but less robust" as compared to the muscimol experiment. Whereas this trend might be true for the experiments under light, this remains inconclusive for the DREADD experiments in darkness since in one animal the average responses were drastically reduced. The authors should report the statistical comparison for the DREADD experiment and increase the n if they feel that this addition is necessary to support the conclusions.

5) Why opt out of showing 'sound only' averages in Figure 6D? For unimodal stimuli was there any background stimulus in either modality (e.g. for sound only, dim light; and for light only, white noise)? If not, why is the sound-only inhibitory response in V1 (as seen in Figure 5) not reproduced in Figure 6?

6) The results of what they call context are the most interesting part of the paper. The claims of effect-specificity to loud onset sounds and looming stimuli are too strong. After all, they only tested a limited amount of stimuli, both auditory and visual. And even within this limited set, the effects are not binary.

7) The value of the minimal model of Figure 7 is unclear. Reproducing the empirical results with a model is a good starting point but eventually it has to provide something more (e.g. some hypotheses to test in the context of mechanism). Do they suggest specific biophysical mechanisms of the neurons are involved? This should be clarified.

8) The authors' major conclusion is that (from the Abstract) "a small number of layer 1 interneurons gates this cross-modal information flow". They then design a model to demonstrate how this might work through the application of distinct gain conditions and a non-linear threshold. However, another possibility (as the authors acknowledge in the Discussion section) is that the gating might occur in the auditory cortex such that the inputs to the L1 population are only active in the dark. Evidence that the A1->V1 population is insensitive to ambient light conditions would add significant support to the authors assumed model.

9) The authors' model suggests that ambient light alters the excitability (and therefore gain) of L1 interneurons. This is a hypothesis that the authors could test by measuring F in baseline conditions (in the absence of auditory stimulation) in the light and dark. Evidence that the L1 neurons that are driven only in the dark have higher baseline F in the dark (while other less selective L1 interneurons do not show such strong modulation) would significantly strengthen the authors' argument.

10 The authors' proposed model assumes a functionally homogeneous input to V1. However, while the majority of V1->A1 neurons prefer down-ramp sounds, there are still a significant number that respond to up-ramps. In fact, up-ramp sounds are sufficient to drive suppression in the dark, though unlike down-ramp sounds do not evoke either excitation or inhibition in the light (at least not on average as shown in Figure 3B). This suggests that down-ramp preferring neurons may only contact L1 interneurons and not provide direct excitation to L2/3. Thus, the authors should make it clear that there are anatomical specializations that might also support the observed gating.
