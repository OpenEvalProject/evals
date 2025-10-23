# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, National Centre for Biological Sciences, Tata Institute of Fundamental Research , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26337.016](https://doi.org/10.7554/eLife.26337.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Odor concentration-invariant subnetworks in the mouse olfactory cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered for publication in eLife at this time. The reviewers felt that the concerns with the paper were too substantial for acceptance, and would not be feasible to address within a short period. They were unsure if the conclusions would still stand after a re-analysis, but did feel that with substantial changes the authors might be able to address the major issues in a resubmission.

A summary of the key points made by the reviewers is below:

This study looks at large-scale coding using optical recordings and concludesthat a subset of piriform neurons respond in a concentration-invariant way,and can be used for identity coding. The dataset is a potentially useful, broadpopulation readout of piriform cortex activity.

1) The reviewers were concerned that the identification, analysis, andrelevance of the concentration-invariant neurons was not well supported.

The authors should be able to devise a model that would more completelyutilize the data.

2) The authors should provide a strong analysis to support theirassertion that the subsample of cells reliably defined odors in aconcentration-invariant way.

3) There should be a more complete analysis of topography of odor responses.

4) This paper doesn't really draw upon the data from the companion paper,and indeed in some ways doesn't seem to match.

There should be a much better discussion of the effects ofanesthesia, which could compare the two datasets.

The analysis of concentration coding in the two datasets could bedone in a comparative manner, with equivalent analyses in the two cases.

5) The authors should provide a better analysis of the dynamics of responses.

Reviewer #1:

This study looks at large-scale coding using optical recordings and concludesthat a subset of piriform neurons respond in a concentration-invariant way,and can be used for identity coding. These are anesthetized recordings, andit would be difficult to do these in awake animals given the quite invasivesurgical preparation.

I review this in context of the companion manuscript by Bolding and Franks.

What do we learn from the current paper that the Bolding manuscript does not say?

The main point here is to identify a subset of concentration-invariant neurons. I'm not sure that this isn't there in the Bolding dataset, but the authors don't seem to have looked for it. I'm surprised that the classification accuracy is so low (69%), with a few hundred neurons on each trial. I'm also surprised at how slowly the classification accuracy builds up and declines. Possibly this is an artifact of the anesthesia.

Overall, I get the sense that the power of optical recordings hasn't beenfully utilized in this study, and that the analysis could be extended toextract more information from the already obtained data. On its own, and inthe present form, the main result of a few cells being concentration-invariant seems limited.

1) The key point of the paper is that piriform odor representations change withincreasing concentrations, but a 10% subset of neurons stay consistent andappear to code only for identity. The authors compare this with an analysisof previous data on OB M/T cells, which are mostly concentration-dependent.

While this result is interesting to olfactory physiologists, I was looking fora more detailed analysis, or a mechanistic insight. For example, ifone confines oneself to fewer odors, does the same subset of neurons stayconsistent? Can the authors devise a model that would span the range fromfully concentration-invariant to concentration-dependent for all odors?

2) I don't see any attempt to relate the optical findings to the electricalrecordings in the companion paper. If one were to filter out the different time-resolutions, would the optical findings simply fall out of the electrical ones? Does the fraction of concentration-independent neurons match?

3) The frame rate for these recordings is quite good, 15 FPS. I am surprisedthere is no analysis of the dynamics of responses for individual neurons,or to compare them between the concentration dependent and independent cells.

4) Did the authors record respiration? Given that the animals were anesthetized, it seems likely that at this frame rate it should be possible to examine respiration dependence of the piriform responses.

5) There are a couple of findings that the authors don't really follow up.

For example, the authors briefly mention functional heterogeneity of PFneuron responses, but they don't seem to follow this up. Also, there isthe finding that the number of responsive Piriform neurons is roughlyindependent of odor concentration.

Reviewer #2:

In their manuscript, 'Odor concentration-invariant subnetworks in the mouse olfactory cortex', Roland et al., investigate how ensemble activity patterns in the olfactory cortex decode odor identity vs. intensity. The authors employ multiphoton imaging in anaesthetized mice and probe GCaMP6s responses to different odors and concentrations. They find that odor identity can be accurately decoded from the population activity using a linear classifier. Across different concentrations, the population representations of odorants change, thus degrading information about odor identity. As a solution to this issue, the authors propose that a subset of concentration-invariant cells in the olfactory cortex is well suited to decode odor identity in a concentration invariant manner.

The study is topical and the experiments are carefully performed. However, I have several major concerns with the interpretation of the results presented here, which, in my opinion, preclude the publication of the manuscript in the current form in eLife.

1) The authors report ~10% concentration-invariant neurons in the PC vs. ~5% in the OB. They perform a shuffling control and suggest that, unlike the OB, the emergence of concentration-invariant cells in the cortex cannot be attributed to chance sampling. Therefore, these neurons represent an emerging feature of the cortex and can solve the identity problem irrespective of changes in concentration.

The fraction of invariant cells is rather small in both the case of cortex and the bulb. The large majority of neurons in the cortex vary substantially in their responses with changes in concentration (Figure 3). Therefore, to this reviewer, asserting that concentration invariance is solved in particular by these neurons is somewhat more anecdotal rather than based on testable evidence. The authors sample 6 times more neurons in the olfactory cortex compared to the bulb (~3,000 vs. 500). Therefore, it is important to determine whether sub-sampling the olfactory cortex data to match the OB recorded cells, and relaxing the significance criterion from p<0.01 to p<0.05 (Figure 6E) change the results presented.

The cross-concentration correlations of odor representations given by even the neurons identified as 'concentration-invariant' are relatively low (0.56, 0.60). What is the average correlation between the neuronal representations of the same odor across repeats, for each of three concentrations sampled? For example, in Figure 5D, for ethyl acetate and hexanone, the correlations across repeats for the highest concentration appear by visual inspection higher than 0.8. This value is substantially higher than the correlations reported between the low-medium, medium-high or low-high concentrations in the sampled range. These observations put into question the concentration-invariant status of these neurons.

Can the authors provide a testable model on how the concentration invariant cells are preserved as such across a wider concentration range (for example 50,000 fold vs. 100 fold sampled), and also how this information is readout selectively?

In addition, in the companion paper (Bolding and Franks), in awake animals, a different mechanism (at the whole population level) is proposed for decoding odor identity, while concentration is read by changes in response latency. Can the authors comment how these two perspectives relate to one another?

2) Comparison of olfactory cortex and olfactory bulb activity patterns is hard to interpret in anaesthetized mice since recent reports suggest that cortical feedback is strongly affected by anaesthesia (Rothermel et al., 2014, Boyd et al., 2015, Otazu et al. 2015).

3) Figure 3's title is not supported by the data. Both the percentage of active neurons and their identity change across the sampled concentration range (3B, C). At the level of individual cells, there is substantial variability in lifetime sparseness across concentrations (3D), even though the percentage of neurons that show similar lifetime sparseness values is same across concentrations. In my opinion, such observations invalidate the title's claim that the overall levels of piriform cortex activity remain largely stable across changes in concentration.

Reviewer #3:

Concentration invariance is known to be a key property of odor identity coding, and the work of Roland et al. is the first (together with a co-submitted article by Bolding and Franks) to study how piriform cortex solves concentration invariance. Furthermore, the authors use a preparation which allows for simultaneous monitoring of large ensembles of spatially-defined neuronal populations, allowing them to examine how concentration-invariance is implemented at the population level.

The authors demonstrate the presence of concentration-invariant neurons, which comprise a subset of piriform neurons. Additionally, a separate sub-population of piriform neurons change their activity as a function of odor concentration. This is an important observation and is worth publishing. However I have a few comments:

1) One of the novel observations is that the concentration-invariant subnetwork lacks topographic organization in piriform cortex. The authors should elaborate more on this point. The case against topographic organization is made in Figure 2—figure supplement 2 by showing similar classification using a local versus random clustering rule. However, this may not rule out that topography exists. (1) It is possible that any single specific topographic mapping may be washed out in the averaging procedure. The authors should perform an additional analysis: artificially simulating topography and performing the exact same analysis to check that this simulated topography actually yields a classification plot that is different from random. (2) Another possible suggestion to examine topography in piriform representations is to examine the spatial distribution of weights in the classifier.

2) The authors made a point about the trial-to-trial variability of piriform neurons (e.g. Figure 1E). A pertinent question is, what is the trial-to-trial variability for neurons in the concentration invariant subnetwork?

3) The author should discuss the effect of anesthesia in their preparations. They compared their research with electrophysiological study co-submitted by Bolding and Franks. The current study revealed the spatial distributions of identity encoding neurons. The authors should discuss the limitations of their approach and clarify what other conclusions can be safely extrapolated for awake case?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Odor concentration-invariant subnetworks in the mouse olfactory cortex" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers felt that the paper was stronger in this resubmission, and that several of the earlier comments had been addressed. Nevertheless, some key points remain.

Essential revisions:

1) The authors must clarify their methods specifically relating to non-randomness of the concentration-invariant responses.

2) The number of cells classified as concentration-invariant seems small and there was some discomfort on whether this population was statistically robust.

3) There must be clarification on what the 'average correlation' of 0.65 refers to: for each odor, or each concentration?

Reviewer #1:

In this revised paper, Roland et al. carry out optical recordings from anterior piriform cortex. They have performed substantial additional analyses of this rich dataset. In doing this they have mostly addressed my concerns from the earlier version of the paper.

The point about subsets of neurons involved in concentration-independent coding has been taken up with further analysis and discussion. The analysis on this is much more thorough.

The current version more completely discusses how the optical findings relate to the electrical recordings by Bolding et al.

The authors don't examine respiration dependence of responses, but do explain that the slow dynamics of GCaMP6s would have made this less useful.

The authors also carry out other useful analyses, including spatial organization of responses, and dynamics of responses.

Overall the study is a valuable characterization of population-wide odor responses in the piriform cortex and reveals interesting features of coding.

Reviewer #2:

In the second submission of the manuscript "Odor concentration-invariant subnetworks in the mouse olfactory cortex", the authors addressed all reviewers' requests and significantly improved the manuscript. I have only one concern.

In the original review, I requested an independent analysis of different features of the of concertation-invariant and generic cell responses in the piriform cortex. The authors presented results on Figure 7—figure supplement 1 Figure. I was hoping that it will reveal some differences between these two classes of cells. However, variability and temporal profiles of concentration-invariant and generic cell responses were undisguisable. This fact raised a concern about statistical significance of the phenomenon. The authors discussed "non-randomness" of concentration invariant responses. This is a very crucial piece of analysis, and the authors should present a better description for their methods, and some discussion of the results and their limitations. For example, if the observed proportion of concertation invariant responses is 11.7% and proportion of the responses due to random sampling is 5.3%, does it mean that the real concentration-invariant pool of cell is significantly smaller than 11.7%? Or what proportion of concentration invariant responses can be missed by chance, etc.?

Reviewer #3:

The authors did perform additional analysis as suggested, but in my opinion, they did not address the main points of criticism. Therefore, I still have concerns regarding the results presented here.

1) The new analysis unfortunately does not fully clarify the points raised related to the concentration invariance. It does show that this group of cells is less concentration variant compared to the entire ensemble of cells imaged. Yet, In the revised version of the manuscript, visual inspection still strongly suggests (Figure 6D) that for a given odor, the correlations across repeats for the same (highest) concentration are higher than correlations across repeats for lower concentrations.

In addition, the correlations across repeats for the same (highest) concentration for a given odor are higher than for the same odor across concentrations. It is unclear whether the average correlation (0.65 +/- 0.10) value given across repeats refers indeed to all odors and all concentrations. Is it the same (0.65 +/- 0.10) for each odor and for each concentration? Plotting side by side, for each odor the correlations across concentration (lowest-highest, lowest-intermediate, intermediate-highest), and respectively the average correlations across repeats for each odor concentration (at low, intermediate and highest concentration) would allow a direct comparison for each stimulus.

2) The small fraction of cells that are classified as concentration invariant, remains a concern, as well as lack of evidence that these cells in the data set indeed constitute a cell type as defined by layer, specific input/output patterns or any other features, besides the difference in observed responses (though proposed as such in the manuscript). It is also unclear what the decoding scheme is for a wider concentration range, except an actual change in perceived odor identity mentioned in the text.

It is indeed important to document that a higher percentage of neurons are called as concentration invariant in the piriform cortex compared to the bulb. However, I'm not convinced that the strong message and title of the manuscript should be focused on a result that summarizes, in the best case scenario, the behavior of ~10% of the responsive neurons in the absence of any additional evidence that these 10% of responsive neurons are doing the job as proposed.

3) The anesthetized vs. awake explanation is not robust. In my opinion, different cells can be differentially affected by the brain state, depending on the local and long range inputs they receive and the strength of corresponding activity patterns.
