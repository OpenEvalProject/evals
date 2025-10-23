# Peer review - Round 1

Editors:
- Thomas Serre, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56603.sa1](https://doi.org/10.7554/eLife.56603.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Recurrent processes support a cascade of hierarchical decisions" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Thomas Serre as Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors use a combination of MEG, structural MRI, and computational modeling to measure how the visual cortex accumulates information for discriminating between objects. Using a digit/letter warping dataset, the authors identify difficult exemplars, devise clever analyses to show when representations become categorical, and combine temporal decoding analyses with modeling to describe dynamics and infer computations. This paper has a significant number of results, elegantly presented in beautiful figures. While some (if not most) of the conclusions derived from the work may have been reached independently by prior studies, one major strength of the present manuscript is to examine all these questions within a single dataset. Further qualities are the use of an elegant experimental design, thorough decoding analysis methods, and adequate use of modeling to help disentangle alternative explanations.

However, as detailed below, the reviewers have identified a number of weaknesses and are requesting that the authors comment on these critiques. One of the main issues raised by the reviewers has to do with some of the effect sizes and underlying statistical tests.

Essential revisions:

Statistics

The reviewers struggled a bit with the effect sizes reported. The authors normalize their scores (Figure 2C, Figure 4), which makes the effects look strikingly similar. But the truth is that some of the effect sizes are so small (AUCs between 0.5-0.6) that it can be hard to accept some of the findings. The reviewers would like to ask the authors to think of additional analyses that they could run that would ease these concerns.

While the maximum values of the curves in this figure are very different in range, the variations in baselines of blue, green, and orange curves do not show the scaling. Please provide figures without the scaling.

Is the trial uncertainty decoding time course significant? The effect size is very small compared to other features and it is very distributed over the brain which makes us wonder if this feature is actually readable from the brain activity.

There are no statistical tests reported in Figure 1G. Please mark significant decoding scores over time by drawing a contour line around the significant clusters. Please describe the statistical tests in Figure 2A and B as the multiple comparison corrections are unclear.

Figure 2A is thresholded based on t-values that exceed an uncorrected p <.1. The reviewers are hoping this is a typo.

For the curves in Figure 2C, the authors do not indicate the time points when the scores are above chance. For example, we do not know if the blue curve with a max of 0.08 is even significant.

In addition to multiple comparison corrections across time, the authors should correct for multiple comparisons across five features.

The authors have not reported the thresholds they use for cluster definition and cluster size corrections. Please comment. This is especially important because it is not clear if the authors have also corrected for 5 multiple comparisons across the five features.

Subsection “Hierarchical recurrence implements a series of all-or-none decisions”: Between 400 and 810 ms, the predictions of 'perceptual category' decoders were better accounted for by sigmoidal (r=0.77 +/-0.03, p<0.001) than by linear trends (r=0.77 +/-0.03, p<0.001)? Please comment.

Subsection “Hierarchical recurrence induces an accumulation of delays”: the authors test the correlation of peak latency of averaged temporal decodings when averaged over training times. Please do this analysis with the temporal decoding time courses in Figure 2C. Because the main temporal dynamics occur along the diagonal of the TG decoding matrix.

Modeling

Another issue is with the modeling simulations described in the subsection “Statistics”, which disambiguates between the hypotheses in Figure 3. The reviewers' (maybe incorrect) interpretation was that the authors tested whether or not these stimuli are being processed via hierarchical recurrent computations or not. The reviewers thought this was a strawman argument, as there is no reason to suspect the converse (non-hierarchical/non-recurrent). This modeling work thus only added to their overall feeling that the contributions of the present manuscript were actually quite limited.

Interpretation

We would suggest adding clear statements in the Abstract and in the Discussion cautioning that these exact results may be limited to this specific task (difficult digit vs. letter classification), and could differ for other tasks (e.g. simple detection task, natural scene or object categorization).

Contributions

There must be a discussion of (Freedman et al., 2002). Those authors parametrically warped dog/cat stimuli to show that a region of the prefrontal cortex (PFC) reflected stimulus discriminability. This is of course closely related to the present work, where the authors use digit/letter stimuli to accomplish the same thing and focus on the visual cortex rather than PFC. The reviewers request some clarification about the contributions of the present study in light of this work and especially discuss the possibility that most of the presented results could be reflecting common input from PFC as suggested by Linsley and MacEvoy, 2014.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Recurrent processes support a cascade of hierarchical decisions" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The reviewers made a few additional comments.

1) The most important one deals with the lack of significance in your mass-univariate analyses. We suggest you describe the analyses in the main text and explain that it did not reach significance. Because the results make sense, the reviewers suggest to keep them but to move it to the SI as they should be taken with a grain of salt (and state that).

2) Related to comment 2 on statistics, the figures in Figure 2—figure supplements 1 and 2 again are scaled; because the y-axis of all plots are scaled to the maximum of each plot.
