# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- Alexandre Hyafil, Universitat Pompeu Fabra Spain
- Jan-Mathijs Schoffelen, Netherlands

## Review text

DOI: [10.7554/eLife.44287.017](https://doi.org/10.7554/eLife.44287.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "A statistical modeling framework to assess cross-frequency coupling while accounting for confounding effects" for peer review at eLife. Your article is being evaluated by Laura Colgin as the Senior Editor, a Reviewing Editor, and three reviewers.

Given the list of essential revisions, the editors and reviewers invite you to respond with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

While the work was appreciated (that is, the importance of including statistical approaches), several aspects were raised that require clarification and additional work (e.g., comparison to other methods, confounding factor issues, etc.). It is unclear whether this would be addressable by the authors and in a timely fashion. As this is understood to be a methods paper, it was not deemed critical for the authors to provide explanations per se of the meaning of results, although they would be welcome to do so.

Essential revisions:

The article by Jessica Nadalin and colleagues makes a key improvement in the statistical methods to detect cross-frequency coupling in neural signals. As the coupling between neural oscillations has become the focus of intense research and has been linked to a wide array of cognitive functions, the proposed method has very general implications for neuroscience. It may constitute the first attempt to assess conjointly different types of CFC. The use of generative models, in particular GLMs, seems like a solid way for building complex statistical approaches – they are increasingly popular in neuroscience to analyze behavioral and neural spiking data. There are nevertheless quite a number of points that should be resolved or clarified in the manuscript to provide a clear validation of the method.

1) The model for PAC and CFC is a Generalized Additive Model (GAM) rather than a GLM, as it takes the form: log μ = f(Фlow).

Here the function f is approximated by splines, which is one typical decomposition of GAMs. See the relevant literature, e.g. textbook by Wood, which provides principled ways of selecting the number of splines, assessing the uncertainty about the inferred function f, performing model comparison, etc. In particular it would be nice to show a few examples of the estimated function f, the typical modulation of Ahigh by Фlow.

2) Presumably, the formula for R is an attempt to mimic the R2 metrics used in linear regression. However there already exists of series of pseudo-R2 metrics for GLMs, for which pros and cons have been discussed, see e.g. https://web.archive.org/web/20130701052120/http://www.ats.ucla.edu:80/stat/mult_pkg/faq/general/Psuedo_RSquareds.htm. These measures should not suffer from the problem of using an unbounded space as is the case here for RAAC and RCFC. The authors should pick one of these and apply it instead of the R measure (unless authors provide a clear explanation of why they used such definition of R).

3) Comparing statistically CFC values between distinct conditions is a key experimental method. The method described in rat data looks really nice, but it would need to be assessed beforehand on synthetic data. Will the method display false alarms (incorrect detection of changes in CFC) when the overall amplitude of the low frequency changes between conditions, as would direct comparison of CFC values between conditions? A method that gets rid of this confound would be a major advancement. Moreover, authors fail to explain the discrepancy in rat data between MI results and GLM results. Is it because of variations of the amplitude of the low frequency signal between conditions?

4) The authors quite surprisingly test their different methods of computing p-values of different synthetic datasets, and never on the same. It is frustrating that one cannot conclude in the end which method provides better results. Moreover, the two methods for generic synthetic data should be presented next to each other to allow comparison (the presentations of the equations could be made more similar).

5) It is important to see how the GLM method compares to other PAC detection method (e.g. MI) for weaker modulations. Is it as sensitive? Moreover, reviewers felt that the comparison of the sensitivity of the PAC measures to changes in Alow (Figure 5) was quite unfair. MI is an unbounded measure while R cannot be larger than 1. If reviewers understood correctly, the base value for scale factor should be around 0.5 (from Figure 4F), so that it cannot increase more than a twofold increase. This could explain the plateau in Figure 5. Is this correct? Perhaps performing the same analysis with a much weaker coupling would remove this concern.

6) The modulation of PAC by the low-frequency amplitude is an important contribution of the paper. It would deserve an actual figure for the second patient data, illustrating it with the method and showing modulations of Ahigh by Фlow splitting the dataset into low and high Alow. From a mechanistic point of view, the fact that PAC is larger when Alow is larger makes perfect sense, and it has been linked to the generation of AAC (Hyafil et al., 2015 Figure 3). Is there an intuitive generative mechanism that would create lower PAC for larger Alow (as in Figure 7)?

7) Figure 9 and Figure 10 make apparent that the recovered amplitude of the low frequency signal Alow fluctuates within each cycle, which goes against the very notion of amplitude of an oscillation. This can lead to falsely detecting AAC when there is PAC, as is evident for example in Figure 9: Ahigh is higher at the phase of the low-frequency signal where Alow is higher. Proper AAC should mean that Ahigh is higher for entire cycles of low frequency where Alow is high/low.

8) Clarification of confounding aspect intention and circularity perception in the method:

8.1) The simulation part is suboptimal and to some extent based on circularity. Specifically, the method is based on modelling the Hilbert-envelope of high frequency band limited activity with different GLMs, using regressors that are functions of the Hilbert envelope and phase of low frequency band limited activity. The test statistic is derived from the response functions, and statistical inference can be done with parametric methods, or, more appropriately for real data, using bootstrap techniques.

For the simulations, a generative model was used which essentially builds the high frequency amplitude component as a function of low frequency phase component and/or the low frequency amplitude component. Thus, it is not really surprising that the method works, specifically if in the processing and generation of the data similar filter passbands etc. have been used. It is unclear how this can be alleviated, unless the perceived circularity is actually not there, or the authors are able to come up with a fairer way to simulate the data in order to convincingly show that their method works in general.

8.2) Next, in support of the claim that the proposed test-statistic 'accounts for confounding effects', I feel that the evidence presented at most shows that the RCFC metric scales less strongly with low frequency amplitude (Figure 5), this property should not be oversold.

8.3) With respect to the application to real data, the abstract mentions that "we illustrate how CFC evolves during seizures and is affected by electrical stimuli". This indeed is illustrated by the data, in that the CFC metric is modulated. Yet, it is questionable (specifically for the human ictal data) that this reflects (patho)physiologically meaningful interactions between band-limited neural signal components. If anything, the increased CFC metric highlights the highly non-sinusoidal nature of the ictal spikes, and demonstrates the generic sensitivity of CFC-measures to the non-sinusoidality of the associated periodic signal components. This is a well-known feature, and the most important confounding interpretational issue in most cross-frequency analyses. Therefore, the high expectations based on the manuscript's title were not met in that respect. This important issue needs to be discussed in more detail, and the title should be adjusted for the sake of the reader's expectation management.

9) The authors proposed new measures of cross frequency coupling (CFC) in neurophysiological data where the emphasis is placed on phase-amplitude coupling (PAC) and amplitude-amplitude coupling (AAC). Statistical properties of the new estimators are discussed. These methods are tested in simulated data and in neural recordings from human epilepsy patients and rodents undergoing electrical stimulation. Whereas CFC is an important research area, and better measures are always welcome, it was not clear if the proposed methods are sufficiently novel to potentially offer new physiological insights into the neural operations represented by the data.

Estimating phase and amplitude from Hilbert transform requires the signal to be narrow band. Whereas the 4-7 Hz filtering band for theta phase and amplitude estimation is adequate, the 100-140 Hz filtering band for estimating high gamma phase and amplitude is too wide; it is thus likely that the phase and amplitude estimated this way is not accurate. A way to empirically test whether the filtering band is sufficiently narrow is to plot the real and the imaginary part of the filtered signal in a phase portrait to see whether the trajectory moves around a well-formed center. It is the rotation around this center that allows us to define instantaneous phase and amplitude properly from Hilbert transforms.

Numerous ad hoc assumptions go into Equations (1)-(4). It is difficult to follow the logic behind the method. The beauty of the original CFC measures (e.g., Canolty's or Tort's definition of PAC) is that they are simple and intuitive.

The synthetic time series considered here are not biologically realistic. First, spiking neural models should be used to generate such time series. In particular, the model should incorporate the property that gamma and high gamma in some way reflect neural spiking. Second, noise should be added to the synthetic time series to mimic the real world recordings; the amplitude of the noise can be used to assess the influence of signal to noise ratio on the various CFC quantities defined.

For the human seizure data, the authors only evaluated their new measures on the data, but did not compute the commonly applied PAC measures for comparison.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A statistical framework to assess cross-frequency coupling while accounting for modeled confounding effects" for further consideration at eLife. Your revised article has been favorably evaluated by Laura Colgin (Senior Editor), a Reviewing Editor (Frances Skinner), and 3 reviewers (Reviewer #1: Alexandre Hyafil; Reviewer #2: Jan-Mathijs Schoffelen; Reviewer #3 has opted to remain anonymous).

The reviewers appreciated the new figures and improvements throughout. The manuscript is likely to be accepted after the remaining essential issues below are addressed; however, they still need to be addressed. The main thrust of most of these requests is to ensure clarity for readers of where this approach is situated relative to others, and in some cases, there may have been misinterpretations of previous requests.

1) Title: Another suggestion is that one could use "analysis", rather than "modeling" to have a title of "… confounding analysis effects". This is a suggestion, not required.

2) The new Figure 2 is fine. It was thought that the comment regarding GLM vs. GAM was misinterpreted. The point was conceptual rather than algorithmic. The essence of the models described here is to capture a nonlinear mapping of the regressor(s), that is then transformed into the observable using a link function and some observation noise: this is exactly what a GAM is. As described in the textbook by Wood (section 4.2), using basis functions such as splines, a GAM can be transformed into a (penalized) GLM, and then exactly fit using the standard GLM procedure that authors have used. (I believe outfitting is rather an outdated form of fitting GAMs). Please simply add some wording to make this clear. That is, the suggestion is not to change the core model fitting part, only to acknowledge the direct link with GAM.

3) We understand that the R measure captures how strongly the regressors modulate high frequency amplitude: this is exactly what R2 does in linear regression (assessing the part of the variance explained by the model), although it is sometimes described incorrectly as measuring goodness-of-fit. In their response, reviewers claim a somehow different thing, that their measure "estimate differences between fits from two different models". Now, if this refers to model comparison, again, there is large literature on how to perform model comparison between GLMs (including AIC, cross-validation, etc.). So I can see no reason to create a new method that suffers some important drawbacks (not derived from any apparent principle, arbitrariness for unbounded regressors, PAC measure is modulated by levels of AAC and low frequency amplitude, etc.) and has not been tested against those standard measures. We fully support the idea of using GLM as statistical tools for complex signals; it is a pity though not to leverage on the rich tools that have been developed within the GLM framework (and beyond that in machine learning). Please either use these rich tools or provide a proper argumentation of why your measure is used.

4) The new simulations represent an important step in the good direction but the analysis performed on the synthetic data is not quite the one performed on the experimental data. Figure 7 shows that the R measure is modulated by amplitude of the low frequency signal as well as AAC (although less so than the MI measure), preventing any direct comparison of PAC between differing conditions. Now on the rodent data, authors very astutely use a single model for both conditions, and indicator functions (Equation 10). For some reason, the model comparison performed on the previous version of the manuscript has disappeared. This was viewed as regrettable as this indicated that PAC was modulated between the two experimental conditions, something that direct comparison of MI/R values cannot afford to test. This is also the manipulation that we would like to see tested on synthetic data, to make sure whether authors are using a method to isolate modulations of PAC from modulations of low frequency amplitude and AAC.

In other words, it would be great to see this method tested on synthetic data to see if they get rid of the confounds, and then possibly applied on rat data as in previous manuscript. This was viewed as something that could make the paper much better. However, it is acceptable to also choose to trim the comparison between conditions part. If so, the authors are requested to be very explicit in their wording that by using separate models for different conditions, they cannot get rid of possible confounds.

5) The R measure seems pretty much as sensitive as the MI measure to low PAC. However, the two measures cannot be compared directly. Since most research is geared towards assessing significance levels of PAC, it would be interesting to rather show how the two methods compare in terms of statistical power: comparing type I error rates for low levels of PAC (although reviewers are a bit wary of what could be the results, since the type II error rate related to Figure 5 was less than 1% when it is supposedly calibrated to be 5%, suggesting the method could be too conservative).

6) The response to point 7 misses the important message: the extraction of the amplitude of the low frequency signal is intrinsically flawed as the recovered amplitude fluctuates within cycles of the low frequency rhythm. Looking at Figure 9C, peaks of Alow and Ahigh coincide within these cycles, which will very likely give rise to spurious AAC for this segment (irrespective of whether slow fluctuations of Alow do modulate Ahigh). It is unclear why this is apparent here but was not detected in the analysis of synthetic data, but in any case, it would require in our opinion a serious assessment of the properties of the algorithm to extract Alow. The authors' solution (changing the frequency range of the simulation to make the problem less apparent) is not a valid one. In any case, we can still see the issue in Figure 11F: sub-second fluctuations in Alow. Perhaps one quick fix would simply be to use a lowpass filter for Alow to remove these spurious fluctuations. It makes no sense conceptually that a signal assessing the amplitude of an oscillation would fluctuate rapidly within each cycle of that oscillation.

7) Regarding point 8.1 in the rebuttal: the change proposed in generating the signals was viewed as just a minor cosmetic change. It does not take away our concern for circularity, since the high frequency amplitude is still a direct function of the phase time series of the low frequency signal. Also, a change in signal generation was only done for the PAC, and not for the AAC, which suffers from the same circularity concern. As mentioned before, perhaps this concern cannot be alleviated at all (although we think that the authors could have done a better job by generating both the low frequency phase time series and the high frequency amplitude time series as a (possibly non-linear) function of a third unobserved time series. Either way, the authors need to at least discuss this concern for circularity explicitly, and argue why this in their view is not a problem in convincingly showing the utility of their new method.

8) Regarding point 8.3 in the rebuttal: we find the proposed fourth concern far too theoretical to be of practical use. The readership really should be informed about the interpretational confounds of CFC metrics, as mentioned in an original comment. We are not convinced that 'appropriate filtering of the data into high and low frequency components' is fundamentally possible, but we'd like to stand corrected with a convincing argumentation. In other words, the authors are requested to be very explicit in the interpretational limitations of any CFC measure, which is independent of the signal processing that is applied to the data before the measure is computed. This is important to be very clear about since 'non-methods' people may use the method without too much thinking about the potential shortcomings.

9) The authors are asked to edit a sentence in their Introduction about cellular mechanisms being ‘well-understood’ for gamma and theta – this was viewed as somewhat arguable for theta. Tort et al. is cited for theta which does not seem to be an appropriate reference for cellular perspectives. A recent paper for cellular mechanisms for theta could be used (Ferguson et al., 2018).

10) Please also consider the following: a) Some of the figures/panels could be placed as figure supplements to avoid distracting the reader away from the main points of the manuscript.

b) The figures could be polished a bit more, notably:

- Use labels such as 'π2' for phase variables.

- Merge single lines panels when possible (e.g. Figure 12B,C).

- Improve the readability of the 3D figures (e.g. using meshgrids; perhaps plotting only the full model surface in Figure 5).

- Adjust font size.

- Adjust axis limit and panel size for better readability (for some panels it's hard to see anything beyond noise, e.g. Figure 4, Figure 9B,C, Figure 10B).

- Figure 5G,K and O are difficult to read.

- Figure 11B: are these stacked bars of is RPAC always larger than RAAC? In the former case, it makes RPAC difficult to read: plot unstacked bars or curves instead.

- Figure 11F: use different scales from Ahigh and Alow to make Ahigh visible (or normalize signals).

c) Names of the models: why name them “Фlow” and “Alow” rather than PAC and AAC models?

d) Isn't the constant offset β0 missing from Equation 1 and Equation 3?

e) Please use semi-colons instead of commas to separate possible values of x (it took me a while to understand this).

f) In the spiking model, specify that the slow oscillation is imposed externally, not generated by the network.

g) "at the segment indicated by the asterisk in Figure 11B (…)": there is no asterisk in Figure 11B.

h) Figure 11F: " Ahigh increases with Alow over time"-> not clear. Ahigh increases over time but it seems that it is higher for intermediate than for high value of Alow.

i) A concern was raised about whether the frequency band corresponding to the low signal in the human data is described in the text.
