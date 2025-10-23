# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101992.3.sa0](https://doi.org/10.7554/eLife.101992.3.sa0)

This important study presents a meta-analysis confirming a statistically significant association between slow oscillation-spindle coupling and memory formation, although the reported effects are limited (~0.5% of variance). The evidence is overall convincing, but the statistical methods may be difficult to follow for readers unfamiliar with advanced techniques. This work will be of particular interest to neuroscientists studying the neural mechanisms of sleep and memory.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101992.3.sa1](https://doi.org/10.7554/eLife.101992.3.sa1)

In this meta-analysis, Ng and colleagues review the association between slow-oscillation spindle coupling during sleep and overnight memory consolidation. The coupling of these oscillations (and also hippocampal sharp-wave ripples) have been central to theories and mechanistic models of active systems consolidation, that posit that the coupling between ripples, spindles, and slow oscillations (SOs) coordinate and drive the coordinated reactivation of memories in hippocampus and cortex, facilitating cross-regional information and ultimately memory strengthening and stabilisation.

Given the importance that these coupling mechanisms have been given in theory, this is a timely and important contribution to the literature in terms of determining whether these theoretical assumptions hold true in human data. The results show that the timing of sleep spindles relative to the SO phase, and the consistency of that timing, predicted overnight memory consolidation in meta-analytic models. The overall amount of coupling events did not show as strong a relationship. Coupling phase in particular was moderated by a number of variables including spindle type (fast, slow), channel location (frontal, central, posterior), age, and memory type. The main takeaway is that fast spindles that consistently couple close to the peak of the SO in frontal channel locations are optimal for memory consolidation, in line with theoretical predictions. These findings will be very useful for future researchers in terms of determining necessary sample sizes to observe coupling - memory relationships, and in the selection and reporting of relevant coupling metrics.

Although the meta-analysis covers the three main coupling metrics that are typically assessed (occurrence, timing, and consistency), the meta-analysis also includes spindle amplitude. This may be confusing to readers, as this is not a measurement of SO-spindle coupling but instead a measurement of spindles in general (which may or may not be coupled).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101992.3.sa2](https://doi.org/10.7554/eLife.101992.3.sa2)

This article reviews the studies on the relationship between slow oscillation (SO)-spindle (SP) coupling and memory consolidation. It innovatively employs non-normal circular linear correlations through a Bayesian meta-analysis. A systematic analysis of the retrieved studies highlighted that co-coupling of SO and the fast SP's phase and amplitude at the frontal part better predicts memory consolidation performance.

Regarding the moderator of age, this study not only provided evidence of the effect across all age groups but also the effect in a younger age group (without the small sample of elders that has a large gap from the younger age groups). The ageing effects become less pronounced, but the model still shows a moderate effect.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101992.3.sa3](https://doi.org/10.7554/eLife.101992.3.sa3)

This manuscript presents a meta-analysis of 23 studies, which report 297 effect sizes, on the effect of SO-spindle coupling on memory performance. The analysis has been done with great care, and the results are described in great detail. In particular, there are separate analyses for coupling phase, spindle amplitude, coupling strength (e.g., measured by vector length or modulation index), and coupling percentage (i.e., the percentage of SPs coupled with SOs). The authors conclude that the precision and strength of coupling showed significant correlations with memory retention.

There are two main points where I do not agree with the authors.

First, the authors conclude that "SO-SP coupling should be considered as a general physiological mechanism for memory consolidation". However, the reported effect sizes are smaller than what is typically considered a "small effect" (0.10)

Second, the study implements state-of-the-art Bayesian statistics. While some might see this as a strength, I would argue that it is not. A classical meta-analysis is relatively easy to understand, even for readers with only a limited background in statistics. A Bayesian analysis, on the other hand, introduces a number of subjective choices that render it much less transparent. This becomes obvious in the forest plots. It is not immediately apparent to the reader how the distributions for each study represent the reported effect sizes (gray dots), which makes the analyses unnecessarily opaque. It is commendable that the authors now provide classical forest plots as Figs. S10.1-4.

However, analyses that require a "Markov chain Monte Carlo (MCMC) method, [..] with the no-U-turn Hamiltonian Monte Carlo (HMC) samplers, [..] with each chain undergoing 12,000 iterations (including 2,000 warm-ups)" for calculating accurate Bayes Factors (BF), and checking its convergence "through graphical posterior predictive checks, [..] trace plots, and [..] Gelman and Rubin Diagnostic", which should then result in something resembling "a uniformly undulating wave with high overlap between chains" still seems overly complex. It follows a recent trend in using more and more opaque methods. Where we had to trust published results a decade ago because the data were not openly available, today we must trust the results because methods (including open source software toolboxes) can no longer be checked with reasonable effort.
