# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82426.sa0](https://doi.org/10.7554/eLife.82426.sa0)

This novel theoretical work outlines a unifying architecture for decision-making via disinhibition. The model clearly links observations across multiple empirical studies and highlights how characteristics from previous decision models can be effectively integrated into a single mechanism. This will be of interest to a wide variety of neuroscientists who work across levels of analysis.


---

# Peer review - Round 1

Editors:
- Timothy Verstynen, https://ror.org/05x2bcf33 Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82426.sa1](https://doi.org/10.7554/eLife.82426.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Flexible control of representational dynamics in a disinhibition-based model of decision making" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Alexandre Filipowicz (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Based on the combined reviews and discussions among the reviewers and review editor, the following issues should be addressed as essential revisions for moving forward.

1) Competing models: While all three reviewers agree that a network that combines both value-based and WTA dynamics is interesting and useful, there is consensus that the lack of competing or contrastive models (beyond the component models that are combined to make the LDDM) tempers the conclusions that can be taken away from the work. The LDDM should be compared with reasonable competing models and, conceptually, the authors should highlight what the LDDM adds over existing models).

2) Parameter specificity: There is a consensus in the reviews regarding questions about the necessity, specificity, and interpretation of some of the model parameters. Reviewer 3, in particular, points out potential inconsistencies in the way the disinhibition Β parameter is interpreted. Reviewer 2 highlights confusion between the necessary and specific role of Α compared to Β in some of their simulations. As both reviewers point out, an examination of the optimization surface of the fits (Reviewer 3) and/or a parameter recovery analysis (Reviewer 2) could help demonstrate the robustness and identifiability of the LDDM model parameters. This would also address Reviewer 1's concern about model complexity and overfitting.

3) Conceptual framing: The reviews point out that the conceptual framing of the goals shifts across the different sections of the manuscript. The authors should be clear about the high-level framing (Reviewer 1), whether it's about the integration of two decision frameworks or the role of disinhibition). The author should also clarify the precise interpretation of the key aspects of the model that explain its behavior (Reviewers 1 and 3). Finally, the authors should more extensively link their model in the context of prior work (Reviewers 1 and 3)

Reviewer #1 (Recommendations for the authors):

1. I recommend the authors take time to more explicitly clarify the goal of the study. What is the singular take-home message that the reader should take away from this? This singular message should be tempered enough so as not to overstate this as the first unification of value normalization and response selection, but more specific to what is being tested.

2. I recommend adding a discussion on known disinhibition circuits like the cortical-basal ganglia loops and showing how the LDDM links to prior models of these networks.

3. I would recommend finding a non-DNM and non-RNM control model to compare the LDDM against.

4. I recommend using model fit metrics to evaluate how well the LDDM (and a control model) explain the neurophysiological data.

Reviewer #3 (Recommendations for the authors):

1) I think the authors will have to rewrite parts of the manuscript to address the concerns I raise – (i) especially to clarify the precise interpretation of the single key parameter that determines the behavior of the model, and (ii) point out the connection to previous work (Machens et al. 2005, Yang et al., 2016, Litwin-Kumar et al. 2016) emphasizing the specific ways in which their work is an advance on these previous studies.

2) It would also greatly help if the usage of notation is made consistent throughout the paper. For instance, in the figures and the equations in the main text (Equations 1-3), disinhibition is denoted as D, but in the methods (Equations 5-8) and the supplementary figures (Figure 2, Supplementary Figure 1) it is denoted as 'I'.

3) I appreciate that the authors also studied a more general and 'extended' version of their model (of which the LDDM is a special case) and explore how it behaves in different regions of parameter space (Figure 2, Supplementary Figure 1). However, I found the general description of their extended model quite confusing, particularly, some of the design choices. For instance, the extended model consists of additional excitatory units (E) that are referred to as 'gain control boost loops'. These are never mentioned in the main text and their purpose for the overall story of the paper seems somewhat unclear to me. Since the R units already have projections to both 'local' and 'lateral' gain units (through 'omega', Figure 2A), couldn't the E units simply be replaced by stronger self-recurrence on the R units?

4) The most interesting analyses in the paper are where the authors fit the circuit model to neurophysiological data. The authors then report the values of the fitted parameters and also perform the model comparisons by reporting AIC/likelihood ratios. However, if possible, it would be very informative to also visualize the optimization surface of these fits to understand whether some of the free parameters trade-offs against one another, as I think that would affect the overall conclusions drawn in the paper, and also convince me about the robustness of the fitted parameters.

5) A somewhat more open-ended question is about the choice of the time constants for the 3 types of units in the model (R, G, and D), which appear to be fixed to a value of 100ms for all the results presented in the manuscript. Can the authors justify this choice? Considering that SST (which, I presume are the gain control units G) and VIP neurons have fundamentally different conductance profiles and are known to show an entire range of spiking patterns (Tremblay et al., 2016), is it justifiable to assume that their time constants all have the same value?

6) In general, the presentation of the figures can be improved:

a) In Figure 2—figure supplement 1, I should be replaced by D. Also, the parameter γ seems to be missing from the rows in subpanel B of this figure.

b) In Figure 5, it's hard to follow which subpanels are the 'main' subpanels and which ones are the insets.

c) The legend of Figure 4B (right column) seems to have an extra set of dots (ones that indicate the legend of V_in)
