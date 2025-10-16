# Peer review - Round 1

Editors:
- Matthieu Louis, University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89330.3.sa0](https://doi.org/10.7554/eLife.89330.3.sa0)

This study addresses an important question in sensory neuroscience: how the olfactory system distinguishes decreases in stimulus intensity from decreases in neural responses due to adaptation. Based on a combination of electrophysiological and behavioral analyses, solid evidence establishes that neural coding changes differently between intensity reductions and adaptation, with intensity changes altering which neurons are activated while adaptation preserves the active ensemble but reduces response magnitude. Intriguingly, behavioral responses tend to increase as the neural responses decrease, suggesting that core features of the odor response persist through adaptation. While the experimental results are convincing overall, the conclusions will be strengthened by future work recording behavior and neural dynamics in the same animals.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89330.3.sa1](https://doi.org/10.7554/eLife.89330.3.sa1)

The authors use electrophysiological and behavioral measurements to examine how animals could reliably determine odor intensity/concentration across repeated experience. Because stimulus repetition leads to short-term adaptation evidenced by reduced overall firing rates in the antennal lobe and firing rates are otherwise concentration-dependent, there could be an ambiguity in sensory coding between reduced concentration or more recent experience. This would have a negative impact on the animal's ability to generate adaptive behavioral responses that depend odor intensities. The authors conclude that changes in concentration alter the constituent neurons contributing to the neural population response, whereas adaptation maintains the 'activated ensemble' but with scaled firing rates. This provides a neural coding account of the ability to distinguish odor concentrations even after extended experience. Additional analyses attempt to distinguish hypothesized circuit mechanisms for adaptation. A larger point that runs through the manuscript is that overall spiking activity has an inconsistent relationship with behavior and that the structure of population activity may be the more appropriate feature to consider.

To my knowledge, the dissociation of effects of odor concentration and adaptation on olfactory system population codes was not previously demonstrated. This is a significant contribution that improves on any simple model based on overall spiking activity. The primary result is most strikingly supported by visualization of a principal components analysis in Figure 4. Additional experiments and analysis complement and provide context for this finding regarding the relationship between neural population changes and behavior. There are some natural limitations on the interpretation of these data imposed by the methodology.

(1) Because individual recordings do not acquire a sufficient cell population to carry our population analyses, the cells must be combined into pseudopopulations for many analyses. This is common practice but it limits the ability to test the repeatability of findings across animals or populations. One potential additional solution would be to subsample the pseudopopulation, which would reveal the importance of individual sampled cells in the overall result. The utility of this additional testing is suggested by, for example, the benzaldehyde responses in supplementary figure 5, where two cells differentiate high and low concentration responses and would be expected to strongly impact correlation and classifier analyses.

(2) I do not think the analysis in Figure 2e can be strongly interpreted in terms of the vesicle depletion model. The hard diagonal bound on the lower part of each scatter plot indicates that features of the data/analysis necessarily exclude data in the lower left quadrant. I think this could be possibly explained by a floor effect wherein lower-response neurons cannot possibly express a large deltaResponse. To strengthen this case, one would need to devise a control analysis for the case where neural responses are simply all going as far down as they can go.

(3) Very minor, but it is confusing and not well-described how the error is computed in Figure 1f. One can imagine that the mean p(POR) is arrived at by averaging the binary values across locusts. Is this the case? If so, the same estimation of variance could be applied to Figures 1d and e


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89330.3.sa2](https://doi.org/10.7554/eLife.89330.3.sa2)

Summary:

How does the brain distinguish stimulus intensity reduction from response reductions due to adaptation? Ling et al study whether and how the locust olfactory system encodes stimulus intensity and repetition differently. They show that these stimulus manipulations have distinguishable effects on population dynamics.

Strengths:

(1) Provides a potential strategy with which the brain can distinguish intensity decrease from adaptation. -- while both conditions reduce overall spike counts, intensity decrease can also changes which neurons are activated and adaptation only changes the response magnitude without changing the active ensemble.

(2) By interleaving a non-repeated odor, they show that these changes are odor-specific and not a non-specific effect.

(3) Describes how proboscis orientation response (POR) changes with stimulus repetition., Unlike the spike counts, POR increases in probability with stimulus. The data portray the variability across subjects in a clear way.

Weaknesses:

While POR and physiology can show a nice correlation when measured in different animals, additional insight would be gained from acquiring behavior and physiology simultaneously.
