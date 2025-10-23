# Peer review - Round 1

Editors:
- Demba Ba, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81499.sa0](https://doi.org/10.7554/eLife.81499.sa0)

This article proposes a combination of biomechanical modeling and in-silico experiments, on a newly-curated passive-movement dataset, to elucidate the nature of computations in the proprioceptive pathway. The authors find that, in addition to its canonical role in representing the body state, the proprioceptive pathway may have evolved to recognize actions. Overall, the authors' findings lead to new hypotheses about proprioception that future in-vivo experiments could test.


---

# Peer review - Round 1

Editors:
- Demba Ba, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81499.sa1](https://doi.org/10.7554/eLife.81499.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Contrasting action and posture coding with hierarchical deep neural network models of proprioception" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Nikolaus Kriegeskorte (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The reviewers found the topic of the paper and its contributions interesting.

At the same time, overall, the reviewers

1. Expressed reservations at the lack of quantitative evaluation of neural data, and more importantly

2. Suggest that to lend support to the current claim that the function of the proprioceptive system is action recognition, the authors would need to train with losses intermediate between posture and action that, in addition to action can decode velocity as well.

The Reviewing Editor agrees with the reviewers that 2. would strengthen the manuscript. In its absence, the Reviewing Editor would find it difficult to fully support the scientific findings of the manuscript. The Reviewing Editor encourages the authors to consider additional experiments based on the detailed comments from the reviewers.

Reviewer #1 (Recommendations for the authors):

As I have explained in the public review, I don't agree with the main conclusion of the paper. The end effector position estimation task is too simple and is not the right model to contrast the action recognition model with. Ideally, I would argue that one should simulate a full closed-loop control model to be able to make a claim like this for proprioception. At the very least, they could have a state estimation network that estimates effector velocities in addition to position, which would likely learn speed, velocity, and direction-selective hidden layer representations. As far as I can see, the lack of such cells is the criterion that they use to rule out the TDT task.

I don't know if it exists, but if there is relevant data available, they could make more detailed comparisons to data. For example, do the trends they see in the change of selectivity across network layers match that in the brain?

Reviewer #2 (Recommendations for the authors):

1) The title refers to "posture", but this term is not at all mentioned in the abstract, which instead contrasts action and trajectory decoding. It would be good to choose consistent terminology or at least to relate the term posture to the trajectory decoding objective in the abstract.

2) Some more motivation is needed, even in the abstract, for the idea that the function of the proprioceptive pathway is to recognize what the brain already knows: the action it is trying to perform. This is fascinating and plausible to me, but it is not at all obvious. The introduction and discussion should contain the authors' best guesses (even if speculative) to better motivate the ART objective and interpret the central result.

3) Please address the two weaknesses I mention in the public review (no quantitative evaluation, unclear what about the ART drives the main result) in the discussion with a view to guiding future follow-up studies (including ones that build on the data set and code from this study).

4) It might be clearer to refer to the control models as untrained models (as different other kinds of control model could have been used).

5) Figure 4A: "CKA score" is not a conceptually informative label for the color bar. "similarity between untrained and trained model representations [CKA]" would be better.

6) Figure 4B: The t-SNE plots seem to show little more than that the ART, but not the TDT model shown achieves the ART model's objective. If models trained with different objectives are to be compared, then the visualization should not be partial to one of the objectives. Coloring dots by trajectory similarity might provide an alternative scheme that could be added. More generally, t-SNE requires setting hyperparameters and its objective function is hard to state concisely (beyond maintaining neighbor relationships), making interpretation more difficult than for say metric-scale MDS. t-SNE may also show classes as clustered that are not linearly separable, failing to visualize the gradual disentangling across layers, as in Figure 5 here: https://arxiv.org/abs/2107.00731. I have no definite suggestion but did not find this panel particularly informative in the present form.

7) Figure 4C: With one tick mark per letter, some readers will miss the many conditions per letter that are shown in the RDMs (despite this being apparent in the proprioceptive RDM). It might be better to show the whole matrix much larger in a separate supplemental figure and to focus on a, b, c, d, and e in Figure 4C and to add tickmarks for, say 5 instances for each of these letters. The number of conditions shown should also be stated in the figure legend and ideally should match the number of tickmarks on the matrix.

8) Figure 5E: The unconventional lines connecting percentiles across the vertical distribution plots add more clutter than clarity. It might be better to plot the distributions and point summaries separately or choose one. An exacerbating factor might be that the coding of the different tuning properties in the shading is not clearly discernible, and I end up having to count which of the five tuning variables I am looking at. Using a separate plot for each tuning type might help.

9) The paper contains some ungrammatical English and typos and would benefit from careful proofreading and editing.

10) CKA stands for "centered kernel alignment" (not "centered kernel analysis").
