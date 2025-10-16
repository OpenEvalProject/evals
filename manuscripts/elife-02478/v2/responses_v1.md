# Author response - Round 1

Authors:
- Julia Mallmann
- David Heckmann
- Andrea Bräutigam
- Martin J Lercher
- Andreas PM Weber
- Peter Westhoff
- Udo Gowik

## Response text

DOI: [10.7554/eLife.02478.021](https://doi.org/10.7554/eLife.02478.021)

1) How could the selected 11 fluxes be fixed from the mechanistic model? The cited mechanistic models (von Caemmerer, 2000; Heckmann et al., 2013) aim at predicting CO2 assimilation rate given a set of parameter values (e.g., Michaelis-Menten constants) as well as input values for partial pressure of CO2 and O2. The cited mechanistic model does not include the plasmodesmatal flux of glycine and serine or the decarboxylation of the GDC. Moreover, the CO2 uptake rate is assumed (not predicted by the model). These points need to be further elaborated on.

We apologize for not explaining these points in more detail. The mentioned fluxes are indeed not described explicitly, but are described by the model implicitly. We expanded the Method section to show how these were included. The net CO2 uptake rate is predicted by the mechanistic model and can be readily used as a constraint in the flux-balance analysis.

2) You state that you maximized biomass production rate. However, you do not comment on why fixed constraints on production of starch and fatty acids were removed; this should be supported by literature or clear reasons should be provided. The remaining model modifications seem plausible.

The original C4GEM model does not contain starch and fatty acid production as part of the biomass function. Instead, the fluxes are fixed by constraints. Since we are not aware of data that explains how these fluxes scale with CO2 assimilation rate, we removed the respective constraints from the model. This rationale is now described in more detail in the Methods section.

3) The second objective applied is the minimization of the sum of absolute fluxes including transport processes (at fixed optimal biomass production rate). In doing so, higher weight was assigned to plasmodesmatal fluxes (expecting that they receive lower flux). However, as shown in the Methods section, the weight for the plasmodesmatal fluxes is seemingly arbitrarily chosen to be 1.1. What effect would the increase of this value to, say, 2 or 5 have on the drawn conclusions from this study? Either clear reasoning for selection of the value 1.1 should be provided (the mentioned trade-off does justify the selection of the value) or additional tests should be carried out to explore the consequences of other (biologically reasonable) weights for these reactions.

Although the trade-off between metabolite transport and CO2 containment suggests additional weight on plasmodesmatal fluxes, we have to admit that an exact value cannot be inferred from available data. To account for this issue, we conducted a sensitivity analysis against the weight on plasmodesmatal flux. The results presented in Figure 4 are generally stable against variation in weights. Interestingly, the shuttles αKG/Glu and the Mal/Asp shuttle are extended to use nitrogen rich compounds (Gln and Asn respectively) when very high weights are applied. We included these findings in the Results section. The resulting flux over plasmodesmata including flux variability (see point 4) can be found as part of the Supplementary Material.

4) You state that this framework allows the prediction of detailed flux distributions that are biologically realistic. In the Methods section, you also indicate that the combination of several objectives was used to reduce the size of the space of optimal solutions. However, you do not provide a statement on whether or not the resulting distributions are indeed unique (e.g., the one provided in Figure 4A). If the distribution for a fixed biomass production and a fixed sum of absolute flux values is not unique, the provided findings and interpretation are just one of many available alternatives! This point should be carefully examined (e.g., by Flux variability analysis); this analysis must be coupled with the issues raised in point 3, above.

Our rationale behind assuming a small solution space was the application of the two optimality criteria; but we agree with you entirely that this should be shown more rigorously. We thus implemented a flux variability analysis and added the results to the fluxes shown in Figure 4 and 5. The analysis shows that the space of optimal solutions is small and only minuscule variability in the fluxes of the shuttles is possible. The algorithm is described in the Methods and the Results section of the main text.

5) The alternative solutions with a larger number of reactions are presented without providing how much they differ in terms of the total absolute values of flux from that of the preferred glutamate/2-oxoglutarate solution. The increase in the total absolute plasmodesmatal flux, evident in Figure 4 A–D, should be discussed with respect to biological implications.

The sum of absolute flux over plasmodesmata was added to the legend of Figure 4 and 5.

6) The statement “In terms of biomass production rate, this shuttle represents another alternative optimal solution” in the Results section, is confusing and may be misleading. Is this an alternative solution for the same total absolute values of flux as the glutamate/2-oxoglutarate solution? If not, this sentence can be dropped since it was already indicated that alternatives were selected to “retain the same biomass output”.

We agree with you that this point does not need further emphasis and removed the sentence.

7) In the Results section, what do you mean by “In a restrictive scenario, all nitrogen containing compounds were excluded, except for glycine and serene”? What does that do to the reactions that use these metabolites? Are they also removed?

We apologize for not stating that we exclusively excluded plasmodesmatal nitrogen compounds and changed the sentence to make this point clear to the reader.

8) The prediction of the model discussed in the Results section should be investigated with respect to the issues raised in points 3 – 5, above.

We now mention the alternative solution of the flux distribution shown in Figure 5 and the trade-off between metabolite diffusion and gas containment in the Results section.

[Editors' note: further clarifications were requested prior to acceptance, as described below.]

1) Please, indicate the value for the latter parameter (i.e., the fraction of photorespiratory CO2 in the bundle sheath derived from mesophyll oxygenations).

We indicate the fraction of photorespiratory CO2 in the bundle sheath derived from mesophyll oxygenation (0.98 – the derivation from transcriptome data is given in Heckmann et al., 2013) now in the Methods section of the manuscript.

2) To thoroughly examine the viability of the modeling strategy, it is also necessary to determine the variability of model predictions without specifying tight lower (and upper) boundaries (as several fluxes are specified together with two optimization criteria), which may a priori fix the solution. What is the variability of the solutions with default lower/upper boundaries (say, of 0/1000 (irreversible case)) for the diffusion fluxes?

The rationale behind our modeling approach was to incorporate current mechanistic knowledge about C2 photosynthesis in Flaveria in such a way that we can answer the question: Given our current understanding of C2 photosynthesis, what is the implementation of this pathway in the plant leaf that optimizes fitness-relevant criteria?

In our opinion, the most reasonable approach to answering this question was the description of the current conceptual model of C2 photosynthesis (that includes diffusion of glycine and serine) through mechanistic equations and to yield lower bounds for the respective reactions in the stoichiometric model. We understand the reviewers’ question as an equivalent of asking:

Why is it necessary to yield lower bounds for the fluxes of the photorespiratory pump from the mechanistic model? If C2 photosynthesis increases biomass yield, shouldn’t FBA be able to predict such a cycle without the need for further constraints?

As stated in the Methods section of the manuscript Flux Balance Analysis is a powerful tool but it cannot model metabolite concentrations explicitly. Therefore fluxes related to concentration-dependent processes, like carbon concentration mechanisms, cannot be captured by this constraint-based approach. To account for this issue we used values, predicted by the mechanistic model of C3-C4 photosynthesis, for constraining certain fluxes within the FBA model to integrate C2 photosynthesis by creating flux through this pathway. The mechanistic model explicitly accounts for concentrations of CO2 and O2 in the two cell types and predicts the rates of rubisco carboxylation and oxygenation that result from these concentrations. The fluxes mentioned by the reviewer: diffusion of glycine, serine and the GDC reaction belong to these fluxes that have to be constrained to ensure flux through the C2 cycle. When we remove these constraints the model will not predict C2 photosynthetic activity anymore.

We checked this and indeed fluxes through the C2 photosynthetic cycle, but also the predicted fluxes to recirculate ammonia from bundle sheath to mesophyll cells, disappear when we remove constraints on the plasmodesmatal diffusion of glycine, serine, and CO2 and the GDC reaction. We added a sentence to the Methods section to clarify this point.
