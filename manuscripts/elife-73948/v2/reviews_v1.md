# Peer review - Round 1

Editors:
- Maureen L Coleman, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73948.sa0](https://doi.org/10.7554/eLife.73948.sa0)

This manuscript tackles an under-explored area in understanding microbial coexistence in marine and aquatic environments. This manuscript adds to the recently renewed interest on applications of optimal foraging theory to the study of microbial growth on marine snow.


---

# Peer review - Round 1

Editors:
- Maureen L Coleman, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73948.sa1](https://doi.org/10.7554/eLife.73948.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Particle foraging strategies promote microbial diversity in marine environments" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: James O' Dwyer (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Ensure modeling choices are clearly explained and documented (including making code available)

2) Discuss the generality and limitations of the model and results

3) Provide additional background context/discussion of prior work as suggested by the reviewers

Reviewer #1 (Recommendations for the authors):

- In framing the paper, I think the authors are right to focus on dispersal and detachment as under-explored mechanisms. But readers will benefit from reference to other work (even on particle-associated microbes) related to resource diversity, succession, and crossfeeding. That can only help put the current study in context with other mechanisms for the maintenance of microbial diversity.

To expand on this, I know the authors have worked also on how microbial interactions, cross-feeding, and succession can maintain diversity, or at least add to our understanding of it on marine particles. Is the situation here envisioned significantly different than those experiments? If not, i think it is fine to focus on this different trait axis, and just consider the particles to in effect be a single resource, without resource preferences, etc. But I wanted to make sure I was understanding that correctly---maybe there is something different about the situation envisaged here that would make it less likely to have all of those other interactions (which clearly can contribute to many species being maintained). Martina Dal Ballo and Jeff Gore's work also seems relevant to this (where many resources are produced endogenously in an experimental system) and also work on resource heterogeneity in DOM in natural systems (e.g. Muscarella, Boot, Broeckling , Lennon).

Again, I don't think any of this detracts from the motivation for the present study. Just might fill out a fuller picture.

- There is a population growth process when a cell settles on a new particle. This is assumed to be logistic growth, though in the end, it seems likely that the precise dynamics of the growth process don't matter so much as the final abundance (carrying capacity). However, this seemed subtle to me for three reasons.

(i) It seems to me that the detachment rate should directly affect this final abundance---as an additional source of "mortality" (in the sense of removing individuals from the particle) contributing to the net growth rate. Maybe that effect will always be small, but this could be made clearer for readers if so.

(ii) The authors' conceptual diagram shows that one possible end point of this process is that the microbial population in effect eat the whole particle (Figure 1). This sharpens the issue to me of what the true dynamics are likely to be on a particle. For example, should I think of the population growing to a capacity that is roughly the surface area of the particle, and then gradually changing thereafter as the particle's physical size is reduced? And what direction would this change be? Could I think of a thickening of the film of particles and population size continuing to grow (maybe linearly) in time as interior layers continue to eat the particle? Or should I think of outer individuals as being shed, and the carrying capacity in effect reducing as the particle size reduces?

(iii) The issue of what is actually going to happen once a population reaches carrying capacity is also at the center of my final point here. It seems from the thought experiment above that it is unlikely that growth as such will stop when cells fill out the surface of a particle, since there are still resources to take up. So I am interested to know whether zero growth rate means to the authors that cells stop reproducing, or are cells dying to balance growth, or are they being shed from the particle?

It's possible that none of this matters too much if all that's important is a final population size. However, it might help to clarify the process for readers if we have a conceptual picture of what this final population size represents (surface of particle being filled? or volume of particle entirely eaten up) and if there is a truer picture of the dynamics than logistic growth.

- The relationship between the trade-off (between different detachment rates) derived in Equation 2 versus the optimal detachment rate (derived in the methods) is framed a little confusingly. If I understand correctly, the "trade-off" actually comes from the condition that a population will have net non-negative growth rate in the absence of other populations with different strategies. So it may be reasonable to frame this as a threshold---a necessary condition rather than a sufficient condition for a given population to persist. The reason I say this is that it is a bit confusing to have a trade-off that suggests a range of detachment rates can coexist so long as they differ in their carrying capacities, since it is then stated that the optimal detachment rate outcompetes all the others. Maybe I misunderstood something important being assumed about the carrying capacity for the optimal case, but a trade-off that also has an optimum is an odd outcome.

In short, it was not clear to me whether to populations satisfying this tradeoff in Equation (2) would tend to coexist. Or would in general one population (say the one closer to the optimum strategy) tend to outcompete the other? If so it might help to define more clearly what this tradeoff means. If I understood this correctly, I would not say that this issue merely indicates that the tradeoff is not "evolutionarily stable".

- In the end, it seems critical that for multiple strategies to be maintained in the population that there is not only whole-particle mortality (which in effect is highly correlated catastrophic dynamics for an individual microbial population), but that the inflow of resources itself fluctuates. Did I interpret that correctly? Readers may appreciate a slightly clearer description of how this environmental stochasticity differs from the previous possibility of whole-cell mortality, and this also left me wondering how to quantity the kind of environmental stochasticity that will generally lead to multiple strategies coexisting.

So my understanding from this was that whole-cell mortality was not on its own to avoid a single population outcompeting others. but I did not get such a clear picture of what environmental stochasticity WOULD allow for coexistence.

- One other reference that might be tangentially related, but I thought could be relevant: "The importance of being discrete: Life always wins on the surface" by Shnerb et al. This describes growth on particles in 2d or 3d, and shedding (which seems different from but not entirely different from detachment).

This could be an important reference because in this stochastic model, the effective growth rate is different from what you would have with the naive mean field model. So I am wondering if this might change any of the outcomes of Equations 1 and 2.

Reviewer #2 (Recommendations for the authors):

The authors investigated an interesting question related to the coexistence of bacterial species with different detachment strategies on particles. The results of this investigation are interesting and relevant for our understanding of microbial diversity in particle-associated communities, but the manuscript would benefit from a more in depth discussion of results from recent papers on microbial community dynamics of particles, many of which are cited in the current version but only in passing. There are also many possible extensions of this work, which the authors are probably aware of, which would be interesting to explore in future work. For example, the role of search strategies (e.g., random walks vs chemotaxis vs Levy walks) and detachment rates that depend non-linearly on the concentration of bacteria on the particle.

The authors seem to adopt a somewhat strict definition of Optimal Foraging Theory (OFP) limited to the Marginal Value Theorem (MVT). There are examples of OFT studies that do consider mortality and predation risk, finding that predictions of the MVT do not hold in these settings, e.g.:

Abrams, PA. "Optimal traits when there are several costs: the interaction of mortality and energy costs in determining foraging behavior." Behavioral Ecology, vol. 4, no. 3, 1993, pp. 246-259.

Newman, JA. " Patch use under predation hazard: foraging behavior in a simple stochastic environment." Oikos, vol. 61, 1991,

pp. 29-44.

It would be important to know how this study relates to previous results of OFT that do include mortality and predation risk.

In its current form, there are a few places where better description of the numerical simulations performed would critically enhance the manuscript and the reproducibility of the results. Specifically:

- There is a deterministic particle mortality rate mp,i in Equation 3, and an additional, stochastic particle mortality in the section "Bacterial mortality". Are the two implemented with the same rate, and what is the rationale for implementing both forms of mortality? The manuscript text only seems to describe the stochastic particle mortality, but is never too explicit about it. As described in lines 385-394, it seems that the stochastic mortality rate depends on the numerical integration time step: because mp is a rate, a fraction mp * dt of particles, where dt is the integration time step, should be chosen at each time step to impose mortality, rather than a "fraction" mp as suggested by the text at lines 387-389.

- The most problematic section is "Bacteria-particle encounter rate". The authors mention explicitly the encounter probability of spherical cells undergoing random walks, but they need a rate to incorporate in the equations via parameter α. An explicit expression for α is not provided, and I would have expected α to be the diffusive flux towards a spherical absorber (see, e.g., Berg's "Random walks in biology" page 27, Equation 2.20): I = 4 \pi D R C0, where C0 is the concentration of detached bacteria, but this is not mentioned. Also, what is d in Equation 5? It should be Dc,p, and it can't be the detachment rate d. The estimate for the diffusion coefficient of cells via the Einstein-Stokes relationship is too small if bacteria are motile, as suggested by Figure 1. For motile cells, cell diffusion can be orders of magnitude larger than the Einstein-Stokes estimate (see, e.g., Berg's "Random walks in biology" page 93 – Movement of self-propelled objects). The sentence "From Equation 5, we calculated the total number attaching cells to a particle at a given time (t) from free living cells of population i by multiplying the hitting probability to the total number of free-living cells" is very hard for me to interpret: which choice of Dc,p was used in Equation 5? I would also mention explicitly that this entire section assumes instantaneous attachment of bacteria to particles with an infinite rate coefficient.

For a study that is mostly numerical such as this one, availability of the computer code for peer review would greatly enhance the reproducibility of the results and would have clarified some of the doubts expressed above. I would encourage the authors to post it on Github for peer review, or provide it as supplementary material with the submission.

It would be very informative to know under which conditions the analytical approximation described at lines 174-216 breaks down. At low particle density, the search time may be much longer than the growth period on the particle, but at high particle densities this may not be true. Would the approximation work less well in those conditions?
