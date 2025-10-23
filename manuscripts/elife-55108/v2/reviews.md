# Peer review - Round 1

Editors:
- Ariel M Pani, University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55108.sa1](https://doi.org/10.7554/eLife.55108.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How secreted signaling proteins disperse to form gradients in living animals is a fundamental question for developmental and cell biology. Mii et al., use quantitative light microscopy to analyze dispersal dynamics of a tagged Wnt and FrzB in Xenopus embryos. The authors provide evidence that the spatial distribution of binding sites and dynamic exchange of bound and freely diffusing proteins facilitate rapid formation of long-range protein gradients and that a similar mechanism could apply to other pathways as well.

Decision letter after peer review:

Thank you for submitting your article "Quantitative analyses reveal extracellular dynamics of Wnt ligands in Xenopus embryos" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is 'in revision at eLife'. Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this manuscript, Mii et al., use quantitative light microscopy to analyze dispersal dynamics of a tagged Wnt and FrzB in Xenopus embryos. Using protein trapping approaches, they demonstrate that Venus-tagged Wnt8 and FrzB can spread across many cell diameters in vivo and that high levels of secreted protein can be captured at a distance from their sources. Importantly, Mii et al., showed using FCS that only a small fraction of the detectable protein was freely diffusing at a given time while the majority was not. Mathematical models of Wnt8 and FrzB dispersal based on experimentally derived parameters including exchange between the free and bound populations were also able to recapitulate a gradient profile for bound extracellular proteins. The authors propose that the spatial distribution of ligand binding sites and on-off dynamics facilitate formation of long-range Wnt protein gradients, and that a similar mechanism could apply to other pathways.

How signaling proteins disperse in living animals is a fundamental question, and a variety of mechanisms are likely to operate in different contexts. This manuscript presents a series of targeted experiments that provide an important step forward for the field. However, there are key issues that need to be addressed to give confidence in the biological relevance of the results and the mathematical techniques.

Essential revisions:

Comments from the three reviewers have been condensed into a single list to help with revisions. Successfully addressing the reviewers' essential revision points 1-3 will require additional laboratory experiments, while the others likely will not. Successfully addressing the reviewers' points 11-14 would normally require new experiments, but based on current eLife guidelines due to COVID-19, I think that these could instead be adequately addressed in the manuscript text if the additional experiments are not practical at this point.

1. All three reviewers had similar reservations regarding the use of overexpression for quantitative analyses. Most importantly, this paper relies entirely on overexpressed Wnt ligand. As the proposed mechanisms controlling Wnt diffusion involve binding to extracellular factors, altering the stoichiometry of Wnt ligands and binding sites may affect the normal balance between the different pools of Wnt. This would be especially problematic if overexpression saturates endogenous mechanisms that limit Wnt diffusion within the areas used for measurements. Similar concerns also apply to the FrzB measurements. To ensure confidence in the physiological relevance of the data, the authors should perform the key experiments over a range of lower mRNA dosages down to the minimum required for FCS to test if the measured parameters (diffusion constants, fraction of molecules in each pool) are the same. If the results differ, would it be possible to extrapolate to a case of zero overexpression?

2. The authors should attempt to estimate how the levels of the tagged proteins compare to the endogenous ones. For Wnt8, this could potentially be done by comparing immunofluorescence levels for the endogenous and the tagged Wnt8.

3. Functionality of tagged proteins.

a. Please provide additional data to demonstrate that the tagged proteins used here are fully functional. This revision is considered critical due to the level of precision in the analyses. Showing only that Wnt or FrzB fusion proteins can induce a phenotype when overexpressed would not be sufficient. The authors could use TOP-FLASH assays like in Figure 4 Supplement 1 over a range of lower concentrations to confirm that the responses at low mRNA levels are the same for tagged and untagged Wnt8 and FrzB.

b. Based on Figure 4, supplement 1, the mKikGR-FrzB fusion protein is not fully functional and should be removed.

4. Some of the details of the proposed mechanism are confusing. The paper seems to measure both slow and fast diffusing components from the FCS measurements and also to propose an immobile fraction that cannot be measured in FCS. Or do the authors believe that the slow component in FCS can be equated with the immobile one? If the former, do the authors really need three different pools of ligand to explain the data? On the other hand, the model only has two components a fast diffusing one and an immobile fraction – would the results be affected by adding a slow diffusing component as measured in FCS? or alternatively treating the immobile fraction as slowly diffusing?

5. In light of (4), the authors should consider whether simpler models fit their data equally well. For example, the effective diffusion model in Figure 4 supplement 3 that has fewer parameters appears to fit the Frzb data better than the two population model in the main text. For Wnt, it isn't clear whether goodness of fit is improved by adding a second component as more parameters are also added.

6. Can the authors speculate about why the sec-mv has a slow diffusing component? This seems surprising. Again, the authors should justify using a two-population (slow and fast) rather than a simpler model.

7. There may be an error in the FDAP equation in figure 4. The data appear to be normalized so that f(0) = 1, however, plugging 0 into the equation does not give 1. More likely, the authors intend to fit to the function f(t) = (1-c)*exp(-koff*t)+c which has the correct limiting behavior at both t = 0 and t = inf. This shows however that there are only two parameters to be fit (this makes sense, they correspond to the decay rate and the immobile fraction) so it is unclear how the authors are fitting three parameters from their data. Essentially, one cannot extract kon from this data – it is lumped into the prefactor of the exponential.

8. Modeling

a. The argument in lines 402-411 is not valid, as can be seen with numerical simulations, in which a molecule with D=0.05 um^2/s does reach the end of a 200 μm long patterning field over 24 h and can be readily absorbed by a localized sink there.

b. In fact, the models (effective diffusion or binding/dissociation) are not mutually exclusive (as described in the Crank reference mentioned by the authors). It would therefore be useful for the readers if the authors could present a unified description of restricted, effective and hindered diffusion.

c. Since the proteins are detected over distances of ~15 cell diameters (~200 um), the spatial range of the simulations should be increased to the length of a Xenopus embryo to avoid reflection from the boundary. It would also be ideal if the authors could measure the gradient throughout the embryo with FCS (similar to PMID 19741606) or note their limitations.

d. Please normalize each curve to the maximum of each species to see if there really is a difference in the ranges of the free and bound components in the model.

e. The authors state that "Notably, in our mathematical model, distributions of both free and bound components converged to steady states within a few minutes, showing rather fast dynamics in the context of embryonic patterning". The cause for these unexpectedly fast dynamics might be the extremely high off-rates compared to previously measured values (e.g. compare to the values used in PMID 22445299). Depending on re-assessment of the FDAP data, the authors should repeat their simulations. It would be ideal to more directly compare the simulations to the experimental data (e.g. overlay data from Figure 2D with simulations) and to compare the fast kinetics prediction of the model to the temporal gradient evolution in real embryos.

f. Please simulate the outcome of FDAP experiments (i.e. the dissipation of concentration from one peak). Is an increase in neighboring regions detected, and how does this compare with the experimental findings?

g. Please simulate the Sec-mV findings. Maybe the simulations will clarify why this protein is not visible?

h. Please clarify why the data in Figure 5F looks different from panel B, even though it should be the same according to the figure legend.

9. FCS analyses and inference of bound/unbound fractions

a. The authors state that "[…] diffusion coefficients measured with FRAP and FCS differ by 3-4 orders of magnitude (Rogers and Schier, 2011)", but this statement is outdated and should be corrected (see e.g. PMIDs 23533171 and 28919007).

b. Figure 3B shows problematic drift that might underlie the long correlation times.

c. The authors further state that "By autocorrelation analysis, FCS can measure the diffusion coefficient (D) and the number of particles, which is equivalent to the concentration of the diffusing molecules (Figure 3E), but it cannot measure immobile molecules (Hess et al., 2002)", but this statement (and similar ones in lines 220-221 and 237-238) is imprecise and needs to be corrected. Avalanche photodiodes or the like used in FCS experiments do detect all signal emitted from fluorescent molecules, but the inference of diffusion coefficients depends on mobile molecules.

d. These imprecisions in FCS theory lead to unsuitable analyses in Figure 3G. Importantly, not only the inferred number of particles but also the count rate is higher for Sec-mV, although the same mRNA amount was used for all constructs. The difference in the outcomes between confocal imaging and FCS might instead be the result of variability between experiments. The authors should therefore measure and compare the intensities using photon counting and FCS within the same embryos if possible or note their limitations.

e. The subsequent considerations about immobile and diffusing molecules (e.g. lines 230-233) are inappropriate and should be corrected. The current logic is: 9.4 detected mV-Wnt8 particles constitute 43% of the 21.7 particles detected for sec-mV, and since 43% of the 19.5 maximally detectable mobile mean photon counts equal 8.4 mean photon counts, the rest of the mean photon counts (219.7) for mV-Wnt8 is immobile; however, this logic is inappropriate since identical amounts of mRNA are not equimolar given the protein size differences, identical mRNA amounts do not necessarily give rise to similar protein amounts due to differences in translation or stability, and day-to-day or instrument differences might influence the intensities.

f. Please use the Akaike information criterion or the like to compare the 2-component fits with more parsimonious 1-component fits of the FCS data, especially given the small differences in the highly and poorly mobile fractions.

g. Please mention from how many independent embryos the FCS measurements were derived.

10. In Figure 3 supplement 1, the comparison is not appropriate given the very different sample numbers and the small effect size. The authors should instead use bootstrapping approaches with similar sample numbers.

11. For the FDAP experiments, the instruments may just not have the sensitivity to detect small numbers of photoconverted molecules that spread locally, especially considering that a large amount of fluorescence loss is due to photobleaching and that the imaging is at a single plane. The authors should take care with interpreting these data unless they are able to repeat the experiments using new acquisition parameters to minimize bleaching. Additionally, as the authors noted that the pseudo-equilibrium binding constant may be underestimated because curve fitting does not consider photobleaching, and the simulations crucially depend on these parameters, they should execute new simulations with the parameters determined in the absence of photobleaching if possible. If repeating these experiments is not practical due to current restrictions the authors should temper their conclusions.

12. A goal of this manuscript is to link quantitative measurements of local protein dynamics to larger spatiotemporal patterns of extracellular protein dispersal in embryos. To do so, the authors assume that short-term measurements at sub-apical junctions fully capture the processes that are important for protein dispersal and gradient formation. The hypothesis is that local dynamics measured by FCS and FDAP in a particular location can be extrapolated to model mechanisms for long distance dispersal across fields of many cells, but this has not been shown experimentally. The authors could use FRAP experiments photobleaching a large area at a distance from the Wnt source followed by time-lapse imaging over a long period to confirm that the pattern and timing of fluorescence recovery across many cells is consistent with predictions from their model. Under normal circumstances, these experiments would be considered required revisions. However, in light of the current research situation it would be acceptable to instead discuss these limitations in the manuscript.

13. The manuscript seems to treat Wnt8 and FrzB dispersal as occurring within a single plane, with the dynamics at sub-apical junctions reflecting dynamics elsewhere. However, the tagged proteins could be spreading along the basal surfaces or through entirely different routes or mechanisms. These possibilities should be considered in the discussion if it is not feasible to assess them experimentally.

14. Similarly to (12), a key assumption is that the freely diffusing population of Wnt detectable by FCS is the protein population that moves between cells, but this cannot be directly concluded from the experiments. The authors should discuss the possibility of Wnt transport on cytonemes/signaling filopodia or contacts between cells at earlier developmental stages. Based on the Xenopus fate map, can the authors rule out potential mechanisms for Wnt gradient formation based on cell lineages or migration patterns? The morphotrap experiments argue against these possibilities, but the fact that tagged protein can accumulate to high levels in distant trap-expressing cells could be explained by higher stability of trapped versus untrapped protein.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Quantitative analyses reveal extracellular dynamics of Wnt ligands in Xenopus embryos" for consideration by eLife. Your revised article has been evaluated by a Reviewing Editor, one Reviewer, and Naama Barkai as the Senior Editor.

The Reviewing Editor has drafted this to help you prepare a revised submission.

The authors have satisfactorily addressed the reviewers' combined points, and the additional experiments have substantially strengthened the conclusions. I am pleased to recommend accepting this paper for publication pending minor revisions. There are only three points to address prior to full acceptance.

Summary:

How secreted signaling proteins disperse to form gradients in living animals is a fundamental question for developmental and cell biology. Mii et al., use quantitative light microscopy to analyze dispersal dynamics of a tagged Wnt and FrzB in Xenopus embryos. The authors provide evidence that the spatial distribution of binding sites and dynamic exchange of bound and freely diffusing proteins facilitate rapid formation of long-range protein gradients and that a similar mechanism could apply to other pathways as well.

Essential Revisions:

1. The authors state "We provide the source code for our mathematical model, written in C.", but we could not find the code among the current manuscript items. Please provide this code as a Supplementary file.

2. The diffusion coefficients for 250 pg and 20 pg of mV-Wnt8 appear to differ between Figure 3D and Figure 3—figure supplement 1B, and the authors should check whether the correct data are plotted.

3. The figure legend for Figure 4 includes a panel F, but this image is missing from the figure. Please provide an updated Figure 4 including F or remove it from the legend.

4. The authors may wish to note in the text that reduced activity of mV-tagged Wnt8 compared to untagged Wnt8 could possibly be due, at least in part, to differences in translation.
