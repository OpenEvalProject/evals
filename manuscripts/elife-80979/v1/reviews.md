# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80979.sa0](https://doi.org/10.7554/eLife.80979.sa0)

This valuable manuscript proposes a neural network mechanism for range adaptation for value-based decision making. The authors present solid evidence for the proposed mechanism.


---

# Peer review - Round 1

Editors:
- Thorsten Kahnt, National Institute on Drug Abuse Intramural Research Program United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80979.sa1](https://doi.org/10.7554/eLife.80979.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Synaptic plasticity in the orbitofrontal cortex explains how risk attitude adapts to the range of risk prospects" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) As you can see in the individual comments, all reviewers thought that your paper addresses an important topic. However, a central concern raised by all reviewers was that a substantial part of the model performance is driven by the activation function – yet, throughout the manuscript, you mainly discuss the role of Hebbian plasticity and largely ignore the effects of the activation function. There was agreement among reviewers that this is not warranted and that your manuscript requires substantial reframing, clarification, justification, and discussion. Reviewers would expect an adequately revised manuscript to look quite different from the current version, with an equal focus on all factors that allow the model to account for the observed changes across different ranges.

2) There are additional comments in the individual critiques that would be important to address, specifically regarding aspects of the analysis and interpretation.

Reviewer #1 (Recommendations for the authors):

1) Please explain on page 4 of the introduction why Hebbian plasticity should lead to spill-over effects. This is not very intuitive.

2) Interpretation of the null findings in the fMRI data (page 4 of results) is problematic because it is unclear whether they reflect a true null effect or a lack of sensitivity. Although this is true for all null results, it is particularly problematic for re-analyses, as the study was not designed or powered to test this question. It would be best to remove these results from the paper.

3) There is a fundamental difference between gaussian and sigmoidal activation functions. It would be important to include an adequate discussion of the assumptions and implications of these different functions in the main text.

4) The out-of-range predictions of the best model (Figure 3, lower-right panel, HP-ANN (gauss)) are not very convincing when considering the entire EV range. Model performance should be compared for the entire EV range, not just the common range. What does this mean for the proposed mechanism?

5) The paper focuses on Hebbian plasticity as a mechanism for context effects but judging from Figure 3, the choice of activation function has a comparable effect. Indeed, HP does almost nothing for models with sigmoidal activation functions, and HP only improves the out-of-range prediction for the common EV range but does very little for the uncommon range. A more balanced presentation that also discusses the type of activation function as a mechanism of adaptation would be important.

6) Are the RSA results in Figure 4 based on the ANNs with gaussian activation function? It would be important to show RSA results for all 4 ANNs in Figure 4, so it is possible to compare the results across models. Also, please add labels to the plot axes.

7) The proportion of offer and chosen value neurons shown in Figure 6 is opposite to what has been reported in the OFC of non-human primates. It would be good to discuss this discrepancy. Also, are the same proportions found for all 4 ANNs?

8) Figure 4: the spheres shown for BA11 are in the posterior medial rather than the lateral OFC. Please double-check the anatomical location of these ROIs. Are they really in the lateral OFC? Also, it would be good to provide center coordinates for the ROIs. In general, it would be important to better describe how the ROIs were generated. What were the search terms used in NeuroQuery? Also, NeuroQuery generates meta-analytic activation maps, not maps of anatomical structures. It would be better to use actual anatomical ROIs for fMRI data analysis.

Reviewer #2 (Recommendations for the authors):

1) Range adaptation is not shown directly in ANN units. Specific questions:

a) How do ANN units respond across different input values? How variable are these response patterns across units?

b) How do these response patterns vary with range?

c) Do these patterns (at the individual unit or mean level) resemble neuronal data from the orbitofrontal cortex (OFC)? Should it be expected to?

d) The example units that are shown (Figure 7) seem potentially different from previously reported neuronal data from OFC. For example, the dynamic range of the model covers only a narrow subset of the input space and varies substantially across conditions, whereas firing rates in OFC neurons tend to span the full range of possible values, and firing rates change only slightly between conditions [ref,ref]. Is this discrepancy just a side effect of showing results in terms of loss units rather than expected value? How should we interpret this apparent discrepancy?

e) ANN unit responses are compared to neuron classes observed in OFC (Figure 6). What does the mean ANN unit in each category look like, and how does this compare to the OFC responses referenced?

2) Modeling results focus on Hebbian networks with gaussian activation functions. Specific questions:

a) Is there a physiological motivation for the model, or is this primarily for mathematical convenience?

b) Do the main qualitative results (range effect on risk sensitivity) require a non-monotonic activation function?

c) How do the properties of the response functions (saturation and (non)-monotonicity) affect responses of ANN units?

d) There are visible differences between model behavior for Hebbian networks with sigmoidal and gaussian activation functions. How should these differences be interpreted? Does this lead to any predictions or constraints on what physiological implementation is consistent with this algorithm?

3) Out-of-sample predicted choices in the Hebbian model with gaussian activation function seem unintuitive for more extreme parts of the value range. E.g. for the out-of-sample wide range predictions, the model seems to over-predict risk aversion to the point that choice probabilities saturate and ~0.6 for increasingly high-value options. For the narrow range, out-of-sample prediction behavior even appears to be non-monotonic, leading to increased acceptance of extremely high loss options.

a) How should this be interpreted?

b) Does this depend on model parameters like update rate or covariance threshold?

c) In these parts of the range, how does the Hebbian model compare to alternate models, such as the other ANNs or logistic regression?

4) The relationship between neural responses and ANN activity relies on representational similarity analysis (RSA). However, significant RDM correlations could arise as a byproduct of the fact that both ANN output and BOLD activity in select regions correlate with behavioral choice patterns. Is there evidence that the correlation between Hebbian ANNs and BOLD activation reflects more than average choice patterns?

5) The authors make the strong claim that this model is the mechanistic explanation for adaptation in orbitofrontal cortex, but there is little comparison with previous models. Divisive normalization and other forms of adaptation to the value range are discarded based on a qualitative argument from the behavioral data. However, given that the Hebbian ANNs also produce some counterintuitive behavioral predictions, it is not obvious that they are better at accounting for observed patterns in neuronal adaptation or behavior. Addressing the following questions could clarify whether there is an argument for Hebbian ANNs over alternate mechanisms of adaptation:

a) How do behavioral predictions and RSA results from HP-ANNs compare quantitatively to results from other models of adaptation, including models of adaptation at the input stage?

b) Can Hebbian ANNs account for other previously observed patterns of behavior across different value ranges, such as stability of relative values across ranges in two-option choices and range-dependent decoy effects []?

c) Are there specific predictions that arise from Hebbian networks that could be tested in later work and used to differentiate between competing models?

Reviewer #3 (Recommendations for the authors):

1) The paper assumes loss aversion as the primary behavioral factor, which is fine. However, it may be worth briefly mentioning the limitation that with the present experimental design it is impossible to dissociate loss aversion from risk aversion (see e.g. Williams et al., 2021, PNAS).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Efficient value synthesis in the orbitofrontal cortex: how does peoples' risk attitude adapts to the range of risk prospects?" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

All reviewers agreed that the revised manuscript has been improved. However, given the revised manuscript is essentially a fundamentally new manuscript, there is a new set of comments that would need to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

I appreciate the authors' effort and dedication in re-working the manuscript. The revised manuscript is a fundamentally new and improved paper with new conclusions. I believe it could make an important contribution to the field and I remain enthusiastic. However, given most of the manuscript has changed, I have new comments that I think should be addressed

1) In general, the manuscript is quite long with extensive supplementary analyses. I believe the paper could be streamlined by highlighting the most important aspects and reducing the extent to which details are discussed in the main text.

2) All relevant information to understand the plots should be embedded within the figure rather than just the figure legends. It is cumbersome for readers to constantly have to consult the legends to understand what is shown in the figure. For instance, there is no label for the different colored plots (red/back, red/blue) or line styles in ANY of the figures. Also, some legends (Figure 4) refer to a color code, but this code is not provided. Moreover, there are no axis ticks and/or axis tick labels in some of the panels in Figures 3, 5, 6, 7, 9, 10 (top row), 12 (top row), 13 (top row), S4, S5, S6, S7, S10, and S12. Several figures don't include a color bar (e.g., Figure S5-7). Please carefully revise all figures. Note that this point was already raised in the previous round of reviews, but it was not addressed.

3) Figure 3D – Loss aversion over time: Instead of running a separate between group comparisons for each time-point, it would be more appropriate to run a single two-way ANOVA with within-subject factor time and between-subject factor group. A significant group-by-time interaction would support the conclusion that loss aversion diverges between the two groups across time.

4) Why was the lateral OFC (area 47/12) not included here, given that work by Suzuki et al. 2017 suggests that lateral OFC represents attribute-specific values?

5) It is not fully clear what is plotted in Figure 5-7. Are these the averages across all RDM cells with a certain δ G/L/EV in Figures S5-S7? Does this include the δ G/L/EV = 0? How is neural coding strength defined in the lower rows? Tick labels would have helped.

6) Figure 9 shows that subject-specific ANNs correlate with subject-specific RDMs. To claim that these models capture individual patterns of OFC activity, it would be important to show that these correlations exceed those with group-level ANNs. Moreover, to claim specificity for plastic ANNs, it would be necessary to show superiority of predictions from plastic vs static ANNs.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Efficient value synthesis in the orbitofrontal cortex explains how loss aversion adapts to the ranges of gain and loss prospects" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

The authors have addressed my comments. I think the manuscript makes an interesting contribution to the field.

Reviewer #2 (Recommendations for the authors):

Overall the proposed model presents an interesting possible explanation for types of context-dependent loss aversion. The manuscript has improved over the course of revision and will be a worthwhile contribution to the literature. I have a few remaining comments that would help improve the clarity and accessibility of the results if they can be addressed before publication, but these are relatively minor.

1) While the figures have been substantially improved, several are still missing a description of the colors in the figure or legend, and instead have the placeholder phrase "(color code)" in the figure legend.

2) I appreciate your response to my previous comment about "undoing" adaptation (R2 Comment 3), but it is not clear to me in your response whether you are describing the computational role of "offer value" units in your model specifically, or just giving a hypothetical scenario. If I understand right, your model produces choice via a comparison of Vt for two options, and the"offer value" units are part of the integration layer (i.e. an input to Vt rather than the signal being compared directly). Is the idea that this would lead to stable preferences even without "undoing" adaptation downstream? Or would your model predict that preferences do shift in responses to "offer value" adaptation, and you suspect that past studies may not have been able to see it? Or are you just trying to say that there are several hypothetical possibilities, and in the specific task you are modeling it is not necessary to modify the weights? (As an aside, I also disagree with the argument that Rustichini et al. are interpreting a null result as evidence of absence – they start by predicting how preferences would change if choices arose from a simple comparison of offer value firing rates, then show that actual choice behavior does not match this prediction.)

3) In line 456 you discuss the spatial specificity of results, but unless I'm missing something this doesn't involve a direct comparison between regions. It may be worth reducing this claim.

Reviewer #3 (Recommendations for the authors):

Thank you for a responsive revision, I have no further points other than that the paper would still benefit from careful spell-checking.
