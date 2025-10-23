# Peer review - Round 1

Editors:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100258.3.sa0](https://doi.org/10.7554/eLife.100258.3.sa0)

This important work combines theory and experiment to demonstrate convincingly how humans make decisions about sequences of pairs of correlated observations. The proposed model for evidence integration in correlated environments will be of use for the study of decision-making.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100258.3.sa1](https://doi.org/10.7554/eLife.100258.3.sa1)

Summary:

The behavioral strategies underlying decisions based on perceptual evidence are often studied in the lab with stimuli whose elements provide independent pieces of decision-related evidence that can thus be equally weighted to form a decision. In more natural scenarios, in contrast, the information provided by these pieces is often correlated, which impacts how they should be weighted. Tardiff, Kang & Gold set out to study decisions based on correlated evidence and compare observed behavior of human decision makers to normative decision strategies. To do so, they presented participants with visual sequences of pairs of localized cues whose location was either uncorrelated, or positively or negatively correlated, and whose mean location across a sequence determined the correct choice. Importantly, they adjusted this mean location such that, when correctly weighted, each pair of cues was equally informative, irrespective of how correlated it was. Thus, if participants follow the normative decision strategy, their choices and reaction times should not be impacted by these correlations. While Tardiff and colleagues found no impact of correlations on choices, they did find them to impact reaction times, suggesting that participants deviated from the normative decision strategy. To assess the degree of this deviation, Tardiff et al. adjusted drift diffusion models (DDMs) for decision-making to process correlated decision evidence. These fits, and a comparison of different model variants revealed that participants considered correlations when weighing evidence, but did so with a slight underestimation of magnitude of this correlation. This finding made Tardiff et al. conclude that participants followed a close-to normative decision strategy that adequately took into account correlated evidence.

Strength:

The authors adjust a previously used experimental design to include correlated evidence in a simple, yet powerful way. The way it does so is easy to understand and intuitive, such that participants don't need extensive training to perform the task. Limited training makes it more likely that the observed behavior is natural and reflective of every-day decision-making. Furthermore, the design allowed the authors to make the amount of decision-related evidence equal across different correlation magnitudes, which makes it easy to assess whether participants correctly take account of these correlations when weighing evidence: if they do, their behavior should not be impacted by the correlation magnitude.

The relative simplicity with which correlated evidence is introduced also allowed the authors to fall back to the well-established DDM for perceptual decisions, that has few parameters, is known to implement the normative decision strategy in certain circumstances, and enjoys a great deal of empirical support. The authors show how correlations ought to impact these parameters, and which changes in parameters one would expect to see if participants mis-estimate these correlations or ignore them altogether (i.e., estimate correlations to be zero). This allowed them to assess the degree to which participants took into account correlations on the full continuum from perfect evidence weighting to complete ignorance. More specifically, the authors showed that a consistent mis-estimation of the correlation magnitude would not impact the fraction of correct choices (as they observe), but only the reaction times. With this, they could show that participants in fact performed rational evidence weighting if one assumed that they slightly underestimated the correlation magnitude.

Weaknesses:

While the authors convincingly demonstrate that the observed decision-making behavior seems to stem from a slight underestimation of the correlation magnitudes, their experimental paradigm did not allow them to determine the origin of this bias. Through additional analyses they rule out various possibilities, like the impact of a Bayesian prior on estimated correlations. Nonetheless, the authors provide no normative explanation of the observed bias.

A further minor weakness is that the authors only focus on a single normative aspect of the observed behavior, namely on whether participants optimally accumulate decision-related evidence across time. Another question is whether participants tune their decision boundaries to maximize reward rates or some other overall performance measures. While the authors discuss that the chosen diffusion models (DDMs) have the potential of also implementing normative decisions in the latter sense, the authors' analysis does not address this question in the context of their task.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100258.3.sa2](https://doi.org/10.7554/eLife.100258.3.sa2)

This study by Tardiff, Kang & Gold seeks to (i) develop a normative account of how observers should adapt their decision-making across environments with different levels of correlation between successive pairs of observations, and (ii) assess whether human decisions in such environments are consistent with this normative model. The authors first demonstrate that, in the range of environments under consideration here, an observer with full knowledge of the generative statistics should take both the magnitude and sign of the underlying correlation into account when assigning weight in their decisions to new observations: stronger negative correlations should translate into stronger weighting (due to the greater information furnished by an anticorrelated generative source), while stronger positive correlations should translate into weaker weighting (due to the greater redundancy of information provided by a positively correlated generative source). The authors then report an empirical study in which human participants performed a perceptual decision-making task requiring accumulation of information provided by pairs of perceptual samples, under different levels of pairwise correlation. They describe a nuanced pattern of results with effects of correlation being largely restricted to response times and not choice accuracy, which could be captured through fits of their normative model (in this implementation, an extension of the well-known drift diffusion model) to the participants' behaviour while allowing for mis-estimation of the underlying correlations. An intriguing result is that the observed pattern of behavioural effects is best explained by a model in which observers marginally underestimated the level of correlation between the generative sources, and that this bias affects behaviour through effects on stimulus encoding that then shape how the evidence furnished by each stimulus sample is weighted in decision formation.

As the authors point out in their very well-written paper, appropriate weighting of information gathered in correlated environments has important consequences for real-world decision-making. Yet, while this function has been well studied for 'high-level' (e.g. economic) decisions, how we account for correlations when making simple perceptual decisions on well-controlled behavioural tasks has not been investigated. As such, this study addresses an important and timely question that will be of broad interest to psychologists and neuroscientists. The computational approach to arrive at normative principles for evidence weighting across environments with different levels of correlation is elegant, makes strong connections with prior work in different decision-making contexts, and should serve as a valuable reference point for future studies in this domain. The empirical study is well designed and executed, and the modelling approach applied to these data showcases an impressively deep understanding of relationships between different parameters of the drift diffusion model and its novel application to this setting. Another strength of the study is that it is preregistered.

In my view, any major weaknesses of the study have been well addressed by the authors during review. An outstanding question that arises from the current work and remains unanswered here is around the (normative?) origin of the correlation underestimates, and the present work lays a strong foundation from which to pursue this question in the future.
