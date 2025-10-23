# Peer review - Round 1

Editors:
- Dorothy Cowie, https://ror.org/01v29qb04 Durham University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87463.sa0](https://doi.org/10.7554/eLife.87463.sa0)

This important work on locomotor development takes a longitudinal approach to show that the number of basic locomotor 'primitives' in infant stepping increases from newborn to walking onset, while the variability in their activation decreases. It presents convincing data from the modelling of EMG and kinematic data, which should be of interest to physiologists and psychologists interested in motor skills and development.


---

# Peer review - Round 1

Editors:
- Dorothy Cowie, https://ror.org/01v29qb04 Durham University United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87463.sa1](https://doi.org/10.7554/eLife.87463.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Generating variability from motor primitives during infant locomotor development" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Vincent C. K. Cheung (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife at this time.

Specifically, while we very much appreciated the difficulty of infant longitudinal data collection, we felt that the dataset presented here was not large and consistent enough to warrant its conclusions. The fact that analyses were split into steps and kicks, with low numbers of participants in each, did not allow R1 or R3 to feel confident about its publication as it stands. Both R1 and R3 also make the point that in such a rich dataset it is not clear why certain cycles, samples or measures were selected. Finally, R2 notes that an alternative interpretation of your results might be possible – rejecting (or accepting) this would require some remodelling of your data. We all felt that the theoretical point of your paper was important, and we welcomed your general approach. We are therefore sorry not to be able to recommend it for publication at this time. However, if you feel that you can address these issues, we are open to a resubmission. In that case, we would ask you to include a point-by-point response to the reviews here, detailing the changes you have made. In any event we commend you on this interesting work and wish you all the best with future submissions.

Reviewer #1 (Recommendations for the authors):

In terms of introducing and interpreting the work, and situating your study in light of others' and in terms of children's overall behavioural repertoire, I think this could be done by additions to the text. I will add here that although I am not familiar with it, it seems that the paper by Sylos-labini (2020) is very relevant, and I think it would be good to make more explicit the similarities and differences between your studies.

My point about analyses being based on a limited sample of data in the Public Review, is for me the major weakness of the study, and I think the very simple solution is to collect more data. I think if you could show the patterns you do in a larger sample, the paper would make a far more substantial contribution to the literature. I really enjoyed the general approach you have taken, but I just don't feel convinced that you can draw strong conclusions from the current dataset. To expand a little on this point: I know that from Thelen's work, early kicking movements are kinematically very similar to steps, but I question whether you can really select these as entirely equivalent. Indeed Figure 2 demonstrates clear differences in the EMG patterns of steps and kicks. If these are not to be considered equivalent, then as far as I understand, the data on the development of stepping is based on a sample of n=6, which is really very low, and I do not think is enough to draw the broad conclusions that one would want for this journal. Likewise, if 6/12 contributed steps at birth and 9/12 contributed kicks, it would be useful to know how much these groups overlapped and what the similarities were between a single infant's steps and kicks.

Finally, I have some additional points on presentation which I hope are helpful for future submissions:

Figure 1

It's not clear to me how the left-right alternating gait pattern comes into play in the model. From the spatial module plots, it looks like there is no particular correlation between a left-foot step and the subsequent right-foot step. Is that true? Is the temporal structure of the gait cycle imposed on the variability in any way or included in the model? Relatedly, why are the spatial but not the temporal modules split by leg?

Figure 2

In Figure 2, from the legend it's not clear why only high-pass filtered data is shown, why the reader needs to know this, and when low-pass filters were also applied. Figure 2 legend Typo: "The scale if 1 second is displayed"

Since the topic is variability, it would be good to see not just the full patterns across 10 muscles for each behaviour/ timepoint, but e.g. indicative traces representing variability in 1 muscle at early and late time points.

Reviewer #2 (Recommendations for the authors):

The authors' argument can potentially be made a lot stronger if alternative models of motor modules that permit cycle-to-cycle variability of the spatial and temporal modules themselves can be considered. For instance, with the NMF algorithm, it is possible to extract trial-specific wi(t) and wj with a second extraction, using results of the first extraction as initial estimates (e.g., see Cheung et al., 2020, IEEE-OJEMB; but there may be other better methods). It can then be assessed whether the variance of wi(t), aijs, or wj relates the best to the kinematic and/or EMG variability.

Reviewer #3 (Recommendations for the authors):

I recommend the authors will collect data from more individuals, in more data points while being consistent with the recording timing. The paper would also benefit from more clarification about the motivation for the study and the rationale of the measurements and the specific techniques. Authors should also consider recording data in the natural environment.

After collecting the additional data, I recommend that the authors will conduct analyses that focus on individual differences that will use the power of longitudinal recordings to provide insights into the development of motor primitives (that can be using unsupervised machine learning, or any other approach). Finally, to cope with infants' real-life changes, I strongly recommend analysing motor movement more generally without focusing on infants' alternating leg movements.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Generating variability from motor primitives during infant locomotor development" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tamar Makin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In general, the reviewers were happy with your revisions, but they have made some relatively minor further suggestions for improving the clarity and presentation of the paper, we would be grateful if you could consider the reviewers suggestions appended below (both public and for authors) while revising your manuscript.

Reviewer #1 (Recommendations for the authors):

As reviewer I made 4 main points.

1. Introduce neural and developmental aspects of the work; relate to more varied patterns of walking.

The reviewer has now added these points in the introduction, giving the reader better context for understanding the work. Still, I suggest that the extant developmental literature on learning to walk needs better integrated into the ms – an excellent place to start is Adolph and Cole, TICS 2018.

2. The dataset is limited and sparse.

The work is now based on a greater number of participants (18 vs 10) and a greater number of cycles (586 vs 200). This enhances the robustness of the work. It is apparent that many of the same patterns apparent in the earlier, more stringent version of the analysis, are still present in this broader dataset. The inclusion of treadmill steps and non-consecutive steps does not seem unreasonable. The table is helpful.

3. Interpretation is unclear at points.

In their rebuttal the authors give an interesting comment on purposeful vs incidental variability. There is no need to go into this in the paper in more detail. You now clarify the difference from the Sylos-Labini paper better. On re-reading Dominici Science, you should clarify why your absolute number of modules is higher than theirs (e.g. yours 4 vs Domini 2 at birth?)

4. You need to clarify aspects of the Figures

These points are now clearer.

Reviewer #2 (Recommendations for the authors):

I read this revised version in detail and found it to be more compelling than the previous version. The Introduction, in particular, is a lot more well written. As shown in your new analysis provided in the rebuttal, it is reassuring that the trend of a decreasing module recruitment variability from neonates to toddlers could still be observed even when the modules themselves were permitted to vary cycle-by-cycle, thus indirectly suggesting that the changes of variability across stages is likely channeled, at least in part, through activations of the modules rather than variability of the modules themselves. I suggest putting this new analysis as supplementary information (if possible) for the interested readers, so that the overall readability of the main text can be kept.
