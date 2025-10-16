# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22341.012](https://doi.org/10.7554/eLife.22341.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Bottom-up and top-down computations in word- and face-selective cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Floris de Lange (Reviewer #1); Geoffrey K. Aguirre (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study used fMRI and computational modeling to investigate bottom-up and top-down contributions to activation patterns in the ventral temporal cortex (VTC) while human subjects viewed different stimuli (face or text of different contrasts and phase coherences) under different task conditions (fixation, one-back, and categorization). They show that responses in human FFA and VWFA are strongly influenced by both stimulus properties and task demands. They also identify a region of the IPS as a source of attentional modulation of the VTC. Finally, they propose a template-matching model that can reasonably account for the observed bottom-up and top-down activity fluctuations in VTC. Given that analyses of these types of experimental data have typically been framed more qualitatively, the reviewers agree that a quantitative and rigorous modeling approach is certainly a welcome contribution. The model also is noted as having the virtue of simplicity.

Nonetheless, the reviewers were also in agreement that there are a number of major issues that need to be addressed, described below.

Essential revisions:

1) Scope and readability: This paper contains an ambitious number of ideas. A challenge for the reader is that the model details are the primary product of the work, yet most of these details are relegated to Methods or Supplementary Materials. Here are some suggestions:

a) Consider moving Figure 2 to the supplement. This is a nice result, but it is not needed for the subsequent modeling work.

b) Re-arrange the results to present: 1) "VTC responses depend on both stimulus properties and cognitive task", 2) "Model of bottom-up computations in VTC". Observe that this model accounts for the fixation data but not the task data, 3) "IPS is the source of top-down modulation to VTC", 4) "Model of top-down computations in VTC", 5) "Model of perceptual decision-making in IPS".

c) Provide some detail in the main text regarding each model. In particular, the primary features of the model that impacts inference should be described. For example, the fact that the category template model is generated from the stimuli themselves is quite relevant.

d) Move the DTI results to the supplement or remove. It is certainly worthwhile noting that the VTC and IPS are connected by a white matter pathway. However, Jason's prior work demonstrates the existence of this fiber tract, and the current paper simply re-demonstrates the pathway. In the absence of some (e.g.) individual difference measurement or other use of the data to support inferences beyond the mere existence of the pathway, this result is not particularly additive.

2) Connection to literature of top-down effects on contrast-sensitivity. The paper ignores a large body of work that has also tried to formalize top-down affects such as attention on contrast-sensitivity in early visual cortex of humans and monkeys. This literature has described contrast-gain, response-gain, and additive-offsets of contrast sensitivity with top-down modulation due to attention. Some connection should be made between these results and this vast literature.

Moreover, how can the results be reconciled with findings from other groups that areas such as EBA and FFA also have category-selective responses in congenitally blind people? Does it pose a problem for their framework?

3) Model analysis and comparison.

a) It would be useful to more completely explain the model comparisons, and the work that the various parameter of each model perform in fitting the data. For example, the category template model provides good fits to the fixation-response data across contrast and phase coherence. How does these fits depend on the Gabor filter bank, the category template, and/or the parameters available in the normalization step? Moreover, the authors conclude that a scaling mechanism is in place for amplification of VTC responses. The alternative models that they draw in Figure 2 seem to make qualitatively quite similar predictions. How do they arrive at the conclusion of which mechanism is most supported by the data? Formal model comparison would be useful. Finally, why don't the top-down and drift-diffusion models make use of the category template model that is fit to the fixation data? This seems like a missed opportunity. Is this because the model fits are poor or a technical limitation?

b) How general is the model for categorical representation in FFA and VWFA? The model transforms images into weightings of a V1-like representation (gabor wavelet pyramid) and then projects these onto a template for faces and text. This amounts to little more than putting a linear classifier on a V1 like representation, which would seem much too simplistic to account for known properties of invariance in high-order visual cortex to things like view angle, lighting, rotation, scale, etc. Moreover, how well can the model predict responses to non-template stimuli? Because the templates are built as the centroid of responses of the actual stimuli used, it is not surprising that it can explain the face and word responses. As the authors point out, the more important tests are for stimuli outside of those that the model is built on. In Figure 4 the phase coherence manipulation (as well as noise and some alternative stimuli) are relevant. However, the phase coherence manipulation in the data of Figure 4 look more like a step function then what the model predicts, suggesting poor fits. Moreover, the supplementary data show that the only way to save the template model for a more general set of stimuli is to basically build the templates based on what stimuli evoked half-maximal response, which is like tweaking the templates to match the responses. While the legend mentions train and test sets, which would suggest cross-validation that might alleviate some of these concerns, the details are omitted. If train and test are different sets of responses to the same presentations of images, then the cross-validation would say more about the consistency in response then whether the model generalizes to new stimuli.

c) It seems a bit unfair to compare the parameterized category template model with a uniform category model. The category model has no contrast-sensitivity and thus gives a flat response across contrast in Figure 4. How much difference would there be between models, if you just allowed the category model to be contrast-sensitive? Likewise, the category model does seem to step for phase coherence, but no description was given for this; is this because at the lower phase coherences the stimulus category cannot be discerned? Also, how is it that some of the category model fits show some decrease in response as a function of contrast for the preferred category? In general, it would be useful to move some of the supplementary material that describes the performance of other models (including for the RT data) to the main text, since the model comparisons are of central importance to this study.

4) IPS fit circularity. Despite the assurances in Methods, the top-down IPS model faces a bit of a circularity problem. The IPS region was found using a search process that sought signals that could account for task effects. It is therefore not surprising to learn (Figure 4, bottom) that these signals well fit the data. Indeed, the r=0.96 fit is a bit worrying in this regard and suggests the possibility of over-fitting. Here are some options to rectify: a) Explicitly describe the fitting as a demonstration exercise, not to be taken as independent evidence of the role of the IPS; b) Obtain data from a new set of subjects, using the IPS region identified in the initial set of subjects to replicate the result.

5) Consistency of model framing of parietal cortex. The parietal cortex is first modeled as the source of an attention signal that modulates VTC, and then also as an accumulator of evidence from VTC. Is this plausible, and can the fMRI data support this conclusion? For example, given high task difficulty, does strong activation of IPS imply strong neural activation to provide attentional control or weak but temporally extended neural activation to accumulate weak evidence?

6) Parietal cortex correlation analysis. The suggested effect of attention is posited to be a gain effect – yet when looking for the source of this gain signal, the fixation condition is subtracted off. If it really is a gain, subtraction would be expected to leave some stimulus-driven effect in the other conditions, and correlations to parietal cortex could be due in part to this residual stimulus representation.

7) Correlation is not causation. A correlation with parietal cortex and VTC modulation is reported and interpreted as a causative signal from IPS areas. But the analysis is a correlation; it does not prove which way causation goes.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Bottom-up and top-down computations in word- and face-selective cortex" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor) and a Reviewing editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The new discussion that makes connections to existing literature on top-down effects on contrast sensitivity is a welcome addition (Discussion section paragraph four). It would likely benefit readers to ascribe specific references to the various models discussed.

2) The cross-validation model comparisons could also be described better. For example, Figure 5c shows 10 models + 2 benchmarks in the fig, but only 7 are described (briefly) in the text. It would also be useful to describe the number of free parameters in each model. How do goodness of fits compare when taking into account the different degrees of freedom?

3) Figure 5: please indicate meaning of colors, arrows, etc. in the legend, not just the associated text.

4) DDM (Figure 6): It would be helpful to readers to clarify the terminology related to the decision model. A DDM has a single decision variable that has Brownian-like dynamics; here the model appears to be closer to a race between linear ballistic accumulators (three in the case of the 3AFC categorization task). It also would be useful to discuss these results in the context of a host of findings that have largely highlighted how difficult it is to use slow BOLD signals to make inferences about accumulator-like activity occurring over relatively short timescales, as in this study (see a nice discussion of these issues in Krueger et al., 2017, "Evidence accumulation detected in BOLD signal using slow perceptual decision making," J Neurosci Methods).
