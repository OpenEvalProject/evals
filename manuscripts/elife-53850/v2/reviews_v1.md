# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53850.sa1](https://doi.org/10.7554/eLife.53850.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents a re-analysis of previous data as well as new data on the effects of distractors on value-based choices. It is an ongoing debate in the field whether such effects exist and what form they take. The current results convincingly show that across multiple experiments, distractors both improve and impair choice accuracy, depending on the difficulty of the decision. Moreover, these effects are reproduced by a dual-route model that combines divisive normalization and mutual inhibition.

Decision letter after peer review:

Thank you for submitting your article "Consistent patterns of distractor effects during decision making" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rani Moran (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the current study, the authors show robust distractor effects both improving and impairing accuracy in different "parts" of the decision space, despite previous reports (Gluth et al.) that these effects do not exist in some of the datasets (analyzed here). The authors present a "dual-route" model that explains the co-existence of these effects and they relate the facilitation and impairment effects to distractor salience and value respectively.

All reviewers agreed that this research is important, informative and of interest for a broad readership. Reviewers also identified a number of issues which need to be addressed before the paper can be accepted for publication. Most importantly, it would be critical to determine why exactly the authors come to such vastly different conclusions than Gluth et al., when analyzing the same data.

Essential revisions:

1) The paper is extremely long and detailed. The reviewers agreed that it would be good to edit it by delegating non-essential material to the supplement. For example, the sections "distractor effect are not driven by artefacts" and "A more complete analysis of distractor effects" could simply be referenced from the main text but detailed in Supplementary Information. Additionally, the manuscript contains substantial redundancy which could be streamlined.

2) The current paper directly contrasts with the results of Gluth, 2018, whose datasets comprise a portion of the results presented. Critically, both Gluth and the current authors examine identical datasets (Chau, 2014 and Gluth, 2018 Experiment 4) but come to different conclusions about the existence of distracter effects. While the authors in places do offer suggestions about why the conclusions are different, they provide no definite answers. It would be important to do more to address this directly. A simple explanation might be that two opposing effects exist in the data, that these on average can cancel out (given specific HV-LV conditions) – therefore the focus on the interaction term between (HV-LV)(D-HV). However, in the same dataset (Gluth, 2018 Experiment 4), Gluth sees no positive distractor effect (in fact he finds the opposite) and no interaction effect; the authors see both. Barring error, this means the authors are running different analyses and the critical question is what exactly is different?

2.1) Gluth et al., make a very specific technical point about the importance of centering or standardizing HV-LV and D-HV before computing the interaction term; without doing so, the interaction term can be highly correlated with one or both of the main predictor variables. Are predictors centered here prior to calculating interaction terms? Subsection “Distractor effects are not driven by statistical artefact” suggests so, but it is unclear what "normalization" means. Despite the statement in subsection “Distractor effects are not driven by statistical artefact”, there is no mention in the Materials and methods section of (1) whether there is centering before interaction terms are calculated, or (2) if so, in which GLMs. The authors should be explicit here.

2.2) The original analyses in Chau, 2014 and Gluth, 2018 included LV+HV as a covariate in the main analyses, which is not the case here for GLM1 which documents the main finding. Was this excluded for a specific reason, and what are the results if it is included? HV+LV *is* included in the stepwise regression in GLM2, but that is not a straightforward comparison.

2.3) The authors suggest (subsection “Both divisive normalization of value and positive distractor effects co-exist in data sets from three sites”) that including two-choice trials (with a nominal D value of zero) may have biased previous results. This sounds plausible but is speculative. It would help if the authors re-ran their analyses with these trials included. A different result would not only back up their assertion but would provide a more definite explanation for the reported differences in findings.

3) Given the reliance on regression measures throughout the paper, reviewers were concerned about whether there are potential multicollinearity issues, particularly because the predictor variables HV-LV and D-HV may be related (due to task design), and due to interaction terms. Illustrations in Figure 9 suggest that some of the GLMs feature strong correlations.

3.1) Please state whether or not the task design orthogonalized HV, LV, and D.

3.2) Please report multicollinearity measures (e.g. variance inflation factors) for the different regression models. This is a concern for all the models, but in particular GLM5 which has many regressors with related terms.

4) In analyzing Experiment 7, it would be important to investigate interactions with D or |D| (e.g., D*(HV-LV), |D|*(HV-LV)) as such interactions play a critical role in studying distractor effects in the rest of the paper. Additionally, it would be highly informative to present panels as in Figure 1 for this experiment and separately for the reward/loss conditions. Do the patterns look different for gains and losses? And can the dual route model account for separate effects of value and salience? Relatedly, how do the authors think negative values are handled in the normalization model?

5) There is now some history between the authors and Gluth et al. This shows in multiple places in the paper. For the sake of de-escalation, the authors are encouraged to tone down their language. Specific examples include (but are not limited to) the subsection “Both divisive normalization of value and positive distractor effects co-exist in data sets from three sites”.

6) In many places, statistical interactions are not interpreted using "simple effects". When an interaction (e.g., X*Y) is significant it is unclear whether the main effects (e.g. of X) is meaningful or whether the simple effects change sign depending on the other variable (e.g., Y). It would be important to conduct follow-up simple effect analyses. Some of the analyses even contain triple interactions. If these are not interpreted it is difficult to understand what the patterns of results mean.

7) The dual route model is attractive as a simple conceptual mechanism for a combination of effects, but there were some questions about the precise implementation, model comparison, and whether the models can account for RT data:

7.1) As reported in Chau, 2014, distracter input to the mutual inhibition only occurs for a brief period of time (before it is indicated as unchoosable); is the same format used for the divisive normalization model?

7.2) How were relevant model parameters (d and σ) determined in the dual model? It appears that for individual mutual inhibition and normalization models, they were chosen to give 85% correct choices. Is the same thing true for all 4 parameters in the dual model?

7.3) It would be more informative to show model predictions based on parameters that were derived from model fits vis a vis empirical data (and show qualitative aspects that the dual route model fits better than the other models) as these parameters are more relevant.

7.4) The authors suggest that the ability of the model to generate both effects is due to the relative speed of each model component in different value conditions. While intuitive, it would be helpful if the authors actually showed this to be the case in the simulation data. Since the two processes act entirely in parallel, it would be simple to perform the simulations for the individual component models (using the dual model parameters) and report average RTs (in the [HV-LV, D-HV] space). In other words, rather than showing solely predictions for accuracy, it would be important to show also predictions for RT. Additionally, in models for RT it is essential to include a "residual, non-decision, time". This doesn't seem to be the case here but should be.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Consistent patterns of distractor effects during decision making" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kenway Louie (Reviewer #1); Rani Moran (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

All reviewers agreed that the authors have done a very thorough job of addressing the essential revisions and minor comments, and that the revised manuscript is much improved. In particular, the discussion of the significance of interaction effects in Gluth, 2018 is illuminating, as it supports the general conclusion in this manuscript. There are, however, a few remaining issues that the authors should address before publication.

Essential revisions:

1) In comment 6, the reviewers previously raised the issue of interpreting triple interactions (e.g., analyses pertaining to GLM5). The authors focus on interpretations of 2-way interactions (HV+LV)D and (HV-LV)D whose signs are of theoretical importance in their framework. The concern is that these interactions are qualified by a significant triple interaction (HV-LV)(HV+LV)D. This means that the sign of each of the 2-way interactions can change as a function of the third variable. Therefore, a simple effect analysis here should examine simple 2 way interactions as a function of the third variable. This analysis is critical for the interpreting the findings.

2) Some questions remain about the modelling.

2.1) In comment 7.4. Reviewers previously raised the importance of modeling residual time. In response the authors included RT but arbitrarily fixed it to 300ms rather that allowing it to vary freely. They argue in their response letter that "because non-decision time has no reason to be different across our models, it would not bring more evidence in favor of one or another model during model comparisons.". It may be impossible to determine this a-priori because in each model residual-RT might trade-off differently with the other parameters. It would be important to re-fit the model with free residual time parameters to see which model is best. It is important to rule out that the results of model-comparison are due to arbitrary assumptions about residual rt.

2.2) A very similar issues pertains to the parameter f (inhibition) which was also fixed to a constant value rather than being a free parameter. This could potentially affect model comparison results.

2.3) It is still unclear whether in fitting the dual-channel model, each channel had its own free parameters or whether they were identical for both channels.

2.4) Why are models comparisons reported only for Experiments 1-3 but not for the other experiments?

3) In comment 4 the reviewers previously raised questions about the loss trials. The revised version does not fully address these questions.

3.1) There are still questions pertaining to how to model loss trials. According to the current equations, it seems that drift rates can be negative for the mutual inhibition model, and in the normalization model, the drift will be strongest for the highest loss option. Clearly, if this is correct, the model will require adjustments to account for loss trials and these have to be explained.

3.2) There are also questions pertaining to whether and how the model can account for differences between gain and loss trials. These are important issues because the results seem quite different for gain and loss trials. It would be important to perform a model comparison for the loss trial to determine the best model for these trials. It is not clear if the dual route model, or one of the simpler models, is best for loss trials. Additionally- looking at Figure 6 and the results of the regression (panel d) it seems that when D is positive (i.e., D = abs(D)) corresponding regression effects for these two terms offset each other but when D is negative (D = -abs(D)) they compound. So this could simply mean that the distractor effects are stronger for losses than for gains. Is this true? This can be seen, by including in the regression, interactions terms with trial identity (what the authors call GainTrial) instead of terms with abs(D). Furthermore, if distractors effects are indeed stronger for losses then these stronger effects could presumably be caused by adjusting model parameters (e.g., inhibition strength or other parameters). It is important to examine this. In sum, the authors should consider fitting models to loss trials to see (1) which model provides the best account for loss trials, (2) what account do the mechanistic models provide loss trials and for differences between gain and loss trials. This will provide a much more informative understanding of the gain-loss issue as compared to the current reliance on the regression model. Currently the authors argue that there are 2 separate effects in play, one for distractor value and one for distractor saliency. But a more informative way to understand the data might be that the context (gain/loss) modulated the distractor value effect, and to query the mechanistic models to identify the locus of this modulations.

4) Reviewers were still unclear about the meaning of terms in the GLMs. This needs to be clarified so that the models are better understood and evaluated. Just for example consider GLM1:

logit(accuracy) = β0 + β1(HV-LV) + β2(D-HV) + β3(HV-LV)(D-HV) + ε

The authors state that "All interaction terms in all GLMs are calculated after the component terms are z-scored". Does this mean that the terms are z-scored only for the purpose of calculating the interaction, or are they z-scored for the main effects as well? Reviewers think they should be z-scored in all terms not just in interaction terms. Additionally, just to be sure- did the authors z-score HV and LV separately or z-score the difference (HV-LV)? A clearer way to write the model to avoid confusions could be:

logit(accuracy) = β0 + β1 z_(HV-LV) + β2z_(D-HV) + β3z_(HV-LV)*z_(D-HV) + ε (underscore indicates subscript).
