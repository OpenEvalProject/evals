# Peer review - Round 1

Editors:
- Daeyeol Lee, Johns Hopkins University United States

Reviewers:
- Daeyeol Lee, Johns Hopkins University United States
- Peter Murphy

## Review text

DOI: [10.7554/eLife.51439.sa1](https://doi.org/10.7554/eLife.51439.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Optimal learning rate during probabilistic reversal depends on the volatility of the environment, namely, the frequency of reversal. Therefore, for the best performance, the learning rate should be adjusted according to the volatility. In this paper, Cook et al., tested the hypothesis that catecholamine level influences the ability to adjust the learning rate according to volatility by testing the effect of MPH on normal subjects. The results described in this manuscript support the hypothesis.

Decision letter after peer review:

Thank you for submitting your article "Catecholaminergic modulation of meta-learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Daeyeol Lee as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Peter Murphy (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Optimal learning rate during probabilistic reversal depends on the volatility of the environment, namely, the frequency of reversal. Therefore, for the best performance, the learning rate should be adjusted according to the volatility. In this paper, Cook et al., tested the hypothesis that catecholamine level influences the ability to adjust the learning rate according to volatility by testing the effect of MPH on normal subjects. Overall, the results are largely consistent with the hypothesis. The large sample size and highly rich experimental design are especially laudable aspects of this study.

Essential revisions:

1) While the authors discuss the relationship between reinforcement learning and working memory, it remains unclear whether the effect of MPH demonstrated in this study is primarily driven its effect on working memory or meta-learning. One possible strategy to examine this question might be to use a logistic regression model to examine the delayed (or lagged) WSLS strategy, for example, by including the effect of WSLS from the outcome in trial t-2, t-3, etc. The effect on learning rate should be reflected not only in the coefficient for the preceding (t-1) trial, but for earlier trials as well.

2) Similarly, recent results from both animal and human studies have demonstrated the learning rate as well as WSLS might depend on the valence of outcomes (i.e., win vs. loss). Therefore, it would be useful for the authors to test the effect of MPH on win-stay vs. lose-switch as well as the model with differential learning rates for rewarded and unrewarded trials. A recent rodent study has even identified specific neural circuits that might underlie learning from positive and negative outcomes (Groman et al., 2019).

3) It is alluded to at various points that the main conclusion to be drawn here is that catecholamines help to "optimize" learning rate as a function of volatility. Can the authors provide the values of learning rates optimal for stable and volatile conditions in the task used in this study? What are the win-stay/lose-switch betas and learning rates (both 'experienced' and 'inferred') for the ideal observer model for this task, estimated in an identical way as for the human participants? Do the participants come close to the ideal observer in placebo, or do they exhibit systematic biases in their behavior that the drug counteracts? Are they weighting the different sources of information (direct vs indirect) appropriately, or do they afford one more weight than they 'should'? Addressing these questions by explicitly comparing human behavior to the ideal observer model would in my opinion make for a more complete manuscript and make claims about the drug helping participants to optimize behavior much easier to evaluate.

4) The authors provided interesting information as to potential factors related to the effect of MPH on accuracy, but it would be better if there are a bit more information about the effect of various model parameters on accuracy and how these parameters were affected by MPH. For example, were the inverse temperature (β) and strategy-weight parameter (zeta) affected by MPH? How strongly were these parameters in either MPH or PLA group related with accuracy? Without this information, it remains difficult to appreciate the last sentence in the subsection “Summary of results” ("… the contribution of learning rate to accuracy is minimal.").

5) The main effect of MPH is to selectively decrease learning rates in stable contexts, and not to increase learning rates (either complementarily in volatile contexts if the meta-learning account is to be believed, or across the board if catecholamines play a more restricted role one level lower in the hierarchy – i.e. unidirectionally shifting the learning rate). This key aspect of the results warrants more extensive discussion. Perhaps the ideal observer analysis suggested above might shed some light. If under placebo participants already well-approximate the ideal observer in volatile contexts but over-estimate volatility in stable contexts, this perhaps lends additional credence to the meta-learning account – i.e. that the drug helps participants to learn the appropriate level of volatility in the context in which they 'need help'.

6) The description of the 'model-free' win-stay/lose-switch analysis is somewhat vague. Are betas for each learning type calculated from the same multiple regression model, or different univariate regressions? The former would seem more appropriate, since learning type constitutes two components (direct vs indirect) that in principle should contribute to the same choice. Authors' rationale for introducing this model in the way they do currently – i.e. to differentiate participants whose choices were primarily driven by experienced vs. inferred value – also needs to be explained more clearly. Isn't exactly this differentiation provided by the epsilon parameter in the existing δ-rule model fits? How are the results from these different models related?

7) The authors report that they measured heart rate before drug administration, and both before and after the task battery. These data are relevant for evaluating both the efficacy of the drug manipulation and the effects reported on fitted model parameters. Did participants whose heart rate was most significantly affected by the drug also show the strongest behavioral effects, or perhaps additional behavioral effects not apparent at the full-sample level? Taking such data into account could greatly improve the sensitivity of the reported analyses.

8) It is striking, but not emphasized, that the authors do not replicate the original study under placebo: there is no effect of volatility on the learning rate for experienced feedback under placebo (Figure 3A green, Results section). It seems important to emphasize this lack of replication and discuss it.

9) The authors should not overstate the adaptiveness of increasing learning rate or changing strategy between stable and volatile environments (e.g. subsection “Win-stay, lose-shift analysis”, and in a few other places). As the authors show at the end, the learning rate effects don't actually seem to make an important difference in this task, so "optimality" claims should be weakened.

10) It would be useful to present more general results before jumping into more specific analyses (win-stay-lose-shift). It might be better to present the information about the overall performance in the task before describing drug effects on performance. Some of the figures in the supplement, including model validation, could usefully be moved to main text.
