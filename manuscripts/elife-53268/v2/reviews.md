# Peer review - Round 1

Editors:
- Brice Bathellier, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53268.sa1](https://doi.org/10.7554/eLife.53268.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study shows that auditory cortex dynamics can be decomposed into a small set of critical dimensions and a set of dimensions that rather account for small variations of the dynamics. In addition, remarkably, critical dimensions are not shared between spontaneous and evoked activity, suggesting that the two types of activity come from different processes. This is an exciting result that should motivate important refinements in current models of auditory cortex dynamics.

Decision letter after peer review:

Thank you for submitting your article "Cortical state transitions and stimulus response evolve along stiff and sloppy parameter dimensions, respectively" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Matthias H. Hennig (Reviewer #2); Mark D Humphries (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper uses model-based analysis of extracellular recordings from the rat auditory cortex to provide evidence for the hypothesis that the stability of the population in cortical networks depends on a small number of neurons with highly sensitive parameters, while parameters associated with the majority of neurons are insensitive to changes. Moreover, the authors show that transitions between desynchronised and synchronised states are associated with changes in the sensitive parameters, while during sensory stimulation this is state-dependent. Finally, it is shown that neurons with sensitive parameters have hub-like properties in the network.

Overall these are very interesting and in fact surprising results. The paper is well written and presented, but a few complementary analyses/clarifications are needed to make the important but complex message of this study more accessible and convincing.

Essential revisions:

1) The central conclusions in this paper are based on analysis of the Fisher information matrix (FIM) for pairwise maximum entropy models fit to binarised multi-neuron patterns. One possible caveat here is that the models were fit on relatively small data sets, which could affect the analysis downstream as the insensitive directions in the FIM could just reflect poor parameter estimates. The around 5000 patterns used here to fit the model are very few, and estimates of correlations used to constrain the model may be poor, given cortical activity is quite sparse. Possible biases should be assessed more thoroughly. In particular it is important to check for the impact of estimation errors given the short epochs. One key measure to check is the sensitivity measure, as this defines both core results (spontaneous = stiff; evoked = sloppy). The authors should provide an estimate of the variation in "sensitivity" as a function of model estimation error.

Most importantly:

– Figure 5E-G, check for how correlations between sensitivity and "state" change with errors in model estimation.

– Figure 6D-E, check for how correlations between sensitivity and the modulation index change with errors in model estimation.

2) It is hard to follow what is 'stiff' and what is 'sloppy', as in most of the cases the frontier between the two categories is obviously not sharp. It is clear that there are two ends of the parameter distribution (one end is more stiff and the other more sloppy), but in between, there are many intermediates. The authors must be more explicit about this and make more precise wherever possible what they mean when they define these two categories.

– In Figure 4B they should display the boundary between stiff and sloppy with a shading or a vertical line. Also, there is a kink in the eigenvalue curve. Is it related to model/population size? Are the eigenvalues beyond this kink relevant?

– It should be explained why stiffness of individual neurons is chosen to be their contribution to the first eigenvalue only. Are further eigenvalues not relevant?

– Together it should be clarified in a dedicated paragraph that stiff and sloppy parameters/neurons are two parts of a wide distribution.
