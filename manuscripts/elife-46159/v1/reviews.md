# Peer review - Round 1

Editors:
- Jörn Diedrichsen, University of Western Ontario Canada

Reviewers:
- Jörn Diedrichsen, University of Western Ontario Canada
- Christian K Machens, Champalimaud Centre for the Unknown Portugal

## Review text

DOI: [10.7554/eLife.46159.026](https://doi.org/10.7554/eLife.46159.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Motor cortex signals for each arm are mixed across hemispheres and neurons yet partitioned in the population response" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Jörn Diedrichsen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Christian K Machens (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper by Ames and Churchland provides an important and fresh look into the characteristics of neural activity in motor cortex during ipsilateral arm movements. In many ways the results confirm the study of Donchin et al., 1998, from 20 years ago, showing a high prevalence of ipsilaterally tuned activity and the lack of a tight relation between tuning for contralateral and ipsilateral movement directions. The new analyses, however, reveals the orthogonality of the population activity for contra- and ipsilateral arm, providing important constraints in understanding the function of the widespread ipsilateral activity.

Essential revisions:

The reviewers discussed the points raised in the individual reviews extensively, and agreed on the following major points that should be addressed in the revision.

1) While these findings are quite convincing, the explanation why this bilateral representation is needed (efference copy to support motor planning?) is less clear. For example, finger movements often require an increased coordination effort between both hands, e.g., for bimanual hand actions. This seems at odds with the authors' point that distal (finger) movements are less represented bilaterally than proximal (reach) movements. An additional hypothesis that maybe should be considered in the Discussion is that the non-driving cortex simply "observes" the activity of the driving hemisphere, but does not causally contribute to the driving arm movement. Like in action observation, the neural activity would occur in a muscle null-space (Kraskov et al., 2014). A possible function of such activity (if there is any) may that it helps lay establish networks in the ipsilateral hemisphere, which then underlie the inter-manual transfer of motor skill (Wiestler et al., 2014).

2) How could you confirm that recordings were actually from M1 and not, e.g., from PMd? Did you look for low ICMS thresholds? This is important since bilateral representations in PMd could be quite different from M1.

3) All analyses seem to have been done on trial-averaged data. We think that it is crucial that the authors show whether the orthogonal subspaces still robustly separate the population activity on single trials. It is necessary that single-trial activity also falls into the Null-space for the contralateral hand, such that it can avoid generating contralateral activity. While your analysis shows that on average the activity falls into the null-space, we believe it would be informative to see the spread of the projection. This could be done by projecting single trials onto the orthogonal subspaces, and showing that the information is there, or by applying single-trial dimensionality reduction techniques.

(In this context, it would be interesting to know if single-trial muscle activity in the non-driven arm can be predicted by deviations from the orthogonal subspaces. As far as I understood the limitations of the data, that will not be testable in the current data-set, as muscle activity and brain activity were recorded separately. I don’t ask the authors to do this, but would just like to point out that it could strengthen the authors' hypothesis considerably.)

4) As noted in the Discussion, activity in one M1 hemisphere has little effect on muscle activity in the non-driven arm. Yet, the dimensionality reduction and prediction analyses in Figures 9 and 10 consider the full cross-hemisphere population. To answer the question of why population activity in one hemisphere does not activate the non-driven arm, the dimensionality reduction and prediction analyses should ideally be done on a single hemisphere. The effect may be weaker (because of less data), but it should still be there. Alternatively, the authors could demonstrate that the decoding weights (or weights characterizing the subspaces) properly separate information between the two hemispheres.

5) Even within a hemisphere, an additional concern is that there might be a mix of cell types, with some responsible for direct motor control (e.g., the small proportion of cells with a preference index close to 1), and some responsible for the general computation, say. Previous work in mouse ALM has shown that such a separation can exist, with associated anatomical differences in left/right preference (Li et al., 2015, Nature 519 51-56). I would like the authors (at a minimum) to display some information about the weights of the decoders or subspaces (see also point 2).

6) The authors use PLS to find a low-dimensional linear mapping between population activity X and population activity Y, and evaluated it in generalization setting how well can predict new data. The main results are that muscle activity can be nearly equally well predicted from contra and ipsilateral M1, and that there are hardly any differences in predicting left M1 from left M1 as from right M1. The main limitation of this analysis is that it can show that the two population codes occupy a common linear subspace, but it does not show that the two population codes are structurally the same (or have the same representational geometry – Diedrichsen and Kriegeskorte, 2017). For example, consider the two population depicted in Image 1. Both have a neural dimension that codes for the vertical position of the hand and a neural dimension that codes for the horizontal position of the hand (of course neural dimensions do not cleanly represent specific physical variables, but that's not the point here). This means that you could find a two-dimensional mapping that would predict the population activity in of region A from region B, likely nearly as good as you could predict region A from region A. Furthermore, a specific muscle activity that is a linear combination of position could be read out of the population activity equally well (or bad). However, this obscures the fact that region A overemphasizes the vertical dimension of the movement, whereas region B emphasizes coding for the horizontal dimension.

This problem is especially prevalent as the underlying behavior is relatively simple. While the cycling direction dissociates position, velocity, and muscle activity, the two starting points probably do very little to add new dimensions that the functional subspace that the brain needs to encode. Thus, as long as both hemispheres occupy this relative restricted subspace of neural activity, prediction performance of the PLS model will be quite good. That is, two very different population codes can look very much the same if the experiment does not dissociate the critical dimensions.

We believe that the authors should at least acknowledge these two limitation of their regression approach.
