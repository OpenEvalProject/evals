# Peer review - Round 1

Editors:
- Alphee Michelot, Institut de Biologie du Développement France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82658.sa0](https://doi.org/10.7554/eLife.82658.sa0)

This important paper uses molecular simulations to explain how actomyosin networks transition from small clusters to the cortex or ring-shaped actin networks. The authors provide compelling evidence that variation in filament turnover rate and myosin concentration triggers a phase transition of these networks. The predictions of this model are consistent with observations made in T cells, where actin ring formation can be induced following their activation by antibodies.


---

# Peer review - Round 1

Editors:
- Alphee Michelot, Institut de Biologie du Développement France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82658.sa1](https://doi.org/10.7554/eLife.82658.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A tug of war between filament treadmilling and myosin induced contractility generates actin ring" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Anatoly B. Kolomeisky (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

You will find that the reviewers have a very positive opinion of your work. Their comments should be easy to address. Please respond to them point by point.

Reviewer #1 (Recommendations for the authors):

I have several specific comments and suggestions that might improve the paper:

1) It would be nice to discuss why rings are observed only in a few types of cells, but not in all of them. Is it known?

2) NMII on page 5 should be properly defined first - it is not done here.

3) On page 6, the authors said that they "excluded NMII from the peripheral region..." But what would happen if simulations started with motor proteins uniformly distributed over the system?

4) I would add a brief discussion that entropic terms most probably are not important for this system, and thus the mechanical energy provides a valid thermodynamic quantity to decide about the proper phase. This is because one could naively argue that in the ring structures the entry is reduced due to higher density.

Reviewer #2 (Recommendations for the authors):

A] Expanding on public review:

– Additional simulation controls are needed:

While the mean length of filaments according to the depolymerization rate is given, the length distribution in the different conditions is not provided – while this distribution has a strong effect on the ring-like organization of actin in confinement. Moreover, in the simulation of lat A treatment, a control that in-silico actin concentration matches the in-vivo one is missing.

– Confusing description of rings/experiment – simulation discrepancies

For instance, the ring in the control of latA treatment (Figure 4a) seems much more focused than that of WT (Figure 1A). In figure 5, supp. 2 it is hard to understand why the simulated ring is contracting in the control condition. Is time 0 not the stationary solution? Then, how is time 0 chosen?

Also, in figure 1, the ring seems much more realistic than in the following.

I am assuming the authors focused on a simpler system with fewer ingredients to establish the phase diagram, but this needs to be made clearer. Also, why not do a phase diagram with a simpler system, and a more realistic system to compare to experiments?

For now, the comparison between experimental results and simulations is not as strong as claimed. Either the conclusions could be toned down a bit, or the discrepancies should be clearly discussed.

– MEDYAN license

This is not directly relevant to this article but falls under the public review guideline "the utility of the methods and data to the community".

While MEDYAN being an open source software is a great boon for the community, it is crippled by its own license. The item 3 "Users can modify the MEDYAN source code for their own academic and research purposes, but cannot redistribute modified MEDYAN source code that differs in any way from Papoian lab's current MEDYAN distribution" goes against the core idea of open source scientific software: if a team decide to build upon MEDYAN, they will not be able to publish the modified code, and thus will not be able to share their results in a significant manner.

Moreover, the guideline "cannot redistribute any other codes that use or extend any MEDYAN source code" prevents anyone from sharing wrappers and utilities for MEDYAN. Most scientific software uses the GPL (most restrictive) or MIT (most permissive) license with great success.

Our main value as scientists is the production and sharing of knowledge – such a restrictive license does not seem to achieve this goal.

– Patches as a metastable state: this is a bit confusing or over-stated. First, this is a highly out-of-equilibrium active system, and I do not think "metastable" quite applies. Both are fundamentally unstable states. A more likely claim is that treadmilling allows for a faster relaxation of filament elastic energy.

B] Additional comments:

– This is a very well-written article that is highly interesting – yet easy to read.

– The claim that ring organization is not understood, not found in vitro, is far-fetched. First, actin rings in vitro have been observed, e.g. Miyazaki et al. 2015 to name one. Second, simulation of actin rings exists, cf Vavylonys 2008, Hang 2015, Nguyen 2018, Koudehi 2016; see also Dmitrieff 2017 for a ring of microtubules. In all these systems, confinement and filament length plays a major role in a ring formation, but the interplay between the rate of treadmilling and motor activity has not yet been really discussed to my knowledge. This is why not only the mean, but also the distribution of filament length has to be documented, and the role of confinement has to be discussed. The existing literature has to be more discussed.

– The difference in filament orientation in Figure 2 supp 4 is striking. I suspect that this could make for a much more striking phase diagram (by computing some order parameter for instance) than the current phase diagram.
