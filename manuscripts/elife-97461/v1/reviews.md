# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97461.3.sa0](https://doi.org/10.7554/eLife.97461.3.sa0)

This important study of artificial selection in microbial communities shows that the possibility of selecting a desired fraction of slow and fast-growing types is impacted by their initial fractions. The evidence, which relies on mathematical analysis and simulations of a stochastic model, is compelling. It highlights the tension between selection at the strain and the community level. This study should be of interest to researchers interested in ecology, both theoretical and experimental.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97461.3.sa1](https://doi.org/10.7554/eLife.97461.3.sa1)

Summary:

The authors demonstrate with a simple stochastic model that the initial composition of the community is important in achieving a target frequency during the artificial selection of a community.

Strengths:

To my knowledge, the intra-collective selection during artificial selection has not been seriously theoretically considered. However, in many cases, the species dynamics during the incubation of each selection cycle is important and relevant to the outcome of the artificial selection experiment. Stochasticity from birth and death (demographic stochasticity) plays a big role in these species' abundance dynamics. This work uses a simple framework to tackle this idea meticulously.

This work may or may not be related to hysteresis (path dependency). If this is true, maybe it would be nice to have a discussion paragraph talking about how this may be the case. Then, this work would even attract the interest of people studying dynamical systems.

Weaknesses:

(1) Connecting structure and function.

In typical artificial selection literature, most of them select the community based on collective function. Here in this paper, the authors are selecting a target composition. Although there is a schematic cartoon illustrating the relationship between collective function (y-axis) and the community composition in the main figure 1, there is no explicit explanation or justification of what may be the origin of this relationship. I think giving the readers a naïve idea about how this structure-function relationship arises in the introduction section would help. This is because the conclusion of this paper is that the intra-collective selection makes it hard to artificially select for a community that has an intermediate frequency of f (or s). If there is really evidence or theoretical derivation from this framework that indeed the highest function comes from the intermediate frequency of f, then the impact of this paper would increase because the conclusions of this stochastic model could allude to the reasons for the prevalent failures of artificial selection in literature.

(2) Explain intra-collective and inter-collective selection better for readers.

The abstract, the introduction, and the result section use these terms or intra-collective and inter-collective selection without much explanation. For the wide readership of eLife, a clear definition in the beginning would help the audience grasp the importance of this paper, because these concepts are at the core of this work.

(3) Achievable target frequency strongly depending on the degree of demographic stochasticity.

I would expect that the experimentalists would find these results interesting and would want to consider these results during their artificial selection experiments. The main figure 4 indicates that the Newborn size N0 is a very important factor to consider during the artificial selection experiment. This would be equivalent to how much bottleneck you impose on the artificial selection process in every iteration step (i.e., the ratio of serial dilution experiment). However, with a low population size, all target frequencies can be achieved, and therefore in these regimes, the initial frequency now does not matter much. It would be great for the authors to provide what the N0 parameter actually means during the artificial selection experiments. Maybe relative to some other parameter in the model. I know this could be very hard. But without this, the main result of this paper (initial frequency matters) cannot be taken advantage of by the experimentalists.

(4) Consideration of environmental stochasticity.

The success (gold area of Figure 2d) in this framework mainly depends on the size of the demographic stochasticity (birth-only model) during the intra-collective selection. However, during experiments, a lot of environmental stochasticity appears to be occurring during artificial selection. This may be out of the scope of this study. But it would definitely be exciting to see how much environmental stochasticity relative to the demographic stochasticity (variation in the Gaussian distribution of F and S) matters in succeeding in achieving the target composition from artificial selection.

(5) Assumption about mutation rates

If setting the mutation rates to zero does not change the result of the simulations and the conclusion, what is the purpose of having the mutation rates \mu? Also, is the unidirectional (S -> F -> FF) mutation realistic? I didn't quite understand how the mutations could fit into the story of this paper.

(6) Minor points

In Figure 3b, it is not clear to me how the frequency difference for the Intra-collective and the Inter-collective selection is computed.

In Figure 5b, the gold region (success) near the FF is not visible. Maybe increase the size of the figure or have an inset for zoom-in. Why is the region not as big as the bottom gold region?

Comments on revisions:

I thank the authors for addressing many points raised by the reviewers. Overall, the readability of the manuscript has improved with more context provided around why they were solving this specific problem. However, I've found many of the responses to be too terse. It would have been nicer if there had been more discussion and description of the thought process that led up to the conclusions they made for each comment or question. Instead, many of the responses only showed the screenshot of the text they added.

Most of my comments or questions were answered. Below are my comments on some of the authors' responses.

(2) Explain intra-collective and inter-collective selection better for readers.

In the Abstract and Introduction, you've added more sentences about the intra-collective or inter-collective selection. However, these are either making analogies to the waterfall or just describing the result of the intra/inter-collective selection. I would still appreciate a proper definition of those terms, which is paramount for readers to understand the entire paper.

(4) Consideration of environmental stochasticity.

I think providing the reason 'why' the paper focuses on demographic stochasticity and not environmental stochasticity will greatly justify the paper's work. For example, citing papers that actually performed artificial selection and pointing out that your model captures the stochasticity from those kinds of experiments would be great.

(5) Assumption about mutation rates.

It would be great if you could add a citation in the added sentence to support your claim: "This scenario is encountered in biotechnology: .....".


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97461.3.sa2](https://doi.org/10.7554/eLife.97461.3.sa2)

The authors address the process of community evolution under collective-level selection for a prescribed community composition. They mostly consider communities composed of two types that reproduce at different rates, and that can mutate one into the other. Due to such difference in 'fitness' and to the absence of density dependence, within-collective selection is expected to always favour the fastest grower, but collective-level selection can oppose this tendency, to a certain extent at least. By approximating the stochastic within-generation dynamics and solving it analytically, the authors show that not only high frequencies of fast growers can be reproducibly achieved, aligned with their fitness advantage. Small target frequencies can also be maintained, provided that the initial proportion of fast growers is sufficiently small. In this regime, similar to the 'stochastic corrector' model, variation upon which selection acts is maintained by a combination of demographic stochasticity and of sampling at reproduction. These two regions of achievable target compositions are separated by a gap, encompassing intermediate frequencies that are only achievable when the bottleneck size is small enough or the number of communities is (disproportionately) large.

A similar conclusion, that stochastic fluctuations can maintain the system over evolutionary time far from the prevalence of the faster-growing type, is then confirmed by analyzing a three-species community, suggesting that the qualitative conclusions of this study are generalizable to more complex communities.

I expect that these results will be of broad interest to the community of researchers who strive to improve community-level selection but are often limited to numerical explorations, with prohibitive costs for a full characterization of the parameter space of such embedded populations. The realization that not all target collective functions can be as easily achieved and that they should be adapted to the initial conditions and the selection protocol is also a sobering message for designing concrete applications.

A major strength of this work is that the qualitative behaviour of the system is captured by an analytically solvable approximation so that the extent of the 'forbidden region' can be directly and generically related to the parameters of the selection protocol.

The phenomenon the authors characterize is ecological in nature, though it is maintained even when switching between types is possible. Calling this dynamics community evolution reflects a widespread ambiguity in the field, not ascribable just to this work.

Although different types compete for being represented in the next generation's propagules, within-generation ecology is here representative of exponential growth. As species interactions are commonly manifest in lab serial dilution experiments, it would be interesting if future work explores the extent of the robustness of these results to density-dependent demography.
