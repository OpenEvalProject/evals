# Peer review - Round 1

Editors:
- Gregory D Horwitz, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65590.sa1](https://doi.org/10.7554/eLife.65590.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

A key step towards understanding the cortical representation of color is to develop mathematical models that accurately and parsimoniously describe cortical representations of broad families of colorful stimuli. This study achieves this goal with the quadratic color model, a new benchmark f-or the quantitative assessment of cortical light responses that provides new insights into the underlying mechanisms.

Decision letter after peer review:

Thank you for submitting your article "A Quadratic Model Captures the Human V1 Response to Variations in Chromatic Direction and Contrast" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Gregory D Horwitz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen A Engel (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) The paper would be strengthened by a more thorough analysis of the QCM: comparison of the QCM to models more biologically plausible than the GLM, residuals analyzed for meaningful patterns, and quality-of-fit metrics compared with those of previous studies.

(2) The new results should be discussed in the context of previous EEG and fMRI studies.

(3) Trends in the data should be compared with predictions from psychophysics.

Reviewer #1 (Recommendations for the authors):

The quality of QCM fits could be appraised more rigorously. Are there any consistent patterns in the residuals? If so, what is the nature of the systematic deviations from the QCM, how big are they, and what might they indicate about the underlying biology?

The GLM allows jagged and non-monotonic contrast-response functions, which is unrealistic. A more useful benchmark would be a model in which contrast-response functions have a Naka-Rushton form, like they do in the QCM.

Neurons in the LGN respond more strongly to 12 Hz, full-field modulations than do most neurons in V1. One possibility is that much of the BOLD signal recorded from V1 under the conditions used in this study reflects the activity of LGN afferents. Some comments on this and potential consequences for the activation of V1 and beyond would be useful.

The changes in minor axis ratio and ellipse orientation with eccentricity are modest, but it is unclear how large we should expect them to be. Predictions from psychophysics, neurophysiology, or anatomy would provide a more useful benchmark than estimates of measurement error ("vertical spread of values at each eccentricity" and "set-to-set differences in parameters values").

More information should be giving regarding the bootstrap calculation of the 68% confidence intervals. Was the percentile method used? Was a normal distribution of parameter estimates assumed ({plus minus}1 SD of bootstrap resamples)?

Line 171: The measured BOLD percent signal change is described as "black line" in the text but more accurately as "thin gray line" in the figure legend.

Lines 626 and 627: Is an experimental run distinct from a functional run?

The discussions of cone fundamentals changing with eccentricity and contrast-response functions changing with eccentricity might be easier to understand if they were separated (both are described in the paragraph spanning lines 422-459).

The legends to Figure 12 and Supplementary Figure 9 are missing at least one line of text.

Typos: "Varience", "grayoordinate", "2-dimentional", "…and the bottom set of the show data for…"

Reviewer #2 (Recommendations for the authors):

This paper presents an important data set and model, and the successes of the paper are laid out in the other portions of this review process. Here I detail specific concerns that could be addressed in revision. Larger ones fall into four categories

1. Response patterns could be characterized even more completely, aiding readers.

Line 175: How does this R2 of the GLM compare to those reported in prior work? It would be good to know if it is in the standard range, which I bet it is.

Figure 2: Potting more of the results in terms of percent signal change rather than arbitrary units would allow comparison with previous results. This might also help readers interpret the lack of saturation of response as a function of contrast.

Line 281: It would be good to give readers a better sense of what responses are like outside of V1. Specifically, what quantitative estimates are there to support the claim that the stimuli are not driving activity beyond V1, even in V4 or V01? One solution might be to show a map of GLM variance explained throughout cortex, with some sample timecourses shown for V4ish and V01ish ROIs. It also may not be clear to non-specialists that neurons beyond V1 require spatial contrast to drive response; this could probably be highlighted more.

2. Additional comparisons of GLM and QCM.

General: While agreement between GLM and QCM is good, are there small but systematic differences? It might be helpful to include some sort of plot of residuals of the QCM fits. I think that is part of the point of Figure 7, but one could plot residuals explicitly, and it is not clear from the figure (at least to me) whether this plot is evaluating fits of just the contrast non-linearity or the entire QCM model. Figure 8: Another additional analysis that might be useful is a spatial map of a GLM to QCM comparison. It seems possible, at least in principle, that there are parts of the brain where the difference between the two models could be larger than in V1.

3. Discussion of other work.

While this is generally quite thorough, the manuscript would be strengthened by discussing the two additions mentioned in the public review: EEG results (e.g.Baseler and Sutter), and Brouwer and Heeger's "channel" model of color responses in cortex.

4. Discussion of implications for neurons in V1. A few additions to the discussion might be helpful. First, could the present results be dominated by input to V1 rather than action potentials generated within V1? This merits some discussion. Relatedly, readers might like to know if the present data set covered the LGN, which could be used in future work to address this issue.

Second, as mentioned above, additional discussion of what single unit work says about what kind of neurons will give strong responses to spatially uniform stimuli, and where they are located in cortex, could be useful.

Finally, and most trickily I suppose, is what conclusions about neurons can one make from the good QCM fit itself (besides lack of eccentricity effects). Can one conclude that for these stimulus conditions neurons in V1 whose preferred color direction is at or near L-M have higher gain than neurons whose preferred color direction is at or near L+M? I realize that there are a lot of assumptions (e.g. about separability and pooling of the signals by the fMRI response) being made in such a statement. I guess one could also build an "LGN-type" model that assumes all signal comes from just L+M or L-M tuned neurons, which could fit comparably to the QCM, but potentially with fewer parameters, since it assumes a 45 degree orientation of one population and a 135 degree orientation of another (almost equivalently a 2 channel version of the Brouwer and Heeger model). This is hinted at in line 370 in terms of psychophysics, but the model can be constrained by single unit data, at least from LGN. Is there anything useful one could conclude from such fits?

A final possible form this discussion could take is to tackle the question: Are there plausible neural response patterns that would be expected to not be well-fit by the QCM, and so the present data discomfirm them? I understand the authors' desire to not be speculative, but readers may already be speculating.

Reviewer #3 (Recommendations for the authors):

I think the main weakness here is the link between biology and data. Is it possible to implement a simple but biologically plausible population model of color processing in V1 (involving just the low SF-sensitive neurons) and test it against the data here? Such a model might have more than 6 parameters.… but fewer than 40: as the authors point out, the data are consistent with a model that sums approximately independent inputs from L-M and L+M channels. The authors might then discuss (qualitatively) how they expect the response functions to change as other populations of chromatically-sensitive neurons are excited by, for example, the presence of spatial structure.

Psychophysical data would also benefit the paper. I know there would be a lot of conditions – but with efficient staircases, data could be collected on at least some subjects to examine, for example, the observation that model parameters do not change across eccentricity (a surprising and interesting result!). Absent that, some more quantitative comparisons with existing psychophysical data (and neuroimaging data – for example Brouwer and Heeger's work) would be nice.
