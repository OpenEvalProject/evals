# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82504.sa0](https://doi.org/10.7554/eLife.82504.sa0)

This important study uses computational simulations to explore when spatial structure can promote the coexistence between different microbial species and when not, ultimately helping to explain diversity in microbial communities. The evidence supporting the conclusions is convincing, based on extensive parameter sweeps. The conclusion that spatial structure only promotes coexistence under certain conditions is a testable hypothesis that is very interesting to microbial ecologists quite broadly.


---

# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82504.sa1](https://doi.org/10.7554/eLife.82504.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Spatial structure may favor or disfavor microbial coexistence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Daniel R Amor (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you can read in more detail below, the three reviewers all made similar recommendations to improve your manuscript. Please address at least the following points:

1) Justify the definition of coexistence (the 90% threshold);

2) Justify the way dispersal is implemented and the choice of diffusion coefficients;

3) Check for typos in the equations and the implementation of the carrying capacity;

4) Explore how relaxing these assumptions or using more realistic parameter values would affect current conclusions;

5) Explore not only coexistence but also population composition and the resulting spatial patterns.

Reviewer #1 (Recommendations for the authors):

I present here more concrete suggestions and concerns related to my comments in the public review.

1. I believe that there might be some errors in how the model's equations for species dynamics (line 298) were written in the manuscript. In the equation in line 299, should the term above the total cell carrying capacity (Ky) be a sum of all the species abundances instead of all the metabolites abundances? I believe that this is not the way that the matlab code was implemented, but it would be worth it for the authors to double-check this in all the scripts.

Ksat should have the same units as Cj(z,t), which is in disagreement with the units proposed in table 1. Similarly, Ky should have the same units as Si(z,t). Furthermore, it was not very clear how interactions, production, and consumption rates were assigned. Do they exist with a certain probability and, provided that they exist, their strength is sampled from a uniform distribution?

2. Line 321 defines the criteria to determine coexistence: 'only those with relative frequencies equal to or larger than 90% of the fastest growing species in the last 20 generations of the simulation are considered to coexist'. I am surprised by the relatively high (90%) threshold. This means that a pair of species that reaches a stable equilibrium of e.g. 10^7cells/ mL and 8*10^6 cells/mL is not classified as a pair of coexisting species. Please, discuss why the criteria imply such a high evenness of species abundances (experimental measures often report stable coexistence of species at many different fractions). I wonder if relaxing this strong requirement would significantly affect the results of community richness.

3. The text should be more clear from the beginning that the 'slow dispersal' scenario that is analyzed through the first sections (Figures1-3) is qualitatively very similar to a 'zero dispersal' scenario. Just to illustrate why I think this, one can use the Fisher's front speed solution v = 2*sqrt (r*D) to have an estimate (based on the proposed parameter values) of how much distance a monoculture could travel in the absence of interactions. The result, taking into account the timescale of the simulations (~350 hr, assuming r0 = 0.2/hr), is a total distance of ~0.02cm, which is consistent with the results in Figure S2. This means that, in this regime, microbial dynamics are mostly driven by growth, not by dispersal. On the other hand, considering the value of D in the 'fast dispersal' scenario gives an approximate front speed of 2*10^(-3)cm/hr (travelling ~0.7cm in 350 hours) for a monoculture in the absence of interactions. This is closer to observed speeds for colonies of non-motile bacteria growing on hard agar, and still falls on the slower end for such speeds. If one thinks about motile bacteria in soft agar, the speeds are even faster. Overall, I wonder about the kind of system that the 'slow dispersal' scenario could be modelling and, more importantly, whether the authors would consider analyzing the implications of 'fast dispersal' scenarios in more depth. How would Figures2 and 3 look under fast dispersal?

4. The figures of the main text could incorporate more analysis and results that further support the main message of each figure. Most of the figures contain only one panel (or one type of panel) and further information on the many parameters that could affect that result is left to the Supplementary Information. In some cases, just bringing some of the supplementary analysis to the main figures would make them more comprehensive while increasing the readability of the paper. Just to give some examples, figure 1 could incorporate the cartoon that explains the model (Figure S1), a time series, and some spatial profiles of species abundances to illustrate the typical dynamics of the system (e.g. incorporate some of the data in Figure S2). More snapshots of spatial profiles would help understand what happens in different scenarios, e.g. in Figure S6. In figures 2 and 3, how do these results depend on the average interaction strength (growth rate impact) of metabolites-to-bacteria?

5. The work will benefit from the additional analysis that can strengthen certain interpretations of the current results. For example, Figure S5 shows the dependence of species richness on the carrying capacity of the system. The authors claim that a shift towards intraspecies competition is responsible for such dependence and that a limited carrying capacity suppresses the more competitive species, but no statistical analysis on individual species performance is provided to back this argument (and species competitiveness is lacking a working definition). The criteria to determine the length of the simulations is another example, the authors said that 100 generations are 'often' enough to reach stability, but a more rigorous analysis or definition of stability would be better. Regarding the statement in line 116, an analysis of how much better or worse species grow when close to facilitative/inhibitory partners would be helpful.

6. The lack of analysis/visualization of spatial profiles for metabolite abundances leaves the reader wondering about the spatial scale of the interactions. Some representative cases could appear in the supplement, or be incorporated into one of the main figures.

Reviewer #2 (Recommendations for the authors):

The authors extend a mathematical model that they previously developed (Niehaus..Momeni, Nature Comm., 2019) for the study of microbial communities growing in well-mixed settings, to the case where species grow in spatial settings. They find that spatial structure promotes the coexistence of species when interactions are more facilitating than inhibiting, and when species dispersal is low. We found the paper well-written and well-organized. However, we have a number of comments: the main contribution of the paper is to extend a well-mixed model to a spatial model; It is thus fundamental that the assumptions made by the authors to model the spatial dynamics are well justified; we think that several physical parameters are chosen to values that do not represent realistic values for spatially structured communities and that the authors should discuss if the results hold also for more realistic values.

Line 84: The Authors state that they start each simulation from an initial distribution in which populations occupy adjacent, overlapping spatial locations at low initial density. What is the variation in the steady state distribution of species if they run many simulations with the same initial state and with the same parameters?

Line 88: "We have chosen 100 generations of growth because we have observed that often this is enough to reliably decide which species stably persist in the community." We think that the concept of generation is not clear. Can the authors define what generation means exactly? Also, can they provide a quantification for "reliably" when they say that the system converges reliably?

Line 91: The authors define a specific dilution procedure. We do not understand how they motivate this specific choice of dilution procedure. At each dilution step, they assume that the overall spatial distribution of the community is preserved and all populations at all locations are diluted by the same factor. Regarding this assumption, the authors say that they "adopt it as the least biased possibility, in the absence of additional information about a particular community." We have two questions regarding this assumption:

i) Is this really the least biased assumption? We suggest that a random distribution of the initial species is more a null model than the current choice. Or is there a reason to think that cells forming a new community by default inherit the spatial configuration of the parent community?

ii) Do the authors have a natural mechanism of community propagation in mind that they could refer to, which would correspond to their assumption?

Having in mind the concept of metacommunities, we don't understand how spatial distribution can be inherited by the new community.

Line 101: The authors say that a shift from competition to competition can favor coexistence in a spatially structured environment. When doing this analysis, the authors impose a cap on the total cell number that can exist at each location in space. The more restrictive the cap is, the more coexistence they find.

Regarding this conclusion, we would like the author to comment on the choice of the cap. The cap they pick is 10^9 cells/ml. This density is quite a low density for a spatially structured system. A back-of-the-envelope calculation can show that at 10^9 cells/ml, the volume ratio between cells and environment is 1:1000, if we consider that a cell occupies approximately 1 μm cube (e.g. E. coli in Minimal media+glucose is about that size. See: https://www.ncbi.nlm.nih.gov/books/NBK224751/). These are the order of magnitude estimates of course, but they suggest that the authors use a density that is much lower than expected in a spatially structured community, like a biofilm. In fact,10^9 cells/ml is about the density of cells in an overnight of E. coli grown in Minimal media (M9) with 0.2% glucose. We would suggest picking values closer to a dense community, and our expectation is that spatially structured communities should be at least 10^11 cells/ml. Following the calculation above, this would lead to a volume ratio between cells and the environment of 1:10, if we consider that a cell occupies 1 μm cube.

We would like the authors to comment on the following two points:

i) Why do they pick 10^9 cells/ml as a maximum cap, which seems such a low density?

ii) The authors pick 10^9 cells/ml because this cap maximizes coexistence. In light of the calculation we do here, what would happen if they used higher values of cell densities?

Line 101: 10^9 cells/ml is not 10^9 cells/cm as stated in Table 1. Can we think of these units as being the same? If yes, can units be homogenized? At the moment most of the units suggest that the effective dynamics is a 3D dynamics (e.g. diffusion constants, densities of cells), even if then they implement a 1D world, where there exists a line of "cubes" filled with sub-communities.

Table 1: The authors state that "Diffusion coefficient for mediators (DMed) 1.8 10-3 (cm2/hr)".

Again we do not understand the choice of parameters. When we look at realistic values of molecules diffusing, we see that these are more than 10 times faster. Here are two examples for glucose and for one amino acid:

For Glucose, the diffusion constant in water is 600 um^2 /sec, which is about 21*10-3 cm2/hr. See: https://bionumbers.hms.harvard.edu/bionumber.aspx?s=n&v=7&id=104089

For amino acids, the diffusion constant in water is 800 um^2/sec. See Wu, Y., Ma, P., Liu, Y. & Li, S. Diffusion coefficients of l-proline, l-threonine and l-arginine in aqueous solutions at 25◦C. Fluid Phase Equilibria 186, 27-38 (2001).

Table 1: Can they comment on the value of diffusion of species? This value represents somehow a fraction of individuals that move away from the local patch into another patch. What should we think this fraction to be?

Figure 1: what is the explanation for which, at a low fraction of facilitative interactions, coexistence in well-mixed and spatial communities is the same? Can they comment on this?

Figure 5: Do the authors expect that by increasing diffusion even further, coexistence should decrease again? Does the exploration stop at the maximum diffusion expected in liquid?

Reviewer #3 (Recommendations for the authors):

– I think there is a typo in the equations shown in the "Model description" section. In the population dynamics equation, the carrying capacity term (the one with k_Y) appears to contain a sum over the C_j rather than the expected sum over the S_i. In the supplied code, it appears that this term sums over the populations.

– Assuming the carrying capacity term is meant to contain a sum over the S_i rather than the C_j, the current formulation of this model may lead to non-physical outcomes. Consider a population that is above carrying capacity, such that the carrying capacity term is negative. If this population is also surrounded by highly detrimental chemical mediators (such that its interaction term is negative), the product of the negative carrying capacity and interaction terms will result in a positive growth rate. From the code I have looked at (Spatial1DInteraction_DpMM_ExMTC_flexibleTimeStep.m, lines 103-110), there doesn't seem to be any mechanism to prevent this. However, from the supplementary plots, it does not appear that the steady-state population abundances exceed the k_Y. The authors should assess whether these non-physical dynamics occur in their simulations, as it could artificially inflate coexistence. One possible solution is to set the population growth to zero if the carrying capacity is exceeded.

– One limitation of the authors' current analyses is that it is based only on richness, which does not reflect population abundance. Equivalent comparisons between the spatial and non-spatial models could be made with a metric like the Shannon entropy, which does consider population abundance. To compute the Shannon entropy in the spatial model, one could measure the total population of each cell type by integrating over the domain. From these abundances, a relative abundance distribution compatible with the Shannon entropy could be calculated. It would be worthwhile to assess whether the observed trends are similar when other metrics are used.

– I think it would be worthwhile for the authors to quantify the spatial patterns of coexistence in their model. I understand the authors' reasoning for focusing on a metric that does not consider spatial structure, as such metrics are the only ones that can be used to compare directly between spatial and well-mixed systems. However, from the plots shown in Figure S2, it appears that coexistence in this model can manifest as quite non-trivial spatial patterns. Spatial coexistence patterns of natural microbial communities are often strikingly beautiful, and it would be interesting to assess how this model's parameters influence its resulting spatial coexistence patterns. For example, one could examine the relationship between the mediator and microbe diffusion rates and the size/overlap of microbial domains, or analyze the existence of the seeming "dead-zones" of the domain seen in the bottom right panel of Figure S2.

– I find the result that changing the order of species in the initial condition can change the final richness to be very interesting (Figure S8). This result implies that there is a great deal of multistability in the dynamics. In a metapopulation context, this could be its own diversity-generating mechanism. I think discussing this multistability more explicitly in the main text would be worthwhile: is this multistability a result of spatial dynamics?

– The authors should specify the distribution of mediator production/consumption and interaction coefficients. Currently, I'm not sure what distribution these parameters are drawn from.

– In the figures with well-mixed vs. spatial heatmaps, it may be worthwhile to include a plot that directly depicts the ratio of the two model's richness values. As it stands, I found it a bit difficult to immediately see the differences between the well-mixed and spatial results.
