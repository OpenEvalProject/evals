# Peer review - Round 1

Editors:
- Barbara G Shinn-Cunningham, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87820.3.sa0](https://doi.org/10.7554/eLife.87820.3.sa0)

This detailed and well powered manuscript explores auditory perception of modulated noise in the presence of transcranial alternating-current stimulation (tACS) and shows valuable results suggesting that there are subject-specific effects when the phase of 2-Hz tACS varies relative to the phase of the noise modulation. The strength of the evidence is mixed. There is convincing evidence that tACS alters perception significantly in individuals; however, the effects are inconsistent across subjects and even across sessions, frustrating attempts to draw conclusions about the underlying mechanisms of the idiosyncratic effects. Despite these limitations, the paper will be of great interest to researchers interested in determining when and how tACS influences neural processes, especially those interested in neural entrainment and its relationship to perception.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87820.3.sa1](https://doi.org/10.7554/eLife.87820.3.sa1)

This paper studies the effects of tACS on detection of silence gaps in an FM modulated noise stimulus. Both FM modulation of the sound and the tACS are at 2Hz, and the phase of the two is varied to determine possible interactions between the auditory and electric stimulation. Additionally, two different electrode montages are used to determine if variation in electric field distribution across the brain may be related to the effects of tACS on behavioral performance in individual subjects.

Major strengths and weaknesses of the methods and results.

The study appears to be well powered to detect modulation of behavioral performance with N=42 subjects. There is a clear and reproducible modulation of behavioral effects with the phase of the FM sound modulation. The study was also well designed and executed in terms of fMRI, current flow modeling, montage optimization targeting, and behavioral analysis. A particular merit of this study is to have repeated the sessions for most subjects in order to test repeat-reliability, which is so often missing in human experiments. The results and methods are generally well described and well conceived. The portion of the analysis related to behavior alone is excellent. The analysis of the tACS results are also generally well described, candidly highlighting how variable results are across subjects and sessions. The figures are all of high quality and clear. One weakness of the experimental design is that no effort was made to control for sensation effects. tACS at 2Hz causes prominent skin sensations which could have interacted with auditory perception and thus, detection performance.

The central claim is that tACS modulates behavioral detection performance across the 0.5s cycle of stimulation. Statistical analysis with randomize relative phase (between audio and tACS) show that detection performance is modulated by tACS. Neither the relative phase or the strength of this effect reproduces across subjects or sessions, which makes the interpretation of these results difficult. These result could be of interest to investigators in the field of tACS.

The claim that the variation in the strength of the effect can be explained by variation of electric fields is not compelling.

The following are more detailed comments to specific sections of the paper, including details on the concerns with the statistical analysis of the tACS effects.

The introduction is well balanced, discussing the promise and limitations of previous results with tACS. The objectives are well defined.

The analysis surrounding behavioral performance and its dependence on phase of the FM modulation (Figure 3) is masterfully executed and explained. It appears that it reproduces previous studies and points to a very robust behavioral task that may be of use in other studies.

The definition of tACS(+) vs tACS(-) phase is adjusted to each subject/session, which seems unconventional. For argument sake, let's assume the curves in Fig. 3E are random fluctuations. Then aligning them to best-fitting cosine will trivially generate a FM-amplitude fluctuation with cosine shape as shown in Fig. 4a. Selecting the positive and negative phase of that will trivially be larger and smaller than sham, respectively, as shown in Fig 4b.

"Data from the optimal tACS lag and its opposite lag (corresponding trough) were excluded to avoid any artificial bias in estimating tACS effects induced by the alignment procedure (33)." The delay was found by fitting a cosine, so removing just the peaks of that cosine does little to avoid this problem.

To demonstrate that this is not a trivial result of the definition, the analysis compares this to the same analysis but with a randomize alignment to the two stimuli (audio and tACS) in Figure 4d. Assuming this shuffle was done correctly, this shows that the modulation observed in 4b is not just a result of the analysis procedure.

The authors are to be commended for analyzing the robustness of their observation across subjects and across sessions in Fig. 5. The lack of consistency in the optimal time delay between the two stimuli is hard to reconcile with the common theory that tACS entrains brain function.

"To better understand what factors might be influencing inter-session variability in tACS effects, we estimated multiple linear models ..." "Inter-individual variability in the simulated E-field predicts tACS effects" Authors here are attempting to predict a property of the subjects that was just shown to not be a reliable property of the subject. Authors are picking 9 possible features for this, testing 33 possible models with N=34 data points. With these circumstances it is not hard to find something that correlates by chance. And some of the models tested had interaction terms, possibly further increasing the number of comparisons. In the absence of multiple comparison correction, what is happening here is that multiple models are fit to the data, and a statistical test is performed for the best model on the same (training) data. The corresponding claim that variations are explained by variations in electric field is not persuasive.

"Can we reduce inter-individual variability in tACS effects ..." This section seems even more speculative and with mixed results.

Given the concerns with the statistical analysis above, there are concerns about the following statements in the summary of the Discussion:

("4) individual variability in tACS effect size was partially explained by two interactions: between the normal component of the E-field and the field focality, and between the normal component of the E-field and the distance between the peak of the electric field and the functional target ROIs."

The complexity of this statement alone may be a good indication that this could be the result of false discovery due to multiple comparisons.

For the same reason as stated above, the following statements in the Abstract do not appear to have adequate support in the data:

"Inter-individual variability of tACS effects was best explained by the strength of the inward electric field, depending on the field focality and proximity to the target brain region. Although additional evidence is necessary, our results

42 also provided suggestive insights that spatially optimizing the electrode montage could be a promising tool to reduce inter-individual variability of tACS effects."


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87820.3.sa2](https://doi.org/10.7554/eLife.87820.3.sa2)

I thank the authors for considering my comments and think the manuscript has been significantly improved with revision. However while I considered that the analysis employed for predicting tACS effects with linear models was convincing, I am still concerned by a multiple comparison issue for this analysis. An alternative option would be to report the results of a Partial Least Squares (PLS) analysis, with the stimulation properties as predictor variables and tACS effects as response variables. The authors could use PLS instead of multiple linear regression models to take into account the multicollinearity in the predictor variables, and also this can be done with only one PLS model. They could then extract the fitted responses values and estimate if the model can significantly fit the tACS effects.

Then, to determine which variables contribute more to the prediction, they can calculate the variable importance in projection (VIP) scores for the PLS regression model.

An alternative option for the authors would be to temper their conclusions regarding how well field modeling/montage explains the variance observed across subjects.
