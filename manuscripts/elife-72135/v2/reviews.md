# Peer review - Round 1

Editors:
- Manuel Zimmer, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72135.sa0](https://doi.org/10.7554/eLife.72135.sa0)

Wirak and colleagues record single cell resolution whole brain dynamics in ageing C. elegans. They make the intriguing observations that coordination of brain wide neuronal activity dynamics declines with age, associated with reduced negative correlativity indicating a shift in the excitatory-inhibitory balance across the brain.


---

# Peer review - Round 1

Editors:
- Manuel Zimmer, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72135.sa1](https://doi.org/10.7554/eLife.72135.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Age-associated changes to neuronal dynamics involve a loss of inhibitory signaling C. elegans for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Piali Sengupta as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Reviewers #1 and #2 raise various concerns that your main result could be better explained by any or a combination of following reasons: age associated brain wide quiescence states, a drop in signal-to-noise ratio over age or a consequence of the slowed-down dynamics with increasing age. We believe that addressing these important concerns can mostly be done with additional analyses though new longer recordings might be needed (see reviewer #2). Reviewer #3 is mostly complementary to #1-2 and among others requests the addition of genetic controls. We would be very excited about a revised manuscript in which you can address the following concerns:

Essential revisions:

Reviewer #1 (Recommendations for the authors):

(1) The authors report an ageing associated increase in reversal frequency in freely behaving animals, which is not seen in in immobilized animals, however there is an increase in the duration of reversal network states. In lines 6-8, they state that these two findings are congruent, however, I think they should be more cautious with this conclusion. It was shown previously that long reversal command states like shown in Figure 1e or 2a occur only in immobilized animals, while corresponding activity of AVA, AVE, AIB, RIM etc. in freely moving animals appears more spiky and transient (Kato et al., 2015). Reversal frequency and durations in immobilised animals therefore do not necessarily always recapitulate what one can observe in freely behaving animals. This should be more openly discussed in the main text.

(1a) The authors should recapitulate the behavioural experiments in the AVA and whole brain imaging strains. There is a concern that elevated proteostatic stress in transgenic overexpression lines upon ageing could affect neuronal function and behaviour.

(2) The authors should measure how absolute expression levels of GCaMP and the red reference fluorophore change. If GCaMP and/or RFP signals decline over the course of ageing, and/or tissue autofluorescence / background increases, this would cause lower signal noise rations (SNR). The shift in power spectral densities (PSD) as well as in the distribution of angular change in PCA trajectory could be easily explained by a drop in SNR. The authors need to test for these possibilities and provide analyses results showing that there is indeed an increase in activity fluctuations rather than in measurement noise.

(3) The reduction particularly in negative pairwise correlations of regularized time derivatives of the traces is very interesting, but I feel that the interpretation of selective global decline in inhibitory signalling is premature and requires more analyses; particularly since this is one of the major concussions the authors draw from their results.

Typically, in immobilised animals, there are two large clusters of positively correlated neurons, the reversal interneurons + motorneurons and the forward interneurons + motorneurons, plus additional smaller clusters of head motor neurons (Kato et al., 2015). In WT animals, these two major clusters are robustly negatively correlated with each other.

It was shown that immobilization can cause a brain wide quiescence state reminiscent of C. elegans lethargus sleep (Gonzales et al., 2019). During sleep, typically all forward neurons become inactive with the exception of RMEs and elevated RIS activity; and animals often revoke from this sleep-like state by initiating reversal states (Nichols et al., 2017). I find it likely that aged worms are more prone to become quiescent in the imaging conditions. If this is the case, the decrease in negative correlations is explained by inactivity of most forward neurons (AVB, RIB, RID, B-MNs within imaging region, etc.) where the animal switches sporadically between a quiescent state and the reverse state. Many of the heatplots in Figure S2 appear to me that this could the case. For their analysis, the authors ranked the activity traces by standard deviation and restricted calculations to the top 40 active neurons. It is therefore likely, that mostly active reversal neurons remained. If this is indeed the case, the major conclusion of the paper falls apart. There would not be a global decline in inhibitory neurotransmission but an increased propensity to enter the quiescent state during forward locomotion, like in (Nichols et al., 2017); the subsequent results from the genetic and pharmacological manipulations are all consistent with this. I, however, think that this would be equally interesting and worth publishing.

If there would be a global decline in inhibitory neurotransmission, as the authors conclude, I would expect that overall activity levels of both forward and backward neurons remain high and that two clusters of positively correlated neuronal ensembles remain. More careful and detailed analysis of activity levels and clustering analyses of the correlation matrices could directly distinguish between the two scenarios. Overall, this is a bit hampered by the lack of cell IDs in the study, acquiring this expertise might be beyond a reasonable time-frame, I think it would tremendously help to ID at least a few neurons like AVA, RIB/AVB, RIS so that forward and backward clusters can be assigned.

(4) The recurrence analyses like in Figure 2b is a nice way to look at these data. It would be fair to credit ref. (Bruno et al., 2017) for introducing this approach to neuronal data analysis. Further, important details are missing in the methods section to properly evaluate this analysis. What is the distance metric used (Euclidean, cosine, correlation…)? Were the PC amplitudes normalized.…? In general, the data analysis section in Methods is very brief and should be expanded.

(5) If I understand correctly, PSDS were calculated across all neurons and then averaged across recordings. This procedure occludes whether PSD distributions reflect diversity of neurons or diversity of signal fluctuations within neuron. This would be interesting to know. More analysis could be done here.

(6) What was F0 for calculating DF/F (mean, min, percdentile?).

(7) In Figure 2a, S2 it looks like traces are min/max normalized; or is this just how heat maps were scaled for display. It should be clearly stated in Figure captions and Methods.

(8) Provide variance explained for PCs and Pareto plots for all PCA analysis.

(9) All data of this study could be shown in supplementary files, like in Figure S2.

(10) It appears that some data are re-utilized across Figures, like WT PSDs of Figure 3a. This is ok but should be clearly started in each Figure panel.

(11) How come that exactly 120 neurons were measured in each recording? Please provide accurate n numbers.

(12) Show SEM or SD for mean traces like PSDs and cumulative power plots.

(13) Line 3-4: I suggest to discuss that aged worm show elevated dwelling like behaviour.

(14) Please use a consistent color & pattern code for genotypes and conditions, see Figure 4 where this gets confused.

Bruno, A.M., Frost, W.N., and Humphries, M.D. (2017). A spiral attractor network drives rhythmic locomotion. eLife 6, 471.

Gonzales, D.L., Zhou, J., Fan, B., and Robinson, J.T. (2019). A microfluidic-induced C. elegans sleep state. Nature Communications, 1-13.

Kato, S., Kaplan, H.S., Schrödel, T., Skora, S., Lindsay, T.H., Yemini, E., Lockery, S., and Zimmer, M. (2015). Global Brain Dynamics Embed the Motor Command Sequence of Caenorhabditis elegans. Cell 163, 1-50.

Nichols, A.L.A., Eichler, T., Latham, R., and Zimmer, M. (2017). A global brain state underlies C. elegans sleep behavior. Science (New York, NY) 356, eaam6851.

Reviewer #2 (Recommendations for the authors):

The authors nicely demonstrate that neural dynamics slow down as animals age, and that this is also a reflection of known behavioral changes, e.g., enhanced reversals. The changes in the reversal command neurons mimic those behavioral changes, with AVA displaying a larger duty ratio. They also show that neural dynamics are grossly changes in young adult and 9-day old adults. Overall, I believe that this paper should be published in eLife if a few major issues are addressed.

(1) To convincingly support their interpretation the authors should add some further sensitivity analyses and control experiments. The key issue for me with the approach taken in this paper is the lack of controls for the changes in the GCaMP signal that can be obtained as a function of age. It is possible that a lot of the effects observed in aging worms is in fact due to changes in protein synthesis and degradation, or changes in the cellular environment altering the kinetics of GCaMP.

(2) – Also related to reviewer #1: But even for clear effects, such as the nicely demonstrated slow-down in neural dynamics the choice of quantification method is not ideal: While the PSD is in principle a good tool for detecting dominant timescales/frequencies in time series, here it might not be the ideal choice: the highly autocorrelated time series (see Figure 2b) only shows very few periods of the lowest frequencies. In this case, the expected output of the PSD is noisy, and dominated by finite sample effects. The presence of 1/f noise is clear from the Figure 3a. To determine how significant the measured PSDs are, error bars would also be very useful.

(3) Similarly, the effects of the smoothness in the PCA trajectories might likely reflect a signal-to-noise ratio issue and a shorter sampling of the neural manifold, rather than a true change in neural activity beyond slowing.

To strengthen these conclusions, the authors could choose one of the following:

– Mimic loss of signal in younger animals e.g. by choosing a less strongly expressed indicator or by bleaching a young adult to a level comparable to day 9 adults.

– Or: determine the expression level of the data.

– _in silico_: test the robustness of the conclusions to noise in the data, as well as shortened sampling. Again, this can be done purely computationally by resampling the day-1 dataset to mimic the slower dynamics of the aged data, and rerun the PSD (to check for finite sampling) and by adding e.g. Gaussian white noise to the dataset (to see the effect of noise of the PCA and correlation metrics).

(4) A key statement made by the authors concerns the loss of correlation between neuron pairs. Due to the rather long autocorrelation within each neuronal trace, the estimation of the time-correlation between neurons is likely biased. This is of concern, since the autocorrelation of neural activity traces between day-1 and day-9 data appear very different, resulting in different effective degrees of freedom. This issue could be addressed by down sampling the day-1 data or -if possible- obtaining a longer day-9 data set and checking if the result still holds.

Note from the consultation session:

I think data of 20 min would definitely help, but one would need to evaluate the actual effective sample number which should be ~Recording length/autocorrelation time and ideally match that between groups.

Other concerns:

– How likely are the neurons that are segmented exactly the same between the day-1 and day-9 worms? Is it possible that due to signal-to-noise different neurons are measured and these have different statistics, affecting the conclusion about the inhibition change?

– Why is df/F0 used when the authors have access to dual-color recordings? It might be advantageous to use the ratiometric signal.

– How is F_0 defined? – see also reviewer #1.

– Figure 4: The data for the positive correlation proportion for ages/genotypes is states as ‘data’ not shown’. It should be displayed somewhere, at least in the supplementary materials.

– The connection between the negative-correlation proportion and excitation-inhibition should be clarified in the Results section and the discussion. It would be especially helpful for the reader if the sentence ‘we would not expect increased inhibitory tone from an exogenous ligand to affect neuronal connectivity’ were unpacked.

Reviewer #3 (Recommendations for the authors):

(1) Figure 2: Please add 2D-projected videos of the whole brain activity of day 1 and day 9 worms, for example, as Supplemental Figures.

(2) Figure 2: Please show PC 1-3, like in Figure 1D of Kato et al.’s study (Cell, 2015).

(3) Figure 3: Is it possible to show example(s) of anticorrelated activities by using the heatmap in Figure 2A?

(4) Figure 2: Similarly, is it possible to show example(s) of frequency change in PSD by using the heatmap in Figure 2A? I would like to emphasize this point because, in my understanding, the aged worms exhibited long-term changes in neural activities as seen in Figure 2A and B, which seems inconsistent with the high-frequency shift.

(5) Although the results of genetic and pharmacological analyses are quite interesting, they are unfortunately not convincing. This is because each gene was analyzed using only one material – one mutant allele (unc-2(gf), unc-2(lf), daf-2, ced-4, sel-12) or an agonist (muscimol for GABAA receptor). Therefore, the phenotype could be caused by side mutation(s) or side effects. As a general principle, mutant experiments should be supported by a rescue experiment or by the use of at least two mutant alleles. In the case of unc-2(gf) and unc-2(lf), they seem to exhibit sort of opposite phenotypes, but the results are not strong enough to support the conclusion. In the case of unc-2(gf), N2;Ex[unc-2(gf)] can be used as in the original report (Huang et al., eLife).

(6) Furthermore, there is no evidence to support the function of these gene products in the brain, given that relationships between unc-2 and GABA were examined in the motor systems but not in the brain according to two previous studies (Huang et al., eLife 2019; Miller-Fleming et al., eLife 2016). In my understanding, UNC-2 P/CaV2 is broadly expressed, not only in GABA neurons, therefore it is difficult to see why unc-2(gf) only affects the negatively correlated proportion. Additionally, in which cells/neurons is ced-4 expressed? In ced-4 mutants, the neural circuits could be different because of cell death defects, and to address this issue, cell-type-specific rescue experiment is essential.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Age-associated changes to neuronal dynamics involve a disruption of excitatory/inhibitory balance in C. elegans for further consideration by eLife. Your revised article has been evaluated by Piali Sengupta (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed. Please further address the concerns by reviewers #1 and #2 stated below, as well as the minor points by reviewer #3. We may send your second revisions to reviewers #1 and #2 for a final evaluation.

Reviewer #1 (Recommendations for the authors):

The authors made major efforts to address my concerns. Still, I have a few remaining issues that I feel are not sufficiently addressed:

(1) Signal-to-noise ratios: I am not convinced that a 12 neuron random sample from each recording is sufficient to assess SNR across all neurons and conditions. I think the authors should devise a systematic SNR analysis across all neurons, which I understand is not trivial but essential.

The authors did not address my concern that expression levels of GcaMP and RFP as well as tissue autofluorescence might change drastically over the course of ageing.

(2) The authors nicely show in the revised manuscript that global quiescence increases with ageing (on its own already an interesting observation) and that this effect does not entirely account for the decrease in anti-correlativity in their wild-type strain. However, this analysis does not exclude that global quiescence does have indeed a contribution to the decrease in anti-correlativity, which could become major in one of their pharmacological and genetic manipulations. The analyses shown in Figure 4b-c and Figure 4 supplement 1 should be performed across all conditions.

Reviewer #2 (Recommendations for the authors):

Unfortunately, the authors have not fully responded to my concerns.

My concerns are still regarding the SNR and duration of the measurements. However, I believe these additional analyses could be added in a short timeframe.

1. The definition of SNR used (while previously published), makes the unstated assumption that the noise is independent of the signal amplitude. This is clearly not true here, as can be seen from the raw traces in Figure 4a, and even the single-neuron traces in Figure 1. Sampling the noise of the ‘off’ periods severely underestimates the noise of the measurement and inflates SNR. If the authors could redo the calculations e.g. using fluctuations of a mean-subtracted signal that would be a stronger evidence of no loss of signal as worms age.

2. The 20 minute recordings. While I am happy to hear the authors successfully completed 20 minute recordings, the presented results didn’t cover all my prior questions:

– The PCA plots for these data are not shown, and I would like to see the results of a down-sampling of the 20 min recording to observe the effects of slower neural dynamics on the PCA plot. Similarly, the correlation plot for at least one 20 min recording would be useful to demonstrate the similarity with the 10 min recordings.

– The PSD analysis for the 10 and 20 min data isn’t shown at all.

3. Quiescence analysis

This is a nice addition to the paper, which connects their results to prior studies.

However, I am a bit surprised at how the results are framed: the data in S4.1a (left), and (b) is described as a ‘dramatic reduction’ in negative correlation proportion, whereas the (visually very similar) data in S4.1a (right) is described as not significant. However, the similarly not significant data in S4.1d is described as a trend.

In contrast to the authors, I would interpret these results as at least contributing to their observed effects, given the trends of all measures in Figure S4.1. While a lot of the quiescence effects are not holding up to the small sample size, a n.s. here could be simply due to low sample size. I wonder why the authors did’'t add the 20 minute data here to increase their numbers and possibly get a conclusive answer.

Reviewer #3 (Recommendations for the authors):

The authors have adequately addressed most of the previous reviewer comments. I think the manuscript is acceptable for publication once the following minor problems are solved.

1) p. 1, line 10: Unnecessary“"”" in front of“"”".

2) p. 5, line 24: It should be Figure 2-Figure sup. 2, not 1.

3) I am glad to see that unc-49 mutants exhibited the changes opposite to the ones by muscimol. However, day 9 results are not shown in Figure 5-Figure sup. 1, although it was mentioned in the main text (p. 15, line 20-21). Is it a mistake?
