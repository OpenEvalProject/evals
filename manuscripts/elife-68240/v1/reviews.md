# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68240.sa1](https://doi.org/10.7554/eLife.68240.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This combined MEG pupillometry study investigated stimulus-specific plasticity in human visual γ-band activity. The work was conducted thoroughly, and exhibits a high degree of technical proficiency. The results show that both gamma-band MEG and pupil size responses to visual stimuli adapt across stimulus repetitions. The claims are fully supported by the data and this work will be of broad interest to readers in the fields of non-human primate and human electrophysiology.

Decision letter after peer review:

Thank you for submitting your article "Stimulus-specific plasticity in human visual gamma-band activity and functional connectivity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tomas Knapen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The reviewers were impressed by the manuscript and data presented. However, there are two issues that should be addressed in a revision:

1) More details should be provided in the current manuscript about aspects of the methods and analyses. See in particular, the recommendations from Reviewer #2.

2) The manuscript would be stronger if clearer links could be drawn between the different aspects of the data, i.e. from pupil to gamma to behavior. You should carefully consider the suggestions from Reviewer #3.

Reviewer #2 (Recommendations for the authors):

The authors should give more details about how induced oscillations were extracted. The reader is referred only to a bioarchive paper, but some essential details should also be given in the present manuscript. It is written that subject specific theta, α, β, and γ frequencies were determined using 1/f-removal and subsequent fitting of Gaussians to the stimulus-induced power spectra. This is a bit confusing, and it is unclear if the power is computed with rather wide canonical frequency bands matching to theta, α, β, and γ or with narrow-band Gaussians which are reported e.g. in Figure 3d. Please clarify. If the latter, please describe also how data was averaged within the frequency bands. This holds at least for data in Figure 5. Could the authors also add information of what is the frequency and temporal resolution of this approach. This is particularly relevant to the analysis of γ peak frequencies shown in Figure 3b.

The stimulus power was calculated and averaged over 0.3-1.3 s post-stimulus period from stimulus onset. This was despite the stimuli containing change in the contrast and rotation (target events) in a period of 0.3-2 s with the reported mean response time being 484ms. From this description it seems that the analysis period for oscillatory power includes the static grating stimuli, its target events (changes) together with the motor responses to these and for sometimes also data after the motor responses. Maybe there is something missing from the Methods section to this description. If not, then the reported γ band responses contain various different forms of neuronal activity some of which cannot be related to behavior nor stimulus processing and which the data-analysis in its present form.

Is these data reported and analysis performed at sensor level or at the source level or is source level data only used for plotting the relevant brain areas?

It is not clear whether data in all panels from Figure 3, that is the main figure of the paper, is group averaged data or data from single subjects. This should be specified for each panel as it is not clear in the current version.

The authors report stimulus specificity of the gamma-band repetition suppression. Can this be due to transient increase in task difficulty by new block of stimuli rather than being stimulus repetition effect per se? The increased feed-back connectivity suggest that this might be the case.

Reviewer #3 (Recommendations for the authors):

This is great work. I have no big comments, but am very interested to see more fleshing out of the possible relations between the different types of data, and how they jointly shed light on the topic of interest.

Due to technical reasons and experimental design choices, the direct investigation of the interrelations between the different signals of interest is difficult; Granger causality analyses could only be performed on those trials for which no pupil-MEG γ correlation exists, and although behavior showed similar time-courses to MEG γ their correlation was not significant. This leaves the link between the different signals up in the air. I would like to suggest a set of analyses that might elucidate this a bit more.

The first of these are concerned specifically with the pupil size analysis.

In my hands, there is a strong inverse correlation between slow and fast pupil responses. The constrictions that the authors here use, are likely joined by slower dilatory changes in the pupil size, making me doubt their purely luminance-based explanations of some of the pupil size signatures. These slower pupil signals could provide a separate source of information that may elucidate the nature of the pupil responses and, possibly, their link to the MEG signals. Could the authors provide the baseline pupil size for all trials, much like they showed the per-trial constrictions? This is because in reversal learning experiments, there is a large pupil dilation when contexts change (cf. doing:10.1371/journal.pone.0185665) and a similar thing might be happening here, too. Such a dilatory response could impact the within-trial stimulus-induced constrictions the authors report. Similarly, the beginning of the experiment is often characterised by a similar slow dilation (cf doi:10.1371/journal.pone.0155574).

Then there's the possibility of blinks either adding large amounts of variance to the pupil size signal, or even that blinks correlate with the experimental block transitions. It would be good if the authors could check this.

Then, the specific time-course analyses. Why 10 trials? This seems a bit arbitrary from how the manuscript is now written. Also, like the authors already say, this pattern of attenuation of signals across blocks hints at two adaptational processes occurring simultaneously. Could the authors not fit two exponential processes, then? The resulting quantification of integration timescales might be an opportune quantification of the signals at hand, and aid in their comparison.

Some questions about the MEG quantifications and results;

– gamma band responses were taken up to 0.6 s post-stimulus-onset (line 829), but these then include the change in contrast of the stimulus in some trials. How do the authors make sure this doesn't impact the results?

– The inflated brain gamma band depictions seem to show ROI boundaries. Is this just an illusory coincidence? Or are there actual differences between ROIs that show themselves in this way?
