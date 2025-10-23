# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63542.sa1](https://doi.org/10.7554/eLife.63542.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The reviewers and editors found that the manuscript presents a simple but compelling model that explains the dynamics of replication origin birth and death, which enhances our understanding of the selection pressures that have shaped the distribution of replication origins.

Decision letter after peer review:

Thank you for submitting your article "An evolutionary model identifies the main selective pressures for the evolution of genome-replication profiles" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alessandro De Moura (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers appreciate that the manuscript presents a simple but compelling model that explains the dynamics of replication origin birth and death, which enhances our understanding of the selection pressures that have shaped the distribution of replication origins. However, both reviewers had a series of concerns. Please go through their reviews below. In your revised manuscript please address in particular the major concerns they have raised.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Reviewer #2:

The manuscript entitled "An evolutionary model identifies the main selective pressures for the evolution of genome-replication profiles" is an examination of the principles shaping evolution of replication origin placement. Overall I found the manuscript to be engaging and interesting, and the topic of general importance. It is quite compelling that with just two parameters, origin efficiency and distance between origins, a good model can be built to describe the dynamics of origin birth and death. While this work on its own is sufficiently important for publication, it would be very interesting to see whether the model can be updated in the future to address whether there are fork-stalling or origin-generating mechanisms that shape evolution of specific inter-origin spaces. This work provides a very good foundation for such efforts.

I have a few major, general concerns I would like the authors to address.

If I'm interpreting the methods correctly, it seems the parameters used in these simulations, such as mean birth rate, mean death rate, γ, and β, were fit to the data once, and used as point estimates during simulation. If true, I expect the simulations to be yielding estimates of birth and death rates with a much narrower distribution of outcomes than is likely to be realistic given what an appropriate level of confidence in those parameter estimates would be. Could the parameters be fit to data in such a way that we attain an estimate of confidence in the parameter values, from which a distribution could be generated and sampled from during simulation?

Closely related to my prior concern, I would like the authors to demonstrate the general predictive value of their model on out-of-sample data. Can the model be applied to other data on replication timing? Without such an attempt to demonstrate the model's applicability to out-of-sample prediction, the reader cannot ascertain whether the model is overfit to the Lachancea data from Agier et al., 2018. Also, keeps the parameter estimates here from being overfit to better predict origin birth and death events in closely related branches of the Lachancea tree in Figure S1? Are γ and β inferred in a way that accounts for the higher correlation in birth and death events in closer-related branches than in distal branches, or has the fit ignored those correlations?

The authors state that their model identifies selective pressures. The authors imply, and specifically state in lines 238-242, that increased death rate of origins which happen to be nearby highly efficient origins represents selective pressure against the less efficient origins. It isn't until the discussion that the authors raise the possibility that there may simply be a lack of selective pressure to retain inefficient origins that are near highly efficient origins. In my view, it's more likely that selection for the existence of an inefficient origin is simply lower than the drift barrier, so mutagenesis and drift can passively remove such origins over time without the need to invoke selection against inefficient origins.

Figure 3 is intended to show that the stall-aversion and interference model performs better at predicting correlations between efficiency of lost origins and their nearest neighbor. I agree, but I do not think Figure 3 presents a strong case for this conclusion. Figure S6 presents stronger evidence to me. While Figure 3 does qualitatively suggest that the joint model may predict the correlation between neighboring origin efficiency and origin loss better than the double-stall model alone, it almost appears to me that the model with fork stalling and interference has significantly overestimated the correlation. Is there a quantitative way, perhaps using information criteria, though I admittedly am not sure how one would go about doing that with simulations such as these, to demonstrate that the model with both effects has better predictive value than the one with only fork stalling?

There are a couple of assumptions of the model that I would like the authors to examine in further detail. First, that origin birth events occur in the middle of an inter-origin space. I am not aware of evidence pointing to this being a good a priori assumption. Can you re-run the simulations, allowing origins to arise at a random site within the inter-origin space into which it is born? Second, is it reasonable to expect origin firing rates to reshuffle to a new value randomly, without any dependence on their prior rate? Perhaps I'm mistaken, but it seems to me that an origin's firing rate should evolve more gradually, and should have a higher probability of sampling from values near its current value than from values very far from its current value.

Reviewer #3:

This paper proposes a novel and relevant evolutionary model that explains many aspects of replication origin statistics in a family of yeast species. It is a step forward in our understanding of the evolutionary pressures that affect the distribution of replication origins in Eukaryotes. I recommend it should be published in eLife, provided the authors revise the paper to address the following issue:

1. Many of the conclusions of the paper are based on the claim that the extending the model by adding an efficiency bias to the origin death rate makes the model fit the data better; in particular, they say in line 213 that "the observed huge divergence in efficiency between lost origins and their neighbors is absent in the model simulations."

This is reinforced in line 243, and in other parts of the text. But inspecting Figure 3, the two models (with and without a death rate bias) yield almost identical box-plots; if anything, the box-plots for the lost/nearest fractions of the pure double-stall aversion model seem visually to match the data marginally better. So why do the authors claim that the model with death rate bias is a much better fit? This is far from clear by just inspecting the data. I see no "huge difference" in the plots. There is a difference, but it is far from huge – the differences in the mean are much smaller than the size of the boxes. It seems to me unjustified to use this to choose one model over another. One way to ascertain this is to do rigorous statistical tests to determine if the differences in the means of the simulated and observed data are statistically significant; for example, a t-test.
