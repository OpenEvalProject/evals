# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55092.sa1](https://doi.org/10.7554/eLife.55092.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study relies on both invasive and non-invasive EEG recordings in humans who were either awake, anesthetized or sleeping, and shows that a particular marker of neural activity – the slope of the EEG power spectrum – can be used to distinguish between different states of arousal. Importantly, this measure can be reliably estimated from scalp EEG recordings, and accurately separates REM sleep from wakefulness, which to date had been challenging using EEG. Furthermore, the authors show that anesthesia reflects a brain-wide state, while sleep patterns are observed in specific networks.

Decision letter after peer review:

Thank you for submitting your article "An Electrophysiological Marker of Arousal Level in Humans" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Giovanni Piantoni (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In recognition of the fact that revisions may take longer than the two months we typically allow, until the research enterprise restarts in full, we will give authors as much time as they need to submit revised manuscripts.

Summary:

Lendner and colleagues assess 1/f EEG activity as a proxy of arousal by comparing both invasive and non-invasive recordings of awake, anesthetized and sleeping humans. The authors calculated the slope in the log-log power spectral density during periods of wakefulness, N3 and REM sleep and propofol anesthesia. They consistently found across four studies (both intracranial and scalp EEG) that the slope is shallower for wakefulness as compared to the other states of reduced arousal. A series of control analyses (LDA, changes in center frequency and width of the frequency range, link to slow waves) confirmed the main finding. The findings are exciting and well tested over multiple studies and recording setups. Particularly intriguing is the similarity between propofol and sleep.

Although the study in general represents an important contribution to the field of human electrophysiological research, we are not entirely convinced by the used methods, inferential statistics, and by the way the findings are integrated into the existing literature. The analysis of multiple data sets in order to draw inferences on various levels is compelling and impressive but warrants a more consistent methodological approach and the acknowledgement of earlier findings.

Essential revisions:

1) Overall, the manuscript is lacking connection with existing literature, leading to unwarranted novelty claims and rather unspecific hypotheses. Authors should integrate the existing literature more thoroughly.

This is especially of importance for the Introduction and Discussion sections. For example, the authors cite Colombo et al., 2019, in the Introduction but do not acknowledge that this study performed a comparison of EEG spectral exponents between the awake state and anesthesia under different drugs, including Propofol, and found a steepening of the spectrum under Propofol anesthesia compared to awake rest. Similarly, the authors cite Miskovic et al., 2019 without noting that the cited study compared PSD exponents between different sleep stages and found results comparable to those of the current manuscript.

It is essential to put the results of the current study into context and note that they replicate earlier findings and are not the first of their kind in data from human subjects. The appeal of novelty claims in the Introduction which states that only non-human animal results exist for the central question of the manuscript, should be omitted. Instead, we suggest to formulate more precise hypotheses regarding the direction of effects (steepening vs. flattening of spectra) and to touch upon E/I balance and neurotransmitters already in the Introduction.

2) We had several concerns regarding the inferential statistics used. Permutation-based or non-parametric tests are more appropriate for the majority of performed tests and should be implemented.

More specifically: Inferential statistics should be adapted to meet the distributional properties of the data they are performed on. The comparison of very small samples (e.g. n = 9) using t-tests should be replaced by non-parametric or permutation-based approaches. Similarly, comparing goodness of fit statistics using t-tests should be omitted (subsection “The relationship of slow waves and the spectral slope”) and replaced by proper model comparisons.

Additionally, performance correct percentages of the used LDA should undergo an appropriate transformation before being tested against each other (e.g. logit).

On a more general note, we suggest to replace the LDA approach with a multivariate model predicting arousal states based on the predictors the authors aim to compare. This way their predictive power can be compared directly (if scaled in the same way, e.g. z-scored) and their shared variance in the dependent variable can be accounted for. Furthermore, the discussion of prediction accuracies should include a reference to the "ground truth" that is predicted here, the ratings of a trained specialist which are 80% reliable.

3) One of the major claims of the paper is that the effect of interest is consistent across techniques (EEG, iEEG) and brain states (propofol, sleep). To support this claim, the authors would need to be consistent in their analysis pipelines of the different datasets. More specifically:

– Why were different length segments (and taper numbers) used for sleep vs anesthesia? Would be better for direct comparison to keep these parameters the same.

– The iEEG studies and the scalp EEG studies use a very different reference. Bipolar for iEEG and common average for the scalp EEG studies (the reference is not clearly specified for study 3 though, please clarify). One would expect that the choice of reference would have a large impact on the slope, but this does not seem the case. For example, local dynamics captured by bipolar referencing are in general very different from global effects such as those observed in scalp EEG. In fact, the Laplacian reference does not change the results. Could the authors discuss in more detail the role of referencing in their interpretation of the neurophysiological basis of 1/f dynamics?

4) Furthermore, we had some concerns regarding anatomical claims.

The fact that sleep stage-slope correlation seems to be dominated by medial PFC/temporal sites is interesting, though might be biased by the iEEG montage, as those are also the regions with the most electrodes due to epilepsy monitoring. There should be a statistical analysis that shows that those regions have a significantly higher proportion of "differentiating" electrodes than other brain regions. In addition to a sound statistical analysis, the authors should provide a table with the number of total electrodes and the number of electrodes showing a significant change in slope, per brain region. As it is, it's hard to define the regions of interest based on the brain plots shown.

Additionally, it would have been much more powerful if the anatomical claims could be corroborated by the EEG recordings. Not sure source localization is possible on the EEG data given low electrode numbers, but that would really have strengthened the story. In current form it remains a little unclear what the main sources of all these effects are.

5) The fitting of 1/f spectral exponents should be improved and frequency ranges should be motivated more clearly.

Although it is correct that Gao et al., 2017, used a frequency range of 30-50 Hz for their 1/f PSD fit, this choice was motivated by the linear decrease of power in LFP recordings within that frequency range. However, oscillatory parts of the spectrum, whether of neural or non-neural origin (line noise), can aptly be fitted and excluded from a 1/f fit using the FOOOF package (https://fooof-tools.github.io/fooof/). The use of this or another software package (e.g. BOSC or eBOSC: https://github.com/jkosciessa/eBOSC) would allow the authors to directly asses the change of PSD exponents across different levels of arousal across wider frequency ranges without having to alter time-series first using IRASA. In fact, Colombo and colleagues show a steepening of the PSD between 1 and 40 Hz from awake rest compared to Propofol anesthesia, a result the authors could try to replicate and discuss using the proposed analyses techniques. Furthermore, goodness of fit statistics for the performed linear fits are missing and should be added for any kind of fitting procedure the authors decide to apply.

6) Discussion could be more in depth in terms of:

– connection with existing literature;

– underlying mechanisms/generation of the recorded signals;

– interpretation of the findings and implications for our understanding of sleep vs wake processes;

– actual discussion of practical use, i.e., how reliable is slope as a measure to distinguish these states on the single subject level.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "An Electrophysiological Marker of Arousal Level in Humans" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and Saskia Haegens (Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We appreciate the very thorough revisions, especially methods wise, and believe they have strengthened the paper considerably. After discussion with one of the original reviewers, we have one remaining point we would still like to see clarified, but other than that all our previous concerns have been adequately dealt with.

The issue we are still unclear on pertains to this claim:

"Critically, the accuracy of this classification is comparable to trained personnel, since the inter-rater reliability between sleep state scoring experts is typically about 80%".

However, if the ground truth here consists of the sleep staging done by trained experts, for whom we know the inter-rater reliability is typically about 80%, then a 100% accuracy of the classifier would be a 100% match with these expert raters (i.e., not necessarily a 100% accurate classification of sleep stage). In other words, the performance of the classifier is bound by the accuracy of the ground truth. Since we do not know the "true" sleep stage, we can only conclude that the classifier accurately predicts the experts' ratings 80% of the time here. Please add some language to make this explicit in the discussion of these results.
