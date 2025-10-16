# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61927.sa1](https://doi.org/10.7554/eLife.61927.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors of the manuscript present a new implementation of the previously developed statistical method called "Estimating Effective Migration Surfaces", which displays on geographical map regions of low or high effective migration under a broad model of isolation by distance. In this new implementation migration surfaces are estimated under a penalized-likelihood approach coupled with optimization instead of MCMC leading to faster running times. The new implementation facilitates faster running times to make its usage computationally possible for a wider range of research groups and likely be applied to an even larger number of species/populations.

Decision letter after peer review:

Thank you for submitting your article "Fast and Flexible Estimation of Effective Migration Surfaces" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by George Perry as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Isabel Alves (Reviewer #1); Wesley Tansey (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The authors of the manuscript present a new implementation of the previously developed statistical method called "Estimating Effective Migration Surfaces", which displays on a geographical map regions of low or high effective migration under a broad model of isolation by distance. In this new implementation migration surfaces are estimated under a penalized-likelihood approach coupled with optimization instead of MCMC leading to faster running times. The new implementation appears very promising as faster running times will make its usage computationally possible for a wider range of research groups and likely be applied to an even larger number of species/populations. Overall, we value the approach for its pragmatism but felt that it falls short at the very end by failing to provide any quantitative, objective way to choose the hyperparameters, which needs to be addressed as per the essential revisions detailed below.

Essential revisions:

1. The authors need to provide principled (or at least reproducible) ways to select the hyperparameters. Specific reviewer comments include:

"This is a major benefit of the L1 penalty. You can use BIC as the model selection criterion in the L1 case since the degrees of freedom are well-described. In the squared L2 case, it's not really possible. The authors discuss the issue and note LOOCV did not produce stable results, but they do not provide any data or examples. A more thorough investigation of hyperparameter settings is needed along with a recommendation that does not rely on biologists' subjective preference of the results on each dataset."

"FEEMS outcomes are very sensitive to user-based settings such as grid density and tuning parameters, as well as to aspects of the real data (eg. sampling design) that may result in an arbitrary choice of the outcome and lead to over-interpretations. I know the authors recommend to explore several combinations of regularization parameters and then compare FEEMS results with clustering/differentiation patterns based on approaches like ADMIXTURE or FST distances in order to support the results, nevertheless it is still difficult to grasp what's the best strategy to assess if a fitted graph is over-fitting the observed data or instead is pointing out to a real area of, let's say, low effective migration rate. Sentences like: "…, while setting up the tuning parameter ɑ to a value that we found that worked for multiple data applications.…" (lines: 225-226) or "it is helpful to look more closely at particular solutions that find balance between spatial homogeneity and complexity…" (lines: 243-245) are confusing and make difficult the choice of the final regularization parameters."

"The grid design is another arbitrary aspect of the method whose influence on the identification of regions of low or high migration isn't clear. Imagining one has the computational power to construct a very dense grid, is it worth doing it once there is observed data in 1% of the nodes? Is there a good relationship between density and number of sampled points? Does it affect the outcome?"

"I think the points above would be clearer if the authors would provide for instance, step-by-step guidelines to help future users of FEEMS and referring to specific examples in the manuscript in order to more clearly justify their parameter choice (eg ɑ = 50 line 226)."

2. Please clarify the modeling decision and its comparison to the L1 approach. For instance, isn't smoothing over nodes vs edges really just the same thing with different penalties? The authors form a lifted graph, where edges are now nodes and they penalize differences between neighboring edges. In the L1 penalty case with a squared error loss, the fused lasso / total variation penalty on neighboring edges is equivalent to linear trend filtering on the nodes. The choice then of linear trend filtering could have been replaced with a higher order trend filtering step to achieve the smoothness that the authors seem to say is lacking in the L1 model.

3. Are the data points we observe actually sampled at random? Is some sort of latent confounding likely? For example, maybe wolves migrate based on the season and the scientists collecting the data only look in one spot in one particular time of year?

4. Please clarify the simulation results in Supp Fig19, panels I and J. Without any data points in the orange regions for panel I, the model somehow infers that there is a band of different edge weights. How? In the 1d case, it's as if someone showed you: [5, 5, 5, missing, missing, missing, 5 ,5 5], and you come back and told me [5, 5, 5, -3, -3, -3, 5, 5, 5]. Is this possible?

5. At present, there is no real quantitative assessment of how good the FEEMS solutions are relative to the EEMS solution. This should be provided.

6. It would be useful to provide another example of a heterogeneous migration scenario where the reduction in migration is less than one order of magnitude in order to give an idea to the user of how the method performs in a less heterogeneous scenario (ie the lower bound).
