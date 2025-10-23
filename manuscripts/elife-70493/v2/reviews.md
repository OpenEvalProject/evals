# Peer review - Round 1

Editors:
- Noah J Cowan, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70493.sa1](https://doi.org/10.7554/eLife.70493.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "A unifying mechanism governing inter-brain neural relationship during social interactions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Noah Cowan as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. Two of the reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter.

After careful consideration and discussion, the reviewers concur that there is some potential for this work, but the reviewers are unanimous in noting that the paper has serious weaknesses and requires extensive new analysis and a major revision to be suitable for publication in eLife. We note that this in part stems from the high bar of publication in eLife; this paper may be suitable in a more field specific journal as is, and so the authors will need to balance the requirements we are placing for new revisions and the desire to publish the work as is.

Also, it was noted that this manuscript reuses portions of the methods section of a prior article by the same authors (Zhang & Yartsev 2019 Cell). The methods should be rewritten so as to avoid this and it should be made clear when you are quoting directly from the prior manuscript.

If the authors choose to revise the manuscript for eLife, it is not guaranteed that future revisions will be accepted, as the model would still need to be vetted by the reviewers.

Reviewer #1:

This paper provides experimental and modeling analysis of the inter-brain coupling of socially interacting bats, and reports that coordinated brain activity evolves at a slower time scale than the activity describing the differences. Specifically, the paper finds that there is an attracting submanifold corresponding to the mean (or "common mode") of neural activity, and that the dynamics in the orthogonal eigenmode, corresponding to the difference in brain activity, decays rapidly. These rapid decays in the difference mode are referred to as "catch up" activity.

There are two main findings:

1) Neural activity (especially higher frequency LFP activity in the 30-150Hz range) is modulated by social context. Specifically, the ratio of the averaged, moment-to-moment MEAN:DIFF ratio is much higher when the bats are in a single chamber, clearly indicating that the animals are coordinating their neural activity. This change also seems to hold -- although not as striking -- in lower-frequency LFP and spiking activity.

2) The time scales of the mean vs. difference dynamics are segregated: the "difference dynamics" evolve at a faster time scale than "similarity dynamics", seems to be well supported.

The basic finding is presented in Figure 1. The rest of the paper is focused on a modeling study to garner further insight into the dynamics.

Weaknesses:

This is an entirely phenomenological paper, and while it claims to garner "mechanistic insight", it is unclear what that means.

The basic idea of the model is simple and somewhat interesting, but the details are extremely complex. There are many examples of this, but the method used to "regress out" the behavior was very hard to interpret.

On the face of it, the model is extremely simple: a two-state linear dynamical system. However, this simplistic description buries extreme complexity. The model is extremely complex as involves a large number of parameters (e.g., time switching 'b' values, the values of which are completely unclear), the switching over time of these parameters based on hand-scored animal behavioral state, and the complex mix of markovian and linear dynamical systems theoretic results. Indeed, a fundamental weakness of the model is that the Markov chain is taken as an "input" to the 2-state linear systems model, as if somehow the neural state does not affect the state transitions. Further, the Markov assumption is not rigorously tested. No model selecting or other model validation appears to be done.

In short, the model, while very interesting, is so complex that it is literally impossible to evaluate. The authors report literally no shortcomings of their model. They do not report parameter estimation methods. They do not report fitting errors or other model validation metrics. The only evaluation is whether it can produce certain outputs that are similar to biological data. While the latter is certainly important, all models are wrong, and it essential to have a model simple enough to understand, both in terms of how it works and how it fails.

In general, while the basic finding is fairly interesting, and the experiments and their findings are highly relevant to the field, the modeling and its explication fall short.

It is not that it is wrong or bad; however, it is not clear that such a complex model increases our understanding beyond the experimental findings in Figure 1, and if it does, there has to be a major caveat that the model itself is not carefully vetted.

Reviewer #2:

In this paper, Wujie Zhang and Michael Yartsev investigate some of the basic underpinnings of inter-brain synchrony in socially interacting animals. The phenomena of inter brain synchrony is fascinating and has been observed in a variety of situations across different mammalian species. It has also been proposed to play a critical role in certain social behaviors. Here, the authors report that brain activity across two interacting bats display not only similarities but also important differences. The also use advance computational modeling to capture s these two characteristics as well as to demonstrate how they are affected by the presence and absence of interaction between animal pairs.

Reviewer #3:

The activity in the frontal cortex of mammals has been previously shown to become more correlated in socially interacting animals than when they are alone. In the current study, the authors examine the differences in brain activity that emerge during social interactions. The correlations and differences in activity were shown to occur over different time scales, with mean correlations occurring over longer time scales whereas differences occur over shorter time scales. The authors made a model of these processes that show how feedback may give rise to these phenomena.
