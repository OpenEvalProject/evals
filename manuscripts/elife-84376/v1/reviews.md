# Peer review - Round 1

Editors:
- Jonas Obleser, https://ror.org/00t3r8h32 University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84376.sa0](https://doi.org/10.7554/eLife.84376.sa0)

This article brings to bear an important set of behavioral methods and neural data reporting that activity in numerous cortical regions robustly covaries with the complexity of tone sequences encoded in memory. The study provides convincing evidence that humans store these sequences based on representations related to the so-called language of thought.


---

# Peer review - Round 1

Editors:
- Jonas Obleser, https://ror.org/00t3r8h32 University of Lübeck Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84376.sa1](https://doi.org/10.7554/eLife.84376.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Compression of binary sound sequences in human working memory" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Barbara Shinn-Cunningham as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

A revision should thoroughly address the many points raised by both reviewers, but let us editorially highlight especially the following requests/concerns:

– As outlined by Reviewer 1, a core issue of the manuscript in its present form is the missing formal description of the LoT model and alternatives, inconsistencies in the model comparisons, and no clear argumentation that would allow the reader to understand the selection of the alternative model. Similar to a recent paper by similar authors (Planton et al., 2021 PLOS Computational Biology), an explicit model comparison analysis would allow a much stronger conclusion. Also, these analyses would provide a more extensive evidence base for the favored LoT model.

– We deem it desirable, if not required, to make the analysis pipeline and the raw data publicly available to investigate the pipeline in detail and reproduce the results (provided hyperlinks are not functional).

– As outlined by Reviewer 2, it is unclear whether the authors have successfully "characterize[d] the mental representation that humans utilize to encode binary sequences of sounds in working memory and detect occasional deviants" as they set out to do. While it is possible that the regions found "constitute the minimal network needed to track sequences" we find the evidence insufficient to assert this.

Further analyses might be needed to elucidate the temporal evolution of the neural signals over its repeated presentation over habituation and test, as well as the experiment overall. Further research might be needed to study persistent activity while minimizing influences from perceptual processing and could even distinguish the representation of individual sequences from each other using pattern analysis.

– Please reconsider the terminology used to describe the proposed model, as argued convincingly and exemplified by Reviewer 2.

Reviewer #1 (Recommendations for the authors):

Weaknesses:

Inconsistencies in the analysis across datasets, for example, a direct comparison of the alternative model with the LoT on the behavioral data (but no figure for the alternative model effect), no analysis including the alternative model for the fMRI data, and providing the linear regression analysis for the MEG data that includes the predictor related to the alternative model only as a secondary analysis is unfortunate. It weakens the main conclusion of the manuscript. The manuscript could establish more robust conclusions when, for example, the or multiple alternative models would be treated equally (e.g., figures for the behavioral data). For the fMRI analysis, one could compare the models with an overlap analysis (similar to in Figure 4) and compare effect sizes from different regions. For the MEG data, one could focus on the analysis that considers both models, as one could expect that the model has a higher model fit and provide extensive descriptions for both effects.

Also, a critical case for the model is the 0-correlation of behavior and LoT for the Alternate condition. The authors choose not to include a correlation between behavior in the bracket task and the alternative account. Moreover, no critical discussion of this inconsistency is included.

Moreover, recent developments indicate selective implementation of representations depending on the complexity of the task (e.g., see Boominathan, L., and Pitkow, X. (2022). Phase transitions in when feedback is useful. Advances in Neural Information Processing Systems, 35, 10849-10861.) the investigation of an interaction of the complexity parameter and the transitional probabilities would be highly intriguing.

Further points:

It is highly recommended to make the analysis pipeline and the raw data publicly available to investigate the pipeline in detail and reproduce the results (provided hyperlinks are not functional).

Figure 1.: For a clear understanding for the reader, one could provide the tree structure for the experimental conditions reflecting the LoT complexity

Figure 2 Please present the p-value and the r in bold letters. The current presentation suggests higher importance for the statistics than the effect size estimate.

Results

195-199. As indicated before, the low correlation between bracketing behavior and the LoT model simulations is low. The following section is provided but unclear from reading the previous sections. Please provide more context here and elaborate in the discussion.

"For the latter, a minor departure from the proposed encoding was found, as the shortest LoT representation (i.e. [+0]^16) can be paraphrased as "16 alternations", while the participants' parses corresponded to "8 AB pairs". The latter encoding, however, only has a marginally larger complexity, so this deviation should not affect subsequent results. "

211-219: Be precise on the formulation of the linear mixed effect model. As the random effect structure can vary drastically, it is essential to present the complete form of the model, especially when reanalyzing it with and without the subject random effect. Also, no indication of the inclusion of random slopes or other random effects like stimuli is included.

220-230: Statistical learning as an alternative explanation. The critical test needs to be included. Has the stats learning or the LoT complexity predictor the higher model fit? Also, why not use a metric that penalizes for the number of predictors in the model (e.g., Akaike Information Criterion). Also, please provide the correlation of the two predictors from the models. A similarity estimation is essential to interpret the findings.

341-345: Why use a quadratic trend, and what is the benefit of making the statistical model more complex here? Please elaborate

364" "for loops" postulated in our language"; Please elaborate.

fMRI part:

Comparison analysis based on the alternative model (based on transitional probabilities) needs to be included. This analysis would allow us to investigate which regions contribute to the added behavioral explainability found in the behavioral analysis.

MEG part:

Unclear why the quadratic trend used for the fMRI analysis is not considered here. Please provide an argumentation.

Alternative model, based on transitional probabilities. Figure S4 provides the complexity effects based on a regression model, including the transitional probabilities measure. For clarity, please provide the corrected version in Figure 6 alongside the effect of the alternative model. Again model comparison or if both show considerable effects, one could investigate the interaction of complexity and transitional probabilities. Similarly, use both parameters or the interaction for the classifier data presented in Figure 7.

L 534: Please provide an argument here, why the leave-one-out was used here. Alternatively, one could use a 5-fold cross-validation that is more efficient to estimate and less problematic when it comes to overfitting. I expect this analysis was implemented because the analysis presented in Figure 7 is based only on the unseen dataset.

L 628 It is not clear what statistical test established cross decoding, as the cluster test provided cannot differentiate between time windows (see Sassenhagen, J., and Draschkow, D. (2019). Cluster‐based permutation tests of MEG/EEG data do not establish significance of effect latency or location. Psychophysiology, 56(6), e13335.).

L 763 "fMRI, MEG and behavioral responses to deviants vary linearly with complexity, while model-related fMRI activations vary as an inverted U function of complexity". This result was not tested for, e.g., the MEG data. As described, no non-linear relationships have been investigated in the study.

Subjects:

Please justify the number of participants participating in the experiment using a Power analysis. If no a-priory analysis was implemented, provide a post hoc analysis. This is especially important because it was previously shown that low power could result in false positive inflation for fMRI data (e.g., Yarkoni, T. (2009). Big correlations in little studies: Inflated fMRI correlations reflect low statistical power-Commentary on Vul et al.(2009). Perspectives on psychological science, 4(3), 294-298.)

L 924-929: Please provide the threshold r used for the automatic detection. Also, explain why the number of components was fixed to 1 for cardio and 2 for eye-movement artifacts.

Reviewer #2 (Recommendations for the authors):

Before we share our evaluations and concerns, we would like to emphasize that our primary expertise is within working memory research using fMRI and behavioral methods. We hope that our comments will prove to be helpful to the authors.

Is this 'in human working memory'

It is almost impossible to design an experiment that fully precludes some use of working memory. This means that to argue that a process is selectively contained within working memory requires the experimenter to rule out influences of perceptual and long-term memory processes.

Behaviorally, this would mean designing a task where information has to be retained over time, and that discourages the use of long-term memory. Instead, the complexity of the stimuli used (which are likely to exceed working memory capacity) and the intense ongoing stimulation (operating in part as a distractor to working memory processing) seems to encourage the use of long-term memory. Consistently, subjects need to be 'habituated' to the to-be-memorized sequence about ten times, making an influence of early forms of long-term memory very likely.

More importantly, when a neural signal is to be attributed to working memory processing this typically requires some claim of delay period activity (i.e. some form of persistent activity). Here, there is little evidence of differential delay-period activity that is different for different task conditions. Instead, MEG data is most reliably affected by sequence complexity between 100 and 200 ms after the onset of an individual stimulus and complexity specific responses only extend beyond this when a violation of the sequence is detected. The fMRI data does little to alleviate this concern and evaluating this question is made harder by the fact that we could not directly link the time-resolved fMRI data time courses (Figure 3B) with the experimental timeline presented in the methods section.

Despite this, the authors seem to argue that the signals found are a kind of load-like signal that is indicative of the storage of the compressed sequences. For this, it is worth noting that whether load-signals are indicative of an underlying representation of memorized content is questionable (Emrich et al., 2013) and that we know of no instance where the load signals reverse like it does here in deviant trials. The authors, however, argue that the successful quadratic fits of the neural complexity signals are akin to ceiling-in-load effects found in the working memory literature (Vogel and Machizawa, 2004) where neural load-signals reach a ceiling for loads that exceed working memory capacity. This ceiling-in-load effect, however, relies on this tight link between neural and behavioral data evidence which is not presented. Furthermore, the 'quadratic' effect reported here seems to be expressed as data for both the most and least complex sequences diverging from the linear trend. This simply might indicate that the precise complexity of extremely simple and highly complex sequences is less precisely captured by the compression model.

In the introduction the authors, however, also highlight a potentially more specific interpretation of their signals. "[…] the internal model of the sequence, as described by the postulated LoT, would be encoded by prefrontal regions of the brain, and would send anticipation signals to auditory areas, where they would be subtracted from incoming signals. As a consequence, we predict a reciprocal effect of LoT on the brain signals during habituation and during deviancy. In the habituation part of the experiment, lower amplitude response signals should be observed for sequences of low complexity – and conversely, during low complexity sequences, we expect top-down predictions to be stronger and therefore deviants to elicit larger responses, than for complex, hard to predict sequences." To us, this prediction-error-like interpretation seems to be more in line with the data presented. We believe that the time-courses presented in MEG closely match both early and late mismatch signals (mismatch activity and P300). The fMRI data is to the extent we can judge consistent with this interpretation, as is the apparent decline in complexity modulation from habituation to deviant free test trials and the inversion when deviance is detected. The authors argue, in this regard, that the complexity effect is not solely explained by a 'surprise' model. But at least some of the variance in question is explained by surprise. This leaves us to ask whether a better surprise or mismatch model could be found than the one used to capture the results fully (the current implementation of which should be fully explained in the methods). In the end, the more complex a sequence, the less predictable it is and the more surprising its individual elements are when initially presented.

Thus, it is unclear whether the authors have successfully "characterize[d] the mental representation that humans utilize to encode binary sequences of sounds in working memory and detect occasional deviants" as they set out to do. While it is possible that the regions found "constitute the minimal network needed to track sequences" we find the evidence insufficient to assert this.

Further analyses might help elucidate the temporal evolution of the neural signals over its repeated presentation over habituation and test, as well as the experiment overall. Further research might be needed to study persistent activity while minimizing influences from perceptual processing and could even distinguish the representation of individual sequences from each other using pattern analysis. Sequence complexity might be seen as a confound in such research as it leads to prediction-error-like or load-like response that can be independent of the representation of the individual sequence.

The essence of our concerns [has been covered above]. In short, we are convinced that the evidence speaks to a prediction-error-like signal that covaries with the complexity, and not a signal directly related to working memory retention. Our first major recommendation is therefore to put substantially more emphasis on this alternative interpretation of the results.

Arguing for a working memory-specific signal would – in our view – require directly establishing the presence of some form of persistent activity that is linked to the current results. Because of the rapid presentation of the sequences and the absence of a delay, we see no avenue to pursue this in the current fMRI data. Even for the EEG data, one would have to look at the brief time periods between individual habituations and see whether the recorded data carries information about the presented sequences. Even in this case, one would need to find a way to carefully distinguish these results from the prediction-area-like signals found so far. It is possible the authors intended to establish a connection to working memory in a way that we did not comprehend. In this case, this point requires clarification.

It would be of interest to further understand the role of long-term memory in this task. For this, it would be helpful to investigate how the complexity effect changes over the course of the experiment. Comparing the first and second (inverted) presentation of the sequence could establish whether the complexity effect is mediated by long-term memory.

Finally, we would suggest reconsidering the terminology used to describe the proposed model. On first read, we got distracted by questioning what the authors meant by 'language of thought' and how it related to the experimentation presented (e.g. "The present results therefore support the hypothesis that the human brain hosts multiple internal languages"). The terminology currently used implies a direct link to the subject's subjective experience of thought and while we all want to know how the words (and 'words') we 'think' come to be, we do not see how the data presented speak to that question, directly.
