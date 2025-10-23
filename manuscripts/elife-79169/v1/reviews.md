# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79169.sa0](https://doi.org/10.7554/eLife.79169.sa0)

This is a valuable study that aims to validate and translate an established non-invasive proxy measure of axonal diameter that is derived from magnetic resonance imaging. The results are solid, demonstrating alterations in the proxy measure in rodent models of axonal damage and patients with multiple sclerosis. The Discussion acknowledges weaknesses relating to the details of modelling and signal-to-noise ratio of the measurements. This work will be of interest to researchers studying the microstructural changes in neurodegeneration.


---

# Peer review - Round 1

Editors:
- Karla L Miller, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79169.sa1](https://doi.org/10.7554/eLife.79169.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors resubmitted a revised version of the paper for consideration. What follows is the authors’ response to the first round of review.]

Thank you for submitting the paper "A translational MRI approach to validate acute axonal damage detection in multiple sclerosis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous. We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Specifically, the reviewers were concerned that the validation is limited by not having a more direct measure of axon diameter. Moreover, the pathological mechanisms are not sufficiently well matched between the rodent model and human disease to draw strong conclusions. As such, the reviewers feel the manuscript is of value but would be better suited to a specialized imaging journal.

Reviewer #1 (Recommendations for the authors):

The rodent protocol used single-shot EPI, long diffusion times, long echo times, and low b-values. The intention would seem to be to match the rodent experiment to the in-vivo human protocol, but it doesn't account for alterations in properties in fixed tissue. It also doesn't take advantage of the better specificity that can be achieved on pre-clinical scanners with better hardware, which can provide cleaner measurements and improved estimates of biologically-relevant parameters. Some discussion of these choices is warranted.

The units reported in Figure 1d (mm) are wrong.

Figure 2 refers to "immunohistochemistry" but as far as I can tell, this study uses exclusively immunofluorescence.

Is it correct that the color code for saline vs IBO in Figure 3 is swapped compared to Figures1-2? If so, this is confusing.

Figure 4 caption notes that "The opposite contrast was not statistically significant", but as a reader I'd prefer to show this comprehensively by including the negative contrast (e.g., as a blue colormap) so I can see whether there are no regions passing significance. This will make the results that much more compelling.

Figure 5 d-e needs a label for the vertical axis.

Figure 5 caption: what is meant by "GLM followed by post hoc comparisons"?

Please provide references for all software packages (FreeSurfer, FSL, etc) in some form (DOIs, URLs or journal articles). What is meant by '(Alexander Leemans et al., n.d.)'?

Control in rodent experiments: could be made more clear that animals are intended as their own contols using two hemispheres. It is not clear in the 'Animal preparation' section that this is what is intended – this only becomes clear in the 'Data analysis' section. Is it well established that this is a robust control (e.g., that the other hemisphere is entirely unaffected)? Similarly, it is only in the 'Data analysis' section that it is clear that saline injection is used in the control hemisphere, whereas the 'Animal preparation' section refers to 'saline and ibotenic acid' as if it is a single injection.

Reviewer #2 (Recommendations for the authors):

This is an interesting paper that sets out to validate the use of AxCaliber as a non-invasive quantification of axonal diameter. This goal is of great importance, especially in the context of pathology. It seems to me, however, that they have missed an opportunity by not comparing the MRI measures with some actual axonal diameter measurement based on electron or confocal microscopy. Such measurements would significantly strengthen the paper and provide some evidence that the diffusion-derived measures reflect actual axonal swelling. It is difficult to interpret the data presented: we have evidence of neurodegeneration, which correlates with estimated axonal diameter, but it is possible that what results in increased estimated diameter might be affected by other effects, e.g., gliosis. So, while the data are very interesting, they are not conclusive, and the Authors should acknowledge that clearly, and explore alternative explanations in their discussion.

Specific comments:

1. In the abstract, the final statement should be toned down, in light of the above comments.

2. The mean axonal diameter reported for both, rats and humans, appears very large, suggesting that the modified AxCaliber is only sensitive to the rightmost tail of the distribution. Can the Authors comment on this?

3. The correlation between fluorescence intensity and axonal diameter is intriguing, but the 2 quantities measure different things. Perhaps it would be more convincing to look at the left vs right difference in both quantities – are the normalised differences also correlated?

4. For the results shown in Figure 4, please state clearly how the statistical comparison and correction for multiple comparisons were conducted.

5. On page 9, the authors state that they performed some ROI analysis – how were the ROIs picked? Were these chosen a priori or after the whole brain analysis (TBSS)?

6. Discussion: please explore alternative potential explanations than an actual axonal diameter increase. While the paper cited to support the possibility of axonal swelling or the formation of spheroids are very interesting, some of these occurrences are the consequence of axonal transaction, which can happen within MS lesions, but unlikely to occur in the NAWM. Is it possible that some kind of bias in the model leads other tissue changes to mimic axonal diameter enlargement?

Reviewer #3 (Recommendations for the authors):

1. To validate the dMRI protocol and model fitting, authors should (1) perform Monte Carlo simulations of diffusion in realistic substrates or (2) compare dMRI results with axon diameter based on histology, such as electron microscopy. Author should also perform noise propagation to evaluate the accuracy and precision of model fitting.

2. In addition to the use of strong diffusion weighting, it is also possible to maximize the dMRI signal sensitivity to axon diameter by tuning the gradient pulse width, rather than varying the diffusion time alone (time interval between gradient pulse pair). As suggested in [Neuman, JCP 1974], the signal decay due to intra-axonal restricted diffusion is roughly proportional to the pulse width and almost independent of the diffusion time.

3. To account for the fiber orientation dispersion, spherically averaged signals of dMRI could be used to estimate the axon diameter, as in [Veraart et al., eLife 2020].

4. The AxCaliber model provides not only the axon diameter estimate but also intra-cellular volume fraction. The value of the volume fraction and its correlation with the histology are valuable and should be reported as well.

5. Authors did not discuss other confounding factors of axon diameter mapping using dMRI, such as the tortuous/undulating axonal shape and the diffusivity time-dependence in extra-cellular space. Ignoring these factors could lead to overestimation of axon size. It is indeed difficult to design a model to accommodate all these factors, but they should be discussed.

6. Some sequence parameters of dMRI are missing, such as the gradient pulse width, partial Fourier factor, spin echo or stimulated echo, maximal gradient strength in animal scan, and acceleration factor of parallel imaging and simultaneous multi-slice if needed.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A translational MRI approach to validate acute axonal damage detection in multiple sclerosis" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

For this study, the experimental data and findings in animals and humans are valuable. However, Reviewer 3 notes that the interpretation and model fitting are problematic.

i) Given that the myelinated axon diameter is < 1.5 micron in histology, the observed diffusion signal time-dependence (~20%) cannot be explained by restricted diffusion in thin axons (~0.1%). Extra-cellular diffusivity time-dependence could be a more reasonable interpretation.

ii) In the response 3.5, the SNR for human and rat scans is 13.2 and 7.3 in b0 image. It is surprisingly low and hard to believe that it is possible to estimate axon size under such low SNR. Their noise propagation also shows the problem.

For the paper to be publishable, the authors will need to reconsider the interpretation and the fitted model.

Reviewer #3 (Recommendations for the authors):

The authors performed time-dependent diffusion MR and histology in the animal model of multiple sclerosis (MS) to demonstrate the correlation of MR estimated axon diameter index and histological findings. Further, they applied the same technique to MS patients and observed the axon size increase in the early event of MS. This study is of interest for researchers studying the microstructural changes in MS and neurodegeneration. The observation of correlation between histology and the diffusion time-dependence is exciting; however, the optimization of the MRI protocol design, the implementation of model fitting, and the interpretation of the observed diffusion time-dependence are problematic. The acquisition protocol of diffusion MR is not optimal for the axon diameter estimation; in fact, it is probably more sensitive to the extra-cellular MR signal contrast. The assumptions in the proposed diffusion MR model were not detailed in this study and even in their previous studies, and the signal-to-noise ratio in the data was not high enough for a reliable fitting. The observed diffusion time-dependence could be interpreted as the result of beadings along axons, packing geometry in extra-cellular space, and the water exchange due to T1 weighting alterations with mixing times of the stimulated echo sequence in animal scans. Given that the absolute value of axon size estimation was different in histology (0.7 micron) and diffusion MR (4 micron) by a factor of ~6, the interpretation of diffusion time-dependence as a result of restricted diffusion inside axons was questionable.

1. The major concern is that the sequence parameter in diffusion MR is not optimal to estimate the axon diameter. At low b-value < = 4000 s/mm2, it is quite impossible to have enough signal decay due to restricted diffusion inside axons [Burcaw et al., NeuroImage 0215], let alone detecting the signal time-dependence in intra-cellular space. In fact, at low b-value, most of the signal decay and signal time-dependence is contributed by the hindered diffusion in extra-cellular space [Fieremans et al., NeuroImage 2016]. Furthermore, the intra-cellular signal time-dependence largely depends on the pulse width, not the diffusion time [Neuman, JCP 1974]. Authors tried to cite the study of Axon Spectrum Imaging [Gast et al., Neuroinformatics 2023] to support their protocol design of varying diffusion time at low b-value. However, Gast et al. did not apply the AxCaliber model (diffusion narrowing regime) to estimate axon size. Actually, Gast et al. applied the assumption of intra-cellular diffusion in narrow pulse limit, and neglected the diffusion time-dependence in extra-cellular space, which has been shown as the dominant source of diffusion time-dependence at low b-values. This problem has been well recognized and further solved in previous studies [Veraart et al., eLife 2020; Fan et al., NeuroImage 2020], where the high b-value data (b-value > 15,000 s/mm2) were included for the model fitting.

2. Authors mentioned that, at low b-value, intra-axonal "signal" dominates. However, at low b-value, extra-axonal "signal decay/signal contrast" and "signal time-dependence" dominate (Figure 4 in [De Santis et al., 2016]). A simple calculation could indicate whether authors may misinterpret the extra-cellular signal time-dependence as intra-cellular one. For the in vivo rat MR protocol, the signal time-dependence of intra-axonal model is 20.3% for an axon diameter = 4 micron (Figure 1e) and intrinsic diffusivity = 3 um2/ms using Neuman's model, and the signal time-dependence of extra-axonal model is 19.5% for a strength of time-dependence = 0.5 micron2 using a log(time)/time model [Burcaw et al., 2015].

3. It is required to apply many assumptions to fit the modified AxCaliber model [De Santis et al., 2016b] to diffusion data with only two b-values at three diffusion times. For example, did authors fix the value of axial diffusivity in intra- and extra-axonal space? Did authors apply the tortuosity relation in extra-cellular space to reduce the number of parameters [Zhang et al., NeuroImage 2010]? What is the value of intrinsic diffusivity in intra-cellular space? How many parameters were fitted exactly in each voxel with 1-3 fiber tracts? These assumptions were not explained even in the previous study [De Santis 2016b].

4. The applicability of the model fitting at a typical SNR (~20) on Connectome scanner should be tested by the noise propagation. In the previous revision 3.5, the noise propagation was tested at only 4 diameter values, and the mean value of 104 repetitions matched the ground truth value. However, the mean value of 104 repetitions for each diameter value is the result of SNR = 20*sqrt(104) = 2000. The wide histogram of fitting result actually indicates the low precision in the model fitting. To perform the noise propagation, authors should apply many different parameter combinations (for example, 105) with diameter, volume fraction, and extra-cellular diffusivity varied in wide ranges.

5. The modified AxCaliber model was validated by the in vivo rat brain scan, where the stimulated echo sequence was applied. However, the diffusion signal measured by stimulated echo had varying T1-weighting due to the varying diffusion time and mixing time. If the non-diffusion weighted signal (b0 signal) was mono-exponential decay with the mixing time, this T1-weighting could be canceled out via dividing DW signals by b0 signal. If the b0 signal was not mono-exponential decay, the T1-weighting variation between multiple compartments (e.g., water around myelin and water away from myelin) could lead to spurious "diffusion" time-dependence that was related with T1-weighting and exchange. It is essential to confirm that the b0 signal is mono-exponential decay with the mixing time in white matter, where the b0 signal decay is usually bi-exponential with the mixing time.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A translational MRI approach to validate acute axonal damage detection in multiple sclerosis" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

It is clear that the review process is converging. As you'll see, Reviewer 3 requests a few further clarifications of the study alongside some requests for limitations to be covered in the Discussion. If you are able to make changes for each of these requested comments, then we will hopefully be able to handle these as editors without the need to return to reviewers.

Reviewer #3 (Recommendations for the authors):

The authors in general did a great job to improve the manuscript. However, some important information about the model and results was only mentioned in the revision but not shown in detail. It is essential to include these details in either Methods or supplementary materials to support their arguments in this study. More specific concerns are given below:

1. Comment R3.1: Authors performed a simple CHARMED experiment and got the value of intra-cellular axial diffusivity close to 0.7-1 um2/ms, different from the values 2.25 um2/ms in previous studies (Dhital et al., NeuroImage 2019, 189:543 and more). This is because the inclusion of multiple highly aligned fiber bundles only factors out the fiber crossing, but not the angular dispersion in each fiber bundle. This dispersion is non-trivial even in highly aligned white matter, such as corpus callosum (~ 20-25 degree dispersion in Ronen et al., BSAF 2014, 219:1773 and Lee et al., BASF 2019, 224:1469). This is the reason why people start to use the spherical mean signal to factor out both fiber crossing and fiber dispersion for the axonal diameter mapping. This should be included in the limitation.

2. Comment R3.2: For the time-dependence of extra-cellular radial diffusivity, authors used a linear time-dependent model and suggested that the linear time-dependent model has better goodness of fit than the well-known [log(Δ/δ)+3/2]/(Δ-δ/3) model in previous studies (Burcaw et al., NeuroImage 2015 and more). What is the functional form of the linear model? Is it 1/Δ? Does it really matter to use the spurious linear model, instead of the validated log(t)/t model? For the time dependence on page 20, does the δ indicate the pulse width or the diffusion time (inter-pulse duration)? In addition, the authors did not show any results related to the fit parameters of this extra-cellular linear model for time-dependence.

3. Comment R3.4: Authors showed the noise propagation of their axonal diameter model at the SNR of 17.3 (human) and 11.2 (animal). It shows that the resolution limit of the smallest detectable axonal diameter is about 1.5 micron (kind of smaller than expected at the given SNR). However, each parameter combination was repeated 10 times with different Rician noise realizations at the same SNR. Why did authors repeat it 10 times with different Rician noise realizations? Were the 10 fitting results averaged in any way (mean, median, or other selection method)? It sounds like the SNR is boosted by a factor of sqrt(10).

4. Comment R3.4 (continued): The fitting algorithm is a little convoluted and difficult to understand now. I strongly suggest sharing the code of the model fitting and noise propagation online on a public repository.

5. Comment E.2: The relation of true signal A and Rician-biased signal E(M) was explained in Koay and Basser JMR 2006, where Equation 13 shows {E(M)}2 ~ = A2 + σ_Rician2 at high SNR. The σ_Rician2 does not have a factor of 2. In the response of comment E.2, authors used the equation for E(M2). However, the magnitude signal is E(M), not sqrt{E(M2)}. Therefore, authors should cite and use the relations in Koay and Basser JMR 2006 to correct and estimate the SNR, though it may not affect the numerical results significantly.
