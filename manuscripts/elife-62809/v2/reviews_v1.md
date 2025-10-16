# Peer review - Round 1

Editors:
- Peter Kok, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62809.sa1](https://doi.org/10.7554/eLife.62809.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Our expectations strongly influence how we perceive painful stimuli, as demonstrated by the well-known placebo effect. This paper elegantly elucidates the neural dynamics involved: expectations modulate low-frequency (alpha and beta) pre-stimulus oscillations, whereas expectation mismatches modulate post-stimulus high-frequency (gamma) power. This work demonstrates important overlap with expectation mechanisms in other perceptual domains (vision, audition), but also striking differences, such as that high-frequency power is decreased rather than increased by pain prediction errors.

Decision letter after peer review:

Thank you for submitting your article "The temporal characteristics of expectations and prediction errors in pain" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Enrico Schulz (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The study by Strube and colleagues investigates neural prediction error processing in the context of painful stimuli. The results suggest that alpha-to-beta oscillations were associated with pain expectation, whereas gamma band oscillations (GBO) were associated with prediction error (PE). The concept and the findings of the study are interesting. However, so far, it is not clear whether the findings unequivocally support the conclusions and additional analyses are needed.

Essential revisions:

1) There is a vast amount of literature on pain-related theta, alpha, and gamma activity that the authors should mention in the Introduction in order to prepare the reader for the results. Similarly, the Discussion section is very much focused on imaging effects despite a vast amount of literature on pain-related oscillations. Interestingly, the only paper the authors are citing for gamma activity is relying on an artefact (Zhang et al., 2012). The authors should discuss their findings in light of neurophysiological studies.

2) In contrast to Fazeli and Büchel, 2018, the behavioral data do not show PE effects. Does it make sense to analyze PE effects in the imaging data if no behavioural PE effects are found?

3) The study deals with expectations and PE in pain. To this end, a cueing paradigm has been performed with three thermal stimulus intensities. However, the lowest stimulus intensity has not been perceived as painful but as warm. Thus, some PE refer to errors regarding pain intensity and other PE to errors regarding pain vs non-painful warm. Moreover, the low pain cue is in fact a no pain cue. Does the study therefore really deal with PE in pain? Wouldn't it be necessary to restrict the analysis to painful stimuli? Or should the study be re-framed as studying PE in thermal perception?

Related to this, it is not clear whether it was a good decision to keep the stimulation temperature at the same level for all participants. As this is a within-subject design, the authors want to maximise the perceptual differences (e.g. no, low, high pain).

4) The current study conceptualizes PE as absolute unsigned PE, i.e., similar PE occur when the sensory evidence is less or more intense than expected. However, other PE concepts have assumed absolute signed PE, i.e., opposite neural effects occur when the sensory evidence is less or more intense than expected. Moreover, a third concept assumes negative PE, i.e., PE occur only when the sensory evidence is more intense than expected. The authors should clearly explain and motivate their PE definition. Moreover, the authors might perform similar analyses for other PE definitions.

5) The relationship between GBO and PE is negative, i.e., the greater the PE the lower the GBO amplitude. This pattern is at variance with all previous findings on GBO and PE and therefore contradicts rather than supports PE coding by GBO.

6) The relationship between alpha-to-beta-oscillations and expectations is not fully clear. The text and Figure 6 indicate a positive relationship whereas later it describes a decrease of alpha-to-beta band power associated with the manipulation of expectations, i.e., a negative relationship.

7) The expectation effects have been analyzed cue-locked. Thus, their timing with respect to thermal stimulus application is unclear, i.e. it is unknown whether expectations effects occur before or after stimulus application. The authors should find a way to clarify this.

8) Is there a reason why the authors focused on the pain part only? The visual part could serve as a control experiment, or the pain part as control for the visual experiment. It would be desirable to see whether there are similar effects of prediction error in either modalities. Alternatively, the authors might explain the motivation of the visual control condition and why it is not relevant for the present study.

9) There are problems with the analysis of gamma oscillations. There are additional and essential steps required in order to prevent that the findings are based on muscle artefacts (such as in Zhang et al., 2012). The authors may want to take the following steps:

a) Inspection of time-frequency decomposed ICA data at single trial level

b) Plot the trials after z-transforming based on the mean and the standard deviation of the entire component or potentially across all components. The z-transformation should be done separately for each frequency.

c) Artefact components or trials are easily visible and should be compared with the raw ICA time course as the muscle spikes can be easily detected there, too. However, the TFR plots are more sensitive. The artefact detection procedure may require a finer sliding window than the 50 ms which the authors used.

d) Single and separate muscle spikes are shown as columns, similar to the figure presented in Zhang (2012). Overlapping muscle spikes appear like "clouds" and can easily be misinterpreted as cortical activity. A sensitive single trial inspection on ICA transformed data is helpful.

e) As the authors have a low number of trials for some combinations (~1%), they may want to focus more on component rejection than on trial rejection. The authors may be required to remove up to 30 components from further analyses. The Vision Analyzer software from Brain Products has some features the authors may find useful, which is a Matlab interface for data export to FieldTrip as well as an excellent overlay function of cleaned vs uncleaned data after component removal.

10) Usually, less than half of the sample exhibits pain-related gamma activity. Could the authors provide a histogramme plot for the baseline-corrected gamma amplitude across the sample?

11) Is there a reason for not including a source analysis for pain intensity encoding? The authors provided a source analysis for all other aspects and should do the same for pain encoding for all frequencies.

12) The analysis should be explained in sufficient detail for replication. In particular, it should be explained for which time-frequency-electrode spaces cluster permutation tests were performed. Moreover, it should be detailed how prediction error effects were calculated (interactions between stimulus intensity and expectations in ANOVA?).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "The temporal characteristics of expectations and prediction errors in pain" for consideration by eLife. Your revised article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Enrico Schulz (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

The reviewers felt that the revisions have improved the manuscript, and the paper has clear potential. However, substantial revisions are still required to make this paper suitable for publication. They point out that several central issues have not been fully addressed for far.

Essential Revisions:

1) One issue that not been fully address are the concerns about the pain rating scale, where the "1" is clearly outside the pain range, being rated as neutral. Moreover, the low pain cue is in fact a no pain cue. What matters is not located in the periphery and the use of C-fibres, but the subjective pain experience of the participants. There's plenty of literature showing that participants exhibit differences in pain sensitivity. The QUEST algorithm to individually adapt pain intensities from Taesler and Rose, 2017, would have been more suitable to define different levels of pain intensity. Within-subject analyses should (probably) always use individually adapted pain intensities. This issue that the stimuli were ranging from non-painful heat to moderate pain needs to be explicitly addressed throughout the manuscript (including the title) and added to the paragraph on limitations. It is essential that the following questions are addressed convincingly and that these considerations are included to the Discussion section. Does the study really deal with PE in pain? Wouldn't it be necessary to restrict the analysis to painful stimuli? Or should the study be re-framed as studying PE in thermal perception?

2) The answer to the central question about the absence of behavioural effects is not fully convincing. The main argument is simply that it does make sense to investigate PE imaging effects without any behavioural effects. However, a more substantiated consideration of the significance of PE imaging effects in the absence of behavioural effects would be appropriate. These considerations should also be included in the Discussion section.

3) The relationship between GBO and PE is negative, i.e., the greater the PE the lower the GBO amplitude. This pattern is at variance with all previous findings on GBO and PE and therefore contradicts rather than supports PE coding by GBO. The authors reply to this point in the previous round was not sufficiently clear. Clear arguments in plain terms are needed. Moreover, the unusual inverse coding of PEs by gamma oscillations should be added to the Abstract.

4) The cluster-based permutation test is central to control for false positives. It has now been clarified that clustering has been performed across electrodes. However, it is best practice to cluster across electrodes, time and space. It is therefore essential to adjust the clustering procedure.

5) It is unclear whether it is appropriate to apply a baseline correction in reference to the entire trial segment. Could the authors provide a reference in order to justify their approach? Otherwise, they might consider applying a conventional baseline correction.

6) The reviewers suggest the authors consider dropping the source localisation. Most of the images do not seem to make much sense. The only exception that resembles a meaningful solution for the expectation analysis appears to be exaggerated. The authors rightfully mention in the manuscript that the anterior insula is involved in cognitive processing, such as expectation. However, the activity cluster points to the posterior insula and has its major part extended to the lingual gyrus. It does not seem appropriate to rely on the interpretation of one (out of many) remotely interpretable source analysis. It suggests selectively interpreting results that fit the hypotheses.

7) For the interpretation of the EXP and PE effect the authors should be sure that there are no differences in subjective pain intensity between the 3 conditions of EXP and the 2 conditions of PE. The question is whether the prediction error is a real error or whether the pain stimuli were "naturally" experienced as more or less painful than intended. Previous studies have shown that the trial-by-trial experience of pain can substantially jitter within subjects, even without any kind of intervention.

8) It is not clear why there is a significant cluster for expectation in the alpha/beta range between 1 – 2 s after cue onset. From visual inspection and "plausibility check" this cluster does not particularly stick out from the scattered apparently insignificant clusters across the entire time-frequency range. The F-values at 2.5s/70Hz even appear to be higher than the significant cluster.

Reviewer #1:

The EEG study by Strube and colleagues used a predictive model paradigm to investigate the temporal dynamics of expectation and prediction errors on the processing of heat and pain. Their elaborate and balanced paradigm allowed to differentiate the neuronal oscillations contributing to the encoding of (a) stimulus intensity, (b) expectation, and (c) prediction errors. As a major weakness of the study, the lowest stimulus intensity was not perceived as painful, which does not justify restricting the interpretation to the pain domain but must include heat processing. The reason for this disadvantage is that the stimulus intensity has not been adapted to the participants. All study participants received the same stimulus intensities. This adaptation is mandatory due to the large differences in pain sensitivity across individuals and the focus on within-subject statistical analyses.

The study corroborates previous work on the influence of cognitive factors on the processing of pain. Furthermore, the study also takes advantage of the higher temporal resolution of EEG, which enabled the authors to analyse the data in reference to the onset of the expectation phase, as well as to analyse the data in reference to the subsequent (jittered) onset of the pain perception phase. As a result, the authors associated pain encoding with gamma activity and high-alpha/low-beta activity for predictor error encoding. The authors utilised an established design, which they have already published using fMRI.

The study is of utmost relevance for a broad readership of scientists in the fields of pain and cognition. The authors applied a timely randomisation algorithm at cluster-level in order to correct for multiple testing. They also applied an EEG source localisation of their effects with barely interpretable results. The many presented source maps are a good example for the challenges of EEG source localisation, which probably often do not exhibit results we can rely on. This can cause severe publication bias, where "good" results are published and "bad" results are dropped. The source localisation could have been improved by the use of individual and accurate electrode positions (instead of standard electrode positions), with the use of individual 3D brain images to account for individual anatomical differences, as well as by the co-registration of EEG electrode positions to the individual head shape.

Reviewer #2:

The revisions have significantly improved the manuscript. Many details have been clarified. However, some important issues should be addressed in more detail.

In contrast to Fazeli and Büchel, 2018, the behavioral data do not show PE effects. Does it make sense to analyze PE effects in the imaging data if no behavioral PE effects are found?

The study deals with expectations and PE in pain. To this end, a cueing paradigm has been performed with three thermal stimulus intensities. However, the lowest stimulus intensity has not been perceived as painful but as warm. Thus, some PE refer to errors regarding pain intensity and other PE to errors regarding pain vs non-painful warm. Moreover, the low pain cue is in fact a no pain cue. Does the study therefore really deal with PE in pain? Wouldn't it be necessary to restrict the analysis to painful stimuli? Or should the study be re-framed as studying PE in thermal perception?

The relationship between GBO and PE is negative, i.e., the greater the PE the lower the GBO amplitude. This pattern is at variance with all previous findings on GBO and PE and therefore contradicts rather than supports PE coding by GBO.

The analysis should be explained in sufficient detail for replication. In particular, it should be explained for which time-frequency-electrode spaces cluster permutation tests were performed. Moreover, it should be detailed how prediction error effects were calculated (interactions between stimulus intensity and expectations in ANOVA?).
