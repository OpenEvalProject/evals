# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Nottingham United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51032.sa1](https://doi.org/10.7554/eLife.51032.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper presents a thorough combination of EM and computational modelling to explain the short term plasticity of synaptic release.

Decision letter after peer review:

Thank you for submitting your article "Rapid regulation of vesicle priming explains synaptic facilitation despite variable vesicle:Ca2+ channel distances" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Victor Matveev (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. While eLife aims to prevent long review cycles and substantial additional work, the reviewers have identified quite a number of distinct issues. In subsequent discussions these were all deemed relevant to support the study's conclusion. However, a number of issues can be addressed by providing a deeper discussion of the limitations and assumptions of the study.

Summary:

This work combines experimental recordings with mathematical modeling to investigate mechanisms of Ca2+-exocytosis coupling and facilitation (STF) at Drosophila NMJ. The distinguishing feature of this study is that vesicle-channel distances were carefully mapped, allowing the authors to investigate the implications of non-uniform channel-vesicle distance on NT release at this NMJ. The main conclusion of this work is that many traditional models cannot account for the STF observed at this NMJ, given the observed distribution of channel-vesicle distances. The reason is that traditional models explain STF through changes in the vesicle release probability, but the latter is very high close to the Ca2+ channel, and very low far from the Ca2+ channel. Therefore, very few vesicles would feel the effect of small Ca2+ accumulation. The authors propose and test an alternative model which explains the observed properties of neurotransmitter release at this terminal. This model posits that vesicle undergo priming prior to becoming fusion-ready. Although similar STF models have been recently considered by others (as cited in this work), the presented model is more comprehensive, implements important stochastic effects, and proposes inhibition of de-priming rather than acceleration of priming as a key target of Ca2+ action. An alternative "site activation" model is also presented, and there is some parameter sensitivity analysis included.

The hypothesis presented for STF and Ca-exocytosis coupling is in general interesting, and the model comparisons presented contribute to the understanding of this problem.

Essential revisions:

1.1) Equation 2: The whole Ca2+ current calibration is very hard to follow, and is my main concern regarding methods description. In Equation 2, shouldn't KM be raised to power "h"? Also, this expression gives the relationship between fluorescence and intracellular Ca2+, or was the fluorescence recorded with extracellular GCaMP? Further, why is KM determined from GCaMP6 calibration? Isn't KM an innate property of the Ca channel conductivity (and possibly Ca-dependent inactivation), having nothing to do with the indicator dye? The entire Ca2+ current calibration has to be explained much more clearly, I could not follow it.

1.2) Unless I misunderstood the modeling/methods, the described stochastic simulation process, while technically correct, appears needlessly complicated and computationally expensive. Any Markov Chain with a single absorbing state and deterministic propensities ([Ca] is deterministic here) is described exactly by its master equation ODE, and the first passage time probability density (vesicle release time density) is directly and exactly computed from this ODE system as the transition rate to the final absorbing state. Therefore, Gillespie SSA simulations are not required, and the only Monte Carlo step involves drawing the vesicle release time from this exact probability distribution, without having to simulate/resolve any intermediate reaction times (once vesicle is released, one may have to recompute the FPT density, but that's not expensive). This should not affect the results, but would greatly improve the simulation efficiency, accuracy, and simplify the parameter sensitivity analysis. Since this should not affect the results, I would not request any significant modifications, but this could be somehow reflected in Materials and methods and checked (unless I misunderstand something and the transition rates are in fact stochastic).

1.3) Subsection “Rate equations of the simulated models”: this part of Materials and methods is particularly hard to read, and could be improved just by a simple re-structuring. It is awkward to explain parameters before the actual equations are shown. The rate dependence on [Ca2+] in subsection “Rate equations of the simulated models” seems strange: shouldn't there be a power of "n" in both terms in the denominator?

1.4) Discussion paragraph ten: when discussing alternative STF scenarios beyond "pVr-based" models, it could be appropriate to specifically distinguish between models where all vesicles have the same properties, and models with distinct vesicle pools with different properties (such as the super-primed pool models cited in various parts of the manuscript). Of course, this distinction is complicated, since vesicle pool heterogeneity could result from vesicles being in different transient states along the same slow priming processes, but this could also be pointed out… If the authors find it appropriate, they could also mention here the putative "highly Ca2+-sensitive pools" at endocrine cells, which I find interesting and potentially relevant (reviewed in Pedersen and Sherman (2009) PNAS 106:7432-7436).

1.5) It would be valuable to briefly comment on the facilitation decay time constant predicted by their model, since facilitation decay provides a powerful additional constraint on the potential model mechanism of STF. Even if experimental data on STF decay is not available in this case, the decay time constant could be presented as a prediction to be verified in future experimental work. The authors could simply quote the relevant priming/unpriming time scale determining STF decay to avoid additional simulation. I note that matching facilitation decay time course puts a strong constraint on the single-sensor and dual-sensor models, and is an extra issue with such models among those mentioned in this work (see e.g. Matveev et al., 2002, cited in this manuscript).

1.6) Discussion paragraph nine: since the site activation model is not described in detail in Results or Discussion, but is one of two presented new models reproducing experimental observations, it would be helpful to describe it slightly more in this part of the manuscript, if not earlier (1-2 more sentences would suffice).

1.7) When the dual-sensor model is first introduced, it would be appropriate to more prominently cite the related work of Sun et al., 2007, (which the authors cite elsewhere). Further, when discussing various STF models and prior work in this direction, I suggest citing the study of Ma et al., 2015, which is one of the most detailed models of STF and involves a fully stochastic approach: https://www.ncbi.nlm.nih.gov/pubmed/25210157.

2.1) While the characterization of the vesicle distribution is well done. It remains possible that the vesicles are not drawn independently from the distribution. In an extreme case, the number of vesicles could be fixed, or they could repulse each other, and yet the same distribution could still be found. I wonder if this can be discussed.

2.2) The role of heterogeneity in release and averaging across experiments (alluded to in Discussion paragraph six) is not clear to me. It would be good to know that the authors have convinced themselves that such heterogeneity does not over-estimate variance or otherwise change the results.

3.1) The EM analysis was conducted in mutant animals. Exact genotypes were not provided, but based on the information in Reddy-Alla et al., 2017 where the data were originally published I think they are working with Unc13 null animals expressing UAS-Unc13A via a Gal4 driver. This data is being used to drive models of normal synaptic function, so it's critical that this experiment is conducted in wild-type animals with normal levels of Unc13.

3.2) The authors use the data presented in Figure 1D to place synaptic vesicles relative to Ca2+ channels in their models. It's difficult to discern the number of animals, NMJs and active zones from the numbers provided: "n=19 observations in 10 EM cross sections/cells." This information should be clearly stated. Assuming an observation is a docked vesicle and a cross section is an active zone, the 3D placement of vesicles was derived from the observation of 19 docked synaptic vesicles in single sections of 10 active zones. Given that the central thesis that vesicles are heterogeneously distributed, so few observations cannot confidently capture the biological range.

This also suggests less than two docked vesicles per cross section, which is somewhat lower than docked vesicle/active zone numbers at wild-type Drosophila type Ib synapses previously reported by multiple groups, including the authors' prior work. This could be the genotype (see below) and/or the fact that single sections do not accurately capture the full complement of docked vesicles at an active zone. For example, vesicles that appear close to, but not in contact, with the membrane in one slice, may be in clear contact with the membrane in an adjacent plane. 3D EM approaches, which have been done at the Drosophila NMJ, would provide much better estimates of synaptic vesicle topology and obviate the need for deriving 3D estimates based on limited information.

3.3) It is well documented that the hundreds of active zones at Drosophila NMJs are of different developmental stages with very different morphologies and release properties, so the distribution of synaptic vesicles observed at a handful of active zones can't accurately represent the NMJ as a whole. This will be very challenging to address experimentally, but should at least be considered in their interpretations and addressed in the Discussion.

3.4) The study seems to involve a mixture of analysis of two motorneuron subtypes with different structural and functional properties without considered this in the modeling. Though not always stated, it looks like the EM, STED and GCaMP experiments were conducted at type Ib synapses, while the electrophysiology measured the compound response to both Ib and Is motor inputs. Can they specifically measure and model type Ib?

3.5) I think wild-type animals were investigated in the STED and electrophysiology experiments, but the genotypes are not noted. All genotypes should be clearly labeled in figures. Additionally, since the data is being re-used here, this manuscript should provide all relevant methods rather than referring readers to the earlier publication. The STED results appear to be based on three animals from a single previously published experiment. Have any technical replicates of this experiment been performed to control for experimental variability?

3.6) There are very few references to other Drosophila labs working in this area. Multiple labs have conducted relevant work on the distribution of synaptic vesicles, Ca2+ channels, and heterogeneous release properties at this synapse that should be cited.
