# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84662.sa0](https://doi.org/10.7554/eLife.84662.sa0)

This important study proposes a phenomenologically motivated theoretical framework to explain observed patterns of the temperature dependence of microbial diversity. The methodology is overall convincing. The manuscript should be of interest to microbial ecologists.


---

# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84662.sa1](https://doi.org/10.7554/eLife.84662.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Variation in thermal physiology can drive the temperature-dependence of microbial community richness" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1) Please clarify, and spell out in detail, what assumptions and approximations are made in calculations, and at what stages. In the presentation of the mean-field approximation, it should be explicitly said that extra have been made approximations (e.g. when computing the mean of the inverse). Moreover, given these approximations, it is important to clarify when they break down and when they work well, both with explanations and concrete examples.

2) Please clarify the manuscript. In particular, please clearly define each notation and motivate parameter or function choices. Please address all of the reviewers' points to improve this.

3) Please discuss why a consumer-resource model was not chosen and what it might change. Please also discuss the motivation of the temperature dependence of the interaction parameters.

Reviewer #1 (Recommendations for the authors):

1) The derivation of the mean field result is not correct. It may hold in some specific conditions that are not properly discussed. The problem is after Eq. (8) of the Methods section. Tacking the average across the N populations does not lead to the following equation for the average stationary population. In fact, denoting by 〈∙〉 the average, then the mean field consistency equation should read: x∗¯=⟨riaii⟩+(N−1)aij¯⟨1aii⟩x∗¯ but ⟨riaii⟩ ≠ ⟨ri⟩⟨aii⟩ and ⟨1aii⟩ ≠ 1⟨aii⟩. Therefore, the mean field result presented in the paper, in general are not correct. In some specific cases, e.g. the random variables aii is sharply peaked around its mean, then it may hold that ⟨riaii⟩ ≈ ⟨ri⟩⟨aii⟩ and ⟨1aii⟩ ≈ 1⟨aii⟩.

Decision letter images 1, 2 and 3 show numerically the comparison of ⟨riaii⟩ with ⟨ri⟩⟨aii⟩ 〈ariii〉 with 〈〈ariii〉〉 and of ⟨1aii⟩ with 1⟨aii⟩ for three different cases (mean and variances highlighted as plot label):

So it is clear that actually, in the log-normal case, that should be the actual distribution from where ri and aii have been drawn, the average of the ratio of the two random variables cannot be substituted with the ratio of the averages.

Relatedly, given the above results, it is not clear to me, how it is possible that the approximation proposed by the authors work so well, for example in Figure 2. Moreover, it is not clear to me how ri, aij and aii are chosen in the numerical simulation of the full GLV. Are they drawn from a LogNormal distribution? Just after Eq. 2 it seems that indeed they are lognormal distributed, but this should be specified better in the Figures and also it is necessary adding information about which parameters have been used. Moreover, how much the goodness of the analytical approximation depends on the specific choices of the parameters? I think that a sensitivity analysis and related discussion on the limitation of the analytical approximations are needed.

In general, I think that it should have been more appropriate to perform a more advanced mean field approximation, for example following the work “Collapse of resilience patterns in generalized Lotka-Volterra dynamics and beyond” (Tu, C., Grilli, J., Schuessler, F., and Suweis, S. (2017). Physical Review E, 95(6), 062307), from which a similar approximation of the effective average population could be derived. Moreover, using this approximation, it is possible to go beyond purely competitive ecosystems, as it holds also for communities with mutualistic interactions. In fact, the statement that GLV only works for competitive communities is not correct (there are many works using GLV with (also) positive interactions (e.g. Rohr, Rudolf P., Serguei Saavedra, and Jordi Bascompte). "On the structural stability of mutualistic systems." Science 345.6195 (2014): 1253497; Suweis, S., Simini, F., Banavar, J. R., and Maritan, A. (2013). Emergence of structural and dynamical properties of ecological mutualistic networks. Nature, 500(7463), 449-452.).

While it is quite clear the physiological dependence of the growth rate on temperature, it is not quite evident why also the interactions strengths should depend on the interactions strengths aij. How the works conclusions would change if only ri depends on time (see also Abreu, C. I., Dal Bello, M., Bunse, C., Pinhassi, J., and Gore, J. (2022). Warmer temperatures favor slower-growing bacteria in natural marine communities. bioRxiv).

The section The theory holds in dynamically-assembled communities is hard to read, as it lacks of the definition of what is a dynamically-assembled community, how it is mathematically defined and why you also want to explore such a case. Some information must be available in the main text, some other you can refer (but please explicitly put the link) to the Methods section.

Reviewer #2 (Recommendations for the authors):

In their paper Variation in thermal physiology can drive the temperature dependence of microbial community richness, Clegg and Parwar present a relatively simple phenomenological model for explaining the wide variety of empirically observed relationships between temperature and diversity in the microbial world. Previous theories such as the Metabolic theory of biodiversity (MTB) and the metabolic niche hypothesis have emphasized the role of energy through either more efficient cellular kinetics or temperature dependent niches. This paper builds on these works by showing that if one accounts for variation of temperature sensitivity across species, one can get a much richer set of behaviors consistent with empirical observations.

Overall, I find the manuscript quite compelling and the model presented as a very nice summary of how variability in temperature dependence, simple Arrhenius scaling, and arguments based on modern coexistence theory can be combined to explain empirical observations of species abundance distributions and temperature. I find Figures 2 and 3 quite interesting and they have the virtue of resolving a major puzzle in the current literature and proposing concrete mechanistic hypothesis. For all these reasons, I think this manuscript makes an important contribution to the literature and I recommend publishing in eLife.

However, I do have some comments and concerns that I think would be helpful for the authors to address.

I feel like the manuscript is too terse and hard to follow. For example, the parameter E is not defined explicitly anywhere in the main text. I would suggest that the incorporating thermal responses of traits (including Equations 13 and 14) be moved to the main text and this discussion greatly expanded. I could not follow what was going on.

I do not understand the physical/ecological motivation for logB0 and E are anti-correlated. Does this follow from theory or empirical fits? How do we know that the experiments from Smith et al. hold more generally?

Currently, parameters are drawn from a log-normal distribution. This means that it is long-tailed. Do the general trends they hold for non-long tailed distributions. I understand that the ri must be positive, but this can be done by for example, using a truncated Gaussian. If the long tails are essential, could you please explain why the tails matter? The form of ¯r below Eq. 15 would suggest that the results here may depend very strongly on the long tailed distribution assumption. It would be nice to understand how the phenomenology changes if this is not the case.

I feel like the averages below equation 7 are done sloppily. The agreements with numerics suggest these are small effects but in reality we have that

x∗=1N∑ixi∗=1N∑i(riaii−(N−1)1N)∑ia¯IIaiix¯∗ (1)

Notice that in general that

1N∑i(riaii≠r¯a¯ii,) (2)

since this is not how averages work. A similar thing holds for the second term. For this reason, the expressions are not correct even under the MFT assumption. Numerics suggest this does not matter but this approximation should be made more clear.

The caption for Figure 4 seems to be cut-off.

Can the author please discuss why they think the predictions of Figures 3b,c fail in greater detail?

Reviewer #3 (Recommendations for the authors):

I think the paper does make inroads into an important question, and the focus on the temperature-dependence of species interactions does go beyond what has been assumed e.g. in metabolic theory. My main questions are detailed in the public review. Namely:

- To what extent is the mean-field approximation for x* (which I think can be interpreted as an approximation for the inverse of a matrix with entries a_ij) valid for the full range of values of a_ij.

There is also a long literature on feasibility analyses, going back at least to the `70s (e.g. Goh and Jennings, 1977, Ecological Modeling), and some of this is pertinent e.g. in relating to the authors' results for the probability of feasibility and how this depends on the number of species present. It would be helpful to engage with this literature.

- In general, I do not fully understand the justification for the functional forms of growth rate and interaction rate on temperature. The latter (the way the a_ij are assumed to depend on the temperature) seems particularly difficult to pin down. Is there any clear justification for this form?

- Whatever the temperature dependence, in Lotka-Volterra it seems inevitable that this will be a phenomenological assumption. The way the authors build up in the introduction, I thought they were headed towards a consumer-resource model, maybe even with intracellular dynamics determining the temperature dependence of interactions. This would be the approach e.g. of the Droop model (also going back to the 70s), or e.g. work from a couple of years ago (Muscarella and O'Dwyer, 2020). I am not claiming that we can't drop explicit resources, reduce to Lotka-Volterra, and make progress. But it makes it hard to understand how robust the results are to the authors' assumptions about the way Lotka-Volterra parameters change with environmental context.
