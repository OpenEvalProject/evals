# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83232.sa0](https://doi.org/10.7554/eLife.83232.sa0)

This important work advances our understanding of the effects of focal perturbations with transcranial magnetic stimulation (TMS) on brain activity. By combining TMS, electroencephalography (EEG), and computational modelling, the authors provide solid evidence to indicate that early EEG signal changes result from local dynamics in the stimulated region whereas later signal changes are influenced by reverberating activity within more broadly connected networks. The work will be of interest to people researching the physiological effects of brain stimulation and biophysical models of large-scale neuronal activity.


---

# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83232.sa1](https://doi.org/10.7554/eLife.83232.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "TMS-evoked responses are driven by recurrent large-scale network dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Jil Meier (Reviewer #1); Andrea Pigorini (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors state: "Our central question is whether these late responses represent evoked oscillatory 'echoes' of the initial stimulation that are entirely locally-driven and independent of the rest of the network, or whether they rather reflect a chain of recurrent activations dispersing from and then propagating back to the initial target site via the connectome." Since the network is connected, it seems unlikely that any effect can be "independent of the rest of the network", in which case Figure 4B would have been sufficient to show that the later responses to TMS are due to recurrent network dynamics. The authors should provide stronger motivation for their temporal virtual lesion analysis.

2. Regarding structural connectivity: "We set strong priors on the connection weights, such that individual fits allow for a small adjustment of these values." How much variance did you allow? How did the structural matrices look afterwards? There is one example of one subject in Figure S4 but could you also please quantify the differences between the original and the individually fitted structural matrices?

3. "This matrix was prepared numerically for physiological network modelling by rescaling values by first taking the matrix Laplacian, and second by scalar division of all entries by the matrix norm." Which matrix norm is referred to here? Please clarify why the Laplacian was taken as input as this seems like an unconventional normalization.

4. "This thresholded E-field map was then used to inject a weighted stimulus into the target regions in the model." How was this weighting calculated? How were the SimNIBS results transferred into the parcellation?

5. "JR model-simulated TEP ŷ was generated" To which state variable of the model does ŷ refer?

6. How were the Gaussian prior distributions chosen for each of the JR model parameters?

7. Why were the source-space waveforms not assessed on an individual subject level? It seems like the waveforms and Figure 4 should be validated on an individual basis.

8. At what time was the stimulus onset? Was this onset time varied and tested for different correlation outcomes with the empirical time series? It seems that the responses are slightly shifted between empirical and simulated waveforms. Related to this, what was the transient time of the simulation, and was this cut-off? What was the total length of the simulation?

9. Can the authors please comment on the differences in the y-axis ranges between simulated and empirical responses? Can these not also be optimized?

10. It could be quite interesting to also compare the TEPs with a resting-state simulation using the same optimized parameters. This could provide a useful benchmark to compare the stimulus ON periods with stimulus OFF periods and distinguish the stimulus propagation from normal activity spreading in the individual brain networks. If the authors compare their model outcomes also with other whole-brain dynamics benchmarks, e.g. resting-state networks or markers of healthy EEG activity, then this could give increased credibility to the model. Since the authors make claims about whole-brain dynamics, it would be important to validate their model beyond the TEP signature.

11. How much does the result of the optimization algorithm depend on the window length? In my opinion, a 40 ms window seems quite long. Could the authors also test shorter time windows?

12. One of the Reviewers reran the code which is provided by the authors (compliments for sharing!) and noticed that the optimization algorithm has quite varying results, e.g. the first run returned an optimal value of 98.53 and the second one an optimal value for the same parameter of 100.34. Thus, did the authors run the newly developed algorithm multiple times and checked the robustness of the fitting results?

13. The HCP data also offers good quality to extract subcortical regions and their connectivity. These regions could play a major role in TEP stimulus propagation. Why did the authors choose to leave out subcortical regions?

14. The main results hinge on the idea of performing virtual lesions at different times and comparing the activity against the no-lesion case, to see whether activity continues in the absence of recurrent feedback from distant regions. This is an elegant and logical approach. But the implementation requires clarification. From the stated premise and the schematics in Figures 1B and 4A, it seems that the lesions are to isolate a stimulated node. But Figures 4B and 4C appear to use a fully-disconnected network, and the Methods text refers to disconnecting the connections of "maximally activated nodes" at different time points. It is thus difficult to understand what type of lesion was used for what analysis. Please clarify.

15. For the central question of teasing apart recurrent vs local activity, the activation map results in Figure 4A appear to focus on spatial spread rather than the precise question of how much activity at the stimulation site is local vs recurrent. It seems potentially trivial that if you lesion around the stimulation site at 20 ms or 50 ms you don't see spread beyond that site, whereas for a later lesion the delayed stimulus-evoked activity has already reached the other areas (i.e., closing the door after the horse has bolted). Please provide a quantitative calculation of the relative contributions of recurrent vs local activity at the stimulation site. Figures 4B and C may speak to this but the text does not address these.

16. Relatedly, it is unclear how the lesions interact with the propagation delays between regions, which could be important for interpreting the post-lesion activity. In particular, if a signal is "in transit" at the time of lesioning, does that delayed activity still make it to the destination? This likely depends on whether the lesions are modelled as being physically close to the sender or close to the receiver (or both). In any case, one would expect that the delays between regions would determine whether the initial pulse is able to drive activity there before the lesion cuts them off.

17. The fitting seems to do impressively well overall, but not so well at the start (within the first ~50 ms post-stimulus). This is interesting because one might think that the earliest part of the pulse is "simpler" than the more complex patterns possible after receiving multiple variously-delayed feedbacks from the rest of the network (this is of course central to the paper's main topic). Do the authors have insight into why the initial pulse is apparently more difficult to fit?

18. Regarding the role of inhibitory time constants, it is stated that this result is "entirely data-driven" but it is not clear whether relationships were sought with the various other model parameters too. Some correlations are given (Figure 5B) and some additional modelling is used to verify this (Figures 5C and D), but those panels are not addressed in the text so it's difficult to know what to take from these results. The authors give some justification along the lines that TMS protocols have inhibitory effects, but it's not clear why this should be specifically the time constant vs a synaptic strength or some other property of the inhibitory population.

19. As is evident from most of the figures and as mentioned by the authors of the database (see below), the data contains residual sensory artefacts (auditory or somatosensory) that can bias the authors' interpretation of the re-entrant activity. One key limitation is due to the stimulation target. Only the primary motor cortex (M1) is considered here. TMS of M1 – especially at Resting Motor Threshold, as in Biabani et al. – leads to peculiar features in the time and frequency domain of the EEG response, possibly due to feedback from the periphery following target muscle activation – see for example Fecchio, Pigorini et al., Plos One 2017. Are the authors able to address this potential contamination of the signal?

20. On a related note, the data used here are collected by delivering white noise to cover TMS-click instead of a customized one (see Russo et al. JNeurosMethods, 2022). This could introduce the residual auditory activity in the EEG response to TMS that might substantially bias the results and their interpretation in terms of network long-range interactions. For example, residual auditory effects (i.e. n100-p200 component) seem to be present in most of the figures. Can the authors rule out a major contribution of such effects to their findings?

21. Besides the influence of late sensory components, in the same subjects the initial response of the real data seems to be of rather low amplitude and not lateralized, suggestive of a non-effective TMS delivery (see Belardinelli et al., Brain Stim, 2019, for the relevance of this topic). Importantly, in the related simulated data it seems that the initial response is instead present and much higher and lateralized with respect to the real data, possibly reflective of a capacity of the model to replicate the typical TEPs obtained by "effective" TMS. The authors should comment on this potential limitation.

22. The work by Biabani et al. reports that "TEPs elicited by motor cortex TMS reflect a combination of transcranially and peripherally evoked brain responses despite adopting sensory attenuation methods during experiments". This spurious effect is particularly relevant after 60 ms following TMS, and thus the present findings, as well as their interpretation, could be in principle biased by somatosensory re-entrant activity. As such, for the purpose of the present manuscript – i.e. evaluating the late effect of TMS, a dataset in which the residual sensory activity is maximally reduced during data collection is recommended (see Casarotto et al., JNeurosc Methods, 2022 for a full discussion on this topic).

23. The Perturbational Complexity Index (PCI, Casali et al., Science Tr Med, 2013) should be used to evaluate changes in complexity induced by cortical lesions (as in Rosanova, Fecchio, Nat comms 2018 or in Sarasso, Brain, 2020) and not for evaluating the similarity between real and simulated data. Indeed, two completely different wave shapes could in principle have exactly the same PCI value. Instead, for evaluating the quality of the simulated signal (i.e. its similarity with real data), the "natural frequency" may be preferable (Rosanova et al. 2009, JNeurosc).

24. Please clarify the rationale for performing virtual lesions only at 20, 60, and 100 ms. A time-resolved analysis would be preferable.

Reviewer #1 (Recommendations for the authors):

Key points:

(i) The authors themselves state that structural connectivity plays an important role in the waveform shapes: "More recently we obtained a similar result with anatomical connectivity (Momi et al., 2021b), namely that network-level anatomical connectivity is more relevant than local and global brain properties in shaping TMS signal propagation after the stimulation of two resting-state networks (again DMN and DAN)." Thus, it would be very interesting to also compare the optimized structural networks among individuals and analyze the relationship between strong structural connections and their individual variability in waveform shapes.

(ii) 26. "Latencies and amplitudes of the SVD left singular vector time series peaks were extracted for every subject and related with the individuals' JR model parameters, with Pearson correlation coefficients and corresponding p-values were computed accordingly." Does this mean that the authors tested correlations of the amplitudes with several of the JR parameters? If the authors ran more tests, one would need to correct for multiple comparisons. Also, it would be great to report the results of these other comparisons in the supplementary material.

Reviewer #2 (Recommendations for the authors):

1. I appreciate the authors including Supplementary Figure S4 showing the parameter distributions across the cohort. It's interesting that there is apparently not a great deal of spread in any of the local region parameters – are these fitted values in line with those found by others using the Jansen-Rit model? What dynamical regime does this place the model in? This would give confidence that the model is indeed in a state consistent with the pre-stimulus resting state.

2. The fitting algorithm apparently allows a great many parameters to vary because the connectivity matrix is allowed to vary from the tractography-derived priors. Can the authors give a sense of how much of the fit is due to this huge number of degrees of freedom in the network, versus the local region parameters? And can they defend against the classic charge that a model with so many free parameters can fit anything?

3. Figure 3, it appears that the model fits better in channel space than in source space. Can the authors give an intuition for why this is so?

4. How focal is the stimulation? It is mentioned that SimNIBS is used, but how many regions are stimulated by the TMS pulse?

5. Can the authors justify why TMS is modeled as perturbing specifically the excitatory interneuron population?

6. What's the reasoning for using the matrix laplacian of the connectivity matrix?

7. Equation (4), it appears that Su(t) should be S(v) or S(v(t)). And why the t=0 boundary? I suspect a typo in the denominator too (I think it should be 1+exp instead of 1-exp).

8. Equation (11), bracket missing.

9. Here the modeled EEG signal is estimated from the difference between the excitatory and inhibitory interneuron activity in each region, which at first sounds at odds with the generally accepted view that EEG is most related to pyramidal neurons. I suspect this choice is because in the Jansen Rit model it is those outputs of the interneurons that drive the pyramidal neurons. This should be clarified.

10. lines 647-649, it is unclear how Equation (13) is a measure of complexity; also a typo referring to it as Equation (14).

11. Figure 4C, what's the inset scalp picture?

12. Figure 4C, if this is Local Mean Field Power how can it go negative? And why does it have units of microvolts?

13. Supp. Figure S4 uses different symbols for the parameters vs the main text.

14. Many of the figures pack in so much detail that it is difficult to see what is going on without excessive zoom to read labels etc. Some labeling should be larger, and some figures should potentially be split into multiple if there's no space to increase the size of details within.

15. There should be a space between a number and its units.

Reviewer #3 (Recommendations for the authors):

I really enjoyed reading this manuscript. I found it interesting and well-conceived. Below the authors can find a list of issues (along with possible suggestions). In case the authors will properly address them, I would really recommend the publication of this otherwise excellent study on eLife.

1) As clearly stated in my public review, most of my issues derive from the data used in the manuscript. My suggestion is to use the open dataset that came with Fecchio, Pigorini et al. (Plos One, 2017), including parietal, premotor, prefrontal, and M1 stimulation. The dataset is available at :

https://figshare.com/articles/dataset/Data_for_Fecchio_Pigorini_et_al_/4970900/1

Using this dataset:

i) You could consider cortices other than M1;

ii) You use data collected with customized noise masking, that minimizes residual auditory evoked potentials (i.e. n100-p200 component, as in Figure S1, Subjects 5, 6, 7, 8, 15… etc);

iii) You use data that maximize the impact of TMS on the cortex;

iv) You can be sure that residual sensory artefacts are maximally reduced during data collection.

For all these reasons, I would really recommend using the above-mentioned dataset (or a similar one). This will be enormously important also for the TMS-EEG community. Indeed, it will allow demonstration, thanks to your modelling approach, that TMS-EEG data can contain late components even in the complete absence of residual sensory artefacts. I understand that re-running the entire analysis over another dataset is an enormous amount of work, but I strongly believe that it is fundamental for a proper interpretation of the results, and to make your study useful for the entire TMS-EEG community.

2) By applying your modelling approach to such a dataset you should also be able to replicate the results reported in Rosanova et al. (JNeurosc, 2009) and Ferrarelli et al. (Arch Gen Psychiatry, 2012) showing that the stimulation of different areas leads to TEPs characterized by different "natural frequencies". Reproducing this feature in simulated data is fundamental to check the quality of simulated data – as a note I would indeed recommend using the natural frequency instead of the Perturbational Complexity Index to evaluate the quality of the simulated data (see also point 5 of the public review), and perhaps PCI to evaluate changes in complexity upon virtual lesion (as in Rosanova, Fecchio et al., Nat Comms, 2020). As a note, I am not 100% sure that a connectome-based approach that accounts for only a few local properties (Jensen and Rit equations) can be able to reproduce the Natural frequency. If it were the case, it would be an incredibly valuable readout of the efficacy of your method; if not, it means that this is just a first step that needs to be perfected (and this can be easily discussed).

3) Related to my point (6) of the public review; if possible and not computationally challenging, I would perform more than 3 lesions over time. Instead of 20, 60, and 100ms, I would try to perform a more time-resolved analysis with one lesion every 5/10 ms, up to 200-300 ms.

4) It is not very clear how the authors performed the statistical comparison between real and simulated data. In addition, in figure 1A, empirical and simulated TEPs exhibit extremely different voltages, so simulated TEPs appear to be remarkably larger than empirical TEPs. How do the authors explain this discrepancy? Since the metric employed by the authors (correlation) is independent of the absolute value of the voltage, it would be important to quantify and report these differences.

5) This is more of a curiosity: what happens to high frequencies (>20Hz) after the lesion? Do you see any suppression as in Rosanova, Fecchio (Nat Comms, 2018)?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "TMS-evoked responses are driven by recurrent large-scale network dynamics" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed. These issues are outlined in the Reviewer comments provided below. These need to be addressed comprehensively before we can consider publication of the manuscript.

Reviewer #1 (Recommendations for the authors):

The authors provided a significantly improved revised manuscript and with most of their responses to my comments. I am very happy. However, there are still a few major and minor points that I suggest the authors take a closer look at.

General point:

Often, the authors nicely provide detailed explanations in the rebuttal but fail to also add those explanations to the manuscript. If these refinements were also added to the improved manuscript, then future readers could benefit from the improved clarity directly without additionally having to consult the rebuttal letter. An example is essential revision 3, where it would be great if the authors could also clarify in the text that they used the Frobenius norm.

Essential revision 2:

– I fail to recognize the distance-dependence in the subject-specific SCs. There are many strongly red-colored entries, not just the ones around the diagonal. It seems similar in the original SC, thus I would not take this as a key feature here to judge the fitted SCs.

– In the visualization of the original SC matrix (Appendix 2- Figure 4), one can see that the range of values is [0:0.003], thus allowing a variance of 1/50=0.02 seems very extreme in my opinion.

– Also for better comparison of the original SC with the subject-specific SCs, could the authors please use the same color bar limits for all SCs?

– If the authors allowed such a 1/50 variance, did they only allow this variance in the positive direction or did their prior distribution also allow for negative entries in the SC?

– "We selected a prior variance for each of these connections of 1/50, which was determined empirically to provide a strong constraint but allow for some flexibility during the fitting process." What exactly is meant with „determined empirically" here?

– "It can be seen here that the distribution of the norm distances scores (see image below) acceptable, indicating a relatively small deviation from the prior connectivity weights." It would be much better if the authors describe in words what they calculated here instead of posting the code as a justification of acceptability of the norm distance scores.

Essential revision 4: The x axis ‚brain regions' should probably be relabeled and also add numbers to the ticks please.

Essential revision 6: I applaud the authors for providing such a table with individually optimized parameters, which is an important step towards full reproducibility of their study.

– In the table, there is only one column of variances added for each variable, was this the variance of the prior or posterior distribution or were they the same?

– How can there be a negative variance for the global gain?

Essential revision 12:

The 100 repetition times of their fitting algorithm show a large and to me alarming variability of optimized parameters and warrants further analyses. One solution to deal with this alarming variability would be to please always run the algorithm 100 times (at least 10 I would suggest) and take the mean of its distribution as the final optimized parameter in order to increase robustness of the presented fitting results.

– "For completeness, the prior means for each parameter are also shown as vertical red lines. Shown below are parameter estimate distribution plots for a single subject, repeated 100 times. The vertical red line indicates the original parameters' value (the one in the manuscript) for the same subject." What do the red lines in the plots represent, the prior means or the parameter value chosen for this subject in the manuscript results?

– "Reassuringly, these histograms are approximately normally distributed, and have a tight range of variation that spans only a few percent of the magnitude of each parameter" Even though the variation spans only a few percent of the magnitude of each parameter, the variation for this single subject (e.g. for parameter a: [94:102]) spans nearly over the whole range of optimal parameter values that were fitted over all subjects (e.g. for parameter a: [92:102], see Appendix 2 – Table 1) – or even a larger range than the one fitted over all subjects as in the case of c1. Thus, all results regarding individual variability should be interpreted with caution. The plot for c4 is probably mislabeled as no subject has optimal values in this range according to Table 1.

Essential comment 18:

Results lack significance after Bonferroni correction, therefore they should in my opinion be moved to the Supplementary Material and not be mentioned in the main text as being significant.

Reviewer #2 (Recommendations for the authors):

The authors have done a good job in responding to the reviewer comments. In particular it is impressive that they successfully replicated the analysis on an independent dataset. Some residual comments:

1. In general it is preferable that if a clarification is made to the reviewers, it is also made in some way in the text. I won't list them all, but for example the matrix laplacian clarifications don't appear to have made it to the text.

2. Re notation difference, figures and the appendix table refer to parameters a, b, c1, c2, c3, c4, g, but I do not see these in Equations 1-11.

3. Re Equation 4, Su(t) appears to be a typo since the other equations refer to the function S(v).

4. Re Equation 4, why the t=0 boundary?

Reviewer #3 (Recommendations for the authors):

First, I would like to congratulate the authors on the incredible amount of work done in order to address all the issues posed by myself and the other reviewers. In particular, I really appreciate the new set of analyses performed on a completely different dataset in order to control for possible confounding factors, such as residual sensory input. In general, the authors have addressed most of the issues I formerly raised, and significantly improved the manuscript with the revised version.

Yet, the first fundamental issue mentioned in my previous review has not been addressed (see point 19 of previous review). The authors mentioned in their response that they "believe that [testing different areas] is beyond the scope of the present manuscript…". I respectfully disagree. In my opinion, the interpretation of the results could be severely biased by the stimulation of one single area (primary motor cortex – M1), having strong efferent connections with periphery. To better clarify my point, by stimulating only M1 it is not possible to conclude that late TEP components are "driven by the recurrent activity within the rest of network" (as stated in the introduction); or at least this is not the only possible interpretation. Indeed, TMS of M1 – especially at Resting Motor Threshold (RMT), as in Biabani et al., or above RMT, as in Fecchio, Pigorini et al. (Experiment_1) – most often leads to muscle twitch, which in turn, induces proprioceptive (sensory) feedback from the periphery. So, TEP components under these experimental conditions are inherently confounded by the peripheral twitch induced by the stimulation. How can the authors address this problem?

In my view, the most straightforward solution implies including other areas in the main analysis (as suggested in my previous review); however, I understand that this implies a huge amount of work, encompassing "diffusion-weighted MRI analysis, TMS-EEG analysis, e-field modeling, deep learning for parameter optimization and neural mass model implementations…". I also understand that "this question is among the scientific priorities" of the authors, which "are currently working on expanding this model further to other stimulation sites".

So in my view, other two – less time consuming – possible solutions to disentangle this problem are:

1) The authors could control whether TEP associated with high voltage and low voltage Motor Evoked Potentials are associated with different late components in the simulated data (data available in Fecchio, Pigorini 2017 – Experiment_2).

2) The authors need to significantly rework the main message of the manuscript by incorporating this confound in the authors' interpretation of their main finding (e.g. the title should be changed because late components could be recurrent large scale network dynamics, but could be also feedback from the periphery…).

I find this second option overly detrimental to the overall significance of the study and I strongly suggest the authors to implement the first in a revision.

Apart of this main issue, I also found a couple of issues the authors may want to address before publication.

1) Perhaps my previous comment about PCI was not clear enough. I did not say that "PCI should never be used for evaluating model fit"; and I fully understand that fitting "could be done with any metric at all that can be computed from empirical and simulated time series". However, while it is true that "the model may be considered a good one to the extent that it captures multiple data features of physiological interest that are reliably quantifiable", it is also true that some metrics are better than others to capture similarities among different time series. As mentioned in my previous review, "two completely different wave shapes could in principle have exactly the same PCI value". The authors can find an example for this in Decision letter image 1. Top and bottom panels report the butterfly plot (black) and the channel under the coil obtained by stimulating (in the same subject) occipital and prefrontal cortices, respectively. In both cases PCI is 0.47, but the wave shapes highlight major differences both in time and space which are not captured by the single PCI scalar. I hope this example clarifies my former concern and suggest the authors to report metrics other than PCI in the main figures (Pearson correlation coefficients are more than enough).

2) Something must be wrong with the axes in Figure S5. See Decision letter image 2 the authors can find a plot with the correct time and voltage scales for each subject. For example, in Subj_1 the first peak is a 4 ms and not at 38 ms (as in Figure S5).

3) Related to my former comment on the original manuscript: "Figure 2B shows a correlation that can be partially driven by the spectral content of the waveforms. It could be relevant to verify whether these correlations are significant with respect to a comparable null hypothesis (e.g. IAAFT, or correlating different empirical and simulated sessions)." I mean that correlation analysis could be strongly affected by low frequencies (characterized by higher power). Thus, a statistical test accounting for different frequencies (e.g., IAAFT) could be preferable (yet not mandatory at this stage).
