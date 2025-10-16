# Peer review - Round 1

Editors:
- Jack L Gallant, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31448.029](https://doi.org/10.7554/eLife.31448.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The lawful imprecision of human surface tilt estimation in natural scenes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Reviewing Editor Jack Gallant, and David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mark Lescroart (Reviewer #1); Michael Landy (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors study the ability of human subjects to estimate surface tilt in natural images. They find (among other results) that humans are biased to estimate tilt at cardinal (vertical and horizontal) orientations and show that an image-computable Bayesian model makes estimates of tilt that are similar to human estimates. Both reviewers found the paper to be interesting and timely. Reviewer 2 made only minor comments, but reviewer 1 had some concerns and requested additional behavioral data. The reviewing editor is persuaded by these arguments.

Essential revisions:

1) The authors have found that variance (or noise) in tilt in the stimulus leads to less accurate estimation of tilt. However, the natural images used in this study are highly variable, so this result isn't all that surprising. The authors should analyze whether the model is predicting human performance well simply because some trials have more or less tilt variance than others. If this is the case, the result is much less interesting – variance (or noise) in a tilt should cause poorer tilt estimates. Similarly, alternative versions of the plots in Figure 3 should be generated with low-tilt-variance scenes, to see if the bias shows up as clearly.

2) The authors should validate their results using artificial images with more naturalistic textures (e.g., 1/f). In general, the authors should try to introduce variability into the artificial images of the same kind and magnitude as the variability in the natural images.

3) The authors should perform some control experiments to verify that the results hold for stimuli larger than 3 degrees. If possible, it would be good to verify these effects in complex natural scenes.

Reviewer #1:

The authors study the ability of human subjects to estimate surface tilt in natural images. They find (among other results) that humans are biased to estimate tilt at cardinal (vertical and horizontal) orientations and show that an image-computable Bayesian model makes estimates of tilt that are similar to human estimates.

This is an interesting and timely question, and the study is generally well executed. The figures are nice, the writing is clear, and the dataset the authors use (if it is to be shared) seems a useful contribution. However, I have some concerns about the experimental paradigm. None of these concerns alone are fatal flaws, but when combined with some of the results, they give me doubts about the impact of the rest of the results.

First, the artificial stimuli are perhaps too simplified (very regularly textured, wholly planar). This is not representative of studies of tilt estimation: several studies have had human subjects estimate surface orientation (or related quantities) of non-planar surfaces (e.g. Todd et al., 1996; Li and Zaidi, 2000; Norman et al., 2006). The highly simple nature of the artificial stimuli here creates several obvious differences between the natural and artificial images. Figure 8A shows that one such difference – tilt variance, present in the natural images but not in the artificial ones – accounts for all of the difference in mean tilt estimation accuracy between artificial and natural images. Stated another way, the authors have found that variance (or noise) in tilt in the stimulus leads to less accurate estimation of tilt. Note that this is not noise in the image cues or anything else – this is variance in the exact parameter that is being estimated. I may be missing something, but this particular result (which appears to be the biggest effect in the experiment) seems wholly expected to me. So, I am unimpressed by the conclusion statement: "The dramatic, but lawful, fall-off in performance with natural stimuli highlights the importance of performing studies with the stimuli visual systems evolved to process."

The large effect of tilt variance calls into question the size of other effects the authors report. Figure 8—figure supplement 1 shows that, for natural stimuli with low tilt variance, the bias toward estimating vertical (0 and 180 degree) tilts is greatly diminished (the count ratio between estimated and true instances of vertical tilt is very near to 1). (As a side note, Figure 8—figure supplement 1 is a critical figure and should appear in the main manuscript). It is also not clear how much tilt variance might be affecting the model's predictions of trial-to-trial errors; the authors should analyze whether the model is predicting human performance well simply because some trials have more or less tilt variance than others. If this is the case, the result is much less interesting – variance (or noise) in a tilt should cause poorer tilt estimates. Similarly, alternative versions of the plots in Figure 3 should be generated with low-tilt-variance scenes, to see if the bias shows up as clearly.

The other striking difference between the artificial and natural images is the extreme regularity of the textures in the artificial images (at least of the plaids shown in Figure 2). The authors also used 1/f noise as a texture in the artificial images – did human performance differ depending on whether the artificial stimuli were plaid or 1/f noise? In general, it seems that adding more types of variation to the artificial stimuli and assessing the effects of that variation would provide a good way to assess what sorts of variation make human performance look more like it does for natural images. I suspect that the authors plan to do this in future work, but I think it would substantially increase the impact of this work to include such data and analyses here.

Finally – I admit some disappointment with the choice of only showing 3 degree stimuli. To me, this lessens the impact of the work as well; a 3 degree image patch hardly constitutes a "scene". Thus, the following conclusion statement seems a bit of a reach: "We quantify performance in natural scenes and report that human tilt percepts are often neither accurate nor precise". Human estimates of tilt given full natural images (including much more context) would likely be better than the estimates reported here. I realize this is a very difficult problem, but eLife is also a broad, prestigous journal; studying tilt estimation in natural image patches may be a critical step on the way to studying tilt estimation in full scenes, but it also seems less broadly interesting.

Last, a few notes on the model: First, I am puzzled as to why the authors do not include model performance on their artificial stimuli, too. This seems to be a straightforward and easy test of the generality of the model. Second, it's not clear to me whether the "estimate cube" of optimal mappings between image cues and tilts is computed using some, all, or none of the same images that the subjects saw in the experiment. The authors should clarify this point.

I should note again that the concerns above are almost entirely about impact. I hesitate to reject an otherwise interesting and well-executed study on grounds that it's just not splashy enough. And there are several interesting and solid results in this paper. The fact that tilt variance is correlated with tilt angle in a large sample of natural scenes seems solidly supported and important. Modulo the questions I raised above, the MMSE model performance appears to provide a good match for human performance in the natural images. The persistent difference between errors estimating cardinal and oblique tilt, as well as the persistent bias to estimate horizontal tilt – both with matched tilt variance – are also interesting. Thus, I am on the fence about this paper, mostly because its impact seems marginal. I could be convinced to accept the paper with revisions or to reject the paper.

Reviewer #2:

This is a lovely paper, showing that a nonparametric Bayesian model of tilt estimation accounts startlingly well for human behavior in a tilt-estimation task. My comments are mainly about improving the clarity, not much more.

Introduction: Many of my comments are a result of reading it in (my) natural order, i.e., your page order with diversions to the Methods when needed. So, when I got here I wondered whether the patches to be judged were centered on the display or occluded in the position in the original images. That's never stated explicitly but implied by a figure that hasn't come up yet.

Introduction: You never motivate/justify pooling over tilt sign until much, much later, and so I was surprised you threw information away from the start. I wondered about it again for Figure 3 where, given that you provide disparity, the tilt sign ambiguity from pictorial cues should be alleviated.

Figure 2 et seq.: Why didn't you run the model on the artificial stimuli and show the model fits for those data points (or misfits, as the case may be)?

Subsection “Normative model”: The citation of Figure 6—figure supplement 2 here seems out of place. The analyses for this figure don't appear until the next page. Also, shouldn't all the supplementary figures be cited somewhere in the main text? I think a bunch aren't.

Subsection “Trial-by-trial Error: Is -> Are.

Figure 8B:Exactly what bin cutoffs did you use for blue vs. red here?

Subsection “Effect of Natural Depth Variation”: artificially -> artificial.

Subsection “Generality of Conclusions and Future Directions”: our -> are.

Subsection “Cue-combination with and without independence assumptions”: This reference to Figure 6—figure supplement 2, since the pooled/averaged model is not in the figure, but merely mentioned in its legend.

Subsectiion “Experiment”: More details please: What's your definition of contrast, refer to the figure to state what part of the patch they were supposed to judge, were the judged bins over 180 or 360 degrees (I only say this because Figure 1 leads the reader to believe that it's over 180 degrees only). Please show and give details about the two types of artificial stimuli. Do responses to them differ from one another?

Subsection “Groundtruth tilt”: "atan2" is MATLAB notation, I'd think. You might want to say what you mean there.

Subsection “Image cues to tilt”: I'd like more detail here as well. The disparity cue must be based on a definition of "local" and a restriction of cross-correlation shifts. The disparity gradient requires a scale. The disparity gradient doesn't have a tilt sign ambiguity, but the texture cue does. I'm not sure "patch size at half height" won't confuse people (you don't mean the viewed patch, but rather the patch after multiplying by the Gaussian window).

Figure 6—figure supplement 2: Actually, I'm rather surprised that the single-cue models (especially those other than disparity) perform as well as they do. It worries me that there are weird regularities in your database. You never say what your definition of luminance is exactly, but why should tilt be dependent on luminance? How are each cue binned? Are the same bins used for the single-cue models, so that those models have vastly smaller measured parameters?

Figure 6—figure supplement 2 legend, line 12: "…but better than the prior or…".
