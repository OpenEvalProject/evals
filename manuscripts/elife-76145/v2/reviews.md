# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76145.sa0](https://doi.org/10.7554/eLife.76145.sa0)

This study investigates the neural basis of the hidden causal structure between visual and proprioceptive signals in the primate premotor and parietal circuit during reaching tasks executed in a virtual reality environment, where information between the two modalities can be dissociated. The key novel result is that premotor neurons represent the integration of bimodal information for small disparities and the segregation for large disparities between the proprioceptive and visual information, while parietal cells show reaching tuning changes that support the updating sensory uncertainty between tasks.


---

# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76145.sa1](https://doi.org/10.7554/eLife.76145.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural dynamics of causal inference in the macaque frontoparietal circuit" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Hugo Merchant as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hugo Merchant (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The present results are novel and provide important notions. However, we have a series of important concerns.

1) First, the paper is difficult to follow. The authors should use a simpler and more intuitive framing of the paper to make it more accessible to a general audience. A reader needs to integrate a large part of the results to really have an idea of what is the paper about and how the authors tested their hypothesis. Indeed, the writing in part uses words or phrases that are 'unusual' or imprecise, which makes the text difficult to understand.

2) Another important concern is that the paper does not show the basic response properties of neurons on both areas across tasks. It is not clear how the neural activity changes between the VP, P, and VPC tasks. It is a change in preferred direction, in the width of the tuning function or on the gain modulation? We strongly suggest providing two 'layers' of information, one based on standards plotting and analysis, to be followed by a second layer of data investigation, addressed to more detailed computational aspects.

3) Statistics:

Results of model fitting: The methods mention that the authors compared three models: segregation, fusion and causal inference. However, in the results (Table S1) only two models are presented. The results for segregation should be reported for the sake of completeness. The Ppriori is high, e.g. 0.98 and 0.999. This makes me wonder in how far the R2 and the EPs' can be so much different between causal inference and fusion. Considering e.g. model averaging decision function for BIC, a prior of 0.999 would make fusion and BCI nearly identical. I feel that either the Methods section is lacking important details about the models (See above) or there is either a mistake in the analysis or the reported numbers in the table. The analysis of Bayesian models seems to lack major details, the statistical reporting is below standard (missing effect sizes, degrees of freedom, lack of individual data in figures), the study shows many unjustified parameter choices and key results seem to lack statistical support: not all statements about differences between parietal and premotor cortex seem supported by a direct statistical comparison. Further, while three monkeys contributed data, for only one does the study report data from both brain regions; this makes the claim of a difference between brain regions rather weak and this shortcoming needs to be clearly acknowledged. The actual underlying data (e.g. how single neuron responses are converted to tuning curves; how decoding accuracies vary across neurons) is not shown, which makes it difficult to interpret the robustness of the results. In particular, as the units of analyses vary tremendously between Figures (experimental blocks, neurons, pseudo-epochs, etc).

The updating of the believe about the sensory causal structure is a central component of this work. The authors present this as well established aspect of the BCI model (l. 170ff). However, most previous studies used a static model that was fit to the aggregate data of an entire experiment without taking the trial history into account (as in the cited Koerding et al. 2007 paper). AS some recent work has incorporated such trial dependencies, it would be important to acknowledge these studies and to explain the novelty of the present work (e.g. Rohe et al. NatComm 2019; Beierholm et al. eLife 2020; Badde et al. Cognition 2020 may also be relevant).

Analysis of recalibration: The analysis of P trials after the VP or VPC task effectively looks at what is known as trial-wise multisensory recalibration (see e.g. Bruns et al. Scientific Reports 2015; Park and Kayser eLife 2019; van der Burg et al. J Neurosci 2013; Wozny et al. JNeurosci 2011; Badde et al. Cognition 2020; there is extensive literature on this both in the spatial and the temporal domain!). It seems awkward to investigate this recalibration of uniusensory judgements without alluding to previous work.

If I understood Figure 3A and the Methods correctly, only in monkey N both brain regions were recorded? If this is correct, the statement that premotor and parietal regions differ in their representations is a result of a mixed within and between subjects analysis. This should be acknowledged explicitly, as it greatly reduces the statistical power of this statement, and the repeated statement about an N of 3 is misleading. CI neurons are defined based on a seemingly arbitrary criterion: exceeding a correlation threshold based on the arbitrary division of the data into 26 bins. Given that neural representations generally span a continuum, I would like to see the distribution of 'causal inference effects' for individual neurons, e.g. in form of a distribution of r2 values (obtained from the correlation; or a regression as I suggest below). The apparent difference between brain regions (Figure 3G) may simply result from the specific choice of statistical cutoff (the criterion of p<0.05 becomes meaningless in the presence of 475+238 tests in total). Seeing the individual-neuron data here seems vital.

The analysis of population timing suggests that premotor cortex leads (Figure 4F). Is it possible to extract by how much time? Also, the authors focus on the encoding of Pcom, which comprises both the a priori binding tendency and the discrepancy. Why did the authors not decode both the prior and the current multisensory discrepancy separately? This would seem important to differentiate neural signatures of priors from those of current sensory signals.

Showing the actual data: The key results (e.g. Figure 3C; 4F; 5B; 5F; 6C) would be much stronger rand more convincing if the actual units of analysis were shown in some ways. How does decoding accuracy vary across neurons?

Other details:

For most tests there are no measures of effect sizes reported, sometimes the respective test-statistics is missing, and the degrees of freedom remain very unclear. I understand that they wary between analysis, but given that some tests are based on the actually recorded units, some of pseudo-trials or binned data, it would be very important to report for each test the assumed independent units and their number. The false-discovery rate is mentioned frequently, but the precise method is not stated. Most analyses are based on Wilcoxon tests, but figures show mean and SDs. I encourage the authors to use the same nonparametric (or parametric) approaches for figures and stats (e.g. show boxplots and individual data). L. 892: what was precisely compared with the ANOVA? Cluster-based tests: the parameters and the procedures for this test are not reported (l.974)

To determine whether a neuron confirms to the expectation of causal inference, why is it necessary to bin the data (l 893ff)? Could one not simply derive a regression model for each neuron and visualize the R2 or F-value?

The authors seem to interpret differences in the significances (e.g. of cluster-based permutation tests) as significant differences between regions and as establishing differences in the relative timing of effects. These are statistical fallacies (e.g. Sassenhagen https://doi.org/10.1111/psyp.13335; and Makin https://doi.org/10.7554/eLife.48175).

For every statement claiming differences between parietal and premotor cortex it is necessary to directly impellent the respective contrast between neurons in each brain region to support such a difference.

Other methods:

Spike sorting: I could not find criteria used for spike sorting. Where the analyzed units single units or MUA? More details about spike thresholds, cluster separation etc. should be provided.

The total number of switches between blocks (e.g. P following VPC) should be reported, as this constitutes the effective degrees of analysis of the block switching analysis (Figure 2C).

Causal inference models and optimization: The methods leave it unclear how the two alternatives of common and separate sources were combined in the BCI model. Previous work has explored a number of decision functions (e.g. Rohe and Noppeney's work, or Wozny et al. PlosCompBiol 2010) but for the present study it remains unclear which decision function was used. Model fitting: how were likelihoods computed and the posteriors sampled for model fitting? I feel that the procedures are not described in sufficient detail to be reproduced. Over what range of disparities was the model optimized? This is important for the Null model mentioned later on. What is the precise number of data points that entered the BIC calculation?

Markov analysis: If I understood it correctly, SigmaA and SigmaV are fit to the entire block, and the Pprior derived from the entire block was used as starting value for this parameter? The authors conclude (l 256ff) that to 'maintain a consistency of causal inference, sensory uncertainty … is updated ' as well. However, the Markov model seems to focus only on the updating of the prior.

Processing of single unit data: In my view the paper would profit from showing actual single neuron PSTH's and how smoothing effected these. The methods (l. 857) mention a 400ms sliding window, but the periods of interest (e.g. target holding) are only minimally longer than this (500ms). This makes we worried that the analyzed data effectively blurs neural representations across epochs and is affected by movement artifacts. When computing the modality contributions to each response, what task epoch was analyzed to derive the tuning curves (l. 869ff)?

Overall there are many seemingly arbitrary choices in the methods. These include the thresholds to define neurons as 'causal inference', the number of trials required for neurons to be included in the population analysis (l. 964), the duration of smoothing kernels and temporal analysis windows (l. 848 ff), the binning of data for neuro-behavioral correlation (l. 893ff), in the generation of population patterns (l. 912ff), in the cluster-based test (not reported!). It would be good to see a justification for these choices or to learn whether the authors ensured that their main results do not depend on these precise choices.

4) The authors do not justify why they recorded in the transition between F4 (rostral ventral premotor) and F5 (caudal ventral premotor) with head visual/tactile optic flow signals and grasping signals respectively. The obvious target is F2 (dorsal premotor) since it has strong reaching signals and is highly connected with area 5 of the parietal lobe (Rizzolati, 1990; Mendoza and Merchant, 2014). The authors should provide a more detailed account on the areas studied and the criteria adopted to localize the recording sites. The specification that they were "determined by individual MRI atlas" does not warrant for areal identification, because on natural variability. On this regard, the Figure 3A' insets should be adjusted (for parietal recording sites in L and R hemispheres, the sulci orientation should be different, and for the premotor ones sulci should be reported).

5) For the discussion and comparison to previous work: The paradigm focuses on visuo-motor paradigm in which the sensory cues are both generated by the subject itself. In contrast, in many classical (e.g. audio-visual; or visual-vestibular)) paradigms both sensory cues are external in nature, and not linked to the subject's action. While in both types of paradigm sensory cues are integrated and can also induce perceptual recalibration, the visuo-motor paradigm still is conceptually distinct and this has implications for the interpretation of the results. The authors should discuss whether they believe that their findings generalize to other paradigms and whether the same or possibly distinct (e.g. parietal) brain regions should be investigated during such paradigms. Such a discussion seems important to place the present work in the context of the plethora of previous work. Indeed, the present study is completely lacking discussion of results with respect to current knowledge on the functional properties of premotor and parietal neurons subtending reaching. The literature on this topic is vast, but the following studies, as examples, could be relevant in this context:

1. Archambault et al. J Neurosci 2011 (comparison on premotor vs parietal, where premotor activity leads parietal one)

2. Caminiti et al. eNeuro, 2017 (overall picture of connectivity of fronto-parietal network with updated literature on functional properties of different areas)

3. Caminiti et al. J Neurosci 1991 (first paper on encoding of reaching in Premotor cortex)

4. Churchland MM, et al. Nature 2012

5. Cisek and Kalaska, Neuron 2005 (on premotor activity during reaching)

6. Gail and Andersen J Neurosci 2006 (on neural dynamics of sensorimotor transformations in parietal cortex)

7. Jerjian SJ, Sahani M, Kraskov A ELife 2020 (on movement representation in premotor cortex)

8. Jiang X et al. Cell Rep 2020 (onpremotor neural Activity during Observed and Executed Movements)

9. Mountcastle et al. J Neurophysiol 1975 (first pioneering study on the role of parietal cortex in visuomotor control)

10. Pezzulo et al. Progr Neurobiol 2022 (on the neural dynamics of premotor neurons during action execution and observation)

11. Santhanam et al. J Neurophysiol 2009

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Neural dynamics of causal inference in the macaque frontoparietal circuit" for further consideration by eLife. Your revised article has been evaluated by Tirin Moore (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors did a good job at answering all the reviewers' comments in the rebuttal, particularly the once regarding analysis and statistically details. However, the consensus of the reviewers is that no real changes in the structure of the paper were carried out to simplify the framing of the manuscript and make it more accessible to a larger audience. In addition, all the reviewers are concerned with the lack of rational regarding the recording locations in the main text.

Reviewer #1 (Recommendations for the authors):

Although the authors did a good job at answering all the reviewers' comments in the rebuttal, particularly the once regarding analysis and statistically details. However, many of the framing and conceptual comments were not really incorporated in the actual reviewed manuscript. Specifically:

1) Please start the paper by giving an intuitive example of the key problem addressed in the manuscript.

2) There is no change in the introduction and the Results sections regarding a simpler and more intuitive framing of the paper (Figure 2A is the same). Again, the reader needs to go quite further into the manuscript to understand the main question and how the authors implemented the experiment.

3) The paper should refer to the classical notions of sensory motor integration in the parieto-premotor circuit in the discussion.

4) The authors did not mention why they recorded ventral premotor and a mix of area 5 and 7a in the main text.

Reviewer #2 (Recommendations for the authors):

In my previous review I pointed out that, although the experimental paradigm was overall well designed and the data analysis technically sophisticated, the manuscript was flawed in several aspects, particularly in relation to the way the paper was written, and the data reported and discussed.

Despite the extensive point-to-point reply, the revision of the paper remains disappointing, as no substantial changes have been made to consider the criticisms. As a matter of fact, the new version of it is essentially identical to the original one in all its sections (Abstract, Introduction, Results and Discussion). Surprisingly enough, despite the authors' attempt to reply with accuracy to the different issue raised in the reviewing process, no significant improvement of the resubmitted manuscript was achieved, as in most instances all new information was not fully integrated in the revised version.

The authors were invited to place the present work in the context of the extensive literature on the neurophysiology of the parieto-frontal network, with special attention to its role on reaching movements. In fact, the original manuscript did not adequately discuss the results within the conceptual frame offered by the knowledge accumulated over the last forty years on the dynamic properties of premotor and parietal neurons subtending arm movements. This suggestion was completely ignored, as both Discussion and Introduction remained virtually identical across versions and the authors just added a few references, among those suggested by the reviewers, in a rather superficial fashion, without any emphasis about how they were related to findings and conclusions of the present study.

Concerning point (1) the authors' action was limited to the mere insertion of new titles at the beginning of some paragraphs. In their response, it is reported that the logic of the manuscript is outlined in the unchanged Fig. 2A, which was already present in the previous version. Therefore, no significant change has been made to take into account this aspect.

Furthermore, the selected units shown in Fig. 3D to offer an example of neural activity in form of raster plots and mean firing rates (not histograms, as stated) are not indicative of clear response modulation.

The mentioned Table 1 is neither reported in the main text, nor in Supplementary Material.

When asked to evaluate the temporal difference between premotor and parietal activity, the authors just replied that "The population decoding of Pcom (Figure 4E) indicated that the premotor cortex leads the parietal by about 300 ms", but this observation refers to what already shown in the earlier version of the manuscript. Even in this case, in fact, no change was made to the analyses and to the text to take this point into consideration.

Also concerning the spike sorting technique adopted, despite the reviewer's request, no further details have been provided, relative to what was already reported in the first version of the manuscript.

Despite the explicit request (see point 4) to provide more details on which premotor area was considered in this study, the authors persist in referring loosely to "premotor" cortex, not specifying exactly which among the different premotor areas is being studied, apart from the details provided graphically in the brain figurine. Given the different functional properties and characteristics in connectivity among different premotor regions, it is inappropriate and misleading from a neurophysiological perspective to simply refer to premotor cortex. Provided that the region of recording mainly encompasses premotor area F2vr (medial to the spur of the arcuate sulcus), a small and medial part of premotor area F5, and part of F4, as evident from Fig. 3A, the main text did not report the rationale underlying the selection of the F2vr, F4/F5 for the present study. In addition, according to the new details provided in the current version of Fig. 3A on recording sites, some of the penetrations (corresponding to about 40-45 collected units) belong to prefrontal area 8 (FEF). These cells should be removed from the premotor database.

Furthermore, the lack of precise identification of the area/s of neural recording concerns parietal cortex as well. In fact, from a careful inspection of Fig. 3A, most of the penetrations in Monkey N belong to area 7 (which is part of the Inferior Parietal Lobule), and not to area 5 (which extends over the Superior Parietal Lobule instead), as stated throughout the manuscript. Finally, in all four insets of Fig. 3a it is not specified what the dashed grey lines refer to. This uncertainty would require a major revision of the parietal database.

Beyond the graphical (subjective) representation, no other information is provided about the criteria adopted to identify the recording areas and sites. First, as pointed out by the reviewers, the specification that they were "determined by individual MRI atlas" does not warrant for any areal identification; second is not even vaguely informative on how frontal and parietal areas were identified. The sentence that "The location of the recording chamber on each animal was determined by an individual MRI atlas" remained unchanged in the revised version of paper, without any further details, not even providing the reference on which Atlas has been used.

Finally, another reason of concern highlighted in the revision process refers to the lack of eye movements data, given that eye position and saccade direction exerts a well-known, although quantitatively different, influence on premotor and parietal neural activity. The authors did not refer to this critical aspect at all, nor did they discuss how eye-related signals might have influenced and eventually contaminated the reported findings.

Reviewer #3 (Recommendations for the authors):

The authors have addressed most reviewer comments to a sufficient degree. The work is still very dense given the large number of analyses implemented, but I have no specific suggestions for how to change this.

One remaining shortcoming is that I did not see a specific rationale for the choice of the precise recording locations in the manuscript. In reply to my previous comment, the authors have provided some rather generic text in the rebuttal, but ideally, a clear rationale for the choices should be in the manuscript.
