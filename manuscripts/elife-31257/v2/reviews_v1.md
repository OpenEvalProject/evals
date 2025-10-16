# Peer review - Round 1

Editors:
- Neil M Ferguson, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31257.037](https://doi.org/10.7554/eLife.31257.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "MERS-CoV spillover at the camel-human interface" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Prabhat Jha as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Erik Volz (Reviewer #1); Christophe Fraser (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, Dudas et al. perform a coalescent analysis of 274 MERS-Cov viruses. They conclude that 1) MERS is sustained in camels (R0>1) and not in humans (R0<1), and that most if not all cross species transmissions have been camel to human. 2) Cross species events are seasonal, but R0 in humans isn't. 3) The relatively low levels of genetic diversity in camel viruses can be explained by camel demography.

Essential revisions:

1) The population genetic model (the particular form of structured coalescent) is highly idealised and this may influence the quantitative conclusions, although we suspect the conclusions are quite robust qualitatively. This model specifically estimates the rate of a lineage moving between demes going backwards in time; the numbers cited for the camel->human rate is really the rate that a lineage in humans goes to a camel going down the tree. The relationship between these migration rates and the epidemiologically meaningful transmission rate is complex and depends among other things on the ratio of population sizes in both demes. Per-capita transmission rates could be estimated using an epidemiologically structured coalescent model (see e.g. papers by Volz and Rasmussen), which would ideally be stochastic due to bursty dynamics in humans. But this would be a large undertaking and so we suggest that for now the distinction is clarified. Overall, a little more discussion of the complexity and pitfalls when relating idealised population genetic models (like the island model used here) to a noisy nonlinear epidemic like this one might be merited.

2) 'Our analyses recover these results despite sequence data heavily skewed towards non-uniformly sampled human cases and are robust to choice of prior.' This is a quite nice result and raises the question if skewed sampling would bias estimates if using a substitution model approach ('discrete trait analysis', DTA). It would strengthen the paper to include a comparison of the structured coalescent estimates to another method for ancestral states; the most popular approach in beast has been substitution models (DTA). These may give divergent results because of skewed sampling. It would be rather easy for the authors to run a DTA and if biased, this would serve as a good cautionary example when sampling is highly skewed towards one deme.

3) A comparison to ML tree reconstruction could potentially be illuminating. We think you could be clearer about what drives the results in your paper. It is unusual for a phylogenetic ancestral reconstruction, that the results seem to be determined as much by the coalescent assumptions as by the tree topology. The two-patch model had a much higher coalescent rate in the human deme than in the camel deme – so long branches are only really possible in the camel deme. This may be why for example, staring at the top clade of Figure 1, one can see camel ancestry to a whole bunch of human sequences that are not topologically separated by camel sequences. If this is correct, these results may not necessarily be wrong, but it made us slightly uncomfortable that the results are driven by the coalescent model, not the tree topology. Please elaborate, either correcting us, or explaining better. A simple test of this hypothesis would be that an ML ancestral reconstruction on the ML tree would not give the same clusters. I don't think that would make the ML result correct, but it might be an enlightening comparison. Or you may prefer another way to address this.

4) Easily addressed, but important. The paper already sounds a strong voice of concern in the final paragraph, but we think this could be even stronger. Antia et al. Nature 2003 first showed, using a simple branching process, that for most genetic landscapes, the probability of a pathogen evolving to state with R0>1 increases dramatically as a function of the wild-type R0. So R0~0.8 is much worse than R0~0.3. More sophisticated models have been done since, especially by Llyod-smith's group, but the basic result is sound. In the light of this theoretical work, your findings are not at all reassuring.

5) More generally, the model choices need better explaining. Why delve into a structured coalescent in BEAST2 for the ancestral reconstruction, but go back to the Skygrid in BEAST1 for computations of Ne? We assume this is a pragmatic choice, and for the latter you carefully reduced the human clusters to reduce bias, but we think the rationale for your choices need laying out more clearly. Even if pragmatic rather than principled, (e.g. there are no structure coalescent options in BEAST1), we think it still needs to be stated why you made the choices you did. Especially since there are other recently-developed BEAST2 packages that could be used to fit the same structured coalescent model: BASTA and MASCOT, as well as the very flexible PhyDyn package (which might offer improvements in computation time).
