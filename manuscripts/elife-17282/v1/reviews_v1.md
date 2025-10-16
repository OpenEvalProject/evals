# Peer review - Round 1

Reviewers:
- Joshua I Gold, University of Pennsylvania , United States

## Review text

DOI: [10.7554/eLife.17282.014](https://doi.org/10.7554/eLife.17282.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A specific role for serotonin in overcoming effort cost" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Joshua Gold as the Reviewing Editor and Sabine Kastner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Read Montague (Reviewer #1); Roshan Cools (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study used a physical effort/incentive-based task with two groups of subjects – one taking escitalopram, the other placebo – to test whether SSRIs, and putatively serotonin, have an effect on the amount of effort human subjects will expend to get a reward. Several of the authors had previously developed a rise-to-bound computational model to account for behavior on this task in terms of a "cost evidence" variable that rises during effort and falls during rest. Here they used the model to show that overall better performance of the SSRI group (more reward) is associated with reduced effort costs and not the weight in monetary incentives. Thus, 5HT's role in action costs might be more general than hitherto thought, extending from the regulation of punishment and delay to that of effort costs.

The reviewers all agreed that this is an excellent paper: interesting, well done, and well written. The role of serotonin in behavioral control and decision-making is complex, and this paper makes a solid contribution to shrinking some of this complexity by sharpening our understanding of it in relation to effort. The ubiquity of SSRI use – in depression, Parkinson's Disease, and other disorders – and the lack of model-based understanding of what these drugs do in terms of information processing makes the contribution important. It is also commendable from a clinical perspective that chronic rather than just acute effects of the drug were assessed.

Essential revisions:

1) Several reviewers thought that the model needed to be explained better, and the modeling results analyzed more thoroughly.

A) Specifically, the text only briefly refers to specific parameters ("amplitude, accumulation and dissipation slopes of the cost-evidence decision variable") that a reader without thorough familiarity of the earlier papers will have a hard time following. It would be useful to describe the model in the text. Likewise, the model parameters are listed ("Ai, Sem, etc.) without being explained. For more context, it might also be useful to relate their model more directly to the RL model in Daw et al. 2002 referenced in the paper, and also the model in Balasubramani et al. 2015, Frontiers of Computational Neuroscience.

B) More substantively, there were questions about the specificity of the effect from the modeling analyses. It is stated that interactions between treatments and pairs of computational variables (Sem versus each other parameter) were always significant. The implication of this result depends on the sign of the parameters. The cumulative payoff effect might represent, for example, enhanced amplitude modulation (Ai) and/or reduced cost-evidence accumulation (Sem). How were computational parameters coded when entered into the ANOVA? To assess specificity, one might want to reverse the coding for A and Sr. More generally, to what extent were the parameters independent of each other in the model? Also, might it be possible to define a different model space that would allow the use of Bayesian stats, and model comparison to estimate the drug effects on the various parameters? The distinct advantage of such an approach would be that it allows the capturing of drug effects despite the presence of individual differences of no interest.

C) Is any background 'reference' neuropsychological data available to confirm that there were no group differences of no interest? If so, please report.

2) There were questions about the interpretation of the effects in terms of the role of time in task performance. The main effects coming out of the modeling analysis appear to be related to effort duration. But longer effort durations are also longer overall durations, which brings up the literature on 5-HT and delay costs (some of the delay discounting papers with 5-HT manipulations are actually cited in the manuscript). The authors appear to favor the view that different types of costs can be reduced to one process that is related overall to multiple types of costs. There is evidence both for and against this, and the authors are of course free to interpret their results in this way. In fact, this discussion contributes to the field in an interesting way. However, how much of the effect they are seeing is related to time per se? The authors should discuss this.

3) The Introduction might benefit from mentioning the implication of 5HT not just in apathy, but also in the other end of the motivation continuum, that is impulsivity. And in the Discussion, how do the findings relate to observations that 5HT is key for impulse control? More generally, the paper might come full circle, by linking, in the Discussion section, the obtained results to these various clinical hypotheses (involvement in apathy, impulsivity).

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A specific role for serotonin in overcoming effort cost" for further consideration at eLife. Your revised article has been favorably evaluated by Sabine Kastner (Senior editor), a Reviewing editor (Joshua Gold), and one new reviewer, who offered input from a statistical perspective. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined by the reviewer:

Reviewer #4:

I have reviewed this paper from a statistical perspective as this is a registered trial.

This manuscript presents the analysis of a single randomised placebo controlled and double blinded study. It is not a trial of an intervention but rather a controlled study to understand the mechanism of action that the specific drug takes. The trial has been registered with a target sample size of 128 and it has a single hypothesis statement that aims to 'assess the effects of' agolmelatine and escitalopram on emotional binding, emotional processing and motivation'. Each participant is measured over several tasks during the treatment period of 9 weeks.

I realise that it is not in the eLife style to report numerical estimates in the Abstract but as this report analyses a single controlled experiment I think they should put the strength of the evidence in the Abstract to back up their statement that 'they show that serotonin also regulates other types of action costs such as effort'. As there is no replication they should report this in a more guarded manner.

The authors have completed the Consort statement but they need to provide more complete information within the manuscript so they can say yes to more of the checklist.

The trial registration lists a compound aim/hypothesis and also lists three primary outcomes listed which I think have all been used in this analysis but the main question for the manuscript is 'does serotonin regulate the weight of effort cost as opposed to the weight of expected benefit?'

I would like to see a clearer link between the main research question and the forms of analysis. A sample size of 58 is not that large even with repeated measurement. Was there really any power to test for interactions? The Consort checklist says 'no' to sample size but surely the size was justified originally? I feel a bit concerned that sometimes Bonferonni correction is used to conclude there were no differences when this just reduces power.
