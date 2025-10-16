# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64176.sa1](https://doi.org/10.7554/eLife.64176.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper, the authors report new results on the collective behavior exhibited by bacteria under confinement. Using microwells of specific sizes on agar surfaces, they found swarming bacteria exhibit a "single-swirl" motion pattern and concentrated planktonic bacteria exhibit "multi-swirls" motion pattern in the diameter range of 31-90 μm. Systematic experiments explore parameters defining the divergence of motion patterns in confinement including cell density, cell length, cell speed and surfactant. They conclude that the single-swirl pattern depends on cohesive cell-cell interaction mediated by biochemical factors removable through matrix dilution.

Decision letter after peer review:

Thank you for submitting your article "Confinement Discerns Swarmers from Planktonic Bacteria" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yan He (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that major revisions are needed before it can be accepted for publication, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this paper, the authors proposed a new approach by mounting a PDMS microwells of specific sizes on agar surface to confine swarming and planktonic SM3 cells. They found swarming bacteria exhibit a "single-swirl" motion pattern and concentrated planktonic bacteria exhibit "multi-swirls" motion pattern in the diameter range of 31-90 μm. The phase diagram shows that in smaller wells concentrated planktonic SM3 forms a single vortex and in larger wells swarming SM3 also breaks into mesoscale vortices.

In addition, they conducted systematic experiments to explore parameters defining the divergence of motion patterns in confinement including cell density, cell length, cell speed and surfactant. They concluded that the single-swirl pattern depends on cohesive cell-cell interaction mediated by biochemical factors removable through matrix dilution.

This paper gives a new method to discern swarmers from planktonic bacteria and carefully studies the factors that influence the formation of bacterial vortices under restriction.

Essential revisions:

While generally supportive of the paper, the reviewers found that major revisions are necessary to clarify aspects of the experiments and the connection between experimental findings and numerical simulations, the modeling approach and the interpretation of numerical results.

1. When the authors put the PDMS chip mounting on the edge of the swarming colony, the PDMS chip is completely attached to agar or suspended in a bacterial solution. The distance between PDMS chip and agar surface should be quantified. It is better to have a schematic diagram of the experimental device.

2. Are the bacteria still expanding outward after a PDMS chip was mounted on agar surface? The effect of PDMS chips on the expansion of bacteria on the agar surface needs to be discussed.

3. "Diluted swarming SM3 show unique dynamic clustering patterns". In the diluted bacteria experiment, the authors found that the diluted swarming bacteria can form bacterial rafts and the concentrated planktonic SM3 disperse uniformly and move randomly. Hence, when bacteria expand and gradually fill up new empty microwells, is there a process of transition from raft to single vortex state?

4. In the experiment of altering the conditions of swarming SM3, the authors diluted the swarming cells in Lysogenic Broth (LB) by 20-fold, re-concentrated the cells by centrifugation and removed extra LB to recover the initial cell density. After these operations, they found the previous single swirl turned to multiple swirls and concluded that matrix dilution can affect single-swirl pattern. The authors conjecture that centrifugation may wash away some surrounding matrix or polymers on the surface of bacteria. Therefore, the steps of centrifugation need to be presented and the effect of centrifugation on the physiological behavior of bacteria should be discussed.

5. This work covers the PDMS chip directly on the agar surface and finds that swarm and planktonic bacteria have different spatial correlation scales in the restricted microwells. The authors have done many experiments to prove the difference between clusters and planktonic bacteria and explain the reason for the single vortex. However, the conclusion is not clear. Therefore, the authors should focus more on the analysis of this new experimental phenomenon, such as critical length and vortex phase diagram, rather than just describing the experiments they did.

6. The authors mentioned the critical length for swarming SM3 is ~49 μm, whereas, for concentrated planktonic SM3, it is ~ 17 μm. Does this quoted data match that which they obtain from their experimental method? I do not see any follow-up discussion and evidence.

7. As shown in Figure 1 and Video S1 mp4, the direction of the single vortex motion of bacteria is clockwise. However, the article simply ignores that the single vortexes of bacteria all present the same direction, and there is no analysis and reasonable explanation on the vortex direction. As shown in Video S5 mp4 on the numerical simulations of circularly confined SM3, simulated bacteria vortex counterclockwise in completely opposite directions. The influence of the microwell boundary on the direction of the vortex should be clearly explained at the level of bacterial movement and preferentially with a numerical simulation.

8. Swarming and concentrated planktonic Bacillus subtilis 3610 show the same motion pattern across different confinement sizes. However, the authors did not give definitive conclusions and evidence. As shown in Figure S1, Bacillus subtilis 3610 show completely different cluster behavior. Therefore, the discussion of 3601WT may cause readers' confusion on the article. It may be better to put it in the supporting material.

9. A central finding of the present study is that the number of vortices/swirls as a function of the well diameter differs for swarming vs. swimming bacteria. The authors argue and show experimentally (Figure 2) that the behavior is identical for small and large diameters. For intermediate values, however, they report that a single swirl is observed for swarming bacteria whereas swimming bacteria show multiple swirls.

The fact that the behavior is identical for large wells suggests that the bulk behavior is identical. This is also confirmed by Figure 2E which shows that the spatial correlation function of the velocity is identical in large wells. That suggests that the boundary conditions play a central role in understanding how the observed phenomenology emerges. [Indeed, it was shown in the past that the interaction of bacteria with boundaries crucially determines the formation of swirls in confinement (Lushi, Wieland and Goldstein PNAS 111 9733 2014). The authors of this work assume reflecting boundary conditions, which – to my knowledge – contradicts the finding of Lushi et al.].

The authors, however, explain the difference of the observed patterns within their modeling study in a different way, namely by a different strength of the (anti-)alignment interactions. Changing the interaction at the level of individual cells will, however, change the bulk behavior too. Accordingly, the numerically observed bulk behavior (Figure 5B ) is very different in both cases (at a qualitative level). It is difficult to judge the difference in detail because the correlation function was not calculated for the simulations.

In short:

– The model (Figure 5A) reproduces the experimental results partially (Figure 2C), but the modeling analogue to Figure 2E is missing;

– The line of arguments seems not to be entirely consistent.

10. Inferring the interactions of active particles from observations of the emergent patterns is a highly non-trivial task. In view of this the reviewers are not entirely convinced by the arguments put forward by the authors that "more substantial cell-cell cohesive interaction(s)" are the reason why the swirling patterns formed by swarming/swimming bacteria differ.

In this context, we call attention to Ref. [Peruani, Deutsch and Bär: Phys. Rev. E 74 030904(R) 2006]. In this work, a clustering transition of self-propelled rods was described. "Rafts", referred to as clusters by Peruani et al., are observed as the aspect ratio of rods is increased. Notably, a kinetic transition towards clustering can emerge even in the absence of any attractive interactions.

In short, the observation that cells move in parallel (polar clusters) next to each other does not allow to conclude that cohesive interactions are present.

The Videos S3 and S4 provided by the authors show that the particle shape of swarming and swimming particles is clearly different. In particular, the elongated swarming bacteria show pronounced clusters (Video S3) whereas the shorter planktonic cells (Video S4) do not. The difference in aspect ratio does indeed suggest that swarming and swimming bacteria differ in their alignment interaction. However, this contradicts the observation that spatial correlations in large wells are indistinguishable (see comment 1 and Figure 2E).

Side remark: in the main text, the authors argue that changes of the aspect ratio are not the reason for an increased alignment interaction, however, in the Discussion section cell morphology changes (e.g. cell elongation and hyper-flagellation) are mentioned as an indicator that swarming is a different phenotype from swimming.
