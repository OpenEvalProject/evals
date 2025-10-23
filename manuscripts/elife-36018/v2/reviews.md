# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36018.037](https://doi.org/10.7554/eLife.36018.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Ongoing, rational calibration of reward-driven perceptual biases" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Peter Latham as the Reviewing Editor, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Roger Ratcliff (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors consider a relatively standard 2AFC task in which monkeys view a random dot kinematogram and have to decide whether the dots are moving to the right or left. To make things slightly more interesting than usual, the rewards are asymmetric: in blocks of 30-50 trials, one saccade directions receives higher reward than the other.

The monkey learned to take the asymmetry into account: the more uncertain they were, the more they favored the direction that had higher reward. However, they were slightly suboptimal: they received about 97% of the reward they could have received if they had used an optimal policy.

To explain the suboptimality, the authors used a "satisficing" gradient-based learning rule. Essentially, the monkeys follow the gradient in trial averaged reward rate until they achieve 97% performance, and then stop learning. For such a model, the final values of the parameters depend on initial conditions. The authors found, however, that, under their model, all the animals used the same initial condition; so-called "over-me".

Essential revisions:

There were a lot of things we liked about this paper (more on that below). However, all of us had problems with the "satisficing" learning rule. We know that's an essential feature of the paper, but it seems like a near untenable hypothesis. How, for instance, can the animal know when it reaches 97%? Presumably there's nothing special about 97%, but that still leaves the problem: how can the animal know when it's near the optimum, and so turn off learning? For the satisficing learning rule to be a viable explanation, these questions need to be answered.

Note that there are reasons to turn down the learning rate; see, for example, Aitchison et al., 2017, and Kirkpatrick et al., PNAS (2016), 106:10296--10301. But those approaches – which essentially turn down the learning rate when the synapses become more sure of their true values – would put a slightly different spin on the paper. In addition, the authors need to try other explanations. For instance, because learning is stochastic, the animal never reaches an optimum. And if the energy surface has a non-quadratic maximum (as it appears the energy surface does in this case), there will be bias. If the bias matches the observed bias, that would be a strong contender for a viable model. It's also possible that the model class used by the monkeys does not contain the true model, which could happen if z and me are tied in some way. That seems like an unlikely model, but probably not less likely than a model that turns down the learning rate. It is, at the very least, worth mentioning.

In addition, you should look for sequential effects: does behavior on one trial depend on the outcome of the previous trial? If so, can you link these to changes in me and z? If so, that could shed light on which model, if any, is correct. And it would be a nice addition to the analysis so far, which is primarily steady state.

On the plus side, the paper is short, well-written, and to the point, and the findings are novel and interesting. We're highly sympathetic to the idea that animals adopt satisficing solutions as opposed to optimal ones in many settings. We also think the ability to account for idiosyncratic differences in performance of different animals is a very nice result.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ongoing, rational calibration of reward-driven perceptual biases" for further consideration at eLife. Your revised article has been reviewed by three reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Ivry as the Senior Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We see no fundamental obstacles to acceptance. However, there are still some things that are not clear. And in one case it appears that we were not sufficiently clear, so there is still a small amount of work to be done. Following are our suggestions; hopefully they will be crystal clear.

1) At least two of the reviewers were somewhat confused by the stopping rule. We think we eventually understood things, and the rule is in fact simple: stop learning when the reward reaches a certain (good enough) value. However, this is surprisingly hard to extract. We have a couple of suggestions to fix this:

a) You say:

"We next consider if and how a consistent, adaptive process used by all three monkeys could lead to these idiosyncratic and not-quite optimal patterns of adjustments."

This is not all that informative – basically, you're saying you have a model, but you're not going to tell the reader what it is. Why not say:

"We show that this can be explained by a model in which the monkeys are initially over-biased, adjust their model parameters to increase reward, but stop learning when the reward is high enough, but not maximum."

b) In Figure 8 legend, you say "All four searches stopped when the reward exceeded the monkeys' RTrialpredict in that session." This is hard to make sense of, for two reasons. First, we had to go back and figure out what RTrialpredict is. Second, the implication is that there's something special about RTrialpredict. In fact, the point is that you stop integrating when the reward reaches the reward the monkeys got on that trial. It would be a lot easier to understand if you just said that, without mentioning RTrialpredict.

c) Identical comments apply to the third paragraph of the subsection “The monkeys’ adaptive adjustments were consistent with a satisficing, gradient based learning process”.

2) The added paragraph was not so clear:

“Our last assumption was that the monkeys terminated adjustments as soon as they reached a good-enough reward outcome. […] Moreover, the updating process could use step sizes that are fixed or adaptive to the gradient of a reward-related cost function (Aitchison et al., 2017 and Kirkpatrick et al., 2017).”

The first two sentences are fine, but after that one would have to know those papers inside and out to understand what's going on. I think all you need to say is something like:

(Aitchison et al., 2017 and Kirkpatrick et al., 2017) proposed a model in which learning rates decreased as synapses become more certain. In this scheme, learning can become very slow near an optimum, and might account for our results.

3) In our previous review, we said

In addition, the authors need to try other explanations. For instance, because learning is stochastic, the animal never reaches an optimum. And if the energy surface has a non-quadratic maximum (as it appears the energy surface does in this case), there will be bias. If the bias matches the observed bias, that would be a strong contender for a viable model.

In your response, you seemed to be able to guess what would happen in this case. We admire you if you are indeed correct, but we think it will require simulations. In particular, you need to run a model of the form

Delta z = eta dR/dz + noise

Delta me = eta dR/dme + noise

where R is reward. The average reward value of z and me under this model will, for a non-quadratic surface, but slightly biased. We think it's important to determine, numerically, what that bias is. Given that you're set up to solve an ODE, it shouldn't be much work to check what happens to the above equations.

4) You should cite Ratcliff, 1985, – as far as we know, that was the first paper to have bias in drift rates and starting point as 2 possibilities.

5) Take out this quote:

"… they may not capture the substantial variability under different conditions and/or across individual subjects".

6) Add in the Green and Swets reference near Figure 2 and note that signal detection theory does not have a model of criterion setting and does not achieve optimal performance where that has been studied.
