# Peer review - Round 1

Editors:
- Jeff Gore, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57857.sa1](https://doi.org/10.7554/eLife.57857.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and I found your article to be an insightful perspective regarding why non-transitive (e.g. rock-paper-scissors) interactions might be rare in natural communities, despite the potential stabilizing effects that non-transitive interactions could have in sustaining diversity. In particular, your approach of analyzing the evolutionary origin of different interactions provides fascinating insight to an important problem.

Decision letter after peer review:

Thank you for submitting your article "Why is cyclic dominance so rare?" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Jeff Gore as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Matthieu Barbier (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation, but we encourage you to also consider the substantive points raise below.

Summary:

Cyclic dominance has been proposed as a possible stabilizing mechanism for diversity in communities. However, empirical evidence has suggested that cyclic dominance appears to be rare. Why might this be? The authors' explanation for this observation, based on a dynamical eco-evo model and various theoretical arguments, can be summed up as follows:

– When drawing a network of qualitative dominance relations, it may seem that cyclic dominance could happen often (1/4th of possible triplets if relations are drawn at random).

– But when the interactions arise from an underlying matrix of payoffs, the conditions on payoffs that create cyclical dominance are actually quite constraining, happening at random only in 1/13th of triplets of dominance links (which themselves are only 1/10th of triplets, since dominance is not the only outcome: one can also observe coexistence or bistability).

– And when the payoffs themselves arise from a continuous evolutionary process (where new types are introduced with small changes in payoffs from their ancestors), the probability is even lower. The authors' simulations show that it occurs only in 1/30th of dominance triplets.

The authors provide arguments for why this probability is even lower: it is due to correlations between parents and offsprings. They show in their simulation results that cyclical dominance is associated with more difference between types (measured as an overall difference in their payoffs) than non-cyclical dominance. They also run a simple genealogy process for a 3-type subcommunity (where, instead of each mutation leading to a new type that competes with all the existing types, mutations are now accumulated along genealogical branches as if, for every mutation, the parent type is automatically replaced) to show that cyclical dominance can be favored when many mutations occur after the branching out of the 3 types, thus decorrelating their properties.

Essential revisions:

1) The authors argue the importance of studying cyclic dominance by noting its potential to increase diversity. This paper would, therefore, be strengthened by including an analysis of whether diversity increased in simulations in which cyclic dominance emerged (or at time points during which it was present) as compared to simulations or time points in/at which there was no cyclic dominance. If there is no correlation between the emergence of cyclic dominance and increases in diversity, the authors should address this in the Discussion section. Relatedly, the authors claim in the Discussion "our results indicate cyclic dominance can support diversity over long time scales". We do not believe the first half of this claim (that cyclic dominance can support diversity) is currently supported by their results (it is rather from other literature).

2) For readers to make sense of the triplet analysis it is necessary to know the link frequencies (e.g. between dominance, coexistence, and bistability). This can be brief (no need for a full supplementary figure in main text).

3) The authors argue that it is difficult to evolve cyclic dominance due to mutants being similar to parents. The paper would therefore be strengthened by including an analysis of how the mutation size sigma influences the frequency of cyclic dominance. This is shown for the toy model in Appendix 6, but not for the main model. Many readers would likely appreciate the results of varying sigma within the main model.

4) On a related note, the authors could directly measure and report on the time passed and/or number of mutations accrued since species in cyclic dominance triplets diverged from their last common ancestor and make appropriate comparisons. The current section "Genealogical structure can promote and can suppress cyclic dominance" could be moved to the Appendix if a direct tracing of the genealogy of triplets is added to the paper. (We found the genealogy section to be a bit difficult to parse).

5) The authors could include a brief analysis of how often the species in cyclic dominance triplets gain large population fractions after emerging. This question is relevant because if the three species in a triplet never reach large population fractions then their effects on each other would presumably be small compared to the effects from other members of the population (which would not affect any of the conclusions of this paper but may affect some readers' interpretations of those conclusions).

6) We believe that an outline of the whole argument (a bit like the summary that we give above) should be introduced early in the article, so that the structure is clear: currently, the text reads like a journey where we discover things on the way, but it is not always clear at first why we are doing one thing or another. In particular, something that may not be an issue for theoretical readers, but would be for a more general audience, is that it is not obvious at first which aspects of the model are going to be important or not for the argument, and therefore, whether the results are specific to the model assumptions. In summarizing the results above, we tried to present them in a way that clarifies that a large part of the argument could be made without invoking any specific simulation model. Readers may worry about the interpretation or lack of realism of some assumptions of the dynamics, when they do not really matter for the argument. This is an issue at different points in the paper: for the general eco-evo model, but also for the genealogy "mini-model", where a reader could find it concerning that the process is now different from the main simulation (the text makes it sound as if a type can accumulate mutations without branching out). It would be helpful for the genealogy section to introduce a quick outline of the argument it will make. We also suggest showing the Appendix 5—figure 1A in the main text, maybe as a panel in Figure 5. It would help understand what this mini-model assumes compared to the main simulation model (that all branches except for 3 have disappeared or can be ignored, thus explaining what it means to "accumulate mutations along a branch").

7) Regarding the main simulation model, there is in fact a concern that does not impact the results. A common issue in eco-evo modela is that the evolving traits will keep changing in the same direction, which is generally avoided by imposing some trade-off.

As the authors note, the average payoff here tends to increase indefinitely, which means that all competition coefficients dij eventually converge to just α. In ecological terms, we would call that going toward neutral dynamics (where all individuals have the same competition strength, both within and between types, see S.P. Hubbell's 2001 book). This issue is not deadly because, as differences of dij between types become smaller, all that really happens is that the time it takes for a type to exclude another diverges. But the qualitative nature of the relationships is not changed: there is still dominance or coexistence or bistability, even if by a very small margin. This is simply impractical because one must wait longer and longer for extinctions to actually happen (this is actually theorized in ecology: types could coexist by becoming so similar than one winning over the other takes forever, see Scheffer and van Nes, 2006). So it seems to me that the simulation would have been easier if the payoffs were relative, e.g. constantly setting the average at zero, so that interactions do not converge to neutrality.

In the same spirit:

"For small α values (rich environments) in particular, the population size N at the steady state becomes large, containing many different types " the value of α should change nothing except the biomass scale (population size N ~ M lambda/alpha – incidentally, why introduce parameter M at all? it is never explained). The fact that more types exist for lower α seems like an artefact, perhaps because it takes longer for interactions to tend toward neutrality.

8) Perhaps one could directly show how adding correlations in the matrix diminishes the occurrence of cyclical dominance? This would directly show that nothing else is needed (i.e. that the eco-evo process does nothing more than add these correlations).

9) It is worth noting that there is a large ecological literature about extensions of cyclic dominance to more than triplets, called intransitive competition. Some of that literature has claimed (although we are not necessarily convinced) that intransitive competition is actually common and important. We would suggest reading these articles and figuring out why their claims would be so different – and if that difference is important, then discussing it in the article.

See for instance as starting points: Soliveres et al., 2015; Gallien et al., 2017.
