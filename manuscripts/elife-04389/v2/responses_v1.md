# Author response - Round 1

Authors:
- Luke H Chao
- Daryl E Klein
- Aaron G Schmidt
- Jennifer M Peña
- Stephen C Harrison

## Response text

DOI: [10.7554/eLife.04389.017](https://doi.org/10.7554/eLife.04389.017)

Generally your work is considered to be novel and of high interest. However, the reviewers agree that the novelty lies primarily in the kinetic model which reveals, for instance, that trimerization is a rate-limiting step, rather than in the experimental approach or the general pathway involving dimer dissociation, trimerization etc. The modeling thus constitutes the key part of the work, and several aspects of it were viewed as rather problematic.

The principal concerns were whether there are too many free parameters in the simulation and whether we could improve the fit with yield for mixed particles of W101A (“dead” fusion-loop mutant). We now point out explicitly that of the five parameters, only three are free, because we have used experimental data on the conformational transition of soluble E to fix the pK of the dimer-monomer step and because we fixed the cooperativity parameter at Pdim=4. We provide details below. We have also found that by introducing a pH dependence for the trimerization step, again fixed by experimental measurement, and by allowing trimers with one “dead” protomer to participate in hemifusion, we considerably improve the agreement of simulated and observed yield. Again, further details below.

1) The simulation model has five fitting parameters (Figure 6). However, could there be other combinations of the parameters that would give similar quality of the fit? Can the combinations be different for different pH? For instance, can lipid mixing be mediated by several trimers at acidic pH and by only one at moderately acidic pH? In the analysis of the mutants four of the five parameters were kept fixed. Can a comparable fit be found by varying kcomp? Also, are the simulations dependent on the grid size, i.e. the spacing of the trimers?

We emphasize that our model in fact has only three free parameters. A well-characterized and biochemically established condition is the pH threshold for dimer dissociation. This value determines the Kdm equilibrium constant in our simulation, thus fixed the ratio of kact to kret. We fixed Pdim (the cooperativity factor for dimer dissociation) at 4, corresponding roughly to a four-fold increase in the dimer to monomer transition rate. Thus, the three values we varied were those of kact, ktri and kcomp. We found that other combinations could not generate as good a fit. The text and figures have been modified to make this clear.

We considered whether models with a different number of trimers required to complete hemifusion could fit our experimental data equally well. We compared the results of simulations in which we varied the number of trimers defining hemifusion (Author response image 1). The model with two trimers clearly fit better than models with one or three trimers. This global behavior applies across the pH range studied. Attempts to optimize the fitted parameters with a three-trimer or one-trimer hemifusion model resulted in poor fits of the simulation distributions to the experimental data.Author response image 1.

We also investigated whether we could generate better agreement with the data from mutants by varying kcomp, as suggested, and found that the fits using this model were poorer (as reflected by the χ2 value and plotted residuals), despite adding a second fitting parameter in the kcomp fit (Author response image 2).Author response image 2.

Grid spacing was not a consideration for describing flavivirus fusion, as unlike influenza hemagglutinin, there is a regular icosahedral arrangement of E on the virion surface. We did note potential differences due to grid area (total number of E proteins in the contact zone) as observed in simulations (Figure 6C).

2) A related problem is that relevant experimental data are not well explained by the fit, such as why VLPs with 1-to-1 mix of wild-type E protein and W101A E protein had a mean dwell time and an overall yield of fusion events similar to those of fully wild-type particles. The yield of hemifused particles depends on pH in simulations much stronger than in the experiment (Figure 7B).

The difference between our experimental observations and the simulation results for the mixed particles prompted us to consider whether a trimer containing two wild-type fusion loops might still be competent to mediate hemifusion. We generated another version of our simulation scheme to account for this possibility and found an overall event yield similar to wild type values, better matching our experimental observations (Updated Figure 7D). The figures in the main text have been updated to reflect the new simulation.

We had considered that pH might influence different stages of the reaction, and in the originally submitted version of the work, we chose to build in a pH-dependence for the initial dimer dissociation step. To determine whether additional steps might depend on pH, without adding further free parameters, we measured the trimerization pH threshold for soluble WNV E protein in a liposome co-floatation assay and obtained a value of 6.1. Because WNV E is monomeric in solution, the measurement deconvolves dimer dissociation from trimerization. We built this parameter into our simulation, just as we had incorporated pH dependence with a measured pK into the dimer dissociation step and found better correlation between our simulation and the experimental yield at higher pH values (updated Figure 7B).

3) Previous studies on several fusion processes suggested that there are higher energy barriers to overcome on the way from hemifusion to an expanding fusion pore than on the way from the tight contact to hemifusion. Should the conclusion “… makes trimerization a bottleneck in the overall course of the fusion reaction” be edited to “a bottleneck in hemifusion”?

We agree, and we have changed the wording as suggested.

[Editors’ note: further revisions were requested prior to acceptance, as described below.]

The reviewers’ principal concern was with the assumption that the pH threshold for bulk fusion is a suitable estimate for the pK of the dimer-monomer step on the virion surface. The point is a good one, and we realized that we could fix the parameter for Kdm (the pH-dependent dimer-monomer equilibrium) by measuring the dimer-monomer equilibrium step directly by dynamic light scattering of Kunjin virions. We have done so and incorporated this experimental value as a fixed parameter in the simulations. We now describe this measurement in the paper.

If the pK of the dimer-monomer step is indeed directly measured, please describe these measurements in the paper.

We used Kunjin virus, the West Nile virus variant; its uniform diameter allows us to interpret a change in dynamic light scattering as a change in effective hydrodynamic radius. We observe a reversible expansion upon low-pH treatment (new Figure 5A). West Nile virions have been shown to undergo transient temperature dependent fluctuations, during which extension of the E protein opens access to otherwise sequestered epitopes (Dowd et al., 2011). A similar transition seen with dengue virions is temperature dependent and can be trapped by binding of antibody to the epitopes it exposes (Zhang et al., 2013b; Zhang et al., 2014). The measured radius is somewhat larger than the fully compact structure seen by cryoEM, suggesting that E subunits can undergo transient, reversible outward excursion even at pH ∼8 and room temperature (see main text for further discussion).

We find that pH 6.8 is the midpoint of the transition from a smaller to a larger radius (new Figure 5B). We interpret the change in hydrodynamic radius as a measure of the rearrangement of E subunits from the circumferential orientation of their long axis seen in mature virions to a partially extended conformation with fusion loops exposed. We take the midpoint pH for this transition as the pK of the dimer-monomer equilibrium for E protein on the virion surface (Figure 5B). We have re-run all of the simulations in the paper with the newly determined Kdm value and updated all of the relevant figures (Figures 6C, 7B-D, 8C and F).

This transition shows a Hill coefficient of ∼3, indicating local cooperativity for the transition, but not a globally cooperative reorganization of the entire surface lattice.

For one of the two fixed parameters –Pdim, the authors now tested a range of values and found the data still fit best to models with two trimers mediating hemifusion. This is an important analysis and it would be useful to specify the tested range.

We tested the Pdim parameter over a range from 2 to 50, as now included in the updated main text. In addition, based on the observed Hill coefficient of 2.5, we investigated if accounting for additional cooperativity effects on other adjacent subunits outside of a dimeric unit would alter our simulations. Incorporation of an additional factor did not make any changes in the properties of the simulation histograms and their fits. This result suggests that we can use a single Pdim factor to introduce cooperativity into the model, and that this factor is an adequate surrogate for the cooperative dimer to monomer transition on the surface of the virion.

(…) Thus, pK of the dimer dissociation step can differ from pH threshold of lipid mixing, and it is important to examine whether small changes in the pK for Kdm would yield better fits with 1 or 3 trimers mediating hemifusion or 2 trimers would remain the best fit.

We once more examined whether our simulation, with the pK value of 6.8 determined by dynamic light scattering, alters the agreement of models with 1 or 3 trimers mediating hemifusion and found that a model with two trimers remains the best fit (Author response image 3).Author response image 3.
