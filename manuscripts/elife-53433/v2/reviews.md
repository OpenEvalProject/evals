# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53433.sa1](https://doi.org/10.7554/eLife.53433.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Doulcier et al. tackled multi-level community selection: selection at the level of individual cells for fast growth and at the level of whole communities for a desired community property. The authors showed that when selecting communities based on species ratios, the growth rates and the inter-species competition effects can evolve such that a desired species ratio (here 1:1) can be achieved. This work contributes to a growing interest in using multi-level selection to achieve desired community properties.

Decision letter after peer review:

Thank you for submitting your article "Eco-evolutionary dynamics of nested Darwinian populations and the emergence of community-level heredity" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity:); Sara Mitri (Reviewer #2); Alvaro Sanchez (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Doulcier et al. tackled multi-level community selection: selection at the level of individual cells for fast growth and at the level of whole communities for a desired community property. The authors showed that when selecting communities based on species ratios, the growth rates and the inter-species competition effects can evolve such that a desired species ratio (here 1:1) can be achieved. The evolved mechanism is rather intuitive: species Blue grows faster than species Red, but species Blue is subject to competitive inhibition by species Red. This allows the species ratio to be 1:1. Consistent with intuition, when possibilities for competition coefficients are eliminated, growth rates of the two species evolved to be equal. When basal grow rates were not allowed to evolve, asymmetric competition arose to achieve equal post-competition growth rates. All three reviewers are positive about this work.

Essential revisions:

1) Allowing ecological interactions to evolve to be positive.

2) Statistics of simulation repeats.

3) What happens if selecting for uneven ratios when noise is present?

4) What does "rapidly" really mean?

To help you revise, the original reviews are attached.

Reviewer 1:

1) Define "interactions".

2) "Developmental correction" is a biologist's way of saying "steady-state species ratio" or "attractor/fixed point". There are multiple ways of achieving steady-state species ratios. The authors had limited species interactions to competition (non-positive coefficients). If they allow interactions to change signs, then commensal or mutually beneficial interactions can arise to stabilize strain ratios. "Developmental correction thus selects for maximal asymmetry in interactions" may no longer hold for positive interactions. This needs to be checked.

Reviewer #2:

In this manuscript, the authors set out to explore whether it's possible to select for phenotypes at the community level, that arise in spite of competition between community members at the individual level. Using a computational model, they show that this is indeed possible, but relies on communities being properly enclosed and only passing on their individuals to their own offspring communities. They also analyse the strategy allowing for the evolution of community phenotypes. They show that community members evolve individual phenotypes that allow them to robustly converge to the community property under selection, independently of the initial community state. They posit that a similar mechanism might explain major evolutionary transitions, allowing lower level entities to be selected as whole entities.

Overall, we like the manuscript. It makes, in our opinion, a major contribution in understanding how competition between individual community members can be overcome – or even used – to allow for selection of the community phenotype. The idea that selection can favor individual-level parameters that have a functional form that increases resemblance between parent and offspring and robustness to initial conditions is very interesting and overcomes some of the issues with community selection observed in previous studies (Xie et al). The authors also nicely show that once this strategy has evolved, it is ecologically stable, and they explore how the evolutionary trajectory depends on starting conditions.

We have some general thoughts that we think are worth discussing further in the manuscript.

First, what we find was missing were statistics on what happens on different runs of the simulation. As far as we could tell, all data shown is based on individual "example" runs. The authors claim that these are general, but there is no data to support that. Please add statistics on the repeatability of the results. A related point: is the outcome always qualitatively similar? Specifically that a) the faster grower becomes less competitive with respect to growth rate, and b) that the emerging population regulation consists of the slower grower suppressing the faster grower while c) the faster grower does not affect the slower. It was not clear to us why, and we believe this is important to understanding the conclusion of the paper.

Second, we believe the authors could elaborate more on the specificity of their system and how their findings depend on them. It is not clear to what extent the same result would be observed in a different system that (1) has more than 2 types, (2) where selection acts on total abundance rather than ratios of two colors, (3) where the selective regime is different (the authors say "A non-exhaustive exploration of other selection rules indicates that the qualitative results of the model are robust to changes in the selective regime, as long as collectives with an optimal colour are favoured and the collective population does not go extinct." It would be worth expanding on this in the supplement); and finally, (4) where the phenotype being selected for is not intermediate. Would this work equally well if the phenotype selected is almost blue or almost red? In short, under what general conditions do you expect to see the same?

From the ecological literature, it is known that coexistence between two competing types requires some limiting force for the strongest grower (e.g. predator). Is that simply what you are selecting for? It may be good to make a link to this literature.

We are also unsure about the parallels made to developmental processes and think this would merit some clarification. Does one see this strategy where a slower-growing type limits the growth of a faster-growing one? Or are the authors hypothesizing that this might explain how smooth developmental processes occur?

Finally, Figure 2 is lacking in visual clarity (color scheme). The selection method should also be better explained in the main text.

Please note that we did not work through all the math nor run the code.

Reviewer #3:

I very much enjoyed this paper. I do not have any significant concerns.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for re-submitting your article "Eco-evolutionary dynamics of nested Darwinian populations and the emergence of community-level heredity" for consideration by eLife. Your article has been re-reviewed by two of the three original reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The only thing that we believe is still missing is a paragraph in the Discussion on the generality of these findings. We understand that adding more than 2 types, trying different selection regimes or selecting on total abundance is beyond the scope of the current manuscript, but we still believe these questions may remain for a reader of the paper, so it is worth bringing them up in the Discussion as future directions.
