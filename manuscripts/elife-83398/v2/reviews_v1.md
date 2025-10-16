# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83398.sa0](https://doi.org/10.7554/eLife.83398.sa0)

This important study presents an interesting example of how complexities of communities may be reduced by showing that when partner species exert a negative effect on the focal species, the joint effects are generally not additive, but rather dominated by the strongest single effect. The evidence, enabled by thousands of measurements using nanodroplet-based microfluidics, is compelling, although the generality of the conclusion awaits further studies. This paper is of interest to microbial ecologists and synthetic biologists.


---

# Peer review - Round 1

Editors:
- Wenying Shou, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83398.sa1](https://doi.org/10.7554/eLife.83398.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Interactions between culturable bacteria are highly non-additive" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Meredith Schuman as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alvaro Sanchez (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Revise the text with a softer tone. For example, the generality of the conclusions is unknown since the 6 focal species were from 1 family, and since the conclusion only works for a subset of focal species, etc. Please see specific comments especially from Reviewers 2 and 3 about revising the claims.

2) Provide a more rigorous analysis of the fluorescence assay. Exactly what is this assay measuring? How might the correlation between growth/biomass and fluorescence be affected by death, diauxic shift, or prolonged lag / stationary phases? See comments to the authors from Reviewer 3.

Reviewer #1 (Recommendations for the authors):

My only suggestions are on writing. Certain key aspects of experiments can be outlined in the main text. For example, when pairs were introduced, did the inoculum for each strain get halved? Figure 3A graphic is unclear, and can be made much clearer by plotting mono effects and predicted coeffects under the three models.

Reviewer #2 (Recommendations for the authors):

Figure 3: (A) I think this panel could be made clearer. What does the green bar represent? It is not explicitly clarified in the caption. I think it depicts the growth of the green "test" bacteria? Maybe clarifying this in the caption would help. Also, why not add the equation representing the interaction?

Figure 3: (B). The data points are so tiny it is difficult to see them. Maybe using larger dots (I understand there are a lot of them, though. I wonder if there is a clearer way to plot this data). Also the color choice is not the friendlies to color-challenged readers like this reviewer. I had trouble in particular distinguishing the pairs when one species had a positive while the other one had a negative effect from those that were both negative.

Lines 167-169: The authors introduce the "mean effect model". What is the theoretical justification for including this model in the analysis? I mean, in terms of ecological theory? The additive model is justified e.g. in that it is the typical assumption in Lotka-Volterra (and also considered in the antibiotic combination literature cited in the paper). But how about the mean model? It would help if the authors explained/justified the theoretical basis for this. Otherwise it feels a bit random, they could have taken the median, or the square root of the variance, or…

Lines 221-224: The authors write: "We further explored this model by basing trios' data not on the additive, mean, or strongest values of the effects of individual species, but on those of the joint effects of the three pairs comprising each trio (the effects of single species and pairs were measured independently again in this experiment, see Materials and methods, Figure S1)." I have read this sentence five times and I am still not sure what the authors meant

Lines 296-300. The authors may want to more explicitly bring up in their discussion that the predictive ability of the "Dominance", strongest-species model, is significantly worse when they try to predict the effect of a trio than when they try to predict the effect of a pair. This would suggest some caution in the reach of their conclusions, as it is possible that the predictive power of a single species will get worse and worse as the diversity of the community increases. Which, by the way, would not be surprising I think and should not be held against their findings, but I still think it would be good to qualify their statements about the potential reach of their conclusions for the bottom-up prediction of population-level interactions in complex communities. While they do state that "further work is needed…" to figure out if they results hold in more diverse communities (Lines 294-96) I felt that the limitations of the study could be written in a sharper manner.

Finally: I was curious if the authors have considered a model where one of the species is dominant in a pair, but the one that dominates is not necessarily the one with the strongest effect? For instance, is it possible that when A is grown with either B alone or C alone, the suppression of growth from B is stronger than the suppression of growth from C. Yet, in the presence of both B and C, the suppression of growth is exactly the same as that by C (or just closer to C than B)? Do the authors see this in any of their pairs? If so, how many?

Reviewer #3 (Recommendations for the authors):

The metric of growth for the focal species was fluorescence. This can be a risky measurement, because other species could autofluoresce in the emission spectrum. Additionally, fluorescent proteins can continue to fluoresce after cell death and lysis (we have personally observed this after phage infection and antibiotic treatment). I think the paper could use a test to verify that fluorescence was an unbiased proxy for growth.

I am confused by the densities that the species start at. In the methods, it says the focal and affecting species had starter cultures that were 2-fold different in concentration, yet were mixed 1:1, and ended up with a 1:1 ratio. How is this possible? Supp Figure S1 did not help me understand this.

It was surprising to me that inoculation density had no effects. This makes me wonder whether the interactions observed in this study are dominated by primary metabolic competition, because density effects are very common when allelopathy occurs. If this is true, it restricts the generality of the results, and is worth being discussed. Related to this, antibiotic resistance was measured, but what about potential to secrete antibiotics?

I think the density effects should be measured with nRMSE, or even absolute difference from y=x, because there could be a strong correlation without the actual numbers being the same sign or magnitude. For example, in S11-B, most of the datapoints appear below y=x, until the effects are near zero, suggesting an effect-size-specific effect of density.

More discussion could be given on what a "meaningful" difference in nRMSE is.

More details on how the resampling during the bootstrap procedure was done is warranted.

It isn't clear to me how Figure 1C is supposed to show that different models were used-perhaps drop this and just leave this explanation for Figure 3A, which is very clear.

Suggestion for additional analysis using the trait data: this dataset seems perfect for using something like a random forest or other continuous-response, "open box" machine learning approach to agnostically ask whether the trait measurements can be used to predict effect when all the measurements are used, rather than summaries of the measurements in the distance metrics.
