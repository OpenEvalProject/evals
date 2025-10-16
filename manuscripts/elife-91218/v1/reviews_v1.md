# Peer review - Round 1

Editors:
- Toby W Allen, RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91218.3.sa0](https://doi.org/10.7554/eLife.91218.3.sa0)

This important study employs multiscale simulations to show that PIP2 lipids bind to DIV S4-S5 linkers within the inactivated state of a voltage-gated sodium channel, affecting the coupling of voltage sensors to the ion-conducting pore. The authors demonstrate that PIP2 prolongs inactivation by binding to the same site that binds the C-terminal during recovery from inactivation, and they suggest that binding to gating charges in the resting state may impede activation, both findings that contribute to our understanding of sodium channel modulation. The coarse-grained and atomistic molecular dynamics simulations are convincing, including state dependence and linker mutants to back up the claims.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91218.3.sa1](https://doi.org/10.7554/eLife.91218.3.sa1)

Summary: Here, the authors were attempting to use molecular simulation or probe the nature of how lipids, especially PIP lipids, bind to a medically-important ion channel. In particular, they look at how this binding impacts the function of the channel.

Strengths: The study is very well written and composed. The techniques are used appropriately, with plenty of sampling and analysis. The findings are compelling, and provide clear insights into the biology of the system.

Weaknesses: A few of the analyses are hard to understand/follow, and rely on "in house" scripts. This is particularly the case for the lipid binding events, which can be difficult to compute accurately. However the provision of these scripts on github means that these can be assessed by the reader if desired. Additionally, a lack of experimental validation, or coupling to existing experimental data, limits the study.

It is my view that the authors have achieved their aims, and their findings are compelling and believable. Their findings should have impacts on how researchers understand the functioning of the Nav1.4 channel, as well as on the study of other ion channels and how they interact with membrane lipids.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91218.3.sa2](https://doi.org/10.7554/eLife.91218.3.sa2)

Summary:

Lin Y., Tao E., et al. used multiscale MD simulations to show that PI(4,5)P2 binds stably to an inactivated state of Nav channels at a conserved site within the DIV S4-S5 linker, which couples the voltage sensing domain (VSD) to the pore. The authors hypothesized that PI(4,5)P2 prolongs inactivation by binding to the same site where the C-terminal tail is proposed to bind during recovery from inactivation. They convincingly showed that PI(4,5)P2 reduces the mobility of both the DIV S4-S5 linker and the DIII-IV linker, thus slowing the conformational changes required for the channel to recover to the resting state. They also conducted MD simulations to show that phosphoinositides bind to VSD gating charges in the resting state of Nav channels. These interactions may anchor VDS at the resting state and impede its activation. Their results provide a mechanism by which phosphoinositides alter the voltage dependence of activation and the recovery rate from inactivation, an important step for developing novel therapies to treat Nav-related diseases. However, the study is incomplete lacks the expected confirmatory studies which are relevant to such proposals.

Strengths:

The authors identified a novel binding between phosphoinositides and the VSD of Nav and showed that the strength of this interaction is state-dependent. Based on their work, the affinity of PIPs to the inactivated state is higher than the resting state. This work will help pave the way for designing novel therapeutics that may help relieve pain or treat diseases like arrhythmia, which may result from a leftward shift of the channel's activation.

Weaknesses:

However, the study lacks the expected confirmatory studies relevant to such proposals. For example, one would expect that the authors would mutate the positive residues that they claim to make interactions with phosphoinositides to show that there are much fewer interactions once they make these mutations. Another point is that the authors found that the main interaction site of PIPs with Nav1.4 is the VSD-DIV and DIII-DIV linker. This interaction is expected to delay fast inactivation if it happens at the resting state. The authors should make a resting state model of the Nav1.4 channel to explain the recent experimental data showing that PIP2 delays the activation of Nav1.4, with almost no effect on the voltage dependence of fast inactivation.

The reviewers answered most of my concerns about the first version of the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91218.3.sa3](https://doi.org/10.7554/eLife.91218.3.sa3)

Summary:

This work uses multiscale molecular dynamics simulations to demonstrate molecular mechanism(s) for phosphatidylinositol regulation of voltage gated sodium channel (Nav1.4) gating. Recent experimental work by Gada et al. JGP 2023 showed altered Nav1.4 gating when Nav1.4 current was recorded with simultaneous application of PI(4,5)P2 dephosphorylate. Here the authors revealed probable molecular mechanism that can explain PI(4,5)P2 modulation of Nav1.4 gating. They found PIP lipids interacting with the gating charges - potentially making it harder to move the voltage sensor domain and altering the channels voltage sensitivity. They also found a stable PIP binding site that reaches the D_IV S4-S5 linker, reducing the mobility of the linker and potentially competing with the C-terminal domain.

Strengths:

Using multiscale simulations with course-grained simulations to capture lipid-protein interactions and the overall protein lipid fingerprint and then all-atom simulations to verify atomistic details for specific lipid-protein interactions is extremely appropriate for the question at hand. Overall, the types of simulation and their length are suitable for the questions the authors pose and a thorough set of analysis was done which illustrates the observed PIP-protein interactions.

Weaknesses:

Although the set of current simulations and analysis supports the conclusions drawn nicely, the course-grained simulations have further utility than that utilized by the authors. With the 4to1 heavy atoms bead mapping in Martini 2 some detailed chemical specificity is averaged out but parameters for different PIP family members do exist - including specific PIP(4,5)P2 vs PIP(3,4)P2, and could have been explored at the course-grained level. However, performing more detailed all-atom simulation, as done in this manuscript, is always advisable to extend and/or confirm course-grained results.
