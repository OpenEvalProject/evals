# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02478.020](https://doi.org/10.7554/eLife.02478.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “The role of photorespiration during the evolution of C4photosynthesis in the genus Flaveria” for consideration at eLife. Your article has been favorably evaluated by a Senior editor (Detlef Weigel) and 3 reviewers, one of whom, Chris Pires, has agreed to reveal his identity.

The Senior editor and the reviewers discussed their comments before we reached this decision, and the Senior editor has assembled the following comments to help you prepare a revised submission.

This is a genuinely exciting and provocative study; if the results hold up, they are extremely important for the field, and represent a major advance in our understanding of C4 evolution.

The hypothesis tested is that the C2 photosynthesis pump is an evolutionary precursor in the shift from C3 to C4 photosynthesis (which has happened multiple times). Across nine Flaveria species that includes C3, C4 and intermediate species taxa with intermediate C3 and C4 photosynthesis, transcriptome and protein data were collected and analyzed in a phylogenetic context. A global genome-wide metabolic model and flux balance analysis (FBA) was used to integrate models with transcript abundance. The coordinated changes in expression of all main photorespiratory enzymes strongly suggest an evolutionary scenario for the origin of C4 photosynthesis. Very little attention has been paid in the past to nitrogen effects of C2, yet the problem is obvious, and if the C4 cycle is the most direct way to rebalance N within the leaf tissue, then this route provides an immediate solution to a very important and poorly understood transition in the trajectory. It implies that C2 crosses a new threshold of C4 accessibility, and that C4 is all but an inevitable outcome. This also can partially explain the relative rarity of known C2 phenotypes – this may be a part of phenotypic space with a low 'persistence time' – an area that lineages rarely evolve into and very quickly evolve out of.

Key to your argument is whether or not the 're-tooling' of the C4GEM model to accommodate a C2 system was done properly. I'd suggest getting an additional reviewer with expertise in metabolic modeling for that. The analysis done is fairly standard, but relies on several assumptions and choices that do not seem to be justified in the present version of the manuscript. In addition, robustness checks, particularly with respect to the uniqueness of the solutions, need to be obtained, analyzed, and subsequently interpreted.

Details:

1) How could the selected 11 fluxes be fixed from the mechanistic model? The cited mechanistic models (von Caemmerer, 2000; Heckmann et al., 2013) aim at predicting CO2 assimilation rate given a set of parameter values (e.g., Michaelis-Menten constants) as well as input values for partial pressure of CO2 and O2. The cited mechanistic model does not include the plasmodesmatal flux of glycine and serine or the decarboxylation of the GDC. Moreover, the CO2 uptake rate is assumed (not predicted by the model). These points need to be further elaborated on.

2) You state that you maximized biomass production rate. However, you do not comment on why fixed constraints on production of starch and fatty acids were removed; this should be supported by literature or clear reasons should be provided. The remaining model modifications seem plausible.

3) The second objective applied is the minimization of the sum of absolute fluxes including transport processes (at fixed optimal biomass production rate). In doing so, higher weight was assigned to plasmodesmatal fluxes (expecting that they receive lower flux). However, as shown in the Methods section, the weight for the plasmodesmatal fluxes is seemingly arbitrarily chosen to be 1.1. What effect would the increase of this value to, say, 2 or 5 have on the drawn conclusions from this study? Either clear reasoning for selection of the value 1.1 should be provided (the mentioned trade-off does justify the selection of the value) or additional tests should be carried out to explore the consequences of other (biologically reasonable) weights for these reactions.

4) You state that this framework allows the prediction of detailed flux distributions that are biologically realistic. In the Methods section, you also indicate that the combination of several objectives was used to reduce the size of the space of optimal solutions. However, you do not provide a statement on whether or not the resulting distributions are indeed unique (e.g., the one provided in Figure 4A). If the distribution for a fixed biomass production and a fixed sum of absolute flux values is not unique, the provided findings and interpretation are just one of many available alternatives! This point should be carefully examined (e.g., by Flux variability analysis); this analysis must be coupled with the issues raised in point 3, above.

5) The alternative solutions with a larger number of reactions are presented without providing how much they differ in terms of the total absolute values of flux from that of the preferred glutamate/2-oxoglutarate solution. The increase in the total absolute plasmodesmatal flux, evident in Figure 4 A–D, should be discussed with respect to biological implications.

6) The statement “In terms of biomass production rate, this shuttle represents another alternative optimal solution” in the Results section, is confusing and may be misleading. Is this an alternative solution for the same total absolute values of flux as the glutamate/2-oxoglutarate solution? If not, this sentence can be dropped since it was already indicated that alternatives were selected to “retain the same biomass output”.

7) In the Results section, what do you mean by “In a restrictive scenario, all nitrogen containing compounds were excluded, except for glycine and serene”? What does that do to the reactions that use these metabolites? Are they also removed?

8) The prediction of the model discussed in the Results section should be investigated with respect to the issues raised in points 3 – 5, above.

[Editors' note: further clarifications were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “The role of photorespiration during the evolution of C4 photosynthesis in the genus Flaveria” for further consideration at eLife. Your revised article has been favorably evaluated by Detlef Weigel (Senior editor) and a member of the Board of Reviewing Editors. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have carefully considered the suggestions provided about the earlier version of the manuscript and have: (1) offered detailed explanations of how the results of the mechanistic model were used to constrain the larger stoichiometric model as well as (2) conducted flux variability analysis for the different alternative scenarios to support the robustness of the predictions.

The only remaining concern deals with the details on lower/upper boundary selection for the diffusion fluxes and their effects on the predictions. Additional clarifications (and/or analyses) may further strengthen the predictions: The lower bounds on the diffusion of gylcine, serine, and NADPME reaction are fixed based on oxygenation rate and the fraction of photorespiratory CO2 in the bundle sheath derived from mesophyll oxygenations.

1) Please, indicate the value for the latter parameter (i.e., the fraction of photorespiratory CO2 in the bundle sheath derived from mesophyll oxygenations).

2) To thoroughly examine the viability of the modeling strategy, it is also necessary to determine the variability of model predictions without specifying tight lower (and upper) boundaries (as several fluxes are specified together with two optimization criteria), which may a priori fix the solution. What is the variability of the solutions with default lower/upper boundaries (say, of 0/1000 (irreversible case)) for the diffusion fluxes?

This additional analysis can be readily conducted and included in the manuscript.
