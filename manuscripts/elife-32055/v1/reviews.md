# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32055.020](https://doi.org/10.7554/eLife.32055.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Adaptive coding for dynamic sensory inference" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript proposes a modeling framework to unify efficient coding of sensory stimuli with Bayesian inference of a latent, behaviorally-relevant variable (e.g. an environmental state that generates the sensory stimulus). The main idea is to replace the traditional objective for efficient coding – quality of the sensory stimulus reconstruction – with an "inference cost", namely the discrepancy between the estimate of the latent state based on the neural code and the estimate of the Bayesian ideal observer. Optimizing for these two objectives, under the constraint of limited metabolic resources, gives qualitatively different results. In particular, optimizing for inference cost produces encoding schemes that are less metabolically expensive and more accurate (with respect to the latent state).

Overall, the reviewers found this to be a very nice contribution towards a unifying framework for these ideas. The manuscript states clearly and accurately addresses this research question. The figures are well laid-out, visually appealing, and informative.

However, several revisions are requested to 1) show a relation to biological data, 2) demonstrate the generality of the results, 3) more clearly state what areas of the brain this work applies to, and 4) improve clarity of the presentation by reducing the overall length of the article.

Essential revisions:

1) The work should include more explicit relation to biological data, both published results and the authors' predictions from their work on what one might expect to see in data. Please provide some examples that link predictions of the proposed framework to published data.

Example: when discussing metamers, the authors state that "stimuli become less distinguishable to the observer as its model of the environment becomes more accurate". How does this relate to the empirical observation that visual metamers are predominant in the periphery of the visual field where resolution is low and presumably the model less accurate, but can be resolved by foveal inspection where resolution is higher and the model more accurate?

Another example: could the predictions of Figure 6 and the final paragraph of subsection “Limited gain and temporal acuity” be related to data on the stimulus-dependence of adaptation in the visual cortex?

2) The manuscript needs to address the generality of these results. A very simple stimulus model with switching between two states was used; how do these results extend to more complex stimuli? Does the work here predict that these results are general and, if so, for which stimulus conditions? Substantive text revisions and additional computational results will be needed to satisfy this point.

The authors discuss the dynamical signatures that distinguish the three encoding schemes (Figure 9). To make a higher impact, they should also provide or suggest examples from biology where one of the three schemes may be more or less likely. Where would one expect to see mean vs variance changing environments? What would one have to measure to observe the dynamical signatures in Figure 9? Can the authors make some predictions/hypotheses about this?

In addition, in the context of the experimental system where the three schemes might apply, how likely is it that one would be able to distinguish between each scheme? In the panels in Figure 9, some of the differences between the different schemes are very small so they might not be measurable with great precision in specific experiments.

In particular, the reviewers noted that actual sensory stimuli are high-dimensional, and behaviorally-relevant latent states (and behavioral output itself) are low-dimensional. The fact that the code optimized for inference leads to better accuracy and efficiency, compared to the code optimized for reconstruction, is true for the latent variable that has been deemed behaviorally relevant, but the result would probably be different in a more realistic generative model in which there are also other latent variables that jointly generate high-d stimuli. Also, as we know from natural image and sound statistics, stimulus distributions are not well described by Gaussians or even mixtures of Gaussians. Related to this, the definition of inference cost as the expected squared error makes sense if assuming Gaussian posteriors, but perhaps the authors should use something more general to encompass a broader range of cases, like D_KL (understanding that's effectively what the authors have done for the Gaussian case).

In the Discussion, the authors claim they have "addressed the issues of both tractability and non-stationarity…", but it is not clear if this is because of the simplifying assumptions that were made for the generative model of stimuli and for the inference cost.

3) It was not clear to the reviewers if this is a theory that applies to the sensory periphery, to the cortex, or to both. The resource limitations considered here make sense if the dimensionality of the stimulus x and neural code y are the same. That would seem to be appropriate for a theory of the periphery, but then optimizing a peripheral code in complex ways for behavioral outputs may be implausible. Conversely, if this applies to cortex, we know dim(y)>>dim(x) and the choice of resource limitations might not be as relevant in practice: e.g. wouldn't a large enough population code overcome the problem of discrete response levels? It has been argued that in cortex the major challenge is the computational complexity of the inferences that need to be performed (Beck et al., 'not noisy just wrong'), and that approximate inference may be more a important constraint than resource limitations.

4) The paper would benefit from some streamlining to reduce the number of figures and the overall length of the paper. Repetitive text should be condensed or eliminated (example: Results section, fourth paragraph is a repeat of earlier statements). Overall, the Introduction could be significantly condensed. It is suggested that Box 1 be moved to the Materials and methods section, because there is significant overlap with it and Figure 1. The figures could be streamlined to some extent, perhaps a few could be combined to reduce the total figure count. At times that the manuscript was hard to read, as long paragraphs are spent describing the mechanics of the effects (which are instead very clearly illustrated in the figures). The authors should consider shortening those descriptions.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Adaptive coding for dynamic sensory inference" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and two reviewers.

Thank you for your extensive and substantive revision of your paper. The manuscript has been improved, and reviewers were largely satisfied with your changes, but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) On the question of resource limitations, the reviewers agree that your argument re: sparse coding is valid, but it does raise questions about noise robustness (connected to point 2 below) and cell death, which might both argue for distributed/redundant coding. Perhaps discussing/citing Deneve's recent work on degenerate population codes is appropriate here. Please add some text to the discussion that addresses this.

2) Regarding adding noise to your model: Please include a discussion of the impact of noise on the structure of neural coding along with your text clearly stating that you have left the work of a thorough exploration of these topics for another study. Relevant literature to discuss/cite are, e.g. Zohary et al., 1994; Abbott Dayan, 1999; Sompolinsky et al., 2001; Ma et al., 2006; Moreno-Bote et al., 2014; a review article by Kohn et al., 2016; as well as Gjorgjieva et al. bioRxiv 2017 (currently cited in the wrong place – should be moved to the discussion of the first framework). Please add some text to the Discussion that addresses this. If possible, the reviewers urge the authors to include one example of the effects of noise (a simple additive Gaussian or Poisson noise source) on their model results.

Points 1 and 2 are connected and that should also be made clear in the added Discussion text.

3) Please address in the Discussion how your results might be thought of in the context of dynamic environments that are stationary – i.e. the stimulus changes in time, and might *also* switch states, but any given state fluctuates.
