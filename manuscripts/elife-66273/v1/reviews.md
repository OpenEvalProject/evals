# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66273.sa1](https://doi.org/10.7554/eLife.66273.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A precise quantitative description of synaptic plasticity is currently unknown, so that most formulate learning rules somewhat ad hoc. This computational neuroscience paper uses genetic algorithms (GAs) to find synaptic plasticity rules that perform best on a variety of simulated plasticity tasks with spiking neurons. In principle GAs are potentially powerful, but by being non-differentiable they are limited by computational requirements and can only find simple equations and rely on pre-processing such pre-defined eligibility traces. Future research might be able to generalize this technique.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Evolving to learn, discovering interpretable plasticity rules for spiking networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Henning Sprekeler (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. Our excuses for the long time we needed to reach our decision.

While the reviewers both saw the potential benefits of the method, the current application only reproduces already known plasticity rules (sometimes not without extra tweaking).

The reviewers agreed that the manuscript does not sufficiently support the applicability of the suggested method to less hand-crafted situations. The scalability of the method is potentially a concern. To be eligible for further consideration in eLife, this would have to be shown, either by applying the method to a situation with more and less hand-crafted inputs to the learning rule and/or by identifying novel, efficient and task ensemble-specific rules. Such a revision would likely require more time than eLife aims for.

Reviewer #1:

This paper uses genetic algorithms to find synaptic plasticity rules.

Overall, I found the results interesting, but as genetic algorithms have been well-established and the amount of new results are limited, I see this more as a tutorial and an effort to bring other researchers to use GAs.

However, the limitations of the method were not clear:

I would like to see a discussion of the computation time, and the scaling with model complexity and other limitations of the technique.

I found it also hard to judge whether this study presents an advance of other methods, such using multiple traces to fit learning rules (Gerstner c.s.).

The inputs to the GAs are quite engineered traces and it was unclear how important this was.

The reworking of the STDP rules in the last Results section was not so clear to me.

First the concept of instability needs to be explained better.

Do these reworked rules perform identically? If so, is there a equivalence class of STDP rules that perform identically on this task?

Furthermore, can stability not be included in the fitness function (either as direct constraint on \Δ w (t->\pm \infty), or by widening the task repertoire)?

It is not so elegant to have a supposedly general technique, and then hand-tune the solutions….

In conclusion, I'm not convinced the study presents enough of a conceptual or methodological advance.

Reviewer #2:

The article "Evolving to learn, discovering interpretable learning rules for spiking networks" by Jordan et al. proposes an evolutionary algorithm to meta-learn plasticity rules for spiking neurons. The algorithm learns to combine user-determined inputs into a mathematical formula for updating synaptic weights, by gradually mutating and selecting a set of candidates based on their performance. The algorithm is applied to (families of) reward-based, error-based, and correlation-based tasks, all three performed by a single neuron. In each case, the algorithm recovers previously proposed learning rules (or variants thereof) that are known to optimize some performance measure.

The article is clearly written, timely, and presents an exciting approach to meta-learning that holds the promise of not only generating task-specific learning rules, but of providing them in an interpretable form. Its key weakness is its limitation to a rediscovery of existing general purpose rules, in a setup where the quantities that enter the rules seem somewhat pre-engineered. As such, the paper is a proof-of-concept presentation of a very exciting method on simplistic examples. Whether the approach will actually be applicable to a situation with more inputs, for more complex settings (e.g., multi-layer networks) and whether it will ultimately discover task ensemble-specific learning rules is yet to be seen.

1. Pre-engineering of inputs: It's nice that the authors test their method on three different learning tasks. However, the inputs that enter these learning rules (e.g., the eligibility traces) are chosen by hand and reflect substantial domain knowledge. To show that the method could be applied by a more agnostic user, it would be nice to see that, e.g., different rules could be learned from the same set of inputs. Would it be possible to learn the shape of the eligibility traces? Does the number of successful evolutionary runs decline quickly with the number of inputs the rules are allowed to use?

2. Computational effort: Meta-learning is somewhat notorious in its demand for computing resources, and the authors acknowledge a high-performance computing center. How computationally expensive is the method? How does the computational expense scale with the number of inputs to the learning rules?

3. Discovery of unknown/non-general purpose rules: The paper would be strengthened substantially by an example of a discovered rule that is better than known general purpose rules. I fully appreciate that a search for such a situation may amount to finding a needle in a haystack and I suspect the authors have tried. I nevertheless dare to make a suggestion for a candidate: In Vasilaki et al. (2009), the authors used reward-based spiking learning rules to learn a navigation task and argue that policy-gradient methods fail. What works much better in the end is a biased rule that effectively amounts to something simple like pre x post x reward. Such a rule is clearly biased and could make catastrophic errors in other situations. However, I've suspected for a while (and I think I discussed this with Walter Senn at some point) that such a rule could actually be very powerful in a setting where rewards and state and action representations are very sparse. I wouldn't suggest to the authors to try their method on a navigation task, but policy gradient rules in spiking neurons are notoriously slow in much simpler settings. It feels like it should be possible to beat them. Maybe there is a simple single neuron task with sparse inputs, sparse target outputs and sparse rewards?

4. How sensitive is the method to hyperparameters? The authors use mutation probability 0.045 in first tasks, but 0.05 in last.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Evolving interpretable plasticity for spiking networks" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Henning Sprekeler (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

This computational neuroscience paper uses genetic algorithms (GAs) to find synaptic plasticity rules that perform best on a variety of simulated plasticity tasks with spiking neurons. While GAs are potential powerful, being non-differentiable the study is limited by computationally requirements and can only find very simple equations and use fairly advanced preprocessing such pre-defined eligibility traces.

Essential revisions:

1) The authors have added a number of additions to the manuscript that present clear improvement. However, I have doubts about one of the main additions: the inclusion of different baselines for the RL task. From my understanding, rewards are either 1 or -1. Doesn't that mean that [R]+ = (R+1)/2 and [R]- = (R-1)/2? If that's true, all three baselines are all linearly dependent. My suspicion is that this leads to substantial amounts of "neutral evolution" of terms that basically sum up to zero (or converge to zero exponentially). I juggled around a bit with the various rules and found quite a few of those "null" terms.

I suspect that the point discussed in the section on error-driven learning rules (l. 270) also applies to the RL rules, and that the differences between the rules mostly amount to learning rate (schedules) and "null terms". This may also explain why the gains in performance are not overwhelming. However, because the difference between the evolved rules is not analyzed in depth, this doesn't become clear in the manuscript. I'd suggest to support the discussion of the learning rules by figures. Maybe plot the different "causal" and "homeostatic" terms over time, and potentially something like a running average covariance with (R-1) E?

2) Proper statistical analysis of the findings.

In particular in Figure 3 significance estimates against the null-hypothesis need to be presented.

For that section, I would also like to see if the found learning rules differ in their convergence speed on new data.

3) Include data on the convergence speed of the learning. I still would like to see compute time used for a typical run, which is suspiciously absent from the paper.

Reviewer #1:

This paper uses genetic algorithms (GAs) to find synaptic plasticity rules on a variety of plasticity problems with spiking neurons. GAs have as an advantage that a free exploration of possible models potentially coming up with original, superior solutions. On the other hand, being non-differentiable they are severely limited by computationally requirements and can only find very simple equations and use fairly advanced pre-processing such pre-defined eligibility traces.

The paper reads on occasion more like an advertisement than a scientific paper.

For the unsupervised rules, was the LTP made explicitly dependent on (w-1)? Or was this found automatically?

The divergencies described in the previous version of the manuscript seemed to have disappeared like snow in the sun.

Reviewer #2:

– The discussion about the need to jointly consider learning rule and homeostatic mechanisms is nice, but of limited novelty. I'd suggest to cite at least Mackay and Miller (1994) here.

– Figure 3: Panel 3 doesn't show any rules with new baselines. Is this old data?

– I failed to find the time window on which the baselines are computed (m=?) This is quite important for your discussion about time varying learning rates.

– Section references are broken. Recompile?

– Double words: l. 82, 377

– l. 364: I learned the hard way to stay away from "first demonstration" claims in papers …
