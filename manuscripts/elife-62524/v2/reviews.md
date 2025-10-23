# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62524.sa1](https://doi.org/10.7554/eLife.62524.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study combines high resolution imaging experiments with mechanical modeling to elucidate the energetics of flagellar propulsion and understand the role of internal dissipation in this system. The authors conclude that the main origin of dissipation is internal to the flagella, a finding that challenges the conventional view of flagellar dynamics, and should prove to be of interest to a wide range of researchers.

Decision letter after peer review:

Thank you for submitting your article "Flagellar energetics from high-resolution imaging of beating patterns in tethered mouse sperm" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analysis is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This study combines high resolution imaging experiments with mechanical modeling to elucidate the energetics of flagellar propulsion and understand the role of internal dissipation in this system. The experiments use mouse sperm cells that are chemically tethered to a glass slip. For each cell, the flagellum shape is imaged over time and segmented into a mathematical curve. This data is analyzed based on a planar Kirckhoff rod model that includes hydrodynamic drag forces (based on resistive force theory), bending elasticity, and an unknown active moment density. An energy balance is written that also includes internal viscous dissipation generated inside the flagellum, with an ad hoc internal friction coefficient. By calculating the various terms in the energy balance based on the reconstructed filament shapes, the authors are able to estimate the active power density along the flagellum. This calculation leads to two unexpected findings: (1) the authors find that the active power density can be negative along some portions of the flagellum, meaning that along these portions the dynein motors act against the local deformation of the structure, and (2) the main origin of dissipation in the system comes from internal dissipation, which exceeds viscous dissipation in the fluid in magnitude.

Essential revisions:

1. It is not completely clear from the manuscript what the configuration of the sperm is with respect to the glass slide where the head is tethered. What is the orientation of the cells with respect to the slide, and in which plane are the deformations measured? (from above or from the side?) We would expect that different configurations may lead to slightly different waveforms. In particular, we are surprised that the mean shapes shown in figure 2(a) have a net asymmetry which is observed in nearly all the cells: could this have to do with the relative configuration of the flagellum with respect to the surface?

2. The experiments are done with flagella very near a no-slip surface, since the cells are chemically adhered to the chamber boundary. Yet, the authors use resistive force theory for filaments in free space, without any reference to the nearby no-slip surface. As the rate of energy dissipation near the surface will be considerably larger than estimated by RFT, it is possible that some (or much, or perhaps all) of the additional dissipation found by the authors is actually within the fluid and simply not accounted for by RFT. Thus, all of the calculations must be redone with the appropriate Blake tensor for stokeslets near a no-slip wall before the results can be considered definitive. The paper must also more carefully illustrate and quantify the proximity of the flagella to the surface in order to make these calculations precise. Absent this analysis, the claims of the paper do not stand up to scrutiny.

A related point is the need to understand the effect of tethering the cell on its kinematics and energetics? In other words, do the conclusions still hold for freely swimming cells?

3. Is there any evidence of 3D dynamics? Some recent experiments with human sperm have suggested that sperm beats can take place in 3D (Gadelha et al., Science Advances 2020). As the model in the paper is 2D, this could also affect the energy balance.

4. The authors should examine the work of K.E. Machin ["The control and synchronization of flagellar movement"], Proc. Roy. Soc. B 158, 88 (1963), which provided the first theoretical formalism to study active moment generation within beating flagella based on examining the difference between known force contributions from viscous dissipation and elastic bending. It seems that this same kind of analysis could be done here to identify directly the non-viscous contribution, rather than having to postulate a particular form.

Stated another way: Why not try to estimate the active power density directly from the active moment density, which could be calculated from the moment balance of equation (4) where all the other terms are known? This would provide a direct estimate of the active power. The force balance could then be used to estimate the internal friction, which would then no longer rely on an assumed value for the internal friction coefficient. In fact, this could be used to obtain an estimate for that coefficient.

5. The paper addresses in detail the use of Chebyshev fitting methods for the filaments, but does not appear to address the physical boundary conditions one would expect on elastic objects (particularly at the free end), involving the vanishing of moments and forces. Unlike, for example, the biharmonic eigenfunctions of simple elastic filament dynamics which are tailored to those boundary conditions [see, e.g. Goldstein, Powers, Wiggins, PRL 80, 5232 (1998)], it is not clear how the Chebyshev functions satisfy those conditions. Some explanation is needed.

6. If indeed internal dissipation dominates, that would suggest that essentially all prior theoretical approaches to calculating sperm waveforms must be quantitatively in error by very large factors. It would be very appropriate for the authors to examine some of those theoretical works to determine if this is the case.

7. The authors note in the Discussion that the beating waveform changes dramatically in fluid with higher viscosity. Yet, if external dissipation plays such a small role how can this be rationalized?
