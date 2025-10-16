# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75007.sa0](https://doi.org/10.7554/eLife.75007.sa0)

This work presents fundamental findings elucidating the debate on how value-based choice behavior is influenced by seemingly irrelevant options (distractors). With convincing behavioral evidence following non-invasive brain stimulation, the authors provide support for the role of medial intraparietal cortex in divisive normalization in decision making. Given the importance of context effects as suboptimal violations of normative choice theories, this finding is significant and broadly relevant to psychologists, neuroscientists, and economists interested in decision making.


---

# Peer review - Round 1

Editors:
- Taraz Lee, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75007.sa1](https://doi.org/10.7554/eLife.75007.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Intraparietal stimulation disrupts negative distractor effects in human multi-alternative decision-making" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) There was some concern about the lack of robustness of the TMS results and running an ANOVA on the betas from subject specific GLMs given that this ignores the estimated variance of the betas. In the follow up ANOVAs the standard errors from the individual GLMs are discarded, potentially impacting the results. In consultation the reviewers suggested potentially running a giant regression (all the data) with subject-specific effects for HV+LV and HV-LV and then a group level interaction on D-HV (including the site*location*TMS interactions). This would allow a simple t-test on the 3-way coefficient. This would essentially be a group-level GLM without subject-specific coefficients (this essentially averages over all subjects) and cluster standard errors at the subject level.

2) There is a strong assumption in the analyses that subjects make choices with perfect calculations of expected value (linear utility). However, it is well-known that people vary quite a bit from optimal EV calculations and have different risk preferences and biases that drive decisions. The authors need to show that their results hold with non-linear utility functions and/or individualized utility functions for each subject if possible.

3) There were several concerns about the interpretation of the results, justification of analysis choices, and potential limitations of the study given the design that need to be addressed (see reviews below).

Reviewer #1 (Recommendations for the authors):

This paper from Kohl and colleagues examines the biological basis of context-dependent decision-making, in which the preference for given options depends on factors beyond their intrinsic values. They authors target a specific form of context effect in trinary choice where unchosen options nevertheless shift the relative preference between the remaining two alternatives, a violation of traditional, normative theories of choice behavior. The existence and nature of these effects have been a recent topic of debate: some studies report negative effects (where distractors decrease choice accuracy in a value-dependent manner), some report positive effects (distractors increase accuracy), and some report no effect at all. Recent work from this same group showed that these disparate results can be reconciled if choosers exhibit both forms of context-dependence (in different regions of decision space defined by choice difficulty), proposing a composite model where prefrontal and parietal cortices mediated positive and negative effects, respectively.

Here, the authors present data replicating the coexistence of positive and negative distractor effects and, furthermore, show causal evidence for the role of intraparietal cortex – disrupting the medial intraparietal cortex (MIP) with transcranial magnetic stimulation selectively reduces negative distractor effects, with the degree of disruption correlating (negatively) with the size of MIP. The paper is clearly written and the results together support both the idea of a composite model, providing one of the only causal manipulations of such context effects. Overall the experimental approach is well reasoned and the results important, though there are some subtleties of analysis the authors should address, including the definition of regressors, the potential impact of nonlinear subjective values, and the interpretability/relevance of phantom decoy effects.

1) Definition and justification for regressors. The choice of regressor terms to test context-dependence could be better explained here, even if they follow past publications. Why is distracter value formalized as D-HV rather than D (e.g. in the interaction term (HV-LV)(D-HV))? Is there a particular reason to use D-HV instead of D, D-LV, or some other construct? And given this formalization, why do the authors use D in the interaction (HV+LV)D when testing the prediction of normalization (pg. 10).

2) Assumption of expected value choosers (linear utility). Given the crucial role of choice accuracy in the analyses, it is a bit concerning that correct choices are defined only by expected value calculations given the common finding of empirical risk preferences. The main question is whether any of the results would change if the choosers were in fact not expected value (risk neutral) choosers and choice performance was misspecified. The authors could reasonably argue that subjects are likely close to risk neutral given the small stakes, but given the central role of accuracy in the analyses, it is an important point to quantitatively establish. For example, the authors could either: (A) quantify a nonlinear utility function for individual subjects (either using effective binary trials where D=0, if they exist; or aggregating across all choices at all D values), or (B) show that the main results still hold assuming a reasonable range of nonlinear utility functions and redefined accuracy values.

3) Practical relevance. The task design using the ultimately unchoosable distractor is clever, allowing the examination of distractor effects in otherwise untestable scenarios (when D is high value and would be chosen over both HV and LV options). One issue is that the nature of the task – involving a mid-trial shift in choosable options – may elicit different internal dynamics and choices than a simple choice. In this regard, a more natural way to elicit distractor effects is a rank ordering approach (as in Dumbalska et al., 2020, PNAS); I certainly don't expect the authors to revise their task, but a discussion of the possible limitations would help. Aside from the unnatural dynamics, the use of the phantom decoy means that distractor effects are examined in many cases when they would not naturally occur (i.e. when the distractor would be selected). Do the main effects (dual distractor effects, MIP role in negative effects, morphometry results) still hold if the authors only include trials where D is lower than the LV and HV?

4) Support for Figure 3D (accuracy as function of D-HV in MIP TMS condition). The figure legend states that this panel supports an increase in accuracy with increasing distractor value, but the support for this statement isn't clear. From the graph, the trend in the MIP Contra condition is only mildly more evident that the other conditions, visually; more importantly, the main text does not present a quantitative analysis of a dependence on D-HV (e.g. regression) – it only presents the results of ANOVAs. Is there additional analysis that the authors meant to present?

5) Robustness of TMS effects. One statistical concern for the paper is that the primary TMS results are supported by effects with relatively marginal significance: three way interaction for D-HV p = 0.044, contralateral site x stimulation ANOVA p = 0.034, contralateral MIP stimulation ANOVA p = 0.049. This limitation is evident to the authors, as they avoid the additional splitting of data by difficulty and acknowledge the power issues. One finding in the authors' favor is that the effect is stronger with the inclusion of MIP size as a covariate. There is not much that we as reviewers can reasonably ask at this point, but perhaps a acknowledgement of this issue and a discussion of potential reasons and future plans to address it would be helpful.

Reviewer #2 (Recommendations for the authors):

This paper addresses a current debate on whether (and how) value-based choice behaviour is influenced by seemingly irrelevant options (distractors). Previous work has proposed an influence of distractor value on accuracy arising from a divisive normalization computation, which acts as a form of gain normalization on neural activity. There is evidence for such a computation in the lateral intra-parietal region of non-human primates.

The view being advanced by the paper is two-fold. First, that the effects of DN (a reduction in choice accuracy) should be most prominent when the magnitudes (sum) of options are low and decisions are difficult. And second, that this DN process takes place in parietal regions, and is competitive with some other process (perhaps in vmPFC) which induces positive distractor effect (increased accuracy).

The paper reports results from new experiments (of a previously studied-design) that assess the causal role of the medial intra-parietal area (MIP) on choice via TMS. The authors report that disruption of MIP increases choice accuracy. This effect is interpreted as disruption of the DN effect on choice. The experimental design is appropriate and the experiment and analysis are well-executed.

My main concerns with the paper are on the interpretation of the results and how they relate to the underlying theory being proposed. These concerns are essentially expositional. I would suggest a revision to address them.

1) The paper ascribes a negative distractor effect to DN, and a positive distractor effect to some other process (perhaps mutual inhibition). It is important to clarify what DN model the paper is considering, and what its predictions are. The theoretical statements on pg 6 lines 97-107 seem to be describing the model presented by Louie et al. in which the normalization term contains the non-weighted sum, but is not clear on the noise assumption. It is important to note a few issues here.

– The form of DN considered in Louie et al., 2013 is highly simplified. The perception literature suggests a number of more complicated functional forms with parameters (or perhaps even computations) that are tuned to the task. It would be VERY surprising if a choice process in cortex used a DN computation in which all weights and rectification parameters were set to 1. This is important, because statements about the role of the distractor in altering choice accuracy depend on this.

– DN can induce a positive distractor effect in some regions of decoy space. This is reported in the original Louie et al. paper, and is due to the Gaussian noise assumption (see Webb et al., 2020a, Figure 5 and Proposition 3).

– More broadly, where DN effects are strongest (as a function of option differences and magnitudes) also depends on the form of DN considered and the noise assumption. The paper is not very precise on the conditions required for the statements on pg 6 to be true. They can be verified analytically for a general form of DN and the Gumbel error. But a more general statement is difficult. Have the authors demonstrated this theoretical statement previously?

pg 6 lines 104-107. Whether positive distractor effects should dominate (depending on decision difficulty) also depends on a few factors. What is verifiable is that, under some assumptions, the influence of DN on choice ratios is smallest when the choice is easy (see above). Whether this leads to a positive distractor effect depends on the other unspecified process (like a MI model) and its relative influence. But this is not a prediction of DN, as implied in line 97, rather it is a prediction of the dual-route theory.

pg11 lines 201-202. It is not clear to me why the effect “reverses” since the main effect is not significant. Perhaps it is “pronounced” or “apparent” on difficult trials?

Figure 3D is a bit hard to interpret. Why is the data binned in to 4 bins? And not just a continuous regression reported? I suspect the figure is trying to demonstrate a positive trend as a function of D, but no statistical tests are run on these bins (and none seem significant). Perhaps the fitted values from the GLM could be generated as a function of D instead?

lines 394-395: What is the increase in gaze shifts between D and HV relative to? gaze shifts between D and LV? HV and LV?

pg 30 lines 540: It is not clear how these results are evidence for a causal relationship between mPFC and a positive distractor effect. Couldn’t the lesion of vmPFC just be creating substantial noise in the valuations, regardless of whether a negative distractor effect is operating. It seems odd to call this a “reduced positive distractor effect”. This matters for the discussion of the causal effect of vmPFC TMS below on pg 31. Assigning this effect to a relatively "stronger influence of DN" wouldn't be accurate, as it could simply reflect an increase in noise.

There is a limitation when using choice data alone to argue that TMS reduces normalization at the expense of some other process which has a positive distractor effect. Perhaps TMS alters the DN computation (i.e. its weights) in a way that induces a positive effect?

More broadly, the paper is not clear on how the dual-route theory operates. Is it an either/or process, so that when intra-parietal regions are TMS’d they are essentially “deactivated” and the decision is guided solely by vmPFC? If so, what process determines which “route” yields the decision in the control conditions? It would seem strange for this switching process to use value (i.e. difficulty) as the switching condition given that value is seemingly what is being constructed/determined. Or is the value process sequential, so that output from vmPFC feeds into parietal regions? If so, wouldn’t the TMS just be adding noise to the valuation process, reducing accuracy?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Intraparietal stimulation disrupts negative distractor effects in human multi-alternative decision-making" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Please address the outstanding concerns of Reviewer 2 (see below).

Reviewer #2 (Recommendations for the authors):

Overall the authors have responded sufficiently to previous comments, however, there is one issue that remains. I am not convinced by the new mixed-effects analysis in Figure 3-supplemental 1 that is intended to bolster the original ANOVA analysis of the TMS results because it is impossible to assess the new results.

The authors don't report the estimated coefficients in a table (only the coefficients and p-values for the variables of interest in Figure 3) and allude to a better fitting model when they include specific (un-reported) co-variates but don't appear to report this metric. This is non-standard when reporting structural model fits of choice behaviour and problematic because including RT in this regression where choice is the outcome variable is subject to a (likely high) endogeneity problem (it is correlated with the error term in the regression) therefore the other coefficients are likely biased (see discussion in Webb (2019) and Chiong et al., (forthcoming)). Without seeing the model results that don't include RT, it is impossible to assess which direction the bias goes. Please report all coefficients in these regressions, as well as the results for the model without RT as a regressor. If the authors want to include RT in the empirical analysis, they need to address the endogeneity problem by either estimating a dynamic model (like they propose with their race model, or finding a valid instrument using a control function approach).

Webb, R. The (Neural) Dynamics of Stochastic Choice. Management Science.i 65, 230-255 (2019).

Chiong, Shum, Webb, Chen. Combining Choice and Response Time Data: A Drift-Diffusion Model of Mobile Advertisements. Management Science. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3289386
