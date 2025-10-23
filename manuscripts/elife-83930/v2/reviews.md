# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83930.sa0](https://doi.org/10.7554/eLife.83930.sa0)

The manuscript is a new analysis of previously published data from experiments in which rats ran on a treadmill in either fixed-time or fixed-distance trials. The valuable results provide convincing evidence to demonstrate that time and distance cells are more common in fixed-time and fixed-distance trials, respectively. These findings suggest that the hippocampus flexibly shifts between representing variables depending on their relevance.


---

# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83930.sa1](https://doi.org/10.7554/eLife.83930.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Time or distance: predictive coding of Hippocampal cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Reviewers agreed that the authors have not been precise and clear enough about what they are referring to as a predictive code and the source of its importance. That is, authors need to provide a properly-referenced definition of what is meant by predictive coding (including to what degree it is or is not distinct from flexibility of representation). Also, authors should provide a summary of why evidence for predictive coding is interesting and important (with respect to hippocampal function). Otherwise, it is not possible to assess why the described findings provide evidence for predictive coding. If the authors mean to use the term "predictive coding" in the same manner in which it has been used in prior publications, then more analysis is needed to support the claim (see individual reviews below for details). However, the main point of the paper was agreed to be the flexible representation of time vs. distance across two tasks, and this finding was viewed as interesting on its own. Therefore, if they prefer, authors can choose to remove the claims about predictive coding, rather than performing more analyses to substantiate the claims related to predictive coding.

2) Other analyses and points of clarification are suggested to strengthen the flexible representation of time vs. distance results. See individual reviews below for details.

Reviewer #1 (Recommendations for the authors):

In this manuscript the authors examine whether place cells (cells that encode specific location on an environment) or "elapsed time cells" (cells that encode total time elapsed on a track) depend on the type of task that the animal is doing. The authors show that in tasks were fixed-distance travel is important, there is a bias for distance-encoding cells and on fixed-time experiments, there is a bias for time-encoding cells. The authors conclude that this indicates that the hippocampal code has a predictive component, as it generates firing patterns that tile the relevant features of each of the tasks respectively. Overall, the analyses are well done, and the results are clear. My main concern is that even if the hippocampal code generates responses that match the most needed variable for each task, it also generates responses that match the alternative variables. For example, in the elapsed time task, there are also place cells and in the fixed-distance travel there are also cells that encode other features. This, rather than a predictive code, can be a regular sample of the environment with an overrepresentation of the more salient variable that animals need to get in order to collect rewards. In addition, the analysis provided in the manuscript are rather simple, and better controls could be provided. Improving the analytical quantification of the results is necessary to support the main claim.

– What is the relationship of each type of cell with the speed of the animal?

– What is the relationship with the n of trial that the animal has run (first 10 trials, last 10 trials)?

– What is the average firing rate of each neuron? Is there any relationship between intrinsic firing rate and the type of coding that the cell develops in each task?

– What is the relation of the units of each type with LFP features (theta phase, ripple recruitment)?

Reviewer #2 (Recommendations for the authors):

I have a couple of comments that I think should be addressed to make the manuscript stronger.

1. It is very unusual to define timing of a cell as the earliest onset of timing prior to the peak. It seems arbitrary, and also not very robust measure: it effectively uses only the earliest spikes fired by the cell on a given trial, instead of using all of the spikes. This measure should therefore be highly susceptible to noise. It's unclear why the authors didn't do something more simple and standard, such as measuring the actual peak (or center of mass) of the firing. Alternatively, they could've fit some template to the spikes and allowed this template to expand and contract to determine whether the firing is more consistent with distance or time coding. If the authors are going to stick with the method they are currently using, I suggest adding a clear justification about why it is the best method to use for distinguishing distance cells from time cells.

2. To be completely honest, I could not understand the model presented in the Discussion, in spite of multiple re-readings. I think the description suffers from being very brief and from using shortcuts in language that are hard to interpret. E.g. phrases like "connections that were active" (how can a connection be active or inactive), "connections that are consistent with time" (what does it mean for a connection to be consistent with something), "signal … coinciding with cells" (what does it mean for a signal to coincide with a cell), and "cells will gradually encode" (what exactly is changing gradually)? I suggest substantially expanding the explanation and using concrete, mechanistic language. Figure 4 that illustrates the model is visually stunning, but is also very hard to interpret and doesn't seem to contribute much to the explanation.

The best option would be to run an actual simulation that produces time or distance encoding in different situations. But I don't think this is required; a more clear explanation should be enough.

Reviewer #3 (Recommendations for the authors):

The main hypothesis test (session type independent of cell responses) is parametric and lacks a measure of strength of effect. A crude measure of strength of effect combined with a more robust hypothesis test would be provided by shuffling session type labels. Even a simple comparison of the proportion in the shuffled data gives a rough estimate of the strength of the effect.

Please motivate the classifiers and their statistical assumptions scientifically. In particular, what alternatives do they have power against, and why are these power profiles of interest scientifically. I didn't understand why you were testing for deviations from linearity to build the third classifier. Was there a motivation for that?

The abstract, for example, spends too much time replicating the Kraus paper. More time should be spent explaining why the results imply hippocampal cells encode prediction, as well as motivating why that's important or potentially important. Related to this, the reward hypothesis is not developed strongly enough.

"encoding dimensions required in order to organize relevant information." What does this mean? Perhaps simplifying it would be helpful. Does dimension mean features of sensory experience?'

I felt the final paragraph was important but not precise enough and therefore hard to parse.

The explicit structure of reward and its relationship to the main conjecture is not really discussed. This seems crucial. I'd prefer to have it upfront in the manuscript, rather than mentioning it obliquely at the beginning and coming back to it at the end.

Are we evaluating our results on the same data we are using to fit the classifiers? And does that matter?
