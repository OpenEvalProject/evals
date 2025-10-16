# Peer review - Round 1

Editors:
- Irene Giardina, https://ror.org/02be6w209 Università Sapienza Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71226.sa0](https://doi.org/10.7554/eLife.71226.sa0)

The work provides new insights into the dual role of chemotactic sensing in both generating and controlling bacterial wave front patterns. Novel and elegant experimental techniques supported by computations using phenomenological models validate the hypothesis that chemotactic sensing smooths morphological variations; however, experiments suggest a richer picture than that predicted by the theory.


---

# Peer review - Round 1

Editors:
- Irene Giardina, https://ror.org/02be6w209 Università Sapienza Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71226.sa1](https://doi.org/10.7554/eLife.71226.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Chemotactic smoothing of collective migration" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both referees reviewed positively the paper. They however suggest a number of clarifications and a more extended discussion of a few issues. The authors are invited to carefully read the attached full reports and to address all the referees' comments in a revised version.

Particular attention must be devoted to:

– Clarify how certain parameters are estimated from the data (e.g. diffusion coefficient, pore properties); discuss the dependence of the susceptibility on pore size and the potential role of bacterial concentration (referee 2).

– Discuss connections with some growth models potentially relevant for the experimental findings presented in the paper (referee 1).

Reviewer #1:

The paper is very clearly written an presents a nice mix of experimental and numerical results. The authors might want to make a connection with the growth-expansion model by Cremer and Honda (see also Narla Cremer and Hwa, arxiv 2103.08100) which appears to be the limiting case of c_{1/2}\to 0 c_{-}\to 0 and infinite carrying capacity. For that model, planar traveling wave solutions exist and their speed and width of the band are analytically known (approximately exact).

It would be interesting to study analytically the transverse stability of such solutions, even though this is clearly outside the scope of the present paper.

Reviewer #2:

Collective bacterial motility relies intimately on the manner by which individual cells sense their environment, chemical and physically sense their neighbors, and adjust to appropriate chemical fields such as nutrient concentrations. In favorable conditions, bacterial cells grow, multiply and move together in well defined fronts or waves. There is a large body of literature on how intrinsic (phenotypic) and extrinsic (environmental) perturbations disrupt these patterns and quench collectivity or destabilize propagating fronts. Here, the authors address the complementary question of how propagating bacterial populations may withstand perturbations. A elegant and novel 3D printing platform that allows for the generation localized, dense bacterial populations with controllable mesoscale structure (wavelength and shape) within a hindering hydrogel medium is used to study the long time spatiotemporal dynamics of bacterial collective motility. Experiments show that initial structured interfaces smooth into rapidly moving bacterial fronts that propagate stably. The authors hypothesize that this autonomous and emergent quenching of destabilizing density perturbations is due to chemotactic response with both single cell and collective aspects playing critical roles. A variation of the Keller-Segel model incorporating bacterial growth, nutrient consumption, and bacterial spread due to diffusion and chemotaxis provides predictions that compare well to experiments and support the hypothesis.

Collective motility with diffusive and (concentration-induced) fluxes feature in many active matter systems; thus insights from this work are applicable to sustained pattern formation in these related systems.

Strengths:

A significant strength of the paper is in the synthesis of novel experiments with variations of a well-established theoretical framework to investigate the role of chemotaxis in modulating bacterial front undulations. The hypothesis is clearly articulated with all features of the growing bacterial population – viz, growth, motility and chemotactic sensing considered in understanding the experiments.

The experimental techniques and protocols that allow for direct imaging of bacterial waves and propagating fronts are novel and allow for cleanly printed sinuous patterns. The hydrogel medium allows for both control of the medium porosity (mean pore size), and also for clean control of nutrient concentration. The data obtained is of high quality and clearly exhibits the smoothing of wave fronts that is the focus of the paper. The permeability of the gel particles allows for experiments where local oxygen and nutrient fields may be sensed easily since small scale gradients are prevented.

It is hard to use the experiments for analyzing the roles played by each of these in isolation.Thus the role of analysis is important – specifically, any phenomenological model used should capture the important biophysical factors that may play a role. The continuum model for chemotactic spread of growing bacterial suspensions (via a Keller-Segel type formulation) is well chosen and carefully analyzed with attempts first to negate the hypothesis (by asking if growth, non-chemotactic diffusion based spreading may mimic the dynamics) and then by proactively supporting it. Computations seem to directly include parameters evaluated from experiments and qualitatively capture the nature of the rapidly propagating wavefronts far from the initial positions. Results with diffusion, and cell proliferation knocked out by choosing parameters appropriately suggest that chemotactic response drives front formation, and is implicated in sustained and unperturbed wave propagation. A strength of this manner of interrogation is the ease by which more complicated features may be introduced in the theory and in the computations. This generality in principle allows extensions to more complicated systems that the authors suggest may benefit from the insights from this paper.

The principle that variations in the driving force (gradient of the nutrient concentration, c here) may compete with variations in cell response to the value of the quantity (the value of c) and overall determine the evolution of undulations at the front is interesting and a crucial insight. Active matter systems such as bacterial swarms, multicellular clusters etc exhibit diffusive, nutrient sensing chemotactic behavior and haptotaxis. Insights from this paper may help understand how emergent patterns remain stable and long-lasting in such systems. The results of this paper and insights will contribute to the on-going dialogue as to the complementary role of collective vs cell-level behavior in controlling motility.

The conclusions of this paper are mostly well supported by the experimental augmented by the computational analysis and associated discussions. Some aspects of the presentation may benefit from further clarification.

1) Some discussion is warranted on the role of additional motility modes such as surface assistant motility and the general tendency of bacteria to stick around near surfaces in mediating the non-chemotactic behavior; and possible surface assistant motility that may help bacteria escape in the initial stages of the wave front formation and propagation and prevent residual trapping. Experiments show a rather striking phenomena for some combinations of the wavelengths and pore size – bacteria located at the point of printing disperse and eventually the central region seems to have local density of bacteria with most of the cells participating in the front and moving away rapidly. The model however seems to suggest that a fraction of the initial cells remain localized at their initial position. Some discussion of how the model may be adapted or modified to account for this will help.

2) Some more clarity and discussion is need to explain how experiments are used to calculate the values of parameters in the simulations. The susceptibility function that connects the convective chemotactic induced flux is dependent on the pore-size and hindrance effects. The effect of confinement for a diffusing nutrient molecule is easy to rationalize based on known literature. The bacterial diffusion coefficient may also be anticipated (for a swimming cell) by using concepts from kinetic theory where an effective diffusion coefficient came be estimated by calculating the mean speed between either tumbling events, wall interactions and reorientations, or cell-cell interactions and reorientations. The manner in which Chi may vary with pore size is however unclear and needs some elaboration. Here, the form of the pore size distribution in addition to the mean pore size may be important.

3) Bacterial cell properties need to be mentioned and connected to pore geometry. Specifically, the cells are stated to have a characteristic size. But bacteria are rods with high aspect rations. Given this, does the concentration of the cells correspond to a semi-dilute or concentrated suspension. If sufficiently concentration alignment effects may arise that augment and enhance over-all spread in addition to chemotaxis based flux.

I encourage the authors to address the following comments in their response or revision.

1) The pore size is a crucial feature in the experiments. However only the mean pore size is reported. It would help to have an estimate of the pore size distribution.

2) Close ups of the bacterial concentration fields in Figure 1(C,D,E) would be very helpful. While the t=0 case is probably difficult to show due to the rather high density of bacteria, how about the large t values ? The experiments do suggest that the bacteria are moving in suspension and not along the gel surfaces. Is this something that can be checked by looking at the suspensions at higher resolutions?

3) The analysis of chemotaxis (following equation 3, and subsequent discussion) brings up an important fact. The physics involves two competing effects – the spatial variation in c that actually amplifies front undulations and irregularities and the intrinsic chemotactic response that allows for receptors to saturate. The form of the response function f(c) and the form of Chi used in the paper is relevant to E. coli. Can the authors further comment on if and how one may modify f(c) and chi to suppress or enhance these effects. There is discussion of this in the final section – however a sample computation that illustrates this would emphasize this point.

4) There are some experimental details missing in the paper. How was the diffusion coefficient D_b measured? For a dense suspension of bacteria (without chemotactic effects), the effective long-time bacterial diffusivity may depend on the concentration of bacteria due to cell-cell interactions and alignment in a manner seen in dense suspensions of rods. Was this done in the dilute regime by tracking single bacteria MSD or was this done when the concentration of bacteria was high?

5) The discussion on calculating the mean separation between cells in the methods section is a tad confusing and needs clarity. A recapitulation or summary of the results from the previous publication would help here.
