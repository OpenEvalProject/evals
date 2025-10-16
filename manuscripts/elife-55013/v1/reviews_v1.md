# Peer review - Round 1

Editors:
- Satyajit Mayor, Marine Biological Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55013.sa1](https://doi.org/10.7554/eLife.55013.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Second messengers, typically small molecules such as cAMP and ions such as Ca2+, regulate a variety of intracellular processes. Understanding their spatial and temporal distributions as well as their dynamics is important to appreciate the spatial biochemistry controlled by these agents. In their manuscript the authors have been able to map exactly this for the oscillations of cAMP and Ca2+. Their analysis reports that the local oscillations of cAMP occur out-of-phase with respect to the oscillations of Ca2+, but in-phase in the rest of the cell. This has implications for the spatial and temporal control of the biochemistry regulated by this second messenger.

Decision letter after peer review:

Thank you for submitting your article "Spatially compartmentalized phase regulation of a Ca2+-cAMP-PKA oscillatory circuit" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: André Nadler (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Tenner et al. describes how spatial confinement of AMP cyclases can entrain the temporal concentration profile of its product cAMP to an oscillating calcium concentration profile. They address an extremely interesting topic that is currently receiving well-deserved attention: The notion that cells encode information not only through on/off switches in the respective signaling circuits but also in the dynamic profiles of the signaling responses. They provide compelling evidence for a two-state system featuring either in-phase or out-of-phase cAMP/calcium oscillations. They use FRET sensors targeted either to a specific (signaling) nano-compartment (AKAP79/150) at the plasma membrane or to the general plasma membrane to demonstrate that these states are due to distinct signaling dynamics on the nanoscale, a conclusion that is further underlined by simulations from a kinetic model describing this behavior.

They propose that a cluster of multiple calcium-sensitive ACs in the membrane shift the balance for the calcium-sensitive cAMP pool to become in-phase with the calcium signal itself, at increased calcium levels. In contrast, in regions away from the clusters, calcium-sensitive cAMP degradation by PDEs during periods of increased calcium drives the cAMP levels to become out-of-phase. In fact, the study goes full circle in illustrating how the spatially induced driving of a phase shift (calcium -> cAMP) could be related to the maintenance of the calcium oscillatory signal itself (via PKA). In general, the authors provide a well written narrative that includes microscopy of protein organisation at the nanometer scale, local and dynamic measurements of activity, and a modelling frame to interpret the data. Overall, this is a very interesting manuscript which would be of considerable general interest (and suitable for eLife) after a number of revisions to strengthen the experimental support for its core hypothesis.

Essential revisions:

A) AC8 nanoclustering and measurement of localized cAMP:

1) Although the STORM images of AKAP79 and AC8 make a plausible case that they are colocalized in nanoclusters a more convincing case would be made if the authors had carried out 2-color STORM.

The authors suggest that a cluster needs to contain 'many' AC8 proteins. Please provide a number: The authors have STORM data as well as simulations. For the reaction diffusion model the authors need to assume that the membrane patterns (AKAP79/150 – AC8 clusters) are immobile. If the domain should be immobile not with respect to a calcium-cAMP oscillation (on the order of 10s of seconds) it would be important to provide data to support this (FRAP, SPT or sequential imaging). How does a cluster of a few molecules of AC8, along with its scaffolding protein remain immobile in the fluid membrane? Is it known what generates and holds the AKAP79/150 compartment in place?

2) How critical is AC8 nanoclustering? Clearly under endogenous expression levels a displacement from the AKAP79/150 compartment disrupts the regularity of the calcium oscillations. But that is under the condition of the PDE activity that is present everywhere in the cytosol. What if the requirement is a calcium-dependent increase of cAMP production above the baseline? Then simple over expression of AC8 should be enough to entrain the calcium oscillations properly. Indeed, Figure 2E seems to suggest that to be a possibility. How critical is nanoclustering of AC8 in such a scenario of overexpression?

B) Sensor design

While the utilized sensor design based on the human protein may be of broader general interest, here a human protein (AKAP79) is used for targeting to a signaling nanodomain in a mouse cell line. The human and the mouse proteins are only 53% identical, thus it is not clear if they can in fact functionally substitute for each other, ensuring that the sensor indeed localized to the AKAP150/79 compartment.

This could for instance be confirmed using the already utilized AKAP150 antibody and an anti-FP antibody in a STORM (or other super-resolution) colocalization experiment. It would be better to generate a construct using the mouse protein and show in representative datasets that the observed phase-shift of cAMP oscillations is still observed. It is also not clear how the presence of a second protein pool (with likely different affinities for interacting proteins), in addition to the endogenous AKAP150 pool, would affect the outcome of the modelling. Possible complications may be discussed.

C) Perturbation of protein concentrations

The authors use overexpression of proteins as perturbations (e.g. for AC8). They do not, however, provide data on the actual changes of protein levels – only the amount of plasmid used for transfection is reported in Figure 2—figure supplement 2. The authors should quantify the changes of AC8 expression on the protein level, ideally in absolute numbers, however, if this is not possible, a combination of immunofluorescence data (to give the reader an estimate of the cell-to-cell variability) and western blot data would be sufficient here.

Does AKAP79 overexpression have an effect on endogenous AC8 expression levels?

Given that AKAP150 and AC8 physically interact, it is possible that their expression levels are co-regulated. Thus, it is at least conceivable that AK79 overexpression (through the FRET construct) could change AC8 expression levels. Given that AC8 concentration is a key factor in determining the phase offset of calcium/cAMP oscillations, this should be tested by quantifying AC8 on the protein level for overexpression of both the Lyn- and the AKAP79 based FRET constructs.

This could be done by western blot or MS to get an idea on the effect on the cell population level, but also by immunofluorescence imaging data on the single cell level (colocalization experiments using both anti-FP and anti-AC8 antibodies to estimate the effects of cell-to-cell variability).

D) Modelling Issues:

The modelling is competently done with well-established software in the field. The authors have made a couple of design decisions that should be probed: (1) the use of Michaelis-Menten enzyme kinetics, rather than multi-step mass-action (2) Not using stochastic calculations. The stochastic analysis would have yielded some estimates of noise in the system that might be interesting. While the mapping between model and experiment seems reasonable, an estimate of noise in the system due to the low numbers of the molecules involved would be worth exploring.

The authors also present two models which both explain the experimental data: (a, in Figure 2) A simpler one, where the concentration of AC8 serves as a (global) switch between out-of-phase and in-phase calcium and cAMP oscillations and (b, in Figure 4) a more complex one that predicts localized cAMP oscillations in the specific AKAP79/150 clusters which are out-of-phase with the (global) cAMP oscillations in the cytosol. All modelling is restricted to simulations, if the statement made in the supplementary information (subsection “Model development”) is to be interpreted correctly. This is a significant limitation for the entire manuscript, as all conclusions are (at least partially) based on choices for parameters that the authors made instead of parameters values that were derived from fitting the model to experimental data which would be much more stringent.

Ideally, the authors should fit their two models to a large, representative dataset and use Akaike's information criterion to decide which one is the more suited one. I understand that this will likely not be possible due to the high number of free parameters – it is unlikely that a fitting algorithm would find a true global minimum, as the available data probably are not sufficient constrains. However, this in turn means that deciding which model is to be preferred has to be done by testing predictions where the two models differ significantly.

The following two predictions where both models would yield diametrically opposing outcomes:

i) The 3D reaction diffusion model predicts that cAMP oscillations in the AKAP79/150 compartments and cAMP oscillations in the bulk cytosol are out of phase in the same cell (see Figure 4). This can be tested by combining the AKAP79-based FRET sensor with a cytosolic, intensiometric, RFP-based cAMP sensor such as R-FlincA (Ohta et al., 2018). If the authors observe a clear phase shift between these two reporters, it would constitute very strong evidence in support of the 3D reaction-diffusion model. The current datasets only report one type of compartment per cell, yet the striking difference between compartments in the same cell is where the model predictions differ most dramatically.

ii) Localized oscillations depend on the assumption that AC diffusion is (close to) zero. Thus, the authors should measure AC diffusion at the plasma membrane. A key assumption of their model is that at least a fraction of the total protein pool should be completely immobile. Furthermore, this fraction should increase in an AKAP150 overexpression background.

E) Final punchline that these elegant biophysical findings are important for some aspect of physiology is not very compelling. The authors should come with a more surgically-dissected physiological parameter that depends on the phase relationship between Ca and CaM, and at least provide this in their Discussion section.
