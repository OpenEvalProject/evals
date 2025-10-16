# Peer review - Round 1

Editors:
- Jan-Marino Ramirez, Seattle Children's Research Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53186.sa1](https://doi.org/10.7554/eLife.53186.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Brain states govern the spatio-temporal dynamics of resting state functional connectivity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Büchel as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this study, the authors reproduce and expand their previous work showing that functional connectivity in the rat brain differs between persistent state, as induced by medetomidine anesthesia, and slow wave state, as induced by deep isoflurane anesthesia. They expand the common ICA analysis to show that there are more significant correlations between brain regions under isoflurane than under medetomidine and that the networks under isoflurane resemble a random graph, while those under medetomidine resemble small world networks. Further, the authors provide evidence for their hypothesis that down-up transitions (as they call the onset of a slow wave event) of neuronal excitability as found in slow wave state drive functional connectivity. To probe this, they employ an unusual combination of calcium recordings and resting state fMRI. Combining these two approaches is challenging. In four of five animals they find a correlation between the number of significantly correlated brain regions and the number of down-up transitions. This result has important implications for resting state fMRI, since it calls for strict control of the brain state during resting state fMRI measurements.

Essential revisions:

As you can read from the following comments, there are two recurrent themes: (a) your text needs to be revised to make it easier to understand for the general reader. (b) you need to specify the statistics used to analyze your data.

1) Many of the observations reported in this study have previously been described (e.g. increasing cortical synchrony within high iso condition vs low iso or vs medetomidine (e.g. PMID: 20530220, Grandjean et al., 2014), network connectivity strength between conditions (Bukhari et al., 2018), graph theory metrics (D'Souza et al., 2014), frequency/power distribution (Paasonen et al., 2018, Grandjean et al., 2014), reduced connectivity when global signal is removed especially when there is global connectivity synchrony in high-iso (Grandjean et al., 2014)). Please cite these published findings and relate to the present study.

2) The combination of BOLD fMRI with the slow-rave recording by photometry (Figure 6B) is novel. However, there, a few methodological concerns that need to be addressed. Most notably, the concept of independence is violated in Figure 6B, because the sampled variable (number of slow-wave and number of significant edges) overlap in their sliding windows approach (3 min windows with 1 min overlap with both the previous and next window). Thus, in a statistical test, the samples may not be considered independent from one another, a key tenant of statistics.

3) The work would gain importance, if these results were reproduced in a larger group of animals. In particular, graph theory analysis is usually performed in larger cohorts of animals (or at least data sets). However, additional data analysis can also strengthen the paper substantially.

4) The text is often unclear, lacks proper definitions, there is wrong punctuation in several places making it difficult to read (some examples below). Specifically there are some terms that are not precise or incorrect in the text. For example, the Abstract refers to "these bimodal recordings". It is not clear to what this refers. Next the Abstract refers to a "persistent state". Normally one refers to "persistent activity", and maybe after a classification, it can be referred to as "the state with persistent activity" or even the persistent state.

4.1) Along these lines: Some sentences in the manuscript are rather confusing, or even wrong, for example in the Introduction there is: "The concept of brain states as defined by the local and global features of network dynamics by no means entails, that different behavioural states as e.g. anesthetized condition or natural sleep would be identical, however, defining features of the slow wave state, such as bimodality, can be identified in a plethora of different conditions as the fundamental difference between fast and slow timescale cortical dynamics is likely regulated by distinct mechanisms at the single neuron level". This needs rewriting.

4.2) With regards to revising the text: In the Introduction it is said: "Surprisingly, in rodents as in humans, little has been investigated on how the brain's current state impacts functional connectivity derived from BOLD activity, despite evidence that, for instance, small changes in anaesthesia can dramatically change brain connectivity ". This suggests that, if small changes in anaesthesia result in dramatic changes in brain connectivity, different brain states are -not surprisingly- going to have an impact on functional connectivity (as it has been shown, although questions remain open).

4.3) The Results start by referring to " We first conducted independent component (IC) analyses of rat task-free fMRI signals in the isoflurane-induced condition, and in the medetomidine-induced condition." Then one wonders, why in medetomidine? Lacking the information that medetomidine is the way to induce "persistent state" (given that the experimental paradigm in this regard was not described earlier). There is a poor definition of the "persistent state" in the presence of medetomidine. It is obviously a different brain state from slow waves, but what kind of brain state? How different is it from the awake? To what extent is it dose-dependent (as indeed it is)? If there is a detailed characterization by the authors or in the literature, it should be better reported, describing what is the state induced by medetomidine. It should be included at the start of the results including what the comparison is, and why medetomidine is a good equivalent of awake.

4.4) In the Discussion: "In contrast, animals in slow wave state showed fast, and temporally irregular transitions. This suggests, that individual, specific events within the slow wave state drive the state-specific network signature The occurrence of these events, down-up transitions, or slow waves, are not occurring in a regular, oscillation-like manner, but depend on the overall physiological state of the animal, such as the depth of anaesthesia.". The concept of "temporally irregular transitions" is confusing. The frequency of the slow oscillations may vary with depth of anaesthesia, however this is compatible with regularity in the oscillations.

4.5) In the Discussion: "Although, there is abundant evidence on the relevance of infra-slow electrical brain activity for resting state connectivity there has been no direct neural evidence so far linking brain states to changes in network configuration". Indeed, there are articles both for humans and for rodents illustrating different connectivity patterns with different brain states. However, the relation with the infra-slow (unmentioned so far) here is not that clear.

4.6) In the Discussion: "pathophysiological condition such as early AD", since the acronym AD was never defined earlier in the text, please use the explicit term.

4.7) Discussion: "In this study, we demonstrated that brain states can modify properties of the functional connectome through changes in cortical excitability." We do not know that it is just "excitability", since excitability is a broad term. There are other concomitant differences, such as dynamics.

4.8) The study of the cross-correlations during down to up states is highly suggestive but needs more robust and obvious evidence than that provided.

5) Description and presentation of the ICA is currently not sufficient.

5.1) More details on how ICA was performed are required: e.g. how many components were allowed; which components were assigned to noise, and how was this done; was breathing or heart rate used as regressor;

5.2) Presentation of ICA results is not clear: how many components were assigned to brain activity; what were the weights of these components; showing only three slices is not sufficient – include all slices relevant slices of the respective networks.

5.3) How was the DMN defined (ie which brain regions were included)? How many of these were found in the ICA component(s) and in which? Suggestion: perhaps register the ICA results on the brain atlas and provide quantitative data on how much of the respective network was identified – how were the average z-scores there.

5.4) To better illustrate the difference between the brain states, the authors may show serial slices of the brain for SW and P state, so the reader can see which regions were identified.

6) Since the activity of different networks in the different brain states is the fundamental point of this paper, the authors should provide a confirmation of their ICA, by performing a ROI based correlation analysis. This should be easily doable with the data and the atlas the authors have used already. Such independent confirmation of active networks in the different brain states would make a strong point and probably silence most of the doubt in the community.

7) Graph theory provides far more information than global results as shown in Figure 4. It would be extremely interesting to see how communities actually are different between brain states. Please provide a representation (e.g. a 2D plot using a force-based algorithm) of the networks in the two brain states.

8) There is a dramatic difference in noise level in the calcium traces in Figure 5 between SW-I and P-M. Is the scale bar with 3% valid for all three traces or only for the top one? Are these data from the same animal, were they acquired in the same session? If yes, the anesthesia switch needs to be described in both Materials and methods and caption. Add scale bars for each trace. Explain experimental details in the caption. Since there seems to be substantial variation in noise levels, the authors should provide exemplary calcium traces for all conditions for all animals (as a Supplement).

9) Why was 0.5-0-7% isoflurane added to medetomidine? This appears arbitrary. Is anything known about which concentration induces brain state changes. How does isoflurane concentration influence networks or hemodynamic and calcium signal. Please discuss.

10) Results shown in Figure 6Bii should be additionally validated by performing correlation plots not only with number of events but also with 1) total up-time during the 180s, 2) average amplitude during the 180s, 3) position of the 180s-frame to exclude an effect of time during 30 min. Please show data also for the fifth animal.

11) What is the meaning of cross correlation amplitude of filtered data as shown in Figure 7D and E?

12) Figure captions do not provide sufficient information. Make sure that all symbols are explained, and experimental conditions become clear – for all figures. Three examples: Explain what is shown in the boxplots. What do lines between left and right data in box plots indicate? What do shaded areas indicate (SD, SEM,…)?

Related to this, there is no statistics described in the Materials and methods section. Adding details is very important to determine what test and how it was performed. Without such a section, the reader cannot assess the plausibility of the results, and thus cannot provide in-depth comments pertaining to the results.

13) Connectivity matrices must be labelled to identify the individual brain regions. Add a legend on the matrix or a color code plus legend (probably best as a supplement).

14) Were both positive and negative correlations used. For graph theory analysis is usually separated for positive and negative correlations.

15) Please explain in detail the process of adjacency matrices construction and the calculation of the threshold.

16) Connectivity analysis, second paragraph: Please specify the procedure of FDR. Please give the correlation value of connectivity strength and distance not only its significance.

17) There is no information about the topography of the FC. It is shown that the correlation between Euclidean distance is more negative in slow wave state. It could illustrate that during slow wave state the activity is propagating so the FC follows a spatial gradient rather than long-range connections. Actually, in Figure 2A, one can see that the interhemispheric connections are weaker in slow-wave state than in persistent state, although the overall correlation magnitude is larger.

18) In Figure 2A, 5C, 6A and 6B, please consider labelling the axis of the matrices, not with all the 96 ROIs but at least partially to give the reader a better idea of the average connectivity found in the two states.

19) Figure 2C: please describe the test used both in text and figure caption.

Figure 3: missing the number of the individuals in the figure legend.

20) In the section Connectivity differences are reflecting different brain states: "In this case, the resulting values of persistent state induced by low isoflurane…. (Figure 4D) (t(5)=5.19, p=0.003). We used the same matrix similarity computation in a dynamic connectivity analysis […] than in the case of slow wave state induced by high isoflurane concentrations (Figure 4E). ". There is an incorrect figure reference, it must be Figure 5D and 5E.

21) In Figure 7B and C, are those recordings from V1 or S1? Consider showing both together for consistency and to show the propagation delay. Maybe different colours can be used for V1 and S1 and different shades for the filter's frequency bands.
