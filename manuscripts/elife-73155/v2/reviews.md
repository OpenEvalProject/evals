# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73155.sa0](https://doi.org/10.7554/eLife.73155.sa0)

This paper will be of interest to electrophysiologists, systems neuroscientists and neural engineers. The authors describe a framework for evaluating the comparison between LFP dynamics and spikes and perform this comparison for several datasets recorded from motor, premotor, and sensory areas of cortex in rhesus macaque monkeys. These results serve as an important benchmark for the information content of LFP recordings, which is relevant to data collection in neuroscientific investigations and to designing brain computer interfaces.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73155.sa1](https://doi.org/10.7554/eLife.73155.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Srdjan OSTOJIC as the Reviewing Editor and Ronald Calabrese as the Senior Editor. The reviewers have opted to remain anonymous at this stage.

Both reviewers were enthusiastic about the manuscript, but have suggested additional analyses and improvements to the text.

The Reviewing Editor has drafted a consolidated list of suggestions to help you prepare a revised submission.

Essential revisions:

Analyses:

1. Given the frequency-based analyses presented, more detailed characterization of the LFP spectra will greatly benefit the paper. A key question the authors should address is whether the frequency-dependence (and its variance across areas) is related to differences in power spectra across areas. They present an analysis suggesting their results are not simply explained by variance differences across bands, but there are no analyses to address power differences (and deviations from the 1/f "noise" spectrum).

2. It would be beneficial to include cross-frequency analyses (e.g. correlation/coherence between LMP and 200-400 hz). The discussion notes that there are potentially different sources of the LFP-latent correlations. More detailed comparisons of relationships within LFP frequency bands and with kinematics might begin to shed some light on this important issue and increase the manuscript's impact. This could be particularly interesting for PMd and area 2 where the 12-25hz band and higher frequencies are both correlated with latent activity, but only higher frequencies are predictive of behavior.

3. The "stable" claims focus on behavioral epochs while ignoring time. Are these relationships consistent across sessions?

4. A supplemental figure showing LFP-latent correlations vs. predictive accuracy on a single electrode basis would be beneficial.

5. The LFP-latent correlations appear larger in M1 than PMd. Is this statistically significant?

6. While the LFP-signal neuron firing correlations are clearly much smaller than LFP-latent correlations, Figure 8B and S8C/E clearly suggests a correlation between these two variables. This should be quantified and discussed.

7. The points below are focused around the central hang-up Reviewer 2 (R2) had while reading this paper: it seems like the motivation for this paper raises the question of what are the discrepancies in information content between LFP signals and latent dynamics estimated using spiking data. The authors do appropriately defend a narrow interpretation of their hypotheses, however, so the following comments should be seen as suggestions that the authors can choose to incorporate if they agree with the proposed rationale. If the authors choose to address these limitations, this would broaden the utility of these results for interpreting studies performed with LFP, or making concrete recommendations regarding future data collection. If the authors choose not to address this, please clarify the rationale and moderate the claims regarding the prescriptive relevance of the study for helping to contextualize LFP-only experiments.

– While R2 liked the questions and motivation for this paper, they were confused by the rationale central to details of the approach the authors used. It seems clear from the main text and methods that CCA is applied independently between the set of latent dynamics [#dim x #timepoints] and individual LFP channels [1 x #timepoints]. Initially, R2 assumed that the CCA was applied to multi-channel single-band LFP data [#channels x #timepoints], allowing for a comparison between two n-dimensional manifolds. This approach, instead, seems to look for the single best alignment between any one signal and one specific dimension of a (rotated) n-dimensional manifold. Using this as the primary metric gives us a sense for how well the signal for each single LFP band and channel is represented within the set of latent dynamics, but doesn't reveal what, if any, information is absent (or present) in LFP vis-a-vis latent dynamics, and vice versa. The correlation metric employed in this work does a good job of establishing that the analyzed LFP signals from individual frequency bands are well represented (or not) within the latent dynamical manifold. It does not, however tell us what information is lost by only considering LFP, which seems to be an important limitation of the approach.

– More specifically, it would be interesting to know if the combined signals from all LFP bands can be used to estimate the latent dynamics. Since the latent dynamics are assumed to be the ground truth for neural state, this seems like the most direct statement of a crucial question. If we form a matrix with dimensions [(#bands * # LFP channels) x #timepoints] and perform PCA on that matrix, does the resulting manifold look anything like the manifold estimated using PCA on spike data? If not, are the distortions the result of noise or a consistent bias?

– Regarding the point above, a complete investigation of the differences in information content between LFP and latent dynamics may be beyond the scope of this this paper, but methods such as probabilistic two-way partial least squares (PO2PLS, see [1]) might be appropriate for identifying components of shared variability, and private variability, between two matrices. In this case specifically, this approach (or another algorithm), could be used to identify components of the multidimensional data which are shared between LFP and the latent dynamics, and components which are only present in each modality's data alone. To be clear, it is up to the authors to choose whether they feel this suggestion is appropriate and within the scope of the work and aligned with their question.

– Regarding the points above, the presentation of Figure 3 is clear, but easy to misinterpret. By presenting 10 frequency bands (nine freq + LMP), compared with 10 latent dimensions, it gives the impression that the alignment procedure is being performed between the multi-band data and the latent dimensions. If this is indeed what was performed, then the text in the main manuscript and the Methods (page 17, Alignment of latent dynamics and LFPs) is confusing.

Text improvements:

8. Some further details of signal processing would be beneficial. For instance, the authors must be doing some form of normalization in power if the bands have similar variance across frequency, but it is not described in the methods. The computations used for the LFP variance analyses are also not explicitly defined, which is unfortunate given the importance of the control. There are several ambiguities in the methodological descriptions of LFP signal processing: 1) subtracting the average "over time" should have the time range defined (for each trial? Across a whole session?)), 2) "We subsampled the LFP signals…", should specify whether they mean broad-band LFP or (more likely) the post-processed signals (e.g., the estimated power time-series in each band).

9. Axes limits across figures need to be standardized. When showing data for two subjects side by side, axes limits should be the same. When comparing two variables to show relationships, the limits for each variable should be the same (i.e. square aspect ratio). These conventions are not systematically used across the manuscript (Example figures: Figures4D, 6B, 7B). Using a consistent scale across all plots of correlation etc. would be helpful for facilitating direct comparisons across areas.

10. The manuscript could be more precise in stating that the authors are looking at within-area relationships only.

11. The statement that β band activity (15-30 Hz) is "less informative" of behavior should be made more precise. Β band power is highly predictive of e.g. movement onset in well-trained tasks. The authors are presumably referring to predictive power of continuous-time kinematics.

12. The introduction's second hypothesis "Second, this relationship should be frequency-dependent, because only specific LFP bands are strongly correlated with the behavior." Somewhat conflicts with the presented data, consider revising this.

13. Figure 3's legend refers to "three reaches" but appears to show 4.

14. The authors state that this work "helps to bridge the wealth of studies reporting neural correlates of behavior using either type of recording," but stop short of making recommendations regarding future experiments or providing other prescriptive takeaways. While addressing this could easily expand beyond the scope of the work presented here, there are some questions that are natural to ask given the highlighted motivations. If little information is lost between LFP and latent dynamics, should we consider only recording LFP? For the design of neural sensors, recording LFP only would greatly reduce the bandwidth, and associated power and data storage or transmission requirements. Given a fixed power budget, one could use many more LFP channels than AP-band channels, suggesting a tradeoff between the number of LFP channels and the accuracy of the estimated neural state. It is perfectly fine for the authors to decide that this question is out of scope for this paper.

15. Figure 3B and 4B – the yellow lines for the 200-400 Hz band are hard to see. This plot uses the same color scheme employed in all other figures, and updating all figures is not a productive use of time. Altering the color for this one panel or thickening this line, or really anything else could help readers make a visual comparison to behavior and latent dynamics.

16. Figure S5 – Why is classification performance for reach direction so low for the low frequency bands when the correlation with latent dynamics is high, and the classification performance for latent dynamics is also high? Is this a concern or not?

17. Were time lags (e.g., ~50 ms) used when correlating behavior and LFP or latent dynamics?

18. Figure S5 – Missing panel label for panel D

References:

[1] Said el Bouhaddani, Hae-Won Uh, Geurt Jongbloed, Jeanine Houwing-Duistermaat. Statistical Integration of Heterogeneous Data with PO2PLS (https://arxiv.org/abs/2103.13490)

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. Specifically, we suggest tempering the claims that results reflect signatures of connectivity, as the evidence is indirect.

Reviewer #1 (Recommendations for the authors):

I thank the reviewers for their responses to my initial comments. Overall, the additional analyses have improved the manuscript. However, I have some lingering comments that I feel still need to be addressed before the paper would be suitable for publication.

1) One of the manuscript's primary claims is that LFP-latent correlations are "stable" within areas while being different between areas. These claims are the main basis of their interpretation that these relationships reflect biophysical properties of the cortical networks (e.g. cytoarchitecture). The claim of stable relationships focuses on comparing motor planning and execution task epochs. These task epochs appear to include partially overlapping time windows based on their methodological description, which seems like a potential confound that should be addressed. The time windows used are also different durations, which should be controlled for. Moreover, their results also show that LFP-latent relationships change (mostly disappearing) in inter-trial intervals. If these correlations truly reflect properties of circuit structure, I am unclear on why they would be task-dependent. This interpretational point needs significant clarification."

A related point is that the hypothesis stated in the introduction does not match well with the claims made by the results themselves. The introduction states "given that the synaptic connections remain stable in the short time scale spanning the preparation and execution of a movement, we expect the various LFP-latent dynamics associations should remain equally stable throughout these two processes underlying behaviour." This is a claim rooted in the underlying structure of neural circuits. In the section presenting the results, the authors say that seeing similar correlations in the movement and planning epoch: "indicates that the observed association is not a trivial epiphenomenal consequence of the frequency content of movement, but instead likely reflects underlying physiological processes related to the production of behaviour." which is not a claim about the underlying neural circuitry directly. The discussion then primarily focuses again on the goal of interpreting population activity as a reflection of neural circuity (e.g. connectivity).

The manuscript needs to be significantly strengthened if the authors wish to make claims in the introduction and discussion about their observations reflecting signatures of the underlying brain networks (cytoarchitecture and connectivity). Alternately, the introduction and discussion need to be revised to alter these claims.
