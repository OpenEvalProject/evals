# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- Malte Woestmann, University of Lübeck Germany
- Nicholas Edward Myers, University of Oxford United Kingdom

## Review text

DOI: [10.7554/eLife.49562.sa1](https://doi.org/10.7554/eLife.49562.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study addresses a timely and relevant question, namely, what is the functional role of alpha- and beta-band oscillations? Here, a novel approach is used to understand whether these oscillations modulate the processing of sensory information in the brain, as suggested (but not empirically tested) by a number of previous studies on the relationship between alpha/beta activity and neural and perceptual excitability. The authors use combined EEG-fMRI to independently estimate two neural measures: the alpha/beta power decrease and fMRI representational similarity analysis as a proxy of stimulus-specific information. They find that alpha/beta power decreases correlate with stimulus-specific information, both in the visual and auditory domains. The authors conclude that alpha/beta power decreases are a neural signature of the fidelity of stimulus-specific information.

Decision letter after peer review:

Thank you for submitting your article "Alpha/beta power decreases track the fidelity of stimulus-specific information" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Saskia Haegens as the Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Malte Woestmann (Reviewer #1); Nicholas Edward Myers (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors analyzed data of a final sample of N=21 human participants in a combined fMRI-EEG study using an associative memory task. Stimulus-specific information, quantified via fMRI representational similarity analysis (RSA), was significantly correlated with concurrently recorded alpha/beta band power decreases. This effect was found for stimulus perception and episodic memory retrieval. The authors conclude that alpha/beta power decreases are a neural signature of the fidelity of stimulus-specific information.

The study addresses an interesting and timely research question and is well designed. We have a number of concerns that should be addressed before the manuscript can be considered for publication in eLife.

Essential revisions:

1) The authors should relate their results to the rich and recent literature regarding the functional role of alpha (and beta) power decreases for information processing. While some studies in the past might suggest that alpha power decreases reflect enhanced sensitivity (Hanslmayr et al., 2007; van Dijk et al., 2008; Busch et al., 2009), more recent studies have used sophisticated psychophysical modeling and neat experimental designs to demonstrate that alpha power decreases (prior to but also following stimulus onset) rather reflect enhanced neural baseline excitability, which affects subjective perception (Lange et al., 2013), confidence ratings (Samaha et al., 2017; Wostmann et al., 2019), response bias (Limbach et al., 2016; Benwell et al., 2017; Iemi et al., 2017), awareness (Benwell et al., 2017), and self-rated levels of attention (Whitmarsh et al., 2017) but not task accuracy.

- The authors interpret alpha/beta power decreases as a signature of the "fidelity of stimulus-specific information", which speaks to sensitivity rather than baseline excitability as the underlying neural mechanism. Unfortunately, results of the present study are difficult to integrate with the existing literature (listed above), since previous studies established relations between alpha/beta power decreases and different behavioral metrics whereas the present study relates alpha/beta power decreases mainly to results of the fMRI representational similarity analysis.

- Related to this point, the same correlation could be the result of a bimodal distribution of power (i.e. alpha/beta is either in a high or low power state, as suggested, e.g., by Freyer et al., 2009). If this distinction is important to the authors, it might be worth elaborating on this point in the Discussion.

- Although the authors made an attempt to relate alpha/beta power decreases to confidence ratings, a multivariate analysis (multiple regression or mediation analysis on single-trial data) would help to interpret the present results and integrate these with the existing literature. In order to investigate the exact relationship between RSA, alpha/beta power decreases and task performance in terms of confidence and accuracy, all of these variables would need to be combined in a statistical analysis. Results of such an analysis could also potentially enhance the impact of the Discussion section, which is somewhat vague at present.

2) The baseline window stretched up to the onset of the stimulus (-1000 to 0 ms). Given the relatively large number of cycles in the estimate, this baseline estimate could include stimulus-evoked power. It would be helpful to rule out this potential confound by moving the baseline window back so that it does not take into account post-stimulus signal. Otherwise there is an ambiguity in the results: It seems plausible that a higher stimulus-evoked response corresponds to better decoding. Since the baseline window might be more influenced by this response than the post-stimulus power estimate (500-1500 ms), this could lead to a negative correlation between power and decoding. This could alternatively be tested by testing for correlations between decoding and ERP amplitude.

3) Related to this point, a recent study (Iemi et al., 2019) showed that strong ERD is present in trials with strong pre-stimulus power whereas weak ERD is present in trials with weak prestimulus power. Accordingly, It is important in this study to understand what oscillatory estimate (pre or post) modulates stimulus-specific information. The authors could re-run their correlation analysis (alpha/beta power x stimulus-specific information) using only prestimulus power and only post-stimulus power. Additionally, if any result is found for the analysis of prestimulus power, it would be useful to visualize the temporal specificity of the effects (e.g. time-frequency plot).

4) The authors focus their analysis on alpha- and beta-band oscillations and use fixed bands for their analysis (in the 8-12 Hz and 13-30 Hz, respectively). It is important to highlight that a change in power in a specific band can be due to either an increase in genuine oscillations (periodic signal), and/or a change in the slope and/or offset of the aperiodic signal (Haller et al., 2018). Accordingly, we do not know whether i) these results are specific to the alpha/beta frequencies, or include other frequencies as well, and whether ii) these results are specific to the periodic and/or aperiodic signal (offset and slope). To address these questions, the authors could analyze the power spectrum in a broad frequency range (e.g. 2-50 Hz) and parameterize it into periodic and aperiodic signal, as suggested by Haller et al., 2018. Then they could assess their results for different aperiodic-adjusted frequency bands and for the slope and offset of the aperiodic signal.

5) How were BOLD responses to individual stimuli estimated? With a single-trial GLM? Was an HRF used, or a FIR basis set? Given the short interval between cue onset and choice screen onset in the retrieval phase, could some of the BOLD response be related to processing of the choice screen, and therefore partially confounded by the perceptual similarity between the chosen visual stimulus and the corresponding video?

6) Was BOLD amplitude correlated with alpha/beta power? It would be interesting to establish this before factoring BOLD amplitude out of the power/decoding correlation analysis. More details could also be given about this analysis - which voxels were selected for the BOLD amplitude estimate? Furthermore, it would be useful to visualize the full/partial correlations between alpha/beta power, fMRI BOLD signal, and fMRI stimulus-specific information in the manuscript.
