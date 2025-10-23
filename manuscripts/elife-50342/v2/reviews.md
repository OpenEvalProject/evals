# Peer review - Round 1

Editors:
- Uri Alon, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50342.sa1](https://doi.org/10.7554/eLife.50342.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Accuracy and robustness of biological signaling is an important concept in systems biology that has received significant attention over the years. In this manuscript, the authors present a novel receptor-based mechanism that is sufficient for cells to compute relative changes of growth-factor concentrations in the extracellular milieu (providing approximate fold change detection or FCD). Experimentally, the authors observe increasing pAKT signaling responses that is concomitant with depletion of surface-exposed EGF receptors in cells exposed to increasing concentrations of EGF. Using ODEs coupled with an elegant analytical model and validation experiments, the authors show that surface receptor downregulation is not only a desensitization mechanism, but also a molecular “reference point” as part of a mechanism that compares background concentrations with future stimuli. Receptor-level relative-sensing imbues cells with a sort of molecular memory that can be used to overcome noisy biological conditions independent of transcription.

Decision letter after peer review:

Thank you for submitting your article "Receptor-based mechanism of relative sensing and cell memory in mammalian signaling networks" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Robin E.C. Lee (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Accuracy and robustness of biological signaling is an important concept in systems biology that has received significant attention over the years. In this manuscript, the authors present a novel receptor-based mechanism that is sufficient for cells to compute relative changes of growth-factor concentrations in the extracellular milieu (fold change detection of FCD). Experimentally, the authors observe increasing pAKT signaling responses that is concomitant with depletion of surface-exposed EGF receptors in cells exposed to increasing concentrations of EGF. Using ODEs coupled with an elegant analytical model and validation experiments, the authors show that surface receptor downregulation is not a desensitization mechanism, but a molecular “reference point” as part of a mechanism that compares background concentrations with future stimuli. Receptor-level relative-sensing imbues cells with a sort of molecular memory that can be used to overcome noisy biological conditions independent of transcription.

Overall, the work is comprehensive and highlights an important emergent property that arises through receptor endocytosis, a property that may recur in other molecular pathways. Although there is still room for improvements, a suitably revised manuscript would certainly be of interest to a broad biological readership and should be published at eLife.

Essential revisions:

1) Review of previous literature:

1a) The Introduction should include a detailed (2-3 paragraph) discussion of fold change detection and its known mechanisms. The present model has approximate (not exact) FCD, and this should be noted.

1b) EGF signaling is one of the better studied signal transduction processes, and multiple observation related to its many facets have been made before. In particular, it has been noted that EGF receptor indeed responds to the EGF dose logarithmically (see e.g., a number of studies from Steve Wiley). These studies are not discussed in the current manuscript, which is quite surprising. The interpretation provided by Wiley and others is that this logarithmic relationship is a consequence of receptors having high and low affinity binding sites, so that the binding of the ligand and the ensuing response depend on a mixture of these binding sites occupied. Needless to say, there is ample literature to support these findings and this model.

We note that a logarithmic dose response is not equivalent to FCD (since FCD is a dynamic property), and thus the present work is novel for the EDF system.

2) The analytical modeling is a strong point of this paper, it has a remarkable ability to reproduce experimental findings and explains the range of molecular conditions that support relative sensing. This model should have more page space in the main text. Specifically, the motivation for the analytical modeling can be developed more, the dimensionless parameters α and β can be defined in the main text (they are already summarised indirectly). Figure 7—figure supplement 1 presents important results that can be combined with Figure 4 and discussed in accompanying text.

3) All three reviewers suggested additional experiments as described below. I suggest that the authors add any data they have or can produce in under two months. For experiment where this is not available/possible, I suggest deferring the experiments to future work.

Basically, there is an analysis of wild type cells and an ODE model. The experimental analysis lacks any perturbations to the pathway to really test the ODE model in any particular way. The model analysis lacks distillation to any particular core component or network motif that could be interpreted in a more general manner. One possible experiment to do is overexpression of EGFR, which should keep the cells more sensitive to changes in EGF concentration despite pre-exposure to EGF. An inhibition or knock-down of EGFR should have the opposite effect. Perturbations timed with the fold increase in ligand would have a greater impact. Another experiment would be to pre-expose the cells to EGF for 3 hours, replace with EGF-free media, and measure the rate at which the cell's EGF sensitivity reverts back to baseline levels. According to the authors' model, we should expect to see the EGF sensitivity correlate with the rate at which EGFR is translocated to the cell surface minus the rate at which EGFR is internalized and degraded.

Related to the above, there are multiple pharmacological and genetic methods to perturb receptor trafficking, including its severe inhibition. One needs to test the effects of these perturbations in the overall signaling but also on the specific model predictions, and their validation. The activation of receptor itself upstream of Akt can also be directly tested, e.g., by detecting its phosphorylation status. A better idea of what the pre-stimulation with EGF can do to the cells, including altering the synthesis and degradation rates of the molecules involved in the analysis, and cell behavior (migration, morphology, etc.) should be provided.

The authors emphasize that the proposed relative sensing mechanism is non-transcriptional, but do not provide evidence for this claim. Although the models and experiments demonstrate sufficiency, they don't demonstrate necessity of a receptor-only mechanism in the axis of EGF/HGF-pAKT-FoxO3 signaling. Note that the timescales mentioned in the Introduction overlap with transcriptional timescales (for example, cytokine-induced transcription can be rapid with strong expression that peaks within 30 minutes – see IL-6 response in PMID: 16191192). I have 2 constructive suggestions: The first would demonstrate necessity by adding additional inhibitor studies: (i) poisoning transcription/translation to demonstrate relative sensing for pAKT/FoxO3 is unaltered; and (ii) inhibiting receptor internalization (MDC, dynasore, etc…) and demonstrating predictable loss of relative sensing (using the model to make predictions). The second suggestion is that the authors can dilute the “non-transcriptional” claims and acknowledge through discussion that transcriptional mechanisms may still supplement the observed non-transcriptional receptor-based mechanism (and explain how future experiments can rule them out).
