# Peer review - Round 1

Editors:
- Bruce Stillman, Cold Spring Harbor Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35192.013](https://doi.org/10.7554/eLife.35192.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The eukaryotic bell-shaped temporal rate of DNA replication origin firing emanates from a balance between origin activation and passivation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Based on the three positive reviews, it is possible that this model can by published in eLife, but there are some issues that two of the reviewers raise that require a response. Once a response is received, the paper will be re-considered.

Summary:

This appealing paper advances a new hypothesis to explain the observed, apparently quite general phenomenon in eukaryotic replication that the initiation rate of origin firing (relative to the amount of unreplicated DNA) decreases at the end of S-phase after having increased substantially throughout the first part of S-phase. There is agreement on the mechanism of the increase, but three different groups (one of which includes two of the present authors) have advanced three different hypotheses (subdiffusive motion, a dependence on replication fork density of firing factor affinity for p-oris, or inhomogeneous firing probabilities). The present paper proposes a fourth, that the limiting factor is the finite average spacing between potential origins (p-oris) and makes a case that this new hypothesis is both simple and natural. The evidence presented is a mix of heuristic argument, simulation, and a limited comparison of experimental data. The major experimental test is of a simple relation derived by the authors, Imax ~ v ρ02, where Imax is the maximum initiation rate, v the fork velocity, and ρ0 the density of potential origins at the start of S-phase. The authors further look at a 3d simulation of the diffusion process in a simple model where all origins are treated on an equal footing and find a qualitative agreement in the I(t) curves.

The paper thus gives a simple model that advances our understanding of the replication process, adding a reasonable dynamical model to explain kinetics, and providing at least some experimental support-probably not enough to be completely convincing on its own but enough to make others take the hypothesis seriously and inspire further experimental tests. It is thus a nice advance.

Having said all of this, there are questions / reservations about some of the details as outlined below.

Essential revisions:

1) In the figures given for Xenopus laevis in Table 1, the value of ρ0is given as 0.333/kb, with Loveland et al. the reference. In that reference, though, Figure 3D shows only that the minimum average distance between fired origins decreases to 3kb. This implies only a lower bound on ρ0, since there may be passive replication in those experiments.

2) The 3D simulations, if they are understood correctly, will fail to reproduce the known genome-position dependence of firing times. Put another way, the authors argue in the Discussion section (second paragraph) that their modeling implies that all p-oris are the same. But in the S. cerevisiae data (and for other organisms), there are known dependences of median firing time on genome position. It may be that the model set forth here does a good job explaining the I(t) dependence but not the full I(x,t) dependence, where x is the genome position.

3) In a related point, the authors speculate that enhanced firing rates could result from diffusion of factors released. However, there is also evidence that chromatin looping can inhibit the firing of neighboring origins. Both effects could be present, suggesting that untangling spatiotemporal correlations might be subtle.

4) When the authors modeled replication in the presence of HU, it appears that the only change made in the parameters from unperturbed replication was the speed of replication forks. Is this correct? If so, it is surprising, as activation of late-firing origins are suppressed or delayed in HU, and according to Figure 1a, one might expect less origins to be passivated with slower replication forks in HU. The authors need to comment on this.

5) Figure 2B: It was unexpected that dubious origins needed to be included for better modeling. The authors need to discuss potential reasons for this.

6) It has been proposed that DNA replication takes place at replication foci in vivo, where replication factors are highly concentrated. Based on the authors' model that the localization of origins and recycling of replication factors can explain most of DNA replication kinetics, the authors need to discuss how the presence of replication foci would affect origin usage and replication kinetics.

7) The paper does not cite a published model for DNA replication timing by Miotto et al., 2016 that essentially states that there are more ORC sites than are utilized during S phase and early replicating regions at the beginning of S phase is favored simply because there are far more ORC sites, whereas firing from relatively few ORC sites in late replication regions is due to increased time and the unavailability of ORC sites previously replicated. This paper should be cited and discussed to compare it to the proposed model.
