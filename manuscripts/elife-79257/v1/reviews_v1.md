# Peer review - Round 1

Editors:
- Thomas Gregor, https://ror.org/00hx57361 Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79257.sa0](https://doi.org/10.7554/eLife.79257.sa0)

The manuscript introduces a compelling theoretical framework to investigate architectures of signal processing. The predictions of the computational model have been convincingly validated with data from fly wing precursor tissues. The work is important and will be highly valuable to biological physicists and developmental biologists interested in morphogenesis and pattern formation.


---

# Peer review - Round 1

Editors:
- Thomas Gregor, https://ror.org/00hx57361 Princeton University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79257.sa1](https://doi.org/10.7554/eLife.79257.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cellular compartmentalisation and receptor promiscuity as a strategy for accurate and robust inference of position during morphogenesis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Marcin Zagorski (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers and reviewing editor agreed that no additional data is needed to support the major conclusions. Therefore a revision focused on improving clarity and presentation will be sufficient. The following two major concerns should be addressed; additional detailed comments and suggestions in the reviews below should be considered for clarity and overall readability.

1) One important point to clarify is whether the presented solutions (parameters identified) are representative of a larger class of sub-optimal or optimal solutions. This can be checked by perturbing the solutions. Presumably, the authors have investigated this point already as in the SM there are parts about, robustness, sensitivity and trade-offs, so improving presentation in the main part should solve that. This will also shed more light on the generality of the obtained results.

2) The important question to address is whether the choice of Eq. 5, which describes how the cell evaluates its position, influences other results in the manuscript.

Reviewer #1 (Recommendations for the authors):

– Extrinsic noise coming from the stochastic ligand production at the source is included in the model by letting cells along the direction parallel to the source boundary experience a spatially-fluctuating level of ligand, with statistics given in (1). From what we understand, this noise is quenched in space. Is it clear to what extent this is equivalent to the more realistic annealed disorder originating from Brownian motion and stochastic source production?

– In some cases, non-specific receptors (e.g. Dlp, Hanandal, Development, 2005) have been shown to increase in expression levels away from the morphogen source. Can the authors comment on this observation in light of their model?

– In appendix L, the local inference error for a (optimised) graded receptor expression is compared to that of a uniform receptor expression pattern. We find that the way this result is presented slightly misleading since the expression level in the uniform case is not optimised; the two setups should be compared after optimisation.

Reviewer #2 (Recommendations for the authors):

– In my opinion, Figure 2 is misleading and is disrupting the flow of the manuscript. Almost the same information is conveyed in Figure 4 and Figure 5. Further Figure 2 suggests some very regular arrangement of the nodes (regular topology of signalling architecture), which is not the case. Presenting a model with tiers and branches, or some different network-like schematic to indicate reaction and flux imbalances could improve presentation.

– In lines 85-87, different timescales of signalling processing are mentioned corresponding to branches (fast) and tiers (slow), but this aspect of regulation seems to be not discussed in the later parts of the paper. It might be worth drawing this analogy again when discussing how noise is integrated by different architectures. Possibly, there is the separation of the timescales or signalling integration takes place on the same timescales.

– Line 98, Figure 5 is mentioned just after Figure 2 (line 91). Please amend the ordering or rephrase so figures are referenced in the text as they appear in the paper.

– Line 114, I would avoid statements "of course any choice consistent with experimental observations would do". For instance, would the model work for stationary wave-like patterns of morphogens that could emerge via Turing mechanism (Green and Sharpe, Development 2015)? Basically, I would rephrase providing a description of acceptable ligand profiles (e.g. monotonically decreasing).

– The optimization procedure employed is computationally quite-consuming as the intrinsic noise is calculated by solving a chemical master equation. Can the model be solved without directly solving CME? What are the differences? If the differences with and without CME are small this might help to have faster optimization and hence more explicitly explore the space of available signalling architectures that result in optimal or close to the optimal solution.

– The intrinsic and extrinsic noises are varied separately as far as I understand. Are there any arguments/heuristics that would indicate the resulting global solutions would be the same if two types of noise would be varied simultaneously?

– In appendix C, the screening is described for the model parameters, but it is still slightly obscure what process was carried out.

– In table 2, in the middle column, we see that the weight of tier 2 is orders of magnitude greater than that for tier 1. In this case, what role does the first tier really play? And does such a strong weighting make sense biologically?

– I don't really understand the need for appendix E, but I might be missing something.

– In Appendix G, Figure 8, we see that adding a third tier does not reduce the minimum average inference error very much at all. Were any simulations done for four-tiered systems? What sort of computational cost does adding one extra tier there?
