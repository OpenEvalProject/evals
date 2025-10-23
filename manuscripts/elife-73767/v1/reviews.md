# Peer review - Round 1

Editors:
- Aida M Andrés, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73767.sa0](https://doi.org/10.7554/eLife.73767.sa0)

This is an important manuscript that presents an elegant framework to infer the dynamics of beneficial alleles over time and space. The authors present a new method and show, convincingly, its utility and great potential to reconstruct the evolutionary history of beneficial alleles. The method is also applied to loci that likely mediated human genetic adaptations, contributing to our understanding of human recent evolution. The work will be of broad interest to evolutionary biologists who seek to understand the dynamics of beneficial mutations in populations.


---

# Peer review - Round 1

Editors:
- Aida M Andrés, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73767.sa1](https://doi.org/10.7554/eLife.73767.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Modelling the spatiotemporal spread of beneficial alleles using ancient genomes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Isabel Alves (Reviewer #1); Anders Eriksson (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers and editor found the manuscript elegant and interesting and appreciate the novelty and promise of your new method. They also value your new inferences on two important targets of positive selection in humans. You will find the individual reviews below, to be addressed individually. Here we provide a summary of the desired revisions, to assist you in the revision process.

1) We believe that the manuscript needs a more systematic test for the sensitivity of the method to 1) misspecification of the age of the aDNA samples, and 2) the geographic location/clustering of the samples. This could be done for example by exploring the effect of these factors on the accuracy of the parameter estimates.

2) Related, we believe that further discussion is needed on the extent to which differences observed across time periods (e.g. before and after 5000 BP) reflect particularities of the alleles (e.g. selection), populations (e.g mobility) or the density of the samples across time and space.

3) Where models are applied to specific loci, results are often reported in the text without enough quantitative information and we think that clearer and more detailed information about the inferences must be presented in the text. As an example, where the model is run for different allele age estimates the (approximate maximum) likelihoods of parameter estimates for the different scenarios should be clearly shown in the text.

4) We believe that the authors should clarify some of their choices for the method. We would like to see a discussion of whether the method may be suitable for treating allele age as a free parameter, or whether it is possible (and superior) to report Bayesian posterior distributions for the parameters and Bayes factors to compare the fit of different models to the data.

5) The loci studied represent unusual cases of very strong positive selection in particular geographic areas. We would welcome more discussion regarding the extent to which the current version of the method can be applied to other alleles, to other geographic regions and even to other species.

6) Finally, the reviewers raised issues regarding the presentation of the numerical implementation that we hope that the authors can easily address.

Reviewer #1 (Recommendations for the authors):

I very much appreciated reading this manuscript and the effort of the authors in developing such an exciting tool. However, I still have some concerns about the accuracy and the meaning of the estimates.

1) We know that ancient DNA samples are clustered in time and space because they are an aggregate of samples coming from different studies often with different scopes in terms of time and geographical area covered. What's the impact of having clustered samples in the parameter estimates? The authors comment on that a little bit when comparing the accuracy tests performed with the deterministic vs forward in time simulations. However, I think a more systematic analysis of different sampling schemes would help clarifying the robustness of the parameter inference. Moreover, I think this would greatly help understanding the differences in behavior of the statistical method before and after 5000 BP. Indeed the authors allow the model parameters to differ across different time periods (before and after 5000 BP) but it is not clear whether differences in the estimates reflect any particularity of the populations (e.g mobility) or they just reflect differences in the density of the samples across time and space.

2) How would the method perform if simulations would be performed without advection (numerical solution to equation 3) but parameter estimates would be inferred from a model C, which includes advection ?

3) Finally and more of a general question: what's the point of estimating the geographical origin of an allele if there are no samples dated from around the same time as the assumed allele age? I have the feeling this can be easily misinterpreted but maybe I am missing something. The authors discuss this (lines 199-210) when discussing the results obtained for the dynamics of the rs4988235(T) for the two assumed allele ages but it is not clear to me if the estimate for the local of origin is actually meaningful under similar situations. I wonder if with simulation one could try to understand what the method is retrieving…

With respect to the presentation of the work I found that the manuscript is globally well explained but there are some parts a bit difficult to follow:

1) it should be clearly stated in the main that the age of the allele is provided as input and not inferred contrarily to the geographical origin of the allele and the value used to perform the inference should also be provided in the corresponding part of the main text.

2) The comparison of the results for the two ages assumed for the rs4988235(T) mutation (Itan et al. 2009 and Albers and McVean 2020), mainly between lines 199-210, is very confusing. From Figure 5a it seems there is no information on the allele for the time period between the allele age inferred by Itan et al. 2009 and Albers and McVean 2020. However, from the text it is not clearly stated whether there is or not information. If there is no information at all how does the algorithm infer an origin in Northeastern Europe?

3) It would also help to follow the results if the authors would clearly state in the main text (lines: 212-230) the age of the allele assumed for the rs1042602(A).

Reviewer #2 (Recommendations for the authors):

Given the ability to of the model to sample at any point in space and time, it would have been very interesting to test the model under actual geographical and temporal distributions of data, such as the Allen Ancient DNA Resource used for one of the empirical investigations, perhaps even taking the observed pattern of missingness in the data into account.

I would recommend using latitude and longitude systematically throughout the manuscript instead of mixing x, y, latitude, longitude.

In the methods: Please fix the typo in Eq (9). Also please clarify which boundary conditions where used, and how the equations were solved numerically (using Eq. (8) or (9)?), including how boundary conditions were implemented.

L437: " the left-hand side of equation 5". This doesn't look right, do you mean the right-hand side of Eq. (6)?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Reviewer #1 (Recommendations for the authors):

It is now the second time I review the manuscript "Modelling the spatiotemporal spread of beneficial alleles using ancient genomes" by Muktupavela et al. and I am glad to see that the authors addressed most of the reviewers' concerns. There is now a more systemic assessment of the advantages/limitations of the method which I truly believe to be crucial for future implementations. That being said, I would like to recommend this manuscript for publication.

Reviewer #2 (Recommendations for the authors):

The authors have made substantial improvements to the manuscript, and is ready for acceptance except for one remaining point:

Contrary to what the authors claim in their rebuttal, Eqs (8) and (9) in Appendix 1 still contain errors.

First, p(x+\δ x,y,t) and p(x+\δ x,y,t) appears twice on line 827.

Second, the coefficients of p(x,y,t) on both sides of Eq (9) sum to -1, which is correct. The term should therefore be absent (have coefficient zero) in Eq (8).
