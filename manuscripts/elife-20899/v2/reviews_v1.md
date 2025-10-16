# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20899.011](https://doi.org/10.7554/eLife.20899.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Biologically plausible learning in recurrent neural networks reproduces neural dynamics observed during cognitive tasks" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Michael Frank as Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript is a theoretical/computational study of reward-based learning in recurrent networks of (non-spiking) neurons. The author compares the simulation results to previously published analyses of experimental data. The author describes an improved reward-based learning rule which is more biologically plausible than other supervised learning rules that have previously been used for similar purposes. The author applies the rule to a number of relevant tasks. It is shown that a network equipped with the rule can learn these tasks surprisingly well. Further, it is demonstrated that the resulting network dynamics is consistent with experimental data.

Essential revisions:

1) Both Reviewers were enthusiastic about the contribution, which they agreed was the learning rule itself, rather than its ability to produce dynamics, but both expressed concerns that it wasn't sufficiently clear why the rule works. This point was underscored in the consultation session in which it was noted that without further analysis, there is a strong risk that either i) the learning rule will be found to break down for more complex tasks and generality will be lost, or ii) someone else will soon publish a detailed theoretical study of this learning rule and greatly shadow this contribution. Thus the most important point for revision is to focus efforts on quantifying the intuitions given in the supplementary material.

Here are more specific comments and suggestions in this regard:

On the one hand, it is very nice to see a simple, plausible learning rule (in a fairly well-written paper) learn non-trivial computations in recurrent networks where we know the gradients of the objective function are hopelessly non-local. I see this paper as a much welcome addition to the upcoming literature on reverse-engineering brain computations by training RNNs. On the other hand, the author seems to spend comparatively too much effort on "extra goodies", or what I would see as mainly "asides" (e.g. studying the activity of those networks after training), and not enough in trying to understand the reasons why this learning rule works so well (again, I see the learning rule itself as the main contribution of this paper - will other reviewers agree?). Dissecting the inner workings of the proposed learning rule quantitatively would considerably strengthen the paper, and would also suggest situations where one would expect it to fail (in a way, the paper could have been more "self-critical"). In its current formulation, the learning rule looks like a hack - so, as for any hack, one has little reason to believe it is generally applicable. One could still argue that the range of tasks studied here is wide enough to suggest this rule will robustly apply to other scenarios, but I would be more convinced by some more thorough theoretical analysis. The supplementary material does give some reasonable intuitions (especially regarding the nonlinearity in the rule), but they remain hand-wavy and at the very least should be included in the main text, since it is central to the paper.

Here are a couple of suggestions:

i) Substantiate the relatively vague intuitions given in the supplementary material, by numerically and/or analytically quantifying the most important relationships stated there ("x is greater than y, while z is neglible etc.").

ii) To dissect the role of the supralinear amplification of co-fluctuations, I would have started by much simpler RNN problems, such as simple nonlinear regression in a multi-layer, feedforward network - this would get rid of all the subtleties related to recurrent processing, short-term memory etc., which I found the supplementary material does not handle very well. How do the updates prescribed by the proposed learning rule compare with the exact gradient of the reward function? How does that depend on supralinear amplification?

iii) Somewhat more generally - we know some of the reasons why it is hard to train recurrent neural networks (without extra hacky components like LSTM etc.): vanishing/exploding gradients, very ill-conditioned saddle points, etc. How does the proposed learning rule overcome these difficulties? (and in fact, does it? - are the tasks studied here representative of more complex cognitive tasks with respect to these generic difficulties in training RNNs?).

2) Figure quality could be improved. Sub panels with labels (A, B, etc.) should be established and referred to. Figure 3 is ugly.

3) The description of Figure 5 in the legend and in the text is hard to follow. For example, in Figure 5, the meaning of colors should be explained.

4) Compared to experiments, the delay of 200 ms in task 1 is very short. Does it also work with more realistic delays on the order of seconds? Relatedly, where the learning rule might break down, it may be nice to address explicitly in discussion whether this rule is dependent on a fixed interval between task relevant events. One central problem for RL rules that depend on eligibility traces with fixed time constants is that without other mechanisms, these may have difficulty in tasks that have distractors, variable timing, or number of intervening events between task relevant stimuli (see for example O'Reilly & Frank 2006 Neural Computation).

5) Although it is common to use rate-based networks in such models, the model used contains a number of coarse approximations to biological reality.i) Rate-based neurons are used instead of spiking models.ii) The tanh-activation function allows for negative neuron outputs. What happens for non-negative outputs (e.g. a logsig)?iii) Synaptic weights from one presynaptic neuron can be positive or negative (violating Dale's law) and presumably even change the sign during learning. What if more realistic constraints are included?

It would be nice if one could have at least one control simulation where ii) and iii) are considered and a brief discussion. This would strengthen the main claims.

6) It would be interesting to discuss how the learning rule compares to the supervised approach considered in other works? How much does one lose in terms of performance or convergence speed?

7) The eligibility trace is typically decaying. According to Equation 3 it is not in this model. Why, and is it important?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Biologically plausible learning in recurrent neural networks for cognitive tasks" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens as Senior editor), Michael Frank as Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The revised paper is clearer in how it exposes the learning rule, but reviewers differed as to whether this was satisfactory or not. Please see concerns below, if you can respond directly to them and expand the manuscript to address them the paper will be improved.

Reviewer #1:

I think this revision only partially addresses my original concern. The supplementary material has merely been rebranded "appendix", with a few (nice) additions, where I was expecting a convincing theoretical analysis of the learning rule as a first-class citizen in the main text. Why does this learning rule work? Why does learning success rely on moments of higher order than the usual Hebbian covariances? I am not sure I understand it better now after reading this revision.

The comparison to the exact gradient in Figure 9 is a nice starting point, but there is potential to squeeze more out of this toy example to explore the role of the supralinear gain function more systematically; e.g. how does the alignment between proposed rule updates and true gradient depend on the exact type of superlinear function used? (e.g. on the exponent n>1 if x → x is used).

The addition of Figure 8 and the explanation of the relaxation effect is not entirely convincing to me. In paragraph two of subsection “Removing the need for continuous reward signals with supralinear amplification”, all the author is saying here is that the average of xx¯ is zero - sure - but this is not what the eligibility trace is accumulating: it's estimating a covariance. The argument works OK when the input is constant, but in recurrent nets it will be anything but constant. In this respect, I am not sure that the example of Figure 9 (which uses constant inputs) is representative. Can the author comment?

I still find the argument appealing though, if it can be made more precise/quantitative; in particular, does this argument inform us of what "a good time constant" would be for the running average of x - e.g. that it should be larger than the typical autocorrelation time of the input fluctuations? Could another fix be to remove a running average of rj from the input rj too, so that the pre and post "relaxation effects" cancel?

Reviewer #2:

The manuscript has significantly been improved in this revision. In particular the learning rule has been analyzed more thoroughly, which provides important insights to the general learning problem addressed in this paper. The author has also added new experiments that show that the rule also works under some more challenging setups. The discussion of the learning rule is now in the Appendix, which is not optimal but acceptable. I think no additional work is necessary at this point.
