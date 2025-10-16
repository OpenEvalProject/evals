# Peer review - Round 1

Editors:
- David Badre, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32548.024](https://doi.org/10.7554/eLife.32548.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Offline Replay Supports Planning: fMRI Evidence from Reward Revaluation" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Fiery Cushman (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript investigates how people engage in offline replay to update their value estimates decisions during a sequential task. Specifically, the experiment constructs a situation in which participants assign value to early decisions based on late outcomes, and then acquire new information about late consequences outside the context of early decisions. This provides a putative opportunity to compute the new expected value of the early decisions through offline replay. The paper reports behavioral and MVPA evidence that offline replay aids in this type of re-planning.

Essential revisions:

The editors and reviewers agreed that this paper investigates a fundamental topic. Further, the approach that combines MVPA estimates of task state with a two-step task is innovative and clever. However, both reviewers also raised significant concerns regarding the design and analysis. The most serious of these questioned what conclusions can be drawn from these results and whether there is specific evidence for planning versus other alternatives. In discussion among the reviewers and editors, it was agreed that several essential revisions are critical to shore up the specific contribution here beyond a basic association of replay with performance.

1) Alternative accounts of these results.

The authors consider the possibility that unsigned reward prediction errors experienced during the "relearning" phase prompt revaluation. This is plausible, but the authors don't consider any alternative hypotheses. In the absence of an alternative, it's hard to evaluate whether the evidence they consider in favor of this model is actually decisive – i.e., does their evidence uniquely favor their model, or is it consistent with other models?

Moreover, they undercut their own model when they write: "the inclusion of reward noise in the noisy-rewards condition (even in control blocks) allowed us to rule out the possibility that replanning is brought about by 'any' experience of uncertainty, whether or not replanning was optimal". This is a good point and an elegant feature of their design, but they don't seem to address how their model of revaluation assesses the "optimality" of replanning beyond unsigned PEs. In other words, they include a control condition specifically to show that their model is incomplete, and then don't address how it could be made complete.

Just to sharpen this point, here is one alternative account of what prompts revaluation. Possibly, during the rest period, people start engaging in value iteration from random points in their task model, which includes Stage 1. They then continue the process of value iteration at all points where value iteration results in high unsigned PEs during update. In other words, when performing value iteration on Stage 1 actions, the mismatch between the existing Stage 1 value estimates and the newly updated Stage 2 value estimates generates high unsigned PEs. These remain high until sufficient value iteration occurs that Stage 1 actions are appropriately revalued.

In summary, perhaps what drives the total amount of revaluation is not the magnitude of Stage 2 PEs during online relearning, but rather the magnitude (or persistence) of Stage 1 PEs during offline revaluation. (It should be clear how this stands in contrast to the "tagging" idea presented in the general Discussion. Incidentally, there is no reason that both things couldn't happen).

This alternative model addresses the question of why there is no reevaluation for high variance rewards in the control condition: the variance of the terminal rewards does not affect the Stage 1 PEs during value iteration.

It also seems to be consistent with all the data the authors present, because (except in the control condition) high unsigned Stage 2 PEs during relearning will be correlated with high unsigned Stage 1 PEs during revaluation.

But this correlation need not always hold – the difference between the two models can be tested. For instance, imagine that during the revaluation phase, values are swapped on the right/left dimension within each state. i.e., if formerly State 2/left was $1 and State 2/right was $8, then now State 2/left is $8 and State 2/right is $1. On the authors' model, this will result in high unsigned PEs during relearning and therefore also high levels of revaluation. On the model sketched above, however, it would not result in high levels of revaluation because max(Q) for each Stage 2 state does not change, and so there is no change to the Q value of each Stage 1 state, and thus no PEs during value iteration.

(A conceptually similar experiment would involve drifting rewards away from their original values but then right back to their original values all within a single relearning phase. This results in high PEs during the phase, but the model sketched above would not predict much revaluation for reasons similar to those described above).

The purpose of detailing this alternative is not to argue that this model is right or the only alternative, but to illustrate a much broader point. By sketching only one model of what prompts revaluation and failing to explicitly consider alternatives, the authors leave the reader in a poor position to evaluate whether the analyses that are consistent with their model are in fact good evidence for it – we don't know whether those analyses are also consistent with all plausible alternatives. Could the authors show us what models of revaluation-prompting are ruled out by their analyses? This would be a big help, whether or not the authors decide to discuss the specific alternative mentioned here.

2) Alternatives raised by the design and logic

Akin to the above point, there were several points regarding the design that raise other alternatives, including basic issues of engagement. Specifically:

- What incentive did people have to go to the higher-valued states in the learning phase? It seems this part of the task was not incentivized, so people had no particular reason to select higher numbers over lower numbers (except for learning for later). The replanning magnitude metric then becomes potentially problematic in that it subtracts away performance during the learning phase, which was not incentivized. This issue becomes especially problematic when trying to assess the impact of the brain replay (e.g., Figure 2). Here replay correlates with replanning, but which aspect of the replanning is not clear. Perhaps this correlation is due to behaviour in the learning phases-i.e., those people who paid more attention and learned more initially show more replay later on. That's not so surprising or interesting. The interesting thing is to predict later behaviour, but subtracting away a baseline that precedes the replay means that the replay can just be correlating with something that occurred earlier (learning/attention/task engagement, not replanning). It would be more convincing to show that the replay correlates solely with the test behaviour not with this replanning metric.

- The above point is compounded somewhat with the choice of the control condition here. Unlike the revaluation condition, there is no learning necessary at all in the second phase. There is also no incentive to pay attention or be engaged at all during this second phase. As a result, the differences in brain activity may be due to differential engagement, rather than specific to the replay-replanning connection as claimed here.

- The test phase gave no feedback or guidance. How were participants supposed to know which experience to draw upon when making those decisions? The assumption here is that the optimal thing here is to integrate the information in the two phases by adjusting the values of the terminal states in phases 2 and keeping the same phase 1 knowledge of task structure. A smart participant, however, might infer that the recurrence of the Stage 1 stimulus (which never appeared in the relearning phase) meant that the Learning phase reward-contingency rules were back in effect. It's not obvious what is optimal here. Maybe they have learned that the Stage 2 stimuli give different values when they are (or are not) preceded by the Stage 1 stimuli (i.e., a type of occasion setting).

- What were the means/variances of the experienced distributions? Were the actual means of the experienced distributions controlled or only the generative process? Were the experienced distributions close to the planned ones? How was it ensured that all conditions were experienced? Could people have avoided one of the outcomes e.g., due to getting initially unlucky (hot-stove effect)?

- It was not clear is why non-specific replaying the Stage 1 stimuli during the replanning task would help. In some ways, it says that people who are more engaged with the task do better on the task. That's interesting, but not groundbreaking. The data here do not seem to show that category-specific replay predicts later performance. Does replay of other categories (not the Stage 1 stimulus) not correlate with replanning behaviour? That would be a good additional piece of evidence beyond simple task engagement.

3) Concerns over the robustness of the analysis and approach to the computational modeling. It should be noted in light of the first comment below that eLife does not require that all hypothesis, predictions, or analyses be preregistered. However, the reviewers agreed that there should be explicit discussion of investigator degrees of freedom and what safeguards against flexibility in the analysis were put in place. Further, any checks that can be provided for robustness would be helpful. Here are the specific comments raised regarding the analysis and modeling.

- The article is pitched as confirmatory in the sense that it makes predictions and then confirms those predictions with evidence. Were any of these predictions pre-registered anywhere? Were there any competing hypotheses? What sort of data might have gone against these predictions? The evidence in the paper could use to be bolstered to establish that it was truly a confirmatory study. Similarly, were any of the metrics or analyses preregistered? If they were indeed hypothesis-driven, that should have been possible. It would seem that there are many, many ways that these data could have been analyzed (both behavioural and neural), and some of the metrics seem very arbitrary (e.g., number of trials in learning phase). Were other analysis pathways attempted? Evaluating the import of the inferential statistics requires more knowledge of the researcher degrees of freedom.

- Two participants were excluded post-hoc due to "not having sufficient number of runs". Were there any pre-defined criteria on this front? Or was this exclusion made after the data were examined? Additionally, the sample size seems small (though not inordinately so for an fMRI study), leaving many of the statistical tests underpowered (and indeed many of the brain-behaviour correlations fell in the marginal zone, making interpretation difficult).

- The idea that high prediction error should be preferentially replayed seems like a rule that would only work in very narrow (static) environments. If there is any variance in the rewards, then this rule could lead to perverse replay of unreducible uncertainty.

- The selection of learning rate requires further justification. How was the.7 estimated? What sort of task? If the task were as simple as the current task, with such a wide gap in rewards, I wonder how reliable an estimate this number represents. Moreover,.7 seems extremely high for a task with variable rewards. That would make people extremely influenced by the most recent outcome, much more so than a typical task with variable or probabilistic rewards. Is it reasonable to use the learning rate estimated in a different sample for analyzing the new sample? How robust are the prediction error analysis to this selection of learning rate?
