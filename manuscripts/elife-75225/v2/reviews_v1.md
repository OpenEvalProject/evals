# Peer review - Round 1

Editors:
- Agnese Seminara, https://ror.org/0107c5v14 University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75225.sa0](https://doi.org/10.7554/eLife.75225.sa0)

The authors present a simple model of fish swimming in a channel and reacting to the surrounding flow with their lateral line and no other sensory system. They demonstrate that the fish stably orients upstream in certain conditions. Particularly, rheotaxis can emerge even in the absence of sensory feedback, purely as a consequence of passive hydrodynamic interactions in the presence of the walls.


---

# Peer review - Round 1

Editors:
- Agnese Seminara, https://ror.org/0107c5v14 University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75225.sa1](https://doi.org/10.7554/eLife.75225.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Hydrodynamic model of fish orientation in a channel flow" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) While the attempt to compare predictions with data is clearly valuable, the data appear inconclusive and weaken the results. Please present these data as a supplementary information, de-emphasize the comparison and temper claims about biological relevance.

2) Please discuss the assumptions of the model, and in what parameter regime they are expected to hold. in particular, please provide evidence for adequacy of the dipole model; the rationale for modelling the external flow as a constant + parabolic perturbation; and the rationale for the feedback.

3) Please validate the model, for example with numerical simulations that solve the Navier Stokes equations.

4) Please include a discussion about experiments that could definitively test the hypothesis with real fish, even if you will not perform them.

Reviewer #1 (Recommendations for the authors):

The paper is missing an independent measure of function. Another line of evidence that this phenomenon is actually contributing to rheotaxis would lend strength to their argument. The strength of the theoretical work largely outweighs the support from the biological literature.

As of now, they come up with a model that matches some of what has been shown in the (inconclusive) literature. Open loop robotics is a useful suggestion and should be implemented for conclusive results. At the very least, I would have the authors suggest more concrete experiments, even if they will not do them. This shows a commitment to advancing our understanding of the actual biological phenomenon. Regarding open loop robots, and I would like to see a more detailed description of what results they would expect and how this would strengthen their argument. Likewise, a discussion on how wider flumes are expected to increase rheotaxis should be included, rather than simply mentioning that this is supported in some biological studies.

Table 1 summarizes experiments for rheotactic fish without vision, with some studies supportive and most inconclusive. I found this table marginally useful (the fault of the studies, not the authors) because these experiments have other sensory modalities intact that can generate rheotaxis. To use this to support that fish can use only their lateral line for rheotaxis is misleading, in my opinion. For the importance of a single parameter threshold to be realized, one would observe cross stream sweeping movements at higher flows for a good majority of fish swimming studies, and this is simply not the case. Literature could be better interpreted. Rheotaxis is a multi-modal behavior, so ablation of the lateral line is not sufficient to guarantee that rheotaxis can occur without it.

If improving biological experiments is the goal, then more discussion is warranted. A discussion of reafference and what flow information is incorporated in the model-acceleration, velocity, both? What do larval zfish (superficial neuromasts) behaviors tell us that are consistent (or not) with adult behaviors (canal neuromasts)?

The impact contracts in the face of what can be conclusively supported, leaving the authors to describe their work as rectifying a methodological oversight in laboratory experiments.

Reviewer #2 (Recommendations for the authors):

Please conduct a quantitative validation and sensitivity analysis of the model.

Reviewer #3 (Recommendations for the authors):

I have now read this manuscript on the stability of a fish in a channel flow. As stated in my public review, I think the assumptions of the model are not adequate for the problem studied. For this reason, I believe the manuscript is not publishable as it is. Here is a list of some comments.

- In the introduction, one aspect of fish locomotion seems to be missing: proprioception. Fish sense their surrounding also be sensing how the hydrodynamic forces and moments affect their own shape.

- The dipole model is very crude, is there any experimental evidence that this model would be appropriate to model zebrafish larvae, for instance? I believe not, because zebrafish do not swim continuously and the Reynolds number is far too small for a potential flow assumption. Besides, there is a wake behind a swimming fish that is not captured by the dipole model.

- What is the Reynolds number of the channel flows in the experiments? I believe that superposing a constant flow and a parabolic flow is not the best model for these channel flows. Usually, people use some sort of plug flow instead.

- It is strange to have a mix between a viscous flow for the channel flow and potential flow for the swimmer. What is the rationale for this mix?

- Eq. (8) describes how the potential flow rotates the dipole. I understand that you consider a sort of dumbbell model, with the dumbbell oriented perpendicular to the swimming direction. But fish are elongated in the longitudinal direction, so it seems strange.

- Eq. (9) is not a "rich nonlinear dynamics" as the author state, but simply a linear feedback with the distance from the wall. Most visual models have the same kind of feedback.

- The comparison with experimental results is presented in tables. This is not very clear and the reader is left with the impression that most comparisons are inconclusive.
