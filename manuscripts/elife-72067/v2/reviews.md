# Peer review - Round 1

Editors:
- Fred Rieke, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72067.sa0](https://doi.org/10.7554/eLife.72067.sa0)

This paper trains a simple neural network model to perform a behaviorally important task: the detection of looming objects. Two solutions emerge, one of which shares several properties with the actual circuit. This is a nice demonstration that training a CNN on a behaviorally-relevant task can reveal how the underlying computations work.


---

# Peer review - Round 1

Editors:
- Fred Rieke, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72067.sa1](https://doi.org/10.7554/eLife.72067.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Shallow neural networks trained to detect collisions recover features of visual loom-selective neurons" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Fred Rieke as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Catherine von Reyn (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The followed issues emerged in review – and were agreed upon by all of the reviewers in consultations.

1. Questions about the model architecture. Several model components (rotation and symmetry) were imposed rather than learned. Was this necessary? Can the model make (testable) predictions about connectomics data?

2. Types of solutions. The text and results needs to explore all three types of solution (inward, outward and unstructured) in more detail. It is currently difficult to understand why the inward and unstructured solutions are essentially dropped part way through.

3. More challenging tests of the model. Can you add distracting optic flow to the current stimulus set and/or use more naturalistic stimuli? This could help reduce the number of viable solutions.

4. Inhibitory component of the model. Inhibition is assumed to have specific properties (e.g. rectification) – and it is not clear if these are essential. Further, it is absent in some solutions. Are the properties of inhibition (when present) consistent with the broad LPi receptive fields?

5. Comparison of model with neural data. A stronger rationale is needed for why two of the many outward models are selected for comparison with neural data (and why comparisons are not made for the inward or unstructured models). It is also important to quantify the similarity of the models with neural data.

Reviewer #1 (Recommendations for the authors):

Line 26-27: It would be helpful to make a somewhat more general statement about the power of the approach that you take here.

Figure 3 is the first figure referred to, so moving it up to Figure 1 would make reading easier.

Line 79: clarify here you mean object motion, not motion of one of the edges.

Line 94-95: the relationship between timing and size-to-speed ratio is likely hard for most readers to make sense of here – suggest deleting.

Lines 150-151: suggest clarifying that excitation and inhibition in the model are not constrained to have opposite spatial dependencies as depicted in the Figure 4.

Line 170: suggest describing the loss function in a sentence in the Results.

Lines 174-176: It would be helpful to connect the outward and inward model terminology more clearly to the flow fields in Figure 3 here. I think this is just a matter of highlighting which elements of the grid in Figure 3 are relevant for each model.

Lines 177-178: describe performance measures here qualitatively.

Lines 206-209: the reason for the difference in baseline activity is not clear – and it requires a lot of effort to extract that from the methods. Can you give more intuition here in the results?

Lines 336-340: this is helpful, and some of it could come up earlier in the Results. More generally, it would be helpful to be clearer (especially in results) how much of the encoding of angular size is a property of expansion of the stimulus, and how much of how the computation is implemented.

Reviewer #2 (Recommendations for the authors):

– The manuscript is a bit difficult to understand. The authors may want to improve their explanations and figures to make them more accessible. For example, in Figure 7B, I can barely see the responses and don't see any grey lines. Perhaps showing only a subset of responses would make the figure clearer -- less is more.

– The usage of the term "ballistic" in the introduction is confusing. In many contexts, "ballistic" suggests free-falling motion; in this paper, the authors are referring to the distinction between ballistic and diffusive motion. To avoid confusion, I would suggest not using the term ballistic at all; instead, "straight line" or "linear" is just as expressive.

– The first figure that is cited in the text is Figure 3. I suggest reorganizing either the text or the figures so that the first figure that is cited is Figure 1.

– Figure 5, panel D: why are there two magenta curves?

– I would also suggest a careful reading to screen for typos -- I found a dozen or so, from misspelled words to mismatched parentheses.

Reviewer #3 (Recommendations for the authors):

1. Suggestions for improved or additional experiments, data or analyses:

a. The authors should provide their criteria for selecting a particular solution to compare to neural data.

b. The authors should evaluate how well their solutions predict neural data.

c. The authors need to mention that certain outward solutions have no inhibitory component (see Figure 5C, Figure 6 supplement 2). It needs to be discussed in the text and it would be very interesting to see how well these solutions recreate actual data.

d. It would be helpful for the authors to provide an example of an "unstructured" solution and an evaluation of its performance, even if it is included as a supplemental figure.

2. Recommendations for improving writing and presentation

a. Lines 89-90 – this can be better supported by adding the criteria/evaluation mentioned above.

b. Methods (~ line 483) – How is the HRC model using T5 (off) and T4 (on) motion input?

c. Lines 492-502 – What was the frame rate (timestep) for both training and testing stimuli?

d. Figures – Please increase the size when there is white space available. Make sure the pink and green color scheme for the two solution sets are very obvious.

e. Figure 1 caption – approximately half of the 200 LPLC2 are directly synaptic to the GF.

f. Figure 5 – is cross entropy loss the same as what is referred to as the loss function (equation 6) in the methods? If so, keep consistent. If not, please explain.

g. Figure 8D, it is difficult to see the boxplots.

h. Figure 10 I-L, it is difficult at first glance to realize what is neural data vs model output. Maybe label the rows instead?

i. Supplemental Figure 1. Add a schematic for the HRC model for readers who may not be familiar with it.
