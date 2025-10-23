# Peer review - Round 1

Editors:
- Dora Angelaki, Baylor College of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01312.013](https://doi.org/10.7554/eLife.01312.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Decoding neural responses to sound location” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This is a modeling study comparing different ways of extracting information about sound location from the responses of a model population of binaural neurons. The conclusion of the manuscript is that, while a labeled line code is too inefficient, summing the activity in each hemisphere discards too much of the information that is present in neural activity patterns.

This is an interesting and important topic that could be of general interest. However, one of the reviewers felt that it would be nice to expand on the population decoding, and discuss the fact that they have not considered population models that do not simply sum activities (e.g.,, those with optimal weighting of the contribution of each cell) and network nonlinearities useful for marginalization of task-irrelevant information like divisive normalization. Other properties known to be critical for information loss and decoding optimality, like shared variability and interneuronal correlations, have also not been considered. The reviewers would like to see a broader coverage/discussion, such that this work can appeal to the broader neuroscience community.

Specific comments:

One of the reviewers particularly liked that the authors model the effects of a unilateral lesion. Such a lesion of their pattern-match model predicts strictly contralesional localization deficits, which is what is seen in all the animal lesion studies. In contrast, a unilateral lesion of their hemispheric model predicts bilateral deficits, which are never seen in animal studies. The reviewers would like to see that result given a little more prominence, such as mention in the Abstract.

The title should be revised to more specifically indicate that the study examines “sound location based on interaural time differences”.

The results in Figure 7 for the simulated lesions should be compared, at least qualitatively, to results for the human listeners with lesions. The two models shown in Figure 7B have very different results, so the comparison may be interesting.

In the section on “Comparison to Behavioral Performance”, the argument is made that the hemispheric difference model predicts errors that are larger than those observed in behavioral studies. In the preamble to this section, it is stated that the pattern match model has very small errors, but the numerical errors for the pattern-match model are not provided for comparison to specific species and cases, as they are for the hemispheric difference model. Despite the fact that the pattern-match model's errors will appear to be quite small, they are useful and should be provided for the reader. Although the absolute errors will be smaller than behavioral thresholds, the trends in the errors across conditions are interesting to present. One can argue that the actual system will have errors larger than this very detailed model, but the (fractional) difference between model and actual performance should be comparable across conditions. (That is, it would be bothersome if the model were 1 order of magnitude too accurate in some cases, and 3 orders of magnitude too accurate in others, such that the degradation in performance required to match behavior had to change dramatically across conditions.)

The model results presented here illustrate an interesting difference in the trend of the errors between the hemispheric model and both the smoothed peak and pattern-match models at high frequencies (e.g., Figures 2, 3, 4). The comparison of this prediction to behavioral results deserves inclusion in the section that compares model to behavioral performance. Again, this is a consistent trend in the results that can be compared qualitatively to trends in behavioral results.

In the Discussion, the argument is made that additional processing would be required to generate spatially tuned neurons from the hemispheric model. This is an interesting point, but it is not clear what spatially tuned neurons the authors are thinking about. It would help to be more specific as to what neurons (presumably at a level higher than the IC) are being considered here (indeed, there are precious few spatially tuned neurons at higher levels, and the hemispheric model doesn't require such neurons, does it?). For example, it might be helpful to consider decoding schemes proposed for the cortex. Stecker, Harrington, and Middlebrooks, 2005 (cited) tested a hemispheric model as a sort of worst-case scenario, although several authors have seized on the hemispheric model as reality. Others have looked at decoding based on spatial tuning of individual neurons, compiled as ensembles (anesthetized cat: Furukawa, Xu, and Middlebrooks, 2000; behaving cat: Lee and Middlebrooks, 2013; awake monkey: Miller and Recanzone, 2009). These experimental studies should be discussed because they do empirically what the authors are doing with their simulations.

It would also be useful for the authors to include comment on the recent paper by Briley et al., JARO 2013, Vol 14: 83-101, which supports the hemispheric model, based on EEG recordings in human.
