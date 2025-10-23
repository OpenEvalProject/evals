# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

## Review text

DOI: [10.7554/eLife.49720.sa1](https://doi.org/10.7554/eLife.49720.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Multistability and regime shifts in microbial communities explained by competition for essential nutrients" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Wenying Shou as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ian Baldwin as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

"Multistability and regime shifts in microbial communities explained by competition for essential nutrients" by Dubinkina et al. explores the presence of diverse, multiple stable states for diverse ecosystems. The model builds on the groups earlier work using results from game theory on the stable marriage problem to ask under what conditions it is possible to have multistability in diverse communities. The authors employ an idealized model of competition for essential nutrients to study patterns of multistability and diversity in microbial ecosystems. By computationally enumerating steady states and classifying them by stability, the authors establish that multistability is a typical feature of resource competition between specialized consumers. Specifically, they show that multistability emerges robustly when nutrient supplies are balanced and competitors have different C:N stoichiometries. The topic of how diversity is maintained in microbial ecosystems is likely to be of broad interest to the readership of eLife. While the current model is quite simplified compared to any real multispecies community, the authors do a good job of highlighting general lessons from the model that make testable predictions for natural and experimental systems. Overall, all three reviewers found the work interesting.

Essential revisions

Essential revisions fall under three categories:

1) Present your model more clearly;

2) Add mechanisms and intuitions (rather than simply describing your data);

3) Discuss generalizability of the results, including sensitivity to parameter choices.

To help you revise, we attach the reviews.

Reviewer #1:

My main suggestions are as following:

1) The authors define states by the presence/absence of species, and if present, which nutrient it would be limited in. Out of the theoretical possible states, the authors found all steady states by noting a correspondence of their problem and the stable marriage problem. This correspondence needs to be explained in an accessible form (perhaps in a figure).

2) Put more emphasis on going through the data and explain what they mean. For example, in Figure 1B: why do we get these states? For the two-species 11, 22 cases, one could imagine a different state where 11 is limited for carbon, and 22 is limited for nitrogen. Why is this case not seen? Does this have something to do with your parameter choices? For Figure 3B, why does the likelihood of multistability peak at C:N supply rates similar to the average C:N stoichiometry? If you change the average C:N stoichiometry ratio by 10-fold, does the peak change by 10-fold? Seems that the authors were simply describing results rather than also giving intuition on why the results arose.

3) Subsection “Three criteria for stability of microbial communities” paragraph four: not clear why invasion does not depend on nutrient supply rates, given that nutrient supply rates could change growth rates.

4) Abstract: Multistability requires different stoichiometries of essential nutrients. How different does "different" have to be? It would be good to supplement with previous experimental data on these ratios and discuss.

Reviewer #2:

My main concern is really about how much the conclusions from this particular model used by the authors generalize to a more general setting. I think the assumptions of the model are quite stringent (and need to be in order to really use the technical apparatus of game theory/stable marriage problem they use):

Each species can use only one C and one N resource; a single metabolite cannot provide both C and N (even though we know for example bacteria can and do use amino acids as C sources).

As the authors point out, this gives rise to non-generic behavior such as the fact:

"Unlike other consumer resource models, in our model the dynamic stability of a state with respect to species invasions does not depend on nutrient supply rates."

At the minimum, the authors have to argue what depends on these assumptions and what does not. Comparing the results to more standard Consumer Resource Models (CRMs) would go a long way at clarifying this. Despite this criticism, I want to emphasize that I think the paper explores and interesting question and gives rise to interesting hypothesis that are interesting and potentially testable.

I now give more detailed comments:

Technical Comments:

The section on Monte-Carlo sampling is extremely unclear. What exactly is the distribution that is sampled? Is this done only in the high-flux regime? What is assumed about the R matrix being invertible? Is this somehow an assumption that the Y are "generic"? It is very unclear to me why one cannot be feasible on a low-dimensional manifold. This is usually a generic situation in most CRMs so why is it excluded here. I would appreciate a much more technical discussion, perhaps with pseudo code so that I can better understand if and when the arguments generalize.

The equations in subsection “Conditions of multistability in the 2C x 2N x 4S ecosystem” have typos (extra factors of Y).

I did not understand in the section on lower-bound, why "double counting" can be discarded (either when # of C = # of N or otherwise).

It is very unclear how sensitive are the results to different "draws" of the λ and Y. There is a particular realization given in SI Tables but it would be nice to have a sense of the fluctuations rather than just for one network.

Another general way of modeling essential resources is to use a function of the fromg=(∑αciα/Rα)−1where the cIα are constants with the same units as Rα that encode ratios of resources required for building biomass (see Taillefumier et al., 2017). Recently, it was shown in arxiv:1901.09673 that such functions can also give rise to multi-stability using a Minimum Environmental Perturbation Principle based on measuring distances from the input flux vectors with appropriate distance metric. This suggests it should be possible to generically construct input fluxes into the system with multiple steady-states by finding input vectors that are equally distant from the intersection of all ZGNIs for a different, more traditional class of CRMs where species can eat many resources. This again raises questions about what generalizes from this simple but interesting model. It seems that this would be more in line with the generalization in equation in subsection “Extensions of the model” but it may qualitatively change the results.

Conceptual Comments:

I really enjoyed the idea of how by continuously changing the environments one cannot connect very different stable states. This reminds me of old arguments in evolutionary theory on neutralness in adaptation by Fontana and collaborators (PNAS 1996) where very different evolutionary minima could be connected even though they changed differently. This is just a thought/comment not a suggestion for investigation.

The idea that equalizing resources promotes diversity is now something that has been found in various CRMs (Posfai et al., 2017; Tikhonov et al; Marsland et al., 2019). The idea is that one gets neutral like dynamics. Is there a way to reconcile these ideas with the multi-stability? It is curious that both these dynamics like equalizing resources and I would like to understand what, if any, the authors think the connection is.

I am really confused as stated above how these results depend on the available resource species pool. In particular, what if I changed the statistics of things were generated, yields, etc.? I think it would be nice to at least understand these things at least semi-quantitatively.

Reviewer #3:

1) Existing literature on competition for essential nutrients.

The authors state that "while real-life ecosystems driven by competition for multiple essential nutrients have been studied experimentally Fanin et al., 2016; Browning et al., 2017; Camenzind et al., 2018, the resource-explicit models capturing this type of growth are not so well developed beyond the foundational work by Tilman, 1982." Although this is generally true, it would be helpful to reference the work that does exist, to orient the reader as to whether the current results are surprising. Huisman's paper (Nature 402 1999) is relevant, as is the plankton literature more generally.

2) Assumptions and parameters of the model.

The assumption of complete specialization to a single carbon and nitrogen resource is very limiting. More care should be taken to justify it in the context of real ecosystems. Would the results hold qualitatively if this assumption were relaxed? Why or why not? Furthermore, each model seems to feature only one realization of the growth coefficient λs. The authors don't need to redo everything for new parameters, but they should confirm that their results are not specific to these parameters. Finally, in the current model a species' λs and Ys (growth yields) are uncorrelated. However, it would be more biologically plausible if these were subject to trade-offs for each species (e.g. high growth rates correspond to low yields). It would be informative if the authors would check the case where λY=constant to confirm that their results do not depend on λ and Y being uncorrelated.

3) Explanation of Figure 2E-F

The authors should try to provide an intuitive, mechanistic understanding of these computational results. Why does state 2 have the largest feasibility volume, and why are regime shifts possible between some states and not others? If I understood the simple case of 2e, I would have a better appreciation of 2f. A discussion of the ecological implications would also be welcome here.

4) 1D manifold in Figure 3C

In the same spirit as point #3, the authors should try to explain this result and its implications. This is certainly an interesting observation, but as of now it's asserted without any mechanistic understanding.

5) Competitive rank and diversity

The "competitive rank" metric is unintuitive, at least as presented. The authors should explain more clearly why ranks run from 1-6 and why they're a species property independent of the environment. The surprising result that a rank 5.5 species is uninvadable 20% of the time should be explained. What is a specific scenario in which this occurs, and why?

6) Volume in abundance space

The authors focus on the feasibility volume of a state in the space of nutrients. However, it is also natural to consider the volume of the basins of attraction in the space of species abundances for a particular state in a given environment, when multiple stable states are possible. Does the volume of the basin of attraction for a state relate to its feasibility volume?
