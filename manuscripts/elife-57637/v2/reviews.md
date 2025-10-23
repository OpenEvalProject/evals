# Peer review - Round 1

Editors:
- Ming Meng, South China Normal University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57637.sa1](https://doi.org/10.7554/eLife.57637.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Sensory adaptation reflects short-term brain plasticity that optimizes the efficiency of information processing. The present study uses cutting-edge ultra-high field fMRI to examine cortical layer-specific neural basis for adaptation. Valuable new data with sub-millimeter resolution are provided to advance our understanding of mechanisms supporting adaptive processing in human visual cortex.

Decision letter after peer review:

Thank you for submitting your article "Fine-scale computations for adaptive processing in the human brain" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study investigates the neural mechanisms of adaptation in human visual cortex with ultra-high-field fMRI. The stimuli were gratings that either had the same orientation repeatedly presented (adaptation) or gratings of different orientation repeatedly presented (non-adaptation). Attention was maintained at fixation throughout with a rsvp task. A primary claim is that adaption is stronger in superficial depths in visual areas V1 through V4, but is not modulated with depth in IPS1 and IPS2. Functional connectivity analyses are used to assess the relative strength of feedforward and feedback connections between the regions studied during adaptation, indicating enhanced feedback connectivity from IPS to V1 and enhanced feedforward connectivity from V1 to V2, V3, and V4 during adaptation. The study combines cutting-edge imaging techniques with clear experimental design and careful analysis to make an important and valuable contribution to our understanding of mechanisms supporting adaptive processing in human visual cortex.

Essential revisions:

Assuming that a direct physiological measure (e.g., spikes) for the present study at this time is difficult, some additional psychophysical experiments would be needed to successfully address reviewer #3's first main concern. Adding some psychophysical experiments would also help to address comments from reviewer #2 better than just adding analyses and tempering claims.

Reviewer #1:

1) The study overall did not add much new evidence that may advance our understandings of feedforward and feedback processes in the visual adaptation, and the reported results were to some extent predictable from previous studies (see review, Lawrence et al., 2019; Self et al., 2019).

2) The authors claimed higher functional connectivity between V1 deeper layers and IPS, however, the reported analysis showed that the difference in adaptation and non-adaptation conditions between V1 deeper layers and IPS1 just reached the significance (p =.049), while that in V1 deeper layers and IPS2 was not significant (p =.281). I feel that these results were not strong enough for the authors make the solid conclusion on the significant difference between adaptive conditions. Also, I noticed that the IPS region was defined using anatomical templates, did the authors included functional localization scan for the IPS regions? In addition, the above analyses were between V1 deeper layers and the overall IPS1 and IPS2 respectively. According to the model (see Figure 1 in the manuscript), the feedback connection was between V1 deeper layers and IPS deeper layer, so the functional connectivity analyses should be conducted between the deeper layers of V1 and deeper layers of IPS1/IPS2. Given that the manuscript has reported the significant different neural responses in different layers of IPS1 and IPS2, so I suggest that the authors do additional analyses on the functional connectivity between V1 deeper layer and IPS1/IPS2 deeper layers, and the results would provide more specific and stronger evidence on the feedback connections in visual adaption.

Reviewer #2:

My concerns fall into two broad categories: 1) that the statistical tests employed in this work don't sufficiently support the authors' claims, and 2) that, even when properly analyzed, the data presented here are insufficient evidence for the circuit-level conclusions presented throughout the manuscript. The authors could improve the evidence and present interpretations that are more closely tied to the data.

Conceptual

1) The language used does not adequately clarify the differences (and potential lack of alignment) between cortical depths and cortical layers. For example, the claim that "UHF imaging affords the sub-millimetre resolution necessary to examine fMRI signals across cortical layers" is not strictly true. Even at the small voxel size used here, cortical curvature, variable thickness, and partial volume effects all make it extremely challenging to map cortical depth to physiologically-distinct cortical layers. This distinction is critical given the motivation of this work as dissecting feedforward and feedback projections.

Suggestion: avoid the term "layer" and instead use "depth", and clarify in the manuscript that inferences about cortical layers, and thus, alignment to existing anatomical models of feedforward and feedback projections is limited.

2) It's not immediately clear how one should combine the functional connectivity and adaptation results into a single framework for thinking about mechanisms of adaptation. Is it possible, for example, that other regions (besides IPS1, IPS2, V2, V3, and V4) feedback to V1 and contribute to suppression? Is the strength of the IPS feedback during the adaptation condition predictive of the amount of adaptive suppression? Conducting these additional analyses would strengthen the authors' claim that top-down feedbacks from the IPS contribute to the adaptive processing reported in visual cortex.

Suggestion: (i) Compare the degree of feedforward and feedback connectivity between conditions for a control region, e.g., hMT+, to demonstrate that IPS is uniquely (or especially) involved in these computations. (ii) Demonstrate that the amount of feedback from IPS correlates with the amount of adaptation in deeper cortical depths in V1 across individual subjects, and (iii) Elucidate it this feedback from IPS that is correlated with adaptation is specific to V1 or occurs to other visual areas that show adaptation (V2, V3, V4).

Data Analyses and Validation of Results

1) The reporting of ANOVA results of differences in adaptation across ROIs and depths throughout the paper is confusing. It is unclear whether a) separate ANOVAs were run to test each effect (main or interaction), or b) that the results of the ANOVAs are misreported. For example, consider the ANOVA reported which tests the effects of ROI, depth, and condition on z-scored BOLD responses. The degrees of freedom (3, 39), indicates that there are four levels to the factor of interest (four ROIs), and 40 total measurements. Where does 40 come from? If there are 15 subjects and each contributes 12 data points (4 ROIs x 3 depths), I would expect that the variance being analyzed is that of 15 x 12 = 180 data points. Then, the next result presented is the main effect of condition, which has a reported (1, 13) degrees of freedom, suggesting that a different model was fit.

Suggestion: Run a single ANOVA and report main effects and interaction terms from that analysis.

2) The authors claim that adaptation is stronger in superficial V1 than in other cortical depths in the Introduction but write "visual cortex" instead of "V1" or "primary visual cortex" elsewhere. It is unclear when the authors are claiming that the result applies to V1 and when it applies to V1 through V4 in aggregate. This is problematic for three reasons. First, the claim being made should be clear, and the Introduction and Discussion should reflect the scope (V1 or V1-V4) intended. Second, if the authors claim is that suppression is stronger in superficial V1, a post-hoc test with appropriate multiple comparisons correction is needed. The tests are insufficient in that they don't compare superficial to middle depths directly, and in that they aggregate across all four ROIs instead of testing V1 separately. Third, if the authors claim is that suppression is stronger in superficial V1 through V4, then the direct comparison of superficial to middle depths is still lacking. Furthermore, the framing of the rest of the paper which compares V1 connectivity to IPS and V2-V4 and discusses V1 in the Introduction and Discussion needs to be justified if V1 is no different from V2, V3, and V4.

Suggestion: Make the claim being made clearer, then compute the appropriate statistical tests to support that claim. If needed, revise the Introduction and Discussion to explain special attention paid to each ROI.

3) In relation to point (2) above, they claim that adaptation is layer specific rests on the results of post-hoc tests. However, it is unclear (i) which ROIs are tested, and (ii) why they are comparing superficial and deep as well as middle and deep but not superficial and middle. Further the Materials and methods indicate that pairwise t-tests were used, if so multiple comparisons correction is needed to validate the result.

Suggestion: The authors should conduct all tests and clarify the reporting of the results. If multiple-comparisons correction is not currently being used, the authors should employ either Tukey's Honest Significant Difference, Bonferroni correction, or an alternative correction. If the tests are already corrected, that fact should be reflected in the Materials and methods section.

4) The inclusion of GRASE results strengthens the work substantially. However, the claim that the same adaptation patterns are observed are not supported numerically. In fact, the results presented in Figure 3—figure supplement 2 suggest that adaptation is not stronger in superficial than middle or deep depths, and that the correlation between adaptation indices across scan sequences (panel B) are moderate; at most, the adaptation indices from one scan sequence predicts 22% of the variance in the adaptation indices from the other scan sequence.

Suggestion: Report statistics for the 3D GRASE results.

Reviewer #3:

The motivation and framing is to characterize "circuit properties of adaptation" but I have two issues with this. First, is the inference that neural adaptation is occurring. Yes, the signal is smaller when stimuli are repeated vs. when they are not, and this is *consistent* with adaptation. But, the origin(s) of fMRI repetition effects is controversial. Without a secondary measure – e.g., psychophysical evidence of adaptation (e.g., reduced sensitivity, tilt aftereffect, etc) in the adapted vs. non-adapted conditions or a direct physiological measure (e.g., spikes) – all we can say is that the fMRI signal is reduced during repetition. What I think this paper does a great job of doing is the set up for an experiment that specifically examines adaptation – for example, is there a specific layer-response that best predicts psychophysical differences in adaptation?

The second issue is the inferences that are made between depth and feedback/feedforward processing. Take, for example, a measured difference in superficial layers. I don't understand how it is possible to know whether a change in the BOLD signal in superficial layers is due to neurons in these layers being affected by within-area circuits (e.g., from known connections between middle-layers to superficial layers) or due to feedback-mediated effects (as feedback affects both superficial and deep layers). In light of this, it's difficult to parse the first paragraph of the Discussion. "First, visual adaptation is implemented by recurrent processing of signals in visual cortex, as indicated by fMRI adaptation (i.e. BOLD decrease due to stimulus repetition) across layers with stronger effects in superficial than middle and deeper layers." What does "recurrent processing" mean here? If it means "feedback" shouldn't deeper layers have stronger effects? Does it mean with-area processing (middle/input -> superficial/output). Overall, I find the report of layer-specific responses interesting but I cannot infer the level of "circuit properties" the authors' wish to ascribe to the effects.

Along similar lines, as a way to refresh my memory of layers/connections in early visual cortex, I looked at this recent paper: "Anatomy and Physiology of Macaque Visual Cortical Areas V1, V2, and V5/MT: Bases for Biologically Realistic Models". It is difficult to map the relatively simple characterization presented in the current paper with the real complexity described in the Vanni et al. paper. As just one example, from Vanni et al., "FF connections from V1 to V5 arise from layers 4B (both blobs and interblobs) and 6 and target primarily L4 and less so L3 of V5." "FB projections from V5 to V1 terminate predominantly in layers 4B and 6 (Maunsell and Van Essen 1983b; Ungerleider and Desimone 1986b; Shipp et al. 1989), that is, the source layers of the V1-to-V5 FF projection." There is very little consistency between this characterization and what is depicted in Figure 1A (though, I understand these quotes are specifically about MT-V1 connections).

Reviewer #2:

1) "while feedback occipito-parietal connectivity" should be "while feedback was enhanced for occipito-parietal connectivity".

2) Introduction second sentence: This claim is lacking citations

3) Results final paragraph: why isn't IPS considered visual cortex? It's definition in the Wang et al. atlas is based on topographic representation of visual space.

Reviewer #3:

Introduction paragraph 1 and paragraph 2: plethora. Maybe don't use plethora twice.

Results: It seems like all ROIs should be in Figure 3A and remove Supplementary figure 3. All ROIs are in Figure 3B and all are included in the ANOVA. It would just be easier to refer to a figure that included all ROIs if ROIs are discussed in the ANOVA.

"Post-hoc comparisons showed significantly decreased fMRI responses for adaptation across cortical layers (deeper: t(14)=-3.244, p=0.006; middle: 126 t(14)=-3.920, p=0.002; superficial: t(14)=-4.134, p=0.001)." What are the t-tests comparing? Is that just in V1?

Error bars: Unfortunately, the error bars make it look as if there are no effects. Visually, looking at Figure 3A, I'd say the responses are identical across layers. And, I'd conclude the same about all ROIs in Figure 3B. In fact, as I write this, it's difficult to reconcile the p-values in the text and what is presented in the figures. I'm guessing the issue is the repeated-measures nature of the analysis in which case between-subject error bars are misleading. You might consider:

https://www.researchgate.net/profile/Denis_Cousineau/publication/49619408_Confidence_intervals_in_within-subject_designs_A_simpler_solution_to_Loftus_and_Masson's_method/links/54e4c9300cf22703d5bf6023.pdf
