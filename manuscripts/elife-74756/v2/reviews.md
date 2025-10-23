# Peer review - Round 1

Editors:
- Yuuki Y Watanabe, https://ror.org/05k6m5t95 National Institute of Polar Research Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74756.sa0](https://doi.org/10.7554/eLife.74756.sa0)

This study will be of interest to wildlife ecologists and conservation practitioners. The authors took a collaborative approach and collated a large dataset of wildlife camera trap recordings across cities in the USA. The analyses reveal variability in diel activity among species and cities, providing important insights into the effects of urbanization.


---

# Peer review - Round 1

Editors:
- Yuuki Y Watanabe, https://ror.org/05k6m5t95 National Institute of Polar Research Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74756.sa1](https://doi.org/10.7554/eLife.74756.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mammals adjust diel activity across gradients of urbanization" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Yuuki Watanabe as the Reviewing Editor and Christian Rutz as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Daniel Cox (Reviewer #1); Jason T Fisher (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this decision letter to help you prepare a revised submission.

Essential revisions:

Both reviewers agreed that this is an interesting study, and their comments are mostly suggestions for better presentation and enhanced clarity regarding the methods. You are encouraged to refine the manuscript as much as possible by considering the comments provided in the original reports below.

Reviewer #1 (Recommendations for the authors):

The introductory paragraph could do with tightening to fully capture the broad range of different time partitioning strategies.

L58: Persist is the wrong term here. Many species positively thrive in urban areas and do better than they do in the wider countryside.

L66-68: Rather than limit this to the two examples given, I feel it would be better to give the broad range of external factors that can cause species to shift their activity e.g. predator-prey relationship, thermoregulation, food availability, local climatic conditions, high seasonal variability or unpredictability, lunar cycles, competition, apex predators, etc.

L100-101: Carnivores can also be thought of as a special case with their diel niches because they are inherently flexible in their activity and many have a 'cathemeral eye'.

L112-114: Before reaching the rest of the manuscript, it would be helpful here to further clarify the differences between objectives 1 and 2. Possibly give an example of the changing behavior that is expected?

L131: It would be helpful to provide a link to the website for the 'urban wildlife network' at the first mention, because many readers will not have heard of it.

L132-135: For the non-US readers, it would be helpful to include a map in the SI showing the distribution of the cities. I would also suggest, either removing the states or giving the full spelling.

L155: I am not sure what the 'softmax function' is at this stage of the manuscript. I would suggest either clarifying or removing and leaving the explanation to the methods.

L213-214: Figure 3g suggests that eastern cottontails were more likely to select diurnal hours as temperatures increase? As shown in Figure 2 and 3.

L265: Should you be citing phylopic www.phylopic.org here or equivalent?

L322-333: Rather than becoming more diurnal from human pressures, it may be that the primary driver of increased diurnal activity is to avoid increased activity in nocturnal predators (see Mills and Harris 2020).

L427: For readers who don't know, they might be interested to know that astronomical sunrise and set is when the sun goes above -18 degree.

L435: I think that the term 'darkest hours' is misleading. Artificial light at night is prevalent throughout urban areas, with strong levels of skyglow even if there are no direct sources close to the camera traps. It would be better to rename this period along the lines of the 'quietest hours', because mammal diel activity is to do with the lack of human activity as opposed to illumination.

On this topic it is a shame that no data were available that measured ALAN at each site. ALAN allows species with high visual acuity (a diurnal adaptation) to operate at night. It would have been interesting to test whether this was a dominant effect driving activity patterns.

The following reference might be useful https://onlinelibrary.wiley.com/doi/full/10.1111/ecog.05251

L443-448: Nicely done.

L450: I assume you mean average daily temperature? Is this not just a repetition of what comes below?

L453: Possibly just to clarify, add 'within each species fixed radius buffer.'

L460: Are these two nature feature variables not highly correlated?

L483: I have some experience of non-Bayesian multinomial modelling and can appreciate the difficulty of explaining it. I think much of the below can be clarified with a careful explanation here of what the different parts are. The authors assume too much and need to spell out more clearly how the categorical model works.

So, there are 5 K categories (dark night, night, dawn, dusk, day).

Why k and K?

k in 1?

'…of the ith in 1,….' What does this mean?

Why a categorical 'random' variable?

1⋅ ɸ = 1 – is this shorthand for stating that the sum of probabilities across the 5 diel activities is equal to 1?

L492: First, mention of the softmax function in the methods. Is this function equation 2? Further, an explanation is required to state what a softmax function is and what it does.

L496: Are k and K the same thing? This would suggest they are?

How does the model control for zero-inflated data (i.e., all the camera traps where the species was not recorded)?

L500: How was the random intercept for each city obtained? Can this not be controlled for by simply including the city as a random factor in the model?

Possibly also expand the explanation into the SI?

L519: As a general point for readers wanting to repeat this analysis, which they might well do given the increased interest in activity patterns, throughout the paper the individual functions should be given along with the R packages.

Figure 3: It might look good if you could also add the silhouettes in Figure 4 to the top right of each panel in Figure 3 and Figure 2?

Table S2: Why not give full state names in the table heading?

Table S3: It would be clearer if full city names are also given.

Dryad link on the manuscript does not work, and nothing comes up when the paper title is searched for within Dryad.

Literature cited:

Mills and Harris (2020) Human disrupt access to prey for large African carnivore. eLife, 9, e60690.

Reviewer #2 (Recommendations for the authors):

Introduction: I mentioned in the public review that your background on using camera traps to analyze diel activity is a little sparse. A review is available, which also highlights some challenges the authors have not apparently considered in the paper. It's not necessary to cite it (it is my paper) but the content may prove useful (Frey et al., 2017).

Line 84: Again it's not necessary to cite this paper (as it's mine) but Frey et al., (2020) refute the simplistic patterns shown in Gaynor et al., (2018) and demonstrate that species adjust their diel cycle according to multiple perceived risks – cascading from top predators to mesopredators. I see you suggest this as a mechanism for foxes/coyotes in Lines 310-381; might be good to lend some support to your argument.

Lines 223-225: I did not understand this logic – why did you combine night/darkest night because dusk/dawn probabilities were low?

Line 302: Formatting of reference "M.I. Grinder and Krausman".

In my version, Figure 2 is quite small.

Frey, S., J. T. Fisher, A. C. Burton, and J. P. Volpe. 2017. Investigating animal activity patterns and temporal niche partitioning using camera‐trap data: Challenges and opportunities. Remote Sensing in Ecology and Conservation 3:123-132.

Frey, S., J. Volpe, N. Heim, J. Paczkowski, and J. Fisher. 2020. Move to nocturnality not a universal trend in carnivore species on disturbed landscapes. Oikos 129:1128-1140.

Ridout, M. S., and M. Linkie. 2009. Estimating overlap of daily activity patterns from camera trap data. Journal of Agricultural, Biological, and Environmental Statistics 14:322-337.
