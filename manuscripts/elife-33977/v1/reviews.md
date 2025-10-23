# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33977.039](https://doi.org/10.7554/eLife.33977.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Laminar-specific cortical dynamics in human visual and sensorimotor cortices" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Tobias H Donner as the Reviewing Editor, and the evaluation has been overseen by Richard Ivry as the Senior Editor.

The reviewers have now discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript investigates brain rhythms in humans and focuses on laminar differences. Several studies in non-human primates have shown that the cortical layers differ with regard to the strength of alpha-beta and gamma rhythms, respectively. Also, inter-areal Granger causality in those bands is related to inter-areal connections with their typical laminar projection pattern, and this has been found also in human subjects. Some of the authors have recently developed a technique for stabilizing subjects' heads in the MEG. In the current manuscript, this technique is used to investigate whether the laminar difference in the strengths of alpha-beta and gamma rhythms can be found in human subjects. MEG data of several subjects is obtained, while they perform a visual or sensorimotor task. A generative model is constructed for each subject based on a surface mesh including both the white matter and pial surfaces. Indeed, the results show that alpha-beta is stronger on the white-matter mesh and gamma stronger on the pial mesh.

Essential revisions:

All reviewers agreed that your study addresses an important and timely issue in systems neuroscience. They also agreed that your methods are overall strong and innovative, and that your findings are interesting. That said, your goal is very ambitious, and all reviewers felt that further important control analyses were necessary to make your claims fully convincing.

1) Further steps to address the SNR confound.

The most important concern shared by all reviewers is the potential SNR confound: The white-matter mesh is on average more distant from the head surface than the pial mesh, and source estimation can be influenced by this distance to the head surface. Laminar MEG analysis is biased toward superficial laminae as a function of SNR (Bonaiuto, 2018), and SNR differs between different rhythms. You partially address this issue by showing similar laminar specificity for beta decreases and beta rebounds. However, this does not fully remove concerns about differences between different rhythms because power is generally larger in the beta-band than in the gamma-band.

The reviewers converged on the following three points for addressing this concern.

1a) An analysis of pairs of vertices, with each pair containing a pial and a corresponding white-matter vertex.

Across all those pairs, the white-matter vertex is almost certainly more distant from the head surface than the pial vertex. However, there are many pairs, for which the white-matter vertex is closer to the head surface than the pial vertex. This can be seen e.g. in Figure 3A and Figure 4—figure supplement 1B. You should test, whether also for those pairs, the laminar preferences of alpha-beta and of gamma hold.

1b) A test of whether laminar preferences are correlated with distances from head surface. You could e.g. derive for each vertex pair two laminar indices, one for power and another for distance from head surface, and then correlate those indices. Ideally, there should be no such correlation, because there is no reason to assume that the physiological specificity of rhythms for layers is related to whether the respective cortical patch is on the surface, or in a sulcus with a reversed distance-to-surface relationship. In fact, Buffalo et al., 2011 have shown that the laminar specificity for rhythms holds both on the surface (V1, V4), and in the depth (V2), where laminar distance from the head surface is reversed.

1c) Showing the full cortical distribution of the laminar bias estimates.

Please show plots like Figure 3B bottom, but for the data in Figures 4 and 5. The laminar-bias (pial-whit matter t-score) is the key measure for the present study, which is assessed all over the cortex. The result of this analysis should be shown. Relatedly, you should show full slices of beamforming on a regular, high-resolution grid. This will help assess the true resolution and spatial structure of the source-estimate, including potential laminar effects.

2) Elaborate on the generative inverse solution (EBB) used here. This technique is obviously crucial for assessing the validity of the present findings. Reviewers felt the explanation needs to be clarified. For example, what are the temporal modes in the subsection “Source reconstruction”? Also, the rest of the description (– hyper-parameters? covariance priors? why can the sensor level covariance be assumed to be an identity matrix? etc.) requires more detail. When expanding this description, please do this with the following question in mind: Can any of these points affect the laminar estimates differentially for the different frequency bands?

3) Discuss the patch-size confound that was shown in Bonaiuto et al., 2018.

The reported laminar bias may reflect the patch-size dependent laminar bias of the employed method. In their previous publication (Bonaito et al., 2018), you did not only demonstrate a SNR-bias, but also a patch-size bias. Laminar estimates were biased towards superficial and deep sources depending on the mismatch between the size of estimated patches and the local dispersion of current flow. The local correlation structure differs between alpha and gamma-band activity, which in turn may induce a laminar bias. This potential problem should be discussed.

4) Present group-level statistics throughout the paper. The manuscript presents t-statistics separately for each of 8 subjects. You should perform additional tests, in which subjects are combined. For some effects, this is done, e.g. in the last paragraph of the subsection “Deep sensorimotor beta scales with RDK motion coherence and cue congruence”, however, it should be done throughout.

5) Further characterize time-frequency representations (TFRs) of visual stimulus responses. TFRs of the group average power modulations (sensor level) should be shown before proceeding to the laminar results (Figures 3-5). You only show the TFRs from a single participant (Figure 2), and in this participant, the gamma-band responses to RDKs and cue are not so compelling. Especially the responses to the sustained RDK presentation do not seem to replicate the sustained stimulus-induced gamma-band responses from earlier MEG work. Do the group average TFRs show stronger visual gamma-band responses? Are those statistically significant (within and/or across participants)?

6) Please change the color scale in Figure 4.

The color maps in Figure 4 are asymmetrically compressed such that effects in the reported and unreported direction are mapped more onto colorful and black colors, respectively. This might bias appearance of the data towards the reported effects.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Lamina-specific cortical dynamics in human visual and sensorimotor cortices" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Tobias Donner as the Reviewing Editor and Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with the Reviewing Editor, who has drafted this decision to help you prepare a revised submission.

Summary:

We have provided a summary of your paper in the decision letter for the initial submission. Both reviewers and the Reviewing Editor were impressed by your thorough revision of the paper and your detailed replies to the reviewers' comments. You have addressed all of their previously raised concerns, which has substantially improved the paper. We are happy to inform you that we would be happy to publish your paper at eLife, in principle, provided that you will address some outstanding issues detailed below. In general, both reviewers felt that some of your statements and conclusions would need to be toned down, to more accurately reflect the results of the new control analyses. This is particularly important, given the strong impact that your paper may have on the community. In addition, reviewer #3 thought that your control analyses exposed a few important issues that would need to be discussed.

Reviewer #3 also suggested some additional control analyses that might help rule out these concerns. We leave it to you to decide whether or not to include these analyses in your revision.

Essential revisions:

1) One major concern is that the reported superficial bias for gamma might reflect the dependency of the estimated depth-bias on relative leadfield-strength (pial vs. white matter), in combination with the higher proportion of stronger pial lead-fields and a low SNR for the gamma-band.

Figure 5—figure supplements 5, 6, 7 and 8 are important in this respect. The new result that the alpha/beta depth-bias does not invert for pairs with stronger white-matter lead-fields is important and re-assuring. This corresponds to the negative offset of the regression fits in Figure 5—figure supplement 6B for alpha/beta. This finding provides compelling evidence for a general deep source of alpha/beta.

However, the situation is different for gamma. First, there seems to be hardly any visual gamma response to the RDK stimuli to begin with (see point 2). Second, the regressions in Figure 5—figure supplement 6B (and corresponding correlations, Figure 5—figure supplement 5A) run through the origin (0,0). Thus, there is no general superficial bias for gamma (no offset) if lead-field strength is taken into account. For stronger white-matter lead-fields, the depth bias reverses. Indeed, sensorimotor gamma shows this reversal effect with a deep gamma bias for vertex pairs with stronger white-matter lead-fields (Figure 5—figure supplement 8). The fact that the depth bias does not reverse for vertex pairs with stronger white-matter lead-fields for all other gamma effects does not provide evidence against this interpretation because the number of vertices and the lead-field bias is much lower for pairs with stronger white-matter lead-fields. Together, this suggests, that the general superficial bias of gamma does – at least to a large extent – reflect a confounding effect of the higher proportion of pairs with stronger pial lead-fields, rather than a genuine superficial bias. It is not clear how, then, you can argue for a superficial gamma bias without a significant offset in Figure 5—figure supplement 6B. (You can argue that gamma is generally "more superficial" than alpha/beta.)

In the revision, you should clearly discuss the meaning of (i) the absence of an offset effect for gamma in the correlation analyses (Figure 5—figure supplement 6B), (ii) the biasing effect of a higher proportion of stronger pial lead-fields (marginal in Figure 5—figure supplement 6B), (iii) the reversal of the depth bias for sensorimotor gamma, (iv) the limited statistical inference that can be drawn from an absence of reversals for smaller number of patches.

2) There is no clear visual gamma response during RDK presentation in Figure 3, and there are no quantitative results reported in the text. This is not sufficiently reflected in your description of Figure 3, which should be changed. Furthermore, in this figure the significance mask often directly connects negative and positive effects. How is this possible? One would expect non-significant time-frequency ranges between ranges with significant positive and negative effects. This should be clarified.

3) The concern remains that the reported differences between alpha/beta and gamma are related to SNR-differences between frequencies. First, as mentioned before, the trial omission may not be a sufficient control for this, because omitting trials does not change the mix between signal and noise in the raw data. Indeed, the results caused by this procedure seem rather different than the SNR effects that you reported previously based on mixing signals with variable levels of noise (Bonaiuto et al., 2018). In these previous simulations, lowering SNR by adding noise induced a superficial bias, which does not seem to be the case for the present procedure. You should explicitly mention and discuss the difference and potential drawback of the trial-omission procedure in comparison to the previously applied method.

4) The new figures that show the cortical distribution of the depth bias (Figures 5 and 6) reveal cortical bias-patterns that seem to match the gyral pattern of the brain. In fact, often the depth bias even seems to reverse (superficial vs. deep) depending on the position along the gyri and sulci. This is particularly apparent for all the global effects in Figure 6. Thus, there seems to be a rather strong correlation between the average depth (or lead-field strength) of a vertex pair and its depth bias, which would not be physiologically plausible. This observation is not mentioned. You should discuss it, and comment on whether or not this is problematic.

5) You report that the gamma superficial bias did not increase with SNR for shuffled sensor data (subsection “Sensorimotor beta and gamma originate from distinct cortical laminae”, last paragraph). In contrast, Figure 5—figure supplement 4 shows a stronger superficial bias for high number of trials for gamma and shuffled sensors (gray lines rising towards the right). Do you mean "with lower SNR"? This needs to be clarified.

6) As noted previously, the argument is not valid, that a deep localization of beta during the pre-response suppression and during the beta-rebound is evidence against an SNR confound (subsection “Sensorimotor beta and gamma originate from distinct cortical laminae”, fourth paragraph). Beta is relatively lower during the suppression than during the rebound, but during both intervals absolute beta power is still much larger than absolute gamma power. It is this absolute power level, which is relevant for potential SNR confounds. The argument should be rephrased or removed altogether.

7) You performed a quantification of the cross-session reproducibility. However, it seems that only the results for one subject are reported (subsection “High SNR MEG recordings using individualized head-casts”, last paragraph). The population results should be reported as well (e.g., mean +/- std).
