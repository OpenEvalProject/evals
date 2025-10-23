# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75353.sa0](https://doi.org/10.7554/eLife.75353.sa0)

This is a rigorous evaluation of whether the compression of time cells in the hippocampus follows the Weber-Fechner Law, using a hierarchical Bayesian model that simultaneously accounts for the firing pattern at the trial, cell, and population levels. The two key results are that the time field width increases linearly with delay, even after taking into account the across trial response variability, and that the time cell population is distributed evenly on a logarithmic time scale.


---

# Peer review - Round 1

Editors:
- Hugo Merchant, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75353.sa1](https://doi.org/10.7554/eLife.75353.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Internally Generated Time in the Rodent Hippocampus is Logarithmically Compressed" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Recommendations for the authors:

The authors state that "The goal of the analyses in this paper is to rigorously test the hypothesis that time cells form a logarithmically-compressed representation of past time." While the authors made great strides and this rigorous analysis, unfortunately, no other hypothesis was really considered. It is common in timing tasks that subjects learn some rote behavioral sequence that happens to match the target interval. Therefore, correlates observed anywhere in the brain cannot uniquely be attributes to time, or that behavioral sequence. Moreover, it is not clear in the present report if the animals have actually learned the target duration and therefore have some representation of that duration. To pose the question in an actionable and concrete manner: what differs about the trials when time fields occur earlier than expected versus later? I strongly recommend that the authors classify each trial as an early firing versus late firing trial (or some other demarcation) and revisit the videos to assess whether animal behavior can explain any variability. My guess is that the behavior is more variable late into the treadmill running, and this could likely explain the variability of the firing fields.

Another major comment pertain to the nature of the statistical modeling. It is not totally clear what data is being used for the goodness-of-fit analysis, though it appears to be single trial firing rates. Are these smoothed? What is the bin size? These issues are important because a main focus of the manuscript is on trial-to-trial variability. The authors use their model to describe a conditional intensity function (equation 2), which is then tested directly with the spiking output. Typically, spikes are thought of as being probabilistically generated from an underlying intensity function and often Poisson link functions are used to translate between the world of stochastic events (spikes) and the world of the underlying, deterministic intensity functions (e.g. equation 2). How can the authors justify a direct estimation of the intensity function?

The authors test which coefficient best describes the power-law distribution of M in the hierarchical bayes model. No other distribution is considered, and then much of the paper is dedicated to a description of the implication of logarithmically compressed time field allocation. First, other distributions should be considered and compared (i.e. with AIC), and second, credible interval analysis should be used to motivate that the coefficient of the power law is not different from one (e.g. Keysers et al., 2020, https://dx.doi.org/10.1038%2Fs41593-020-0660-4).

Other models, and empirical observations, suggest skewed receptive fields that significantly differ from Gaussian – do the findings hold if the assumption of a Gaussian tuning is relaxed and other functions are considered (e.g. α function)?

The pairwise analysis for consistent shifts in the time field location is interesting though the effect seems modest. Two points, (1) since the authors are working within a Bayesian framework, confidence intervals and effect sizes can be given through an analysis of credible intervals (Keysers et al., 2020, https://dx.doi.org/10.1038%2Fs41593-020-0660-4), (2) Is it possible to leverage more than just a pairwise analysis since the authors conducted high density recordings. Several recent methods exist for such an analysis, such as Williams et al., 2020 https://doi.org/10.1016/j.neuron.2019.10.020, or Kawabata et al., 2020 https://doi.org/10.1152/jn.00200.2020. Similarly, a hidden markov model approach could be fruitful as well (Chen et al., 2012, https://dx.doi.org/10.1007%2Fs10827-012-0384-x).

In Figure 4c, the curved dashed line shows a sparsification of the putative temporal representation of long intervals. One issue is that, as the authors quantify, the time fields at the later delays are broader and show more variability. How does the compression differ with more relaxed inclusion criteria? This issue is important as the inclusion criteria (“a Gaussian-shaped time field, with a mean and a standard deviation, and a constant term”) select specifically for fields that show high trial-to-trial reliability (e.g. early fields). The authors must report how many total neurons per rat were recorded and what percentage was included/excluded.

Figure 5b – To my eye, it looks like there are a number of cells with low width throughout the interval hovering around the bottom of this graph and, at later peak times, across a gap from 0.25-0.5. I’m curious what the authors think about these cells. Are they merely outliers, or are there possibly subsets of cells that retain strong temporal fidelity even far into the interval? Is it possible to use unsupervised learning techniques like k-means clustering to find differences between these cells and the other ones which seem to follow the logarithmic law? Are there differences in the overall firing rates or any other properties? If there end up being different classes of cells, that would not invalidate the overall conclusion, but could be a novel discovery, And it could make the relationship with the other set of cells even stronger.

If I were of the opinion that a number of cells simply fired due to the onset of the event (as they would to an event boundary) and had different onset times as a result of the beginning of the interval due to the sudden change (Bright et al., 2020) but did not believe that variability increased thereafter, how would the authors address this? I realize this is tricky because it is not clear at what time point one may not consider a response to be directly related to some onset, but if the relationship in Figure 4b held when only investigating cells with peak firing times between two seconds and the end of the interval, that would address the concern.

In the regression analysis at the bottom of page 7, is the argument that the linear significance is relevant here? If so, the authors should make this more explicit, especially because the quadratic aspect looks so prominent.

“Section S1 of the supplementary materials provides an elementary explanation of why logarithmic compression leads to these properties.” It would be preferable to include a brief description of this logic in the main paper.

In discussing the Nielson Study, it seems highly relevant that the relationship between representational similarity and both space and time was logarithmic. It would also be nice to include the neurophysiological timing literature on the scalar property of timing. Recordings in the primate medial premotor areas during rhythmic timing have shown neural sequences linked with temporal processing (Crowe et al., 2014i; Merchant et al., 2015 i) and neural population codes that could underpin the scalar property of timing (Averbeck and Merchant, 2017; Gamez et al., 2019).
