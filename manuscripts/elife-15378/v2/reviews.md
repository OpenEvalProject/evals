# Peer review - Round 1

Editors:
- Richard Ivry, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15378.015](https://doi.org/10.7554/eLife.15378.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Tagging motor memories with transcranial direct current stimulation allows later artificially-controlled retrieval" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Michael Nitsche and Richard Ivry, who is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers found considerable merit in this paper. The role of context in sensorimotor learning has been the subject of considerable interest in the past few years. While early results emphasized how sensorimotor adaptation was relatively impervious to context (e.g., color cues), recent work has identified a number of conditions in which contextual cues can be quite powerful. The current study takes the question of context in an entirely new direction, at least within the world of human motor learning, asking if modulation of the (endogenous) neural state can serve as a sufficient contextual cue. To this end, the authors use tDCS to establish the context, associating a force field in one direction with anodal tDCS and a force field in the opposite direction with cathodal tDCS. Of special note here is that the participants are completely unaware of the "cue", something that is not (usually) possible in studies involving behavioral manipulations of context.

Essential revisions:

In general, the reviewers found the motivation of the study of the study to be sound, were intrigued by the results, and found the discussion to be appropriate. While our requests for revision are relatively modest, there is one major, indeed critical, issue that needs to be addressed. While the leftward and rightward force fields induce significant changes in performance, the context effect is relatively small (estimate of about 5% of the force difference). In itself, this is not a concern if the effect is robust-that the authors see any effect here is impressive. However, the key analysis seems overly complex with a lot of parameters. The authors fit a 5-parameter function to every noisy individual-subject test-period data set, the result of which is there are over 400 free parameters (5params/subject x [48 subjects in the main experiments + 36 subjects in the controls], or about 80 in each experiment) to "model" the decay curves in the data. The residuals of these models serve as the primary "data" for the main analysis. With this analysis, one would want to see some graphic depiction of the parameters of the individual double-exponential fit. But, as noted below, we believe there is a better solution.

While there is a general concern with the complexity of this analysis, there is an additional statistical issue here. Between subgroup differences in the fits may seem quite different for the anodal-cathodal switching pattern, but the patterns are not statistically independent. Fitting double exponentials may distort the estimate of the true anodal/cathodal switching effect. This is especially concerning if the switching effects are small compared to the size of the double exponential fits (as is the case here).

The reviewers believe that a much simpler analysis should be possible. The authors could simply analyze the differences in forces that are shown in the middle row, left panel of Figure 2. The middle panel (2e, difference for the sham condition) should probably be subtracted from the left panel (2b, the difference for the stimulation condition), and then the mean of each block can be statistically compared.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tagging motor memories with transcranial direct current stimulation allows later artificially-controlled retrieval" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens as the Senior Editor, a Reviewing Editor, Rich Ivry, and one reviewer.

We appreciate your response to the initial reviews. We continue to think that this paper can make a novel and intriguing contribution to the literature on context effects in sensorimotor learning. However, we believe another round of revision is required. I think we can all agree that the effects are small here - not surprisingly so given the subtlety of the manipulation. Given this, we think it important that the primary analysis entail the fewest possible assumptions, and that these assumptions be thoroughly vetted in the paper.

The challenge you face in the analysis here is that your context effects are intermingled with natural decay processes. The curve fitting is designed to factor out the decay, but to do so requires making various assumptions (single vs double exponential), as well as entails lots of parameters since this is done on an individual basis for multiple epochs.

Your new Figure 3, which we think is a nice addition to the paper, suggests an alternative, and simple approach: use the S-T group data as a way to estimate the decay effect. These data are not involved in the critical analyses and thus constitute an independent method to look at decay, one that will not be conflated with the effect of stimulation context. In a sense, this provides a straightforward way to subtract out a baseline effect of the decay and then observe your main point of interest, the residual context effect. Making Figure 3 the key here, you end up subtracting 3d from 3b. In looking at things, it looks like the effect will be limited to the latter two probes. This would change your story to make the point that the effects of tDCS build up over time. We recommend that this analysis be the primary one in the manuscript, with panels A, C, and E providing the key raw data and the Panels B, D, and F the main point of comparison. You can still include the analysis from Figure 2, either moving this to a secondary analysis, or appended as an addition to a primary figure.

We were also confused why your model-free analysis was not performed in an analogous manner as you had done with the double exponential. You opted to turn to a bootstrap procedure here. While there is nothing wrong with the bootstrap approach, the lack of symmetry between the two approaches is confusing. It would seem more straightforward to employ a similar approach for the model-free and double exponential analysis and then presenting both analyses in the paper. Assuming the results converge on a common finding-namely that there is a residual context effect, the reader could then have confidence that the results were not specific to a given set of assumptions. As you now do things, we end up with a parametric analysis when considering a double exponential for decay and a non-parametric analysis when considering a single exponential.
